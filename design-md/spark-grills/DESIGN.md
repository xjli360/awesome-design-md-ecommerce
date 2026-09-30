---
version: alpha
name: "Spark Grills"
source_url: "https://www.sparkgrills.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Charcoal inside a sealed, steel-shelled chamber with a brushless fan wired to a Bluetooth stack — Spark Grills converts the oldest cooking method into something you dial by degree from a phone. The site matches the product's logic: a dark carbon ground (`#111111`) holds the hero, while a single combustion orange (`#E8500A`) marks every interactive state, live temperature readout, and primary CTA. Nothing competes with it. Product photography shoots the grill from low angles under dramatic side-light, letting the lid geometry read as precision hardware rather than patio furniture.

  Type leans on a geometric sans weighted for drama in display positions (56px, 700) and dropped to clean 16px/400 for body copy — a range wide enough that a feature headline like "±5°F accuracy" reads as a spec claim rather than marketing padding. Letter-spacing tightens at large sizes (`-0.5px`) to close the visual gaps that open in dark-on-dark compositions. The color system avoids midtone warmth: no amber, no tan, no wood-brown despite the BBQ category. That restraint signals engineering confidence rather than barbecue kitsch.

  Corners are sharp to moderate — `{rounded.xs}` on badges and spec chips, `{rounded.sm}` on cards, inputs, and buttons; no pill shapes anywhere. Interactive affordances are dense: a sticky add-to-cart bar with a live temperature graphic, a feature carousel, a modal spec sheet. Section breaks lean on 64px gaps to breathe between dense product blocks on a dark canvas. Mobile collapses to single-column linear narrative with full-bleed photography and a bottom-docked CTA strip, keeping the orange button always in thumb reach.

colors:
  primary: "#E8500A"
  primary-active: "#C43D08"
  primary-disabled: "#F5B492"
  ink: "#1A1A1A"
  body: "#2C2C2C"
  muted: "#767676"
  hairline: "#E2E2E2"
  hairline-dark: "#2E2E2E"
  canvas: "#FFFFFF"
  surface-soft: "#F6F5F3"
  surface-card: "#FFFFFF"
  surface-dark: "#111111"
  surface-mid: "#1C1C1C"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  on-dark-muted: "#9A9A9A"
  temp-display: "#E8500A"

typography:
  display-xl:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  spec-label:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  logo-display:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: -0.2px

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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 52px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1.5px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 52px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.logo-display}"
    logoColor: "{colors.on-dark}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    descTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.on-dark-muted}"
    minHeight: 640px
    layout: split-left-text-right-image
    ctaGap: "{spacing.sm}"
  feature-strip:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.on-dark}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.on-dark-muted}"
    valueTypography: "{typography.display-sm}"
    valueColor: "{colors.temp-display}"
    itemGap: "{spacing.xxl}"
    padding: "{spacing.xl} {spacing.section}"
    borderTop: "1px solid {colors.hairline-dark}"
  spec-badge:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.on-dark}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  temp-readout:
    textColor: "{colors.temp-display}"
    typography: "{typography.display-xl}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.on-dark-muted}"
  sticky-cart-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    borderTop: "1px solid {colors.hairline-dark}"
    height: 72px
    ctaVariant: button-primary
  feature-card:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.on-dark-muted}"
    iconColor: "{colors.primary}"
    padding: "{spacing.xl}"
  section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    overlineTypography: "{typography.spec-label}"
    overlineColor: "{colors.primary}"
    overlineMarginBottom: "{spacing.sm}"
  app-callout:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.on-dark-muted}"
    rounded: "{rounded.md}"
    layout: left-text-right-mockup
    padding: "{spacing.xxl}"
  divider:
    color: "{colors.hairline}"
    height: 1px
  divider-dark:
    color: "{colors.hairline-dark}"
    height: 1px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark-muted}"
    linkColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    logoTypography: "{typography.logo-display}"
    logoColor: "{colors.on-dark}"
    borderTop: "1px solid {colors.hairline-dark}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Solid combustion orange (`#E8500A`) fill on a 52px tall target, 28px horizontal padding, `{rounded.sm}` corners. Used for "Add to Cart", "Buy Now", and top-of-funnel CTAs. Active state darkens to `#C43D08`; disabled state bleaches to `#F5B492` while keeping white label text. On the dark-canvas hero the orange button reads as the only warm element in the entire frame — no competing warm tones anywhere in the surrounding UI.

**`button-secondary`** — Transparent background with a 1.5px black stroke and `{rounded.sm}`. Pairs with `button-primary` in hero and product sections to offer a secondary path (e.g. "See full specs" beside "Add to Cart"). The `button-secondary-on-dark` variant swaps stroke and label to `{colors.on-dark}` for placement over `{colors.surface-dark}` or `{colors.surface-mid}` backgrounds.

**`button-ghost`** — Label-only in `{colors.primary}` orange, no background or border. Used for inline tertiary actions: "View all features", "Read the science", inline review prompts inside feature cards.

### Text Input

**`text-input`** — 48px tall, `{rounded.sm}`, 1px `{colors.hairline}` border at rest. Focus ring upgrades to 1.5px `{colors.primary}` orange — the only point in the light-canvas UI where the brand voltage enters a form element. Placeholder copy renders in `{colors.muted}`. Appears in email newsletter capture and any quote/order flow.

### Navigation

**`nav-bar`** — Fixed 64px dark bar (`{colors.surface-dark}`) with wordmark left-aligned in `{typography.logo-display}` and `{colors.on-dark}`. Primary links (Shop, Technology, Recipes, Support) in `{typography.nav-link}`. Right side carries a cart icon button sized to a 48×48px touch target. No mega-menu; the minimal nav keeps visual focus on the product photography below. A 1px `{colors.hairline-dark}` bottom border separates it from dark-background hero sections without visible seam.

### Product Card

**`product-card`** — White card with 1px `{colors.hairline}` border and `{rounded.sm}`. Product image at 4:3 aspect ratio, product name in `{typography.title-sm}`, price in `{typography.title-md}` beneath. A `{typography.body-sm}` line carries the one-line feature descriptor ("Smart Temperature Control"). Padding is `{spacing.base}` on all sides. No drop shadow — the hairline border alone provides card separation on the white canvas.

### Hero Section

**`hero-section`** — Full-width dark-canvas (`{colors.surface-dark}`) section, minimum 640px tall. Left column carries headline in `{typography.display-xl}` / `{colors.on-dark}`, a subhead paragraph in `{typography.body-md}` / `{colors.on-dark-muted}`, and a paired CTA row (`button-primary` beside `button-secondary-on-dark`). Right column is product photography — grill lit with warm side-light against a dark background, no lifestyle clutter. On mobile, columns collapse to image-above / text-and-CTAs-below with full-bleed photography extending edge to edge.

### Feature Strip

**`feature-strip`** — A full-width dark band (`{colors.surface-mid}`) running immediately below the hero. Contains 3–4 icon+stat pairs: the stat value renders in `{typography.display-sm}` / `{colors.temp-display}` orange, and its label in `{typography.spec-label}` / `{colors.on-dark-muted}`. Items are separated by `{spacing.xxl}` gaps. Representative stats: "±5°F", "24hr cook", "600°F max". A `{colors.hairline-dark}` top border defines the boundary with the hero above.

### Temperature Readout

**`temp-readout`** — A specialized display block used in the app-integration section and PDP. The live or example temperature value renders at `{typography.display-xl}` scale in `{colors.temp-display}` orange. A `{typography.spec-label}` overline in `{colors.on-dark-muted}` ("CURRENT TEMP") provides context. The component is the most direct visual translation of the product's core promise — fire precision — and deliberately mimics a digital instrument panel rather than a marketing graphic.

### Sticky Cart Bar

**`sticky-cart-bar`** — A 72px strip docked to the viewport bottom on PDP, appearing once the user scrolls past the main hero CTA. Left side shows product name in `{typography.title-sm}` and price in `{typography.title-md}`, both in `{colors.on-dark}`. Right side mounts a full-width `button-primary`. Background is `{colors.surface-dark}` with `{colors.hairline-dark}` top border. Mobile and tablet only; hidden on desktop where the hero CTA remains in viewport.

### Feature Card

**`feature-card`** — Dark tile (`{colors.surface-mid}`, `{rounded.sm}`) used in a 2- or 3-column grid on the technology page. Icon at top-left in `{colors.primary}` orange. Headline in `{typography.title-md}` / `{colors.on-dark}`. Body in `{typography.body-sm}` / `{colors.on-dark-muted}`. Padding is `{spacing.xl}` all sides. The uniform dark tile grid creates a dense, spec-sheet rhythm that signals the product's technical depth without requiring infographics.

### Section Heading

**`section-heading`** — Opens each content section outside the hero. An `{typography.spec-label}` overline in `{colors.primary}` orange (e.g. "THE TECHNOLOGY") precedes the main title in `{typography.display-md}`. On dark-canvas sections the title is `{colors.on-dark}`; on the white-canvas sections it is `{colors.ink}`. The uppercase overline `{spacing.sm}` above the headline creates a visual anchor that echoes the product's precision-instrument language across every section transition.

### App Callout

**`app-callout`** — Left-text / right-phone-mockup block in `{colors.surface-mid}`, `{rounded.md}`. Headline in `{typography.display-sm}` / `{colors.on-dark}`, body paragraph in `{typography.body-md}` / `{colors.on-dark-muted}`. App store badge buttons appear below the body. This section promotes Bluetooth connectivity and the temperature-monitoring companion app. The phone mockup renders the `temp-readout` component, tying the visual system back to the product's data-driven identity.

### Spec Badge

**`spec-badge`** — Small rectangular chip in `{colors.surface-mid}`, `{rounded.xs}`, `{typography.spec-label}` text in `{colors.on-dark}`. Used to surface claims inline on PDP: "CHARCOAL", "BLUETOOTH", "2-YEAR WARRANTY". The sharp `{rounded.xs}` corner distinguishes these from softer badge styles — they read as hardware labels, not marketing tags.

### Footer

**`footer`** — Full-width `{colors.surface-dark}` band with `{spacing.section}` top and bottom padding. Wordmark in `{typography.logo-display}` / `{colors.on-dark}` top-left. Three or four link columns (Shop, Support, Company, Legal) in `{typography.body-sm}` / `{colors.on-dark-muted}`, with hover state surfacing to `{colors.on-dark}`. Bottom strip carries copyright text and a social icon row. The dark footer creates a bookend with the dark hero — the entire light-canvas product content is sandwiched between two black surfaces.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single column throughout. Hero image moves above text, full-bleed edge-to-edge. Sticky cart bar docked to bottom. Feature strip converts to horizontal snap-scroll container. Nav collapses to hamburger; drawer slides from right. |
| Tablet | 744–1128px | Two-column hero retained. Feature strip wraps to 2×2 grid. Feature cards shift to 2-column grid. App callout stacks vertically (text above, mockup below). Sticky cart bar still visible. |
| Desktop | 1128–1440px | Full three-column feature card grid. Hero at full split layout. Feature strip displays all 4 stats inline in one row. Sticky cart bar hidden. |
| Wide | > 1440px | Max content width capped at ~1360px, centered. Hero image scales within its right column. No further horizontal padding expansion beyond the content cap. |

### Touch Targets

- All primary and secondary buttons are minimum 52px tall.
- `button-sm` and ghost buttons maintain a minimum 44px tap target via padding even if the visual height is smaller.
- Nav icon buttons (cart, hamburger) are 48×48px tap targets regardless of visible icon size.
- Sticky cart bar CTA maintains 52px height on all mobile breakpoints.
- Feature card tap areas cover the entire card surface, not just the headline.
- Spec badges are display-only; if made interactive, wrap to minimum 36px tap height.

### Collapsing Strategy

- Navigation collapses to hamburger icon at < 744px; full-height drawer slides from right over a dark scrim.
- Hero two-column splits to stacked (image → headline → body → CTAs) at < 744px.
- Feature strip converts from inline row to horizontal scroll container with snap points at < 744px; items do not wrap.
- Feature card grid: 3 columns → 2 columns → 1 column across Desktop → Tablet → Mobile.
- App callout drops the side-by-side split at < 744px; phone mockup renders below the text and badge buttons.
- Section headings retain full `{typography.display-md}` sizing through Tablet; at Mobile they scale down to `{typography.display-sm}` to prevent overflow.
- Sticky cart bar is present on Mobile and Tablet only; hidden at Desktop where the hero CTA anchor is always visible.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: The extraction returned zero color values. All palette entries in this file are estimated from brand name, product category, and aesthetic conventions. Every hex value must be verified against the live site at https://www.sparkgrills.com before production use.
- **No font families extracted**: The typeface stack shown (`Inter, -apple-system, ...`) is a plausible geometric-sans placeholder. The actual brand font — possibly a custom or licensed face — must be confirmed from the live site's CSS or design assets.
- **No meta theme-color**: Cannot corroborate the primary brand color via the HTML meta tag, which is a common secondary confirmation signal.
- **Platform unconfirmed**: Extraction indicates non-Shopify, but the actual e-commerce platform and its default component behaviors (cart drawer, variant selectors, reviews widget) are unknown.
- **Dark vs. light primary canvas**: Whether the home page leads with a dark or light canvas is unconfirmed; this design assumes dark-primary based on product category and brand name conventions for tech-forward grill brands.
- **Logo treatment**: Whether the brand mark is a wordmark, icon+wordmark, or standalone flame/spark icon is unconfirmed. `{typography.logo-display}` sizing is estimated.
- **App existence and design**: The presence and visual design of a companion mobile app section is inferred from the product's fan-control feature set, not confirmed from the live site.
- **Navigation link labels**: The specific nav items (Shop, Technology, Recipes, Support) are estimated from common DTC grill brand IA patterns, not extracted from the live page.
