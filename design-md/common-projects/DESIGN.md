---
version: alpha
name: "Common Projects"
source_url: "https://commonprojects.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Six digits embossed in gold on white leather — Common Projects built its entire identity on that one mark, and the website enforces the same logic: nothing decorative, no logomark, no swatch explosion, just a stark white canvas where the product photograph does the persuading. The single extracted color, #e9e9e9, turns up as the hairline rule and faint surface separators; against canvas white (#ffffff) and near-black ink (#111111), it barely registers, which is the point. Product pages strip navigation to the minimum — a wordmark in fine-weight roman type, a category dropdown, a bag count. The brand's signature gold (#b8963c) appears only on the serialized stamp rendered in editorial photography, never as a UI accent; using it as a button would break the spell. Body copy runs in a neutral sans-serif, lowercase category labels, all numbers in tabular figures so size grids sit perfectly flush. Rounded corners are functionally absent — images bleed full to their containers, form inputs carry `{rounded.none}`, and size-selector tiles share the same hard-edged square. Spacing is generous: product listings breathe at `{spacing.section}` vertical intervals, image crops feel uncropped, and the add-to-cart bar emerges from the bottom of the viewport on scroll without a drop shadow — just a crisp 1px hairline at `{colors.hairline}`. The whole system reads like a deliberately deflated luxury object: value is communicated by what is absent rather than added.

colors:
  primary: "#111111"
  primary-active: "#333333"
  primary-disabled: "#999999"
  ink: "#111111"
  body: "#333333"
  muted: "#777777"
  hairline: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gold-stamp: "#b8963c"
  size-active: "#111111"
  size-inactive: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.04em
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.03em
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0.02em
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0.02em
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em
  label-uppercase:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.02em
  stamp-mono:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.14em

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
    padding: 14px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 23px
    height: 48px
  size-swatch-active:
    backgroundColor: "{colors.size-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    width: 48px
    height: 48px
  size-swatch-inactive:
    backgroundColor: "{colors.size-inactive}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    width: 48px
    height: 48px
  size-swatch-soldout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-disabled}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    textDecoration: line-through
    width: 48px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: none
    borderBottom: "1px solid {colors.ink}"
    padding: "12px 0"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "4/5"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  product-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    border: "1px solid {colors.ink}"
    padding: "4px 8px"
    rounded: "{rounded.none}"
  sticky-add-to-cart:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    imagePosition: center
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "6px 12px"
  filter-chip-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "6px 12px"
  serial-stamp:
    textColor: "{colors.gold-stamp}"
    typography: "{typography.stamp-mono}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"

## Components

### Buttons
**`button-primary`** — Flat black fill (`{colors.primary}`), white text, zero radius, all-caps wide-tracked label via `{typography.button-md}`. The only state change on hover is a subtle opacity shift to ~85%; no color transition, no elevation. Disabled state uses `{colors.primary-disabled}` and does not alter the shape contract — the form remains the same, the color drains out.

**`button-secondary`** — White fill with a 1px ink border, same all-caps typography. Used for secondary PDPs actions such as "Add to Wishlist." The border softens to `{colors.hairline}` on hover, signaling interactivity without any motion.

### Size Selector
**`size-swatch-active`** / **`size-swatch-inactive`** / **`size-swatch-soldout`** — 48×48px square tiles, no radius, arranged in a tight grid with `{spacing.sm}` gaps. Selected fills black with white text; available shows white with a hairline border; sold-out renders in `{colors.surface-soft}` with `{colors.primary-disabled}` text and a diagonal CSS strikethrough. No swatch is ever rounded — even the size grid refuses softness.

### Text Input
**`text-input`** — Underline-only treatment: no visible left, right, or top border; a 1px bottom border in `{colors.ink}` is the sole visible boundary. Zero border-radius. Placeholder text in `{colors.muted}`. Search and contact forms share this same rule without variation; the input system has no component variants, only this one.

### Nav Bar
**`nav-bar`** — 56px tall, white background, wordmark at far left in `{typography.nav-link}`, category links centered, bag icon at far right. A 1px `{colors.hairline}` runs the full bottom edge. On scroll the bar goes sticky; no shadow, no blur, no background change — the hairline alone marks the boundary.

### Product Card
**`product-card`** — Full-bleed 4:5 image, zero radius, product name in `{typography.body-sm}` and price in `{typography.price-display}` stacked below. Color variant counts display as plain text — "3 colors" — never as swatches. No add-to-cart affordance lives in the card; the purchase action is reserved entirely for the PDP.

### Hero
**`hero`** — Full-viewport editorial image, white canvas for any text overlays, headline in `{typography.display-xl}` at weight 300. No gradient scrim, no graphic overlay, no CTA button within initial viewport. The first screen is a lookbook spread; a scroll or nothing is the only affordance.

### Sticky Add-to-Cart Bar
**`sticky-add-to-cart`** — Pins to the bottom of the viewport once the inline ATC button scrolls out of frame. White background with a single 1px top hairline (`{colors.hairline}`). Displays product name, selected size confirmation, and the black primary button. No shadow, no blur, no transition animation — it appears and disappears as a hard cut.

### Serial Stamp
**`serial-stamp`** — Typographic echo of Common Projects' physical product stamp: a six-digit string in `{colors.gold-stamp}` set in `{typography.stamp-mono}` with wide tracking. Appears in editorial photography captions and product detail provenance sections. Never used as an interactive or structural UI element — contact with the gold breaks the minimalist contract.

### Filter Chips
**`filter-chip-active`** / **`filter-chip-inactive`** — Square-cornered filter tokens for category and size refinement on listing pages. Active fills black; inactive shows hairline border on white. The hardness of the shape prevents the filter row from reading as decorative chrome.

### Product Badge
**`product-badge`** — 1px ink-bordered label in `{typography.label-uppercase}` for editorial callouts such as "New" or a season name. White background, no radius, padding `4px 8px`. Used sparingly — one badge per product grid view at most.

### Footer
**`footer`** — White background, 1px top hairline, muted `{typography.body-sm}` type. Four to five text columns (Men, Women, About, Stockists, Contact) with no visual dividers beyond column spacing. Legal and copyright lines use the same weight and color as column links; nothing is deprioritized.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + bag icon; sticky ATC bar spans full width; size swatches wrap across two rows |
| Tablet | 744–1128px | Two-column product grid; nav shows full category links inline; hero crops to 16:9; filters move to horizontal scroll strip |
| Desktop | 1128–1440px | Three- or four-column product grid; sidebar filter panel becomes persistent left rail; hero restores to full-bleed portrait |
| Wide | > 1440px | Grid capped at ~1400px max-width, centered with equal side margins; type scale and spacing unchanged |

### Touch Targets
- Size swatches maintain 48×48px minimum on all touch viewports
- Nav icons (bag, hamburger) padded to a minimum 44×44px tap area
- Filter chips carry minimum 40px height; container scrolls horizontally on mobile

### Collapsing Strategy
- Primary nav links collapse into a full-screen overlay drawer on mobile — no partial-width panel
- Product filters shift from a persistent left rail to a modal sheet triggered by a plain "Filter" text button
- Footer columns stack vertically at mobile; column headers remain as non-interactive plain-text labels

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color was extractable (`#e9e9e9`); the site likely renders design tokens via client-side JavaScript or sits behind anti-bot protection — the full palette could not be confirmed
- No font stacks were found in extracted CSS; typography is inferred from widely documented brand conventions (clean neutral sans-serif consistent with Helvetica Neue) rather than confirmed computed values
- The gold serial number color (`#b8963c`) is a reasoned approximation based on published product photography, not an extracted or officially stated value
- Exact button padding, nav height, grid gutter measurements, and breakpoint pixel values are estimated from observed brand patterns rather than measured from source
- Dark mode support (if any) is unknown
- Whether the brand uses a custom or licensed typeface beyond system sans-serif is unconfirmed without font-loading inspection
