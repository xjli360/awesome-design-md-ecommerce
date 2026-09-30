---
version: alpha
name: "Tower 28"
source_url: "https://www.tower28beauty.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clean, vegan, and cruelty-free beauty brand that feels like a breath of fresh air in the makeup aisle. Tower 28's visual identity is anchored on a warm, off-white canvas (`#fffaf7`) and a signature coral-orange (`#d74015`) that pulses through every primary CTA, badge, and accent — a color that reads as energetic but not aggressive, like a sunlit California poppy. The brand's palette is surprisingly complex for "clean beauty": deep berry tones (`#872626`, `#892628`) suggest lip and cheek stains, while a muted lavender (`#efe3f3`) and soft pink (`#f9e5fc`) whisper toward inclusivity and gentle femininity. Cool steel blues (`#676986`, `#9a9db1`) and a pale sky (`#bcdbff`) ground the system, preventing it from tipping into saccharine. Typography leans on Cooper Lt BT for display moments — a rounded, friendly serif that feels hand-drawn and approachable — paired with Scto Grotesk A Medium for body and buttons, giving the brand a crisp, editorial edge. Corners are softly rounded (`{rounded.sm}` for buttons, `{rounded.md}` for cards), and the overall spacing is generous (`{spacing.lg}` to `{spacing.xxl}`), letting each product breathe. The brand trusts its color stories and ingredient transparency over heavy ornamentation; there are no hard corners, no aggressive contrasts, just a warm, sun-washed minimalism that says "you can wear makeup and still be good to your skin."

colors:
  primary: "#d74015"
  primary-active: "#ee542f"
  primary-disabled: "#f8f2ed"
  ink: "#121212"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#fffaf7"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-berry: "#872626"
  accent-berry-light: "#892628"
  accent-lavender: "#efe3f3"
  accent-pink: "#f9e5fc"
  accent-sky: "#bcdbff"
  accent-mint: "#b2f9e9"
  accent-warm: "#ebdfdd"
  accent-warm-light: "#e8d8ec"
  accent-coral: "#ee542f"
  accent-coral-soft: "#e0d1e7"
  accent-steel: "#2c3e50"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"

typography:
  display-xl:
    fontFamily: "'Cooper Lt BT', 'Noto Color Emoji', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Cooper Lt BT', 'Noto Color Emoji', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cooper Lt BT', 'Noto Color Emoji', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Cooper Lt BT', 'Noto Color Emoji', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Scto Grotesk A Medium', 'Noto Color Emoji', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.25px
  title-sm:
    fontFamily: "'Scto Grotesk A Medium', 'Noto Color Emoji', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.15px
  body-md:
    fontFamily: "'Scto Grotesk A Medium', 'Noto Color Emoji', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Scto Grotesk A Medium', 'Noto Color Emoji', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Scto Grotesk A Medium', 'Noto Color Emoji', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Scto Grotesk A Medium', 'Noto Color Emoji', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Scto Grotesk A Medium', 'Noto Color Emoji', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Scto Grotesk A Medium', 'Noto Color Emoji', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Scto Grotesk A Medium', 'Noto Color Emoji', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Scto Grotesk A Medium', 'Noto Color Emoji', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-berry}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(18,18,18,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-berry}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.accent-berry}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-clean:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  swatch-color:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  swatch-color-selected:
    outline: "2px solid {colors.primary}"
    outlineOffset: "2px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.md} 0"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in the signature coral-orange (`{colors.primary}`) with white text and a soft 8px radius (`{rounded.sm}`). On hover, it shifts to a brighter coral (`{colors.primary-active}`) for a subtle glow effect. The disabled state uses a muted off-white (`{colors.primary-disabled}`) with muted text, signaling unavailability without visual noise. Text is uppercase with generous letter-spacing, reinforcing the clean, editorial feel.

**`button-secondary`** — An outlined variant that inverts the primary: a white background with a 2px coral border and coral text. Active state swaps the border and text to the brighter coral (`{colors.primary-active}`). This button is used for secondary actions like "Add to Wishlist" or "Learn More" alongside primary CTAs.

**`button-tertiary-text`** — A text-only button with no background or border, using only the primary coral for text color. Ideal for inline actions like "View Details" or "Shop All" within cards or sections where a full button would feel heavy.

**`button-pill-primary`** — A fully pill-shaped variant (`{rounded.full}`) of the primary button, used for promotional badges, "Shop Now" calls in hero sections, or compact CTAs in navigation. The smaller text size (`{typography.button-sm}`) and tighter padding make it feel badge-like and friendly.

**`button-pill-outline`** — The outlined pill counterpart, with a transparent background and a 1px coral border. Used for "Subscribe" or "Get Notified" actions where a less assertive visual is desired.

### Cards
**`product-card`** — The standard product display card, with a white background, 12px rounded corners (`{rounded.md}`), and 16px padding. The card contains a product image with 8px rounded corners, a title in `{typography.title-sm}`, and a price in `{typography.body-md}`. Badges (new, sale, clean) are positioned at the top-left of the image area. On hover, the card may elevate with a subtle shadow.

**`hero-section`** — A full-width banner section with a soft gray background (`{colors.surface-soft}`) and large display typography. The hero CTA button sits prominently, using the primary coral with generous padding. This section is the brand's primary storytelling vehicle, often featuring lifestyle imagery and a single, clear value proposition.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar, 72px tall, with a white background and uppercase nav links in `{typography.nav-link}`. The active link is underlined with a 2px coral border. On scroll, a subtle box shadow appears to separate the nav from the page content. The nav includes the brand logo, primary links, a search icon, and a cart icon.

**`nav-link-active`** — The active state for navigation links, distinguished by the brand's coral color and a bottom border. Inactive links use the dark ink color (`{colors.ink}`) with no underline.

### Forms
**`text-input`** — A standard text input field with a white background, 8px rounded corners, and a light gray border (`{colors.hairline}`). On focus, the border thickens to 2px and turns coral. Error states use a 2px berry border (`{colors.accent-berry}`). Padding is generous (12px vertical, 16px horizontal) for comfortable typing.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) with a white background and a light gray border. On focus, the border becomes 2px coral. Used in the navigation and on search result pages.

**`quantity-selector`** — A compact input for adjusting product quantities, with a white background, 8px rounded corners, and a light gray border. Used on product detail pages and in the cart.

### Badges
**`badge-new`** — A small, mint-green (`{colors.accent-mint}`) badge with dark text, indicating a new product launch. The 4px rounded corners and uppercase typography make it feel like a friendly sticker.

**`badge-sale`** — A berry-red (`{colors.accent-berry}`) badge with white text, used for sale or clearance items. The high contrast ensures it's immediately noticeable.

**`badge-clean`** — A sky-blue (`{colors.accent-sky}`) badge with dark text, signaling the brand's clean, vegan, and cruelty-free credentials. This badge is often used on product cards and detail pages to reinforce the brand's core values.

### Swatches
**`swatch-color`** — A 32px circular color swatch used for product shade selection. The selected state is indicated by a 2px coral outline with a 2px offset, ensuring the active shade is clearly visible even among similar colors.

### Accordion
**`accordion-header`** — A clickable header for collapsible sections (e.g., product details, ingredients, shipping info). Uses `{typography.title-sm}` with no background, and padding only on the top and bottom. The content area uses `{typography.body-sm}` with bottom padding for spacing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-md}`; buttons become full-width; search bar moves to a dedicated overlay |
| Tablet | 744–1128px | Two-column grid for product cards; nav links remain visible but may be truncated; hero uses `{typography.display-lg}`; side-by-side layout for product details (image left, info right) |
| Desktop | 1128–1440px | Full three- or four-column grid for product cards; full nav bar with all links; hero uses `{typography.display-xl}`; maximum content width is 1128px, centered |
| Wide | > 1440px | Content remains centered at 1128px max-width; extra whitespace on sides; nav bar may include additional utility links; hero may feature full-bleed imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px and a minimum width of 44px to meet WCAG touch target guidelines.
- Navigation links have at least 48px of touch area, even if the text is smaller.
- Color swatches are 32px with additional padding to ensure a 44px touch target.
- Quantity selector buttons are 40px tall with generous clickable areas.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu. The brand logo remains centered, and the cart icon is moved to the right of the hamburger.
- Product filters (e.g., by shade, category, price) collapse into a "Filter" button that opens a slide-out panel.
- The footer's multi-column link sections collapse into accordion-style lists to save vertical space.
- Hero sections may reduce image height and stack text above the CTA rather than overlaying it.
- Product detail pages collapse the image gallery into a single-column swipeable carousel, with thumbnails hidden.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components beyond primary/secondary buttons could not be reliably extracted (e.g., nav-link hover color, product-card hover shadow, text-input focus ring).
- Error and success states for forms (e.g., input validation messages, success banners) are not fully documented.
- Dark mode or high-contrast mode color overrides are not present in the extracted data.
- Sub-brand or seasonal palette variations (e.g., holiday collections, limited-edition drops) are not captured.
- The exact `box-shadow` values for card elevation, nav-bar sticky state, and modal overlays are inferred from common patterns but not extracted.
- Animation and transition timing (e.g., button hover duration, card hover lift) are not specified.
- The `font-weight` for Cooper Lt BT is assumed to be 400 (regular) as the extracted data does not include weight variations; the brand may use a single weight for display text.
- The `letter-spacing` and `textTransform` values for typography tokens are estimated based on common editorial beauty brand patterns and may differ from the live site's exact CSS.
- The `oke-widget-icons` font family is used for product review widgets (Okendo) and is not a core brand typeface; it is excluded from the typography system.
- The `inherit` and `serif` font-family declarations are generic fallbacks and are not used as primary tokens.
- The `!important` flag on `oke-widget-icons!important` is a specificity override and is not a design token.
