"use client";

import React, { useState } from "react";
import Link from "next/link";
import Image from "next/image";
import { MessageSquare, Phone, Menu, X, ArrowRight } from "lucide-react";

export function Navbar() {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <>
      {/* Top Announcement Ribbon */}
      <div className="bg-gradient-to-r from-emerald-50 via-teal-50 to-emerald-50 border-b border-emerald-100 py-2 px-4 text-center text-xs text-slate-700">
        <span className="inline-flex items-center gap-1.5 text-emerald-700 font-bold">
          <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
          Next.js 16 Portfolio:
        </span>{" "}
        Unifying 6 Business Ventures, 48 Live Software Demos & Client Case Studies.
        <a href="#ventures" className="text-emerald-700 hover:text-emerald-800 font-bold underline ml-1">
          Explore Ventures &rarr;
        </a>
      </div>

      {/* Main Sticky Header */}
      <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200/80 shadow-xs transition-all">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
          
          {/* Logo & Brand */}
          <Link href="/" className="flex items-center gap-3 group">
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-teal-500 flex items-center justify-center text-white font-extrabold shadow-md shadow-emerald-500/20 group-hover:scale-105 transition-transform">
              YB
            </div>
            <div>
              <div className="text-xl font-black text-slate-900 tracking-tight flex items-center gap-1">
                <span className="text-emerald-600">YESS</span>BANGLA
              </div>
              <div className="text-[10px] uppercase font-bold tracking-widest text-slate-400">
                Where Solution Begins
              </div>
            </div>
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden lg:flex items-center gap-8 text-sm font-semibold text-slate-600">
            <a href="#ventures" className="hover:text-emerald-600 transition flex items-center gap-1.5">
              <span>Ventures</span>
              <span className="text-[10px] bg-emerald-100 text-emerald-800 px-1.5 py-0.5 rounded-full font-bold">6</span>
            </a>
            <a href="#demos" className="hover:text-emerald-600 transition flex items-center gap-1.5">
              <span>Software Hub</span>
              <span className="text-[10px] bg-amber-100 text-amber-800 px-1.5 py-0.5 rounded-full font-bold">48 Demos</span>
            </a>
            <a href="#capabilities" className="hover:text-emerald-600 transition">Services</a>
            <a href="#projects" className="hover:text-emerald-600 transition">Case Studies</a>
            <a href="#process" className="hover:text-emerald-600 transition">Roadmap</a>
            <a href="#team" className="hover:text-emerald-600 transition">Team</a>
          </nav>

          {/* Action Buttons */}
          <div className="hidden sm:flex items-center gap-3">
            <a
              href="https://wa.me/881805464343"
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1.5 text-xs font-bold text-slate-700 bg-slate-100 hover:bg-slate-200 px-3.5 py-2 rounded-xl transition"
            >
              <MessageSquare className="w-3.5 h-3.5 text-emerald-600" />
              <span>WhatsApp</span>
            </a>
            <a
              href="#contact"
              className="text-xs font-bold text-white bg-slate-900 hover:bg-emerald-600 px-4 py-2.5 rounded-xl shadow-xs transition-all hover:scale-[1.02]"
            >
              Get In Touch
            </a>
          </div>

          {/* Mobile Menu Button */}
          <button
            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
            className="lg:hidden p-2 rounded-xl text-slate-600 hover:bg-slate-100"
          >
            {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>

        {/* Mobile Dropdown Menu */}
        {mobileMenuOpen && (
          <div className="lg:hidden bg-white border-b border-slate-200 px-4 pt-2 pb-6 space-y-3 animate-in slide-in-from-top-2 duration-200">
            <a
              href="#ventures"
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2 text-sm font-semibold text-slate-700 hover:bg-emerald-50 rounded-lg"
            >
              6 Corporate Ventures
            </a>
            <a
              href="#demos"
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2 text-sm font-semibold text-slate-700 hover:bg-emerald-50 rounded-lg"
            >
              48 Software Demos
            </a>
            <a
              href="#capabilities"
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2 text-sm font-semibold text-slate-700 hover:bg-emerald-50 rounded-lg"
            >
              Services & Capabilities
            </a>
            <a
              href="#projects"
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2 text-sm font-semibold text-slate-700 hover:bg-emerald-50 rounded-lg"
            >
              Client Case Studies
            </a>
            <a
              href="#process"
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2 text-sm font-semibold text-slate-700 hover:bg-emerald-50 rounded-lg"
            >
              Delivery Roadmap
            </a>
            <a
              href="#team"
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2 text-sm font-semibold text-slate-700 hover:bg-emerald-50 rounded-lg"
            >
              Leadership & Team
            </a>
            <a
              href="#contact"
              onClick={() => setMobileMenuOpen(false)}
              className="block px-3 py-2.5 text-center text-sm font-bold text-white bg-emerald-600 rounded-xl shadow-sm"
            >
              Book Consultation
            </a>
          </div>
        )}
      </header>
    </>
  );
}
