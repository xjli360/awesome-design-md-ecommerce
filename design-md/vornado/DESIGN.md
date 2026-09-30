---
version: alpha
name: "Vornado"
source_url: "https://www.vornado.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The vortex spiral pressed into every Vornado housing — its physical signature of air-column engineering — carries into the digital system as one act of visual compression: nearly everything routes through #d3161f, an industrial red with no warm undertone, punched against deep charcoal (#2d2d2d) and a cool near-white (#f4f4f4) grid with no softening intermediary. This is not a brand that distributes energy across a spectrum of accent colors; it bets the entire CTA layer on one signal, trusting the red to do simultaneous work as buy button, sale badge, urgency callout, and hover state. The discipline reads closer to power-tool branding than home-comfort lifestyle.

  Typography runs entirely on system stacks — Arial and Helvetica Neue — at weights that match the mechanical directness of the hardware. Display headlines sit at 700 weight and 36–48px; the heaviness is structural, echoing the solidity of cast-plastic housings rather than decorating a page. Body copy drops to 400/16px for legibility through spec-dense product pages where airflow ratings, BTU figures, and wattage numbers compete with marketing copy. No custom typeface was found in the extracted stacks; the plainness keeps attention on product photography and engineering credentials.

  Secondary system colors follow functional logic rather than aesthetic variety. A saturated cyan (#00aeef) handles informational UI, links, and select promotional callouts — its coolness reads as technical precision beside the hot red. An environmental green (#2f8541) isolates energy-efficiency badges and eco-claims, keeping them visually distinct from the commerce layer. Lavender (#e5dbed) and warm cream (#fbf3eb) surfaces appear on seasonal or curated collection tiles as promotional anomalies — present in the extracted palette but not structural regulars.

  Corner geometry is controlled and rectilinear: `{rounded.xs}` at 4px on buttons and inputs, `{rounded.sm}` at 8px on cards. No pill shapes exist in the primary product UI. Spec data — CFM, square footage coverage, decibel ratings — surfaces at the product-card level rather than hiding behind a tap. The overall effect mirrors the product's industrial transparency: you are buying an appliance, and the interface does not pretend otherwise.

colors:
  primary: "#d3161f"
  primary-active: "#b3131a"
  primary-disabled: "#e8a0a3"
  accent-blue: "#00aeef"
  accent-green: "#2f8541"
  accent-pink: "#ef2d8e"
  ink: "#1a1a1a"
  body: "#2d2d2d"
  muted: "#595959"
  muted-soft: "#808080"
  hairline: "#d3d3d3"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ededed"
  surface-warm: "#fbf3eb"
  surface-lavender: "#e5dbed"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    ctaAccentColor: "{colors.primary}"
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xl} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imagePadding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.label-caps}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    overlayColor: "rgba(26,26,26,0.45)"
    minHeight: 480px
    padding: "{spacing.xxl} {spacing.section}"
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 400px
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  energy-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  info-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    submitIconColor: "{colors.primary}"
    height: 40px
    padding: "0 {spacing.base}"
  spec-row:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  sticky-atc:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTop: "2px solid {colors.hairline}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.md} {spacing.base}"
    zIndex: 100
  category-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    borderActive: "2px solid {colors.primary}"
    textColorActive: "{colors.primary}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.label-caps}"
    linkTypography: "{typography.body-sm}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.section}"
  collection-tile-warm:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    rounded: "{rounded.sm}"
  collection-tile-lavender:
    backgroundColor: "{colors.surface-lavender}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — Solid #d3161f fill with white text at `{typography.button-md}` weight 700, 44px height, and a 4px corner radius (`{rounded.xs}`). On hover the fill deepens to `{colors.primary-active}` (#b3131a) with no other change. The disabled state uses `{colors.primary-disabled}` — a desaturated dusty pink — keeping the red family visible without signaling affordance. No drop shadow; the color alone carries the click signal.

**`button-secondary`** — White fill with a 2px `{colors.primary}` border and matching red label text. On hover, fill shifts to `{colors.surface-soft}` and border deepens to `{colors.primary-active}`. Used for secondary actions like "Compare" and "Learn More" where a full red fill would compete with the primary add-to-cart.

**`button-ghost`** — Transparent background, `{colors.ink}` text, no border, 8px padding. Used for tertiary nav actions and inline text-links within content blocks where any visible boundary would add visual noise.

### Text Input
**`text-input`** — White canvas, 1px `{colors.hairline}` border, `{rounded.xs}` radius, 44px height. On focus, the border upgrades to 2px solid `{colors.primary}` — consistent with the brand's single-accent discipline. Error states inherit the red border with an inline error message in `{typography.caption}` below the field.

### Navigation
**`nav-bar`** — 64px tall, white canvas with a 1px bottom hairline divider. Logo and menu text in `{colors.ink}` at `{typography.nav-link}` weight 700. Cart and account icons in ink. The primary shop CTA accent renders in `{colors.primary}` red. A mega-menu drops on hover with a 3px red top accent border and two-column category links at `{typography.body-sm}`.

### Product Card
**`product-card`** — White background, 1px `{colors.hairline-soft}` border, `{rounded.sm}` corner. Product name in `{typography.title-sm}` weight 600; price in `{typography.price-display}` weight 700. Sale badges stack in the top-left corner as `{colors.primary}` filled rectangles with `{typography.label-caps}` uppercase text. On hover, a shallow shadow (0 4px 12px rgba) lifts the card without animating its position.

### Hero Banner
**`hero-banner`** — Full-width, minimum 480px tall. Sits on a `{colors.body}` charcoal base or a full-bleed photo with a semi-transparent dark overlay; headline in `{typography.display-xl}` white, subhead in `{typography.body-md}` white, anchored by a `button-primary` CTA. The light variant (`hero-banner-light`) uses `{colors.surface-soft}` background for category landing pages and product-family introductions.

### Badges
**`promo-badge`** — `{colors.primary}` fill, white text, `{typography.label-caps}`, `{rounded.xs}`. Stacks on the product-card corner for promotional and sale messaging.

**`energy-badge`** — `{colors.accent-green}` (#2f8541) fill, same typography and radius. Reserved strictly for energy-efficiency and eco-claims; never used for discount callouts, maintaining a hard semantic boundary between eco and sale.

**`info-badge`** — `{colors.accent-blue}` (#00aeef) fill for technical certifications, shipping-status chips, and compatibility callouts. The cyan coolness signals information rather than urgency.

### Search Bar
**`search-bar`** — `{colors.surface-soft}` fill, `{rounded.xs}`, 40px height, inline search icon in `{colors.muted}`. The submit trigger accents in `{colors.primary}` red. Lives inline in the nav on desktop; expands to a full-width overlay on mobile tap.

### Spec Row
**`spec-row`** — `{colors.surface-card}` background, 1px bottom hairline. Label in `{typography.label-caps}` `{colors.muted}`; value in `{typography.body-sm}` `{colors.ink}`. Used in product detail pages to surface airflow (CFM), coverage area, power draw, and noise level in a scannable table format. Scrolls horizontally before reflowing to single-column on narrow viewports.

### Sticky Add-to-Cart
**`sticky-atc`** — Fixed to the viewport bottom once the user scrolls past the primary ATC zone. White canvas with a 2px top hairline, price in `{typography.price-display}`, and a full-width `button-primary`. Z-index 100. Condenses to a slim bar on mobile with price and button side-by-side.

### Category Pill
**`category-pill`** — `{colors.surface-card}` fill, `{rounded.xs}`, `{typography.button-sm}`. The active state gains a 2px `{colors.primary}` border and red label text; inactive pills remain neutral. Used on collection pages to filter by product type (Fans, Heaters, Air Purifiers, Humidifiers, etc.).

### Footer
**`footer`** — `{colors.body}` (#2d2d2d) background with a 4px `{colors.primary}` red top accent stripe as the only brand signal in an otherwise neutral dark shell. Column headings in `{typography.label-caps}` white; links in `{typography.body-sm}` `{colors.hairline}` (#d3d3d3), turning `{colors.canvas}` white on hover. Four-column layout on desktop, single-accordion on mobile.

### Collection Tiles
**`collection-tile-warm`** and **`collection-tile-lavender`** — Promotional tiles using `{colors.surface-warm}` (#fbf3eb) and `{colors.surface-lavender}` (#e5dbed) respectively, both at `{rounded.sm}` with `{typography.display-sm}` headlines in `{colors.ink}`. These break the dominant gray-white-red grid for seasonal or lifestyle promotions without introducing new structural tokens.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + logo + cart icon. Search expands full-width overlay. Product grid 1-column. Sticky ATC condenses to slim bar. Hero min-height 320px; subhead hides below 375px. Footer becomes accordion. |
| Tablet | 744–1128px | Nav shows top-level category labels; mega-menu still available via tap. Product grid 2-column. Hero at 400px. Footer 2-column. Spec rows scroll horizontally. |
| Desktop | 1128–1440px | Full nav-bar with hover mega-menu. Product grid 3–4 column. Hero full 480px+. Footer 4-column. Spec rows render as side-by-side table. |
| Wide | > 1440px | Max content width 1440px centered. Side padding `{spacing.section}`. Hero imagery expands; product grid gutters widen; no additional layout change. |

### Touch Targets
- All buttons, inputs, pills, and nav links hold a minimum 44×44px touch target on mobile
- Product card entire surface is tappable on mobile; the explicit CTA button is not the only tap zone
- Sticky ATC button runs full-width on mobile for maximum thumb reach
- Category pills expand to full-row tap targets in mobile list views

### Collapsing Strategy
- Nav mega-menu becomes a full-height drawer with nested category accordions on mobile
- Footer link columns collapse into tap-to-expand accordion sections
- Spec row table scrolls horizontally on narrow viewports before reflowing to a single-column label/value list
- Search bar collapses to an icon button in the nav on mobile; tap expands to a full-screen input overlay
- Hero subhead text hides on viewports narrower than 375px to keep headline and CTA above the fold

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected in extracted stacks — Arial and Helvetica Neue inferred as primary; Vornado may load a proprietary or licensed web font via Shopify theme JavaScript that the static extraction did not capture
- Meta theme-color not set; system chrome defaults apply on mobile browsers, no brand red in the OS chrome bar
- Exact button padding, input heights, and grid column/gutter widths are estimated from category conventions — not extracted from computed CSS
- The purple and pink tones (#c64cf4, #bb32ed, #ef2d8e, #d4c3e1) appear in the extracted palette but could not be confirmed as structural system colors vs. one-time promotional widgets or third-party injected content
- Shadow values, elevation scale, and focus-ring offset/color specifications were not extractable from the static scrape
- Animation and transition timing (hover durations, mega-menu slide behavior, sticky ATC entrance) is unspecified
- Icon style — stroke weight, fill vs. outline treatment, and whether icons are a licensed library or custom-drawn — was not identified in the extraction
