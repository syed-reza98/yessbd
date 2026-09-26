import React from "react";
import Link from "next/link";
import { MapPin, Phone, Mail, Globe, ArrowUpRight } from "lucide-react";

export function Footer() {
  return (
    <footer className="bg-slate-50 border-t border-slate-200 py-16 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto text-xs text-slate-500">
      <div className="grid grid-cols-2 md:grid-cols-5 gap-10 mb-14">
        
        {/* Company Bio */}
        <div className="col-span-2">
          <div className="flex items-center gap-2.5 mb-4">
            <div className="w-8 h-8 rounded-xl bg-emerald-600 flex items-center justify-center text-white font-black text-sm shadow-xs">
              YB
            </div>
            <span className="font-black text-base text-slate-900 tracking-tight">
              Yess Bangla Private Limited
            </span>
          </div>
          <p className="text-xs text-slate-500 max-w-sm mb-6 leading-relaxed">
            Where Solution Begins. A diversified business conglomerate and enterprise IT studio transforming media, agriculture, e-commerce, cloud infrastructure, and software applications across Bangladesh.
          </p>

          <div className="space-y-2 text-[11px] text-slate-500">
            <div className="flex items-start gap-2">
              <MapPin className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
              <span>Block-A, Road-3, House-127, Mirpur-12, Dhaka-1216, Bangladesh</span>
            </div>
            <div className="flex items-center gap-2">
              <Mail className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
              <a href="mailto:yessbangla.bd@gmail.com" className="hover:text-emerald-600">yessbangla.bd@gmail.com</a>
            </div>
            <div className="flex items-center gap-2">
              <Phone className="w-3.5 h-3.5 text-emerald-600 shrink-0" />
              <span>+880 1805-464343 / +880 1805-464341</span>
            </div>
          </div>
        </div>

        {/* 6 Ventures */}
        <div>
          <div className="font-extrabold text-slate-900 mb-4 uppercase tracking-wider text-[11px]">
            6 Ventures
          </div>
          <ul className="space-y-2.5 font-medium">
            <li><a href="https://shondhaan.com" target="_blank" rel="noopener noreferrer" className="hover:text-emerald-600 flex items-center justify-between">Shondhaan <ArrowUpRight className="w-3 h-3 text-slate-400" /></a></li>
            <li><a href="https://organichaat.top" target="_blank" rel="noopener noreferrer" className="hover:text-emerald-600 flex items-center justify-between">Organic Haat <ArrowUpRight className="w-3 h-3 text-slate-400" /></a></li>
            <li><a href="https://akash.tv" target="_blank" rel="noopener noreferrer" className="hover:text-emerald-600 flex items-center justify-between">Akash OTT <ArrowUpRight className="w-3 h-3 text-slate-400" /></a></li>
            <li><a href="https://yessbangla.top" target="_blank" rel="noopener noreferrer" className="hover:text-emerald-600 flex items-center justify-between">Yess Soft <ArrowUpRight className="w-3 h-3 text-slate-400" /></a></li>
            <li><a href="#ventures" className="hover:text-emerald-600">Yess Host</a></li>
            <li><a href="#ventures" className="hover:text-emerald-600">Yess Event</a></li>
          </ul>
        </div>

        {/* Engineering Capabilities */}
        <div>
          <div className="font-extrabold text-slate-900 mb-4 uppercase tracking-wider text-[11px]">
            Capabilities
          </div>
          <ul className="space-y-2.5 font-medium">
            <li><a href="#capabilities" className="hover:text-emerald-600">Next.js 16 Applications</a></li>
            <li><a href="#capabilities" className="hover:text-emerald-600">Custom Laravel Backends</a></li>
            <li><a href="#capabilities" className="hover:text-emerald-600">E-Commerce Platforms</a></li>
            <li><a href="#capabilities" className="hover:text-emerald-600">POS & Inventory Systems</a></li>
            <li><a href="#capabilities" className="hover:text-emerald-600">Video Streaming Playout</a></li>
            <li><a href="#capabilities" className="hover:text-emerald-600">Cloud Infrastructure</a></li>
          </ul>
        </div>

        {/* Software Systems */}
        <div>
          <div className="font-extrabold text-slate-900 mb-4 uppercase tracking-wider text-[11px]">
            48 Software Hub
          </div>
          <ul className="space-y-2.5 font-medium">
            <li><a href="#demos" className="hover:text-emerald-600">YessPOS Terminals</a></li>
            <li><a href="#demos" className="hover:text-emerald-600">yCourier Logistics</a></li>
            <li><a href="#demos" className="hover:text-emerald-600">yPharma Healthcare</a></li>
            <li><a href="#demos" className="hover:text-emerald-600">School ERP System</a></li>
            <li><a href="#demos" className="hover:text-emerald-600">GurmentsERP Suite</a></li>
            <li><a href="#demos" className="hover:text-emerald-600">OTT Playout Media</a></li>
          </ul>
        </div>
      </div>

      <div className="pt-8 border-t border-slate-200 flex flex-col sm:flex-row items-center justify-between gap-4">
        <div>&copy; {new Date().getFullYear()} Yess Bangla Private Limited. All rights reserved.</div>
        <div className="flex items-center gap-6 font-semibold">
          <a href="https://yessbd.com" target="_blank" rel="noopener noreferrer" className="hover:text-emerald-600">Corporate Portal</a>
          <a href="https://yessbangla.top" target="_blank" rel="noopener noreferrer" className="hover:text-emerald-600">Software Portal</a>
          <a href="https://www.facebook.com/yessbanglaltd" target="_blank" rel="noopener noreferrer" className="hover:text-emerald-600">Facebook</a>
        </div>
      </div>
    </footer>
  );
}
