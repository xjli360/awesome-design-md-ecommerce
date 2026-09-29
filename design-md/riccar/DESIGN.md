---
version: alpha
name: "Riccar"
source_url: "https://www.riccar.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Pull the Tandem Air motor badge into a grid and you get the Riccar design system in miniature: compressed navy (#00548e), white letterforms, uppercase Gotham set at micro scale, and a geometry that trusts negative space over decoration. That badge propagates outward — the same navy anchors hero panels, primary buttons, and the nav bar, sitting against broad near-white fields (#f6f6f6, #f4f4f4) that let vacuum photography carry the emotional weight the color system deliberately withholds. Riccar does not reach for visual excitement; it reaches for the visual grammar of a brand that has been engineering belt-driven motors longer than most of its retail competitors have existed. Dapifer, a bracketed serif, handles display headlines exclusively — at 48px bold it lends "Tandem Air Technology" an editorial authority that a geometric sans alone could not sustain. Gotham A/B and NeueKabel take everything else: nav links at 14px/600, badge labels at 11px/700 with 0.8px tracking in uppercase, body copy at 16px/400. The two-typeface system maps cleanly onto a two-register brand voice: Dapifer for product storytelling, Gotham for interface utility. Orange enters as a single accent voltage — #da532c, a burnt brick tone, used on promotional badges, "Add to Cart" states, and clearance callouts. It is visually hot against the navy primary but Riccar gives it a narrow operational brief: conversion moments only, never structural chrome. Card geometry is conservative throughout — `{rounded.xs}` on buttons and inputs, `{rounded.sm}` on product cards — no large radii, which would read as playful in a category that earns trust through longevity and engineering credibility. The dealer-locator CTA is the site's most structurally recurring element, appearing in sidebars and section breaks far more often than a direct checkout button; Riccar's conversion architecture routes browse traffic toward authorized specialty retailers rather than online purchase, making that one block as load-bearing as the hero banner itself.

colors:
  primary: "#00548e"
  primary-active: "#003d6b"
  primary-disabled: "#cbd5e1"
  accent: "#da532c"
  accent-hover: "#c44820"
  ink: "#111827"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#f4f4f4"
  surface-mid: "#eeeeee"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  link: "#2563eb"

typography:
  display-xl:
    fontFamily: "Dapifer, Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Dapifer, Georgia, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Dapifer, Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham A', 'Gotham B', NeueKabel, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham A', 'Gotham B', NeueKabel, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  body-md:
    fontFamily: "'Gotham A', 'Gotham B', NeueKabel, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham A', 'Gotham B', NeueKabel, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham A', 'Gotham B', NeueKabel, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Gotham A', 'Gotham B', NeueKabel, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham A', 'Gotham B', NeueKabel, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gotham A', 'Gotham B', NeueKabel, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "'Gotham A', 'Gotham B', NeueKabel, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "'Gotham A', 'Gotham B', NeueKabel, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase

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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 48px
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageBg: "{colors.surface-card}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  hero-photo-scrim:
    backgroundColor: "rgba(0,84,142,0.70)"
    textColor: "{colors.on-primary}"
  tandem-air-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "2px solid {colors.on-primary}"
  promo-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  spec-row-label:
    typography: "{typography.title-sm}"
    textColor: "{colors.muted}"
  dealer-locator-cta:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  category-filter-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 20px
  category-filter-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: 8px 20px
  comparison-banner:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.lg} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    linkColor: "{colors.surface-mid}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline-soft}"

---

## Components

### Buttons

**`button-primary`** — Deep navy (#00548e) fill with white uppercase Gotham text at 15px/600 weight and 0.6px tracking. The all-caps treatment projects product authority rather than consumer friendliness — this is a tool-category brand. Height is fixed at 48px with 14px/28px padding; radius is `{rounded.xs}` (4px), just enough to break a hard corner without signaling playfulness. Hover state darkens to `{colors.primary-active}` (#003d6b); disabled state renders in `{colors.primary-disabled}` with `{colors.muted}` text.

**`button-secondary`** — White canvas fill with a 2px navy border and navy text in the same uppercase Gotham stack. Used alongside `button-primary` wherever two CTAs share a row — "Shop Now" paired with "Find a Dealer" is the canonical instance. Matching 48px height keeps the pair optically level.

**`button-accent`** — Burnt orange (#da532c) fill with white uppercase text. Reserved for urgency-flagged moments: promotional pricing, limited-stock callouts, and "Add to Cart" states on product detail pages. Hover darkens to `{colors.accent-hover}` (#c44820). The orange is temperature — Riccar applies it narrowly so it doesn't bleed into structural chrome.

### Navigation

**`nav-bar`** — Full-width white bar at 72px desktop, 60px mobile. Riccar logo sits at the left edge; category links (Upright, Canister, Accessories, Tandem Air) run center-right in `{typography.nav-link}` Gotham semibold. A search icon and a "Find a Dealer" text link anchor the far right. A 1px `{colors.hairline}` bottom border separates the nav from page content without adding visual weight. On mobile the link cluster collapses to a hamburger; the "Find a Dealer" link persists as an icon+text pair.

### Product Card

**`product-card`** — White card, 1px `{colors.hairline}` border, `{rounded.sm}` radius, `{spacing.lg}` interior padding. Product image sits on a `{colors.surface-card}` pale gray field so vacuum photography does not float. Title renders in `{typography.title-md}` Gotham 600 in `{colors.ink}`; price in `{typography.price}` at 22px/700 in `{colors.primary}` navy. The Tandem Air badge (`tandem-air-badge`) drops beneath the product image on qualifying models — navy fill, white double-border, badge-label typography. A single `button-primary` drives to the product detail page.

### Hero Banner

**`hero-banner`** — Two modes: solid navy fill (#00548e) for feature and promotional heroes; photography with a `hero-photo-scrim` overlay (70% navy opacity) for lifestyle content. Display headline uses `{typography.display-xl}` Dapifer serif at 48px, contrasting the Gotham body copy and marking product narrative apart from interface utility. Minimum height 480px desktop; content left-aligns on photography heroes, centers on solid-color fields. The `button-primary` and `button-secondary` pair typically appears at the hero base.

### Tandem Air Badge

**`tandem-air-badge`** — Riccar's proprietary motor technology earns its own visual mark: `{colors.primary}` navy fill, `{colors.on-primary}` white text at `{typography.badge-label}` (11px/700/0.8px tracking), 2px white inset border. Compact padding (6px/12px) keeps it reading as a certification indicator rather than a banner. Applied at the product card image base and the PDP hero header for any vacuum in the Tandem Air line.

### Promo Badge

**`promo-badge`** — Orange (#da532c) fill, white uppercase text at `{typography.badge-label}`. Flat rectangle at `{rounded.xs}` — consistent with the minimal-radius geometry throughout the site. Applied to product card corners for "NEW," "SALE," and "Clearance" states. Never stacked with the Tandem Air badge on the same card; the two badges serve distinct informational registers.

### Spec Table

**`spec-row`** — Alternating `{colors.surface-soft}` rows divided by 1px `{colors.hairline}` borders. Value text in `{typography.body-sm}` at `{colors.body}`; attribute labels (Motor Type, Filtration System, Weight, Cord Length) in `{typography.title-sm}` uppercase Gotham at `{colors.muted}` — receded so values read first. On mobile the table wraps into a stacked label/value pair per row inside a horizontal scroll container.

### Dealer Locator CTA

**`dealer-locator-cta`** — A recurring block in sidebars and section breaks: `{colors.surface-card}` background, `{rounded.sm}`, `{spacing.xl}` padding, 1px `{colors.hairline}` border. Headline in `{typography.title-md}`, supporting body copy in `{typography.body-md}`, terminated by a full-width `button-primary`. This component is Riccar's structural conversion point — the brand sells predominantly through authorized specialty retailers, and the site funnels almost every product browse toward this touchpoint rather than an online checkout.

### Category Filter Tabs

**`category-filter-tab`** / **`category-filter-tab-active`** — Pill-shaped filter tabs using `{rounded.full}` for browsing vacuum types (Upright, Canister, Handheld, Commercial). Inactive state: white fill, `{colors.hairline}` border, `{colors.muted}` uppercase Gotham text. Active state: navy fill, white text, navy border. Padding at 8px/20px keeps tabs compact for horizontal scrolling on mobile without sacrificing touch target size.

### Comparison Banner

**`comparison-banner`** — A `{colors.surface-mid}` gray strip with a 3px `{colors.primary}` navy top border, used to frame cross-model comparison tables or feature-matrix callouts. Body copy in `{typography.body-md}`; section title in `{typography.title-md}`. The colored top border is the lightest structural use of navy outside of buttons and badges, differentiating this block from general surface cards without full navy fill.

### Footer

**`footer`** — `{colors.ink}` (#111827) background with `{colors.muted-soft}` body text and `{colors.surface-mid}` link color. Four-column grid on desktop: Products, Support, About Riccar, Find a Dealer. Column headings in `{typography.title-sm}` (uppercase Gotham 700) at `{colors.canvas}` white. Footer collapses to single-column accordions on mobile. Legal copy and copyright run in `{typography.caption}` at `{colors.muted-soft}` in a full-bleed row beneath the column grid.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark; hero headline drops to `{typography.display-md}` (32px), min-height to 320px; category filter tabs scroll horizontally; dealer-locator CTA stacks vertically; spec table rows stack as label/value pairs |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category links, hides secondary CTAs; hero retains photography with scrim overlay; spec table contained in horizontal scroll; footer in two-column grid |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all category links and "Find a Dealer" CTA button; hero at full 480px min-height; spec table full-width with all columns visible |
| Wide | > 1440px | Content constrained to ~1320px max-width with auto side margins; hero image scales to fill; no additional layout changes beyond column grid tightening |

### Touch Targets

- All primary and accent buttons fixed at 48px height; minimum touch target maintained across all breakpoints
- Category filter tabs minimum 44px height on mobile with `{spacing.sm}` invisible vertical padding extension
- Nav hamburger icon minimum 44×44px tap target area
- Product card entire surface tappable to PDP, not only the CTA button
- Dealer-locator CTA block tappable as a unit on mobile

### Collapsing Strategy

- Navigation: hamburger at < 744px; full link bar with search and dealer CTA at 744px+; "Find a Dealer" persists at all breakpoints (icon+text on mobile, full button on desktop)
- Footer: single-column accordion at mobile; two-column at tablet; four-column grid at desktop
- Hero: headline type steps down one scale per breakpoint (display-xl → display-md → display-sm); min-height relaxes from 480px to 320px on mobile
- Product grid: 1 col mobile → 2 col tablet → 3–4 col desktop; card padding stays at `{spacing.lg}` throughout
- Spec table: horizontal scroll container on mobile and tablet; full-width native table on desktop

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact brand-designated primary blue unconfirmed from style guide; #00548e chosen as most distinctive non-framework blue in extracted set and consistent with Riccar's known navy identity
- Several extracted blues (#2563eb, #3875d7, #2a62bc, #1979c2, #0077cb, #0095ff, #5897fb) are likely UI framework or component-state variants rather than brand tokens; only #00548e treated as primary brand color
- Orange accent (#da532c) appears in extracted set; unclear whether it is a structural accent or limited to promotional/sale surfaces only
- #f97316 in the extracted list matches Tailwind orange-500 exactly — likely a framework default and excluded from brand token treatment
- Dapifer weight variants available on site (Book, Semibold, Bold) not determinable from color/font extraction alone; display-xl assumes Bold (700) as the hero weight
- NeueKabel role versus Gotham A/B not separable from extraction — assumed as a Gotham complement or alternate weight rather than a primary typeface
- luma-icons glyph map, size defaults, and icon-to-label pairings not extractable from color scans
- Cart and checkout UI surfaces not visible in extraction; component coverage limited to browse and product discovery flows
- No motion or animation tokens confirmed; transition timing and easing defaults not extracted
