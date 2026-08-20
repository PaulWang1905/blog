"""Build script for Puyu's Personal Blog.

Run with:  python build.py
Requires:  pip install -r requirements.txt  &&  npm install
"""
from oxie import Site, SiteConfig

# Note on src/meta_data.json: "description" is a one-element LIST, not a
# string. oxie 0.3.1's IndexPage.parse() does meta_data["description"][0]
# (it expects the list the Markdown meta extension produces), so a plain
# string would reach the home page as its first character. Wrapping it
# keeps the site description intact in the masthead and the <meta> tag.

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

if __name__ == "__main__":
    Site(config).build()
