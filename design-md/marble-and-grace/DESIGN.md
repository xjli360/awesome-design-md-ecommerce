---
version: alpha
name: "Marble and Grace"
source_url: "https://marbleandgracestudios.com"
captured_at: "2026-09-28T09:32:47.518103+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Marble & Grace Studios is a Shopify-hosted storefront blending a photography
  portfolio with handmade soaps, wax melts, candles, and engraved keepsakes.
  The evidenced theme (Shopify Dawn-derived) exposes a neutral base of white
  (#ffffff) and near-black (#121212) for foreground/background, with a
  documented button/link color of rgb(16,113,15)—approximated here to the
  nearest supplied swatch, #12370b, a deep forest green, since no exact hex
  match exists in the observed palette. Supporting grays (#333333, #666666,
  #dddddd, #eeeeee) come directly from the CSS custom properties and utility
  classes. Soft natural tones (#f4f7f3, #a8b5a2, #bdddbd) and a warm gold
  (#fbcd0a) are present in the palette and are proposed here as secondary
  "handmade craft" accents for candle/soap merchandising, though their exact
  on-site usage is not confirmed. Typography draws on the observed font stack:
  Nunito Sans for body copy (matching the .text-body rule's letter-spacing and
  line-height), Playfair Display for headings, and Playball reserved as an
  inferred script accent for taglines or logotype treatment. All sizes beyond
  the literal 1.5rem/0.06rem body rule are proposed, since root font-size was
  not supplied.

colors:
  primary: "#12370b"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f4f7f3"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  accent-gold: "#fbcd0a"
  sage: "#a8b5a2"
  sage-light: "#bdddbd"
  badge-border: "#121212"
  badge-background: "#ffffff"
typography:
  display-xl: {fontFamily: "'Playfair Display', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Playfair Display', serif", fontSize: 34px, fontWeight: 600, lineHeight: 1.25, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Playfair Display', serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Nunito Sans', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0.6px}
  body-sm: {fontFamily: "'Nunito Sans', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.4px}
  caption: {fontFamily: "'Playball', cursive", fontSize: 18px, fontWeight: 400, lineHeight: 1.3, letterSpacing: "0px"}
  button-md: {fontFamily: "'Nunito Sans', Arial, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.6px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.xl}"
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
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-background}"
    textColor: "{colors.ink}"
    borderColor: "{colors.badge-border}"
    rounded: "{rounded.none}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  review-stars:
    backgroundColor: "{colors.canvas}"
    starColor: "{colors.ink}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    typography: "{typography.caption}"

## Components

**button-primary** — The evidenced `--color-button: 16,113,15` / `--color-button-text: 255,255,255` pairing is mapped to the closest supplied palette swatch (`#12370b`) for the "Book Your Session" and "Add to Cart" calls to action. Hover/active states darken the tone; exact hover value not observed and is proposed.

**button-secondary** — Derived from the theme's `.button--secondary` rule, which swaps foreground/background via CSS custom properties. Rendered here as an outlined variant using the primary green on a white field, appropriate for "Explore" links seen across the Photography and Craft category tiles.

**text-input** — Used for search, newsletter, and Shopify cart forms. Border and radius are proposed (no explicit input CSS was supplied) but padding follows the theme's general spacing rhythm.

**nav-bar** — Reflects the site's flat, text-based navigation (Home, Contact, Photography, Handcrafted Soaps/Wax Melts/Candles, Custom Engraved Items, Handcrafted Home Decor, Kubes Coffee, Log in, Cart). Sticky/scroll behavior is not confirmed from static CSS and is treated as proposed.

**product-card** — Maps to the observed `.product-card-wrapper .card` selector, which exposes CSS variables for border radius, border width, shadow, and text alignment without resolved values; radius is therefore set to `none` pending confirmation, with soft gray card background for shop grid items like soaps and wax melts.

**hero** — The homepage "Welcome! About Me" and seasonal "Recent Work" sections suggest a warm, editorial hero treatment. Background uses the pale sage-tinted `surface-soft` swatch to echo the natural/handmade positioning; exact hero markup and imagery cropping were not observed.

**footer** — Proposed layout using the muted sage background and small body type, consistent with the site's soft, faith-and-family brand voice; actual footer column structure not confirmed in evidence.

**badge** — Modeled on the Judge.me review widget variables (`--jdgm-border-radius: 0`, black primary/star color), reused for small labels such as "Handmade" or "New" tags on product tiles.

**search** — Rounded pill treatment is a proposed convention for Shopify Dawn-based storefronts; no explicit search-bar radius or border was present in the supplied CSS.

**review-stars** — Directly reflects the Judge.me integration variables (`--jdgm-primary-color: #000`, `--jdgm-star-color: #000`, `--jdgm-border-radius: 0`), a category-appropriate component for surfacing customer reviews on handmade soap and candle listings.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width      | Behavior (proposed)                                  |
|-----------|------------|-------------------------------------------------------|
| Mobile    | ≤ 749px    | Single-column stack; nav collapses to hamburger menu |
| Tablet    | 750–989px  | 2-column product grid; nav remains condensed          |
| Desktop   | ≥ 990px    | Full horizontal nav; 3–4 column product/craft grid    |

Touch targets should be a minimum of 44×44px for buttons and nav links, consistent with typical Shopify Dawn accessibility conventions. Mobile nav collapse and cart-drawer behavior were not observed in the supplied static CSS and are recommendations only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS custom properties, selector declarations, and page text only; no rendered screenshots, computed styles, or JavaScript-driven states were captured. The primary/link color (`#12370b`) is an approximation of the observed `rgb(16,113,15)` value, since no exact hex match exists in the supplied palette. Root `font-size` was not supplied, so all pixel equivalents for typography are proposed rather than measured. Button, input, and card border-radius values reference undefined CSS custom properties (`--buttons-radius-outset`, `--product-card-corner-radius`) whose resolved values were not present in evidence; they are therefore treated as proposed, not observed. Hover, focus, active, and error states are proposed conventions, not verified interactions. Mobile/tablet layout, navigation collapse behavior, and cart-drawer design were not observed. Availability, licensing, and webfont-loading behavior for Playfair Display, Playball, and Nunito Sans were not verified beyond their presence in the CSS font-family declarations.
