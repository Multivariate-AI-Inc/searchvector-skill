# SearchVector API — gsc-indexing

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 18 endpoints.

### GET /api/activity-logs/indexing/
`activity_logs_indexing_list` — List indexing activity logs
Returns paginated Google Indexing activity logs visible to the authenticated user. Users can see their own logs and logs for projects where they are active members.
- Query: date (string) — Filter by created date, YYYY-MM-DD; page (integer) — Page number; page_size (integer) — Page size, max 100; project_id (integer) — Filter by project ID; search (string) — Search user, project, service account, job, or URL; service_account_id (integer) — Filter by service account ID; source (string) — Filter by source: tool or automation; status (string) — Filter by log status
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<IndexingActivityLogList> | 400 | 401

### GET /api/activity-logs/indexing/{id}/
`activity_logs_indexing_retrieve` — Get indexing activity log
Returns one indexing activity log with per-URL submission results.
- Path: id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 IndexingActivityLogDetail | 401 | 404

### POST /api/projects/{project_id}/gsc/breakdown/
`projects_gsc_breakdown_create` — GSC Breakdown with Filtering
Break down GSC data by query, page, country, or device with optional filters.
- Path: project_id* (integer) — Project ID
- Body (required): GSCBreakdownRequestRequest
  - start_date* (string(date))
  - end_date* (string(date))
  - breakdown_by* (any) — Dimension to break down by: query, page, country, device * `query` - query * `page` - page * `country` - country * `dev…
  - limit (integer) — Maximum number of results (default: 100, max: 5000)
  - page_filter (string) — Filter pages (e.g., '/blog/', 'https://example.com/')
  - page_filter_type (any) — Page filter type: contains (default), not_contains, exact * `contains` - contains * `not_contains` - not_contains * `ex…
  - query_filter (string) — Filter queries (e.g., 'seo tools')
  - query_filter_type (any) — Query filter type: contains (default), not_contains, exact * `contains` - contains * `not_contains` - not_contains * `e…
  - country (string) — Filter by country code (e.g., IND, USA, GBR)
  - device (any) — Filter by device type * `DESKTOP` - DESKTOP * `MOBILE` - MOBILE * `TABLET` - TABLET
- Auth: JWT/Token/Cookie
- Returns: 200 GSCBreakdownResponse | 400 any | 401 any | 402 any | 403 any | 404 any | 409 any

### GET /api/projects/{project_id}/gsc/charts/
`projects_gsc_charts_retrieve` — Get GSC Charts Data
Returns trend and hourly pattern
- Path: project_id* (integer) — Project ID
- Query: end_date* (string(date)) — End date (YYYY-MM-DD); start_date* (string(date)) — Start date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 any | 401 any | 402 any | 403 any | 404 any | 409 any

### GET /api/projects/{project_id}/gsc/countries/
`projects_gsc_countries_retrieve` — Get GSC Countries List
Returns all countries with traffic data, sorted by clicks
- Path: project_id* (integer) — Project ID
- Query: end_date* (string(date)) — End date (YYYY-MM-DD); start_date* (string(date)) — Start date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 CountriesResponse | 400 any | 401 any | 402 any | 403 any | 404 any | 409 any

### POST /api/projects/{project_id}/gsc/custom-query/
`projects_gsc_custom_query_create` — GSC Custom Query (Raw Pass-through)
Raw pass-through to Google Search Console Search Analytics API. FE sends any GSC parameters and receives the full response.
- Path: project_id* (integer) — Project ID
- Body (required): GSCCustomQueryRequestRequest
  - startDate* (string(date))
  - endDate* (string(date))
  - dimensions (array<enum(country|device|page|query|searchAppearance|date|…1 more)>)
  - dimensionFilterGroups (array<GSCDimensionFilterGroupRequest>)
  - aggregationType (any)
  - type (any)
  - rowLimit (integer)
  - startRow (integer)
  - dataState (any)
- Auth: JWT/Token/Cookie
- Returns: 200 GSCCustomQueryResponse | 400 any | 401 any | 402 any | 403 any | 404 any | 409 any | 503 any

### GET /api/projects/{project_id}/gsc/keywords/
`projects_gsc_keywords_retrieve` — Get GSC Keywords Insights
Returns all queries, cannibalization issues, and opportunities. Use 'sections' parameter to filter response.
- Path: project_id* (integer) — Project ID
- Query: end_date* (string(date)) — End date (YYYY-MM-DD); limit (integer) — Number of results (1-5000, default: 100); query_contains (string) — Filter keywords containing this string (e.g., 'gsc'). Filtering happens server-side via G…; sections (string) — Comma-separated sections to include (e.g., 'all_queries' or 'all_queries,opportunities').…; start_date* (string(date)) — Start date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 any | 401 any | 402 any | 403 any | 404 any | 409 any

### POST /api/projects/{project_id}/gsc/mapping/
`projects_gsc_mapping_create` — Map Keywords and URLs to GSC Data
Maps user input keywords to GSC query data and URLs to GSC page data with case-insensitive exact matching. Returns GSC metrics for each keyword or URL, or N/A if not found. Credits charged: 3.00 per non-cached request.
- Path: project_id* (integer) — Project ID
- Body: KeywordMappingRequestRequest
  - keywords (array<string>) — List of keywords to map (max 25000)
  - urls (array<string>) — List of URLs to map (max 25000)
  - start_date (string(date)) — Start date (default: 30 days ago)
  - end_date (string(date)) — End date (default: yesterday)
- Auth: JWT/Token/Cookie
- Returns: 200 KeywordMappingResponse | 400 any | 401 any | 403 any | 404 any | 409 any

### GET /api/projects/{project_id}/gsc/overview/
`projects_gsc_overview_retrieve` — Get GSC Overview Stats
Returns aggregated metrics with previous period comparison
- Path: project_id* (integer) — Project ID
- Query: end_date* (string(date)) — End date (YYYY-MM-DD); start_date* (string(date)) — Start date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 OverviewResponse | 400 any | 401 any | 403 any | 404 any | 409 any

### POST /api/projects/{project_id}/gsc/page-query-breakdown/
`projects_gsc_page_query_breakdown_create` — GSC Breakdown by Dimensions
Returns GSC data grouped by dimensions and matches Google Search Console API format.
- Path: project_id* (integer) — Project ID
- Body (required): PageQueryBreakdownRequestRequest
  - dimensions* (array<enum(PAGE|QUERY|COUNTRY|DEVICE|DATE|SEARCH_APPEARANCE)>) — Array of GSC dimensions (e.g., ['PAGE'], ['QUERY'], ['PAGE', 'QUERY'])
  - startDate* (string(date)) — Start date in YYYY-MM-DD format
  - endDate* (string(date)) — End date in YYYY-MM-DD format
- Auth: JWT/Token/Cookie
- Returns: 200 PageQueryBreakdownResponse | 400 any | 401 any | 402 any | 403 any | 404 any | 409 any

### GET /api/projects/{project_id}/gsc/pages/
`projects_gsc_pages_retrieve` — Get GSC Pages Insights
Returns all pages with metrics, distribution stats, and daily fluctuation analysis.
- Path: project_id* (integer) — Project ID
- Query: end_date* (string(date)) — End date (YYYY-MM-DD); limit (integer) — Number of results (1-1000, default: 100); sections (string) — Comma-separated list of sections to return: all_pages, distribution, fluctuation (default…; start_date* (string(date)) — Start date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 any | 401 any | 402 any | 403 any | 404 any | 409 any

### GET /api/projects/{project_id}/gsc/performance/
`projects_gsc_performance_retrieve` — Get GSC Performance Insights
Returns device and search type breakdowns
- Path: project_id* (integer) — Project ID
- Query: end_date* (string(date)) — End date (YYYY-MM-DD); start_date* (string(date)) — Start date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 any | 401 any | 402 any | 403 any | 404 any | 409 any

### POST /api/projects/{project_id}/gsc/urls/
`projects_gsc_urls_create` — Filter GSC URLs
Filter GSC URLs with presets and custom filters
- Path: project_id* (integer)
- Body: GSCUrlsFilterQueryRequest
  - preset (any) — Preset filter to apply * `high_traffic_pages` - High Traffic Pages * `low_ctr_product_pages` - Low CTR Product Pages * …
  - date_range (any) — Preset date range * `last_7_days` - Last 7 Days * `last_14_days` - Last 14 Days * `last_28_days` - Last 28 Days * `last…
  - start_date (string(date)) — Custom start date (overrides date_range)
  - end_date (string(date)) — Custom end date (overrides date_range)
  - min_impressions (integer) — Minimum impressions
  - max_impressions (integer) — Maximum impressions
  - min_clicks (integer) — Minimum clicks
  - max_clicks (integer) — Maximum clicks
  - min_ctr (number(double)) — Minimum CTR (%)
  - max_ctr (number(double)) — Maximum CTR (%)
  - min_position (number(double)) — Minimum position
  - max_position (number(double)) — Maximum position
  - query_contains (string) — Search query contains
  - query_not_contains (string) — Search query excludes
  - page_contains (string) — URL contains
  - page_not_contains (string) — URL excludes
  - device (any) — Device type filter * `DESKTOP` - Desktop * `MOBILE` - Mobile * `TABLET` - Tablet
  - country (string) — Country code (e.g., IND, USA)
  - limit (integer) — Max results
- Auth: JWT/Token/Cookie
- Returns: 200 GSCUrlsFilterResponse | 400 any | 401 any | 402 any | 403 any | 404 any | 409 any

### GET /api/tools/google-indexing/quota/
`tools_google_indexing_quota_retrieve` — Get Google Indexing API Quota
Retrieve current quota usage and limits for a specific service account.\n\n**Query Parameters:**\n- `serviceAccountId` (required): Service account ID to get quota for\n\n**Example:**\n```\nGET /api/tools/google-indexing…
- Auth: JWT/Token/Cookie
- Returns: 200 GetQuotaOutput | 400 | 404 | 500

### DELETE /api/tools/google-indexing/service-account/
`tools_google_indexing_service_account_destroy` — Delete Service Account
Delete a Google Service Account by ID. **Request Body:** ```json { "id": 1 } ``` **Response (Success - 200):** ```json { "message": "Service account deleted successfully", "clientEmail": "service-account@project.iam.gse…
- Auth: JWT/Token/Cookie
- Returns: 200 DeleteServiceAccountOutput | 400 | 404 | 500

### GET /api/tools/google-indexing/service-account/
`tools_google_indexing_service_account_retrieve` — Get Service Accounts List
Retrieve all Google Service Accounts saved by the authenticated user. **Response Format:** ```json { "count": 2, "service_accounts": [ { "id": 1, "projectId": "your-project-id", "clientEmail": "service-account@project.i…
- Auth: JWT/Token/Cookie
- Returns: 200 GetServiceAccountsOutput | 500

### POST /api/tools/google-indexing/service-account/
`tools_google_indexing_service_account_create` — Save Google Service Account
Save or update Google Service Account credentials for Google Indexing API. **Request Body:** - `serviceAccountJson`: Base64-encoded service account JSON string **Service Account JSON Structure:** ```json { "type": "serv…
- Body (required): SaveServiceAccountInputRequest
  - serviceAccountJson* (string) — Base64-encoded service account JSON string
- Auth: JWT/Token/Cookie
- Returns: 200 SaveServiceAccountOutput | 400 | 500

### POST /api/tools/google-indexing/submit/
`tools_google_indexing_submit_create` — Submit URLs to Google Indexing API
Submit one or more URLs to Google Indexing API for indexing or removal.\n\n**Request Body:**\n```json\n{\n "urls": ["https://example.com/page1", "https://example.com/page2"],\n "type": "URL_UPDATED", // or "URL_DELETED"…
- Body (required): SubmitIndexingInputRequest
  - urls* (array<string(uri)>) — Array of URLs to submit (1-100 URLs)
  - type* (any) — Type of indexing request: URL_UPDATED or URL_DELETED * `URL_UPDATED` - URL_UPDATED * `URL_DELETED` - URL_DELETED
  - serviceAccountId* (integer) — Service account ID to use for indexing
- Auth: JWT/Token/Cookie
- Returns: 200 SubmitIndexingOutput | 400 | 404 | 429 | 500

## Response schemas

### CountriesResponse
- countries* (array<CountryItem>)
- total_countries* (integer)
- date_range* (object)

### DeleteServiceAccountOutput
- message* (string) — Success message
- clientEmail* (string(email)) — Deleted service account email
- deletedAt* (string(date-time)) — Timestamp when service account was deleted

### GSCBreakdownResponse
- breakdown* (array<BreakdownItem>)
- applied_filters* (object)

### GSCCustomQueryResponse
- rows* (array<GSCCustomQueryRow>)
- total_results* (integer)
- responseAggregationType (string?)

### GSCUrlsFilterResponse
- total_count* (integer)
- filters_applied* (object)
- urls* (array<GSCUrlItem>)

### GetQuotaOutput
- dailyLimit* (integer) — Daily quota limit (Google's default: 200)
- usedToday* (integer) — Number of requests used today
- remainingToday* (integer) — Remaining quota for today
- resetTime* (string(date-time)) — Timestamp when quota will reset (midnight UTC)
- lastUpdated* (string(date-time)) — Timestamp when quota was last updated

### GetServiceAccountsOutput
- count* (integer) — Total number of service accounts
- service_accounts* (array<ServiceAccountItem>) — List of service accounts

### IndexingActivityLogDetail
- id* (integer) [read-only]
- job_id (string(uuid)?)
- source* (enum(tool|automation))
- status* (enum(completed|partial_success|failed|skipped))
- indexing_type (string)
- user* (any?) [read-only]
- project* (any?) [read-only]
- service_account_email* (string(email)?)
- total_urls (integer)
- success_count (integer)
- failed_count (integer)
- skipped_count (integer)
- blocked_domains (any)
- quota_date (string(date)?)
- quota_daily_limit (integer)
- quota_used_before (integer)
- quota_used_after (integer)
- quota_remaining_after (integer)
- error_message (string)
- completed_at (string(date-time)?)
- created_at* (string(date-time)) [read-only]
- metadata (any)
- url_logs* (array<IndexingActivityURLLog>) [read-only]

### IndexingActivityLogList
- id* (integer) [read-only]
- job_id (string(uuid)?)
- source* (enum(tool|automation))
- status* (enum(completed|partial_success|failed|skipped))
- indexing_type (string)
- user* (any?) [read-only]
- project* (any?) [read-only]
- service_account_email* (string(email)?)
- total_urls (integer)
- success_count (integer)
- failed_count (integer)
- skipped_count (integer)
- blocked_domains (any)
- quota_date (string(date)?)
- quota_daily_limit (integer)
- quota_used_before (integer)
- quota_used_after (integer)
- quota_remaining_after (integer)
- error_message (string)
- completed_at (string(date-time)?)
- created_at* (string(date-time)) [read-only]

### KeywordMappingResponse
- keywords* (array<KeywordMappingItem>)
- urls* (array<URLMappingItem>)

### OverviewResponse
- current_period* (Metric)
- previous_period* (Metric)
- change* (Change)
- cache (boolean)

### PageQueryBreakdownResponse
- rows* (array<PageQueryBreakdownRow>)
- total_results* (integer)

### SaveServiceAccountOutput
- id* (integer) — Service account ID
- savedAt* (string(date-time)) — Timestamp when service account was saved

### SubmitIndexingOutput
- jobId* (string(uuid)) — Unique job identifier
- totalUrls* (integer) — Total number of URLs submitted
- status* (any) — Overall job status * `completed` - completed * `failed` - failed
- successCount* (integer) — Number of successful submissions
- failedCount* (integer) — Number of failed submissions
- skippedCount* (integer) — Number of URLs skipped due to site-level 403 filtering
- blockedDomains* (array<string>) — List of domains blocked due to 403 Forbidden errors in this batch
- results* (array<URLResult>) — Detailed results for each URL
