import Link from "next/link";
import Image from "next/image";
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
    photo: "/images/church/pastor-kelsey-goodson.jpg",
    photoAlt:
      "Pastor Kelsey M. Goodson at the Strong Tower sanctuary, before the church's Strong Tower wall",
    name: "Pastor Kelsey M. Goodson",
    role: "Senior Pastor",
    bio: [
      "Pastor Kelsey M. Goodson was born and raised in Darlington, South Carolina, and graduated from Mayo High School in 1989. He gave 22 years of his life to the service of his country as a soldier in the United States Army.",
      "In 2001 he gave his life to Christ, and in 2015 he answered the call to preach. He went on to complete his studies at the Sonship School of the Firstborn in Killeen, Texas, and was licensed and ordained under Covenant Connection International.",
      "He and Prophetess Angela Goodson have been married for 29 years. Together they are the parents of two daughters and are blessed with a son-in-law. He shepherds the Tower family with a soldier's steadiness and a father's heart.",
    ],
  },
  {
    initials: "AG",
    photo: "/images/church/prophetess-angela-goodson.jpg",
    photoAlt:
      "Prophetess Angela Goodson at the Strong Tower sanctuary, before the church's Strong Tower wall",
    name: "Prophetess Angela Goodson",
    role: "Prophetess",
    bio: [
      "Prophetess Angela Goodson stands beside Pastor Goodson as his wife of 29 years and as mother to their two daughters, Chelsea and Naudia.",
      "Down-to-earth, approachable and transparent, she is known throughout the congregation for her encouragement and her watchful, caring oversight. She meets people right where they are, and the Tower family is warmer for her presence.",
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
                <div className={styles.portrait}>
                  <Image
                    src={leader.photo}
                    alt={leader.photoAlt}
                    fill
                    sizes="(max-width: 900px) 100vw, 50vw"
                    className={styles.portraitImg}
                  />
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
