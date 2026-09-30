---
version: alpha
name: "Levoit"
source_url: "https://levoit.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The four-step teal progression — #02454f, #005e6e, #006689, #00c1bc — is Levoit's visual grammar for filtered air: a depth chart that moves from ocean-bottom dark to bright surface shimmer without leaving the same hue family, the brand's way of rendering invisible air quality as color. Against this cool spectrum sits #f9d861, a single warm-yellow voltage used on sale badges and promotional moments — its rarity is its function, a directional pop in a grid of teal-dominant product cards. The warm beige at #dacebf surfaces only on lifestyle feature rows, where product photography needs a domestic ground tone rather than the clinical white that dominates the rest of the canvas.

  DIN handles display headers with utilitarian precision suited to air-quality metrics — short, numeric-adjacent strings like "CADR 400" or "PM 2.5" read cleanly in the condensed geometric cuts. Museo Slab steps in at mid-hierarchy callouts as the more editorial voice; where DIN is a readout, Museo Slab is a declaration. Proxima Nova carries body copy, review text, and UI labels with approachable neutrality. Sun Valley appears in campaign imagery as a display flourish rather than a workhorse stack.

  The shop structure is Shopify-standard but the product card treatment skews technical rather than lifestyle: filter-type chips (HEPA H13, Smart Wi-Fi), CADR ratings, and modestly rounded cards at `{rounded.sm}` rather than the aggressive pill shapes of fashion DTC. Buttons are teal-filled at 48px height — not pill-shaped, not sharp-cornered — a middle register that signals clinical reliability without sterile austerity. The mint-to-teal gradient (#64edc2 → #00c1bc) appears in hero alternates and feature callout sections as the brand's shorthand for visible clean air. Navigation stays minimal: category bar at top, search prominent in a full-pill bar, cart and account icons right — the layout trusts specification data and photography to do the selling.

colors:
  primary: "#005e6e"
  primary-hover: "#006689"
  primary-active: "#02454f"
  primary-disabled: "#a3c4c8"
  accent-yellow: "#f9d861"
  teal-bright: "#00c1bc"
  teal-mint: "#64edc2"
  teal-deep: "#02454f"
  teal-mid: "#006689"
  blue-soft: "#a3bff0"
  ink: "#121212"
  body: "#393939"
  muted: "#9e9e9e"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#dacebf"
  surface-card: "#ffffff"
  surface-muted: "#f5f5f5"
  on-primary: "#ffffff"
  on-accent: "#121212"

typography:
  display-xl:
    fontFamily: "'DIN', 'DIN Condensed', Impact, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'DIN', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'DIN', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Museo Slab', Georgia, serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Museo Slab', Georgia, serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'DIN', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'DIN', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'Proxima Nova', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge-label:
    fontFamily: "'DIN', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  metric-display:
    fontFamily: "'DIN', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  product-label:
    fontFamily: "'Proxima Nova', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px

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
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
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
    padding: 13px 27px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  button-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    fontWeight: 600
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspect: "1/1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
    labelTypography: "{typography.product-label}"
  hero-section:
    backgroundGradientFrom: "{colors.teal-deep}"
    backgroundGradientTo: "{colors.primary}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
  hero-mint-gradient:
    backgroundGradientFrom: "{colors.teal-mint}"
    backgroundGradientTo: "{colors.teal-bright}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
  feature-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  feature-badge-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  filter-indicator:
    backgroundColor: "{colors.teal-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    activeColor: "{colors.teal-bright}"
  metric-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    metricTypography: "{typography.metric-display}"
    labelTypography: "{typography.caption}"
    metricColor: "{colors.primary}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg}"
  specification-row:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  category-pill:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.body}"
    typography: "{typography.product-label}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.product-label}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  app-connect-banner:
    backgroundColor: "{colors.teal-deep}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.teal-mint}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  review-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    starColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg}"
  lifestyle-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.teal-mint}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — A 48px-tall teal block (`{colors.primary}` fill, white label) with `{rounded.sm}` radius and DIN at 15px/600 weight. On hover the fill steps one stop warmer to `{colors.primary-hover}` (#006689); on active press it deepens to `{colors.primary-active}` (#02454f), walking down the brand's own teal depth chart. Used for primary CTAs — "Add to Cart," "Shop Now," "Get Yours."

**`button-secondary`** — Same 48px height as the primary, white fill with a 1.5px `{colors.primary}` border and teal label text. Used for secondary CTAs like "Learn More," "Compare Models," and "See All Reviews" where a teal-filled button would compete with a nearby primary.

**`button-accent`** — Yellow (`{colors.accent-yellow}`) fill with black label, same `{rounded.sm}` shape. Reserved for sale events, bundle promotions, and limited-time campaign pages. Used sparingly — its rarity is its impact.

**`button-text`** — Transparent background, teal underlined text at `{typography.button-sm}` scale. Used for "See all," "View specs," and secondary navigational nudges in carousels and feature lists.

### Text Input & Search
**`text-input`** — 48px height, 1px `{colors.hairline}` border, `{rounded.sm}` radius. On focus, the border thickens to 1.5px in `{colors.primary}`. Placeholder text in `{colors.muted}`. Used in account forms, subscription modals, and address entry.

**`search-bar`** — Full-pill shape (`{rounded.full}`) with a light `{colors.surface-muted}` fill, distinguishing it from standard form inputs. Placed prominently in the header and on mobile as the primary navigation aid. On focus, transitions to a white fill with `{colors.primary}` border.

### Navigation
**`nav-bar`** — 64px height, white canvas, 1px `{colors.hairline}` bottom border. Logo anchored left; category links centered using `{typography.nav-link}` (Proxima Nova 14px/500); cart, account, and search icons right. The active category link shifts to `{colors.primary}` at weight 600. Below 744px the category links collapse into a hamburger drawer; top bar retains logo, search, and cart icons.

### Product Card
**`product-card`** — 1:1 image crop, white background, 1px `{colors.hairline}` border, `{rounded.sm}` radius. Title renders in `{typography.title-sm}` (Museo Slab 16px), price in `{typography.body-md}`. A horizontal chip row of `feature-badge` components sits below the image identifying filter type, connectivity, and compatibility certifications. A `sale-badge` overlays the top-left image corner when a promotional price is active.

### Hero
**`hero-section`** — Deep-teal-to-mid-teal gradient (from `{colors.teal-deep}` to `{colors.primary}`) carries the primary campaign and seasonal launch heroes. White headline in `{typography.display-xl}` (DIN 48px/700) sits left-aligned at desktop; product photography floats right on a transparent or cut-out background. The primary CTA button renders in its standard teal-on-teal treatment using a white-outlined variant for legibility over dark backgrounds.

**`hero-mint-gradient`** — Alternate hero treatment using the mint-to-bright-teal gradient (`{colors.teal-mint}` → `{colors.teal-bright}`) for spring campaigns and new-product launches where a lighter, more energetic tone fits the moment. Text renders dark (`{colors.ink}`) because the lighter mint cannot sustain white type contrast.

### Feature & Filter Badges
**`feature-badge`** — Compact solid-teal chips using `{typography.badge-label}` (DIN 11px/700 uppercase) at `{rounded.xs}` radius. Labels filter tiers (HEPA H13), connectivity (Smart Wi-Fi), and compatibility (Works with Alexa) on product pages and cards.

**`feature-badge-outline`** — White-fill, teal-border variant of the feature badge. Appears on dark hero backgrounds where the solid chip would be lost in the teal fill.

**`sale-badge`** — Yellow (`{colors.accent-yellow}`) chip with black label. The only warm-spectrum element on the product card; reads as immediately distinct in listing grids.

**`filter-indicator`** — Pill-shaped (`{rounded.full}`) status indicator for filter life state. Healthy status uses `{colors.teal-mint}` fill; the color walk from mint toward amber and then red communicates urgency without breaking the teal family at healthy and semi-healthy states.

### Metric & Specification Displays
**`metric-card`** — White card at `{rounded.md}` radius. The metric value renders in `{typography.metric-display}` (DIN 36px/700) in `{colors.primary}`, with a descriptor label below in `{typography.caption}`. Used in comparison tables and spec callout rows for values like CADR, room coverage (sq ft), and noise level (dB).

**`specification-row`** — Hairline-divided table rows: left-column label in `{colors.muted}` at `{typography.body-sm}`, right-column value in `{colors.ink}`. The alternation-free white background keeps long spec tables from reading as dense grids.

### Lifestyle & App Sections
**`lifestyle-section`** — Warm beige (`{colors.surface-soft}` = #dacebf) section background used on homepage feature rows where Levoit products appear in domestic settings. Breaks the white-or-dark-teal alternation with a neutral temperature shift.

**`app-connect-banner`** — Deep teal (`{colors.teal-deep}`) card with mint-colored accent text and a VeSync app UI mockup or QR tile. Title in `{typography.display-sm}`, body in `{typography.body-sm}`. Communicates smart home integration, voice assistant compatibility, and app-based scheduling.

### Category Navigation
**`category-pill`** — Muted gray rounded pills at `{rounded.full}` radius in Proxima Nova 13px, populating the product-filter bar. Selected state fills teal (`{colors.primary}`) with white label in `{colors.on-primary}`.

### Reviews
**`review-card`** — White card with hairline border and `{rounded.sm}` radius. Star rating renders in `{colors.accent-yellow}`, title in `{typography.title-sm}` (Museo Slab), body copy in `{typography.body-sm}`. Arranged in a horizontally scrolling carousel at desktop, single column at mobile.

### Footer
**`footer`** — Near-black canvas (`{colors.ink}`), white body text, mint links (`{colors.teal-mint}`) for accessibility contrast on dark. Four columns at desktop (Shop, Support, About, Connect), collapsing to accordions on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text stacks above product image with full-width gradient; nav collapses to hamburger drawer; metric cards scroll horizontally; specification rows stack label/value vertically; footer columns become accordions |
| Tablet | 744–1128px | Two-column product grid; hero side-by-side layout; nav shows top-level categories; metric cards in 2-column grid; search bar in header |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with dropdown category panels; hero full-bleed gradient; metric cards in 4-column row |
| Wide | > 1440px | Content max-width capped ~1400px, centered; hero maintains proportions; product grid holds at 4 columns with increased card padding |

### Touch Targets
- All buttons and pill filter controls minimum 44px height on mobile
- Category filter pills have a 44px minimum tap area even when visually shorter
- Nav icons (cart, account, search) padded to 44×44px tap targets
- Full product card face is tappable — not just the title or image
- Filter-indicator chips padded to 36px minimum height on touch viewports

### Collapsing Strategy
- Nav: hamburger drawer below 744px; top bar retains logo, search bar, and cart/account icons
- Footer: four-column link grid collapses to `<details>` accordions below 744px
- Metric cards: 4-column → 2-column below 1128px → horizontal scroll below 744px
- Specification tables: scroll horizontally below 744px; label/value stacks vertically below 480px
- Hero headline scales from 48px (desktop) to 32px (tablet) to 28px (mobile) using `{typography.display-xl}` → `{typography.display-md}` → `{typography.display-sm}` breakpoint swap
- Feature badge chips on product cards wrap to two rows on mobile rather than truncating

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- White canvas (`#ffffff`) is inferred; the extraction contains no explicit white, and the brand may use a very slightly off-white background not captured
- Sun Valley font has no widely-documented scale or weight spec; appears to be a campaign-display typeface only — omitted from functional typography tokens
- Exact nav height and sticky-scroll behavior not confirmed from extraction; 64px is a Shopify-DTC estimate
- Dark mode / night-mode palette not observed in extraction
- Gradient stop ordering for the mint hero variant (#64edc2 leading vs trailing) not confirmed from live extraction
- Secondary gray surface (`{colors.surface-muted}` = #f5f5f5) inferred from DTC convention; not directly in extracted hex list
- VeSync app badge artwork, icon glyph set, and QR code treatment not extractable from hex data
- Blue-soft (#a3bff0) appears in extracted palette but its specific usage context (promotional banner, informational callout, or link state) is unconfirmed
