---
version: alpha
name: "Rolling Square"
source_url: "https://rollingsquare.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The company calls itself "The lifehackers company" and then proves it with a color-coded product matrix where sky blue (#7fd7ff), teal (#108474), amber (#ffc100), salmon (#ff7f7f), lavender (#a89cc8), mint (#c1e6e6), and electric green (#17e260) each map to a cable finish or hub variant — a paint-chip logic where the palette encodes the SKU rather than decorating it. Basier Square Mono anchors the technical vocabulary: port labels, wattage specs, cable-length callouts set in a grid-aligned monospace that signals exactness over style. Montserrat handles display hierarchies at weight 700, providing geometric punch without serif softness; Inter carries body copy at comfortable reading weight. The meta theme color is black (#000000) — the nav and top chrome hold that dark register while product content lifts to a near-white canvas (#f2f2f2, #f9fafb), a dark-light toggle that frames each product photograph as primary information rather than surrounding UI. Cards sit on tight radii ({rounded.sm}) so the hardware itself reads as the dominant shape on screen. Deep navy (#004d8b) carries high-priority CTAs at a contrast weight that works equally on the light product grid and the dark global header — it is a different register from the sky-blue accent, colder and more decisive. Rolling Square's real design language is the spec table: amperage, compatibility matrices, and exact millimeter lengths set in Basier Square Mono on neutral backgrounds, a visual argument that the person buying a USB-C hub wants truth before advertising. Multiple product-line accent colors allow variant selectors to be parsed at a glance across the catalog without text labels — the color encodes the difference, the mono type confirms it.

colors:
  primary: "#7fd7ff"
  primary-hover: "#5bc8ff"
  primary-dark: "#004d8b"
  primary-dark-active: "#003a6b"
  primary-disabled: "#c1e6e6"
  accent-teal: "#108474"
  accent-amber: "#ffc100"
  accent-salmon: "#ff7f7f"
  accent-green: "#17e260"
  accent-lavender: "#a89cc8"
  accent-mint: "#c1e6e6"
  accent-red: "#8b0000"
  ink: "#1a1a1a"
  body: "#242728"
  muted: "#555555"
  muted-soft: "#888888"
  hairline: "#dfdfe1"
  hairline-soft: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#f9fafb"
  surface-mid: "#eeeeee"
  surface-dark: "#242728"
  on-primary: "#1a1a1a"
  on-primary-dark: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-label:
    fontFamily: "'Basier Square Mono', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-spec:
    fontFamily: "'Basier Square Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
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
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-cta-dark:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-cta-dark-active:
    backgroundColor: "{colors.primary-dark-active}"
    textColor: "{colors.on-primary-dark}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid rgba(255,255,255,0.35)"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary-dark}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspectRatio: "1/1"
    hoverElevation: "0 4px 16px rgba(0,0,0,0.10)"
  product-card-name:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-variant-dot:
    width: 16px
    height: 16px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    selectedInnerRing: "2px solid {colors.canvas}"
  color-variant-swatch:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
    selectedInnerRing: "2px solid {colors.canvas}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.mono-spec}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.mono-label}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.sm} {spacing.base}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.muted-soft}"
    minHeight: 520px
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-accent:
    accentColor: "{colors.primary}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
  section-divider:
    backgroundColor: "{colors.surface-mid}"
    padding: "{spacing.section} 0"
  compatibility-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.mono-spec}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Sky-blue (#7fd7ff) fill with near-black text ({colors.on-primary}), uppercase Montserrat 14px/700 at 0.5px tracking. Corners use {rounded.xs} (4px), keeping the shape crisp and hardware-adjacent. Hover transitions to {colors.primary-hover} (#5bc8ff). Used for secondary product actions and filter confirmations where the full-navy CTA weight would overpower.

**`button-cta-dark`** — The high-conversion variant: deep navy ({colors.primary-dark}, #004d8b) with white text, same uppercase Montserrat type. Carries Add to Cart and Buy Now across both the light product grid and the dark header — the navy holds authority in both contexts where the sky-blue primary would lose contrast on dark surfaces.

**`button-secondary`** — White fill ({colors.canvas}) with 1px hairline border, dark text. Paired alongside the primary CTA on product pages for secondary actions such as "Learn More" or "See Compatibility." Hover darkens the border to {colors.muted}.

**`button-ghost-dark`** — Transparent with a semi-opaque white border (rgba 35%), used on dark hero sections and the footer to keep CTAs legible without disrupting the dark-canvas register.

### Text Input

**`text-input`** — White fill, 1px hairline border ({colors.hairline}), 48px height, {rounded.xs} corners. Focus state upgrades the border to {colors.primary-dark} (navy), tying the focus moment to the CTA color language. Placeholder text in {colors.muted-soft} (#888888) using {typography.body-md}.

### Navigation

**`nav-bar`** — Fixed 64px dark bar ({colors.surface-dark}, #242728). Links in {typography.nav-link}: Montserrat 13px/600/0.3px tracking, white. No bottom border — the dark-to-light page transition handles the visual break. Logo set in {typography.display-sm}.

### Product Card

**`product-card`** — Light surface ({colors.surface-card}, #f9fafb) with {rounded.sm} corners and no visible border. Product image fills a square container at 1:1. Name in {typography.title-md} (Montserrat 18px/600), price in {typography.price-display} (Montserrat 22px/700). Hover adds 0 4px 16px rgba(0,0,0,0.10) elevation.

**`product-card-variant-dot`** and **`color-variant-swatch`** — The core SKU-navigation mechanism. Small 16px dots for card-grid previews; full 24px swatches on detail pages. Both use the brand accent palette — sky blue ({colors.primary}), teal ({colors.accent-teal}), amber ({colors.accent-amber}), salmon ({colors.accent-salmon}), lavender ({colors.accent-lavender}), mint ({colors.accent-mint}) — as the variant signal. Selected state uses a two-ring system: ink border with a canvas inner ring, a convention borrowed from apparel that communicates selection without an additional label.

### Spec Table

**`spec-table`** — The brand's most distinctive UI pattern and its clearest design statement. A two-column grid on {colors.surface-soft} with Basier Square Mono at two scales: {typography.mono-spec} (11px) for row labels in {colors.muted}, and {typography.mono-label} (13px) for values in {colors.ink}. Hairline dividers between rows, {spacing.sm}/{spacing.base} padding per cell, {rounded.sm} outer container. The monospace typeface transforms wattage ratings, port counts, and cable lengths from marketing bullets into engineering data.

**`compatibility-tag`** — Inline chips for compatibility callouts ("USB-C", "Thunderbolt 4", "MFi Certified") in {typography.mono-spec} on a light surface with hairline border and {rounded.xs}. Non-interactive; sits within or below the spec table.

### Badges

**`product-badge`** — Sky blue (#7fd7ff) with {typography.mono-label} in Basier Square Mono and {colors.on-primary} text. Used for product-line name callouts.

**`product-badge-new`** — Electric green ({colors.accent-green}, #17e260) with ink text. High-visibility launch signal — the green reads as live/active against both light and dark surfaces.

**`product-badge-sale`** — Amber ({colors.accent-amber}, #ffc100) with ink text. Intentionally shares its color with the amber cable variant so sale states on amber-variant SKUs create a visual rhyme across the grid.

### Category Filtering

**`category-chip`** — Pill-shaped ({rounded.full}) filter tags in {colors.surface-soft} with {typography.title-sm} (uppercase Montserrat/700). Active state inverts to {colors.ink} fill with {colors.on-dark} text — a clean binary toggle without decorative borders. On mobile, chips scroll horizontally in a single row.

### Hero

**`hero-banner`** — Dark-canvas ({colors.surface-dark}) section at minimum 520px tall. Title in {typography.display-xl} (Montserrat 48px/700/−1px tracking), white. Subtitle in {typography.body-md} (Inter 16px/400) in {colors.muted-soft}. A single thin horizontal accent rule or icon glyph in {colors.primary} (sky blue, #7fd7ff) punctuates the monochrome field. The hero anchors the page's structural dark-light flip: dark top, light product content, dark footer.

### Footer

**`footer`** — Dark surface ({colors.surface-dark}) that mirrors the nav, sandwiching the light product content between two dark registers. Column headings in {typography.title-sm} (uppercase Montserrat) in {colors.on-dark}. Links in {typography.body-sm} (Inter 14px) in {colors.muted-soft}. {spacing.xxl} vertical padding maintains the section rhythm of the rest of the page.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer; hero shrinks to 360px min-height; spec table scrolls horizontally; variant swatches stack below product image; category chips scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav collapses to logo + cart + hamburger; hero at 440px min-height; product detail switches to side-by-side image/info layout |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav; hero at 520px; spec table sits alongside images in a 55/45 split; category chip row pinned below nav on collection pages |
| Wide | > 1440px | Content capped at 1440px centered; product grid can extend to five columns on collection pages; hero image bleeds full-width behind a constrained text column |

### Touch Targets

- All buttons minimum 48px height
- Variant swatches (24px visual) wrapped in a 44px touch target
- Nav links and hamburger icon minimum 44×44px tap area
- Category chips minimum 40px height
- Compatibility tags and badges are display-only; no minimum tap height required

### Collapsing Strategy

- Global nav collapses to hamburger at < 744px; logo and cart icon remain in the fixed header bar
- Category/filter chips transition from a static row to a horizontally scrolling single-line rail on mobile
- Spec tables reformat from two-column grid to stacked label-above-value card rows on mobile
- Hero CTAs stack vertically to full-width at < 744px
- Footer multi-column layout collapses to tap-to-expand accordion sections on mobile while maintaining the dark-surface backdrop

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed font-size scale from extraction; sizes derived from Shopify theme conventions and Montserrat/Inter standard pairings for this product category
- Basier Square Mono confirmed in font-family stack but weight variants (400 vs 500) and exact size usage contexts not extractable from CSS font lists alone
- Border-radius values not directly extracted; {rounded.xs} (4px) inferred from typical tech-accessory Shopify themes with tight-corner aesthetics
- Whether the black meta theme color (#000000) indicates a true dark-mode experience or only applies to the nav/header against a light product canvas is ambiguous from extraction data alone
- Whether #7fd7ff functions as a singular brand primary or as one of several equal-weight product-line accent colors is not resolvable from extraction; it may be the color of one specific cable family rather than a universal brand marker
- No icon set, illustration style, or motion/animation timing data extractable from the provided hints
- Exact grid column counts, gutter widths, and responsive breakpoint pixel values not extracted; values above are estimated from Shopify theme defaults
- Hover and focus state transition durations not confirmed
