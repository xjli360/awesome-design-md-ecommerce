---
version: alpha
name: "The Mysterious Bookshop"
source_url: "https://www.mysteriousbookshop.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A narrow, wood-paneled bookstore in Tribeca that has been selling crime, mystery, and suspense fiction since 1979, and its digital storefront mirrors that same sense of curated discovery. The palette is deliberately restrained — #dedede as a warm, paper-like canvas and #121212 as a deep, ink-black text color — with no bright accent colors to distract from the book covers themselves. The site trusts typographic hierarchy and generous whitespace over decorative elements, letting the product photography (jacket art, author photos) provide all the visual drama. Navigation is minimal: a sticky top bar with the shop's name, a search icon, and a cart icon, plus a dropdown menu for categories like "First Editions," "Signed Copies," and "Mystery & Crime." Product cards are simple — a cover image, title, author, and price — with no badges, no ratings, no social proof. The checkout flow uses Shopify's default widgets, which introduce a brief flash of green (#5c6ac4) and blue (#007bff) that feels slightly foreign against the otherwise monochrome site. The overall mood is that of a serious, well-stocked independent bookstore that happens to also sell online: no pop-ups, no countdown timers, no urgency tactics. Just books, organized by genre and rarity, with a shipping policy that promises careful packaging.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#6a6a6a"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#6a6a6a"
  muted-soft: "#9a9a9a"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-book-cover-border: "#dedede"
  accent-sale: "#c13515"
  accent-signed: "#121212"

typography:
  display-xl:
    fontFamily: "'Times New Roman', Georgia, 'Palatino Linotype', 'Book Antiqua', Palatino, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "'Times New Roman', Georgia, 'Palatino Linotype', 'Book Antiqua', Palatino, serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Times New Roman', Georgia, 'Palatino Linotype', 'Book Antiqua', Palatino, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    textColor: "{colors.accent-sale}"
  badge-signed:
    backgroundColor: "{colors.accent-signed}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-first-edition:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  search-icon:
    textColor: "{colors.ink}"
    height: 24px
  cart-icon:
    textColor: "{colors.ink}"
    height: 24px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} 0"
    borderTop: "1px solid {colors.hairline-soft}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.md}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  collection-grid:
    gap: "{spacing.base}"
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    textColor: "{colors.ink}"
    fontWeight: 600
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 8px 12px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  checkout-button-active:
    backgroundColor: "{colors.primary-active}"

## Components

### Buttons
**`button-primary`** — A solid black rectangle with white uppercase text, used for primary actions like "Add to Cart" and "Checkout." The sharp corners (`{rounded.none}`) and condensed letter-spacing give it a no-nonsense, literary feel — like the spine of a hardcover book. On hover, the background deepens to pure black (`{colors.primary-active}`). The disabled state uses a medium gray (`{colors.primary-disabled}`) to indicate inactivity without visual noise.

**`button-secondary`** — An outlined button with a white fill and black text, used for secondary actions like "Continue Shopping" or "View Details." The 1px hairline border (`{colors.hairline}`) keeps it visually subordinate to the primary button. On hover, the background shifts to a soft gray (`{colors.surface-soft}`) and the border darkens to ink.

### Navigation
**`nav-bar`** — A fixed 64px white bar at the top of every page, separated from the content by a thin `{colors.hairline-soft}` border. The shop name sits on the left in a serif display font; a search icon and cart icon sit on the right. Category links (First Editions, Signed Copies, etc.) appear in a dropdown menu triggered by a hamburger icon on mobile, or as a horizontal strip on desktop. Active nav links are indicated by a 2px black underline.

**`nav-link`** — Sans-serif, 14px, medium weight, with 8px horizontal padding. The active state adds a 2px solid black underline, creating a clear but understated wayfinding signal.

### Product Cards
**`product-card`** — A minimal, borderless card consisting of a 3:4 aspect ratio book cover image, followed by the title in a serif 18px bold, the author in muted 14px sans-serif, and the price in 16px semibold. There is no background fill, no shadow, no border — the card is just the image and text stacked vertically. Sale prices appear in a deep rust red (`{colors.accent-sale}`). Signed copies and first editions are flagged with small black or white badges (`{badge-signed}`, `{badge-first-edition}`) positioned at the top-left corner of the cover image.

**`badge-signed`** — A small, solid black rectangle with white uppercase text, used to denote author-signed copies. The sharp corners and condensed tracking match the button style.

**`badge-first-edition`** — Identical in form to `badge-signed`, but with a black background and white text. Used to denote first-edition copies.

### Forms
**`text-input`** — A white input field with a 1px `{colors.hairline}` border and no border-radius, used for search, email signup, and checkout fields. On focus, the border switches to `{colors.ink}`, providing a clear but subtle focus indicator. Padding is 10px vertical, 16px horizontal, with 16px body text.

**`filter-dropdown`** — A white dropdown with a 1px hairline border, used on collection pages to sort by price, author, or publication date. The typography matches `{typography.body-sm}`.

### Footer
**`footer`** — A light gray (`{colors.surface-soft}`) section at the bottom of every page, separated from the main content by a 1px `{colors.hairline-soft}` border. Contains links to About, Shipping, Returns, and Contact pages, plus a copyright notice. All links are `{colors.muted}` by default and darken to `{colors.ink}` on hover.

### Hero Section
**`hero-section`** — A full-width white section at the top of the homepage, featuring the shop's name in a large serif display font and a subtitle in muted body text. No background image, no carousel, no animation — just typography and whitespace.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero text reduces to 22px; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible as horizontal strip; hero text at 28px |
| Desktop | 1128–1440px | Three-column product grid; full nav with category dropdowns; hero section with 64px vertical padding |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero section centered with max-width 1200px |

### Touch Targets
- All buttons and interactive elements are at least 44px tall (meeting WCAG 2.1 minimum).
- Search and cart icons are 24px with 12px padding, creating a 48px touch target.
- Nav links have 8px horizontal padding and 44px minimum touch height.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu that opens a full-screen overlay with category links, search, and cart.
- The product grid collapses from 4 columns on wide screens to 1 column on mobile.
- The footer collapses from a 3-column layout on desktop to a single stacked column on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were extractable from the live site; the typography block uses educated guesses based on common bookstore ecommerce patterns (serif for display, sans-serif for body). Actual fonts may differ.
- Only two hex colors were extracted (#dedede, #121212); the remaining colors in the palette are inferred from common Shopify bookstore patterns and may not match the live site exactly.
- No hover, focus, or active states could be extracted for any component; all state variants are best-guess implementations.
- No error styling (form validation, 404 pages, empty states) could be extracted.
- No dark mode support was detected.
- No animation or transition timing data was extractable.
- The checkout flow uses Shopify's default widgets, which may introduce colors (#5c6ac4, #007bff) that are not part of the brand's design system.
- No social media icon colors or placement could be reliably extracted.
- No sub-brand or seasonal palette variations were detected.
