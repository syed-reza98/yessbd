import React from "react";
import Image from "next/image";
import { ArrowUpRight, CheckCircle2, ShieldCheck, Zap, Sparkles } from "lucide-react";
import { VENTURES } from "@/data/ventures";

export function VenturesBento() {
  const shondhaan = VENTURES.find((v) => v.id === "shondhaan")!;
  const organicHaat = VENTURES.find((v) => v.id === "organic-haat")!;
  const akashOtt = VENTURES.find((v) => v.id === "akash-ott")!;
  const yessSoft = VENTURES.find((v) => v.id === "yess-soft")!;
  const yessHost = VENTURES.find((v) => v.id === "yess-host")!;
  const yessEvent = VENTURES.find((v) => v.id === "yess-event")!;

  return (
    <section id="ventures" className="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
      <div className="flex flex-col md:flex-row md:items-end justify-between mb-16">
        <div>
          <div className="inline-block text-xs font-extrabold text-emerald-700 bg-emerald-50 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
            Conglomerate Subsidiaries
          </div>
          <h2 className="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">The 6 Core Ventures</h2>
        </div>
        <p className="text-sm text-slate-500 max-w-md mt-4 md:mt-0 font-medium leading-relaxed">
          Our specialized business units addressing mission-critical markets in Bangladesh, backed by shared IT infrastructure, engineering pods, and visionary leadership.
        </p>
      </div>

      {/* Bento Grid */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        
        {/* Venture 1: Shondhaan (Span 2) */}
        <div className="md:col-span-2 group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-xs hover:shadow-2xl transition-all duration-300 relative overflow-hidden flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <span className="px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 text-xs font-bold">
                {shondhaan.category}
              </span>
              <a
                href={shondhaan.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-xs font-bold text-emerald-600 hover:text-emerald-700 hover:underline flex items-center gap-1"
              >
                <span>shondhaan.com</span>
                <ArrowUpRight className="w-3.5 h-3.5" />
              </a>
            </div>
            <h3 className="text-3xl font-extrabold text-slate-900 mb-3">{shondhaan.name}</h3>
            <p className="text-sm text-slate-600 leading-relaxed mb-6 max-w-xl">
              {shondhaan.description}
            </p>
          </div>

          <div className="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-64 mb-6 relative">
            <Image
              src={shondhaan.image}
              alt={shondhaan.name}
              fill
              className="object-cover group-hover:scale-105 transition-transform duration-500"
              unoptimized
            />
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t border-slate-100 text-xs text-slate-600">
            {shondhaan.stats.map((s, idx) => (
              <div key={idx}>
                <strong className="text-slate-900 block text-sm font-bold">{s.value}</strong>
                <span>{s.label}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Venture 2: Organic Haat */}
        <div className="group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-xs hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <span className="px-3 py-1 rounded-full bg-teal-50 text-teal-700 border border-teal-200 text-xs font-bold">
                {organicHaat.category}
              </span>
              <a
                href={organicHaat.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-xs font-bold text-teal-600 hover:underline flex items-center gap-1"
              >
                <span>organichaat.top</span>
                <ArrowUpRight className="w-3.5 h-3.5" />
              </a>
            </div>
            <h3 className="text-2xl font-extrabold text-slate-900 mb-2">{organicHaat.name}</h3>
            <p className="text-xs text-slate-600 leading-relaxed mb-4">
              {organicHaat.description}
            </p>
          </div>

          <div className="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-48 mb-4 relative">
            <Image
              src={organicHaat.image}
              alt={organicHaat.name}
              fill
              className="object-cover group-hover:scale-105 transition-transform duration-500"
              unoptimized
            />
          </div>

          <div className="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
            <span>🌱 100% Lab Tested</span>
            <span>🚚 Cold-Chain Logistics</span>
          </div>
        </div>

        {/* Venture 3: Akash OTT */}
        <div className="group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-xs hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <span className="px-3 py-1 rounded-full bg-cyan-50 text-cyan-700 border border-cyan-200 text-xs font-bold">
                {akashOtt.category}
              </span>
              <a
                href={akashOtt.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-xs font-bold text-cyan-600 hover:underline flex items-center gap-1"
              >
                <span>akash.tv</span>
                <ArrowUpRight className="w-3.5 h-3.5" />
              </a>
            </div>
            <h3 className="text-2xl font-extrabold text-slate-900 mb-2">{akashOtt.name}</h3>
            <p className="text-xs text-slate-600 leading-relaxed mb-4">
              {akashOtt.description}
            </p>
          </div>

          <div className="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-48 mb-4 relative">
            <Image
              src={akashOtt.image}
              alt={akashOtt.name}
              fill
              className="object-cover group-hover:scale-105 transition-transform duration-500"
              unoptimized
            />
          </div>

          <div className="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
            <span>📺 HD Playout Playout</span>
            <span>📰 Real-Time News CMS</span>
          </div>
        </div>

        {/* Venture 4: Yess Soft (Span 2) */}
        <div className="md:col-span-2 group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-xs hover:shadow-2xl transition-all duration-300 relative overflow-hidden flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <span className="px-3 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 text-xs font-bold">
                {yessSoft.category}
              </span>
              <a
                href={yessSoft.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-xs font-bold text-emerald-600 hover:underline flex items-center gap-1"
              >
                <span>yessbangla.top</span>
                <ArrowUpRight className="w-3.5 h-3.5" />
              </a>
            </div>
            <h3 className="text-3xl font-extrabold text-slate-900 mb-2">{yessSoft.name}</h3>
            <p className="text-sm text-slate-600 leading-relaxed mb-6 max-w-xl">
              {yessSoft.description}
            </p>
          </div>

          <div className="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-64 mb-6 relative">
            <Image
              src={yessSoft.image}
              alt={yessSoft.name}
              fill
              className="object-cover group-hover:scale-105 transition-transform duration-500"
              unoptimized
            />
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t border-slate-100 text-xs text-slate-600">
            {yessSoft.stats.map((s, idx) => (
              <div key={idx}>
                <strong className="text-slate-900 block text-sm font-bold">{s.value}</strong>
                <span>{s.label}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Venture 5: Yess Host */}
        <div className="group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-xs hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <span className="px-3 py-1 rounded-full bg-indigo-50 text-indigo-700 border border-indigo-200 text-xs font-bold">
                {yessHost.category}
              </span>
              <span className="text-xs font-bold text-indigo-600">99.9% Uptime</span>
            </div>
            <h3 className="text-2xl font-extrabold text-slate-900 mb-2">{yessHost.name}</h3>
            <p className="text-xs text-slate-600 leading-relaxed mb-4">
              {yessHost.description}
            </p>
          </div>

          <div className="p-6 rounded-2xl bg-gradient-to-br from-indigo-50 to-slate-50 border border-indigo-100 text-center mb-4">
            <div className="text-3xl mb-2">⚡</div>
            <div className="text-sm font-bold text-slate-900">Pure NVMe SSD Storage</div>
            <div className="text-xs text-slate-500 mt-1">Free SSL & Daily Cloud Backups</div>
          </div>

          <div className="pt-4 border-t border-slate-100 flex items-center justify-between text-xs text-slate-500">
            <span>🛡️ DDoS Protected</span>
            <span>🎧 24/7 Live Support</span>
          </div>
        </div>

        {/* Venture 6: Yess Event (Span 2) */}
        <div className="md:col-span-2 group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-xs hover:shadow-2xl transition-all duration-300 flex flex-col justify-between">
          <div>
            <div className="flex items-center justify-between mb-4">
              <span className="px-3 py-1 rounded-full bg-amber-50 text-amber-700 border border-amber-200 text-xs font-bold">
                {yessEvent.category}
              </span>
              <span className="text-xs font-bold text-amber-600">Full In-House AV</span>
            </div>
            <h3 className="text-3xl font-extrabold text-slate-900 mb-2">{yessEvent.name}</h3>
            <p className="text-sm text-slate-600 leading-relaxed mb-6 max-w-xl">
              {yessEvent.description}
            </p>
          </div>

          <div className="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-60 mb-6 relative">
            <Image
              src={yessEvent.image}
              alt={yessEvent.name}
              fill
              className="object-cover group-hover:scale-105 transition-transform duration-500"
              unoptimized
            />
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 pt-4 border-t border-slate-100 text-xs text-slate-600">
            {yessEvent.stats.map((s, idx) => (
              <div key={idx}>
                <strong className="text-slate-900 block text-sm font-bold">{s.value}</strong>
                <span>{s.label}</span>
              </div>
            ))}
          </div>
        </div>

      </div>
    </section>
  );
}
