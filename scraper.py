#!/usr/bin/env python3
"""
Scraper script for extracting products and services from:
- https://yessbd.com
- https://yessbangla.top
"""

import os
import re
import csv
import json
import urllib.request

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'

def fetch_url(url):
    req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode('utf-8', errors='ignore')

def main():
    print("Scraping https://yessbangla.top and https://yessbd.com...")
    all_items = []

    # 1. Fetch / Read yessbangla.top
    yb_file = os.path.join('raw_scraped_pages', 'yessbangla_home.html')
    if os.path.exists(yb_file):
        with open(yb_file, 'r', encoding='utf-8') as f:
            yb_html = f.read()
    else:
        yb_html = fetch_url('https://yessbangla.top')

    # Products (#products)
    products_sec = re.search(r'<section[^>]*id=[\"\']products[\"\'][^>]*>(.*?)</section>', yb_html, re.DOTALL).group(1)
    product_cards = re.findall(r'<a\s+([^>]*class=[\"\'][^\"\']*product-card[^\"\']*[\"\'][^>]*)>(.*?)</a>', products_sec, re.DOTALL)

    for attrs, inner in product_cards:
        href = re.search(r'href=[\"\']([^\"\']+)[\"\']', attrs).group(1)
        cat = re.search(r'data-category=[\"\']([^\"\']+)[\"\']', attrs)
        category = cat.group(1).capitalize() if cat else 'General'
        title_m = re.search(r'<h[1-5][^>]*>(.*?)</h[1-5]>', inner, re.DOTALL)
        title = ' '.join(re.sub(r'<[^>]+>', ' ', title_m.group(1)).split()) if title_m else ''
        p_m = re.search(r'<p[^>]*>(.*?)</p>', inner, re.DOTALL)
        desc = ' '.join(re.sub(r'<[^>]+>', ' ', p_m.group(1)).split()) if p_m else ''
        type_m = re.search(r'<span[^>]*class=[\"\'][^\"\']*(?:bg-emerald-50|text-emerald-700|text-xs)[^\"\']*[\"\'][^>]*>(.*?)</span>', inner, re.DOTALL)
        app_type = ' '.join(re.sub(r'<[^>]+>', ' ', type_m.group(1)).split()) if type_m else 'Web Application'

        all_items.append({
            'site': 'yessbangla.top',
            'type': 'Software Product / Demo',
            'name': title,
            'category': category,
            'platform': app_type,
            'url': href,
            'description': desc
        })

    # Services (#others_products)
    others_sec = re.search(r'<section[^>]*id=[\"\']others_products[\"\'][^>]*>(.*?)</section>', yb_html, re.DOTALL).group(1)
    others_cards = re.findall(r'<a\s+([^>]*href=[\"\'][^\"\']+[\"\'][^>]*)>(.*?)</a>', others_sec, re.DOTALL)

    for attrs, inner in others_cards:
        href = re.search(r'href=[\"\']([^\"\']+)[\"\']', attrs).group(1)
        title_m = re.search(r'<h[1-5][^>]*>(.*?)</h[1-5]>', inner, re.DOTALL)
        title = ' '.join(re.sub(r'<[^>]+>', ' ', title_m.group(1)).split()) if title_m else ''
        p_m = re.search(r'<p[^>]*>(.*?)</p>', inner, re.DOTALL)
        desc = ' '.join(re.sub(r'<[^>]+>', ' ', p_m.group(1)).split()) if p_m else ''

        all_items.append({
            'site': 'yessbangla.top',
            'type': 'Software Service / System Solution',
            'name': title,
            'category': 'Enterprise Management Solutions',
            'platform': 'SaaS / Enterprise System',
            'url': href if href != '#' else 'https://yessbangla.top/#contact',
            'description': desc
        })

    # Projects (#projects)
    proj_sec = re.search(r'<section[^>]*id=[\"\']projects[\"\'][^>]*>(.*?)</section>', yb_html, re.DOTALL).group(1)
    all_items.append({
        'site': 'yessbangla.top',
        'type': 'Featured Product / Project',
        'name': 'Akash.tv',
        'category': 'OTT Platform & Media',
        'platform': 'Responsive Web & Mobile OTT Platform',
        'url': 'https://akash.tv/',
        'description': 'A professional OTT streaming system designed with responsive desktop and mobile experiences, smooth content browsing, and a polished user interface for modern digital entertainment.'
    })

    cards = re.split(r'<div[^>]*class=[\"\'][^\"\']*group\s+bg-white[^\"\']*[\"\']', proj_sec)
    for item in cards[1:]:
        title_m = re.search(r'<h[1-5][^>]*>(.*?)</h[1-5]>', item, re.DOTALL)
        title = ' '.join(re.sub(r'<[^>]+>', ' ', title_m.group(1)).split()) if title_m else ''
        p_m = re.search(r'<p[^>]*>(.*?)</p>', item, re.DOTALL)
        desc = ' '.join(re.sub(r'<[^>]+>', ' ', p_m.group(1)).split()) if p_m else ''
        cat_m = re.search(r'<span[^>]*class=[\"\'][^\"\']*(?:badge|text-xs|tracking-wide)[^\"\']*[\"\'][^>]*>(.*?)</span>', item, re.DOTALL)
        cat = ' '.join(re.sub(r'<[^>]+>', ' ', cat_m.group(1)).split()) if cat_m else ''
        link_m = re.search(r'<a\s+[^>]*href=[\"\']([^\"\']+)[\"\']', item)
        link = link_m.group(1) if link_m else ''
        if title:
            all_items.append({
                'site': 'yessbangla.top',
                'type': 'Delivered Project / Solution',
                'name': title,
                'category': f'Custom Solution ({cat})' if cat else 'Custom Solution',
                'platform': 'Web Solution',
                'url': link,
                'description': desc
            })

    # 2. YESSBD.COM Services & Ventures
    yessbd_services = [
        {
            'site': 'yessbd.com',
            'type': 'Core Digital Service',
            'name': 'Akash OTT',
            'category': 'Streaming & Media Platform',
            'platform': 'OTT Platform',
            'url': 'https://yessbd.com/ventures/9?type=Akash%20OTT',
            'description': 'A new Bangladeshi digital streaming platform launched by YESS Bangla Communications under Akash TV, bringing premium entertainment to screens nationwide.'
        },
        {
            'site': 'yessbd.com',
            'type': 'Core Digital Service',
            'name': 'Akash News',
            'category': 'Digital News Platform',
            'platform': 'Digital Media Portal & CMS',
            'url': 'https://yessbd.com/services',
            'description': 'A modern Bangladeshi news platform delivering real-time stories with a robust editorial CMS, editorial workflows, verified journalism, and multi-format delivery.'
        },
        {
            'site': 'yessbd.com',
            'type': 'Core Business Service',
            'name': 'YESS One Stop Solution',
            'category': 'Managed IT & Home Services',
            'platform': 'Managed Support Services',
            'url': 'https://yessbd.com/services',
            'description': 'Centralised technology, IT support, and home services (cleaning, electrical, plumbing, AC servicing) under one trusted roof.'
        },
        {
            'site': 'yessbd.com',
            'type': 'Core IT Service',
            'name': 'Web Development',
            'category': 'Engineering & Custom Software',
            'platform': 'Full-Stack Web Development',
            'url': 'https://yessbd.com/services',
            'description': 'Responsive frontend and backend engineering with PHP, Laravel, Node.js, and modern integrations for custom web applications and business portals.'
        },
        {
            'site': 'yessbd.com',
            'type': 'Core Design Service',
            'name': 'Web Design',
            'category': 'Design & UX',
            'platform': 'UI/UX & Branding',
            'url': 'https://yessbd.com/services',
            'description': 'Visually appealing, functional websites combining layout, colour, typography, brand-aligned UI design, UX prototyping, and mobile-first responsiveness.'
        },
        {
            'site': 'yessbd.com',
            'type': 'Core E-commerce Service',
            'name': 'Yess Bangla Shop',
            'category': 'E-Commerce Platform & Retail',
            'platform': 'E-Commerce Solution',
            'url': 'https://yessbd.com/services',
            'description': 'End-to-end commerce with web storefronts, mobile apps, secure payment gateways, inventory synchronization, and doorstep delivery.'
        }
    ]
    all_items.extend(yessbd_services)

    yessbd_ventures = [
        {
            'site': 'yessbd.com',
            'type': 'Venture / Service Marketplace',
            'name': 'Shondhaan',
            'category': 'Home & Professional Services',
            'platform': 'Digital Service Marketplace',
            'url': 'https://yessbd.com/ventures/5?type=Shondhaan',
            'description': 'Digital marketplace connecting customers with reliable home & professional service providers (AC repair, plumbing, cleaning, electrical, appliance repair) across Bangladesh. Website: https://shondhaan.com'
        },
        {
            'site': 'yessbd.com',
            'type': 'Venture / Marketplace',
            'name': 'Organic Haat',
            'category': 'Organic Marketplace & Agro',
            'platform': 'E-Commerce Marketplace',
            'url': 'https://yessbd.com/ventures/8?type=Organic%20Haat',
            'description': 'Verified organic produce, direct farm sourcing, cold-chain logistics, subscription deliveries, and lab-tested organic grocery. Website: https://organichaat.top'
        },
        {
            'site': 'yessbd.com',
            'type': 'Venture / Cloud Infrastructure',
            'name': 'Yess Host',
            'category': 'Hosting & Cloud Infrastructure',
            'platform': 'Cloud & Hosting Infrastructure',
            'url': 'https://yessbd.com/ventures/7?type=Yess%20Host',
            'description': 'High-performance NVMe shared hosting, domain registration, managed cloud servers, one-click stacks, and 24/7 technical support.'
        },
        {
            'site': 'yessbd.com',
            'type': 'Venture / Streaming Platform',
            'name': 'Akash OTT',
            'category': 'Entertainment & Streaming',
            'platform': 'Digital OTT Platform',
            'url': 'https://yessbd.com/ventures/9?type=Akash%20OTT',
            'description': 'Bangladeshi digital entertainment and TV streaming platform offering 24/7 content, original drama series, newsroom broadcasts, and brand-safe streaming. Website: https://akash.tv'
        },
        {
            'site': 'yessbd.com',
            'type': 'Venture / Software Division',
            'name': 'Yess Soft',
            'category': 'Software & IT Solutions',
            'platform': 'IT Solutions & Enterprise Software',
            'url': 'https://yessbd.com/ventures/10?type=Yess%20Soft',
            'description': 'Full-service IT solutions, web development, mobile apps, enterprise ERP, and cloud systems with senior-only delivery pods. Website: https://yessbangla.top'
        },
        {
            'site': 'yessbd.com',
            'type': 'Venture / Event Management',
            'name': 'Yess Event',
            'category': 'Event Management & Production',
            'platform': 'Event Production & Management',
            'url': 'https://yessbd.com/ventures/6?type=Yess%20Event',
            'description': 'Full-service event management and technical production for corporate conferences, concerts, weddings, and live events with owned sound and lighting equipment.'
        }
    ]
    all_items.extend(yessbd_ventures)

    external_portals = [
        {
            'site': 'yessbd.com',
            'type': 'Associated Venture Portal',
            'name': 'Shondhaan Portal',
            'category': 'Home Service Provider',
            'platform': 'Service Platform',
            'url': 'https://shondhaan.com',
            'description': 'External portal for Shondhaan home and professional services provider.'
        },
        {
            'site': 'yessbd.com',
            'type': 'Associated Venture Portal',
            'name': 'Organic Haat Portal',
            'category': 'Organic Marketplace',
            'platform': 'E-commerce Platform',
            'url': 'https://organichaat.top',
            'description': 'External portal for Organic Haat organic grocery and food marketplace.'
        },
        {
            'site': 'yessbd.com',
            'type': 'Associated Venture Portal',
            'name': 'Akash TV Portal',
            'category': 'OTT & News Streaming',
            'platform': 'Media Portal',
            'url': 'https://akash.tv',
            'description': 'Official portal for Akash TV streaming entertainment and news platform.'
        },
        {
            'site': 'yessbd.com',
            'type': 'Associated Venture Portal',
            'name': 'Yess Bangla Software Portal',
            'category': 'Software & IT Solutions',
            'platform': 'IT Portal',
            'url': 'https://yessbangla.top',
            'description': 'Official portal showcasing software solutions, ready-made management systems, and interactive demos.'
        }
    ]
    all_items.extend(external_portals)

    # Save to JSON
    with open('scraped_products_and_services.json', 'w', encoding='utf-8') as f:
        json.dump(all_items, f, indent=2, ensure_ascii=False)

    # Save to CSV
    with open('scraped_products_and_services.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['site', 'type', 'name', 'category', 'platform', 'url', 'description'])
        writer.writeheader()
        writer.writerows(all_items)

    # Save to Markdown
    doc = []
    doc.append('# Comprehensive Directory: Products & Services of Yess Bangla')
    doc.append('**Target Websites:**')
    doc.append('- [https://yessbd.com](https://yessbd.com) — *Yess Bangla Private Limited (Corporate & Venture Portal)*')
    doc.append('- [https://yessbangla.top](https://yessbangla.top) — *Yess Bangla IT Solutions (Software & Demo Hub)*\n')
    doc.append('**Date of Crawl:** September 26, 2026')
    doc.append(f'**Total Offerings Cataloged:** {len(all_items)}\n')
    doc.append('---\n')
    doc.append('## Executive Summary')
    doc.append('This document represents the complete scraped inventory of products, services, interactive demos, corporate ventures, and client projects offered across **Yess Bangla Private Limited** (`yessbd.com`) and its dedicated software solutions showcase (`yessbangla.top`).\n')
    doc.append('### Key Contact & Organization Details')
    doc.append('- **Headquarters:** Block-A, Road-3, House-127 (Green View), 1st Floor, Mirpur-12, Dhaka-1216, Bangladesh')
    doc.append('- **Email:** [yessbangla.bd@gmail.com](mailto:yessbangla.bd@gmail.com)')
    doc.append('- **Phone / WhatsApp:** [+880 1805-464343](https://wa.me/881805464343) / [+880 1805-464341](tel:+8801805464341)')
    doc.append('- **Official Facebook:** [facebook.com/yessbanglaltd](https://www.facebook.com/yessbanglaltd)\n')
    doc.append('---\n')
    doc.append('## 1. Corporate Services (yessbd.com)')
    doc.append('| Service Name | Category | Delivery Mode | Link | Description |')
    doc.append('|---|---|---|---|---|')
    for it in all_items:
        if it['site'] == 'yessbd.com' and it['type'] in ['Core Digital Service', 'Core Business Service', 'Core IT Service', 'Core Design Service', 'Core E-commerce Service']:
            doc.append(f"| **{it['name']}** | {it['category']} | {it['platform']} | [{it['url']}]({it['url']}) | {it['description']} |")
    doc.append('\n## 2. Business Ventures & Subsidiaries (yessbd.com)')
    doc.append('| Venture Name | Category | Primary Focus | Venture Page | Description / Value Proposition |')
    doc.append('|---|---|---|---|---|')
    for it in all_items:
        if it['site'] == 'yessbd.com' and it['type'].startswith('Venture'):
            doc.append(f"| **{it['name']}** | {it['category']} | {it['platform']} | [{it['url']}]({it['url']}) | {it['description']} |")
    doc.append('\n## 3. Interactive Software Product Demos (yessbangla.top)')
    doc.append('The software division showcases 48 live interactive application demos across multiple sectors:\n')
    cat_mapping = [
        ('Entertainment & Media', ['Entertainment']),
        ('E-Commerce & Online Stores', ['Ecommerce']),
        ('News Portals & Digital E-Papers', ['News']),
        ('Logistics, Courier & Delivery', ['Business']),
        ('Healthcare, Clinics & Pharmacies', ['Healthcare']),
        ('Retail, POS & Invoicing', ['Retail']),
        ('Enterprise & Legal ERP', ['Enterprise']),
        ('Education & School Management', ['Education']),
        ('Travel, Tourism & Booking', ['Travel']),
        ('Finance & Microfinance', ['Finance']),
    ]
    products = [it for it in all_items if it['site'] == 'yessbangla.top' and it['type'] == 'Software Product / Demo']
    for section_title, target_cats in cat_mapping:
        sec_items = [p for p in products if p['category'] in target_cats]
        if sec_items:
            doc.append(f'### {section_title}')
            doc.append('| # | Product Name | Type | Live Demo Link | Description |')
            doc.append('|---|---|---|---|---|')
            for idx, p in enumerate(sec_items, 1):
                doc.append(f"| {idx} | **{p['name']}** | {p['platform']} | [{p['url']}]({p['url']}) | {p['description']} |")
            doc.append('')
    doc.append('## 4. Enterprise Software Services (yessbangla.top)')
    doc.append('| System Name | Domain | Architecture | Access Link | Scope & Purpose |')
    doc.append('|---|---|---|---|---|')
    for it in all_items:
        if it['site'] == 'yessbangla.top' and it['type'] == 'Software Service / System Solution':
            link_str = f"[{it['url']}]({it['url']})" if it['url'] != '#' and not it['url'].endswith('#contact') else '[Contact for Inquiry](https://yessbangla.top/#contact)'
            doc.append(f"| **{it['name']}** | {it['category']} | {it['platform']} | {link_str} | {it['description']} |")
    doc.append('\n## 5. Delivered Client Projects & Case Studies (yessbangla.top)')
    doc.append('| Project / Product | Sector | Tech Stack | Live Site Link | Overview |')
    doc.append('|---|---|---|---|---|')
    for it in all_items:
        if it['site'] == 'yessbangla.top' and it['type'] in ['Featured Product / Project', 'Delivered Project / Solution']:
            doc.append(f"| **{it['name']}** | {it['category']} | {it['platform']} | [{it['url']}]({it['url']}) | {it['description']} |")
    doc.append('\n## 6. Associated Ecosystem Portals')
    doc.append('| Entity / Portal | Sector | Direct URL | Description |')
    doc.append('|---|---|---|---|')
    for it in all_items:
        if it['site'] == 'yessbd.com' and it['type'] == 'Associated Venture Portal':
            doc.append(f"| **{it['name']}** | {it['category']} | [{it['url']}]({it['url']}) | {it['description']} |")
    doc.append('\n## 7. Industry Verticals Served')
    doc.append('As detailed on [yessbd.com/industries](https://yessbd.com/industries), solutions are tailored for:')
    doc.append('- **Media & Broadcasting:** Cloud playout, OTT infrastructure, editorial CMS, real-time streaming.')
    doc.append('- **Retail & E-commerce:** Point-of-sale software, multi-vendor marketplaces, inventory synchronization, mobile commerce.')
    doc.append('- **Education:** School management ERPs, student grading systems, fees and admissions processing.')
    doc.append('- **Healthcare:** Clinic operations, hospital management systems (HMS), doctor chambers, pharmacy retail.')
    doc.append('- **Banking & Finance:** Microfinance, loan installment ledgers, multi-channel payment integrations.')
    doc.append('- **Manufacturing:** Garments ERP, supply chain tracking, production scheduling.')
    doc.append('- **Logistics & Supply Chain:** Courier parcel delivery tracking, merchant management, automated dispatch.')
    doc.append('- **Government & NGOs:** Custom public sector portals, compliance software, records management.\n')
    doc.append('---\n**Exported Files:**')
    doc.append('- JSON format: `scraped_products_and_services.json`')
    doc.append('- CSV format: `scraped_products_and_services.csv`')

    with open('SCRAPED_PRODUCTS_AND_SERVICES.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(doc))

    print(f'Successfully compiled {len(all_items)} products and services to JSON, CSV, and Markdown.')

if __name__ == '__main__':
    main()

