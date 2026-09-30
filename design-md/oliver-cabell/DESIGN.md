---
version: alpha
name: "Oliver Cabell"
source_url: "https://olivercabell.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The Future Mono typeface printing a cost breakdown — "Materials: $28.40 | Labor: $14.60 | Duties: $8.20 | Transport: $5.10 | True Cost: $56.30" — beside a $130 sneaker is the Oliver Cabell tell. No other footwear brand publishes factory-floor ledger data at the SKU level, and selecting a monospaced geometric typeface for that disclosure is not incidental: it signals receipts, not marketing copy. The warm off-white canvas (#f6f6f3) reads like unbleached cotton, calm and material-honest, interrupted once by a single high-voltage note — #ffcf2a, a marigold yellow that fires exclusively on primary CTAs and promotional banners. Deep navy (#272d45) anchors dark hero blocks and the footer, while the in-between lavender-gray (#676986) handles muted labels, secondary UI states, and category metadata — a hue sitting precisely where neutral and brand-tinted overlap. Mint (#b2f9e9) and teal (#0e7a82) surface as accent backgrounds for comfort-technology and pain-relief feature callouts, giving clinical credibility without pharmaceutical coldness. ArizonaSerif carries editorial weight in tall, humanist letterforms for hero headlines and brand storytelling. NeueHelveticaCondensedBold stacks campaign copy into tight columns. The Future handles navigation and UI chrome with geometric confidence, and The Future Mono earns a dedicated data role — cost tables, factual specs, price display — where a proportional-width font would feel dishonest. Corners are near-flat throughout: product cards sit at a hairline radius ({rounded.xs}), buttons carry minimal rounding ({rounded.sm}), and pills surface only on filter tags and small badges ({rounded.full}). Grid structure is generous and measured, with substantial breathing room between editorial storytelling and commerce zones — a rhythm that communicates quality over volume even when the catalog runs dozens of colorways.

colors:
  primary: "#ffcf2a"
  primary-active: "#e6b800"
  primary-disabled: "#f9e88a"
  navy: "#272d45"
  navy-alt: "#2c3e50"
  ink: "#121212"
  body: "#272d45"
  muted: "#676986"
  warm-gray: "#c2c1bd"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  cool-light: "#e5e5eb"
  canvas: "#f6f6f3"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#121212"
  on-dark: "#ffffff"
  accent-mint: "#b2f9e9"
  accent-teal: "#0e7a82"

typography:
  display-xl:
    fontFamily: "'ArizonaSerif', Georgia, serif"
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -1px
  display-md:
    fontFamily: "'ArizonaSerif', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-condensed:
    fontFamily: "'NeueHelveticaCondensedBold', 'Helvetica Neue Condensed', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
  title-md:
    fontFamily: "'The Future', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'The Future', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'Ufficio', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Ufficio', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'The Future', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.03em
  mono-data:
    fontFamily: "'The Future Mono', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  mono-label:
    fontFamily: "'The Future Mono', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.04em
    textTransform: uppercase
  price-display:
    fontFamily: "'The Future Mono', 'Courier New', monospace"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'The Future', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'The Future', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'The Future', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.06em

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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.warm-gray}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.on-dark}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "none"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    placeholderColor: "{colors.warm-gray}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "4/5"
    gap: "{spacing.sm}"
    padding: "{spacing.xs}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-colorcount:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    maxWidth: 1200px
  hero-dark:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
  cost-breakdown-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.mono-label}"
    valueTypography: "{typography.mono-data}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    borderTop: "2px solid {colors.ink}"
    rowBorder: "1px solid {colors.hairline-soft}"
    totalRowBackground: "{colors.canvas}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    activeBorder: "1px solid {colors.ink}"
    disabledOpacity: 0.3
    height: 44px
    minWidth: 48px
  color-swatch:
    rounded: "{rounded.full}"
    size: 24px
    activeBorder: "2px solid {colors.ink}"
    activeOffset: 2px
    inactiveBorder: "1px solid {colors.hairline}"
  comfort-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.navy}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  transparency-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    paddingHorizontal: "{spacing.base}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    activeBorder: "1px solid {colors.ink}"
    padding: 6px 16px
    height: 32px
  material-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.mono-label}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    accentBorder: "3px solid {colors.accent-teal}"
  factory-origin-block:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    dataTypography: "{typography.mono-data}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    flagSize: 24px
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "1px solid {colors.muted}"
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Marigold yellow (#ffcf2a) with near-black ink text, giving the CTA maximum contrast on both the warm canvas and dark navy backgrounds. Uppercase tracking via `{typography.button-md}` (0.08em) keeps the label crisp at 48px tall with `{rounded.sm}` corners. Active state deepens to #e6b800; disabled washes out to #f9e88a with `{colors.warm-gray}` text to signal unavailability without disappearing.

**`button-secondary`** — Transparent fill with a 1.5px `{colors.ink}` border, same height and uppercase spec as primary. A `button-secondary-dark` variant swaps to `{colors.on-dark}` border and text for use on navy hero sections. Neither variant uses fill color on hover — the border thickens or the type shifts weight to signal interactivity.

**`button-ghost`** — No border, no background. `{colors.muted}` lavender-gray text in `{typography.button-sm}` for low-priority actions like "View all" or inline dismissals.

### Inputs

**`text-input`** — `{colors.canvas}` background with `{rounded.sm}` and a thin `{colors.hairline}` border that snaps to full-ink on focus. Placeholder renders in `{colors.warm-gray}`. No drop shadow; the flat style matches the brand's direct, document-like aesthetic.

### Navigation

**`nav-bar`** — 60px tall, `{colors.canvas}` background with a single-pixel `{colors.hairline}` bottom rule. Logo sits left; main navigation links in `{typography.nav-link}` (The Future, 0.06em tracking) are center or right-weighted. An inverted `nav-bar-dark` variant uses `{colors.navy}` fill for campaign landing pages and dark editorial sections.

**`promo-banner`** — A 36px horizontal strip in `{colors.primary}` marigold above the nav, `{colors.on-primary}` text in `{typography.caption}`. Used for sitewide promotions ("Free shipping on orders over $X") and seasonal callouts. Its yellow is the only warm color that breaks the otherwise cool/neutral palette above the fold.

### Product Cards

**`product-card`** — `{rounded.xs}` (2px) corners keep the card feeling precise rather than bubbly. Image fills a 4:5 aspect ratio. Below the image: product name in `{typography.title-sm}` uppercase, color count in `{typography.caption}` muted gray, and price in `{typography.price-display}` (The Future Mono) so digits align across a grid row. No shadow; cards are distinguished by tight spacing and the natural edge of the photograph.

**`color-swatch`** — 24px circles with a 2px `{colors.ink}` ring on active state plus a 2px offset gap, giving a "selected" halo effect. Inactive swatches show a 1px `{colors.hairline}` border to delineate white and light colorways against the canvas.

### Transparency Components

**`cost-breakdown-table`** — The signature Oliver Cabell element. `{colors.surface-soft}` background, 2px `{colors.ink}` top border (heavier rule signals a formal ledger), rows separated by `{colors.hairline-soft}` lines. Labels render in `{typography.mono-label}` uppercase mono; cost values right-align in `{typography.mono-data}`. A final "True Cost" row uses `{colors.canvas}` background to visually separate the total.

**`factory-origin-block`** — Country of manufacture, factory name, and city rendered in `{typography.mono-data}` with a national flag icon. A `{rounded.sm}` card with `{colors.hairline}` border. The heading "Made In" uses `{typography.title-sm}`. This component appears on every PDP and is a primary trust signal.

**`material-callout`** — `{colors.surface-soft}` card with a 3px left-edge accent in `{colors.accent-teal}`. Label in `{typography.mono-label}`, body in `{typography.body-sm}`. Used for material provenance ("Italian full-grain leather from Conceria Walpier") and comfort-technology explanations.

### Badges

**`comfort-badge`** — `{colors.accent-mint}` pill in `{typography.caption}`, navy text, `{rounded.full}`. Applied to PDPs and collection cards for pain-relief or orthopedic comfort features.

**`transparency-badge`** — `{colors.accent-teal}` pill with white mono-label text, `{rounded.full}`. Signals "cost breakdown available" or "factory verified" at a glance.

**`filter-pill`** — 32px-tall `{rounded.full}` chips for collection filtering by category, material, or colorway. Inactive: `{colors.canvas}` with `{colors.hairline}` border. Active: `{colors.ink}` fill with `{colors.on-dark}` text. No animation — state switches are instant.

### Size Selector

**`size-selector`** — Flat 44px buttons in a grid layout. `{colors.canvas}` background with `{colors.hairline}` border for available sizes; active state fills `{colors.ink}` with white text. Sold-out sizes render at 30% opacity with a diagonal strike line.

### Hero

**`hero-editorial`** — Full-width block on `{colors.canvas}`. Headline in `{typography.display-xl}` (ArizonaSerif, 60px) for editorial storytelling; `{typography.body-md}` for supporting copy. `{spacing.section}` (64px) vertical padding. CTA is `button-primary`.

**`hero-dark`** — Same structure on `{colors.navy}` with `{colors.on-dark}` text. Used for seasonal campaign launches and brand-statement pages. `button-secondary-dark` is the preferred CTA variant here.

### Footer

**`footer`** — `{colors.navy}` background, `{colors.on-dark}` link text in `{typography.body-sm}`. Section headings in `{typography.title-sm}` uppercase. A 1px `{colors.muted}` top rule separates footer from the last content section. Legal copy and certifications render in `{typography.caption}` at reduced opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero headline drops to `{typography.display-md}` (40px); cost-breakdown-table scrolls horizontally if needed; size-selector wraps into 5-across grid |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links, secondary links in dropdown; hero headline at 48px; factory-origin-block shifts to inline layout |
| Desktop | 1128–1440px | Three or four-column product grid; full horizontal nav; hero at full 60px display-xl; cost-breakdown-table visible inline on PDP without scroll |
| Wide | > 1440px | Grid constrained to 1200px max-width, centered; section padding scales to 80px; hero type may step up to 72px for campaign pages |

### Touch Targets

- All interactive size selectors minimum 44×44px
- Color swatches expanded to 36px touch area on mobile via padding, visual size unchanged at 24px
- Filter pills maintain 32px height; horizontal scrolling row on mobile rather than wrapping grid
- Nav tap targets full-width on mobile drawer, minimum 48px tall per row

### Collapsing Strategy

- Product grid: 4-col → 3-col → 2-col → 1-col at breakpoints above
- Nav: horizontal links → hamburger drawer; drawer uses `{colors.canvas}` background with full-bleed rows in `{typography.nav-link}`
- Cost-breakdown-table: always full-width; on mobile, label and value stack vertically rather than two columns
- Hero: copy and image stack vertically on mobile; image moves above text; CTA becomes full-width
- Factory-origin-block: flag + location text collapses to single centered line on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius values not confirmed from live extraction — `{rounded.sm}` (4px) for buttons and `{rounded.xs}` (2px) for cards are reasonable estimates based on the brand's flat aesthetic
- Specific font weights for ArizonaSerif (Regular 400 assumed; may also use Italic variant for editorial pull-quotes)
- Hover and focus-visible transition timing (duration and easing) not extracted
- Exact nav height not confirmed — 60px estimated from typical Shopify theme headers at this brand tier
- Dark-mode palette not confirmed; brand appears to be light-only based on `#f6f6f3` canvas dominance
- Ufficio font usage scope is inferred — it may be limited to body copy or may overlap with The Future for UI labels
- Animation behavior for add-to-cart confirmation, size-selector selection, and filter-pill activation not documented
- Whether `#e5e5eb` (cool-light) is used for a specific component type or is a framework default not yet confirmed
