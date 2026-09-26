import React from "react";
import Image from "next/image";
import Link from "next/link";
import { ArrowRight, Sparkles, ShieldCheck, CheckCircle2, Play, Layers } from "lucide-react";

export function HeroSection() {
  return (
    <section id="hero" className="relative pt-12 pb-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto overflow-hidden bg-grid-pattern">
      {/* Ambient Light Glow Orbs */}
      <div className="absolute top-10 left-1/2 -translate-x-1/2 w-[700px] h-[400px] bg-gradient-to-r from-emerald-200/40 via-teal-200/30 to-cyan-200/30 blur-[130px] rounded-full pointer-events-none animate-glow" />

      <div className="relative z-10 text-center max-w-4xl mx-auto">
        {/* Pill Badge */}
        <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full border border-emerald-200 bg-emerald-50/80 text-emerald-800 text-xs font-bold uppercase tracking-wider mb-8 shadow-xs">
          <span className="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse" />
          Enterprise IT Conglomerate & Venture Studio
        </div>

        {/* Main Headline */}
        <h1 className="text-4xl sm:text-6xl lg:text-7xl font-extrabold text-slate-900 tracking-tight leading-[1.1] mb-6">
          Engineering Scalable Software. <br className="hidden sm:inline" />
          <span className="text-transparent bg-clip-text bg-gradient-to-r from-emerald-600 via-teal-600 to-cyan-600">
            Transforming Modern Ventures.
          </span>
        </h1>

        <p className="text-lg sm:text-xl text-slate-600 max-w-2xl mx-auto mb-10 leading-relaxed font-normal">
          A full-service business consulting and IT solutions powerhouse in Bangladesh. Powering nationwide streaming, organic marketplaces, high-speed cloud infrastructure, and{" "}
          <strong className="text-slate-800 font-semibold">48+ ready-to-deploy enterprise SaaS solutions</strong>.
        </p>

        {/* Action Buttons */}
        <div className="flex flex-wrap items-center justify-center gap-4 mb-16">
          <a
            href="#demos"
            className="px-8 py-4 rounded-2xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-sm shadow-xl shadow-emerald-600/25 transition-all hover:scale-[1.02] flex items-center gap-2"
          >
            <span>🚀</span>
            <span>Explore 48+ Interactive Demos</span>
          </a>
          <a
            href="#ventures"
            className="px-7 py-4 rounded-2xl bg-white border border-slate-200 hover:border-emerald-300 text-slate-800 font-bold text-sm shadow-xs hover:shadow-md transition-all flex items-center gap-2"
          >
            <span>Discover Our 6 Ventures</span>
            <ArrowRight className="w-4 h-4 text-emerald-600" />
          </a>
        </div>

        {/* Live Metrics Strip */}
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 p-6 rounded-3xl bg-white/90 backdrop-blur-xl border border-slate-200 shadow-[0_8px_30px_rgb(0,0,0,0.04)]">
          <div className="p-3 text-center border-r border-slate-100 last:border-0">
            <div className="text-3xl sm:text-4xl font-black text-emerald-600">6</div>
            <div className="text-xs font-semibold text-slate-500 mt-1 uppercase tracking-wider">Independent Ventures</div>
          </div>
          <div className="p-3 text-center border-r border-slate-100 last:border-0">
            <div className="text-3xl sm:text-4xl font-black text-slate-900">48+</div>
            <div className="text-xs font-semibold text-slate-500 mt-1 uppercase tracking-wider">Software Demos</div>
          </div>
          <div className="p-3 text-center border-r border-slate-100 last:border-0">
            <div className="text-3xl sm:text-4xl font-black text-emerald-600">600+</div>
            <div className="text-xs font-semibold text-slate-500 mt-1 uppercase tracking-wider">Satisfied Clients</div>
          </div>
          <div className="p-3 text-center">
            <div className="text-3xl sm:text-4xl font-black text-slate-900">100%</div>
            <div className="text-xs font-semibold text-slate-500 mt-1 uppercase tracking-wider">Delivery Success</div>
          </div>
        </div>
      </div>

      {/* Hero Visual Frame with Real Mockup Images */}
      <div className="mt-16 max-w-5xl mx-auto rounded-3xl border border-slate-200 bg-white p-3 sm:p-5 shadow-2xl relative">
        <div className="flex items-center justify-between pb-3 px-3 border-b border-slate-100 mb-4">
          <div className="flex items-center gap-2">
            <div className="flex gap-1.5">
              <span className="w-3 h-3 rounded-full bg-rose-400" />
              <span className="w-3 h-3 rounded-full bg-amber-400" />
              <span className="w-3 h-3 rounded-full bg-emerald-400" />
            </div>
            <span className="ml-2 text-xs font-mono text-slate-400">yessbd.com/ecosystem-showcase</span>
          </div>
          <div className="text-xs font-bold text-emerald-600 bg-emerald-50 px-3 py-1 rounded-full border border-emerald-100 flex items-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5" />
            <span>Next.js 16 App Router</span>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Mockup 1: Akash Desktop */}
          <div className="group relative rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 p-2 hover:border-emerald-300 transition-all shadow-xs">
            <div className="h-44 w-full rounded-xl overflow-hidden bg-slate-200 relative">
              <Image
                src="/assets/yessbangla/projects/akash_desktop.png"
                alt="Akash.tv Preview"
                fill
                className="object-cover group-hover:scale-105 transition-transform duration-500"
                unoptimized
              />
            </div>
            <div className="p-3">
              <div className="flex items-center justify-between text-xs font-bold text-emerald-600 mb-1">
                <span>STREAMING VENTURE</span>
                <span>akash.tv</span>
              </div>
              <h4 className="font-extrabold text-sm text-slate-900">Akash.tv Digital Platform</h4>
              <p className="text-xs text-slate-500 mt-1">High-concurrency video playout & editorial CMS.</p>
            </div>
          </div>

          {/* Mockup 2: Shopix Ecommerce */}
          <div className="group relative rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 p-2 hover:border-emerald-300 transition-all shadow-xs">
            <div className="h-44 w-full rounded-xl overflow-hidden bg-slate-200 relative">
              <Image
                src="/assets/yessbangla/demos/ecom1.JPG"
                alt="Shopix Ecommerce Preview"
                fill
                className="object-cover group-hover:scale-105 transition-transform duration-500"
                unoptimized
              />
            </div>
            <div className="p-3">
              <div className="flex items-center justify-between text-xs font-bold text-teal-600 mb-1">
                <span>ECOMMERCE SUITE</span>
                <span>Demo #1</span>
              </div>
              <h4 className="font-extrabold text-sm text-slate-900">Shopix E-Commerce Platform</h4>
              <p className="text-xs text-slate-500 mt-1">Order tracking, courier dispatch & payment gateway.</p>
            </div>
          </div>

          {/* Mockup 3: YessPOS Retail */}
          <div className="group relative rounded-2xl overflow-hidden border border-slate-200 bg-slate-50 p-2 hover:border-emerald-300 transition-all shadow-xs">
            <div className="h-44 w-full rounded-xl overflow-hidden bg-slate-200 relative">
              <Image
                src="/assets/yessbangla/demos/yess_pos.png"
                alt="YessPOS Preview"
                fill
                className="object-cover group-hover:scale-105 transition-transform duration-500"
                unoptimized
              />
            </div>
            <div className="p-3">
              <div className="flex items-center justify-between text-xs font-bold text-amber-600 mb-1">
                <span>RETAIL POS</span>
                <span>Cloud SaaS</span>
              </div>
              <h4 className="font-extrabold text-sm text-slate-900">YessPOS Smart Terminal</h4>
              <p className="text-xs text-slate-500 mt-1">Barcode scanning, stock ledgers & cashier registers.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
