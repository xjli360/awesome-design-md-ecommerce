---
version: alpha
name: "2 Hounds Design"
source_url: "https://2houndsdesign.com"
captured_at: "2026-09-29T03:54:45.695331+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  2 Hounds Design sells premium American-made dog collars, leashes, and harnesses,
  and its storefront CSS reflects a straightforward e-commerce theme layered with a
  third-party review widget (Okendo). The observed palette centers on a muted navy
  blue (#3f548e) used as the primary button background, with a darker navy
  (#2b3960) appearing as its hover/active state and as text on a chartreuse-green
  secondary button (#c1cd42). Body copy uses a near-black (#232323) on white
  (#ffffff), with light grays (#f4f4f4, #dedede, #f1f0ee) forming soft surfaces and
  hairlines. The only observed typeface is Brandon Grotesque, a licensed display
  sans, stacked with system-font fallbacks (Helvetica, Arial, Roboto, sans-serif);
  no serif or secondary family was found. Payment-badge colors (PayPal blue,
  Mastercard red/orange, etc.) are excluded from the brand palette as
  third-party marks. Rounded corners are inferred narrowly from the Okendo button
  token (4px) and applied here as a general small-radius convention, since no
  broader corner-radius evidence was supplied. Spacing, type scale beyond the
  observed 1rem body size, and component layout are proposed conventions suited
  to a pet-product retail site, not measured observations, and are labeled
  accordingly throughout.

colors:
  primary: "#3f548e"
  primary-hover: "#2b3960"
  secondary: "#c1cd42"
  ink: "#232323"
  canvas: "#ffffff"
  body: "#232323"
  muted: "#676986"
  hairline: "#dedede"
  surface-soft: "#f4f4f4"
  surface-card: "#f1f0ee"
  on-primary: "#ffffff"
  on-secondary: "#2b3960"
  border-input: "#dbdde4"
  disabled-text: "#555555"
  disabled-bg: "#f4f4f4"
typography:
  display-xl: {fontFamily: "Brandon Grotesque, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Brandon Grotesque, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "Brandon Grotesque, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Brandon Grotesque, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  body-sm: {fontFamily: "Brandon Grotesque, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "Brandon Grotesque, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "Brandon Grotesque, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.3px}
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
    padding: "{spacing.base} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-input}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-input}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  size-guide-callout:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"

## Components
**button-primary** uses the observed navy (`#3f548e`) background with white text, directly sourced from the Okendo widget's `--oke-button-backgroundColor` token and the theme's `.btn--primary` rule; hover/active state (proposed to reuse `#2b3960`) is grounded in the Okendo hover token but not confirmed for native theme buttons.

**button-secondary** reuses the observed `.btn--secondary` pairing of chartreuse (`#c1cd42`) background with dark navy (`#2b3960`) text, suited to secondary CTAs like "Learn More" links seen in the blog excerpt.

**text-input** is proposed styling for search and account forms; the border color (`#dbdde4`) is observed from the Okendo button border token, reused here for form inputs since no native input CSS was supplied.

**nav-bar** reflects the site's evident structure (logo, search, cart, category menu) with white canvas and dark ink text; exact height is known (`--header-height: 83px`) but padding/spacing values are proposed.

**product-card** is a proposed pattern for collar/leash/harness listings, using the light card surface (`#f1f0ee`) and hairline border (`#dedede`) observed in the palette, with no confirmed card CSS from the evidence.

**hero** is inferred from homepage copy describing a "Shop Now" hero banner; soft gray background and large display type are proposed, not measured.

**footer** is a proposed dark-ink footer treatment; actual footer background color was not confirmed in the supplied CSS, so this is a stylistic inference from the ink/canvas contrast pair.

**badge** supports "Free Shipping" or "As Seen On" style callouts using the secondary chartreuse color; fully proposed, no badge CSS observed.

**search** and **size-guide-callout** are additional proposed components suited to the product category (collar/harness sizing is a known customer need per the site's "Size Guide" link), styled with soft surface and hairline tokens already present in the palette.

## Responsive Behavior
Recommended, not measured breakpoints:
| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | single-column, hamburger nav, promo bar (`37px`) may collapse |
| tablet | 600–1024px | 2-column product grid, sticky header (`83px`) preserved |
| desktop | >1024px | full nav bar, 3–4 column product grid |

Touch targets should be a minimum 44px hit area for cart/menu icons; mobile menu collapse behavior is proposed given the "Open Mobile Menu" label found in page text, but exact interaction/animation was not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS extraction and a single page-text excerpt; no rendered layout, responsive behavior, or interaction states (hover, focus, active transitions beyond the Okendo tokens) were directly observed. Semantic color roles (e.g., which gray serves as card vs. hairline) are inferred from usage context in Okendo tokens and general theme conventions, not confirmed per-component CSS. Typography sizes beyond the base `1rem` body value are proposed estimates scaled for a retail storefront; Brandon Grotesque's licensing and self-hosted availability were not verified. Spacing and rounded-corner scales beyond the single observed `4px` Okendo radius are proposed conventions. Mobile menu, cart drawer, and product-page layouts were not present in the supplied evidence and are therefore absent from concrete claims.
