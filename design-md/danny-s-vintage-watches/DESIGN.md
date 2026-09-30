---
version: alpha
name: "Danny's Vintage Watches"
source_url: "https://dannysvintagewatches.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep navy (#132558) anchors every primary call-to-action on a site whose commercial premise is the machinery of lost decades — pocket watches, dress watches, and tool watches from eras when mechanical precision was craft rather than commodity. The surrounding palette is almost entirely silver-gray: #e6e6e6, #dedede, and #ededed form a cool, neutral gallery that lets dial photography breathe without chromatic competition, while near-black (#202223) grounds the text hierarchy. Georgia carries the editorial weight in body copy, bringing a serif tradition appropriate to horological history, while Oswald handles display and category headings in condensed uppercase — a pairing that reads as auction catalog rather than lifestyle blog. Coral (#ff6a6a) surfaces as the alert and badge accent, flagging new arrivals or price signals with warmth that contrasts the otherwise steel-toned system. The product-card architecture places the dial image on a #f3f3f3 surface with movement type, case size, and decade as secondary metadata in muted gray (#6d7175). Vintage collector commerce lives and dies on condition disclosure, so the design allocates explicit space for grade badges — Excellent, Very Good, Good — rendered as small uppercase pills behind a hairline border ({rounded.xs}). The nav retains the full brand wordmark at every breakpoint and keeps a persistent search icon prominent, because search is the primary entry point for a buyer hunting a specific reference number. Spacing is generous between product rows but compressed within card metadata, letting the collector scan year, diameter, and movement type before committing to a detail page. The footer runs in near-black (#272727) with reversed white type, grounding the page with permanence that mirrors the longevity of the objects for sale. No gradients, no decorative texture: the design trusts the objects themselves to carry the visual interest, keeping chrome minimal so a patinated dial face becomes its own composition.

colors:
  primary: "#132558"
  primary-active: "#0d1a3d"
  primary-disabled: "#4f60ca"
  ink: "#202223"
  body: "#393939"
  muted: "#6d7175"
  muted-soft: "#959ea9"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  surface-dark: "#272727"
  surface-medium: "#393939"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent: "#ff6a6a"
  accent-strong: "#ff2626"
  accent-green: "#41b883"

typography:
  display-xl:
    fontFamily: "'Oswald', Helvetica, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Oswald', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Oswald', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
    textTransform: uppercase
  title-md:
    fontFamily: "'Oswald', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "Georgia, serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica, 'gt-eesti', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Oswald', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Helvetica, 'gt-eesti', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Helvetica, 'gt-eesti', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Oswald', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  meta-label:
    fontFamily: "Helvetica, 'gt-eesti', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    opacity: 0.5
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 13px 23px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 13px 23px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm}"
    imageAspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    lineClamp: 2
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  product-card-meta:
    typography: "{typography.meta-label}"
    textColor: "{colors.muted}"
  condition-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    backgroundColor: "{colors.canvas}"
  condition-badge-excellent:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    border: "1px solid {colors.accent-green}"
    textColor: "{colors.accent-green}"
    backgroundColor: "{colors.canvas}"
  condition-badge-good:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    backgroundColor: "{colors.canvas}"
  new-arrival-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  watch-detail-hero:
    imageBackground: "{colors.surface-soft}"
    imageRounded: "{rounded.none}"
    thumbnailBorder: "2px solid {colors.hairline}"
    thumbnailBorderActive: "2px solid {colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeTextColor: "{colors.ink}"
  price-display:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"
  footer-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-bottom-bar:
    backgroundColor: "{colors.surface-medium}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — Flat rectangular button (`{rounded.none}`) in deep navy (#132558) with uppercase Helvetica type at 1px letter-spacing, conveying the authority of an auction house catalog rather than a consumer storefront. Active state deepens to #0d1a3d; disabled falls to muted indigo at reduced opacity. Used for "Add to Cart," "Contact Seller," and primary form submissions across PDP and checkout.

**`button-secondary`** — White fill with a 1px navy (#132558) border and matching uppercase type. Used for secondary actions like "Save to Watchlist" or "Ask a Question." Maintains the same squared footprint (`{rounded.none}`) as the primary, keeping both at visual parity — the fill is the only differentiator.

**`button-ghost`** — Transparent background with a hairline (#dedede) border and dark ink text in `{typography.button-md}`. Handles tertiary actions such as filter toggles, sort controls, and "Clear All" in the product grid without drawing attention away from the product imagery.

### Navigation
**`nav-bar`** — 72px height on a white canvas with a 1px bottom hairline. Brand wordmark in Oswald uppercase is left-anchored; right-side links use `{typography.nav-link}` (14px Oswald, 1px tracking, uppercase). On scroll depth, the hairline lifts and a faint box-shadow signals elevation without changing background color. Mobile collapses to hamburger + centered wordmark + search icon — search stays visible because reference-number lookup is the dominant entry pattern for collectors.

**`nav-bar-scrolled`** — Drops the hairline border and adds a subtle shadow to indicate the nav has detached from the page edge, maintaining legibility over light product image backgrounds.

### Product Card
**`product-card`** — Flush rectangular card with a 1px hairline-soft border on a white surface. The image zone sits on #f3f3f3 (`{colors.surface-soft}`), square-cropped at 1:1 to center the dial face. Below: watch name in `{typography.title-sm}` (Georgia 16px bold, two-line clamp), a metadata row of brand, movement type, and decade in `{typography.meta-label}` (11px muted), and price in `{typography.price-display}` (Oswald 22px navy). Condition badge and new-arrival flag stack top-left over the image. No hover shadow — the hairline border simply deepens to the primary navy on hover.

### Condition Badges
**`condition-badge-excellent`** — Small 2px-radius pill (`{rounded.xs}`) with a green (#41b883) border and matching green text, using `{typography.badge}` (10px Helvetica bold uppercase). Overlays the product card image top-left and immediately communicates top-tier pieces at a glance across a dense grid.

**`condition-badge-good`** — Same pill geometry in muted gray, hairline border, and `{typography.badge}` uppercase. Signals inspected pieces below the excellent threshold without alarming the buyer — gray communicates context, not rejection.

**`new-arrival-badge`** — Coral (#ff6a6a) solid fill in `{typography.badge}` uppercase, stacking below or beside the condition badge. Warm coral against the cool gray grid creates a deliberate visual interrupt without competing with the deep navy primary CTA system.

### Search
**`search-bar`** — Full-width or contained input on #f3f3f3 background, no border radius, 1px hairline that switches to navy on focus. Placeholder in muted-soft (#959ea9). Positioned prominently in the nav and as a hero element on the homepage, reflecting that collectors arrive with a specific reference number, brand, or complication in mind rather than browsing category tiles.

### Watch Detail Hero
**`watch-detail-hero`** — Main image on #f3f3f3 ground with no border radius; thumbnail strip beneath uses 2px hairline borders that switch to 2px navy on the active selection. No lightbox chrome is added — the dial photograph is the primary product asset and should dominate its container cleanly without UI decoration competing for attention.

### Category Pills
**`category-pill`** — Rounded full pill (`{rounded.full}`) on surface-soft in 12px Helvetica uppercase (`{typography.caption}`) for filter tags: Era, Movement Type, Brand, Complication, Case Material. Active state fills with navy (#132558) and white type. Provides a scannable horizontal filter row above the product grid without the overhead of dropdown accordions.

### Section Headers
**`section-header`** — Oswald 28px condensed uppercase (`{typography.display-md}`) with a 2px navy underline and 8px padding below. A direct reference to the divider typography of printed auction catalogs and horological price guides — it reads as authoritative rather than decorative.

### Footer
**`footer-dark`** — Near-black (#272727) footer with reversed white nav links and muted-gray (#959ea9) secondary links in Georgia 14px (`{typography.body-sm}`). A lighter #393939 bottom bar carries copyright and legal text in 12px uppercase caption (`{typography.caption}`). The dark register grounds the page and produces a sharp contrast with the light gray product canvas above, signaling a clean end-of-page boundary.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered wordmark + search icon; category pills scroll horizontally with a fade-mask edge; hero image full-bleed |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline, secondary links in a slide-out drawer; watch detail hero splits 60/40 image-to-details |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav; sticky left-rail filter panel on collection pages |
| Wide | > 1440px | Max-width container ~1400px centered with generous lateral padding; four-column grid maintained |

### Touch Targets
- All buttons minimum 48px height
- Nav links minimum 44px tap height on mobile
- Condition badge and new-arrival overlay are display-only; the card tap target covers the full card
- Thumbnail strip images on mobile detail page minimum 48×48px
- Category pill minimum 36px height with 16px horizontal padding

### Collapsing Strategy
- Filter sidebar collapses to a bottom-sheet modal on mobile, triggered by a "Filter" ghost button pinned above the product grid
- Product card metadata truncates to price + condition badge only at Mobile width; full metadata (brand, movement, decade) is visible at Tablet and above
- Footer nav collapses to stacked accordion sections on Mobile; three-column layout on Tablet+
- Horizontal category pill row becomes a scroll-snapped single row on Mobile, with overflow hidden behind a right-side gradient mask
- Section headers maintain full Oswald uppercase at all breakpoints; font-size steps from 28px (Desktop) to 22px (Mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font confirmed beyond extracted stacks; Oswald and Georgia are inferred from font-family data but exact licensed weights and pairing logic are unverified from extraction alone
- Several extracted colors (#35495e, #41b883, #56b280) match Vue.js framework defaults and were excluded from the brand palette; actual usage in brand-authored UI is unconfirmed
- #007ace matches the Shopify admin blue and is excluded as a storefront brand color
- No meta theme-color set; mobile browser chrome color is unknown
- Exact button border-radius is unverifiable from extraction; flat (`{rounded.none}`) assumed based on vintage catalog aesthetic
- Card shadow depth (flat vs. subtle elevation) cannot be confirmed; hairline-only treatment assumed
- Logo asset color unconfirmed; navy (#132558) assumed as primary from palette uniqueness analysis
- Exact Shopify theme breakpoints not extractable; responsive behavior inferred from Shopify Dawn defaults
- Hover and focus state animations (duration, easing) not determinable from static extraction
