"use server";

import { getResend, fromAddress, isValidEmail } from "@/lib/email";
import type { PrayerState } from "./types";

export async function sendPrayer(
  _prev: PrayerState,
  formData: FormData
): Promise<PrayerState> {
  // Honeypot
  if (String(formData.get("company") || "")) {
    return { ok: true };
  }

  const name = String(formData.get("name") || "").trim() || "Anonymous";
  const email = String(formData.get("email") || "").trim();
  const request = String(formData.get("request") || "").trim();
  const keepPrivate = formData.get("private") === "on";

  if (!request) {
    return { ok: false, error: "Please share your prayer request." };
  }
  if (email && !isValidEmail(email)) {
    return {
      ok: false,
      error: "Please enter a valid email, or leave it blank.",
    };
  }

  const resend = getResend();
  const to = process.env.PRAYER_TO_EMAIL || process.env.CONTACT_TO_EMAIL;
  if (!resend || !to) {
    return {
      ok: false,
      error:
        "Prayer requests are not set up online yet. Please call the church and we will pray with you.",
    };
  }

  try {
    await resend.emails.send({
      from: fromAddress(),
      to,
      replyTo: email || undefined,
      subject: `[Prayer]${keepPrivate ? " [Private]" : ""} from ${name}`,
      text: `From: ${name}\nEmail: ${email || "not provided"}\nKeep private: ${
        keepPrivate ? "Yes" : "No"
      }\n\nRequest:\n${request}`,
    });
    return { ok: true };
  } catch {
    return {
      ok: false,
      error: "Something went wrong. Please try again or call the church.",
    };
  }
}
