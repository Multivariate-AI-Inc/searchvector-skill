# SearchVector API — apple-ads

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 4 endpoints.

### POST /api/apple-ads/bulk/
`apple_ads_bulk_create` — Apple Ads Bulk
Create, update, or delete multiple Apple Ads resources. Use this endpoint when the frontend needs to modify many campaigns, ad groups, keywords, negative keywords, or ads in one request. Each item should include a `corr…
- Body (required): AppleAdsPlatformBulkRequest
  - ad_account_id* (string)
  - resource* (enum(campaigns|adgroups|keywords|negative_keywords|ads))
  - operation* (enum(create|update|delete))
  - allow_partial_success (boolean)
  - items* (array<object>)
- Auth: JWT/Token/Cookie
- Returns: 200 AppleAdsPlatformResponse | 400 | 401 | 402 | 404

### POST /api/apple-ads/read/
`apple_ads_read_create` — Apple Ads Read
Read Apple Ads account and campaign data. Use this endpoint for read-only Apple Ads data needed by the frontend, such as account access, apps, campaigns, ad groups, keywords, ads, assets, product pages, and rejection re…
- Body (required): AppleAdsPlatformReadRequest
  - ad_account_id* (string)
  - resource* (enum(me|acls|search_apps|app_eligibilities|apps|app_locale_details|…11 more))
  - operation* (enum(get|query|search|list))
  - campaign_id (string)
  - adgroup_id (string)
  - id (string)
  - payload (object)
  - query_params (object)
- Auth: JWT/Token/Cookie
- Returns: 200 AppleAdsPlatformResponse | 400 | 401 | 402 | 404

### POST /api/apple-ads/report/
`apple_ads_report_create` — Apple Ads Report
Fetch Apple Ads performance reports. Use this endpoint for campaign, ad group, ad, keyword, search term, and impression share reporting. The frontend controls date range, pagination, sorting, filters, row totals, and gr…
- Body (required): AppleAdsPlatformReportRequest
  - ad_account_id* (string)
  - report_type* (enum(campaigns|adgroups|ads|keywords|search_terms|impression_share))
  - campaign_id (string)
  - payload* (object)
- Auth: JWT/Token/Cookie
- Returns: 200 AppleAdsPlatformResponse | 400 | 401 | 402 | 404

### POST /api/apple-ads/write/
`apple_ads_write_create` — Apple Ads Write
Create, update, patch, or delete a single Apple Ads resource. Use this endpoint when the frontend needs to modify one campaign, ad group, keyword, negative keyword, ad, shared budget, or creative. For multiple records, …
- Body (required): AppleAdsPlatformWriteRequest
  - ad_account_id* (string)
  - resource* (enum(campaigns|adgroups|keywords|negative_keywords|ads|shared_budgets|…1 more))
  - operation* (enum(create|update|patch|delete))
  - campaign_id (string)
  - adgroup_id (string)
  - id (string)
  - payload (object)
- Auth: JWT/Token/Cookie
- Returns: 200 AppleAdsPlatformResponse | 400 | 401 | 402 | 404

## Response schemas

### AppleAdsPlatformResponse
- success* (boolean)
- data (any)
- message (string)
