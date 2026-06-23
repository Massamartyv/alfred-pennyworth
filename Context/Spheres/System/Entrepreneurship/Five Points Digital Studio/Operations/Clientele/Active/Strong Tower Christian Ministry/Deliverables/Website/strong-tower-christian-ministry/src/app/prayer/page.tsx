import type { Metadata } from "next";
import { site } from "@/lib/site";
import RevealSection from "@/components/RevealSection/RevealSection";
import PrayerForm from "./prayer-form";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "Prayer",
  description:
    "Submit a prayer request to Strong Tower Christian Ministry. Our prayer team will stand with you in agreement.",
};

export default function PrayerPage() {
  return (
    <>
      <RevealSection />

      <section className="global-page-hero">
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">Prayer</span>
          <h1 className="global-hero-title global-hero-title-light">
            Let Us Pray With You
          </h1>
          <p className="global-page-hero-desc">
            There is power when we agree in prayer. Share your request and our
            team will stand with you.
          </p>
        </div>
      </section>

      <section className="section">
        <div className={`container ${styles.inner}`}>
          <div className={`${styles.intro} reveal`}>
            <p className="scripture">
              &ldquo;Again I say unto you, that if two of you shall agree on
              earth as touching any thing that they shall ask, it shall be done
              for them of my Father which is in heaven.&rdquo;
            </p>
            <p className={styles.ref}>Matthew 18:19</p>
            <p className={styles.body}>
              Whatever you are carrying, you do not have to carry it alone.
              Every request that comes to the Tower is prayed over. Share as
              little or as much as you like.
            </p>
          </div>

          <div className={`${styles.formWrap} reveal`}>
            <PrayerForm />
            <p className={styles.callNote}>
              Need prayer now? Call us at{" "}
              <a href={site.contact.phoneHref}>{site.contact.phone}</a>.
            </p>
          </div>
        </div>
      </section>
    </>
  );
}
