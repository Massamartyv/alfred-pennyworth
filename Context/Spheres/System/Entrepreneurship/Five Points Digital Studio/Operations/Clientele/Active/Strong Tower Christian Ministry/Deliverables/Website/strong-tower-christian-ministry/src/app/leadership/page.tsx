import Link from "next/link";
import { ArrowRight } from "lucide-react";
import { site } from "@/lib/site";
import RevealSection from "@/components/RevealSection/RevealSection";
import styles from "./page.module.css";

export const metadata = {
  title: "Our Leadership",
  description: `Meet the leaders of ${site.name} — Pastor Kelsey M. Goodson and Prophetess Angela Goodson, shepherding the Tower family in ${site.contact.address.city}, ${site.contact.address.state}.`,
};

const leaders = [
  {
    initials: "KG",
    name: "Pastor Kelsey M. Goodson",
    role: "Pastor",
    bio: [
      "Pastor Kelsey M. Goodson was born and raised in Darlington, SC to Argie M. Goodson.",
      "He is a graduate of Mayo High School, class of 1989.",
    ],
  },
  {
    initials: "AG",
    name: "Prophetess Angela Goodson",
    role: "Prophetess",
    bio: [
      "Prophetess Angela Goodson is the wife of Pastor Kelsey Goodson.",
      "Together they are the parents of two daughters, Chelsea and Naudia.",
    ],
  },
];

export default function LeadershipPage() {
  return (
    <>
      <RevealSection />

      {/* Hero */}
      <section className="global-page-hero">
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">Leadership</span>
          <h1 className="global-hero-title global-hero-title-light">
            Our Leadership
          </h1>
          <p className="global-page-hero-desc">
            The Tower is shepherded by leaders who love this family the way
            Christ has loved us. Meet the hearts behind the ministry.
          </p>
        </div>
      </section>

      {/* Leader cards */}
      <section className={`section ${styles.leaders}`}>
        <div className="container">
          <div className={styles.leaderGrid}>
            {leaders.map((leader) => (
              <article key={leader.name} className={`${styles.leaderCard} reveal`}>
                {/* CONFIRM: leader photos and any additional leaders */}
                <div className={styles.portrait} aria-hidden="true">
                  <span className={styles.monogram}>{leader.initials}</span>
                </div>
                <div className={styles.leaderBody}>
                  <p className={styles.leaderRole}>{leader.role}</p>
                  <h2 className={styles.leaderName}>{leader.name}</h2>
                  {leader.bio.map((line) => (
                    <p key={line} className={styles.leaderBio}>
                      {line}
                    </p>
                  ))}
                </div>
              </article>
            ))}
          </div>

          <p className={`${styles.moreNote} reveal`}>
            More of the Tower family — our ministry leaders and those who serve
            this body — will be added here soon.
            {/* CONFIRM: additional ministry leaders, names and roles */}
          </p>
        </div>
      </section>

      {/* Closing CTA */}
      <section className={`section ${styles.cta}`}>
        <div className={`container ${styles.ctaInner} reveal`}>
          <h2 className={styles.ctaTitle}>We would love to meet you</h2>
          <p className={styles.ctaBody}>
            Plan a visit and worship with us, or reach out with any question —
            our door and our hearts are open.
          </p>
          <div className={styles.ctaActions}>
            <Link href="/visit" className="btn btn-primary">
              Plan your visit <ArrowRight size={18} />
            </Link>
            <Link href="/contact" className="btn btn-secondary">
              Get in touch <ArrowRight size={18} />
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
