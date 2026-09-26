"use client";

import React, { useState } from "react";
import { 
  MapPin, 
  Phone, 
  Mail, 
  Send, 
  CheckCircle2, 
  Download, 
  FileText, 
  MessageSquare,
  Sparkles
} from "lucide-react";

export function ConsultationForm() {
  const [submitted, setSubmitted] = useState(false);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    service: "Next.js 16 Web & App Engineering",
    notes: ""
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitted(true);
  };

  return (
    <section id="contact" className="py-24 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto border-t border-slate-100">
      <div className="p-8 sm:p-14 rounded-3xl bg-gradient-to-br from-slate-900 via-slate-800 to-emerald-950 text-white shadow-2xl grid grid-cols-1 lg:grid-cols-2 gap-12 relative overflow-hidden">
        {/* Glow orb */}
        <div className="absolute top-0 right-0 w-96 h-96 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />

        {/* Contact info side */}
        <div className="relative z-10 flex flex-col justify-between">
          <div>
            <span className="px-3.5 py-1 rounded-full bg-emerald-500/20 text-emerald-400 border border-emerald-500/30 text-xs font-extrabold uppercase tracking-wider mb-4 inline-block">
              Let&apos;s Build Together
            </span>
            <h2 className="text-3xl sm:text-5xl font-black text-white tracking-tight mb-4 leading-tight">
              Ready to Scale Your Enterprise?
            </h2>
            <p className="text-sm text-slate-300 leading-relaxed mb-8 max-w-md">
              Whether you need a bespoke ERP solution, a high-converting web platform, or are looking to partner with our 6 ventures — we respond within 24 hours.
            </p>

            <div className="space-y-4 text-xs text-slate-300 mb-10">
              <div className="flex items-start gap-3">
                <MapPin className="w-5 h-5 text-emerald-400 shrink-0 mt-0.5" />
                <div>
                  <strong className="text-white block text-sm font-bold">Headquarters:</strong>
                  <span>Block-A, Road-3, House-127 (Green View), 1st Floor, Mirpur-12, Dhaka-1216, Bangladesh</span>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Phone className="w-5 h-5 text-emerald-400 shrink-0" />
                <div>
                  <strong className="text-white">Phone & WhatsApp:</strong>
                  <a href="https://wa.me/881805464343" target="_blank" rel="noopener noreferrer" className="text-emerald-400 hover:underline ml-1">
                    +880 1805-464343
                  </a>{" "}
                  / +880 1805-464341
                </div>
              </div>
              <div className="flex items-center gap-3">
                <Mail className="w-5 h-5 text-emerald-400 shrink-0" />
                <div>
                  <strong className="text-white">Email:</strong>
                  <a href="mailto:yessbangla.bd@gmail.com" className="text-emerald-400 hover:underline ml-1">
                    yessbangla.bd@gmail.com
                  </a>
                </div>
              </div>
            </div>
          </div>

          {/* Download PDF Briefs */}
          <div className="pt-6 border-t border-slate-700/80">
            <div className="text-xs font-bold text-slate-200 mb-3 uppercase tracking-wider flex items-center gap-2">
              <FileText className="w-4 h-4 text-emerald-400" />
              <span>Official Company Profiles (17 Pages):</span>
            </div>
            <div className="flex flex-wrap gap-3">
              <button
                type="button"
                onClick={() => alert("Official Company Profile (English Edition, 17 Pages) requested. Our team will send it directly to your email or WhatsApp.")}
                className="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-white transition flex items-center gap-2"
              >
                <Download className="w-3.5 h-3.5 text-emerald-400" />
                <span>English Profile (v1.1)</span>
              </button>
              <button
                type="button"
                onClick={() => alert("কোম্পানি প্রোফাইল (বাংলা সংস্করণ, ১৭ পৃষ্ঠা) অনুরোধ সফল হয়েছে। আমাদের টিম সরাসরি আপনার ইমেইল বা হোয়াটসঅ্যাপে পাঠিয়ে দিবে।")}
                className="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-bold text-white transition flex items-center gap-2"
              >
                <Download className="w-3.5 h-3.5 text-emerald-400" />
                <span>বাংলা প্রোফাইল (v1.2)</span>
              </button>
            </div>
          </div>
        </div>

        {/* Lead Form */}
        <div className="relative z-10 bg-white p-8 rounded-3xl text-slate-800 shadow-xl">
          <h3 className="text-xl font-extrabold text-slate-900 mb-2">Request a Consultation</h3>
          <p className="text-xs text-slate-500 mb-6">Fill out the brief below and our technical leads will reach out.</p>

          {submitted ? (
            <div className="py-12 text-center space-y-3">
              <div className="w-14 h-14 mx-auto rounded-full bg-emerald-100 text-emerald-600 flex items-center justify-center">
                <CheckCircle2 className="w-8 h-8" />
              </div>
              <h4 className="text-xl font-extrabold text-slate-900">Inquiry Received!</h4>
              <p className="text-xs text-slate-600 max-w-xs mx-auto">
                Thank you, <strong className="text-slate-900">{formData.name}</strong>. A technical director from Yess Bangla will contact you via WhatsApp or Email within 24 hours.
              </p>
              <button
                onClick={() => setSubmitted(false)}
                className="mt-4 text-xs font-bold text-emerald-600 hover:underline"
              >
                Send another inquiry &rarr;
              </button>
            </div>
          ) : (
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Full Name</label>
                <input
                  type="text"
                  required
                  value={formData.name}
                  onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                  placeholder="Syed Reza"
                  className="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Corporate Email</label>
                <input
                  type="email"
                  required
                  value={formData.email}
                  onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                  placeholder="reza@company.com"
                  className="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Phone / WhatsApp</label>
                <input
                  type="tel"
                  required
                  value={formData.phone}
                  onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
                  placeholder="+880 1805 000000"
                  className="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-emerald-500 focus:ring-2 focus:ring-emerald-500/20"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Service / Venture of Interest</label>
                <select
                  value={formData.service}
                  onChange={(e) => setFormData({ ...formData, service: e.target.value })}
                  className="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-emerald-500"
                >
                  <option>Next.js 16 Web & App Engineering</option>
                  <option>48 Ready-Made Software Demo Purchase</option>
                  <option>Shondhaan Service Marketplace Partnership</option>
                  <option>Akash OTT Media & Playout CMS</option>
                  <option>Organic Haat Agro Supply Chain</option>
                  <option>Yess Host Enterprise NVMe Cloud</option>
                  <option>Yess Event Production</option>
                </select>
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-700 mb-1">Project Requirements / Scope</label>
                <textarea
                  rows={3}
                  value={formData.notes}
                  onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
                  placeholder="Tell us about your timeline, feature requirements, or project goals..."
                  className="w-full px-4 py-2.5 rounded-xl bg-slate-50 border border-slate-200 text-xs text-slate-800 focus:outline-none focus:border-emerald-500"
                />
              </div>

              <button
                type="submit"
                className="w-full py-3.5 rounded-xl bg-emerald-600 hover:bg-emerald-700 text-white font-extrabold text-xs shadow-lg shadow-emerald-600/30 transition-all hover:scale-[1.01] flex items-center justify-center gap-2"
              >
                <span>Send Project Inquiry</span>
                <Send className="w-3.5 h-3.5" />
              </button>
            </form>
          )}
        </div>
      </div>
    </section>
  );
}
