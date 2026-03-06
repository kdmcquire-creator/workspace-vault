# AI Productivity Hub - Parity + CMS + Automations (7-12 days)

## Goal
Replace the current aiproductivityhub.co implementation with the newly bootstrapped Next.js App Router repo, while preserving the existing public experience (parity), and adding:
- A CMS so content updates don’t require code changes
- Automations to keep tool listings, links, and content ops fresh with minimal manual effort

## Assumptions (I’ll validate as we go)
- Current site is a public directory + reviews/blog (no user accounts required for visitors)
- Existing routes include at least: / (home), /tools, /blog, /affiliate-disclosure (or similar)
- The “populated” content is either stored somewhere (CMS/spreadsheet/db) or embedded in the current codebase

## Deliverables
1) Parity rebuild in new Next.js repo
- Home page: hero + primary CTAs + category browse grid
- Tools directory page with filters (category, pricing, etc. as applicable)
- Tool detail pages (if present today)
- Blog index + blog post pages
- Affiliate disclosure page
- Shared components: header/nav/footer, SEO metadata, OG images, basic analytics hooks

2) CMS
- Content models for Tools, Categories, Blog Posts, Pages (Affiliate disclosure)
- Admin/editor UX with preview support
- Draft/publish flow
- Image hosting + optimization strategy

3) Automations
- Scheduled data hygiene jobs (broken links, missing images, stale listings)
- Ingestion helpers (import tools/categories from a spreadsheet/CSV/Airtable/Notion)
- Editorial helpers (reminders, “stale review” flags, queue of items to update)

4) Migration + SEO safety
- URL parity or redirect map
- Sitemap + robots.txt
- Canonical URLs, meta titles/descriptions, OpenGraph
- Basic performance pass (LCP/CLS)

## Recommended stack (fast, flexible, low-maintenance)
### Option A (recommended): Sanity CMS + Next.js
Pros: great editor UX, fast to ship, strong preview tooling, easy schemas, hosted.
Cons: hosted vendor dependency.

### Option B: Payload CMS (self-host) + Next.js
Pros: keep everything in one repo, full control, good TS alignment.
Cons: more DevOps/maintenance.

### Option C: Contentful/Prismic
Pros: polished, stable.
Cons: more rigid, costs scale.

## Proposed content model (minimal but extensible)
- Category
  - name, slug, description, icon
- Tool
  - name, slug, tagline
  - categories (many)
  - pricingModel (free/trial/subscription/one-time)
  - startingPrice (optional)
  - affiliateUrl (optional)
  - websiteUrl
  - shortDescription, longDescription
  - pros/cons (optional)
  - screenshots (optional)
  - lastReviewedAt, reviewStatus
- BlogPost
  - title, slug, excerpt, body, coverImage, publishedAt, author
- Page
  - title, slug, body (used for affiliate disclosure and other legal pages)

## Automations (what I’ll implement)
### 1) Tool import pipeline
- Source: CSV/Google Sheet/Airtable/Notion (we’ll pick one)
- Scheduled sync (daily) that:
  - upserts tools by slug
  - validates required fields
  - flags missing affiliateUrl/websiteUrl

### 2) Link + health checker
- Nightly crawl of tool websiteUrl + affiliateUrl
- Flag non-200s, long response times, redirect chains
- Write results back into CMS fields (status, lastCheckedAt, error)

### 3) Stale content queue
- Weekly job that:
  - finds tools not reviewed in N days
  - generates an “update queue” list
  - optionally emails/slacks a digest

### 4) Lightweight SEO ops
- Auto-regenerate sitemap on publish
- Auto-generate OG images for blog/tool pages (template-based)

## Execution plan by day (7-12 days)
Day 1: Inventory current site + route map + data sources + parity acceptance criteria
Day 2-3: Build parity pages + shared UI + SEO metadata scaffolding
Day 4-6: Add CMS, schemas, preview, migrate initial content
Day 7-9: Automations (import, link checker, stale queue) + dashboards in CMS
Day 10-12: Redirects + sitemap/robots + performance + final QA + domain cutover

## What I need from you (only the essentials)
1) CMS choice (Sanity vs Payload vs Contentful/Prismic)
2) Content source for import (Sheet vs Airtable vs Notion vs “scrape then curate”)
3) Where you want automation notifications (email only vs Slack)

## Acceptance criteria (parity)
- Home, Tools, Blog, Affiliate Disclosure match the current visible structure and core UX
- No major SEO regressions (titles, canonicals, sitemap, redirects)
- CMS edits can publish content without code changes
- Automations run on schedule and write results somewhere you can see (CMS dashboard + optional digest)
