import Link from "next/link";
import {
  ArrowRight,
  MapPin,
  Heart,
  Music,
  BookOpen,
  HandHeart,
  Clock,
  Shirt,
  Baby,
  Car,
} from "lucide-react";
import { site } from "@/lib/site";
import RevealSection from "@/components/RevealSection/RevealSection";
import VideoSlot from "@/components/Motion/VideoSlot";
import styles from "./page.module.css";

export const metadata = {
  title: "Plan Your Visit",
  description: `Planning your first visit to ${site.name} in ${site.contact.address.city}, ${site.contact.address.state}? Here is what to expect, when we gather and how to find us. We saved you a seat.`,
};

const expectations = [
  {
    icon: Heart,
    title: "Come as You Are",
    body: "No dress code, no pretense, no perfect record required. Walk in exactly as you are — you are welcome at the Tower.",
  },
  {
    icon: Music,
    title: "Heartfelt Worship",
    body: "We make room for the presence of God in worship — a time to sing, lift your hands and simply be with Him.",
  },
  {
    icon: BookOpen,
    title: "The Word, Preached",
    body: "At the center of everything is the Word of God, taught plainly and lived out — something to carry into your week.",
  },
  {
    icon: HandHeart,
    title: "Prayer for You",
    body: "Whatever you are carrying, you do not carry it alone. There is always someone ready to stand and pray with you.",
  },
];

const quickAnswers = [
  {
    icon: Shirt,
    title: "What Should I Wear?",
    body: "Whatever you are comfortable in. Some dress up, many keep it casual — either way you will fit right in.",
  },
  {
    icon: Baby,
    title: "Are Kids Welcome?",
    body: "Absolutely. Children are a gift to this family and are welcome in the service with you.",
    // CONFIRM: kids/childcare specifics — dedicated children's ministry, ages, check-in
  },
  {
    icon: Car,
    title: "Where Do I Park?",
    body: "Parking is available on site. Arrive a few minutes early and a friendly face will help you find your way in.",
    // CONFIRM: parking specifics — lot location, accessibility, overflow
  },
];

export default function VisitPage() {
  return (
    <>
      <RevealSection />

      {/* Hero */}
      <section className="global-page-hero">
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">Plan your visit</span>
          <h1 className="global-hero-title global-hero-title-light">
            We Saved You a Seat
          </h1>
          <p className="global-page-hero-desc">
            Walking into a new church can feel like a big step. Take a breath —
            here is everything you need to know before your first visit, so you
            can show up and simply be welcomed.
          </p>
        </div>
      </section>

      {/* What to expect */}
      <section className={`section ${styles.expect}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="eyebrow">What to expect</p>
            <h2 className={styles.sectionTitle}>Your First Time with Us</h2>
            <p className={styles.lead}>
              A service usually runs around 90 minutes — unhurried, warm and
              centered on Christ. Expect worship, the preaching of the Word and
              time for prayer. On Saturdays we also gather for Prophetic
              Impartation, a focused time of seeking God together.
            </p>
            {/* CONFIRM: typical service length */}
          </div>
          <div className={styles.expectGrid}>
            {expectations.map((e, i) => {
              const Icon = e.icon;
              return (
                <article
                  key={e.title}
                  className={`${styles.expectCard} reveal reveal-d${i + 1}`}
                >
                  <span className={styles.expectIcon} aria-hidden="true">
                    <Icon size={22} />
                  </span>
                  <h3 className={styles.expectTitle}>{e.title}</h3>
                  <p className={styles.expectBody}>{e.body}</p>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      {/* Service times */}
      <section className={`section ${styles.services}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="eyebrow">When we gather</p>
            <h2 className={styles.sectionTitle}>Service Times</h2>
          </div>
          <div className={styles.serviceGrid}>
            {site.services.map((s) => (
              <article key={s.name} className={`${styles.serviceCard} reveal`}>
                <p className={styles.serviceDay}>{s.day}</p>
                <h3 className={styles.serviceName}>{s.name}</h3>
                <p className={styles.serviceTime}>
                  <Clock size={16} aria-hidden="true" /> {s.time}
                </p>
                <p className={styles.serviceMode}>{s.mode}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      {/* Before you come */}
      <section className={`section ${styles.before}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="eyebrow">Before you come</p>
            <h2 className={styles.sectionTitle}>A Few Quick Answers</h2>
          </div>
          <div className={styles.answerGrid}>
            {quickAnswers.map((q, i) => {
              const Icon = q.icon;
              return (
                <article
                  key={q.title}
                  className={`${styles.answerCard} reveal reveal-d${i + 1}`}
                >
                  <span className={styles.answerIcon} aria-hidden="true">
                    <Icon size={20} />
                  </span>
                  <div>
                    <h3 className={styles.answerTitle}>{q.title}</h3>
                    <p className={styles.answerBody}>{q.body}</p>
                  </div>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      {/* Atmospheric interlude — the church praying together, the church's own
          footage. Poster is the fallback, so there is no layout shift and
          reduced-motion holds on the still. */}
      <section className={styles.interlude} aria-hidden="true">
        <VideoSlot
          poster="/images/church/prayer-ministry-poster.jpg"
          videoSrc="/videos/prayer-ministry.mp4"
          alt=""
          sizes="100vw"
          imgClassName={styles.interludeImg}
          motion="ken-burns"
        />
        <div className={styles.interludeScrim} />
        <div className={styles.interludeGrain} />
      </section>

      {/* Location */}
      <section className={`section ${styles.location}`}>
        <div className={`container ${styles.locationInner}`}>
          <div className={`${styles.locationText} reveal`}>
            <p className="eyebrow">Find the Tower</p>
            <h2 className={styles.sectionTitle}>Where to Find Us</h2>
            <address className={styles.locationAddr}>
              <MapPin size={18} aria-hidden="true" /> {site.contact.full}
            </address>
            <p className={styles.bodyLg}>
              We are easy to find in {site.contact.address.city}. When you
              arrive, look for a welcoming face near the entrance — they will be
              glad you came.
            </p>
            <a
              href={site.contact.mapsUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="btn btn-secondary"
            >
              Get directions <ArrowRight size={18} />
            </a>
          </div>
          <div className={`${styles.mapWrap} reveal`}>
            <iframe
              src={site.contact.mapsEmbed}
              title={`Map to ${site.name}`}
              loading="lazy"
              referrerPolicy="no-referrer-when-downgrade"
              className={styles.map}
            />
          </div>
        </div>
      </section>

      {/* Closing CTA */}
      <section className={styles.ctaBand}>
        <div className={`container ${styles.ctaInner} reveal`}>
          <h2 className={styles.ctaTitle}>Questions before You Come?</h2>
          <p className={styles.ctaBody}>
            Reach out — we would love to hear from you and help however we can
            before your first visit.
          </p>
          <Link href="/contact" className="btn btn-primary">
            Reach out <ArrowRight size={18} />
          </Link>
        </div>
      </section>
    </>
  );
}
