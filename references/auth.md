# SearchVector API — auth

Auto-generated from openapi.yaml — do not treat any endpoint/param not listed here as existing. 24 endpoints.

### POST /api/auth/apple/callback
`auth_apple_callback_create` — Apple Web Callback
Handle Apple Sign in web callback posted by Apple.
- Body: object
- Auth: JWT/Token/Cookie/none
- Returns: 302

### POST /api/auth/apple/ios/
`auth_apple_ios_create` — Apple iOS Login
Authenticate iOS user with Sign in with Apple ID token.
- Body (required): AppleIOSLoginRequest
  - id_token* (string)
  - nonce* (string)
  - user (AppleIOSUserRequest)
- Auth: JWT/Token/Cookie/none
- Returns: 200 | 400 | 401

### GET /api/auth/apple/login/
`auth_apple_login_retrieve` — Start Apple Web Login
Initiate Sign in with Apple web flow by redirecting the browser to Apple.
- Query: next (string) — Frontend dashboard path to redirect to after login. Must start with /dashboard.
- Auth: JWT/Token/Cookie/none
- Returns: 302 | 500

### POST /api/auth/apple/webhooks/notifications/
`auth_apple_webhooks_notifications_create` — Apple Notification Webhook
Handle Apple server-to-server notifications for consent and email forwarding changes.
- Body (required): AppleWebhookNotificationRequest
  - payload* (string)
- Auth: JWT/Token/Cookie/none
- Returns: 200

### POST /api/auth/delete-account/
`auth_delete_account_create` — Request Account Deletion
Schedule account deletion with a 30-day recovery window. Logging in again within 30 days restores the account.
- Body (required): AccountDeletionRequestRequest
  - confirm* (boolean)
  - reason (string)
- Auth: JWT/Token/Cookie
- Returns: 200 AccountDeletionResponse | 400 | 500

### GET /api/auth/google/authorize/
`auth_google_authorize_retrieve` — Get OAuth Authorization URL
Get Google OAuth authorization URL (fallback method when One Tap is not available). Redirects user to Google consent screen.
- Auth: JWT/Token/Cookie/none
- Returns: 200 | 500

### GET /api/auth/google/callback/
`auth_google_callback_retrieve` — OAuth Callback Handler
Handle Google OAuth callback and return JWT tokens. Called by Google after user grants consent.
- Query: code* (string) — OAuth authorization code from Google; state* (string) — CSRF protection state token
- Auth: JWT/Token/Cookie/none
- Returns: 200 | 400 | 401

### POST /api/auth/google/one-tap/
`auth_google_one_tap_create` — Google One Tap Login
Authenticate user via Google One Tap and return JWT tokens. This is the primary authentication method.
- Body: object
  - credential* (string) — Google One Tap JWT credential
- Auth: JWT/Token/Cookie/none
- Returns: 200 | 400 | 401 | 500

### POST /api/auth/logout/
`auth_logout_create` — Logout User
Logout user by blacklisting the refresh token. Requires authentication via access token.
- Body: object
  - refresh* (string) — JWT refresh token to blacklist
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 401

### POST /api/auth/token/refresh/
`auth_token_refresh_create`
Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.
- Body (required): TokenRefreshRequest
  - refresh* (string)
- Auth: JWT/Token
- Returns: 200 TokenRefresh

### POST /api/integrations/oauth/gsc/native/
`integrations_oauth_gsc_native_create` — Native Google Sign-In for GSC (Mobile)
Exchange a serverAuthCode from native Google Sign-In on mobile for OAuth tokens. Saves GSC token to the user account. Use this instead of the browser-based OAuth flow for mobile apps.
- Body: object
  - server_auth_code* (string) — serverAuthCode received from native Google Sign-In on mobile
- Auth: JWT/Token/Cookie
- Returns: 200 | 201 | 400 | 500

### GET /api/integrations/oauth/{service}/authorize/
`integrations_oauth_authorize_retrieve` — Get Service OAuth Authorization URL
Get OAuth authorization URL for connecting a service (GSC, Google Ads, YouTube, GMB, GA4, or Apple Search Ads). User can use different accounts for each service. Requires authentication.
- Path: service* (enum(apple_search_ads|ga4|gmb|google_ads|gsc|youtube)) — Service name: gsc, google_ads, youtube, gmb, ga4, or apple_search_ads
- Query: next (string) — Web URL to redirect after OAuth (web flow only).; redirect_uri (string) — Mobile deep link URI for callback (e.g. searchvector://oauth-callback). Must be in the se…
- Auth: JWT/Token/Cookie
- Returns: 200 | 400 | 401 | 409 | 500

### GET /api/integrations/oauth/{service}/callback
`integrations_oauth_callback_no_slash_retrieve` — Service OAuth Callback Handler
No-slash OAuth callback route for providers that require it.
- Path: service* (string)
- Auth: JWT/Token/Cookie/none
- Returns: 200 | 400 | 401

### GET /api/integrations/oauth/{service}/callback/
`integrations_oauth_callback_retrieve` — Service OAuth Callback Handler
Handle OAuth callback and save service tokens. Called by Google after user grants service-specific permissions. Requires authentication.
- Path: service* (enum(apple_search_ads|gmb|google_ads|gsc|youtube)) — Service name: gsc, google_ads, youtube, or gmb
- Query: code* (string) — OAuth authorization code from Google/Apple; state* (string) — CSRF protection state token
- Auth: JWT/Token/Cookie/none
- Returns: 200 | 400 | 401

### POST /api/integrations/oauth/{service}/disconnect/
`integrations_oauth_disconnect_create` — Disconnect Service Account
Disconnect a specific Google account from a service and revoke Google tokens. Removes service connection and invalidates tokens. Requires authentication.
- Path: service* (enum(apple_search_ads|gmb|google_ads|gsc|youtube)) — Service name: gsc, google_ads, youtube, or gmb
- Body (required): DisconnectAccountRequest
  - account_id* (integer) — ID of the ServiceOAuthToken to disconnect (get from /api/integrations/oauth/status/)
- Auth: JWT/Token/Cookie
- Returns: 200 object | 400 | 401 | 404

### POST /api/integrations/oauth/{service}/native/
`integrations_oauth_native_create` — Native Google Sign-In for Service OAuth
Exchange a serverAuthCode from native Google Sign-In on mobile for OAuth tokens and save them for GA4, Google Ads, or YouTube. This endpoint is for mobile/native flows only and does not change the browser OAuth flow.
- Path: service* (enum(ga4|google_ads|youtube)) — Supported services: ga4, google_ads, youtube
- Body: object
  - server_auth_code* (string) — serverAuthCode received from native Google Sign-In on mobile
- Auth: JWT/Token/Cookie
- Returns: 200 | 201 | 400 | 500

### GET /api/integrations/status/
`integrations_status_retrieve` — Get All Services Status
Get connection status for all services (GSC, Google Ads, YouTube, GMB, GA4, Apple Search Ads). Shows which services are connected and lists all connected accounts per service. Supports multiple accounts per service. Req…
- Auth: JWT/Token/Cookie
- Returns: 200 | 401

### POST /api/uac/ad-copies/generate/
`uac_ad_copies_generate_create` — Generate UAC ad copy variations
Generate 3 variants of ad copies (5 headlines + 5 descriptions each) using AI based on app details and product brief.
- Body (required): GenerateAdCopiesRequestRequest
  - app_id* (string) — App package ID (e.g., com.example.app)
  - product_brief* (string) — Product description/brief for ad copy generation
  - app_metadata (object) — Optional app metadata from validate API
- Auth: JWT/Token/Cookie
- Returns: 200 GenerateAdCopiesResponse

### GET /api/user/api-key/
`user_api_key_retrieve` — Get API Key
Get permanent API key for the authenticated user. Use this key for external API integrations.
- Auth: JWT/Token/Cookie
- Returns: 200 | 401

### POST /api/user/api-key/regenerate/
`user_api_key_regenerate_create` — Regenerate API Key
Delete existing API key and generate a new one. Old key will stop working immediately.
- Auth: JWT/Token/Cookie
- Returns: 200 | 401

### GET /api/user/extensions/
`user_extensions_retrieve` — List Extensions
Get all available extensions with user's activation status.
- Auth: JWT/Token/Cookie
- Returns: 200

### POST /api/user/mobile-feedback/
`user_mobile_feedback_create` — Submit mobile feedback
Submit mobile app feedback for the authenticated user. The backend stores the authenticated user ID and email; optional user_id/email in the payload must match the authenticated user.
- Body (required): MobileAppFeedbackRequestRequest
  - rating* (integer) — Rating value from 1 to 5
  - feedback_text (string) — Optional feedback text
  - platform* (string) — Mobile app platform: ios or android
  - timestamp (string(date-time)) — Timestamp from the mobile app. If omitted, server time is used.
  - user_id (integer) — Optional authenticated user ID for client-side traceability
  - email (string(email)) — Optional authenticated user email for client-side traceability
- Auth: JWT/Token/Cookie
- Returns: 201 MobileAppFeedbackResponse | 400 | 401 | 500

### GET /api/user/profile/
`user_profile_retrieve` — Get User Profile
Get complete user profile with credits, integrations, stats, and subscription info.
- Auth: JWT/Token/Cookie
- Returns: 200 ProfileResponse

### POST /api/user/validate-token/
`user_validate_token_create` — Validate API Token & Manage Extension Lifecycle
Validate API token and manage extension lifecycle with 3 event types: **event='install'**: Activate or reactivate the extension **event='validation'**: Refresh last active timestamp (only if extension is active) **event…
- Body: object
  - token (string) — API token to validate
  - extension_name (string) — Extension display name (e.g., ASO Chrome Extension)
  - extension_key (string) — Extension unique identifier (e.g., aso_chrome_extension)
  - event (enum(install|validation|inactive)) — Event type: install, validation, inactive (must be explicitly provided)
  - reason (string) — Deactivation reason (required for event='inactive')
- Auth: JWT/Token/none
- Returns: 200 | 400 | 401

## Response schemas

### AccountDeletionResponse
- detail* (string)
- deleted_at* (string(date-time))
- deletion_deadline* (string(date-time))

### GenerateAdCopiesResponse
- variants* (array<AdCopyVariant>) — 3 ad copy variants

### MobileAppFeedbackResponse
- success* (boolean)
- feedback_id* (integer)
- user_id* (integer)
- email* (string(email))
- rating* (integer)
- platform* (string)
- timestamp* (string(date-time))
- created_at* (string(date-time))

### ProfileResponse
- user* (ProfileUser)
- credits* (ProfileCredits)
- connected_integrations* (ProfileIntegrations)
- stats* (ProfileStats)
- subscription* (ProfileSubscription)

### TokenRefresh
- access* (string) [read-only]
- refresh* (string)
