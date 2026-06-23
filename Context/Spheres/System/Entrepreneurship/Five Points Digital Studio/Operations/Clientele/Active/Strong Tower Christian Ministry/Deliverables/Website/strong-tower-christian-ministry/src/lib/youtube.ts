/**
 * YouTube Data API v3 helpers — live status and latest videos.
 * Both degrade safely to "nothing" when YOUTUBE_API_KEY or YOUTUBE_CHANNEL_ID
 * is missing, so the site builds and runs without credentials.
 */

const API = "https://www.googleapis.com/youtube/v3";

export interface Video {
  id: string;
  title: string;
  publishedAt: string;
  thumbnail: string;
}

interface YTThumb {
  url: string;
}

interface YTSearchItem {
  id?: { videoId?: string };
  snippet?: {
    title?: string;
    publishedAt?: string;
    thumbnails?: { high?: YTThumb; medium?: YTThumb };
  };
}

interface YTSearchResponse {
  items?: YTSearchItem[];
}

function creds() {
  const key = process.env.YOUTUBE_API_KEY;
  const channelId = process.env.YOUTUBE_CHANNEL_ID;
  return key && channelId ? { key, channelId } : null;
}

export async function getLiveStatus(): Promise<{
  isLive: boolean;
  videoId: string | null;
}> {
  const c = creds();
  if (!c) return { isLive: false, videoId: null };

  try {
    const url = `${API}/search?part=snippet&channelId=${c.channelId}&eventType=live&type=video&maxResults=1&key=${c.key}`;
    const res = await fetch(url, { next: { revalidate: 300 } });
    if (!res.ok) return { isLive: false, videoId: null };

    const data = (await res.json()) as YTSearchResponse;
    const item = data.items?.[0];
    return item?.id?.videoId
      ? { isLive: true, videoId: item.id.videoId }
      : { isLive: false, videoId: null };
  } catch {
    return { isLive: false, videoId: null };
  }
}

export async function getLatestVideos(max = 9): Promise<Video[]> {
  const c = creds();
  if (!c) return [];

  try {
    const url = `${API}/search?part=snippet&channelId=${c.channelId}&order=date&type=video&maxResults=${max}&key=${c.key}`;
    const res = await fetch(url, { next: { revalidate: 1800 } });
    if (!res.ok) return [];

    const data = (await res.json()) as YTSearchResponse;
    return (data.items ?? [])
      .filter((i) => i.id?.videoId)
      .map((i) => ({
        id: i.id!.videoId!,
        title: i.snippet?.title ?? "",
        publishedAt: i.snippet?.publishedAt ?? "",
        thumbnail:
          i.snippet?.thumbnails?.high?.url ??
          i.snippet?.thumbnails?.medium?.url ??
          "",
      }));
  } catch {
    return [];
  }
}

export function embedUrl(videoId: string): string {
  return `https://www.youtube-nocookie.com/embed/${videoId}`;
}

export function watchUrl(videoId: string): string {
  return `https://www.youtube.com/watch?v=${videoId}`;
}
