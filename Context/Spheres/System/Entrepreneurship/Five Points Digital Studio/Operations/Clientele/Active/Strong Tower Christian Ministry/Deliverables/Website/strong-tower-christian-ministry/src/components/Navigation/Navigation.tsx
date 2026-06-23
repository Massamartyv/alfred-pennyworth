"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Menu, X } from "lucide-react";
import { site } from "@/lib/site";
import Wordmark from "@/components/Wordmark/Wordmark";
import LiveButton from "./LiveButton";
import styles from "./Navigation.module.css";

export default function Navigation() {
  const [scrolled, setScrolled] = useState(false);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 24);
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
    return () => window.removeEventListener("scroll", onScroll);
  }, []);

  useEffect(() => {
    document.body.style.overflow = open ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [open]);

  const giveExternal = Boolean(site.giving.url);

  return (
    <header className={`${styles.header} ${scrolled ? styles.scrolled : ""}`}>
      <div className={styles.inner}>
        <Link href="/" className={styles.brand} onClick={() => setOpen(false)}>
          <Wordmark size="sm" tone="light" />
        </Link>

        <nav className={styles.desktopNav} aria-label="Primary">
          {site.navPrimary.map((l) => (
            <Link key={l.href} href={l.href} className={styles.navLink}>
              {l.label}
            </Link>
          ))}
        </nav>

        <div className={styles.actions}>
          <LiveButton />
          {giveExternal ? (
            <a
              href={site.giving.url}
              target="_blank"
              rel="noopener noreferrer"
              className={`btn btn-primary ${styles.give}`}
            >
              Give
            </a>
          ) : (
            <Link href="/give" className={`btn btn-primary ${styles.give}`}>
              Give
            </Link>
          )}
          <button
            className={styles.menuBtn}
            aria-label={open ? "Close menu" : "Open menu"}
            aria-expanded={open}
            onClick={() => setOpen(!open)}
          >
            {open ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>
      </div>

      {open && (
        <div className={styles.mobileMenu}>
          <nav className={styles.mobileNav} aria-label="All pages">
            {site.navAll.map((l) => (
              <Link
                key={l.href}
                href={l.href}
                className={styles.mobileLink}
                onClick={() => setOpen(false)}
              >
                {l.label}
              </Link>
            ))}
          </nav>
        </div>
      )}
    </header>
  );
}
