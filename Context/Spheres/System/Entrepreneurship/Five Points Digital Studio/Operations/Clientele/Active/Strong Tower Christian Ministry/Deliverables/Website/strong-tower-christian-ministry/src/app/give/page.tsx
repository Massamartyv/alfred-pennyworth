import Link from "next/link";
import {
  Heart,
  Globe,
  MapPin,
  Mail,
  Clock,
  ArrowRight,
} from "lucide-react";
import { site } from "@/lib/site";
import RevealSection from "@/components/RevealSection/RevealSection";
import styles from "./page.module.css";

export const metadata = {
  title: "Give",
  description:
    "Partner with the work of Strong Tower Christian Ministry through your tithes and offering. Give online, in person or by mail.",
};

export default function GivePage() {
  const givingUrl = site.giving.url;

  return (
    <>
      <RevealSection />

      {/* Hero */}
      <section className="global-page-hero">
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">Give</span>
          <h1 className="global-hero-title global-hero-title-light">Give</h1>
          <p className="global-page-hero-desc">
            Generosity is worship. When you give to the Tower, you help us
            preach the Word, serve our city and love people to life. Thank you
            for partnering with this ministry.
          </p>
        </div>
      </section>

      {/* Scripture */}
      <section className={styles.scriptureBand}>
        <div className="container">
          <p className={`scripture ${styles.scriptureText}`}>
            &ldquo;Each of you should give what you have decided in your heart to
            give, not reluctantly or under compulsion, for God loves a cheerful
            giver.&rdquo;
          </p>
          <p className={styles.scriptureRef}>2 Corinthians 9:7</p>
        </div>
      </section>

      {/* Ways to give */}
      <section className={`section ${styles.ways}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="eyebrow">Ways to give</p>
            <h2 className={styles.sectionTitle}>Three simple ways</h2>
            <p className={styles.sectionLede}>
              Give whichever way is easiest for you. Every gift, large or small,
              makes a difference.
            </p>
          </div>

          <div className={styles.waysGrid}>
            {/* Online — swap-slot */}
            <article className={`${styles.wayCard} reveal`}>
              <span className={styles.wayIcon} aria-hidden="true">
                <Globe size={24} />
              </span>
              <h3 className={styles.wayTitle}>Online</h3>
              {givingUrl ? (
                <>
                  <p className={styles.wayDesc}>
                    Give securely from anywhere in just a few moments. Set up a
                    one-time gift or make it recurring.
                  </p>
                  <a
                    href={givingUrl}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn btn-primary"
                  >
                    Give online <ArrowRight size={18} />
                  </a>
                </>
              ) : (
                <>
                  {/* CONFIRM: online giving destination — set NEXT_PUBLIC_GIVING_URL to enable the live button */}
                  <p className={styles.wayDesc}>
                    Online giving is coming soon. For now, you can give in person
                    at any service or by mail using the details here.
                  </p>
                  <Link href="/contact" className="btn btn-secondary">
                    Questions? Contact us <ArrowRight size={18} />
                  </Link>
                </>
              )}
            </article>

            {/* In person */}
            <article className={`${styles.wayCard} reveal`}>
              <span className={styles.wayIcon} aria-hidden="true">
                <MapPin size={24} />
              </span>
              <h3 className={styles.wayTitle}>In person</h3>
              <p className={styles.wayDesc}>
                Bring your tithes and offering with you when we gather. You are
                welcome to give at any of our services:
              </p>
              <ul className={styles.serviceList}>
                {site.services.map((s) => (
                  <li key={s.name} className={styles.serviceItem}>
                    <Clock size={16} aria-hidden="true" />
                    <span>
                      <strong>{s.day}</strong> &middot; {s.time}
                    </span>
                  </li>
                ))}
              </ul>
            </article>

            {/* By mail */}
            <article className={`${styles.wayCard} reveal`}>
              <span className={styles.wayIcon} aria-hidden="true">
                <Mail size={24} />
              </span>
              <h3 className={styles.wayTitle}>By mail</h3>
              <p className={styles.wayDesc}>
                Prefer to send a check? Mail your gift to the church office at:
              </p>
              <address className={styles.mailAddr}>{site.contact.full}</address>
            </article>
          </div>
        </div>
      </section>

      {/* A word on giving */}
      <section className={`section ${styles.word}`}>
        <div className={`container ${styles.wordInner} reveal`}>
          <span className={styles.wordIcon} aria-hidden="true">
            <Heart size={28} />
          </span>
          <h2 className={styles.wordTitle}>
            Your generosity moves the ministry forward
          </h2>
          <p className={styles.wordCopy}>
            Tithes and offerings are how we keep the doors of the Tower open and
            the work of God moving. Through your faithfulness, the gospel is
            preached, our church family is cared for and the love of Christ
            reaches further into our community. We never take that partnership
            for granted &mdash; thank you for giving with a willing and cheerful
            heart.
          </p>
        </div>
      </section>

      {/* Closing CTA */}
      <section className={styles.ctaBand}>
        <div className={`container ${styles.ctaInner} reveal`}>
          <h2 className={styles.ctaTitle}>Have a question about giving?</h2>
          <p className={styles.ctaCopy}>
            We are glad to help. Reach out to the church office and we will get
            back to you.
          </p>
          <Link href="/contact" className="btn btn-primary">
            Contact us <ArrowRight size={18} />
          </Link>
        </div>
      </section>
    </>
  );
}
