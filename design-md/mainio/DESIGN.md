---
version: alpha
name: "Mainio"
source_url: "https://www.mainioclothing.fi/en/"
captured_at: "2026-09-29T04:37:19.271333+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Mainio's storefront (mainioclothing.fi/en) presents a Nordic, editorial-minimal
  aesthetic built almost entirely from a neutral grayscale system: near-black ink
  (#1c1b1b, #363636), mid grays (#5c5c5c, #939393), and soft off-whites
  (#fafafa, #ecede9, #e7e7e7) against a white canvas. The only typeface observed
  in the CSS evidence is Montserrat with a sans-serif fallback, a geometric
  grotesk consistent with the brand's confident, unfussy tone ("Being Mainio is
  about being bold").
  The hero/slideshow Button rule set (#363636 text, white border, white
  ::before fill, white text on :hover) suggests an outline-style CTA intended
  to sit over photography, though the precise hover contrast behavior cannot be
  fully confirmed from static CSS alone. A blue pair (#1990c6 / #136f99)
  appears only inside Shopify's generic accelerated-checkout button styling and
  is treated here as a platform default, not a verified brand accent — no
  brand-specific accent color is confirmed in the supplied evidence, so the
  interpretation below leans on the observed neutral scale for primary actions
  and reserves color for sustainability/GOTS badging callouts, which is
  thematically central to the brand's GOTS-certified, Tencel™-forward
  positioning. Rounded corners default to sharp edges (0px), matching the one
  observed border-radius value.

colors:
  primary: "#1c1b1b"
  ink: "#1c1b1b"
  canvas: "#ffffff"
  body: "#363636"
  muted: "#5c5c5c"
  hairline: "#e7e7e7"
  surface-soft: "#fafafa"
  surface-card: "#ecede9"
  on-primary: "#ffffff"
  border-outline: "#ffffff"
  overlay-scrim: "#1c1b1b99"
  divider-soft: "#36363633"
  neutral-quiet: "#939393"
  checkout-accent-unverified: "#1990c6"
  checkout-accent-unverified-hover: "#136f99"
typography:
  display-xl: {fontFamily: "Montserrat, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Montserrat, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "Montserrat, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    borderColor: "{colors.border-outline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    overlayColor: "{colors.overlay-scrim}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  sustainability-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.divider-soft}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary**: A solid dark CTA (`{colors.primary}` fill, white label) proposed for core commerce actions like "Add to cart" and "Subscribe." Corner radius is set to `{rounded.none}`, matching the one sharp-edged border-radius value observed in the evidence (Shopify's accelerated-checkout button default). Hover/active states are not confirmed and are proposed as a slight darken.

**button-secondary**: Modeled on the hero slideshow `.Button` rule — transparent background, `{colors.border-outline}` (white) border, dark label text. This is evidenced directly in the CSS for on-image CTAs like "Look all." The hover transition (label turning white as a `::before` fill animates in) is present in the CSS but its final visual contrast could not be fully resolved statically, so the hover treatment is labeled proposed.

**text-input**: A plain bordered field using the light hairline gray for its border and the base body color for typed text, sized for forms such as newsletter signup or account login. No focus-state color is evidenced, so focus treatment is proposed (e.g., border darkening to `{colors.ink}`).

**nav-bar**: Reflects the `--header-is-transparent: 1` custom property, indicating the header sits over hero imagery without an opaque background at load, with white text for legibility against dark hero art. Scroll-triggered opaque/sticky states are implied by `--use-sticky-header: 1` but the resulting styling was not present in the supplied rules, so exact sticky appearance is proposed.

**hero**: A full-bleed slideshow section (`section-slideshow_*` selectors observed) using a dark overlay scrim over photography with large display type and an outline button, consistent with editorial fashion-site conventions. Copy content ("Season's Favorites," "Gorgeous Dresses") is evidenced in the page text; exact overlay opacity is inferred from the available `#1c1b1b99` token.

**product-card**: Proposed pattern for the "Look All" and collection grids (Dresses, Pants) referenced in the page text. Uses the soft neutral `{colors.surface-card}` as a card background to separate product imagery from the white page canvas, with title and price typography scaled down for grid density. No actual card markup was present in the supplied CSS, so this is a proposed adaptation of the neutral palette.

**footer**: Built on the light `{colors.surface-soft}` background with muted gray body text, housing information links (Shipping, Returns, Retailers), business/legal details, and the newsletter form referenced in the page text. Structure (columns, stacking) is not evidenced and is left to responsive guidance below.

**badge**: A small pill-shaped label proposed for merchandising flags like "Clearance Sale," "2nd Hand," or "New." Colors are drawn from the neutral surface/ink pair since no dedicated sale-tag color was present in the observed palette; a brand red or green accent (e.g., `#cb2b2b`, `#307a07`) could exist elsewhere on the site but is unverified here and intentionally excluded from primary UI roles.

**search**: A minimal bordered search affordance, styled consistently with `text-input`, intended for the header search flyout implied by the `.Search[aria-hidden]` selector in the evidence.

**sustainability-tag**: A category-appropriate component for a GOTS-certified kidswear brand — a small tag/callout style for GOTS, Tencel™ Lyocell, or "2nd Hand" material and program labels referenced heavily in the page copy. Uses the same quiet neutral tones as `badge` rather than an invented "eco-green," since no such accent color is confirmed as brand-owned in the supplied palette.

## Responsive Behavior

This is a proposed recommendation only; no live breakpoints, container queries, or mobile layouts were present in the supplied CSS.

| Breakpoint | Range | Nav | Grid |
|---|---|---|---|
| Mobile | <600px | Collapsed hamburger, transparent header likely becomes opaque on scroll | 1 product-card column |
| Tablet | 600–1024px | Condensed inline nav or hamburger | 2 columns |
| Desktop | >1024px | Full transparent-to-sticky header per `--use-sticky-header` | 3–4 columns |

Touch targets for `button-primary`, `button-secondary`, and `search` should be at least 44px tall, consistent with the Shopify accelerated-checkout button's own `clamp(25px, 44px, 55px)` sizing found in the evidence. Footer link lists and information pages should collapse into an accordion or stacked list below tablet width; this is a UX recommendation, not an observed behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover, focus, open menu, cart drawer) were directly observed.
- No explicit font-size, font-weight, or line-height values were present in the supplied CSS for headings or body copy; all `typography` sizes are proposed defaults, not measured.
- The blue pair `#1990c6`/`#136f99` comes exclusively from Shopify's generic `accelerated-checkout` wallet button styling and is explicitly excluded from brand-identity roles; the true brand accent color (if any) beyond the neutral grayscale is unverified.
- Several vivid palette entries (`#00aced`, `#4469af`, `#c8232c`, `#cb2b2b`, `#307a07`, etc.) resemble third-party social-icon or review-widget colors rather than brand tokens and were deliberately omitted from primary component roles.
- No responsive breakpoints, grid column counts, or mobile navigation patterns were observed; the table above is a recommendation only.
- Montserrat is used as the only observed font-family; its licensing/self-hosting versus Google Fonts delivery was not verified from the supplied evidence.
- The hero button's hover contrast (white border/fill combined with a white hover text color) could not be fully resolved from the static rule order alone and is flagged as proposed/uncertain.
