"""
Scrape every page on redesign--datastrategist.netlify.app and find encoding artifacts.
Reports which pages have issues and what they are.
"""
import re
import requests
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from collections import defaultdict

BASE = "https://redesign--datastrategist.netlify.app"

# ΓÇÖ etc are UTF-8 bytes decoded as CP437, appearing as multi-char sequences
# These are the exact character sequences that appear as visible garbage
BAD_PATTERNS = [
    "ΓÇÖ", "ΓÇÿ",           # right/left single quote
    "ΓÇ£", "ΓÇ¥",           # left/right double quote
    "ΓÇö", "ΓÇô",           # em dash, en dash
    "ΓÇª",                   # ellipsis
    "ΓÇÜ", "ΓÇ¢",           # low single quotes
    "┬á",                    # non-breaking space (UTF-8 nbsp misread)
    "┬½", "┬╗",             # angle quotes
    "┬«", "┬⌐",             # registered, copyright
    "Γäó",                   # trademark
    "Γé¼",                   # euro sign
    "├⌐", "├¿", "├ó", "├á", # e/a accents
    "├«", "├¬", "├»",       # i/e accents
    "├╝", "├╗", "├╣", "├┤", # u/o accents
    "├º", "├ç",             # c cedilla
    "ΓÇÑ",                   # bullet point
]

class LinkExtractor(HTMLParser):
    def __init__(self, base):
        super().__init__()
        self.base = base
        self.links = set()
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, val in attrs:
                if attr == 'href' and val:
                    full = urljoin(self.base, val)
                    if full.startswith(self.base):
                        self.links.add(full.rstrip('/') + '/')

def get_text(html):
    """Strip HTML tags and return text."""
    return re.sub(r'<[^>]+>', ' ', html)

def check_page(url):
    """Fetch URL and return dict of bad patterns found with context."""
    try:
        r = requests.get(url, timeout=15, headers={'Accept-Encoding': 'identity'})
        r.encoding = 'utf-8'
        html = r.text
        text = get_text(html)
        found = {}
        for pat in BAD_PATTERNS:
            if pat in text:
                # Get a short context snippet
                idx = text.index(pat)
                ctx = text[max(0, idx-30):idx+50].replace('\n', ' ').strip()
                found[pat] = ctx
        return found
    except Exception as e:
        return {"ERROR": str(e)}

def get_all_blog_urls():
    """Get all article URLs from blog listing pages."""
    article_urls = set()
    # Try up to 10 pages
    for page in range(1, 11):
        if page == 1:
            url = f"{BASE}/blog/"
        else:
            url = f"{BASE}/blog/page/{page}/"
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 404:
                break
            r.encoding = 'utf-8'
            extractor = LinkExtractor(BASE)
            extractor.feed(r.text)
            # Filter: only links that look like blog posts (not tag/page links)
            for link in extractor.links:
                path = urlparse(link).path
                parts = path.strip('/').split('/')
                # Blog post = has a slug, not index pages like /blog/, /tags/, /page/
                if (not any(p in parts for p in ['tags', 'page', 'blog', 'series', 'talks', 'about', 'contact'])
                        and len(parts) >= 1 and parts[0] not in ('', 'blog')):
                    article_urls.add(link)
                # Also include /blog/slug/ paths
                if len(parts) == 2 and parts[0] == 'blog':
                    article_urls.add(link)
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            break
    return article_urls

print("=== Collecting article URLs ===")
urls = get_all_blog_urls()

# Also add known problem pages directly
extra = [
    f"{BASE}/10-things-you-didnt-know-about-taxi-costs-in-accra/",
    f"{BASE}/setting-up-twitter-streamr-service-on-an-ubuntu-server/",
    f"{BASE}/introducing-the-monitoring-and-evaluation-bullet-chart/",
]
urls.update(extra)

print(f"Found {len(urls)} URLs to check")
print()

issues = {}
clean = []
for url in sorted(urls):
    found = check_page(url)
    if found and "ERROR" not in found:
        issues[url] = found
    elif "ERROR" in found:
        print(f"ERROR: {url} -> {found['ERROR']}")
    else:
        clean.append(url)

print(f"\n=== RESULTS ===")
print(f"Clean: {len(clean)}")
print(f"Has issues: {len(issues)}")
print()

for url, found in sorted(issues.items()):
    path = urlparse(url).path
    print(f"\n{'='*60}")
    print(f"URL: {path}")
    for pat, ctx in found.items():
        print(f"  [{pat}] in: ...{ctx}...")
