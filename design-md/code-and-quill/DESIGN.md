---
version: alpha
name: "Code&Quill"
source_url: "https://www.codeandquill.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Crimson (#d0021b) strikes with the finality of a correction mark: it lands on the primary add-to-cart button, the sale price tag, and the logo, and almost nowhere else on the page. The restraint is the whole argument. Everything around it is paper and ink — near-black (#121212, #1c1d1d) for body type and product photography, medium charcoal (#444444) for secondary prose, an off-white page field (#f9f9f9) that reads like uncoated notebook stock, and a cool silver hairline (#dedede) drawing grid lines between sections. The dark navy (#112233) surfaces as a secondary brand accent — the color of a terminal at 2 a.m. — appearing in feature callout blocks and ghost CTAs, giving the brand its dual register: analog craft paired against something that reads like command-line blue.

  Figtree is the sole typeface across every role. Its open apertures and even stroke weight read cleanly at 12px caption scale and sit comfortably at 48px without the slab heaviness that a self-consciously "artisanal" brand might reach for. Weight alone does the organizational work: 700 for hero headlines and product titles, 600 for buttons and subheads, 400 for prose, and a 700-weight all-caps 11px variant ({typography.label-caps}) for badge text and section overlines. No secondary serif appears anywhere; the "quill" romance in the brand name lives in product texture — grid paper, dot matrices, cloth covers — rather than in letterform nostalgia.

  The geometry is deliberately firm. Buttons use {rounded.xs} (4px), form inputs use {rounded.xs}, product cards use {rounded.sm} (8px). Nothing approaches pill shape. The card system is photography-dominant: a 3:4 notebook portrait fills the image well, format label and price below in clean white ({colors.surface-card}) padding, and a horizontal row of {rounded.full} cover-color swatches marking product variants with a 24px ink-ring selection state. The announcement bar flips to near-black ({colors.ink}) with on-dark type — a 40px band that collapses into the header white without a seam. The footer mirrors it: ink field, soft-surface body type, hairline-toned links. Both ends of the page hold the same dark anchor, so the crimson CTA reads as a voltage spike rather than a brand color trying to be everywhere at once.

colors:
  primary: "#d0021b"
  primary-active: "#c21519"
  primary-disabled: "#e8909a"
  ink: "#121212"
  body: "#1c1d1d"
  muted: "#444444"
  hairline: "#dedede"
  canvas: "#f9f9f9"
  surface-card: "#ffffff"
  surface-soft: "#f9f9f9"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  navy: "#112233"

typography:
  display-xl:
    fontFamily: "Figtree, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Figtree, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Figtree, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Figtree, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Figtree, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Figtree, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Figtree, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Figtree, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "Figtree, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "Figtree, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "Figtree, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "Figtree, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through
  button-md:
    fontFamily: "Figtree, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Figtree, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Figtree, sans-serif"
    fontSize: 15px
    fontWeight: 500
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: 12px 14px
    height: 48px
    focus-borderColor: "{colors.ink}"
    focus-outline: none
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-caps}"
    height: 40px
    textAlign: center
    paddingInline: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "3/4"
    imageObjectFit: cover
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    salePriceTypography: "{typography.price-sale}"
    salePriceColor: "{colors.primary}"
    comparePriceTypography: "{typography.price-compare}"
    comparePriceColor: "{colors.muted}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 8px
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  notebook-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedBorderColor: "{colors.ink}"
    selectedBorderWidth: 2px
    selectedBorderOffset: 2px
    gap: "{spacing.xs}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.muted}"
    minHeight: 560px
    contentMaxWidth: 640px
    paddingBlock: "{spacing.section}"
    paddingInline: "{spacing.xl}"
    imagePosition: right
  feature-callout:
    backgroundColor: "{colors.navy}"
    headlineTypography: "{typography.display-md}"
    headlineColor: "{colors.on-dark}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.on-dark}"
    paddingBlock: "{spacing.section}"
    paddingInline: "{spacing.section}"
    ctaComponent: button-primary
  collection-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    activeTextColor: "{colors.primary}"
    activeBorderColor: "{colors.primary}"
    activeBorderWidth: 1px
  review-stars:
    starColor: "{colors.primary}"
    emptyStarColor: "{colors.hairline}"
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    gap: "{spacing.xxs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.label-caps}"
    headingColor: "{colors.on-dark}"
    paddingBlock: "{spacing.section}"
    paddingInline: "{spacing.xl}"
    borderTop: none

## Components

### Buttons

**`button-primary`** — Solid crimson (#d0021b) fill, white type, 4px radius, 48px tall. The sole use of `{colors.primary}` as a surface color in the entire UI; hover shifts to `{colors.primary-active}` (#c21519) without scale or shadow animation. Disabled state uses the muted pink `{colors.primary-disabled}` (#e8909a) with the same white text and a `not-allowed` cursor.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border and ink text, matching the primary in height and radius. On hover, fill lifts to a very light tint of `{colors.surface-soft}`. Use wherever a secondary action sits beside a primary CTA (e.g., "Learn more" next to "Add to cart").

**`button-ghost-navy`** — Navy (#112233) fill, `{colors.on-dark}` text, same geometry as primary. Used in feature callout sections on the navy background, or in dark promotional banners where the crimson primary would lose contrast.

**`button-sm`** — Compact 36px tall crimson button, `{typography.button-sm}`, 10px 20px padding. Used in quick-add overlays on product card hover and in inline newsletter prompts.

### Text Input

**`text-input`** — White fill, 1px `{colors.hairline}` border, 4px radius, 48px tall. Placeholder in `{colors.muted}`. On focus, border color steps up to `{colors.ink}` with no box-shadow glow — keeps the form visually flat, consistent with the notebook-grid aesthetic. Error state swaps border to `{colors.primary}`.

### Navigation

**`nav-bar`** — White surface, 64px height, bottom hairline divider. Logo mark left-aligned in crimson. Nav text links (`{typography.nav-link}`) centered or right-grouped with cart and account icons. No dropdown mega-menu observed; collection links navigate directly. Sticky on scroll; the `announcement-bar` scrolls away before the nav locks.

**`announcement-bar`** — 40px ink-black band above the nav, centered `{typography.label-caps}` in white. Used for shipping thresholds, limited-run notices, and sale countdowns. Collapses on mobile to a single scrolling ticker if content exceeds one line.

### Product Card

**`product-card`** — 3:4 aspect-ratio image well at top, white padding block below. Title in `{typography.title-sm}`, price in `{typography.price-display}`. Sale prices render in crimson (`{colors.primary}`) with the original price struck through in `{colors.muted}` beside it. The `{product-badge}` component (`SALE`, `NEW`, `BESTSELLER`) pins absolute top-left in crimson with no radius. Cover-color swatches (`notebook-swatch`) appear below the title row as a horizontal run of 24px `{rounded.full}` dots.

### Notebook Swatch

**`notebook-swatch`** — 24px filled circles, each in the notebook cover color, spaced 4px apart. Active swatch gains a 2px `{colors.ink}` ring with 2px offset (CSS `outline`). On hover, a color name tooltip appears above. Used on product cards (compact row) and product detail pages (larger, labeled grid).

### Hero Section

**`hero-section`** — Off-white (`{colors.canvas}`) background, min-height 560px, split layout: editorial copy left (max-width 640px), product lifestyle image right. Headline in `{typography.display-xl}`, body in `{typography.body-md}` `{colors.muted}`, primary CTA below. Padding uses `{spacing.section}` vertically. On mobile, image stacks above copy.

### Feature Callout

**`feature-callout`** — Full-width navy (#112233) section used for brand value propositions (lay-flat binding, paper quality, format variety). White headline (`{typography.display-md}`), white body (`{typography.body-md}`), and a `button-primary` CTA. The navy creates the brand's dark-mode register without requiring a global theme switch.

### Collection Filter

**`collection-filter`** — Inline chip row for filtering by format (dot grid, lined, blank), cover type, or size. Chips sit in `{colors.surface-soft}`, 4px radius, `{typography.body-sm}`. Active chip gets a 1px `{colors.primary}` border and crimson text weight bump to 600. No dropdown filter panels observed.

### Review Stars

**`review-stars`** — Five stars in `{colors.primary}`, empty stars in `{colors.hairline}`. Review count and average in `{typography.caption}` `{colors.muted}` beside the star row. Appears below product titles on cards and above the add-to-cart on PDP.

### Footer

**`footer`** — Ink-black (#121212) field, `{typography.label-caps}` column headers in white, `{typography.body-sm}` links in `{colors.hairline}` that step to full white on hover. Four columns on desktop: Shop, About, Support, Social. Collapses to stacked accordions on mobile. No redundant secondary nav; all links present on the announcement bar or main nav are omitted.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero image stacks above copy; nav collapses to hamburger icon; announcement bar becomes single-line ticker; footer becomes stacked accordions |
| Tablet | 744–1128px | Two-column product grid; hero remains split but at reduced copy width; nav links may truncate to icons + label; filter chips scroll horizontally |
| Desktop | 1128–1440px | Three- or four-column product grid; full split hero; all nav links visible; feature callout at full bleed with side-by-side text and image |
| Wide | > 1440px | Content capped at ~1440px max-width with canvas-colored gutters; grid remains four columns; hero image expands to fill right half |

### Touch Targets

- All interactive elements (buttons, swatches, nav links, filter chips) minimum 44×44px tap target
- Notebook swatches (24px visual) padded to 36px touch area via invisible padding
- Cart icon and hamburger minimum 44px hit area despite smaller visual size

### Collapsing Strategy

- Footer nav: four desktop columns collapse to vertically stacked label-plus-links accordions, each toggled by the `{typography.label-caps}` header row
- Product filters: horizontal chip row gains horizontal scroll on mobile; no collapse to a dropdown unless chip count exceeds eight
- Hero: image moves from right-column to full-width top-of-card on mobile; copy stack below; CTA remains full-width
- Announcement bar: single long message becomes a CSS marquee or truncated single line at mobile widths

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-disabled` color (#e8909a) not extracted from site; value is an estimate — verify against Shopify theme settings or computed button disabled state
- `surface-card` pure white (#ffffff) is inferred; not directly present in the extracted hex list (closest extracted is #f9f9f9)
- Hover transition timing and easing curves not captured; all motion specs are absent from extracted data
- Icon system style (stroke weight, corner radius on SVGs, filled vs outlined) not determinable from color/font extraction alone
- Mobile navigation pattern (drawer vs fullscreen overlay vs simple dropdown) not confirmed
- Product detail page layout specifics — image gallery behavior (thumbnails, zoom, video), sticky add-to-cart bar threshold — not extracted
- Figtree variable font axis ranges (weight axis min/max) and whether a subset is self-hosted vs loaded via Google Fonts not confirmed
- Any loyalty, rewards, or subscription UI components not visible in extraction pass
