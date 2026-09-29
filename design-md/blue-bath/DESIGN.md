---
version: alpha
name: "Blue Bath"
source_url: "https://bluebath.com"
captured_at: "2026-09-29T04:07:14.896177+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Blue Bath is a Los Angeles–based e-commerce retailer of kitchen and bathroom
  fixtures — farmhouse sinks, faucets, freestanding tubs, vanities, and
  fixtures for brands like ALFI, EAGO, Whitehaus, and BOCCHI. The observed
  CSS defines a --global-color of #0056B3 as the site's core brand blue,
  reused across page titles, link hovers, and interactive accents, alongside
  a deeper navy (#033871) used for mega-menu headers and "view all" call-outs.
  Body copy is set in a neutral dark gray (#222/#333) on white, a restrained
  palette typical of a dense product-catalog storefront. Sale pricing uses a
  burnt-orange (#C13A00), distinct from a separate warm-orange CSS variable
  set (#f4511e/#ff7043) that appears defined but whose exact UI role is not
  confirmed in the supplied evidence — it is treated here as a secondary
  accent, inferred rather than observed in context.
  Typography is anchored on "Geist" for body copy, controls, and most
  headings, with "Oswald" observed specifically on product page titles,
  giving a condensed, technical accent to key headers. Buttons use a light
  gray fill (#f2f2f2) with a thin #cdcdcd border, a utilitarian pattern
  consistent with a catalog/checkout-first retail experience rather than a
  lifestyle-brand aesthetic. All spacing, radius, and unmeasured type sizes
  below are proposed and labeled as inferred to fit this observed system.

colors:
  primary: "#0056B3"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#cdcdcd"
  surface-soft: "#f8f9fc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-price: "#C13A00"
  accent-orange: "#f4511e"
  navy-deep: "#033871"
  link-hover: "#0459B6"
  border-muted: "#e2e2e2"
  old-price: "#aaaaaa"
  control-fill: "#f2f2f2"
typography:
  display-xl: {fontFamily: "'Geist', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Oswald', sans-serif", fontSize: 29px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Geist', Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Geist', Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.42857143, letterSpacing: 0px}
  body-sm: {fontFamily: "'Geist', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.42857143, letterSpacing: 0px}
  caption: {fontFamily: "'Geist', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Geist', Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.6rem, letterSpacing: 0.2px}
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.control-fill}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
  mega-menu:
    backgroundColor: "{colors.surface-soft}"
    headerBackground: "{colors.navy-deep}"
    headerTextColor: "{colors.on-primary}"
    hoverBackground: "{colors.border-muted}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    titleHoverColor: "{colors.link-hover}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.accent-price}"
    oldPriceColor: "{colors.old-price}"
    padding: "{spacing.md}"
  price-badge:
    backgroundColor: "{colors.accent-price}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.link-hover}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.xxl} {spacing.lg}"
  trust-badge:
    backgroundColor: "{colors.canvas}"
    iconColor: "{colors.primary}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.ink}"
    supportTypography: "{typography.caption}"
    supportColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    iconColor: "#2563EB"
    suggestionBackground: "{colors.canvas}"
    suggestionHoverBackground: "{colors.surface-soft}"
    suggestionDivider: "#f0f2f8"
    typography: "{typography.body-sm}"

## Components

**button-primary** — Uses the site-wide `--global-color` brand blue (#0056B3) as its fill with white text; proposed for primary calls-to-action such as "Add to Cart" or "View All." Hover state is not confirmed in evidence and is treated as inferred (darkening toward `#333`, per the observed `.button-primary:hover` rule).

**button-secondary** — Directly reflects the observed default `button` styling: light gray `#f2f2f2` fill, `#cdcdcd` border, dark gray text, with confirmed hover/focus states shifting to `#e2e2e2` background and `#555` text. This is the storefront's dominant control style (add-to-cart, filters, quantity steppers).

**text-input** — Proposed pattern for search and form fields, inferring a white background, thin hairline border, and body-md typography consistent with the retailer's utilitarian control language; exact padding and focus ring are not observed.

**nav-bar** — Proposed top navigation bar pairing the white canvas with brand-blue accents for active/hover states, based on link-hover color `#0459B6` observed on product names and the home title. Category structure (Kitchen, Bath, Farm Sinks, etc.) is evidenced in page text but visual chrome is inferred.

**mega-menu** — Modeled on the confirmed `--dlx-*` CSS variables: a deep navy header (`#033871`) with white text, a soft off-white body background (`#f8f9fc`), and a light-blue hover state (`#eef2fb`, mapped here to `border-muted` for token economy). This corresponds to the extensive Kitchen/Bath dropdown taxonomy in the evidence.

**product-card** — Proposed layout for the "Top Rated Best Sellers" and category grids seen in the page text (e.g., EAGO toilets, Whitehaus sinks). Title color and hover state are directly observed (`.product-list-name a` black, hover `#0459B6`); price/old-price colors are drawn from confirmed `--dlx-price` (#C13A00) and `--dlx-old-price` (#aaaaaa) variables.

**price-badge** — Small discount-percentage tag (e.g., "-30%", "-47%") inferred from the repeated markdown-style discount patterns in page text; color reuses the confirmed accent-price token since no distinct badge color was supplied.

**hero** — Proposed banner treatment for the homepage's "Explore Kitchen, Bath & Farmhouse Fixtures" intro copy, using the soft surface background and the observed `.title-home h1` blue (`#0459B6`) for the headline.

**trust-badge** — Category-appropriate component for the four value props shown in evidence ("Price Match + 5%," "Free US Shipping," "Seamless Canada Shipping," "Authorized Brand Dealer") — common in fixtures/appliance retail to reassure buyers on authenticity and freight logistics for heavy items like tubs and vanities. Visual treatment is proposed.

**footer** — Proposed dark navy footer reusing `navy-deep` for brand consistency with the mega-menu header; no footer-specific CSS was supplied, so structure and link styling are inferred.

**search** — Directly reflects observed `#search_mini_form button` (blue icon `#2563EB` on transparent background) and `.dlx-product-item` suggestion styling (white background, `#f0f2f8` divider, subtle hover transition), used for the autosuggest search dropdown.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | < 640px | Single-column product grids; mega-menu collapses to accordion/drawer; touch targets ≥ 44px. |
| Tablet | 640–1023px | 2-column product grids; condensed top nav with icon-only search/cart. |
| Desktop | 1024–1439px | Full mega-menu on hover; 3–4 column product grids. |
| Wide | ≥ 1440px | 4–5 column grids; max content width constrained, generous `{spacing.section}` gutters. |

This table is a proposed recommendation based on typical catalog-retailer patterns and is **not** measured from live site behavior, which was not observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no live rendering, computed layout, animation, or JavaScript-driven interaction (e.g., mega-menu open/close, cart drawer behavior) was observed.
- Two conflicting body text colors were present in source CSS (`#222` on the root `body` rule vs. `#333` in a merged bundle); both are retained as `ink` and `body` respectively rather than resolved definitively.
- The `--c-orange` / `--c-orange2` and `--c-blue-mid` / `--c-blue-lite` CSS custom properties are defined in evidence but their applied UI context was not confirmed; `accent-orange` is included as inferred-only.
- Font family list includes several names (Inter, Open Sans, Roboto, Oswald, Helvetica Neue) present in the raw evidence; only "Geist" (body/headings) and "Oswald" (page titles) had confirmed selector-level CSS rules and are used in the typography scale. Licensing and self-hosting/CDN status of "Geist" were not verified.
- All spacing values and most typography sizes beyond the two directly observed rules (`.page-title` at 29px, body at 16px/1.4rem) are proposed estimates for a coherent scale, not measurements from rendered layout.
- Border-radius values are proposed; the one confirmed data point (`border-radius:3px` on compare/wishlist buttons) was rounded to the nearest token (`rounded.sm` = 4px) for system consistency.
- Mobile/touch interaction patterns, breakpoint pixel values, and collapse behavior are recommendations only, not observed from the source.
