import type { Metadata } from "next";
import Link from "next/link";
import { ArrowRight } from "lucide-react";
import RevealSection from "@/components/RevealSection/RevealSection";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "What We Believe",
  description:
    "The faith we stand on at Strong Tower Christian Ministry — our Confession of Faith and the heart of Sonship.",
};

/*
  CONFIRM: The Confession of Faith and the Sonship teaching below are Five Points
  drafts prepared for pastoral approval. Align the wording with the church's
  specific doctrine before launch.
*/

const beliefs = [
  {
    title: "The Scriptures",
    text: "The Bible is the inspired, infallible Word of God and our final authority for faith and life.",
    ref: "2 Timothy 3:16",
  },
  {
    title: "One God",
    text: "One God, eternally existing in three persons: Father, Son and Holy Spirit.",
    ref: "Matthew 28:19",
  },
  {
    title: "Jesus Christ",
    text: "Fully God and fully man, born of a virgin, crucified for our sin, risen and coming again.",
    ref: "John 1:1, 14",
  },
  {
    title: "Salvation",
    text: "We are saved by grace through faith in Jesus Christ alone, not by works, so that no one can boast.",
    ref: "Ephesians 2:8-9",
  },
  {
    title: "The Holy Spirit",
    text: "The Holy Spirit indwells, empowers and gifts every believer for life and ministry.",
    ref: "Acts 1:8",
  },
  {
    title: "The Church",
    text: "The Church is the body of Christ, called to worship, grow and serve together in love.",
    ref: "1 Corinthians 12",
  },
  {
    title: "Baptism and Communion",
    text: "We practice water baptism and the Lord's Supper as Christ commanded.",
    ref: "Matthew 28:19",
  },
  {
    title: "The Prophetic",
    text: "God still speaks. The gifts of the Spirit are active today to edify, encourage and impart.",
    ref: "1 Corinthians 14:1",
  },
  {
    title: "Healing and Wholeness",
    text: "By His wounds we are healed. God restores us in body, soul and spirit.",
    ref: "Isaiah 53:5",
  },
  {
    title: "Our Hope",
    text: "Jesus will return, and we live in the certain hope of eternal life with God.",
    ref: "1 Thessalonians 4:16-17",
  },
];

const sonship = [
  "At the heart of the Tower is one conviction: the Father loves you to life. The gospel is not only forgiveness from sin, it is adoption into a family.",
  "In Christ you are not a servant earning a place. You are a son, a daughter, fully received and fully loved. The same Spirit that raised Jesus now teaches you to call God Father.",
  "Sonship is growing up into that identity: learning to live loved, to know the Father's voice, and to carry His likeness into the world. It is why we say, He loves you to life, so we love you to life.",
];

export default function WhatWeBelievePage() {
  return (
    <>
      <RevealSection />

      <section className="global-page-hero">
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">What we believe</span>
          <h1 className="global-hero-title global-hero-title-light">
            The Faith We Stand On
          </h1>
          <p className="global-page-hero-desc">
            Rooted in the Word, alive in the Spirit, anchored in the love of the
            Father.
          </p>
        </div>
      </section>

      {/* Confession of Faith */}
      <section className={`section ${styles.confession}`}>
        <div className="container">
          <div className={`${styles.head} reveal`}>
            <p className="eyebrow">Our confession of faith</p>
            <h2 className={styles.h2}>What We Hold to Be True</h2>
          </div>
          <div className={styles.grid}>
            {beliefs.map((b, i) => (
              <article key={b.title} className={`${styles.belief} reveal`}>
                <span className={styles.num}>{String(i + 1).padStart(2, "0")}</span>
                <div>
                  <h3 className={styles.beliefTitle}>{b.title}</h3>
                  <p className={styles.beliefText}>{b.text}</p>
                  <p className={styles.beliefRef}>{b.ref}</p>
                </div>
              </article>
            ))}
          </div>
        </div>
      </section>

      {/* Sonship */}
      <section className={styles.sonship}>
        <div className={`container ${styles.sonshipInner} reveal`}>
          <p className="eyebrow">The heart of the Tower</p>
          <h2 className={styles.sonshipTitle}>Sonship</h2>
          {sonship.map((p, i) => (
            <p key={i} className={styles.sonshipText}>
              {p}
            </p>
          ))}
          <p className={styles.sonshipRef}>Romans 8:14-17 · Galatians 4:4-7</p>
        </div>
      </section>

      {/* CTA */}
      <section className={`section ${styles.cta}`}>
        <div className={`container ${styles.ctaInner} reveal`}>
          <h2 className={styles.ctaTitle}>Come and See for Yourself</h2>
          <div className={styles.ctaActions}>
            <Link href="/visit" className="btn btn-primary">
              Plan your visit <ArrowRight size={18} />
            </Link>
            <Link href="/contact" className="btn btn-secondary">
              Ask a question <ArrowRight size={18} />
            </Link>
          </div>
        </div>
      </section>
    </>
  );
}
