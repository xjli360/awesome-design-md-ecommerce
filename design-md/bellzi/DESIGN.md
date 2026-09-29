---
version: alpha
name: "Bellzi"
source_url: "https://bellzi.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A cheerful, squeezable world built on a minty-teal primary (#108474) that reads more like a candy wrapper than a brand color — it is the exact shade of a green apple Jolly Rancher, and it appears on every add-to-cart button, every header banner, and every product badge. The canvas is a warm off-white (#f9fafb) rather than pure white, giving the storefront a soft, unbleached-cotton feel that lets the plush animals pop. Accent colors arrive like sprinkles: a marigold yellow (#fbcd0a) for sale tags and star ratings, a lavender (#a89cc8) for limited-edition labels, and a pale seafoam (#c1e6e6) for category dividers. The typography stack leans on Nunito Sans for display and body — a rounded, friendly sans-serif with open apertures that mirrors the soft curves of the plushies themselves. Buttons are pill-shaped (`{rounded.full}`) and generously padded, inviting taps. Product cards use a subtle drop shadow and `{rounded.md}` corners, with the animal photo filling the full card width — no cropping tricks, just the creature in its full stuffed glory. The brand voice is direct and delighted: "Meet your new best friend" appears above every product grid. There is no cynicism here, no luxury pretense — just a clean Shopify storefront that lets the plushies do the selling. The navigation is minimal: a sticky top bar with the Bellzi wordmark, a search icon, a cart count, and a single "Shop All" link. The footer is dense with policy links and social icons, but the visual weight stays on the product photography. The overall feeling is that of a well-loved toy box — organized, colorful, and impossible to walk past without smiling.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d5c9"
  ink: "#374151"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fbcd0a"
  accent-lavender: "#a89cc8"
  accent-seafoam: "#c1e6e6"
  star-rating: "#fbcd0a"
  sale-badge: "#fbcd0a"
  error: "#dc2626"
  success: "#108474"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  price:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  price-sale:
    fontFamily: "'Nunito Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
    color: "{colors.accent-yellow}"

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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    box-shadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    box-shadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1 / 1"
    objectFit: "cover"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "8px"
    left: "8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.md}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.surface-card}"
  social-icon:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  add-to-cart-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 52px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  review-stars:
    color: "{colors.star-rating}"
    fontSize: "16px"
  badge-new:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid transparent"
  color-swatch-selected:
    border: "2px solid {colors.primary}"
  loading-spinner:
    color: "{colors.primary}"
    size: "24px"
  toast-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  toast-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The workhorse CTA, a pill-shaped button in Bellzi's minty-teal (#108474) with white text and bold Nunito Sans. Hover state darkens to `{colors.primary-active}` (#0d6b5d). Disabled state fades to a pale seafoam (#a3d5c9). Used for "Add to Cart," "Shop Now," and primary form submissions.

**`button-secondary`** — An outlined variant with a white fill and a 2px teal border. Text remains teal. Used for secondary actions like "View Details" or "Continue Shopping." Hover state fills the background with a 10% teal tint.

**`button-yellow`** — A bright marigold (#fbcd0a) pill button with dark ink text. Reserved for sale promotions, limited-time offers, and "Grab Yours" urgency calls. The yellow against the teal primary creates a cheerful, carnival-like contrast.

**`button-tertiary-text`** — A plain text button with no background or border. Teal text with underline on hover. Used for "Learn More" links within product descriptions and "Read Reviews" triggers.

### Cards
**`product-card`** — A white card with `{rounded.md}` corners and a subtle drop shadow (0 2px 8px rgba(0,0,0,0.08)). The product image fills the top of the card with a 1:1 aspect ratio and `{rounded.md}` top corners. The title and price sit below in a clean vertical stack. On hover, the shadow deepens (0 4px 16px rgba(0,0,0,0.12)) and the card lifts slightly.

**`product-card-badge`** — A small yellow rectangle positioned absolutely at the top-left of the product image. Contains uppercase text like "SALE" or "NEW" in bold 11px type. The badge uses `{rounded.xs}` for a subtle soft corner.

**`review-card`** — A bordered white card with `{rounded.sm}` corners and 16px padding. Contains the reviewer's name, a star rating rendered in `{colors.star-rating}` yellow, and the review text in `{typography.body-sm}`. Multiple review cards stack vertically with 12px gaps.

### Navigation
**`nav-bar`** — A 64px white sticky header with a 1px bottom border in `{colors.hairline}`. Contains the Bellzi wordmark on the left, a "Shop All" link in the center, and a search icon plus cart icon on the right. The cart icon shows a badge with the item count. On scroll, the nav bar gains a subtle shadow.

**`nav-link-active`** — The active navigation link uses `{colors.primary}` teal instead of the default `{colors.ink}`. Underline appears on hover for all nav links.

### Forms
**`text-input`** — A standard input field with a white background, 1px `{colors.hairline}` border, and `{rounded.sm}` corners. Padding is 12px vertical and 16px horizontal. On focus, the border thickens to 2px and turns `{colors.primary}` teal. Error state uses a red border (`{colors.error}`).

**`select-dropdown`** — Matches the text-input styling but includes a custom dropdown arrow in `{colors.muted}`. Used for product variant selection (size, color) and filtering.

**`search-bar`** — A pill-shaped (`{rounded.full}`) input field with a search icon on the left. White background, 1px `{colors.hairline}` border, 48px height. On focus, the border turns teal. Placeholder text reads "Search plushies..."

### Footer
**`footer`** — A dark section with `{colors.ink}` (#374151) background and white text. Organized into columns: "Shop," "Help," "About," and "Connect." Links are `{colors.muted-soft}` gray and turn white on hover. Social media icons (Facebook, Twitter, Instagram) sit at the bottom in `{rounded.full}` circles. The footer includes a newsletter signup form with a teal submit button.

### Badges & Labels
**`badge-new`** — A lavender (#a89cc8) badge with white text. Used for newly released plushies. Small and uppercase.

**`badge-sale`** — A yellow (#fbcd0a) badge with dark text. Used for discounted items. Often paired with a strikethrough on the original price.

**`badge-sold-out`** — A gray (#7b7b7b) badge with white text. Used for out-of-stock items. The product card remains visible but the "Add to Cart" button is disabled.

### Interactive Elements
**`quantity-selector`** — A small bordered box with minus, number, and plus controls. Used on product pages to adjust purchase quantity. The controls are clickable and change the number display.

**`add-to-cart-bar`** — A prominent 52px teal pill button at the bottom of the product page. Contains a shopping cart icon and the text "Add to Cart — $29.99" (price dynamic). On click, it triggers a toast notification.

**`color-swatch`** — A 32px circle showing the plushie's color. Selected state shows a 2px teal border. Used in product variant selectors.

### Feedback & Status
**`toast-success`** — A green (#108474) notification bar that slides in from the top. Contains a checkmark icon and message like "Added to cart!" Auto-dismisses after 3 seconds.

**`toast-error`**** — A red (#dc2626) notification bar for errors like "Out of stock" or "Please select a size." Same behavior as success toast.

**`loading-spinner`** — A teal (#108474) spinning circle used during add-to-cart processing and page transitions. 24px in size.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row). Nav bar collapses to hamburger menu. Footer stacks vertically. Hero banner reduces padding. Product images remain full-width. |
| Tablet | 744–1128px | Two-column product grid. Nav bar shows "Shop All" and cart icon only. Footer shows two columns. Hero banner uses medium padding. |
| Desktop | 1128–1440px | Three-column product grid. Full nav bar with all links visible. Footer shows four columns. Hero banner uses full padding. Product detail page shows image and description side by side. |
| Wide | > 1440px | Four-column product grid. Max-width container (1440px) centered. Hero banner scales with background image. Product cards maintain max-width. |

### Touch Targets
- All buttons and interactive elements are minimum 44px height (48px preferred) to meet WCAG touch target guidelines.
- Icon buttons (search, cart, social) are 40px circles — comfortably tappable.
- Product cards have a minimum 120px height on mobile to ensure the image and title are visible.
- Quantity selector controls are 40px tall with 32px wide clickable areas.
- Color swatches are 32px circles with 8px gaps — easy to tap without mis-selection.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger icon that opens a full-screen overlay menu.
- The product filter sidebar (if present) collapses into a "Filter" button that opens a bottom sheet.
- The footer's four-column layout collapses to a single column with accordion-style expandable sections.
- Product image galleries collapse from a row of thumbnails to a swipeable carousel.
- The "Description" and "Reviews" tabs on product pages collapse into an accordion stack.
- The search bar collapses from a full input to a magnifying glass icon that expands on tap.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (button-secondary, product-card, footer-links) are inferred from common patterns — exact color values and shadow depths were not extractable from the static HTML/CSS.
- Error styling for form inputs (text-input-error) uses a generic red (#dc2626) — the brand may use a different error color or include an icon.
- The exact font stack is uncertain: "Nunito Sans" was found in the CSS but may be paired with a secondary font for headings or used only in specific sections. The fallback stack is a best-guess.
- Dark mode is not implemented on the live site — all colors assume a light theme.
- The brand's sub-brand or seasonal color palettes (e.g., holiday collections) were not extractable.
- Animation durations and easing curves (button press, card hover, toast slide-in) were not found in the extracted data — standard 200-300ms ease-in-out is assumed.
- The checkout flow uses Shopify's default styling, which may differ from the brand's design system — colors like #2563eb (Shopify blue) and #3b5998 (Facebook) appear in the extracted list but are likely widget defaults, not brand colors.
- The exact shade of the accent-yellow (#fbcd0a) and accent-lavender (#a89cc8) may vary slightly between product badges and UI elements — these are the most frequently occurring values.
- The star-rating color (#fbcd0a) is assumed from the yellow accent — the actual rating widget may use a different yellow or include half-star rendering.
- The "sold out" badge styling is inferred — the live site may use a different opacity or include a "Notify Me" button instead.
