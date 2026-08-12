import Link from "next/link";
import { Calendar, Clock, ArrowRight } from "lucide-react";
import { FacebookIcon, YoutubeIcon } from "@/components/SocialIcons";
import { site } from "@/lib/site";
import RevealSection from "@/components/RevealSection/RevealSection";
import Newsletter from "@/components/Newsletter/Newsletter";
import styles from "./page.module.css";

export const metadata = {
  title: "What's Happening @ the Tower",
  description:
    "Weekly gatherings and upcoming events at Strong Tower Christian Ministry in Florence, SC. Find a time to gather with us, in person and online.",
};

export default function EventsPage() {
  return (
    <>
      <RevealSection />

      {/* Hero */}
      <section className="global-page-hero">
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">What&apos;s happening</span>
          <h1 className="global-hero-title global-hero-title-light">
            What&apos;s Happening @ the Tower
          </h1>
          <p className="global-page-hero-desc">
            There is always a place at the table. Gather with us each week, and
            keep an eye here for the special moments God is preparing for our
            church family.
          </p>
        </div>
      </section>

      {/* Weekly gatherings */}
      <section className={`section ${styles.weekly}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="eyebrow">Every week</p>
            <h2 className={styles.sectionTitle}>Our Weekly Gatherings</h2>
            <p className={styles.sectionLede}>
              These are the rhythms of the Tower. Come as you are, whether it is
              your first time or your hundredth.
            </p>
          </div>

          <div className={styles.weeklyGrid}>
            {site.services.map((s) => (
              <article key={s.name} className={`${styles.weeklyCard} reveal`}>
                <p className={styles.weeklyDay}>{s.day}</p>
                <h3 className={styles.weeklyName}>{s.name}</h3>
                <p className={styles.weeklyTime}>
                  <Clock size={18} aria-hidden="true" /> {s.time}
                </p>
                <p className={styles.weeklyMode}>{s.mode}</p>
              </article>
            ))}
          </div>
        </div>
      </section>

      {/* Upcoming events — empty state */}
      <section className={`section ${styles.upcoming}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="eyebrow">On the calendar</p>
            <h2 className={styles.sectionTitle}>Upcoming Events</h2>
          </div>

          {/*
            CONFIRM: events will be CMS-managed via Keystatic; this is the
            empty-state design. When events exist, map them into a grid of
            .eventCard articles in place of this empty state.
          */}
          <div className={`${styles.emptyState} reveal`}>
            <span className={styles.emptyIcon} aria-hidden="true">
              <Calendar size={32} />
            </span>
            <h3 className={styles.emptyTitle}>
              More Events Are on the Way &mdash; Check Back Soon
            </h3>
            <p className={styles.emptyCopy}>
              We are planning gatherings, services and special occasions for the
              season ahead. Subscribe below and we will let you know the moment
              the calendar fills in.
            </p>
            <Link href="/visit" className="btn btn-secondary">
              Plan your visit <ArrowRight size={18} />
            </Link>
          </div>
        </div>
      </section>

      {/* Stay notified band */}
      <section className={styles.notifyBand}>
        <div className={`container ${styles.notifyInner}`}>
          <div className={`${styles.notifyText} reveal`}>
            <p className="eyebrow">Never miss a moment</p>
            <h2 className={styles.notifyTitle}>
              Be the First to Know What&apos;s Next
            </h2>
            <p className={styles.notifyCopy}>
              Get announcements, events and a word of encouragement delivered to
              your inbox. You can also follow along with us on social media for
              services and updates throughout the week.
            </p>
            <div className={styles.socialLinks}>
              <a
                href={site.social.facebook}
                target="_blank"
                rel="noopener noreferrer"
                className={styles.socialLink}
              >
                <FacebookIcon size={18} /> Facebook
              </a>
              <a
                href={site.social.youtube}
                target="_blank"
                rel="noopener noreferrer"
                className={styles.socialLink}
              >
                <YoutubeIcon size={18} /> YouTube
              </a>
            </div>
          </div>
          <div className={`${styles.notifyForm} reveal`}>
            <Newsletter compact />
          </div>
        </div>
      </section>
    </>
  );
}
