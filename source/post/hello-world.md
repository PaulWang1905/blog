---
Title: Hello World
Summary: The first post on Puyu's Personal Blog — how posts work in oxie.
Authors: Puyu Wang
Date: 2026-08-18
Category: Blog
Tags: [oxie, writing]
---

# Hello World

Every file in `source/post/` becomes a post. The frontmatter above uses
**capitalised keys** (`Title`, `Authors`, `Date`, `Category`, `Tags`), which
oxie reads to build the blog index and per-category pages.

## Things that work out of the box

- Tables, footnotes[^1] and `~~strikethrough~~`
- Fenced code with syntax highlighting:

```python
from oxie import Site, SiteConfig

Site(SiteConfig()).build()
```

- Maths, via `pymdownx.arithmatex`
- Category pages: this post is in *Blog*, so it appears on `blog_Blog.html`

[^1]: Footnotes look like this.

## Next steps

Delete this file, write your own, and rebuild.
