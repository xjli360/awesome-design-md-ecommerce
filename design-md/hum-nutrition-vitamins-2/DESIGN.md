---
version: alpha
name: "HUM Nutrition"
source_url: "https://humnutrition.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A confident pink pulse — #ee4b9b — runs through every CTA, badge, and accent on a near-white canvas (#fefefe), signaling that this is a wellness brand unafraid of color and pleasure. The palette is a study in contrast: the hot pink sits alongside a warm marigold (#fecf0a), a soft blush (#f8c1d9), and a pale lemon (#f1f781), creating a system that feels both clinical and joyful. Body text runs in #303030 on white, with secondary copy in #545454 and #757575, keeping readability high while the brand's personality lives in the accents. The typography uses Montserrat as its primary voice — a geometric sans-serif that balances the playfulness of the color system with a clean, structured presence. Buttons are pill-shaped ({rounded.full}), cards have soft corners ({rounded.md}), and the overall spacing is generous, with {spacing.xxl} padding around sections and {spacing.xl} between content blocks. The brand's signature move is the "HUM pink" badge — a small, rounded pill in #ee4b9b with white text that appears on product cards, quiz results, and promotional banners, creating a consistent visual shorthand for "this is the thing to click." The navigation is minimal: a sticky top bar with the logo, a search icon, and a cart icon, all on a white background with a thin #e0e0e0 hairline. The overall feeling is that of a clean, modern pharmacy counter — but one designed by someone who loves color.

colors:
  primary: "#ee4b9b"
  primary-active: "#d60092"
  primary-disabled: "#f8c1d9"
  ink: "#303030"
  body: "#545454"
  muted: "#757575"
  muted-soft: "#949494"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#fefefe"
  surface-soft: "#f5f9fc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fecf0a"
  accent-lemon: "#f1f781"
  accent-blush: "#f8c1d9"
  accent-pink-deep: "#a01c3d"
  accent-pink-bright: "#e10098"
  accent-pink-hot: "#ee0aa4"
  accent-pink-light: "#ffe6f7"
  accent-pink-wash: "#ffecfb"
  accent-gray-light: "#f2f2f2"
  accent-gray-mid: "#9ca3af"
  accent-gray-dark: "#222222"
  accent-near-black: "#010202"
  accent-black: "#060606"
  accent-white-warm: "#f7f6f2"
  accent-border: "#d8d8d8"
  accent-border-soft: "#bbbbbb"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-pill-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-blush:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.accent-pink-deep}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.accent-pink-deep}"
  text-input-label:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  text-input-helper:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  product-card-price:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  product-card-badge-sold-out:
    backgroundColor: "{colors.accent-gray-mid}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  product-card-badge-bestseller:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
  hero-secondary-cta:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "13px 31px"
    border: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "2px solid {colors.primary}"
  search-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
  quiz-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
  quiz-option:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  quiz-option-selected:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"
    border: "2px solid {colors.primary}"
  quiz-progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 8px
  quiz-progress-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 8px
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  testimonial-author:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
  rating-stars:
    backgroundColor: transparent
    textColor: "{colors.accent-yellow}"
  badge-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-pill-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-pill-blush:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.accent-pink-deep}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  badge-pill-lemon:
    backgroundColor: "{colors.accent-lemon}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a pill-shaped button in #ee4b9b with white Montserrat 600 text. On hover, it shifts to #d60092; when disabled, it fades to #f8c1d9. Used for "Add to Cart," "Shop Now," and primary quiz CTAs. Height is 48px with 14px top/bottom and 32px side padding.
**`button-secondary`** — An outlined variant with a white background, #ee4b9b text, and a 2px solid #ee4b9b border. On hover, the background fills with #f8c1d9 and the border shifts to #d60092. Used for "Learn More" and secondary quiz actions.
**`button-tertiary-text`** — A text-only button with no background or border, using #ee4b9b text. On hover, it shifts to #d60092. Used for "View All" links and inline actions.
**`button-pill-accent`** — A yellow pill button in #fecf0a with dark text (#303030). Used for promotional badges and limited-time offers.
**`button-pill-blush`** — A blush-toned pill button in #f8c1d9 with deep pink text (#a01c3d). Used for "New" badges and gentle CTAs.

### Cards
**`product-card`** — A white card with 12px rounded corners, 16px padding, and a subtle shadow (implied by the surface-card color). Contains a product image with 8px rounded corners, a title in 16px Montserrat 600, a price in 14px Montserrat 400 (#545454), and optional badges. Badges appear as small pills in the top-left corner of the image area.
**`quiz-card`** — A larger card with 20px rounded corners and 32px padding, used for the product quiz interface. Contains quiz options, progress bars, and navigation buttons.
**`testimonial-card`** — A white card with 12px rounded corners, 24px padding, and a 1px #eeeeee border. Contains a testimonial quote in body text and an author name in title-sm.

### Navigation
**`nav-bar`** — A sticky top navigation bar, 64px tall, white background, with a 1px #e0e0e0 bottom border. Contains the HUM logo, a search icon, and a cart icon. Navigation links are uppercase Montserrat 600 at 14px, with active links in #ee4b9b and inactive links in #303030.
**`nav-link-active`** — Active navigation link styled in #ee4b9b.
**`nav-link-inactive`** — Inactive navigation link styled in #303030.

### Forms
**`text-input`** — A standard text input with 8px rounded corners, 12px/16px padding, 48px height, and a 1px #e0e0e0 border. On focus, the border thickens to 2px #ee4b9b. Error state uses a 2px #a01c3d border. Labels use caption typography, helper text uses caption-sm in #757575.
**`search-bar`** — A pill-shaped search input with 48px height, 12px/20px padding, and a 1px #e0e0e0 border. On focus, the border thickens to 2px #ee4b9b. The search icon sits inside the input in #757575.

### Footer
**`footer-section`** — A dark footer with #303030 background and white text. Contains columns of links, each with a title-sm heading and body-sm links. Links are white by default and turn #ee4b9b on hover. Padding is 64px top/bottom and 24px sides.

### Quiz
**`quiz-option`** — A selectable option in the product quiz, with a light gray background (#f5f9fc), 12px rounded corners, 16px/24px padding, and a 1px #e0e0e0 border. When selected, the background shifts to #f8c1d9 and the border becomes 2px #ee4b9b.
**`quiz-progress-bar`** — A thin 8px pill-shaped progress bar with a #e0e0e0 background and a #ee4b9b fill.

### Badges
**`badge-pill-primary`** — A small pill badge in #ee4b9b with white uppercase text. Used for "Best Seller," "Top Rated," and similar labels.
**`badge-pill-yellow`** — A yellow pill badge in #fecf0a with dark text. Used for "Sale" and "Limited Time" labels.
**`badge-pill-blush`** — A blush pill badge in #f8c1d9 with deep pink text. Used for "New" and "Just Added" labels.
**`badge-pill-lemon`** — A pale lemon pill badge in #f1f781 with dark text. Used for "Bundle & Save" labels.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero section reduces padding to 32px; quiz cards use full width; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links; hero section uses 48px padding; quiz cards use two-column layout; footer uses two-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links; hero section uses 64px padding; quiz cards use two-column layout; footer uses four-column grid |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero section uses 80px padding; quiz cards use three-column layout; footer uses four-column grid with wider spacing |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Product card CTAs are at least 48px tall
- Navigation links have a minimum 44px tap area
- Search bar is 48px tall for easy tapping
- Quiz options have 48px minimum height

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport shrinks
- Hero section reduces padding from 64px to 32px on mobile
- Footer grid collapses from 4 columns to 2 columns to 1 column
- Quiz options collapse from 3 columns to 2 columns to 1 column
- Testimonial cards collapse from 3 columns to 1 column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, scale transforms) could not be extracted from static CSS
- Error states for form validation (specific error messages, iconography) are not documented
- Sub-brand or collection-specific color palettes (e.g., "Gut Health," "Skin Clear") may exist but were not extracted
- Dark mode is not supported or documented
- Animation and transition timing values (ease-in-out durations, spring curves) are not available
- Specific icon set and icon sizing conventions are not documented
- Dropdown menu styles (for account, cart, or search) are not captured
- Modal and overlay styles (for quick view, cart drawer) are not documented
- The extracted font list includes monospace fallbacks (Consolas, Courier New, etc.) which may be used for code blocks or technical content, but their usage context is unclear
- The extracted color list includes many near-black and near-white variants (#010202, #020303, #060606, #1f1f1f, #222222, #2d2d2d) — the specific use case for each is not determined
- Checkout widget colors (Shopify Pay, Klarna, Afterpay) may be present in the extracted list but were not isolated
- Social media icon colors are not separately documented
