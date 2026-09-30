---
version: alpha
name: "Carlotta Films"
source_url: "https://laboutique.carlottafilms.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A Parisian film boutique where a deep, ink-black canvas (#1c1d1d) meets a warm, aged-gold accent (#a26b25) — the kind of gold you find on a vintage movie-poster frame, not a luxury brand. The site breathes cinema history through a restrained palette: the primary action color is a confident, archival blue (#006fcf) that recalls old Criterion menus, while body text sits in a soft charcoal (#3d4246) on a pale, almost mint-tinged off-white (#eff5f5) that reads as aged paper rather than sterile white. Typography leans into serif authority — Big Caslon and Bodoni MT for display headings, Georgia for body, Helvetica and Myriad for utilitarian navigation — creating a deliberate tension between scholarly film-text and functional e-commerce. Cards use generous {rounded.sm} corners, buttons are pill-shaped at {rounded.full}, and the entire layout is built on a generous {spacing.section} rhythm that gives each film product room to breathe like a gallery wall. The checkout flow introduces a secondary palette of payment-brand colors (Klarna pink, PayPal blue, CB silver) that clash intentionally with the editorial tone — a reminder that this is a shop, not a museum. The overall effect is a quiet, serious, cinephile space where the gold accent never overwhelms and the blue button is the only thing that asks you to buy.

colors:
  primary: "#006fcf"
  primary-active: "#005bb0"
  primary-disabled: "#b0d4f0"
  ink: "#1c1d1d"
  body: "#3d4246"
  muted: "#5f6368"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#eff5f5"
  canvas: "#eff5f5"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gold-accent: "#a26b25"
  gold-accent-light: "#d4a76a"
  dark-surface: "#343535"
  dark-muted: "#404242"
  error: "#eb001b"
  success: "#34a853"
  warning: "#fbbc04"

typography:
  display-xl:
    fontFamily: "'Big Caslon', 'Bodoni MT', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Big Caslon', 'Bodoni MT', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Big Caslon', 'Bodoni MT', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Cardo', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Cardo', Georgia, serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica, 'Myriad', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-uppercase:
    fontFamily: "Helvetica, 'Myriad', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "Helvetica, 'Myriad', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Oswald', Helvetica, 'Myriad', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Oswald', Helvetica, 'Myriad', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  link:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Oswald', Helvetica, 'Myriad', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
  full: 9999px

spacing:
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
  button-gold-accent:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-gold-accent-active:
    backgroundColor: "{colors.gold-accent-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
  nav-link-item:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
  nav-link-item-active:
    backgroundColor: transparent
    textColor: "{colors.gold-accent}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "2px solid {colors.gold-accent}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "2/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 48px
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.gold-accent}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-banner-accent:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-md}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.sm}"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  filter-dropdown-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
    border: "2px solid {colors.primary}"
  pagination-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 36px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline}"
  cart-total:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a pill-shaped button in archival blue (#006fcf) with white uppercase Oswald text. On hover, it deepens to `{colors.primary-active}` (#005bb0). When disabled, it fades to a pale blue `{colors.primary-disabled}` (#b0d4f0) with white text, signaling non-interactivity without visual noise.

**`button-secondary`** — An outlined variant for secondary actions like "Add to Wishlist" or "View Details." It uses a transparent background with a 2px solid `{colors.ink}` border and dark text. On hover or active state, the background fills with `{colors.ink}` and text flips to `{colors.canvas}`, creating a satisfying inversion.

**`button-gold-accent`** — A special accent button reserved for premium actions like "Pre-order Collector's Edition" or "Explore Criterion." It uses the warm gold `{colors.gold-accent}` (#a26b25) as background. On hover, it lightens to `{colors.gold-accent-light}` (#d4a76a) and text shifts to `{colors.ink}`, mimicking the patina of aged brass.

### Navigation
**`nav-bar`** — A fixed top bar in deep ink (#1c1d1d) that spans the full viewport width. Navigation links use uppercase Oswald at 13px with 1px letter-spacing, rendered in white. The active page is indicated by a subtle gold underline (`{colors.gold-accent}`) and gold text, creating a quiet wayfinding system that doesn't compete with the product content.

**`nav-link-item`** — Individual navigation links with generous horizontal padding (`{spacing.md}`) for comfortable tap targets. The active state uses a 2px gold bottom border and gold text, while inactive links remain white. No background change on hover — the brand trusts the gold accent to do the signaling.

### Cards
**`product-card`** — The primary content container for film listings, a white card on the pale `{colors.canvas}` background. Each card holds a 2:3 aspect ratio image (the classic film-poster proportion) with `{rounded.sm}` corners, a serif title below, and a body-text price. A gold badge can be overlaid on the image for "New Release" or "Exclusive" labels.

**`product-card-badge`** — A small gold pill (`{colors.gold-accent}`) with white uppercase text, positioned absolutely over the top-left corner of the product image. Uses tight padding (2px 8px) and `{rounded.xs}` for a subtle, non-distracting label.

### Forms
**`text-input`** — Standard text input fields for search, checkout, and account forms. A white background with a light gray border (`{colors.hairline}`) and 12px internal padding. On focus, the border thickens to 2px and shifts to `{colors.primary}` blue. Error states use a 2px red border (`{colors.error}`) with no additional icon — the color change alone signals the issue.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a white background and gray border, designed to sit in the header or hero area. On focus, the border becomes a 2px blue ring. The pill shape contrasts with the card's `{rounded.sm}` corners, giving the search field a distinct, friendly identity.

**`filter-dropdown`** — Dropdown selectors for sorting and filtering the film catalog (by director, year, format). A compact 40px height with `{rounded.sm}` corners and a gray border. The active state uses a 2px blue border to match the text-input focus pattern.

### Footer
**`footer`** — A full-width footer in deep ink (#1c1d1d) with white body text and muted gray links. Link hover states shift to `{colors.gold-accent}`, echoing the navigation's active indicator. The footer uses `{spacing.section}` vertical padding to match the generous rhythm of the rest of the site.

### Hero
**`hero-banner`** — A large, immersive banner for featured films or collections. Uses the ink background with white serif display text. The `{spacing.section}` vertical padding and 400px minimum height create a dramatic entry point. An optional gold accent block (`{colors.gold-accent}`) can be used for callout text like "New Arrivals" or "Limited Edition."

### Pagination
**`pagination-button`** — Small, square-ish buttons for page navigation at the bottom of the catalog. Default state is a white background with gray text. The active page uses the primary blue background with white text, creating a clear visual anchor for the user's current position.

### Cart
**`cart-item`** — A simple row in the shopping cart, with a white background and a bottom border (`{colors.hairline}`) separating items. Uses `{spacing.base}` vertical padding for comfortable spacing. The `cart-total` section uses a soft gray background (`{colors.surface-soft}`) to visually separate the summary from the item list.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger menu; hero-banner reduces to 300px min-height; search-bar moves below hero; footer links stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows top-level links only; hero-banner maintains 400px height; search-bar remains in header; footer uses two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar visible; hero-banner at full height; search-bar in header; footer uses four-column layout |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; hero-banner may include parallax or full-bleed imagery; footer remains four-column with wider gutters |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for comfortable touch interaction on mobile.
- Nav-link items use `{spacing.md}` (12px) horizontal padding to ensure adequate tap area.
- Product cards have a minimum tap area of 48x48px for the "Add to Cart" button overlay.
- Filter dropdowns and pagination buttons maintain 40px height to meet touch-target guidelines.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer. The drawer uses the same `{colors.ink}` background and `{colors.gold-accent}` active indicators.
- The search bar collapses from a full-width pill to a compact icon-button that expands on tap.
- The product grid collapses from 3–4 columns to a single column, with cards stacking vertically.
- The footer collapses from a multi-column layout to a single column, with links stacked and section headers as accordion toggles.
- The hero banner reduces its minimum height and may hide secondary text to prioritize the headline and primary CTA.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states for all components** were not reliably extracted from the live site. Hover colors for buttons, links, and cards are inferred from common patterns (darkening primary, lightening gold, underlining links) but may not match the exact implementation.
- **Error and validation styling** for forms (beyond the red border) was not observed. Error messages, icons, and inline validation patterns are assumed based on e-commerce conventions.
- **Dark mode** is not supported by the current site. The palette is designed for a light background (`{colors.canvas}`) and dark text (`{colors.ink}`), with no dark-mode tokens defined.
- **Sub-brand or collection-specific palettes** (e.g., "Criterion Collection" or "Carlotta Signature") were not extracted. The gold accent (`{colors.gold-accent}`) may be used for premium labels, but dedicated sub-brand colors are unknown.
- **Typography scale** is inferred from the extracted font families and common e-commerce sizes. The exact `fontSize`, `fontWeight`, and `lineHeight` values for each token are best-guess approximations based on the brand's editorial tone.
- **Animation and transition durations** were not extracted. Hover transitions, page-load animations, and micro-interactions (e.g., card hover lift, button press) are not defined.
- **Checkout-specific styling** (Shopify Pay button, Klarna badge, Afterpay banner) uses external payment-provider colors that clash with the brand palette. These are not included in the design system tokens but are noted as intentional visual breaks.
- **Accessibility tokens** (focus rings, high-contrast mode, screen-reader-only text) are not defined. The primary blue (`{colors.primary}`) may not meet WCAG AA contrast ratios on all backgrounds — this should be verified.
