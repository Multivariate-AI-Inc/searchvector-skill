# SearchVector API — cms

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 33 endpoints.

### POST /api/projects/{project_id}/wordpress/fetch-post-ids/
`projects_wordpress_fetch_post_ids_create` — Fetch WordPress post IDs
Fetch WordPress post/page IDs for multiple URLs by matching slugs. Uses project's linked WordPress site.
- Path: project_id* (integer)
- Body (required): FetchWordPressPostIdsRequestRequest
  - urls* (array<string>) — List of URLs or post IDs to fetch WordPress post IDs for (max 20)
- Auth: JWT/Token/Cookie
- Returns: 200 FetchWordPressPostIdsResponse

### GET /api/projects/{project_id}/wordpress/fetch-urls/
`projects_wordpress_fetch_urls_retrieve` — Fetch all WordPress URLs
Fetch all URLs from connected WordPress site including all post types (posts, pages, products, events, etc.). Supports pagination and status filtering.
- Path: project_id* (integer)
- Query: page (integer) — Page number (default: 1); per_page (integer) — Number of items per page (default: 50, max: 10000); status (string) — Filter by post status: publish/draft/pending/all (default: publish)
- Auth: JWT/Token/Cookie
- Returns: 200 FetchWordPressUrlsResponse

### GET /api/webflow/auth-url/
`webflow_auth_url_retrieve` — OAuth authorization URL
- Query: return_url (string) — Frontend path to return to after OAuth
- Auth: JWT/Token/Cookie
- Returns: 200

### GET /api/webflow/callback/
`webflow_callback_retrieve` — OAuth callback
- Auth: JWT/Token/Cookie/none
- Returns: 200 | 400

### POST /api/webflow/callback/
`webflow_callback_create` — OAuth callback
- Body (required): WebflowOAuthCallbackRequest
  - code* (string)
  - state* (string)
- Auth: JWT/Token/Cookie/none
- Returns: 200 | 400

### GET /api/webflow/collections/{collection_id}/
`webflow_collections_retrieve` — Get collection schema
- Path: collection_id* (string)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/webflow/collections/{collection_id}/items/
`webflow_collections_items_retrieve` — List collection items
- Path: collection_id* (string)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/webflow/collections/{collection_id}/items/
`webflow_collections_items_create` — List collection items
- Path: collection_id* (string)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### POST /api/webflow/collections/{collection_id}/items/publish/
`webflow_collections_items_publish_create` — Publish items
- Path: collection_id* (string)
- Body (required): WebflowItemsPublishRequest
  - itemIds* (array<string>)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### DELETE /api/webflow/collections/{collection_id}/items/{item_id}/
`webflow_collections_items_destroy` — Update or delete item
- Path: collection_id* (string); item_id* (string)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### PATCH /api/webflow/collections/{collection_id}/items/{item_id}/
`webflow_collections_items_partial_update` — Update or delete item
- Path: collection_id* (string); item_id* (string)
- Body: PatchedWebflowItemUpdateRequest
  - fieldData (object)
  - isDraft (boolean)
  - isArchived (boolean)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### DELETE /api/webflow/disconnect/
`webflow_disconnect_destroy` — Disconnect Webflow
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/webflow/pages/{page_id}/
`webflow_pages_retrieve` — Get page detail
Get one Webflow page by page ID, optionally scoped to a locale.
- Path: page_id* (string)
- Query: localeId (string) — Optional Webflow locale ID.
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 401 | 403 | 404 | 500

### PUT /api/webflow/pages/{page_id}/
`webflow_pages_update` — Update page metadata
Update Webflow page title, slug, SEO metadata, and Open Graph metadata.
- Path: page_id* (string)
- Query: localeId (string) — Optional Webflow locale ID.
- Body: WebflowPageUpdateRequest
  - title (string)
  - slug (string)
  - seo (WebflowSeoRequest)
  - openGraph (WebflowOpenGraphRequest)
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 401 | 403 | 404 | 422 | 500

### GET /api/webflow/pages/{page_id}/dom/
`webflow_pages_dom_retrieve` — Get page content
Fetch Webflow page DOM/content nodes. This endpoint retrieves nodes in batches up to the requested limit and aggregates results up to 1000 nodes so frontend can fetch all page components.
- Path: page_id* (string) — Webflow page ID.
- Query: limit (integer) — Maximum nodes per Webflow request batch. Default 100, max 100.; localeId (string) — Optional Webflow locale ID.; offset (integer) — Starting pagination offset. Default 0.
- Auth: JWT/Token/Cookie
- Returns: 200 WebflowPageContentResponse | 400 | 401 | 403 | 404 | 500

### POST /api/webflow/pages/{page_id}/dom/
`webflow_pages_dom_create` — Update page content
Update Webflow page DOM/content nodes. localeId is optional and Webflow supports updating up to 1000 nodes in a single request.
- Path: page_id* (string) — Webflow page ID.
- Query: localeId (string) — Optional Webflow locale ID.
- Body (required): WebflowPageContentUpdateRequest
  - nodes* (array<WebflowPageContentUpdateNodeRequest>)
- Auth: JWT/Token/Cookie
- Returns: 200 WebflowPageContentUpdateResponse | 400 | 401 | 403 | 404 | 422 | 500

### DELETE /api/webflow/projects/{project_id}/connected-sites/
`webflow_projects_connected_sites_destroy` — Disconnect Webflow site from project
Disconnect the selected Webflow site from a project. Only the project owner can use this.
- Path: project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 | 403 | 404

### GET /api/webflow/projects/{project_id}/connected-sites/
`webflow_projects_connected_sites_list` — List project connected Webflow site
Return the explicitly selected Webflow site for this project. A project can have at most one connected Webflow site, so this returns either an empty list or a single-item list.
- Path: project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 array<WebflowProjectSite> | 403 | 404

### POST /api/webflow/projects/{project_id}/connected-sites/
`webflow_projects_connected_sites_create` — Connect Webflow site to project
Save one selected Webflow site against a project. Only the project owner can set the Webflow site connection.
- Path: project_id* (integer)
- Body (required): WebflowProjectConnectRequest
  - site_id* (string)
- Auth: JWT/Token/Cookie
- Returns: 200 WebflowProjectSite | 201 WebflowProjectSite | 400 | 401 | 403 | 404 | 409 | 500

### GET /api/webflow/sites/
`webflow_sites_retrieve` — List Webflow sites
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/webflow/sites/{site_id}/collections/
`webflow_sites_collections_retrieve` — List collections
- Path: site_id* (string)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/webflow/sites/{site_id}/pages/
`webflow_sites_pages_retrieve` — List site pages
List all Webflow pages for a site, optionally scoped to a locale. This endpoint fetches pages in batches of 100 and aggregates results up to 1,000 pages.
- Path: site_id* (string)
- Query: localeId (string) — Optional Webflow locale ID.
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 401 | 403 | 404 | 500

### POST /api/webflow/sites/{site_id}/publish/
`webflow_sites_publish_create` — Publish site
- Path: site_id* (string)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/webflow/status/
`webflow_status_retrieve` — Connection status
- Auth: JWT/Token/Cookie
- Returns: 200

### GET /api/wordpress/
`wordpress_list` — List WordPress Sites
Get all WordPress sites connected to user's projects.
- Auth: JWT/Token/Cookie
- Returns: 200 array<WordPressSite>

### GET /api/wordpress/categories/{project_id}/
`wordpress_categories_retrieve` — Get WordPress Categories
Fetch all categories from connected WordPress site for filtering posts.
- Path: project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 any | 403 any | 404 any

### POST /api/wordpress/connect/
`wordpress_connect_create` — Connect WordPress Site
Verify and connect a WordPress site to a project using application password. Only the project owner can use this flow.
- Body (required): WordPressConnectRequest
  - project_id* (integer) — Project ID to connect WordPress site to
  - site_url* (string(uri)) — WordPress site URL (e.g., https://example.com)
  - username* (string) — WordPress username
  - password* (string) — WordPress application password
- Auth: JWT/Token/Cookie
- Returns: 200 WordPressSite | 201 WordPressSite | 400 any | 403 any | 404 any

### POST /api/wordpress/manual-title-update/
`wordpress_manual_title_update_create` — Manual WordPress title update
Update WordPress post/page title manually using post ID. Set update_date=true to automatically update the post date to today's date.
- Body (required): ManualWordPressTitleUpdateRequest
  - project_id* (integer) — Project ID
  - wordpress_post_id* (integer) — WordPress post/page ID
  - new_title* (string) — New title to update
  - update_date (boolean) — Set to true to update post date to today's date
- Auth: JWT/Token/Cookie
- Returns: 200 ManualWordPressTitleUpdateResponse

### POST /api/wordpress/posts/create/
`wordpress_posts_create_create` — Create WordPress Post
Create a new WordPress post or page with full control over content, metadata, and publishing options.
- Body (required): WordPressCreatePostRequest
  - project_id* (integer) — Project ID with connected WordPress site
  - title (string) — Post title (optional - can be empty)
  - content (string) — Post content - HTML supported
  - excerpt (string) — Post excerpt/meta description for SEO
  - status (any) — Post status * `publish` - publish * `draft` - draft * `pending` - pending * `private` - private * `future` - future
  - date (string(date-time)?) — Publication date in site timezone (ISO 8601 format)
  - date_gmt (string(date-time)?) — Publication date in GMT/UTC (ISO 8601 format)
  - slug (string) — URL slug (auto-generated from title if not provided)
  - password (string) — Password to protect post content (leave empty for public)
  - author (integer?) — WordPress author user ID (defaults to authenticated user)
  - categories (array<integer>) — List of category term IDs
  - tags (array<integer>) — List of tag term IDs
  - featured_media (integer?) — Featured image media attachment ID
  - comment_status (any) — Comment status * `open` - open * `closed` - closed
  - ping_status (any) — Pingback/trackback status * `open` - open * `closed` - closed
  - format (any) — Post format - theme must support it * `standard` - standard * `aside` - aside * `chat` - chat * `gallery` - gallery * `…
  - sticky (boolean) — Sticky post designation (pin to front page)
  - template (string) — Theme template file to use (e.g., 'template-full-width.php')
  - meta (any?) — Custom meta fields as JSON object
  - article_id (integer?) — Article ID to link with this WordPress post after creation
- Auth: JWT/Token/Cookie
- Returns: 201 any | 400 any | 403 any | 404 any

### PUT /api/wordpress/posts/update/
`wordpress_posts_update_update` — Update WordPress Post (by body)
Update an existing WordPress post. WordPress post ID is provided in the request body.
- Body (required): WordPressUpdatePostByBodyRequest
  - project_id* (integer)
  - wordpress_post_id* (integer) — WordPress post ID to update
  - post_type (string) — REST base of post type (default: posts)
  - title (string)
  - content (string)
  - excerpt (string)
  - status (enum(publish|draft|pending|private|future))
  - date (string(date-time)?)
  - date_gmt (string(date-time)?)
  - slug (string)
  - password (string)
  - author (integer?)
  - categories (array<integer>)
  - tags (array<integer>)
  - featured_media (integer?)
  - comment_status (enum(open|closed))
  - ping_status (enum(open|closed))
  - format (enum(standard|aside|chat|gallery|link|image|…4 more))
  - sticky (boolean)
  - template (string)
  - meta (any?)
- Auth: JWT/Token/Cookie
- Returns: 200

### GET /api/wordpress/posts/{project_id}/
`wordpress_posts_retrieve` — List WordPress Posts/Pages
Get posts and pages from connected WordPress site with filtering, search, sorting, and pagination.
- Path: project_id* (integer)
- Query: category (integer) — Category ID (only works with post types that support categories); order (enum(desc|asc)) — Sort direction: 'asc', 'desc' * `desc` - Descending * `asc` - Ascending; orderby (enum(date|title|modified)) — Sort field: 'date', 'title', 'modified' * `date` - Date * `title` - Title * `modified` - …; page (integer) — Page number for pagination; per_page (enum(10|25|50|100)) — Number of items per page (10, 25, 50, 100) * `10` - 10 * `25` - 25 * `50` - 50 * `100` - …; post_type (string) — REST base of post type (e.g., 'posts', 'pages', 'blog'); search (string) — Search term to filter posts by title and content; search_url (string) — Search term to filter posts by URL (e.g., 'online' matches posts with 'online' in their U…; status (enum(publish|draft|future|any)) — Post status filter: 'publish' (default), 'draft', 'future', 'any' * `publish` - Published…
- Auth: JWT/Token/Cookie
- Returns: 200 any | 400 any | 403 any | 404 any

### GET /api/wordpress/posts/{project_id}/{post_id}/
`wordpress_post_retrieve` — Get Single WordPress Post
Fetch full HTML content of a single WordPress post. No credits charged.
- Path: post_id* (integer); project_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200

### DELETE /api/wordpress/{site_id}/
`wordpress_destroy` — Disconnect WordPress Site
Remove a connected WordPress site from a project. Only the project owner can use this flow.
- Path: site_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204 any | 403 any | 404 any

## Response schemas

### FetchWordPressPostIdsResponse
- results* (array<WordPressPostIdResult>)
- total* (integer)
- found* (integer)
- not_found* (integer)

### FetchWordPressUrlsResponse
- success* (boolean)
- total* (integer)
- page* (integer)
- per_page* (integer)
- total_pages* (integer)
- urls* (array<WordPressUrlItem>)
- error (string)

### ManualWordPressTitleUpdateResponse
- success* (boolean)
- post_id (integer)
- old_title (string)
- new_title (string)
- post_type (string)
- error (string)

### WebflowPageContentResponse
- pageId* (string)
- branchId (string?)
- nodes (array<object>)
- pagination (object)
- lastUpdated (string?)

### WebflowPageContentUpdateResponse
- errors (array<string>)

### WebflowProjectSite
- connectionId (integer)
- projectId (integer)
- id* (string?)
- displayName* (string)
- shortName* (string)
- lastUpdated* (string)
- previewUrl* (string?)
- customDomains (array<string>)
- isActive (boolean)

### WordPressSite
- id* (integer) [read-only]
- project_id* (integer) [read-only]
- project_name* (string) [read-only]
- site_url* (string(uri)) [read-only]
- site_name* (string) [read-only]
- wp_version* (string) [read-only]
- is_valid* (boolean) [read-only]
- connected_at* (string(date-time)) [read-only]
