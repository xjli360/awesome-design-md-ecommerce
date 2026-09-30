---
version: alpha
name: "Discotek Media"
source_url: "https://discotekmedia.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A midnight-blue (#091727) digital storefront for a physical-media revivalist, where the warmth of #fffbf0 — a buttery off-white that reads like aged paper stock — offsets the institutional weight of #003399, a deep corporate blue that appears on every product badge and price tag. The site runs Tahoma and Trebuchet MS, two system fonts that feel like they were chosen in the early 2000s and never revisited, which is exactly right for a brand selling DVD and Blu-ray releases of anime and cult films from that era. Navigation is a simple horizontal bar of text links in #091727 on the cream canvas, with no dropdowns or mega-menus — the brand trusts its grid of product thumbnails to do the selling. Product cards sit on {rounded.sm} corners with the cream background, each showing a key visual, title, and price in #003399, creating a consistent blue-accent rhythm across the page. The footer is a dense block of #111111 with white links, a classic dark-bottom layout that anchors the light content above. There is no hero section, no carousel, no search bar — just a straightforward catalog grid and a sidebar of category filters, suggesting a brand that prioritizes browsability over persuasion.

colors:
  primary: "#003399"
  primary-active: "#002266"
  primary-disabled: "#8099cc"
  ink: "#091727"
  body: "#111111"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#fffbf0"
  surface-soft: "#f5f0e0"
  surface-card: "#fffbf0"
  on-primary: "#ffffff"
  footer-bg: "#111111"
  footer-link: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  link:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Tahoma', 'Trebuchet MS', Geneva, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  full: 9999px

spacing:
  xxs: 2px
  xs: 4px
  sm: 8px
  md: 12px
  base: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  sidebar-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px
  sidebar-filter-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-link}"
    typography: "{typography.body-sm}"
    padding: 24px 16px
  footer-link:
    textColor: "{colors.footer-link}"
    typography: "{typography.link}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 4px 8px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in #003399 on white text. Used for "Add to Cart", "Checkout", and "Submit" actions. On hover, shifts to #002266. Disabled state uses #8099cc with white text, indicating the action is unavailable. Corners are slightly softened at {rounded.sm} to avoid feeling too harsh against the cream canvas.

**`button-secondary`** — An outlined or ghost variant on the cream background with #091727 text. Used for "View Details", "Cancel", and secondary form actions. Maintains the same height and padding as the primary button for visual consistency in forms and product listings.

### Cards
**`product-card`** — The core content unit of the Discotek Media storefront. Each card displays a product thumbnail, title in bold #091727, and price in #003399. Cards sit on the cream background with {rounded.sm} corners and 8px padding. The thumbnail fills the top of the card with no border radius on the image itself — only the card container is rounded. A small badge in #003399 may appear in the top-left corner for "New Release" or "Pre-order" labels.

**`product-card-badge`** — A compact label pinned to product cards, using #003399 background with white text in 11px bold. Corners are {rounded.xs} (2px), creating a subtle pill shape that doesn't compete with the card's visual hierarchy.

### Navigation
**`nav-bar`** — A simple horizontal strip at the top of the page, 48px tall, on the cream background. Links are in #091727 bold Tahoma, with no underline or hover effects beyond color shift. The nav includes "HOME", "NEW RELEASES", "CATALOG", "ABOUT", and "CONTACT" — all text links with no dropdowns. Active page is indicated by a slightly darker text or a subtle bottom border.

**`nav-link`** — Individual navigation items with 8px horizontal padding and 8px vertical padding within the nav bar. No background change on hover — the brand relies on text weight and positioning for wayfinding.

### Forms
**`text-input`** — Standard form input fields for search, newsletter signup, and checkout forms. Uses the cream background with #091727 text in 14px. Border is a subtle #cccccc hairline. Focus state would typically show a #003399 border, though this was not confirmed from extraction. Height is 36px to match button heights.

### Footer
**`footer`** — A dense dark block at the bottom of every page, using #111111 background with white text links. Contains copyright information, legal links, and social media icons. Links are 14px white text with no underline. The footer padding is 24px top/bottom and 16px sides, creating a solid visual anchor.

### Sidebar
**`sidebar-filter`** — A category filter panel on catalog pages, using a slightly darker cream (#f5f0e0) background to distinguish it from the main content area. Headings are in bold 16px #091727, filter options in 14px body text. Checkboxes or radio buttons accompany each filter option.

### Breadcrumbs
**`breadcrumb`** — Secondary navigation showing the user's path (e.g., HOME > CATALOG > ANIME). Uses 12px muted gray text with ">" separators. The active (current) page is in #091727 to indicate the user's location.

### Pagination
**`pagination`** — Page navigation at the bottom of catalog listings. Page numbers are 13px muted gray text. The active page gets a #003399 background with white text in a small {rounded.sm} box. Previous/Next links are text-only in muted gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav links collapse to hamburger menu; sidebar filters become a collapsible panel at top; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav remains horizontal but with reduced padding; sidebar filters remain visible but narrower |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all links visible; sidebar filters at full width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px with centered content; no layout changes beyond grid expansion |

### Touch Targets
- All interactive elements (buttons, links, form inputs) maintain a minimum 44px height for touch accessibility
- Nav links have 48px tap targets within the nav bar
- Product card tap targets are the entire card surface, not just the title or price
- Pagination page numbers have 36px tap targets (below recommended 44px — a known gap)

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger icon that reveals a vertical menu overlay
- Sidebar filters collapse to a "Filter" button at the top of the catalog page, opening a slide-in or dropdown panel
- Product grid collapses from 3-4 columns to 2 columns on tablet, then 1 column on mobile
- Footer columns stack vertically on mobile, with each link group becoming a full-width block

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site CSS
- Error styling for form inputs (validation states, error messages) was not observed
- The exact border width and style for text inputs and cards is inferred from common patterns, not confirmed
- No data on modal or overlay styling (if any exist)
- Sub-brand or category-specific color palettes (e.g., anime vs. live-action) were not detected
- Dark mode is not supported and no dark-mode tokens were found
- The font stack uses Tahoma and Trebuchet MS as primary faces; exact fallback order is inferred
- Button hover animations or transitions were not captured
- The site may use a Shopify or other e-commerce platform whose default styling was partially filtered but may still influence some components
- No search bar component was found on the live site — search functionality may be absent or handled externally
- The extracted color list (#fffbf0, #091727, #003399, #111111) is sparse but consistent; no additional accent or secondary colors were found beyond these four
