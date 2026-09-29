---
version: alpha
name: "Antigravity Batteries"
source_url: "https://antigravitybatteries.com"
captured_at: "2026-09-28T09:43:37.219332+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Antigravity Batteries sells lithium motorsports batteries, Micro-Start jump
  power supplies, Super-Chargers, and lithium deep-cycle/solar energy-storage
  products through a WordPress/WooCommerce storefront. The supplied CSS is
  dominated by WordPress core and Gutenberg block-editor defaults rather than
  bespoke brand tokens: neutral grays (#32373c, #313131, #6d6d6d, #eeeeee,
  #dddddd, #ffffff) sit alongside the standard Gutenberg swatch set (blues,
  greens, reds, oranges) used for block-color utility classes. No custom
  webfont was found in the evidence; the only text stack present is the
  system-ui font list (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto,
  Helvetica Neue, sans-serif), which this interpretation adopts as the site
  typeface for both headings and body copy. #32373c is directly observed as
  the WooCommerce/Gutenberg button background and is promoted here to the
  primary action color, paired with #ffffff as on-primary text and canvas.
  Fully-rounded (9999px) buttons and 700-weight, 1.2-line-height product
  titles are directly observed in the CSS. Roles such as link/accent
  (#007cba), success, danger, and warning states are inferred from generic
  editor-preset swatches rather than confirmed live brand usage, since this
  hex only appears as a WordPress admin theme-color variable in the evidence.
  Spacing scale, card treatments, and responsive breakpoints below are
  proposed e-commerce conventions, not measured layout.

colors:
  primary: "#32373c"
  ink: "#313131"
  canvas: "#ffffff"
  body: "#6d6d6d"
  muted: "#888888"
  hairline: "#dddddd"
  surface-soft: "#eeeeee"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  link: "#007cba"
  link-hover: "#005a87"
  success: "#46b450"
  danger: "#dc3545"
  warning: "#fcb900"
  highlight: "#ff6900"
typography:
  display-xl: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: 42px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: 18px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.base}"
  battery-finder-widget:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** is the dark charcoal (#32373c), fully-rounded call-to-action used for "Add to Cart," "Learn More," and "Battery Finder" actions; this background/border-radius pairing is directly observed in the WooCommerce/Gutenberg button CSS.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Read More," "Select Options") sharing the same rounded-full shape and font but with a transparent fill; its bordered state is inferred, not measured.

**text-input** covers search fields, login, and finder-tool inputs. Border color and padding are proposed since no explicit input CSS was supplied; the hairline gray keeps inputs visually consistent with the neutral palette.

**nav-bar** represents the top utility/search/cart row and primary product-category menu (Starter Batteries, Micro-Starts, Super-Chargers, Energy Storage). Layout and sticky behavior are proposed; only the surrounding neutral tones are grounded in evidence.

**product-card** models catalog tiles such as the DC-125/DC-200H/DC-300H listings and featured products, using the 700-weight/1.2-line-height title rule observed in the WooCommerce grid CSS, with a soft off-white card surface proposed for separation from the page background.

**hero** is the dark, full-bleed banner area implied by homepage copy ("HI-POWER LITHIUM-ION," "MOTORSPORTS BATTERIES"), using display-xl type sized from the observed 42px "huge" preset; exact hero layout is not confirmed.

**footer** groups the multi-column Shop/Support/Info/Partner links and social icons noted in the page text, set on the dark ink background with the light link/blue accent for interactive text; column structure is proposed.

**badge** is a proposed small pill for "New," "Sale," or "Specials" labeling seen in navigation copy, using the orange highlight swatch from the supplied Gutenberg palette since no dedicated badge CSS was present.

**search** models the header search box referenced in page text ("Search for: Search"); styling is proposed from the neutral surface/hairline pairing.

**battery-finder-widget** is a category-specific component for the site's "Battery Finder" tool (find a replacement battery by vehicle), using primary-color accents on a soft surface to visually anchor this conversion-critical utility; interaction states are proposed.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| mobile | <600px | Single-column product grid, collapsed hamburger nav, stacked footer columns |
| tablet | 600–959px | 2-column product grid, condensed nav labels |
| desktop | 960–1279px | 3–4 column product grid, full nav bar |
| wide | ≥1280px | 4+ column grid, max-width content container |

Touch targets for buttons and nav items should be at least 44×44px. Primary nav is expected to collapse into a hamburger/off-canvas menu below the tablet breakpoint; the search and account/cart icons likely persist in a condensed header bar. None of this has been observed in live rendering—only inferred from standard WooCommerce theme patterns.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, computed styles, hover/focus states, or JavaScript-driven interactions were observed.
- The palette is dominated by WordPress/Gutenberg default swatches (e.g., #007cba as `--wp-admin-theme-color`), so link/accent, success, danger, and warning role assignments are inferred, not confirmed as intentional brand colors.
- No custom or licensed brand font was found; the system-ui stack is used as a best-effort typographic match, and its long-term availability/licensing is a platform default, not brand-specific.
- All spacing values, card/hero/footer paddings, and the responsive breakpoint table are proposed conventions for a batteries/electrical e-commerce catalog, not measured from the site.
- Component existence (battery finder, badges, nav collapse) is based on page text/menu labels, not on confirmed DOM structure or visual screenshots.
