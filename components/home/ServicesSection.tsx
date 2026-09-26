import React from "react";
import Image from "next/image";
import { 
  Code, 
  Palette, 
  Server, 
  ShoppingCart, 
  Database, 
  Video, 
  ArrowRight, 
  CheckCircle2, 
  Cpu 
} from "lucide-react";
import { SERVICES } from "@/data/services";

const TECH_STACK = [
  { name: "React", file: "react-original.svg" },
  { name: "Next.js & JS", file: "javascript-original.svg" },
  { name: "Tailwind CSS", file: "tailwindcss-original.svg" },
  { name: "Node.js", file: "nodejs-original.svg" },
  { name: "Laravel", file: "laravel-original.svg" },
  { name: "Python", file: "python-original.svg" },
  { name: "Docker", file: "docker-original.svg" },
  { name: "AWS Cloud", file: "amazonwebservices-plain-wordmark.svg" },
  { name: "Figma", file: "figma-original.svg" },
  { name: "Git", file: "git-original.svg" },
  { name: "Linux OS", file: "linux-original.svg" },
  { name: "Vue.js", file: "vuejs-original.svg" },
];

export function ServicesSection() {
  const getIcon = (iconName: string) => {
    switch (iconName) {
      case "Code":
        return <Code className="w-6 h-6 text-emerald-600" />;
      case "Palette":
        return <Palette className="w-6 h-6 text-teal-600" />;
      case "Server":
        return <Server className="w-6 h-6 text-indigo-600" />;
      case "ShoppingCart":
        return <ShoppingCart className="w-6 h-6 text-amber-600" />;
      case "Database":
        return <Database className="w-6 h-6 text-cyan-600" />;
      case "Video":
        return <Video className="w-6 h-6 text-rose-600" />;
      default:
        return <Cpu className="w-6 h-6 text-emerald-600" />;
    }
  };

  return (
    <section id="capabilities" className="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-end justify-between mb-16">
        <div>
          <div className="inline-block text-xs font-extrabold text-teal-700 bg-teal-50 border border-teal-200 px-3 py-1 rounded-full uppercase tracking-wider mb-3">
            Core Engineering Capabilities
          </div>
          <h2 className="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">
            End-to-End Technology Services
          </h2>
        </div>
        <p className="text-sm text-slate-500 max-w-md mt-4 md:mt-0 font-medium leading-relaxed">
          From full-stack enterprise web platforms to cloud infrastructure and video streaming playouts, we craft dependable digital solutions.
        </p>
      </div>

      {/* Services Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
        {SERVICES.map((srv) => (
          <div
            key={srv.id}
            className="group rounded-3xl bg-white border border-slate-200 hover:border-emerald-400 p-8 shadow-xs hover:shadow-xl hover:-translate-y-1 transition-all duration-300 flex flex-col justify-between"
          >
            <div>
              <div className="w-12 h-12 rounded-2xl bg-slate-50 border border-slate-100 flex items-center justify-center mb-6 group-hover:scale-110 group-hover:bg-emerald-50 transition-all">
                {getIcon(srv.iconName)}
              </div>

              <div className="text-[11px] font-bold text-slate-400 uppercase tracking-wider mb-1">
                {srv.category}
              </div>
              <h3 className="text-xl font-extrabold text-slate-900 mb-3 group-hover:text-emerald-600 transition">
                {srv.name}
              </h3>
              <p className="text-xs text-slate-600 leading-relaxed mb-6">
                {srv.description}
              </p>

              <div className="space-y-2 mb-6">
                {srv.features.map((feat, idx) => (
                  <div key={idx} className="flex items-center gap-2 text-xs text-slate-600">
                    <CheckCircle2 className="w-4 h-4 text-emerald-500 shrink-0" />
                    <span>{feat}</span>
                  </div>
                ))}
              </div>
            </div>

            <a
              href="#contact"
              className="pt-4 border-t border-slate-100 text-xs font-bold text-slate-700 hover:text-emerald-600 flex items-center justify-between group-hover:text-emerald-600 transition"
            >
              <span>Consult on {srv.name.split(" ")[0]}</span>
              <ArrowRight className="w-3.5 h-3.5 group-hover:translate-x-1 transition-transform" />
            </a>
          </div>
        ))}
      </div>

      {/* Tech Stack Strip */}
      <div className="rounded-3xl bg-slate-50 border border-slate-200 p-8 sm:p-10">
        <div className="text-center max-w-xl mx-auto mb-8">
          <div className="text-xs font-bold uppercase tracking-wider text-slate-400 mb-1">
            Engineered With Modern Standards
          </div>
          <h4 className="text-xl font-extrabold text-slate-900">
            Enterprise Technology & Cloud Ecosystem
          </h4>
        </div>

        <div className="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-6 gap-6 items-center">
          {TECH_STACK.map((tech, idx) => (
            <div
              key={idx}
              className="flex flex-col items-center justify-center p-3 rounded-2xl bg-white border border-slate-200/80 hover:border-emerald-300 hover:shadow-xs transition-all group"
            >
              <div className="w-10 h-10 relative mb-2 flex items-center justify-center">
                <Image
                  src={`/assets/yessbangla/tech_icons/${tech.file}`}
                  alt={tech.name}
                  width={36}
                  height={36}
                  className="object-contain group-hover:scale-110 transition-transform"
                  unoptimized
                />
              </div>
              <span className="text-[11px] font-semibold text-slate-600 group-hover:text-slate-900">
                {tech.name}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
