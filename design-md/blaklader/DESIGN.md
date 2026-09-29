---
version: alpha
name: "Blaklader"
source_url: "https://blaklader.com"
captured_at: "2026-09-28T09:38:23.718641+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Blåkläder's storefront pairs a stark black-and-white industrial base with a
  single high-visibility brand yellow (#ffe000, exposed as --color-yellow and
  used on hotspot hover states) and a secondary review-widget yellow
  (#fee101, the judge.me --jdgm-primary-color). Dark near-black navy tones
  (#0d1523, #060a11, #111c36) appear repeatedly and are inferred here as the
  primary text/ink and dark-section background color, consistent with a
  workwear brand's utilitarian, high-contrast aesthetic. Neutral grays
  (#f5f5f5, #dddddd, #666666, #999999) are inferred as soft surfaces,
  hairlines, and muted text, since no role labels are present in the raw
  CSS. Typography draws on the observed "Akkurat Pro" family (paired with
  Arial/Helvetica fallbacks) for primary UI text, and "Stratum1" for the
  uppercase, tightly tracked labels seen in review widgets and product-title
  styling (letter-spacing ±0.28px, 700 weight, 14px, uppercase — directly
  observed in the hotspot dialog rules). The judge.me border-radius token is
  set to 0, suggesting a squared-off, no-radius visual language, which this
  interpretation treats as the default corner style for primary CTAs while
  reserving small radii for softer secondary elements. All measurements
  beyond the cited CSS are proposed, not measured.

colors:
  primary: "#ffe000"
  accent: "#fee101"
  ink: "#0d1523"
  canvas: "#ffffff"
  body: "#111111"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#000000"
  danger: "#cc0000"
  overlay: "#00000066"
  border-strong: "#999999"
typography:
  display-xl: {fontFamily: "Akkurat Pro, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Akkurat Pro, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "Akkurat Pro, Arial, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.2px}
  body-md: {fontFamily: "Nunito Sans, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Stratum1, sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.28px}
  button-md: {fontFamily: "Akkurat Pro, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.28px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.button-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    overlay: "{colors.overlay}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-hotspot:
    triggerBackground: "{colors.overlay}"
    triggerBorderHover: "{colors.primary}"
    dialogBackground: "{colors.surface-card}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.button-md}"
    rounded: "{rounded.none}"

## Components

**button-primary** uses the observed brand yellow (#ffe000) as a solid fill with dark text, matching the --color-yellow token used for hover states on product hotspots; the squared corner follows the judge.me `--jdgm-border-radius: 0` convention observed sitewide.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Find Store", "Track order"), using ink-colored text and border on a white ground, since no distinct secondary-button CSS was supplied.

**text-input** is inferred from generic hairline/gray tones (#dddddd, #f5f5f5) for form fields such as search or account login; no dedicated input CSS was present in the evidence.

**nav-bar** reflects the header/utility bar implied by the extensive mega-menu text content (All Workwear, Safety Footwear, Work Pants, Shop By, Discover) with a white background and hairline bottom border; exact height/collapse behavior is not observed.

**product-card** is proposed for PLP/PDP grid tiles, referencing the `--depict-grid-columns-desktop: 4` / `--depict-grid-columns-mobile: 2` tokens found in the CSS, which confirm a grid-based product listing exists, though card padding/border are inferred.

**hero** uses the dark ink background with a yellow-accented overlay, matching the hotspot-hover treatment (`rgba(0,0,0,0.25)` scrim plus yellow border) observed on homepage product hotspots; large display type is proposed for hero headlines.

**footer** is inferred as a dark-ink section given the repeated near-black tokens (#0d1523, #060a11, #111c36) in the palette, commonly used for footer/utility backgrounds in this type of layout; not directly confirmed by supplied selectors.

**badge** models the "Free shipping" / "Lifetime guarantee" ribbon text seen in the page copy, using the brand yellow fill and uppercase caption type consistent with the Stratum1 uppercase styling observed in review widgets.

**search** is a proposed light-surface search field for the header search icon referenced in navigation text; no direct search-input CSS was supplied.

**product-hotspot** is directly evidenced: `.hotspot-module` CSS defines a trigger button, hover border-color of `#ffe000`, a semi-transparent black background on hover, and a dialog with bold uppercase 14px title/price typography with ±0.28px letter-spacing — used here as the category-appropriate interactive component for shoppable lifestyle imagery.

## Responsive Behavior

*Recommendation only — not measured from live site rendering.*

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <640px | Single-column nav collapses to hamburger menu; `--depict-grid-columns-mobile: 2` confirms a 2-column product grid. |
| Tablet | 640–1024px | Hero height steps up per observed `--height-*` custom properties (17.5rem/21.25rem/25rem at the `@media` breakpoint shown in evidence). |
| Desktop | >1024px | `--depict-grid-columns-desktop: 4` confirms a 4-column product grid; full mega-menu navigation assumed visible. |

Touch targets should be at least 44×44px for hotspot triggers and nav items. Mega-menu items should collapse into accordions on mobile. None of this collapse/interaction behavior was directly observed; it is proposed based on standard responsive patterns and the grid-column tokens present in the CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, open/closed menu, cart drawer) were directly observed beyond the explicit `.hotspot-module` hover rule. Semantic color roles (ink, body, muted, hairline, surface-soft/card) are inferred from generic hex values without confirmed usage context, since the supplied palette is not annotated by role. Font-family assignments to specific text roles (display vs. body vs. caption) are inferred from partial evidence (e.g., Stratum1 tied to a judge.me review selector, "font-primary" var used in hotspot title/price without a resolved value) and may not match actual site typography. All pixel sizes for typography, spacing, and rounding beyond the two explicitly cited values (14px/700/±0.28px letter-spacing, border-radius: 0) are proposed defaults, not measurements. Mobile layout, breakpoint pixel values (beyond the one partial `@media` rule shown), and touch-target sizing are recommendations, not observed behavior. Licensing and availability of "Akkurat Pro" and "Stratum1" as web fonts were not verified and should be confirmed before implementation.
