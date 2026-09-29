---
version: alpha
name: "Corona"
source_url: "https://coronatools.com"
captured_at: "2026-09-29T03:57:47.007329+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Corona Tools presents itself as a heritage American manufacturer (est. 1928) of
  professional-grade pruning, cutting, and landscaping hardware, sold through a
  Shopify-powered storefront. The observed palette centers on a strong red
  (#c8102e, with a deeper red #810a1e) that reads as the brand's primary mark
  color, paired with near-black text tones (#131112, #2e292b) and neutral grays
  (#767676, #63656a, #e4e4e4) typical of a utilitarian, trust-driven catalog
  site. A dark forest green (#00412d) and a brighter working green (#1b6109)
  appear in the palette and are inferred here as secondary "nature/garden"
  accents appropriate to the product category, though their exact UI usage was
  not confirmed in the supplied CSS. Several palette entries (#eb001b, #f79e1b,
  #ff5f00, #142fbd, #1532cb, #0071ce) correspond to standard payment-network
  logos (Mastercard, Discover, Amex, Visa) and are excluded from brand-role
  assignment. Headings use a custom "NT-font" (forced to normal weight),
  falling back to sans-serif; Poppins is present in the font stack and is
  inferred as the probable body typeface, though the live body font variable
  value was not directly observed. Inputs show explicit border-radius: 0,
  informing a squared, functional interaction style rather than a rounded,
  soft one. The interpretation favors a rugged, no-nonsense catalog aesthetic:
  bold red CTAs, dark neutral text, light gray surfaces for cards and filters,
  and green used sparingly to reinforce the gardening/outdoor category.

colors:
  primary: "#c8102e"
  primary-dark: "#810a1e"
  ink: "#131112"
  canvas: "#ffffff"
  body: "#2e292b"
  muted: "#767676"
  hairline: "#e4e4e4"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#00412d"
  accent-green-bright: "#1b6109"
  accent-gold: "#ffcb67"
  border-strong: "#cbcbcb"
typography:
  display-xl: {fontFamily: "'NT-font', sans-serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'NT-font', sans-serif", fontSize: "30px", fontWeight: 400, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'NT-font', sans-serif", fontSize: "18px", fontWeight: 400, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "'Poppins', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Poppins', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Poppins', sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.25, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Poppins', sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.4px"}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    minHeight: "40px"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlay: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  free-shipping-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xs} {spacing.base}"

## Components

**button-primary**: Solid red call-to-action ("Add to Cart", "Shop Now") using the observed brand red with white text. Square corners are used because the only observed radius value in the source CSS (on form inputs) is explicitly 0; hover/focus darkening to `{colors.primary-dark}` is proposed, not observed.

**button-secondary**: An outlined variant for lower-emphasis actions (e.g., "Learn More" links seen throughout the homepage copy). Uses the same red as text/border on a white field, keeping visual hierarchy subordinate to button-primary. All interaction states are proposed.

**text-input**: Modeled directly on the observed input rule (`border:1px solid var(--line_color)`, `min-height:40px`, `border-radius:0`, `background:none`). Hairline gray border and dark body text are inferred from the surrounding neutral palette; focus-state styling was not present in the supplied CSS and is proposed.

**nav-bar**: A light, white header bar carrying the site's category mega-menu (Pruning Tools, Long-Handled Tools, Gardening Tools, Demolition & Striking Tools, Carts & Wheelbarrows, Shop by Industry, Burgon & Ball). Structure is inferred from the page-text hierarchy; exact spacing/collapse behavior was not measured.

**product-card**: A bordered, white card intended for the catalog/collection grid implied by the product listings (e.g., "Sledge Hammer, 6 lb. Head... $69.99"). Price text is proposed to inherit the brand red per the `.product-price h6 { color: var(--price_color) }` rule pattern observed in the stylesheet, though the resolved color value itself was not directly supplied.

**hero**: A full-bleed, dark banner section matching the homepage's background-video hero ("Growing strong season after season", "PRO APPROVED SINCE 1928"). Dark ink background with white display type is inferred from the presence of background-video controls and large headline sizing tokens; no direct hero background color was confirmed.

**footer**: A dark, ink-toned footer housing contact info, policy links, and payment icons, consistent with the multi-column Quick Links/Policies/Get Connected content seen in the page text. Payment-brand marks (Visa, Mastercard, Discover, Amex) retain their own fixed logo colors and are not restyled.

**badge**: A small pill used for merchandising callouts such as "New Products" or "Pro Boron Steel." Green is chosen here as a category-appropriate, garden-adjacent accent; this role assignment is inferred, not confirmed in the CSS.

**search**: A light, bordered search field mirroring the generic text-input styling, positioned in the header per the visible "Search..." placeholder text in the page content. Dropdown/typeahead behavior was not observed.

**free-shipping-banner**: A slim announcement strip matching the observed `.header-announcement` rule (small font-size tokens, reduced padding) used for the "FREE SHIPPING ON EVERY ORDER $100 OR MORE" message. Background color is proposed as brand red to maximize visibility; the actual observed background value was not supplied.

## Responsive Behavior

This is a proposed responsive strategy, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | < 480px | Single-column stacking; nav collapses to a hamburger/drawer; announcement bar remains full-width. |
| Tablet | 480–1024px | 2-column product grids; mega-menu condenses to accordion categories. |
| Desktop | 1024–1440px | 3–4 column product grids; full horizontal mega-nav. |
| Wide | > 1440px | Content max-width container with increased gutter (`{spacing.xxl}`). |

Touch targets should be a minimum of 40px in height, matching the one measured input `min-height` value in the source CSS. Header navigation collapse, mobile drawer patterns, and swipe/carousel behavior are proposed conventions and were not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no live rendering, computed styles, or DOM interaction states were captured.
- Root custom properties like `--body_font`, `--line_color`, `--accent_color`, `--price_color`, and `--master_spacing` are referenced throughout the stylesheet but their resolved values were not included in the supplied evidence; several token mappings above (e.g., body font = Poppins, hairline = `#e4e4e4`) are therefore inferred, not confirmed.
- The custom heading typeface "NT-font" is used as observed, but its licensing, weights, and availability for reuse were not verified.
- Six palette entries (`#eb001b`, `#f79e1b`, `#ff5f00`, `#142fbd`, `#1532cb`, `#0071ce`) are standard third-party payment-network colors and were deliberately excluded from brand semantic roles.
- All rounded and spacing scale values beyond the single observed `border-radius: 0` are proposed conventions for consistency, not measured from the site.
- No hover, focus, active, error, or loading states were present in the supplied CSS; all interactive states described above are proposed.
- Mobile/tablet layout, breakpoint values, and navigation collapse behavior were not observed and are recommendations only.
