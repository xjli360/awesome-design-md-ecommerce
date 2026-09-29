---
version: alpha
name: "Chirp"
source_url: "https://www.chirpbooks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, ink-black (#313131) audiobook storefront that trusts its covers and its copy over ornament — the single extracted hex is the brand's entire foreground vocabulary, from body text to nav links to star ratings. The site reads like a well-stocked library shelf: dense with metadata (author, narrator, length, price, rating), each book card a compact information block rather than a visual hero. The system font stack (-apple-system, system-ui, sans-serif) means Chirp lets the content speak without typographic branding; there is no custom typeface, no brand font, just clean, legible text at modest sizes. The primary action — buying a book — uses a bold accent color (likely a distinctive green or orange from the extracted palette, though only #313131 survived extraction), set against white canvas with soft rounded corners on cards and buttons. The experience is utilitarian but warm: high information density, clear pricing, and a persistent "Listen Now" or "Add to Cart" affordance that never competes with the book's own cover art. Chirp's design philosophy is "the book is the hero" — the interface steps back, using only one strong color, one type stack, and generous spacing to let thousands of titles breathe.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#b0b0b0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#6a6a6a"
  muted-soft: "#8a8a8a"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#2e7d32"
  accent-hover: "#1b5e20"
  badge-new: "#e65100"
  badge-sale: "#c62828"
  star-rating: "#313131"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.accent-hover}"
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
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.accent}"
    typography: "{typography.button-sm}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}20"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}20"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-cover:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-rating:
    typography: "{typography.caption-sm}"
    textColor: "{colors.star-rating}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.base} 0"
  category-tab:
    typography: "{typography.button-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.full}"
  category-tab-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Buy Now", and "Start Listening". Rendered in the brand's accent green (`{colors.accent}`) with white text and a subtle 6px corner radius. On hover, shifts to a darker shade (`{colors.accent-hover}`). The disabled state uses a light gray (`{colors.primary-disabled}`) to signal unavailability. Height is 44px with 12px/24px padding, making it compact enough to sit alongside book metadata without overwhelming the cover art.

**`button-secondary`** — An outlined or ghost alternative for "Preview", "Learn More", or "Add to Wishlist". Uses a white background with `{colors.ink}` text and a 1px hairline border. Active state fills with `{colors.surface-soft}`. Same 44px height as primary for alignment in button groups.

**`button-tertiary-text`** — A text-only link styled as a button, used for "See all" links in category sections or "Sign in" prompts. Uses `{colors.accent}` for color and `{typography.button-sm}` for size. No background or border — just a clickable text label.

### Text Inputs
**`text-input`** — Standard form input for search, email signup, and account forms. White background, `{colors.ink}` text, 6px rounded corners, 44px height. On focus, gains a 2px `{colors.primary}` ring with 12% opacity. Placeholder text uses `{colors.muted}`.

### Navigation
**`top-nav`** — A fixed 64px header bar with white background. Contains the Chirp logo (left), navigation links (center), and user account / cart icons (right). Active nav links get a 2px bottom border in `{colors.primary}`. The nav uses `{typography.nav-link}` at 14px with 0.3px letter spacing for a slightly tighter, more editorial feel.

### Search
**`search-bar`** — A pill-shaped search field (`{rounded.full}`) with a light gray background (`{colors.surface-soft}`) and a magnifying glass icon. On focus, the background turns white and a `{colors.primary}` ring appears. Used for searching titles, authors, or narrators. Height is 44px with 10px/16px padding.

### Product Cards
**`product-card`** — The core content unit, used on browse pages, search results, and category grids. A white card with 8px rounded corners, 16px padding, and a 1:1 cover image area. Contains the book title (`{typography.title-sm}`), author name (`{typography.caption}` in `{colors.muted}`), star rating, and price (`{typography.price}` in `{colors.ink}`). On hover, a subtle box shadow lifts the card. The card is designed for high-density grids — typically 4-6 columns on desktop, 2 on tablet, 1 on mobile.

### Badges
**`badge-new`** and **`badge-sale`** — Small, uppercase labels pinned to the top-left corner of product card covers. `badge-new` uses an orange background (`{colors.badge-new}`) for "New Release" flags; `badge-sale` uses red (`{colors.badge-sale}`) for discounted titles. Both use 11px bold text with 0.5px letter spacing and 4px rounded corners.

### Footer
**`footer`** — A full-width section with a light gray background (`{colors.surface-soft}`). Contains links to About, Help, Terms, Privacy, and social icons. Links use `{colors.muted}` and darken to `{colors.ink}` on hover. Padding is `{spacing.section}` top and bottom for breathing room.

### Hero Section
**`hero-section`** — Used on the homepage and category landing pages. A soft gray background (`{colors.surface-soft}`) with a large display title (`{typography.display-xl}`) and a supporting subtitle (`{typography.body-md}` in `{colors.muted}`). May include a featured book cover or promotional graphic. Padding is `{spacing.section}` on all sides.

### Category Strip
**`category-strip`** — A horizontal scrolling strip of category pills (e.g., "Fiction", "Nonfiction", "Mystery", "Romance"). Each pill is a `{rounded.full}` button with `{colors.muted}` text. The active pill gets a light gray background (`{colors.surface-soft}`) and `{colors.ink}` text. Used above the product grid for filtering.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu; search bar moves below nav; hero section reduces padding to 32px; category strip becomes horizontally scrollable without labels |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (logo, search, cart); hero uses 48px padding; category strip shows 4-5 pills |
| Desktop | 1128–1440px | Four-column product grid; full top-nav with all links; hero at full `{spacing.section}` padding; category strip shows all pills |
| Wide | > 1440px | Six-column product grid; max-width container (1440px) centered; hero may feature a larger cover image; category strip expands to 8+ pills |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (exceeds Apple's 44pt guideline)
- Search bar is 44px tall with generous padding for fat-finger accuracy
- Category pills are minimum 36px tall with 8px horizontal padding
- Product cards have a minimum tap area of 120px x 160px on mobile

### Collapsing Strategy
- Top-nav links collapse into a hamburger menu below 744px; the menu is a full-screen overlay with large touch targets
- Search bar moves from the top-nav into a dedicated row below the nav on mobile, expanding to full width
- Product grid collapses from 4-6 columns to 2 columns on tablet and 1 column on mobile
- Hero section reduces vertical padding from 64px to 32px on mobile; the subtitle may be hidden
- Category strip becomes horizontally scrollable on mobile with snap points; labels may be truncated to single words
- Footer links stack vertically on mobile instead of the multi-column layout used on desktop

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was reliably extracted from the live site; the accent color (likely green or orange) and all other palette tokens are inferred from common DTC audiobook patterns and may not match the actual brand. The extracted font stack is system-only — no custom brand typeface was detected. Hover states, focus rings, error styling, and disabled state colors are estimated based on accessibility best practices and common e-commerce patterns. Dark mode support is unknown. The actual brand may use a different accent color, additional secondary colors, or a custom typeface that was not present in the extracted CSS. Sub-brand or promotional color palettes (e.g., for seasonal sales or genre-specific landing pages) are not captured. The star rating color and badge colors are inferred from the primary ink color and common conventions. The actual button height, padding, and border radius values are estimated from typical audiobook store patterns and may differ from the live site. No animation or transition timing data was extracted.
