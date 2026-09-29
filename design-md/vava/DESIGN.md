---
version: alpha
name: "VAVA"
source_url: "https://vava.com"
captured_at: "2026-09-28T09:40:41.811581+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  VAVA's storefront evidence shows a teal-led palette (#00bfb2 as the dominant
  interactive/brand color, paired with a darker teal #215654 used as text and
  border foreground in Shopify section variables) set against a white canvas.
  Light teal tints (#e5f9f7, #b2e8e7, #7dd8d6) recur as section backgrounds and
  badge fills, while neutral grays (#232323, #333333, #888888, #dedede,
  #eeeeee) carry body copy, muted text, and hairlines. An orange (#c45500)
  appears in the palette and is treated here as an inferred sale/accent color
  since no other warm hue is present. Typography is Helvetica-family
  (Helvetica Now, Helvetica Neue, Arial fallback) for buttons and review UI,
  with Inter also present in the font stack and assigned here to body/UI text
  as an inferred split between a Helvetica display voice and an Inter reading
  voice. Judge.me review widget variables (--jdgm-border-radius: 0) and
  Shopify hotspot variables (0 191 178, positioned on featured-product media)
  are the only concrete interaction/layout signals; all spacing, radius, and
  breakpoint values below are proposed conventions, not measured page
  geometry. The interpretation favors a clean, clinical-calm retail tone
  suited to both nursery products and the brand's Home Theater line (4K Laser
  TV, ALR Screen Pro).

colors:
  primary: "#00bfb2"
  primary-strong: "#108474"
  ink: "#215654"
  canvas: "#ffffff"
  body: "#232323"
  muted: "#888888"
  hairline: "#dedede"
  surface-soft: "#e5f9f7"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent: "#c45500"
  tint-100: "#b2e8e7"
  tint-200: "#7dd8d6"
  overlay-40: "#2156544d"
  overlay-50: "#21565480"
  overlay-70: "#215654b2"
typography:
  display-xl: {fontFamily: "'Helvetica Now', 'Helvetica Neue', Arial, sans-serif", fontSize: 48px, fontWeight: 900, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Helvetica Now', 'Helvetica Neue', Arial, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Helvetica Neue', Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Helvetica Now', 'Helvetica Neue', Arial, sans-serif", fontSize: 15px, fontWeight: 900, lineHeight: 1.2, letterSpacing: 0.3px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    saleColor: "{colors.accent}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  media-hotspot:
    markerColor: "{colors.primary}"
    labelBackground: "{colors.overlay-70}"
    labelTextColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"

## Components

**button-primary** uses the observed `#00bfb2` teal (also the Judge.me `--jdgm-primary-color` and `--jdgm-write-review-bg-color`) as its fill, with white text and the bold Helvetica Now weight seen on the review-widget button (`font-weight:900`). Rounded value is proposed at `sm`, since the review widget itself sets `--jdgm-border-radius: 0`, suggesting the brand mixes sharp UI elements with softer product-card corners elsewhere — treated here as inferred, not confirmed for primary buttons.

**button-secondary** is a proposed outline treatment using the darker teal `#215654` (the `--color-foreground` value from the header section) for both border and text, intended for "Continue shopping" or "Buy now" secondary actions seen in the page text.

**text-input** is a proposed pattern for search, discount code, and order-note fields referenced in the cart text ("Order special instructions", "Discount code"). Border color uses the light hairline gray `#dedede`; no focus-state color was observed, so focus styling is not specified.

**nav-bar** reflects the header section's explicit CSS variables: white background (`255 255 255`) and teal-ink foreground (`33 86 84`). Sticky/scroll behavior was not observed and is not claimed.

**product-card** is proposed for catalog tiles such as "VAVA 4K Laser TV" and "VAVA ALR Screen Pro," using a white surface, hairline border, and the accent orange for the "Save %" sale label implied by repeated "Sale price / Regular price" pairs in the text.

**hero** maps to the light teal section background (`#e5f9f7` with foreground `0 191 178`) explicitly defined in a Shopify section's custom properties, used for slideshow/banner content like "Gentle Sound Better Sleep."

**footer** is a proposed dark-ink footer for contrast and closure; no footer-specific CSS was supplied, so its colors are inferred from the darkest brand ink rather than observed footer rules.

**badge** covers "Sale," "Sold Out," and promotional ribbons ("Up to 30% OFF") referenced in the page text; the accent orange is reused here since no dedicated badge color was captured in the evidence.

**media-hotspot** is a category-relevant, TVs & Projectors–specific component derived directly from observed CSS: `--hotspot-color: 0 191 178` with percentage-based `--hotspot-x/--hotspot-y` on featured-product blocks. This pattern (a marker with a dark translucent label, using `overlay-70`) is proposed for annotating projector/screen features like throw distance or ALR coating callouts on product imagery.

## Responsive Behavior
This is a recommended, non-measured breakpoint scheme, since no media queries were included in the supplied evidence:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | <600px | Single-column product grid; nav collapses to a hamburger/menu icon; touch targets ≥44px. |
| Tablet | 600–1024px | Two-column product grid; hero retains full-bleed background. |
| Desktop | 1024–1280px | Matches observed `--page-width` clamp logic (`min(100vw - scrollbar, max(page-width, 1280px))`). |
| Wide | >1280px | Content capped near 1280px per the `--page-container` calculation observed in `:root`. |

Interactive/touch states (hover, focus rings, active press) were not present in the supplied CSS and are proposed conventions only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction; no rendered layout, computed styles, or DOM screenshots were available, so all spacing, radius, and breakpoint values are proposed, not measured.
- Color **roles** (e.g., which teal is "primary" vs. "hover") are inferred from variable names like `--jdgm-primary-color` and `--color-foreground`; the underlying CSS does not label a canonical brand palette.
- The `accent` orange (`#c45500`) has no confirmed usage context in the supplied rules and is assigned to sale/badge use as a best-fit inference.
- Font stacks list Helvetica Now, Helvetica Neue, and Inter together; which family governs headings vs. body text was inferred from typical weight/usage patterns (bold Helvetica Now on buttons), not confirmed page-wide.
- Custom font (`Helvetica Now`, `HelveticaNowDisplay`) licensing/availability was not verified; generic sans-serif fallbacks are included per instructions.
- Mobile navigation, cart drawer, and slideshow interaction behavior were described in page text but not observed as rendered CSS/JS behavior.
- The site's current catalog emphasizes baby-care products; TVs & Projectors items (4K Laser TV, ALR Screen Pro) exist as a smaller "Home Theater" line within the same storefront, and this document treats that category using the same evidence-based brand system rather than a separate, unverified visual language.
