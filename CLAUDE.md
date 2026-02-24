# Rebuild amitkohli.com

## Current State (as of 2026-02-24)

**Branch:** `redesign` (created from `master`)
**Hugo:** v0.156.0 Extended (installed via winget)
**Theme:** Blowfish (git submodule at `themes/blowfish/`)
**Hugo binary:** `C:\Users\AmitKohli\AppData\Local\Microsoft\WinGet\Packages\Hugo.Hugo.Extended_Microsoft.Winget.Source_8wekyb3d8bbwe\hugo.exe`

### Completed
- **Phase 1: Repo Setup + Blowfish Foundation** ✅
  - Created `redesign` branch from `master`
  - Removed old `config.yaml`, `.Rprofile`, `.Rproj`, `index.Rmd`, `worldMapOfProjects.R`
  - Removed `hugo-lithium` theme from git tracking
  - Added `public/` to `.gitignore`, removed from git tracking
  - Installed Blowfish as git submodule
  - Created `config/_default/` with 5 config files (hugo.toml, params.toml, languages.en.toml, menus.en.toml, markup.toml)
  - Fixed blog post frontmatter issues (tags/categories as lists, empty slug)
  - Hugo builds successfully (92 pages)

- **Phase 2: Static Assets** ✅
  - Decks copied to `static/decks/` (earl2025, gpir, what-is-rag)
  - Downloaded vis-network.min.js (630KB) to `static/js/vis-network.min.js`
  - Copied consulting images (66 files + `new/` subfolder) to `static/img/`

- **Phase 3: Python Sync Script** ✅
  - Created `scripts/sync_from_vault.py` with 3 jobs
  - Sync talks: 21 talks from `C:\boom\Stuff\Talks\` → `content/talks/<slug>/index.md` (skips decks, templates, metadata files)
  - Sync videos: 7 videos from `C:\boom\Stuff\Content\Data in the Real World Series\` → `content/series/<num>-<slug>/index.md`
  - Generate ontology: 156 tags, 296 projects → `static/data/ontology.json` (211 nodes, 210 edges)
  - Usage: `python scripts/sync_from_vault.py --vault-path C:\boom [--dry-run]`

- **Phase 4: Content Pages + Layouts** ✅
  - Homepage: `layouts/partials/home/custom.html` — hero, ontology vis-network, 3 value cards
  - Talks: `layouts/talks/list.html` + `single.html` — Alpine.js topic filtering, card grid, featured section
  - Series: `layouts/series/list.html` + `single.html` — 3 tracks (A/B/C), episode grid, YouTube embeds
  - About: `content/about/index.md` — narrative bio + 5 testimonials from consulting page
  - Contact: `content/contact/index.md` — Calendly embed, available-for block, social links
  - Archive: 8 blog posts migrated from `content/post/` → `content/archive/` with URL aliases (40 total)
  - Custom CSS: `assets/css/custom.css` — ontology viz, talk cards, track badges, responsive embeds
  - Alpine.js loaded via `layouts/partials/extend-head.html`
  - Also fixed sync script: partial dates (e.g. "2024") padded to "2024-01-01"
  - Hugo builds: **138 pages**, no errors

- **Phase 5: Redirects + Netlify Config** ✅
  - Updated `netlify.toml`: Hugo 0.156.0 extended, `hugo --gc --minify`
  - Redirects: /aboutme/ → /about/, /comfort/ → /about/, consulting decks → /decks/

- **Phase 6: Test + Deploy** ✅ (build verified)
  - Production build: 138 pages, 40 aliases, 848 static files, no errors
  - All 6 key pages verified: homepage, talks, series, about, contact, archive
  - Ready to push `redesign` branch → Netlify preview, then merge to `master`

## Site Structure
```
/                    Homepage (hero + ontology network viz + value prop + CTA)
/talks/              Speaking portfolio (card grid with topic filtering)
/series/             "Data in the Real World" video series landing page
/about/              Narrative bio + downloadable CV PDF
/contact/            Calendly booking
/decks/[name]/       Slide deck presentations
/archive/            Old blog posts (redirects from old URLs)
```

## Key Existing Blog Posts (need aliases when migrating to /archive/)
- `2015-10-29-how-to-move-odbc-dsn-information-from-one-computer-to-another.md` — has explicit `url:` field
- `2018-07-07-crime-statistics-in-london.html` — rendered HTML
- `2019-03-08-plot-shapes-for-100000-movies-using-new-package-theplotthickens.html` — rendered HTML
- `2020-07-31-introducing-carbonfootprintr...html` — rendered HTML
- `2022-07-20-how-are-sdgs-interconnected/` — page bundle with index.Rmd + index.html
- `2022-10-19-10-reasons-why-random-forest.../` — page bundle
- `2023-03-15-an-r-user-s-guide-to-python.../` — page bundle
- `2023-07-30-sdg-direction-estimation/` — page bundle
- `2024-08-08-match-the-feeling-not-the-question/` — page bundle
