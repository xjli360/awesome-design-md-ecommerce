---
version: alpha
name: "Opposit"
source_url: "https://opposit.shop"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every frame on opposit.shop is treated as a wall-ready object first and a product second — the shop steps back so the art can step forward, wrapping print imagery in maximum white canvas with an ink-black typographic system that refuses to compete. The brand name itself announces a design philosophy: opposition between sparse UI chrome and full-bleed photographic print reproductions, between the near-invisible navigation and the loud geometry of the posters it sells. Without a distinctive brand hue fighting for attention, Opposit's identity is carried entirely through restraint — a hairline-thin border world, unhurried letterforms, and a surface vocabulary that reads more like an art-bookshop catalogue than a commerce platform. Product cards are gallery plaques: the image dominates, the title appears in compact body weight underneath with almost no decorative ornament, and the price is typeset at the same scale as the caption, refusing urgency. The checkout-path buttons are the one place hierarchy breaks from white — a hard `#000000` fill on `{rounded.none}` or near-flat corners signals "proceed" with the bluntness of a gallery label rather than the glow of a retail CTA. Type is likely a neutral geometric sans in the Helvetica Neue / Inter lineage, set at modest weights; display headings stay under 700 weight, letting letter-spacing carry emphasis instead of mass. The overall rhythm is columnar: a four-column desktop grid collapses to two columns on tablet and a single column on mobile, each breakpoint maintaining the same generous margin so the prints never feel crowded. Internal spacing leans wide — section gutters at 64–96px, card padding that keeps the mat border feeling intact. If Opposit has a secret, it is the belief that white space is the most expensive surface in poster retail, and that spending it freely is the brand's sharpest differentiator.

colors:
  primary: "#000000"
  primary-active: "#1a1a1a"
  primary-disabled: "#999999"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  hairline: "#e0e0e0"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-warm: "#f0ece6"
  error: "#cc3333"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0

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
  section-xl: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 46px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 46px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 14px
    height: 46px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
  nav-bar-mobile:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 50px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspect: "3/4"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.muted}"
    gap: "{spacing.sm}"
    hover: "image scale 1.02 over 300ms ease"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.muted}"
    layout: "full-width image right, text left column"
    padding: "{spacing.section} {spacing.xl}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption-label}"
    borderBottom: "1px solid {colors.hairline}"
    itemSpacing: "{spacing.xl}"
    activeColor: "{colors.ink}"
    activeBorder: "2px solid {colors.ink}"
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "10px {spacing.base}"
    height: 40px
    iconColor: "{colors.muted}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 14px"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    padding: "8px 12px"
  product-detail-image:
    backgroundColor: "{colors.surface-soft}"
    imageRounded: "{rounded.none}"
    aspectRatio: "3/4"
    zoomOnHover: true
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption-label}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "none"

## Components

### Buttons

**`button-primary`** — Flat black fill, zero border-radius, uppercase tracking label at 13px/0.6px — signals "add to cart" and checkout actions without gloss or gradient. Active state deepens to `#1a1a1a`; disabled state uses `#999999` fill with white type, preserving legibility without an opacity trick. The all-caps spaced label is the brand's primary visual commitment to a typography-first hierarchy.

**`button-secondary`** — White background with a 1px `{colors.ink}` border and identical uppercase label; used for wishlist, "view details," and secondary checkout actions. On hover the border weight can optionally increase to 2px for tactile feedback without introducing color.

**`button-ghost`** — Low-contrast hairline-bordered button with muted label; reserved for filter resets, "clear all," and supplementary navigation where directing focus away from content would be counterproductive.

### Navigation

**`nav-bar`** — 56px tall, white, separated from content by a single `{colors.hairline}` bottom border. Logo sits left; category links center or right; cart icon and search icon at far right. No background fill on scroll — the bar stays white even when overlapping content. Mobile collapses to a hamburger toggle at 50px height.

**`category-strip`** — A horizontal pill-free filter rail that runs beneath the nav on collection pages. Labels are uppercase 11px/0.5px in `{colors.body}`, the active item underlined with a 2px `{colors.ink}` rule. Scrolls horizontally on mobile with no visible scrollbar.

### Product Grid & Cards

**`product-card`** — Portrait 3:4 image with zero rounding, flush to card edges. Artist name in `{typography.body-sm}` muted, print title in the same scale at ink color immediately below. Price sits as a third line, also `{typography.price-display}` in `{colors.muted}` — priced like a caption, not a conversion CTA. Hover scales the image 1.02× over 300ms for depth without disruption. Badge (NEW / SALE) is a flat black chip, uppercase, positioned top-left inside the image frame.

**`product-detail-image`** — Full 3:4 portrait on a `{colors.surface-soft}` matte; no frame chrome, no drop-shadow. Desktop shows a left-column image stack with a right-column detail panel. Zoom activates on hover or pinch.

### Size Selector

**`size-selector`** — Flat rectangular chips, no radius, 1px `{colors.hairline}` border default, 1px `{colors.ink}` border when selected. Unavailable sizes receive a diagonal strikethrough line rather than an opacity reduction, keeping the grid optically clean.

### Cart Drawer

**`cart-drawer`** — Slides in from the right at 400px width, white background, 1px left border in `{colors.hairline}`. Line items render as a compact image + title + size + price row; the remove button is an × icon in `{colors.muted}`. Subtotal and checkout button occupy a sticky footer inside the drawer.

### Hero Banner

**`hero-banner`** — Full-width editorial layout: text block left (headline in `{typography.display-xl}`, subline in `{typography.body-md}` muted), large print image right. No overlay gradient. Background remains `{colors.canvas}`, so the poster image reads as a physical object on a white wall rather than a digitally staged crop.

### Filter System

**`filter-pill`** — Pill-shaped labels with `{rounded.full}` and `{colors.hairline}` borders in resting state. Active state inverts to full black fill (`filter-pill-active`). Filters sit above the product grid as a wrapping row, not a sidebar, keeping the layout single-column at every breakpoint.

### Footer

**`footer`** — Full-width black band (`{colors.ink}` background) with white body copy and hairline-tone links. Organized in three or four columns: navigation, customer service, social links, and newsletter input. No decorative dividers — the shift from white to black canvas does the separating work.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav; category-strip horizontally scrollable; cart drawer full-width overlay; hero stacks image above text; filter pills collapse into a "Filter" toggle drawer |
| Tablet | 744–1128px | Two-column product grid; nav bar retains icon links, hides category text labels; hero image/text split maintained at 50/50; filter pills wrap to two rows |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with category labels; hero at full editorial width; cart drawer 400px fixed panel |
| Wide | > 1440px | Grid max-width capped at 1440px, centered; side margins expand; hero image scales to fill remaining space while text column holds fixed 480px width |

### Touch Targets

- All interactive controls (buttons, nav icons, size chips) maintain minimum 44×44px touch target via padding even when the visible element is smaller
- Filter pills padded to at least 36px height on mobile for comfortable single-thumb use
- Cart and search icons in the mobile nav bar get a 48×48px tap zone

### Collapsing Strategy

- Desktop sidebar filters do not exist — filter strip collapses on mobile into a bottom-sheet modal triggered by a "Filter & Sort" button above the grid
- Nav categories visible in desktop bar become the first items inside the hamburger slide-out on mobile
- Product card artist/title/price stack maintains the same text hierarchy at all breakpoints; only the grid column count changes
- Footer columns restack vertically on mobile in priority order: newsletter → navigation → social → legal

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site returned zero color tokens during extraction (likely JS-rendered or anti-bot protected); all palette values above are inferred from Scandinavian poster-shop conventions and the brand name's high-contrast framing, not live measurements
- **No font stacks extracted** — typography family above defaults to Helvetica Neue as a neutral editorial fallback; actual brand font (possibly GT America, Aktiv Grotesk, or a custom cut) is unconfirmed
- **Primary accent color unknown** — it is plausible Opposit uses a single warm or editorial accent (terracotta, sage, dusty rose) that was not captured; `{colors.accent-warm}` above is a placeholder
- **Logo type treatment** — wordmark weight, letter-spacing, and whether the logo uses a custom drawn form versus a stock typeface is unverified
- **Exact border-radius values** — zero-radius assumption is consistent with Nordic poster shops but not confirmed from live DOM inspection
- **Platform** — detected as non-Shopify; underlying platform (custom, Contentful-fronted, or proprietary) affects component markup conventions but could not be confirmed
