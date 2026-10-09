from pathlib import Path
import re, json
root = Path("content/seo/pages")
files = sorted(root.rglob("*.md"))
assert files, "No markdown pages found"
for path in files:
    text = path.read_text()
    assert text.startswith("---"), f"Missing frontmatter: {path}"
    assert re.search(r"^# ", text, re.M), f"Missing H1: {path}"
    assert "meta_description:" in text, f"Missing meta_description: {path}"
    assert len(re.findall(r"^# ", text, re.M)) == 1, f"Expected exactly one H1 in {path}"
for path in [Path('content/seo/structured-data/local-business.json'), Path('content/seo/structured-data/faq-home.json')]:
    json.loads(path.read_text())
print(f"OK {len(files)} pages validated")
