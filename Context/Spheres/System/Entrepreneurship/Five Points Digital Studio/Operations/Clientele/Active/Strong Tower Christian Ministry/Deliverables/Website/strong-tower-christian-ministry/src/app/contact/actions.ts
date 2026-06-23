"use server";

import { getResend, fromAddress, isValidEmail } from "@/lib/email";
import type { ContactState } from "./types";

export async function sendContact(
  _prev: ContactState,
  formData: FormData
): Promise<ContactState> {
  // Honeypot: bots fill this hidden field.
  if (String(formData.get("company") || "")) {
    return { ok: true };
  }

  const name = String(formData.get("name") || "").trim();
  const email = String(formData.get("email") || "").trim();
  const phone = String(formData.get("phone") || "").trim();
  const subject = String(formData.get("subject") || "General enquiry").trim();
  const message = String(formData.get("message") || "").trim();

  if (!name || !email || !message) {
    return { ok: false, error: "Please add your name, email and a message." };
  }
  if (!isValidEmail(email)) {
    return { ok: false, error: "Please enter a valid email address." };
  }

  const resend = getResend();
  const to = process.env.CONTACT_TO_EMAIL;
  if (!resend || !to) {
    return {
      ok: false,
      error:
        "Messaging is not set up yet. Please call or email the church directly for now.",
    };
  }

  try {
    await resend.emails.send({
      from: fromAddress(),
      to,
      replyTo: email,
      subject: `[Website] ${subject} — ${name}`,
      text: `Name: ${name}\nEmail: ${email}\nPhone: ${phone}\nSubject: ${subject}\n\nMessage:\n${message}`,
    });
    return { ok: true };
  } catch {
    return {
      ok: false,
      error: "Something went wrong. Please try again or call the church.",
    };
  }
}
