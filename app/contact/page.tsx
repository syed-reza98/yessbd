import React from "react";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { ConsultationForm } from "@/components/home/ConsultationForm";

export const metadata = {
  title: "Contact & Consultation | Yess Bangla Private Limited",
  description: "Get in touch with Yess Bangla IT Solutions and explore partnership opportunities with our 6 ventures.",
};

export default function ContactPage() {
  return (
    <div className="py-12 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      {/* Breadcrumb */}
      <div className="mb-6">
        <Link
          href="/"
          className="inline-flex items-center gap-1.5 text-xs font-bold text-slate-500 hover:text-emerald-600 transition"
        >
          <ArrowLeft className="w-4 h-4" />
          <span>Back to Home</span>
        </Link>
      </div>

      <ConsultationForm />
    </div>
  );
}
