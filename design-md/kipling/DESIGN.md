---
version: alpha
name: "Kipling"
source_url: "https://kipling.com"
captured_at: "2026-09-29T04:10:34.858540+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from the live us.kipling.com storefront CSS,
  a Shopify-based site presenting Kipling's soft-goods range: handbags,
  backpacks, luggage, and travel accessories. The observed design tokens
  show a custom "Kipling" display/heading typeface (weight 700 confirmed
  via a bundled woff2), paired with Roboto for body copy and Roboto Mono
  for accent/label text — a utilitarian, catalog-driven pairing suited to
  a colorful, product-dense assortment.
  The neutral system (near-black #111111/#282828, white #ffffff, light
  grays #f7f7f7/#c9c9c9) forms the functional UI scaffold: text, surfaces,
  and hairlines. A deep teal (#004b48) appears explicitly as a hover/link
  accent in the site's own custom properties and is promoted here to the
  primary interactive color. Corner radii and shadow tokens are directly
  observed; the numeric spacing scale is not exposed in the evidence (only
  named custom-property references), so spacing values below are proposed
  and labeled inferred. Additional swatch colors (rust, plum, navy) are
  drawn from real product-thumbnail hexes and used only as optional accent/
  badge colors, not as core brand identity, since Kipling's palette is
  driven by rotating seasonal product colorways rather than a fixed brand
  palette.

colors:
  primary: "#004b48"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#282828"
  muted: "#6d6d6d"
  hairline: "#c9c9c9"
  surface-soft: "#f7f7f7"
  surface-card: "#f6f6f4"
  on-primary: "#ffffff"
  accent-rust: "#cb8b6a"
  accent-plum: "#825562"
  accent-navy: "#2c5290"
  error: "#a91101"
  success: "#6cc04a"
  warning: "#f79009"
typography:
  display-xl: {fontFamily: "Kipling, sans-serif", fontSize: "64px", fontWeight: 700, lineHeight: 1.125, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Kipling, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.166, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Kipling, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.43, letterSpacing: "0px"}
  caption: {fontFamily: "Roboto Mono, monospace", fontSize: "12px", fontWeight: 400, lineHeight: 1.33, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.4, letterSpacing: "0.2px"}
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
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  swatch-selector:
    size: "{spacing.lg}"
    rounded: "{rounded.full}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    unavailableOverlay: "{colors.muted}"

## Components
**button-primary**: The main add-to-cart/checkout call-to-action, using the teal accent color observed as the site's own hover/link token, promoted to a solid fill for primary actions. Proposed as the dominant CTA treatment; actual production button color not directly screenshotted.

**button-secondary**: An outlined ink-on-white variant for tertiary actions like "View Details" or filter toggles, following the same button typography and radius tokens as the primary button. Hover/active states are proposed, not observed.

**text-input**: Used for search, email capture (e.g., membership signup), and account forms. Border uses the explicitly observed light-border color; focus-state ring color is proposed as the primary teal, not confirmed in evidence.

**nav-bar**: Represents the persistent top utility/category navigation implied by the extensive menu text (New, Handbags, Backpacks, Luggage, Accessories, Sale, Outlet). Sticky behavior and the promo-bar height variable are referenced in CSS custom properties, but exact positioning was not visually verified.

**product-card**: A grid tile showing product image, name, price, and rotating color swatches, matching the repeated "+N color available" pattern seen throughout the page text. Card background uses a warm off-white surface tone distinct from pure white to lift product photography.

**hero**: A full-width promotional banner pattern (e.g., "$29.99 MINI BAG MUST-HAVES", "TIME FOR A FALL GETAWAY") using the largest display typography token. Background tone is proposed as a soft neutral rather than a hard white, pending confirmation.

**footer**: Inverted dark panel carrying legal/relevant links (FAQ, Return Policy, Size Guide) seen in the source text. Ink-background/white-text treatment is proposed for contrast; not confirmed from supplied CSS beyond palette availability.

**badge**: A small pill label for sale/outlet flags ("UP TO 50% OFF", "NEW") and stock-status indicators. Red badge coloring pulls from the observed alert-red hex; actual promotional badge styling on-site not directly inspected.

**search**: A rounded search field in the header, inferred from the "Search" navigation entries; pill radius and soft-surface background are proposed conventions rather than measured values.

**swatch-selector** (category-specific): Given the heavy repetition of per-product color swatches ("Black Noir," "Copper Glimmer," "Grape Wine Metallic," etc.), a dedicated round swatch component is proposed for color selection on PDP/PLP cards, with a muted overlay treatment for "unavailable" colors as referenced in the source text ("Pure Alabaster color is unavailable").

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width      | Layout notes (proposed) |
|-----------|------------|--------------------------|
| mobile    | 0–639px    | Single-column product grid, collapsed hamburger nav, stacked hero text |
| tablet    | 640–1023px | 2–3 column product grid, condensed nav with overflow menu |
| desktop   | 1024–1439px| Full mega-menu nav, 4-column product grid |
| wide      | 1440px+    | Max-width content container, 4–5 column grid |

Touch targets should be at minimum 44×44px for nav and swatch controls. The mega-menu (implied by the deep category list: Handbags, Backpacks, Luggage, Accessories, Collabs, Personalization, Gifts, Sale, Outlet) is expected to collapse into an accordion drawer below tablet width. None of this was directly observed in rendered layout; it is a standard e-commerce pattern applied to the evidence provided.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Extraction is static (CSS + text only); no rendered screenshots, computed layout, or interaction states (hover, focus, active, error) were observed.
- The numeric spacing scale is entirely inferred — the source CSS only exposes named custom-property references (e.g., `--spacing-400`, `--spacing-700`) without resolving pixel values, so the spacing token set above is a proposed convention, not extracted data.
- `rounded.lg` (16px) is not directly present in the observed radius tokens (which stop at 8px plus a `100%` full token); it is inferred to complete a conventional scale.
- Body/caption font sizes (16px/14px/12px) are proposed defaults; only display/heading sizes and the 20px button type size were explicitly present in evidence.
- The teal `#004b48` is confirmed only as a hover/link state color in the site's own CSS variables, not confirmed as an official "brand primary" — its promotion to primary button color here is an inferred design decision.
- Accent colors (rust, plum, navy) are sampled from rotating product-swatch hexes in page text and may not represent a stable brand palette season-over-season.
- Custom "Kipling" webfont availability, licensing, and full weight range beyond the observed 700 (Bold) are not verified.
- Mobile/tablet navigation collapse behavior, cart drawer, and search overlay patterns are conventional e-commerce assumptions, not confirmed from this evidence.
