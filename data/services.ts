export interface ServiceOffering {
  id: string;
  name: string;
  category: string;
  description: string;
  iconName: string;
  features: string[];
}

export const SERVICES: ServiceOffering[] = [
  {
    id: "web-engineering",
    name: "Full-Stack Web & App Engineering",
    category: "Software Development",
    description: "Modern web applications built with Next.js 16, React 19, TypeScript, Laravel, and Node.js for maximum performance and conversion.",
    iconName: "Code",
    features: [
      "Next.js 16 Server Components",
      "API integrations & Microservices",
      "Progressive Web Apps (PWA)",
      "High-traffic scalable architecture"
    ]
  },
  {
    id: "ui-ux-design",
    name: "UI/UX & Design Systems",
    category: "Product Design",
    description: "Human-centric digital interfaces, accessible Figma prototypes, and cohesive brand identities tailored for engagement and retention.",
    iconName: "Palette",
    features: [
      "User research & Wireframing",
      "Figma design tokens & components",
      "Mobile-first responsive layouts",
      "WCAG 2.1 accessible UX"
    ]
  },
  {
    id: "cloud-devops",
    name: "Cloud Infrastructure & Hosting",
    category: "DevOps & Cloud",
    description: "Enterprise NVMe SSD hosting, AWS cloud architecture, automated CI/CD deployments, and 99.9% uptime SLA monitoring.",
    iconName: "Server",
    features: [
      "AWS / Cloud server provisioning",
      "Automated CI/CD pipelines",
      "DDoS mitigation & SSL security",
      "24/7 technical infrastructure support"
    ]
  },
  {
    id: "ecommerce-solutions",
    name: "E-Commerce & Digital Payments",
    category: "Commerce",
    description: "End-to-end commerce platforms with multi-vendor capabilities, bKash, Nagad, and card gateway integrations, and logistics synchronization.",
    iconName: "ShoppingCart",
    features: [
      "Multi-vendor store architectures",
      "bKash / Nagad / SSLCommerz gateways",
      "Real-time courier API sync",
      "Automated inventory ledgers"
    ]
  },
  {
    id: "enterprise-erp",
    name: "Enterprise ERP & Management Systems",
    category: "Enterprise Systems",
    description: "Tailored ERP solutions for garments manufacturing, courier logistics networks, hospital clinical suites, and school administrations.",
    iconName: "Database",
    features: [
      "Garments production line tracking",
      "Courier dispatch & rider management",
      "Hospital OPD & pharmacy management",
      "School student fee & exams portal"
    ]
  },
  {
    id: "ott-media-playout",
    name: "OTT Video Playout & Editorial CMS",
    category: "Media Technology",
    description: "Cloud-hosted video on demand and 24/7 live television streaming infrastructure with low-latency adaptive bitrate and newsroom CMS.",
    iconName: "Video",
    features: [
      "HLS video adaptive bitrate",
      "Editorial approval workflows",
      "Custom video players & DRM",
      "Multi-device responsive streaming"
    ]
  }
];
