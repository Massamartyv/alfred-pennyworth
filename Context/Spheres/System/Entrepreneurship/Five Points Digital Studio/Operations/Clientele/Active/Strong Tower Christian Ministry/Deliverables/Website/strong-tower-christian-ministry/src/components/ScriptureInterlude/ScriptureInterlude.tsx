import HaloArc from "@/components/HaloArc/HaloArc";
import styles from "./ScriptureInterlude.module.css";

type Props = {
  verse: string;
  reference: string;
  tone?: "light" | "dark";
  sacred?: boolean;
};

/**
 * The Word spoken over the gathering — an italic Fraunces verse between
 * sections, under a small halo. The recurring punctuation of the page.
 */
export default function ScriptureInterlude({
  verse,
  reference,
  tone = "light",
  sacred = false,
}: Props) {
  return (
    <section
      className={`${styles.interlude} ${tone === "dark" ? styles.dark : styles.light}`}
    >
      <div className={`container ${styles.inner} reveal`}>
        <HaloArc className={styles.arc} arcs={4} />
        <p className={`scripture ${sacred ? "scripture-sacred" : ""} ${styles.verse}`}>
          &ldquo;{verse}&rdquo;
        </p>
        <p className={styles.ref}>{reference}</p>
      </div>
    </section>
  );
}
