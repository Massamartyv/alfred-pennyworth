import Link from "next/link";
import Image from "next/image";
import {
  DoorOpen,
  Compass,
  Sparkles,
  GraduationCap,
  Flame,
  ArrowRight,
} from "lucide-react";
import { site } from "@/lib/site";
import RevealSection from "@/components/RevealSection/RevealSection";
import ScriptureInterlude from "@/components/ScriptureInterlude/ScriptureInterlude";
import MinistryPlaceholder from "@/components/MinistryPlaceholder/MinistryPlaceholder";
import styles from "./page.module.css";

export const metadata = {
  title: "Our Ministries",
  description: `The ministries of ${site.name} — outreach, mentoring, formation and worship carrying the love of Christ across ${site.contact.address.city}, ${site.contact.address.state} and beyond.`,
};

/*
  CONFIRM: ministry leaders and the fuller description of each ministry.
  The names, types and any quoted mottos below come from the church's former
  website and are authoritative. Leader attributions carried over from that
  site are marked with an inline CONFIRM, since the church has since
  reorganised. Descriptions that go beyond the seed names, types and quotes are
  warm, plain-spoken inferences and should be confirmed with the church.
*/
const ministries = [
  {
    icon: DoorOpen,
    name: "SCORE",
    type: "Outreach",
    monogram: "S",
    // CONFIRM: leader attribution — the former site named Pastor Goodson; verify.
    leader: "Pastor Kelsey M. Goodson",
    desc: "A reentry ministry that walks alongside citizens returning home from incarceration — meeting them with support, dignity and a family to belong to as they begin again.",
  },
  {
    icon: Compass,
    name: "Is there Not a Cause",
    type: "Mentoring",
    monogram: "C",
    // CONFIRM: leader attribution — the former site named Pastor Goodson; verify.
    leader: "Pastor Kelsey M. Goodson",
    desc: "A mentoring ministry for those who are searching — coming alongside them with guidance, encouragement and people who believe in the cause God has set within them.",
  },
  {
    icon: Sparkles,
    name: "GEMS & GENTS",
    type: "Mentoring",
    monogram: "G&G",
    // CONFIRM: leader attribution — the former site named Pastor Goodson; verify.
    leader: "Pastor Kelsey M. Goodson",
    desc: "Mentoring for young adults — pouring into the next generation of women and men and helping them grow into all that God has called them to be.",
  },
  {
    icon: GraduationCap,
    name: "Sonship School of the Firstborn",
    type: "Formation",
    // CONFIRM: leader / teachers for this ministry.
    leader: null,
    motto: "Transforming Servants, to Sons",
    image: "/images/church/sonship-graduation.jpg",
    imageAlt:
      "The Sonship School of the Firstborn Class of 2021 in graduation robes at the Tower",
    desc: "Teaching and formation for those being shaped and matured in the faith — a school of the Spirit for the whole body.",
  },
  {
    icon: Flame,
    name: "Prophetic Impartation Service",
    type: "Worship",
    monogram: "P",
    // CONFIRM: who carries this service week to week.
    leader: null,
    schedule: "Saturdays · 10:00 AM · In house",
    desc: "A gathering where the Holy Spirit has its way, utilizing the speaker of the hour to bring forth what thus says the Lord.",
  },
] as const;

export default function MinistriesPage() {
  return (
    <>
      <RevealSection />

      {/* Hero */}
      <section className="global-page-hero">
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">Ministries</span>
          <h1 className="global-hero-title global-hero-title-light">
            Our Ministries
          </h1>
          <p className="global-page-hero-desc">
            The love of God does not stay inside our walls. Through these
            ministries the Tower family reaches out, mentors, teaches and
            worships &mdash; carrying His love to life in every place it is
            needed.
          </p>
        </div>
      </section>

      {/* The Word */}
      <ScriptureInterlude
        verse={site.scripture.verse}
        reference={site.scripture.reference}
        tone="light"
      />

      {/* Ministry grid */}
      <section className={`section ${styles.ministries}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="eyebrow">The work of the Tower</p>
            <h2 className={styles.sectionTitle}>
              Where His Love Takes Hold
            </h2>
            <p className={styles.sectionLede}>
              Each of these ministries is a hand extended in the name of Jesus.
              Some reach beyond our doors, some pour into the next generation,
              and some make room for the Spirit to move. All of them are the
              same love, given away.
            </p>
          </div>

          <div className={styles.grid}>
            {ministries.map((m, i) => {
              const Icon = m.icon;
              return (
                <article
                  key={m.name}
                  className={`${styles.card} reveal ${i % 2 === 1 ? "reveal-d1" : ""}`}
                >
                  <div className={`${styles.cardMedia} motion-float`}>
                    {"image" in m ? (
                      <Image
                        src={m.image}
                        alt={m.imageAlt}
                        fill
                        sizes="(max-width: 900px) 100vw, 50vw"
                        className={styles.cardMediaImg}
                      />
                    ) : (
                      <MinistryPlaceholder monogram={m.monogram} />
                    )}
                  </div>
                  <div className={styles.cardHead}>
                    <span className={styles.icon} aria-hidden="true">
                      <Icon size={24} />
                    </span>
                    <span className={styles.type}>{m.type}</span>
                  </div>

                  <h3 className={styles.name}>{m.name}</h3>

                  {"motto" in m && m.motto ? (
                    <p className={styles.motto}>
                      &ldquo;{m.motto}&rdquo;
                    </p>
                  ) : null}

                  <p className={styles.desc}>{m.desc}</p>

                  <div className={styles.meta}>
                    {"schedule" in m && m.schedule ? (
                      <p className={styles.schedule}>{m.schedule}</p>
                    ) : null}
                    {m.leader ? (
                      <p className={styles.leader}>
                        <span className={styles.leaderLabel}>Blessed to deliver it</span>
                        {m.leader}
                      </p>
                    ) : null}
                  </div>
                </article>
              );
            })}
          </div>
        </div>
      </section>

      {/* Closing CTA */}
      <section className={styles.ctaBand}>
        <div className={`container ${styles.ctaInner} reveal`}>
          <h2 className={styles.ctaTitle}>There Is a Place for You Here</h2>
          <p className={styles.ctaCopy}>
            If the Lord is stirring something in you, come and serve alongside
            us. Meet the leaders who shepherd this family, or take your first
            step toward a ministry that fits your heart.
          </p>
          <div className={styles.ctaActions}>
            <Link href="/get-involved" className="btn btn-primary">
              Find your place <ArrowRight size={18} />
            </Link>
            <Link href="/leadership" className="btn btn-secondary">
              Meet our leadership <ArrowRight size={18} />
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
