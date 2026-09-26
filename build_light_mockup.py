#!/usr/bin/env python3
import json
import os

with open('scraped_products_and_services.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Extract subsets
demos = [it for it in items if it['site'] == 'yessbangla.top' and it['type'] == 'Software Product / Demo']
ventures_list = [it for it in items if it['site'] == 'yessbd.com' and it['type'].startswith('Venture')]
services_list = [it for it in items if it['site'] == 'yessbd.com' and it['type'].startswith('Core')]
projects_list = [it for it in items if it['site'] == 'yessbangla.top' and it['type'] in ['Featured Product / Project', 'Delivered Project / Solution']]

# Map image filenames
demo_img_map = {
    'GoFlix-OTT': 'assets/yessbangla/demos/goflix.png',
    'Shopix (Ecommerce Demo-1)': 'assets/yessbangla/demos/ecom1.JPG',
    'GadgetBD (Ecommerce Demo-2)': 'assets/yessbangla/demos/ecom2.png',
    'OrganicMarket (Ecommerce Demo-3)': 'assets/yessbangla/demos/ecom3.png',
    'BoiBazar (Ecommerce Demo-4)': 'assets/yessbangla/demos/ecom4.png',
    'Chuijhal (Ecommerce Demo-5)': 'assets/yessbangla/demos/ecom5.png',
    'yFashion (Ecommerce Demo-6)': 'assets/yessbangla/demos/ecom6.JPG',
    'GlowMart (Ecommerce Demo-7)': 'assets/yessbangla/demos/ecom7.JPG',
    'Femina (Ecommerce Demo-8)': 'assets/yessbangla/demos/ecom8.JPG',
    'Shopora (Ecommerce Demo-9)': 'assets/yessbangla/demos/ecom9.JPG',
    'Ecommerce Demo-10': 'assets/yessbangla/demos/ecom8.png',
    'News Portal Demo-1': 'assets/yessbangla/demos/news1.JPG',
    'News Portal Demo-2': 'assets/yessbangla/demos/news2.JPG',
    'News Portal Demo-3': 'assets/yessbangla/demos/news3.JPG',
    'News Portal Demo-4': 'assets/yessbangla/demos/news4.png',
    'News Portal Demo-5': 'assets/yessbangla/demos/news5.png',
    'E-Paper (Demo-1)': 'assets/yessbangla/demos/epaper-1.png',
    'E-Paper (Demo-2)': 'assets/yessbangla/demos/epaper-2.png',
    'Digital Mart': 'assets/yessbangla/demos/digital_mart.png',
    'yCourier': 'assets/yessbangla/demos/y_courier.png',
    'Swift Courier Service': 'assets/yessbangla/demos/swift-courier.png',
    'Shiply Courier Service': 'assets/yessbangla/demos/shiply.png',
    'Surjo Courier Service': 'assets/yessbangla/demos/shurjo.png',
    'yPharma': 'assets/yessbangla/demos/ypharma.png',
    'yClinic': 'assets/yessbangla/demos/clinic.png',
    'yessDoctor': 'assets/yessbangla/demos/yessDoctor.png',
    'yessHMS': 'assets/yessbangla/demos/yesshms.png',
    'YessHR': 'assets/yessbangla/demos/yesshr.png',
    'ySales': 'assets/yessbangla/demos/y_salse.png',
    'YessLaw': 'assets/yessbangla/demos/yess_law.png',
    'GurmentsERP': 'assets/yessbangla/demos/y_garments.png',
    'YessEnterprise': 'assets/yessbangla/demos/yessenterprise.png',
    'YessStore': 'assets/yessbangla/demos/yess_store.png',
    'yInvoice': 'assets/yessbangla/demos/yinvoice.JPG',
    'YessPOS': 'assets/yessbangla/demos/yess_pos.png',
    'YessPOS-1': 'assets/yessbangla/demos/POS1.JPG',
    'YessPOS-2': 'assets/yessbangla/demos/pos2.JPG',
    'SalsePOS': 'assets/yessbangla/demos/salsepos.png',
    'POS Software': 'assets/yessbangla/demos/pos.png',
    'CRM System': 'assets/yessbangla/demos/crm.png',
    'EasyCRM': 'assets/yessbangla/demos/crm1.png',
    'Hospital Management System': 'assets/yessbangla/demos/ehospital.png',
    'School Management System': 'assets/yessbangla/demos/yschool.png',
    'Travel Agency': 'assets/yessbangla/demos/yesstravel.png',
    'Booking Core (Booking Management)': 'assets/yessbangla/demos/booking.png',
    'Booking Management System': 'assets/yessbangla/demos/yessbooking.png',
    'Loan Management System': 'assets/yessbangla/demos/loan1.png'
}

venture_img_map = {
    'Shondhaan': 'assets/yessbd/ventures/shondhaan-full.png',
    'Organic Haat': 'assets/yessbd/ventures/organic-haat.png',
    'Akash OTT': 'assets/yessbangla/projects/akash_desktop.png',
    'Yess Soft': 'assets/yessbd/ventures/yesssoft.png',
    'Yess Host': 'assets/yessbd/logos/logo_6a8975c2b891b.png',
    'Yess Event': 'assets/yessbd/heroes/hero_6a89646fd72ff.jpg'
}

project_img_map = {
    'Akash.tv': 'assets/yessbangla/projects/akash_desktop.png',
    'Yess Dinning Lounge': 'assets/yessbangla/projects/table.png',
    'YessBangla Shop': 'assets/yessbangla/projects/shop.png',
    'Ascension Accounting': 'assets/yessbangla/projects/ascension.png',
    'Coast Bangladesh Limited (CBL)': 'assets/yessbangla/projects/cbl.png',
    'BharaGhor': 'assets/yessbangla/projects/bharaghor.png'
}

team_members = [
    {'name': 'Sadia', 'role': 'Lead UI/UX Designer', 'img': 'assets/yessbangla/teams/sadia.png'},
    {'name': 'Tanvi', 'role': 'Senior Frontend Engineer', 'img': 'assets/yessbangla/teams/tanvi.png'},
    {'name': 'Mohima', 'role': 'Full-Stack Developer', 'img': 'assets/yessbangla/teams/mohima.png'},
    {'name': 'Sumaiya', 'role': 'Product Manager', 'img': 'assets/yessbangla/teams/sumaiya.png'},
    {'name': 'Hiya', 'role': 'QA & Compliance Lead', 'img': 'assets/yessbangla/teams/hiya.png'},
    {'name': 'Ovijit', 'role': 'DevOps & Cloud Architect', 'img': 'assets/yessbangla/teams/ovijit.jpeg'},
    {'name': 'NI Tushar', 'role': 'Senior Software Architect', 'img': 'assets/yessbangla/teams/NI_Tushar.png'}
]

html = []
html.append('''<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Yess Bangla - Modern Next.js 16 Redesign (Light Theme)</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @keyframes floatSlow {
      0%, 100% { transform: translateY(0px); }
      50% { transform: translateY(-8px); }
    }
    @keyframes pulseGlow {
      0%, 100% { opacity: 0.3; transform: scale(1); }
      50% { opacity: 0.6; transform: scale(1.08); }
    }
    @keyframes shimmer {
      0% { background-position: -200% 0; }
      100% { background-position: 200% 0; }
    }
    .animate-float {
      animation: floatSlow 4s ease-in-out infinite;
    }
    .animate-glow {
      animation: pulseGlow 6s ease-in-out infinite;
    }
    .bg-grid-pattern {
      background-image: radial-gradient(#cbd5e1 1px, transparent 1px);
      background-size: 28px 28px;
    }
    .custom-scroll::-webkit-scrollbar {
      width: 6px;
    }
    .custom-scroll::-webkit-scrollbar-thumb {
      background: #10b981;
      border-radius: 9999px;
    }
    .glass-card {
      background: rgba(255, 255, 255, 0.85);
      backdrop-filter: blur(12px);
    }
  </style>
</head>
<body class="bg-white text-slate-800 antialiased font-sans custom-scroll selection:bg-emerald-500 selection:text-white">

  <!-- Top Controller Toolbar -->
  <div class="sticky top-0 z-50 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-sm px-4 py-2.5 flex flex-wrap items-center justify-between gap-3">
    <div class="flex items-center gap-3">
      <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center text-white font-extrabold shadow-md shadow-emerald-500/20">
        YB
      </div>
      <div>
        <div class="text-[11px] font-bold text-emerald-600 uppercase tracking-wider flex items-center gap-1.5">
          <span class="w-2 h-2 rounded-full bg-emerald-500 animate-ping"></span>
          Live Light Theme Redesign
        </div>
        <div class="text-sm font-extrabold text-slate-900">
          Yess Bangla Conglomerate & Venture Studio
        </div>
      </div>
    </div>

    <!-- Quick Navigation Pills -->
    <div class="hidden md:flex items-center gap-1.5 bg-slate-100 p-1 rounded-xl text-xs font-semibold text-slate-600">
      <a href="#hero" class="px-3 py-1.5 rounded-lg hover:bg-white hover:text-emerald-700 hover:shadow-sm transition">Hero</a>
      <a href="#ventures" class="px-3 py-1.5 rounded-lg hover:bg-white hover:text-emerald-700 hover:shadow-sm transition">6 Ventures</a>
      <a href="#demos" class="px-3 py-1.5 rounded-lg bg-emerald-600 text-white shadow-sm transition">48 Software Demos</a>
      <a href="#projects" class="px-3 py-1.5 rounded-lg hover:bg-white hover:text-emerald-700 hover:shadow-sm transition">Client Portfolios</a>
      <a href="#process" class="px-3 py-1.5 rounded-lg hover:bg-white hover:text-emerald-700 hover:shadow-sm transition">Roadmap</a>
      <a href="#team" class="px-3 py-1.5 rounded-lg hover:bg-white hover:text-emerald-700 hover:shadow-sm transition">Team</a>
      <a href="#contact" class="px-3 py-1.5 rounded-lg hover:bg-white hover:text-emerald-700 hover:shadow-sm transition">Contact</a>
    </div>

    <div class="flex items-center gap-2">
      <button onclick="document.getElementById('contact').scrollIntoView({behavior: 'smooth'})" class="text-xs bg-emerald-600 hover:bg-emerald-700 text-white font-bold px-4 py-2 rounded-xl shadow-md shadow-emerald-600/20 transition-all hover:scale-[1.02]">
        Book Consultation
      </button>
    </div>
  </div>

  <!-- Announcement Bar -->
  <div class="bg-gradient-to-r from-emerald-50 via-teal-50 to-emerald-50 border-b border-emerald-100 py-2.5 px-4 text-center text-xs text-slate-700">
    <span class="inline-flex items-center gap-1.5 text-emerald-700 font-bold">
      <span class="w-2 h-2 rounded-full bg-emerald-500"></span>
      Portfolio Launch v16.2:
    </span>
    Complete unified ecosystem bringing together 6 Corporate Ventures, 48 Interactive Software Demos & Client Portfolios.
    <a href="#ventures" class="text-emerald-700 hover:text-emerald-800 font-bold underline ml-1">Explore Ventures &rarr;</a>
  </div>

  <!-- Main Navigation Header -->
  <header class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-5 flex items-center justify-between">
    <div class="flex items-center gap-3">
      <img src="assets/yessbangla/logos/logo.png" alt="Yess Bangla Logo" class="h-10 w-auto object-contain" onerror="this.style.display='none'"/>
      <div>
        <div class="text-xl font-black text-slate-900 tracking-tight flex items-center gap-1">
          <span class="text-emerald-600">YESS</span>BANGLA
        </div>
        <div class="text-[10px] uppercase font-bold tracking-widest text-slate-400">Where Solution Begins</div>
      </div>
    </div>

    <nav class="hidden lg:flex items-center gap-8 text-sm font-semibold text-slate-600">
      <a href="#ventures" class="hover:text-emerald-600 transition flex items-center gap-1">
        Ventures
        <span class="text-[10px] bg-emerald-100 text-emerald-800 px-1.5 py-0.5 rounded-full font-bold">6</span>
      </a>
      <a href="#demos" class="hover:text-emerald-600 transition flex items-center gap-1">
        Software Hub
        <span class="text-[10px] bg-amber-100 text-amber-800 px-1.5 py-0.5 rounded-full font-bold">48 Demos</span>
      </a>
      <a href="#capabilities" class="hover:text-emerald-600 transition">Services</a>
      <a href="#projects" class="hover:text-emerald-600 transition">Case Studies</a>
      <a href="#process" class="hover:text-emerald-600 transition">Our Process</a>
      <a href="#team" class="hover:text-emerald-600 transition">Leadership</a>
    </nav>

    <div class="flex items-center gap-3">
      <a href="https://wa.me/881805464343" target="_blank" class="hidden sm:inline-flex items-center gap-1.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 px-3.5 py-2 rounded-xl transition">
        <span>💬</span> WhatsApp
      </a>
      <a href="#contact" class="text-xs font-bold text-white bg-slate-900 hover:bg-emerald-600 px-4 py-2 rounded-xl shadow-sm transition">
        Get In Touch
      </a>
    </div>
  </header>

  <!-- ================= HERO SECTION ================= -->
  <section id="hero" class="relative pt-12 pb-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto overflow-hidden bg-grid-pattern">
    <!-- Ambient Light Glow Orbs -->
    <div class="absolute top-10 left-1/2 -translate-x-1/2 w-[700px] h-[400px] bg-gradient-to-r from-emerald-200/40 via-teal-200/30 to-cyan-200/30 blur-[130px] rounded-full pointer-events-none animate-glow"></div>

    <div class="relative z-10 text-center max-w-4xl mx-auto">
      
      <!-- Pill Badge -->
      <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-emerald-200 bg-emerald-50/80 text-emerald-800 text-xs font-bold uppercase tracking-wider mb-8 shadow-sm">
        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
        Enterprise IT Conglomerate & Venture Studio
      </div>

      <!-- Main Headline -->
      <h1 class="text-4xl sm:text-6xl lg:text-7xl font-extrabold text-slate-900 tracking-tight leading-[1.1] mb-6">
        Engineering Scalable Software. <br class="hidden sm:inline"/>
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 via-teal-600 to-cyan-600">
          Transforming Modern Ventures.
        </span>
      </h1>

      <p class="text-lg sm:text-xl text-slate-600 max-w-2xl mx-auto mb-10 leading-relaxed font-normal">
        A full-service business consulting and IT solutions powerhouse in Bangladesh. Powering nationwide streaming, organic marketplaces, high-speed cloud infrastructure, and <strong>48+ ready-to-deploy enterprise SaaS solutions</strong>.
      </p>

      <!-- Action Buttons -->
      <div class="flex flex-wrap items-center justify-center gap-4 mb-16">
        <a href="#demos" class="px-8 py-4 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm shadow-xl shadow-emerald-600/25 transition-all hover:scale-[1.02] flex items-center gap-2">
          <span>🚀</span> Explore 48+ Interactive Demos
        </a>
        <a href="#ventures" class="px-7 py-4 rounded-2xl bg-white border border-slate-200 hover:border-emerald-300 text-slate-800 font-bold text-sm shadow-sm hover:shadow-md transition-all flex items-center gap-2">
          Discover Our 6 Ventures &rarr;
        </a>
      </div>

      <!-- Live Metrics Strip -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4 p-6 rounded-3xl bg-white/90 backdrop-blur-xl border border-slate-200 shadow-[0_8px_30px_rgb(0,0,0,0.04)]">
        <div class="p-3 text-center border-r border-slate-100 last:border-0">
          <div class="text-3xl sm:text-4xl font-black text-emerald-600">6</div>
          <div class="text-xs font-semibold text-slate-500 mt-1 uppercase tracking-wider">Independent Ventures</div>
        </div>
        <div class="p-3 text-center border-r border-slate-100 last:border-0">
          <div class="text-3xl sm:text-4xl font-black text-slate-900">48+</div>
          <div class="text-xs font-semibold text-slate-500 mt-1 uppercase tracking-wider">Software Demos</div>
        </div>
        <div class="p-3 text-center border-r border-slate-100 last:border-0">
          <div class="text-3xl sm:text-4xl font-black text-emerald-600">600+</div>
          <div class="text-xs font-semibold text-slate-500 mt-1 uppercase tracking-wider">Satisfied Clients</div>
        </div>
        <div class="p-3 text-center">
          <div class="text-3xl sm:text-4xl font-black text-slate-900">100%</div>
          <div class="text-xs font-semibold text-slate-500 mt-1 uppercase tracking-wider">Delivery Success</div>
        </div>
      </div>
    </div>

    <!-- Hero Visual Frame with Real Mockup Images -->
    <div class="mt-16 max-w-5xl mx-auto rounded-3xl border border-slate-200 bg-white p-3 sm:p-5 shadow-2xl relative">
      <div class="flex items-center justify-between pb-3 px-3 border-b border-slate-100 mb-4">
        <div class="flex items-center gap-2">
          <div class="flex gap-1.5">
            <span class="w-3 h-3 rounded-full bg-rose-400"></span>
            <span class="w-3 h-3 rounded-full bg-amber-400"></span>
            <span class="w-3 h-3 rounded-full bg-emerald-400"></span>
          </div>
          <span class="ml-2 text-xs font-mono text-slate-400">yessbd.com/ecosystem-showcase</span>
        </div>
        <div class="text-xs font-bold text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-100">
          ✨ Next.js 16 App Router
        </div>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
        <!-- Mockup 1: Akash Desktop -->
        <div class="group relative rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 p-2 hover:border-emerald-300 transition-all shadow-sm">
          <div class="h-44 w-full rounded-xl overflow-hidden bg-slate-200 relative">
            <img src="assets/yessbangla/projects/akash_desktop.png" alt="Akash.tv Preview" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/600x400/e2e8f0/0f172a?text=Akash.tv+Platform'"/>
          </div>
          <div class="p-3">
            <div class="flex items-center justify-between text-xs font-bold text-emerald-600 mb-1">
              <span>STREAMING VENTURE</span>
              <span>akash.tv</span>
            </div>
            <h4 class="font-extrabold text-sm text-slate-900">Akash.tv Digital Platform</h4>
            <p class="text-xs text-slate-500 mt-1">High-concurrency video playout & editorial CMS.</p>
          </div>
        </div>

        <!-- Mockup 2: Shopix Ecommerce -->
        <div class="group relative rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 p-2 hover:border-emerald-300 transition-all shadow-sm">
          <div class="h-44 w-full rounded-xl overflow-hidden bg-slate-200 relative">
            <img src="assets/yessbangla/demos/ecom1.JPG" alt="Shopix Ecommerce Preview" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/600x400/e2e8f0/0f172a?text=Shopix+Ecommerce'"/>
          </div>
          <div class="p-3">
            <div class="flex items-center justify-between text-xs font-bold text-teal-600 mb-1">
              <span>ECOMMERCE DEMO</span>
              <span>Demo #1</span>
            </div>
            <h4 class="font-extrabold text-sm text-slate-900">Shopix E-Commerce Suite</h4>
            <p class="text-xs text-slate-500 mt-1">Order tracking, courier dispatch & payment gateway.</p>
          </div>
        </div>

        <!-- Mockup 3: YessPOS Retail -->
        <div class="group relative rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 p-2 hover:border-emerald-300 transition-all shadow-sm">
          <div class="h-44 w-full rounded-xl overflow-hidden bg-slate-200 relative">
            <img src="assets/yessbangla/demos/yess_pos.png" alt="YessPOS Preview" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/600x400/e2e8f0/0f172a?text=YessPOS+Retail'"/>
          </div>
          <div class="p-3">
            <div class="flex items-center justify-between text-xs font-bold text-amber-600 mb-1">
              <span>RETAIL POS</span>
              <span>Cloud SaaS</span>
            </div>
            <h4 class="font-extrabold text-sm text-slate-900">YessPOS Smart Terminal</h4>
            <p class="text-xs text-slate-500 mt-1">Barcode scanning, stock ledgers & cashier registers.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= SECTION: 6 CORPORATE VENTURES ================= -->
  <section id="ventures" class="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-16">
      <div>
        <div class="inline-block text-xs font-extrabold text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
          Conglomerate Subsidiaries
        </div>
        <h2 class="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">The 6 Core Ventures</h2>
      </div>
      <p class="text-sm text-slate-500 max-w-md mt-4 md:mt-0 font-medium">
        Our specialized business units addressing mission-critical markets in Bangladesh, backed by shared IT infrastructure and leadership.
      </p>
    </div>

    <!-- Bento Grid with Images and Animations -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      
      <!-- Venture 1: Shondhaan (Span 2) -->
      <div class="md:col-span-2 group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-sm hover:shadow-2xl transition-all duration-300 relative overflow-hidden flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 text-xs font-bold">
              Home & Professional Services Marketplace
            </span>
            <a href="https://shondhaan.com" target="_blank" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 hover:underline flex items-center gap-1">
              shondhaan.com &rarr;
            </a>
          </div>
          <h3 class="text-3xl font-extrabold text-slate-900 mb-3">Shondhaan</h3>
          <p class="text-sm text-slate-600 leading-relaxed mb-6 max-w-xl">
            A nationwide service marketplace connecting households and businesses with verified electricians, AC repair technicians, plumbers, cleaners, and appliance specialists.
          </p>
        </div>

        <div class="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-56 mb-6">
          <img src="assets/yessbd/ventures/shondhaan-full.png" alt="Shondhaan" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/800x400/ecfdf5/065f46?text=Shondhaan+Marketplace'"/>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t border-slate-100 text-xs text-slate-600">
          <div><strong class="text-slate-900 block text-sm font-bold">500+</strong> Verified Pros</div>
          <div><strong class="text-slate-900 block text-sm font-bold">4.9 / 5</strong> Quality Rating</div>
          <div><strong class="text-slate-900 block text-sm font-bold">Fast</strong> Real-time Booking</div>
          <div><strong class="text-slate-900 block text-sm font-bold">Dhaka</strong> Nationwide Next</div>
        </div>
      </div>

      <!-- Venture 2: Organic Haat -->
      <div class="group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-sm hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="px-3 py-1 rounded-full bg-teal-50 text-teal-700 border border-teal-200 text-xs font-bold">
              Organic Agro & Food
            </span>
            <a href="https://organichaat.top" target="_blank" class="text-xs font-bold text-teal-600 hover:underline">organichaat.top &rarr;</a>
          </div>
          <h3 class="text-2xl font-extrabold text-slate-900 mb-2">Organic Haat</h3>
          <p class="text-xs text-slate-600 leading-relaxed mb-4">
            Direct-from-farm organic groceries, chemical-free cold-chain produce, and weekly doorstep subscription deliveries.
          </p>
        </div>

        <div class="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-44 mb-4">
          <img src="assets/yessbd/ventures/organic-haat.png" alt="Organic Haat" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/400x300/f0fdf4/166534?text=Organic+Haat'"/>
        </div>

        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
          <span>🌱 100% Lab Tested</span>
          <span>🚚 Cold-Chain Logistics</span>
        </div>
      </div>

      <!-- Venture 3: Akash OTT -->
      <div class="group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-sm hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="px-3 py-1 rounded-full bg-cyan-50 text-cyan-700 border border-cyan-200 text-xs font-bold">
              Digital OTT & Broadcast
            </span>
            <a href="https://akash.tv" target="_blank" class="text-xs font-bold text-cyan-600 hover:underline">akash.tv &rarr;</a>
          </div>
          <h3 class="text-2xl font-extrabold text-slate-900 mb-2">Akash OTT</h3>
          <p class="text-xs text-slate-600 leading-relaxed mb-4">
            24/7 digital streaming platform bringing premium Bangladeshi movies, original drama serials, and real-time editorial news broadcasting.
          </p>
        </div>

        <div class="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-44 mb-4">
          <img src="assets/yessbangla/projects/akash_desktop.png" alt="Akash OTT" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/400x300/ecfeff/155e75?text=Akash+OTT'"/>
        </div>

        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
          <span>📺 HD Video Streaming</span>
          <span>📰 Real-Time News CMS</span>
        </div>
      </div>

      <!-- Venture 4: Yess Soft (Span 2) -->
      <div class="md:col-span-2 group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-sm hover:shadow-2xl transition-all duration-300 relative overflow-hidden flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 text-xs font-bold">
              Enterprise Software & SaaS Wing
            </span>
            <a href="https://yessbangla.top" target="_blank" class="text-xs font-bold text-emerald-600 hover:underline">yessbangla.top &rarr;</a>
          </div>
          <h3 class="text-3xl font-extrabold text-slate-900 mb-2">Yess Soft</h3>
          <p class="text-sm text-slate-600 leading-relaxed mb-6 max-w-xl">
            Custom software engineering pods developing large-scale ERPs, sales CRMs, hospital systems, courier dispatch networks, and 48 ready-made management products.
          </p>
        </div>

        <div class="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-56 mb-6">
          <img src="assets/yessbd/ventures/yesssoft.png" alt="Yess Soft" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/800x400/ecfdf5/047857?text=Yess+Soft+IT+Solutions'"/>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t border-slate-100 text-xs text-slate-600">
          <div><strong class="text-slate-900 block text-sm font-bold">Next.js 16</strong> Frontend</div>
          <div><strong class="text-slate-900 block text-sm font-bold">Laravel & Node</strong> Backends</div>
          <div><strong class="text-slate-900 block text-sm font-bold">48 Demos</strong> Ready to Test</div>
          <div><strong class="text-slate-900 block text-sm font-bold">DevOps</strong> AWS Cloud</div>
        </div>
      </div>

      <!-- Venture 5: Yess Host -->
      <div class="group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-sm hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="px-3 py-1 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-200 text-xs font-bold">
              Cloud Infrastructure
            </span>
            <span class="text-xs font-bold text-indigo-600">99.9% Uptime</span>
          </div>
          <h3 class="text-2xl font-extrabold text-slate-900 mb-2">Yess Host</h3>
          <p class="text-xs text-slate-600 leading-relaxed mb-4">
            High-speed NVMe shared hosting, business cloud servers, domain registration, and 24/7 human technical support.
          </p>
        </div>

        <div class="p-6 rounded-2xl bg-gradient-to-br from-indigo-50 to-slate-50 border border-indigo-100 text-center mb-4">
          <div class="text-3xl mb-2">⚡</div>
          <div class="text-sm font-bold text-slate-900">Pure NVMe SSD Storage</div>
          <div class="text-xs text-slate-500 mt-1">Free SSL & Daily Cloud Backups</div>
        </div>

        <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
          <span>🛡️ DDoS Protected</span>
          <span>🎧 24/7 Live Support</span>
        </div>
      </div>

      <!-- Venture 6: Yess Event -->
      <div class="md:col-span-2 group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-sm hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
        <div>
          <div class="flex items-center justify-between mb-4">
            <span class="px-3 py-1 rounded-full bg-amber-50 text-amber-700 border border-amber-200 text-xs font-bold">
              Event Management & Technical Production
            </span>
            <span class="text-xs font-bold text-amber-600">Full In-House AV</span>
          </div>
          <h3 class="text-3xl font-extrabold text-slate-900 mb-2">Yess Event</h3>
          <p class="text-sm text-slate-600 leading-relaxed mb-6 max-w-xl">
            Full-service corporate summits, national trade fairs, concerts, weddings, and live brand activations with owned sound and lighting equipment.
          </p>
        </div>

        <div class="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-52 mb-6">
          <img src="assets/yessbd/heroes/hero_6a89646fd72ff.jpg" alt="Yess Event Production" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/800x400/fffbeb/b45309?text=Yess+Event+Production'"/>
        </div>

        <div class="grid grid-cols-2 sm:grid-cols-3 gap-4 pt-4 border-t border-slate-100 text-xs text-slate-600">
          <div><strong class="text-slate-900 block text-sm font-bold">Conferences</strong> Corporate Summits</div>
          <div><strong class="text-slate-900 block text-sm font-bold">AV Staging</strong> Owned Gear</div>
          <div><strong class="text-slate-900 block text-sm font-bold">Turnkey</strong> Single Accountable Lead</div>
        </div>
      </div>

    </div>
  </section>

  <!-- ================= SECTION: 48-DEMO INTERACTIVE SOFTWARE HUB ================= -->
  <section id="demos" class="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
    <div class="text-center max-w-3xl mx-auto mb-12">
      <div class="inline-block text-xs font-extrabold text-amber-700 bg-amber-50 border border-amber-200 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
        Interactive Demo Gallery
      </div>
      <h2 class="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">48 Ready-to-Deploy Software Systems</h2>
      <p class="text-base text-slate-500 mt-3 font-normal">
        Test our pre-built software systems across 10 industries. Filter by category, test the UI, and launch live interactive demos.
      </p>

      <!-- Search Input -->
      <div class="mt-8 max-w-md mx-auto relative">
        <input type="text" id="demo-search" oninput="searchDemos()" placeholder="Search system (e.g., POS, Pharmacy, Courier, ERP)..." class="w-full px-5 py-3.5 pl-11 rounded-2xl bg-white border border-slate-200 text-sm text-slate-800 shadow-sm focus:outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20 transition"/>
        <svg class="w-5 h-5 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
      </div>
    </div>

    <!-- Category Tabs -->
    <div class="flex flex-wrap items-center justify-center gap-2 mb-12">
      <button onclick="filterCategory('all', this)" class="cat-pill active px-4 py-2 rounded-full text-xs font-bold bg-emerald-600 text-white shadow-sm transition">All (48)</button>
      <button onclick="filterCategory('Ecommerce', this)" class="cat-pill px-4 py-2 rounded-full text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 transition">E-Commerce (10)</button>
      <button onclick="filterCategory('Healthcare', this)" class="cat-pill px-4 py-2 rounded-full text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 transition">Healthcare & Clinic (5)</button>
      <button onclick="filterCategory('Retail', this)" class="cat-pill px-4 py-2 rounded-full text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 transition">POS & Retail (7)</button>
      <button onclick="filterCategory('Business', this)" class="cat-pill px-4 py-2 rounded-full text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 transition">Courier & CRM (8)</button>
      <button onclick="filterCategory('Enterprise', this)" class="cat-pill px-4 py-2 rounded-full text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 transition">ERP & Legal (4)</button>
      <button onclick="filterCategory('Education', this)" class="cat-pill px-4 py-2 rounded-full text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 transition">School Systems (2)</button>
      <button onclick="filterCategory('News', this)" class="cat-pill px-4 py-2 rounded-full text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 transition">News & E-Paper (7)</button>
      <button onclick="filterCategory('Travel', this)" class="cat-pill px-4 py-2 rounded-full text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 transition">Travel & Tour (3)</button>
      <button onclick="filterCategory('Finance', this)" class="cat-pill px-4 py-2 rounded-full text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 transition">Microfinance (1)</button>
    </div>

    <!-- Demos Grid (All 48 Items) -->
    <div id="demos-container" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
''')

# Populate all 48 software demos
for i, d in enumerate(demos, 1):
    img_src = demo_img_map.get(d['name'], 'assets/yessbangla/demos/ecom1.JPG')
    cat = d['category']
    title = d['name']
    desc = d['description']
    url = d['url']
    platform = d['platform']
    
    badge_color = {
        'Ecommerce': 'bg-emerald-50 text-emerald-700 border-emerald-200',
        'Healthcare': 'bg-rose-50 text-rose-700 border-rose-200',
        'Retail': 'bg-indigo-50 text-indigo-700 border-indigo-200',
        'Business': 'bg-amber-50 text-amber-700 border-amber-200',
        'Enterprise': 'bg-violet-50 text-violet-700 border-violet-200',
        'Education': 'bg-blue-50 text-blue-700 border-blue-200',
        'News': 'bg-slate-100 text-slate-700 border-slate-200',
        'Travel': 'bg-teal-50 text-teal-700 border-teal-200',
        'Finance': 'bg-emerald-50 text-emerald-700 border-emerald-200',
        'Entertainment': 'bg-cyan-50 text-cyan-700 border-cyan-200'
    }.get(cat, 'bg-slate-100 text-slate-700 border-slate-200')

    html.append(f'''
      <div class="demo-item group rounded-2xl bg-white border border-slate-200 hover:border-emerald-400 p-4 shadow-sm hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between" data-category="{cat}" data-title="{title.lower()}">
        <div>
          <!-- Thumbnail with hover zoom -->
          <div class="h-44 w-full rounded-xl overflow-hidden bg-slate-100 border border-slate-100 mb-3 relative">
            <img src="{img_src}" alt="{title}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/600x400/f8fafc/334155?text={title.replace(' ', '+')}'"/>
            <span class="absolute top-2.5 left-2.5 px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase border {badge_color} backdrop-blur-md">
              {cat}
            </span>
          </div>
          <div class="flex items-center justify-between text-[11px] text-slate-400 mb-1">
            <span class="font-semibold text-emerald-600">{platform}</span>
            <span>Demo #{i}</span>
          </div>
          <h4 class="font-extrabold text-base text-slate-900 group-hover:text-emerald-600 transition mb-1">{title}</h4>
          <p class="text-xs text-slate-500 line-clamp-2 leading-relaxed mb-4">{desc}</p>
        </div>

        <div class="pt-3 border-t border-slate-100 flex items-center justify-between">
          <a href="{url}" target="_blank" class="text-xs font-bold text-emerald-600 hover:text-emerald-700 flex items-center gap-1.5 hover:underline">
            <span>Launch Demo</span>
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
          </a>
          <button onclick="openDemoModal('{title}', '{cat}', '{img_src}', '{url}', '{desc}')" class="text-[11px] font-semibold text-slate-500 hover:text-slate-800 bg-slate-100 hover:bg-slate-200 px-2.5 py-1 rounded-lg transition">
            Preview Specs
          </button>
        </div>
      </div>
    ''')

html.append('''
    </div>
  </section>

  <!-- ================= SECTION: FEATURED CLIENT CASE STUDIES ================= -->
  <section id="projects" class="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-16">
      <div>
        <div class="inline-block text-xs font-extrabold text-cyan-700 bg-cyan-50 border border-cyan-200 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
          Delivered Client Work
        </div>
        <h2 class="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">Enterprise Client Case Studies</h2>
      </div>
      <p class="text-sm text-slate-500 max-w-md mt-4 md:mt-0 font-medium">
        Proven digital platforms engineered and deployed for industry leaders across Bangladesh.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
''')

for p in projects_list:
    pname = p['name']
    pcat = p['category']
    pimg = project_img_map.get(pname, 'assets/yessbangla/projects/akash_desktop.png')
    purl = p['url']
    pdesc = p['description']

    html.append(f'''
      <div class="group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-6 shadow-sm hover:shadow-xl transition-all duration-300 flex flex-col justify-between">
        <div>
          <div class="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-48 mb-4 relative">
            <img src="{pimg}" alt="{pname}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" onerror="this.src='https://placehold.co/600x400/e2e8f0/0f172a?text={pname}'"/>
          </div>
          <div class="text-[11px] font-bold text-cyan-600 uppercase tracking-wider mb-1">{pcat}</div>
          <h3 class="font-extrabold text-xl text-slate-900 mb-2">{pname}</h3>
          <p class="text-xs text-slate-600 leading-relaxed mb-4">{pdesc}</p>
        </div>
        <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
          <a href="{purl}" target="_blank" class="text-xs font-bold text-emerald-600 hover:underline flex items-center gap-1">
            Visit Live Platform &rarr;
          </a>
          <span class="text-[10px] font-mono bg-slate-100 text-slate-600 px-2 py-0.5 rounded">Production</span>
        </div>
      </div>
    ''')

html.append('''
    </div>
  </section>

  <!-- ================= SECTION: 4-STAGE DELIVERY ROADMAP ================= -->
  <section id="process" class="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
    <div class="text-center max-w-3xl mx-auto mb-16">
      <div class="inline-block text-xs font-extrabold text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
        Delivery Model
      </div>
      <h2 class="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">Our 4-Stage Execution Framework</h2>
      <p class="text-base text-slate-500 mt-3 font-normal">
        From the initial strategic blueprint to post-deployment 24/7 reliability.
      </p>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
      <div class="p-8 rounded-3xl bg-white border border-slate-200 hover:border-emerald-300 shadow-sm hover:shadow-md transition">
        <div class="text-4xl font-black text-emerald-600 mb-4">01</div>
        <h4 class="font-extrabold text-lg text-slate-900 mb-2">Discover & Audit</h4>
        <p class="text-xs text-slate-600 leading-relaxed">
          Deep discovery sessions to map operational bottlenecks, customer pain points, and business KPIs.
        </p>
      </div>
      <div class="p-8 rounded-3xl bg-white border border-slate-200 hover:border-emerald-300 shadow-sm hover:shadow-md transition">
        <div class="text-4xl font-black text-teal-600 mb-4">02</div>
        <h4 class="font-extrabold text-lg text-slate-900 mb-2">Architect & UX</h4>
        <p class="text-xs text-slate-600 leading-relaxed">
          Creating high-fidelity Figma design systems, database schemas, and microservice architectures.
        </p>
      </div>
      <div class="p-8 rounded-3xl bg-white border border-slate-200 hover:border-emerald-300 shadow-sm hover:shadow-md transition">
        <div class="text-4xl font-black text-cyan-600 mb-4">03</div>
        <h4 class="font-extrabold text-lg text-slate-900 mb-2">Build & Launch</h4>
        <p class="text-xs text-slate-600 leading-relaxed">
          Agile sprints with senior-only engineering pods, automated CI/CD pipelines, and security testing.
        </p>
      </div>
      <div class="p-8 rounded-3xl bg-white border border-slate-200 hover:border-emerald-300 shadow-sm hover:shadow-md transition">
        <div class="text-4xl font-black text-amber-600 mb-4">04</div>
        <h4 class="font-extrabold text-lg text-slate-900 mb-2">Scale & Support</h4>
        <p class="text-xs text-slate-600 leading-relaxed">
          Cloud performance monitoring, auto-scaling, and long-term feature evolution with dedicated SLA.
        </p>
      </div>
    </div>
  </section>

  <!-- ================= SECTION: LEADERSHIP & CORE TEAM ================= -->
  <section id="team" class="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
    <div class="flex flex-col md:flex-row md:items-end justify-between mb-16">
      <div>
        <div class="inline-block text-xs font-extrabold text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
          Our People
        </div>
        <h2 class="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">The Minds Behind Yess Bangla</h2>
      </div>
      <p class="text-sm text-slate-500 max-w-md mt-4 md:mt-0 font-medium">
        Senior engineers, UI/UX researchers, and project managers driving digital excellence across Bangladesh.
      </p>
    </div>

    <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-7 gap-4">
''')

for tm in team_members:
    tname = tm['name']
    trole = tm['role']
    timg = tm['img']
    html.append(f'''
      <div class="group text-center p-3 rounded-2xl bg-white border border-slate-200 hover:border-emerald-400 transition-all hover:shadow-md">
        <div class="w-20 h-20 mx-auto rounded-full overflow-hidden border-2 border-emerald-100 group-hover:border-emerald-500 transition mb-3 bg-slate-100">
          <img src="{timg}" alt="{tname}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" onerror="this.src='https://placehold.co/150x150/e2e8f0/047857?text={tname}'"/>
        </div>
        <h4 class="font-bold text-sm text-slate-900">{tname}</h4>
        <p class="text-[11px] text-slate-500 mt-0.5">{trole}</p>
      </div>
    ''')

html.append('''
    </div>
  </section>

  <!-- ================= SECTION: CONTACT & BRIEF REQUEST ================= -->
  <section id="contact" class="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
    <div class="p-8 sm:p-14 rounded-3xl bg-gradient-to-br from-slate-900 via-slate-800 to-emerald-950 text-white shadow-2xl grid grid-cols-1 lg:grid-cols-2 gap-12">
      <div>
        <span class="px-3.5 py-1 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-xs font-extrabold uppercase tracking-wider mb-4 inline-block">
          Let's Build Together
        </span>
        <h2 class="text-3xl sm:text-5xl font-black text-white tracking-tight mb-4 leading-tight">
          Ready to Scale Your Enterprise?
        </h2>
        <p class="text-sm text-slate-300 leading-relaxed mb-8 max-w-md">
          Whether you need a bespoke ERP solution, a high-converting web platform, or are looking to partner with our ventures — we respond within 24 hours.
        </p>

        <div class="space-y-4 text-xs text-slate-300 mb-10">
          <div class="flex items-start gap-3">
            <span class="text-emerald-400 text-base">📍</span>
            <div>
              <strong class="text-white block text-sm">Headquarters:</strong>
              Block-A, Road-3, House-127 (Green View), 1st Floor, Mirpur-12, Dhaka-1216, Bangladesh
            </div>
          </div>
          <div class="flex items-center gap-3">
            <span class="text-emerald-400 text-base">📞</span>
            <div>
              <strong class="text-white">Phone & WhatsApp:</strong>
              <a href="https://wa.me/881805464343" class="text-emerald-400 hover:underline ml-1">+880 1805-464343</a> / +880 1805-464341
            </div>
          </div>
          <div class="flex items-center gap-3">
            <span class="text-emerald-400 text-base">✉️</span>
            <div>
              <strong class="text-white">Email:</strong>
              <a href="mailto:yessbangla.bd@gmail.com" class="text-emerald-400 hover:underline ml-1">yessbangla.bd@gmail.com</a>
            </div>
          </div>
        </div>

        <!-- Download PDF Briefs -->
        <div class="pt-6 border-t border-slate-700/80">
          <div class="text-xs font-bold text-slate-200 mb-3 uppercase tracking-wider">Download Official Company Profiles:</div>
          <div class="flex flex-wrap gap-3">
            <button onclick="alert('Company Profile (English Edition, 17 pages) download initiated.')" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-white transition flex items-center gap-2">
              📄 English Profile (v1.1)
            </button>
            <button onclick="alert('কোম্পানি প্রোফাইল (বাংলা সংস্করণ, ১৭ পৃষ্ঠা) ডাউনলোড শুরু হয়েছে।')" class="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-white transition flex items-center gap-2">
              📄 বাংলা প্রোফাইল (v1.2)
            </button>
          </div>
        </div>
      </div>

      <!-- Form -->
      <div class="bg-white p-8 rounded-3xl text-slate-800 shadow-lg">
        <h3 class="text-xl font-extrabold text-slate-900 mb-4">Request a Consultation</h3>
        <form onsubmit="event.preventDefault(); alert('Inquiry submitted! Our team will get back to you within 24 business hours.');" class="space-y-4">
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Full Name</label>
            <input type="text" required placeholder="Syed Reza" class="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20"/>
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Corporate Email</label>
            <input type="email" required placeholder="reza@company.com" class="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20"/>
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Phone / WhatsApp</label>
            <input type="tel" required placeholder="+880 1805 000000" class="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20"/>
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Service / Venture of Interest</label>
            <select class="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-emerald-500">
              <option>Next.js 16 Web & App Development</option>
              <option>48 Ready-Made Software Demo Purchase</option>
              <option>Shondhaan Service Marketplace Partnership</option>
              <option>Akash OTT Media & Playout CMS</option>
              <option>Organic Haat Agro Supply Chain</option>
              <option>Yess Host Enterprise NVMe Cloud</option>
              <option>Yess Event Production</option>
            </select>
          </div>
          <div>
            <label class="block text-xs font-bold text-slate-700 mb-1">Project Requirements</label>
            <textarea rows="3" placeholder="Tell us about your objectives, timeline, or scope..." class="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-emerald-500"></textarea>
          </div>
          <button type="submit" class="w-full py-3.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs shadow-lg shadow-emerald-600/30 transition-all hover:scale-[1.01]">
            Send Project Inquiry &rarr;
          </button>
        </form>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="bg-slate-50 border-t border-slate-200 py-16 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto text-xs text-slate-500">
    <div class="grid grid-cols-2 md:grid-cols-5 gap-8 mb-12">
      <div class="col-span-2">
        <div class="flex items-center gap-2 mb-3">
          <div class="w-8 h-8 rounded-xl bg-emerald-600 flex items-center justify-center text-white font-extrabold text-sm">YB</div>
          <span class="font-black text-base text-slate-900">Yess Bangla Private Limited</span>
        </div>
        <p class="text-xs text-slate-500 max-w-sm mb-4 leading-relaxed">
          Where Solution Begins. Complete IT & digital solutions, corporate venture studio, and software product powerhouse in Bangladesh.
        </p>
        <div class="text-[11px] text-slate-400">
          Block-A, Road-3, House-127, Mirpur-12, Dhaka-1216 &bull; yessbangla.bd@gmail.com
        </div>
      </div>

      <div>
        <div class="font-extrabold text-slate-900 mb-3 uppercase tracking-wider text-[11px]">6 Ventures</div>
        <ul class="space-y-2 font-medium">
          <li><a href="https://shondhaan.com" target="_blank" class="hover:text-emerald-600">Shondhaan</a></li>
          <li><a href="https://organichaat.top" target="_blank" class="hover:text-emerald-600">Organic Haat</a></li>
          <li><a href="https://akash.tv" target="_blank" class="hover:text-emerald-600">Akash OTT</a></li>
          <li><a href="https://yessbangla.top" target="_blank" class="hover:text-emerald-600">Yess Soft</a></li>
          <li><a href="#ventures" class="hover:text-emerald-600">Yess Host</a></li>
          <li><a href="#ventures" class="hover:text-emerald-600">Yess Event</a></li>
        </ul>
      </div>

      <div>
        <div class="font-extrabold text-slate-900 mb-3 uppercase tracking-wider text-[11px]">Engineering</div>
        <ul class="space-y-2 font-medium">
          <li><a href="#capabilities" class="hover:text-emerald-600">Next.js 16 Apps</a></li>
          <li><a href="#capabilities" class="hover:text-emerald-600">Laravel Backends</a></li>
          <li><a href="#capabilities" class="hover:text-emerald-600">E-Commerce</a></li>
          <li><a href="#capabilities" class="hover:text-emerald-600">ERP & POS Systems</a></li>
          <li><a href="#capabilities" class="hover:text-emerald-600">Streaming Playout</a></li>
        </ul>
      </div>

      <div>
        <div class="font-extrabold text-slate-900 mb-3 uppercase tracking-wider text-[11px]">Software Hub</div>
        <ul class="space-y-2 font-medium">
          <li><a href="#demos" class="hover:text-emerald-600">POS Terminals</a></li>
          <li><a href="#demos" class="hover:text-emerald-600">yCourier Logistics</a></li>
          <li><a href="#demos" class="hover:text-emerald-600">yPharma Healthcare</a></li>
          <li><a href="#demos" class="hover:text-emerald-600">School ERP</a></li>
          <li><a href="#demos" class="hover:text-emerald-600">Ott Playout</a></li>
        </ul>
      </div>
    </div>

    <div class="pt-8 border-t border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-4">
      <div>&copy; 2026 Yess Bangla Private Limited. All rights reserved.</div>
      <div class="flex items-center gap-6 font-semibold">
        <a href="https://yessbd.com" target="_blank" class="hover:text-emerald-600">yessbd.com</a>
        <a href="https://yessbangla.top" target="_blank" class="hover:text-emerald-600">yessbangla.top</a>
        <a href="https://www.facebook.com/yessbanglaltd" target="_blank" class="hover:text-emerald-600">Facebook</a>
      </div>
    </div>
  </footer>

  <!-- ================= INTERACTIVE MODAL FOR DEMO DETAILS ================= -->
  <div id="demo-modal" class="fixed inset-0 z-50 bg-slate-900/60 backdrop-blur-sm hidden items-center justify-center p-4">
    <div class="bg-white rounded-3xl max-w-lg w-full p-6 shadow-2xl border border-slate-200 relative animate-float">
      <button onclick="closeDemoModal()" class="absolute top-4 right-4 w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500 font-bold flex items-center justify-center transition">
        ✕
      </button>
      <div class="h-48 w-full rounded-2xl overflow-hidden bg-slate-100 border border-slate-100 mb-4">
        <img id="modal-img" src="" alt="Demo preview" class="w-full h-full object-cover"/>
      </div>
      <div id="modal-badge" class="inline-block px-3 py-1 rounded-full text-xs font-bold uppercase mb-2"></div>
      <h3 id="modal-title" class="text-2xl font-black text-slate-900 mb-2"></h3>
      <p id="modal-desc" class="text-xs text-slate-600 leading-relaxed mb-6"></p>

      <div class="flex items-center gap-3">
        <a id="modal-link" href="#" target="_blank" class="flex-1 py-3 text-center rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-md shadow-emerald-600/20 transition">
          Launch Live Interactive Demo &rarr;
        </a>
        <button onclick="closeDemoModal(); document.getElementById('contact').scrollIntoView({behavior: 'smooth'})" class="py-3 px-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-xs font-bold text-slate-700 transition">
          Request Quote
        </button>
      </div>
    </div>
  </div>

  <!-- Interactive JavaScript -->
  <script>
    function filterCategory(cat, btn) {
      document.querySelectorAll('.cat-pill').forEach(b => {
        b.className = "cat-pill px-4 py-2 rounded-full text-xs font-semibold bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 transition";
      });
      btn.className = "cat-pill active px-4 py-2 rounded-full text-xs font-bold bg-emerald-600 text-white shadow-sm transition";

      const cards = document.querySelectorAll('.demo-item');
      cards.forEach(c => {
        if (cat === 'all' || c.getAttribute('data-category') === cat) {
          c.style.display = 'flex';
        } else {
          c.style.display = 'none';
        }
      });
    }

    function searchDemos() {
      const q = document.getElementById('demo-search').value.toLowerCase();
      const cards = document.querySelectorAll('.demo-item');
      cards.forEach(c => {
        const title = c.getAttribute('data-title');
        const cat = c.getAttribute('data-category').toLowerCase();
        if (title.includes(q) || cat.includes(q)) {
          c.style.display = 'flex';
        } else {
          c.style.display = 'none';
        }
      });
    }

    function openDemoModal(title, cat, img, url, desc) {
      document.getElementById('modal-title').innerText = title;
      document.getElementById('modal-badge').innerText = cat;
      document.getElementById('modal-badge').className = "inline-block px-3 py-1 rounded-full text-xs font-bold uppercase mb-2 bg-emerald-50 text-emerald-700 border border-emerald-200";
      document.getElementById('modal-img').src = img;
      document.getElementById('modal-desc').innerText = desc;
      document.getElementById('modal-link').href = url;
      
      const modal = document.getElementById('demo-modal');
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }

    function closeDemoModal() {
      const modal = document.getElementById('demo-modal');
      modal.classList.remove('flex');
      modal.classList.add('hidden');
    }
  </script>
</body>
</html>
''')

content = ''.join(html)

dest_path = '/home/syed/.gemini/antigravity/brain/e18cf2c8-ba95-487f-98f1-7d887dfdcb63/yess_redesign_mockup.html'
with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Successfully compiled light mockup to {dest_path} ({len(content):,} bytes)')
