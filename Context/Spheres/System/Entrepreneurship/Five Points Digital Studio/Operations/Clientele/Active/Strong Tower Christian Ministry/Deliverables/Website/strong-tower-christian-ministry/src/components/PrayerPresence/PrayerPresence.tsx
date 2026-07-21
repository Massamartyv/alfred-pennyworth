"use client";

import { useActionState, useEffect, useId, useRef, useState } from "react";
import { HandHeart, X, Send } from "lucide-react";
import { sendPrayer } from "@/app/prayer/actions";
import type { PrayerState } from "@/app/prayer/types";
import styles from "./PrayerPresence.module.css";

/**
 * An ever-present, discreet prayer element mounted site-wide.
 * A gentle floating tab opens a chat-styled guided form that reuses the
 * existing prayer Server Action. Not an AI chatbot — a quiet way to ask
 * the prayer team to stand with you.
 */
export default function PrayerPresence() {
  const [open, setOpen] = useState(false);
  const [state, formAction, pending] = useActionState<PrayerState, FormData>(
    sendPrayer,
    null
  );

  const tabRef = useRef<HTMLButtonElement>(null);
  const panelRef = useRef<HTMLDivElement>(null);
  const firstFieldRef = useRef<HTMLTextAreaElement>(null);

  const panelId = useId();
  const titleId = useId();

  function close() {
    setOpen(false);
    tabRef.current?.focus();
  }

  // Move focus into the panel when it opens on the form (not on success).
  useEffect(() => {
    if (open && !state?.ok) {
      firstFieldRef.current?.focus();
    }
  }, [open, state?.ok]);

  // Escape closes the panel and returns focus to the tab.
  useEffect(() => {
    if (!open) return;
    function onKey(e: KeyboardEvent) {
      if (e.key === "Escape") {
        setOpen(false);
        tabRef.current?.focus();
      }
    }
    document.addEventListener("keydown", onKey);
    return () => document.removeEventListener("keydown", onKey);
  }, [open]);

  // A click outside the panel and tab closes it, without stealing focus.
  useEffect(() => {
    if (!open) return;
    function onDown(e: MouseEvent) {
      const target = e.target as Node;
      if (
        panelRef.current &&
        !panelRef.current.contains(target) &&
        tabRef.current &&
        !tabRef.current.contains(target)
      ) {
        setOpen(false);
      }
    }
    document.addEventListener("mousedown", onDown);
    return () => document.removeEventListener("mousedown", onDown);
  }, [open]);

  return (
    <div className={styles.root}>
      {open && (
        <div
          ref={panelRef}
          id={panelId}
          role="dialog"
          aria-labelledby={titleId}
          className={styles.panel}
        >
          <div className={styles.header}>
            <div className={styles.headingGroup}>
              <p className={styles.eyebrow}>Prayer</p>
              <p id={titleId} className={styles.title}>
                Let us pray with you
              </p>
            </div>
            <button
              type="button"
              onClick={close}
              className={styles.close}
              aria-label="Close prayer panel"
            >
              <X size={18} aria-hidden="true" />
            </button>
          </div>

          {state?.ok ? (
            <div className={styles.success} role="status">
              <p className={styles.successTitle}>
                Our prayer team has received this.
              </p>
              <p className={styles.successBody}>
                We will lift it up before the Lord. You are not walking through
                it alone.
              </p>
              <button
                type="button"
                onClick={close}
                className={`btn btn-secondary ${styles.done}`}
              >
                Close
              </button>
            </div>
          ) : (
            <>
              <p className={styles.welcome}>
                Whatever you are carrying, you do not have to carry it alone.
                Share your request and our team will stand with you.
              </p>

              <form action={formAction} className={styles.form}>
                <label className={styles.field}>
                  <span>Your name (optional)</span>
                  <input type="text" name="name" autoComplete="name" />
                </label>

                <label className={styles.field}>
                  <span>How can we pray for you?</span>
                  <textarea
                    ref={firstFieldRef}
                    name="request"
                    rows={4}
                    required
                    placeholder="Share what is on your heart."
                  />
                </label>

                <label className={styles.toggle}>
                  <input type="checkbox" name="private" />
                  <span>Keep this between us and the prayer team</span>
                </label>

                {/* Honeypot — hidden from people, tempting to bots */}
                <div className={styles.hp} aria-hidden="true">
                  <label htmlFor={`${panelId}-company`}>Company</label>
                  <input
                    id={`${panelId}-company`}
                    name="company"
                    type="text"
                    tabIndex={-1}
                    autoComplete="off"
                  />
                </div>

                {state?.error && (
                  <p className={styles.error} role="alert">
                    {state.error}
                  </p>
                )}

                <button
                  type="submit"
                  className={`btn btn-primary ${styles.submit}`}
                  disabled={pending}
                >
                  {pending ? (
                    "Sending…"
                  ) : (
                    <>
                      Send to the prayer team{" "}
                      <Send size={16} aria-hidden="true" />
                    </>
                  )}
                </button>
              </form>
            </>
          )}
        </div>
      )}

      <button
        ref={tabRef}
        type="button"
        className={styles.tab}
        aria-label="Need prayer?"
        aria-expanded={open}
        aria-controls={panelId}
        onClick={() => setOpen((v) => !v)}
      >
        <HandHeart size={18} aria-hidden="true" />
        <span className={styles.tabLabel}>Need prayer?</span>
      </button>
    </div>
  );
}
