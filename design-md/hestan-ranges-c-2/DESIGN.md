---
version: alpha
name: "Hestan"
source_url: "https://www.hestan.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep-teal precision: the color anchoring every Hestan surface — #226d7a — reads less like a branding decision and more like the patina of a well-seasoned copper line, the shade of a cold salt marsh at first light. Where most kitchen-equipment brands retreat into stainless silver and matte black, Hestan commits to an aquatic spectrum running from #226d7a at full saturation down through the glacial #b0e0e9 and the near-white #e4f5fa, building a chromatic argument about thermal clarity rather than raw power. This is not accidental: the flagship NanoBond and ProBond lines are defined by metallurgical precision and molecularly bonded layers, and the palette mirrors that logic — depth layered on depth, each hue a slightly different pressure of the same sea.

  Typography runs in Open Sans, a humanist sans that keeps technical specification tables readable without sacrificing warmth. Weights climb from 400 in body copy to 700 in display headers, with generous tracking on uppercase labels that lend the configurator and spec modules a laboratory quality. The type system annotates rather than shouts — the way engineering drawings mark tolerances.

  Rounded corners sit at the conservative end: `{rounded.xs}` on inline series badges, `{rounded.sm}` on input fields and product cards, `{rounded.md}` on primary CTAs. There are no pill shapes, no extreme radii — the geometry is closer to a professional appliance panel than a consumer app. The bright cyan accent (#22b8d1) appears selectively as a hover signal and interactive highlight, a burst of active energy against the measured teal ground. Surface hierarchy uses ice-blue tints (#e4f5fa for page-background wash, #b0e0e9 for selected and mid-surface states) so that even the neutral zones carry the brand's aquatic signature. Ink is near-black (#1a1a1a), body text a softened graphite (#3d3d3d), muted labels in medium gray — all calibrated to let stainless-steel product photography read at full contrast against the cool canvas.

colors:
  primary: "#226d7a"
  primary-active: "#1a5562"
  primary-hover: "#1e6d7a"
  primary-disabled: "#b0e0e9"
  accent-cyan: "#22b8d1"
  accent-cyan-hover: "#1da3ba"
  surface-teal-mid: "#b0e0e9"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#6b6b6b"
  hairline: "#d8d8d8"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#e4f5fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#c0392b"
  success: "#27ae60"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-lg:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.3px
  label-upper:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
    hover:
      backgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.md}"
    padding: 12px 26px
    height: 48px
    hover:
      backgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    shadow: "0 2px 12px rgba(0,0,0,0.08)"
    imageAspect: "4:3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    badgeTypography: "{typography.label-upper}"
    hover:
      shadow: "0 6px 20px rgba(0,0,0,0.12)"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    overlayColor: "rgba(34,109,122,0.45)"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
    ctaVariant: button-primary
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.primary}"
    headerTypography: "{typography.label-upper}"
    cellTypography: "{typography.body-sm}"
    valueTypography: "{typography.spec-value}"
    rowBorder: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
  badge-series:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.surface-soft}"
    activeTextColor: "{colors.primary}"
    activeBorder: "2px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 14px
    border: "1px solid {colors.hairline}"
  configurator-panel:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    labelTypography: "{typography.label-upper}"
    valueTypography: "{typography.title-sm}"
    accentColor: "{colors.primary}"
    selectedBorder: "2px solid {colors.primary}"
    selectedShadow: "0 0 0 3px {colors.surface-teal-mid}"
  swatch-selector:
    size: 32px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.primary}"
    selectedShadow: "0 0 0 3px {colors.surface-teal-mid}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    height: 44px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.accent-cyan}"
    height: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-teal-mid}"
    linkHoverColor: "{colors.accent-cyan}"
    headingTypography: "{typography.label-upper}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The main CTA carries Hestan's deep teal (#226d7a) at `{rounded.md}` — deliberate without softening to pill. At 48px height the button holds visual weight on both desktop configurator flows and mobile product pages. On hover it deepens to #1a5562; when disabled it retreats to the powder-blue `{colors.primary-disabled}` with muted text to communicate unavailability without visual conflict.

**`button-secondary`** — An outlined variant sharing the same `{rounded.md}` geometry: transparent fill with a 2px `{colors.primary}` border and teal label text. On hover a `{colors.surface-soft}` wash signals interactivity without committing full color. Used for secondary CTAs such as "Compare Models" or "Download Spec Sheet" adjacent to a primary "Shop Now."

**`button-ghost`** — Transparent, ink-colored, `{rounded.sm}`, for tertiary navigation actions like "View All" in section headers and breadcrumb contexts. No border; type weight at 600 provides the only affordance signal.

### Navigation

**`nav-bar`** — White canvas at 72px height with a `{colors.hairline-soft}` bottom rule. The Hestan wordmark renders in `{colors.primary}` teal. Nav links in `{typography.nav-link}` (14px/600) carry a teal underline on hover; the active category shows a persistent underline in `{colors.primary}`. On mobile the layout collapses to a hamburger icon that triggers a full-screen `{colors.ink}` overlay with accordion sub-navigation.

### Product Cards

**`product-card`** — Soft 1px `{colors.hairline-soft}` border, `{rounded.sm}` corners, and a 2px lifted shadow on hover. Series badges (`badge-series`) anchor to the top-left corner of the product image using `{typography.label-upper}` white labels on teal. Price appears in `{typography.title-md}` below the product name in `{typography.title-sm}`. "New" SKU status uses `badge-new` in accent cyan (#22b8d1) to distinguish from series designations.

### Hero

**`hero-banner`** — Full-bleed product or lifestyle photography with a 45%-opacity `{colors.primary}` teal overlay that preserves image detail while pulling the brand palette into every scene. Headline in `{typography.display-xl}` white sits in the upper third; subhead in `{typography.body-md}` below. The primary CTA button anchors center at the lower third. Minimum 560px desktop height; the overlay doubles as contrast insurance for accessibility.

### Spec Table

**`spec-table`** — The backbone of Hestan's product detail and configurator pages. The header row uses `{colors.surface-soft}` background with `{typography.label-upper}` rendered in `{colors.primary}`. Specification labels run in `{typography.body-sm}` graphite; values in `{typography.spec-value}` (14px/600) for scan-read clarity. Row separators use `{colors.hairline-soft}`; the whole table container sits on `{rounded.sm}`. On mobile the table scrolls horizontally with the label column frozen left.

### Badges

**`badge-series`** — Uppercase 11px/700 label in white on `{colors.primary}` teal, 4px 8px padding, `{rounded.xs}` corner — marks NanoBond, ProBond, and Thomas Keller Insignia product lines with consistent placement. **`badge-new`** — Identical geometry but uses `{colors.accent-cyan}` (#22b8d1) to flag new SKUs without diluting the series system. Neither badge shape ever reaches pill geometry; the sharp `{rounded.xs}` reads as product taxonomy, not marketing flair.

### Configurator Panel

**`configurator-panel`** — An ice-blue `{colors.surface-soft}` panel at `{rounded.md}` housing finish selectors, burner-count options, and BTU specifications. Labels in `{typography.label-upper}`, selected state: 2px solid `{colors.primary}` border plus a `{colors.surface-teal-mid}` outer glow ring via `selectedShadow`. Swatch selectors (`swatch-selector`) are 32px pill-shaped circles with matching selection ring — the only place `{rounded.full}` appears in the UI, isolating finish samples from the panel's rectilinear grid.

### Search

**`search-bar`** — 44px height, `{rounded.md}`, `{colors.surface-soft}` fill, teal icon left-inset. On focus the border upgrades from `{colors.hairline}` to `{colors.primary}`. Suggestion dropdown inherits the same rounded container with `{colors.hairline-soft}` row dividers and `{typography.body-sm}` text.

### Footer

**`footer`** — Full-width `{colors.ink}` (#1a1a1a) background. Section headings in `{typography.label-upper}` white. Navigation links in `{typography.body-sm}` at `{colors.surface-teal-mid}` (#b0e0e9), lifting to `{colors.accent-cyan}` (#22b8d1) on hover — the only place the full aquatic spectrum reads in vertical sequence: dark canvas, powder link, cyan hover.

### Promo Banner

**`promo-banner`** — A 40px full-width strip in `{colors.primary}` teal carrying promotional messaging in `{typography.body-sm}` white. Inline links use `{colors.accent-cyan}` to remain legible against the teal ground. Sits above the nav bar; dismissed on scroll past the first viewport on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with ink overlay; hero reduces to 380px min-height; configurator panel stacks vertically; spec table scrolls horizontally with frozen label column |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories with overflow menu; hero at 460px; configurator panel 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with mega-menu on category hover; hero at 560px; side-by-side configurator and spec panel |
| Wide | > 1440px | Max-width container at 1440px centered on page; four-column product grid; hero expands to full viewport height with parallax image |

### Touch Targets
- All buttons and interactive controls maintain 48px minimum height on mobile
- Swatch selectors expand to 44px minimum tap area via transparent padding around 32px visual
- Nav items in mobile overlay: 56px row height for comfortable thumb reach
- Collection filter chips minimum 40px height on touch viewports
- Spec table row height increases to 48px on mobile for accessible tap rows

### Collapsing Strategy
- Mega-menu collapses to accordion-style expandable sections in the hamburger overlay; icons collapse first, labels persist
- Spec table scrolls horizontally rather than reflowing — label column is sticky-left
- Configurator panel shifts from 2-column horizontal to single-column stacked below 744px
- Footer multi-column grid collapses to single-column with accordion toggle per section on mobile
- Promo banner text truncates to a single centered line on viewports narrower than 375px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned 403 Forbidden during extraction; no live CSS, design tokens, or DOM could be inspected directly
- True brand typeface unconfirmed — Arial, Open Sans, and Roboto all appear in extracted font stacks; a licensed geometric or humanist sans may be in use that did not surface in the crawl
- #1e6d7a and #226d7a are nearly identical teal values (≈2 units apart in all channels); the extracted duplicate likely reflects a hover or pressed state rather than two distinct brand colors — used as `primary-hover` here but the actual mapping may differ
- Exact nav structure, mega-menu content, and category taxonomy unknown
- Motion and animation tokens (hover transition durations, easing curves, scroll animations) not observed
- Shadow and elevation system not extracted — values above are inferred from category conventions
- Error, success, and warning state color usage unconfirmed; #c0392b and #27ae60 are standard convention defaults, not observed on site
- No dark-mode variant observed or confirmed
- Button border-radius may differ from `{rounded.md}` 12px — value is an informed estimate without live DOM measurement
