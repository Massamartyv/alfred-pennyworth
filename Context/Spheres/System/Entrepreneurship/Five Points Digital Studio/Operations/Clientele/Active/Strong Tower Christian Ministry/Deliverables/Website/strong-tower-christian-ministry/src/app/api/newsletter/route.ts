import { getResend, fromAddress, isValidEmail } from "@/lib/email";

/**
 * Newsletter signup — routed to the church inbox, like the contact and prayer
 * forms. There is no list provider and no database: a signup is an email the
 * office receives and adds to whatever list they keep.
 *
 * This replaces the earlier Resend-audience version, which accepted a signup
 * and silently discarded it whenever the audience was not configured.
 */

interface Body {
  email?: unknown;
  company?: unknown; // honeypot
}

export async function POST(req: Request) {
  try {
    const body = (await req.json().catch(() => null)) as Body | null;

    // Honeypot: bots fill the hidden field. Accept without sending.
    if (typeof body?.company === "string" && body.company.trim()) {
      return Response.json({ ok: true });
    }

    const email = typeof body?.email === "string" ? body.email.trim() : "";
    if (!email || !isValidEmail(email)) {
      return Response.json(
        { error: "Please enter a valid email address." },
        { status: 400 }
      );
    }

    const resend = getResend();
    const to = process.env.NEWSLETTER_TO_EMAIL || process.env.CONTACT_TO_EMAIL;

    if (!resend || !to) {
      return Response.json(
        {
          error:
            "Sign-ups are not set up online yet. Please call the church and we will add you to the list.",
        },
        { status: 503 }
      );
    }

    await resend.emails.send({
      from: fromAddress(),
      to,
      replyTo: email,
      subject: `[Newsletter] New sign-up — ${email}`,
      text: `Someone asked to join the Strong Tower mailing list.\n\nEmail: ${email}\n\nAdd them to the list the office keeps, and reply to this message to greet them.`,
    });

    return Response.json({ ok: true });
  } catch {
    return Response.json(
      { error: "Could not sign you up right now. Please try again." },
      { status: 500 }
    );
  }
}
