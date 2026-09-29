---
version: alpha
name: "Lighthouse Records"
source_url: "https://www.lighthouserecords.jp"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A raw, unpolished independent record store webstore where #0000ff — a piercing, almost synthetic blue — cuts through a palette of warm pinks (#ffe8e8), aggressive reds (#d40f0f, #ff0000), and deep navy tones (#222255, #000088) like a neon sign in a dimly lit basement. The extracted palette reads less like a designed system and more like a crate-digger’s notebook: the blues and navies suggest a default framework skeleton, while the pinks and reds hint at sale tags, sold-out badges, and the urgency of limited pressings. Typography defaults to system stacks — Arial, Helvetica Neue, and Japanese fallbacks like Hiragino Kaku Gothic Pro and Meiryo — with monospace (Consolas, Monaco, Courier New) appearing for pricing or catalog numbers, giving the interface a utilitarian, almost database-like honesty. There is no polished hero image or curated lifestyle photography; the site leans on {rounded.none} corners, tight {spacing.sm} gaps between rows of album covers, and a dense information hierarchy where every pixel competes for attention. The search bar, if present, likely sits as a simple text input with {rounded.xs} and a hairline border (#e1e1e8), while primary actions — "Add to Cart" or "Buy Now" — probably wear the most saturated accent (#0088cc or #dd1144) against a {colors.canvas} of #fcfcfc. This is a store that prioritizes inventory over interface: the design exists to get out of the way, not to impress.

colors:
  primary: "#0000ff"
  primary-active: "#3300ff"
  primary-disabled: "#7777cc"
  ink: "#222255"
  body: "#555555"
  muted: "#7777cc"
  muted-soft: "#a9dba9"
  hairline: "#e1e1e8"
  hairline-soft: "#f7f7f9"
  canvas: "#fcfcfc"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#d40f0f"
  accent-pink: "#ffe8e8"
  accent-orange: "#ff9900"
  accent-green: "#46a546"
  badge-sold: "#dd1144"
  badge-new: "#0088cc"
  link-blue: "#005580"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  price-mono:
    fontFamily: "Consolas, 'Courier New', Monaco, monospace"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Consolas, 'Courier New', Monaco, monospace"
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-price:
    typography: "{typography.price-mono}"
    color: "{colors.body}"
  product-card-title:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new-arrival:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    padding: "{spacing.lg} {spacing.base}"
    borderTop: "1px solid {colors.hairline}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
  category-tab-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  pagination-link:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"
    border: "1px solid {colors.hairline}"
  pagination-link-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in a piercing #0000ff against white text. Used for "Add to Cart" and "Checkout" actions. On hover/active, shifts to #3300ff. When disabled, fades to #7777cc with reduced opacity. The button uses {rounded.xs} (4px) corners — intentionally sharp to match the utilitarian grid.

**`button-secondary`** — A ghost button with a white background and a thin #e1e1e8 border. Used for "View Details" or "Continue Shopping" actions. Text sits in {colors.ink} (#222255). On hover, the border darkens to {colors.hairline-soft} (#f7f7f9) and a subtle background shift occurs.

**`button-accent-red`** — A high-urgency variant in #d40f0f, reserved for "Buy Now" or limited-time offers. Same sharp 4px corners and 40px height as the primary button. This is the visual equivalent of a red "SOLD OUT" stamp on a record sleeve.

### Cards
**`product-card`** — A minimal, borderless container with zero rounding. Each card holds an album cover image (typically 1:1 square), the artist name in {typography.body-md}, the album title in {typography.body-sm}, and the price in monospace (#555555). Cards sit in a dense grid with {spacing.sm} (8px) gutters — no padding between the image and the edge of the card. The lack of visual hierarchy forces the album art to do all the work.

**`product-card-image`** — Square aspect ratio, no rounding, no shadow. The image fills the card width. On hover, a subtle 1px #e1e1e8 border may appear, but the default is borderless.

### Navigation
**`nav-bar`** — A 56px-tall white bar with a 1px bottom border in #e1e1e8. Navigation links are uppercase, 14px, weight 600, with 0.5px letter spacing. The active link is underlined with a 2px #0000ff border. Categories (Vinyl, CD, Cassette, Merch) sit in a horizontal strip below the nav bar.

**`category-strip`** — A secondary navigation row for filtering by format. Links are styled like nav links but in muted #7777cc. The active category gets a 2px bottom border in #0000ff. No rounding, no background — just text and a line.

### Forms
**`text-input`** — A simple white input field with a 1px #e1e1e8 border and 4px rounding. Used for search, email signup, and checkout forms. On focus, the border switches to #0000ff. Height is 40px with 8px vertical padding and 12px horizontal padding.

**`search-bar`** — Identical to the text input in appearance, but may include a magnifying glass icon (in #7777cc) on the left or right. No pill shape, no rounded full — this is a functional search input, not a design statement.

### Badges
**`badge-sold-out`** — A small, sharp-cornered badge in #dd1144 with white monospace text reading "SOLD OUT" or "SOLD". 11px, weight 700, uppercase, with 0.5px letter spacing. Positioned in the top-left corner of product card images.

**`badge-new-arrival`** — Same shape and size as the sold-out badge, but in #0088cc. Reads "NEW" or "NEW ARRIVAL". The blue stands out against the warm pink (#ffe8e8) that may appear on sale banners or promotional strips.

### Footer
**`footer`** — A light gray (#f5f5f5) background with a 1px #e1e1e8 top border. Text is in #555555 at 12px. Contains links to About, Shipping, Returns, and Contact, plus social media icons. Padding is {spacing.lg} (24px) vertically and {spacing.base} (16px) horizontally.

### Pagination
**`pagination-link`** — Small square buttons (roughly 32x32px) with a 1px #e1e1e8 border and 4px rounding. The active page is filled with #0000ff and white text. Inactive pages are white with #222255 text. Used at the bottom of product listing pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; search bar moves to top; category strip scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav remains visible but condensed; category strip wraps to two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; category strip in single row; search bar in header |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; additional whitespace on sides |

### Touch Targets
- All buttons and links maintain a minimum 44x44px touch target
- Product cards are tappable as entire units
- Category strip items have 48px minimum height for touch scrolling
- Pagination links are at least 40x40px on mobile

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px
- Category strip becomes a horizontally scrollable row on mobile
- Footer links stack vertically on mobile
- Product grid reduces columns from 4 to 1 on mobile
- Search bar moves from header to a full-width row below the nav on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is heavily polluted with framework defaults (multiple blues, grays, and greens from Bootstrap, Shopify, or similar). The true brand palette may be more restrained than the 25+ colors listed. The most distinctive accent (#0000ff) was chosen as primary, but this may be a framework default rather than a deliberate brand choice.
- No hover or active states could be reliably extracted for most components beyond buttons.
- Font-family declarations are all system stacks — no custom or web fonts were detected. The brand may use a Japanese-specific typeface not captured in extraction.
- No dark mode or high-contrast mode data available.
- Error states (form validation, 404 pages, out-of-stock messages) could not be extracted.
- The meta theme-color tag was absent, suggesting no PWA or mobile browser chrome customization.
- No animation or transition timing data (hover fades, page transitions, loading states) could be extracted.
- The platform may be custom-built (Shopify flag is False), so component structure may differ from typical e-commerce templates.
- No data on checkout flow, cart drawer, or modal styling.
