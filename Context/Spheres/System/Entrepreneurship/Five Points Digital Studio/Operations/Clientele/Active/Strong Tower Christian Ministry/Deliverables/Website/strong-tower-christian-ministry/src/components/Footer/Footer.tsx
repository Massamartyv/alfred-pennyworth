import Link from "next/link";
import { MapPin, Phone, Mail } from "lucide-react";
import { FacebookIcon, YoutubeIcon } from "@/components/SocialIcons";
import { site } from "@/lib/site";
import Wordmark from "@/components/Wordmark/Wordmark";
import Newsletter from "@/components/Newsletter/Newsletter";
import styles from "./Footer.module.css";

export default function Footer() {
  const year = new Date().getFullYear();

  return (
    <footer className={styles.footer}>
      <div className={`container ${styles.inner}`}>
        <div className={styles.brandCol}>
          <Wordmark size="lg" tone="light" markOnly className={styles.wordmark} />
          <p className={styles.tagline}>{site.taglines.primary}</p>
          <div className={styles.socials}>
            <a
              href={site.social.facebook}
              aria-label="Facebook"
              target="_blank"
              rel="noopener noreferrer"
            >
              <FacebookIcon size={20} />
            </a>
            <a
              href={site.social.youtube}
              aria-label="YouTube"
              target="_blank"
              rel="noopener noreferrer"
            >
              <YoutubeIcon size={20} />
            </a>
          </div>
        </div>

        <nav className={styles.linksCol} aria-label="Footer">
          <h3 className={styles.colTitle}>Explore</h3>
          <ul>
            {site.navAll.map((l) => (
              <li key={l.href}>
                <Link href={l.href}>{l.label}</Link>
              </li>
            ))}
          </ul>
        </nav>

        <div className={styles.servicesCol}>
          <h3 className={styles.colTitle}>Gather</h3>
          <ul>
            {site.services.map((s) => (
              <li key={s.name}>
                <span className={styles.svcName}>{s.name}</span>
                <span className={styles.svcTime}>
                  {s.day} · {s.time}
                </span>
              </li>
            ))}
          </ul>
        </div>

        <div className={styles.contactCol}>
          <h3 className={styles.colTitle}>Find Us</h3>
          <address className={styles.address}>
            <a href={site.contact.mapsUrl} target="_blank" rel="noopener noreferrer">
              <MapPin size={16} /> <span>{site.contact.full}</span>
            </a>
            <a href={site.contact.phoneHref}>
              <Phone size={16} /> <span>{site.contact.phone}</span>
            </a>
            <a href={site.contact.emailHref}>
              <Mail size={16} /> <span>{site.contact.email}</span>
            </a>
          </address>
          <div className={styles.news}>
            <Newsletter compact />
          </div>
        </div>
      </div>

      <div className={styles.bottom}>
        <div className="container">
          <p>
            © {year} {site.name}. Built by Five Points Digital Studio.
          </p>
        </div>
      </div>
    </footer>
  );
}
