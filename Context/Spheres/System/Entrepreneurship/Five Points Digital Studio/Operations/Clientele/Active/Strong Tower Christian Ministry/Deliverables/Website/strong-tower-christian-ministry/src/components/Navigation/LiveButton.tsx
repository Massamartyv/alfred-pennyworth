"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import styles from "./LiveButton.module.css";

/**
 * Polls /api/live-status every five minutes. Renders nothing unless the
 * church's YouTube channel is live, so it degrades silently when the API
 * is unconfigured.
 */
export default function LiveButton() {
  const [live, setLive] = useState(false);

  useEffect(() => {
    let active = true;

    const check = async () => {
      try {
        const res = await fetch("/api/live-status", { cache: "no-store" });
        if (!res.ok) return;
        const data = await res.json();
        if (active) setLive(Boolean(data.isLive));
      } catch {
        /* network or config issue: stay hidden */
      }
    };

    check();
    const id = setInterval(check, 5 * 60 * 1000);
    return () => {
      active = false;
      clearInterval(id);
    };
  }, []);

  if (!live) return null;

  return (
    <Link href="/watch" className={styles.live}>
      <span className="pulse" aria-hidden="true" />
      <span>Live Now</span>
    </Link>
  );
}
