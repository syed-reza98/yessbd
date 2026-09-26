"use client";

import React from "react";
import Image from "next/image";
import { X, ExternalLink, ArrowRight, ShieldCheck } from "lucide-react";
import { SoftwareDemo } from "@/data/demos";

interface DemoModalProps {
  demo: SoftwareDemo | null;
  onClose: () => void;
}

export function DemoModal({ demo, onClose }: DemoModalProps) {
  if (!demo) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/60 backdrop-blur-sm animate-in fade-in duration-200">
      <div 
        className="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl border border-slate-200 relative animate-float"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          onClick={onClose}
          className="absolute top-4 right-4 w-9 h-9 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-500 font-bold flex items-center justify-center transition-all hover:scale-105"
        >
          <X className="w-5 h-5" />
        </button>

        <div className="h-48 w-full rounded-2xl overflow-hidden bg-slate-100 border border-slate-100 mb-5 relative">
          <Image
            src={demo.image}
            alt={demo.name}
            fill
            className="object-cover"
            unoptimized
          />
        </div>

        <div className="inline-block px-3 py-1 rounded-full text-xs font-bold uppercase mb-2 bg-emerald-50 text-emerald-700 border border-emerald-200">
          {demo.category} &bull; {demo.platform}
        </div>

        <h3 className="text-2xl font-black text-slate-900 mb-2">
          {demo.name}
        </h3>

        <p className="text-xs text-slate-600 leading-relaxed mb-6">
          {demo.description}
        </p>

        <div className="bg-slate-50 rounded-xl p-3.5 border border-slate-100 mb-6 space-y-1.5 text-xs text-slate-600">
          <div className="flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-emerald-600" />
            <span>Multi-device responsive: Mobile, Tablet & Desktop</span>
          </div>
          <div className="flex items-center gap-2">
            <ShieldCheck className="w-4 h-4 text-emerald-600" />
            <span>Interactive sandbox credentials pre-filled</span>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <a
            href={demo.url}
            target="_blank"
            rel="noopener noreferrer"
            className="flex-1 py-3.5 text-center rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs shadow-md shadow-emerald-600/20 transition-all hover:scale-[1.01] flex items-center justify-center gap-2"
          >
            <span>Launch Live Interactive Demo</span>
            <ExternalLink className="w-4 h-4" />
          </a>
          <button
            onClick={() => {
              onClose();
              const contactEl = document.getElementById("contact");
              if (contactEl) contactEl.scrollIntoView({ behavior: "smooth" });
            }}
            className="py-3.5 px-4 rounded-xl border border-slate-200 hover:bg-slate-50 text-xs font-bold text-slate-700 transition"
          >
            Request Quote
          </button>
        </div>
      </div>
    </div>
  );
}
