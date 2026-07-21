import Link from "next/link";
import {
  Music,
  HandHeart,
  Coffee,
  Globe,
  Baby,
  Video,
  ArrowRight,
} from "lucide-react";
import RevealSection from "@/components/RevealSection/RevealSection";
import styles from "./page.module.css";

export const metadata = {
  title: "Find Your Place",
  description:
    "There is a place for you at Strong Tower Christian Ministry. Discover ways to serve, connect and grow with our church family in Florence, SC.",
};

/*
  CONFIRM: the serving areas below are warm, generic invitations to serve until
  the real teams and team leaders are set. The church's named ministries and
  their leaders now live on the dedicated /ministries page.
*/
const ministries = [
  {
    icon: Music,
    title: "Worship & Arts",
    desc: "Lift the name of Jesus through music, song and creative expression. Singers, musicians and tech all have a home here.",
  },
  {
    icon: HandHeart,
    title: "Prayer & Intercession",
    desc: "Stand in the gap for our church, our city and the world. Join a team devoted to seeking God on behalf of others.",
  },
  {
    icon: Coffee,
    title: "Hospitality & Welcome",
    desc: "Be the first smile a guest sees. Greet, host and help every person who walks through our doors feel at home.",
  },
  {
    icon: Globe,
    title: "Outreach",
    desc: "Carry the love of Christ beyond our walls. Serve our neighbours and meet practical needs across the community.",
  },
  {
    icon: Baby,
    title: "Youth & Children",
    desc: "Pour into the next generation. Teach, mentor and create safe, joyful spaces where young hearts can meet Jesus.",
  },
  {
    icon: Video,
    title: "Media",
    desc: "Help us reach people near and far. Run our livestream, capture moments and share the message online.",
  },
];

const steps = [
  {
    num: "01",
    title: "Come and gather",
    desc: "Join us for a service and simply be present. The best first step is showing up and worshipping with us.",
  },
  {
    num: "02",
    title: "Say hello",
    desc: "Let us know you would like to get involved. Reach out and tell us a little about where you feel led to serve.",
  },
  {
    num: "03",
    title: "Find your team",
    desc: "We will help you take the next step toward a ministry where your gifts and your heart fit best.",
  },
];

export default function GetInvolvedPage() {
  return (
    <>
      <RevealSection />

      {/* Hero */}
      <section className="global-page-hero">
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">Get involved</span>
          <h1 className="global-hero-title global-hero-title-light">
            Find Your Place
          </h1>
          <p className="global-page-hero-desc">
            You were never meant to do faith alone. There is a place for you to
            belong, to serve and to grow at the Tower &mdash; and we would love
            to help you find it.
          </p>
        </div>
      </section>

      {/* Ways to serve */}
      <section className={`section ${styles.serve}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="eyebrow">Ways to serve</p>
            <h2 className={styles.sectionTitle}>Where will you serve?</h2>
            <p className={styles.sectionLede}>
              Every gift matters and every hand is needed. Explore a few of the
              ways you can give your time and talent to the body of Christ.
            </p>
          </div>

          <div className={styles.serveGrid}>
            {ministries.map((m) => {
              const Icon = m.icon;
              return (
                <article key={m.title} className={`${styles.serveCard} reveal`}>
                  <span className={styles.serveIcon} aria-hidden="true">
                    <Icon size={24} />
                  </span>
                  <h3 className={styles.serveTitle}>{m.title}</h3>
                  <p className={styles.serveDesc}>{m.desc}</p>
                </article>
              );
            })}
          </div>

          <p className={`${styles.serveMore} reveal`}>
            Want to see the ministries of the Tower?{" "}
            <Link href="/ministries" className="link-arrow">
              Explore our ministries <ArrowRight size={16} />
            </Link>
          </p>
        </div>
      </section>

      {/* Next steps */}
      <section className={`section ${styles.steps}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="eyebrow">Next steps</p>
            <h2 className={styles.sectionTitle}>How to get connected</h2>
            <p className={styles.sectionLede}>
              Getting plugged in is simpler than you might think. Here is how it
              works.
            </p>
          </div>

          <ol className={styles.stepsGrid}>
            {steps.map((step) => (
              <li key={step.num} className={`${styles.stepCard} reveal`}>
                <span className={styles.stepNum}>{step.num}</span>
                <h3 className={styles.stepTitle}>{step.title}</h3>
                <p className={styles.stepDesc}>{step.desc}</p>
              </li>
            ))}
          </ol>
        </div>
      </section>

      {/* Closing CTA */}
      <section className={styles.ctaBand}>
        <div className={`container ${styles.ctaInner} reveal`}>
          <h2 className={styles.ctaTitle}>Let&apos;s get you connected</h2>
          <p className={styles.ctaCopy}>
            Tell us you are interested and we will walk with you from here. Your
            place at the Tower is waiting.
          </p>
          <Link href="/contact" className="btn btn-primary">
            Get connected <ArrowRight size={18} />
          </Link>
        </div>
      </section>
    </>
  );
}
