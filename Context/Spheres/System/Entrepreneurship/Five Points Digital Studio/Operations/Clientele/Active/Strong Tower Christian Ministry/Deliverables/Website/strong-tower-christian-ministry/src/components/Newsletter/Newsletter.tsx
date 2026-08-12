"use client";

import { useState } from "react";
import { Send } from "lucide-react";
import styles from "./Newsletter.module.css";

type Status = "idle" | "loading" | "ok" | "error";

export default function Newsletter({ compact = false }: { compact?: boolean }) {
  const [email, setEmail] = useState("");
  const [company, setCompany] = useState(""); // honeypot
  const [status, setStatus] = useState<Status>("idle");
  const [error, setError] = useState("");

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email) return;
    setStatus("loading");
    setError("");
    try {
      const res = await fetch("/api/newsletter", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, company }),
      });
      if (res.ok) {
        setStatus("ok");
        setEmail("");
      } else {
        // Surface the server's own wording — it tells the reader what to do
        // instead when sign-ups are not wired up yet.
        const data = await res.json().catch(() => null);
        setError(
          (data && typeof data.error === "string" && data.error) ||
            "Something went wrong. Please try again."
        );
        setStatus("error");
      }
    } catch {
      setError("Something went wrong. Please try again.");
      setStatus("error");
    }
  };

  return (
    <form
      className={`${styles.form} ${compact ? styles.compact : ""}`}
      onSubmit={submit}
    >
      {!compact && <h3 className={styles.title}>Stay in the Loop</h3>}
      <p className={styles.copy}>
        Announcements, events and a word of encouragement to your inbox.
      </p>
      <div className={styles.row}>
        <label htmlFor="newsletter-email" className={styles.srOnly}>
          Email address
        </label>
        <input
          id="newsletter-email"
          type="email"
          required
          placeholder="you@email.com"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className={styles.input}
          disabled={status === "loading"}
        />
        <button
          type="submit"
          className={styles.button}
          disabled={status === "loading"}
          aria-label="Subscribe"
        >
          <Send size={18} />
        </button>
      </div>
      {/* Honeypot — hidden from readers and assistive technology alike.
          Matches the pattern the contact and prayer forms already use. */}
      <div className={styles.hp} aria-hidden="true">
        <label htmlFor="newsletter-company">Company</label>
        <input
          id="newsletter-company"
          name="company"
          type="text"
          value={company}
          onChange={(e) => setCompany(e.target.value)}
          tabIndex={-1}
          autoComplete="off"
        />
      </div>
      {status === "ok" && (
        <p className={styles.ok} role="status">
          Thank you. You are on the list.
        </p>
      )}
      {status === "error" && (
        <p className={styles.err} role="status">
          {error || "Something went wrong. Please try again."}
        </p>
      )}
    </form>
  );
}
