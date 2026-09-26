export interface Venture {
  id: string;
  name: string;
  tagline: string;
  category: string;
  badge: string;
  description: string;
  url: string;
  image: string;
  stats: { label: string; value: string }[];
  highlights: string[];
}

export const VENTURES: Venture[] = [
  {
    id: "shondhaan",
    name: "Shondhaan",
    tagline: "Find trusted professionals. Get things done.",
    category: "Home & Professional Services Marketplace",
    badge: "Marketplace",
    description: "A comprehensive digital service marketplace connecting households and businesses across Bangladesh with verified professionals for AC servicing, electrical, plumbing, home cleaning, and appliance repair.",
    url: "https://shondhaan.com",
    image: "/assets/yessbd/ventures/shondhaan-full.png",
    stats: [
      { label: "Verified Pros", value: "500+" },
      { label: "Rating", value: "4.9/5" },
      { label: "Avg Response", value: "<15 Mins" },
      { label: "Coverage", value: "Dhaka & Nationwide" }
    ],
    highlights: [
      "On-demand technician dispatch",
      "Transparent upfront pricing",
      "Customer reviews & ratings",
      "One platform for all home repairs"
    ]
  },
  {
    id: "organic-haat",
    name: "Organic Haat",
    tagline: "Purity from farm to fork.",
    category: "Agro & Organic Food Supply Chain",
    badge: "AgroTech",
    description: "Direct-from-farm organic groceries, chemical-free produce, lab-tested natural pantry staples, and scheduled recurring subscription boxes delivered in cold-chain logistics.",
    url: "https://organichaat.top",
    image: "/assets/yessbd/ventures/organic-haat.png",
    stats: [
      { label: "Organic Purity", value: "100%" },
      { label: "Partner Farms", value: "40+" },
      { label: "Delivery", value: "Cold-Chain" },
      { label: "Products", value: "120+ Items" }
    ],
    highlights: [
      "Lab-tested pesticide-free produce",
      "Direct ethical farmer sourcing",
      "Recurring weekly grocery subscriptions",
      "Temperature-controlled logistics"
    ]
  },
  {
    id: "akash-ott",
    name: "Akash OTT & News",
    tagline: "Premium digital entertainment and trusted journalism.",
    category: "Streaming Media & Playout CMS",
    badge: "MediaTech",
    description: "A digital streaming platform and real-time news network under Akash TV, delivering high-definition drama serials, movies, live television channels, and an editorial newsroom CMS.",
    url: "https://akash.tv",
    image: "/assets/yessbangla/projects/akash_desktop.png",
    stats: [
      { label: "Playout", value: "24/7 Live" },
      { label: "Resolution", value: "Full HD 1080p" },
      { label: "Architecture", value: "Low-Latency HLS" },
      { label: "Viewports", value: "Web, Mobile, SmartTV" }
    ],
    highlights: [
      "Adaptive bitrate video streaming",
      "Editorial workflow & CMS approvals",
      "Original Bangladeshi drama productions",
      "Cloud video CDN acceleration"
    ]
  },
  {
    id: "yess-soft",
    name: "Yess Soft",
    tagline: "Engineering enterprise software that scales.",
    category: "Enterprise IT & SaaS Engineering",
    badge: "Software Hub",
    description: "The technological engine of Yess Bangla. Building bespoke ERPs, sales CRMs, multi-outlet POS platforms, and maintaining a catalog of 48+ ready-to-deploy software management products.",
    url: "https://yessbangla.top",
    image: "/assets/yessbd/ventures/yesssoft.png",
    stats: [
      { label: "Ready Demos", value: "48 Systems" },
      { label: "Delivery Sprint", value: "90 Days" },
      { label: "Framework", value: "Next.js & Laravel" },
      { label: "Pods", value: "Senior Engineers" }
    ],
    highlights: [
      "Modern Next.js 16 & React 19 stacks",
      "Multi-tenant SaaS cloud architecture",
      "Custom enterprise integrations",
      "End-to-end QA & DevOps automation"
    ]
  },
  {
    id: "yess-host",
    name: "Yess Host",
    tagline: "High-performance cloud infrastructure and hosting.",
    category: "Hosting & Cloud Infrastructure",
    badge: "Cloud Infra",
    description: "Enterprise NVMe SSD web hosting, automated cloud server provisioning, official domain name registration, and 24/7 technical monitoring with a 99.9% uptime SLA.",
    url: "https://yessbd.com/ventures/7?type=Yess%20Host",
    image: "/assets/yessbd/logos/logo_6a8975c2b891b.png",
    stats: [
      { label: "Storage", value: "Pure NVMe" },
      { label: "Uptime SLA", value: "99.9%" },
      { label: "Support", value: "24/7 Humans" },
      { label: "Security", value: "Free SSL + DDoS" }
    ],
    highlights: [
      "One-click software deployments",
      "Automated daily offsite backups",
      "Isolated container resources",
      "Enterprise cPanel & root access"
    ]
  },
  {
    id: "yess-event",
    name: "Yess Event",
    tagline: "Flawless corporate summits and live technical production.",
    category: "Event Management & Production",
    badge: "Production",
    description: "Turnkey corporate conference management, national business summits, concerts, brand activation showcases, and weddings with fully owned audiovisual and staging equipment.",
    url: "https://yessbd.com/ventures/6?type=Yess%20Event",
    image: "/assets/yessbd/heroes/hero_6a89646fd72ff.jpg",
    stats: [
      { label: "Equipment", value: "100% Owned" },
      { label: "Conferences", value: "50+ Executed" },
      { label: "Stage & AV", value: "Line-Array Audio" },
      { label: "Execution", value: "Single Lead" }
    ],
    highlights: [
      "Full high-definition LED stage walls",
      "Corporate keynote conference staging",
      "Live broadcast multi-camera feeds",
      "Exhibition booth design & logistics"
    ]
  }
];
