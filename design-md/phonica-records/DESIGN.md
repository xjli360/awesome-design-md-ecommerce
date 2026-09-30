---
version: alpha
name: "Phonica Records"
source_url: "https://www.phonicarecords.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record shop that treats its homepage like a crate-digging session — a dense, monochrome grid of album covers where the only color comes from the vinyl itself. The canvas is pure white (`#ffffff`), the ink is near-black (`#111111`), and the entire experience is built around letting the artwork breathe. There are no hero carousels, no lifestyle photography, no brand illustrations — just a relentless cascade of square sleeves, each one a portal to a product page that reads like a Discogs listing crossed with a zine. The typography is a single utilitarian sans-serif stack, set small and tight, with tracklists rendered in a monospaced font that whispers "I buy my records from a proper shop, not an algorithm." The only structural color is the muted gray of the top nav (`#666666`) and the hairline-thin borders (`#e0e0e0`) that separate rows without shouting. The search bar is a simple outlined rectangle (`{rounded.sm}`), not a pill — this is a shop for people who know what they want. The footer is a wall of text: shipping policies, payment icons, a mailing list signup, and a map link to the Soho store. The entire site feels like it was built by someone who loves records more than they love design trends — and that is exactly the point.

colors:
  primary: "#111111"
  primary-active: "#333333"
  primary-disabled: "#999999"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#111111"
  link-hover: "#555555"
  price: "#111111"
  badge-new: "#111111"
  badge-sale: "#cc0000"
  star-rating: "#111111"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  mono:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 32px
    width: 32px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    border-bottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.price}"
    fontWeight: 600
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  product-grid:
    gap: "{spacing.base}"
    columns: 2
    padding: "{spacing.base}"
  product-detail-title:
    typography: "{typography.display-md}"
    marginBottom: "{spacing.sm}"
  product-detail-artist:
    typography: "{typography.title-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.base}"
  product-detail-tracklist:
    typography: "{typography.mono}"
    color: "{colors.body}"
    lineHeight: 1.8
  product-detail-label:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-detail-format:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  product-detail-price:
    typography: "{typography.display-md}"
    color: "{colors.price}"
    marginBottom: "{spacing.lg}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    width: "100%"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
    border-top: "1px solid {colors.hairline}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  mailing-list-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  mailing-list-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    color: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  pagination-active:
    typography: "{typography.body-sm}"
    color: "{colors.ink}"
    fontWeight: 600
  filter-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  category-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  category-link-active:
    typography: "{typography.link}"
    color: "{colors.ink}"
    fontWeight: 600

## Components

### Buttons
**`button-primary`** — Solid black rectangle with white text, used for primary actions like "Add to Cart" and "Checkout." On hover, the background shifts to `{colors.primary-active}` (#333333). The disabled state uses `{colors.primary-disabled}` (#999999) with white text. The button has a subtle `{rounded.sm}` corner, avoiding the pill shape common in consumer brands — this is a utilitarian, no-nonsense interaction.

**`button-secondary`** — Outlined variant with a white background, black text, and a 1px `{colors.hairline}` border. Used for secondary actions like "View Details" or "Continue Shopping." Hover state adds a slightly darker border (`{colors.muted-soft}`). The `{button-tertiary-text}` variant is a bare text link with no border or background, used for inline actions like "Clear filters."

**`button-pill`** — A fully rounded pill button used sparingly, primarily for the "New In" badge or promotional call-to-action banners. Uses `{colors.primary}` background with white text and `{rounded.full}`.

### Navigation
**`top-nav`** — A 56px white bar with a thin `{colors.hairline}` bottom border. Contains the Phonica logo (text-based, left-aligned), a set of uppercase nav links (`{typography.nav-link}`), and a search icon. The active link state is indicated by a 2px black bottom border (`{nav-link-active}`). On mobile, the nav collapses into a hamburger menu.

**`nav-link`** — Uppercase, 13px, weight 600, with `{spacing.base}` horizontal padding. The active state uses a bottom border instead of a background color change, maintaining the site's minimal aesthetic.

### Search
**`search-bar`** — A simple outlined rectangle with `{rounded.sm}`, 40px height, and 8px/12px padding. The border is `{colors.hairline}` by default and shifts to `{colors.primary}` on focus. No rounded pill, no shadow — just a functional input for customers who know what they're looking for.

### Product Cards
**`product-card`** — A square, borderless container with no rounded corners. The image fills the card at a 1:1 aspect ratio (`{product-card-image}`). Below the image, the artist name appears in `{typography.body-sm}` at `{colors.muted}`, the album title in `{typography.title-sm}` at `{colors.ink}`, and the price in `{typography.body-md}` at `{colors.price}` with weight 600. A small badge (`{product-card-badge}`) can appear in the top-left corner for "New In" or "Sale" items.

**`product-grid`** — A two-column grid on mobile, expanding to 3-4 columns on tablet and desktop. The gap is `{spacing.base}`. No gutters, no padding between rows — the density is part of the aesthetic.

### Product Detail
**`product-detail-title`** — The album title in `{typography.display-md}` (22px, weight 700). The artist name sits below in `{typography.title-md}` at `{colors.muted}`. The tracklist is rendered in `{typography.mono}` (Courier New, 12px) with 1.8 line height, giving it the feel of a printed insert.

**`add-to-cart-button`** — Full-width, 44px tall, solid black with white text. Uses `{rounded.sm}`. The `{quantity-selector}` sits beside it, a simple outlined box with the same height and corner radius.

### Footer
**`footer`** — A light gray (`{colors.surface-soft}`) section with a `{colors.hairline}` top border. Contains columns for "Help," "Info," "Social," and a mailing list signup. Links are `{typography.link}` at `{colors.muted}`. The mailing list input (`{mailing-list-input}`) is a standard outlined text field paired with a small submit button (`{mailing-list-submit}`).

### Filters & Pagination
**`filter-dropdown`** — A standard select dropdown with `{rounded.sm}`, 40px height, and a `{colors.hairline}` border. Used for sorting by genre, format, or price. The `{category-link}` is a simple text link at `{colors.muted}`, with the active state at `{colors.ink}` and weight 600.

**`pagination`** — Small text links at `{typography.body-sm}` and `{colors.muted}`. The active page is `{colors.ink}` with weight 600. No fancy arrows or large touch targets — just numbers.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; footer stacks vertically; search bar moves to a dedicated overlay; product detail page stacks image above text |
| Tablet | 744–1128px | Two-column product grid; top-nav shows all links; footer displays in two rows; product detail page shows image and text side-by-side at 50/50 |
| Desktop | 1128–1440px | Three-column product grid; top-nav at full width; footer in four columns; product detail page has wider image column (60%) |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; content centered with auto margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 40px on mobile.
- Nav links have a minimum touch area of 44px x 44px on mobile (via padding).
- Product cards are fully tappable, with the entire card linking to the product detail page.
- The search icon in the top nav has a 44px x 44px touch target on mobile.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu with a slide-out drawer.
- The product grid collapses from 3-4 columns to 2 columns on tablet, and 1 column on mobile.
- The footer collapses from 4 columns to 2 columns on tablet, and 1 column on mobile.
- The product detail page collapses from a side-by-side layout to a stacked layout on mobile.
- Filter and sort controls collapse into a single "Filter & Sort" button on mobile, opening a modal overlay.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations could be extracted from the live site; the typography stack uses a generic sans-serif fallback (`'Helvetica Neue', Helvetica, Arial, sans-serif`) and a monospaced fallback (`'Courier New', Courier, monospace`). The actual brand font may differ.
- No hex colors could be extracted from the live site (the page returned a redirect). The color palette is inferred from common record-store ecommerce conventions and the brand's known minimal aesthetic.
- Hover and focus states for all components are assumed based on standard web patterns; actual brand-specific hover transitions (ease, duration) are unknown.
- Error states for forms (mailing list, search, checkout) are not defined.
- The checkout flow (cart, shipping, payment) is not included; this is likely handled by a third-party provider (Shopify, WooCommerce, etc.) with its own design system.
- Dark mode is not supported.
- The brand's logo is text-based and assumed to be in the primary font; no SVG or custom logo component is defined.
- The "New In" and "Sale" badge colors are assumed; the actual badge system may use different colors or icons.
- The product card hover state (e.g., image zoom, shadow) is not defined.
- The site may use a different grid system (e.g., CSS Grid with named areas) than the simple column layout described here.
- The mobile navigation drawer's animation, overlay color, and close button are not specified.
- The search overlay on mobile (background, animation, input size) is not defined.
