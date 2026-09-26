#!/usr/bin/env python3
"""
Asset Downloader for yessbd.com and yessbangla.top
Downloads all logos, banners, demo screenshots, icons, project graphics, team photos, and documents.
"""

import os
import re
import glob
import time
import urllib.parse
import urllib.request
import ssl
from concurrent.futures import ThreadPoolExecutor, as_completed

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# Ensure directories exist
dirs = [
    'assets/yessbd/logos',
    'assets/yessbd/heroes',
    'assets/yessbd/ventures',
    'assets/yessbd/testimonials',
    'assets/yessbd/icons',
    'assets/yessbd/docs',
    'assets/yessbd/general',
    'assets/yessbangla/logos',
    'assets/yessbangla/hero',
    'assets/yessbangla/demos',
    'assets/yessbangla/projects',
    'assets/yessbangla/icons',
    'assets/yessbangla/teams',
    'assets/yessbangla/tech_icons',
    'assets/yessbangla/general',
]
for d in dirs:
    os.makedirs(d, exist_ok=True)

def collect_asset_tasks():
    tasks = []
    seen_urls = set()

    def add_task(url, local_path, category):
        if url not in seen_urls:
            seen_urls.add(url)
            tasks.append((url, local_path, category))

    files = glob.glob('raw_scraped_pages/*.html')

    for fpath in files:
        with open(fpath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        is_yb = 'yessbangla' in fpath
        base_url = 'https://yessbangla.top' if is_yb else 'https://yessbd.com'

        # Check attributes
        for raw in re.findall(r'(?:src|href|data-src|data-original)=[\"\']([^\"\']+)[\"\']', content, re.IGNORECASE):
            clean = raw.strip()
            if not clean or clean.startswith('data:') or clean.startswith('mailto:') or clean.startswith('tel:') or clean.startswith('javascript:'):
                continue
            
            lower = clean.lower()
            is_media = any(lower.endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico', '.jfif', '.pdf'])
            is_media_path = any(p in lower for p in ['/img/', '/images/', '/uploads/', '/testimonials/', '/demo_img/', '/demo_projects/', '/icons/', '/teams/'])
            
            if is_media or is_media_path:
                full_url = urllib.parse.urljoin(base_url, clean)
                fname = os.path.basename(urllib.parse.urlparse(full_url).path)
                if not fname or '.' not in fname:
                    fname = 'asset_' + re.sub(r'[^a-zA-Z0-9]', '_', clean) + '.png'
                
                if is_yb or 'yessbangla' in full_url:
                    if 'devicon' in full_url or 'jsdelivr' in full_url:
                        dest = os.path.join('assets/yessbangla/tech_icons', fname)
                        cat = 'Technology Icon'
                    elif '/demo_img/' in full_url:
                        dest = os.path.join('assets/yessbangla/demos', fname)
                        cat = 'Product Demo Screenshot'
                    elif '/demo_projects/' in full_url:
                        dest = os.path.join('assets/yessbangla/projects', fname)
                        cat = 'Client Project Screenshot'
                    elif '/icons/' in full_url:
                        dest = os.path.join('assets/yessbangla/icons', fname)
                        cat = 'Product / Feature Icon'
                    elif '/teams/' in full_url:
                        dest = os.path.join('assets/yessbangla/teams', fname)
                        cat = 'Team Member Photo'
                    elif 'logo' in fname.lower():
                        dest = os.path.join('assets/yessbangla/logos', fname)
                        cat = 'Logo'
                    elif 'hero' in fname.lower():
                        dest = os.path.join('assets/yessbangla/hero', fname)
                        cat = 'Hero Background'
                    else:
                        dest = os.path.join('assets/yessbangla/general', fname)
                        cat = 'General Graphic'
                else:
                    if '/logo/' in full_url or 'logo' in fname.lower():
                        dest = os.path.join('assets/yessbd/logos', fname)
                        cat = 'Corporate / Venture Logo'
                    elif '/hero/' in full_url or 'hero' in fname.lower():
                        dest = os.path.join('assets/yessbd/heroes', fname)
                        cat = 'Hero & Section Header'
                    elif '/testimonials/' in full_url:
                        dest = os.path.join('assets/yessbd/testimonials', fname)
                        cat = 'Client Testimonial Photo'
                    elif '/hero_section/' in full_url or '/Configuration/' in full_url:
                        dest = os.path.join('assets/yessbd/ventures', fname)
                        cat = 'Venture Branding & Graphic'
                    elif fname.lower().endswith('.pdf'):
                        dest = os.path.join('assets/yessbd/docs', fname)
                        cat = 'Corporate Brochure / Brief (PDF)'
                    elif '/icons/' in full_url or 'coin' in fname.lower():
                        dest = os.path.join('assets/yessbd/icons', fname)
                        cat = 'UI Icon'
                    else:
                        dest = os.path.join('assets/yessbd/general', fname)
                        cat = 'General Asset'
                
                add_task(full_url, dest, cat)

        # Also check background url(...) in content
        for raw in re.findall(r'url\([\'\"]?([^()\'\"]+)[\'\"]?\)', content, re.IGNORECASE):
            clean = raw.strip()
            if any(clean.lower().endswith(ext) for ext in ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.ico', '.jfif']):
                full_url = urllib.parse.urljoin(base_url, clean)
                fname = os.path.basename(urllib.parse.urlparse(full_url).path)
                folder = 'assets/yessbangla/hero' if is_yb else 'assets/yessbd/heroes'
                add_task(full_url, os.path.join(folder, fname), 'CSS Background Graphic')

    return tasks

def download_one(task):
    url, dest, cat = task
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    retries = 3
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=12, context=ctx) as resp:
                data = resp.read()
                if len(data) > 0:
                    with open(dest, 'wb') as f:
                        f.write(data)
                    return (url, dest, cat, len(data), 'SUCCESS')
                else:
                    return (url, dest, cat, 0, 'EMPTY_FILE')
        except Exception as e:
            if attempt < retries - 1:
                time.sleep(1)
            else:
                return (url, dest, cat, 0, f'ERROR: {e}')

def main():
    tasks = collect_asset_tasks()
    print(f'Starting concurrent download of {len(tasks)} assets...')
    
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_map = {executor.submit(download_one, t): t for t in tasks}
        for future in as_completed(future_map):
            res = future.result()
            results.append(res)
            url, dest, cat, size, status = res
            if status == 'SUCCESS':
                print(f'[OK] {dest} ({size:,} bytes)')
            else:
                print(f'[{status}] {url} -> {dest}')

    # Summary
    success = [r for r in results if r[4] == 'SUCCESS']
    failed = [r for r in results if r[4] != 'SUCCESS']
    print(f'\nFinished: {len(success)} downloaded successfully, {len(failed)} failed.')

    # Generate Markdown Catalog
    catalog = []
    catalog.append('# Downloaded Assets Catalog')
    catalog.append(f'**Total Assets Downloaded:** {len(success)}')
    catalog.append(f'**Total Size:** {sum(r[3] for r in success):,} bytes\n')
    catalog.append('---')
    
    # Group by category and directory
    grouped = {}
    for url, dest, cat, size, status in success:
        parent_dir = os.path.dirname(dest)
        grouped.setdefault(parent_dir, []).append((url, dest, cat, size))

    for pdir in sorted(grouped.keys()):
        items = grouped[pdir]
        catalog.append(f'\n## Directory: `{pdir}` ({len(items)} files)')
        catalog.append('| File Name | Category | Size | Source URL |')
        catalog.append('|---|---|---|---|')
        for url, dest, cat, size in sorted(items, key=lambda x: x[1]):
            fname = os.path.basename(dest)
            catalog.append(f'| **{fname}** | {cat} | {size:,} B | [{url}]({url}) |')

    if failed:
        catalog.append('\n## Unreachable / Missing Assets')
        catalog.append('| Source URL | Destination Path | Error Reason |')
        catalog.append('|---|---|---|')
        for url, dest, cat, size, status in failed:
            catalog.append(f'| [{url}]({url}) | `{dest}` | {status} |')

    with open('ASSETS_CATALOG.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(catalog))

    print('Wrote ASSETS_CATALOG.md')

if __name__ == '__main__':
    main()
