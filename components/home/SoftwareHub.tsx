"use client";

import React, { useState, useMemo } from "react";
import Image from "next/image";
import { Search, ExternalLink, Eye, CheckCircle2, Laptop } from "lucide-react";
import { SOFTWARE_DEMOS, SoftwareDemo } from "@/data/demos";
import { DemoModal } from "@/components/ui/DemoModal";

const CATEGORIES = [
  { id: "all", label: "All Systems", count: 48 },
  { id: "Ecommerce", label: "E-Commerce", count: 10 },
  { id: "Healthcare", label: "Healthcare & Clinic", count: 5 },
  { id: "Retail", label: "POS & Retail", count: 7 },
  { id: "Business", label: "Courier & CRM", count: 8 },
  { id: "Enterprise", label: "ERP & Legal", count: 4 },
  { id: "Education", label: "School Systems", count: 2 },
  { id: "News", label: "News & E-Paper", count: 7 },
  { id: "Travel", label: "Travel & Booking", count: 3 },
  { id: "Finance", label: "Microfinance", count: 1 },
  { id: "Entertainment", label: "OTT Playout", count: 1 },
];

export function SoftwareHub() {
  const [selectedCategory, setSelectedCategory] = useState("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [activeModalDemo, setActiveModalDemo] = useState<SoftwareDemo | null>(null);

  const filteredDemos = useMemo(() => {
    return SOFTWARE_DEMOS.filter((demo) => {
      const matchesCategory =
        selectedCategory === "all" ||
        demo.category.toLowerCase() === selectedCategory.toLowerCase();

      const matchesSearch =
        demo.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        demo.category.toLowerCase().includes(searchQuery.toLowerCase()) ||
        demo.description.toLowerCase().includes(searchQuery.toLowerCase());

      return matchesCategory && matchesSearch;
    });
  }, [selectedCategory, searchQuery]);

  const getBadgeColor = (category: string) => {
    switch (category) {
      case "Ecommerce":
        return "bg-emerald-50 text-emerald-700 border-emerald-200";
      case "Healthcare":
        return "bg-rose-50 text-rose-700 border-rose-200";
      case "Retail":
        return "bg-indigo-50 text-indigo-700 border-indigo-200";
      case "Business":
        return "bg-amber-50 text-amber-700 border-amber-200";
      case "Enterprise":
        return "bg-violet-50 text-violet-700 border-violet-200";
      case "Education":
        return "bg-blue-50 text-blue-700 border-blue-200";
      case "News":
        return "bg-slate-100 text-slate-700 border-slate-200";
      case "Travel":
        return "bg-teal-50 text-teal-700 border-teal-200";
      case "Finance":
        return "bg-emerald-50 text-emerald-700 border-emerald-200";
      case "Entertainment":
        return "bg-cyan-50 text-cyan-700 border-cyan-200";
      default:
        return "bg-slate-100 text-slate-700 border-slate-200";
    }
  };

  return (
    <section id="demos" className="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
      <div className="text-center max-w-3xl mx-auto mb-12">
        <div className="inline-block text-xs font-extrabold text-amber-700 bg-amber-50 border border-amber-200 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
          Interactive Demo Gallery
        </div>
        <h2 className="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">
          48 Ready-to-Deploy Software Systems
        </h2>
        <p className="text-base text-slate-500 mt-3 font-normal">
          Explore our pre-engineered management software systems spanning 10 key industries. Filter by category, test features in real-time, and launch full interactive demos.
        </p>

        {/* Search Bar */}
        <div className="mt-8 max-w-md mx-auto relative">
          <input
            type="text"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search systems (e.g. POS, Pharmacy, Courier, ERP, News)..."
            className="w-full px-5 py-3.5 pl-11 rounded-2xl bg-white border border-slate-200 text-sm text-slate-800 shadow-xs focus:outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20 transition placeholder:text-slate-400"
          />
          <Search className="w-5 h-5 text-slate-400 absolute left-4 top-1/2 -translate-y-1/2 pointer-events-none" />
        </div>
      </div>

      {/* Category Filter Pills */}
      <div className="flex flex-wrap items-center justify-center gap-2 mb-12">
        {CATEGORIES.map((cat) => {
          const isActive = selectedCategory === cat.id;
          return (
            <button
              key={cat.id}
              onClick={() => setSelectedCategory(cat.id)}
              className={`px-4 py-2 rounded-full text-xs font-semibold transition-all ${
                isActive
                  ? "bg-emerald-600 text-white font-bold shadow-sm scale-105"
                  : "bg-white border border-slate-200 text-slate-700 hover:border-emerald-400 hover:bg-slate-50"
              }`}
            >
              {cat.label} ({cat.count})
            </button>
          );
        })}
      </div>

      {/* Demos Count Indicator */}
      <div className="flex items-center justify-between text-xs text-slate-500 mb-6 px-1">
        <span>
          Showing <strong className="text-slate-900 font-bold">{filteredDemos.length}</strong> systems
          {searchQuery && ` for "${searchQuery}"`}
        </span>
        <span className="hidden sm:inline-flex items-center gap-1.5 text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full font-semibold border border-emerald-100">
          <CheckCircle2 className="w-3.5 h-3.5" />
          All demos deployed & live
        </span>
      </div>

      {/* Demos Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredDemos.map((demo, index) => (
          <div
            key={demo.id}
            className="group rounded-2xl bg-white border border-slate-200 hover:border-emerald-400 p-4 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between"
          >
            <div>
              {/* Thumbnail Container */}
              <div className="h-44 w-full rounded-xl overflow-hidden bg-slate-100 border border-slate-100 mb-3 relative">
                <Image
                  src={demo.image}
                  alt={demo.name}
                  fill
                  className="object-cover group-hover:scale-105 transition-transform duration-500"
                  unoptimized
                />
                <span
                  className={`absolute top-2.5 left-2.5 px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase border backdrop-blur-md ${getBadgeColor(
                    demo.category
                  )}`}
                >
                  {demo.category}
                </span>
              </div>

              {/* Meta strip */}
              <div className="flex items-center justify-between text-[11px] text-slate-400 mb-1">
                <span className="font-semibold text-emerald-600">{demo.platform}</span>
                <span>Demo #{index + 1}</span>
              </div>

              <h4 className="font-extrabold text-base text-slate-900 group-hover:text-emerald-600 transition mb-1 line-clamp-1">
                {demo.name}
              </h4>

              <p className="text-xs text-slate-500 line-clamp-2 leading-relaxed mb-4">
                {demo.description}
              </p>
            </div>

            {/* Action Buttons */}
            <div className="pt-3 border-t border-slate-100 flex items-center justify-between">
              <a
                href={demo.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-xs font-bold text-emerald-600 hover:text-emerald-700 flex items-center gap-1.5 hover:underline"
              >
                <span>Launch Demo</span>
                <ExternalLink className="w-3.5 h-3.5" />
              </a>

              <button
                onClick={() => setActiveModalDemo(demo)}
                className="text-[11px] font-semibold text-slate-500 hover:text-slate-800 bg-slate-100 hover:bg-slate-200 px-2.5 py-1 rounded-lg transition flex items-center gap-1"
              >
                <Eye className="w-3 h-3" />
                <span>Preview Specs</span>
              </button>
            </div>
          </div>
        ))}
      </div>

      {filteredDemos.length === 0 && (
        <div className="text-center py-16 bg-slate-50 rounded-3xl border border-slate-200 mt-6">
          <p className="text-base font-semibold text-slate-700">No software demos found matching your filter.</p>
          <button
            onClick={() => {
              setSelectedCategory("all");
              setSearchQuery("");
            }}
            className="mt-3 text-xs font-bold text-emerald-600 hover:underline"
          >
            Clear filters & view all 48 demos &rarr;
          </button>
        </div>
      )}

      {/* Interactive Modal */}
      <DemoModal
        demo={activeModalDemo}
        onClose={() => setActiveModalDemo(null)}
      />
    </section>
  );
}
