---
version: alpha
name: "Bennett Winch"
source_url: "https://bennettwinch.com"
captured_at: "2026-09-28T09:12:54.916767+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Bennett Winch presents as a restrained, editorial English leather-goods brand built on a pure black-and-white foundation. The observed stylesheet sets body copy in Montserrat (sans-serif) at 16px/1.5 in solid black (#000) on a white (#fff) canvas, while all headings and primary button labels switch to Monotype Baskerville, a serif face, rendered in uppercase with wide letter-spacing on buttons — a classic "sans-serif body, serif display" pairing common to heritage-leather positioning. Some supplementary UI text (dates, overlays) uses Helvetica Neue/Arial as a secondary sans fallback.

  The captured palette mixes true brand values (pure black #000000, white #ffffff, a black-hover-to-#404040 state, and several warm/cool greys such as #ebebeb, #f2f2f2, #f7f7f7, #685858) with generic Bootstrap-style utility colors (#007bff, #28a745, #dc3545, #ffc107, alert-state tints) that are almost certainly framework defaults rather than brand decisions; these are treated here as inferred/unused rather than promoted into brand roles. The interpretation below therefore centers on a monochrome ink-on-canvas system with soft grey surfaces for cards and dividers, a single muted warm-grey for secondary text, and a sparing red reserved for alert/badge use only, all explicitly labeled where semantic role is inferred rather than measured.

colors:
  primary: "#000000"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#685858"
  hairline: "#ebebeb"
  surface-soft: "#f7f7f7"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  hover-ink: "#404040"
  divider: "#dee2e6"
  accent-alert: "#d20000"
typography:
  display-xl: {fontFamily: "Monotype Baskerville, serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Monotype Baskerville, serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "Monotype Baskerville, serif", fontSize: "20px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "Montserrat, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Montserrat, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Montserrat, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.02em"}
  button-md: {fontFamily: "Monotype Baskerville, serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0.08em"}
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
    padding: "{spacing.sm} {spacing.lg}"
    hover:
      backgroundColor: "{colors.hover-ink}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.lg}"
    hover:
      textColor: "{colors.hover-ink}"
      borderColor: "{colors.hover-ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.divider}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
    focus:
      borderColor: "{colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottomColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    borderTopColor: "{colors.hover-ink}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  gallery-carousel:
    backgroundColor: "{colors.ink}"
    dotColor: "{colors.on-primary}"
    dotActiveOpacity: 0.75
    dotInactiveOpacity: 0.25
    padding: "{spacing.sm}"

## Components

**button-primary** — Solid black fill with white uppercase serif label and a lighter grey (#404040) hover state, matching the observed `.btn` and `:hover` declarations; used for "Add to Bag" and primary CTAs.

**button-secondary** — Transparent/outlined variant with black border and text, darkening to the same #404040 on hover/focus, directly mirroring the observed `.btn--secondary` rule; suited to "View Bag" or filter actions.

**text-input** — Proposed field style using a light hairline border and white background, since no explicit input border CSS was supplied; focus state darkening the border to pure ink is inferred to match button hover logic.

**nav-bar** — White header bar with black text and a thin hairline underline; proposed structure only, as no header-specific selectors were captured, but colors are drawn from the observed base palette.

**product-card** — A soft off-white card (#f2f2f2) framed by a light hairline, holding a serif product title and a smaller sans-serif price line — proposed composition appropriate to a duffel/holdall catalog grid.

**hero** — Full-bleed black band with white display serif headline, used for campaign moments (e.g. "BW x 24H Le Mans"); background/text colors are observed values, but the hero layout itself is inferred from category convention, not measured.

**footer** — Black footer with white body-sm links, echoing the ink/on-primary pairing used elsewhere; multi-column structure (Shop, Discover, Currency) is inferred from the navigation text found in the page excerpt.

**badge** — Small pill using the one clearly non-utility red (#d20000) found in the palette, proposed for "New" or "Best Seller" tags; role is inferred since no badge selector was present in the supplied CSS.

**gallery-carousel** — Directly grounded in the observed `.slick-dots` rules: black/dark backdrop, white dot indicators at 25% opacity inactive and 75% opacity active, sized 20×20px — suited to the product-image slider on duffel/holdall detail pages.

## Responsive Behavior

| Breakpoint | Width      | Layout guidance (proposed) |
|-----------|------------|------------------------------|
| Mobile    | < 480px    | Single-column stack, hamburger nav, full-width buttons, touch targets ≥ 44px |
| Small     | 480–768px  | 2-column product grid, condensed nav-bar padding |
| Tablet    | 768–1024px | 2–3 column product grid, inline search reveal |
| Desktop   | 1024–1440px| 3–4 column grid, full horizontal nav with dropdown categories |
| Wide      | > 1440px   | Max-width content container, generous section spacing (`{spacing.section}`) |

This table is a recommendation based on common Shopify-theme patterns and category norms; no live responsive behavior, container widths, or JS breakpoints were observed in the supplied evidence. Nav collapse to a mobile menu button is plausible given the "Mobile Menu Button" text found in the page excerpt, but its visual behavior was not captured.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, computed styles, or DOM screenshots were available. The supplied color list mixes genuine brand values (black, white, mid-greys) with generic Bootstrap utility colors (#007bff, #28a745, #dc3545, alert tints, etc.) that are unlikely to be true brand colors — these were deliberately excluded from role assignment rather than guessed into use. Several role mappings (muted text, hairline, surface-card, badge accent) are inferred best-fits from the available palette, not confirmed via observed selectors for those exact purposes. Font sizes for headings, captions, and inputs are proposed defaults since only body (16px) and button (14px) sizes were explicitly present in the CSS; Monotype Baskerville is a licensed commercial font and its availability/licensing for any implementation has not been verified. No interaction states beyond `:hover`/`:focus` on buttons were observed, and mobile/responsive layout, spacing scale, and border-radius values beyond the button's 2px are proposed conventions, not measured from the live site.
