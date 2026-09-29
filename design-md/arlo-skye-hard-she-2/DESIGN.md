---
version: alpha
name: "Arlo Skye"
source_url: "https://arloskye.com"
captured_at: "2026-09-29T04:09:14.871126+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Arlo Skye presents hard-shell luggage, bags, and travel accessories through a
  restrained, editorial neutral palette punctuated by warm SKU-specific accent
  tones. The supplied evidence shows a near-black/charcoal family (#0b0b0b,
  #212121, #262626, #2e2e2e) used for text and themed UI chrome (the reviews
  widget's button background is explicitly set to #262626 via CSS variables,
  which is treated here as an inferred proxy for the brand's primary button
  color). Warm off-white surfaces (#f7f7f5, #f8f6f0, #f3f0e6) sit behind product
  photography, while three accent hues — navy #153151, champagne #e8d4ae, and
  lemon #e6c96b — map directly to the actual luggage colorway names ("Navy,"
  "Champagne," "Lemon") found in the page text, giving unusually strong
  confidence for these role assignments. A muted utility blue (#3b82f6) appears
  once and is treated as a possible link/focus accent, not a core brand color.

  Typography combines a self-hosted display face, "Bricolage Grotesque" (only
  weight 400 confirmed via @font-face), for headlines and product titles, with
  "untitled sans" — present in the observed font list — inferred as the running
  body typeface, falling back to Helvetica/Arial/system-ui. Root font-size is
  observed at 19px, driving rem-based body scale tokens. All type weights above
  400 and all pixel sizes beyond the confirmed rem variables are proposed, not
  measured.

colors:
  primary: "#262626"
  ink: "#0b0b0b"
  canvas: "#ffffff"
  body: "#2e2e2e"
  muted: "#707070"
  hairline: "#dbdde4"
  surface-soft: "#f7f7f5"
  surface-card: "#f8f6f0"
  on-primary: "#ffffff"
  accent-navy: "#153151"
  accent-champagne: "#e8d4ae"
  accent-lemon: "#e6c96b"
  accent-tan: "#ab8c52"
  border-subtle: "#e7e0cf"
  overlay-black: "#0000001f"
  focus-blue: "#3b82f6"
typography:
  display-xl: {fontFamily: "'Bricolage Grotesque', sans-serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Bricolage Grotesque', sans-serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Bricolage Grotesque', sans-serif", fontSize: "22px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "'untitled sans', Helvetica, Arial, sans-serif", fontSize: "1.0625rem", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'untitled sans', Helvetica, Arial, sans-serif", fontSize: "0.9rem", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'untitled sans', Helvetica, Arial, sans-serif", fontSize: "0.825rem", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Helvetica, 'Helvetica Neue', Arial, 'Lucida Grande', sans-serif", fontSize: "16px", fontWeight: 700, lineHeight: 1, letterSpacing: "2px"}
rounded:
  none: "0px"
  xs: "2px"
  sm: "4px"
  md: "8px"
  lg: "16px"
  full: "9999px"
spacing:
  none: "0px"
  xxs: "2px"
  xs: "4px"
  sm: "8px"
  md: "12px"
  base: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
  section: "64px"
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
    borderColor: "{colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    height: "86px"
    borderBottomColor: "{colors.border-subtle}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    swatchColors: ["{colors.accent-navy}", "{colors.accent-champagne}", "{colors.accent-lemon}", "{colors.ink}"]
  hero:
    backgroundColor: "{colors.ink}"
    overlayColor: "{colors.overlay-black}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    ctaButton: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    columnGap: "{spacing.xl}"
    borderTopColor: "{colors.border-subtle}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    size: "20px"
    rounded: "{rounded.full}"
    activeRingColor: "{colors.primary}"
    optionColors: ["{colors.accent-navy}", "{colors.accent-champagne}", "{colors.ink}", "{colors.accent-lemon}"]
    gap: "{spacing.xs}"

## Components

**button-primary** — The dominant call-to-action style ("SHOP NOW", "SUBMIT"), inferred to use the dark charcoal (#262626) observed as a themed button background in the reviews-widget CSS variables, with white text and uppercase letter-spaced button typography. Hover/active darkening is proposed, not observed directly on storefront buttons.

**button-secondary** — An outline variant for lower-emphasis actions (e.g. filter or account links), using a hairline border and dark ink text on transparent background. State transitions (hover fill) are proposed.

**text-input** — Used for newsletter signup and search fields; a simple bordered rectangle with hairline border, minimal radius, and body typography sized to the observed 19px root scale.

**nav-bar** — A fixed-height header (86–87px matches the observed `--HEADER-HEIGHT` custom property) with white background, uppercase category links (LUGGAGE, BAGS, ACCESSORIES, PRESS), and dark ink text. Sticky/scroll behavior is proposed, not confirmed from static CSS.

**product-card** — Presents product imagery, title, price, and a colorway swatch row. Swatch colors are drawn directly from evidence-confirmed SKU names (Navy, Champagne, Lemon, Black), giving this component unusually high evidentiary grounding versus other proposed patterns.

**hero** — A full-bleed banner ("Luggage Reinvented") using a dark overlay over imagery for text legibility, paired with a large display headline and a primary CTA button. Overlay opacity and exact image treatment are inferred from the transparent-black overlay tokens present in the palette.

**footer** — Multi-column resource/legal links (Returns, Warranty, FAQ, Retailers) plus a newsletter capture field, set on the soft off-white surface tone with muted gray caption-sized text.

**badge** — Small inline labels seen in the product excerpt ("Bestseller," "Low Stock," "In-Cabin Approved"). Rendered here as a dark filled pill/rectangle; alternate outline or accent-tinted variants per label type are proposed, since exact visual treatment per badge type was not observed.

**search** — A minimal bordered input, likely paired with an icon trigger given the compact header height; expand/collapse interaction is proposed and not verified.

**color-swatch-selector** — A category-specific control for hard-shell luggage colorways, rendered as small circular swatches with a primary-colored active ring. Directly grounded in the Navy/Champagne/Black/Lemon options listed against best-selling products.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width        | Nav behavior                  | Product grid |
|------------|--------------|--------------------------------|---------------|
| Mobile     | < 480px      | Collapsed to menu icon (`--HEADER-HEIGHT-MOBILE` ≈ 60px observed) | 1 column |
| Small      | 480–767px    | Collapsed hamburger nav        | 2 columns |
| Medium     | 768–1023px   | Partial inline nav (`--HEADER-HEIGHT-MEDIUM` ≈ 80px observed) | 2–3 columns |
| Large      | 1024px+      | Full inline nav (~86px header) | 3–4 columns |

Touch targets should be a minimum of 44×44px for buttons, badges, and swatch selectors on mobile. Navigation collapse points and exact grid column counts are proposed defaults consistent with the observed header-height custom properties, not confirmed layout observations.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, a font @font-face declaration, a page-text excerpt, and a color palette list — not a rendered or interactively tested page. Specific gaps:

- No live layout, spacing rhythm, or grid measurements were observed; all spacing and breakpoint values are proposed defaults.
- Semantic color-role assignments (e.g. `primary` = #262626) are inferred from a third-party reviews-widget theme variable, not confirmed as the storefront's own button color.
- "Untitled Sans" is inferred as the body typeface from its presence in the aggregated font list; no direct `font-family` declaration tying it to body text was supplied.
- Only Bricolage Grotesque weight 400 was confirmed via @font-face; heavier display weights are assumed, not verified.
- Hover, focus, active, and error states for all components are proposed and were not present in the supplied evidence.
- Mobile/tablet navigation collapse behavior, drawer/cart interactions, and swatch-selection interaction states were not observed.
- Custom font licensing/self-hosting terms for Bricolage Grotesque and Untitled Sans were not verified beyond the presence of a self-hosted woff2/woff file.
