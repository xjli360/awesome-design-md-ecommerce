---
version: alpha
name: "Zens"
source_url: "https://www.zens.tech"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Four near-identical darks stacked in micro-steps — #121212 as the base void, #171717 as the page canvas, #1f1f1f lifting card surfaces just barely above it — give Zens a topology you feel more than see. Against that compressed darkness, a single off-white at #dedede does every unit of expressive work the brand allows itself: CTA borders, price figures, product silhouettes snapping out of shadow. There is no accent hue, no brand color, no warm-or-cool statement. The chromatic restraint is not austerity for its own sake — it mirrors the product itself, a charging pad that disappears into the desk and leaves only the charged device visible. Inter runs the entire type system at measured weights; display headings sit at 600 rather than 800, because the brand does not shout about convenience, it assumes it. Letter-spacing opens slightly at caption and label scale, keeping small text readable against surfaces that offer almost no luminance contrast as a safety margin. Rounded values stay decisively modest — {rounded.sm} on cards, {rounded.xs} on spec badges — signaling precision-engineered hardware rather than consumer softness. A {rounded.md} appears only on interactive inputs and buttons where a softer profile signals touch-friendly affordance. Section cadence is open: {spacing.section} between content bands lets each charging solution present as a self-contained object study, and {spacing.xxl} governs the internal rhythm of product detail blocks. The footer inherits the same near-black palette with no sharp contrast break, dissolving the page boundary the way a wireless charging surface dissolves the cable. Where most tech accessories brands chase a hero color to anchor brand recognition, Zens bets entirely on material authority: deep matte backgrounds, unhurried typography, and photography that carries all chromatic weight the design system withholds.

colors:
  primary: "#dedede"
  primary-active: "#ffffff"
  primary-disabled: "#555555"
  ink: "#ffffff"
  body: "#c8c8c8"
  muted: "#888888"
  muted-soft: "#5a5a5a"
  hairline: "#2d2d2d"
  hairline-strong: "#3d3d3d"
  canvas: "#121212"
  surface-soft: "#171717"
  surface-card: "#1f1f1f"
  surface-elevated: "#252525"
  on-primary: "#121212"
  on-dark: "#ffffff"
  danger: "#e05555"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 52px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 38px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.4px
  display-sm:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.1px
  caption:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-sm:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  spec-label:
    fontFamily: "'Inter', system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
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
    rounded: "{rounded.sm}"
    padding: 13px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.5
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 48px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    padding: 0 {spacing.xl}
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    backdropFilter: blur(12px)
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.hairline-strong}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    eyebrowTypography: "{typography.label-sm}"
    eyebrowColor: "{colors.muted}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
    maxWidth: 1280px
  spec-badge:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    border: "1px solid {colors.hairline}"
  compatibility-chip:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    activeBackground: "{colors.surface-card}"
  wattage-label:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  collection-grid:
    backgroundColor: "{colors.canvas}"
    columns: 3
    gap: "{spacing.base}"
    paddingHorizontal: "{spacing.xl}"
    responsiveMobile: 1
    responsiveTablet: 2
  device-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 18px
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    activeBackground: "{colors.surface-elevated}"
    gap: "{spacing.xs}"
  product-detail-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: "1:1"
    padding: "{spacing.xl}"
  accordion-faq:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    dividerColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    padding: "{spacing.base} 0"
  banner-strip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
    borderBottom: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    headingColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — A solid #dedede fill with #121212 text, 48px tall, 8px radius, and 13px/28px padding. This is the only warm-toned element on a page of near-blacks, so it reads as the singular call to action with no ambiguity. Hover transitions to `{colors.primary-active}` (full white) for a crisp luminance bump; disabled state drops opacity and shifts fill to `{colors.primary-disabled}` to signal inactivity without introducing a new hue.

**`button-secondary`** — Transparent background with a 1px `{colors.primary}` border and matching text, pairing cleanly alongside button-primary in split-CTA layouts. On focus/hover the background fills to `{colors.surface-card}` so the button gains substance without overpowering the primary. Shares height and radius with button-primary for consistent touch targets.

**`button-ghost`** — No border, transparent background, muted body-colored label at 40px height. Used for secondary navigation actions (account, wishlist) in nav-bar and secondary product page actions where presence is needed but hierarchy must stay flat.

### Navigation

**`nav-bar`** — 64px tall sticky bar sitting on `{colors.surface-soft}` (#171717) with a 1px `{colors.hairline}` bottom border, creating a visible but low-contrast shelf above content. Logo renders in `{colors.ink}` (white). When the page scrolls past the hero, `nav-bar-sticky` applies a canvas (#121212) fill with backdrop blur to separate it from content below without a hard shadow. Nav links use `{typography.nav-link}` at 14px/500 weight in `{colors.body}` tone, brightening to `{colors.ink}` on the active route.

### Product Card

**`product-card`** — `{colors.surface-card}` (#1f1f1f) card with 8px radius and a 1px hairline border that strengthens to `{colors.hairline-strong}` on hover. Image area uses `{colors.surface-soft}` as a neutral photo backdrop. Title renders in `{typography.title-md}`, price in `{typography.price-display}` colored `{colors.primary}` — the off-white price figure is the only consistently accented element within the card. Spec badges (`wattage-label`) sit beneath the title line, providing Qi wattage and device compatibility at a glance in uppercase 11px.

### Hero Banner

**`hero-banner`** — Full-bleed `{colors.canvas}` section with eyebrow label in `{typography.label-sm}` uppercase muted text above a headline at `{typography.display-xl}` (52px/600). Body copy drops to `{typography.body-md}` in `{colors.body}` tone. {spacing.section} top and bottom padding isolates the hero from nav and first content row. On desktop, product photography occupies the right half of a two-column grid; on mobile, stacks below the text block.

### Spec Badge & Wattage Label

**`spec-badge`** — Small rectangular token (`{rounded.xs}`, 4px radius) in `{colors.surface-elevated}` with a hairline border, uppercase 11px `{typography.spec-label}` in `{colors.body}`. Used inline in product cards and detail pages to surface charging speed (5W, 10W, 15W) and protocol tags (Qi, MagSafe). **`wattage-label`** is a narrower variant with `{colors.primary}` text on `{colors.surface-soft}` background, calling out peak wattage as a headline spec.

### Device Selector

**`device-selector`** — A horizontal scrolling row of pill-like tap targets (8px radius, 1px hairline border) that filter the charger compatibility view by device family (iPhone, Samsung, AirPods, Apple Watch). The inactive state is muted text on transparent; active switches to `{colors.ink}` text, `{colors.primary}` border, and `{colors.surface-elevated}` fill. On mobile the row scrolls horizontally with no visible scrollbar.

### Compatibility Chip

**`compatibility-chip`** — Structurally similar to device-selector but used inline in product detail to list compatible devices. Inert (non-interactive) variant drops the hover state and uses hairline border throughout. Active/selected variant uses `{colors.primary}` border to confirm the user's device is in the supported set.

### Accordion / FAQ

**`accordion-faq`** — Borderless section dividers at `{colors.hairline}` separate question rows. Title in `{typography.title-sm}`, body content in `{typography.body-sm}` with `{colors.body}` tone, revealing on expand with a smooth max-height transition. Chevron icon in `{colors.muted}` rotates 180° on open. No card background — the accordion floats directly on the page canvas to avoid double-dark layering.

### Footer

**`footer`** — Canvas (#121212) background with a single 1px `{colors.hairline}` top divider, no sharp contrast shift from the page body. Column headings in `{typography.label-sm}` uppercase `{colors.ink}`, links in `{typography.body-sm}` `{colors.body}` tone, brightening to `{colors.ink}` on hover. Social icons render as muted ghost icons that lighten on hover. A bottom strip carries legal copy in `{typography.caption}` `{colors.muted}`.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text/image stacks vertically; device-selector scrolls horizontally; nav collapses to hamburger + logo; collection-grid gap tightens to {spacing.sm} |
| Tablet | 744–1128px | Two-column product grid; hero shifts to 60/40 text-image split; nav shows top-level links, secondary items in dropdown |
| Desktop | 1128–1440px | Three-column product grid; hero uses 50/50 split with constrained max-width; full nav with utility icons right-aligned |
| Wide | > 1440px | Content capped at 1280px maxWidth and centered; hero padding scales to 80px top/bottom; grid columns stay at 3, card width increases |

### Touch Targets

- All primary buttons hold 48px height minimum on mobile
- Device-selector chips maintain 40px tap height even at small label sizes
- Nav hamburger target is 44×44px minimum
- Accordion rows are 48px minimum touch height with the full row tappable
- Product card image area is independently tappable from the add-to-cart region below

### Collapsing Strategy

- Top nav collapses to logo + hamburger icon at < 744px; search icon remains visible as a standalone icon button
- Product detail page shifts from two-column (image left, info right) to single-column stacked at < 744px
- Footer four-column layout collapses to two columns at tablet and single accordion-style expandable columns at mobile
- Spec badge rows wrap naturally; wattage-label stays inline with product title at all breakpoints
- Hero eyebrow label hides at mobile to reduce headline clutter; CTA button goes full-width

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only four colors were extracted, all in a near-black/off-white range (#171717, #dedede, #1f1f1f, #121212). Any accent hues used in promotional banners, sale badges, or seasonal campaigns could not be confirmed — the site likely loads additional tokens via JavaScript or Shopify theme settings not accessible to static extraction.
- No secondary typeface was detected; if Zens uses a display or serif face for campaign headlines or lifestyle sections, it was not surfaced in font-family stacks.
- Exact button border-radius and padding values are inferred from Inter-based dark-UI conventions; pixel-precise values require live DOM inspection.
- Hover and transition timing values (duration, easing) are entirely inferred — no animation tokens were extractable from static hints.
- Icon set style (outlined vs. filled, stroke weight) is unconfirmed; a consistent icon library choice would materially affect component spec.
- Product photography art direction (white-background studio vs. lifestyle/contextual) is unknown and would affect hero-banner and product-card image treatment decisions.
- Pricing display format (currency symbol placement, sale/original price color) could not be confirmed without a live product page traversal.
