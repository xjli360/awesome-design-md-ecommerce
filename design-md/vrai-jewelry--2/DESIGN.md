---
version: alpha
name: "Vrai"
source_url: "https://vrai.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The first thing that registers at vrai.com is the deliberate evacuation of color — not as neglect but as argument. Every surface runs on a near-monochrome system where #241f20, a warm charcoal carrying a barely perceptible amber undertone, serves as the single brand ink pressed against an off-white #f7f7f7 canvas that the meta theme-color tag confirms as the site's base temperature. No accent hue punctuates the grid, no gradient bridges the transitions — the diamonds are the chromatic event, and the surrounding UI steps entirely aside to let them be. Button labels, navigation links, price displays, and heading hierarchies all resolve to that same near-black or its close relative #3c3c3b, with #9ca3af absorbing secondary and placeholder roles: a palette of exactly three luminance levels. The engagement ring configurator — the brand's signature interaction — embeds this restraint inside a precision tool, letting customers sequence cut, setting, and metal through clean-edged selector tiles with no decorative distraction. Because the site loads typography via JavaScript (no font-family stacks were capturable at extraction time), the type system here is reconstructed from visual context: thin-weight serifs for display headings signal the editorial fine jewelry register, while a geometric sans handles UI labels and body copy with near-zero default letter-spacing and tracked uppercase for functional text. Corners lean toward minimal radius — `{rounded.none}` and `{rounded.xs}` rather than the pill-shaped softness of lifestyle brands — which reads as architectural rather than cold. Spacing is generous and even: `{spacing.xl}` gutters between product cards, `{spacing.section}` breathing room above hero text. The net effect is a site that performs the logic of a light-filled showroom — white walls, one object at a time — rather than a conventional e-commerce grid.

colors:
  primary: "#241f20"
  primary-active: "#010101"
  primary-disabled: "#9ca3af"
  ink: "#241f20"
  body: "#3c3c3b"
  muted: "#9ca3af"
  hairline: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#f7f7f7"
  charcoal-mid: "#3c3c3b"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  micro-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 0"
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-announcement:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.micro-label}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    imagePadding: "{spacing.lg}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    gap: "{spacing.md}"
  hero-full:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    textAlign: center
    paddingV: "{spacing.section}"
    ctaMarginTop: "{spacing.lg}"
  diamond-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    activeBorderColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    tileSize: 80px
  ring-configurator:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"
    dividerColor: "{colors.hairline}"
    stepIndicatorColor: "{colors.ink}"
    rounded: "{rounded.none}"
  metal-swatch:
    size: 28px
    rounded: "{rounded.full}"
    activeBorder: "2px solid {colors.ink}"
    inactiveBorder: "1px solid {colors.hairline}"
  badge-sustainable:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.none}"
    padding: "4px {spacing.sm}"
  pdp-detail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price-display}"
    descriptionTypography: "{typography.body-md}"
    dividerColor: "{colors.hairline}"
    sectionSpacing: "{spacing.lg}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} 0"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.micro-label}"
    padding: "{spacing.xxl} {spacing.xl}"
  modal-overlay:
    backdropColor: "rgba(36, 31, 32, 0.5)"
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-md}"
    lineItemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    borderColor: "{colors.hairline}"
    width: 400px

## Components

### Buttons
**`button-primary`** — A sharp-edged rectangle (`{rounded.none}`) in near-black #241f20 with #f7f7f7 label text set in tracked uppercase `{typography.button-md}` at 13px. Active state deepens to `{colors.primary-active}` (#010101); the disabled state shifts to `{colors.primary-disabled}` (#9ca3af), indicating unavailability without reaching for red. Height is consistently 48px. The hard corner is non-negotiable — it runs through every button variant as a house rule.

**`button-secondary`** — Canvas-white fill with a 1px `{colors.primary}` border and matching ink label in the same uppercase tracked typography. Paired alongside `button-primary` in the ring configurator CTA area and PDP, forming a visual hierarchy through fill contrast rather than size or shape difference. Both variants share identical height and corner treatment.

**`button-ghost`** — Transparent fill, no border radius, delineated only by a bottom-border underline in `{colors.ink}`. Appears in editorial contexts — "Learn more about lab-grown diamonds," "Compare stones" — where a full-fill button would overpower flowing prose. Carries the same uppercase tracking as the heavier variants to maintain family cohesion.

### Text Input
**`text-input`** — Square-cornered (`{rounded.none}`) at 48px height, 1px `{colors.hairline}` border at rest, tightening to `{colors.ink}` on focus with no radius anywhere in the form system. Placeholder in `{colors.muted}` (#9ca3af). Used in email capture, ring-size entry, gift message fields, and site search. The form system is zero-softness throughout.

### Navigation
**`nav-bar`** — 64px tall white canvas, `{colors.hairline}` bottom border. Navigation links render in `{typography.nav-link}` (13px, lightly tracked) with no hover background fill — only a subtle tone shift. A 36px announcement bar (`nav-bar-announcement`) sits above in `{colors.surface-soft}`, carrying sustainability or promotion copy in `{typography.micro-label}` uppercase. The wordmark anchors left; cart and account icons sit right.

### Product Card
**`product-card`** — Square `{colors.surface-soft}` tile with generous internal image padding (`{spacing.lg}`) so rings float on off-white rather than bleeding to the tile edge. Product name in `{typography.title-sm}`, price in `{typography.price-display}` (serif, 18px, normal weight). No border, no shadow, no radius — the card is defined entirely by its background tone against the page canvas. Hover triggers no transform, only a subtle image-scale at 1.02.

### Hero
**`hero-full`** — Full-width section anchored to `{colors.surface-soft}` or editorial photography. Headline in `{typography.display-xl}` (48px, 300 weight serif), centered, with `{spacing.section}` vertical padding producing the airy register the brand trades in. CTA sits `{spacing.lg}` below headline text. On collection landing pages, the hero shrinks to `{typography.display-md}` (32px) and left-aligns within the content grid.

### Diamond Selector
**`diamond-selector`** — The brand's signature interaction unit. An evenly spaced grid of 80px square tiles, each displaying a cut silhouette (round, oval, cushion, pear, emerald, etc.) on a white ground with `{colors.hairline}` border at rest. Active selection tightens the border to `{colors.ink}` with no fill change — selection state communicated by border weight alone. Category label below the icon in `{typography.caption}` uppercase. The same tile system handles cut, carat range, and setting style steps.

### Ring Configurator
**`ring-configurator`** — A multi-step sequencing tool that walks the customer through diamond, setting, and metal choices before landing on a fully specified product. Each step uses `{typography.caption}` uppercase labels with `{typography.body-md}` values, separated by 1px `{colors.hairline}` dividers. A horizontal step indicator in `{colors.ink}` tracks progress. Metal choices render as 28px `metal-swatch` circles with `{rounded.full}` and a 2px ink border on the active selection. On desktop, the live ring preview renders alongside the step panel; on mobile, it stacks above.

### Sustainability Badge
**`badge-sustainable`** — A flat rectangular chip (`{rounded.none}`) in `{colors.surface-soft}` with `{typography.micro-label}` uppercase copy in `{colors.body}`. Surfaces "zero-mine," "carbon-neutral," and certification claims without creating visual hierarchy disruption. Appears in PDP sidebars, cart drawers, and the environmental messaging section of the footer.

### PDP Detail Panel
**`pdp-detail`** — Right-column layout on desktop with product title in `{typography.display-sm}` (serif, 24px), price in `{typography.price-display}`, and descriptive copy in `{typography.body-md}`. Below the CTA cluster, `accordion` components expand material details, sizing information, and sustainability facts. Every divider is 1px `{colors.hairline}` with `{spacing.base}` vertical rhythm. On mobile, the panel sits below a full-width image with sticky CTA bar anchored to the viewport bottom.

### Accordion
**`accordion`** — Used throughout PDP and editorial pages for expandable detail. Row label in `{typography.title-sm}`, body in `{typography.body-sm}`, separated by full-width `{colors.hairline}` rules. Chevron icon rotates 180° on open. No background fill change on expand — the content simply reveals beneath the rule. Consistent `{spacing.base}` padding top and bottom on each row.

### Footer
**`footer`** — Fully inverted: `{colors.primary}` (#241f20) background against `{colors.on-primary}` text. Section column headings in `{typography.micro-label}` (uppercase, heavily tracked), link lists in `{typography.body-sm}`. The dark footer creates a deliberate visual bracket against the light-canvas body — it is the only moment of full-bleed intentional color in the layout. Four columns on desktop, collapsing to accordion rows on mobile.

### Cart Drawer
**`cart-drawer`** — A 400px right-anchored panel over a 50% opacity backdrop, sharing the modal's `rgba(36, 31, 32, 0.5)` scrim. Canvas-white interior with `{colors.hairline}` dividers between line items. Header in `{typography.title-md}`, line item names in `{typography.body-sm}`, prices in `{typography.price-display}`. CTA buttons at bottom use the standard `button-primary` spec. No border radius on the panel itself.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen canvas drawer; hero headline drops to `{typography.display-md}`; ring configurator steps stack vertically with preview above, inputs below |
| Tablet | 744–1128px | Two-column product grid; primary nav links visible but condensed; hero text left-aligns; PDP splits 50/50 image and detail panel |
| Desktop | 1128–1440px | Three-column product grid; full nav with all category links; hero center-aligned `{typography.display-xl}`; configurator shows step panel alongside live ring preview |
| Wide | > 1440px | Content max-width ~1280px centered; viewport-edge whitespace grows; hero image bleeds full-viewport width while text block remains grid-constrained |

### Touch Targets
- Diamond selector tiles: minimum 44×44px, typically rendered at 80px square
- Metal swatches (28px circles): padded to 44px hit area with invisible padding
- Nav drawer links: 48px row height minimum, full-width tap zone
- CTA buttons: locked to 48px height at all breakpoints
- Accordion rows: 48px tap target, full-width activation area
- Cart icon and account icon in nav: minimum 40px touch target

### Collapsing Strategy
- Navigation: wordmark stays centered; hamburger icon triggers full-screen overlay in canvas white
- Product grid: 3-col → 2-col at tablet breakpoint; 2-col → 1-col at mobile with sticky viewport-bottom CTA
- Ring configurator: side-by-side (preview + steps) → stacked (preview top, scrollable steps below)
- Footer: 4-col grid → 2-col at tablet → single-column accordion at mobile
- Announcement bar persists at all breakpoints; text truncates with horizontal scroll if overflow
- PDP sticky CTA bar appears at mobile only, anchored to viewport bottom above safe-area inset

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stacks extractable — typography loads via JavaScript. All font-family values in this file are system-fallback stacks; the actual brand typefaces (likely a licensed editorial serif for display and a geometric sans for UI) are unknown.
- Hairline color (#e2e2e2) is inferred from typical fine jewelry UI conventions, not extracted directly from the site.
- #9ca3af matches Tailwind CSS gray-400 exactly and may originate partially from framework defaults rather than intentional brand token usage — treat with caution.
- Interactive state colors for non-primary elements (hover tones on nav links, accordion chevrons, swatch borders) are inferred from the overall system, not confirmed.
- Exact ring configurator transition durations, easing curves, and animation sequencing are not captured.
- Mobile navigation drawer layout (header, close button placement, sub-menu behavior) is not confirmed.
- Section-level padding on configurator, editorial, and PDP templates may differ from the inferred spacing scale.
- Dark/inverted footer link hover states are not extractable.
