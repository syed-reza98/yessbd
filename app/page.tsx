import React from "react";
import { HeroSection } from "@/components/home/HeroSection";
import { VenturesBento } from "@/components/home/VenturesBento";
import { SoftwareHub } from "@/components/home/SoftwareHub";
import { ServicesSection } from "@/components/home/ServicesSection";
import { CaseStudies } from "@/components/home/CaseStudies";
import { DeliveryRoadmap } from "@/components/home/DeliveryRoadmap";
import { TeamSection } from "@/components/home/TeamSection";
import { ConsultationForm } from "@/components/home/ConsultationForm";

export default function HomePage() {
  return (
    <div className="relative">
      <HeroSection />
      <VenturesBento />
      <SoftwareHub />
      <ServicesSection />
      <CaseStudies />
      <DeliveryRoadmap />
      <TeamSection />
      <ConsultationForm />
    </div>
  );
}
