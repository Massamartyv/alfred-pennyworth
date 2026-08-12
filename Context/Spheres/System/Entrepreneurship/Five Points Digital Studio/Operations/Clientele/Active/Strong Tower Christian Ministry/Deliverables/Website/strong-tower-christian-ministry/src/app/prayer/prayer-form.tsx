"use client";

import { useActionState } from "react";
import { sendPrayer } from "./actions";
import type { PrayerState } from "./types";
import styles from "./prayer-form.module.css";

export default function PrayerForm() {
  const [state, formAction, pending] = useActionState<PrayerState, FormData>(
    sendPrayer,
    null
  );

  if (state?.ok) {
    return (
      <div className={styles.success} role="status">
        <p className={styles.successTitle}>We Received Your Request.</p>
        <p>
          Our prayer team will lift it up. You are not walking through it alone.
        </p>
      </div>
    );
  }

  return (
    <form action={formAction} className={styles.form}>
      <div className={styles.field}>
        <label htmlFor="request">Your prayer request</label>
        <textarea
          id="request"
          name="request"
          rows={6}
          required
          placeholder="Share what is on your heart."
        />
      </div>

      <div className={styles.row}>
        <div className={styles.field}>
          <label htmlFor="name">Name (optional)</label>
          <input id="name" name="name" type="text" autoComplete="name" />
        </div>
        <div className={styles.field}>
          <label htmlFor="email">Email (optional)</label>
          <input id="email" name="email" type="email" autoComplete="email" />
        </div>
      </div>

      <label className={styles.checkbox}>
        <input type="checkbox" name="private" />
        <span>Keep this request private to the prayer team</span>
      </label>

      {/* Honeypot */}
      <div className={styles.hp} aria-hidden="true">
        <label htmlFor="company">Company</label>
        <input id="company" name="company" type="text" tabIndex={-1} autoComplete="off" />
      </div>

      {state?.error && (
        <p className={styles.error} role="alert">
          {state.error}
        </p>
      )}

      <button type="submit" className="btn btn-primary" disabled={pending}>
        {pending ? "Sending…" : "Submit prayer request"}
      </button>
    </form>
  );
}
