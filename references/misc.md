# SearchVector API — misc

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 70 endpoints.

### GET /api/backlink-records/
`backlink_records_list` — List accessible backlink records
List backlink record rows from active projects shared with the authenticated user.
- Query: fields (string) — Comma-separated response fields for list results. Example: url,planned_date; ordering (enum(-created_at|-planned_date|-published_date|created_at|planned_date|published_date)) — Order by created_at, planned_date, or published_date; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 500.; planned_from (string(date)) — Filter rows planned on or after this date; planned_to (string(date)) — Filter rows planned on or before this date; project (integer) — Filter by project ID; published_from (string(date)) — Filter rows published on or after this date; published_to (string(date)) — Filter rows published on or before this date; search (string) — Search URL, anchor, destination URL, or page brief
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<PublishedPage>

### GET /api/changelog/
`changelog_list` — List accessible changelog rows
List manual changelog and revision history rows from active projects shared with the authenticated user. Activity values: - Title and Meta: title_and_meta - Changed Body Content: changed_body_content - Interlinking: int…
- Query: activity (enum(changed_body_content|interlinking|other|page_speed_improvements|revamped_page_design|schema_or_other_technical_attributes|…1 more)) — Filter by activity. Activity values: - Title and Meta: title_and_meta - Changed Body Cont…; fields (string) — Comma-separated response fields for list results. Example: url,update_date; ordering (enum(-created_at|-update_date|created_at|update_date)) — Order by created_at or update_date; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 500.; project (integer) — Filter by project ID; search (string) — Search URL, activity, or description; update_from (string(date)) — Filter rows updated on or after this date; update_to (string(date)) — Filter rows updated on or before this date
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<Changelog>

### GET /api/competitor-top-pages/
`competitor_top_pages_list` — List competitor top pages
List competitor top-page library rows owned by the authenticated user. Use filters to narrow by competitor domain, URL, keyword, traffic, or keyword count.
- Query: competitors (string) — Optional comma-separated competitor domains filter.; fields (string) — Comma-separated response fields for list results. Example: url,traffic,top_keyword; keywords_count_max (integer) — Maximum keywords count value.; keywords_count_min (integer) — Minimum keywords count value.; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 10000.; top_keyword (string) — Optional top keyword contains filter.; top_keyword_regex (string) — Optional regex filter for top keyword.; traffic_max (integer) — Maximum traffic value.; traffic_min (integer) — Minimum traffic value.; url (string) — Optional URL contains filter.; url_regex (string) — Optional regex filter for URL.
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<CompetitorTopPagesPaginatedResponse> | 404

### POST /api/competitor-top-pages/
`competitor_top_pages_create` — Create competitor top page
Create one or more competitor top-page rows for the authenticated user. The competitor domain is derived from the URL.
- Body: CompetitorTopPageWrite | array<CompetitorTopPageWrite>
- Auth: JWT/Token/Cookie
- Returns: 201 CompetitorTopPage | CompetitorTopPagesBulkCreateResponse | 400 | 404

### DELETE /api/competitor-top-pages/bulk/
`competitor_top_pages_bulk_destroy` — Bulk delete competitor top pages
Delete multiple rows owned by the authenticated user.
- Auth: JWT/Token/Cookie
- Returns: 200 BulkDeleteRowsResponse | 400 | 404

### PATCH /api/competitor-top-pages/bulk/
`competitor_top_pages_bulk_partial_update` — Bulk update competitor top pages
Update multiple rows owned by the authenticated user.
- Body: array<object>
- Auth: JWT/Token/Cookie
- Returns: 200 CompetitorTopPagesBulkPatchResponse | 400 | 404

### GET /api/competitor-top-pages/competitors/
`competitor_top_pages_competitors_list` — List competitor domains
List competitor domain filter options from the authenticated user's competitor top-page library.
- Query: page (integer) — A page number within the paginated result set.; page_size (integer) — Number of results to return per page.
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<CompetitorTopPageCompetitorOptions>

### DELETE /api/competitor-top-pages/{id}/
`competitor_top_pages_destroy` — Delete competitor top page
Delete a row owned by the authenticated user.
- Path: id* (integer) — A unique integer value identifying this Competitor Top Page.
- Auth: JWT/Token/Cookie
- Returns: 204 | 404

### GET /api/competitor-top-pages/{id}/
`competitor_top_pages_retrieve` — Get competitor top page
Get one competitor top-page row owned by the authenticated user.
- Path: id* (integer) — A unique integer value identifying this Competitor Top Page.
- Auth: JWT/Token/Cookie
- Returns: 200 CompetitorTopPage | 404

### PATCH /api/competitor-top-pages/{id}/
`competitor_top_pages_partial_update` — Partially update competitor top page
Partially update a row owned by the authenticated user.
- Path: id* (integer) — A unique integer value identifying this Competitor Top Page.
- Body: PatchedCompetitorTopPageWriteRequest
  - url (string)
  - traffic (integer)
  - keywords_count (integer)
  - top_keyword (string)
  - competitors (array<string>)
  - country (string)
- Auth: JWT/Token/Cookie
- Returns: 200 CompetitorTopPage | 400 | 404

### PUT /api/competitor-top-pages/{id}/
`competitor_top_pages_update` — Update competitor top page
Update a row owned by the authenticated user.
- Path: id* (integer) — A unique integer value identifying this Competitor Top Page.
- Body (required): CompetitorTopPageWriteRequest
  - url* (string)
  - traffic (integer)
  - keywords_count (integer)
  - top_keyword (string)
  - competitors (array<string>)
  - country (string)
- Auth: JWT/Token/Cookie
- Returns: 200 CompetitorTopPage | 400 | 404

### GET /api/filter-presets/
`filter_presets_list` — List filter presets
List saved filter presets owned by the authenticated user. Use tool_id to fetch presets for one or more frontend tools. Send tool_id once, repeat it, or pass comma-separated values.
- Query: tool_id (string) — Frontend filter tool ID. Repeat this parameter or use comma-separated values to fetch mul…
- Auth: JWT/Token/Cookie
- Returns: 200 array<FilterPreset>

### POST /api/filter-presets/
`filter_presets_create` — Create filter preset
Create a saved filter preset for the authenticated user. The backend sets the user from the request; clients must not send user_id. The filters JSON, column_visibility JSON, and table_layout JSON are stored and returned…
- Body (required): FilterPresetRequest
  - tool_id* (string)
  - name* (string)
  - filters* (any)
  - column_visibility (any)
  - table_layout (any)
  - schema_version (integer)
  - is_default (boolean)
- Auth: JWT/Token/Cookie
- Returns: 201 FilterPreset | 400 | 401

### DELETE /api/filter-presets/{id}/
`filter_presets_destroy` — Delete filter preset
Delete one saved filter preset owned by the authenticated user.
- Path: id* (integer) — A unique integer value identifying this Filter Preset.
- Auth: JWT/Token/Cookie
- Returns: 204 | 401 | 404

### GET /api/filter-presets/{id}/
`filter_presets_retrieve` — Get filter preset
Get one saved filter preset owned by the authenticated user.
- Path: id* (integer) — A unique integer value identifying this Filter Preset.
- Auth: JWT/Token/Cookie
- Returns: 200 FilterPreset | 401 | 404

### PATCH /api/filter-presets/{id}/
`filter_presets_partial_update` — Update filter preset
Partially update one saved filter preset owned by the authenticated user. The filters JSON, column_visibility JSON, and table_layout JSON are stored and returned unchanged.
- Path: id* (integer) — A unique integer value identifying this Filter Preset.
- Body: PatchedFilterPresetRequest
  - tool_id (string)
  - name (string)
  - filters (any)
  - column_visibility (any)
  - table_layout (any)
  - schema_version (integer)
  - is_default (boolean)
- Auth: JWT/Token/Cookie
- Returns: 200 FilterPreset | 400 | 401 | 404

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

### GET /api/projects/{project_pk}/backlink-records/
`projects_backlink_records_list` — List backlink records
List backlink record rows for a project. Any active project member can read rows.
- Path: project_pk* (integer) — Project ID
- Query: fields (string) — Comma-separated response fields for list results. Example: url,planned_date; ordering (enum(-created_at|-planned_date|-published_date|created_at|planned_date|published_date)) — Order by created_at, planned_date, or published_date; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 500.; planned_from (string(date)) — Filter rows planned on or after this date; planned_to (string(date)) — Filter rows planned on or before this date; published_from (string(date)) — Filter rows published on or after this date; published_to (string(date)) — Filter rows published on or before this date; search (string) — Search URL, anchor, destination URL, or page brief
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<PublishedPage> | 403 | 404

### POST /api/projects/{project_pk}/backlink-records/
`projects_backlink_records_create` — Create backlink record
Create one or many project-scoped backlink record rows. Send a JSON object for one row or a JSON array for bulk create. planned_date is required. published_date is optional. Only project owner/admin can create rows.
- Path: project_pk* (integer)
- Body (required): PublishedPageWriteRequest
  - url* (string(uri))
  - anchor (string?)
  - destination_url (string(uri)?)
  - page_brief (string) — Optional plain text or Markdown page brief.
  - planned_date* (string(date)) — Required planned date for the backlink record.
  - published_date (string(date)?) — Optional actual published date for the backlink record.
- Auth: JWT/Token/Cookie
- Returns: 201 BacklinkRecordCreateResponse | 400 | 402 | 403 | 409

### DELETE /api/projects/{project_pk}/backlink-records/bulk/
`projects_backlink_records_bulk_destroy` — Bulk delete backlink records
Delete many backlink record rows in this project. Only project owner/admin can delete rows. If any row is invalid, no rows are deleted.
- Path: project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 BulkDeleteRowsResponse | 400 | 403 | 409

### PATCH /api/projects/{project_pk}/backlink-records/bulk/
`projects_backlink_records_bulk_partial_update` — Bulk partially update backlink records
Partially update many backlink records in this project. Send a JSON array where each item contains id plus the fields to update. Only project owner/admin can update rows. If any row is invalid, no rows are saved.
- Path: project_pk* (integer)
- Body: array<object>
- Auth: JWT/Token/Cookie
- Returns: 200 BacklinkRecordBulkPatchResponse | 400 | 403 | 409

### DELETE /api/projects/{project_pk}/backlink-records/{id}/
`projects_backlink_records_destroy` — Delete backlink record
Hard delete a backlink record row. Only project owner/admin can delete rows.
- Path: id* (integer) — A unique integer value identifying this Backlink Record.; project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204 | 403 | 404 | 409

### GET /api/projects/{project_pk}/backlink-records/{id}/
`projects_backlink_records_retrieve` — Get backlink record
Get one backlink record row visible to project members.
- Path: id* (integer) — Backlink record row ID; project_pk* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 200 PublishedPage | 403 | 404

### PATCH /api/projects/{project_pk}/backlink-records/{id}/
`projects_backlink_records_partial_update` — Partially update backlink record
Partially update a backlink record row. Only project owner/admin can update rows.
- Path: id* (integer) — A unique integer value identifying this Backlink Record.; project_pk* (integer)
- Body: PatchedPublishedPageWriteRequest
  - url (string(uri))
  - anchor (string?)
  - destination_url (string(uri)?)
  - page_brief (string) — Optional plain text or Markdown page brief.
  - planned_date (string(date)) — Required planned date for the backlink record.
  - published_date (string(date)?) — Optional actual published date for the backlink record.
- Auth: JWT/Token/Cookie
- Returns: 200 PublishedPage | 400 | 403 | 409

### PUT /api/projects/{project_pk}/backlink-records/{id}/
`projects_backlink_records_update` — Update backlink record
Update a backlink record row. Only project owner/admin can update rows.
- Path: id* (integer) — A unique integer value identifying this Backlink Record.; project_pk* (integer)
- Body (required): PublishedPageWriteRequest
  - url* (string(uri))
  - anchor (string?)
  - destination_url (string(uri)?)
  - page_brief (string) — Optional plain text or Markdown page brief.
  - planned_date* (string(date)) — Required planned date for the backlink record.
  - published_date (string(date)?) — Optional actual published date for the backlink record.
- Auth: JWT/Token/Cookie
- Returns: 200 PublishedPage | 400 | 403 | 409

### GET /api/projects/{project_pk}/changelog/
`projects_changelog_list` — List changelog rows
List manual changelog and revision history rows for a project. Any active project member can read rows. Activity values: - Title and Meta: title_and_meta - Changed Body Content: changed_body_content - Interlinking: inte…
- Path: project_pk* (integer) — Project ID
- Query: activity (enum(changed_body_content|interlinking|other|page_speed_improvements|revamped_page_design|schema_or_other_technical_attributes|…1 more)) — Filter by activity. Activity values: - Title and Meta: title_and_meta - Changed Body Cont…; fields (string) — Comma-separated response fields for list results. Example: url,update_date; ordering (enum(-created_at|-update_date|created_at|update_date)) — Order by created_at or update_date; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 500.; search (string) — Search URL, activity, or description; update_from (string(date)) — Filter rows updated on or after this date; update_to (string(date)) — Filter rows updated on or before this date
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
- Returns: 201 Changelog | 400 | 402 | 403 | 409

### DELETE /api/projects/{project_pk}/changelog/bulk/
`projects_changelog_bulk_destroy` — Bulk delete changelog rows
Delete many changelog rows in this project. Only project owner/admin can delete rows. If any row is invalid, no rows are deleted.
- Path: project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 BulkDeleteRowsResponse | 400 | 403 | 409

### PATCH /api/projects/{project_pk}/changelog/bulk/
`projects_changelog_bulk_partial_update` — Bulk partially update changelog rows
Partially update many changelog rows in this project. Send a JSON array where each item contains id plus the fields to update. Only project owner/admin can update rows. If any row is invalid, no rows are saved. Activity…
- Path: project_pk* (integer)
- Body: array<object>
- Auth: JWT/Token/Cookie
- Returns: 200 ChangelogBulkPatchResponse | 400 | 403 | 409

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

### GET /api/projects/{project_pk}/refresh-content-calendar/
`projects_refresh_content_calendar_list` — List refresh content calendar rows
List refresh content calendar rows for a project. Any active project member can read rows. Page types: - Product or Service: product_or_service - Programmatic or Tool Page: programmatic_or_tool_page - Article or Blog: a…
- Path: project_pk* (integer) — Project ID
- Query: activity (enum(changed_body_content|interlinking|other|page_speed_improvements|revamped_page_design|schema_or_other_technical_attributes|…1 more)) — Filter by one or more comma-separated activity values. Activity values: - Title and Meta:…; assigned_to (integer) — Filter by assigned user ID; fields (string) — Comma-separated response fields for list results. Example: url,planned_publishing_date; ordering (enum(-created_at|-planned_publishing_date|created_at|planned_publishing_date)) — Order by created_at or planned_publishing_date; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 500.; page_type (enum(article_or_blog|product_or_service|programmatic_or_tool_page)) — Filter by page type. Page types: - Product or Service: product_or_service - Programmatic …; planned_from (string(date)) — Filter rows planned on or after this date; planned_to (string(date)) — Filter rows planned on or before this date; published (boolean) — Filter published or unpublished rows; search (string) — Search topic or URL
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<RefreshContentCalendarPaginatedResponse> | 403 | 404

### POST /api/projects/{project_pk}/refresh-content-calendar/
`projects_refresh_content_calendar_create` — Create refresh content calendar row
Create one or many project-scoped refresh content calendar rows. Send a JSON object for one row or a JSON array for bulk create. Only project owner/admin can create rows. Assigned user is optional. When provided, the us…
- Path: project_pk* (integer)
- Body: RefreshContentCalendarWrite | array<RefreshContentCalendarWrite>
- Auth: JWT/Token/Cookie
- Returns: 201 RefreshContentCalendarCreateResponse | 400 | 402 | 403 | 409

### DELETE /api/projects/{project_pk}/refresh-content-calendar/bulk/
`projects_refresh_content_calendar_bulk_destroy` — Bulk delete refresh content calendar rows
Delete many refresh content calendar rows in this project. Only project owner/admin can delete rows. If any row is invalid, no rows are deleted.
- Path: project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 BulkDeleteRowsResponse | 400 | 403 | 409

### PATCH /api/projects/{project_pk}/refresh-content-calendar/bulk/
`projects_refresh_content_calendar_bulk_partial_update` — Bulk partially update refresh content calendar rows
Partially update many refresh content calendar rows in this project. Send a JSON array where each item contains id plus the fields to update. Only project owner/admin can update rows. If any row is invalid, no rows are …
- Path: project_pk* (integer)
- Body: array<object>
- Auth: JWT/Token/Cookie
- Returns: 200 RefreshContentCalendarBulkPatchResponse | 400 | 403 | 409

### DELETE /api/projects/{project_pk}/refresh-content-calendar/{id}/
`projects_refresh_content_calendar_destroy` — Delete refresh content calendar row
Hard delete a refresh content calendar row. Only project owner/admin can delete rows.
- Path: id* (integer) — A unique integer value identifying this Refresh Content Calendar Row.; project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204 | 403 | 404 | 409

### GET /api/projects/{project_pk}/refresh-content-calendar/{id}/
`projects_refresh_content_calendar_retrieve` — Get refresh content calendar row
Get one refresh content calendar row visible to project members.
- Path: id* (integer) — Refresh content calendar row ID; project_pk* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 200 RefreshContentCalendar | 403 | 404

### PATCH /api/projects/{project_pk}/refresh-content-calendar/{id}/
`projects_refresh_content_calendar_partial_update` — Partially update refresh content calendar row
Partially update a refresh content calendar row. Only project owner/admin can update rows. Assigned user is optional. Page types: - Product or Service: product_or_service - Programmatic or Tool Page: programmatic_or_too…
- Path: id* (integer) — A unique integer value identifying this Refresh Content Calendar Row.; project_pk* (integer)
- Body: PatchedRefreshContentCalendarWriteRequest
  - url (string)
  - topic (string)
  - focused_keywords (array<any>)
  - target_traffic (integer?) — Optional target traffic estimate. When provided, must be at least 1.
  - competitor_urls (array<string>)
  - notes (string) — Optional plain text or Markdown notes.
  - planned_publishing_date (string(date))
  - published_at (string(date-time)?)
  - assigned_to (integer?) — Optional active project member user ID.
  - page_type (enum(product_or_service|programmatic_or_tool_page|article_or_blog))
  - activity (array<enum(title_and_meta|changed_body_content|interlinking|schema_or_other_technical_attributes|revamped_page_design|other|…1 more)>) — Optional refresh activity values. Defaults to other.
- Auth: JWT/Token/Cookie
- Returns: 200 RefreshContentCalendar | 400 | 403 | 409

### PUT /api/projects/{project_pk}/refresh-content-calendar/{id}/
`projects_refresh_content_calendar_update` — Update refresh content calendar row
Update a refresh content calendar row. Only project owner/admin can update rows. Assigned user is optional. Page types: - Product or Service: product_or_service - Programmatic or Tool Page: programmatic_or_tool_page - A…
- Path: id* (integer) — A unique integer value identifying this Refresh Content Calendar Row.; project_pk* (integer)
- Body (required): RefreshContentCalendarWriteRequest
  - url* (string)
  - topic* (string)
  - focused_keywords (array<any>)
  - target_traffic (integer?) — Optional target traffic estimate. When provided, must be at least 1.
  - competitor_urls (array<string>)
  - notes (string) — Optional plain text or Markdown notes.
  - planned_publishing_date* (string(date))
  - published_at (string(date-time)?)
  - assigned_to (integer?) — Optional active project member user ID.
  - page_type* (enum(product_or_service|programmatic_or_tool_page|article_or_blog))
  - activity (array<enum(title_and_meta|changed_body_content|interlinking|schema_or_other_technical_attributes|revamped_page_design|other|…1 more)>) — Optional refresh activity values. Defaults to other.
- Auth: JWT/Token/Cookie
- Returns: 200 RefreshContentCalendar | 400 | 403 | 409

### GET /api/projects/{project_pk}/title-meta-planner/
`projects_title_meta_planner_list` — List title meta planner rows
List manual title and meta planner rows for a project.
- Path: project_pk* (integer) — Project ID
- Query: fields (string) — Comma-separated response fields for list results. Example: id,project,project_name,page_u…; ordering (enum(-created_at|-planned_date|created_at|planned_date)) — Order by created_at or planned_date; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 500.; planned_from (string(date)) — Filter rows planned on or after this date; planned_to (string(date)) — Filter rows planned on or before this date; search (string) — Search page URL, current title, or current meta description
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<TitleMetaPlannerPaginatedResponse> | 403 | 404

### POST /api/projects/{project_pk}/title-meta-planner/
`projects_title_meta_planner_create` — Create title meta planner rows
Create one or many project-scoped title and meta planner rows. Send a JSON object for one row or a JSON array for bulk create. Only project owner/admin can create rows. When suggestion fields are omitted or sent as empt…
- Path: project_pk* (integer)
- Body (required): TitleMetaPlannerWriteRequest
  - page_url* (string)
  - current_title (string)
  - title_suggestions (array<string>)
  - current_meta_description (string)
  - meta_description_suggestions (array<string>)
  - planned_date (string(date)?)
- Auth: JWT/Token/Cookie
- Returns: 201 TitleMetaPlannerCreateResponse | 400 | 402 | 403 | 409

### POST /api/projects/{project_pk}/title-meta-planner/suggestions/
`projects_title_meta_planner_suggestions_create` — Fetch title meta suggestions
Fetch up to 5 title and meta description suggestions for one or many page URLs. For normal pages, the keyword is extracted from the URL slug and used to fetch suggestions. For project homepage URLs, the API uses project…
- Path: project_pk* (integer) — Project ID
- Body (required): TitleMetaPlannerSuggestionRequestRequest
  - page_url* (string)
- Auth: JWT/Token/Cookie
- Returns: 200 TitleMetaPlannerSuggestionSingleOrBulkResponse | 400 | 402 | 403 | 404 | 500

### DELETE /api/projects/{project_pk}/title-meta-planner/{id}/
`projects_title_meta_planner_destroy` — Delete title meta planner row
Delete one title and meta planner row. Only project owner/admin can delete rows.
- Path: id* (integer) — A unique integer value identifying this Title Meta Planner Row.; project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204 | 403 | 409

### GET /api/projects/{project_pk}/title-meta-planner/{id}/
`projects_title_meta_planner_retrieve` — Get title meta planner row
Return one title and meta planner row for a project.
- Path: id* (integer) — A unique integer value identifying this Title Meta Planner Row.; project_pk* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 200 TitleMetaPlanner | 403 | 404

### PATCH /api/projects/{project_pk}/title-meta-planner/{id}/
`projects_title_meta_planner_partial_update` — Partially update title meta planner row
Partially update one title and meta planner row. Only project owner/admin can update rows.
- Path: id* (integer) — A unique integer value identifying this Title Meta Planner Row.; project_pk* (integer)
- Body: PatchedTitleMetaPlannerWriteRequest
  - page_url (string)
  - current_title (string)
  - title_suggestions (array<string>)
  - current_meta_description (string)
  - meta_description_suggestions (array<string>)
  - planned_date (string(date)?)
- Auth: JWT/Token/Cookie
- Returns: 200 TitleMetaPlanner | 400 | 403 | 409

### PUT /api/projects/{project_pk}/title-meta-planner/{id}/
`projects_title_meta_planner_update` — Update title meta planner row
Replace one title and meta planner row. Only project owner/admin can update rows.
- Path: id* (integer) — A unique integer value identifying this Title Meta Planner Row.; project_pk* (integer)
- Body (required): TitleMetaPlannerWriteRequest
  - page_url* (string)
  - current_title (string)
  - title_suggestions (array<string>)
  - current_meta_description (string)
  - meta_description_suggestions (array<string>)
  - planned_date (string(date)?)
- Auth: JWT/Token/Cookie
- Returns: 200 TitleMetaPlanner | 400 | 403 | 409

### GET /api/refresh-content-calendar/
`refresh_content_calendar_list` — List accessible refresh content calendar rows
List refresh content calendar rows from active projects shared with the authenticated user. Page types: - Product or Service: product_or_service - Programmatic or Tool Page: programmatic_or_tool_page - Article or Blog: …
- Query: activity (enum(changed_body_content|interlinking|other|page_speed_improvements|revamped_page_design|schema_or_other_technical_attributes|…1 more)) — Filter by one or more comma-separated activity values. Activity values: - Title and Meta:…; assigned_to (integer) — Filter by assigned user ID; fields (string) — Comma-separated response fields for list results. Example: url,planned_publishing_date; ordering (enum(-created_at|-planned_publishing_date|created_at|planned_publishing_date)) — Order by created_at or planned_publishing_date; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 500.; page_type (enum(article_or_blog|product_or_service|programmatic_or_tool_page)) — Filter by page type. Page types: - Product or Service: product_or_service - Programmatic …; planned_from (string(date)) — Filter rows planned on or after this date; planned_to (string(date)) — Filter rows planned on or before this date; project (integer) — Filter by project ID; published (boolean) — Filter published or unpublished rows; search (string) — Search topic or URL
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<RefreshContentCalendarPaginatedResponse>

### GET /api/title-meta-planner/
`title_meta_planner_list` — List accessible title meta planner rows
List title meta planner rows from active projects shared with the authenticated user.
- Query: fields (string) — Comma-separated response fields for list results. Example: id,project,project_name,page_u…; ordering (enum(-created_at|-planned_date|created_at|planned_date)) — Order by created_at or planned_date; page (integer) — A page number within the paginated result set.; page_size (integer) — Number of rows per page. Maximum 500.; planned_from (string(date)) — Filter rows planned on or after this date; planned_to (string(date)) — Filter rows planned on or before this date; project (integer) — Filter by project ID; search (string) — Search page URL, current title, or current meta description
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<TitleMetaPlannerPaginatedResponse>

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
Start a site audit job. This endpoint charges 1 credit per 100 URLs, with a maximum of 10 credits for 1000 URLs, only when the job is successfully started. If a completed report already exists for the same site URL and …
- Body (required): SiteAuditStartRequestRequest
  - url* (string)
  - max_urls (integer)
  - project_id (integer)
  - issue_exclusion_patterns (array<string>)
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditStartResponse | 400 | 401 | 402 | 403 | 500 | 503

### GET /api/tools/site-audit/jobs/history/
`tools_site_audit_jobs_history_retrieve` — List site audit history
List previous Site Audit jobs for the authenticated user. Use job_id from this response with the existing results endpoint to open any previous report.
- Query: limit (integer) — Number of jobs to return. Default 20, max 100.; offset (integer) — Offset for history pagination.; project_id (integer) — Optional project ID. When supplied, returns only jobs attached to that project.
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditHistoryResponse | 400 | 401 | 404 | 500

### POST /api/tools/site-audit/jobs/{job_id}/cancel/
`tools_site_audit_jobs_cancel_create` — Cancel site audit
Cancel a running site audit job started by the authenticated user.
- Path: job_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditCancelResponse | 401 | 403 | 404 | 500 | 503

### GET /api/tools/site-audit/jobs/{job_id}/compare-latest/
`tools_site_audit_jobs_compare_latest_retrieve` — Compare latest site audit
Compare a Site Audit job with the latest previous completed Site Audit job for the same URL owned by the authenticated user using saved CSV ZIP reports. Use this endpoint when the UI only needs current audit versus last…
- Path: job_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditCompareResponse | 401 | 404 | 500 | 503

### GET /api/tools/site-audit/jobs/{job_id}/compare/
`tools_site_audit_jobs_compare_retrieve` — Compare site audits
Compare a current Site Audit job with a previous Site Audit job owned by the authenticated user using saved CSV ZIP reports. Returns link count difference and summary issues that are present in the current audit but abs…
- Path: job_id* (integer)
- Query: previous_job_id* (integer) — Previous Site Audit job_id to compare against.
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditCompareResponse | 400 | 401 | 404 | 500 | 503

### GET /api/tools/site-audit/jobs/{job_id}/compare/new-issues/
`tools_site_audit_jobs_compare_new_issues_retrieve` — Compare new site audit issues
Return paginated issue rows from the current Site Audit job that were not present in the previous audit for the same issue key and URL. When previous_job_id is omitted, the latest previous completed audit for the same s…
- Path: job_id* (integer)
- Query: limit (integer) — Number of new issue rows to return. Default 100, max 1000.; offset (integer) — Offset for new issue pagination.; previous_job_id (integer) — Optional previous Site Audit job_id to compare against. Omit to use the latest previous c…
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditNewIssuesResponse | 400 | 401 | 404 | 500 | 503

### GET /api/tools/site-audit/jobs/{job_id}/compare/new-rows/
`tools_site_audit_jobs_compare_new_rows_retrieve` — Compare new site audit rows
Return paginated rows that are present in the current Site Audit job but not in the previous audit for the selected result type. Supported types are issues, pages, links, and resources.
- Path: job_id* (integer)
- Query: limit (integer) — Number of new rows to return. Default 100, max 1000.; offset (integer) — Offset for new row pagination.; previous_job_id (integer) — Optional previous Site Audit job_id to compare against. Omit to use the latest previous c…; type* (enum(issues|links|pages|resources)) — Result type to compare.
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditNewRowsResponse | 400 | 401 | 404 | 500

### GET /api/tools/site-audit/jobs/{job_id}/issue-urls/
`tools_site_audit_jobs_issue_urls_retrieve` — Get issue URLs
Fetch affected page rows for one Site Audit summary issue. Use the existing summary row fields as filters: issue is required, category and type are optional. Read the affected page URL from items[].url.
- Path: job_id* (integer)
- Query: category (string) — Optional category from the summary row.; issue* (string) — Issue label from the summary row.; limit (integer) — Number of affected URLs to return. Default 100, max 5000.; offset (integer) — Offset for affected URL pagination.; type (string) — Optional issue severity/type from the summary row.
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditIssueUrlsResponse | 400 | 401 | 404 | 500 | 503

### GET /api/tools/site-audit/jobs/{job_id}/results/
`tools_site_audit_jobs_results_retrieve` — Get site audit results
Fetch site audit results for a job started by the authenticated user or attached to a project the user can access. Use type to select summary, pages, issues, links, resources, or sf-report. Use the issue URLs endpoint t…
- Path: job_id* (integer)
- Query: limit (integer) — Page size for paginated result types. Max 5000. Use CSV ZIP for the full report.; offset (integer) — Offset for paginated result types.; type (enum(issues|links|pages|resources|sf-report|summary)) — Result type to fetch.
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditResultsResponse | 400 | 401 | 403 | 404 | 500 | 503

### GET /api/tools/site-audit/jobs/{job_id}/status/
`tools_site_audit_jobs_status_retrieve` — Get site audit status
Get job status for a site audit started by the authenticated user or attached to a project the user can access.
- Path: job_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 SiteAuditStatusResponse | 401 | 403 | 404 | 500 | 503

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

### BacklinkRecordBulkPatchResponse
- updated* (integer)
- results* (array<PublishedPage>)

### BacklinkRecordCreateResponse
- (PublishedPage | PublishedPageBulkCreateResponse)

### BulkDeleteRowsResponse
- deleted* (integer) — Number of rows deleted.
- ids* (array<integer>) — Row IDs deleted by this request.

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

### ChangelogBulkPatchResponse
- updated* (integer)
- results* (array<Changelog>)

### CompetitorTopPage
- id* (integer) [read-only]
- project* (integer?) [read-only]
- project_name* (string) [read-only]
- url* (string(uri))
- competitor_domain* (string) [read-only]
- traffic (integer(int64))
- keywords_count (integer)
- top_keyword (string)
- competitors (any)
- country (string)
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### CompetitorTopPageCompetitorOptions
- domain* (string)
- count* (integer)

### CompetitorTopPagesBulkPatchResponse
- updated* (integer)
- results* (array<CompetitorTopPage>)

### CompetitorTopPagesPaginatedResponse
- count* (integer)
- total_count* (integer)
- page* (integer)
- page_size* (integer)
- total_pages* (integer)
- next* (string?)
- previous* (string?)
- results* (array<CompetitorTopPage>)

### FilterPreset
- id* (integer) [read-only]
- tool_id* (string)
- name* (string)
- filters* (any)
- column_visibility (any)
- table_layout (any)
- schema_version (integer)
- is_default (boolean)
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

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

### PublishedPage
- id* (integer) [read-only]
- project* (integer) [read-only]
- project_name* (string) [read-only]
- url* (string(uri))
- anchor (string?)
- destination_url (string(uri)?)
- page_brief (string)
- planned_date* (string(date)) — Required planned date for the backlink record.
- published_date (string(date)?) — Optional actual published date for the backlink record.
- created_by* (integer) [read-only]
- created_by_email* (string(email)) [read-only]
- created_by_name* (string) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### RefreshContentCalendar
- id* (integer) [read-only]
- project* (integer) [read-only]
- project_name* (string) [read-only]
- url* (string(uri))
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
- activity* (array<enum(title_and_meta|changed_body_content|interlinking|schema_or_other_technical_attributes|revamped_page_design|other|…1 more)>) [read-only]
- activity_display* (array<string>) [read-only]
- created_by* (integer) [read-only]
- created_by_email* (string(email)) [read-only]
- created_by_name* (string) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### RefreshContentCalendarBulkPatchResponse
- updated* (integer)
- results* (array<RefreshContentCalendar>)

### RefreshContentCalendarCreateResponse
- (RefreshContentCalendar | RefreshContentCalendarBulkCreateResponse)

### RefreshContentCalendarPaginatedResponse
- count* (integer)
- next* (string?)
- previous* (string?)
- stats* (RefreshContentCalendarStats)
- results* (array<RefreshContentCalendar>)

### SiteAuditCancelResponse
- success* (boolean)
- message (string)
- job (any)

### SiteAuditCompareResponse
- success* (boolean)
- current_job_id* (integer)
- previous_job_id* (integer)
- links* (SiteAuditCompareLinks)
- new_issues* (array<SiteAuditCompareIssue>)

### SiteAuditHistoryResponse
- success* (boolean)
- total* (integer)
- limit* (integer)
- offset* (integer)
- jobs* (array<SiteAuditHistoryJob>)

### SiteAuditIssueUrlsResponse
- success* (boolean)
- job_id* (integer)
- issue* (string)
- category (string)
- type (string)
- affected_url_count* (integer)
- limit* (integer)
- offset* (integer)
- items (array<SiteAuditIssueUrlItem>)

### SiteAuditNewIssuesResponse
- success* (boolean)
- current_job_id* (integer)
- previous_job_id* (integer)
- total* (integer)
- limit* (integer)
- offset* (integer)
- new_issues* (array<SiteAuditNewIssueRow>)

### SiteAuditNewRowsResponse
- success* (boolean)
- current_job_id* (integer)
- previous_job_id* (integer)
- type* (string)
- total* (integer)
- limit* (integer)
- offset* (integer)
- new_rows* (any)

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
- reused (boolean)
- fresh_crawl_available_at (string(date-time))
- fresh_crawl_remaining_seconds (integer)

### SiteAuditStatusResponse
- success* (boolean)
- job* (any)
- csv_export_status (string)
- csv_zip_url (string)
- csv_export_error (string)

### TitleMetaPlanner
- id* (integer) [read-only]
- project* (integer) [read-only]
- project_name* (string) [read-only]
- page_url* (string(uri))
- current_title (string)
- title_suggestions* (array<string>) [read-only]
- current_meta_description (string)
- meta_description_suggestions* (array<string>) [read-only]
- planned_date (string(date)?)
- created_by* (integer) [read-only]
- created_by_email* (string(email)) [read-only]
- created_by_name* (string) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### TitleMetaPlannerCreateResponse
- (TitleMetaPlanner | TitleMetaPlannerBulkCreateResponse)

### TitleMetaPlannerPaginatedResponse
- count* (integer)
- next* (string?)
- previous* (string?)
- stats* (TitleMetaPlannerStats)
- results* (array<TitleMetaPlanner>)

### TitleMetaPlannerSuggestionSingleOrBulkResponse
- (TitleMetaPlannerSuggestionResponse | TitleMetaPlannerBulkSuggestionResponse)
