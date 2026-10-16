"""Bundle static/style.css and static/app.js into a single self-contained static/index.html.

Workflow:
  1. Keep editing static/index.html (with the <link> and <script src> tags), style.css and app.js.
  2. Run:  python scripts/bundle_ui.py
  3. Deploy / run the bundled static/index.html.

The first run saves your un-bundled page as static/index.src.html. Every later run rebuilds
index.html from that source, so editing style.css or app.js and re-running ALWAYS takes effect.
(Edit index.src.html, not index.html, if you change the page markup after the first run.)
"""
import sys
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
static_dir = base_dir / "static"

index_path = static_dir / "index.html"
src_path = static_dir / "index.src.html"
css_path = static_dir / "style.css"
js_path = static_dir / "app.js"

CSS_TAG = '<link rel="stylesheet" href="/static/style.css">'
JS_TAG = '<script src="/static/app.js"></script>'

# Pick the un-bundled source page.
if src_path.exists():
    source_html = src_path.read_text(encoding="utf-8")
else:
    source_html = index_path.read_text(encoding="utf-8")
    if CSS_TAG not in source_html and JS_TAG not in source_html:
        sys.exit(
            "index.html is already bundled and there is no index.src.html to rebuild from.\n"
            "Restore a version of index.html that contains the <link> and <script src> tags, then run again."
        )
    src_path.write_text(source_html, encoding="utf-8")
    print(f"Saved un-bundled source to {src_path.name}")

html = source_html

if CSS_TAG in html:
    html = html.replace(CSS_TAG, f"<style>\n{css_path.read_text(encoding='utf-8')}\n</style>")
else:
    print("WARNING: stylesheet <link> not found in the source page; style.css was NOT bundled.")

if JS_TAG in html:
    html = html.replace(JS_TAG, f"<script>\n{js_path.read_text(encoding='utf-8')}\n</script>")
else:
    print("WARNING: app.js <script src> tag not found in the source page; app.js was NOT bundled.")

index_path.write_text(html, encoding="utf-8")
print(f"Bundled UI written to {index_path}. Total size: {len(html)} bytes.")