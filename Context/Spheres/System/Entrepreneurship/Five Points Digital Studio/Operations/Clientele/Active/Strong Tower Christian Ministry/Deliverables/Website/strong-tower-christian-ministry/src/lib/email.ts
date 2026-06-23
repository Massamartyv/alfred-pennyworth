import { Resend } from "resend";

/**
 * Returns a Resend client when RESEND_API_KEY is set, otherwise null so
 * callers can degrade gracefully without a key during local dev or preview.
 */
export function getResend(): Resend | null {
  const key = process.env.RESEND_API_KEY;
  return key ? new Resend(key) : null;
}

/** Verified sending identity. Set RESEND_FROM once the domain is verified. */
export function fromAddress(): string {
  return (
    process.env.RESEND_FROM ||
    "Strong Tower Website <noreply@strongtowercm.org>"
  );
}

export function isValidEmail(value: string): boolean {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);
}
