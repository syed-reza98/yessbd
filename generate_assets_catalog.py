#!/usr/bin/env python3
import os

def generate_catalog():
    catalog = []
    catalog.append('# Comprehensive Downloaded Assets Catalog')
    catalog.append('**Source Portals:** [https://yessbd.com](https://yessbd.com) and [https://yessbangla.top](https://yessbangla.top)')

    all_files = []
    for root, dirs, files in os.walk('assets'):
        for f in files:
            fpath = os.path.join(root, f)
            size = os.path.getsize(fpath)
            all_files.append((fpath, size))

    catalog.append(f'**Total Assets Downloaded:** {len(all_files)}')
    catalog.append(f'**Total Downloaded Size:** {sum(s for p, s in all_files):,} bytes ({sum(s for p, s in all_files)/(1024*1024):.2f} MB)\n')
    catalog.append('---\n')

    grouped = {}
    for fpath, size in all_files:
        pdir = os.path.dirname(fpath)
        grouped.setdefault(pdir, []).append((fpath, size))

    dir_purposes = {
        'assets/yessbd/logos': 'Corporate & Subsidiary Logos (High-res PNGs)',
        'assets/yessbd/heroes': 'Main Hero Banners & Section Backgrounds',
        'assets/yessbd/ventures': 'Ventures Graphics & Branding (Shondhaan, Organic Haat, Akash OTT, Yess Soft)',
        'assets/yessbd/testimonials': 'Client Testimonial Headshots',
        'assets/yessbd/icons': 'Corporate UI Icons',
        'assets/yessbd/general': 'Infographics, Delivery, & Service Illustrations',
        'assets/yessbangla/logos': 'Yess Bangla IT Solutions Main Brand Logo',
        'assets/yessbangla/hero': 'Hero Section Background Image',
        'assets/yessbangla/demos': 'Interactive Product Demo Screenshots (All 48 Software Systems)',
        'assets/yessbangla/projects': 'Client Delivered Project Mockups (Akash TV, Shop, Table, etc.)',
        'assets/yessbangla/icons': 'Category & Product Badges / Icons',
        'assets/yessbangla/teams': 'Team Member Portraits',
        'assets/yessbangla/tech_icons': 'Technology Stack Vector Graphics (SVGs)',
    }

    catalog.append('## Assets Summary by Directory')
    catalog.append('| Directory | File Count | Size (MB) | Purpose / Content |')
    catalog.append('|---|---|---|---|')

    for pdir in sorted(grouped.keys()):
        items = grouped[pdir]
        total_sz = sum(s for p, s in items) / (1024 * 1024)
        purpose = dir_purposes.get(pdir, 'Website Assets')
        catalog.append(f'| [`{pdir}`]({pdir}) | {len(items)} files | {total_sz:.2f} MB | {purpose} |')

    catalog.append('\n---\n')

    for pdir in sorted(grouped.keys()):
        items = grouped[pdir]
        purpose = dir_purposes.get(pdir, 'Website Assets')
        catalog.append(f'## Directory: `{pdir}` ({len(items)} files — {purpose})')
        catalog.append('| File Name | File Size | Local File Link |')
        catalog.append('|---|---|---|')
        for fpath, size in sorted(items, key=lambda x: x[0]):
            fname = os.path.basename(fpath)
            catalog.append(f'| **{fname}** | {size:,} B | [`{fpath}`]({fpath}) |')
        catalog.append('')

    with open('ASSETS_CATALOG.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(catalog))

    print(f'Catalog generated successfully for {len(all_files)} assets.')

if __name__ == '__main__':
    generate_catalog()
