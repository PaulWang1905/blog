"""Build script for Puyu's Personal Blog.

Run with:  python build.py
Requires:  pip install -r requirements.txt  &&  npm install
"""
import hashlib
import re

from oxie import Site, SiteConfig

config = SiteConfig(
    # source/, src/ and docs/ are the defaults; override them if you move things.
    collect_dirs={
        # Everything in source/image is copied to docs/image ...
        "source/image": "docs/image",
        # ... and source/static lands at the site root, next to index.html.
        "source/static": "docs",
    },
    # Syntax highlighting stylesheet written to docs/pygments.css.
    pygments_style="github-dark",
    # Compiles src/styles.css into docs/styles.css with Tailwind + daisyUI.
    # Set to None if you want to manage CSS yourself.
    css_build_command=("npm", "run", "build:css"),

    # --- Optional pages -------------------------------------------------
    # Both templates below live in src/ but are switched off, because this
    # blog has no content for them yet.
    #
    # Reading notes: a standalone page that pulls the list from
    # github.com/PaulWang1905/Readings at view time, so it needs nothing
    # in this repo. Turn it on with:
    #   simple_pages={"readings_note_template.html": "readings_note.html"},
    # then add a /readings_note.html link to src/header.html.
    #
    # Photography: needs source/photo/photos.md plus the images, and
    # Pillow for the thumbnails. Turn it on with:
    #   photography=True, thumbnails=True,
    # then add a /photography.html link to src/header.html.
)

# --- Post-build: the subscribe page ------------------------------------
# docs/feed.xml is a document, not a page, so a browser shows it as raw XML
# to anyone who clicks an RSS link expecting something readable. The usual
# fix — an XSLT stylesheet on the feed — has an expiry date now: Chrome
# disables XSLT on 17 November 2026, and Firefox and WebKit intend to
# follow. So the readable version is a real HTML page instead.
#
# This runs after Site.build() rather than through oxie's `simple_pages`,
# which renders with only meta_data and phrases in context; the page also
# needs the posts. Tailwind has already run by this point, but styles.css
# scans src/**/*.html as well as docs/, so the template's classes survive.
FEED_PAGE_TEMPLATE = "feed_page_template.html"
FEED_PAGE_OUTPUT = "feed.html"


def build_feed_page(site):
    """Render docs/feed.html, the human-readable face of docs/feed.xml."""
    posts = site.posts[:site.config.feed_max_items]
    rendered = site.template(FEED_PAGE_TEMPLATE).render(
        meta_data=site.meta_data,
        phrases=site.meta_data["phrases"],
        posts=posts,
    )
    path = site.config.output_dir / FEED_PAGE_OUTPUT
    path.write_text(rendered, encoding="utf-8")
    print(f"Feed page written to {path} ({len(posts)} items)")


# --- Post-build: the table ----------------------------------------------
# docs/table.html deals every post out as a card and turns the aphorisms
# into a deck to draw from: the playful counterpart to the home page's
# index. Built here for the same reason as the feed page: it needs the
# posts, which `simple_pages` does not pass.
TABLE_PAGE_TEMPLATE = "table_template.html"
TABLE_PAGE_OUTPUT = "table.html"


def build_table_page(site):
    """Render docs/table.html, every post as a card on a table."""
    rendered = site.template(TABLE_PAGE_TEMPLATE).render(
        meta_data=site.meta_data,
        phrases=site.meta_data["phrases"],
        posts=site.posts,
    )
    path = site.config.output_dir / TABLE_PAGE_OUTPUT
    path.write_text(rendered, encoding="utf-8")
    print(f"Table page written to {path} ({len(site.posts)} cards)")


# --- Post-build: a version on the stylesheet ----------------------------
# Every page links /styles.css. Browsers keep a copy of it for a while
# (GitHub Pages allows 10 minutes), so just after a deploy a visitor can
# get a new page with the old stylesheet, and see it broken: the header's
# glass, for one, needs the stylesheet it was built with. Putting the
# stylesheet's own fingerprint in the link (/styles.css?v=1a2b3c4d5e) gives
# every new stylesheet a new address, so each page loads the stylesheet it
# was built with. Runs last, once styles.css and every page are written.
STYLESHEET_LINK = re.compile(r'href="/styles\.css(?:\?v=[0-9a-f]+)?"')


def version_stylesheet(site):
    """Point every page in docs/ at this build's styles.css, by fingerprint."""
    out = site.config.output_dir
    version = hashlib.sha256((out / "styles.css").read_bytes()).hexdigest()[:10]
    pages = 0
    for page in out.rglob("*.html"):
        text = page.read_text(encoding="utf-8")
        linked = STYLESHEET_LINK.sub(f'href="/styles.css?v={version}"', text)
        if linked != text:
            page.write_text(linked, encoding="utf-8")
            pages += 1
    print(f"Stylesheet linked as styles.css?v={version} in {pages} pages")


if __name__ == "__main__":
    site = Site(config)
    site.build()
    if config.feed:
        build_feed_page(site)
    build_table_page(site)
    version_stylesheet(site)
