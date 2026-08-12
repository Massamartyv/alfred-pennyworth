import Link from "next/link";
import Image from "next/image";
import { Clock, MapPin, ArrowRight, ArrowUpRight, Play } from "lucide-react";
import { site } from "@/lib/site";
import RevealSection from "@/components/RevealSection/RevealSection";
import VideoSlot from "@/components/Motion/VideoSlot";
import HaloArc from "@/components/HaloArc/HaloArc";
import ScriptureInterlude from "@/components/ScriptureInterlude/ScriptureInterlude";
import Newsletter from "@/components/Newsletter/Newsletter";
import styles from "./page.module.css";

export default function Home() {
  return (
    <>
      <RevealSection />

      {/* Hero — Rising Light, over real light */}
      <section className={styles.hero}>
        <div className={styles.heroMedia}>
          {/* The Goodsons and the praise team beneath the cross — the church's
              own footage. The poster is the LCP image and reduced-motion
              fallback; the muted loop fades in over it. */}
          <VideoSlot
            poster="/images/church/hero-family-poster.jpg"
            alt="Pastor and Prophetess Goodson ministering at the Strong Tower pulpit with the praise team gathered beneath the cross"
            videoSrc="/videos/hero-family.mp4"
            priority
            sizes="100vw"
            imgClassName={styles.heroImg}
            motion="ken-burns-slow"
          />
          <div className={styles.heroScrim} aria-hidden="true" />
          <div className={styles.heroGrain} aria-hidden="true" />
        </div>
        <div className={`container hero-scroll-drift ${styles.heroInner}`}>
          <p className={`eyebrow ${styles.heroEyebrow}`}>
            Strong Tower Christian Ministry · {site.contact.address.city}, South
            Carolina
          </p>
          <h1 className={styles.heroTitle}>
            He Loves You to Life,
            <span className={styles.heroTitleScript}>
              So We Love You to Life.
            </span>
          </h1>
          <p className={styles.heroSub}>
            A Spirit-filled family at the Tower. Wherever you are on the journey,
            there is room for you here.
          </p>
          <div className={styles.heroActions}>
            <Link href="/visit" className="btn btn-primary">
              Plan your visit <ArrowRight size={18} />
            </Link>
            <Link href="/watch" className={`btn ${styles.heroWatch}`}>
              <Play size={18} /> Watch online
            </Link>
          </div>
          <p className={styles.heroService}>
            <Clock size={16} /> Sundays at 10:30 AM · In person and online
          </p>
        </div>
      </section>

      {/* The Word */}
      <ScriptureInterlude
        verse={site.scripture.verse}
        reference={site.scripture.reference}
        tone="light"
      />

      {/* 01 — Welcome */}
      <section className={`section ${styles.welcome}`}>
        <div className={`container ${styles.welcomeInner}`}>
          <div className={`${styles.welcomeMedia} motion-float reveal`}>
            <Image
              src="/images/church/goodsons-ministering.jpg"
              alt="Pastor Kelsey M. Goodson and Prophetess Angela Goodson ministering together at the Strong Tower pulpit"
              fill
              sizes="(max-width: 900px) 100vw, 44vw"
              className={`${styles.welcomeImg} motion-kenburns`}
            />
            <HaloArc variant="up" arcs={4} className={styles.welcomeArc} />
          </div>
          <div className={`${styles.welcomeBody} reveal`}>
            <p className="section-index">01 — Welcome home</p>
            <h2 className={styles.h2}>A Place to Run To, and a Place to Grow</h2>
            <p className={`${styles.lead} lead-text`}>
              Strong Tower Christian Ministry is a church body dependent on the
              Word of God, preaching it, teaching it and living it. We exist to
              help every person grow in the knowledge of Jesus Christ and walk
              in the love He has shown us.
            </p>
            <Link href="/about" className="link-arrow">
              Our story <ArrowRight size={16} />
            </Link>
          </div>
        </div>
        <div className={`container ${styles.welcomeLinksWrap} reveal`}>
          <ul className={styles.welcomeLinks}>
            <li>
              <Link href="/what-we-believe">
                <span>What we believe</span> <ArrowUpRight size={18} />
              </Link>
            </li>
            <li>
              <Link href="/leadership">
                <span>Our leadership</span> <ArrowUpRight size={18} />
              </Link>
            </li>
            <li>
              <Link href="/get-involved">
                <span>Get involved</span> <ArrowUpRight size={18} />
              </Link>
            </li>
          </ul>
        </div>
      </section>

      <HaloArc className={styles.divider} />

      {/* 02 — When we gather */}
      <section className={`section ${styles.services}`}>
        <div className="container">
          <div className={`${styles.sectionHead} reveal`}>
            <p className="section-index">02 — When we gather</p>
            <h2 className={styles.h2}>Come as You Are</h2>
          </div>
          <ul className={styles.serviceList}>
            {site.services.map((s, i) => (
              <li key={s.name} className={`${styles.serviceRow} reveal`}>
                <span className={styles.serviceNum}>
                  {String(i + 1).padStart(2, "0")}
                </span>
                <span className={styles.serviceName}>{s.name}</span>
                <span className={styles.serviceWhen}>{s.day}</span>
                <span className={styles.serviceTime}>{s.time}</span>
                <span className={styles.serviceMode}>{s.mode}</span>
              </li>
            ))}
          </ul>
        </div>
      </section>

      {/* 03 — Watch */}
      <section className={styles.watch}>
        <div className={styles.watchMedia} aria-hidden="true">
          {/* Pastor Goodson preaching to the congregation — the church's own
              footage. Poster is the LCP-safe fallback; the muted loop fades in. */}
          <VideoSlot
            poster="/images/church/preaching-sanctuary-poster.jpg"
            videoSrc="/videos/preaching-sanctuary.mp4"
            alt=""
            sizes="100vw"
            imgClassName={styles.watchImg}
            objectPosition="center 40%"
            motion="ken-burns-slow"
          />
        </div>
        <div
          className={`${styles.watchGlow} motion-ambient-glow`}
          aria-hidden="true"
        />
        <div className={`container ${styles.watchInner} reveal`}>
          <div>
            <p className="section-index">03 — The Word, on demand</p>
            <h2 className={styles.watchTitle}>
              Missed a Service? Watch Any Time.
            </h2>
            <p className={styles.watchCopy}>
              Every Sunday and midweek message, ready when you are. New messages
              land here on their own.
            </p>
          </div>
          <Link href="/watch" className="btn btn-primary">
            <Play size={18} /> Watch messages
          </Link>
        </div>
      </section>

      {/* The Word — sacred */}
      <ScriptureInterlude
        verse="See what great love the Father has lavished on us, that we should be called children of God."
        reference="1 John 3:1"
        tone="light"
        sacred
      />

      {/* 04 / 05 — Visit + Give */}
      <section className={`section ${styles.split}`}>
        <div className={`container ${styles.splitInner}`}>
          <div className={`${styles.splitCard} reveal reveal-d1`}>
            <p className="section-index">04 — New here</p>
            <h2 className={styles.splitTitle}>We Saved You a Seat</h2>
            <p className={styles.splitCopy}>
              Know what to expect before you walk in. Come as you are.
            </p>
            <Link href="/visit" className="btn btn-secondary">
              Plan your visit <ArrowRight size={18} />
            </Link>
          </div>
          <div className={`${styles.splitCard} ${styles.splitGive} reveal reveal-d2`}>
            <p className="section-index">05 — Give</p>
            <h2 className={styles.splitTitle}>Partner with the Tower</h2>
            <p className={styles.splitCopy}>
              Support the work of the ministry through your tithes and offering.
            </p>
            <Link href="/give" className="btn btn-primary">
              Give online <ArrowRight size={18} />
            </Link>
          </div>
        </div>
      </section>

      {/* 06 — Location */}
      <section className={`section ${styles.location}`}>
        <div className={`container ${styles.locationInner}`}>
          <div className={`${styles.locationText} reveal`}>
            <p className="section-index">06 — Find the Tower</p>
            <h2 className={styles.h2}>We Would Love to Meet You</h2>
            <address className={styles.locationAddr}>
              <MapPin size={18} /> {site.contact.full}
            </address>
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

      {/* Newsletter */}
      <section className={`section ${styles.newsletter}`}>
        <div className={`container ${styles.newsletterInner} reveal`}>
          <Newsletter />
        </div>
      </section>
    </>
  );
}
