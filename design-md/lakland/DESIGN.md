---
version: alpha
name: "Lakland"
source_url: "https://www.lakland.com"
captured_at: "2026-09-29T04:03:19.172932+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Lakland's WordPress/Astra-based site presents a plain, trade-oriented storefront for a Chicago-built bass and guitar manufacturer. The only clearly site-authored colors in the supplied evidence are a mid-tone blue (#0274be) used for links, the mobile menu toggle, and all buttons, paired with a near-black neutral (#3a3a3a) used for hover states and default menu text. Backgrounds are unadorned white and off-white (#fafafa, #eeeeee), consistent with a WordPress theme's default code-block and comment-input tokens rather than bespoke brand surfaces. Most of the remaining supplied hex values (Bootstrap alert reds/greens/yellows, Facebook/Twitter/LinkedIn/Pinterest/WhatsApp brand colors) are plugin and social-share artifacts, not part of the product's visual identity, and are excluded from the working palette below.
  Typography is inherited from Astra's system-font stack (-apple-system, Segoe UI, Roboto, Helvetica Neue). A "Din Condensed" family also appears in the page's font list; given its condensed, display-oriented character and the site's use of bold all-caps section labels ("BASSES," "FEATURED MODELS"), it is inferred here as the display/heading family, though no selector evidence confirms this pairing. This interpretation proposes a spare, catalog-forward layout: flat 2px-radius buttons matching the observed CSS, thin hairline dividers, and generous whitespace suited to instrument photography.

colors:
  primary: "#0274be"
  ink: "#1f2124"
  canvas: "#ffffff"
  body: "#3a3a3a"
  muted: "#777777"
  hairline: "#eeeeee"
  surface-soft: "#fafafa"
  surface-card: "#f9fafa"
  on-primary: "#ffffff"
  border: "#cccccc"
  surface-alt: "#f7f6f7"
  divider: "#d5d8dc"
typography:
  display-xl: {fontFamily: "Din Condensed, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Din Condensed, Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.3px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.body-md}"
    borderBottom: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.divider}"
    linkColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border}"
    iconColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  model-spec-card:
    backgroundColor: "{colors.surface-alt}"
    borderColor: "{colors.divider}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-md}"

## Components

**button-primary** reflects the one concretely observed interactive style on the page: solid `#0274be` fill, white text, and a 2px corner radius, matching the button/menu-toggle CSS supplied in evidence. Hover swapping to the dark neutral (`#3a3a3a`) is also directly observed and should be treated as a confirmed state.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "View Catalog PDF"), inferred from Astra's generic `.is-style-outline` rule which shares the same 2px radius but was not shown paired with a specific button instance on this page.

**text-input** is a proposed field style for search and contact forms; the light background is drawn from the theme's `--ast-comment-inputs-background` token, while border and padding values are estimated defaults, not measured.

**nav-bar** models the primary menu (BASSES, GUITARS, PICKUPS, STRINGS, MERCHANDISE, DEALERS, ARTISTS, ABOUT, CONTACT) using the observed link color and the confirmed active-state blue. Collapse behavior into a mobile toggle is proposed based on the presence of `.ast-header-break-point` classes, not directly observed.

**product-card** is a proposed container for series tiles such as "USA Series," "Skyline Series," and "USA Classic Series," each pairing a condensed display title with short descriptive copy and a "DETAILS" link, mirroring the page's excerpted content structure.

**hero** proposes a dark, full-width band for the "Modern Classics. Sublime Build Quality." headline treatment implied by the page copy; the dark background and large display type are inferred stylistic choices, not measured from a captured hero element.

**footer** groups the sitemap-style link columns (Basses, Guitars, Pickups, About, Artists, Dealers, Contact) visible in the excerpt, using the dark ink background consistent with a full-bleed footer common to this theme family; exact footer styling was not captured in the CSS evidence.

**badge** is proposed for small status labels like "AVAILABLE NOW," using the confirmed brand blue at full pill radius; no badge-specific CSS was supplied.

**search** models the header search icon/field pair referenced in the page text ("Search / Search"), using the same soft background as text-input for consistency; interaction behavior (overlay vs. inline) was not observed.

**model-spec-card** is a category-appropriate addition for displaying bass/guitar specifications (body wood, pickups, scale length) on product pages, using a soft off-white surface and caption-weight labels to keep technical data legible without competing with product photography; this component has no direct evidence in the supplied CSS and is a proposed pattern for an instrument catalog.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Range | Width | Nav | Grid |
|---|---|---|---|
| Mobile | <600px | Collapsed toggle menu | Single-column product cards |
| Tablet | 600–960px | Toggle or condensed inline menu | 2-column grid |
| Desktop | 960–1200px | Full inline menu | 3-column grid |
| Wide | >1200px | Full inline menu, max content width 1200px per `--ast-normal-container-width` | 3–4 column grid |

Touch targets on button-primary/secondary should maintain a minimum 44px height given the observed `10px 40px` padding is text-height only. The mobile menu toggle's existing color tokens (`#0274be` icon, transparent background) should carry through to any hamburger/drawer implementation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS and text extraction only; no rendered layout, computed spacing, or live interaction states were observed. The palette supplied mixed genuine site tokens with numerous third-party plugin/social-icon colors (Bootstrap alert hues, Facebook/Twitter/LinkedIn/Pinterest/WhatsApp brand colors); these were deliberately excluded from the working color set as not representative of Lakland's brand identity. The role of "Din Condensed" as a display/heading font is inferred from its presence in the font-family list and the site's apparent use of bold section labels, but no selector-level CSS confirms this pairing, and its licensing/availability for production use was not verified. All spacing, rounded (beyond the confirmed 2px button radius), and component states beyond button hover are proposed defaults for a coherent system, not measurements taken from the live site. Footer, hero, and search layouts in particular were reconstructed from page text/content structure rather than captured CSS.
