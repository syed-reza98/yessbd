import React from "react";
import Image from "next/image";
import Link from "next/link";
import { ArrowLeft, ArrowUpRight, CheckCircle2, ShieldCheck, Zap } from "lucide-react";
import { VENTURES } from "@/data/ventures";

export const metadata = {
  title: "Corporate Ventures | Yess Bangla Private Limited",
  description: "Explore the 6 independent corporate ventures and specialized subsidiaries of Yess Bangla.",
};

export default function VenturesPage() {
  return (
    <div className="py-16 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      {/* Breadcrumb */}
      <div className="mb-8">
        <Link
          href="/"
          className="inline-flex items-center gap-1.5 text-xs font-bold text-slate-500 hover:text-emerald-600 transition"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Overview</span>
        </Link>
      </div>

      {/* Header */}
      <div className="max-w-3xl mb-16">
        <div className="inline-block text-xs font-extrabold text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
          Conglomerate Portfolio
        </div>
        <h1 className="text-4xl sm:text-6xl font-black text-slate-900 tracking-tight mb-4">
          Our 6 Independent Ventures
        </h1>
        <p className="text-base text-slate-600 leading-relaxed font-normal">
          Each venture solves a mission-critical infrastructure, consumer, or enterprise demand in Bangladesh — backed by centralized cloud engineering and corporate governance.
        </p>
      </div>

      {/* Ventures List */}
      <div className="space-y-16">
        {VENTURES.map((venture, index) => (
          <div
            key={venture.id}
            id={venture.id}
            className="rounded-3xl bg-white border border-slate-200 p-8 sm:p-12 shadow-sm hover:shadow-xl transition-all duration-300 grid grid-cols-1 lg:grid-cols-12 gap-8 items-center"
          >
            <div className="lg:col-span-7">
              <div className="flex items-center gap-2 mb-3">
                <span className="px-3 py-1 rounded-full text-xs font-bold uppercase bg-emerald-50 text-emerald-700 border border-emerald-200">
                  {venture.badge}
                </span>
                <span className="text-xs font-semibold text-slate-400">Venture 0{index + 1}</span>
              </div>

              <h2 className="text-3xl sm:text-4xl font-black text-slate-900 mb-2">
                {venture.name}
              </h2>
              <p className="text-sm font-semibold text-emerald-700 mb-4">
                &ldquo;{venture.tagline}&rdquo;
              </p>

              <p className="text-sm text-slate-600 leading-relaxed mb-6">
                {venture.description}
              </p>

              {/* Highlights */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5 mb-8">
                {venture.highlights.map((h, i) => (
                  <div key={i} className="flex items-center gap-2 text-xs text-slate-700 font-medium">
                    <CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" />
                    <span>{h}</span>
                  </div>
                ))}
              </div>

              {/* Stats Bar */}
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-4 p-4 rounded-2xl bg-slate-50 border border-slate-100 text-xs mb-8">
                {venture.stats.map((s, idx) => (
                  <div key={idx}>
                    <strong className="text-slate-900 block text-base font-extrabold">{s.value}</strong>
                    <span className="text-slate-500">{s.label}</span>
                  </div>
                ))}
              </div>

              <div className="flex flex-wrap items-center gap-3">
                <a
                  href={venture.url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="px-6 py-3 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs shadow-md shadow-emerald-600/20 transition-all hover:scale-[1.02] flex items-center gap-2"
                >
                  <span>Visit {venture.name} Portal</span>
                  <ArrowUpRight className="w-4 h-4" />
                </a>
                <Link
                  href="/#contact"
                  className="px-5 py-3 rounded-xl border border-slate-200 hover:bg-slate-50 text-xs font-bold text-slate-700 transition"
                >
                  Partner With Venture
                </Link>
              </div>
            </div>

            {/* Visual Frame */}
            <div className="lg:col-span-5">
              <div className="rounded-2xl overflow-hidden border border-slate-200 bg-slate-100 h-72 sm:h-80 relative shadow-inner">
                <Image
                  src={venture.image}
                  alt={venture.name}
                  fill
                  className="object-cover"
                  unoptimized
                />
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
