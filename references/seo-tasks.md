# SearchVector API — seo-tasks

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 20 endpoints.

### GET /api/projects/{project_pk}/seo-tasks/
`projects_seo_tasks_list` — List SEO tasks
List non-archived SEO tasks visible to project members. Repeating tasks completed in a previous calendar period are lazily reset to todo on read, with subtasks unchecked. Visibility is inherited from project sharing.
- Path: project_pk* (integer) — Project ID
- Query: assigned_to (integer) — Filter by assigned user ID; due (enum(none|overdue|today|upcoming)) — Filter by deadline bucket; include_archived (boolean) — Include archived tasks; include_done (boolean) — Include done tasks. Defaults to false.; page (integer) — A page number within the paginated result set.; priority (enum(1|2|3|4)) — Filter by priority; quantity_is_null (boolean) — Only include tasks where quantity is empty; quantity_max (integer) — Maximum quantity; quantity_min (integer) — Minimum quantity; repeat_frequency (enum(daily|monthly|weekly)) — Filter by repeat frequency; repeat_task (boolean) — Filter by repeat task flag; status (enum(awaiting|doing|done|parked|sent_for_review|todo)) — Filter by effective/current status after repeat reset
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<SEOTask> | 403 | 404

### POST /api/projects/{project_pk}/seo-tasks/
`projects_seo_tasks_create` — Create SEO task
Create a project-scoped SEO task. Only project owner/admin can create tasks. Assigned user must be an active project member.
- Path: project_pk* (integer)
- Body (required): SEOTaskCreateUpdateRequest
  - task* (string)
  - deadline (string(date)?)
  - status (enum(todo|doing|awaiting|done|parked|sent_for_review))
  - priority (enum(1|2|3|4) | enum(None))
  - assigned_to (integer?)
  - description (string)
  - quantity (integer?)
  - repeat_task (boolean)
  - repeat_frequency (enum(daily|weekly|monthly) | enum(None))
  - subtasks (array<SEOTaskNestedSubtaskRequest>)
- Auth: JWT/Token/Cookie
- Returns: 201 SEOTask | 400 | 403 | 409

### GET /api/projects/{project_pk}/seo-tasks/assignees/
`projects_seo_tasks_assignees_list` — List SEO task assignees
List active project members who can be assigned SEO tasks. If someone is missing, add or invite them through the project members API first.
- Path: project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 array<SEOTaskAssignee> | 403 | 404

### DELETE /api/projects/{project_pk}/seo-tasks/{id}/
`projects_seo_tasks_destroy` — Archive SEO task
Archive a task. Only project owner/admin can archive tasks.
- Path: id* (integer) — A unique integer value identifying this SEO Task.; project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204 | 403 | 404 | 409

### GET /api/projects/{project_pk}/seo-tasks/{id}/
`projects_seo_tasks_retrieve` — Get SEO task
Get one SEO task visible to project members.
- Path: id* (integer) — Task ID; project_pk* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 200 SEOTask | 403 | 404

### PATCH /api/projects/{project_pk}/seo-tasks/{id}/
`projects_seo_tasks_partial_update` — Partially update SEO task
Partially update a task. Owner/admin can update all fields. Assigned users can only change their own task status.
- Path: id* (integer) — A unique integer value identifying this SEO Task.; project_pk* (integer)
- Body: PatchedSEOTaskCreateUpdateRequest
  - task (string)
  - deadline (string(date)?)
  - status (enum(todo|doing|awaiting|done|parked|sent_for_review))
  - priority (enum(1|2|3|4) | enum(None))
  - assigned_to (integer?)
  - description (string)
  - quantity (integer?)
  - repeat_task (boolean)
  - repeat_frequency (enum(daily|weekly|monthly) | enum(None))
  - subtasks (array<SEOTaskNestedSubtaskRequest>)
- Auth: JWT/Token/Cookie
- Returns: 200 SEOTask | 400 | 403 | 409

### PUT /api/projects/{project_pk}/seo-tasks/{id}/
`projects_seo_tasks_update` — Update SEO task
Update a task. Owner/admin can update all fields. Assigned users can only change their own task status.
- Path: id* (integer) — A unique integer value identifying this SEO Task.; project_pk* (integer)
- Body (required): SEOTaskCreateUpdateRequest
  - task* (string)
  - deadline (string(date)?)
  - status (enum(todo|doing|awaiting|done|parked|sent_for_review))
  - priority (enum(1|2|3|4) | enum(None))
  - assigned_to (integer?)
  - description (string)
  - quantity (integer?)
  - repeat_task (boolean)
  - repeat_frequency (enum(daily|weekly|monthly) | enum(None))
  - subtasks (array<SEOTaskNestedSubtaskRequest>)
- Auth: JWT/Token/Cookie
- Returns: 200 SEOTask | 400 | 403 | 409

### POST /api/projects/{project_pk}/seo-tasks/{id}/status/
`projects_seo_tasks_status_create` — Change SEO task status
Change task status. Owner/admin can change any task. Assigned users can change their own task status.
- Path: id* (integer) — A unique integer value identifying this SEO Task.; project_pk* (integer)
- Body (required): SEOTaskStatusUpdateRequest
  - status* (enum(todo|doing|awaiting|done|parked|sent_for_review))
- Auth: JWT/Token/Cookie
- Returns: 200 SEOTask | 400 | 403 | 409

### GET /api/projects/{project_pk}/seo-tasks/{id}/subtasks/
`projects_seo_tasks_subtasks_list` — List SEO task subtasks
List subtasks for a task.
- Path: id* (integer) — A unique integer value identifying this SEO Task.; project_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 array<SEOTaskSubtask> | 403 | 404

### POST /api/projects/{project_pk}/seo-tasks/{id}/subtasks/
`projects_seo_tasks_subtasks_create` — Create SEO task subtask
Create a subtask. Only project owner/admin can create subtasks.
- Path: id* (integer) — A unique integer value identifying this SEO Task.; project_pk* (integer)
- Body (required): SEOTaskSubtaskRequest
  - title* (string)
  - is_done (boolean)
- Auth: JWT/Token/Cookie
- Returns: 201 SEOTaskSubtask | 400 | 403 | 404 | 409

### DELETE /api/projects/{project_pk}/seo-tasks/{id}/subtasks/{subtask_pk}/
`projects_seo_tasks_subtasks_destroy` — Delete SEO task subtask
Delete a task subtask. Only project owner/admin can delete subtasks.
- Path: id* (integer) — A unique integer value identifying this SEO Task.; project_pk* (integer); subtask_pk* (integer) — Subtask ID
- Auth: JWT/Token/Cookie
- Returns: 204 | 400 | 403 | 404 | 409

### PATCH /api/projects/{project_pk}/seo-tasks/{id}/subtasks/{subtask_pk}/
`projects_seo_tasks_subtasks_partial_update` — Update SEO task subtask
Update a task subtask. Only project owner/admin can update subtasks.
- Path: id* (integer) — A unique integer value identifying this SEO Task.; project_pk* (integer); subtask_pk* (integer) — Subtask ID
- Body: PatchedSEOTaskSubtaskUpdateRequest
  - title (string)
  - is_done (boolean)
- Auth: JWT/Token/Cookie
- Returns: 200 SEOTaskSubtask | 400 | 403 | 404 | 409

### GET /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/
`projects_seo_tasks_comments_list` — List SEO task comments
List top-level comments on an SEO task, each with its replies nested inline. Any active project member can read.
- Path: project_pk* (integer) — Project ID; seo_task_pk* (integer) — SEO task ID
- Query: page (integer) — Page number; page_size (integer) — Comments per page. Default 10, max 100.
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<SEOTaskComment> | 403

### POST /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/
`projects_seo_tasks_comments_create` — Post an SEO task comment
Post a comment or a reply. Any active member may comment, view-only included. **Body is Markdown.** Raw HTML and javascript:/data:/vbscript: link schemes are rejected. Mention a member with the token `@[Name](user:12)` …
- Path: project_pk* (string); seo_task_pk* (integer)
- Body (required): SEOTaskCommentWriteRequest
  - body* (string)
  - parent (integer?)
- Auth: JWT/Token/Cookie
- Returns: 201 SEOTaskComment | 400 | 403 | 409

### DELETE /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/{id}/
`projects_seo_tasks_comments_destroy` — Delete your comment
Soft-delete your own comment. The body is cleared and the row is kept as a tombstone so replies do not orphan.
- Path: id* (integer) — A unique integer value identifying this SEO Task Comment.; project_pk* (string); seo_task_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204 | 403

### PATCH /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/{id}/
`projects_seo_tasks_comments_partial_update` — Edit your comment
Edit your own comment. Mentions are re-synced from the new body; only newly-added mentions are notified.
- Path: id* (integer) — A unique integer value identifying this SEO Task Comment.; project_pk* (string); seo_task_pk* (integer)
- Body: PatchedSEOTaskCommentWriteRequest
  - body (string)
  - parent (integer?)
- Auth: JWT/Token/Cookie
- Returns: 200 SEOTaskComment | 403

### DELETE /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/{id}/reactions/{emoji}/
`projects_seo_tasks_comments_reactions_destroy` — Add or remove a reaction
PUT adds the reaction, DELETE removes it. Both are idempotent — a retried request never flips the state back, which a POST toggle would. `emoji` is an ASCII slug: thumbs_up, thumbs_down, check, tada, heart, eyes, rocket…
- Path: emoji* (string) — Reaction slug; id* (integer) — A unique integer value identifying this SEO Task Comment.; project_pk* (string); seo_task_pk* (integer)
- Auth: JWT/Token/Cookie
- Returns: 200 | 204 | 400 | 403

### PUT /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/{id}/reactions/{emoji}/
`projects_seo_tasks_comments_reactions_update` — Add or remove a reaction
PUT adds the reaction, DELETE removes it. Both are idempotent — a retried request never flips the state back, which a POST toggle would. `emoji` is an ASCII slug: thumbs_up, thumbs_down, check, tada, heart, eyes, rocket…
- Path: emoji* (string) — Reaction slug; id* (integer) — A unique integer value identifying this SEO Task Comment.; project_pk* (string); seo_task_pk* (integer)
- Body: SEOTaskCommentRequest
  - parent (integer?)
  - body (string)
  - is_edited (boolean)
  - is_deleted (boolean)
- Auth: JWT/Token/Cookie
- Returns: 200 | 204 | 400 | 403

### GET /api/seo-tasks/
`seo_tasks_list` — List accessible SEO tasks
List SEO tasks from all active projects shared with the authenticated user. Repeating tasks completed in a previous calendar period are lazily reset to todo on read, with subtasks unchecked.
- Query: assigned_to (integer) — Filter by assigned user ID; due (enum(none|overdue|today|upcoming)) — Filter by deadline bucket; include_archived (boolean) — Include archived tasks; include_done (boolean) — Include done tasks. Defaults to false.; page (integer) — A page number within the paginated result set.; priority (enum(1|2|3|4)) — Filter by priority; quantity_is_null (boolean) — Only include tasks where quantity is empty; quantity_max (integer) — Maximum quantity; quantity_min (integer) — Minimum quantity; repeat_frequency (enum(daily|monthly|weekly)) — Filter by repeat frequency; repeat_task (boolean) — Filter by repeat task flag; status (enum(awaiting|doing|done|parked|sent_for_review|todo)) — Filter by effective/current status after repeat reset
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<AccessibleSEOTask>

### GET /api/seo-tasks/meta/
`seo_tasks_meta_retrieve` — Get SEO task metadata
Return allowed SEO task status and priority values for filters and forms.
- Auth: JWT/Token/Cookie
- Returns: 200 SEOTaskMeta

## Response schemas

### AccessibleSEOTask
- project* (integer) [read-only]
- project_name* (string) [read-only]
- id* (integer) [read-only]
- task* (string)
- deadline (string(date)?)
- status (enum(todo|doing|awaiting|done|parked|sent_for_review))
- status_display* (string) [read-only]
- effective_status* (string) [read-only]
- priority (enum(1|2|3|4) | enum(None))
- assigned_to (integer?)
- assigned_to_email* (string?) [read-only]
- assigned_to_name* (string) [read-only]
- description (string)
- quantity (integer?)
- repeat_task (boolean)
- repeat_frequency (enum(daily|weekly|monthly) | enum() | enum(None))
- last_completed_at* (string(date-time)?) [read-only]
- is_due_this_period* (boolean) [read-only]
- added_by* (integer?) [read-only]
- added_by_email* (string?) [read-only]
- added_by_name* (string) [read-only]
- is_archived* (boolean) [read-only]
- archived_at* (string(date-time)?) [read-only]
- archived_by* (integer?) [read-only]
- archived_by_email* (string?) [read-only]
- archived_by_name* (string) [read-only]
- subtasks* (array<SEOTaskSubtask>) [read-only]
- comment_count* (integer) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### SEOTask
- id* (integer) [read-only]
- task* (string)
- deadline (string(date)?)
- status (enum(todo|doing|awaiting|done|parked|sent_for_review))
- status_display* (string) [read-only]
- effective_status* (string) [read-only]
- priority (enum(1|2|3|4) | enum(None))
- assigned_to (integer?)
- assigned_to_email* (string?) [read-only]
- assigned_to_name* (string) [read-only]
- description (string)
- quantity (integer?)
- repeat_task (boolean)
- repeat_frequency (enum(daily|weekly|monthly) | enum() | enum(None))
- last_completed_at* (string(date-time)?) [read-only]
- is_due_this_period* (boolean) [read-only]
- added_by* (integer?) [read-only]
- added_by_email* (string?) [read-only]
- added_by_name* (string) [read-only]
- is_archived* (boolean) [read-only]
- archived_at* (string(date-time)?) [read-only]
- archived_by* (integer?) [read-only]
- archived_by_email* (string?) [read-only]
- archived_by_name* (string) [read-only]
- subtasks* (array<SEOTaskSubtask>) [read-only]
- comment_count* (integer) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### SEOTaskComment
- id* (integer) [read-only]
- parent (integer?)
- author* (object) [read-only]
- body (string)
- is_edited (boolean)
- is_deleted (boolean)
- mentions* (array<any>) [read-only]
- reactions* (array<any>) [read-only]
- replies* (array<any>) [read-only]
- can_edit* (boolean) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### SEOTaskMeta
- statuses* (array<SEOTaskChoice>)
- priorities* (array<SEOTaskChoice>)
- repeat_frequencies* (array<SEOTaskChoice>)

### SEOTaskSubtask
- id* (integer) [read-only]
- title* (string)
- is_done (boolean)
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]
