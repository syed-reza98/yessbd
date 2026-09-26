import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Navbar } from "@/components/layout/Navbar";
import { Footer } from "@/components/layout/Footer";

const inter = Inter({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-inter",
});

export const metadata: Metadata = {
  title: "Yess Bangla | Enterprise IT Solutions & Venture Studio",
  description:
    "Next.js 16 unified company portfolio for Yess Bangla Private Limited and Yess Bangla IT Solutions. Powering 6 ventures, 48 ready-to-deploy software demos, and enterprise client solutions.",
  keywords: [
    "Yess Bangla",
    "Yess Bangla IT Solutions",
    "Software Company Bangladesh",
    "Next.js 16",
    "48 Software Demos",
    "ERP Software",
    "POS Terminal",
    "Akash OTT",
    "Shondhaan",
    "Organic Haat",
    "Yess Host",
    "Yess Event"
  ],
  icons: {
    icon: "/assets/yessbangla/logos/logo.png"
  }
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`scroll-smooth ${inter.variable}`}>
      <body className="bg-white text-slate-800 antialiased font-sans selection:bg-emerald-500 selection:text-white">
        <Navbar />
        <main className="min-h-screen">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
