---
version: alpha
name: "Arc'teryx"
source_url: "https://arcteryx.com"
captured_at: "2026-09-29T04:20:02.915736+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation reflects Arc'teryx's technical, minimal outdoor-brand identity as evidenced
  in the supplied CSS. The observed palette is dominated by near-neutral tones: true black
  (#000000), off-black (#1a1a1a), white (#ffffff), and a range of greys (#333333, #666666,
  #767676, #b2b2b2, #cccccc, #f5f5f5, #fafafa) used for text, hairlines, and surface layering.
  A small set of accent hues appear in the source (#990000, #227733, #5b9dd9) and are inferred
  here as status/alert, success, and informational colors respectively, not confirmed brand
  accents. Typography is built on two observed families: "Elan ITC Pro Updated" (assigned via
  CSS variable to h1/h4, serving display/headline roles) and "Helvetica Now Display" / generic
  Helvetica (assigned to body text via --font-helvetica). "urw-din-condensed" also appears in the
  font stack and is applied here, as inferred, to compact UI labels such as buttons and badges,
  consistent with its condensed proportions. Layout spacing tokens (--space-purple/pink/red at
  3rem/6rem/10rem) suggest a generous, section-based rhythm, which this spec generalizes into a
  broader spacing scale. Corner radii, precise component states, and responsive breakpoints were
  not present in the evidence and are proposed defaults suited to a technical apparel/equipment
  retailer.

colors:
  primary: "#000000"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#cccccc"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  border-subtle: "#e9e9e9"
  disabled: "#b2b2b2"
  overlay: "#000000cc"
  accent-alert: "#990000"
  accent-success: "#227733"
  accent-info: "#5b9dd9"
typography:
  display-xl: {fontFamily: "Elan ITC Pro Updated, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Elan ITC Pro Updated, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Elan ITC Pro Updated, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Helvetica Now Display, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Now Display, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "urw-din-condensed, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    minHeight: "44px"
    hairline: "{colors.border-subtle}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.overlay}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    hairline: "{colors.disabled}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  category-nav-flyout:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.border-subtle}"
    padding: "{spacing.lg} {spacing.xl}"

## Components

**button-primary** — Solid black call-to-action (e.g. "Shop women's", "Trade in now") using the condensed UI typeface inferred for buttons; on-primary white text ensures contrast against `{colors.primary}`.

**button-secondary** — Outlined variant on white canvas for lower-emphasis actions ("Find a store"); shares button-primary's condensed typography but inverts fill/border for visual hierarchy.

**text-input** — Generic form/search field styling using body typography and a light hairline border; states such as focus/error are proposed and not confirmed in the evidence.

**nav-bar** — Top navigation with a 44px minimum touch target, matching the `min-height:44px` observed on link/button rules in the extracted CSS; uses small body typography for menu items (Women, Men, Footwear, Equipment, Veilance).

**product-card** — Grid tile for packs/apparel listings; darker ink text on the soft off-white surface card color, with a distinct title typeface for product names and body typography for price, reflecting a catalog-heavy site structure (Day Packs, Multi-day, Travel & Commute).

**hero** — Full-width promotional banner (e.g. "Meet the Sperro SV") using the display typeface on a dark ink background with an overlay scrim, proposed for legibility over imagery; not a measured layout.

**footer** — Full black footer band with white text and inverse hairlines, consistent with the black background rule used elsewhere in the CSS (`--colour-white` text on dark containers).

**badge** — Small pill label for promotional flags (e.g. "New", "Sale", trade-in credit callouts), using the alert red accent color and caption typography; state and placement are proposed.

**search** — Lightweight search affordance on a soft grey surface, distinct from primary form fields, sized for header placement.

**category-nav-flyout** — Mega-menu panel structure inferred from the extensive nested navigation text (Clothing, Activities, Footwear, Learn more); uses canvas background and body-sm typography, generous padding to accommodate multi-column link lists.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | 0–599px | Single-column nav collapses to drawer; hero stacks text over image; product grid 2-up |
| tablet | 600–1023px | Product grid 3-up; nav flyouts may remain collapsed behind menu icon |
| desktop | 1024–1439px | Full mega-menu flyouts; product grid 4-up |
| wide | 1440px+ | Increased horizontal padding using `{spacing.xxl}`/`{spacing.section}` |

All interactive controls should maintain a minimum 44px touch target, consistent with the one observed `min-height:44px` rule. Mega-menus are assumed to collapse into an accordion or drawer pattern below desktop widths; this has not been observed and is a UX recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence was extracted from static CSS/text only; no rendered layout, interaction states (hover, focus, active, error), or JavaScript-driven behavior was observed.
- Color-to-role mapping (e.g. which grey is a "hairline" vs. "muted" text) is inferred from typical usage patterns, not confirmed via rendered screenshots.
- Accent colors (#990000, #227733, #5b9dd9) appear in the palette but their actual UI usage (alerts, success states, links) is inferred, not confirmed.
- Font availability, licensing, and exact weight/style variants for "Elan ITC Pro Updated" and "urw-din-condensed" were not verified; only family names as they appear in source CSS variables are used.
- All font sizes, line-heights, letter-spacing, corner radii, and spacing scale values beyond the two literal `:root` spacing variables (3rem/6rem/10rem) are proposed defaults, not measured.
- Responsive breakpoints and mobile/tablet layout behavior are recommendations only; no viewport-specific CSS was supplied in evidence.
- Component definitions (nav-bar, hero, product-card, etc.) are structurally inferred from page text/navigation content, not from confirmed DOM/CSS class observations of those exact components.
