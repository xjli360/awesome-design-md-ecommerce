---
version: alpha
name: "Biblio"
source_url: "https://www.biblio.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, quiet marketplace for used and rare books, built on a single strong neutral — #313131 — that anchors every headline, body link, and navigation label against a warm off-white canvas. The brand trusts the book cover, not the interface: product photography occupies the full width of the listing card, and typography stays in the background with a system-native stack of -apple-system, BlinkMacSystemFont, Segoe UI, and Roboto at modest weights. There is no hero animation, no gradient, no brand illustration — the design is a library shelf, not a storefront window. Search sits in a full-width bar with a soft inner shadow and a pill-shaped submit button (`{rounded.full}`), and category navigation runs as a horizontal scroll of text-only links under a thin hairline. The footer collapses into a dense column of links, contact info, and payment badges, all set in `{colors.muted}` gray. The only color beyond the neutral scale is the occasional Amazon-orange affiliate badge and the green of a "Add to Cart" button, both inherited from third-party checkout flows rather than brand choice. The extraction returned only one distinctive hex — #313131 — and a generic system font stack, so the system is defined by what it does not do: no brand color, no custom typeface, no decorative border. It is a functional, text-first marketplace that treats every pixel as a cost.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#8c8c8c"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#6e6e6e"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e6e6e6"
  canvas: "#fafafa"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#313131"
  link-hover: "#1a1a1a"
  badge-sold: "#d32f2f"
  badge-rarity: "#1976d2"
  star-rating: "#f5a623"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill-search:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    boxShadow: "inset 0 2px 4px rgba(0,0,0,0.05)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
    padding: "0 {spacing.base} {spacing.sm}"
  badge-sold:
    backgroundColor: "{colors.badge-sold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-rarity:
    backgroundColor: "{colors.badge-rarity}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  category-tab-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.ink}"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Sign Up". Renders as a solid dark rectangle (`{colors.primary}`) with white text, `{rounded.sm}` corners, and 44px height. On hover, shifts to `{colors.primary-active}` (#1a1a1a). Disabled state uses `{colors.primary-disabled}` (#8c8c8c) with no shadow.

**`button-secondary`** — Used for "View Details", "Save for Later", and secondary form actions. White background with a 1px `{colors.hairline}` border and `{colors.ink}` text. Hover state darkens the border to `{colors.muted}`. Same 44px height as primary for alignment in forms.

**`button-tertiary-text`** — A text-only button for "Cancel", "Clear Filters", and inline actions. No background or border. Hover state adds a subtle underline. Uses `{typography.button-md}` weight 600.

**`button-pill-search`** — The submit button inside the search bar. A fully pill-shaped (`{rounded.full}`) dark button at 40px height, positioned at the right edge of the search input. Uses `{typography.button-sm}` for compact sizing.

### Cards
**`product-card`** — The core listing card for a used or rare book. A white rectangle with a 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners. The book cover image fills the full card width with no padding. Title and price sit below the image with `{spacing.sm}` padding on sides and `{spacing.base}` on bottom. On hover, the border shifts to `{colors.hairline}` and a subtle box shadow appears. No badge by default — badges only appear for "Sold" or "Rare" items.

**`badge-sold`** — A small red (`{colors.badge-sold}`) pill badge overlaid on the top-left corner of the product image. Uses `{typography.badge}` (11px uppercase) with `{rounded.xs}` corners and tight padding.

**`badge-rarity`** — A blue (`{colors.badge-rarity}`) badge for first editions, signed copies, or other rare designations. Same shape and typography as `badge-sold`.

### Navigation
**`nav-bar`** — A 60px white bar with a 1px `{colors.hairline-soft}` bottom border. Contains the logo on the left, a horizontal list of text-only category links in `{typography.nav-link}`, and a search icon on the right. No background color change on scroll.

**`nav-link-active`** — The active category link gets `{colors.primary}` text and a 2px `{colors.primary}` bottom border. Inactive links remain `{colors.ink}` with no underline.

**`category-strip`** — A secondary navigation row below the main nav, used for subcategories (Fiction, Non-Fiction, Rare, etc.). Text-only links in `{typography.button-sm}` with `{colors.muted}` color. Active tab uses `{colors.primary}` text and a 2px bottom border. Scrolls horizontally on mobile.

### Forms
**`text-input`** — Standard text input for search, email, and address fields. White background, 44px height, `{rounded.sm}`, 1px `{colors.hairline}` border. Focus state swaps to a 2px `{colors.primary}` border with no outline. Placeholder text in `{colors.muted-soft}`.

**`search-bar`** — The primary search field on the homepage and header. Same shape as `text-input` but with an inset box shadow (`0 2px 4px rgba(0,0,0,0.05)`) for a slight recessed look. The `button-pill-search` sits inside the right edge.

### Footer
**`footer`** — A dense, text-heavy footer on a `{colors.surface-soft}` background. Links are stacked in columns (About, Help, Browse, My Account) with `{typography.link}` in `{colors.muted}`. Hover shifts to `{colors.ink}`. The bottom row contains payment method icons (Visa, Mastercard, PayPal) and a copyright line in `{typography.caption-sm}`. No brand color accent — all text is neutral.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; footer links stack vertically; search bar moves below logo |
| Tablet | 744–1128px | Two-column product grid; category strip scrolls horizontally; footer columns in 2x2 layout |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; footer in 4 columns |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 4 columns; extra whitespace on sides |

### Touch Targets
- All buttons and clickable elements minimum 44px height (WCAG AAA for touch)
- Nav links minimum 40px tap area
- Search bar submit button 40px × 40px minimum
- Category strip links minimum 36px tap area with 8px gap between items

### Collapsing Strategy
- Main navigation collapses to a hamburger icon at < 744px; the hamburger opens a full-screen overlay menu
- Category strip becomes a horizontal scroll at < 744px with no overflow indicator
- Footer columns collapse to a single vertical stack at < 744px
- Product grid goes from 4 columns (wide) to 1 column (mobile) with no intermediate break for 3 columns
- Search bar moves from the header row to below the logo on mobile, full-width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one distinctive hex color (#313131) was extracted from the live site. The brand may use additional accent colors (e.g., for sale badges, ratings, or affiliate links) that were not captured due to framework filtering or low frequency in the DOM.
- No custom font family was found; the site uses a system font stack. The brand may have a custom typeface that is loaded via JavaScript or a CDN that was not detected during extraction.
- Hover, focus, and active states for all components are inferred from common patterns and may not match the exact live implementation.
- Error state styling for form inputs (red border, error message typography) was not extracted.
- Dark mode is not supported; the site appears to be light-mode only.
- The "Add to Cart" button color may vary by book listing (e.g., Amazon affiliate integration) and was not captured as a brand token.
- Star rating color (#f5a623) is inferred from common e-commerce patterns; the actual color on the site may differ.
- No animation or transition durations were extracted; all motion is assumed to be 200ms ease-in-out where applicable.
- The site uses a Cloudflare challenge page ("Just a moment...") which may have blocked extraction of deeper page content and styles.
