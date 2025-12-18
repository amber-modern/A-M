#!/usr/bin/env python3
"""
Script to convert Squarespace export to self-hostable static site.
Removes external Squarespace CDN dependencies and cleans up HTML.
"""

import os
import re
import glob
from pathlib import Path

def remove_squarespace_cdn_links(content):
    """Remove external Squarespace CDN links for components."""
    # Remove button component CDN links
    content = re.sub(
        r'<link rel="stylesheet" type="text/css" href="https://definitions\.sqspcdn\.com/website-component-definition/static-assets/website\.components\.button/[^"]+\.css"/>',
        '',
        content
    )
    content = re.sub(
        r'<script defer src="https://definitions\.sqspcdn\.com/website-component-definition/static-assets/website\.components\.button/[^"]+\.js"></script>',
        '',
        content
    )
    
    # Remove other component CDN links
    content = re.sub(
        r'<link rel="stylesheet" type="text/css" href="https://definitions\.sqspcdn\.com/website-component-definition/static-assets/[^"]+\.css"/>',
        '',
        content
    )
    content = re.sub(
        r'<script defer src="https://definitions\.sqspcdn\.com/website-component-definition/static-assets/[^"]+\.js"></script>',
        '',
        content
    )
    
    # Remove data attributes that reference external CDN
    content = re.sub(
        r'data-block-css="\[&quot;https://definitions\.sqspcdn\.com/[^&]+&quot;\]"',
        '',
        content
    )
    content = re.sub(
        r'data-block-scripts="\[&quot;https://definitions\.sqspcdn\.com/[^&]+&quot;\]"',
        '',
        content
    )
    
    # Remove preconnect to Squarespace CDN (keep Typekit)
    content = re.sub(
        r'<link rel="preconnect" href="https://images\.squarespace-cdn\.com">\s*',
        '',
        content
    )
    
    return content

def remove_squarespace_badge(content):
    """Remove 'Made with Squarespace' badge."""
    content = re.sub(
        r'<p[^>]*>Made with <a[^>]*href="https://www\.squarespace\.com/"[^>]*>Squarespace</a></p>',
        '',
        content,
        flags=re.IGNORECASE
    )
    return content

def process_html_file(filepath):
    """Process a single HTML file."""
    print(f"Processing {filepath}...")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Remove Squarespace CDN links
    content = remove_squarespace_cdn_links(content)
    
    # Remove Squarespace badge
    content = remove_squarespace_badge(content)
    
    # Only write if content changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ Updated {filepath}")
        return True
    else:
        print(f"  - No changes needed for {filepath}")
        return False

def main():
    """Main conversion function."""
    base_dir = Path(__file__).parent
    
    # Find all HTML files
    html_files = list(base_dir.glob('*.html'))
    
    if not html_files:
        print("No HTML files found!")
        return
    
    print(f"Found {len(html_files)} HTML file(s) to process\n")
    
    updated_count = 0
    for html_file in html_files:
        if process_html_file(html_file):
            updated_count += 1
    
    print(f"\n✓ Conversion complete! Updated {updated_count} file(s).")
    print("\nNote: Some Squarespace-specific features may not work:")
    print("  - Forms will need a backend replacement")
    print("  - Shopping cart functionality requires backend")
    print("  - Some interactive features may need JavaScript updates")

if __name__ == '__main__':
    main()

