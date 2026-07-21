import type { MetadataRoute } from "next";
import { site } from "@/lib/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const routes = [
    "",
    "/about",
    "/what-we-believe",
    "/leadership",
    "/ministries",
    "/watch",
    "/events",
    "/visit",
    "/get-involved",
    "/give",
    "/prayer",
    "/contact",
  ];

  const lastModified = new Date();

  return routes.map((route) => ({
    url: `${site.url}${route}`,
    lastModified,
    changeFrequency:
      route === "" || route === "/watch" || route === "/events"
        ? "weekly"
        : "monthly",
    priority: route === "" ? 1 : 0.7,
  }));
}
