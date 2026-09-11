# SearchVector API — ai-tools

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 31 endpoints.

### POST /api/ai/generate-seo-meta/
`ai_generate_seo_meta_create` — Generate SEO titles/meta descriptions
Generate SEO-optimized titles and/or meta descriptions based on SERP data and custom prompts.
- Body (required): GenerateSEOMetaRequestRequest
  - type* (any) — Type of content to generate * `meta` - Meta Description Only * `title` - Title Only * `both` - Both Title and Meta
  - keyword* (string) — Keyword to generate SEO content for
  - prompt (string?) — Custom prompt for content generation (optional)
  - num_variations* (integer) — Number of variations to generate (1-5)
  - country (string) — Country code for SERP data (default: in)
  - use_brand_info (boolean) — Whether to include brand context from project description in prompt
  - project_id (integer?) — Project ID to fetch brand description from (required if use_brand_info=true)
- Auth: JWT/Token/Cookie
- Returns: 200 GenerateSEOMetaResponse

### GET /api/apps/search/
`apps_search_retrieve` — Search apps
Search for apps on Play Store or App Store.
- Query: gl (string); keyword* (string); lg (string); num (integer); platform (string)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400

### GET /api/apps/validate/
`apps_validate_retrieve` — Validate app
Validate app and return metadata.
- Query: gl (string); lg (string); package_id* (string); platform (string)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400

### POST /api/articles/extract/
`articles_extract_create` — Article Extraction from URLs
Extracts article content from provided list of URLs. Use 'fresh=true' to force real-time content fetch.
- Body (required): ArticleExtractionInputRequest
  - urls* (array<string(uri)>) — List of URLs to extract (max 100)
  - fresh (boolean) — Force real-time extraction. Default: False
  - freshness_window_in_days (integer) — Maximum age of data in days to consider valid. Default: 30 days
  - html (boolean) — Ask the external extractor to include HTML in its response. Default: True
- Auth: JWT/Token/Cookie
- Returns: 200 ArticleExtractionResponse | 400 any | 403 any | 500 any

### GET /api/articles/snapshot/
`articles_snapshot_retrieve` — List article snapshots
Returns stored article extraction snapshots. Use mode=domain to get the latest snapshot for each page under a domain. Use mode=page to get all snapshots for a single page ordered by date.
- Query: domain (string) — Required when mode is domain; mode* (enum(domain|page)) — Snapshot lookup mode; page_url (string) — Required when mode is page
- Auth: JWT/Token/Cookie
- Returns: 200 ArticleSnapshotResponse | 400 | 401 | 500

### POST /api/articles/title-meta/
`articles_title_meta_create` — Get title meta
Returns title and meta description data. Send exactly one input mode. Use domain to get latest active pages with pagination. Use url to get all title/meta history for one exact URL. Use urls to look up a list of exact U…
- Query: fields (string) — Comma-separated result row fields to return. Supported fields: url, title, meta_descripti…
- Body: TitleMetaLookupRequestRequest
  - urls (array<string(uri)>) — List of exact URLs to look up. Send only one of urls, url, or domain.
  - url (string(uri)) — Single exact URL. Returns all title and meta history records for this URL.
  - domain (string(uri)) — Domain URL. Returns latest active page title/meta rows for this domain.
  - limit (integer) — Domain mode only. Page size. Default 100, maximum 100.
  - offset (integer) — Domain mode only. Pagination offset. Use next_offset from the previous response.
  - title (string) — Domain mode only. Filter by title text.
  - title_regex (string) — Domain mode only. Filter by title regex.
  - meta_description (string) — Domain mode only. Filter by meta description text.
  - meta_description_regex (string) — Domain mode only. Filter by meta description regex.
  - url_filter (string) — Domain mode only. Filter by page URL text. Comma-separated values are supported.
  - url_exact (string) — Domain mode only. Filter by exact page URL or path. Comma-separated values are supported. Examples: https://example.com…
  - url_regex (string) — Domain mode only. Filter by page URL regex.
  - has_title (boolean) — Domain mode only. true returns rows with title, false returns rows without title.
  - has_meta_description (boolean) — Domain mode only. true returns rows with meta description, false returns rows without meta description.
  - last_extracted_from (string(date-time)) — Domain mode only. Return rows extracted on or after this datetime.
  - last_extracted_to (string(date-time)) — Domain mode only. Return rows extracted on or before this datetime.
  - include_failures (boolean) — Domain mode only. When true, also include failed extraction URLs from FailedArticleExtraction. Failed rows include only…
  - fields (string) — Optional comma-separated result row fields to return. Supported fields: url, title, meta_description, last_extracted_at…
- Auth: JWT/Token/Cookie
- Returns: 200 TitleMetaLookupResponse | 400 | 403 | 500

### POST /api/keyword-content-score/
`keyword_content_score_create` — Calculate keyword content scores
Analyze keyword occurrences in extracted article content. Calculates weighted scores based on keyword placement in title, meta description, headings, and body text.
- Body (required): KeywordContentScoreInputRequest
  - force (boolean) — Force real-time fetch (default: false)
  - data* (array<KeywordUrlPairRequest>) — Array of keyword-URL pairs to analyze
- Auth: JWT/Token/Cookie
- Returns: 200 KeywordContentScoreOutput

### POST /api/projects/{project_id}/ai/fetch-page/
`projects_ai_fetch_page_create` — Fetch page details
Scrape page title, meta description, content, and headings from a URL.
- Path: project_id* (integer)
- Body (required): FetchPageRequestRequest
  - url* (string(uri)) — URL of the page to fetch
- Auth: JWT/Token/Cookie
- Returns: 200 FetchPageResponse

### POST /api/projects/{project_id}/ai/generate-titles/
`projects_ai_generate_titles_create` — Generate SEO titles
Generate SEO-optimized titles using AI based on page content. Results are saved to history.
- Path: project_id* (integer)
- Body (required): GenerateTitlesRequestRequest
  - url* (string(uri)) — Page URL
  - title (string?) — Current page title
  - meta_description (string?) — Current meta description
  - content (string?) — Page content (truncated)
  - h1 (string?) — Main H1 heading
  - h2s (array<string>) — List of H2 headings
  - title_count (integer) — Number of titles to generate (1-10)
  - force_refresh (boolean) — Regenerate new titles (consumes credits)
- Auth: JWT/Token/Cookie
- Returns: 200 GenerateTitlesResponse

### POST /api/projects/{project_id}/ai/generate-titles/bulk/
`projects_ai_generate_titles_bulk_create` — Bulk generate SEO titles
Generate SEO-optimized titles for multiple selected URLs using the current title. WordPress post ID is required for WordPress flows, but optional when the user has a valid Webflow connection.
- Path: project_id* (integer)
- Body (required): BulkGenerateTitlesRequestRequest
  - items* (array<BulkItemInputRequest>) — List of items to generate titles for (max 10)
  - num_variants (integer) — Number of title variants per item (1-10)
  - force_refresh (boolean) — Regenerate new titles for all items (consumes credits)
- Auth: JWT/Token/Cookie
- Returns: 200 BulkGenerateTitlesResponse

### GET /api/projects/{project_id}/experiments/
`projects_experiments_list` — List experiments
Get all title experiments for a project.
- Path: project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 array<ExperimentList>

### POST /api/projects/{project_id}/experiments/
`projects_experiments_create` — Create experiment
Create a new title A/B testing experiment with variants.
- Path: project_id* (integer)
- Body (required): CreateExperimentRequest
  - url* (string(uri)) — URL of the page to test
  - wordpress_post_id (integer?) — WordPress post/page ID
  - name (string) — Optional experiment name
  - variants* (array<TitleVariantInputRequest>) — List of title variants (first should be original)
  - interval_days (integer) — Days between variant changes (0-90)
  - interval_minutes (integer) — Minutes to add to interval (0-1440 = 24 hours)
  - auto_apply_winner (boolean) — Auto-apply winning title to WordPress
  - scheduled_at (string(date-time)?) — When to start the experiment
- Auth: JWT/Token/Cookie
- Returns: 201 ExperimentDetail

### POST /api/projects/{project_id}/experiments/bulk-action/
`projects_experiments_bulk_action_create` — Bulk action on experiments
Perform bulk actions on multiple experiments in one request.
- Path: project_id* (integer)
- Body (required): BulkExperimentActionRequest
  - action* (any) — Action to perform on experiments * `pause` - Pause * `resume` - Resume * `cancel` - Cancel * `delete` - Delete * `sched…
  - experiment_ids* (array<integer>) — List of experiment IDs (max 50)
  - schedule_date (string(date-time)) — Schedule date (required when action is 'schedule')
- Auth: JWT/Token/Cookie
- Returns: 200 BulkActionResponse

### POST /api/projects/{project_id}/experiments/bulk-create/
`projects_experiments_bulk_create_create` — Bulk create experiments
Create multiple experiments at once with a master experiment container.
- Path: project_id* (integer)
- Body (required): BulkCreateExperimentsRequest
  - master_name* (string) — Name for the master experiment
  - interval_days (integer) — Days between variant changes (0-90)
  - interval_minutes (integer) — Minutes to add to interval (0-1440 = 24 hours)
  - auto_apply_winner (boolean) — Auto-apply winning title to WordPress
  - scheduled_at (string(date-time)?) — When to start all experiments
  - experiments* (array<BulkExperimentItemRequest>) — List of experiments to create (1-10 URLs)
- Auth: JWT/Token/Cookie
- Returns: 201 ExperimentDetail

### DELETE /api/projects/{project_id}/experiments/{experiment_id}/
`projects_experiments_destroy` — Delete experiment
Delete an experiment. Only allowed for draft/cancelled/completed experiments.
- Path: experiment_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204

### GET /api/projects/{project_id}/experiments/{experiment_id}/
`projects_experiments_retrieve` — Get experiment details
Get detailed information about a specific experiment.
- Path: experiment_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentDetail

### PUT /api/projects/{project_id}/experiments/{experiment_id}/
`projects_experiments_update` — Update experiment
Update experiment settings. Only allowed for draft/scheduled experiments.
- Path: experiment_id* (integer); project_id* (integer)
- Body (required): CreateExperimentRequest
  - url* (string(uri)) — URL of the page to test
  - wordpress_post_id (integer?) — WordPress post/page ID
  - name (string) — Optional experiment name
  - variants* (array<TitleVariantInputRequest>) — List of title variants (first should be original)
  - interval_days (integer) — Days between variant changes (0-90)
  - interval_minutes (integer) — Minutes to add to interval (0-1440 = 24 hours)
  - auto_apply_winner (boolean) — Auto-apply winning title to WordPress
  - scheduled_at (string(date-time)?) — When to start the experiment
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentDetail

### POST /api/projects/{project_id}/experiments/{experiment_id}/apply-winner/
`projects_experiments_apply_winner_create` — Apply winner to WordPress
Apply the winning title to WordPress. Requires WordPress post ID.
- Path: experiment_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentDetail

### POST /api/projects/{project_id}/experiments/{experiment_id}/cancel/
`projects_experiments_cancel_create` — Cancel experiment
Cancel an experiment. Cannot be undone.
- Path: experiment_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentDetail

### POST /api/projects/{project_id}/experiments/{experiment_id}/complete/
`projects_experiments_complete_create` — Complete experiment
Complete an experiment early and determine the winner.
- Path: experiment_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentDetail

### GET /api/projects/{project_id}/experiments/{experiment_id}/logs/
`projects_experiments_logs_list` — Get experiment logs
Get all activity logs for an experiment.
- Path: experiment_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 array<ExperimentLog>

### POST /api/projects/{project_id}/experiments/{experiment_id}/pause/
`projects_experiments_pause_create` — Pause experiment
Pause a running experiment.
- Path: experiment_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentDetail

### GET /api/projects/{project_id}/experiments/{experiment_id}/performance-report/
`projects_experiments_performance_report_retrieve` — Get experiment performance report
Fetch real-time GSC data for experiment variants and generate performance comparison report.
- Path: experiment_id* (integer); project_id* (integer)
- Query: end_date* (string(date)) — End date (YYYY-MM-DD); kpi (enum(clicks|ctr|impressions|position)) — KPI to analyze (default: impressions); start_date* (string(date)) — Start date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 PerformanceReportResponse

### POST /api/projects/{project_id}/experiments/{experiment_id}/reorder-pending-variants/
`projects_experiments_reorder_pending_variants_create` — Reorder pending variants
Reorder only pending variants. Completed and running variants cannot be reordered. Only allowed for running/paused experiments.
- Path: experiment_id* (integer); project_id* (integer)
- Body: object
  - variant_orders (array<object>)
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentDetail

### GET /api/projects/{project_id}/experiments/{experiment_id}/results/
`projects_experiments_results_retrieve` — Get experiment results
Get experiment results with comparison data between variants.
- Path: experiment_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentResults

### POST /api/projects/{project_id}/experiments/{experiment_id}/resume/
`projects_experiments_resume_create` — Resume experiment
Resume a paused experiment.
- Path: experiment_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentDetail

### POST /api/projects/{project_id}/experiments/{experiment_id}/revoke-cancel/
`projects_experiments_revoke_cancel_create` — Revoke cancelled experiment
Revoke a cancelled experiment and restore it to its previous status. Only allowed within 24 hours of cancellation.
- Path: experiment_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentDetail

### POST /api/projects/{project_id}/experiments/{experiment_id}/schedule/
`projects_experiments_schedule_create` — Schedule/Start experiment
Schedule an experiment to start at a specific time, or start immediately if no time provided.
- Path: experiment_id* (integer); project_id* (integer)
- Body: ScheduleExperimentRequest
  - scheduled_at (string(date-time)?) — When to start. If null, starts immediately.
- Auth: JWT/Token/Cookie
- Returns: 200 ExperimentDetail

### POST /api/projects/{project_id}/experiments/{experiment_id}/variants/{variant_id}/resume/
`projects_experiments_variants_resume_create` — Resume a skipped variant
Resume a skipped variant. It will be added to the end of the queue and run after all other pending variants.
- Path: experiment_id* (integer); project_id* (integer); variant_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/projects/{project_id}/experiments/{experiment_id}/variants/{variant_id}/skip/
`projects_experiments_variants_skip_create` — Skip a variant
Skip a pending variant so it won't be uploaded to WordPress. Only pending variants can be skipped.
- Path: experiment_id* (integer); project_id* (integer); variant_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/tools/citations/
`tools_citations_create` — Get citation sources
Run a citation search request through the configured AI proxy service and return only the citation sources.
- Body (required): AIOGeoRequestRequest
  - country* (string)
  - input* (string)
- Auth: JWT/Token/Cookie
- Returns: 200 AIOGeoCitationsResponse | 400 | 401 | 500 | 503

## Response schemas

### AIOGeoCitationsResponse
- citations* (array<any>)

### ArticleExtractionResponse
- total* (integer)
- successful* (integer)
- failed* (integer)
- results* (array<ExtractedArticleDetail>)

### ArticleSnapshotResponse
- mode* (enum(domain|page))
- domain (string)
- page_url (string(uri))
- total* (integer)
- results* (array<ArticleSnapshotItem>)

### BulkActionResponse
- success* (array<BulkActionResult>)
- failed* (array<BulkActionResult>)
- summary* (object)

### BulkGenerateTitlesResponse
- total_urls* (integer)
- successful* (integer)
- failed* (integer)
- results* (array<BulkUrlResult>)

### ExperimentDetail
- id* (integer)
- name* (string)
- url* (string(uri))
- wordpress_post_id* (integer?)
- status* (string)
- status_display* (string) [read-only]
- interval_days* (integer)
- interval_minutes* (integer)
- auto_apply_winner* (boolean)
- total_variants* (integer)
- total_duration_days* (integer)
- current_variant_index* (integer)
- scheduled_at* (string(date-time)?)
- started_at* (string(date-time)?)
- completed_at* (string(date-time)?)
- cancelled_at* (string(date-time)?)
- next_change_at* (string(date-time)?)
- created_at* (string(date-time))
- winner_variant_id* (integer?)
- winner_applied* (boolean)
- winner_applied_at* (string(date-time)?)
- variants* (array<TitleVariant>)
- schedule* (array<ExperimentScheduleItem>) [read-only]
- current_variant* (any?)
- winner* (any?)

### ExperimentResults
- experiment_id* (integer)
- status* (string)
- winner* (any?)
- variants* (array<TitleVariant>)
- improvement_percentage* (number(float)) [read-only]
- comparison* (object) [read-only]

### FetchPageResponse
- url* (string(uri))
- final_url* (string(uri)?)
- title* (string?)
- meta_description* (string?)
- content* (string?)
- content_length* (integer)
- h1* (string?)
- h2s* (array<string>)
- success* (boolean)
- error* (string?)

### GenerateSEOMetaResponse
- type* (string)
- keyword* (string)
- difficulty_score* (string) — Keyword difficulty score (0-100) or 'N/A' if no SERP data
- titles (array<string>) — Generated titles (if type=title or both)
- metas (array<string>) — Generated meta descriptions (if type=meta or both)

### GenerateTitlesResponse
- success* (boolean)
- generated_titles* (array<GeneratedTitle>)
- original_title* (string?)
- error* (string?)

### KeywordContentScoreOutput
- results* (array<KeywordScoreResult>)

### PerformanceReportResponse
- experiment* (ExperimentInfo)
- date_range* (object)
- kpi* (string)
- summary* (PerformanceReportSummary)
- winner* (any?)
- variants* (array<VariantPerformance>)

### TitleMetaLookupResponse
- success* (boolean)
- total* (integer) — Total rows available for this response mode.
- limit (integer) — Domain mode only. Current page size.
- offset (integer) — Domain mode only. Current pagination offset.
- next_offset (integer?) — Domain mode only. Offset for the next page, or null when no next page exists.
- has_next (boolean) — Domain mode only. True when another page exists.
- found_count* (integer) — Number of rows returned in this response.
- missing_count* (integer) — Number of requested URLs not found where applicable.
- results* (array<TitleMetaLookupResult>)
