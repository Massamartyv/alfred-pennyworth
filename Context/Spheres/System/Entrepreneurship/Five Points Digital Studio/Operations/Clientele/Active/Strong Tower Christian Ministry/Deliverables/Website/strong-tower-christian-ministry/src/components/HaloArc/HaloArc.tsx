import styles from "./HaloArc.module.css";

type Props = {
  arcs?: number;
  className?: string;
  /** "up" rises from a baseline (divider, hero backdrop); "full" is a full halo ring set */
  variant?: "up" | "full";
};

/**
 * The ownable signature: concentric arcs of gold light. The logo halo,
 * generalised into a system. Decorative, so aria-hidden throughout.
 */
export default function HaloArc({
  arcs = 4,
  className = "",
  variant = "up",
}: Props) {
  const rings = Array.from({ length: arcs });

  if (variant === "full") {
    return (
      <svg
        className={`${styles.halo} ${className}`}
        viewBox="0 0 400 400"
        aria-hidden="true"
      >
        {rings.map((_, i) => (
          <circle
            key={i}
            cx="200"
            cy="200"
            r={56 + i * 40}
            fill="none"
            stroke="var(--accent-gold)"
            strokeWidth={1.25}
            opacity={0.42 - i * 0.08}
          />
        ))}
      </svg>
    );
  }

  return (
    <svg
      className={`${styles.arc} ${className}`}
      viewBox="0 0 400 130"
      aria-hidden="true"
    >
      {rings.map((_, i) => {
        const r = 38 + i * 32;
        return (
          <path
            key={i}
            d={`M ${200 - r} 120 A ${r} ${r} 0 0 1 ${200 + r} 120`}
            fill="none"
            stroke="var(--accent-gold)"
            strokeWidth={1.5}
            opacity={0.5 - i * 0.1}
          />
        );
      })}
    </svg>
  );
}
