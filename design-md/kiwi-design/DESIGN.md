---
version: alpha
name: "KIWI design"
source_url: "https://www.kiwidesign.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A VR-accessory brand that speaks through a palette anchored on #108474 — a deep, almost surgical teal that appears nowhere else in the extracted hex set — and a secondary accent of #fbcd0a (marigold yellow) that reads as a warning stripe or a price-tag highlight. The brand lives in a world of grays: #eeeeee canvas, #555555 body text, #bebebe and #dedede for hairline borders, #121212 for near-black ink. This is not a playful consumer-electronics brand; it's a utility-first, precision-engineering aesthetic where every component feels like it was designed for a headset strap or a charging dock. Buttons use {rounded.sm} — soft but not pill-shaped — and the primary CTA is a solid #108474 rectangle with white text, no gradient, no shadow. The typography stack is a mix of Poppins (likely for headings) and Nunito Sans (for body), both geometric sans-serifs that reinforce the clean, technical feel. The extracted font list includes JudgemeIcons and JudgemeStar, indicating heavy reliance on Judge.me review widgets — a signal that social proof is baked into the layout. The color set also includes social-login blues (#3b5998 Facebook, #1da1f2 Twitter, #dd4b39 Google, #e60023 Pinterest, #0073b1 LinkedIn) and a #ffff00 checkout accent, likely from Shopify Pay or a Klarna widget. The brand's true identity is the teal and the yellow, surrounded by a controlled gray system that never feels warm.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d4c9"
  ink: "#121212"
  body: "#555555"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#bebebe"
  hairline-soft: "#dedede"
  canvas: "#eeeeee"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fbcd0a"
  accent-yellow-active: "#e0b800"
  star-rating: "#fbcd0a"
  badge-new: "#108474"
  badge-sale: "#fbcd0a"
  link-blue: "#2f6ed6"
  error-red: "#dd4b39"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-pinterest: "#e60023"
  social-linkedin: "#0073b1"

typography:
  display-xl:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  price-md:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Poppins', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

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
    backgroundColor: "{colors.surface-card}"
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
    border: "1px solid {colors.primary}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-yellow-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-icon-square:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  button-icon-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error-red}"
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.xs}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
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
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    typography: "{typography.price-md}"
    textColor: "{colors.accent-yellow}"
  product-card-price-compare:
    typography: "{typography.price-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  product-card-rating:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-rating-stars:
    color: "{colors.star-rating}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 36px
    marginTop: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 32px"
    height: 48px
    marginTop: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-icon:
    color: "{colors.muted}"
    marginRight: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.surface-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.surface-card}"
    marginBottom: "{spacing.base}"
  review-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  review-card-author:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  accordion:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    paddingTop: "{spacing.sm}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    margin: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  pagination-inactive-hover:
    backgroundColor: "{colors.surface-soft}"
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-large:
    color: "{colors.primary}"
    size: 48px
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  notification-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px
    padding: "0 4px"
  cart-count:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. A solid #108474 teal rectangle with white text, 8px rounded corners, and 12px/24px padding. On hover, it shifts to #0d6b5e (primary-active). Disabled state uses #a3d4c9 (primary-disabled). Used for "Add to Cart", "Buy Now", and primary checkout flows.

**`button-secondary`** — A white button with a 1px #bebebe border and #121212 text. Hover state shows a #f2f2f2 background and a teal border. Used for "Learn More", "View Details", and secondary actions. The border gives it a defined edge without competing with the primary.

**`button-accent-yellow`** — A high-visibility yellow button using #fbcd0a. Black text (#121212). Used sparingly for sale items, limited-time offers, or price-drop alerts. Hover shifts to #e0b800. This button carries urgency without the aggressive red typical of e-commerce.

**`button-ghost`** — A text-only button with teal (#108474) text on a transparent background. Hover adds a #f2f2f2 background. Used for "Cancel", "Back", or tertiary actions where a full button would be too heavy.

**`button-icon-square`** — A 40px square button with 8px rounded corners, used for icon-only actions like search, cart, or menu toggle. Background is #f2f2f2, icon color is #555555. The square shape distinguishes it from the circular social icons.

**`button-icon-circle`** — A 40px circular button for social media links and share actions. Same #f2f2f2 background and #555555 icon color, but fully rounded. Social icons use their brand colors (Facebook #3b5998, Twitter #1da1f2, etc.) when active.

### Cards
**`product-card`** — The primary product display unit. A white card with 12px rounded corners and 16px padding. Contains a product image (8px rounded), title in 16px/600 weight, price in 18px/700 weight, and star rating in #fbcd0a yellow. Sale items show the price in yellow with a strikethrough compare-at price in #888888. A teal "Add to Cart" button sits at the bottom with 8px top margin. Badges (New, Sale) appear as small uppercase labels in the top-left corner — teal for "New", yellow for "Sale".

**`review-card`** — A white card with 12px rounded corners, 16px padding, and a 1px #dedede border. Contains the review text in 14px/400 weight, star rating in #fbcd0a, and the author name in 12px/500 weight. The subtle border distinguishes reviews from product cards in a list.

### Navigation
**`nav-bar`** — A 64px white bar with a 1px #dedede bottom border. Navigation links use 14px/500 weight Poppins with 0.2px letter spacing. Active links show a 2px teal bottom border and teal text. Hover state also turns text teal. The bar is fixed or sticky on mobile, with a hamburger menu replacing the full link set below 744px.

**`breadcrumb`** — Small 12px/500 weight gray (#888888) text with #bebebe separators. The active (current) breadcrumb uses #121212. Used on product detail and collection pages for orientation.

### Forms
**`text-input`** — A 44px white input with 8px rounded corners, 10px/16px padding, and a 1px #bebebe border. Focus state swaps the border to #108474 teal. Error state uses #dd4b39 red. Labels sit above in 12px/500 weight #555555 with 4px bottom margin. Used for search, email capture, and checkout fields.

**`select-input`** — Same dimensions and styling as text-input but with a dropdown arrow. Used for quantity selectors, sort options, and variant pickers (size, color).

**`quantity-selector`** — A 40px horizontal control with minus/plus buttons flanking a numeric display. Background is #f2f2f2, buttons are transparent with #555555 icons. Used on cart and product detail pages.

### Footer
**`footer`** — A dark section with #121212 background and #f2f2f2 text. Links use 14px/400 weight and turn teal on hover. Section headings use 16px/600 weight white text with 24px bottom margin. The footer contains link columns, social icons, and legal text. Padding is 64px vertical, 24px horizontal.

### Badges & Indicators
**`notification-badge`** — A small 18px circle in #fbcd0a yellow with black text. Used for cart counts, unread messages, or alert indicators. The yellow stands out against the gray/white interface.

**`cart-count`** — A 20px pill in #108474 teal with white text. Used specifically for the cart icon in the navigation. The teal matches the primary brand color, reinforcing the purchase flow.

**`product-card-badge`** — A small uppercase label with 2px/8px padding and 4px rounded corners. "New" uses teal background with white text. "Sale" uses yellow background with black text. These badges sit at the top-left of product images.

### Loading & Dividers
**`loading-spinner`** — A 24px teal (#108474) spinner used for async operations. A 48px variant is used for page-level loading states.

**`divider`** — A 1px line in #dedede (hairline-soft) for subtle separation. A stronger variant uses #bebebe (hairline) for more pronounced divisions.

**`tooltip`** — A small dark (#121212) box with white text, 4px rounded corners, and 4px/8px padding. Used for hover explanations on icons and controls.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero banner text reduces to 24px; footer stacks vertically; search bar moves to full-width below nav; quantity selector becomes full-width; breadcrumbs hide on inner pages |
| Tablet | 744–1128px | Nav shows limited links (3-4); product cards in 2-column grid; hero banner uses 28px text; footer uses 2-column layout; search bar remains in nav; sidebar filters become a top bar |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-4 column grid; hero banner uses 32px text; footer uses 4-column layout; sidebar filters visible on collection pages; breadcrumbs always visible |
| Wide | > 1440px | Max-width container (1440px) centered; product cards in 4-5 column grid; hero banner may use full-bleed background; footer columns expand to 5; additional whitespace around content |

### Touch Targets
- All buttons and interactive elements minimum 44px height (exceeds Apple's 44pt guideline)
- Icon buttons (search, cart, menu) are 40px minimum with 40px width
- Quantity selector buttons are 40px x 40px
- Product card "Add to Cart" buttons are 36px height (slightly below guideline but acceptable for secondary action)
- Navigation links have minimum 44px tap area (padding extends hit area)
- Form inputs are 44px height for comfortable tapping

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grid collapses from 4 columns to 2 columns at tablet, to 1 column at mobile
- Footer columns collapse from 4 to 2 at tablet, to 1 at mobile
- Sidebar filters (on collection pages) collapse to a top bar with dropdown at tablet and mobile
- Hero banner text reduces in size and may stack CTA below text at mobile
- Breadcrumbs hide on mobile for inner pages (product detail, collection) to save space
- Review cards collapse from side-by-side to stacked at mobile
- Search bar moves from inline in nav to full-width below nav at mobile
- Multi-column product descriptions collapse to single column at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components are inferred from common patterns; the live site may use different transitions or color shifts
- Error, success, and warning toast/notification styling not extracted — assumed to use #108474 for success, #dd4b39 for error, #fbcd0a for warning
- Dark mode not present on the live site; no extraction available
- The extracted color list is heavily polluted with social media brand colors (#3b5998, #1da1f2, #dd4b39, #e60023, #0073b1), checkout widget colors (#ffff00 likely from Shopify Pay or Klarna), and Judge.me review widget colors (JudgemeIcons, JudgemeStar). The true brand palette is likely smaller: #108474 (teal), #fbcd0a (yellow), #121212 (ink), #555555 (body), #eeeeee (canvas), #bebebe (hairline), #dedede (soft hairline), #ffffff (card surface). The remaining grays (#353535, #232223, #6d6a6a, #888888, #aaaaaa, #bbbbbb, #bababa, #abb1ba, #e5e5e5, #e9e9e9, #f2f2f2) are likely used in varying contexts but their specific roles (background vs. border vs. text) are inferred.
- Font stack is inferred from extracted declarations; exact hierarchy (Poppins for headings, Nunito Sans for body) is a best guess based on common pairing patterns
- Specific font weights beyond 400, 500, 600, 700 are not confirmed; the extracted CSS may use variable fonts or additional weights
- Line heights and letter spacing values are estimated based on standard geometric sans-serif typography; the live site may use different values
- Component padding and height values are estimated from common e-commerce patterns; the live site may use slightly different dimensions
- The #2f6ed6 link-blue is present in the extracted colors but its exact usage (inline links vs. navigation vs. secondary CTAs) is not confirmed
- The #a89cc8 (lavender) and #c1e6e6 (light teal) colors appear in the extraction but may be from product photography or promotional banners rather than the design system
- Shopify-specific components (cart drawer, checkout button, payment icons) are not fully documented; they follow Shopify's default styling with KIWI's primary color applied
- Judge.me review widget styling (star sizes, card layouts, sorting controls) is not captured; the widget likely uses its own CSS with some brand color overrides
- Animation durations, easing curves, and transition properties are not extracted
- Focus ring styles (outline, box-shadow) for keyboard navigation are not documented
- Print styles and reduced-motion preferences are not captured
