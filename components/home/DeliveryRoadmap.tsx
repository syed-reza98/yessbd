import React from "react";
import { Compass, PenTool, Rocket, ShieldCheck, ArrowRight } from "lucide-react";

export function DeliveryRoadmap() {
  const steps = [
    {
      num: "01",
      title: "Discover & Audit",
      color: "text-emerald-600",
      accent: "border-emerald-200 bg-emerald-50/50",
      icon: <Compass className="w-6 h-6 text-emerald-600" />,
      desc: "Deep discovery workshops to map operational bottlenecks, customer pain points, data flows, and precise revenue and growth KPIs."
    },
    {
      num: "02",
      title: "Architect & UX",
      color: "text-teal-600",
      accent: "border-teal-200 bg-teal-50/50",
      icon: <PenTool className="w-6 h-6 text-teal-600" />,
      desc: "Creating high-fidelity Figma design systems, entity-relationship database schemas, and microservice cloud deployment blueprints."
    },
    {
      num: "03",
      title: "Build & Launch",
      color: "text-cyan-600",
      accent: "border-cyan-200 bg-cyan-50/50",
      icon: <Rocket className="w-6 h-6 text-cyan-600" />,
      desc: "Agile sprints delivered by senior engineering pods with automated CI/CD pipelines, penetration testing, and zero-downtime deployment."
    },
    {
      num: "04",
      title: "Scale & Support",
      color: "text-amber-600",
      accent: "border-amber-200 bg-amber-50/50",
      icon: <ShieldCheck className="w-6 h-6 text-amber-600" />,
      desc: "24/7 cloud performance monitoring, automated database replication, continuous feature evolution, and dedicated SLA contracts."
    }
  ];

  return (
    <section id="process" className="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
      <div className="text-center max-w-3xl mx-auto mb-16">
        <div className="inline-block text-xs font-extrabold text-emerald-700 bg-emerald-50 border border-emerald-200 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
          Delivery Model
        </div>
        <h2 className="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">
          Our 4-Stage Execution Framework
        </h2>
        <p className="text-base text-slate-500 mt-3 font-normal">
          From the initial strategic blueprint to post-deployment 24/7 enterprise reliability.
        </p>
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
        {steps.map((st) => (
          <div
            key={st.num}
            className="p-8 rounded-3xl bg-white border border-slate-200 hover:border-emerald-300 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between"
          >
            <div>
              <div className="flex items-center justify-between mb-6">
                <span className={`text-4xl font-black ${st.color}`}>{st.num}</span>
                <div className={`w-12 h-12 rounded-2xl border ${st.accent} flex items-center justify-center`}>
                  {st.icon}
                </div>
              </div>

              <h4 className="font-extrabold text-lg text-slate-900 mb-2">{st.title}</h4>
              <p className="text-xs text-slate-600 leading-relaxed">{st.desc}</p>
            </div>

            <div className="pt-6 border-t border-slate-100 mt-6 flex items-center text-xs font-bold text-slate-400">
              <span>Phase {st.num} Protocol</span>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
