"use client";

import Image from "next/image";
import { useEffect, useRef, useState } from "react";
import styles from "./VideoSlot.module.css";

/**
 * VideoSlot — a video-ready media layer that renders a poster image today and
 * accepts the church's real footage later with zero redesign.
 *
 * SWAP-IN PATH (when real video arrives):
 *   1. Drop the file into /public/videos/ (e.g. /public/videos/worship-loop.mp4).
 *      Provide an .mp4 (H.264) and, ideally, a .webm for the same clip.
 *   2. Pass it in: <VideoSlot ... videoSrc="/videos/worship-loop.mp4" />
 *      Optionally videoSrcWebm="/videos/worship-loop.webm".
 *   3. Nothing else changes. The poster stays as the first frame / fallback,
 *      so there is no layout shift and the LCP image is unaffected.
 *
 * Behaviour:
 *   - No videoSrc  → the poster renders with the Ken Burns drift (interim state).
 *   - videoSrc set → the poster shows immediately, the muted/looping/inline
 *     video fades in on canplay and layers over it.
 *   - Ambient use only: muted, loop, playsInline, no controls, aria-hidden.
 *   - Lazy: the video is only mounted when it is provided and motion is allowed,
 *     and playback pauses whenever the slot scrolls offscreen (IntersectionObserver).
 *   - prefers-reduced-motion: the video is never mounted and the Ken Burns drift
 *     is neutralised by globals.css — the still poster holds.
 */

type Motion = "ken-burns" | "ken-burns-slow" | "none";

type Props = {
  /** Poster image path — shown today, and the video's first-frame fallback. */
  poster: string;
  /** Alt text. Empty string for purely decorative/ambient use. */
  alt: string;
  /** Optional video source (mp4/H.264). Drop in later; poster is the fallback. */
  videoSrc?: string;
  /** Optional WebM source for the same clip, offered first for smaller payloads. */
  videoSrcWebm?: string;
  /** Pass true for above-the-fold LCP imagery (e.g. the home hero). */
  priority?: boolean;
  /** next/image sizes hint. */
  sizes?: string;
  /** next/image quality. */
  quality?: number;
  /** object-position for both poster and video (e.g. "center 32%"). */
  objectPosition?: string;
  /** Extra class names merged onto the poster image (page-scoped img styling). */
  imgClassName?: string;
  /** Ambient drift treatment on the poster. Defaults to a gentle Ken Burns. */
  motion?: Motion;
};

export default function VideoSlot({
  poster,
  alt,
  videoSrc,
  videoSrcWebm,
  priority = false,
  sizes = "100vw",
  quality,
  objectPosition,
  imgClassName = "",
  motion = "ken-burns",
}: Props) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [reduced, setReduced] = useState(false);
  const [ready, setReady] = useState(false);

  // Respect the reader's motion preference.
  useEffect(() => {
    const mq = window.matchMedia("(prefers-reduced-motion: reduce)");
    const sync = () => setReduced(mq.matches);
    sync();
    mq.addEventListener("change", sync);
    return () => mq.removeEventListener("change", sync);
  }, []);

  const mountVideo = Boolean(videoSrc) && !reduced;

  // Play only while onscreen; pause otherwise. Keeps the compositor and the
  // decoder quiet when the slot is out of view.
  useEffect(() => {
    const v = videoRef.current;
    if (!v || !mountVideo) return;

    const play = () => v.play().catch(() => {});

    if (!("IntersectionObserver" in window)) {
      play();
      return;
    }

    const io = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) play();
        else v.pause();
      },
      { threshold: 0.15 }
    );
    io.observe(v);
    return () => io.disconnect();
  }, [mountVideo]);

  const motionClass =
    motion === "ken-burns"
      ? "motion-kenburns"
      : motion === "ken-burns-slow"
        ? "motion-kenburns-slow"
        : "";

  const posStyle = objectPosition ? { objectPosition } : undefined;

  return (
    <>
      <Image
        src={poster}
        alt={alt}
        fill
        priority={priority}
        sizes={sizes}
        quality={quality}
        className={`${styles.media} ${motionClass} ${imgClassName}`.trim()}
        style={posStyle}
      />
      {mountVideo && (
        <video
          ref={videoRef}
          className={`${styles.video} ${ready ? styles.videoReady : ""}`}
          poster={poster}
          muted
          loop
          playsInline
          preload="none"
          aria-hidden="true"
          onCanPlay={() => setReady(true)}
          style={posStyle}
        >
          {videoSrcWebm && <source src={videoSrcWebm} type="video/webm" />}
          {videoSrc && <source src={videoSrc} type="video/mp4" />}
        </video>
      )}
    </>
  );
}
