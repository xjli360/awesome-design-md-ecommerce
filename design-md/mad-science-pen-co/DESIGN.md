---
version: alpha
name: "Mad Science Pen Co."
source_url: "https://madsciencepenco.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every pen in the lineup is tagged with a formula number set in monospace type alongside the nib grade — not a model name, a formula number, as though each instrument emerged from a laboratory process rather than a product roadmap. That precision-theater defines the brand's posture: a niche fountain pen and specialty ink maker that borrows from chemistry-lab aesthetics — beakers, pH-indicator color shifts, UV-reactive hues — to sell craft objects to a community that already measures ink flow in milliliters per minute and debates nib geometry past midnight. With zero hex tokens and no font stacks extracted from the live site (the site likely blocks automated extraction or loads styles client-side), the system below is reconstructed from brand positioning and category conventions; all color and typography values are inferred at alpha confidence only, not confirmed from source.

  The palette reaches for the pH-indicator shift and the late-night laboratory: {colors.surface-dark} (#0F0E1A) serves as the hero-section canvas, a near-black that reads as deep fountain ink pooling in a glass well. The primary action color is electric violet {colors.primary} (#7B2FBE) — the color family most associated with chemistry glassware and UV exposure — handling all CTAs, add-to-cart buttons, and focused link states. A cold accent cyan {colors.accent-cyan} (#00E5CC) appears as a secondary voltage on formula callouts, footer links, and pill badges, evoking glowing reagent solutions without literal prop styling. Product cards and body pages live on warm off-white {colors.canvas} (#FAF9F6), parchment-adjacent — paper that has been held and considered, not clinical white.

  Typography splits the brand's dual personality cleanly: a serif display face (Playfair Display or equivalent) handles hero titles and section headings with the weight and spread of a broad-nib stroke, while Space Grotesk handles body copy, navigation, and UI labels with the legibility of graph-paper annotation. The third register — JetBrains Mono for nib specs, ink codes, formula numbers, and callout blocks — gives the brand its laboratory-notebook texture without costuming the entire site. Radius tokens stay conservative: {rounded.sm} (8px) on buttons and inputs, {rounded.md} (12px) on product cards, {rounded.full} (9999px) on ink-swatch circles and lab-badge pills. The system reads precise rather than playful, matching a customer who owns calipers.

colors:
  primary: "#7B2FBE"
  primary-active: "#6025A0"
  primary-disabled: "#C4A0E8"
  accent-cyan: "#00E5CC"
  accent-cyan-dim: "#00BBA8"
  lab-amber: "#F5A623"
  ink: "#0F0E1A"
  body: "#2C2B3E"
  muted: "#6B6A8A"
  hairline: "#E2E1EC"
  hairline-dark: "#2A293C"
  canvas: "#FAF9F6"
  surface-soft: "#F2F1F8"
  surface-card: "#FFFFFF"
  surface-dark: "#0F0E1A"
  surface-dark-raised: "#1E1D2E"
  on-primary: "#FFFFFF"
  on-dark: "#F0EFF8"
  ink-swatch-ring: "#E2E1EC"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Space Grotesk', 'DM Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Space Grotesk', 'DM Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'Space Grotesk', 'DM Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Space Grotesk', 'DM Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Space Grotesk', 'DM Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Space Grotesk', 'DM Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.01em
  button-sm:
    fontFamily: "'Space Grotesk', 'DM Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.02em
  mono-spec:
    fontFamily: "'JetBrains Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  mono-label:
    fontFamily: "'JetBrains Mono', 'Fira Code', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.05em
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.accent-cyan}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
  ink-swatch-badge:
    shape: "{rounded.full}"
    size: 36px
    borderColor: "{colors.ink-swatch-ring}"
    borderWidth: 2px
  nib-spec-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.mono-spec}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  formula-callout:
    backgroundColor: "{colors.surface-dark-raised}"
    textColor: "{colors.on-dark}"
    accentBorderLeft: "3px solid {colors.accent-cyan}"
    typography: "{typography.mono-spec}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  lab-badge:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  collection-band:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    paddingY: "{spacing.md}"
    borderBottom: "1px solid {colors.hairline}"
  ink-color-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    textTransform: uppercase
    letterSpacing: 0.08em
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.accent-cyan}"
    borderTop: "1px solid {colors.hairline-dark}"
    paddingTop: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Electric violet (#7B2FBE) fill with white label at 15px/600 weight, 44px height, {rounded.sm} corners. The primary CTA for add-to-cart, checkout, and account actions. On hover the background shifts to {colors.primary-active} (#6025A0) with no other change; disabled state bleaches to {colors.primary-disabled} (#C4A0E8), signaling unavailability without hard grey.

**`button-secondary`** — Transparent fill with a 1.5px violet border and violet label text; same dimensions as primary. Used for secondary actions like "Learn More," "View Full Spec Sheet," and wishlist. On hover the border weight stays fixed and the label gains slight underline; no fill is added.

**`button-ghost`** — Borderless transparent button in {colors.body} text at 13px/600 weight, {rounded.xs}. Appears in navigation dropdowns, close controls, and inline text-adjacent actions where a bordered button would over-emphasize.

### Inputs

**`text-input`** — Off-white {colors.canvas} fill, 1px {colors.hairline} border at rest, 1.5px violet border on focus. Placeholder in {colors.muted}; body text in {colors.ink}. Height 44px, {rounded.sm}. Error state uses a 1.5px red-adjacent stroke (derived from primary-active family); no background fill change on error.

**`search-bar`** — Slightly smaller at 40px height, {colors.surface-soft} fill (vs. canvas for inputs), same focus behavior. Includes a monospace placeholder like "Search inks, nibs, formulas…" to reinforce the laboratory register.

### Navigation

**`nav-bar`** — 64px tall, {colors.canvas} background, 1px {colors.hairline} bottom rule. Logo sits left; center links use {typography.title-sm} in {colors.ink}; right side holds search trigger, account icon, and cart count badge. On scroll past 80px the nav picks up a soft box-shadow rather than changing background, preserving the clean canvas.

**`collection-band`** — A full-width horizontal strip in {colors.surface-soft} below the nav, containing category scroll links (Inks / Pens / Nibs / Accessories / Limited) in {typography.title-sm}. Active category gets a 2px bottom border in {colors.primary}; inactive links are {colors.muted} at rest, {colors.ink} on hover.

### Product Card

**`product-card`** — White card, 1px {colors.hairline} border, {rounded.md} corners, {spacing.base} padding. Image fills top portion at 4:3 aspect ratio with a subtle {colors.surface-soft} placeholder background. Below the image: ink-color-label (monospace category code in uppercase muted text), product name in {typography.title-md}, price in {typography.body-md} ink, and a row of ink-swatch-badges when multiple colorways exist. Add-to-cart appears as a full-width button-primary on hover via overlay, keeping the card face clean at rest.

### Ink Swatch System

**`ink-swatch-badge`** — 36px circle filled with the ink's actual color, 2px {colors.ink-swatch-ring} border to separate dark swatches from the white card background. Swatches render in a flex row, max 5 visible with "+N" overflow pill in {colors.surface-soft}. Tooltip on hover shows the formula name and {typography.mono-spec} color code.

**`ink-color-label`** — Uppercase {typography.caption} in {colors.muted}, 0.08em letter-spacing. Used below the product card image to display the formula category code (e.g. "INK · SERIES 04") before the human-readable name. Acts as a sub-taxonomy signal without competing with the title.

### Technical Detail Components

**`nib-spec-tag`** — Small pill in {colors.surface-soft} with {typography.mono-spec} text in {colors.body}, {rounded.xs}. Displays values like "EF · 0.4mm" or "M · FLEX" adjacent to product titles and in spec tables. Multiple tags render inline-flex with {spacing.xs} gap.

**`formula-callout`** — A dark panel in {colors.surface-dark-raised} with a 3px left accent stripe in {colors.accent-cyan}. Body text uses {typography.mono-spec} in {colors.on-dark}. Used for ink chemistry notes, technical care instructions, and ingredient disclosures — the laboratory-notebook moment of the page. Internal padding {spacing.lg} on all sides; {rounded.sm} on the right corners only (flat left edge against the accent stripe).

**`lab-badge`** — A small pill badge in {colors.accent-cyan} background with {colors.ink} text, {typography.mono-label} at uppercase, {rounded.full}. Used for "NEW FORMULA," "LIMITED," "COLLAB," and "SOLD OUT" states on product cards and collection headers. The cyan-on-dark-ink contrast is intentional: readable at small size without relying on red for urgency.

### Hero

**`hero-dark`** — Full-bleed section in {colors.surface-dark} (#0F0E1A) with display headline in {typography.display-xl} set in {colors.on-dark}, subhead in {typography.body-md} {colors.on-dark} at 70% opacity, and a single button-primary below. An ambient ink-drop or gradient overlay in {colors.accent-cyan} at 5–8% opacity can be layered behind the type as a brand-texture detail. Vertical padding {spacing.section} top and bottom; max content width 1080px centered.

### Footer

**`footer`** — {colors.surface-dark} background, 1px {colors.hairline-dark} top rule, {spacing.section} top padding. Four columns: Brand / Shop / Support / Newsletter. Link text in {colors.on-dark} at {typography.body-sm}; hover state shifts links to {colors.accent-cyan} with no underline. Social icons rendered as 20px outlines in {colors.on-dark} at 60% opacity, full opacity on hover. Newsletter input sits in the fourth column using a dark-adapted text-input with {colors.hairline-dark} border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; collection-band becomes horizontal scroll strip; hero headline drops to {typography.display-md}; nib-spec-tags wrap to two lines; ink-swatch-badge row caps at 4 visible |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + 2 top categories + icons, remaining categories in overflow dropdown; hero uses constrained max-width with padding 48px each side; formula-callout renders full-width |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with collection-band below; hero max-width 1080px centered; product-card hover reveals add-to-cart overlay |
| Wide | > 1440px | Grid stays at 3–4 columns with increased gutter; hero content constrained to 1080px with background bleeding edge-to-edge; section padding scales to 80px |

### Touch Targets

- All interactive elements minimum 44×44px on mobile (button-primary, text-input, and nav icons already meet this)
- Ink-swatch-badges increase hit area to 44px via padding while visual size stays 36px
- Nib-spec-tags receive 8px vertical padding on mobile to prevent mis-tap in dense spec rows
- Collection-band category links receive 48px minimum touch height via paddingY expansion

### Collapsing Strategy

- Nav: logo + hamburger only below 744px; hamburger opens a full-screen drawer in {colors.surface-dark} with links in {typography.display-sm} and accent dividers in {colors.hairline-dark}
- Collection-band: horizontal scroll with snap points on mobile, no visible scrollbar, fade-out on right edge
- Product grid: 1 → 2 → 3 → 4 column as breakpoints increase; card aspect ratio stays fixed
- Hero: stacks image above text block on mobile; side-by-side from tablet up
- formula-callout: full-width on all breakpoints, padding reduces to {spacing.base} on mobile
- Footer: single column stack on mobile, 2-column at tablet, 4-column at desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All color tokens are inferred** — zero hex values were extracted from the live site. The palette is reconstructed from brand-name analysis (mad science / laboratory aesthetic) and pen-brand category conventions. Treat every hex value as a hypothesis requiring live-site verification.
- **All typography tokens are inferred** — no font-family stacks were returned by extraction. Playfair Display and Space Grotesk are proposed based on brand positioning; the actual site may use entirely different typefaces, including a proprietary or licensed font.
- **No platform confirmed** — the site is not identified as Shopify or any other known platform, so component structure assumptions (cart drawer, collection pages, product template) are based on generic DTC e-commerce patterns.
- **Logo treatment unknown** — wordmark vs. emblem, color usage on dark vs. light, minimum sizes, and clear-space rules cannot be determined without live assets.
- **Navigation structure unverified** — the number of top-level categories, presence of a mega-menu, and any loyalty or subscription program entry points are not confirmed.
- **Dark mode support unknown** — the dark hero and dark footer are assumed design zones, not a confirmed full-site dark mode toggle.
- **Motion and animation tokens absent** — no transition durations, easing curves, or animation patterns could be extracted; none are defined here.
- **Ink swatch implementation** — the circle-swatch system is inferred as common in pen/ink retail; actual implementation (SVG fills, CSS background, image sprites) is unconfirmed.
- **Lab-amber ({colors.lab-amber} #F5A623)** — included as a potential warning/highlight state color consistent with the laboratory theme; no confirmed usage found.
