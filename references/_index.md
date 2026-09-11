# Endpoint index — METHOD path → reference file

GET /api/activity-logs/indexing/ → gsc-indexing.md — List indexing activity logs
GET /api/activity-logs/indexing/{id}/ → gsc-indexing.md — Get indexing activity log
POST /api/ai/generate-seo-meta/ → ai-tools.md — Generate SEO titles/meta descriptions
GET /api/ai/prompts/ → misc.md — List all AI prompts with variables
POST /api/apple-ads/bulk/ → apple-ads.md — Apple Ads Bulk
POST /api/apple-ads/read/ → apple-ads.md — Apple Ads Read
POST /api/apple-ads/report/ → apple-ads.md — Apple Ads Report
POST /api/apple-ads/write/ → apple-ads.md — Apple Ads Write
GET /api/apps/search/ → ai-tools.md — Search apps
GET /api/apps/validate/ → ai-tools.md — Validate app
GET /api/article-settings/ → content.md — Get user article settings
PUT /api/article-settings/ → content.md — Update user article settings
GET /api/articles/ → content.md — List articles
POST /api/articles/ → content.md — Create article
POST /api/articles/extract/ → ai-tools.md — Article Extraction from URLs
POST /api/articles/generate-outline/ → content.md — Generate outline variations (single or bulk)
POST /api/articles/generate-title-meta/ → content.md — Generate title and meta options (single or bulk)
GET /api/articles/snapshot/ → ai-tools.md — List article snapshots
POST /api/articles/{article_id}/generate-image/ → content.md — Generate featured image for article
POST /api/articles/{article_id}/retry/ → content.md — Retry article generation
POST /api/articles/{article_id}/rewrite/ → content.md — AI rewrite selected text
POST /api/articles/{article_id}/select-featured-image/ → content.md — Select featured image from generated images
POST /api/articles/{article_id}/status/ → content.md — Update article status
DELETE /api/articles/{id}/ → content.md — Delete article
GET /api/articles/{id}/ → content.md — Get article details
PATCH /api/articles/{id}/ → content.md — Update article
POST /api/auth/apple/callback → auth.md — Apple Web Callback
POST /api/auth/apple/ios/ → auth.md — Apple iOS Login
GET /api/auth/apple/login/ → auth.md — Start Apple Web Login
POST /api/auth/apple/webhooks/notifications/ → auth.md — Apple Notification Webhook
POST /api/auth/delete-account/ → auth.md — Request Account Deletion
GET /api/auth/google/authorize/ → auth.md — Get OAuth Authorization URL
GET /api/auth/google/callback/ → auth.md — OAuth Callback Handler
POST /api/auth/google/one-tap/ → auth.md — Google One Tap Login
POST /api/auth/logout/ → auth.md — Logout User
POST /api/auth/token/refresh/ → auth.md — 
GET /api/automations/alert-groups/ → automations.md — List alert groups
POST /api/automations/alert-groups/ → automations.md — Create alert group
DELETE /api/automations/alert-groups/{group_id}/ → automations.md — Delete alert group
PATCH /api/automations/alert-groups/{group_id}/ → automations.md — Update alert group
GET /api/automations/combined-alerts/ → automations.md — Get combined alert state
PATCH /api/automations/combined-alerts/ → automations.md — Get combined alert state
GET /api/automations/eligible-targets/ → automations.md — List eligible automation targets
GET /api/automations/global-state/ → automations.md — Get global automation state
POST /api/automations/global-state/ → automations.md — Set global automation state
GET /api/automations/project-alerts/ → automations.md — List project alert states
PATCH /api/automations/project-alerts/ → automations.md — Toggle project alert
GET /api/automations/rules/ → automations.md — List automation rules
POST /api/automations/rules/ → automations.md — Create automation rule
DELETE /api/automations/rules/{id}/ → automations.md — Delete automation rule
GET /api/automations/rules/{id}/ → automations.md — Get automation rule
PATCH /api/automations/rules/{id}/ → automations.md — Update automation rule
GET /api/automations/types/ → automations.md — List automation types
POST /api/billing/checkout/ → billing.md — 
GET /api/billing/credits/history/ → billing.md — 
GET /api/billing/credits/packs/ → billing.md — 
POST /api/billing/credits/purchase/ → billing.md — 
GET /api/billing/plans/ → billing.md — 
POST /api/billing/portal/ → billing.md — 
GET /api/billing/status/ → billing.md — 
GET /api/billing/usage/ → billing.md — 
GET /api/changelog/ → misc.md — List accessible changelog rows
GET /api/content-calendar/ → content.md — List accessible content calendar rows
GET /api/credits/actions/ → billing.md — List Available Actions
GET /api/credits/balance/ → billing.md — Get Credit Balance
POST /api/credits/estimate/ → billing.md — Estimate Cost
GET /api/credits/history/ → billing.md — Get Usage History
POST /api/dashboard/cwv/ → analytics.md — Get dashboard CWV data
GET /api/dashboard/gsc-sitemap/ → analytics.md — Get dashboard GSC sitemap data
GET /api/dashboard/gsc/ → analytics.md — Get dashboard GSC data
POST /api/dashboard/organic-competitor/ → analytics.md — Get dashboard organic competitor data
POST /api/dashboard/organic-keywords/ → analytics.md — Get dashboard organic keywords
POST /api/dashboard/sitemap/ → analytics.md — Get dashboard sitemap data
POST /api/dashboard/social-competitor/ → analytics.md — Get dashboard social competitor data
POST /api/integrations/oauth/gsc/native/ → auth.md — Native Google Sign-In for GSC (Mobile)
GET /api/integrations/oauth/{service}/authorize/ → auth.md — Get Service OAuth Authorization URL
GET /api/integrations/oauth/{service}/callback → auth.md — Service OAuth Callback Handler
GET /api/integrations/oauth/{service}/callback/ → auth.md — Service OAuth Callback Handler
POST /api/integrations/oauth/{service}/disconnect/ → auth.md — Disconnect Service Account
POST /api/integrations/oauth/{service}/native/ → auth.md — Native Google Sign-In for Service OAuth
GET /api/integrations/status/ → auth.md — Get All Services Status
GET /api/invitations/ → projects.md — Get my pending invitations (all projects)
POST /api/invitations/accept/ → projects.md — Accept invitation
POST /api/invitations/reject/ → projects.md — Reject invitation
POST /api/keyword-content-score/ → ai-tools.md — Calculate keyword content scores
GET /api/notifications/ → misc.md — Get all notifications
POST /api/notifications/mark-all-read/ → misc.md — Mark all as read
GET /api/notifications/unread-count/ → misc.md — Get unread count
DELETE /api/notifications/{notification_id}/ → misc.md — Delete notification
POST /api/notifications/{notification_id}/mark-read/ → misc.md — Mark notification as read
GET /api/projects/ → projects.md — List user's projects
POST /api/projects/ → projects.md — Create a new project
GET /api/projects/fetch-brand-regex/ → projects.md — Fetch brand regex for project URL
DELETE /api/projects/{id}/ → projects.md — Delete project
GET /api/projects/{id}/ → projects.md — Get project details
PATCH /api/projects/{id}/ → projects.md — Partially update project
PUT /api/projects/{id}/ → projects.md — Update project
GET /api/projects/{id}/available_properties/ → projects.md — Get available GSC properties for an OAuth token
POST /api/projects/{id}/confirm-unlock/ → projects.md — Confirm unlock with selected members
POST /api/projects/{id}/unlock/ → projects.md — Unlock a project
POST /api/projects/{project_id}/ai/fetch-page/ → ai-tools.md — Fetch page details
POST /api/projects/{project_id}/ai/generate-titles/ → ai-tools.md — Generate SEO titles
POST /api/projects/{project_id}/ai/generate-titles/bulk/ → ai-tools.md — Bulk generate SEO titles
GET /api/projects/{project_id}/experiments/ → ai-tools.md — List experiments
POST /api/projects/{project_id}/experiments/ → ai-tools.md — Create experiment
POST /api/projects/{project_id}/experiments/bulk-action/ → ai-tools.md — Bulk action on experiments
POST /api/projects/{project_id}/experiments/bulk-create/ → ai-tools.md — Bulk create experiments
DELETE /api/projects/{project_id}/experiments/{experiment_id}/ → ai-tools.md — Delete experiment
GET /api/projects/{project_id}/experiments/{experiment_id}/ → ai-tools.md — Get experiment details
PUT /api/projects/{project_id}/experiments/{experiment_id}/ → ai-tools.md — Update experiment
POST /api/projects/{project_id}/experiments/{experiment_id}/apply-winner/ → ai-tools.md — Apply winner to WordPress
POST /api/projects/{project_id}/experiments/{experiment_id}/cancel/ → ai-tools.md — Cancel experiment
POST /api/projects/{project_id}/experiments/{experiment_id}/complete/ → ai-tools.md — Complete experiment
GET /api/projects/{project_id}/experiments/{experiment_id}/logs/ → ai-tools.md — Get experiment logs
POST /api/projects/{project_id}/experiments/{experiment_id}/pause/ → ai-tools.md — Pause experiment
GET /api/projects/{project_id}/experiments/{experiment_id}/performance-report/ → ai-tools.md — Get experiment performance report
POST /api/projects/{project_id}/experiments/{experiment_id}/reorder-pending-variants/ → ai-tools.md — Reorder pending variants
GET /api/projects/{project_id}/experiments/{experiment_id}/results/ → ai-tools.md — Get experiment results
POST /api/projects/{project_id}/experiments/{experiment_id}/resume/ → ai-tools.md — Resume experiment
POST /api/projects/{project_id}/experiments/{experiment_id}/revoke-cancel/ → ai-tools.md — Revoke cancelled experiment
POST /api/projects/{project_id}/experiments/{experiment_id}/schedule/ → ai-tools.md — Schedule/Start experiment
POST /api/projects/{project_id}/experiments/{experiment_id}/variants/{variant_id}/resume/ → ai-tools.md — Resume a skipped variant
POST /api/projects/{project_id}/experiments/{experiment_id}/variants/{variant_id}/skip/ → ai-tools.md — Skip a variant
POST /api/projects/{project_id}/gsc/breakdown/ → gsc-indexing.md — GSC Breakdown with Filtering
GET /api/projects/{project_id}/gsc/charts/ → gsc-indexing.md — Get GSC Charts Data
GET /api/projects/{project_id}/gsc/countries/ → gsc-indexing.md — Get GSC Countries List
POST /api/projects/{project_id}/gsc/custom-query/ → gsc-indexing.md — GSC Custom Query (Raw Pass-through)
GET /api/projects/{project_id}/gsc/keywords/ → gsc-indexing.md — Get GSC Keywords Insights
POST /api/projects/{project_id}/gsc/mapping/ → gsc-indexing.md — Map Keywords and URLs to GSC Data
GET /api/projects/{project_id}/gsc/overview/ → gsc-indexing.md — Get GSC Overview Stats
POST /api/projects/{project_id}/gsc/page-query-breakdown/ → gsc-indexing.md — GSC Breakdown by Dimensions
GET /api/projects/{project_id}/gsc/pages/ → gsc-indexing.md — Get GSC Pages Insights
GET /api/projects/{project_id}/gsc/performance/ → gsc-indexing.md — Get GSC Performance Insights
POST /api/projects/{project_id}/gsc/urls/ → gsc-indexing.md — Filter GSC URLs
POST /api/projects/{project_id}/wordpress/fetch-post-ids/ → cms.md — Fetch WordPress post IDs
GET /api/projects/{project_id}/wordpress/fetch-urls/ → cms.md — Fetch all WordPress URLs
GET /api/projects/{project_pk}/changelog/ → misc.md — List changelog rows
POST /api/projects/{project_pk}/changelog/ → misc.md — Create changelog row
DELETE /api/projects/{project_pk}/changelog/{id}/ → misc.md — Delete changelog row
GET /api/projects/{project_pk}/changelog/{id}/ → misc.md — Get changelog row
PATCH /api/projects/{project_pk}/changelog/{id}/ → misc.md — Partially update changelog row
PUT /api/projects/{project_pk}/changelog/{id}/ → misc.md — Update changelog row
GET /api/projects/{project_pk}/content-calendar/ → content.md — List content calendar rows
POST /api/projects/{project_pk}/content-calendar/ → content.md — Create content calendar row
DELETE /api/projects/{project_pk}/content-calendar/{id}/ → content.md — Delete content calendar row
GET /api/projects/{project_pk}/content-calendar/{id}/ → content.md — Get content calendar row
PATCH /api/projects/{project_pk}/content-calendar/{id}/ → content.md — Partially update content calendar row
PUT /api/projects/{project_pk}/content-calendar/{id}/ → content.md — Update content calendar row
GET /api/projects/{project_pk}/integrations/ → projects.md — List project integrations
POST /api/projects/{project_pk}/integrations/ → projects.md — Create project integration
POST /api/projects/{project_pk}/integrations/add/ → projects.md — Add integration to project
DELETE /api/projects/{project_pk}/integrations/{id}/ → projects.md — Remove integration
GET /api/projects/{project_pk}/integrations/{id}/ → projects.md — Get integration details
PATCH /api/projects/{project_pk}/integrations/{id}/ → projects.md — Partially update integration
PUT /api/projects/{project_pk}/integrations/{id}/ → projects.md — Update integration
GET /api/projects/{project_pk}/members/ → projects.md — List project members and invitations
POST /api/projects/{project_pk}/members/ → projects.md — Add/invite members to project (Google Sheets style)
DELETE /api/projects/{project_pk}/members/{id}/ → projects.md — Remove member or cancel invitation
GET /api/projects/{project_pk}/members/{id}/ → projects.md — Get project member details
PATCH /api/projects/{project_pk}/members/{id}/ → projects.md — Update member role
POST /api/projects/{project_pk}/members/{id}/resend_invitation/ → projects.md — Resend invitation email
GET /api/projects/{project_pk}/seo-tasks/ → seo-tasks.md — List SEO tasks
POST /api/projects/{project_pk}/seo-tasks/ → seo-tasks.md — Create SEO task
GET /api/projects/{project_pk}/seo-tasks/assignees/ → seo-tasks.md — List SEO task assignees
DELETE /api/projects/{project_pk}/seo-tasks/{id}/ → seo-tasks.md — Archive SEO task
GET /api/projects/{project_pk}/seo-tasks/{id}/ → seo-tasks.md — Get SEO task
PATCH /api/projects/{project_pk}/seo-tasks/{id}/ → seo-tasks.md — Partially update SEO task
PUT /api/projects/{project_pk}/seo-tasks/{id}/ → seo-tasks.md — Update SEO task
POST /api/projects/{project_pk}/seo-tasks/{id}/status/ → seo-tasks.md — Change SEO task status
GET /api/projects/{project_pk}/seo-tasks/{id}/subtasks/ → seo-tasks.md — List SEO task subtasks
POST /api/projects/{project_pk}/seo-tasks/{id}/subtasks/ → seo-tasks.md — Create SEO task subtask
DELETE /api/projects/{project_pk}/seo-tasks/{id}/subtasks/{subtask_pk}/ → seo-tasks.md — Delete SEO task subtask
PATCH /api/projects/{project_pk}/seo-tasks/{id}/subtasks/{subtask_pk}/ → seo-tasks.md — Update SEO task subtask
GET /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/ → seo-tasks.md — List SEO task comments
POST /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/ → seo-tasks.md — Post an SEO task comment
DELETE /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/{id}/ → seo-tasks.md — Delete your comment
PATCH /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/{id}/ → seo-tasks.md — Edit your comment
DELETE /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/{id}/reactions/{emoji}/ → seo-tasks.md — Add or remove a reaction
PUT /api/projects/{project_pk}/seo-tasks/{seo_task_pk}/comments/{id}/reactions/{emoji}/ → seo-tasks.md — Add or remove a reaction
GET /api/rank-tracker/competitors/ → seo-tools.md — List or create project competitors
POST /api/rank-tracker/competitors/ → seo-tools.md — List or create project competitors
DELETE /api/rank-tracker/competitors/{competitor_id}/ → seo-tools.md — Delete a project competitor
POST /api/rank-tracker/keyword-score/ → seo-tools.md — Calculate keyword difficulty scores from stored SERP data
DELETE /api/rank-tracker/keywords/ → seo-tools.md — List, create, or bulk delete project keywords
GET /api/rank-tracker/keywords/ → seo-tools.md — List, create, or bulk delete project keywords
POST /api/rank-tracker/keywords/ → seo-tools.md — List, create, or bulk delete project keywords
POST /api/rank-tracker/serp/fetch/ → seo-tools.md — Fetch Google SERP and store top ranks (single or bulk)
GET /api/rank-tracker/serp/top10/ → seo-tools.md — SERP top 10 payload for keyword popup
GET /api/rank-tracker/views/competitor/ → seo-tools.md — Competitor table payload for selected project
GET /api/rank-tracker/views/daywise/ → seo-tools.md — Day-wise snapshot payload for selected project
GET /api/seo-tasks/ → seo-tasks.md — List accessible SEO tasks
GET /api/seo-tasks/meta/ → seo-tasks.md — Get SEO task metadata
POST /api/tools/ch/stats/ → analytics.md — Fetch Data for an Analytics Report
POST /api/tools/citations/ → ai-tools.md — Get citation sources
POST /api/tools/competitor-domains/ → seo-tools.md — Find top competitor domains based on keyword overlap (Jacca…
POST /api/tools/competitor-keywords/ → seo-tools.md — Compare keywords across websites
GET /api/tools/ga4/accessible-properties/ → analytics.md — Get accessible GA4 properties
POST /api/tools/ga4/custom-report/ → analytics.md — Run custom GA4 report
GET /api/tools/ga4/metadata/{propertyId}/ → analytics.md — Get GA4 property metadata
GET /api/tools/ga4/properties/ → analytics.md — List connected GA4 properties
POST /api/tools/ga4/properties/connect/ → analytics.md — Connect Selected GA4 Properties
DELETE /api/tools/ga4/properties/{id}/ → analytics.md — Disconnect GA4 Property
POST /api/tools/ga4/realtime/ → analytics.md — GA4 Realtime report
POST /api/tools/ga4/report/ → analytics.md — Run GA4 report
GET /api/tools/gmb/accessible-accounts/ → gmb.md — List accessible GMB accounts
GET /api/tools/gmb/accounts/ → gmb.md — List connected GMB accounts
POST /api/tools/gmb/accounts/connect/ → gmb.md — Connect GMB accounts
DELETE /api/tools/gmb/accounts/{account_id}/ → gmb.md — Disconnect GMB account
POST /api/tools/gmb/location/insights/ → gmb.md — Get GMB location insights
GET /api/tools/gmb/locations/ → gmb.md — List GMB locations
POST /api/tools/gmb/reviews/ai-generate-replies/ → gmb.md — Generate AI replies for reviews
POST /api/tools/gmb/reviews/batch/ → gmb.md — Batch fetch GMB reviews
POST /api/tools/gmb/reviews/list/ → gmb.md — List GMB reviews
POST /api/tools/gmb/reviews/reply/ → gmb.md — Reply to GMB review(s)
GET /api/tools/gmb/templates/ → gmb.md — List GMB reply templates
POST /api/tools/gmb/templates/ → gmb.md — Create GMB reply template
DELETE /api/tools/gmb/templates/{id}/ → gmb.md — Delete GMB reply template
GET /api/tools/gmb/templates/{id}/ → gmb.md — Get GMB reply template
PATCH /api/tools/gmb/templates/{id}/ → gmb.md — Partially update GMB reply template
PUT /api/tools/gmb/templates/{id}/ → gmb.md — Update GMB reply template
GET /api/tools/google-ads/accessible-accounts/ → google-ads.md — List Accessible Google Ads Accounts
GET /api/tools/google-ads/accounts/ → google-ads.md — List Google Ads Accounts
POST /api/tools/google-ads/accounts/connect/ → google-ads.md — Connect Selected Google Ads Accounts
DELETE /api/tools/google-ads/accounts/{id}/ → google-ads.md — Disconnect Google Ads Account
POST /api/tools/google-ads/ad-groups/performance/ → google-ads.md — Ad Group Performance
GET /api/tools/google-ads/campaigns/automation-controls/ → google-ads.md — List Campaign Automation Entries
POST /api/tools/google-ads/campaigns/automation-controls/ → google-ads.md — Create Campaign Automation Entry
POST /api/tools/google-ads/campaigns/performance/ → google-ads.md — Campaign Performance Dashboard
POST /api/tools/google-ads/campaigns/performance/auto-bid-tool/ → google-ads.md — Auto Bid Tool - UAC Campaign Performance
POST /api/tools/google-ads/campaigns/uac/ → google-ads.md — Create UAC Campaign
POST /api/tools/google-ads/change-history/ → google-ads.md — Get Change History
POST /api/tools/google-ads/custom-query/ → google-ads.md — Execute Custom GAQL Query
POST /api/tools/google-ads/gaql-query/ → misc.md — Execute Dynamic GAQL Query
POST /api/tools/google-ads/geo/performance/ → google-ads.md — Geographic Performance
POST /api/tools/google-ads/keyword-ideas/ → google-ads.md — Generate Keyword Ideas
POST /api/tools/google-ads/keyword-ideas/direct/ → misc.md — Generate Keyword Ideas Direct
POST /api/tools/google-ads/keywords/performance/ → google-ads.md — Keyword Performance
GET /api/tools/google-ads/language-search/ → google-ads.md — Search Google Ads languages
GET /api/tools/google-ads/location-search/ → google-ads.md — Search Google Ads locations
GET /api/tools/google-ads/manager-accounts/{manager_id}/children/ → google-ads.md — Get Manager Account Children
POST /api/tools/google-ads/mutate/ → misc.md — Universal Google Ads Mutate
POST /api/tools/google-ads/search-terms/ → google-ads.md — Search Terms Analysis
POST /api/tools/google-ads/search-terms/all/ → google-ads.md — All Search Terms (Account Level)
GET /api/tools/google-indexing/quota/ → gsc-indexing.md — Get Google Indexing API Quota
DELETE /api/tools/google-indexing/service-account/ → gsc-indexing.md — Delete Service Account
GET /api/tools/google-indexing/service-account/ → gsc-indexing.md — Get Service Accounts List
POST /api/tools/google-indexing/service-account/ → gsc-indexing.md — Save Google Service Account
POST /api/tools/google-indexing/submit/ → gsc-indexing.md — Submit URLs to Google Indexing API
POST /api/tools/historical-serp-data/ → misc.md — Get historical SERP data
POST /api/tools/index-inspect/ → seo-tools.md — Inspect URLs for indexing status
POST /api/tools/keyword-research-database/ → misc.md — Search keyword research database
POST /api/tools/metrics/ → seo-tools.md — Get keyword metrics
POST /api/tools/metrics/v2/ → seo-tools.md — Get keyword metrics v2
POST /api/tools/pagespeed/ → seo-tools.md — Analyze URLs with PageSpeed Insights
POST /api/tools/public/keyword-suggestions/ → misc.md — Public Keyword Suggestions
POST /api/tools/public/sitemap/ → misc.md — Public Sitemap Discovery/Parse
POST /api/tools/serp-ranking/ → seo-tools.md — Get SERP ranking data with keyword difficulty scores
POST /api/tools/serp/google/ → seo-tools.md — Google SERP Results
POST /api/tools/site-audit/jobs/ → misc.md — Start site audit
POST /api/tools/site-audit/jobs/{job_id}/cancel/ → misc.md — Cancel site audit
GET /api/tools/site-audit/jobs/{job_id}/results/ → misc.md — Get site audit results
GET /api/tools/site-audit/jobs/{job_id}/status/ → misc.md — Get site audit status
POST /api/tools/sitemap/discover/ → seo-tools.md — Discover sitemap files
POST /api/tools/sitemap/full-parse/ → seo-tools.md — Full sitemap parser
POST /api/tools/sitemap/parse/ → seo-tools.md — Parse sitemap and extract URLs
POST /api/tools/suggestions/ → seo-tools.md — Get bulk keyword suggestions
POST /api/tools/suggestions/v2/ → seo-tools.md — Get keyword suggestions v2
POST /api/tools/title-description/ → seo-tools.md — Get page title and description
POST /api/tools/topic-gap/ → seo-tools.md — Advanced Topic Gap Analysis
GET /api/tools/url-comparison/ → seo-tools.md — List URL comparisons
POST /api/tools/url-comparison/ → seo-tools.md — Create URL comparison
DELETE /api/tools/url-comparison/{id}/ → seo-tools.md — Delete URL comparison
PUT /api/tools/url-comparison/{id}/ → seo-tools.md — Update URL comparison
POST /api/tools/url-keywords/ → seo-tools.md — Get keywords for multiple URLs
POST /api/tools/v1/aio-geo/ → misc.md — Check brand citation
POST /api/tools/v2/aio-geo/ → misc.md — Check AIO GEO citation
GET /api/tools/whatsnew/ → misc.md — Get What's New Announcements
GET /api/tools/youtube-channel-data/ → seo-tools.md — Get channel videos
POST /api/tools/youtube-hashtag/ → seo-tools.md — Get hashtag ideas
GET /api/tools/youtube-video-detail/ → seo-tools.md — Get video details
POST /api/tools/youtube/analytics/ → youtube.md — YouTube Analytics Report
GET /api/tools/youtube/channels/ → youtube.md — List connected YouTube channels
DELETE /api/tools/youtube/channels/delete/ → youtube.md — Delete YouTube channel
POST /api/tools/youtube/comments/ → youtube.md — Fetch YouTube video comments
POST /api/tools/youtube/comments/reply/ → youtube.md — Reply to YouTube comments
GET /api/tools/youtube/fetch-channels/ → youtube.md — Fetch YouTube channels
POST /api/tools/youtube/playlist-videos/ → youtube.md — Fetch playlist videos (lightweight)
POST /api/tools/youtube/playlists/ → youtube.md — Fetch YouTube playlists
POST /api/uac/ad-copies/generate/ → auth.md — Generate UAC ad copy variations
GET /api/user/api-key/ → auth.md — Get API Key
POST /api/user/api-key/regenerate/ → auth.md — Regenerate API Key
POST /api/user/contact-us/ → misc.md — Contact Us Form
GET /api/user/extensions/ → auth.md — List Extensions
POST /api/user/mobile-feedback/ → auth.md — Submit mobile feedback
GET /api/user/profile/ → auth.md — Get User Profile
GET /api/user/user-interest/ → misc.md — Submit user interest
POST /api/user/user-interest/ → misc.md — Submit user interest
POST /api/user/validate-token/ → auth.md — Validate API Token & Manage Extension Lifecycle
GET /api/webflow/auth-url/ → cms.md — OAuth authorization URL
GET /api/webflow/callback/ → cms.md — OAuth callback
POST /api/webflow/callback/ → cms.md — OAuth callback
GET /api/webflow/collections/{collection_id}/ → cms.md — Get collection schema
GET /api/webflow/collections/{collection_id}/items/ → cms.md — List collection items
POST /api/webflow/collections/{collection_id}/items/ → cms.md — List collection items
POST /api/webflow/collections/{collection_id}/items/publish/ → cms.md — Publish items
DELETE /api/webflow/collections/{collection_id}/items/{item_id}/ → cms.md — Update or delete item
PATCH /api/webflow/collections/{collection_id}/items/{item_id}/ → cms.md — Update or delete item
DELETE /api/webflow/disconnect/ → cms.md — Disconnect Webflow
GET /api/webflow/pages/{page_id}/ → cms.md — Get page detail
PUT /api/webflow/pages/{page_id}/ → cms.md — Update page metadata
GET /api/webflow/pages/{page_id}/dom/ → cms.md — Get page content
POST /api/webflow/pages/{page_id}/dom/ → cms.md — Update page content
DELETE /api/webflow/projects/{project_id}/connected-sites/ → cms.md — Disconnect Webflow site from project
GET /api/webflow/projects/{project_id}/connected-sites/ → cms.md — List project connected Webflow site
POST /api/webflow/projects/{project_id}/connected-sites/ → cms.md — Connect Webflow site to project
GET /api/webflow/sites/ → cms.md — List Webflow sites
GET /api/webflow/sites/{site_id}/collections/ → cms.md — List collections
GET /api/webflow/sites/{site_id}/pages/ → cms.md — List site pages
POST /api/webflow/sites/{site_id}/publish/ → cms.md — Publish site
GET /api/webflow/status/ → cms.md — Connection status
GET /api/wordpress/ → cms.md — List WordPress Sites
GET /api/wordpress/categories/{project_id}/ → cms.md — Get WordPress Categories
POST /api/wordpress/connect/ → cms.md — Connect WordPress Site
POST /api/wordpress/manual-title-update/ → cms.md — Manual WordPress title update
GET /api/wordpress/post-types/{project_id}/ → cms.md — Get WordPress Post Types
POST /api/wordpress/posts/create/ → cms.md — Create WordPress Post
PUT /api/wordpress/posts/update/ → cms.md — Update WordPress Post (by body)
GET /api/wordpress/posts/{project_id}/ → cms.md — List WordPress Posts/Pages
GET /api/wordpress/posts/{project_id}/{post_id}/ → cms.md — Get Single WordPress Post
DELETE /api/wordpress/{site_id}/ → cms.md — Disconnect WordPress Site
