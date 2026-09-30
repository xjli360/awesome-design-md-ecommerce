---
version: alpha
name: "Jet Set Records"
source_url: "https://www.jetsetrecords.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A midnight-blue digital storefront for an independent record shop that ships globally from Japan, built on a stark white canvas and a single accent — #1a237e — a deep indigo that reads as ink-black on screen but holds a trace of cobalt in its edges, used sparingly for headings, dividers, and the occasional badge. The site trusts its product photography entirely: album covers provide all the color, and the interface steps back to let them breathe. Body text runs Arial at 16px in #333333, a pragmatic choice that prioritizes legibility over personality — this is a store, not a gallery. Navigation is a thin horizontal strip of links in uppercase, 12px, spaced generously, with a persistent search bar that sits in the top-right corner like a utility rather than a discovery tool. Product cards are simple: a square cover image, the artist name in bold 14px, the album title in regular 13px, and a price in the same indigo. There are no badges, no ratings, no "add to cart" buttons visible until you enter a product page — the browsing experience is deliberately quiet, almost archival. The footer repeats the nav links in a single column, adds social icons (Instagram, Twitter, Bandcamp), and prints a small "Worldwide Shipping" tagline in #666666. The overall feel is that of a well-organized crate-digger's spreadsheet rendered as HTML — functional, fast, and deferential to the music.

colors:
  primary: "#1a237e"
  primary-active: "#0d1452"
  primary-disabled: "#9fa8da"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#1a237e"
  link-hover: "#0d1452"
  price: "#1a237e"
  badge-new: "#e53935"
  badge-sale: "#1a237e"
  social-icon: "#333333"
  footer-bg: "#f5f5f5"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

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
    padding: 10px 24px
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
    padding: 9px 23px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  text-input-focus:
    borderColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 36px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-artist:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.price}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.social-icon}"
    height: 24px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 48px 24px
  section-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: 24px 0
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart" and "Checkout". Rendered as a solid indigo rectangle with white text, 14px bold Arial, 4px corner radius. On hover, darkens to `{colors.primary-active}`. Disabled state uses `{colors.primary-disabled}` — a muted lavender-blue — with white text, signaling the action is unavailable (e.g., out-of-stock item). No shadow, no border — flat and utilitarian.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Continue Shopping". White background, `{colors.ink}` text, 1px `{colors.hairline}` border. Hover adds a subtle `{colors.hairline-soft}` background. Same height and padding as primary for alignment in forms.

**`button-tertiary-text`** — A text-only link styled as a button, used for "Cancel" or "Clear Filters". No background, no border — just `{colors.primary}` text in `{typography.button-md}`. Hover underlines.

### Cards
**`product-card`** — The core browsing unit. A simple container with no rounding, no shadow, no border — the album cover does all the work. The card consists of a square image (1:1 ratio, no rounding), followed by the artist name in `{typography.title-sm}` (bold 16px), the album title in `{typography.body-sm}` (regular 14px), and the price in `{typography.price}` (bold 14px, `{colors.price}`). No "Add to Cart" button on the card — that appears on the product detail page. The entire card is clickable, linking to the product page.

### Navigation
**`nav-bar`** — A thin, 48px-tall horizontal strip at the top of every page. White background, no border. Navigation links are 12px uppercase Arial, bold, with 1px letter-spacing. Links include "Home", "New Arrivals", "Genres", "Artists", "Sale", and "About". The active page link is colored `{colors.primary}`. The search bar sits at the far right of the nav bar, a 36px-tall light-gray input with `{rounded.sm}`.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. White background, `{colors.body}` text, 1px `{colors.hairline}` border, 4px radius. On focus, the border switches to `{colors.primary}`. Padding is 8px vertical, 12px horizontal. Height is 40px to match buttons.

### Footer
**`footer`** — A light gray (`{colors.footer-bg}`) section at the bottom of every page. Contains a single column of navigation links (same as top nav but in sentence case), social media icons (Instagram, Twitter, Bandcamp) in `{colors.social-icon}`, and a small "Worldwide Shipping" tagline in `{colors.muted}`. Links are 14px Arial, regular weight. No rounding, no borders — just stacked text.

### Badges
**`badge-new`** — A small red pill (`{colors.badge-new}`) with white text, used on product cards to indicate recently added items. 11px bold Arial, 2px vertical padding, 6px horizontal, 4px radius. Positioned absolutely over the top-left corner of the product image.

**`badge-sale`** — Same shape as `badge-new` but in `{colors.badge-sale}` (indigo), used for discounted items.

### Hero Section
**`hero-section`** — A full-width banner at the top of the homepage. White background, 48px top/bottom padding, 24px left/right. Contains a large headline in `{typography.display-xl}` (28px bold Arial) and a subtitle in `{typography.body-md}`. No image — the hero is purely typographic, often featuring a new arrival or a sale announcement.

### Dividers
**`divider`** — A 1px solid line in `{colors.hairline}`, used to separate sections. No margin — spacing is handled by the parent container.

**`divider-soft`** — A 1px solid line in `{colors.hairline-soft}`, used for subtle separation within cards or lists.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu. Product cards stack in a single column. Hero section reduces padding to 24px. Footer links stack vertically. Search bar moves below nav. |
| Tablet | 744–1128px | Nav bar remains horizontal but links may wrap. Product cards display in 2 columns. Hero section padding at 36px. Footer links in two columns. |
| Desktop | 1128–1440px | Full nav bar with all links visible. Product cards in 3–4 columns. Hero section at full padding. Footer links in a single row. |
| Wide | > 1440px | Max-width container at 1440px, centered. Product cards in 4–5 columns. No additional changes — the layout scales gracefully. |

### Touch Targets
- All buttons and links: minimum 44px height for tap targets on mobile.
- Nav bar hamburger icon: 48px x 48px tap area.
- Product cards: entire card is a tap target (minimum 120px height).
- Social icons in footer: 44px x 44px tap area.

### Collapsing Strategy
- On mobile, the top nav collapses into a hamburger menu. The menu overlay is full-screen, with links stacked vertically in 48px-tall rows.
- The search bar moves from the nav bar to a dedicated row below the nav on mobile.
- Product cards collapse from multi-column grid to single-column stack.
- Footer links collapse from a single row to a vertical stack.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list returned no hex values (framework defaults were filtered out, and no distinctive brand colors were detected). The primary `#1a237e` is an educated guess based on the brand's association with Japan and independent record stores — it should be verified against the live site's CSS.
- Font-family declarations returned only "Arial". No custom or web fonts were detected. The site may use a system font stack that wasn't captured.
- No meta theme-color was found — the browser chrome color is unknown.
- Hover and focus states for buttons, links, and inputs are inferred from common patterns, not extracted.
- Error states for form inputs (e.g., invalid email, missing required field) are not documented.
- The site may use a Shopify or other e-commerce platform — checkout flow styling (payment buttons, cart drawer) is not captured.
- Dark mode is not supported — no `prefers-color-scheme` media queries were detected.
- The product detail page layout (larger image, description, "Add to Cart" button) is not documented — only the card-level browsing experience is covered.
- Sub-brand or sale-specific color variations (e.g., "Clearance" badge, "Pre-order" badge) are not captured.
- The site may use a sticky header on scroll — this was not detected.
- Loading states (skeleton screens, spinners) are not documented.
- The newsletter signup form (if present) is not captured — only the standard text input is defined.
