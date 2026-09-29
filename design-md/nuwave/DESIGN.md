---
version: alpha
name: "NuWave"
source_url: "https://www.nuwavenow.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Digital readouts and thermal-gradient orange signal that a NuWave product is running — and those same visual cues carry directly into the brand's web presence. The confirmed site color is #313131, a near-black charcoal that NuWave deploys as both a product-shell finish and a marketing canvas: dark backgrounds let heated-element orange snap to attention without any lifestyle softening. Where most countertop-appliance brands reach for clinical white and stainless, NuWave's command-center aesthetic goes the other direction, treating precision engineering as the primary visual argument. The orange primary — broadly documented across NuWave's logo mark, product packaging, and CTA buttons throughout the Brio and Pro4+ lines — reads as a thermal reference, not a trend color; it belongs in the same visual grammar as LED digits and backlit control panels. No custom typeface was detected during extraction (the site returned an anti-bot challenge, yielding a single color token), so the system-native sans-serif stack carries full hierarchy: weight 700 for display headlines and appliance model numbers, weight 600 for product card titles, weight 400 for body and legal copy. Numerics carry unusual weight in this category — wattages, temperature ranges, preset counts — and the type system must handle spec-dense rows without collapsing; `{typography.caption}` labels in all-caps tracking echo the on-device panel readouts, unifying screen UI with physical product language. Interactive elements use `{rounded.sm}` — the brand stays functional rather than playful, reserving `{rounded.full}` only for promotional badges and secondary tags. Hero blocks need `{spacing.section}` breathing room around product renders so each machine reads as a countertop object, not a catalog thumbnail. PDP and collection pages lean heavily on comparison tables and feature-icon strips, components that carry more purchase-signal weight than photography alone for a buyer choosing between the 6-quart and 8-quart model.

colors:
  primary: "#FF6600"
  primary-active: "#E05200"
  primary-disabled: "#FFBE99"
  ink: "#313131"
  body: "#484848"
  muted: "#767676"
  muted-soft: "#999999"
  hairline: "#E0E0E0"
  hairline-soft: "#EFEFEF"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  surface-dark: "#313131"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  warning: "#FFC107"
  success: "#2E7D32"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  caption-plain:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.4px
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 50px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        cursor: not-allowed

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 50px
    states:
      hover:
        borderColor: "{colors.primary}"
        textColor: "{colors.primary}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "2px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 50px

  button-sm-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px

  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    states:
      focus:
        borderColor: "{colors.ink}"
        outlineColor: "{colors.ink}"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    ctaButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-sm}"
      rounded: "{rounded.sm}"

  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    accentColor: "{colors.primary}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    borderColor: "{colors.hairline-soft}"
    borderWidth: 1px
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    imageAspectRatio: "4/3"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.12)"
    badge:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.badge}"
      rounded: "{rounded.full}"
      padding: 4px 10px

  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    ctaSpacing: "{spacing.lg}"
    overlayOpacity: 0.55
    accentColor: "{colors.primary}"

  spec-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 5px 12px

  spec-block:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    valueTypography: "{typography.spec-value}"
    labelTypography: "{typography.spec-label}"
    valueColor: "{colors.ink}"
    labelColor: "{colors.muted}"
    borderTop: "3px solid {colors.primary}"

  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    paddingVertical: "{spacing.sm}"
    paddingHorizontal: "{spacing.base}"

  feature-icon-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    paddingVertical: "{spacing.xl}"
    columnGap: "{spacing.xl}"
    iconSize: 40px

  comparison-table:
    headerBackgroundColor: "{colors.surface-dark}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.body-sm}"
    labelTypography: "{typography.caption}"
    rowStripedColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    highlightColumnBorder: "2px solid {colors.primary}"
    checkmarkColor: "{colors.primary}"
    xmarkColor: "{colors.muted}"

  newsletter-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    paddingVertical: "{spacing.xxl}"
    input:
      backgroundColor: "{colors.canvas}"
      textColor: "{colors.ink}"
      typography: "{typography.body-md}"
      rounded: "{rounded.xs}"
      height: 48px
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.button-md}"
      rounded: "{rounded.xs}"
      height: 48px

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary}"
    headlineTypography: "{typography.caption}"
    linkTypography: "{typography.body-sm}"
    copyrightTypography: "{typography.caption-plain}"
    borderTop: "3px solid {colors.primary}"
    paddingVertical: "{spacing.section}"

  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.muted-soft}"

## Components

### Buttons

**`button-primary`** — Solid orange `{colors.primary}` fill with white type set in uppercase `{typography.button-md}` (700 weight, 0.3px tracking); corner radius is `{rounded.sm}` keeping the shape purposeful without softening into lifestyle territory. Hover deepens to `{colors.primary-active}`; disabled state washes to `{colors.primary-disabled}` with `not-allowed` cursor. The all-caps transform and generous letter spacing align the button with the on-product control-panel language.

**`button-secondary`** — White canvas with a 2px `{colors.ink}` border; same uppercase `{typography.button-md}` as primary. On hover, border and label both shift to `{colors.primary}`, creating a clear active state without a fill change. Used for secondary CTAs alongside a primary orange button, never floating alone as the sole action.

**`button-ghost`** — Transparent fill with a 2px white border and `{colors.on-dark}` label; lives exclusively on `{colors.surface-dark}` hero sections. Pairs with `button-primary` to give hero blocks a primary/secondary action hierarchy on dark backgrounds.

**`button-sm-pill`** — Small `{rounded.full}` pill in `{colors.primary}` for in-card CTAs, collection-page filter tags, and accessory upsell modules. Smaller `{typography.button-sm}` scale keeps it subordinate to primary page actions.

### Navigation

**`nav-bar`** — White canvas, 64px tall, `{colors.hairline}` bottom border. The NuWave logo renders in `{colors.primary}` orange. Links use `{typography.nav-link}` at weight 600. A compact "Shop Now" CTA in `{colors.primary}` with `{rounded.sm}` sits at the trailing edge. On scroll, a drop shadow replaces the hairline to maintain stack separation.

**`announcement-bar`** — A 36px `{colors.ink}` charcoal strip that sits above the nav, carrying promotional copy in `{typography.caption}` uppercase. Brand-orange `{colors.primary}` is used to highlight numeric offers (e.g., percentage-off values) within the strip text.

### Product Cards

**`product-card`** — White surface, `{rounded.sm}` corners, `{colors.hairline-soft}` 1px border. Images use a 4:3 aspect ratio with object-fit cover. Title at `{typography.title-md}` weight 600, price matching that scale but in `{colors.primary}`. Hover state lifts a 16px blur shadow. Promo badges (`spec-badge`) float over the image corner in solid orange with `{rounded.full}`.

### Hero

**`hero-banner`** — Full-width dark module using `{colors.surface-dark}` (#313131) as the base, with a 0.55 opacity scrim over product photography. Headline in `{typography.display-xl}` at 700 weight, sub-copy in `{typography.body-md}`. Two buttons — `button-primary` and `button-ghost` — sit spaced by `{spacing.lg}`. The dark base is the deliberate stage: it gives product renders and heating-element photography maximum contrast.

### Spec Components

**`spec-block`** — A `{colors.surface-soft}` card with a 3px `{colors.primary}` top border, carrying a large `{typography.spec-value}` number (wattage, quart capacity, temperature) above a small `{typography.spec-label}` uppercase descriptor. Used in horizontal rows of 3–4 across PDP pages to surface the purchase-deciding numbers without paragraph prose.

**`feature-icon-strip`** — A soft-gray `{colors.surface-soft}` band housing 4–6 icon-plus-label pairs. Icons render in `{colors.primary}` at 40px, labels in `{typography.caption}` uppercase, short descriptions in `{typography.body-sm}`. Columns spread with `{spacing.xl}` gutters; on mobile, collapses to a 2-column grid.

### Comparison Table

**`comparison-table`** — Dark `{colors.surface-dark}` header row with `{colors.on-dark}` labels. Alternating rows use `{colors.surface-soft}` stripes. The "recommended" or featured column is marked with a 2px `{colors.primary}` full-height border. Checkmarks render in `{colors.primary}`; X-marks in `{colors.muted}`. Dense spec rows use `{typography.body-sm}` for values and `{typography.caption}` for row headers.

### Utility

**`promo-strip`** — A thin `{colors.primary}` orange band above or below hero blocks, `{typography.caption}` uppercase, used for free-shipping thresholds or limited-time callouts.

**`newsletter-bar`** — Dark `{colors.surface-dark}` section with a headline in `{typography.display-sm}`, an inline text input, and a solid-orange submit button flush to the input's trailing edge. The pair shares a 48px height for visual lockup.

**`footer`** — Deep `{colors.ink}` (#313131) background with a 3px `{colors.primary}` top border that marks the section break. Column heads in `{typography.caption}` uppercase, links in `{typography.body-sm}` at `{colors.muted-soft}` brightening to `{colors.primary}` on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to `display-md` scale; `announcement-bar` hides secondary copy, shows offer code only; `comparison-table` scrolls horizontally; `feature-icon-strip` collapses to 2-column grid; nav becomes hamburger with full-screen overlay |
| Tablet | 744–1128px | 2-column product grid; hero shifts to side-by-side text/image layout; `spec-block` rows hold 3 columns; nav shows top-level links, collapses sub-categories under hamburger |
| Desktop | 1128–1440px | 3-column product grid; full horizontal nav with mega-menu dropdowns; `hero-banner` uses split layout with full-bleed image right and text left; `comparison-table` shows all columns without scroll |
| Wide | > 1440px | Max content width 1440px, centered with `{colors.surface-dark}` side gutters on hero; product grid optionally extends to 4 columns; `spec-block` rows hold 5–6 columns |

### Touch Targets

- All primary and secondary buttons maintain 50px height (exceeds 44px minimum)
- `button-sm-pill` uses 36px height minimum on mobile with `{spacing.sm}` side margins for tap separation
- Nav hamburger icon target: 48×48px
- Product card entire surface is tappable, not just the CTA
- Comparison-table cells add `{spacing.sm}` vertical padding on touch to reduce mis-taps

### Collapsing Strategy

- Hero dual-button row stacks vertically on mobile, full-width each
- `feature-icon-strip` 4-column layout collapses to 2×2 grid at tablet and below
- `comparison-table` pins first column (product name) and allows horizontal scroll on columns at tablet and below
- `spec-block` horizontal band wraps to 2-column grid on mobile
- Footer multi-column layout stacks to accordion-style expandable sections on mobile
- `announcement-bar` truncates to a single centered message on mobile, hiding secondary CTAs

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Site extraction blocked:** The page title returned "Just a moment…" indicating an anti-bot / Cloudflare challenge. Only one hex color (#313131) was captured; all remaining color tokens are inferred from widely-observed NuWave brand usage (orange logo, orange CTAs across Brio/Pro4+ packaging) and should be verified against the live site.
- **Primary orange unverified:** `{colors.primary}` (#FF6600) is inferred from brand knowledge, not extracted. The actual value may differ — verify via browser dev tools on nuwavenow.com and update `primary`, `primary-active`, and `primary-disabled` accordingly.
- **No custom typeface detected:** All font stacks resolved to system-native sans-serif. NuWave may use a licensed font loaded via JS (common in Cloudflare-gated sites). Inspect the live site's CSS `@font-face` declarations and update all `fontFamily` values if a custom font is found.
- **Secondary palette unconfirmed:** Colors beyond #313131 (muted grays, surface tones, success/warning states) are convention-based estimates for a dark-primary appliance brand. Verify hairline, surface-soft, and muted values against actual UI.
- **Component inventory incomplete:** Without live site access, PDP layout specifics (sticky add-to-cart bar, variant selectors, upsell modules) and any loyalty or rewards UI could not be documented.
- **Dark mode / alternate themes:** Unknown whether NuWave uses a dark-mode toggle or if #313131 is the permanent brand tone rather than a theme variable.
