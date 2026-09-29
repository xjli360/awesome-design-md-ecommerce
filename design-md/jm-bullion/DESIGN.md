---
version: alpha
name: "JM Bullion"
source_url: "https://www.jmbullion.com"
captured_at: "2026-09-28T04:13:21.166643+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  JM Bullion's observed CSS shows a utilitarian e-commerce shell built on Open Sans (with Arial and sans-serif fallbacks) at a compact 15px/18px body rhythm, layered over a white canvas. The confirmed brand blue (#125ea7) and a darker navy (#14253b, seen on the cart icon) anchor the primary/ink roles, while a family of mid-grays (#666666, #858585, #cccccc) supplies body text, muted copy, and hairlines. A cluster of warm gold tones (#edbb56, #deb053, #fadb99) and the cart-border gold (#ffca5e) is inferred as a bullion-appropriate accent family, since gold/silver retail commonly signals its product category through warm metallic color even though no explicit "brand gold" swatch was labeled in the source. A secondary blue (#428bca) appears in carousel-dot active states and is treated as a highlight accent. Red (#c01313, #d0011b) and green (#439439) values are inferred as alert/count and price-movement indicators respectively, consistent with a precious-metals storefront that displays live spot-price deltas. Rounded corners are small and functional (pill badges, 4-6px inputs/buttons) rather than decorative, suggesting a dense, transactional interface prioritizing legibility and trust signals over expressive styling.

colors:
  primary: "#125ea7"
  ink: "#14253b"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#858585"
  hairline: "#cccccc"
  surface-soft: "#f5faff"
  surface-card: "#eef0f2"
  on-primary: "#ffffff"
  accent-gold: "#edbb56"
  accent-gold-deep: "#deb053"
  accent-gold-pale: "#fadb99"
  highlight-blue: "#428bca"
  alert: "#c01313"
  success: "#439439"
  danger: "#d0011b"
  border-strong: "#b7b7b7"
typography:
  display-xl: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 40px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.5px}
  display-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 28px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 18px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 11px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.2px}
  button-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
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
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.base}"
    height: "35px"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-md}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.none} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-md}"
    metaTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
    accentColor: "{colors.highlight-blue}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    mutedTextColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.xs}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: "35px"
    width: "375px"
  spot-price-ticker:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.accent-gold-deep}"
    positiveColor: "{colors.success}"
    negativeColor: "{colors.danger}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"

## Components
**button-primary** uses the confirmed brand blue as a solid fill with white text, matching the weight-600 Open Sans styling seen on cart and utility links; hover/active states are not observed and are proposed as a slight darkening toward `{colors.ink}`.

**button-secondary** is a white-fill, bordered variant inferred for lower-emphasis actions (e.g., "view details"), reusing the border-gray from the chart-button evidence (`border-color:rgb(155 155 155)`), approximated here with `{colors.border-strong}`.

**text-input** reflects the observed utility-bar search field exactly: 35px height, small radius, left-padded text, white background, and a light hairline border; focus-ring styling is not observed and is proposed as a subtle primary-colored outline.

**nav-bar** is inferred from the toolbar/utility-bar rules showing a solid colored bar with white capitalized link text at 35px line-height; the fixed/sticky header state (`.header.fixed`) is confirmed in CSS but its scroll-trigger behavior was not visually observed.

**product-card** is a proposed pattern appropriate to a bullion catalog, using the light neutral surface-card background and hairline border for separation, with bold pricing typography since price is the primary decision driver in this category.

**hero** is proposed as a dark, full-bleed band (using `{colors.ink}`) to host large display type and a carousel, consistent with the `.slick-dots`/`.first-slide` evidence indicating a slider-driven top-of-page banner; exact hero copy and imagery were not observed.

**footer** is inferred as a dark, information-dense block (site links, trust badges) mirroring the header's dark/blue palette for brand consistency; no footer-specific selectors were present in the supplied evidence.

**badge** models the confirmed cart-count pill: red fill, white bold small text, fully rounded, matching `.items-in-cart` styling exactly as observed.

**search** duplicates the text-input treatment but is called out separately because the evidence isolates it as a distinct utility-bar element with a fixed pixel width (375px), suggesting a desktop-only inline search affordance.

**spot-price-ticker** is a category-specific, proposed component for live gold/silver spot pricing, inferred from the `#charts .chart-block` button evidence (bordered, rounded, bold, colored text) and extended with success/danger colors to indicate price direction, a common bullion-site convention not directly confirmed in the supplied CSS.

## Responsive Behavior
This is a proposed responsive structure, not a measured observation of the live site:

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | 0–639px     | Single-column stacking; nav collapses to a hamburger/menu icon; search hidden behind an icon toggle |
| tablet    | 640–1023px  | Two-column product grids; utility bar search may remain hidden or condense |
| desktop   | 1024–1279px | Full utility bar with visible 375px search field, as observed in CSS |
| wide      | 1280px+     | Fixed/sticky header (`.header.fixed`) engages per observed CSS; max-width containers center content |

Touch targets should be at least 44×44px on mobile regardless of the 35px desktop input height observed. Header collapse, hamburger behavior, and any mobile drawer navigation are proposed conventions only; no mobile DOM or breakpoint values were present in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from a static CSS/color/font extraction only; no rendered page, DOM structure, or JavaScript-driven interaction (carousel timing, cart drawer, sticky-header trigger point) was observed. Semantic role assignments (e.g., which grays are "muted" vs. "hairline," which golds are "accent" vs. purely decorative image assets) are inferred from naming context and typical bullion-retail conventions, not confirmed via visual inspection. All `display-*`, `title-md`, and `body-sm` sizes are proposed extrapolations since only 11px, 15px, and 22px sizes appeared directly in the supplied rules. The `font-family:bold` value found on `.etabs .tab a` appears to be a CSS artifact rather than an intentional typeface and was excluded from the typography tokens. Font Awesome 5 and Skeleticons were identified as icon fonts, not text typefaces, and are not included in the typography scale. Licensing and hosting/self-serving status of Open Sans were not verified. Mobile layout, hover/focus states, and breakpoint pixel values are proposed design recommendations, not measured behavior.
