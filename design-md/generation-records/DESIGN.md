---
version: alpha
name: "Generation Records"
source_url: "https://www.generationrecords.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A black-walled punk cathedral where #f94877 — a hot, almost-fluorescent pink — cuts through the darkness like a stage light, used sparingly on sale badges, add-to-cart buttons, and the occasional header accent. The site runs on a near-monochrome palette of #111111, #222222, #272727, and #1e1e1e for backgrounds and body text, with #fbfbfb and #eeeeee providing the only relief on cards and hover states. League Gothic, a compressed, high-contrast display face, handles category headers and price tags with the same blunt-force impact as a seven-inch single sleeve, while Arial and Helvetica Neue carry product descriptions and navigation in utilitarian weight 400. The grid is tight — product thumbnails sit at {rounded.sm} with minimal padding, and the search bar is a simple outlined rectangle rather than a pill, refusing any of the friendly curves that e-commerce defaults to. Social icons for Facebook (#3b5998), Instagram (#e4405f), Twitter (#55acee), and YouTube (#cc2127) appear as raw brand-color circles in the footer, unsoftened and unapologetic. The overall effect is less "record store website" and more "zine layout from 1994 that happens to have a checkout flow" — a deliberate roughness that signals authenticity over polish.

colors:
  primary: "#f94877"
  primary-active: "#e52d27"
  primary-disabled: "#e99292"
  ink: "#111111"
  body: "#222222"
  muted: "#aaaaaa"
  muted-soft: "#e1e1e1"
  hairline: "#272727"
  hairline-soft: "#1e1e1e"
  canvas: "#040404"
  surface-soft: "#111111"
  surface-card: "#222222"
  on-primary: "#ffffff"
  on-dark: "#fbfbfb"
  facebook: "#3b5998"
  instagram: "#e4405f"
  twitter: "#55acee"
  youtube: "#cc2127"
  bandcamp: "#629aa9"
  discogs: "#333333"
  sale-badge: "#f94877"
  sold-out: "#aaaaaa"
  preorder: "#0099e5"
  vinyl-swatch: "#112233"
  cd-swatch: "#112255"

typography:
  display-xl:
    fontFamily: "'League Gothic', 'Arial Narrow', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1px
  display-lg:
    fontFamily: "'League Gothic', 'Arial Narrow', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'League Gothic', 'Arial Narrow', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.5px
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'League Gothic', 'Arial Narrow', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.5px

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
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    border: "1px solid {colors.muted}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.muted}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
    marginTop: "{spacing.xs}"
  product-card-sold-out:
    typography: "{typography.badge}"
    textColor: "{colors.sold-out}"
    backgroundColor: transparent
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  format-badge:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "1px 4px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.primary}"
  category-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "4px 0"
  category-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "4px 0"
  footer-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
  social-icon-circle:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  social-icon-circle-hover:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
    minHeight: 300px
  hero-banner-overlay:
    backgroundColor: "{colors.canvas}"
    opacity: 0.6
  cart-count-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 5px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in hot pink `#f94877` with white uppercase Arial bold at 14px. Used exclusively for add-to-cart, checkout, and submit actions. On hover, shifts to `#e52d27` — a deeper red-pink that maintains contrast against the dark canvas. Disabled state drops to `#e99292`, a washed-out pink that signals unavailability without ambiguity. All primary buttons use `{rounded.sm}` (4px) — deliberately minimal, refusing the friendly pill shape of mainstream e-commerce.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Continue Shopping." Uses the dark canvas background with white text and a single-pixel `{colors.hairline}` border. On hover, the border thickens visually by shifting to `{colors.muted}` and the background fills with `{colors.surface-soft}`. The uppercase Arial bold treatment matches the primary button, keeping the visual language consistent even when the hierarchy drops.

### Cards
**`product-card`** — A compact, information-dense tile for the product grid. Background sits at `{colors.surface-card}` (#222222) — one step lighter than the page canvas but still deeply dark. The product image uses `{rounded.xs}` (2px) — barely a corner, preserving the raw, unpolished feel of a physical record sleeve. Title runs in Arial bold 15px, price in League Gothic 22px hot pink. A sold-out state replaces the price with a gray uppercase badge. On hover, the entire card lifts by adding a `{colors.muted}` border and shifting the background to `{colors.surface-soft}`.

**`sale-badge`** — A tiny hot-pink flag pinned to the top corner of sale items. Set in 11px uppercase Arial bold with 2px rounding and tight padding. The badge is the only place `#f94877` appears on the product card itself, making it a genuine signal rather than decorative noise.

### Navigation
**`nav-bar`** — A 60px fixed-height bar on the dark canvas, separated from content by a single-pixel `{colors.hairline}` border. Navigation links are uppercase Arial bold 14px in white, with the active state switching to `{colors.primary}` pink. The bar carries no background gradient, no shadow, no logo treatment — just text links and a search input. The cart count appears as a small pink pill badge in the upper-right corner.

**`category-link`** — Sidebar or dropdown links for browsing by genre, format, or label. Inactive links are `{colors.muted}` gray; active links switch to `{colors.primary}` pink. No underline, no background fill — the color shift alone signals state.

### Forms
**`text-input`** — A simple dark-field input with a `{colors.hairline}` border and white text. On focus, the border swaps to `{colors.primary}` pink — the only color feedback in the form system. No placeholder styling beyond standard gray. The search bar uses the same treatment, reinforcing that search is just another input, not a hero feature.

**`search-bar`** — Identical to `text-input` in structure, placed in the nav bar rather than as a standalone hero element. No magnifying glass icon by default — the input is self-evident in context. On focus, the pink border appears, and a subtle cursor change indicates interactivity.

### Footer
**`footer-section`** — A dark-on-dark footer separated from the main content by a `{colors.hairline}` border. Text runs in `{colors.muted}` gray at 13px Arial. Social media icons appear as outlined circles with brand-color fills on hover — Facebook blue `#3b5998`, Instagram pink `#e4405f`, Twitter blue `#55acee`, YouTube red `#cc2127`. The footer also includes links to Bandcamp and Discogs, using their respective brand colors as hover states. No newsletter signup, no decorative patterns — just links and social proof.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-2 columns); nav collapses to hamburger; search bar moves below nav; footer stacks vertically; category links hide behind "Browse" dropdown |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed (abbreviated labels); search bar stays in nav; footer splits into two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav links visible; search bar in nav; footer in three columns; category sidebar appears on collection pages |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; nav and footer remain same layout; additional whitespace on sides |

### Touch Targets
- All buttons and links: minimum 44px height (40px button + 4px padding buffer)
- Nav links: 44px tap area even if text is smaller
- Social icons: 44px minimum tap target (36px icon + 4px padding on each side)
- Product cards: entire card is tappable, not just the title or image
- Search bar: 44px minimum height for input field

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Category sidebar collapses into a dropdown select on mobile
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport shrinks
- Footer sections stack vertically on mobile, with accordion-style expand/collapse for link groups
- Search bar moves from inline nav position to full-width below the nav on mobile
- Sale badges and format badges remain visible at all breakpoints — never hidden

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all interactive elements could not be fully extracted — only primary button and product card hover were confirmed from the live site
- Error states for form inputs (validation, required fields, incorrect formats) were not observed
- Loading states (spinners, skeleton screens, progress indicators) are absent from the extracted data
- Dark mode is not applicable — the site already uses a dark canvas as its default
- Sub-brand or collection-specific color variations (e.g., "New Arrivals" vs "Sale" vs "Pre-Orders") may exist but were not captured
- Typography scale is inferred from common record-store patterns and the extracted font stack — exact font sizes for every level were not directly observable
- The checkout flow (Shopify or custom) could not be inspected — button styles and form components may differ in the cart/checkout context
- Mobile navigation behavior (hamburger menu animation, overlay style) was not documented from the live site
- The site does not appear to use a Shopify platform, so any platform-specific components (Shopify Pay buttons, cart drawers) are absent
- Accessibility details (focus outlines, ARIA labels, skip-to-content links) were not extracted
- Animation and transition durations (hover fades, page transitions, menu open/close) are unknown
