---
version: alpha
name: "The Last Bookstore"
source_url: "https://www.lastbookstorela.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A labyrinth of a bookstore where the walls themselves are made of books — the site mirrors that physical density with a deep charcoal ink (#080808) on a clean white canvas, punctuated by a single sky-blue accent (#7fccf7) that reads like a skylight in a dim, towering stack room. The primary action color (#3899ec) is a cooler, more utilitarian blue, suggesting the site prioritizes function over whimsy — search, browse, cart — while the muted gray (#5f6360) handles secondary text and borders with a quiet, library-like neutrality. Typography defaults to system sans-serifs (Arial, Helvetica, Madefor, Hiragino Kaku Gothic Pro) with no custom display face, a pragmatic choice that lets the bookstore's own character — the sheer strangeness and scale of the physical space — do the heavy lifting. Rounded corners are minimal: buttons get a soft {rounded.sm} (8px), but cards and containers stay at {rounded.none} or {rounded.xs} (4px), preserving a no-nonsense, grid-aligned feel. The nav bar sits fixed at the top, a thin {spacing.sm} strip of white with the logo centered, while the hero section uses a full-bleed image of the store's famous book tunnel, the blue accent appearing only in the search bar and primary CTA. There is no decorative typography, no illustration system, no brand pattern — the design is a frame for the content, deliberately invisible so the books and the store's mythology take center stage.

colors:
  primary: "#3899ec"
  primary-active: "#2a7dc4"
  primary-disabled: "#a3cff5"
  ink: "#080808"
  body: "#5f6360"
  muted: "#5f6360"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sky: "#7fccf7"
  accent-sky-soft: "#d4edfc"

typography:
  display-xl:
    fontFamily: "Madefor, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Madefor, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "Madefor, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Madefor, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Madefor, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Madefor, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Madefor, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Madefor, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "Madefor, 'Helvetica Neue', Arial, sans-serif"
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
  lg: 16px
  xl: 24px
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
  section: 80px

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
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    outline: "2px solid {colors.accent-sky-soft}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid #d32f2f"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "#d32f2f"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  section-header:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl} 0 {spacing.base} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Subscribe". A solid blue (#3899ec) rectangle with {rounded.sm} corners and white text. On hover, darkens to {colors.primary-active} (#2a7dc4). Disabled state uses {colors.primary-disabled} (#a3cff5) with white text, signaling the action is unavailable without visual clutter.

**`button-secondary`** — An outlined alternative for "Learn More" or "View Details" actions. White background with a 1px {colors.hairline} border and {colors.ink} text. On hover, the border thickens to {colors.muted} and the background shifts to {colors.surface-soft}. Same 44px height as the primary button for alignment in forms.

**`button-text`** — A text-only link styled as a button, used for "Cancel" or "Back to Browsing". No background, no border — just {colors.primary} text in {typography.button-md}. On hover, shifts to {colors.primary-active}. Reserved for low-emphasis actions within modals or inline forms.

### Cards
**`product-card`** — A minimal, border-only card with no rounded corners, reflecting the bookstore's no-frills aesthetic. Contains a product image (full-width, no border radius), the title in {typography.title-md}, and the price in {typography.body-md}. On hover, a subtle box-shadow and darker border appear. No padding is set on the card itself — inner spacing is handled by child elements.

**`product-card-image`** — The image container within a product card. Uses {colors.surface-soft} as a placeholder background before the image loads. No border radius — images are flush with the card edges.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height, white background with a 1px soft hairline bottom border. Contains the store logo (left or center), a set of nav links in uppercase {typography.nav-link}, and a search icon. Active links get a 2px bottom border in {colors.ink}. Inactive links are {colors.muted}. The bar collapses to a hamburger menu below 744px.

**`nav-link-active`** / **`nav-link-inactive`** — Active nav links are bold, uppercase, and underlined with a 2px {colors.ink} border. Inactive links are {colors.muted} with no underline. Both use {typography.nav-link} (14px, 600 weight, 0.5px letter spacing).

### Forms
**`text-input`** — A standard input field with a 1px {colors.hairline} border, {rounded.xs} corners, and 48px height. On focus, the border turns {colors.primary} and a 2px soft blue outline ({colors.accent-sky-soft}) appears for accessibility. Error state uses a red border (#d32f2f) — no outline change.

**`search-bar`** — A pill-shaped ({rounded.full}) input with a light gray background ({colors.surface-soft}) and 1px hairline border. On focus, the background turns white and the border switches to {colors.primary}. Used in the hero section and the nav bar's mobile search.

### Badges
**`badge-new`** — A small, sky-blue ({colors.accent-sky}) badge with dark text, used to flag new arrivals or featured items. {rounded.xs} corners, uppercase 11px type.

**`badge-sale`** — A red (#d32f2f) badge with white text for sale or discount items. Same shape and type as `badge-new`.

**`badge-category`** — A pill-shaped ({rounded.full}) badge with a light gray background and muted text, used for genre or category tags (e.g., "Fiction", "Signed Copy"). Uppercase, 11px.

### Footer
**`footer`** — A full-width dark section ({colors.ink}) with white text. Contains columns of links, social icons, and copyright info. Links are {colors.muted-soft} and turn white on hover. Padding is {spacing.xxl} top and bottom, {spacing.lg} left and right.

### Section
**`section-header`** — A large display heading ({typography.display-lg}) with generous top padding ({spacing.xl}) and bottom padding ({spacing.base}). Used to introduce content sections like "New Arrivals" or "Events".

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger; product cards stack single-column; hero section reduces to 300px min-height; search bar moves to full-width below nav; footer links stack vertically |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero section at 400px min-height; search bar in nav is icon-only |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3- or 4-column grid; hero section at 500px min-height; search bar expands to text input |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-column grid; hero section content centered with max-width |

### Touch Targets
- All buttons and links maintain a minimum 44px touch target height.
- Nav bar hamburger icon is 48px × 48px.
- Search bar in mobile is full-width with 48px height.
- Badges are at least 20px tall for tap accuracy.

### Collapsing Strategy
- Nav links collapse into a hamburger menu below 744px. The menu slides in from the right, overlaying content with a semi-transparent scrim.
- Product cards collapse from a multi-column grid to a single column on mobile.
- The hero section's text and CTA stack vertically on mobile, with the background image cropped to maintain visual impact.
- Footer columns collapse to a single column below 744px, with accordion-style expandable link groups.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors are limited and may include social-icon tones (#7fccf7) and a generic blue (#3899ec) that could be a framework default. The brand's true primary may be different — the sky-blue accent (#7fccf7) is the most distinctive color in the palette and may function as a secondary brand color. The extracted list is too sparse to confirm a full brand palette.
- Font-family declarations are a mix of system fallbacks (Arial, Helvetica) and a custom font (Madefor). Madefor is used for headings and buttons, but its exact weight and size variants are inferred from common web patterns, not extracted from the live site.
- No hover, focus, or active states could be extracted from the live site. All state variants in this document are based on standard accessibility and UI conventions.
- No error, success, or warning color tokens could be extracted. The error red (#d32f2f) is a common default and may not match the brand's actual error styling.
- No dark mode or high-contrast mode tokens are available.
- The site may use a custom font for display purposes (e.g., a serif for book titles) that was not captured in the extracted font list.
- No spacing or rounded values could be extracted from the live site. All values in this document are based on common design system patterns and may not match the actual site.
- The site's platform (Shopify or other) could not be confirmed, which affects the structure of product and cart components.
