import Link from "next/link";
import styles from "./Wordmark.module.css";

type Props = {
  /** "sm" for the nav bar, "lg" for the footer and standalone lockups */
  size?: "sm" | "lg";
  /** text colour: light on dark grounds, dark on light grounds */
  tone?: "light" | "dark";
  /** show the "Christian Ministry" sub-line */
  full?: boolean;
  /** when set, wraps the lockup in a link to home */
  href?: string;
  className?: string;
  onClick?: () => void;
};

/**
 * The typographic identity. A slim tower stroke rising into concentric arcs of
 * light — the brand's own signature, set in Fraunces — leads in place of the
 * logo emblem. Decorative glyph is aria-hidden; the words carry the name.
 */
export default function Wordmark({
  size = "sm",
  tone = "light",
  full = false,
  href,
  className = "",
  onClick,
}: Props) {
  const rings = [0, 1, 2];

  const content = (
    <span className={`${styles.lockup} ${styles[size]} ${styles[tone]} ${className}`}>
      <svg className={styles.glyph} viewBox="0 0 48 30" aria-hidden="true">
        {rings.map((i) => {
          const r = 9 + i * 7;
          return (
            <path
              key={i}
              d={`M ${24 - r} 27 A ${r} ${r} 0 0 1 ${24 + r} 27`}
              fill="none"
              stroke="var(--accent-gold)"
              strokeWidth={1.5}
              opacity={0.85 - i * 0.22}
            />
          );
        })}
        {/* the tower — a slim upright rising into the light */}
        <line
          x1="24"
          y1="27"
          x2="24"
          y2="6"
          stroke="var(--accent-gold)"
          strokeWidth={1.5}
          opacity={0.95}
        />
      </svg>
      <span className={styles.words}>
        <span className={styles.name}>Strong Tower</span>
        {full && <span className={styles.sub}>Christian Ministry</span>}
      </span>
    </span>
  );

  if (href) {
    return (
      <Link
        href={href}
        className={styles.link}
        onClick={onClick}
        aria-label="Strong Tower Christian Ministry — home"
      >
        {content}
      </Link>
    );
  }

  return content;
}
