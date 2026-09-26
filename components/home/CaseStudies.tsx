import React from "react";
import Image from "next/image";
import { ArrowUpRight, CheckCircle2, Layers } from "lucide-react";
import { CLIENT_PROJECTS } from "@/data/projects";

export function CaseStudies() {
  return (
    <section id="projects" className="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
      <div className="flex flex-col md:flex-row md:items-end justify-between mb-16">
        <div>
          <div className="inline-block text-xs font-extrabold text-cyan-700 bg-cyan-50 border border-cyan-200 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
            Delivered Client Work
          </div>
          <h2 className="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">
            Enterprise Client Case Studies
          </h2>
        </div>
        <p className="text-sm text-slate-500 max-w-md mt-4 md:mt-0 font-medium leading-relaxed">
          Proven digital platforms engineered and deployed for industry leaders, startups, and public institutions across Bangladesh.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {CLIENT_PROJECTS.map((proj) => (
          <div
            key={proj.id}
            className="group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-6 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between"
          >
            <div>
              <div className="rounded-2xl overflow-hidden border border-slate-100 bg-slate-50 h-52 mb-5 relative">
                <Image
                  src={proj.image}
                  alt={proj.name}
                  fill
                  className="object-cover group-hover:scale-105 transition-transform duration-500"
                  unoptimized
                />
              </div>

              <div className="flex items-center justify-between text-[11px] font-bold text-cyan-700 uppercase tracking-wider mb-1.5">
                <span>{proj.category}</span>
                <span className="text-slate-400 font-normal">{proj.client}</span>
              </div>

              <h3 className="font-extrabold text-xl text-slate-900 group-hover:text-emerald-600 transition mb-2">
                {proj.name}
              </h3>

              <p className="text-xs text-slate-600 leading-relaxed mb-5">
                {proj.description}
              </p>

              {/* Tech Stack Pills */}
              <div className="flex flex-wrap gap-1.5 mb-6">
                {proj.stack.map((item, idx) => (
                  <span
                    key={idx}
                    className="text-[10px] font-semibold bg-slate-100 text-slate-700 px-2 py-0.5 rounded-md"
                  >
                    {item}
                  </span>
                ))}
              </div>
            </div>

            <div className="pt-4 border-t border-slate-100 flex items-center justify-between">
              <a
                href={proj.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-xs font-bold text-emerald-600 hover:text-emerald-700 hover:underline flex items-center gap-1"
              >
                <span>Visit Live Platform</span>
                <ArrowUpRight className="w-3.5 h-3.5" />
              </a>
              <span className="text-[10px] font-mono bg-emerald-50 text-emerald-700 border border-emerald-100 px-2 py-0.5 rounded-full font-bold">
                Production
              </span>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
