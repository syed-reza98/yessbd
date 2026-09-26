import React from "react";
import Link from "next/link";
import { ArrowLeft } from "lucide-react";
import { SoftwareHub } from "@/components/home/SoftwareHub";

export const metadata = {
  title: "48 Software Systems & Demos | Yess Bangla IT Solutions",
  description:
    "Test, explore, and launch 48 ready-to-deploy enterprise SaaS solutions across e-commerce, healthcare, retail POS, logistics, ERP, education, and news.",
};

export default function ProductsPage() {
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

      <SoftwareHub />
    </div>
  );
}
