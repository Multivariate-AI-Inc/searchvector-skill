# SearchVector API — projects

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 26 endpoints.

### GET /api/invitations/
`invitations_list` — Get my pending invitations (all projects)
Get all pending invitations for the authenticated user across all projects.
- Auth: JWT/Token/Cookie
- Returns: 200 array<ProjectMembership>

### POST /api/invitations/accept/
`invitations_accept_create` — Accept invitation
Accept a pending invitation using only the token. The token is globally unique, so no project_id is required. Frontend should call this when user clicks invitation link.
- Query: token* (string) — Invitation token from email link
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectMembership | 400 | 403 | 404

### POST /api/invitations/reject/
`invitations_reject_create` — Reject invitation
Reject a pending invitation. This deletes the invitation.
- Query: token* (string) — Invitation token from email link
- Body (required): ProjectMembershipRequest
  - project* (integer)
  - user (integer?) — Null for pending invitations to unregistered emails
  - email (string(email)) — Email address for invitation (required for pending members)
  - role (enum(owner|admin|viewer))
  - status (any)
  - invited_by (integer?)
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 403 | 404

### GET /api/projects/
`projects_list` — List user's projects
Returns all projects where the authenticated user is a member, including project competitors. Supports search by name or URL.
- Query: page (integer) — A page number within the paginated result set.; search (string) — Search projects by name or website URL
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<ProjectList>

### POST /api/projects/
`projects_create` — Create a new project
Creates a new project and automatically assigns the creator as the owner.
- Body (required): ProjectCreateRequest
  - name* (string)
  - website_url* (string(uri)) — Main website URL for this project
  - description (string)
  - brand_regex (string) — Regex pattern for brand filtering (e.g., 'nike|adidas')
  - default_country (string) — Default country code for this project (e.g., 'us', 'in', 'uk')
- Auth: JWT/Token/Cookie
- Returns: 201 ProjectCreate

### GET /api/projects/fetch-brand-regex/
`projects_fetch_brand_regex_retrieve` — Fetch brand regex for project URL
Fetch global brand regex pattern for a project URL. Returns regex if available, otherwise returns a message to check back later.
- Query: project_url* (string) — Project URL (e.g., 'https://example.com' or 'example.com')
- Auth: JWT/Token/Cookie
- Returns: 200 FetchBrandRegexResponse | 400

### DELETE /api/projects/{id}/
`projects_destroy` — Delete project
Deletes a project. Only the project owner can archive it, and data is preserved for recovery.
- Path: id* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 204

### GET /api/projects/{id}/
`projects_retrieve` — Get project details
Returns detailed information about a specific project including members, competitors, and integrations.
- Path: id* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectDetail

### PATCH /api/projects/{id}/
`projects_partial_update` — Partially update project
Partially update project information. Only members with edit permissions can update.
- Path: id* (integer) — Project ID
- Body: PatchedProjectDetailRequest
  - name (string)
  - website_url (string(uri)) — Main website URL for this project
  - description (string)
  - brand_regex (string) — Regex pattern for brand filtering (e.g., 'nike|adidas')
  - default_country (string) — Default country code for this project (e.g., 'us', 'in', 'uk')
  - is_active (boolean)
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectDetail

### PUT /api/projects/{id}/
`projects_update` — Update project
Update project information. Only members with edit permissions can update.
- Path: id* (integer) — Project ID
- Body (required): ProjectDetailRequest
  - name* (string)
  - website_url* (string(uri)) — Main website URL for this project
  - description (string)
  - brand_regex (string) — Regex pattern for brand filtering (e.g., 'nike|adidas')
  - default_country (string) — Default country code for this project (e.g., 'us', 'in', 'uk')
  - is_active (boolean)
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectDetail

### GET /api/projects/{id}/available_properties/
`projects_available_properties_retrieve` — Get available GSC properties for an OAuth token
Lists all GSC properties (domains) available for a specific OAuth token. The project path is only used to route the request and is not validated.
- Path: id* (string) — Project path segment used for routing only
- Query: oauth_token_id* (integer) — OAuth token ID to fetch properties from
- Auth: JWT/Token/Cookie
- Returns: 200 GSCPropertiesResponse | 400 | 401 | 404 | 500

### POST /api/projects/{id}/confirm-unlock/
`projects_confirm_unlock_create` — Confirm unlock with selected members
Confirm project unlock after user selects which members to keep. Call this only when unlock returned requires_member_selection=true. Pass the IDs of members to KEEP. All other non-owner members will be marked inactive. …
- Path: id* (integer) — A unique integer value identifying this Project.
- Body (required): ConfirmUnlockRequest
  - keep_member_ids* (array<integer>) — List of ProjectMembership IDs to keep active (owner is always kept)
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 402 | 403 | 404

### POST /api/projects/{id}/unlock/
`projects_unlock_create` — Unlock a project
Unlock a locked project. Only possible if within plan limits. If the project has more members than the new plan allows, returns requires_member_selection=true with a list of current members. Frontend must then call conf…
- Path: id* (integer) — Project ID
- Body (required): ProjectListRequest
  - name* (string)
  - website_url* (string(uri)) — Main website URL for this project
  - description (string)
  - brand_regex (string) — Regex pattern for brand filtering (e.g., 'nike|adidas')
  - default_country (string) — Default country code for this project (e.g., 'us', 'in', 'uk')
  - is_active (boolean)
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 402 | 403 | 404

### GET /api/projects/{project_pk}/integrations/
`projects_integrations_list` — List project integrations
Returns all integrations for a specific project.
- Path: project_pk* (integer) — Project ID
- Query: page (integer) — A page number within the paginated result set.
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<ProjectIntegration>

### POST /api/projects/{project_pk}/integrations/
`projects_integrations_create` — Create project integration
Links an OAuth token to a project as an integration.
- Path: project_pk* (integer) — Project ID
- Body (required): ProjectIntegrationRequest
  - project* (integer)
  - oauth_token* (integer)
  - integration_type* (enum(gsc|google_ads|ga4|youtube))
  - is_active (boolean)
  - config (any) — Service-specific configuration (e.g., property IDs, account IDs)
  - last_synced_at (string(date-time)?) — Last time data was fetched from this integration
- Auth: JWT/Token/Cookie
- Returns: 201 ProjectIntegration

### POST /api/projects/{project_pk}/integrations/add/
`projects_integrations_add_create` — Add integration to project
Adds a new integration to a project. Can either link an existing OAuth token or redirect to OAuth flow to connect a new account. Each project can have only one integration per type (e.g., one GSC, one Google Ads). GSC c…
- Path: project_pk* (integer) — Project ID
- Body (required): AddIntegrationRequest
  - integration_type* (enum(gsc|google_ads|ga4|youtube))
  - action* (enum(use_existing|connect_new))
  - oauth_token_id (integer)
  - property_url (string)
- Auth: JWT/Token/Cookie
- Returns: 200 OAuthRedirectResponse | 201 ProjectIntegration | 400 | 403 | 404 | 409

### DELETE /api/projects/{project_pk}/integrations/{id}/
`projects_integrations_destroy` — Remove integration
Removes an integration from a project. The OAuth token is preserved and can be reused.
- Path: id* (integer) — Integration ID; project_pk* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 204

### GET /api/projects/{project_pk}/integrations/{id}/
`projects_integrations_retrieve` — Get integration details
Returns details about a specific project integration including OAuth status.
- Path: id* (integer) — Integration ID; project_pk* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectIntegration

### PATCH /api/projects/{project_pk}/integrations/{id}/
`projects_integrations_partial_update` — Partially update integration
Partially update integration configuration or status.
- Path: id* (integer) — Integration ID; project_pk* (integer) — Project ID
- Body: PatchedProjectIntegrationRequest
  - project (integer)
  - oauth_token (integer)
  - integration_type (enum(gsc|google_ads|ga4|youtube))
  - is_active (boolean)
  - config (any) — Service-specific configuration (e.g., property IDs, account IDs)
  - last_synced_at (string(date-time)?) — Last time data was fetched from this integration
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectIntegration

### PUT /api/projects/{project_pk}/integrations/{id}/
`projects_integrations_update` — Update integration
Update integration configuration or status.
- Path: id* (integer) — Integration ID; project_pk* (integer) — Project ID
- Body (required): ProjectIntegrationRequest
  - project* (integer)
  - oauth_token* (integer)
  - integration_type* (enum(gsc|google_ads|ga4|youtube))
  - is_active (boolean)
  - config (any) — Service-specific configuration (e.g., property IDs, account IDs)
  - last_synced_at (string(date-time)?) — Last time data was fetched from this integration
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectIntegration

### GET /api/projects/{project_pk}/members/
`projects_members_list` — List project members and invitations
Returns all active members and pending invitations for a project.
- Path: project_pk* (integer) — Project ID
- Query: page (integer) — A page number within the paginated result set.; status (enum(active|pending)) — Filter by status (active or pending)
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<ProjectMembership>

### POST /api/projects/{project_pk}/members/
`projects_members_create` — Add/invite members to project (Google Sheets style)
Add or invite multiple members at once. If user exists, they're added instantly (active). If user doesn't exist, they receive an invitation email (pending). Existing members can have their roles updated.
- Path: project_pk* (integer)
- Body (required): AddMembersRequest
  - members* (array<MemberInputRequest>) — List of members to add/invite
- Auth: JWT/Token/Cookie
- Returns: 200 AddMembersResponse | 400 | 402 | 403 | 409

### DELETE /api/projects/{project_pk}/members/{id}/
`projects_members_destroy` — Remove member or cancel invitation
Removes an active member or cancels a pending invitation. Only owners/admins can remove members.
- Path: id* (integer) — Membership ID; project_pk* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 204

### GET /api/projects/{project_pk}/members/{id}/
`projects_members_retrieve` — Get project member details
Returns details for a single project member or invitation.
- Path: id* (integer) — Membership ID; project_pk* (integer) — Project ID
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectMembership

### PATCH /api/projects/{project_pk}/members/{id}/
`projects_members_partial_update` — Update member role
Update an existing member's role. Only owners can update roles.
- Path: id* (integer) — A unique integer value identifying this Project Membership.; project_pk* (integer)
- Body: PatchedUpdateMemberRoleRequest
  - role (enum(owner|admin|viewer))
- Auth: JWT/Token/Cookie
- Returns: 200 ProjectMembership | 400 | 403

### POST /api/projects/{project_pk}/members/{id}/resend_invitation/
`projects_members_resend_invitation_create` — Resend invitation email
Resend invitation email for a pending membership. Generates new token and extends expiry.
- Path: id* (integer) — Membership ID; project_pk* (integer)
- Body (required): ProjectMembershipRequest
  - project* (integer)
  - user (integer?) — Null for pending invitations to unregistered emails
  - email (string(email)) — Email address for invitation (required for pending members)
  - role (enum(owner|admin|viewer))
  - status (any)
  - invited_by (integer?)
- Auth: JWT/Token/Cookie
- Returns: 200 ResendInvitationResponse | 400 | 403

## Response schemas

### AddMembersResponse
- added* (array<ProjectMembership>) — Users instantly added (already registered)
- invited* (array<ProjectMembership>) — Users invited (pending registration)
- updated* (array<object>) — Existing members whose roles were updated
- errors* (array<object>) — Errors encountered during processing

### FetchBrandRegexResponse
- project_url* (string)
- brand_regex* (string?)
- found* (boolean)
- message (string)

### GSCPropertiesResponse
- oauth_token_id* (integer)
- google_email* (string(email))
- properties* (array<GSCProperty>)

### OAuthRedirectResponse
- oauth_url* (string(uri))
- message* (string)

### ProjectCreate
- id* (integer) [read-only]
- name* (string)
- website_url* (string(uri)) — Main website URL for this project
- description (string)
- brand_regex (string) — Regex pattern for brand filtering (e.g., 'nike|adidas')
- default_country (string) — Default country code for this project (e.g., 'us', 'in', 'uk')

### ProjectDetail
- id* (integer) [read-only]
- name* (string)
- website_url* (string(uri)) — Main website URL for this project
- description (string)
- brand_regex (string) — Regex pattern for brand filtering (e.g., 'nike|adidas')
- default_country (string) — Default country code for this project (e.g., 'us', 'in', 'uk')
- is_active (boolean)
- is_locked* (boolean) [read-only] — Locked projects are read-only until user unlocks them (within plan limits)
- locked_at* (string(date-time)?) [read-only] — When the project was locked due to plan downgrade
- lock_reason* (string) [read-only] — Reason for locking (e.g., 'plan_downgrade')
- owner* (object) [read-only]
- member_count* (integer) [read-only]
- members_limit* (integer?) [read-only]
- members_remaining* (integer?) [read-only]
- memberships* (array<ProjectMembership>) [read-only]
- competitors* (array<ProjectCompetitorSummary>) [read-only]
- integrations* (array<ProjectIntegration>) [read-only]
- active_integrations* (object) [read-only]
- metrics* (object) [read-only]
- my_role* (any?) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### ProjectIntegration
- id* (integer) [read-only]
- project* (integer)
- oauth_token* (integer)
- integration_type* (enum(gsc|google_ads|ga4|youtube))
- integration_display* (string) [read-only]
- is_active (boolean)
- config (any) — Service-specific configuration (e.g., property IDs, account IDs)
- property_url* (string?) [read-only]
- last_synced_at (string(date-time)?) — Last time data was fetched from this integration
- google_email* (string) [read-only]
- oauth_status* (object) [read-only]
- status_display* (string) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### ProjectList
- id* (integer) [read-only]
- name* (string)
- website_url* (string(uri)) — Main website URL for this project
- description (string)
- brand_regex (string) — Regex pattern for brand filtering (e.g., 'nike|adidas')
- default_country (string) — Default country code for this project (e.g., 'us', 'in', 'uk')
- is_active (boolean)
- is_locked* (boolean) [read-only] — Locked projects are read-only until user unlocks them (within plan limits)
- locked_at* (string(date-time)?) [read-only] — When the project was locked due to plan downgrade
- lock_reason* (string) [read-only] — Reason for locking (e.g., 'plan_downgrade')
- owner_email* (string) [read-only]
- member_count* (integer) [read-only]
- competitors* (array<ProjectCompetitorSummary>) [read-only]
- integration_count* (integer) [read-only]
- active_integrations* (object) [read-only]
- metrics* (object) [read-only]
- my_role* (any?) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### ProjectMembership
- id* (integer) [read-only]
- project* (integer)
- user (integer?) — Null for pending invitations to unregistered emails
- email (string(email)) — Email address for invitation (required for pending members)
- user_email* (string) [read-only]
- user_name* (string) [read-only]
- role (enum(owner|admin|viewer))
- role_display* (string) [read-only]
- status (any)
- status_display* (string) [read-only]
- is_expired* (boolean) [read-only]
- invitation_expires_at* (string(date-time)?) [read-only] — When the invitation expires
- created_at* (string(date-time)) [read-only]
- accepted_at* (string(date-time)?) [read-only] — When the invitation was accepted
- invited_by (integer?)
- invited_by_email* (string) [read-only]

### ResendInvitationResponse
- message* (string)
- invitation* (ProjectMembership)
