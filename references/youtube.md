# SearchVector API — youtube

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 8 endpoints.

### POST /api/tools/youtube/analytics/
`tools_youtube_analytics_create` — YouTube Analytics Report
Get detailed analytics for all videos in a playlist
- Body (required): YouTubeAnalyticsInputRequest
  - google_email* (string(email)) — Google account email for OAuth
  - start_date* (string(date)) — Start date for analytics (YYYY-MM-DD)
  - end_date* (string(date)) — End date for analytics (YYYY-MM-DD)
  - playlist_id* (string) — YouTube Playlist ID
  - channel_id (string) — YouTube Channel ID (defaults to 'MINE')
- Auth: JWT/Token/Cookie
- Returns: 200 any | 400 | 404 | 500

### GET /api/tools/youtube/channels/
`tools_youtube_channels_retrieve` — List connected YouTube channels
Get all YouTube channels connected by the authenticated user, grouped by Google account
- Auth: JWT/Token/Cookie
- Returns: 200 any

### DELETE /api/tools/youtube/channels/delete/
`tools_youtube_channels_delete_destroy` — Delete YouTube channel
Remove a YouTube channel from user's connected channels
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 404

### POST /api/tools/youtube/comments/
`tools_youtube_comments_create` — Fetch YouTube video comments
Fetch comments for multiple YouTube videos (max 10 videos per request)
- Body (required): YouTubeVideoCommentsInputRequest
  - google_email* (string(email)) — Google account email for OAuth
  - video_ids* (array<string>) — List of YouTube Video IDs (max 10)
  - max_results (integer) — Maximum comments per video (1-100, default 100)
  - page_tokens (object) — Dict of video_id: page_token for pagination
- Auth: JWT/Token/Cookie
- Returns: 200 any | 400 | 404 | 503

### POST /api/tools/youtube/comments/reply/
`tools_youtube_comments_reply_create` — Reply to YouTube comments
Reply to multiple YouTube comments (max 10 replies per request). Validates canReply before posting.
- Body (required): YouTubeCommentReplyInputRequest
  - google_email* (string(email)) — Google account email for OAuth
  - replies* (array<YouTubeCommentReplyItemRequest>) — List of replies (max 10)
- Auth: JWT/Token/Cookie
- Returns: 200 any | 400 | 404 | 503

### GET /api/tools/youtube/fetch-channels/
`tools_youtube_fetch_channels_retrieve` — Fetch YouTube channels
Fetch and sync user's YouTube channels.
- Query: google_email* (string) — Google account email with YouTube OAuth access
- Auth: JWT/Token/Cookie
- Returns: 200 any | 400 | 404 | 500

### POST /api/tools/youtube/playlist-videos/
`tools_youtube_playlist_videos_create` — Fetch playlist videos (lightweight)
Fetch basic video details from a playlist using Data API only
- Body (required): PlaylistVideosInputRequest
  - google_email* (string(email)) — Google account email for OAuth
  - playlist_id* (string) — YouTube Playlist ID
- Auth: JWT/Token/Cookie
- Returns: 200 any | 400 | 404 | 503

### POST /api/tools/youtube/playlists/
`tools_youtube_playlists_create` — Fetch YouTube playlists
Fetch all playlists for a specific YouTube channel. Set mine=true to return only playlists that contain 100% your uploaded videos (filters out playlists with others' videos).
- Body (required): FetchPlaylistsInputRequest
  - google_email* (string(email)) — Google account email for OAuth
  - channel_id* (string) — YouTube Channel ID
  - mine (boolean) — If true, return only playlists containing 100% your uploaded videos
- Auth: JWT/Token/Cookie
- Returns: 200 any | 400 | 404 | 500
