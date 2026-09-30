---
version: alpha
name: "GE"
source_url: "https://www.geappliances.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  GE Appliances anchors its entire digital palette in a saturated navy — #092c74 — that the General Electric marque has carried since the mid-twentieth century, now applied as solid rectangular fills across the persistent navigation bar, primary CTAs, and major section headings with no gradient softening or transparency. The sharpness is deliberate: interactive corners default to `{rounded.none}`, a hard-edge philosophy that separates GE from the rounded, consumer-friendly conventions of post-2020 direct-to-consumer entrants. The effect reads as American institutional confidence — reliable infrastructure, not lifestyle aspiration.

  Two custom web fonts structure the type system. Effra, a geometric humanist sans with open counters and slightly mechanical strokes, handles display headings and button labels — its uppercase tracking giving CTAs a catalog-grade authority. Nudista Web, a more condensed humanist with stronger x-height contrast, carries body copy and product specification tables, together producing the layered density appropriate when refrigerator capacity, energy certification, and cubic footage share a card with photography and pricing.

  The color system is unusually broad for an appliance brand. Beyond the navy primary and its interactive hover tone #1a63a2, the extracted palette maps five distinct accent channels: coral #f05a4f for flash-sale urgency banners; amber #ffbc00 for star ratings and in-cart rebate callouts; sage #acc37e reserved for ENERGY STAR and sustainability certification marks; deep magenta #a11f7f and its promotion-event sibling #db3eb1 for limited-time offers and rebate event branding; and a burnt rust #c54b25 that appears in lifestyle-photography editorial callbacks. Each accent operates as a semantic signal rather than decorative variety — the system is color-coded across certification tiers, urgency levels, and savings hierarchies.

  The canvas runs warm rather than clinical: #f4f3ef, a near-white with a cream undertone, forms the ground for product cards that sit against it with single-pixel hairline borders (#cfcfcf) and a modest `{rounded.sm}` corner. Photography aspect ratios are consistently square within card boundaries, maintaining grid regularity across wide refrigerators and compact countertop units. The grid is catalog-dense — six category slots span desktop width, three-column product cards at 1280px — collapsing to horizontal-scroll category tabs and two-column cards on tablet rather than breaking to a hamburger.

colors:
  primary: "#092c74"
  primary-active: "#003b71"
  primary-hover: "#1a63a2"
  primary-disabled: "#a1aeb7"
  accent-coral: "#f05a4f"
  accent-amber: "#ffbc00"
  accent-sage: "#acc37e"
  accent-magenta: "#a11f7f"
  accent-magenta-light: "#db3eb1"
  accent-rust: "#c54b25"
  ink: "#212226"
  body: "#393a37"
  muted: "#757575"
  muted-soft: "#717171"
  hairline: "#cfcfcf"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f4f3ef"
  surface-warm: "#f2f1f0"
  surface-card: "#f5f5f5"
  surface-blue-tint: "#f2f5f7"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#4496f6"
  link-dark: "#0056b4"
  info-light: "#dde8f1"
  info-medium: "#accef7"

typography:
  display-xl:
    fontFamily: "'effra', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'effra', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'effra', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'effra', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'effra', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'nudista-web', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'nudista-web', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'nudista-web', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'nudista-web', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'effra', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'effra', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'effra', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'effra', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'effra', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'nudista-web', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 10px 22px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-blue-tint}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.link-dark}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "2px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 48px 10px 40px
    height: 48px
    iconColor: "{colors.muted}"
    submitBackground: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitRounded: "{rounded.none}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    logoHeight: 32px
    borderBottom: none
  nav-mega-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xl} {spacing.section}"
    boxShadow: "0 8px 24px rgba(9,44,116,0.12)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    ctaTypography: "{typography.button-sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  energy-star-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  promo-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  rebate-badge:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackground: "{colors.accent-coral}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  hero-lifestyle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.none}"
    minHeight: 400px
  category-tab:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorderBottom: "3px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"
  star-rating:
    filledColor: "{colors.accent-amber}"
    emptyColor: "{colors.hairline}"
    ratingTypography: "{typography.caption-bold}"
  promo-banner-strip:
    backgroundColor: "{colors.accent-rust}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    padding: "{spacing.sm} {spacing.base}"
  info-callout:
    backgroundColor: "{colors.info-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderLeft: "4px solid {colors.primary-hover}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    headerBackground: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.title-sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.info-medium}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Solid #092c74 navy fill with uppercase Effra at `{typography.button-md}`, 0.5px letter-spacing amplifying the label's institutional weight. Height locks at 48px with `{rounded.none}` corners everywhere — hover shifts the fill to the lighter interactive navy `{colors.primary-hover}` (#1a63a2), active compresses to the darker `{colors.primary-active}` (#003b71), disabled renders in the blue-gray `{colors.primary-disabled}` at 70% opacity.

**`button-secondary`** — Canvas background with a 2px solid `{colors.primary}` border and matching navy label text. Hover floods the interior with `{colors.surface-blue-tint}` and darkens the border to `{colors.primary-active}`. Applied to secondary product actions: Compare, Add to Wishlist, Learn More.

**`button-ghost`** — Transparent, borderless; `{colors.link-dark}` underlined label at `{typography.button-sm}`. Used inline within spec sections, footnote areas, and secondary editorial CTAs where adding a bordered button would create visual clutter.

### Navigation

**`nav-bar`** — Full-width navy bar at 60px height; `{colors.primary}` background carries the GE monogram logo (32px tall) at far left and search, cart, and account icons at far right in `{colors.on-primary}`. A secondary row below renders the product category labels in `{typography.nav-link}` against the same navy. Hovering a category label drops the `nav-mega-panel` with no delay.

**`nav-mega-panel`** — Full-viewport-width overlay in `{colors.canvas}`, topped with a 3px solid `{colors.primary}` rule that visually connects the panel back to the nav bar. Category sections are icon-led column groups in `{typography.body-sm}`; a drop shadow set to 12% navy opacity at 8px vertical prevents the panel from appearing to float independently. Panel closes on outside click or category re-hover.

### Product Cards

**`product-card`** — White card with a single hairline border (`{colors.hairline}`), `{rounded.sm}` corner, and a square product photography region at top. The product title renders in `{typography.title-sm}` (Effra 600, 16px); price in `{typography.price-display}` (Effra 700, 22px). A CTA button in `{typography.button-sm}` sits at card bottom, full-width. Badge slots layer at the image top-left — a single refrigerator may carry both a coral sale badge and a sage ENERGY STAR badge simultaneously, stacked vertically.

**`product-card-badge`** — Hard-cornered chip in `{colors.accent-coral}` (#f05a4f) for sale and clearance marks. Uppercase Effra at 11px with 0.5px tracking gives the badge readable density at thumbnail scale.

**`energy-star-badge`** — Same hard-cornered chip geometry in `{colors.accent-sage}` (#acc37e) with white type. The muted sage is intentional — sustainability certification reads as institutional endorsement, not marketing-bright green.

**`promo-badge`** — Amber `{colors.accent-amber}` (#ffbc00) with dark `{colors.ink}` text for dollar-amount savings callouts ("Save $200") on cards and within hero panels.

**`rebate-badge`** — Deep magenta `{colors.accent-magenta}` (#a11f7f) for seasonal manufacturer rebate events. The lighter sibling `{colors.accent-magenta-light}` (#db3eb1) surfaces in the corresponding promotional hero banners and email headers during rebate event windows.

### Hero Panels

**`hero-banner`** — Full-bleed navy panel (`{colors.primary}`) with left-aligned headline in `{typography.display-xl}` (Effra 700, 40px) and a coral CTA (`{colors.accent-coral}`, `{rounded.none}`). Lifestyle photography bleeds edge-to-edge at right on desktop; stacks above the text block on mobile. Min-height 480px with `{spacing.section}` top and bottom padding on desktop.

**`hero-lifestyle`** — Warm surface (`{colors.surface-soft}`) variant for editorial mid-page modules: kitchen remodel bundles, whole-home appliance suites. Title at `{typography.display-lg}`, CTA in standard navy primary. Used between product grid sections to break catalog density with an editorial register.

### Utility Components

**`star-rating`** — Filled stars in `{colors.accent-amber}` (#ffbc00), empty stars in `{colors.hairline}`. Review count and rating score render in `{typography.caption-bold}` directly beside the star row.

**`promo-banner-strip`** — Rust-colored `{colors.accent-rust}` (#c54b25) full-width strip with `{typography.caption-bold}` in `{colors.on-primary}`. Used for site-wide promotional messages, free-shipping threshold callouts, and limited-time countdown notices.

**`info-callout`** — `{colors.info-light}` (#dde8f1) tinted panel with a 4px `{colors.primary-hover}` left border. Applied to shipping lead-time notices, installation requirement disclosures, and rebate eligibility explanations. Corner at `{rounded.xs}`.

**`spec-table`** — Alternating `{colors.surface-soft}` row fills for refrigerator specification detail: capacity, dimensions, energy consumption, noise rating. Header row in solid `{colors.primary}` / `{colors.on-primary}`. Label column in `{typography.spec-label}` (Nudista 13px, regular), value column in `{typography.body-sm}`. Used on PDP below the product photography and pricing block.

**`footer`** — Near-black `{colors.ink}` ground with a 3px `{colors.primary}` top border marking the transition from page content. Column headings in `{typography.title-sm}` / `{colors.canvas}`; link text in `{colors.info-medium}` (#accef7, a muted sky blue) hovering to full `{colors.canvas}` white. Four to five columns on desktop: Products, Support, About GE, Rebates & Promotions, Trade Partners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category tabs become horizontal-scroll strip with left/right arrows; hero stacks image above text; nav becomes hamburger with left-slide drawer; mega-panel replaced by accordion; badge text collapses to icon-only at narrow widths |
| Tablet | 744–1128px | Two-column product grid; category tabs maintain full horizontal bar (no hamburger); hero splits 50/50 text and image; spec tables scroll horizontally within card |
| Desktop | 1128–1440px | Three-column product grid; six-slot category nav inline; full mega-panel on hover; hero at minimum 480px with photography bleed to right edge |
| Wide | > 1440px | Content max-width ~1440px centered with side gutters; hero photography expands but text column caps at ~560px; product grids gain a fourth column at extreme widths |

### Touch Targets

- All tappable nav items and category tabs: minimum 44×44px interactive area
- Product card CTA button: full-width on mobile at 48px height
- Badge chips receive 8px additional invisible tap padding on mobile via wrapper expansion
- Star rating row (when used as filter control) expands to 44px row height for reliable tap
- Search submit button: minimum 44×44px hit area regardless of visible size

### Collapsing Strategy

- Desktop mega-nav collapses to hamburger drawer at < 744px; drawer slides in from left with accordion category groups in `{typography.title-sm}`
- Six-slot category grid collapses to horizontally scrollable tab strip at tablet, then a strip with forward/back scroll controls at mobile
- Hero two-column layout stacks vertically on mobile: lifestyle hero places image first, promotional hero places headline and CTA first
- Spec tables use horizontal overflow scroll container on mobile rather than reflowing columns — preserves tabular alignment across wide specification sets
- Footer five-column grid collapses to two columns at tablet, single-column accordion at mobile with headings as expand triggers

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius values not confirmed from CSS extraction; `{rounded.sm}` (8px) for product cards and `{rounded.none}` for buttons are inferred from visual inspection of the live site
- Font weight and size values for Effra and Nudista Web are estimated from brand typographic conventions; no raw CSS pixel declarations were extracted
- The magenta accent pair (#a11f7f, #db3eb1) appears campaign-scoped — likely active only during GE rebate event windows, not part of evergreen UI; confirm persistence before applying to permanent components
- GE Profile, GE Café, and Monogram sub-brands each carry distinct color treatments (slate, matte brass, graphite) not captured here — this spec covers base geappliances.com branding only
- No animation or transition duration values were extracted; motion design tokens (easing curves, durations) are unspecified
- Mega-nav category icon set not accessible from static extraction; icon style (stroke weight, fill vs. outline) and grid size are unknown
- No dark mode or high-contrast accessibility mode variants observed in the extraction pass
- #4496f6 and #0056b4 link color roles are partially inferred; the precise distinction between interactive link blue and primary navy in inline body-copy contexts requires a full CSS audit
