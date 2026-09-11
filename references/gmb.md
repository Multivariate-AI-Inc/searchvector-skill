# SearchVector API — gmb

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 16 endpoints.

### GET /api/tools/gmb/accessible-accounts/
`tools_gmb_accessible_accounts_retrieve` — List accessible GMB accounts
Fetch all GMB accounts accessible to the authenticated user from Google API
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/tools/gmb/accounts/
`tools_gmb_accounts_list` — List connected GMB accounts
Get all GMB accounts connected by the authenticated user
- Auth: JWT/Token/Cookie
- Returns: 200 array<GMBAccount>

### POST /api/tools/gmb/accounts/connect/
`tools_gmb_accounts_connect_create` — Connect GMB accounts
Connect selected GMB accounts to user profile for tracking
- Body (required): ConnectGMBAccountsInputRequest
  - account_numbers* (array<string>) — List of GMB account numbers to connect
- Auth: JWT/Token/Cookie
- Returns: 201 array<GMBAccount>

### DELETE /api/tools/gmb/accounts/{account_id}/
`tools_gmb_accounts_destroy` — Disconnect GMB account
Disconnect a GMB account and remove all associated locations
- Path: account_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 | 404

### POST /api/tools/gmb/location/insights/
`tools_gmb_location_insights_create` — Get GMB location insights
Fetch insights data (views, searches, actions) for a specific GMB location
- Body (required): LocationInsightsInputRequest
  - location_id* (integer) — GMB Location ID
  - date_from* (string(date)) — Start date (YYYY-MM-DD)
  - date_to* (string(date)) — End date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/tools/gmb/locations/
`tools_gmb_locations_list` — List GMB locations
Get all business locations for connected GMB accounts
- Query: account_id (integer) — Filter by specific GMB account ID
- Auth: JWT/Token/Cookie
- Returns: 200 array<GMBLocation>

### POST /api/tools/gmb/reviews/ai-generate-replies/
`tools_gmb_reviews_ai_generate_replies_create` — Generate AI replies for reviews
Generate professional AI-powered replies for multiple GMB reviews using Google Gemini. Supports Hindi and English auto-detection.
- Body (required): AIGenerateBulkRepliesInputRequest
  - reviews* (array<AIGenerateReplyReviewItemRequest>) — List of reviews to generate replies for (max 10)
- Auth: JWT/Token/Cookie
- Returns: 200 AIGenerateBulkRepliesOutput

### POST /api/tools/gmb/reviews/batch/
`tools_gmb_reviews_batch_create` — Batch fetch GMB reviews
Fetch reviews for multiple GMB locations in a single request (up to 50 locations). More efficient than calling list_reviews for each location individually.
- Body (required): BatchGMBReviewsInputRequest
  - account_id* (integer) — GMB Account ID
  - location_ids* (array<integer>) — List of GMB Location IDs (max 50)
  - page_size (integer) — Number of reviews per page (max 50)
  - page_token (string) — Pagination token for fetching next page
  - order_by (any) — Sort order for reviews * `updateTime desc` - Most Recent First * `rating` - Lowest Rating First * `rating desc` - Highe…
  - ignore_rating_only_reviews (boolean) — Exclude reviews that have only rating without text comment
- Auth: JWT/Token/Cookie
- Returns: 200 BatchGMBReviewsOutput

### POST /api/tools/gmb/reviews/list/
`tools_gmb_reviews_list_create` — List GMB reviews
Fetch reviews for a specific GMB location
- Body (required): ListReviewsInputRequest
  - location_id* (integer) — GMB Location ID
  - page_size (integer) — Number of reviews per page (max 50)
- Auth: JWT/Token/Cookie
- Returns: 200 array<GMBReview>

### POST /api/tools/gmb/reviews/reply/
`tools_gmb_reviews_reply_create` — Reply to GMB review(s)
Post reply to one or multiple customer reviews on GMB. Supports single and bulk modes.
- Body (required): ReplyReviewInputRequest
  - location_id* (integer) — GMB Location ID
  - review_id (string) — GMB Review ID (single mode)
  - reply_text (string) — Reply message text (single mode, max 4000 characters)
  - reviews (array<object>) — List of reviews with reply texts (bulk mode, max 50)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/tools/gmb/templates/
`tools_gmb_templates_list` — List GMB reply templates
Get all reply templates for authenticated user
- Query: page (integer) — A page number within the paginated result set.
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<GMBReplyTemplate>

### POST /api/tools/gmb/templates/
`tools_gmb_templates_create` — Create GMB reply template
Create new reply template for GMB reviews
- Body (required): GMBReplyTemplateRequest
  - title* (string) — Template name (e.g., 'Thank You - Positive Review')
  - text* (string) — Reply text template (max 4000 chars as per Google limit)
- Auth: JWT/Token/Cookie
- Returns: 201 GMBReplyTemplate

### DELETE /api/tools/gmb/templates/{id}/
`tools_gmb_templates_destroy` — Delete GMB reply template
Delete reply template by ID
- Path: id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204

### GET /api/tools/gmb/templates/{id}/
`tools_gmb_templates_retrieve` — Get GMB reply template
Get single reply template by ID
- Path: id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 GMBReplyTemplate

### PATCH /api/tools/gmb/templates/{id}/
`tools_gmb_templates_partial_update` — Partially update GMB reply template
Update reply template (partial update)
- Path: id* (integer)
- Body: PatchedGMBReplyTemplateRequest
  - title (string) — Template name (e.g., 'Thank You - Positive Review')
  - text (string) — Reply text template (max 4000 chars as per Google limit)
- Auth: JWT/Token/Cookie
- Returns: 200 GMBReplyTemplate

### PUT /api/tools/gmb/templates/{id}/
`tools_gmb_templates_update` — Update GMB reply template
Update reply template (full update)
- Path: id* (integer)
- Body (required): GMBReplyTemplateRequest
  - title* (string) — Template name (e.g., 'Thank You - Positive Review')
  - text* (string) — Reply text template (max 4000 chars as per Google limit)
- Auth: JWT/Token/Cookie
- Returns: 200 GMBReplyTemplate

## Response schemas

### AIGenerateBulkRepliesOutput
- total_reviews* (integer)
- success_count* (integer)
- failed_count* (integer)
- results* (array<AIGeneratedReplyItem>)

### BatchGMBReviewsOutput
- location_reviews* (array<BatchGMBLocationReviews>)
- total_locations* (integer)
- total_reviews* (integer)
- next_page_token* (string?)

### GMBReplyTemplate
- id* (integer) [read-only]
- title* (string) — Template name (e.g., 'Thank You - Positive Review')
- text* (string) — Reply text template (max 4000 chars as per Google limit)
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]
