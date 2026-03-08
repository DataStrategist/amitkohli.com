"""
sync_from_vault.py — Sync talks, videos, and ontology from Obsidian vault to Hugo content.

Usage:
    python scripts/sync_from_vault.py --vault-path C:\\boom [--dry-run]
"""

import argparse
import csv
import json
import os
import re
import shutil
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def strip_wikilinks(text: str) -> str:
    """Remove [[ ]] wrappers from Obsidian wiki-links."""
    if not isinstance(text, str):
        return text
    return re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)


def slugify(text: str) -> str:
    """Create a URL-safe slug from text."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown content. Returns (metadata, body)."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)", content, re.DOTALL)
    if not match:
        return {}, content
    try:
        meta = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, match.group(2)


def write_hugo_page(output_dir: Path, frontmatter: dict, body: str, dry_run: bool):
    """Write a Hugo page bundle (index.md) with YAML frontmatter."""
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / "index.md"

    lines = ["---"]
    lines.append(yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True, sort_keys=False).rstrip())
    lines.append("---")
    if body.strip():
        lines.append("")
        lines.append(body.strip())
    lines.append("")

    text = "\n".join(lines)
    action = "DRY-RUN" if dry_run else "WRITE"
    print(f"  [{action}] {path}")
    if not dry_run:
        path.write_text(text, encoding="utf-8")


# ---------------------------------------------------------------------------
# Job 1: Sync Talks
# ---------------------------------------------------------------------------

SKIP_TALK_PATTERNS = [
    r"\(deck\)",
    r"metadata",
    r"^Talks Index",
    r"^talk_template",
    r"^_Talks",
    r"Metadata Audit",
]


def should_skip_talk(filename: str, meta: dict) -> bool:
    """Determine if a talk file should be skipped."""
    for pattern in SKIP_TALK_PATTERNS:
        if re.search(pattern, filename, re.IGNORECASE):
            return True
    raw_type = strip_wikilinks(str(meta.get("type", "")))
    if raw_type.lower() in ("deck", "index"):
        return True
    return False


def parse_topics(raw) -> list[str]:
    """Parse topic field into a list of clean strings."""
    if not raw:
        return []
    if isinstance(raw, list):
        return [strip_wikilinks(str(t)).strip() for t in raw if t]
    text = strip_wikilinks(str(raw))
    return [t.strip() for t in text.split(",") if t.strip()]


def sync_talks(vault_path: Path, content_dir: Path, dry_run: bool):
    """Sync talks from vault to Hugo content/talks/."""
    talks_src = vault_path / "Stuff" / "Talks"
    talks_dst = content_dir / "talks"

    if not talks_src.exists():
        print(f"  [SKIP] Talks source not found: {talks_src}")
        return

    print(f"\n=== Syncing Talks from {talks_src} ===")

    # Write section _index.md
    section_fm = {
        "title": "Talks",
        "description": "Conference talks, panels, and workshops.",
    }
    if not dry_run:
        talks_dst.mkdir(parents=True, exist_ok=True)
        idx = talks_dst / "_index.md"
        idx.write_text(
            "---\n"
            + yaml.dump(section_fm, default_flow_style=False, allow_unicode=True, sort_keys=False).rstrip()
            + "\n---\n",
            encoding="utf-8",
        )
        print(f"  [WRITE] {idx}")
    else:
        print(f"  [DRY-RUN] {talks_dst / '_index.md'}")

    count = 0
    for md_file in sorted(talks_src.glob("*.md")):
        raw = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)

        if should_skip_talk(md_file.name, meta):
            print(f"  [SKIP] {md_file.name}")
            continue

        # Build title — prefer frontmatter, fall back to filename
        title = meta.get("title") or md_file.stem

        slug = slugify(title)
        if not slug:
            continue

        # Normalize fields
        topics = parse_topics(meta.get("topic"))
        date = meta.get("date")
        if date:
            date = str(date).strip()[:10]
            # Pad partial dates: "2024" -> "2024-01-01", "2024-06" -> "2024-06-01"
            if re.match(r"^\d{4}$", date):
                date = f"{date}-01-01"
            elif re.match(r"^\d{4}-\d{2}$", date):
                date = f"{date}-01"

        fm = {"title": title}
        if date:
            fm["date"] = date
        if meta.get("event"):
            fm["event"] = strip_wikilinks(str(meta["event"]))
        if meta.get("host org") or meta.get("host_org"):
            fm["host_org"] = strip_wikilinks(str(meta.get("host org") or meta.get("host_org")))
        if meta.get("location"):
            fm["location"] = str(meta["location"])
        if topics:
            fm["topic"] = topics
        if meta.get("audience"):
            fm["audience"] = str(meta["audience"])
        if meta.get("abstract"):
            fm["abstract"] = str(meta["abstract"])
        if meta.get("deck"):
            fm["deck_url"] = str(meta["deck"])
        if meta.get("recording"):
            fm["recording_url"] = str(meta["recording"])
        if meta.get("status"):
            fm["status"] = str(meta["status"])
        fm["featured"] = bool(meta.get("featured", False))
        if meta.get("tags"):
            fm["tags"] = meta["tags"] if isinstance(meta["tags"], list) else [meta["tags"]]

        write_hugo_page(talks_dst / slug, fm, "", dry_run)
        count += 1

    print(f"  Total talks synced: {count}")


# ---------------------------------------------------------------------------
# Job 2: Sync Videos (Data in the Real World Series)
# ---------------------------------------------------------------------------

def sync_videos(vault_path: Path, content_dir: Path, dry_run: bool):
    """Sync video series from vault to Hugo content/series/."""
    series_src = vault_path / "Stuff" / "Content" / "Data in the Real World Series"
    series_dst = content_dir / "series"

    if not series_src.exists():
        print(f"  [SKIP] Video series source not found: {series_src}")
        return

    print(f"\n=== Syncing Video Series from {series_src} ===")

    # Write section _index.md
    section_fm = {
        "title": "Data in the Real World",
        "description": "A video series exploring real data problems — from messy spreadsheets to AI governance.",
    }
    if not dry_run:
        series_dst.mkdir(parents=True, exist_ok=True)
        idx = series_dst / "_index.md"
        idx.write_text(
            "---\n"
            + yaml.dump(section_fm, default_flow_style=False, allow_unicode=True, sort_keys=False).rstrip()
            + "\n---\n",
            encoding="utf-8",
        )
        print(f"  [WRITE] {idx}")
    else:
        print(f"  [DRY-RUN] {series_dst / '_index.md'}")

    count = 0
    for folder in sorted(series_src.iterdir()):
        if not folder.is_dir():
            continue
        # Only process numbered folders (01, 02, etc.)
        if not re.match(r"^\d+$", folder.name):
            continue

        # Find the video metadata .md file (not script.md or PROMPT files)
        video_md = None
        for f in folder.glob("*.md"):
            if f.name.lower() in ("script.md",) or f.name.startswith("PROMPT"):
                continue
            video_md = f
            break

        if not video_md:
            print(f"  [SKIP] No video md in {folder.name}/")
            continue

        raw = video_md.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)

        title = meta.get("title") or video_md.stem
        number = meta.get("number", folder.name.lstrip("0") or "0")
        slug = f"{int(number):02d}-{slugify(title)}"

        track = meta.get("track", "")
        date = meta.get("published_date")
        if date:
            date = str(date).strip()[:10]
            if re.match(r"^\d{4}$", date):
                date = f"{date}-01-01"
            elif re.match(r"^\d{4}-\d{2}$", date):
                date = f"{date}-01"
        status = meta.get("status", "")
        topic = strip_wikilinks(str(meta.get("topic", "")))

        fm = {
            "title": title,
            "number": int(number),
            "track": track,
        }
        if date:
            fm["date"] = date
        if status:
            fm["status"] = status
        if topic:
            fm["topic"] = topic
        if meta.get("linkedin_url"):
            fm["linkedin_url"] = str(meta["linkedin_url"])
        if meta.get("youtube_url"):
            fm["youtube_url"] = str(meta["youtube_url"])

        # Extract abstract from body — first paragraph after frontmatter
        abstract = meta.get("abstract", "")
        if not abstract and body.strip():
            # Use first non-heading, non-empty paragraph
            for para in re.split(r"\n\s*\n", body):
                para = para.strip()
                if para and not para.startswith("#") and not para.startswith("!") and not para.startswith("[["):
                    abstract = para[:500]
                    break
        if abstract:
            fm["abstract"] = abstract

        write_hugo_page(series_dst / slug, fm, "", dry_run)
        count += 1

    print(f"  Total videos synced: {count}")


# ---------------------------------------------------------------------------
# Job 3: Generate Ontology JSON
# ---------------------------------------------------------------------------

def extract_tags_from_project(content: str) -> list[str]:
    """Extract backtick-enclosed tags from a project readme's ## Tags section."""
    tags_match = re.search(r"##\s+Tags\s*\n(.+?)(?=\n##|\Z)", content, re.DOTALL)
    if not tags_match:
        return []
    return re.findall(r"`([^`]+)`", tags_match.group(1))


def generate_ontology(vault_path: Path, static_dir: Path, dry_run: bool):
    """Generate ontology.json for vis-network visualization."""
    ontology_csv = vault_path / "_ontologies" / "core" / "tag_ontology.csv"
    projects_dir = vault_path / "Stuff" / "Project_readmes"

    if not ontology_csv.exists():
        print(f"  [SKIP] Ontology CSV not found: {ontology_csv}")
        return

    print(f"\n=== Generating Ontology JSON ===")
    print(f"  Source: {ontology_csv}")

    # Read ontology
    ontology = []
    with open(ontology_csv, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ontology.append({
                "category": row["category"].strip(),
                "subcategory": row["subcategory"].strip(),
                "tag": row["tag"].strip(),
            })

    print(f"  Ontology entries: {len(ontology)}")

    # Count projects per tag
    tag_counts: dict[str, int] = {}
    if projects_dir.exists():
        for md_file in projects_dir.glob("*.md"):
            try:
                content = md_file.read_text(encoding="utf-8")
            except Exception:
                continue
            tags = extract_tags_from_project(content)
            for tag in tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        print(f"  Projects scanned: {len(list(projects_dir.glob('*.md')))}")
    else:
        print(f"  [WARN] Projects dir not found: {projects_dir}")

    print(f"  Tags with projects: {len(tag_counts)}")

    # Category colors
    category_colors = {
        "Technical Stack": "#4FC3F7",
        "Organizations": "#81C784",
        "Domain Areas": "#FFB74D",
        "Technical Approaches": "#E57373",
        "Functional Areas": "#BA68C8",
        "Work Context": "#FFD54F",
        "Data Sources": "#4DB6AC",
        "Delivery": "#F06292",
    }

    # Build vis-network nodes and edges
    nodes = []
    edges = []

    # Center node
    nodes.append({
        "id": "center",
        "label": "Amit Kohli",
        "size": 30,
        "color": "#FFFFFF",
        "font": {"size": 16, "bold": True},
        "shape": "box",
    })

    # Collect unique categories and subcategories
    categories = {}
    subcategories = {}

    for entry in ontology:
        cat = entry["category"]
        sub = entry["subcategory"]
        tag = entry["tag"]

        cat_id = f"cat-{slugify(cat)}"
        sub_id = f"sub-{slugify(cat)}-{slugify(sub)}"
        tag_id = f"tag-{slugify(tag)}"

        color = category_colors.get(cat, "#90A4AE")

        # Category node
        if cat_id not in categories:
            categories[cat_id] = cat
            nodes.append({
                "id": cat_id,
                "label": cat,
                "size": 20,
                "color": color,
                "font": {"size": 14, "bold": True},
                "shape": "box",
            })
            edges.append({"from": "center", "to": cat_id})

        # Subcategory node
        if sub_id not in subcategories:
            subcategories[sub_id] = sub
            nodes.append({
                "id": sub_id,
                "label": sub,
                "size": 14,
                "color": color,
                "font": {"size": 11},
                "shape": "box",
            })
            edges.append({"from": cat_id, "to": sub_id})

        # Tag node — size based on project count
        project_count = tag_counts.get(tag, 0)
        tag_size = 6 + min(project_count * 2, 20)
        nodes.append({
            "id": tag_id,
            "label": tag,
            "size": tag_size,
            "color": color,
            "font": {"size": 10},
            "title": f"{tag} ({project_count} projects)",
            "shape": "dot",
        })
        edges.append({"from": sub_id, "to": tag_id})

    data = {"nodes": nodes, "edges": edges}

    output_dir = static_dir / "data"
    output_file = output_dir / "ontology.json"

    action = "DRY-RUN" if dry_run else "WRITE"
    print(f"  [{action}] {output_file}")
    print(f"  Nodes: {len(nodes)}, Edges: {len(edges)}")

    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Sync Obsidian vault content to Hugo site.")
    parser.add_argument("--vault-path", required=True, type=Path, help="Path to the Obsidian vault root (e.g. C:\\boom)")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing files")
    args = parser.parse_args()

    vault = args.vault_path
    if not vault.exists():
        print(f"ERROR: Vault path does not exist: {vault}")
        return

    # Project root is one level up from scripts/
    project_root = Path(__file__).resolve().parent.parent
    content_dir = project_root / "content"
    static_dir = project_root / "static"

    print(f"Vault:   {vault}")
    print(f"Content: {content_dir}")
    print(f"Static:  {static_dir}")
    if args.dry_run:
        print("MODE:    DRY RUN (no files will be written)")

    sync_talks(vault, content_dir, args.dry_run)
    sync_videos(vault, content_dir, args.dry_run)
    generate_ontology(vault, static_dir, args.dry_run)

    print("\nDone!")


if __name__ == "__main__":
    main()
