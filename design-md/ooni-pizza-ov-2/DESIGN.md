---
version: alpha
name: "Ooni"
source_url: "https://ooni.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The amber-on-charcoal contrast—#ffc633 punching against the near-black #25282a—is the visual metaphor that structures the entire Ooni system: fire against coal. That single chromatic tension generates an appetite that product photography amplifies at every scroll, ovens photographed mid-flame with glowing mouths, caught at the moment of peak heat. The orange-to-brick gradient embedded in the extracted palette—#f48120, #f37521, #e16f27, #d4602c, #bc3c26—maps almost exactly to a wood fire burning from bright crown to dying ember; the product is made chromatic and the design system reflects it deliberately. Primary CTAs carry the amber voltage at a {rounded.xs} radius that reads as machined and precise rather than consumer-soft.

  The canvas splits by context. Editorial and category pages run deep charcoal #25282a backgrounds that frame ovens as serious high-heat instruments, while shopping and comparison grids shift to near-white #f5f5f5 where specification tables require legibility. Surfaces stack predictably along a single coal axis: #0b1318 at the deepest UI layer, #293035 for containers, #575a5d for secondary labels, #c1c2c3 as hairlines dividing product spec rows. No pastels, no cross-hue gradients—every ramp step moves from near-black toward pale ash, anchored by fire-orange as the only warm interruption.

  No custom typeface was recoverable from the live site; assets load through a JS bundle that evades static extraction. The heading posture—short, declarative, weight-forward—suggests a condensed or semi-condensed geometric sans. Buttons carry sentence-case labels at 15px on a 48px touch target; hover and active states step to #ffd057, a brighter amber, keeping the fire-tone vocabulary intact rather than reaching for a separate active-color family. Fuel-type taxonomy—wood, gas, charcoal, multi-fuel—drives a badge system on product listing cards that lets shoppers filter without opening a detail page. Temperature callouts such as 850°F and 950°F surface in oversized display numerics that function as typographic performance claims, foregrounding the oven's core value proposition. Corners hold to {rounded.xs} on interactive elements and {rounded.sm} on cards; no pill shapes appear. This is a brand whose products reach 950°F, and the geometry reflects it with the same no-nonsense precision.

colors:
  primary: "#ffc633"
  primary-active: "#ffd057"
  primary-disabled: "#c1c2c3"
  ink: "#25282a"
  body: "#293035"
  muted: "#575a5d"
  muted-mid: "#6b6a68"
  hairline: "#c1c2c3"
  hairline-soft: "#e2e2e2"
  canvas: "#f5f5f5"
  canvas-dark: "#25282a"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#17191a"
  on-dark: "#f5f5f5"
  deep-dark: "#0b1318"
  mid-dark: "#17191a"
  fire-orange: "#f48120"
  fire-ember: "#e16f27"
  fire-brick: "#bc3c26"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.75px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.11
    letterSpacing: -0.4px
  display-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  spec-number:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  badge-label:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.6px
    textTransform: uppercase
  promo-text:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.1px

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
    padding: 14px 24px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 22px
    height: 48px
  button-secondary-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.on-dark}"
    rounded: "{rounded.xs}"
    padding: 12px 22px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
    logoColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageBorderRadius: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    captionTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.hairline-soft}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"
    minHeight: 540px
    paddingX: "{spacing.xxl}"
  fuel-type-badge:
    rounded: "{rounded.xs}"
    typography: "{typography.badge-label}"
    padding: 4px 10px
    wood:
      backgroundColor: "{colors.fire-brick}"
      textColor: "{colors.on-dark}"
    gas:
      backgroundColor: "{colors.body}"
      textColor: "{colors.on-dark}"
    charcoal:
      backgroundColor: "{colors.deep-dark}"
      textColor: "{colors.on-dark}"
    multi:
      backgroundColor: "{colors.fire-orange}"
      textColor: "{colors.on-primary}"
  temp-callout:
    numberTypography: "{typography.spec-number}"
    numberColor: "{colors.primary}"
    unitTypography: "{typography.title-md}"
    unitColor: "{colors.muted}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.title-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    padding: "{spacing.md} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    inputTypography: "{typography.body-md}"
    iconColor: "{colors.muted}"
    height: 48px
  oven-size-chip:
    backgroundColor: "{colors.surface-soft}"
    selectedBackgroundColor: "{colors.ink}"
    textColor: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    typography: "{typography.button-sm}"
    padding: 8px 18px
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.promo-text}"
    height: 40px
    textAlign: center
  footer:
    backgroundColor: "{colors.deep-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-soft}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    paddingTop: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Amber `#ffc633` fill on a 4px `{rounded.xs}` radius, 48px tall, sentence-case label at 15px/600 weight, dark `#17191a` text for contrast on the warm background. Hover steps up to `#ffd057`, a brighter amber that maintains the fire-tone palette rather than introducing a separate active-color family. Disabled state collapses to the `#c1c2c3` hairline gray with muted text.

**`button-secondary`** — Transparent fill with a 2px `{colors.ink}` border on the same 48px height and `{rounded.xs}` radius. Inverts to `button-secondary-on-dark` for use on charcoal hero sections, swapping ink border and text for `{colors.on-dark}` `#f5f5f5`.

### Text Input

**`text-input`** — White fill, `{colors.hairline}` border tightening to `{colors.ink}` on focus, 4px radius. Sized at 48px to match button touch targets, keeping checkout and search flows dimensionally consistent.

### Navigation

**`nav-bar`** — Full-width charcoal `#25282a` strip at 64px, no border-bottom, logotype in amber `{colors.primary}`. Links in `{typography.nav-link}` 15px/500 weight, `{colors.on-dark}` white. The dark nav anchors every page in the brand's fire-against-coal register regardless of page section color.

### Product Card

**`product-card`** — White card on a soft `{colors.hairline-soft}` border, `{rounded.sm}` 8px corners, 16px internal padding. Title at `{typography.title-md}` 18px/600, price at `{typography.title-sm}` 15px/600. Hover adds a subtle shadow (0 4px 16px rgba black 10%) to lift the card without animation cost. Fuel-type badges sit in the upper corner of the card image.

### Hero

**`hero-dark`** — Charcoal `#25282a` full-bleed section, minimum 540px tall, headline at `{typography.display-xl}` 52px/700 in `{colors.on-dark}`, body copy at 16px/400 in `{colors.hairline-soft}` for reduced weight against the dark field. CTA renders as `button-primary`. Intended for campaign and homepage entry points where fire photography bleeds through the dark field.

### Fuel Type Badges

**`fuel-type-badge`** — Uppercase 11px/600 labels at 0.6px letter-spacing on 4px `{rounded.xs}` chips. Four variants keyed by fuel: wood in fire-brick `#bc3c26`, gas in body-dark `#293035`, charcoal in deepest `#0b1318`, multi-fuel in fire-orange `#f48120`. Applied directly to product card images and listing filter chips.

### Temperature Callout

**`temp-callout`** — Oversized 42px/700 numeral in amber `{colors.primary}` beside a 18px/600 unit label in `{colors.muted}`. A 12px caption below the number names the measurement context (e.g. "Max oven temperature"). Functions as a typographic marketing claim surfaced in product detail heroes and comparison tables.

### Spec Table Row

**`spec-table-row`** — Two-column row on a `{colors.canvas}` `#f5f5f5` ground, divided by `{colors.hairline}` bottom border. Label column in 14px/400 `{colors.muted}`, value column in 15px/600 `{colors.ink}`. Used for weight, dimensions, fuel type, max temperature, and warranty data across product detail pages.

### Oven Size Chip

**`oven-size-chip`** — Filter and selection pill in `{rounded.full}` with `{colors.surface-soft}` default background and `{colors.hairline}` border. Selected state fills with `{colors.ink}` charcoal and inverts text to `{colors.on-dark}`. Used in size and model selectors on product detail and comparison pages.

### Promo Banner

**`promo-banner`** — Amber `{colors.primary}` full-width bar at 40px, centered `{typography.promo-text}` in `{colors.on-primary}` dark text. Hosts shipping threshold messages, seasonal discount codes, and new product announcements above the nav bar.

### Footer

**`footer`** — Deepest `#0b1318` background anchored by a 3px `{colors.primary}` amber top border that echoes the nav's amber-on-dark register. Heading labels in 15px/600 `{colors.on-dark}`, body links in `{colors.hairline-soft}` at 14px/400. The amber top rule is the sole decorative element.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero headline drops to `{typography.display-md}` 36px; temp callouts stack vertically; spec table scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links, hides tertiary; hero padding reduces to `{spacing.xl}`; fuel-type badge chips wrap freely |
| Desktop | 1128–1440px | Three-column product grid; full nav expanded; hero min-height increases to 600px; temp callout cluster aligns horizontally in a stat row |
| Wide | > 1440px | Content max-width 1440px centred on `{colors.canvas}` or `{colors.canvas-dark}` bleed; four-column grid on category pages; hero headline may reach `{typography.display-xl}` at full 52px |

### Touch Targets

- All interactive elements minimum 48px height and 48px width
- Fuel-type filter chips minimum 44px height on mobile with 8px horizontal gap
- Nav links padded to full 64px nav bar height for tap target coverage
- Oven size chips minimum 44px tall on mobile

### Collapsing Strategy

- Nav: primary product category links remain visible at tablet; account, cart, and search icons persist; hamburger reveals full link tree on mobile
- Hero: headline font-size scales from 52px (desktop) to 36px (mobile) in two steps; body copy hides on smallest breakpoint to reduce scroll depth
- Spec table: full table collapses to a single scrollable row on mobile rather than stacking, preserving label-value alignment
- Comparison grid: side-by-side oven comparison collapses to a swipeable carousel on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font family extracted — site loads typefaces via JS asset pipeline; heading font is visually a bold geometric or condensed sans but could not be identified by name or file reference
- Blues `#006fcf` and `#3086c8` and orange `#ff9900` appear to originate from Shopify payment-method badges and Amazon Pay widgets, not brand design tokens; excluded from palette
- Exact border-radius values for product image frames could not be confirmed; `{rounded.sm}` is inferred from visual inspection of comparable Shopify-hosted DTC sites
- Dark mode / light mode split logic (which sections use charcoal vs. white canvas) was not derivable from static extraction; the canvas-dark / canvas split above is based on observed page structure patterns
- Hover and focus ring styling (color and width) not confirmed; current spec is inferred from brand conventions
- Specific font weights for display headings (whether 700 or 800/900) could not be verified without font file access
- Exact letter-spacing values for headline sizes are estimated; no design tokens file was publicly accessible
