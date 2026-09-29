---
version: alpha
name: "Meletrix"
source_url: "https://meletrix.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A desktop art creator that builds keyboards as if they were gallery pieces — the brand's visual system is anchored on a deep, almost-black ink (#212121) against a warm off-white canvas (#f9fafb), with a single electric accent in #108474 that appears in product highlights, hover states, and select badges. The extracted palette reveals a surprisingly playful secondary language: a marigold (#ffeb3c) and neon chartreuse (#e2ff3f) appear in limited-edition keycap sets and packaging accents, while #de3813 (a rusted orange) and #5d6ac0 (a muted periwinkle) suggest a brand that's comfortable with color-blocking and unexpected pairings. The typography runs Jost at display sizes — a geometric sans with humanist warmth — paired with Nunito Sans for body copy, creating a system that feels both precise and approachable. Cards use generous padding ({spacing.lg}) and soft radii ({rounded.md}), while the primary CTA button takes a full-pill shape ({rounded.full}) in the brand teal, creating a single focal point per view. The nav bar is minimal — a thin hairline (#e9e9e9) separates it from content, and the logo sits left with a compact product-menu strip. Product cards feature a large hero image (often a full-keyboard flat lay), a bold price in display weight, and a subtle "in stock" badge in #2a8156. The checkout flow uses Shopify's default widget colors, which introduce a cooler gray (#7b7b7b) and a lighter surface (#f2f2f2) that don't fully match the brand's warmer palette — a known gap. Overall, Meletrix reads as a brand that treats mechanical keyboards as functional art: the design system is clean enough to let the product photography sing, but playful enough to accommodate limited-edition drops with neon accents and custom keycap sets.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d4c9"
  ink: "#212121"
  body: "#414141"
  muted: "#7b7b7b"
  muted-soft: "#bbbbbb"
  hairline: "#e9e9e9"
  hairline-soft: "#f2f2f2"
  canvas: "#f9fafb"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffeb3c"
  accent-chartreuse: "#e2ff3f"
  accent-rust: "#de3813"
  accent-periwinkle: "#5d6ac0"
  badge-green: "#2a8156"
  badge-purple: "#8e24aa"
  stock-green: "#267860"
  star-yellow: "#fbcd0a"
  star-yellow-active: "#f4f80a"
  error-red: "#de3813"
  link-blue: "#5d6ac0"

typography:
  display-xl:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Jost', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  button-accent-chartreuse:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.error-red}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-limited:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: "16px 32px"
    height: 56px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  badge-in-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-pre-order:
    backgroundColor: "{colors.badge-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-rust}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-yellow}"
    size: 16px
  star-rating-active:
    color: "{colors.star-yellow-active}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a full-pill in the brand teal (#108474). Used for "Add to Cart", "Pre-order", and primary checkout flows. On hover, it shifts to a slightly darker teal (#0d6b5e). The disabled state uses a muted teal (#a3d4c9) with reduced opacity. Text is white, set in Jost 16px/600 with 0.2px letter spacing.

**`button-secondary`** — An outlined variant with a white fill and a 2px hairline border (#e9e9e9). Used for secondary actions like "View Details" or "Compare". On hover, the border switches to the brand teal. Text is ink (#212121). The pill shape matches the primary button for visual consistency.

**`button-tertiary`** — A text-only button with no background or border, used for less prominent actions like "Learn More" or "Cancel". Text is the brand teal. On hover, a soft surface background (#f2f2f2) appears behind the text. The pill shape is maintained for alignment with the button system.

**`button-accent-marigold`** and **`button-accent-chartreuse`** — Limited-use accent buttons for special promotions, limited-edition drops, or seasonal campaigns. These use the brand's secondary palette (#ffeb3c and #e2ff3f) with dark ink text. They are smaller (40px height) and use button-sm typography. These should be used sparingly to maintain their impact.

### Cards
**`product-card`** — The primary product display unit, a white card with 12px rounded corners and 16px padding. Contains a square product image (1:1 aspect ratio) with 8px rounded corners, a title in title-sm, a price in price-display (22px/600), and an optional badge. On hover, a subtle box shadow (0 4px 12px rgba(0,0,0,0.08)) lifts the card. Badges appear in the top-left corner of the image area.

**`product-card-badge`** — A small uppercase label (11px/600, 0.5px letter spacing) with 4px rounded corners. Three variants exist: green (#2a8156) for "In Stock", gray (#7b7b7b) for "Sold Out", and marigold (#ffeb3c) for "Limited Edition". The marigold variant uses dark ink text for contrast.

### Navigation
**`nav-bar`** — A 72px-tall white bar with a thin bottom border (#e9e9e9). Contains the brand logo on the left and navigation links (nav-link: 14px/500) on the right. Active links use the brand teal; inactive links use muted gray (#7b7b7b). On mobile, the nav collapses into a hamburger menu.

**`nav-link-active`** and **`nav-link-inactive`** — Simple text-based navigation states. No background or border — just color changes. The active state uses the brand teal to indicate the current section.

### Forms
**`text-input`** — A standard text input with a white background, 8px rounded corners, and a 1px hairline border. On focus, the border thickens to 2px and switches to the brand teal. Error state uses a 2px rust-red (#de3813) border. Disabled state uses a soft gray background (#f2f2f2) with muted text.

**`search-bar`** — A full-pill search input with 48px height, white background, and a 1px hairline border. On focus, the border becomes 2px teal. Used in the header and on collection pages.

### Footer
**`footer`** — A dark footer with a deep ink (#212121) background and muted-soft (#bbbbbb) text. Links are set in link typography (14px/400) and turn white on hover. Padding is generous at 48px vertical and 16px horizontal. The footer typically contains three columns: brand info, support links, and social/legal links.

### Badges & Indicators
**`badge-in-stock`** — Green (#267860) badge with white text, 4px rounded corners, and 2px/8px padding. Used on product cards and product detail pages to indicate availability.

**`badge-pre-order`** — Purple (#8e24aa) badge for pre-order items. Same shape and size as in-stock badge.

**`badge-new`** — Rust-red (#de3813) badge for newly released products. Same shape and size.

**`star-rating`** — A 16px star icon in marigold (#fbcd0a) for the base rating. Active/hovered stars use a slightly brighter yellow (#f4f80a). Used on product cards and review sections.

### Dividers
**`divider`** and **`divider-soft`** — Simple 1px horizontal lines. The standard divider uses hairline (#e9e9e9); the soft variant uses hairline-soft (#f2f2f2). Used to separate sections within cards, between product rows, and in the footer.

### Filter Chips
**`filter-chip`** — A pill-shaped filter toggle with a white background, 1px hairline border, and 8px/16px padding. Active chips fill with the brand teal and white text. Used on collection pages for filtering by switch type, layout, or price range.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav collapses to hamburger, hero section reduces padding to 32px, filter chips wrap to 2 per row, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid (2 cards per row), nav links remain visible but reduce font size to 13px, hero uses 28px display, filter chips show in a horizontal scrollable strip |
| Desktop | 1128–1440px | Three-column product grid (3 cards per row), full nav with all links, hero uses 36px display, filter chips in a 3-column grid, footer in 3-column layout |
| Wide | > 1440px | Four-column product grid (4 cards per row), max-width container at 1440px centered, hero section uses 40px display, increased padding on cards to 24px |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Filter chips are 40px tall with 16px horizontal padding for easy tapping
- Product card images include a full-surface tap target (no dead zones)
- Nav links have 44px minimum tap area even when text is smaller
- Search bar is 48px tall with generous internal padding

### Collapsing Strategy
- On mobile (< 744px), the nav bar collapses to a hamburger icon with a slide-in drawer menu
- Filter chips collapse from a visible grid to a horizontal scrollable strip on tablet, and to a single "Filter" button on mobile that opens a modal
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer collapses from 3 columns to a single stacked column on mobile
- Hero section collapses from a two-column layout (image + text) to a single-column stack on tablet and mobile
- Secondary navigation (category strip) collapses to a dropdown on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While hover colors are inferred for primary buttons and cards, many hover/focus/active states for secondary elements (filter chips, nav links, footer links) are based on common patterns rather than extracted data. The exact hover transition timing and easing functions are unknown.
- **Error and validation styling**: The error state for text inputs uses a rust-red (#de3813) based on the extracted palette, but the exact error message styling (position, icon, animation) is not confirmed.
- **Dark mode**: No dark mode implementation was detected. The brand's dark footer suggests some dark-surface thinking, but a full dark mode palette is not available.
- **Sub-brand palettes**: The extracted colors include several accents (marigold, chartreuse, periwinkle, rust) that may belong to specific product lines or limited editions rather than the core system. Their usage rules are inferred.
- **Typography hierarchy**: Jost and Nunito Sans were found in the CSS, but exact font sizes, weights, and line heights for each level are inferred from common patterns. The extracted data did not include specific font-size declarations for each token.
- **Spacing system**: The spacing scale is based on common 4px/8px increments. The actual spacing values used in the live site may differ.
- **Component-specific radii**: While the button system uses full-pill shapes, the exact radii for cards, inputs, and badges are inferred from common values. The extracted data did not include specific border-radius declarations.
- **Shopify checkout widgets**: The checkout flow uses Shopify's default widget colors, which introduce cooler grays (#7b7b7b, #f2f2f2) that don't match the brand's warmer palette. These are not part of the Meletrix design system.
- **Animation and transition values**: No timing functions, durations, or easing curves were extracted. Standard 200-300ms ease-in-out transitions are assumed.
- **Icon system**: The extracted data did not include icon specifications. The brand likely uses custom SVG icons for keyboard layouts, switches, and keycaps, but their styling is unknown.
