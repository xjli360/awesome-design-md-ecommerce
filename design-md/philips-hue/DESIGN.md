---
version: alpha
name: "Philips Hue"
source_url: "https://www.philips-hue.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Before a Philips Hue bulb fires, the room is dark — and the product site takes that condition as its design premise. The canvas is #101010, a near-total black, with surface layers stepping up through #18181a, #242427, and #303034 in increments just large enough to register depth without breaking the room-at-dusk illusion. Against that backdrop, a single frequency of light activates all interactive affordances: #0066f5, a high-voltage electric blue borrowed from the visible spectrum of their LED technology, appears on every primary button, active link, and selected state; on hover it deepens to #0050a8 — the same hue at lower wattage. Product photography of lit rooms earns its drama precisely because the UI chrome stays controlled and dark; a warm amber Gradient Signe Lamp or magenta-lit outdoor facade lands with full emotional force because nothing in the interface competes. Error states assert in #e63535, a warm red that surfaces rarely enough to carry genuine authority. Border radii follow a deliberate rhythm: large scene cards and hero modules sit at {rounded.lg} (20px), input fields and inline chips at {rounded.sm} (8px), and status pills snap to {rounded.full} — human enough to signal consumer software, restrained enough to hold the brand's premium posture. Secondary text, icon labels, and helper copy descend through a muted gray ladder (#8a8a8d → #636367 → #3c3c41) that structures hierarchy across dark surfaces without requiring color. The JP version of the site loads CJK and system font stacks as initial fallbacks, indicating a custom Latin display face is injected via JS after DOMContentLoaded; the underlying proportions suggest a geometric sans at comfortable tracking, unhurried and precise.

colors:
  primary: "#0066f5"
  primary-active: "#0050a8"
  primary-disabled: "#404040"
  ink: "#f9f9f9"
  body: "#d8d8d9"
  muted: "#8a8a8d"
  muted-soft: "#636367"
  hairline: "#3c3c41"
  hairline-subtle: "#242427"
  canvas: "#101010"
  surface-soft: "#18181a"
  surface-card: "#242427"
  surface-raised: "#303034"
  on-primary: "#f9f9f9"
  error: "#e63535"
  error-active: "#d03131"
  light-canvas: "#f9f9f9"
  light-surface: "#f5f5f6"
  scrim: "#0c0c0d"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.21
    letterSpacing: -0.2px
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.6px
    textTransform: uppercase
  price:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 52px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    border: "1px solid {colors.body}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 52px
  button-secondary-hover:
    backgroundColor: "{colors.surface-raised}"
    border: "1px solid {colors.ink}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 52px
  search-input:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-subtle}"
    activeIndicator: "{colors.primary}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  breadcrumb:
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    imageAspectRatio: "1/1"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    descriptionTypography: "{typography.body-sm}"
    descriptionColor: "{colors.muted}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
    hoverShadow: "0 8px 32px rgba(0,0,0,0.55)"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
    minHeight: 600px
    overlay: "linear-gradient(to right, rgba(16,16,16,0.88) 40%, rgba(16,16,16,0) 100%)"
  scene-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    imageAspectRatio: "16/9"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    descriptionTypography: "{typography.body-sm}"
    descriptionColor: "{colors.muted}"
    padding: "{spacing.lg}"
  color-scene-badge:
    backgroundColor: "{colors.surface-raised}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    colorDotSize: 10px
  compatibility-chip:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    iconSize: 16px
  price-badge:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  quantity-stepper:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    buttonBackgroundColor: "{colors.surface-raised}"
    buttonTextColor: "{colors.ink}"
  error-banner:
    backgroundColor: "{colors.error}"
    textColor: "#ffffff"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The primary CTA runs #0066f5 fill with {colors.on-primary} text at 52px height and {rounded.sm} radius. Hover deepens to #0050a8 — same blue channel, reduced luminance — without changing shape or size. Disabled collapses to {colors.primary-disabled} fill with {colors.muted} text, effectively merging into the surrounding surface stack. Used for "Add to Cart," "Buy Now," and primary configurator actions.

**`button-secondary`** — Ghost variant: transparent fill, 1px border in {colors.body}, matching 52px height to align with primary in dual-CTA pairs. Hover acquires {colors.surface-raised} fill and sharpens the border to {colors.ink}. Used for "Learn More," "Compare," and secondary navigation within product detail flows.

**`button-ghost`** — Text-only in {colors.primary} with underline, no padding container. Appears inline in body copy, within card footers for soft navigation, and in modal dismiss flows. Does not carry height or border constraints.

### Form Inputs

**`text-input`** — 52px height with {rounded.sm} radius. Resting border is 1px {colors.hairline}; focus upgrades to 2px {colors.primary} ring. Background is {colors.surface-card}, lifting the field visually above the {colors.canvas} page body. Placeholder copy sits in {colors.muted}.

**`search-input`** — Full-pill form ({rounded.full}) distinguishing global site search from data-entry inputs. Same focus ring behavior as text-input. A magnifier icon in {colors.muted} anchors the leading edge; active input swaps it for an X dismiss at the trailing edge.

### Navigation

**`nav-bar`** — 72px fixed bar on {colors.canvas} with a 1px {colors.hairline-subtle} bottom edge. Category links render in {typography.nav-link}; the active category receives {colors.primary} text color. Cart and hamburger icons use {colors.ink} with the cart badge count appearing as a {colors.primary} dot. Scrolls away at mobile, pinned on desktop.

**`breadcrumb`** — Caption-scale trail ({typography.caption}) in {colors.muted-soft} with "/" separators in {colors.hairline}. Terminal node resolves to {colors.ink}. Appears beneath the nav on category and product detail pages, never on the homepage hero.

**`nav-link-active`** — Isolated state token for the currently active top-level category: text color shifts to {colors.primary}, weight stays at {typography.nav-link} (500) rather than jumping to bold — the color alone signals selection.

### Product Surface

**`product-card`** — {colors.surface-card} card with {rounded.lg} corners, square product image at 1:1 ratio, then {spacing.lg} padding carrying title ({typography.title-sm}), price ({typography.price}), a short descriptor ({typography.body-sm}/{colors.muted}), and an Add-to-Cart CTA button in {colors.primary}. Hover lifts with a deep rgba shadow (0 8px 32px / 0.55 opacity) that reads as the card floating off the dark canvas.

**`scene-card`** — Wider 16:9 format for room-inspiration and lighting-scene modules. Image at 16/9 with {rounded.lg} corners, then {spacing.lg} interior padding for title ({typography.title-md}) and description ({typography.body-sm}/{colors.muted}). Background stays {colors.surface-card}. Appears in "Explore scenes" rails and interior design inspiration sections.

**`color-scene-badge`** — Pill-shaped tag ({rounded.full}, {colors.surface-raised}) pairing a 10px color dot with a short mood label ("Relax," "Energize," "Reading") in {typography.caption}/{colors.body}. Arrays of these badges appear under product cards and scene cards for previewing available lighting presets. Minimum 8px horizontal gap between badges.

**`compatibility-chip`** — Rectangular micro-chip ({rounded.xs}) for ecosystem compatibility marks: Works with Alexa, Google Home, Apple HomeKit. Leading 16px icon in {colors.muted} plus label in {typography.caption}/{colors.muted}. Appears in a horizontal scroll row on product detail pages. Border is 1px {colors.hairline} on {colors.surface-soft} fill.

### Utility

**`price-badge`** — Unstyled number block in {typography.price}/{colors.ink}, placed inline with the product title. No container box — scale alone signals the pricing tier.

**`quantity-stepper`** — Minus / count / plus in a 1px {colors.hairline} bordered {rounded.sm} container. Outer increment buttons use {colors.surface-raised} fill; the center count renders in {typography.body-md}/{colors.ink}. Appears on product detail pages adjacent to the primary Add-to-Cart button.

### Feedback

**`error-banner`** — Solid #e63535 banner spanning full content width, white text in {typography.body-sm}, {rounded.sm}, with {spacing.base} vertical and {spacing.lg} horizontal padding. Appears for cart failures, stock unavailability, and form validation errors. Active/hover state on any dismiss action deepens to {colors.error-active}.

### Structure

**`hero-section`** — Full-bleed {colors.canvas} section with a right-side product image and a left-aligned text column. Headline in {typography.display-xl}, supporting copy in {typography.body-md}/{colors.body}, primary CTA in {colors.primary}. A directional gradient overlay (rgba 16,16,16 / 0.88 at 40%, transparent at 100%) keeps text legible against lit-room photography without a hard mask.

**`footer`** — {colors.surface-soft} base, 1px {colors.hairline} top border, {spacing.xxl} vertical padding. Four link columns in {typography.body-sm}/{colors.body}; hover resolves to {colors.ink}. Legal row and social icons sit below a secondary hairline divider.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to {typography.display-sm}; nav collapses to hamburger + logo + cart icon; color-scene-badge arrays scroll horizontally in snap-scroll rail |
| Tablet | 744–1128px | 2-column product grid; hero switches to stacked text-over-image; nav shows 3–4 top-level links with overflow ellipsis menu |
| Desktop | 1128–1440px | 3-column product grid; full horizontal nav with all category links visible; hero runs text-left / image-right split at 50/50 |
| Wide | > 1440px | Content max-width caps at ~1400px centered; hero image bleeds edge-to-edge behind gradient overlay; grid stays 3-column with increased gutters |

### Touch Targets
- Minimum 48×48px tap target on all interactive elements including nav icons and badge pills
- product-card entire surface is tappable on mobile, not just the CTA button
- quantity-stepper increment buttons minimum 44px width
- color-scene-badge minimum 40px height with 8px horizontal gap between items in a rail

### Collapsing Strategy
- Primary nav folds to hamburger drawer at < 744px; panel slides from left over {colors.surface-card} background with {colors.scrim} overlay
- Scene cards reflow from 3-up desktop row to full-width stacked mobile cards; "Explore Scenes" rail offers horizontal scroll at mobile rather than reflowing
- Compatibility chips collapse from wrapping grid to a horizontal snap-scroll rail below 744px
- Footer four-column link grid stacks vertically at mobile with {spacing.lg} between groups; social and legal rows always full-width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specific display font detected — the JP site surfaces only CJK system fallbacks (Meiryo, Hiragino Kaku Gothic Pro, Malgun Gothic, Dotum) and monospace stacks (Consolas, Menlo, Monaco); a custom Latin geometric sans is almost certainly injected via JS post-render. All typography tokens use a system-ui fallback stack pending font identification.
- No explicit light-mode color ramp confirmed — extracted palette is predominantly dark (#101010–#303034); light neutrals (#f9f9f9, #f5f5f6) exist but their precise page-role (checkout, modal overlay, product detail white section) could not be verified from static extraction.
- Exact computed border-radius values not measured; {rounded.sm} (8px) and {rounded.lg} (20px) are approximated from visual proportion rather than computed-style capture.
- No elevation or box-shadow tokens extracted; shadow values in product-card and hero are inferred from premium dark-UI conventions.
- No animation or transition-timing values captured (hover transition duration, drawer easing, etc.).
- meta theme-color absent from the JP page, removing one common signal for confirming primary brand color; #0066f5 is supported by its position as the single most distinctive non-neutral in the extracted palette.
- Red values (#e63535, #d03131, #e41d30) appear in extracted palette but their precise semantic assignments (error vs. promotional badge vs. sale price) could not be confirmed from extraction alone.
