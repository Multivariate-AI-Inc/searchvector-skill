# SearchVector API — content

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 23 endpoints.

### GET /api/article-settings/
`article_settings_retrieve` — Get user article settings
Retrieve user's default wizard settings (auto-created if doesn't exist)
- Auth: JWT/Token/Cookie
- Returns: 200 UserArticleSettings

### PUT /api/article-settings/
`article_settings_update` — Update user article settings
Update user's default wizard settings
- Body: UserArticleSettingsRequest
  - default_word_count (integer)
  - default_perspective (string?)
  - default_tone (array<string>)
  - default_sales_approach (string?)
  - default_content_type (string?)
  - default_target_locations (array<string>)
  - default_language (string)
  - default_year_from (integer?)
  - default_year_to (integer?)
  - default_keywords (string)
  - default_brand_guidelines (string)
  - default_custom_instructions (string)
- Auth: JWT/Token/Cookie
- Returns: 200 UserArticleSettings

### GET /api/articles/
`articles_list` — List articles
Get paginated list of user's articles with filtering
- Query: language (string) — Filter by language code (e.g., en, ja, fr); ordering (string) — Sort field (created_at, -created_at, updated_at, -updated_at); page (integer) — A page number within the paginated result set.
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<ArticleList>

### POST /api/articles/
`articles_create` — Create article
Create new article and start AI generation in background. Returns immediately with status='queued'. Frontend should poll GET /articles/{id}/ to check status.
- Body: ArticleCreateRequest
  - articles (array<SingleArticleCreateRequest>) — Bulk mode
  - topic (string) — Single mode: Article topic or subject
  - source (any) — Article creation source * `ai` - ai * `manual` - manual * `imported` - imported
  - title (string) — Article title (for manual/imported mode)
  - meta_description (string) — Meta description (for manual/imported mode)
  - wordpress_post_id (integer?) — Linked WordPress post ID (for imported mode)
  - project_id (integer?) — Project ID this article belongs to
  - published_url (string(uri)?) — Published WordPress post URL
  - url (string(uri)?) — Alias for published_url
  - slug (string?) — URL slug of the article
  - word_count (integer?) — Target word count
  - language (string) — ISO 639-1 language code
  - country (string) — Target country/region (deprecated, use target_country instead)
  - target_country (string) — Target country code
  - mode (any) — Generation mode * `instant` - instant * `wizard` - wizard
  - generation_parameters (any) — AI generation settings per API requirements
  - category (string) — Article category
  - tags (array<string>) — Tags
  - self_url (string(uri)) — Client's own website URL for context
  - competitor_urls (array<string(uri)>) — Array of competitor URLs for analysis (max 10)
  - content_type (enum(informational|conversational|transactional) | enum() | enum(None)) — Content type for article generation * `informational` - informational * `conversational` - conversational * `transactio…
  - perspective (enum(positive|negative|neutral) | enum() | enum(None)) — Content perspective * `positive` - positive * `negative` - negative * `neutral` - neutral
  - tone (array<string>) — Array of tone options
  - sales_approach (enum(pro_sales|less_sales) | enum() | enum(None)) — Sales approach style * `pro_sales` - pro_sales * `less_sales` - less_sales
  - year_from (integer?) — Year range start
  - year_to (integer?) — Year range end
  - keywords (string) — SEO keywords (comma-separated)
  - brand_guidelines (string) — Brand voice and style guidelines
  - custom_instructions (string) — Additional custom instructions
  - target_locations (array<string>) — Target locations/regions
  - selected_title (string) — Pre-selected title
  - selected_meta_description (string) — Pre-selected meta description
  - outline (array<string>) — Pre-generated outline
  - content (string) — Pre-generated article content (Markdown)
- Auth: JWT/Token/Cookie
- Returns: 201 ArticleSimpleResponse

### POST /api/articles/generate-outline/
`articles_generate_outline_create` — Generate outline variations (single or bulk)
Generates outline variations based on title/meta. Supports SINGLE mode (1 request) or BULK mode (up to 5 requests). Does NOT create article. Returns outline_options array.
- Body: GenerateOutlineRequest
  - outlines (array<SingleOutlineRequestRequest>) — Bulk mode: Array of outline requests (max 5)
  - selected_title (string) — Single mode: User-selected title
  - selected_meta_description (string) — Single mode: User-selected meta description
  - topic (string) — Single mode: Article topic
  - content_type (any) — Single mode: Content type selected by user * `informational` - informational * `conversational` - conversational * `tra…
  - word_count (integer) — Single mode: Target word count
  - target_country (string) — Single mode: Target country code
  - language (string) — ISO 639-1 language code
  - self_url (string(uri)) — Client's own website URL
  - competitor_urls (array<string(uri)>) — Array of competitor URLs
  - perspective (enum(positive|negative|neutral) | enum() | enum(None)) — Content perspective * `positive` - positive * `negative` - negative * `neutral` - neutral
  - tones (array<string>) — Array of tone options
  - sales_approach (enum(pro_sales|less_sales) | enum() | enum(None)) — Sales approach style * `pro_sales` - pro_sales * `less_sales` - less_sales
  - year_from (integer?) — Year range start
  - year_to (integer?) — Year range end
  - brand_guidelines (string) — Brand voice, style guidelines
  - custom_instructions (string) — Additional custom instructions for content generation
  - keywords (string) — Keywords to incorporate in the outline
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/articles/generate-title-meta/
`articles_generate_title_meta_create` — Generate title and meta options (single or bulk)
Generates title/meta options based on topic. Supports SINGLE mode (1 topic) or BULK mode (up to 5 topics). Does NOT create article. Use POST /articles/ to create article with selected values.
- Body: TitleMetaGenerationRequest
  - generate_only (any) — What to generate * `titles` - titles * `meta_descriptions` - meta_descriptions * `both` - both
  - topics (array<SingleTopicRequest>) — Bulk mode: Array of topics (max 5)
  - topic (string) — Single mode: Article topic
  - word_count (integer) — Single mode: Target word count
  - target_country (string) — Single mode: Target country code
  - language (string) — ISO 639-1 language code
  - self_url (string(uri)) — Client's own website URL for context
  - competitor_urls (array<string(uri)>) — Array of competitor URLs for analysis
  - content_type (enum(informational|conversational|transactional) | enum() | enum(None)) — Content type for better title generation * `informational` - informational * `conversational` - conversational * `trans…
  - perspective (enum(positive|negative|neutral) | enum() | enum(None)) — Content perspective * `positive` - positive * `negative` - negative * `neutral` - neutral
  - tones (array<string>) — Array of tone options
  - sales_approach (enum(pro_sales|less_sales) | enum() | enum(None)) — Sales approach style * `pro_sales` - pro_sales * `less_sales` - less_sales
  - year_from (integer?) — Starting year for content relevance
  - year_to (integer?) — Ending year for content relevance
  - brand_guidelines (string) — Brand writing guidelines
  - custom_instructions (string) — Custom generation instructions
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/articles/{article_id}/generate-image/
`articles_generate_image_create` — Generate featured image for article
Generate AI-powered featured image for blog post using article content. Image size: 1200x675 (optimized for blog headers and social sharing). **Maximum 5 images can be generated per article.** After 5th generation, API …
- Path: article_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ImageGenerationResponse

### POST /api/articles/{article_id}/retry/
`articles_retry_create` — Retry article generation
Re-queue an article for generation. Works for articles with status: 'failed', 'error', 'queued' (stuck), or 'processing' (stuck). Cannot retry 'draft', 'generated', or 'published' articles.
- Path: article_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ArticleDetail

### POST /api/articles/{article_id}/rewrite/
`articles_rewrite_create` — AI rewrite selected text
Rewrite selected text based on user instruction (e.g., 'make more engaging', 'add statistics'). Preserves Markdown formatting from original text.
- Path: article_id* (integer)
- Body (required): RewriteRequest
  - text* (string) — Text to rewrite
  - instruction* (string) — Rewrite instruction (e.g., 'make more engaging')
- Auth: JWT/Token/Cookie
- Returns: 200 RewriteResponse

### POST /api/articles/{article_id}/select-featured-image/
`articles_select_featured_image_create` — Select featured image from generated images
Select a different image from the generated images to be the featured image
- Path: article_id* (integer)
- Body (required): SelectFeaturedImageRequest
  - image_id* (integer) — ID of the generated image to set as featured
- Auth: JWT/Token/Cookie
- Returns: 200 ImageGenerationResponse

### POST /api/articles/{article_id}/status/
`articles_status_create` — Update article status
Change article status with transition validation (generated → editing → ready → published)
- Path: article_id* (integer)
- Body (required): ArticleStatusUpdateRequest
  - status* (any) — New status * `editing` - editing * `ready` - ready * `generated` - generated * `published` - published
- Auth: JWT/Token/Cookie
- Returns: 200 ArticleDetail

### DELETE /api/articles/{id}/
`articles_destroy` — Delete article
Permanently delete article.
- Path: id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204

### GET /api/articles/{id}/
`articles_retrieve` — Get article details
Retrieve full article including content and all options
- Path: id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 ArticleDetail

### PATCH /api/articles/{id}/
`articles_partial_update` — Update article
Update article fields (content, title, meta, tags, category, etc.)
- Path: id* (integer)
- Body: PatchedArticleUpdateRequest
  - topic (string)
  - word_count (integer)
  - content (string)
  - selected_title (string)
  - outline (array<string>)
  - selected_meta_description (string)
  - category (string)
  - tags (array<string>)
  - published_url (string(uri)?)
  - url (string(uri)?)
  - slug (string?)
  - project_id (integer?)
- Auth: JWT/Token/Cookie
- Returns: 200 ArticleUpdate

### GET /api/content-calendar/
`content_calendar_list` — List accessible content calendar rows
List content calendar rows from active projects shared with the authenticated user. Page types: - Product or Service: product_or_service - Programmatic or Tool Page: programmatic_or_tool_page - Article or Blog: article_…
- Query: assigned_to (integer) — Filter by assigned user ID; fields (string) — Comma-separated response fields for list results. Example: slug,planned_publishing_date; ordering (enum(-created_at|-planned_publishing_date|created_at|planned_publishing_date)) — Order by created_at or planned_publishing_date; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 500.; page_type (enum(article_or_blog|product_or_service|programmatic_or_tool_page)) — Filter by page type. Page types: - Product or Service: product_or_service - Programmatic …; planned_from (string(date)) — Filter rows planned on or after this date; planned_to (string(date)) — Filter rows planned on or before this date; project (integer) — Filter by project ID; published (boolean) — Filter published or unpublished rows; search (string) — Search topic or slug
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<ContentCalendarPaginatedResponse>

### GET /api/projects/{project_pk}/content-calendar/
`projects_content_calendar_list` — List content calendar rows
List content calendar rows for a project. Any active project member can read rows. Page types: - Product or Service: product_or_service - Programmatic or Tool Page: programmatic_or_tool_page - Article or Blog: article_o…
- Path: project_pk* (integer) — Project ID
- Query: assigned_to (integer) — Filter by assigned user ID; fields (string) — Comma-separated response fields for list results. Example: slug,planned_publishing_date; ordering (enum(-created_at|-planned_publishing_date|created_at|planned_publishing_date)) — Order by created_at or planned_publishing_date; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 500.; page_type (enum(article_or_blog|product_or_service|programmatic_or_tool_page)) — Filter by page type. Page types: - Product or Service: product_or_service - Programmatic …; planned_from (string(date)) — Filter rows planned on or after this date; planned_to (string(date)) — Filter rows planned on or before this date; published (boolean) — Filter published or unpublished rows; search (string) — Search topic or slug
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<ContentCalendarPaginatedResponse> | 403 | 404

### POST /api/projects/{project_pk}/content-calendar/
`projects_content_calendar_create` — Create content calendar row
Create one or many project-scoped content calendar rows. Send a JSON object for one row or a JSON array for bulk create. Only project owner/admin can create rows. Assigned user is optional. When provided, the user must …
- Path: project_pk* (integer)
- Body (required): ContentCalendarWriteRequest
  - slug* (string)
  - topic* (string)
  - focused_keywords (array<any>)
  - target_traffic (integer?) — Optional target traffic estimate. When provided, must be at least 1.
  - competitor_urls (array<string>)
  - notes (string) — Optional plain text or Markdown notes.
  - planned_publishing_date* (string(date))
  - published_at (string(date-time)?)
  - assigned_to (integer?) — Optional active project member user ID.
  - page_type* (enum(product_or_service|programmatic_or_tool_page|article_or_blog))
- Auth: JWT/Token/Cookie
- Returns: 201 ContentCalendarCreateResponse | 400 | 402 | 403 | 409

### DELETE /api/projects/{project_pk}/content-calendar/bulk/
`projects_content_calendar_bulk_destroy` — Bulk delete content calendar rows
Delete many content calendar rows in this project. Only project owner/admin can delete rows. If any row is invalid, no rows are deleted.
- Path: project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 BulkDeleteRowsResponse | 400 | 403 | 409

### PATCH /api/projects/{project_pk}/content-calendar/bulk/
`projects_content_calendar_bulk_partial_update` — Bulk partially update content calendar rows
Partially update many content calendar rows in this project. Send a JSON array where each item contains id plus the fields to update. Only project owner/admin can update rows. If any row is invalid, no rows are saved. P…
- Path: project_pk* (integer)
- Body: array<object>
- Auth: JWT/Token/Cookie
- Returns: 200 ContentCalendarBulkPatchResponse | 400 | 403 | 409

### DELETE /api/projects/{project_pk}/content-calendar/{id}/
`projects_content_calendar_destroy` — Delete content calendar row
Hard delete a content calendar row. Only project owner/admin can delete rows.
- Path: id* (integer) — A unique integer value identifying this Content Calendar Row.; project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204 | 403 | 404 | 409

### GET /api/projects/{project_pk}/content-calendar/{id}/
`projects_content_calendar_retrieve` — Get content calendar row
Get one content calendar row visible to project members.
- Path: id* (integer) — Content calendar row ID; project_pk* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 200 ContentCalendar | 403 | 404

### PATCH /api/projects/{project_pk}/content-calendar/{id}/
`projects_content_calendar_partial_update` — Partially update content calendar row
Partially update a content calendar row. Only project owner/admin can update rows. Assigned user is optional. Page types: - Product or Service: product_or_service - Programmatic or Tool Page: programmatic_or_tool_page -…
- Path: id* (integer) — A unique integer value identifying this Content Calendar Row.; project_pk* (integer)
- Body: PatchedContentCalendarWriteRequest
  - slug (string)
  - topic (string)
  - focused_keywords (array<any>)
  - target_traffic (integer?) — Optional target traffic estimate. When provided, must be at least 1.
  - competitor_urls (array<string>)
  - notes (string) — Optional plain text or Markdown notes.
  - planned_publishing_date (string(date))
  - published_at (string(date-time)?)
  - assigned_to (integer?) — Optional active project member user ID.
  - page_type (enum(product_or_service|programmatic_or_tool_page|article_or_blog))
- Auth: JWT/Token/Cookie
- Returns: 200 ContentCalendar | 400 | 403 | 409

### PUT /api/projects/{project_pk}/content-calendar/{id}/
`projects_content_calendar_update` — Update content calendar row
Update a content calendar row. Only project owner/admin can update rows. Assigned user is optional. Page types: - Product or Service: product_or_service - Programmatic or Tool Page: programmatic_or_tool_page - Article o…
- Path: id* (integer) — A unique integer value identifying this Content Calendar Row.; project_pk* (integer)
- Body (required): ContentCalendarWriteRequest
  - slug* (string)
  - topic* (string)
  - focused_keywords (array<any>)
  - target_traffic (integer?) — Optional target traffic estimate. When provided, must be at least 1.
  - competitor_urls (array<string>)
  - notes (string) — Optional plain text or Markdown notes.
  - planned_publishing_date* (string(date))
  - published_at (string(date-time)?)
  - assigned_to (integer?) — Optional active project member user ID.
  - page_type* (enum(product_or_service|programmatic_or_tool_page|article_or_blog))
- Auth: JWT/Token/Cookie
- Returns: 200 ContentCalendar | 400 | 403 | 409

## Response schemas

### ArticleDetail
- id* (integer) [read-only]
- user* (integer) [read-only]
- topic* (string)
- word_count* (integer)
- word_count_actual* (integer) [read-only]
- language* (string)
- target_country* (string)
- self_url* (string(uri))
- competitor_urls* (any)
- mode* (string)
- content_type* (string) [read-only]
- perspective* (string) [read-only]
- tone* (object) [read-only]
- sales_approach* (string) [read-only]
- year_from* (integer) [read-only]
- year_to* (integer) [read-only]
- keywords* (string) [read-only]
- brand_guidelines* (string) [read-only]
- custom_instructions* (string) [read-only]
- target_locations* (object) [read-only]
- content* (string)
- selected_title* (string)
- outline* (any)
- selected_meta_description* (string)
- category* (string)
- tags* (any)
- featured_image* (string(uri)) [read-only]
- image_generated_at* (string(date-time)) [read-only]
- generated_images* (array<ArticleDetailGeneratedImage>) [read-only] — Array of all generated images (max 5)
- source* (string)
- wordpress_post_id* (integer?)
- project_id* (integer?)
- published_url* (string(uri)?)
- url* (string(uri)?)
- slug* (string?)
- status* (string)
- error_message* (string)
- message* (string) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]
- generated_at* (string(date-time)) [read-only]

### ArticleList
- id* (integer) [read-only]
- topic* (string)
- selected_title* (string)
- language* (string)
- status* (string)
- mode* (string)
- source* (string)
- wordpress_post_id* (integer?)
- project_id* (integer?)
- published_url* (string(uri)?)
- slug* (string?)
- word_count_actual* (integer) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### ArticleSimpleResponse
- id* (integer) [read-only]
- topic* (string)
- selected_title* (string)
- status* (string)
- source* (string)
- wordpress_post_id* (integer?)
- project_id* (integer?)
- published_url* (string(uri)?)
- slug* (string?)
- message* (string) [read-only]
- word_count* (integer)
- created_at* (string(date-time)) [read-only]

### ArticleUpdate
- topic (string)
- word_count (integer)
- content (string)
- selected_title (string)
- outline (array<string>)
- selected_meta_description (string)
- category (string)
- tags (array<string>)
- published_url (string(uri)?)
- url (string(uri)?)
- slug (string?)
- project_id (integer?)

### BulkDeleteRowsResponse
- deleted* (integer) — Number of rows deleted.
- ids* (array<integer>) — Row IDs deleted by this request.

### ContentCalendar
- id* (integer) [read-only]
- project* (integer) [read-only]
- project_name* (string) [read-only]
- slug* (string)
- topic* (string)
- focused_keywords* (array<any>) [read-only]
- target_traffic (integer?)
- competitor_urls* (array<string>) [read-only]
- notes (string)
- planned_publishing_date* (string(date))
- published_at (string(date-time)?)
- assigned_to (integer?)
- assigned_to_email* (string?) [read-only]
- assigned_to_name* (string) [read-only]
- page_type* (enum(product_or_service|programmatic_or_tool_page|article_or_blog))
- page_type_display* (string) [read-only]
- created_by* (integer) [read-only]
- created_by_email* (string(email)) [read-only]
- created_by_name* (string) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### ContentCalendarBulkPatchResponse
- updated* (integer)
- results* (array<ContentCalendar>)

### ContentCalendarCreateResponse
- (ContentCalendar | ContentCalendarBulkCreateResponse)

### ContentCalendarPaginatedResponse
- count* (integer)
- next* (string?)
- previous* (string?)
- stats* (ContentCalendarStats)
- results* (array<ContentCalendar>)

### ImageGenerationResponse
- featured_image_url* (string(uri)) [read-only] — Full absolute URL to currently featured image
- generated_images* (array<ArticleGeneratedImage>) [read-only] — Array of all generated images (max 5)

### RewriteResponse
- original_text* (string)
- rewritten_text* (string)

### UserArticleSettings
- default_word_count (integer)
- default_perspective (string?)
- default_tone (array<string>)
- default_sales_approach (string?)
- default_content_type (string?)
- default_target_locations (array<string>)
- default_language (string)
- default_year_from (integer?)
- default_year_to (integer?)
- default_keywords (string)
- default_brand_guidelines (string)
- default_custom_instructions (string)
