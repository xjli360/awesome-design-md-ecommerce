---
version: alpha
name: "Baker Creek Heirloom Seeds"
source_url: "https://www.rareseeds.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Parchment-warm surfaces (#f1d2a6) set against deep forest green (#15815b) give the interface the feel of a nineteenth-century seed catalog that has arrived, intact, in a browser — the palette reads as physical before it reads as designed. The near-black ink (#1b1c1b) carries a faint olive warmth, never neutral, as if type were set in printer's ink rather than screen pixels. Satoshi, the geometric sans-serif pulled from the font stack, does unexpected work here — a face normally at home on fintech dashboards becomes the vehicle for cultivar names and three-sentence varietal descriptions, creating a productive friction between the antiquarian subject matter and a clean, legible presentation. Red (#dc2626) arrives surgically: sale badges, low-stock flags, and promotional callouts only — it carries transactional meaning and does not appear in decorative contexts. A deep navy range (#003399 down to #0f2973) handles link hierarchy and secondary navigation, a quiet echo of the official blue that has appeared on commercial seed-packet typography for well over a century. Cards round gently at `{rounded.sm}` and `{rounded.md}`, suggesting the soft corner of paper stock rather than the aggressive pill of contemporary SaaS design. The spacing system breathes slowly — generous section padding lets photography of rare Brandywine tomatoes and century-old corn do the persuasion work without needing supporting copy. Navigation stays practical and catalog-deep: category browsing dominates the primary bar, with a search field prominent enough to serve a collection of over two thousand varieties. The footer settles into a rich green-black field (#2b2d2a), dense and grounding, a counterweight to the warm cream composition above it. Product cards present seed packets as botanical specimens — variety name in heavier weight, parentage dimmed and italicized below, availability and sale status surfaced by color rather than copy. The result is a living archive: centuries of seed knowledge organized for fast digital browsing, where the warmth of the palette carries the emotional freight the brand does not need to shout.

colors:
  primary: "#15815b"
  primary-active: "#0f6347"
  primary-disabled: "#8ec4b5"
  accent-red: "#dc2626"
  accent-navy: "#003399"
  accent-navy-mid: "#163ca6"
  accent-navy-deep: "#0f2973"
  ink: "#1b1c1b"
  body: "#393b38"
  muted: "#6b6b6b"
  muted-soft: "#878787"
  hairline: "#d1d1d1"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-warm: "#f1d2a6"
  surface-card: "#ffffff"
  surface-dark: "#2b2d2a"
  on-primary: "#ffffff"
  on-dark: "#f1d2a6"

typography:
  display-xl:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  botanical-name:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    fontStyle: italic
  price:
    fontFamily: "'Satoshi', system-ui, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
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
    padding: "12px 24px"
    height: 44px
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
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "11px 23px"
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 18px 10px 40px"
    height: 44px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    shadow: "0 4px 16px rgba(27,28,27,0.10)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    shadow: "0 2px 8px rgba(27,28,27,0.07)"
    padding: "{spacing.base}"
    imageAspect: "1/1"
    titleTypography: "{typography.title-sm}"
    subtitleTypography: "{typography.botanical-name}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.body}"
  hero:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.lg}"
    imagePosition: right
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  seasonal-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xl} {spacing.section}"
    textAlign: center
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.body}"
    separatorColor: "{colors.hairline}"
    linkColor: "{colors.accent-navy}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons

**`button-primary`** — Forest green (#15815b) fill at 44px height with Satoshi Semi-Bold 15px and `{rounded.sm}` corners. Hover darkens to `{colors.primary-active}` (#0f6347) without a transition delay — the catalog audience is task-oriented and expects immediate feedback. Disabled state fades to `{colors.primary-disabled}`, a desaturated sage that signals inactivity without disappearing. These appear on "Add to Cart" on seed packet detail pages, newsletter signup CTAs, and the checkout progression steps.

**`button-secondary`** — White fill with a 1.5px green border and matching `{colors.primary}` text. The border weight is intentional: a thinner stroke would read as disabled against the warm parchment and light-gray backgrounds that appear throughout the catalog. Used for "View All Varieties", "Browse Category", and any action that sits adjacent to a primary CTA without competing with it.

**`button-ghost`** — Transparent background, no border, ink text at `{typography.button-sm}`. Appropriate for inline editorial actions and "Learn More" links within content blocks where a filled or outlined button would visually overpower surrounding copy.

### Search

**`search-bar`** — A full-radius pill (`{rounded.full}`) on `{colors.surface-soft}` with a left-inset magnifying-glass icon at 40px from the left edge. The border sharpens from `{colors.hairline}` to a 1.5px `{colors.primary}` ring on focus. Given the catalog depth — over two thousand listed varieties — the search field is a top-nav fixture on all viewport widths and does not collapse behind a hamburger or secondary toggle. It remains at 44px height across breakpoints and spans the full available width on mobile.

### Navigation

**`nav-bar`** — 60px tall, white canvas, with a single `{colors.hairline-soft}` bottom border providing the only structural separator. Logo anchors left; primary category dropdowns (Vegetables, Flowers, Herbs, Grains, Accessories) span the center zone at `{typography.nav-link}` weight 500; account, wishlist, and cart icons sit right. On desktop widths the dropdowns open into a two-column grid of subcategories, wide enough to preview category depth without requiring a click.

**`nav-dropdown`** — White card with `{rounded.sm}` corners and a soft box-shadow (`0 4px 16px rgba(27,28,27,0.10)`). Subcategory labels render in `{typography.body-sm}` with `{colors.hairline}` separating logical groups. The dropdown appears on hover with no delay — catalog shoppers navigate by category habitually, and any hesitation in the reveal creates friction against that muscle memory.

### Product Card

**`product-card`** — A square 1:1 image fills the card top; below it, the variety name appears in `{typography.title-sm}` at weight 600, followed immediately by the cultivar's botanical parentage in `{typography.botanical-name}` italic at 13px — this two-line hierarchy distinguishes common name from scientific or historical lineage, a distinction that matters to the heirloom gardener audience. Price renders in `{typography.price}` (Satoshi 18px Semi-Bold) in `{colors.body}`. Sale and new-arrival badges overlay the image corner at top-left via `{rounded.xs}` chips. The card sits on a single hairline border (`{colors.hairline-soft}`) with a shallow box-shadow — it frames the packet image without competing with the product photography.

### Hero

**`hero`** — A parchment-warm (`{colors.surface-warm}`) band spanning the full viewport width, with an oversized hero image right-aligned and the headline in `{typography.display-xl}` anchored left. The warm background is structurally load-bearing: even when the image crops differently across viewport widths, the #f1d2a6 field maintains tonal continuity and prevents the layout from reading as broken. A single `button-primary` CTA sits below the subheading in `{typography.body-md}`. Seasonal hero rotations replace photography without touching the layout contract.

### Badges

**`sale-badge`** — Red (#dc2626) rectangular chip with all-caps 11px Satoshi Bold and `{rounded.xs}`. Overlays product images at top-left or sits inline in list views. Red is used exclusively for price-reduction events; it carries urgent transactional meaning that would be diluted by any decorative use elsewhere.

**`category-badge`** — Warm parchment fill (`{colors.surface-warm}`) with `{colors.body}` text, same type scale and shape as `sale-badge`. Labels seed variety attributes (Heirloom, Organic, Rare, Open-Pollinated) inside product cards and on listing filter rails.

**`new-badge`** — Forest green fill (`{colors.primary}`) with white text. Flags recently introduced varieties in the current season's catalog additions. The green signal reads as additive and positive, distinct from the red urgency of `sale-badge` even when both appear on the same card.

### Seasonal Banner

**`seasonal-banner`** — Full-width green band in `{colors.primary}` with centered heading in `{typography.display-sm}` and body copy in `{typography.body-md}`, both in `{colors.on-primary}`. Used for time-sensitive catalog announcements (spring planting deadlines, sold-out warnings, new catalog arrivals). Sits directly below the nav bar. Because it uses the same green as the primary button, it reads as action-oriented rather than decorative.

### Footer

**`footer`** — Deep green-black (#2b2d2a) full-width band with column headers in `{typography.title-sm}` weight 600, warmed by `{colors.on-dark}` (the parchment tone) to preserve brand warmth on dark ground. Navigation links render in `{colors.muted-soft}` and lift to `{colors.on-dark}` on hover. No top border is needed — the color shift creates the structural break. A newsletter signup row embeds a `text-input` with `{colors.canvas}` fill alongside a `button-primary` in an inline flex row. On mobile this stacks vertically with the input above the button.

### Breadcrumb

**`breadcrumb`** — Caption-scale (`{typography.caption}`) horizontal trail. Ancestor segments appear in `{colors.muted}` with `{colors.accent-navy}` underlining links. The active/current page segment uses `{colors.body}` without underline. A `/` separator renders in `{colors.hairline}`. Breadcrumbs are especially load-bearing on this site given the catalog depth — users navigating from a specific tomato variety back to the Vegetables category rely on them as the primary wayfinding shortcut.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer + logo + cart icon; search expands to full-width bar below nav; hero stacks image above text; footer columns stack vertically; seasonal banner text reduces to `{typography.title-sm}` |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline with dropdowns collapsed; hero image reappears side-by-side at reduced height (~320px); footer shows two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with hover dropdowns; hero at full 480px height with generous side padding; footer in four columns |
| Wide | > 1440px | Content max-width caps at 1440px with auto side margins; optional four-column product grid; hero image scales but text column stays fixed-width at ~560px |

### Touch Targets

- All buttons and nav links minimum 44px tall and 44px wide on mobile
- Product cards are fully tappable — the entire card surface links to the PDP, not just the image or title
- Badge overlays do not intercept taps; the parent card link is the sole active touch target
- Dropdown nav items have a minimum 44px height per row in the hamburger drawer
- Search pill maintains 44px height across all breakpoints

### Collapsing Strategy

- Primary nav collapses to a left-slide hamburger drawer at < 744px; drawer opens full-height with category tree expanded by default and subcategories accessible via accordion
- Product card variety names truncate at two lines with `text-overflow: ellipsis`; botanical subtitle shows one line maximum on mobile and card-grid tablet views
- Hero image is hidden below 480px viewport width and reappears at tablet+; the parchment background persists to maintain warmth even when image-less
- Newsletter form in footer stacks vertically (label → input → button) on mobile; remains inline at tablet+
- Seasonal banner reduces from `{typography.display-sm}` heading to `{typography.title-sm}` and collapses body copy to a single line on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit hover/active/disabled color states were extracted — `primary-active` (#0f6347) and `primary-disabled` (#8ec4b5) are derived by darkening and lightening #15815b respectively; verify against live site CTAs
- Satoshi is confirmed in the font stack but exact weight variants loaded (Regular 400 / Medium 500 / SemiBold 600 / Bold 700) were not verified; the variable font may ship a subset
- No box-shadow or elevation tokens were extractable; shadow values on cards, dropdowns, and modals are estimated from common conventions
- Icon set not identified — whether Baker Creek uses a proprietary glyph set, Heroicons, Phosphor, or another library could not be determined from extraction
- Exact nav height (60px assumed) and footer column count not directly extracted; both require live measurement
- Dark-mode support is unclear — no `prefers-color-scheme` media query tokens or alternate palette were found in the extraction
- Monospace font stack (Consolas, Courier New, Liberation Mono, Menlo) suggests a code or data display context (perhaps variety SKU or growing-data tables) but no such component was identified in the extraction
