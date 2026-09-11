# SearchVector API — google-ads

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 21 endpoints.

### GET /api/tools/google-ads/accessible-accounts/
`tools_google_ads_accessible_accounts_retrieve` — List Accessible Google Ads Accounts
Get all Google Ads accounts accessible by the user's OAuth token (for account selection)
- Query: account_id (integer) — Google Ads Account ID (from /api/tools/google-ads/accounts/); token_id (integer) — OAuth Token ID (from /api/integrations/status/)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/tools/google-ads/accounts/
`tools_google_ads_accounts_retrieve` — List Google Ads Accounts
Get all connected Google Ads accounts for the authenticated user
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/tools/google-ads/accounts/connect/
`tools_google_ads_accounts_connect_create` — Connect Selected Google Ads Accounts
Create GoogleAdsAccount entries for selected customer IDs
- Body (required): ConnectGoogleAdsAccountInputRequest
  - customer_ids* (array<string>) — List of Google Ads customer IDs to connect (e.g., ['123-456-7890', '987-654-3210'])
  - manager_customer_id (string?) — Optional manager account ID (required for child accounts accessed via manager)
  - token_id* (integer) — OAuth token ID (from accessible-accounts API response) - required to ensure correct token is used
- Auth: JWT/Token/Cookie
- Returns: 200 object

### DELETE /api/tools/google-ads/accounts/{id}/
`tools_google_ads_accounts_destroy` — Disconnect Google Ads Account
Disconnect a Google Ads account from this project.
- Path: id* (integer) — Google Ads Account ID
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/tools/google-ads/ad-groups/performance/
`tools_google_ads_ad_groups_performance_create` — Ad Group Performance
Get ad group breakdown for a specific campaign
- Body (required): AdGroupPerformanceInputRequest
  - account_id* (integer) — Google Ads Account ID
  - campaign_id* (integer) — Campaign ID
  - date_from* (string(date)) — Start date (YYYY-MM-DD or ISO 8601)
  - date_to* (string(date)) — End date (YYYY-MM-DD or ISO 8601)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/tools/google-ads/campaigns/automation-controls/
`tools_google_ads_campaigns_automation_controls_retrieve` — List Campaign Automation Entries
Get shared campaign automation entries for the selected Google Ads account. Users who connected the same Google Ads customer_id in Searchvector will see the same campaign automation state.
- Query: account_id* (integer) — Google Ads Account ID
- Auth: JWT/Token/Cookie
- Returns: 200 CampaignAutomationListResponse

### POST /api/tools/google-ads/campaigns/automation-controls/
`tools_google_ads_campaigns_automation_controls_create` — Create Campaign Automation Entry
Create or update a shared campaign automation entry. Users who connected the same Google Ads customer_id in Searchvector will update the same campaign automation state.
- Body (required): CampaignAutomationInputRequest
  - account_id* (integer) — Google Ads Account ID
  - campaign_id* (string) — Google Ads Campaign ID
  - campaign_name* (string) — Campaign name
  - status* (any) — Automation status: enabled or disabled * `enabled` - Enabled * `disabled` - Disabled
  - current_bid (string(decimal)?) — Current bid amount (e.g., 10.50 for $10.50)
- Auth: JWT/Token/Cookie
- Returns: 200 CampaignAutomationCreateResponse

### POST /api/tools/google-ads/campaigns/performance/
`tools_google_ads_campaigns_performance_create` — Campaign Performance Dashboard
Get Google Ads campaign performance metrics including budget, serving status, bidding strategy, cost, and conversion values. Campaign rows also include any extra GAQL fields selected in the active campaign performance t…
- Body (required): CampaignPerformanceInputRequest
  - account_id* (integer) — Google Ads Account ID
  - date_from* (string(date)) — Start date (YYYY-MM-DD or ISO 8601)
  - date_to* (string(date)) — End date (YYYY-MM-DD or ISO 8601)
  - campaign_ids (array<integer>) — Optional: Filter by specific campaign IDs
  - cache (boolean) — Use cached data when available. Set false to always fetch fresh Google Ads campaign performance data.
- Auth: JWT/Token/Cookie
- Returns: 200 CampaignPerformanceResponse

### POST /api/tools/google-ads/campaigns/performance/auto-bid-tool/
`tools_google_ads_campaigns_performance_auto_bid_tool_create` — Auto Bid Tool - UAC Campaign Performance
Fetch UAC campaign performance with bidding metrics: target CPA, cost per conversion, impressions, clicks, budget
- Body (required): AutoBidToolInputRequest
  - account_id* (integer) — Google Ads Account ID
  - date_from* (string(date)) — Start date (YYYY-MM-DD or ISO 8601)
  - date_to* (string(date)) — End date (YYYY-MM-DD or ISO 8601)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/tools/google-ads/campaigns/uac/
`tools_google_ads_campaigns_uac_create` — Create UAC Campaign
Create Universal App Campaign in Google Ads with app install optimization. Campaign will be created in PAUSED status.
- Body (required): CreateUACCampaignRequestRequest
  - campaign_name* (string) — Campaign name
  - budget_name* (string) — Budget name
  - account_id* (integer) — Google Ads Account ID
  - app_id* (string) — Android package name (com.example.app) or iOS app ID (123456789)
  - app_platform* (any) — App platform * `ANDROID` - ANDROID * `IOS` - IOS
  - daily_budget* (number(double)) — Daily budget in dollars (minimum $1.00)
  - target_cpa* (number(double)) — Target cost per install in dollars
  - campaign_goal* (any) — Campaign optimization goal * `OPTIMIZE_INSTALLS_TARGET_INSTALL_COST` - OPTIMIZE_INSTALLS_TARGET_INSTALL_COST * `OPTIMIZ…
  - location_ids* (array<string>) — Location target constants (e.g., ['2356'] for India, ['2840'] for USA)
  - language_ids* (array<string>) — Language constants (e.g., ['1000'] for English, ['1003'] for Spanish)
  - variants* (array<UACAdVariantRequest>) — Ad variants (1-5 variants, each with headlines and descriptions)
  - campaign_status (any) — Campaign status - PAUSED (default) or ENABLED * `PAUSED` - PAUSED * `ENABLED` - ENABLED
  - start_date (string(date)?) — Campaign start date (YYYY-MM-DD)
  - end_date (string(date)?) — Campaign end date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 CreateUACCampaignResponse

### POST /api/tools/google-ads/change-history/
`tools_google_ads_change_history_create` — Get Change History
Fetch all changes (manual and automated) from Google Ads including Budget, Bidding, Audience, Location, Language, Conversion, Asset, Status, Feed, and Other changes
- Body (required): ChangeHistoryInputRequest
  - account_id* (integer) — Google Ads Account ID
  - date_from* (string(date)) — Start date (YYYY-MM-DD, cannot be more than 29 days in the past)
  - date_to* (string(date)) — End date (YYYY-MM-DD, max 30 days from start date)
  - change_types (array<enum(budget|bidding|audience|location|language|conversion|…5 more)>) — Types of changes to fetch (can select multiple)
  - campaign_id (string) — Optional: Filter by specific campaign ID
  - tool_filter (enum(GOOGLE_ADS_API|GOOGLE_ADS_WEB_CLIENT|GOOGLE_ADS_EDITOR|GOOGLE_ADS_MOBILE_APP|AUTOMATED_SYSTEM|OTHER) | enum()) — Optional: Filter by tool used to make changes * `` - All Tools * `GOOGLE_ADS_API` - Google Ads API * `GOOGLE_ADS_WEB_CL…
  - user_email_filter (string) — Optional: Filter by user email who made the change
  - item_changed_filter (enum(Campaign|Ad Group|Ad|Keyword|Campaign Criterion|Ad Group Criterion|…3 more) | enum()) — Optional: Filter by item/resource type that was changed * `` - All Items * `Campaign` - Campaign * `Ad Group` - Ad Grou…
  - search_query (string) — Optional: Free text search in resource names, descriptions, and values
- Auth: JWT/Token/Cookie
- Returns: 200 ChangeHistoryResponse

### POST /api/tools/google-ads/custom-query/
`tools_google_ads_custom_query_create` — Execute Custom GAQL Query
Execute custom GAQL query templates with dynamic parameters (campaign_id, date range, etc.)
- Body (required): CustomGAQLQueryInputRequest
  - account_id* (integer) — Google Ads Account ID
  - query_name* (string) — Name of the GAQL query template to execute
  - campaign_id (string) — Google Ads Campaign ID (optional - omit to get all campaigns)
  - date_from* (string(date)) — Start date (YYYY-MM-DD or ISO 8601)
  - date_to* (string(date)) — End date (YYYY-MM-DD or ISO 8601)
  - cache (boolean) — Use cached data when available. Set false to always fetch fresh Google Ads data.
  - limit (integer) — Maximum number of keyword rows to return (1-5000).
  - min_impressions (integer) — Minimum impressions for search-term rows.
  - kw_min_click (integer) — Minimum clicks for keyword queries (default: 5)
  - st_min_click (integer) — Minimum clicks for search term queries (default: 3)
  - st_budget_leak_min_click (integer) — Minimum clicks for budget leak search term queries (default: 5)
  - device_min_clicks (integer) — Minimum clicks for device performance queries (default: 10)
  - profit_all_conv_value_per_cost (number(double)) — Minimum ROAS threshold (conversion value / cost ratio, e.g., 1.5 means 150% return)
  - st_min_cost (integer) — Minimum cost threshold for search terms (in micros, e.g., 1000000 = $1)
  - device_min_cost (integer) — Minimum cost threshold for device performance (in micros, e.g., 1000000 = $1)
- Auth: JWT/Token/Cookie
- Returns: 200 CustomGAQLQueryResponse

### POST /api/tools/google-ads/geo/performance/
`tools_google_ads_geo_performance_create` — Geographic Performance
Get performance metrics by country/region for a campaign
- Body (required): GeoPerformanceInputRequest
  - account_id* (integer) — Google Ads Account ID
  - campaign_id (integer) — Campaign ID (optional - omit to get all campaigns)
  - date_from* (string(date)) — Start date (YYYY-MM-DD or ISO 8601)
  - date_to* (string(date)) — End date (YYYY-MM-DD or ISO 8601)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/tools/google-ads/keyword-ideas/
`tools_google_ads_keyword_ideas_create` — Generate Keyword Ideas
Generate keyword ideas and metrics from seed keywords. Credits charged: 2.00 per unique seed keyword.
- Body (required): KeywordIdeasInputRequest
  - seed_keywords* (array<string>) — Seed keywords to generate ideas from
  - location_codes (array<string>) — Country codes (e.g., ['us', 'ca']). Leave empty for global volume. Default: ['us']
  - language_code (string) — Language code (e.g., 'en' for English). Default: 'en'
  - fresh (boolean) — Whether to fetch fresh results. Default: true
  - fresh_days (integer) — Freshness window in days when fresh=true. Default: 30
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/tools/google-ads/keywords/performance/
`tools_google_ads_keywords_performance_create` — Keyword Performance
Get top-performing keywords within a campaign with quality scores
- Body (required): KeywordPerformanceInputRequest
  - account_id* (integer) — Google Ads Account ID
  - campaign_id (integer) — Campaign ID (optional - omit to get all campaigns)
  - date_from* (string(date)) — Start date (YYYY-MM-DD or ISO 8601)
  - date_to* (string(date)) — End date (YYYY-MM-DD or ISO 8601)
  - limit (integer) — Maximum number of keywords to return (1-5000)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/tools/google-ads/language-search/
`tools_google_ads_language_search_retrieve` — Search Google Ads languages
Search for targetable languages using Google Ads API. Auto-detects connected account.
- Query: name* (string) — Language name to search (e.g., "English", "Spanish", "Hindi")
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 402 | 403 | 500

### GET /api/tools/google-ads/location-search/
`tools_google_ads_location_search_retrieve` — Search Google Ads locations
Search for geo-target locations (countries, regions, cities) using Google Ads API. Auto-detects connected account.
- Query: name* (string) — Location name to search (e.g., "United States", "California", "San Francisco")
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 402 | 403 | 500

### GET /api/tools/google-ads/manager-accounts/{manager_id}/children/
`tools_google_ads_manager_accounts_children_retrieve` — Get Manager Account Children
Fetch all child accounts under a Manager (MCC) Google Ads account
- Path: manager_id* (string) — Manager account customer ID (e.g., '123-456-7890')
- Query: account_id (integer) — Google Ads Account ID (from /api/tools/google-ads/accounts/); token_id (integer) — OAuth Token ID (from /api/integrations/status/)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/tools/google-ads/mutate/logs/
`tools_google_ads_mutate_logs_retrieve` — List Google Ads mutate logs
Return Google Ads mutate actions performed by the authenticated user. Logs belonging to other users are never included.
- Query: created_from (string(date)) — Include logs created on or after this date (YYYY-MM-DD).; created_to (string(date)) — Include logs created on or before this date (YYYY-MM-DD).; page (integer) — Page number. Default: 1.; page_size (integer) — Rows per page. Default: 20, maximum: 100.; status (enum(failed|success)) — Filter logs by execution status.
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 401 | 403

### POST /api/tools/google-ads/search-terms/
`tools_google_ads_search_terms_create` — Search Terms Analysis
Get actual user search queries that triggered your ads. Find negative keywords and new opportunities.
- Body (required): SearchTermsInputRequest
  - account_id* (integer) — Google Ads Account ID
  - campaign_id (integer) — Campaign ID (optional - omit to get all campaigns)
  - date_from* (string(date)) — Start date (YYYY-MM-DD or ISO 8601)
  - date_to* (string(date)) — End date (YYYY-MM-DD or ISO 8601)
  - min_impressions (integer) — Minimum impressions threshold
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/tools/google-ads/search-terms/all/
`tools_google_ads_search_terms_all_create` — All Search Terms (Account Level)
Get all search terms across all campaigns for an account. No campaign filter required.
- Body (required): AllSearchTermsInputRequest
  - account_id* (integer) — Google Ads Account ID
  - date_from* (string(date)) — Start date (YYYY-MM-DD or ISO 8601)
  - date_to* (string(date)) — End date (YYYY-MM-DD or ISO 8601)
  - min_impressions (integer) — Minimum impressions threshold
- Auth: JWT/Token/Cookie
- Returns: 200 object

## Response schemas

### CampaignAutomationCreateResponse
- success* (boolean) — Whether the creation was successful
- campaign_id* (string) — Google Ads Campaign ID
- campaign_name* (string) — Campaign name
- account_id* (integer) — Account ID
- status* (string) — Automation status: enabled or disabled
- current_bid* (string(decimal)?) — Current bid amount
- created_at* (string(date-time)) — Entry creation timestamp

### CampaignAutomationListResponse
- campaigns* (array<CampaignAutomationItem>) — List of campaigns with automation status

### CampaignPerformanceResponse
- campaigns* (array<CampaignPerformanceRow>)
- total_campaigns* (integer)
- date_from* (string(date))
- date_to* (string(date))
- credits_charged* (number(double))

### ChangeHistoryResponse
- changes* (array<ChangeEvent>) — List of change events
- total_changes* (integer) — Total number of changes found

### CreateUACCampaignResponse
- campaign_id* (string) — Google Ads campaign ID
- campaign_name* (string) — Campaign name
- budget_name* (string) — Budget name
- campaign_resource_name* (string) — Full campaign resource name
- ad_groups* (array<UACAdGroupResponse>) — List of created ad groups (one per variant)
- status* (string) — Campaign status (PAUSED initially)
- app_id* (string) — App package name or iOS app ID
- app_platform* (string) — ANDROID or IOS
- daily_budget* (number(double)) — Daily budget in dollars
- target_cpa* (number(double)) — Target cost per install in dollars
- campaign_goal* (string) — Campaign optimization goal
- created_at* (string(date-time)) — Campaign creation timestamp

### CustomGAQLQueryResponse
- query_name* (string) — Name of the executed query template
- cached* (boolean) — Whether the results are from a previous fetch
- results* (array<object>) — Query results as list of dictionaries
- row_count* (integer) — Number of rows returned
- credits_charged* (string(decimal)) — Credits charged for this query
