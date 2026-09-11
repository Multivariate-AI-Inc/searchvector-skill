# SearchVector API — misc

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 30 endpoints.

### GET /api/ai/prompts/
`ai_prompts_list` — List all AI prompts with variables
Returns all AI prompts along with the list of variables extracted from each prompt template.
- Auth: JWT/Token/Cookie
- Returns: 200 array<AIPrompt>

### GET /api/changelog/
`changelog_list` — List accessible changelog rows
List manual changelog and revision history rows from active projects shared with the authenticated user. Activity values: - Title and Meta: title_and_meta - Changed Body Content: changed_body_content - Interlinking: int…
- Query: activity (enum(changed_body_content|interlinking|other|page_speed_improvements|revamped_page_design|schema_or_other_technical_attributes|…1 more)) — Filter by activity. Activity values: - Title and Meta: title_and_meta - Changed Body Cont…; ordering (enum(-created_at|-update_date|created_at|update_date)) — Order by created_at or update_date; page (integer) — A page number within the paginated result set.; project (integer) — Filter by project ID; search (string) — Search URL, activity, or description; update_from (string(date)) — Filter rows updated on or after this date; update_to (string(date)) — Filter rows updated on or before this date
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<Changelog>

### GET /api/notifications/
`notifications_retrieve` — Get all notifications
Get the latest 100 notifications for the current user with unread count.
- Auth: JWT/Token/Cookie
- Returns: 200 NotificationListResponse

### POST /api/notifications/mark-all-read/
`notifications_mark_all_read_create` — Mark all as read
Mark all notifications as read for current user.
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/notifications/unread-count/
`notifications_unread_count_retrieve` — Get unread count
Get only the unread notification count (for badge).
- Auth: JWT/Token/Cookie
- Returns: 200 object

### DELETE /api/notifications/{notification_id}/
`notifications_destroy` — Delete notification
Delete a specific notification.
- Path: notification_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204

### POST /api/notifications/{notification_id}/mark-read/
`notifications_mark_read_create` — Mark notification as read
Mark a specific notification as read.
- Path: notification_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 Notification

### GET /api/projects/{project_pk}/changelog/
`projects_changelog_list` — List changelog rows
List manual changelog and revision history rows for a project. Any active project member can read rows. Activity values: - Title and Meta: title_and_meta - Changed Body Content: changed_body_content - Interlinking: inte…
- Path: project_pk* (integer) — Project ID
- Query: activity (enum(changed_body_content|interlinking|other|page_speed_improvements|revamped_page_design|schema_or_other_technical_attributes|…1 more)) — Filter by activity. Activity values: - Title and Meta: title_and_meta - Changed Body Cont…; ordering (enum(-created_at|-update_date|created_at|update_date)) — Order by created_at or update_date; page (integer) — A page number within the paginated result set.; search (string) — Search URL, activity, or description; update_from (string(date)) — Filter rows updated on or after this date; update_to (string(date)) — Filter rows updated on or before this date
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<Changelog> | 403 | 404

### POST /api/projects/{project_pk}/changelog/
`projects_changelog_create` — Create changelog row
Create a project-scoped manual changelog row. Only project owner/admin can create rows. Activity values: - Title and Meta: title_and_meta - Changed Body Content: changed_body_content - Interlinking: interlinking - Schem…
- Path: project_pk* (integer)
- Body (required): ChangelogWriteRequest
  - url* (string(uri))
  - activity* (enum(title_and_meta|changed_body_content|interlinking|schema_or_other_technical_attributes|revamped_page_design|other|…1 more))
  - update_date* (string(date))
  - description (string) — Optional plain text or Markdown description.
- Auth: JWT/Token/Cookie
- Returns: 201 Changelog | 400 | 403 | 409

### DELETE /api/projects/{project_pk}/changelog/{id}/
`projects_changelog_destroy` — Delete changelog row
Hard delete a changelog row. Only project owner/admin can delete rows.
- Path: id* (integer) — A unique integer value identifying this Changelog Row.; project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204 | 403 | 404 | 409

### GET /api/projects/{project_pk}/changelog/{id}/
`projects_changelog_retrieve` — Get changelog row
Get one changelog row visible to project members.
- Path: id* (integer) — Changelog row ID; project_pk* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 200 Changelog | 403 | 404

### PATCH /api/projects/{project_pk}/changelog/{id}/
`projects_changelog_partial_update` — Partially update changelog row
Partially update a changelog row. Only project owner/admin can update rows. Activity values: - Title and Meta: title_and_meta - Changed Body Content: changed_body_content - Interlinking: interlinking - Schema or other t…
- Path: id* (integer) — A unique integer value identifying this Changelog Row.; project_pk* (integer)
- Body: PatchedChangelogWriteRequest
  - url (string(uri))
  - activity (enum(title_and_meta|changed_body_content|interlinking|schema_or_other_technical_attributes|revamped_page_design|other|…1 more))
  - update_date (string(date))
  - description (string) — Optional plain text or Markdown description.
- Auth: JWT/Token/Cookie
- Returns: 200 Changelog | 400 | 403 | 409

### PUT /api/projects/{project_pk}/changelog/{id}/
`projects_changelog_update` — Update changelog row
Update a changelog row. Only project owner/admin can update rows. Activity values: - Title and Meta: title_and_meta - Changed Body Content: changed_body_content - Interlinking: interlinking - Schema or other technical a…
- Path: id* (integer) — A unique integer value identifying this Changelog Row.; project_pk* (integer)
- Body (required): ChangelogWriteRequest
  - url* (string(uri))
  - activity* (enum(title_and_meta|changed_body_content|interlinking|schema_or_other_technical_attributes|revamped_page_design|other|…1 more))
  - update_date* (string(date))
  - description (string) — Optional plain text or Markdown description.
- Auth: JWT/Token/Cookie
- Returns: 200 Changelog | 400 | 403 | 409

### POST /api/tools/google-ads/gaql-query/
`tools_google_ads_gaql_query_create` — Execute Dynamic GAQL Query
Execute a GAQL query using a direct GAQL query string. Internal users only.
- Body (required): GAQLQueryInputRequest
  - account_id* (integer) — Google Ads Account ID
  - query* (string) — Full GAQL query string to execute directly
- Auth: JWT/Token/Cookie
- Returns: 200 GAQLQueryResponse | 403

### POST /api/tools/google-ads/keyword-ideas/direct/
`tools_google_ads_keyword_ideas_direct_create` — Generate Keyword Ideas Direct
Generate keyword ideas and metrics from seed keywords using the direct upstream service. Internal users only. Credits charged: 2.00 per unique seed keyword.
- Body (required): KeywordIdeasInputRequest
  - seed_keywords* (array<string>) — Seed keywords to generate ideas from
  - location_codes (array<string>) — Country codes (e.g., ['us', 'ca']). Leave empty for global volume. Default: ['us']
  - language_code (string) — Language code (e.g., 'en' for English). Default: 'en'
  - fresh (boolean) — Whether to fetch fresh results. Default: true
  - fresh_days (integer) — Freshness window in days when fresh=true. Default: 30
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/tools/google-ads/mutate/
`tools_google_ads_mutate_create` — Universal Google Ads Mutate
Execute any Google Ads mutate operation — create, update, or remove — for any supported resource type. All requests are fully logged (user, IP, payload, response). --- ## `operations` array — each item supports: ### `re…
- Body (required): GoogleAdsMutateRequestRequest
  - account_id* (integer)
  - operations* (array<MutateOperationItemRequest>)
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 401 | 403 | 404 | 500

### POST /api/tools/historical-serp-data/
`tools_historical_serp_data_create` — Get historical SERP data
Fetch SERP results for one or more keywords using exact country and language filters. Keyword matching is case-insensitive. For each keyword, this endpoint only returns rows from the latest available added_date, ordered…
- Body (required): HistoricalSERPDataBulkRequestRequest
  - keywords* (array<string>) — List of keywords to search in historical SERP data.
  - country* (string) — Country code filter, for example `in` or `us`.
  - language* (string) — Language code filter, for example `en`.
  - limit (integer) — Maximum number of ranked URLs to return per keyword. Max 10.
- Auth: JWT/Token/Cookie
- Returns: 200 HistoricalSERPDataBulkResponse | 400 | 402 | 403 | 500 | 503

### POST /api/tools/keyword-research-database/
`tools_keyword_research_database_create` — Search keyword research database
Searches keyword phrases. Returns keyword matches grouped by each input keyword. Use `match=contains` to find phrases containing the input keyword, or `match=starts_with` / `match=ends_with` for prefix or suffix search.…
- Body (required): KeywordResearchDatabaseQueryRequest
  - keyword* (array<string>)
  - match (any)
  - limit (integer)
  - offset (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 KeywordResearchDatabaseResponse | 400 | 403 | 500 | 503

### POST /api/tools/public/keyword-suggestions/
`tools_public_keyword_suggestions_create` — Public Keyword Suggestions
Get keyword suggestions without authentication. Rate limited: 5/min, 20/day per IP. Returns max 10 results.
- Body: object
  - keyword* (string) — Seed keyword (1-100 chars)
  - source* (enum(google|youtube|amazon|playstore|appstore)) — Platform source
  - country (string) — ISO country code
  - language (string) — ISO language code
- Auth: JWT/Token/none
- Returns: 200 object | 400 | 429

### POST /api/tools/public/sitemap/
`tools_public_sitemap_create` — Public Sitemap Discovery/Parse
Discover sitemaps or extract URLs from sitemap. No authentication required. Rate limited: 3/min, 10/day per IP. - If website URL provided (e.g., example.com): Returns a fast, bounded list of sitemap URLs with partial/mo…
- Body: object
  - url* (string) — Website URL (e.g., example.com) or Sitemap URL (e.g., example.com/sitemap.xml)
- Auth: JWT/Token/none
- Returns: 200 object | 400 | 404 | 429 | 503

### POST /api/tools/site-audit/jobs/
`tools_site_audit_jobs_create` — Start site audit
Start a site audit job. This endpoint charges 3 credits only when the job is successfully started. If a completed report already exists for the same site URL and max_urls, and its CSV ZIP is valid and less than 30 days …
- Body (required): SiteAuditStartRequestRequest
  - url* (string)
  - max_depth (integer)
  - max_urls (integer)
  - scan_delay (number(double))
  - enable_javascript (boolean)
  - discover_sitemaps (boolean)
  - respect_robots (boolean)
  - include_external_links (boolean)
  - issue_exclusion_patterns (array<string>)
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditStartResponse | 400 | 401 | 402 | 403 | 500 | 503

### POST /api/tools/site-audit/jobs/{job_id}/cancel/
`tools_site_audit_jobs_cancel_create` — Cancel site audit
Cancel a running site audit job started by the authenticated user.
- Path: job_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditCancelResponse | 401 | 403 | 404 | 500 | 503

### GET /api/tools/site-audit/jobs/{job_id}/results/
`tools_site_audit_jobs_results_retrieve` — Get site audit results
Fetch site audit results for a job started by the authenticated user. Use type to select summary, pages, issues, links, resources, or sf-report.
- Path: job_id* (integer)
- Query: limit (integer) — Page size for paginated result types. Max 1000.; offset (integer) — Offset for paginated result types.; type (enum(issues|links|pages|resources|sf-report|summary)) — Result type to fetch.
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditResultsResponse | 400 | 401 | 403 | 404 | 500 | 503

### GET /api/tools/site-audit/jobs/{job_id}/status/
`tools_site_audit_jobs_status_retrieve` — Get site audit status
Get job status for a site audit started by the authenticated user.
- Path: job_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditStatusResponse | 401 | 403 | 404 | 500 | 503

### POST /api/tools/v1/aio-geo/
`tools_v1_aio_geo_create` — Check brand citation
Check whether a brand is cited for a keyword on the selected AI search surface. Available only for internal users.
- Body (required): AskRequestRequest
  - keyword* (string)
  - brand_name* (string)
  - brand_domain* (string)
  - surface (string)
- Auth: JWT/Token/Cookie/none
- Returns: 200 AskResponse | 400 | 403 | 500 | 503

### POST /api/tools/v2/aio-geo/
`tools_v2_aio_geo_create` — Check AIO GEO citation
Run an internal AIO GEO request through the configured proxy service. Available only for internal users.
- Body (required): AIOGeoRequestRequest
  - country* (string)
  - input* (string)
- Auth: JWT/Token/Cookie/none
- Returns: 200 AIOGeoResponse | 400 | 403 | 500 | 503

### GET /api/tools/whatsnew/
`tools_whatsnew_list` — Get What's New Announcements
Fetch active announcements/updates ordered by latest published time first.
- Auth: JWT/Token/Cookie/none
- Returns: 200 array<WhatsNew>

### POST /api/user/contact-us/
`user_contact_us_create` — Contact Us Form
Submit a contact us form. No authentication required.
- Body (required): ContactUsRequest
  - name* (string)
  - email* (string(email))
  - website_url (string)
  - message* (string)
  - phone_number (string)
- Auth: JWT/Token/none
- Returns: 201 | 400

### GET /api/user/user-interest/
`user_user_interest_retrieve` — Submit user interest
Capture user interest in features, waitlist signups, demo requests, and similar requests. - POST: Create a new interest entry (AllowAny - anonymous users allowed) - GET: Fetch user's own interest entries (IsAuthenticate…
- Auth: JWT/Token/Cookie/none
- Returns: 201 | 400

### POST /api/user/user-interest/
`user_user_interest_create` — Submit user interest
Capture user interest in features, waitlist signups, demo requests, and similar requests. - POST: Create a new interest entry (AllowAny - anonymous users allowed) - GET: Fetch user's own interest entries (IsAuthenticate…
- Body: object
  - name (string) — User's full name
  - email* (string) — User's email address
  - interested (string) — Feature name or JSON with interest details
  - role (string) — User's job role (e.g., Marketing Manager)
  - phone_number (string) — User's phone number (optional)
- Auth: JWT/Token/Cookie/none
- Returns: 201 | 400

## Response schemas

### AIOGeoResponse
- output (any)
- citations (any)
- raw (any)

### AskResponse
- keyword* (string)
- brand_cited* (boolean)
- cited_urls* (array<string(uri)>)
- evidence* (array<string>)
- checked_surface* (string)
- confidence* (enum(high|medium|low))
- notes* (string)

### Changelog
- id* (integer) [read-only]
- project* (integer) [read-only]
- project_name* (string) [read-only]
- url* (string(uri))
- activity* (enum(title_and_meta|changed_body_content|interlinking|schema_or_other_technical_attributes|revamped_page_design|other|…1 more))
- activity_display* (string) [read-only]
- update_date* (string(date))
- description (string)
- created_by* (integer) [read-only]
- created_by_email* (string(email)) [read-only]
- created_by_name* (string) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### GAQLQueryResponse
- query* (string) — Final GAQL query sent to Google Ads
- cached* (boolean) — Whether the results were served from cache
- results* (array<object>) — Query results as list of dictionaries
- row_count* (integer) — Number of rows returned
- query_resource_consumption (string) — Google Ads query resource consumption value

### HistoricalSERPDataBulkResponse
- success* (boolean) — Whether the request completed successfully.
- country* (string) — Country code used for the lookup.
- language* (string) — Language code used for the lookup.
- total_keywords* (integer) — Total keywords processed in this request.
- results* (array<HistoricalSERPDataKeywordResult>) — Grouped SERP results for each requested keyword.

### KeywordResearchDatabaseResponse
- success* (boolean)
- keyword* (array<string>)
- match* (string)
- limit* (integer)
- results* (array<KeywordResearchDatabaseResult>)

### Notification
- id* (integer) [read-only]
- type (enum(system|credit|integration|alert|update|report|…1 more))
- title* (string)
- message* (string)
- icon (string?)
- link (string?)
- is_read (boolean)
- created_at* (string(date-time)) [read-only]

### NotificationListResponse
- unread_count* (integer)
- notifications* (array<Notification>)

### SiteAuditCancelResponse
- success* (boolean)
- message (string)
- job (any)

### SiteAuditResultsResponse
- success* (boolean)
- job_id (integer)
- job (any)
- csv_export_status (string)
- csv_zip_url (string)
- csv_export_error (string)
- top_issues (any)
- report (any)
- total (integer)
- limit (integer)
- offset (integer)
- items (any)

### SiteAuditStartResponse
- success* (boolean)
- job_id* (integer)
- status* (string)
- message (string)
- csv_export_status (string)
- csv_zip_url (string)

### SiteAuditStatusResponse
- success* (boolean)
- job* (any)
- csv_export_status (string)
- csv_zip_url (string)
- csv_export_error (string)
