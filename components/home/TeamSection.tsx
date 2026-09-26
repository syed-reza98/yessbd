import React from "react";
import Image from "next/image";
import { TEAM_MEMBERS } from "@/data/team";

export function TeamSection() {
  return (
    <section id="team" className="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
      <div className="flex flex-col md:flex-row md:items-end justify-between mb-16">
        <div>
          <div className="inline-block text-xs font-extrabold text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
            Our People
          </div>
          <h2 className="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">
            The Minds Behind Yess Bangla
          </h2>
        </div>
        <p className="text-sm text-slate-500 max-w-md mt-4 md:mt-0 font-medium leading-relaxed">
          Senior software architects, UI/UX researchers, QA leads, and cloud DevOps engineers driving digital excellence across Bangladesh.
        </p>
      </div>

      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-7 gap-4">
        {TEAM_MEMBERS.map((tm, idx) => (
          <div
            key={idx}
            className="group text-center p-4 rounded-2xl bg-white border border-slate-200 hover:border-emerald-400 transition-all hover:shadow-lg hover:-translate-y-1"
          >
            <div className="w-20 h-20 mx-auto rounded-full overflow-hidden border-2 border-emerald-100 group-hover:border-emerald-500 transition mb-3 bg-slate-100 relative">
              <Image
                src={tm.image}
                alt={tm.name}
                fill
                className="object-cover group-hover:scale-110 transition-transform duration-300"
                unoptimized
              />
            </div>
            <h4 className="font-bold text-sm text-slate-900 group-hover:text-emerald-600 transition">
              {tm.name}
            </h4>
            <p className="text-[11px] text-slate-500 mt-1 leading-snug">
              {tm.role}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}
