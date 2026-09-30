---
version: alpha
name: "Beckett Simonon"
source_url: "https://beckettsimonon.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The first legible signal on beckettsimonon.com isn't leather or last shapes — it's the acid-lime CTA button (#83cc1c) sitting against a near-black canvas (#141414), a pairing that announces value-forward directness before any headline loads. Beckett Simonon builds handcrafted, Goodyear-welted dress shoes and boots on a made-to-order model, and the site's color logic mirrors that commitment: nothing pretends to be precious. Alverata — a humanist serif with Renaissance proportions — handles display type and gives the editorial voice a quiet backbone; Inter carries the workload in body and UI contexts while Work Sans tightens button labels and form controls. An amber-gold cluster (#ffb829, #ffcf2a, #f59e0b) runs through sale callouts, savings badges, and countdown timers as its own persistent promotional system, distinct enough from the lime primary to read immediately as urgency signal rather than brand identity. A deep forest tone (#384a42) surfaces in waitlist strips and craft-process storytelling — the brand's second accent, lending earnest weight to pre-order moments without competing with the lime for primary attention. The mid-gray (#545454) anchors secondary text, and a measured gradient of near-whites (#f6f6f6, #e2e2e2, #dedede) structures surface hierarchy across product listing and checkout flows. Corners lean spare throughout: product cards sit at {rounded.sm}, primary buttons at {rounded.xs}, and only detail elements like material tags reach {rounded.full}. Section padding is generous in hero and editorial contexts ({spacing.section} at 64px) and tightens predictably through the product grid. The made-to-order arc concentrates conversion into a tight hero-CTA-to-waitlist sequence, so the dark hero section, countdown timer, and lime add-to-cart button carry disproportionate visual mass relative to the breadth of inventory the site displays.

colors:
  primary: "#83cc1c"
  primary-active: "#6eb015"
  primary-disabled: "#c4e593"
  promo: "#ffb829"
  promo-warm: "#f59e0b"
  promo-light: "#ffcf2a"
  forest: "#384a42"
  ink: "#141414"
  body: "#1f1f1f"
  muted: "#545454"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-dark: "#141414"
  on-primary: "#141414"
  on-dark: "#f6f6f6"

typography:
  display-xl:
    fontFamily: "Alverata, Georgia, serif"
    fontSize: 56px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Alverata, Georgia, serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Alverata, Georgia, serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Work Sans', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  label:
    fontFamily: "Underground, 'Work Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "'Work Sans', Inter, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Work Sans', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px

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
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-ghost-light:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.on-dark}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageBorderRadius: "{rounded.sm}"
    padding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    minHeight: 580px
    padding: "{spacing.section}"
  promo-banner:
    backgroundColor: "{colors.promo}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    height: 40px
  sale-badge:
    backgroundColor: "{colors.promo}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  countdown-timer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.promo-light}"
    typography: "{typography.title-md}"
    digitBackground: "{colors.body}"
    captionTypography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md}"
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    height: 48px
  size-selector-default:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 48px
  size-selector-soldout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    height: 48px
  waitlist-strip:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-dark}"
    bodyTypography: "{typography.caption}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.lg} {spacing.section}"
  material-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  breadcrumb:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Acid-lime (#83cc1c) fill with dark text ({colors.on-primary} = #141414), 48px tall, sharp {rounded.xs} corners, uppercase Work Sans labels tracking at 0.5px. Hover darkens to {colors.primary-active} (#6eb015); disabled washes out to {colors.primary-disabled} with {colors.muted} text. The dark-on-lime pairing achieves maximum contrast without reaching for white, reinforcing the brand's directness. This is the sole primary CTA color — lime never appears on badges or banners.

**`button-secondary`** — White fill with a 1px {colors.ink} outline, same 48px height and uppercase typography as primary. Used for secondary actions ("View Details", "Learn More") sitting adjacent to a primary CTA. On hover the border color intensifies without a fill change.

**`button-ghost-light`** — Transparent with a 1px {colors.on-dark} border, used when a secondary action must remain legible on {colors.surface-dark} hero backgrounds. Pairs with `button-primary` in hero two-up CTA arrangements.

### Text Inputs
**`text-input`** — 48px height, 1px {colors.hairline} border at rest transitioning to 1px {colors.ink} on focus. No fill change on focus. Placeholder text rendered in {colors.muted}. Used in waitlist email capture, newsletter signup, and checkout address fields.

### Navigation
**`nav-bar`** — 64px tall, white canvas with a 1px {colors.hairline} bottom divider. Logo sits left; right side holds bag icon, account link, and a sale/offer pill when a sitewide promo is live. Transitions to `nav-bar-dark` (near-black fill, {colors.on-dark} text) when overlaid on hero sections. Sticky on scroll with a solid background fill.

### Product Card
**`product-card`** — White card with {rounded.sm} image crop. Product name in {typography.title-sm}, price in {typography.price-display}. When a product is on sale, a `sale-badge` overlays the top-left corner of the image. Hover state elevates the card with a subtle drop shadow; the image does not zoom. Sold-out state overlays a muted scrim on the image with no interactive affordance.

### Hero
**`hero-dark`** — Full-bleed {colors.surface-dark} section with Alverata display headline ({typography.display-xl}) in {colors.on-dark}, a one- to two-line supporting body paragraph in {typography.body-md}, and a single `button-primary` (lime) CTA. Minimum 580px tall on desktop with product photography filling the right half. This is the primary conversion entry point for the made-to-order funnel — all other content defers to it on page load.

### Promotional Elements
**`promo-banner`** — Full-width 40px strip in {colors.promo} amber above the nav, carrying sitewide offer copy in {typography.caption} with centered dark text. The amber reads as warm urgency and keeps the lime CTA reserved for interactive elements below.

**`sale-badge`** — Amber fill ({colors.promo}) with {colors.ink} text, {rounded.xs} corners, uppercase {typography.label} tracking at 1px. Positioned top-left on product card images. Amber is used exclusively here and in the promo banner — it never appears on buttons or forms.

**`countdown-timer`** — Dark background block ({colors.surface-dark}) with individual digit cells in {colors.body} (#1f1f1f) and digit values rendered in {colors.promo-light} (#ffcf2a). Unit labels (DAYS / HRS / MIN / SEC) sit below each digit cell in {typography.label}. Used for limited pre-order windows and flash sale endings; the lime/amber/dark color system makes it immediately recognizable as time-critical.

### Size Selector
**`size-selector-active`** — Black fill ({colors.ink}), white text ({colors.on-dark}), 48px height. The selected state uses the darkest ink rather than the lime primary, reserving green for the single add-to-cart / add-to-waitlist CTA that follows.

**`size-selector-soldout`** — Soft gray fill ({colors.surface-soft}), muted text, same 48px height. Typically rendered with a diagonal strikethrough overlay to communicate unavailability without removing the cell from the grid.

### Waitlist Strip
**`waitlist-strip`** — Forest green (#384a42) background strip spanning the full content width, positioned between the product hero and the product description. Contains a short explanatory line in {typography.caption} and an inline email field + `button-primary` (lime) pair. The forest green is the brand's third distinct hue in functional use, signaling scarcity and pre-order intent at a register distinctly quieter than the amber promo system.

### Material Tags
**`material-tag`** — Soft gray pill ({rounded.full}), uppercase {typography.label} in {colors.muted}. Lists construction and material attributes (Full-Grain Leather, Goodyear Welt, Blake Stitch, Leather Lining) beneath the product title, functioning as spec chips rather than interactive filters.

### Footer
**`footer`** — Near-black ({colors.surface-dark}) background echoing the hero treatment, creating a visual bookend. Four-column grid with uppercase {typography.label} section headings and {typography.body-sm} links in {colors.on-dark}. Bottom row contains newsletter capture and social icons. No color variation within the footer — all text and links use {colors.on-dark} with opacity-based hover states.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to logo + hamburger + bag icon; hero headline drops to display-sm scale; size selector becomes full-width horizontal scroll row; countdown timer stacks 2×2 digit grid; promo-banner wraps to two lines at 48px height; waitlist-strip stacks form below copy |
| Tablet | 744–1128px | 2-column product grid; hero is 50/50 text-image split; nav shows logo + primary links + icons; waitlist-strip uses inline form layout; countdown timer horizontal row |
| Desktop | 1128–1440px | 3-column product grid; nav fully expanded with all links visible; hero full-bleed with text left, photography right; all components at designed proportions |
| Wide | > 1440px | Content capped at ~1440px max-width with auto margins; hero photography scales to fill; product grid optionally expands to 4 columns; section padding increases proportionally |

### Touch Targets
- All buttons (primary, secondary, ghost, size selectors) maintain 48px minimum height
- Size selector grid cells minimum 44×44px on mobile
- Nav hamburger and icon buttons minimum 44×44px tap area
- Material tags are display-only; no minimum touch target requirement
- Countdown timer digit cells are display-only; no interactive target needed

### Collapsing Strategy
- Nav: logo + bag + hamburger below 744px; full horizontal link row at 1128px+
- Hero photography: stacks above text block on mobile (text below fold acceptable for editorial pages)
- Waitlist strip: form stacks below copy on mobile, inline on tablet+
- Promo banner: single-line at tablet+, wraps to two lines on mobile with height auto-expansion
- Footer: single column on mobile, 2-column on tablet, 4-column on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius values inferred from aesthetic; site-specific radius tokens not directly extracted
- The amber/gold cluster (#f59e0b, #fbbf24, #ffb829, #ffcf2a) contains four close values; their exact functional assignments (badge vs. banner vs. countdown highlight vs. hover state) could not be distinguished from the color extraction alone
- Underground font usage context is uncertain — it may appear only in a specific badge or tag context not captured in the extraction; WorkSans assigned as fallback
- Hover/focus transition durations and easing curves not extracted
- Whether the site defaults to a dark-mode or light-mode canvas at the top level is ambiguous from the color list; this file assumes a hybrid layout (dark hero and footer, light product grid sections)
- No icon set style, illustration system, or photography art direction data was extractable from the scrape
- Exact nav height and sticky behavior not confirmed; 64px is inferred from Shopify theme norms and the brand's category
