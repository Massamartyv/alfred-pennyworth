import Link from "next/link";
import { ArrowRight, BookOpen, Flame, Users, Send } from "lucide-react";
import { site } from "@/lib/site";
import RevealSection from "@/components/RevealSection/RevealSection";
import styles from "./page.module.css";

export const metadata = {
  title: "Our Story",
  description: `${site.name} is a Spirit-filled, prophetic church family in ${site.contact.address.city}, ${site.contact.address.state}, centered on the Word of God and led by Pastor Kelsey and Prophetess Angela Goodson.`,
};

const values = [
  {
    icon: BookOpen,
    title: "Word-Centered",
    body: "We are a church body dependent on the Word of God — preaching it, teaching it and living it in all we do.",
  },
  {
    icon: Flame,
    title: "Spirit-Led",
    body: "We make room for the presence of God, expecting Him to move, heal and speak in the life of every believer.",
  },
  {
    icon: Users,
    title: "Family",
    body: "There is room for you here. We grow together as one body, carrying one another in love.",
  },
  {
    icon: Send,
    title: "Sent",
    body: "We strive to be ambassadors for Christ, taking His love beyond these walls into the world.",
  },
];

export default function AboutPage() {
  return (
    <>
      <RevealSection />

      {/* Hero */}
      <section className="global-page-hero">
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">About</span>
          <h1 className="global-hero-title global-hero-title-light">
            Our Story
          </h1>
          <p className="global-page-hero-desc">
            A Spirit-filled family in {site.contact.address.city}, South
            Carolina, gathered around the Word of God and the love He has shown
            us. Here is who we are and why we do what we do.
          </p>
        </div>
      </section>

      {/* Scripture band */}
      <section className={styles.scriptureBand}>
        <div className="container">
          <p className={`scripture ${styles.scriptureText}`}>
            &ldquo;{site.scripture.verse}&rdquo;
          </p>
          <p className={styles.scriptureRef}>{site.scripture.reference}</p>
        </div>
      </section>

      {/* Mission */}
      <section className={`section ${styles.statement}`}>
        <div className={`container ${styles.statementInner} reveal`}>
          <p className="eyebrow">Our mission</p>
          <h2 className={styles.statementTitle}>Ambassadors for Christ</h2>
          <p className={styles.statementBody}>
            We the Strong Tower Christian Ministries strive to be ambassadors
            for Christ. This is accomplished in harmonious phases. We are a
            church body that is dependent on the Word of God through preaching,
            teaching, and displaying the Word of God in all we do.
          </p>
        </div>
      </section>

      {/* Vision */}
      <section className={`section ${styles.vision}`}>
        <div className={`container ${styles.statementInner} reveal`}>
          <p className="eyebrow">Our vision</p>
          <h2 className={styles.statementTitle}>Growing in His Love</h2>
          <p className={styles.statementBody}>
            To provide an environment for each person to grow in the knowledge
            of Jesus Christ and demonstrate that same love He has shown to all
            creations.
          </p>
        </div>
      </section>

      {/* Who we are */}
      <section className={`section ${styles.story}`}>
        <div className={`container ${styles.storyInner}`}>
          <div className={`${styles.storyText} reveal`}>
            <p className="eyebrow">Who we are</p>
            <h2 className={styles.sectionTitle}>A Place to Run To</h2>
            <p className={styles.bodyLg}>
              Strong Tower Christian Ministry is a Spirit-filled, prophetic
              church family in {site.contact.address.city}, South Carolina. We
              are centered on the Word of God — preached, taught and lived — and
              we believe the name of the Lord is a strong tower the righteous
              can run to and be safe.
            </p>
            <p className={styles.bodyLg}>
              The Tower is led by Pastor Kelsey M. Goodson and Prophetess Angela
              Goodson, who shepherd this body with the same love Christ has shown
              us. Wherever you are on the journey, you will find a seat saved for
              you and a family ready to grow alongside you.
            </p>
            {/* CONFIRM: founding year and fuller history */}
            <div className={styles.storyActions}>
              <Link href="/leadership" className="btn btn-secondary">
                Meet our leadership <ArrowRight size={18} />
              </Link>
            </div>
          </div>
          <aside className={`${styles.tagCard} motion-float reveal`}>
            <p className={styles.tagPrimary}>
              &ldquo;{site.taglines.primary}.&rdquo;
            </p>
            <p className={styles.tagSecondary}>{site.taglines.secondary}.</p>
          </aside>
        </div>
      </section>

      {/* Values */}
      <section className={`section ${styles.values}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="eyebrow">What we hold to</p>
            <h2 className={styles.sectionTitle}>The Heart of the Tower</h2>
          </div>
          <div className={styles.valueGrid}>
            {values.map((v) => {
              const Icon = v.icon;
              return (
                <article key={v.title} className={`${styles.valueCard} reveal`}>
                  <span className={styles.valueIcon} aria-hidden="true">
                    <Icon size={22} />
                  </span>
                  <h3 className={styles.valueTitle}>{v.title}</h3>
                  <p className={styles.valueBody}>{v.body}</p>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      {/* Closing CTA */}
      <section className={styles.ctaBand}>
        <div className={`container ${styles.ctaInner} reveal`}>
          <h2 className={styles.ctaTitle}>Come and See for Yourself</h2>
          <p className={styles.ctaBody}>
            Read the faith we stand on, or plan a visit and meet the family in
            person.
          </p>
          <div className={styles.ctaActions}>
            <Link href="/what-we-believe" className={`btn ${styles.ctaGhost}`}>
              What we believe <ArrowRight size={18} />
            </Link>
            <Link href="/visit" className="btn btn-primary">
              Plan your visit <ArrowRight size={18} />
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
