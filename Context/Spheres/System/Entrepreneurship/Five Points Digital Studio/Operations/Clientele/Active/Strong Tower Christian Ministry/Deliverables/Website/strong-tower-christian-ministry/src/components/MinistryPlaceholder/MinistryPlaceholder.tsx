import styles from "./MinistryPlaceholder.module.css";

type Props = {
  /** Short monogram set in the display face — e.g. "S", "G&G". */
  monogram: string;
};

/**
 * MinistryPlaceholder — a type-and-light composition holding the media slot
 * until the church supplies a photograph of the ministry. The fortress
 * ground, a rising gold bloom and the concentric halo arcs (the signature),
 * with the ministry's monogram in the display face.
 *
 * Rendered inline (not as an image) so the page's real fonts apply, and so
 * the arcs join the site-wide scroll draw-in where supported. Swap path:
 * replace this element with an <Image> in the same .cardMedia slot — no
 * layout change.
 */
export default function MinistryPlaceholder({ monogram }: Props) {
  const arcs = [120, 190, 260, 330];

  return (
    <svg
      className={`${styles.placeholder} sd-draw`}
      viewBox="0 0 800 500"
      preserveAspectRatio="xMidYMid slice"
      aria-hidden="true"
    >
      <defs>
        <linearGradient id="mp-ground" x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stopColor="#1c2a3f" />
          <stop offset="1" stopColor="#131d2c" />
        </linearGradient>
        <radialGradient id="mp-bloom" cx="0.5" cy="1" r="0.9">
          <stop offset="0" stopColor="rgba(198, 162, 78, 0.26)" />
          <stop offset="1" stopColor="rgba(198, 162, 78, 0)" />
        </radialGradient>
      </defs>

      <rect width="800" height="500" fill="url(#mp-ground)" />
      <rect width="800" height="500" fill="url(#mp-bloom)" />

      {/* The halo, rising from below the frame */}
      {arcs.map((r) => (
        <path
          key={r}
          d={`M ${400 - r} 520 A ${r} ${r} 0 0 1 ${400 + r} 520`}
          fill="none"
          stroke="var(--accent-gold)"
          strokeWidth={2}
          opacity={0.52 - (r - 120) / 700}
          pathLength={1}
        />
      ))}

      <text
        x="400"
        y="318"
        textAnchor="middle"
        className={styles.monogram}
      >
        {monogram}
      </text>
    </svg>
  );
}
