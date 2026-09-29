---
version: alpha
name: "Bob's Watches"
source_url: "https://www.bobswatches.com"
captured_at: "2026-09-28T04:14:15.320588+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Bob's Watches' available CSS surfaces a utilitarian Bootstrap-based system
  layered with a small set of brand-specific tokens. The clearest observed
  brand marks are a mid-tone blue (#0058ab) used for search-result links and
  an off-black (#333333) applied to input borders and consent-banner text,
  alongside pure black/white for base ink and canvas. Bootstrap's default
  state palette (#dc3545 danger, #198754 success, #ffc107 warning) is present
  in the stylesheet but its application to specific UI moments is not
  confirmed here. Font evidence lists proxima_nova_bold/semibold alongside
  Inter, Roboto, and system-UI fallbacks for interface text, plus Frank Ruhl
  Libre and Utopia Std as serif candidates; no rule ties these serifs to a
  selector, so their use for display headlines below is an inferred editorial
  choice suited to a pre-owned luxury-watch retailer. This interpretation
  treats #0058ab as primary interactive color, #333333/#000000 as ink,
  #f7f7f7/#f3f3f3 as soft surfaces (seen on the search-close button and
  consent hover state), and #c4c4c4/#dee2e6 as hairlines. Two conflicting
  header-search radius rules (16px and 40px) inform a pill-shaped search
  pattern. Sizes absent from the CSS are proposed defaults.

colors:
  primary: "#0058ab"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#c4c4c4"
  surface-soft: "#f7f7f7"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  accent: "#d42b2a"
  success: "#198754"
  warning: "#ffc107"
  danger: "#dc3545"
  border-subtle: "#dee2e6"
  dark: "#212529"
typography:
  display-xl: {fontFamily: "Frank Ruhl Libre, Georgia, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "proxima_nova_bold, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "proxima_nova_semibold, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "proxima_nova_semibold, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 20px, letterSpacing: 0.2px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.display-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  authentication-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.success}"
    borderColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** uses `{colors.primary}` as its fill, echoing the observed link color (#0058ab) on search results. It is proposed as the main "Sell Your Watch" / "Buy Now" action; hover and disabled states are not observed and remain proposed.

**button-secondary** is an outline treatment on canvas with a hairline border, intended for lower-priority actions (e.g., "Learn More," "Compare"). Its border color reuses `{colors.hairline}`, matching the observed #c4c4c4 input border.

**text-input** mirrors the header search field evidence directly: a white background, 1px hairline border, and a rounded shape. Two conflicting radius values were observed (16px and 40px); this spec standardizes on `{rounded.full}` as a pill-input pattern, which is a design decision rather than a literal measurement.

**nav-bar** is proposed as a white bar with dark body text and a bottom hairline, consistent with the light canvas and #333 border tones seen in header rules. Sticky behavior and dropdown states are not confirmed by the CSS and are proposed only.

**product-card** uses the lighter of the two near-white surfaces (#f3f3f3, observed as a hover background elsewhere) as a card surface to separate watch listings from the page canvas, with a hairline border and medium rounding. Price and title typography reuse the display/title tokens; this pairing is inferred for a resale-catalog layout, not observed directly.

**hero** is proposed as a dark, full-bleed banner using `{colors.ink}` with reversed canvas-colored display type, appropriate to a premium watch storefront; no hero markup or imagery was present in the supplied evidence.

**footer** adopts the Bootstrap-adjacent dark tone (#212529) with reversed body-sm text, consistent with typical dark-footer commerce patterns; actual footer content and column structure are not observed.

**badge** is proposed for sale/condition labels (e.g., "Certified," "Sold") using the palette's red (#d42b2a) as an attention accent; this color's real-world usage on the live site is unconfirmed, so the role is inferred.

**search** reflects the two header search-input rules most closely: white background, hairline border, pill rounding, and a trailing icon-button pattern (`.searchButton`/`.closeButton` are transparent, borderless, flex-aligned per the CSS).

**authentication-badge** is a category-specific addition for a watch-collector marketplace, signaling verified/authenticated timepieces using the success green (#198754) on a soft surface; this component is entirely proposed to fit domain conventions and is not present in the supplied CSS.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| xs        | < 480px     | Single-column product cards, collapsed nav into a menu icon, full-width pill search |
| sm        | 480–767px   | Two-column product grid, search remains full-width in header |
| md        | 768–991px   | Three-column product grid, inline nav links begin to appear |
| lg        | 992–1199px  | Four-column grid, full horizontal nav, search fixed-width (min 216px per observed rule) |
| xl        | ≥ 1200px    | Max-width content container, generous section padding (`{spacing.section}`) |

Touch targets should be at least 44px, matching the observed `.closeSearchButton` dimensions (44px × 44px). Primary and secondary buttons should maintain a minimum 44px height on touch devices. Nav collapse into a hamburger/menu pattern below `md` is a proposed convention, not observed in the supplied markup.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS only; no rendered layout, interaction states (hover/focus/active beyond the consent banner), or JavaScript-driven behavior (e.g., search autocomplete UX) were observed.
- Two conflicting header-search border-radius values (16px vs. 40px) exist in the source; this spec resolves them to a single pill token, which is a design decision, not a confirmed live value.
- Role assignments for Bootstrap default state colors (#0d6efd, #dc3545, #198754, #ffc107) are inferred from common framework convention, not from selectors tying them to Bob's Watches-specific components.
- The accent red (#d42b2a) and authentication-badge green are proposed/inferred mappings for a watch-resale domain and are not verified against live UI.
- Font families proxima_nova_bold/semibold, Frank Ruhl Libre, and Utopia Std appear in the evidence's font-family list without a confirming selector; their assignment to display vs. body roles is inferred, and licensing/availability of any custom or paid fonts has not been verified.
- All numeric type sizes, spacing scale values, and breakpoints beyond the few literal pixel values in the CSS (16px input font-size, 44px button height, 20px line-height) are proposed defaults for internal consistency, not measurements of the live site.
- Mobile navigation, hero content, and footer structure were not present in the supplied CSS and are proposed based on common commerce patterns only.
