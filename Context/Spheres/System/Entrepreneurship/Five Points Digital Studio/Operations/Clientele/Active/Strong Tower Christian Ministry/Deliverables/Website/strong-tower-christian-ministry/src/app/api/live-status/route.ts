import { getLiveStatus } from "@/lib/youtube";

// Cache the live check for five minutes; the client polls at the same cadence.
export const revalidate = 300;

export async function GET() {
  const status = await getLiveStatus();
  return Response.json(status, {
    headers: {
      "Cache-Control": "public, s-maxage=300, stale-while-revalidate=600",
    },
  });
}
