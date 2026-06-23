/**
 * Single source of truth for Strong Tower site data.
 * Service times, contact details and navigation are defined once here and
 * reused everywhere. Keystatic layers an editing UI over a subset of this
 * later; this typed module is the robust base.
 */

export const site = {
  name: "Strong Tower Christian Ministry",
  shortName: "Strong Tower",

  taglines: {
    primary: "He Loves You to Life, So We Love You to Life",
    secondary: "It's All About Him",
  },

  scripture: {
    verse:
      "The name of the LORD is a strong tower; the righteous run to it and are safe.",
    reference: "Proverbs 18:10",
  },

  contact: {
    address: {
      street: "320 E National Cemetery Rd",
      city: "Florence",
      state: "SC",
      zip: "29506",
    },
    full: "320 E National Cemetery Rd, Florence, SC 29506",
    phone: "843-468-0964",
    phoneHref: "tel:+18434680964",
    email: "strongtowercm@yahoo.com",
    emailHref: "mailto:strongtowercm@yahoo.com",
    mapsUrl:
      "https://www.google.com/maps/search/?api=1&query=320+E+National+Cemetery+Rd+Florence+SC+29506",
    mapsEmbed:
      "https://www.google.com/maps?q=320+E+National+Cemetery+Rd+Florence+SC+29506&output=embed",
  },

  services: [
    {
      name: "Sunday Worship",
      day: "Sunday",
      time: "10:30 AM",
      mode: "In person, Facebook and YouTube",
    },
    {
      name: "Mid-Week Service",
      day: "Wednesday",
      time: "7:00 PM",
      mode: "In person, Facebook and YouTube",
    },
    {
      name: "Prophetic Impartation",
      day: "Saturday",
      time: "10:00 AM",
      mode: "In house",
    },
  ],

  social: {
    facebook: "https://www.facebook.com/StrongTowerCm",
    youtube: "https://www.youtube.com/@strongtowerchristianminist4397",
  },

  giving: {
    // Swap-slot: set NEXT_PUBLIC_GIVING_URL to the church's giving destination.
    url: process.env.NEXT_PUBLIC_GIVING_URL || "",
  },

  // Concise top bar for desktop.
  navPrimary: [
    { label: "About", href: "/about" },
    { label: "Watch", href: "/watch" },
    { label: "Events", href: "/events" },
    { label: "Visit", href: "/visit" },
    { label: "Get Involved", href: "/get-involved" },
    { label: "Contact", href: "/contact" },
  ],

  // Full set for the mobile menu and footer.
  navAll: [
    { label: "About", href: "/about" },
    { label: "What We Believe", href: "/what-we-believe" },
    { label: "Leadership", href: "/leadership" },
    { label: "Watch", href: "/watch" },
    { label: "Events", href: "/events" },
    { label: "Visit", href: "/visit" },
    { label: "Get Involved", href: "/get-involved" },
    { label: "Prayer", href: "/prayer" },
    { label: "Contact", href: "/contact" },
  ],

  url: process.env.NEXT_PUBLIC_SITE_URL || "https://strongtowercm.org",
} as const;

export type Service = (typeof site.services)[number];
export type NavLink = { label: string; href: string };
