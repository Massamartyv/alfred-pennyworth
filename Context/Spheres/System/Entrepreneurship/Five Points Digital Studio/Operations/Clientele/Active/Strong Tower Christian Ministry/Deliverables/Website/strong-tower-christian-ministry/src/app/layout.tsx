import type { Metadata } from "next";
import { Inter, Cormorant_Garamond } from "next/font/google";
import "./globals.css";
import Navigation from "@/components/Navigation/Navigation";
import Footer from "@/components/Footer/Footer";
import { site } from "@/lib/site";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-body",
  display: "swap",
  weight: ["300", "400", "500", "600"],
});

const cormorant = Cormorant_Garamond({
  subsets: ["latin"],
  variable: "--font-heading",
  display: "swap",
  weight: ["400", "500", "600", "700"],
  style: ["normal", "italic"],
});

export const metadata: Metadata = {
  title: {
    template: `%s | ${site.name}`,
    default: `${site.name} | Florence, SC`,
  },
  description:
    "Strong Tower Christian Ministry is a Spirit-filled church in Florence, South Carolina. He loves you to life, so we love you to life. Join us Sundays at 10:30 AM, in person or online.",
  metadataBase: new URL(site.url),
  openGraph: {
    type: "website",
    locale: "en_US",
    siteName: site.name,
    title: `${site.name} | Florence, SC`,
    description:
      "A Spirit-filled church in Florence, South Carolina. He loves you to life, so we love you to life.",
  },
  twitter: {
    card: "summary_large_image",
    title: site.name,
    description:
      "A Spirit-filled church in Florence, South Carolina. He loves you to life, so we love you to life.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`${inter.variable} ${cormorant.variable}`}>
      <body>
        <a href="#main-content" className="skip-link">
          Skip to content
        </a>
        <Navigation />
        <main id="main-content">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
