"use client";

import { useActionState } from "react";
import { sendContact } from "./actions";
import type { ContactState } from "./types";
import styles from "./contact-form.module.css";

export default function ContactForm() {
  const [state, formAction, pending] = useActionState<ContactState, FormData>(
    sendContact,
    null
  );

  if (state?.ok) {
    return (
      <div className={styles.success} role="status">
        <p className={styles.successTitle}>Thank You.</p>
        <p>Your message is on its way. We will be in touch soon.</p>
      </div>
    );
  }

  return (
    <form action={formAction} className={styles.form}>
      <div className={styles.field}>
        <label htmlFor="name">Name</label>
        <input id="name" name="name" type="text" required autoComplete="name" />
      </div>

      <div className={styles.row}>
        <div className={styles.field}>
          <label htmlFor="email">Email</label>
          <input
            id="email"
            name="email"
            type="email"
            required
            autoComplete="email"
          />
        </div>
        <div className={styles.field}>
          <label htmlFor="phone">Phone (optional)</label>
          <input id="phone" name="phone" type="tel" autoComplete="tel" />
        </div>
      </div>

      <div className={styles.field}>
        <label htmlFor="subject">Subject</label>
        <select id="subject" name="subject" defaultValue="General enquiry">
          <option>General enquiry</option>
          <option>I am planning my first visit</option>
          <option>Prayer request</option>
          <option>Ministries and getting involved</option>
          <option>Giving</option>
        </select>
      </div>

      <div className={styles.field}>
        <label htmlFor="message">Message</label>
        <textarea id="message" name="message" rows={6} required />
      </div>

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
        {pending ? "Sending…" : "Send message"}
      </button>
    </form>
  );
}
