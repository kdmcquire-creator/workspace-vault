# AI Productivity Hub - Parity Checklist (live site map)

## Purpose
This checklist defines what the rebuilt Next.js site must match (or safely improve) when we replace the current production implementation.

## Canonical host + URL conventions
- Primary host: https://aiproductivityhub.co
- Enforce trailing slash on key directory routes:
  - /tools -> 301 -> /tools/
  - /blog -> 301 -> /blog/
- Keep canonical on homepage: https://aiproductivityhub.co (no trailing slash)

## Routes (must exist)
### Core public routes
- / (Homepage)
- /tools/ (Tools directory)
- /tools/[toolSlug] (Tool detail pages)
- /blog/ (Blog index)
- /blog/[postSlug] (Blog post pages)

### “Go” redirect routes
- /go/[goSlug] (Outbound redirect/affiliate bridge)
  - Must resolve quickly
  - Must allow measuring clicks (server-side)
  - Must 301/302 to destination depending on SEO policy

### Static/company routes
- /about/
- /contact/

### Author routes
- /author/[authorSlug]/

### Legal routes (must exist)
- /affiliate-disclosure/
- /disclaimer/
- /privacy/
- /privacy-policy/
- /terms/

## Legacy/duplicate slugs (must not break)
These currently return 200. In the rebuild, either:
A) Keep them as real pages (content parity), or
B) 301 redirect them to the canonical equivalent.

- /affiliate-disclosure-2/ -> 301 -> /affiliate-disclosure/
- /disclaimer-2/ -> 301 -> /disclaimer/
- /privacy-policy-2/ -> 301 -> /privacy-policy/
- /terms-2/ -> 301 -> /terms/

(Decision: default to 301 redirects unless the content differs materially.)

## SEO infrastructure (must exist)
- /robots.txt (200 text/plain)
- /sitemap.xml (200 application/xml)
- /sitemap_index.xml (200 text/xml)
- /post-sitemap.xml (200 text/xml)
- /page-sitemap.xml (200 text/xml)

## Homepage template parity
Homepage should include:
- H1: “Find the Best AI Tools for Your Productivity” (or extremely close)
- Hero copy describing discovery/comparison/reviews
- CTAs:
  - Browse All Tools -> /tools/
  - Read Reviews -> /blog/ (or best equivalent)
- “Explore by Category” section:
  - Categories shown (at minimum): Writing, Design, Marketing, Development, Project Management, Research, Video Editing, Customer Support, Audio, Meeting Assistants, Code
  - Each category card must link to a filtered tools view (either a category page or /tools/?category=...)
- “Featured AI Tools” section:
  - Tool cards with: name, pricing label, short description, category tag, “View Details” link

## Tools directory template parity (/tools/)
- Must list tools (cards or rows) with:
  - Name, pricing label, short description, category badge
  - Link to /tools/[slug]
- Must support browsing by category (UI)
- Nice-to-have: search box and filters (pricingModel, use-case)

## Tool detail template parity (/tools/[slug])
Must support:
- Title + short tagline
- Category badges
- Pricing model (free/freemium/paid/trial/etc.)
- Primary outbound CTA (affiliate link if present)
- Secondary outbound CTA (official website)
- Review/content blocks
- “Related tools” (category-based)

## Blog index template parity (/blog/)
- List posts with title, excerpt, date, author
- Category/tag filtering is optional (but recommended)

## Blog post template parity (/blog/[slug])
- Title, date, author attribution
- Affiliate disclosure snippet at top (if present today)
- Content body
- “Tools Mentioned in This Article” block:
  - Pulls tool cards (name, pricing, short description, link to tool detail)

## Author page parity (/author/[slug]/)
- Author name + bio (if available)
- List of posts by that author

## Legal page parity
- Content should be present and readable for:
  - affiliate disclosure
  - disclaimer
  - privacy
  - privacy-policy
  - terms

## Redirect rules (must implement)
- Trailing slash normalization:
  - /tools -> /tools/
  - /blog -> /blog/
- Legacy -2 pages -> canonical page (301):
  - /affiliate-disclosure-2/ -> /affiliate-disclosure/
  - /disclaimer-2/ -> /disclaimer/
  - /privacy-policy-2/ -> /privacy-policy/
  - /terms-2/ -> /terms/
- Keep any existing /go/* slugs stable (no slug changes)

## Metadata parity (minimum)
- Homepage:
  - <title> matches current value (or improved without changing intent)
  - meta description present
  - canonical present
  - og:title and og:description present
- Tools + Blog pages:
  - unique titles
  - canonical URLs
  - OpenGraph/Twitter cards (template-based)

## Analytics + monetization safety
- Outbound click tracking for affiliate links and /go/*
- Noindex policy: do NOT accidentally noindex core pages
- Ensure disclosures appear where required
