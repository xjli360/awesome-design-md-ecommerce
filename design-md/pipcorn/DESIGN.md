---
version: alpha
name: "Pipcorn"
source_url: "https://pipsnacks.com"
captured_at: "2026-09-28T09:26:15.257460+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Pip's Heirloom Snacks (formerly Pipcorn) presents a farm-forward, ingredient-led
  snack brand built on a small observed palette: an olive/light green
  (#95c058) used as the primary call-to-action color on ".pip-button",
  a deep "cafe noir" brown (#512d1e), a light teal-blue (#3eadb8), and a
  tan "cardboard" (#b69775), all declared as CSS custom properties. A
  brighter utility blue pair (#1990c6 / #136f99) appears only on Shopify's
  generic unbranded payment-button component, so it is treated as a
  secondary/system accent rather than a core brand color. Near-black
  (#121212) and white (#ffffff) round out text and canvas roles; #dedede
  appears solely as a loading-skeleton background and is reused here as a
  hairline/divider tone.
  Typography is set in a proprietary "Pluto" family (regular, Medium,
  Heavy weights) with sans-serif fallback, plus a "vinyl" face referenced
  in the font stack that is assumed to be a display/logotype accent used
  sparingly; its availability and license are unverified.
  The interpretation leans into an earthy, farm-to-bag identity: green as
  the primary action color, cafe-noir brown for headings/ink, cardboard
  tan and light-blue as supporting accents for badges, farm-story cards,
  and dividers. Layout, spacing, and component states below are proposed
  patterns consistent with the evidence, not measured observations.

colors:
  primary: "#95c058"
  ink: "#512d1e"
  canvas: "#ffffff"
  body: "#121212"
  muted: "#b69775"
  hairline: "#dedede"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#3eadb8"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  transparent: "#00000000"
typography:
  display-xl: {fontFamily: "PlutoHeavy, sans-serif", fontSize: 56px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Pluto, sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "PlutoMedium, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Pluto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Pluto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Pluto, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "PlutoMedium, sans-serif", fontSize: 19px, fontWeight: 500, lineHeight: 1, letterSpacing: 0px}
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    accent: "{colors.muted}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaButton: "button-primary"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.base}"
  farm-provenance-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    accent: "{colors.muted}"

## Components
- **button-primary**: Uses the observed `.pip-button` pattern (`#95c058` background, white text, larger 19px label). Proposed as the default add-to-cart/CTA style; hover/active states are not observed and are treated as proposed darker-tint states.
- **button-secondary**: An outline variant in brand ink for lower-emphasis actions (e.g. "Learn About Us"); border and fill states are inferred, not measured.
- **text-input**: Newsletter/email capture field styling ("Sign up" in footer copy) using canvas background and hairline border; focus/error states are proposed.
- **nav-bar**: Top navigation carrying "Shop", "About Us", "Why heirloom", "Press", "Blog", "Find a store", "Search" links; sticky/scroll behavior is not confirmed by evidence.
- **product-card**: Grid tile for bestseller items (e.g. "Cheddar Cheese Balls $20"), pairing a title, price, and review-count caption; image treatment and hover elevation are proposed.
- **hero**: Homepage banner area referencing "Your favorite childhood snacks made better," using a large display headline and primary CTA; exact hero imagery/overlay is not observed.
- **footer**: Dark-ink footer block containing legal links (Privacy, Terms, Refund Policy) and the 20%-off signup form; color inversion (ink background, white text) is inferred from `#512d1e`/`#121212` availability, not directly measured on the footer element.
- **badge**: Small pill label for claims like "Non-GMO Project Verified" or "Gluten Free," using the teal accent for differentiation from the green primary; this pairing is proposed.
- **search**: Rounded search field/trigger tied to the "Search" nav item; interaction (modal vs. inline) is not observed.
- **farm-provenance-card**: Category-appropriate component for the "It all starts with family farms" storytelling section (Ernst Farms, Rankin Farm, etc.), pairing a farm name, location, and narrative copy in a bordered card; cardboard-tan accent ties it visually to the packaging-inspired palette.

## Responsive Behavior
Recommended (not measured) breakpoints:

| Breakpoint | Width        | Notes                                   |
|------------|--------------|------------------------------------------|
| sm         | 0–639px      | Single-column stack, nav collapses to menu icon |
| md         | 640–1023px   | 2-column product grid, inline search reveal |
| lg         | 1024–1439px  | 3–4 column product grid, full nav visible |
| xl         | 1440px+      | Max-width content container, generous section padding |

Touch targets should be at least 44px tall (aligning with the `.shopify-payment-button__button` clamp(25px, …, 55px) pattern observed in cart CSS). Primary nav should collapse to a hamburger/drawer below `md`; the cart should render as a slide-in drawer per the "Cart / Close cart" copy found in evidence. This table is a design recommendation, not a measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction only; no rendered screenshots, computed styles, or JavaScript-driven states were captured.
- Semantic role assignments (ink vs. body vs. muted) are inferred from limited custom-property names and one component rule; actual usage across the live site may differ.
- All typography sizes except the `.pip-button` 1.2rem value are proposed, not measured.
- Interaction states (hover, focus, active, disabled) beyond the two documented button-hover rules are proposed, not observed.
- Mobile/responsive layout, breakpoints, and collapse behavior were not directly observed and are offered only as recommendations.
- "Pluto" and "vinyl" font families are referenced in CSS but their licensing, weights, and full availability were not verified.
- The `#1990c6`/`#136f99` blue pair originates from a generic Shopify wallet-button stylesheet, not brand-specific CSS, and may not reflect intentional brand color choices.
