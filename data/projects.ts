export interface ClientProject {
  id: string;
  name: string;
  category: string;
  client: string;
  description: string;
  stack: string[];
  url: string;
  image: string;
}

export const CLIENT_PROJECTS: ClientProject[] = [
  {
    id: "akash-tv",
    name: "Akash.tv Streaming Network",
    category: "OTT Streaming & News CMS",
    client: "Akash Media Group",
    description: "Custom OTT platform engineered for responsive web and mobile viewports with real-time news syndication and high-concurrency video delivery.",
    stack: ["React", "HLS Video", "AWS CloudFront", "Tailwind CSS"],
    url: "https://akash.tv/",
    image: "/assets/yessbangla/projects/akash_desktop.png"
  },
  {
    id: "cbl",
    name: "Coast Bangladesh Limited (CBL)",
    category: "Corporate Tax & Legal Advisory",
    client: "CBL Consulting",
    description: "Corporate advisory web application for Income Tax, VAT compliance, legal consulting, and encrypted document exchange.",
    stack: ["PHP", "Laravel", "Tailwind CSS", "MySQL"],
    url: "https://cbl.yessbd.top/",
    image: "/assets/yessbangla/projects/cbl.png"
  },
  {
    id: "ascension",
    name: "Ascension Accounting",
    category: "FinTech & Cloud Bookkeeping",
    client: "Ascension Global",
    description: "Cloud-based corporate accounting portal managing automated bookkeeping, corporate financial reporting, and tax calculations.",
    stack: ["PHP", "Laravel", "Tailwind CSS", "PDF Engine"],
    url: "https://ascension-accounting.yessbd.top/",
    image: "/assets/yessbangla/projects/ascension.png"
  },
  {
    id: "bharaghor",
    name: "BharaGhor Real Estate Portal",
    category: "PropTech & Rental Marketplace",
    client: "BharaGhor Technologies",
    description: "Smart residential rental system connecting landlords and tenants with digital lease agreements, property search, and rent tracking.",
    stack: ["React", "Node.js", "Firebase", "Stripe"],
    url: "https://bharaghor-321e2.web.app/",
    image: "/assets/yessbangla/projects/bharaghor.png"
  },
  {
    id: "yess-dinning",
    name: "Yess Dinning Lounge",
    category: "Hospitality & Restaurant POS",
    client: "Yess Hospitality",
    description: "Smart restaurant table reservation management system designed to handle real-time table availability, digital menu ordering, and kitchen billing.",
    stack: ["React", "Node.js", "Stripe", "Tailwind CSS"],
    url: "https://yessrestaurant.akashtv.top/",
    image: "/assets/yessbangla/projects/table.png"
  },
  {
    id: "yessbangla-shop",
    name: "YessBangla Shop",
    category: "E-Commerce Retail Storefront",
    client: "Yess Retail Division",
    description: "Full-scale e-commerce shopping experience with order management, parcel delivery sync, and multiple digital payment gateways.",
    stack: ["React", "Node.js", "Tailwind CSS", "Payment Gateways"],
    url: "https://yessbangla.shop/",
    image: "/assets/yessbangla/projects/shop.png"
  }
];
