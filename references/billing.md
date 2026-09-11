# SearchVector API — billing

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 12 endpoints.

### POST /api/billing/checkout/
`billing_checkout_create`
- Body (required): CheckoutInputRequest
  - plan_name* (string) — Plan name to subscribe to (pro, enterprise)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/billing/credits/history/
`billing_credits_history_list`
- Query: page (integer) — A page number within the paginated result set.
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<OneTimePurchase>

### GET /api/billing/credits/packs/
`billing_credits_packs_list`
- Auth: JWT/Token/Cookie
- Returns: 200 array<CreditPack>

### POST /api/billing/credits/purchase/
`billing_credits_purchase_create`
- Body (required): PurchaseCreditsInputRequest
  - credit_amount* (any) — Number of credits to purchase (1000, 5000, or 10000) * `1000` - 1000 * `5000` - 5000 * `10000` - 10000
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/billing/plans/
`billing_plans_list`
- Query: page (integer) — A page number within the paginated result set.
- Auth: JWT/Token/Cookie/none
- Returns: 200 Paginated<SubscriptionPlan>

### POST /api/billing/portal/
`billing_portal_create`
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/billing/status/
`billing_status_retrieve`
- Auth: JWT/Token/Cookie
- Returns: 200 BillingStatus

### GET /api/billing/usage/
`billing_usage_retrieve`
- Query: project_id (integer) — Optional project ID. When provided, only the active owner can access the project usage da…
- Auth: JWT/Token/Cookie
- Returns: 200 UsageLimits

### GET /api/credits/actions/
`credits_actions_list` — List Available Actions
Get list of all active credit actions available for use
- Query: ordering (string) — Which field to use when ordering the results.; page (integer) — A page number within the paginated result set.
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<CreditAction>

### GET /api/credits/balance/
`credits_balance_retrieve` — Get Credit Balance
Retrieve authenticated user's current credit balance and subscription tier
- Auth: JWT/Token/Cookie
- Returns: 200 CreditBalance

### POST /api/credits/estimate/
`credits_estimate_create` — Estimate Cost
Calculate cost estimate for an action without reserving credits
- Body (required): EstimateCostRequest
  - action_id* (integer) — ID of the CreditAction to estimate cost for
  - quantity* (integer) — Quantity for cost calculation (e.g., number of days, keywords, accounts)
- Auth: JWT/Token/Cookie
- Returns: 200 object

### GET /api/credits/history/
`credits_history_list` — Get Usage History
Retrieve paginated usage history for authenticated user with optional filters
- Query: end_date (string) — Filter to date (YYYY-MM-DD); ordering (string) — Which field to use when ordering the results.; page (integer) — A page number within the paginated result set.; service (string) — Filter by service (gsc, google_ads, youtube); start_date (string) — Filter from date (YYYY-MM-DD)
- Auth: JWT/Token/Cookie
- Returns: 200 Paginated<UsageLog>

## Response schemas

### BillingStatus
- current_plan* (string) [read-only] — Get current plan name (custom or standard).
- plan_display_name* (string) [read-only] — Get plan display name (custom or standard).
- plan_type* (string) [read-only] — Get plan type: 'standard' or 'custom'.
- subscription_status* (string)
- credits_remaining* (number) [read-only] — Get current credit balance.
- credits_limit* (integer) [read-only] — Get credits limit (custom plan override or standard).
- projects_current* (integer) [read-only] — Get current project count.
- projects_limit* (integer) [read-only] — Get projects limit (custom plan override or standard).
- keywords_current* (integer) [read-only] — Get current keyword count.
- keywords_limit* (integer) [read-only] — Get keywords limit (custom plan override or standard).
- features* (object) [read-only] — Get features (custom plan overrides merged with standard).
- is_custom_plan* (boolean) [read-only] — Check if user has active custom plan.
- custom_plan_expires_at* (string(date-time)) [read-only] — Get custom plan expiration date (if applicable).
- trial_ends_at (string(date-time))
- subscription_ends_at (string(date-time))
- current_period_start (string(date-time))
- current_period_end (string(date-time))
- cancel_at_period_end (boolean)
- canceled_at (string(date-time))
- is_grandfathered* (boolean)
- grandfathered_price (string(decimal))
- is_active* (boolean) [read-only] — Check if subscription is truly active (includes trialing subscriptions).
- cancellation_status* (string) [read-only] — Get cancellation status message (when it will cancel).
- cancellation_feedback* (object) [read-only] — Get the user's cancellation feedback/reason from Stripe.
- days_until_renewal* (integer) [read-only] — Calculate full calendar days until renewal or scheduled cancellation.
- trial_eligible* (boolean) [read-only] — Check if user is eligible for a trial.
- has_used_trial* (boolean)

### CreditAction
- id* (integer) [read-only]
- name* (string) [read-only]
- service* (any) [read-only]
- service_display* (string) [read-only]
- pricing_type* (any) [read-only]
- pricing_type_display* (string) [read-only]
- base_cost* (string(decimal)) [read-only]
- description* (string) [read-only]
- is_active* (boolean) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### CreditBalance
- id* (integer) [read-only]
- user_email* (string(email)) [read-only]
- balance* (string(decimal)) [read-only]
- subscription_tier* (any) [read-only]
- subscription_tier_display* (string) [read-only]
- last_reset_at* (string(date-time)?) [read-only]
- created_at* (string(date-time)) [read-only]
- updated_at* (string(date-time)) [read-only]

### OneTimePurchase
- id* (integer)
- purchase_type* (string)
- quantity* (integer) — Credits purchased
- amount_paid* (string(decimal))
- currency* (string)
- status* (string)
- purchased_at* (string(date-time))
- fulfilled_at (string(date-time))

### SubscriptionPlan
- id* (integer) [read-only]
- name* (string) [read-only]
- display_name* (string) [read-only]
- price_monthly* (string(decimal)) [read-only]
- credits_per_month* (integer) [read-only]
- max_projects* (integer?) [read-only]
- max_keywords* (integer?) [read-only]
- max_team_members* (integer) [read-only]
- features* (any) [read-only]
- features_display* (object) [read-only] — Get human-readable feature list.
- is_free* (boolean) [read-only]

### UsageLimits
- credits* (CreditBreakdown)
- projects* (object)
- keywords* (object)
- features* (object)

### UsageLog
- id* (integer) [read-only]
- action_name* (string) [read-only]
- amount* (string(decimal)) [read-only]
- balance_before* (string(decimal)) [read-only]
- balance_after* (string(decimal)) [read-only]
- service* (string) [read-only]
- service_display* (string) [read-only] — Get human-readable service name
- metadata* (any) [read-only]
- created_at* (string(date-time)) [read-only]
