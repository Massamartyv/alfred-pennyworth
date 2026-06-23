"use client";

import { useState } from "react";
import { Send } from "lucide-react";
import styles from "./Newsletter.module.css";

type Status = "idle" | "loading" | "ok" | "error";

export default function Newsletter({ compact = false }: { compact?: boolean }) {
  const [email, setEmail] = useState("");
  const [status, setStatus] = useState<Status>("idle");

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!email) return;
    setStatus("loading");
    try {
      const res = await fetch("/api/newsletter", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email }),
      });
      if (res.ok) {
        setStatus("ok");
        setEmail("");
      } else {
        setStatus("error");
      }
    } catch {
      setStatus("error");
    }
  };

  return (
    <form
      className={`${styles.form} ${compact ? styles.compact : ""}`}
      onSubmit={submit}
    >
      {!compact && <h3 className={styles.title}>Stay in the loop</h3>}
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
      {status === "ok" && (
        <p className={styles.ok} role="status">
          Thank you. You are on the list.
        </p>
      )}
      {status === "error" && (
        <p className={styles.err} role="status">
          Something went wrong. Please try again.
        </p>
      )}
    </form>
  );
}
