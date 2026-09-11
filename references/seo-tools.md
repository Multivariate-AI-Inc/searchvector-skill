# SearchVector API — seo-tools

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 42 endpoints.

### GET /api/rank-tracker/competitors/
`rank_tracker_competitors_list` — List or create project competitors
GET: list project competitors. POST requires owner or admin access. POST is limited by the project owner's max_competitors plan feature.
- Auth: JWT/Token/Cookie
- Returns: 200 array<ProjectCompetitor> | 201 ProjectCompetitor | 402 | 403

### POST /api/rank-tracker/competitors/
`rank_tracker_competitors_create` — List or create project competitors
GET: list project competitors. POST requires owner or admin access. POST is limited by the project owner's max_competitors plan feature.
- Body (required): ProjectCompetitorRequest
  - project* (integer)
  - domain* (string)
  - global_traffic (integer)
  - priority (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 array<ProjectCompetitor> | 201 ProjectCompetitor | 402 | 403

### DELETE /api/rank-tracker/competitors/{competitor_id}/
`rank_tracker_competitors_destroy` — Update or delete a project competitor
PATCH updates a project competitor. DELETE removes it. Owner/admin access required.
- Path: competitor_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectCompetitor | 204 | 400 | 403

### PATCH /api/rank-tracker/competitors/{competitor_id}/
`rank_tracker_competitors_partial_update` — Update or delete a project competitor
PATCH updates a project competitor. DELETE removes it. Owner/admin access required.
- Path: competitor_id* (integer)
- Body: PatchedProjectCompetitorRequest
  - project (integer)
  - domain (string)
  - global_traffic (integer)
  - priority (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectCompetitor | 204 | 400 | 403

### POST /api/rank-tracker/keyword-score/
`rank_tracker_keyword_score_create` — Calculate keyword difficulty scores from stored SERP data
Accepts either project_id + keywords + country or project_id + items[]. Looks up stored SERP rows in Rank, calculates a weighted title-match score, and returns N/A when no data exists. Credits charged: 0.02 per keyword …
- Body (required): RankTrackerKeywordScoreInputRequest
  - project_id* (integer)
  - items (array<BulkItemRequest>)
  - keywords (array<string>) — List of keywords to score (max 1000)
  - country (string) — Country code (e.g., 'us', 'in')
  - serp (boolean) — Include SERP URLs in response (default: False)
  - cached (boolean) — Use cached score when available. Set false to force a fresh recalculation.
- Auth: JWT/Token/Cookie
- Returns: 200 RankTrackerKeywordScoreResponse

### DELETE /api/rank-tracker/keywords/
`rank_tracker_keywords_destroy` — List, create, or bulk delete project keywords
GET: list active keywords for a project (project_id required). POST/DELETE require owner or admin access. Keywords are billed to the project owner. POST: create single keyword (object with project_id) or multiple keywor…
- Auth: JWT/Token/Cookie
- Returns: 200 array<Keyword> | 201 Keyword | 204 | 400 | 403

### GET /api/rank-tracker/keywords/
`rank_tracker_keywords_list` — List, create, or bulk delete project keywords
GET: list active keywords for a project (project_id required). POST/DELETE require owner or admin access. Keywords are billed to the project owner. POST: create single keyword (object with project_id) or multiple keywor…
- Auth: JWT/Token/Cookie
- Returns: 200 array<Keyword> | 201 Keyword | 204 | 400 | 403

### POST /api/rank-tracker/keywords/
`rank_tracker_keywords_create` — List, create, or bulk delete project keywords
GET: list active keywords for a project (project_id required). POST/DELETE require owner or admin access. Keywords are billed to the project owner. POST: create single keyword (object with project_id) or multiple keywor…
- Body (required): BulkDeleteKeywordsRequest
  - keyword_ids* (array<integer>)
- Auth: JWT/Token/Cookie
- Returns: 200 array<Keyword> | 201 Keyword | 204 | 400 | 403

### POST /api/rank-tracker/serp/fetch/
`rank_tracker_serp_fetch_create` — Fetch Google SERP and store top ranks (single or bulk)
Pass keyword_id for single keyword or keyword_ids list for bulk. Already scraped keywords are skipped.
- Body (required): FetchKeywordSerpRequest
  - keyword_id (integer)
  - keyword_ids (array<integer>)
  - project_id* (integer)
  - num_results (integer)
- Auth: JWT/Token/Cookie
- Returns: 200

### GET /api/rank-tracker/serp/top10/
`rank_tracker_serp_top10_retrieve` — SERP top 10 payload for keyword popup
- Query: keyword_id* (integer); project_id* (integer); recorded_date (string(date))
- Auth: JWT/Token/Cookie
- Returns: 200

### GET /api/rank-tracker/views/competitor/
`rank_tracker_views_competitor_retrieve` — Competitor table payload for selected project
Returns latest rank for each keyword by default. Pass 'date' (YYYY-MM-DD) to get ranks for a specific date.
- Query: date (string(date)); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200

### GET /api/rank-tracker/views/daywise/
`rank_tracker_views_daywise_retrieve` — Day-wise snapshot payload for selected project
Returns day-wise snapshots for the project's own domain. For each available scrape date, rank is the self-domain rank when present, 0 when SERP data exists but the self domain is not ranking, and N/A when that keyword h…
- Query: end_date (string(date)); project_id* (integer); start_date (string(date))
- Auth: JWT/Token/Cookie
- Returns: 200

### GET /api/tools/advertise-urls/
`tools_advertise_urls_list` — List advertise URLs
Returns advertise URLs. Use `search` to filter by URL text and `page_size` to request larger pages, up to 1000 rows.
- Query: ordering (string) — Order by url, created_at, or updated_at. Prefix with - for descending.; page (integer) — Page number.; page_size (integer) — Number of rows per page. Maximum 1000.; search (string) — Search text matched against URL.
- Auth: JWT
- Returns: 200 object | 401

### POST /api/tools/advertiser-competitors/
`tools_advertiser_competitors_create` — Get advertiser competitor domains
Returns advertiser domains that rank for keywords also ranking for the requested domain.
- Body (required): AdvertiserCompetitorsRequestRequest
  - domain* (string)
- Auth: JWT/Token/Cookie
- Returns: 200 AdvertiserCompetitorsResponse | 400 | 402 | 500 | 503

### POST /api/tools/competitor-domains/
`tools_competitor_domains_create` — Find top competitor domains based on keyword overlap (Jaccard similarity)
Analyze your domain and discover top competitors based on keyword overlap using Jaccard similarity. Returns competitor domains with shared keyword metrics, overlap percentage, and unique keyword counts. **Features:** - …
- Body (required): CompetitorDomainsInputRequest
  - self_url* (string) — Your website URL/domain to analyze
  - country (string) — 2-character ISO country code (e.g., 'us', 'sg', 'in'). Default: 'us'
  - language (string) — 2-character ISO language code (e.g., 'en', 'es', 'fr'). Default: 'en'
  - limit (integer) — Max competitors to analyze (default: 50). Auto-capped: Free users=50, Paid users=100
- Auth: JWT/Token/Cookie
- Returns: 200 CompetitorDomainsOutput | 503

### POST /api/tools/competitor-keywords/
`tools_competitor_keywords_create` — Compare keywords across websites
Compare ranking keywords across your website and competitor websites. **What this endpoint does** - Fetches unique ranking keywords from your site and competitors - Combines self and competitor data into one flat list -…
- Body (required): CompetitorKeywordsInputRequest
  - self_url* (string) — Your website URL/domain to compare
  - competitor_urls* (array<string>) — List of competitor URLs/domains to compare against (required, min 1, max 5 competitors)
  - mode (any) — Mode: 'domain' for domain-level match (all subdomains/pages), 'page' for exact page/path match * `domain` - domain * `p…
  - page (integer) — Page number for pagination (default: 1). Free users: page 1 only. Paid users: page 1 returns 5000 rows, page 2+ returns…
- Auth: JWT/Token/Cookie
- Returns: 200 CompetitorKeywordsOutput | 402 | 503

### POST /api/tools/index-inspect/
`tools_index_inspect_create` — Inspect URLs for indexing status
Inspect multiple URLs for indexing, crawl, and mobile signals. **What this endpoint does** - Checks whether each URL is indexed - Returns canonical and crawl information - Returns mobile and rich result signals when ava…
- Body (required): IndexInspectInputRequest
  - project_id* (integer) — Project ID to inspect URLs for
  - urls* (array<string(uri)>) — List of URLs to inspect (max 10)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 | 401 | 403 | 404 | 429 | 500

### POST /api/tools/metrics/v2/
`tools_metrics_v2_create` — Get keyword metrics v2
Fetch keyword metrics with optional global support when country is omitted. **What this endpoint does** - Validates keyword list and optional location fields - Supports country-specific or global requests - Returns the …
- Body: object
  - keywords* (array<string>) — List of keywords to get metrics for. Maximum 10000 keywords per request.
  - country (string) — Country code (e.g., 'in', 'us'). Omit for global data.
  - language (string) — Language code (e.g., 'en', 'hi')
- Auth: JWT/Token/Cookie
- Returns: 200 KeywordMetricsOutput | 400 | 500

### POST /api/tools/pagespeed/
`tools_pagespeed_create` — Analyze URLs with PageSpeed Insights
Analyze 1-5 URLs in parallel using Google PageSpeed Insights API. Each URL is analyzed for both mobile and desktop. Credits charged: 2.00 per successful URL.
- Body (required): PageSpeedInputRequest
  - urls* (array<string(uri)>) — List of URLs to analyze (1-5 URLs)
- Auth: JWT/Token/Cookie
- Returns: 200 PageSpeedBulkOutput

### POST /api/tools/serp-ranking/
`tools_serp_ranking_create` — Get SERP ranking data with keyword difficulty scores
Fetches SERP data and calculates keyword difficulty scores based on top 10 results. Optionally includes SERP URLs when serp=true. Credits charged: 0.20 per keyword on cache miss.
- Body (required): SERPRankingInputRequest
  - keywords* (array<string>) — List of keywords to check ranking data (max 1000)
  - country* (string) — Country code (e.g., 'us', 'in', 'uk')
  - serp (boolean) — Include SERP URLs in response (default: False)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 any | 500 any | 503

### POST /api/tools/serp/google/
`tools_serp_google_create` — Google SERP Results
Fetch search results for a keyword. **What this endpoint does** - Returns organic search results for a keyword - Supports country, language, device, and location inputs - Uses cache when possible - Uses `SERP_PROVIDER` …
- Body (required): SERPInputRequest
  - keyword* (string) — Search keyword
  - country (string) — Country code (e.g., 'us', 'uk', 'in')
  - device (any) — Device type * `desktop` - desktop * `mobile` - mobile
  - language (string) — Language code (e.g., 'en', 'es', 'fr')
  - num_results (integer) — Number of results (1-100)
  - latitude (number(double)?) — Latitude for location-based search (e.g., 40.7128 for New York)
  - longitude (number(double)?) — Longitude for location-based search (e.g., -74.0060 for New York)
  - dynamic (string?) — If not provided, returns static data
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 | 500

### POST /api/tools/sitemap/discover/
`tools_sitemap_discover_create` — Discover sitemap files
Find sitemap files for a website. **What this endpoint does** - Looks up sitemap locations for a website - Returns a bounded sitemap file list quickly for UI usage - Expands a discovered sitemap index by one level when …
- Body: object
  - url* (string) — Website URL (e.g., https://example.com)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 | 404 | 500 | 503

### POST /api/tools/sitemap/full-parse/
`tools_sitemap_full_parse_create` — Full sitemap parser
Discover and parse all sitemaps for a domain. **What this endpoint does** - Finds sitemap files for a domain - Parses nested sitemap indexes too - Returns URLs grouped by sitemap file - Includes last modified dates and …
- Body (required): SitemapFullParseInputRequest
  - domain* (string) — Domain name (e.g., example.com or https://example.com)
- Auth: JWT/Token/Cookie
- Returns: 200 SitemapFullParseOutput | 400 object | 404 object | 503 object | 504 object

### POST /api/tools/sitemap/parse/
`tools_sitemap_parse_create` — Parse sitemap and extract URLs
Extract page URLs and last modified dates from a sitemap file. **What this endpoint does** - Parses a sitemap XML file - Returns all page URLs found in that sitemap - Includes last modified dates when available - Can re…
- Body: object
  - sitemap_url* (string) — Sitemap XML URL (e.g., https://example.com/sitemap.xml)
  - fresh (boolean) — Force real-time fetch. Default: false
  - freshness_window_in_days (integer) — Cache validity in days. Accept cached data if age < this value. Default: 30 days. Example: 720 for 2 years
- Auth: JWT/Token/Cookie
- Returns: 200 SitemapParseResponse | 400 | 402 | 404 | 500

### POST /api/tools/suggestions/
`tools_suggestions_create` — Get bulk keyword suggestions
Get keyword suggestions for multiple seed keywords in one request. **What this endpoint does** - Expands each keyword using the selected platform - Saves each result in keyword suggestion logs - Charges credits per keyw…
- Body: object
  - keywords* (array<string>) — List of keywords to get suggestions for (max 10)
  - platform (string) — Platform: google, bing, youtube, play_store, amazon, apple, llm
  - lang (string)
  - country (string)
  - include_questions (boolean) — Set to true to include question-based keywords
- Auth: JWT/Token/Cookie
- Returns: 200 BulkKeywordSuggestionOutput | 400 | 402 | 500

### POST /api/tools/suggestions/v2/
`tools_suggestions_v2_create` — Get keyword suggestions v2
Get keyword suggestions with optional A-Z expansion. **What this endpoint does** - Expands each input keyword using the selected platform - Supports either simple suggestions or full A-Z expansion - Can include question…
- Body (required): KeywordSuggestionV2Request
  - keywords* (array<string>) — List of keywords to get suggestions for (max 25)
  - platform (any) — Platform: google, youtube, play_store, amazon, apple, llm * `google` - google * `youtube` - youtube * `play_store` - pl…
  - lang (string) — Language code (e.g., en, hi, es)
  - country (string) — Country code (e.g., us, in, uk)
  - bulk (boolean) — Set to true for A-Z variations. Default false = simple suggestions only.
  - include_questions (boolean) — Set to true to include question-based keywords (Google only).
- Auth: JWT/Token/Cookie
- Returns: 200 KeywordSuggestionV2Output | 400 | 402 | 500

### POST /api/tools/title-description/
`tools_title_description_create` — Get page title and description
Fetch the page title and meta description for a URL. **What this endpoint does** - Reads the page title - Reads the meta description - Falls back to standard HTML tags when needed - Charges credits only on success **Inp…
- Body: TitleDescriptionRequestRequest
  - url (string)
  - urls (array<string>)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 | 402 | 500 | 502

### POST /api/tools/topic-gap/
`tools_topic_gap_create` — Advanced Topic Gap Analysis
Compare a primary site against competitor data to surface missing and weak topics. **What this endpoint does** - Analyzes topic overlap between your inputs - Returns gaps and weaker areas that need coverage - Supports d…
- Body (required): UnifiedEmbeddingInputRequest
  - self_data* (any) — Primary data as a string or non-empty list. Supports domain, page URL, sitemap URL, or keyword input.
  - competitor_data* (any) — Competitor data as a string or non-empty list. Supports domain, page URL, sitemap URL, or keyword input.
  - use_cache (boolean) — Whether upstream service should use cache
  - non_zero_volume_keyword (boolean) — Whether upstream service should return only keywords with non-zero volume
- Auth: JWT/Token/Cookie
- Returns: 200 TopicGapResponse | 400 | 402 | 500

### GET /api/tools/url-comparison/
`tools_url_comparison_list` — List URL comparisons
Return paginated URL comparison records owned by the authenticated user. This endpoint returns up to 1000 records per page. Use project_id to filter records by project. If no project filter is sent, all records owned by…
- Query: fields (string) — Comma-separated response fields for list results. Example: id,url,organic_traffic_goal,pr…; page (integer) — A page number within the paginated result set.; project_id (integer) — Optional project ID filter. Returns records linked to this project.
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<UrlComparisonListResponse>

### POST /api/tools/url-comparison/
`tools_url_comparison_create` — Create URL comparison
Create URL comparison records. This API charges 1 credit. Send a single object to create one row, or send a raw array of objects to create multiple rows in one request. Bulk requests allow up to 1000 rows. Required fiel…
- Body (required): UrlComparisonWriteRequest
  - url* (string) — Target page URL. If scheme is missing, backend adds https:// automatically.
  - last_30_days_impression (integer) — Optional last 30 days impressions for the target URL. Defaults to 0 when omitted.
  - organic_traffic_goal* (integer) — Organic traffic goal used to calculate per_day and share.
  - direct_competitor (array<string>) — Optional direct competitor URLs. Send up to 20 URLs.
  - indirect_competitor (array<string>) — Optional indirect competitor URLs. Send up to 20 URLs.
  - slug_keyword (string) — Optional. If missing, backend generates it from the last URL segment.
  - project_id* (integer) — Project ID. Project lookup is limited to authenticated user's projects.
  - country (string) — Optional country code. Priority is project country, then this country, then US.
  - volume (boolean) — When true, fetch country and global slug keyword volume. Defaults to false when omitted.
- Auth: JWT/Token/Cookie
- Returns: 201 UrlComparisonRead | 400 | 402 | 500

### DELETE /api/tools/url-comparison/{id}/
`tools_url_comparison_destroy` — Delete URL comparison
Hard delete one URL comparison record by ID. Delete does not charge credits.
- Path: id* (integer) — A unique integer value identifying this URL Comparison.
- Auth: JWT/Token/Cookie
- Returns: 200

### GET /api/tools/url-comparison/{id}/
`tools_url_comparison_retrieve` — Get URL comparison
Return one project-scoped URL comparison record by ID. Project owner/admin/viewer users with active project access can retrieve it. Users without active project access receive 404.
- Path: id* (integer) — A unique integer value identifying this URL Comparison.
- Auth: JWT/Token/Cookie
- Returns: 200 UrlComparisonRead | 404

### PUT /api/tools/url-comparison/{id}/
`tools_url_comparison_update` — Update URL comparison
Fully update a URL comparison record by ID. This API charges 1 credit. Required fields: url, organic_traffic_goal, project_id. Optional fields: last_30_days_impression, direct_competitor, indirect_competitor, slug_keywo…
- Path: id* (integer) — A unique integer value identifying this URL Comparison.
- Body (required): UrlComparisonWriteRequest
  - url* (string) — Target page URL. If scheme is missing, backend adds https:// automatically.
  - last_30_days_impression (integer) — Optional last 30 days impressions for the target URL. Defaults to 0 when omitted.
  - organic_traffic_goal* (integer) — Organic traffic goal used to calculate per_day and share.
  - direct_competitor (array<string>) — Optional direct competitor URLs. Send up to 20 URLs.
  - indirect_competitor (array<string>) — Optional indirect competitor URLs. Send up to 20 URLs.
  - slug_keyword (string) — Optional. If missing, backend generates it from the last URL segment.
  - project_id* (integer) — Project ID. Project lookup is limited to authenticated user's projects.
  - country (string) — Optional country code. Priority is project country, then this country, then US.
  - volume (boolean) — When true, fetch country and global slug keyword volume. Defaults to false when omitted.
- Auth: JWT/Token/Cookie
- Returns: 200 UrlComparisonRead | 400 | 402 | 500

### POST /api/tools/us-vs-competitor-analysis/
`tools_us_vs_competitor_analysis_create` — Start us vs competitor analysis
Queue a report job that compares one self URL against up to three competitor URLs. When fresh=false and the same normalized report payload is submitted again within 24 hours, the API returns the existing queued, running…
- Body (required): UsVsCompetitorAnalysisRequestRequest
  - self_url* (string)
  - competitor_urls* (array<string>)
  - country (string)
  - fresh (boolean)
  - include_pagespeed (boolean)
- Auth: JWT/Token/Cookie
- Returns: 200 UsVsCompetitorAnalysisStartResponse | 400 | 402 | 500

### GET /api/tools/us-vs-competitor-analysis/jobs/history/
`tools_us_vs_competitor_analysis_jobs_history_retrieve` — List us vs competitor analysis jobs
List the authenticated user's us vs competitor analysis jobs. The response is lightweight and does not include the full report result. Use the job status endpoint to load a selected job's full result.
- Query: end_date (string(date)); limit (integer); offset (integer); start_date (string(date))
- Auth: JWT/Token/Cookie
- Returns: 200 UsVsCompetitorAnalysisJobHistoryResponse | 400 | 500

### GET /api/tools/us-vs-competitor-analysis/jobs/{job_id}/
`tools_us_vs_competitor_analysis_jobs_retrieve` — Get us vs competitor analysis job
Return the queued, running, completed, or failed status for a us vs competitor analysis job. Completed results include the frontend table and omit the raw per-URL results array.
- Path: job_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 UsVsCompetitorAnalysisJobStatusResponse | 404

### GET /api/tools/youtube-channel-data/
`tools_youtube_channel_data_retrieve` — Get channel videos
Fetch channel details and recent videos for a channel or handle. **What this endpoint does** - Normalizes a channel name into a channel URL - Returns channel information - Returns a list of recent videos - Charges credi…
- Query: channel_url* (string) — Channel URL or handle (e.g., @channelname); count (integer) — Number of videos to fetch (default: 30). First 100 videos cost 1 credit, then each additi…; gl (string) — Country code (default: IN); language (string) — Language code (default: en)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 | 402 | 500

### POST /api/tools/youtube-hashtag/
`tools_youtube_hashtag_create` — Get hashtag ideas
Generate hashtag ideas for a search term. **What this endpoint does** - Expands the input term into hashtag suggestions - Returns a unique list of hashtag ideas - Charges credits only when results are found **Input** - …
- Body: object
  - term* (string) — Search term for hashtag suggestions
  - gl* (string) — Country code (e.g., US, IN, UK)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 | 402 | 500

### GET /api/tools/youtube-video-detail/
`tools_youtube_video_detail_retrieve` — Get video details
Fetch detailed information about a video. **What this endpoint does** - Returns video metadata - Adds engagement statistics when available - Charges credits only on success **Input** - `video_url`: Video URL or video ID…
- Query: gl (string) — Country code (default: IN); language (string) — Language code (default: en); video_url* (string) — YouTube video URL or video ID
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 | 402 | 500

### POST /api/v2/topic-gap/
`v2_topic_gap_create` — Advanced Topic Gap Analysis
Compare a primary site against competitor data to surface missing and weak topics. **What this endpoint does** - Analyzes topic overlap between your inputs - Returns gaps and weaker areas that need coverage - Supports d…
- Body (required): UnifiedEmbeddingInputRequest
  - self_data* (any) — Primary data as a string or non-empty list. Supports domain, page URL, sitemap URL, or keyword input.
  - competitor_data* (any) — Competitor data as a string or non-empty list. Supports domain, page URL, sitemap URL, or keyword input.
  - use_cache (boolean) — Whether upstream service should use cache
  - non_zero_volume_keyword (boolean) — Whether upstream service should return only keywords with non-zero volume
- Auth: JWT/Token/Cookie
- Returns: 200 TopicGapResponse | 400 | 402 | 500

### GET /api/v2/topic-gap/jobs/history/
`v2_topic_gap_jobs_history_retrieve` — List Topic Gap jobs
Returns previous Topic Gap reports for the authenticated user.
- Query: limit (integer) — Number of jobs to return. Default 20, max 100.; offset (integer) — Number of jobs to skip. Default 0.
- Auth: JWT/Token/Cookie
- Returns: 200 TopicGapJobHistoryResponse | 401 | 500

### GET /api/v2/topic-gap/jobs/{job_id}/
`v2_topic_gap_jobs_retrieve` — Get Topic Gap job
Returns one saved Topic Gap report for the authenticated user. If the saved job is queued or running and has an upstream job id, the backend refreshes its status from the external V2 analyze API before responding.
- Path: job_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 TopicGapJobDetailResponse | 401 | 404 | 500

## Response schemas

### AdvertiserCompetitorsResponse
- success* (boolean)
- domain* (string)
- total_domains* (integer)
- items* (array<object>) — Advertiser domains with advertise URLs and shared keyword counts.

### BulkKeywordSuggestionOutput
- cached* (boolean)
- total_keywords* (integer)
- results* (array<KeywordSuggestion>)
- credits_charged* (number(double))

### CompetitorDomainsOutput
- success* (boolean)
- total_domains* (integer) — Total number of competitor domains returned
- limit_used* (integer) — Actual competitor analysis limit used (auto-capped: Free=50, Paid=100)
- domains* (array<CompetitorDomain>)
- message (string)

### CompetitorKeywordsOutput
- success* (boolean)
- total_keywords* (integer)
- keywords* (array<CompetitorKeyword>)
- pagination (object)
- message (string)

### Keyword
- id* (integer) [read-only]
- billing_profile (integer?)
- project* (integer)
- keyword* (string)
- country_code (string)
- language_code (string)
- device (any)
- search_engine (any)
- frequency (enum(weekly|monthly))
- location (string)
- is_active* (boolean) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### KeywordMetricsOutput
- cached* (boolean)
- data* (any)
- credits_charged* (number(double))

### KeywordSuggestionV2Output
- cached* (boolean)
- total_keywords* (integer)
- bulk_mode* (boolean)
- results* (array<KeywordSuggestion>)
- credits_charged* (number(double))

### PageSpeedBulkOutput
- results* (array<PageSpeedResult>)
- total_analyzed* (integer)
- successful* (integer)
- failed* (integer)
- total_credits_charged* (string(decimal))

### ProjectCompetitor
- id* (integer) [read-only]
- project* (integer)
- domain* (string)
- global_traffic (integer)
- priority (integer)
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### RankTrackerKeywordScoreResponse
- success* (boolean)
- cached (boolean)
- data* (array<RankTrackerKeywordScoreItem>)
- total_keywords* (integer)

### SitemapFullParseOutput
- domain* (string)
- total_urls* (integer)
- total_sitemaps* (integer)
- warnings (array<string>)
- sitemaps* (array<SitemapFile>)

### SitemapParseResponse
- url* (string(uri)) — Sitemap URL that was parsed
- status* (string) — Status: success or error
- urls* (array<SitemapURL>) — List of URLs with last modified dates
- count* (integer) — Number of URLs extracted
- total_found (integer) — Total URLs found before limiting
- credits_charged (string(decimal)) — Credits charged for this operation
- cached (boolean) — Whether result is from a previous fetch

### TopicGapJobDetailResponse
- success* (boolean)
- job_id* (integer)
- status* (string)
- self_data* (any)
- competitor_data* (any)
- request_payload* (any)
- result_available* (boolean)
- result* (any?)
- error* (string)
- created_at* (string(date-time))
- completed_at* (string(date-time)?)

### TopicGapJobHistoryResponse
- success* (boolean)
- total* (integer)
- limit* (integer)
- offset* (integer)
- jobs* (array<TopicGapJobSummary>)

### TopicGapResponse
- success* (boolean)
- job_id (integer)
- status (string)
- has_data (boolean)
- message (string?)
- missing_topics (any)
- weak_topics (any)
- total (integer)
- data (any)

### UrlComparisonListResponse
- count* (integer)
- next* (string?)
- previous* (string?)
- results* (array<UrlComparisonRead>)

### UrlComparisonRead
- id* (integer) [read-only]
- url* (string(uri))
- last_30_days_impression* (integer)
- organic_traffic_goal* (integer)
- direct_competitor* (any)
- indirect_competitor* (any)
- slug_keyword* (string)
- project_id* (integer?)
- project_name* (string?)
- country (string)
- per_day* (string) [read-only]
- share* (string) [read-only]
- slug_volume_country (integer?)
- slug_volume_global (integer?)
- volume* (boolean)

### UsVsCompetitorAnalysisJobHistoryResponse
- success* (boolean)
- total* (integer)
- limit* (integer)
- offset* (integer)
- jobs* (array<UsVsCompetitorAnalysisJobHistoryItem>)

### UsVsCompetitorAnalysisJobStatusResponse
- success* (boolean)
- job_id* (integer)
- status* (string)
- created_at* (string(date-time))
- completed_at* (string(date-time)?)
- result (any?)
- error (string)

### UsVsCompetitorAnalysisStartResponse
- success* (boolean)
- job_id* (integer)
- status* (string)
