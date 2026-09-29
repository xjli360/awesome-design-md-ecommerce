---
version: alpha
name: "Jovial"
source_url: "https://jovialfoods.com"
captured_at: "2026-09-28T09:27:57.280321+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Jovial Foods presents a warm, farm-rooted identity built on a single observed
  typeface, Poppins, used for both display and body text via the site's
  `--heading-font-stack` and `--main-font-stack` variables. Headings are bold,
  uppercase, and lightly tracked (0.025em), giving product and category titles
  a confident, packaging-label quality; body copy uses the same family at
  regular weight for continuity.

  The palette is inferred from multiple CSS custom-property "color schemes"
  rather than a single static stylesheet, so role assignments here are
  interpretive. A deep terracotta/rust (#5a1400) recurs as the dominant
  accent and text color across the primary scheme and is treated as the
  brand's signature color, evoking tomato sauce and toasted grain rather than
  a generic food-brand green. A forest green (#21632c) appears consistently
  as a secondary accent (organic/regenerative cues), and a warm off-white
  card tone (#f7f5f5) recurs as a content-surface background distinct from
  pure white. Grays (#676986, #272d45) are assumed to serve muted text and
  navigation roles based on typical usage patterns, not direct measurement.
  No breakpoints, interaction states, or mobile layouts were observed; all
  such details below are proposed conventions suited to a pasta/grains grocery
  storefront.

colors:
  primary: "#5a1400"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#272d45"
  muted: "#676986"
  hairline: "#e5e5e5"
  surface-soft: "#f9f8f4"
  surface-card: "#f7f5f5"
  on-primary: "#ffffff"
  accent-green: "#21632c"
  accent-green-bright: "#11930b"
  accent-teal: "#00caaa"
  accent-teal-soft: "#b2f9e9"
  accent-blue: "#1990c6"
  border-strong: "#9a9db1"
typography:
  display-xl: {fontFamily: "Poppins, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: 0.025em, textTransform: uppercase}
  display-md: {fontFamily: "Poppins, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0.025em, textTransform: uppercase}
  title-md: {fontFamily: "Poppins, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0.025em, textTransform: uppercase}
  body-md: {fontFamily: "Poppins, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "Poppins, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.01em}
  button-md: {fontFamily: "Poppins, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.025em, textTransform: uppercase}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    borderRadius: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-green-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  recipe-callout:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    accentColor: "{colors.accent-green}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** uses the rust brand color (#5a1400) as a solid fill with white text, matching the accent-1/accent-2 contrast pairing seen repeatedly in the scheme variables; intended for primary CTAs like "Shop Now" and "Add to Cart." Hover/focus states are proposed, not observed.

**button-secondary** is an outlined variant sharing the same rust color for border and text on a transparent background, for lower-emphasis actions (e.g., "Learn More") alongside a primary button.

**text-input** proposes a white field with a light hairline border (#e5e5e5) and dark ink text, sized for account, newsletter, and search-adjacent forms; no live input styling was captured in the evidence.

**nav-bar** assumes a white background with dark slate (#272d45) label text, reflecting the site's dense multi-level "Shop / About / Recipes / Resources" menu structure described in the text content; a bottom hairline separates it from page content.

**product-card** uses the warm off-white card surface (#f7f5f5, matching the scheme1 card token) with rust-colored title text, suited to grid listings of pasta, einkorn, and pantry items; price and name typography are distinguished by weight rather than color.

**hero** is proposed on the forest-green background (#21632c) with white type at display-xl size, appropriate for the "Regenerative Organic Certified" and seasonal promotional banners referenced in the page copy; actual hero background was not directly measured and may vary by campaign.

**footer** inherits the rust primary as a dark background with white text, consistent with scheme5's white-on-rust and rust-on-white reversible pairing found in the CSS variables.

**badge** renders small organic/certification callouts (e.g., "Organic," "Regenerative") as a pill using the bright green (#11930b) accent, distinct from the deeper brand green, based on its presence as a standalone palette value.

**search** proposes a soft warm-white input field (#f9f8f4) for the "Search our site" overlay mentioned in the page text; exact overlay styling was not observed.

**recipe-callout** is a category-appropriate component for surfacing einkorn/pasta recipe links (per the "Recipes / Videos / Einkorn Sourdough" menu items), pairing the card surface with a green accent rule to differentiate editorial content from product cards.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | < 640px     | Single-column stacks; nav collapses to hamburger + drawer |
| tablet    | 640–1024px  | 2-column product grids; sticky top announcement bar likely persists |
| desktop   | 1024–1820px | Full multi-column nav and 3–4 column product grids, capped by `--max-site-width: 1820px` |
| wide      | > 1820px    | Content centers within max-width container |

Touch targets are recommended at a minimum 44×44px for nav, cart, and add-to-cart controls. Primary navigation is expected to collapse into a slide-out or accordion drawer below tablet width, given the "Menu / Close (esc)" pattern implied by the page text. This table is a recommendation only; no responsive CSS or live breakpoints were captured in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived solely from static CSS custom properties, a page-text excerpt, and a color/font list — no rendered layout, computed styles, or DOM screenshots were available. Color-to-role mapping (e.g., which scheme applies to header vs. hero vs. footer) is inferred from variable naming and RGB pairing patterns, not confirmed visual placement. Typography sizes, line-heights, and letter-spacing beyond the root `--heading-*`/`--main-*` declarations are proposed conventions, not measured values. No hover, focus, active, or error states were observed. Mobile menu behavior, cart drawer interaction, and subscription-widget styling are inferred from menu/text content only. Poppins is used per CSS variables, but its licensing/self-hosting versus Google Fonts delivery was not verified. Several palette values (e.g., #467c99, #38637a, #90b0c2, #136f99) appear in the supplied hex list but could not be confidently assigned a UI role and were omitted from the token set.
