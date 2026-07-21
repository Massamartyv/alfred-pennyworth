import type { Metadata } from "next";
import Image from "next/image";
import { Play } from "lucide-react";
import { FacebookIcon, YoutubeIcon } from "@/components/SocialIcons";
import { site } from "@/lib/site";
import {
  getLatestVideos,
  getLiveStatus,
  embedUrl,
  watchUrl,
} from "@/lib/youtube";
import RevealSection from "@/components/RevealSection/RevealSection";
import VideoSlot from "@/components/Motion/VideoSlot";
import styles from "./page.module.css";

export const metadata: Metadata = {
  title: "Watch",
  description:
    "Watch Strong Tower Christian Ministry live and on demand. Sunday worship and midweek messages, ready when you are.",
};

export const revalidate = 1800;

export default async function WatchPage() {
  const [live, videos] = await Promise.all([
    getLiveStatus(),
    getLatestVideos(9),
  ]);

  const latest = videos[0];
  const archive = videos.slice(1);
  const featuredId = live.isLive ? live.videoId : latest?.id ?? null;
  const hasContent = Boolean(featuredId);

  return (
    <>
      <RevealSection />

      <section className="global-page-hero">
        {/* Video-ready ambient backdrop. Add videoSrc="/videos/gathering.mp4"
            to bring it to life; the poster is the fallback and holds today. */}
        <div className={styles.heroMedia} aria-hidden="true">
          <VideoSlot
            poster="/images/worship/congregation-gold.jpg"
            alt=""
            sizes="100vw"
            imgClassName={styles.heroImg}
            motion="ken-burns-slow"
          />
        </div>
        <div className={styles.heroScrim} aria-hidden="true" />
        <div className="global-page-hero-container">
          <span className="global-page-hero-badge">
            {live.isLive ? "Live now" : "Watch"}
          </span>
          <h1 className="global-hero-title global-hero-title-light">
            Watch &amp; Worship
          </h1>
          <p className="global-page-hero-desc">
            {live.isLive
              ? "We are live right now. Pull up a seat and join the service."
              : "Sunday worship and midweek messages, ready whenever you are."}
          </p>
        </div>
      </section>

      {hasContent ? (
        <>
          <section className={`section ${styles.featured}`}>
            <div className="container">
              <div className={`${styles.player} reveal`}>
                <iframe
                  src={embedUrl(featuredId as string)}
                  title={
                    live.isLive
                      ? "Live service"
                      : latest?.title || "Latest message"
                  }
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                  allowFullScreen
                  className={styles.iframe}
                />
              </div>
              {!live.isLive && latest?.title && (
                <p className={`${styles.featuredTitle} reveal`}>
                  {latest.title}
                </p>
              )}
            </div>
          </section>

          {archive.length > 0 && (
            <section className={`section ${styles.archive}`}>
              <div className="container">
                <div className={`${styles.head} reveal`}>
                  <p className="eyebrow">The archive</p>
                  <h2 className={styles.h2}>Recent messages</h2>
                </div>
                <div className={styles.grid}>
                  {archive.map((v) => (
                    <a
                      key={v.id}
                      href={watchUrl(v.id)}
                      target="_blank"
                      rel="noopener noreferrer"
                      className={`${styles.card} reveal`}
                    >
                      <div className={styles.thumb}>
                        {v.thumbnail && (
                          <Image
                            src={v.thumbnail}
                            alt=""
                            fill
                            sizes="(max-width: 900px) 100vw, 33vw"
                            className={styles.thumbImg}
                          />
                        )}
                        <span className={styles.playBadge}>
                          <Play size={20} />
                        </span>
                      </div>
                      <p className={styles.cardTitle}>{v.title}</p>
                    </a>
                  ))}
                </div>
                <div className={`${styles.moreRow} reveal`}>
                  <a
                    href={site.social.youtube}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="btn btn-secondary"
                  >
                    <YoutubeIcon size={18} /> See all on YouTube
                  </a>
                </div>
              </div>
            </section>
          )}
        </>
      ) : (
        <section className={`section ${styles.empty}`}>
          <div className={`container ${styles.emptyInner} reveal`}>
            <h2 className={styles.h2}>Watch with us</h2>
            <p className={styles.emptyCopy}>
              Our services stream on YouTube and Facebook. Follow along live or
              catch the latest message there.
            </p>
            <div className={styles.emptyActions}>
              <a
                href={site.social.youtube}
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-primary"
              >
                <YoutubeIcon size={18} /> Watch on YouTube
              </a>
              <a
                href={site.social.facebook}
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-secondary"
              >
                <FacebookIcon size={18} /> Watch on Facebook
              </a>
            </div>
            {/* CONFIRM: set YOUTUBE_API_KEY and YOUTUBE_CHANNEL_ID to auto-populate live status and the sermon archive */}
          </div>
        </section>
      )}
    </>
  );
}
