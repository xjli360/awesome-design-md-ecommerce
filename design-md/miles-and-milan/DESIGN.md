---
version: alpha
name: "Miles & Milan"
source_url: "https://milesandmilan.com"
captured_at: "2026-09-29T03:55:13.085719+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Miles & Milan's stylesheet is built on a restrained black-and-white foundation typical of a Shopify baby-apparel storefront: pure black (#000000) text and button borders against a white (#ffffff) canvas, with a family of warm mid-grays (#333333, #4e4b4b, #686464) used for secondary text, hover states, and button interactions. The single observed type family is Oswald paired with Helvetica Neue/Arial fallbacks, applied uniformly to both body copy (14px/1.6, regular weight) and headings (uppercase, 1px letter-spacing), giving the brand a clean, slightly editorial, gender-neutral tone appropriate for "Joyfully Made" baby and toddler clothing.
  No brand accent color is explicitly declared in the supplied evidence; #d02e2e and #56ad6a appear in the palette without confirmed semantic roles, so they are mapped here as inferred accent (sale/CTA emphasis) and success (confirmation/availability) colors rather than confirmed brand hues. Hairlines and card surfaces are drawn from the observed light-gray set (#dddddd, #f7f7f7, #fafafa) to suggest soft, low-contrast separation between header, product grid, and footer, consistent with the site's minimal, whitespace-forward layout implied by its copy ("shop by age," "buy together and save"). All roles below are evidence-grounded reuses of the supplied palette; layout, spacing, and componentry are proposed interpretations, not measured observations.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#686464"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent: "#d02e2e"
  success: "#56ad6a"
  overlay: "#00000099"
typography:
  display-xl: {fontFamily: "Oswald, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Oswald, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Oswald, Helvetica Neue, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 1px}
  body-md: {fontFamily: "Oswald, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Oswald, Helvetica Neue, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Oswald, Helvetica Neue, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Oswald, Helvetica Neue, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 1px}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    hoverBackgroundColor: "{colors.muted}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid {colors.ink}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    overlayColor: "{colors.overlay}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid transparent"
    focusBorderColor: "{colors.primary}"
    padding: "{spacing.xs} {spacing.base}"
  milestone-size-selector:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

**button-primary**: A solid black call-to-action button (e.g., "Add to Cart," "View Products") with white text, reflecting the site's high-contrast, black-bordered button system observed in `.btn--secondary` and `.btn--clear` rules. Hover/focus states are proposed as slightly lighter grays for feedback, consistent with the muted-gray hover values seen on secondary buttons.

**button-secondary**: A white/outline button with a black 1px border, directly mirroring the observed `.btn--secondary` and `.btn--outline` rules, including the confirmed `#686464` hover fill and `#5b5858` active/focus fill. Used for lower-emphasis actions like "View Collection."

**text-input**: A minimal bordered input for search, email capture, and forms. Border color and focus treatment are proposed, since only the header search bar's transitional and z-index behavior was observed, not its resting border color.

**nav-bar**: A white, bottom-bordered header (per `.site-header`) holding logo, category links (Newborn–12M, Toddlers, Big Kids), search, and cart. Uppercase Oswald link styling is inferred from the global heading transform rule.

**product-card**: A grid tile for product listings with a soft off-white card surface and thin hairline border, proposed to organize price, title, and swatch/size information; no card shadow or radius was directly observed.

**hero**: A full-width banner section (matching homepage copy like "Go Outside and Explore!") using the largest display type scale and a soft background tint, with an optional dark scrim for text legibility over imagery — proposed, not confirmed by layout evidence.

**footer**: A light, low-contrast block containing legal links, payment icons, and social links, using muted gray body text on white, consistent with the footer text list in the page excerpt (Shipping & Returns, Privacy Policy, Wholesale).

**badge**: A small pill using the inferred accent red, proposed for sale/new/exclusive labeling (e.g., "Exclusive Collection only at Kohl's"), since no dedicated badge selector was present in the CSS evidence.

**search**: A right-aligned, expand-on-interaction search control matching `.header-search .search-bar`'s observed transition and z-index properties; resting/expanded width values beyond the 5px collapsed state are not confirmed.

**milestone-size-selector**: A category-specific component for age/size selection (0–2yrs, Newborn–12M, Toddlers, Big Kids) referencing the site's "Child Milestones" navigation concept; active-state styling reuses the primary/on-primary pairing and is proposed rather than observed.

## Responsive Behavior

| Breakpoint | Range          | Layout intent (proposed)                          |
|------------|----------------|-----------------------------------------------------|
| mobile     | < 480px        | Single-column stack, collapsed hamburger nav, full-width buttons |
| tablet     | 480–1024px     | 2-column product grid, condensed nav labels          |
| desktop    | > 1024px       | 3–4 column product grid, full horizontal nav with visible search |

Touch targets are recommended at a minimum 44×44px for cart, search, and menu icons. Navigation is proposed to collapse into a slide-out or hamburger menu below tablet width, with the search bar expanding to full-width on focus. This table is a recommendation based on typical Shopify baby-apparel patterns and the theme's transition/z-index hints; it does not reflect measured responsive behavior of the live site.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS and page-text extraction only; no rendered layout, breakpoint behavior, or interactive states (hover, focus, active, mobile menu) were directly observed. The primary/accent/success color roles are inferred mappings from a broader supplied palette that includes many utility and overlay tones (e.g., alpha-blended blacks/whites) whose actual UI usage is unconfirmed. Typography sizes beyond the confirmed 14px/1.6 body rule are proposed scale estimates, not measured values. Oswald's licensing and self-hosted vs. third-party delivery were not verified. Component definitions (product-card, hero, milestone-size-selector, badge) are reasonable, category-appropriate proposals for a baby-clothing storefront but are not confirmed against actual rendered markup.
