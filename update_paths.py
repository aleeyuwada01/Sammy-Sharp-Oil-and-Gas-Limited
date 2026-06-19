import os
import re

# Update all HTML files: replace src="imagename" with src="assets/images/imagename"
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

img_extensions = ('.jpeg', '.jpg', '.png', '.gif', '.webp', '.svg')

def replace_img_src(content):
    # Match src="something.jpg/png/etc" NOT already in assets/images/
    def replacer(m):
        quote = m.group(1)
        path = m.group(2)
        # skip if already has a path prefix or is a URL
        if '/' in path or path.startswith('http'):
            return m.group(0)
        ext = os.path.splitext(path)[1].lower()
        if ext in img_extensions:
            return f'src={quote}assets/images/{path}{quote}'
        return m.group(0)
    return re.sub(r'src=(["\'])([^"\']+)\1', replacer, content)

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fh:
        content = fh.read()
    new_content = replace_img_src(content)
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new_content)
        print(f"Updated: {f}")
    else:
        print(f"No change: {f}")

# Update nav.js too
nav_path = os.path.join('assets', 'js', 'nav.js')
with open(nav_path, 'r', encoding='utf-8') as fh:
    nav_content = fh.read()
new_nav = replace_img_src(nav_content)
if new_nav != nav_content:
    with open(nav_path, 'w', encoding='utf-8') as fh:
        fh.write(new_nav)
    print(f"Updated: {nav_path}")

print("\nAll paths updated.")
