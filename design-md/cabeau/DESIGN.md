---
version: alpha
name: "Cabeau"
source_url: "https://cabeau.com"
captured_at: "2026-09-28T09:31:29.187521+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Cabeau's storefront evidence shows a Shopify theme with a single confirmed
  brand accent: teal `#108474`, used consistently across the Judge.me review
  widget (primary color, star color, write-review button, reviewer-name
  color), which is the strongest signal of an intentional brand color in the
  supplied CSS. A darker teal (`#0d736e`) and a plum/purple (`#5a1c6a`, with a
  lighter tint `#a89cc8`) also appear and are treated as inferred secondary
  accents, since their exact usage roles are not confirmed by selectors. The
  remaining palette is dominated by neutrals (`#ffffff`, `#101421`,
  `#333333`, grays from `#cccccc` to `#f7f5fa`) consistent with a
  product-photography-led ecommerce layout, plus a cluster of recognizable
  payment/social-icon colors (Visa, Mastercard, PayPal, Facebook, Pinterest,
  WhatsApp) that are excluded here as third-party marks, not brand tokens.
  Two font families recur outside monospace/icon fonts — DM Sans and Plus
  Jakarta Sans — so this spec assigns Plus Jakarta Sans to display/heading
  roles and DM Sans to body/UI text as an inferred pairing. Spacing and
  rounded-corner scales are proposed, since the site's actual `--sp-*` and
  radius values were not resolvable to fixed pixel numbers from the supplied
  CSS.

colors:
  primary: "#108474"
  primary-hover: "#0d736e"
  ink: "#101421"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#7b7b7b"
  hairline: "#e4e4e4"
  surface-soft: "#f7f5fa"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  accent: "#5a1c6a"
  accent-soft: "#a89cc8"
  border: "#cccccc"
typography:
  display-xl: {fontFamily: "'Plus Jakarta Sans', sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Plus Jakarta Sans', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Plus Jakarta Sans', sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'DM Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'DM Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'DM Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'DM Sans', sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    overlayColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.accent}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  fit-finder:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"

## Components

**button-primary** is proposed as Cabeau's core conversion action (Shop, Add to Cart, Join Cabeau Club), using the observed teal `#108474` since it is the only color reinforced across multiple CSS custom properties (review-widget primary/star/button colors), with white text matching the observed `--jdgm-write-review-text-color: white`.

**button-secondary** is a proposed outline treatment for lower-emphasis actions (Continue Shopping, Shop All), using ink-on-canvas since no secondary button color was directly observed.

**text-input** covers cart notes, discount code, and search fields referenced in the page text; styling (bordered, minimal radius) is proposed, not measured.

**nav-bar** reflects the observed header section variables (`--section-padding-top/bottom: 32px`, `--color-background: 255 255 255`, `--color-foreground: 23 23 23`), interpreted here as a white bar with near-black text and a bottom hairline; the exact hairline color is inferred.

**product-card** supports the Best Sellers grid (Evolution X, TNE S3, Evolution Cushion) with title and price typography split into two observed-adjacent sizes; card background and radius are proposed defaults for a photography-forward catalog.

**hero** models the homepage's rotating promotional banners (Slim TNE S3, Evolution X Deluxe, Personalize Your Pillow); the soft lavender background is one candidate from the observed palette, with overlay/text contrast proposed for legibility over imagery.

**footer** uses ink as background with white text, inferred from the dark, condensed brand-club/newsletter block described in the page text; actual footer color was not directly isolated in the CSS evidence.

**badge** is proposed for promotional flags ("Now Available," "20% Off," sustainability/warranty callouts) using the plum accent-soft pairing as a distinguishing but secondary tone from the primary teal.

**search** models the "Search drawer" pattern referenced in navigation text, styled as a pill-shaped overlay field; interaction behavior (drawer animation, focus states) is not observed.

**fit-finder** is a category-specific component proposed for the "Find Your Fit" flow evidenced in navigation — a quiz-like or guided-selection panel helping travelers choose a pillow style; visual treatment is proposed, not observed.

## Responsive Behavior

A compact, proposed breakpoint table (not measured from live rendering):

| Breakpoint | Range | Layout guidance |
|---|---|---|
| mobile | <640px | Single-column product grid, collapsed nav into a drawer/menu icon, sticky add-to-cart. |
| tablet | 640–1024px | 2-column product grid, condensed top promo bar, search icon triggers overlay. |
| desktop | 1024–1280px | 3–4 column product grid, full horizontal nav, visible top announcement bar. |
| wide | >1280px | Content capped near the theme's observed `--page-width`/`--page-container` logic (max ~1280px content, extra space as margin). |

Touch targets should be at least 44×44px for cart, search, and nav icons. Nav collapse point, drawer behavior, and sticky elements are recommendations only, not measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Colors are drawn only from the supplied palette; several entries (Visa/Mastercard/Amex blues-reds, Facebook/Pinterest/WhatsApp brand colors) were identified as third-party payment/social icon colors and deliberately excluded from the design token set rather than treated as brand colors.
- `ink`, `body`, `surface-soft`, `surface-card`, `accent`, and `accent-soft` role assignments are inferred from limited signals (one header foreground declaration, one review-widget variable set) and are not confirmed as global brand tokens.
- Typography pairing (Plus Jakarta Sans for display, DM Sans for body) is inferred from font-family evidence alone; no selector in the supplied CSS confirms which family is applied to which element.
- All pixel values for typography, spacing, and radius are proposed defaults; the live theme uses custom `--sp-*` and `--text-h*` variables whose resolved pixel values were not present in the supplied evidence.
- No interaction states (hover, focus, active, disabled), mobile navigation behavior, or animation timing were observed; all such states are proposed placeholders.
- Custom font availability, licensing, and self-hosting status for DM Sans and Plus Jakarta Sans were not verified from the supplied evidence.
