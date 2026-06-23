import { getResend, isValidEmail } from "@/lib/email";

interface Body {
  email?: unknown;
}

export async function POST(req: Request) {
  try {
    const body = (await req.json().catch(() => null)) as Body | null;
    const email = typeof body?.email === "string" ? body.email.trim() : "";

    if (!email || !isValidEmail(email)) {
      return Response.json(
        { error: "A valid email is required." },
        { status: 400 }
      );
    }

    const resend = getResend();
    const audienceId = process.env.NEWSLETTER_LIST_ID;
    const provider = process.env.NEWSLETTER_PROVIDER || "resend";

    // Swap-slot: when the newsletter is not configured, accept gracefully so
    // the form is never broken. Wire NEWSLETTER_LIST_ID before launch.
    if (!resend || !audienceId || provider !== "resend") {
      return Response.json({ ok: true, queued: false });
    }

    await resend.contacts.create({ email, audienceId, unsubscribed: false });
    return Response.json({ ok: true, queued: true });
  } catch {
    return Response.json(
      { error: "Could not subscribe right now." },
      { status: 500 }
    );
  }
}
