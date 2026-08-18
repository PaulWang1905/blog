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
    # Compiles src/styles.css into docs/styles.css with Tailwind.
    # Set to None if you want to manage CSS yourself.
    css_build_command=("npm", "run", "build:css"),
)

if __name__ == "__main__":
    Site(config).build()
