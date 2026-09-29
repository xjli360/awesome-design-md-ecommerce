---
version: alpha
name: "Alen"
source_url: "https://www.alen.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  ITC Avant Garde Gothic — the geometric typeface born for a 1970s counterculture magazine that never published — sets Alen's entire visual register before the first hero image loads: its perfectly circular letterforms and rhythmic negative space communicate engineered precision without a word. Against that structural typography, the brand's operative color is a medical teal centered on #00b2a9, a hue that reads simultaneously clinical and biological. It carries every primary CTA, every active filter pill, every progress ring in the air-quality module, and the airflow illustrations that distinguish Alen from generic white-box appliance brands. A deep navy-slate (#364151) grounds headings and structural text; near-black (#141414) and a dark charcoal shell (#121212) back hero sections so the teal glows with genuine contrast rather than relying on a white field. The page ground itself leans teal — surface-mint (#f4f9f9) appears behind product listings and spec cards, tinting the entire catalog with the faintest reminder of what the machine does to air. A coral-orange (#f3712a) and amber (#f59e0b) accent pair reserves itself for promotional urgency: countdown banners, clearance badges, and limited-stock callouts pop against the cool palette without disrupting it. Geometry is rounded but never bubbly — inputs and product cards sit at {rounded.sm} (8px), standard buttons at {rounded.md} (12px), filter pills at {rounded.full} — conveying approachability inside a precise, geometric frame. Montserrat handles interface copy at weight 600 for labels and 400 for prose, partnering with ITC Avant Garde Gothic on display headlines. Section rhythm is deliberate: {spacing.section} (64px) between content bands, {spacing.lg} (24px) inside cards, {spacing.xxl} (48px) above fold-break CTAs — spacing that positions Alen as a considered home system rather than a budget appliance. HEPA certification marks, room-coverage sq-ft callouts, and filter-life indicators appear inline with product titles as data-dense chips, treating performance statistics as primary brand expression rather than spec-sheet fine print.

colors:
  primary: "#00b2a9"
  primary-active: "#00918f"
  primary-disabled: "#bee6e3"
  primary-deep: "#126072"
  teal-mid: "#00a4a1"
  teal-light: "#bee6e3"
  ink: "#141414"
  body: "#364151"
  muted: "#6d6d6d"
  muted-soft: "#6b6c6c"
  hairline: "#dde0e3"
  hairline-soft: "#dfe5e6"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-mint: "#f4f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  dark-shell: "#121212"
  dark-alt: "#1f1f1f"
  accent-orange: "#f3712a"
  accent-amber: "#f59e0b"
  success: "#198754"
  scrim: "#000000"

typography:
  logo-display:
    fontFamily: "'ITC Avant Garde Gothic', 'Avant Garde', Montserrat, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
  display-xl:
    fontFamily: "'ITC Avant Garde Gothic', 'Avant Garde', Montserrat, sans-serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -1px
  display-lg:
    fontFamily: "'ITC Avant Garde Gothic', 'Avant Garde', Montserrat, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ITC Avant Garde Gothic', 'Avant Garde', Montserrat, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'ITC Avant Garde Gothic', 'Avant Garde', Montserrat, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "Montserrat, Poppins, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Montserrat, Poppins, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Montserrat, Poppins, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Montserrat, Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Montserrat, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Montserrat, Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Montserrat, Poppins, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Montserrat, Poppins, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "Montserrat, Poppins, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "Montserrat, Poppins, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  label-upper:
    fontFamily: "Montserrat, Poppins, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 52px
    transition: background-color 150ms ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 52px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 52px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 26px
    height: 52px
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "2px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 26px
    height: 52px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.logo-display}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    titleColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.title-lg}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
    imageBackground: "{colors.surface-mint}"
    hoverShadow: "0 4px 16px rgba(0,178,169,0.12)"
  hero-section:
    backgroundColor: "{colors.dark-shell}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleOpacity: 0.8
    minHeight: 600px
    paddingVertical: "{spacing.section}"
  promo-banner:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    padding: "{spacing.sm} {spacing.lg}"
    textTransform: uppercase
  promo-banner-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    padding: "{spacing.sm} {spacing.lg}"
    textTransform: uppercase
  hepa-badge:
    backgroundColor: "{colors.primary-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: none
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
  air-quality-chip:
    backgroundColor: "{colors.teal-light}"
    textColor: "{colors.primary-deep}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
    border: "1px solid {colors.primary}"
  coverage-stat:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.body}"
    valueTypography: "{typography.display-sm}"
    labelTypography: "{typography.label-upper}"
    valueColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  trust-strip:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    padding: "{spacing.lg} 0"
    borderTop: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.dark-alt}"
    textColor: "{colors.on-dark}"
    mutedColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    paddingVertical: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Alen's medical teal (#00b2a9) as a solid fill, white Montserrat at 700 weight with 0.5px tracking, 12px corner radius, 52px height. On hover the fill shifts to {colors.primary-active} (#00918f) in 150ms; disabled states drain to the mint-tinted {colors.primary-disabled} with {colors.muted} text. Standard labels: "Shop Now", "Add to Cart", "Build My System".

**`button-secondary`** — Outlined in 2px {colors.primary} with teal text on a transparent ground, mirroring primary's 52px height and {rounded.md} radius. The dark-surface variant (`button-secondary-dark`) reverses to a white border and white text for placement over {colors.dark-shell} hero sections. Used for "Learn More", "Compare Models", and "View Specs".

**`button-ghost`** — Text-only in {colors.primary} with no border or fill; zero padding. Reserved for tertiary in-context actions such as "See all filters" and "View full specs" within product cards where adding another bordered button would create visual clutter.

### Text Input

**`text-input`** — White fill, 1px {colors.hairline} border, {rounded.sm} corners, 48px height. Focus state fattens the border to 2px {colors.primary} with no box-shadow bleed — clean and clinical, matching the brand's precision register. Placeholder text at {colors.muted}. Appears in site search, email capture, filter sidebars, and chat/support widgets.

### Navigation

**`nav-bar`** — White canvas at 72px height with a 1px {colors.hairline-soft} bottom border, collapsing to 64px on scroll with a soft drop-shadow. The Alen wordmark renders in {typography.logo-display} (ITC Avant Garde Gothic, 700, 24px). Navigation links use {typography.nav-link} (Montserrat 600, 14px) in {colors.body}; the primary shop CTA in the right cluster takes the full `button-primary` treatment at reduced padding. On scroll the shadow cues depth without introducing color change.

### Product Card

**`product-card`** — White fill, 1px {colors.hairline-soft} border, {rounded.sm} corners. On hover a teal-tinted shadow (rgba(0,178,169,0.12)) lifts the card without shifting position. The product image zone uses {colors.surface-mint} as its background — that faint teal tint unifies the grid even before images load. Title at {typography.title-md} in {colors.ink}; price at {typography.title-lg}; prose at {typography.body-sm} in {colors.body}. A badge row of `hepa-badge` and `air-quality-chip` elements sits between the image and the title, treating certification data as visual hierarchy rather than footnote.

### Hero Section

**`hero-section`** — Full-bleed {colors.dark-shell} (#121212) ground with product rendered large-format, floating on an unmodified dark field. Headline at {typography.display-xl} in {colors.on-dark}; subtitle at {typography.body-md} with 0.8 opacity. Two CTAs sit horizontally: solid teal `button-primary` and white-outline `button-secondary-dark`. Minimum height 600px; top and bottom padding at {spacing.section}. The dark hero creates maximum contrast with the teal CTA — the brand's most important conversion surface.

### Promo Banner

**`promo-banner`** — A full-width strip pinned above the nav in {colors.accent-orange} (#f3712a) for flash sales ("TODAY ONLY — 20% OFF") or {colors.accent-amber} (#f59e0b) for threshold offers ("FREE SHIPPING OVER $75"). Text at {typography.badge}, uppercase, 0.5px tracking. No border-radius; the banner runs edge-to-edge. The amber variant reverses to {colors.ink} text since amber is insufficiently dark for white legibility.

### Badges

**`hepa-badge`** — A compact chip in {colors.primary-deep} (#126072) with {colors.on-primary} text at {typography.label-upper}; {rounded.xs} corners, tight horizontal padding. Surfaces certification tier: "True HEPA", "H13", "Medical Grade". Sits in a badge row directly above the product title on cards and PDPs.

**`air-quality-chip`** — Mint fill ({colors.teal-light}) with {colors.primary-deep} text at {typography.caption}, 1px {colors.primary} border. Visually lighter than `hepa-badge`; used for performance callouts like "Up to 1300 sq ft" and "CADR 300". The transparent-feeling fill distinguishes it from the opaque certification badge while keeping both in the same teal family.

### Filter Pills

**`filter-pill`** / **`filter-pill-active`** — Horizontal pill-shaped category filters (Home, Business, Bedroom, Large Room, etc.). Inactive: {colors.surface-soft} fill, {colors.muted} text, 1px hairline border. Active: solid {colors.primary} fill, {colors.on-primary} text, no border — the same teal-to-white flip as the primary button. Both at 36px height, {rounded.full} corners. Pills scroll horizontally in a no-wrap row on mobile to preserve vertical space.

### Coverage Stat

**`coverage-stat`** — A data tile in {colors.surface-mint} with the numeric value rendered at {typography.display-sm} (ITC Avant Garde Gothic) in {colors.primary} and a {typography.label-upper} descriptor below in {colors.body}. Used in PDP spec strips and product comparison panels to surface sq-ft coverage, CADR ratings, and fan-speed counts as branded callouts rather than tabular rows. The ITC Avant Garde geometric numerals make performance data feel like design, not documentation.

### Trust Strip

**`trust-strip`** — A full-width band in {colors.surface-mint} with Font Awesome icon glyphs tinted {colors.primary} and {typography.body-sm} labels in {colors.body}. Typical nodes: "Lifetime Warranty", "60-Day Returns", "Free Shipping", "USA-Based Support". Sits between the hero and the product grid; the mint ground echoes the card image zone, stitching the two sections together visually.

### Footer

**`footer`** — Dark ground in {colors.dark-alt} (#1f1f1f) with {colors.on-dark} body text at {typography.body-sm}; column headings at {typography.title-sm} (Montserrat 600); muted links in {colors.muted-soft}. The teal brand wordmark reappears in the footer logo at {typography.logo-display}, completing the dark-to-dark vertical bookend from hero to footer. No top border; the transition from the last light section is handled by a full-bleed background color change.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to {typography.display-md}; nav collapses to hamburger with full-screen drawer over {colors.dark-shell}; filter pills scroll horizontally in a no-wrap row; promo banner wraps to two lines; hero CTAs stack vertically |
| Tablet | 744–1128px | Two-column product grid; hero at {typography.display-lg}; nav shows primary links only with overflow in a dropdown; coverage-stat tiles reflow to 2-up; trust-strip wraps to 2×2 |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at {typography.display-xl}; filter pills in a wrapping row; trust-strip shows all items inline; coverage stats in a 4-up row |
| Wide | > 1440px | Content max-width 1440px centered; product grid optionally 4-column; hero background extends edge-to-edge beyond max-width; promo banner always full-viewport-width |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch target on mobile viewports
- Filter pills gain additional vertical padding on touch screens to reach 44px height while keeping {rounded.full} shape
- Product cards are fully tappable on mobile with no ambiguous sub-target zones; the badge row does not intercept the card tap

### Collapsing Strategy

- Nav collapses behind a hamburger icon below 744px; mega-menu becomes a full-screen left drawer with {colors.dark-shell} scrim overlay
- Hero CTAs stack vertically at < 744px; secondary button drops below primary with {spacing.sm} gap
- Promo banner reduces to a marquee-scrolling single line on viewports below 375px to preserve vertical real estate
- Product comparison tables collapse to a swipeable card format at < 744px
- Footer columns collapse from 4-up to 2-up at tablet and single-column at mobile, with accordion toggles revealing link groups on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- ITC Avant Garde Gothic is almost certainly served as a licensed web font via a third-party CDN not visible in top-level extraction; the fallback stack (Montserrat) is confirmed present via font-family extraction
- Exact nav height on scroll and sticky/fixed behavior not confirmed; 64px scrolled value is inferred from common Shopify patterns
- Product card hover animation specifics (transform-scale vs. shadow-only vs. border-color shift) not determinable from static extraction
- Mega-menu column structure and depth not extractable; assumed multi-column dropdown based on product category breadth
- Whether #198754 (Bootstrap success green) is used for brand "in-stock" indicators or is a pure Bootstrap default could not be confirmed; excluded from primary palette
- Dark-mode support status unknown; no `prefers-color-scheme` media query tokens observed in extraction
- Review star color not confirmed from extraction; {colors.accent-amber} assumed by convention
- Promo banner countdown-timer animation styling (if present) not captured
- Exact letter-spacing on button labels (0.5px) is inferred from Montserrat-700 best practice rather than directly extracted
