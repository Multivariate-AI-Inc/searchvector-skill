# SearchVector API — automations

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 17 endpoints.

### GET /api/automations/alert-groups/
`automations_alert_groups_list` — List alert groups
Return all named combined alert groups for the given automation type. Team member sharing is supported only for GSC project alerts.
- Query: automation_type* (string) — Automation type slug (gsc_weekly_report, ga4_weekly_report, google_ads_weekly_report)
- Auth: JWT/Token/Cookie
- Returns: 200 array<AlertGroup> | 400

### POST /api/automations/alert-groups/
`automations_alert_groups_create` — Create alert group
Create a new named combined alert group. Each group maps to one combined AutomationRule and sends one email per group. A project can only belong to one enabled group at a time. Team member sharing is supported only for …
- Body (required): AlertGroupCreateRequest
  - automation_type* (enum(gsc_weekly_report|ga4_weekly_report|google_ads_weekly_report))
  - group_name* (string)
  - is_enabled (boolean)
  - share_with_team_members (boolean)
  - target_ids (array<integer>)
- Auth: JWT/Token/Cookie
- Returns: 201 AlertGroup | 400 | 500

### DELETE /api/automations/alert-groups/{group_id}/
`automations_alert_groups_destroy` — Delete alert group
Delete a named combined alert group and all its targets.
- Path: group_id* (integer)
- Auth: JWT/Token/Cookie
- Returns: 204 | 404 | 500

### PATCH /api/automations/alert-groups/{group_id}/
`automations_alert_groups_partial_update` — Update alert group
Rename, toggle enabled state, update team sharing, or update targets of a named combined alert group. Team member sharing is supported only for GSC project alerts.
- Path: group_id* (integer)
- Body: PatchedAlertGroupUpdateRequest
  - group_name (string)
  - is_enabled (boolean)
  - share_with_team_members (boolean)
  - target_ids (array<integer>)
- Auth: JWT/Token/Cookie
- Returns: 200 AlertGroup | 400 | 404 | 500

### GET /api/automations/combined-alerts/
`automations_combined_alerts_retrieve` — Get combined alert state
Return the helper-managed combined weekly alert state for one automation type, including eligible targets and which ones are selected. Team member sharing is supported only for GSC project alerts.
- Auth: JWT/Token/Cookie
- Returns: 200 AutomationCombinedAlert | 400

### PATCH /api/automations/combined-alerts/
`automations_combined_alerts_partial_update` — Get combined alert state
Return the helper-managed combined weekly alert state for one automation type, including eligible targets and which ones are selected. Team member sharing is supported only for GSC project alerts.
- Body: PatchedAutomationCombinedAlertToggleRequest
  - automation_type (enum(gsc_weekly_report|ga4_weekly_report|google_ads_weekly_report))
  - is_enabled (boolean)
  - share_with_team_members (boolean)
  - target_ids (array<integer>)
- Auth: JWT/Token/Cookie
- Returns: 200 AutomationCombinedAlert | 400

### GET /api/automations/eligible-targets/
`automations_eligible_targets_list` — List eligible automation targets
Return valid targets for the selected automation type for the logged-in user.
- Query: automation_type* (string) — Automation type slug such as gsc_weekly_report or ga4_weekly_report.
- Auth: JWT/Token/Cookie
- Returns: 200 array<EligibleAutomationTarget> | 400

### GET /api/automations/global-state/
`automations_global_state_retrieve` — Get global automation state
Return the user's current global automation master switch state.
- Auth: JWT/Token/Cookie
- Returns: 200 AutomationGlobalStateResponse

### POST /api/automations/global-state/
`automations_global_state_create` — Set global automation state
Turn the user's global automation master switch on or off. Turning it off stops all automation emails for the user. Turning it on allows emails again for rules that are already individually enabled. This endpoint does n…
- Body (required): AutomationGlobalStateRequest
  - is_enabled* (boolean)
- Auth: JWT/Token/Cookie
- Returns: 200 AutomationGlobalStateResponse | 400

### GET /api/automations/project-alerts/
`automations_project_alerts_list` — List project alert states
Return alert state rows for the selected automation type. GSC returns owner projects. GA4 returns connected GA4 properties. Google Ads returns connected Google Ads accounts. Sitemap weekly report returns owner projects …
- Query: automation_type (string) — Supported values: gsc_weekly_report, ga4_weekly_report, google_ads_weekly_report, sitemap…
- Auth: JWT/Token/Cookie
- Returns: 200 array<AutomationProjectAlert> | 400

### PATCH /api/automations/project-alerts/
`automations_project_alerts_partial_update` — Toggle project alert
Enable or disable one alert target for the selected automation type. GSC uses project_id. GA4 uses property_id. Google Ads uses account_id. Sitemap weekly report also uses project_id and requires sitemap_urls plus servi…
- Body: PatchedAutomationProjectAlertToggleRequest
  - automation_type (any)
  - project_id (integer)
  - property_id (integer)
  - account_id (integer)
  - sitemap_urls (array<string(uri)>)
  - service_account_id (integer)
  - schedule_frequency (enum(daily|weekly|monthly))
  - is_enabled (boolean)
  - share_with_team_members (boolean)
  - selected_recipient_user_ids (array<integer>)
  - dashboard_report_type (enum(gsc_connected|gsc_not_connected))
- Auth: JWT/Token/Cookie
- Returns: 200 AutomationProjectAlert | 400

### GET /api/automations/rules/
`automations_rules_list` — List automation rules
Return automation rules for the logged-in user.
- Query: page (integer) — A page number within the paginated result set.
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<AutomationRuleList>

### POST /api/automations/rules/
`automations_rules_create` — Create automation rule
Create one automation rule and its nested targets. Set share_with_team_members=true to send project alert emails to active project members who have global automation email enabled.
- Body (required): AutomationRuleWriteRequest
  - automation_type* (string)
  - is_enabled (boolean)
  - delivery_mode (any)
  - config (object)
  - share_with_team_members (boolean)
  - targets* (array<AutomationRuleTargetWriteRequest>)
- Auth: JWT/Token/Cookie
- Returns: 201 AutomationRuleDetail | 400

### DELETE /api/automations/rules/{id}/
`automations_rules_destroy` — Delete automation rule
Delete one automation rule for the logged-in user.
- Path: id* (integer) — A unique integer value identifying this Automation Rule.
- Auth: JWT/Token/Cookie
- Returns: 204

### GET /api/automations/rules/{id}/
`automations_rules_retrieve` — Get automation rule
Return one automation rule with its nested targets.
- Path: id* (integer) — A unique integer value identifying this Automation Rule.
- Auth: JWT/Token/Cookie
- Returns: 200 AutomationRuleDetail

### PATCH /api/automations/rules/{id}/
`automations_rules_partial_update` — Update automation rule
Partially update one automation rule. share_with_team_members controls whether project alert emails go only to owners or to all active project members.
- Path: id* (integer) — A unique integer value identifying this Automation Rule.
- Body: PatchedAutomationRuleUpdateRequest
  - is_enabled (boolean)
  - delivery_mode (enum(combined|separate))
  - config (object)
  - share_with_team_members (boolean)
  - targets (array<AutomationRuleTargetWriteRequest>)
- Auth: JWT/Token/Cookie
- Returns: 200 AutomationRuleDetail | 400

### GET /api/automations/types/
`automations_types_list` — List automation types
Return active automation types and their FE capabilities.
- Auth: JWT/Token/Cookie
- Returns: 200 array<AutomationTypeList>

## Response schemas

### AlertGroup
- id* (integer)
- automation_type* (string)
- group_name* (string)
- is_enabled* (boolean)
- share_with_team_members* (boolean)
- target_ids* (array<integer>)
- target_count* (integer)
- targets* (array<AlertGroupTarget>)

### AutomationCombinedAlert
- automation_type* (string)
- rule_id* (integer?)
- is_enabled* (boolean)
- delivery_mode* (string)
- share_with_team_members* (boolean)
- selected_target_ids* (array<integer>)
- selected_target_count* (integer)
- targets* (array<AutomationCombinedAlertTarget>)

### AutomationGlobalStateResponse
- is_enabled* (boolean)
- disabled_rules_count* (integer)
- enabled_rules_count* (integer)
- total_rules_count* (integer)

### AutomationProjectAlert
- automation_type* (string)
- project_id (integer?)
- property_id (integer?)
- account_id (integer?)
- name (string?)
- property_name (string?)
- display_name (string?)
- account_name (string?)
- website_url (string?)
- gsc_connected (boolean)
- gsc_valid (boolean)
- service_account_exists (boolean)
- service_account_active (boolean)
- service_account_id (integer?)
- service_account_email (string?)
- available_service_accounts (array<object>)
- sitemap_urls (array<string>)
- can_enable_sitemap_weekly_report (boolean)
- schedule_frequency (string)
- blocking_reasons (array<string>)
- ga4_connected (boolean)
- ga4_valid (boolean)
- google_ads_connected (boolean)
- google_ads_valid (boolean)
- property_url* (string?)
- google_property_id (string?)
- customer_id (string?)
- currency_code (string?)
- timezone (string?)
- google_email (string?)
- alert_enabled* (boolean)
- share_with_team_members (boolean)
- available_recipients (array<object>)
- selected_recipient_user_ids (array<integer>)
- dashboard_report_type (string)
- alert_type* (enum(individual|group) | enum(None))
- group_name* (string?)
- rule_id* (integer?)
- target_id* (integer?)

### AutomationRuleDetail
- id* (integer) [read-only]
- automation_type* (object) [read-only]
- is_enabled (boolean)
- schedule_frequency (enum(daily|weekly|monthly))
- schedule_weekday (any)
- delivery_mode (enum(combined|separate))
- config* (object)
- recipient_mode (enum(owner))
- share_with_team_members (boolean) — Send project automation emails to all active project members.
- target_count* (integer) [read-only]
- targets* (array<object>) [read-only]
- last_run_at (string(date-time)?)
- last_success_at (string(date-time)?)
- latest_run_status* (string?) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### AutomationRuleList
- id* (integer) [read-only]
- automation_type* (object) [read-only]
- is_enabled (boolean)
- schedule_frequency (enum(daily|weekly|monthly))
- schedule_weekday (any)
- delivery_mode (enum(combined|separate))
- recipient_mode (enum(owner))
- share_with_team_members (boolean) — Send project automation emails to all active project members.
- target_count* (integer) [read-only]
- targets* (array<object>) [read-only]
- last_run_at (string(date-time)?)
- last_success_at (string(date-time)?)
- latest_run_status* (string?) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]
