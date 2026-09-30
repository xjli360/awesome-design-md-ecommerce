---
version: alpha
name: "Pilot Pen"
source_url: "https://pilotpen.us"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Three shades of the same navy — #054a7a anchoring the deep end, #0f72b7 as the working primary, #0b598f threading between them — compress the entire brand voltage into a single blue family that reads like the color of fresh ink drying on cotton-bond paper. The palette is nearly monochromatic: one gray (#eeeeee) provides the only departure from the blue-and-white axis, leaving the white canvas and the ink-blue spectrum to carry every product shot, CTA, and editorial block. This restraint is purposeful. A writing instrument brand selling precision and longevity doesn't reach for chromatic noise; the blue does everything.

  Without a confirmed text typeface in the extracted font manifest — only Font Awesome 5 Free and Brands appear, both icon fonts — the typography system falls back to a neutral system sans-serif. The visual hierarchy almost certainly leans on weight shifts and modest uppercase tracking rather than a proprietary variable font. Button labels and navigation items likely run at 14–16px medium-weight; editorial hierarchy is earned through size jumps rather than expressive faces.

  Interaction surfaces follow the corporate-consumer hybrid pattern common to Japanese stationery brands operating a US retail arm: nav bars carry product-line mega-dropdowns rather than lifestyle photography, product cards are dense with model numbers and ink-type metadata, and CTAs drive directly to SKUs rather than to editorial content. The hero likely pairs a product photograph against the primary blue fill with a white headline — high contrast, no gradient softening, no overlay scrim. Corner radii are minimal throughout, sitting around `{rounded.xs}` (4px), consistent with the precision-instrument aesthetic rather than the soft-round consumer goods language of competitors. The `{rounded.full}` pill shape is reserved, if used at all, for tag or badge contexts, not for primary CTAs.

  The icon system — Font Awesome 5 Free for utility glyphs (cart, search, social links) — handles everything confirmable. Any proprietary nib or ink-type iconography lives in assets not captured by the extraction. Footer real estate allocates columns to product families, customer service, and corporate links, set against the deep navy (#054a7a) that bookends the palette at both ends of the page.

colors:
  primary: "#0f72b7"
  primary-dark: "#054a7a"
  primary-mid: "#0b598f"
  primary-disabled: "#7ab8db"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-light: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  product-sku:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px

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
  button-primary-hover:
    backgroundColor: "{colors.primary-mid}"
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
    border: "1px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-dark}"
    border: "1px solid {colors.primary-dark}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    shadow: "0 4px 16px rgba(0,0,0,0.10)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    imageRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    skuTypography: "{typography.product-sku}"
    padding: "{spacing.base}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    shadow: "0 2px 12px rgba(15,114,183,0.12)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    minHeight: 480px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid transparent"
    padding: "{spacing.sm} {spacing.base}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-bestseller:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    iconColor: "{colors.muted}"
  ink-swatch:
    width: 20px
    height: 20px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  ink-swatch-selected:
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    shadow: "0 0 0 3px {colors.primary-disabled}"
  feature-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    accentBorder: "3px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-caps}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    opacity: 0.8
    hoverOpacity: 1

## Components

### Buttons

**`button-primary`** — The workhorse CTA fills with primary blue (#0f72b7) and white text at `{typography.button-md}` weight, sitting on `{rounded.xs}` (4px) corners — a minimal radius that signals precision over approachability. Hover deepens to the mid-blue (#0b598f); disabled washes to `{colors.primary-disabled}` at roughly 50% luminance saturation. Height locks at 44px.

**`button-secondary`** — White canvas fill with a 1px primary-blue border and primary-blue text; used where the full blue fill would compete with product photography or editorial imagery. On hover the background shifts to `{colors.surface-soft}` and the border deepens to `{colors.primary-dark}`, preserving the monochromatic vocabulary throughout the state sequence.

**`button-ghost`** — Text-only with underline, no background or border, in `{colors.primary}`. Reserved for tertiary actions ("view all," "learn more") that need to be present but not compete with adjacent filled CTAs.

### Text Input

**`text-input`** — 44px tall, hairline border (#dddddd) that shifts to `{colors.primary}` on focus. Interior padding runs 10px vertical and 14px horizontal. The background stays white canvas; the only dynamic element on interaction is the border color — no shadow bloom, no scale shift.

### Navigation

**`nav-bar`** — White bar at 64px with a hairline bottom border. The Pilot wordmark renders in `{colors.primary}`. Mega-dropdown panels (`nav-dropdown`) open on hover with product-family column grids, a 16px drop shadow, and `{rounded.xs}` container corners. Utility icons (search, cart, account) populate the right rail using Font Awesome 5 Free glyphs colored in `{colors.ink}`.

**`category-tab`** — Flat tab strip for product-family navigation within category pages. Inactive tabs carry `{colors.muted}` text and a transparent bottom border. Active tabs flip to `{colors.primary}` text with a 2px solid primary-blue underline. No background fill at any state — the transition is color-only, preserving visual flatness.

### Product Card

**`product-card`** — White background with 1px hairline border and `{rounded.xs}` corners; 1:1 image aspect ratio for consistency across cylindrical pen bodies. The title runs `{typography.title-sm}` and model/SKU metadata renders in `{typography.product-sku}` (11px, tracked at 0.5px). On hover the border shifts to `{colors.primary}` and a subtle blue-tinted shadow at 12% opacity lifts the card just enough to register selection without departing from the flat system.

### Hero Banner

**`hero-banner`** — Full-width block in `{colors.primary}` (#0f72b7) with the white headline at `{typography.display-xl}` (40px/700) and white subtitle at `{typography.body-md}`. Minimum height of 480px accommodates a right-anchored product photograph. The solid-color fill strategy keeps the hero from competing with the pen itself — the product is always the feature, the blue is the stage.

### Ink Swatches

**`ink-swatch`** — 20px circles with a 2px hairline border, the primary color-selection surface on product detail pages. The selected state (`ink-swatch-selected`) gains a 2px primary-blue border plus a 3px outer glow using `{colors.primary-disabled}` as the box-shadow color — three concentric rings that communicate selection without requiring a hover tooltip. Touch targets expand to 44px via transparent padding padding on mobile.

### Feature Callout

**`feature-callout`** — Soft gray block (`{colors.surface-soft}`) with a 3px solid left border in `{colors.primary}`, used for inline product feature highlights ("Erasable ink," "Retractable nib," "Waterproof formula"). Title uses `{typography.title-md}`, body copy uses `{typography.body-sm}`, `{rounded.sm}` corners soften the block without undermining the clinical tone.

### Badges

**`badge-new`** — All-caps label in primary blue fill with white text, `{rounded.xs}` corners, 3px/8px padding. Applied to newly launched SKUs. **`badge-bestseller`** — Identical geometry in `{colors.primary-dark}` (#054a7a), darker to signal established demand rather than novelty — both tokens occupying the same blue family, distinguished only by depth.

### Search Bar

**`search-bar`** — 40px compact input in `{colors.surface-soft}` with hairline border and a muted magnifier icon from Font Awesome 5 Free. Appears in the nav rail on desktop and expands full-width on mobile. Uses `{rounded.xs}` corners and `{typography.body-md}` for input text.

### Footer

**`footer`** — Deep navy (`{colors.primary-dark}`, #054a7a) base with white text. Column headings use `{typography.label-caps}` (11px, 700, uppercase, 0.8px tracked); links use `{typography.body-sm}` at 80% opacity, rising to full opacity on hover. Section padding `{spacing.xxl}` vertical and `{spacing.section}` horizontal gives the multi-column product-family link grid room to breathe without crowding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger icon + slide-in drawer; hero stacks headline above product image at full width; product grid becomes 2-up; category tab strip scrolls horizontally; ink swatches move below product image |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + cart/search icons with condensed primary links (no mega-dropdown); hero maintains side-by-side layout at reduced horizontal padding; feature callouts arrange 2×2 |
| Desktop | 1128–1440px | Full mega-dropdown nav; 3–4 column product grid; hero at full 480px minimum height with right-aligned photography; feature callouts in a single horizontal row |
| Wide | > 1440px | Content caps at 1440px centered on white canvas; hero blue background extends edge-to-edge while content remains centered within the grid |

### Touch Targets

- All interactive elements (buttons, tabs, ink swatches, nav items) meet 44×44px minimum touch target on mobile
- Ink swatches expand from 20px visual size to 44px touch target via transparent padding
- Footer links gain 32px minimum line height on touch devices to prevent mis-taps in dense link columns
- Search icon in mobile nav expands to a 44px tap zone before triggering the full-width search input

### Collapsing Strategy

- Mega-dropdown nav compresses to a two-level accordion drawer on mobile: top-level product families expand inline
- Category tab strip enables horizontal momentum scroll rather than wrapping to multiple rows
- Hero CTA buttons stack vertically (primary above secondary) on screens below 480px
- Product card grid steps 4-up → 3-up → 2-up → 1-up as viewport narrows; never drops to 1-up until below 480px
- Feature callout left-border accent is preserved at all breakpoints; the row layout collapses to vertical stacking on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No text typeface confirmed**: font manifest captured only Font Awesome 5 Free and Font Awesome 5 Brands (icon fonts); the actual display and body typeface is unknown — system-ui fallbacks used throughout all typography tokens
- **No meta theme-color set**: browser chrome accent is unspecified; primary blue (#0f72b7) assumed as the intended representative color
- **Sparse color extraction**: only four hex values captured — the full system likely includes error/success states, promotional pricing accents, and additional neutral tones not present in the extraction
- **No dark mode tokens**: insufficient data to confirm whether the site ships a dark theme variant
- **Custom iconography unknown**: Font Awesome covers utility glyphs but any proprietary nib-type, ink-color, or product-line icons (SVG sprite or custom font) were not captured
- **Animation and transition specs absent**: no easing functions, durations, or motion patterns extractable from static analysis
- **Promotional/sale color unconfirmed**: no red or orange accent detected; Pilot global sites sometimes use red for sale pricing — applicability to the US site cannot be confirmed
