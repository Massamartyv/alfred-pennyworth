import type { Metadata } from "next";
import { MapPin, Phone, Mail } from "lucide-react";
import { site } from "@/lib/site";
import RevealSection from "@/components/RevealSection/RevealSection";
import ContactForm from "./contact-form";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "Contact",
  description:
    "Reach Strong Tower Christian Ministry in Florence, SC. Call, email or send a message and we will get back to you.",
};

export default function ContactPage() {
  return (
    <>
      <RevealSection />

      <section className="global-page-hero">
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">Contact</span>
          <h1 className="global-hero-title global-hero-title-light">
            Get in Touch
          </h1>
          <p className="global-page-hero-desc">
            Questions, prayer or planning a first visit — we would love to hear
            from you.
          </p>
        </div>
      </section>

      <section className="section">
        <div className={`container ${styles.grid}`}>
          <div className={`${styles.formCol} reveal`}>
            <h2 className={styles.h2}>Send a Message</h2>
            <ContactForm />
          </div>

          <aside className={`${styles.infoCol} reveal`}>
            <div className={styles.infoCard}>
              <h3 className={styles.infoTitle}>Reach Us</h3>
              <ul className={styles.infoList}>
                <li>
                  <Phone size={18} />
                  <a href={site.contact.phoneHref}>{site.contact.phone}</a>
                </li>
                <li>
                  <Mail size={18} />
                  <a href={site.contact.emailHref}>{site.contact.email}</a>
                </li>
                <li>
                  <MapPin size={18} />
                  <a
                    href={site.contact.mapsUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {site.contact.full}
                  </a>
                </li>
              </ul>
            </div>

            <div className={styles.infoCard}>
              <h3 className={styles.infoTitle}>Service Times</h3>
              <ul className={styles.svcList}>
                {site.services.map((s) => (
                  <li key={s.name}>
                    <span>{s.name}</span>
                    <span className={styles.svcTime}>
                      {s.day} · {s.time}
                    </span>
                  </li>
                ))}
              </ul>
            </div>

            <div className={styles.mapWrap}>
              <iframe
                src={site.contact.mapsEmbed}
                title={`Map to ${site.name}`}
                loading="lazy"
                referrerPolicy="no-referrer-when-downgrade"
                className={styles.map}
              />
            </div>
          </aside>
        </div>
      </section>
    </>
  );
}
