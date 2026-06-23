"use client";

import { useRevealOnScroll } from "@/hooks/useRevealOnScroll";

/**
 * Drop once into any page to activate scroll-reveal on its `.reveal` elements.
 * Renders nothing.
 */
export default function RevealSection() {
  useRevealOnScroll();
  return null;
}
