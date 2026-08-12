import Link from "next/link";
import Image from "next/image";
import styles from "./Wordmark.module.css";

type Props = {
  /** "sm" for the nav bar, "lg" for the footer and standalone lockups */
  size?: "sm" | "lg";
  /** ground the lockup sits on: "light" = light ink on a dark ground */
  tone?: "light" | "dark";
  /** show the "Christian Ministry" sub-line beside the emblem */
  full?: boolean;
  /** render the logo alone, at a size where its own wordmark is legible */
  markOnly?: boolean;
  /** when set, wraps the lockup in a link to home */
  href?: string;
  className?: string;
  onClick?: () => void;
};

/**
 * The church's own logo — the tower beneath the cross, wrapped in the halo.
 *
 * The artwork is an integrated lockup: the name is drawn into it and stops
 * being readable below roughly 100px. So it is used two ways.
 *   markOnly  — the logo alone, large enough to speak for itself (footer).
 *   otherwise — the logo as an emblem beside the name set in type (nav),
 *               where at 46px the drawn name reads as texture, not words.
 *
 * Two files, because the drawn name is near-black and would vanish on the
 * fortress grounds: logo.png for pale grounds, logo-light.png for dark.
 */
export default function Wordmark({
  size = "sm",
  tone = "light",
  full = false,
  markOnly = false,
  href,
  className = "",
  onClick,
}: Props) {
  const src = tone === "light" ? "/logo-light.png" : "/logo.png";
  const px = markOnly ? 190 : size === "lg" ? 76 : 46;

  const content = (
    <span
      className={`${styles.lockup} ${styles[size]} ${styles[tone]} ${
        markOnly ? styles.markOnly : ""
      } ${className}`}
    >
      {/* Beside the typographic name the emblem is decorative; standing
          alone it is the only thing carrying the name, so it speaks. */}
      <Image
        src={src}
        alt={markOnly ? "Strong Tower Christian Ministry" : ""}
        aria-hidden={markOnly ? undefined : true}
        width={px}
        height={px}
        className={styles.mark}
        priority={size === "sm"}
      />
      {!markOnly && (
        <span className={styles.words}>
          <span className={styles.name}>Strong Tower</span>
          {full && <span className={styles.sub}>Christian Ministry</span>}
        </span>
      )}
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
