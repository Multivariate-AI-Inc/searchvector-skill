# SearchVector API — analytics

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 16 endpoints.

### POST /api/dashboard/cwv/
`dashboard_cwv_create` — Get dashboard CWV data
Fetch Core Web Vitals for the requested URL or up to 10 URLs. The API checks PHONE and DESKTOP form factors in parallel, falls back from URL level data to origin level data when needed, and returns simplified dashboard-…
- Body: DashboardCruxRequestRequest
  - url (string) — Page URL or domain to fetch CrUX Core Web Vitals for.
  - urls (array<string>) — List of page URLs or domains. Maximum 10 URLs per request.
- Auth: JWT/Token
- Returns: 200 DashboardCruxAnyResponse | 400 | 402 | 404 | 500

### GET /api/dashboard/gsc-sitemap/
`dashboard_gsc_sitemap_retrieve` — Get dashboard GSC sitemap data
Returns sitemap submission details for a connected Search Console project. Use this endpoint to show the list of submitted sitemaps, submission and download dates, pending status, sitemap index status, content counts, w…
- Query: project_id* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 200 DashboardGSCSitemapResponse | 400 | 401 | 402 | 404 | 409 | 500 | 503

### GET /api/dashboard/gsc/
`dashboard_gsc_retrieve` — Get dashboard GSC data
Returns the main Search Console dashboard data for a connected project and date range. Use this endpoint to populate the dashboard overview cards, top pages, top queries, page and query opportunities, country breakdowns…
- Query: end_date* (string(date)) — End date (YYYY-MM-DD); project_id* (integer) — Project ID; start_date* (string(date)) — Start date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 DashboardGSCResponse | 400 | 401 | 402 | 403 | 404 | 409 | 500 | 503

### POST /api/dashboard/organic-competitor/
`dashboard_organic_competitor_create` — Get dashboard organic competitor data
Returns organic keyword data for one or more competitor domains. Use this endpoint to fill the competitor section of the dashboard with keyword, URL, ranking, traffic, and related metric rows for the provided competitor…
- Body (required): DashboardOrganicCompetitorRequestRequest
  - competitors* (array<string>) — List of competitor domains or URLs (max 50)
- Auth: JWT/Token
- Returns: 200 URLKeywordsOutput | 400 | 402 | 500 | 503

### POST /api/dashboard/organic-keywords/
`dashboard_organic_keywords_create` — Get dashboard organic keywords
Returns the top 10 organic keywords for one or more domains or URLs. This endpoint keeps the response small for dashboard widgets.
- Body (required): DashboardOrganicKeywordsRequestRequest
  - urls* (array<string>) — List of domains or URLs to fetch top organic keywords for
  - mode (any) — Use domain for domain-level match, or page for page-level match * `domain` - domain * `page` - page
- Auth: JWT/Token
- Returns: 200 URLKeywordsOutput | 400 | 402 | 500 | 503

### POST /api/dashboard/sitemap/
`dashboard_sitemap_create` — Get dashboard sitemap data
Find and parse sitemap information for a website so the dashboard can show the discovered sitemap files and sample URLs from each file. Send a website URL or domain in the request body. The response includes the normali…
- Body (required): DashboardSitemapRequestRequest
  - url* (string)
- Auth: JWT/Token
- Returns: 200 DashboardSitemapResponse | 400 | 402 | 404 | 500 | 503

### POST /api/dashboard/social-competitor/
`dashboard_social_competitor_create` — Get dashboard social competitor data
Compares a primary domain with one competitor domain and returns the top dashboard rows for shared or competitor-related query visibility. Use this endpoint to show how the selected domain compares with a competitor acr…
- Body (required): DashboardSocialCompetitorRequestRequest
  - domain* (string) — Primary domain to compare, e.g. example.com
  - competitor_domain* (string) — Competitor domain to compare, e.g. competitor.example.com
- Auth: JWT/Token
- Returns: 200 CHStatsOutput | 400 | 402 | 500 | 503

### POST /api/tools/ch/stats/
`tools_ch_stats_create` — Fetch Data for an Analytics Report
Fetch analytics data for a selected report. Send the report name in `query_name` and pass the required filters in `parameters`. This endpoint resolves templates by `query_name` from admin-managed query templates. Curren…
- Body (required): CHStatsInputRequest
  - query_name* (string) — Name of the active query template to execute. See the endpoint description for the current available query names and th…
  - parameters (any) — JSON object of parameters required by the selected query template. Parameter names depend on query_name.
- Auth: JWT/Token/Cookie
- Returns: 200 CHStatsOutput | 503

### GET /api/tools/ga4/accessible-properties/
`tools_ga4_accessible_properties_list` — Get accessible GA4 properties
List all GA4 properties accessible by user's OAuth token. Shows which are already connected.
- Query: property_id (integer) — GA4 Property ID (from /api/tools/ga4/properties/) - Used to fetch properties accessible b…; token_id (integer) — OAuth Token ID (from /api/integrations/status/) - Recommended for multi-account users to …
- Auth: JWT/Token/Cookie
- Returns: 200 array<AccessibleGA4Property> | 400 | 401 | 404

### POST /api/tools/ga4/custom-report/
`tools_ga4_custom_report_create` — Run custom GA4 report
Run an advanced custom Google Analytics 4 report for a connected property. Supports: - dimensions and metrics - date ranges - dimension filters - metric filters - order by metric or dimension - metric aggregations - kee…
- Body (required): GA4CustomReportInputRequest
  - property_id* (string) — GA4 Property ID (numeric, e.g. '123456789')
  - dimensions* (array<string>) — List of dimension names (e.g. ['date', 'sessionDefaultChannelGroup'])
  - metrics* (array<string>) — List of metric names (e.g. ['sessions', 'activeUsers'])
  - date_ranges* (array<GA4DateRangeRequest>) — Date ranges for the report (max 4)
  - order_bys (array<GA4CustomOrderByRequest>) — Optional order by clauses
  - dimension_filter (any) — Optional GA4 dimension filter expression
  - metric_filter (any) — Optional GA4 metric filter expression
  - metric_aggregations (array<enum(TOTAL|MINIMUM|MAXIMUM|COUNT)>) — Optional GA4 metric aggregations
  - limit (integer) — Max rows to return (default 10000, max 100000)
  - offset (integer) — Pagination offset (default 0)
  - keep_empty_rows (boolean) — Return rows whose metric values are all zero
  - currency_code (string) — Optional ISO 4217 currency code override, e.g. USD
- Auth: JWT/Token/Cookie
- Returns: 200 GA4CustomReportResponse | 400 | 401 | 402 | 500 | 502 | 503

### GET /api/tools/ga4/metadata/{propertyId}/
`tools_ga4_metadata_retrieve` — Get GA4 property metadata
Returns all available dimensions and metrics for a connected GA4 property, including custom dimensions and custom metrics defined in the property. Use this to discover what dimensions/metrics can be used in the report A…
- Path: propertyId* (string) — GA4 Property ID (numeric, e.g. 123456789)
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 401 | 404 | 500 | 502 | 503

### GET /api/tools/ga4/properties/
`tools_ga4_properties_retrieve` — List connected GA4 properties
Return the authenticated user's connected Google Analytics 4 properties. Use this endpoint to show the user's saved GA4 properties, connection status, reconnect status, property details, and sync timestamps.
- Auth: JWT/Token/Cookie
- Returns: 200 | 401

### POST /api/tools/ga4/properties/connect/
`tools_ga4_properties_connect_create` — Connect Selected GA4 Properties
Connect selected GA4 properties to user account. Returns detailed results with connected/failed properties.
- Body (required): GA4ConnectRequest
  - property_ids* (array<string>) — List of GA4 property IDs to connect (numeric format)
  - token_id* (integer) — OAuth token ID (from /api/integrations/status/ or accessible-properties API) - required to ensure correct token is used
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 401 | 404

### DELETE /api/tools/ga4/properties/{id}/
`tools_ga4_properties_destroy` — Disconnect GA4 Property
Disconnect a GA4 property from this project.
- Path: id* (integer) — GA4 Property ID
- Auth: JWT/Token/Cookie
- Returns: 200 | 404

### POST /api/tools/ga4/realtime/
`tools_ga4_realtime_create` — GA4 Realtime report
Fetch realtime data for a connected GA4 property (last 30 minutes). No date ranges needed — always returns current active data. **Available realtime dimensions:** `country`, `city`, `deviceCategory`, `operatingSystem`, …
- Body (required): GA4RealtimeInputRequest
  - property_id* (string) — GA4 Property ID (numeric, e.g. '123456789')
  - dimensions* (array<string>) — Realtime dimensions (e.g. ['country', 'deviceCategory', 'unifiedScreenName'])
  - metrics* (array<string>) — Realtime metrics (e.g. ['activeUsers', 'screenPageViews', 'eventCount'])
  - limit (integer) — Max rows to return (default 100, max 10000)
- Auth: JWT/Token/Cookie
- Returns: 200 GA4RealtimeResponse | 400 | 401 | 402 | 404 | 500 | 502 | 503

### POST /api/tools/ga4/report/
`tools_ga4_report_create` — Run GA4 report
Run a generic Google Analytics 4 report for a connected property. Send any combination of dimensions, metrics, date ranges and order by clauses — BE proxies directly to Google Analytics Data API v1beta. **Common dimensi…
- Body (required): GA4ReportInputRequest
  - property_id* (string) — GA4 Property ID (numeric, e.g. '123456789')
  - dimensions* (array<string>) — List of dimension names (e.g. ['date', 'sessionDefaultChannelGroup'])
  - metrics* (array<string>) — List of metric names (e.g. ['sessions', 'activeUsers'])
  - date_ranges* (array<GA4DateRangeRequest>) — Date ranges for the report (max 4)
  - order_bys (array<GA4OrderByRequest>) — Optional order by clauses
  - limit (integer) — Max rows to return (default 10000, max 100000)
  - offset (integer) — Pagination offset (default 0)
- Auth: JWT/Token/Cookie
- Returns: 200 GA4ReportResponse | 400 | 401 | 402 | 404 | 500 | 502 | 503

## Response schemas

### CHStatsOutput
- success* (boolean) — Query execution status
- query_name* (string) — Query template name
- rows* (integer) — Number of results
- data* (array<object>) — Query results

### DashboardCruxAnyResponse
- (DashboardCruxResponse | DashboardCruxBulkResponse)

### DashboardGSCResponse
- project_id* (integer)
- date_range* (DashboardDateRange)
- metric_cards* (OverviewResponse)
- top_pages* (DashboardTopPagesSection)
- top_queries* (DashboardTopQueriesSection)
- page_opportunities* (DashboardPageOpportunitiesSection)
- query_opportunities* (DashboardQueryOpportunitiesSection)
- top_countries* (DashboardTopCountriesSection)
- performance* (PerformanceResponse)
- charts* (ChartsResponse)

### DashboardGSCSitemapResponse
- project_id* (integer)
- property_url* (string)
- total_sitemaps* (integer)
- sitemaps* (array<DashboardGSCSitemapItem>)

### DashboardSitemapResponse
- normalized_url* (string(uri))
- main_sitemap_url* (string(uri))
- sitemaps* (array<DashboardSitemapFile>)
- warnings (array<string>)

### GA4CustomReportResponse
- rows* (array<object>)
- row_count* (integer)
- dimension_headers* (array<string>)
- metric_headers* (array<string>)
- totals* (array<object>)
- minimums (array<object>)
- maximums (array<object>)

### GA4RealtimeResponse
- rows* (array<object>)
- row_count* (integer)
- dimension_headers* (array<string>)
- metric_headers* (array<string>)

### GA4ReportResponse
- rows* (array<object>)
- row_count* (integer)
- dimension_headers* (array<string>)
- metric_headers* (array<string>)
- totals* (array<object>)

### URLKeywordsOutput
- success* (boolean)
- total_urls* (integer)
- total_unique_keywords* (integer)
- data* (array<URLKeywordsData>)
- pagination (object)
- message (string)
