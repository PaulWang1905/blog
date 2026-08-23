"""Build script for Puyu's Personal Blog.

Run with:  python build.py
Requires:  pip install -r requirements.txt  &&  npm install
"""
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


if __name__ == "__main__":
    site = Site(config)
    site.build()
    if config.feed:
        build_feed_page(site)
