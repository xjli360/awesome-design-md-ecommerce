---
version: alpha
name: "Rogue Hoe"
source_url: "https://roguehoe.com"
captured_at: "2026-09-28T10:14:07.722089+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Rogue Hoe is a Missouri-made hand-tool manufacturer serving gardeners, farmers,
  trailbuilders, and wildland firefighters. The observed CSS comes from a Divi/WordPress
  theme stack layered with WooCommerce and Gutenberg default palettes, so the working
  brand signal is narrower than the full extracted color list. Confirmed, page-applied
  values are a near-black heading color (#333333), a mid-gray body/copy color (#666666)
  on a white canvas, and a sky-blue accent (#2ea3f2) used for hover and link states.
  A dark charcoal (#32373c) appears as the default WordPress button background, which
  we treat as a secondary/utility button color rather than the primary brand accent,
  since #2ea3f2 is the color explicitly tied to interactive link and hover states.
  Grays (#dddddd, #eeeeee, #f4f4f4) are inferred as hairline and soft-surface roles from
  common Divi utility shades in the palette, not from directly observed border/background
  declarations. Typography is Open Sans with Arial/sans-serif fallback, the only font-family
  explicitly set on body copy; Montserrat and Work Sans appear in the raw font list but
  are not confirmed applied to visible text, so they are omitted from the type scale.
  The resulting interpretation favors a plain, utilitarian, rugged-tool aesthetic: dense
  gray text, sparse blue accenting, square-edged buttons, and minimal ornamentation,
  consistent with a working-tools catalog site rather than a lifestyle brand.

colors:
  primary: "#2ea3f2"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#666666"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  button-dark: "#32373c"
  border-light: "#cccccc"
  accent-deep: "#006799"
typography:
  display-xl: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.7em, letterSpacing: 0px}
  body-sm: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.7em, letterSpacing: 0px}
  caption: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0.2px}
  button-md: {fontFamily: "Open Sans, Arial, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.7em, letterSpacing: 0px}
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
    backgroundColor: "{colors.button-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "2px solid {colors.button-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  tool-category-menu:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    hoverTextColor: "{colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.button-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer:
    backgroundColor: "{colors.button-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"

## Components
**button-primary** uses the confirmed accent blue (#2ea3f2) as a solid fill, intended for primary calls to action such as "Shop Now" or "Learn More" links seen in the category teasers. Hover/active darkening is proposed, not observed.

**button-secondary** reuses the dark charcoal (#32373c) captured from the default WordPress `.wp-element-button` rule, appropriate for lower-priority actions like "Add to Cart" alternates or filter toggles. Border and fill share the same dark tone per the source declaration.

**text-input** is a proposed pattern for search and contact-form fields; canvas background and hairline border are inferred defaults since no explicit input styling was present in the supplied CSS.

**nav-bar** represents the top utility/category bar implied by the page-text menu structure ("By Purpose," "By Type," "About," "Contact"). Layout, sticky behavior, and exact spacing are proposed, not measured.

**tool-category-menu** is a category-appropriate component reflecting the dual navigation taxonomy (by purpose: gardening/farming/firefighting/trailbuilding; by type: hoe/rake/scraper). Soft gray background and blue hover state are proposed to visually separate this from primary nav.

**product-card** covers tool listing tiles (e.g., "70AR – Travis Tool," "575G"). Card background and hairline border are inferred from the generic light-gray palette; no explicit card CSS was supplied.

**hero** models the homepage category-promo blocks ("Trailbuilding Tools," "Firefighting Tools," "Garden Tools"). Dark charcoal background with white text is proposed to match the one dark-background utility class (`et_pb_bg_layout_dark`) found in the evidence.

**footer** reflects the site's "Hours & Info" and link-list footer content (address, phone, policy links). Dark background and blue link color are proposed for contrast and consistency with the button-dark and primary accent tokens.

**badge** is a proposed small-label component (e.g., "New," "Best Seller," as implied by "New Flat Hoes & Rakes" and "Best Selling Garden Hoe" copy) using the primary accent as fill.

**search** models the site's visible search icon/overlay ("Search ×" in the page text) using canvas background and accent-colored icon, consistent with the `#2ea3f2` hover rule applied to `#et_search_icon:hover`.

## Responsive Behavior
Recommended, not measured, breakpoint table:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | 0–599px | Single-column stacking; nav collapses to hamburger/off-canvas menu (proposed) |
| tablet | 600–979px | Two-column product grids; category mega-menu collapses to accordion (proposed) |
| desktop | 980–1279px | Full nav bar with dropdowns; matches Divi's typical `--wp--style--global--wide-size: 1080px` container hint |
| wide | 1280px+ | Max content width constrained near observed 1080px wide-size token; extra margin only |

Touch targets should be a minimum 44×44px for nav and cart icons; the dual "By Purpose / By Type" menu should collapse into a single expandable list on mobile. None of this is confirmed site behavior — it is a UX recommendation based on the taxonomy implied by page text.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction only; no rendered layout, breakpoints, or interaction states (hover, focus, active, disabled) were directly observed.
- The supplied color list mixes confirmed page-applied colors with default WooCommerce/Gutenberg editor palette swatches (e.g., #7f54b3, #cf2e2e, #00d084); only colors tied to actual selectors in the evidence were promoted to named roles.
- Heading font-family is inherited/assumed from body (Open Sans) since no explicit `font-family` was set on `h1–h6`; this is an inferred mapping.
- Montserrat and Work Sans appear in the raw font-family list but have no confirmed applied selector, so they were excluded from the typography scale.
- Border-radius on buttons was observed as 3px (`.et_pb_button`) but mapped to the nearest standard token (`rounded.sm` = 4px) for system consistency; exact pixel match is not guaranteed.
- Spacing scale values are proposed conventions, not extracted from layout measurements.
- Custom font licensing/availability (e.g., ETmodules icon font, WPMenuCart, WooCommerce icon fonts) was not verified for reuse outside the original site.
- Mobile navigation collapse behavior, cart drawer behavior, and product-grid column counts are inferred from typical e-commerce patterns, not confirmed from this site's live rendering.
