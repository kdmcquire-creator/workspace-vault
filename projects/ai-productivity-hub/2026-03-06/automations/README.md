AI Productivity Hub - Automations

What these automations do
1) Google Sheet import (daily or manual)
- Reads your Tool list from a Google Sheet
- Upserts Categories and Tools into Sanity

2) Link health checker (nightly)
- Checks Tool websiteUrl + affiliateUrl and GoLink destinationUrl
- Writes linkStatus, linkError, lastCheckedAt back into Sanity

3) Stale content queue (weekly)
- Finds tools not reviewed recently (or missing lastReviewedAt)
- Generates a markdown report and commits it into workspace-vault under:
  projects/ai-productivity-hub/reports/stale-queue/YYYY-MM-DD.md

Required GitHub Secrets
- SANITY_PROJECT_ID
- SANITY_DATASET
- SANITY_TOKEN

For Google Sheets import (service account)
- GOOGLE_SERVICE_ACCOUNT_JSON  (the full JSON, stored as a secret)
- GOOGLE_SHEET_ID
- GOOGLE_SHEET_RANGE  (example: Tools!A1:Z)

Optional
- SANITY_API_VERSION (default: 2025-01-01)
- STALE_DAYS (default: 90)

Notes
- No secrets are stored in this repo.
- If you prefer a public CSV instead of a service account, we can add that mode later.
