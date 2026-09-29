---
version: alpha
name: "Womier"
source_url: "https://womierkeyboard.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A keyboard brand that speaks through its materials — the extracted palette reveals a teal-green anchor at #108474, a color that appears nowhere in the social-icon or checkout-widget noise, and that carries the entire visual identity across buttons, badges, and accent lines. The site runs on a near-white canvas (#fafafa, #f9f9f9, #f9fafb) with a secondary teal at #c1e6e6 and a tertiary mint at #c5f7f0, creating a cool, aqueous atmosphere that contrasts with the warm yellow (#fbcd0a) used sparingly for sale badges and price highlights. The typography stack is Nunito Sans — a rounded, approachable sans-serif — set at modest weights (400–700) with generous line heights that make dense product grids feel airy. Buttons use the primary teal at {rounded.sm} with white text, while secondary actions drop to a soft #eeeeee background with #555555 ink. Product cards float on white with a #dedede hairline, and the footer collapses into a dense column of #555555 links on #f2f2f2. The brand's design moves are functional: the search bar is a pill-shaped field at {rounded.full}, category tabs are underlined on active state, and the cart badge appears as a #108474 circle with white numeral. There is no hero video or full-bleed imagery — the site trusts product photography against clean, spaced grids, with the teal acting as the single voltage that says "click here."

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#a3d4c4"
  ink: "#121212"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fbcd0a"
  accent-mint: "#c5f7f0"
  accent-teal-light: "#c1e6e6"
  badge-sale: "#fbcd0a"
  badge-new: "#108474"
  star-rating: "#fbcd0a"
  social-facebook: "#3b5998"
  social-twitter: "#1da1f2"
  social-pinterest: "#e60023"
  social-linkedin: "#0073b1"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
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
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  price:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
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
    backgroundColor: "#eeeeee"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "0 {spacing.base} {spacing.sm}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    padding: "0 {spacing.base} {spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.body}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  filter-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the brand teal #108474 on white. Rounded at {rounded.sm} with 12px vertical padding and 24px horizontal, set in Nunito Sans 600 weight. On hover, shifts to {colors.primary-active} (#0d6b5c). Disabled state uses {colors.primary-disabled} (#a3d4c4) with white text.

**`button-secondary`** — Used for less prominent actions like "View All" or "Cancel." Background is a soft #eeeeee with #555555 body text. Active state darkens to {colors.hairline} (#dedede). Same dimensions and typography as primary.

**`button-tertiary-text`** — A text-only link styled as a button, using the primary teal for the text color. No background, no border. Used for "Learn More" links in product descriptions and footer navigation.

**`button-pill-primary`** — A compact, fully rounded variant used for quick actions like "Add to Cart" in mobile views or filter tags. Uses {rounded.full} with 10px vertical padding, 20px horizontal, and 40px height.

### Navigation
**`top-nav`** — Fixed at 64px height on a white (#fafafa) canvas. Links are set in Nunito Sans 600 at 15px with #555555 body color. Active page or hover state switches text to {colors.primary} with a 2px solid underline in the same teal. The logo sits left-aligned; the cart icon with badge and account link sit right-aligned.

**`nav-link`** — Standard navigation link with 8px vertical and 12px horizontal padding. No background, no border-radius. Active state adds a bottom border in {colors.primary}.

### Cards
**`product-card`** — The core product display unit. A white card with {rounded.md} (12px) corners, no shadow, relying on the product image to do the visual work. The image itself has rounded top corners ({rounded.md} {rounded.md} 0 0). Title uses {typography.title-sm} (16px, 600 weight) with 8px horizontal padding. Price sits below in {typography.price} (16px, 700 weight). Sale prices render in {colors.accent-yellow} (#fbcd0a).

**`badge-sale`** — A small yellow pill (#fbcd0a) with black text, set in 11px uppercase bold with 0.5px letter spacing. Used to flag discounted items on product cards and collection pages.

**`badge-new`** — Same dimensions as sale badge but uses the brand teal (#108474) on white. Marks newly added products.

### Forms & Search
**`search-bar`** — A pill-shaped input field at {rounded.full} with a 1px #dedede border. White background, 14px placeholder text in #7b7b7b. On focus, the border thickens to 2px and switches to {colors.primary}. Height is 40px with 10px vertical padding.

**`filter-dropdown`** — Used on collection pages for sorting and filtering. A white box with {rounded.sm} and a 1px #dedede border. Text is 14px in #555555. Dropdown arrow is implied; the component uses native select styling.

### Badges & Indicators
**`cart-badge`** — A 20px circle in {colors.primary} with white text at 12px. Positioned absolutely over the cart icon in the top nav. Shows the item count.

**`star-rating`** — Rendered as filled stars in {colors.accent-yellow} (#fbcd0a) at 14px. Used on product cards and review sections.

### Footer
**`footer`** — A full-width band at #f2f2f2 with #555555 body text. Section headings use {typography.title-sm} (16px, 600 weight) in #121212. Links are 14px regular weight with no underline. Padding is 48px vertical, 16px horizontal. On mobile, columns stack vertically.

### Pagination
**`pagination-button`** — Used on collection and search result pages. A white box with {rounded.sm} and a 1px #dedede border. Active page uses {colors.primary} background with white text. Inactive pages use white background with #555555 text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item per row); top nav collapses to hamburger menu; footer columns stack vertically; search bar becomes full-width; filter dropdowns become full-width accordion panels; product card images scale to 100% width |
| Tablet | 744–1128px | Two-column product grid; top nav shows limited links (Home, Shop, About) with hamburger for rest; footer columns in 2x2 grid; search bar remains pill but shrinks to 60% width |
| Desktop | 1128–1440px | Three-column product grid; full top nav with all links visible; footer in 4-column layout; search bar at 320px fixed width; filter sidebar visible on collection pages |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered; increased whitespace around sections; search bar expands to 400px |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Icon buttons (cart, account, search) are 36px circles — meets minimum 44px touch target with padding
- Product card tap targets (title, price, image) are the full card width
- Filter dropdowns and pagination buttons are minimum 40px tall
- Navigation links have 8px vertical padding for comfortable tapping

### Collapsing Strategy
- Top nav: On mobile (< 744px), all navigation links collapse behind a hamburger icon. The logo and cart icon remain visible.
- Footer: On mobile, the 4-column layout collapses to a single vertical stack. Each section heading becomes a tap-to-expand accordion.
- Product grid: Reduces from 4 columns on wide to 1 column on mobile. Padding between cards reduces from 24px to 12px.
- Filter sidebar: On desktop, filters appear as a persistent left sidebar. On tablet and mobile, filters collapse into a top bar with dropdowns or a slide-out drawer.
- Search bar: On mobile, the search bar expands to full width below the nav. On desktop, it sits inline in the nav at a fixed width.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted from static CSS — only primary button hover (#0d6b5c) and nav link hover (teal underline) are confirmed. All other hover colors are inferred from the active state pattern.
- Error styling (form validation, 404 page, error messages) was not visible in the extracted data. No error red or warning orange appeared in the palette.
- Dark mode is not present on the live site — no dark theme tokens exist in the extracted colors.
- The exact font weight for Nunito Sans in headings (600 vs 700) is inferred from common usage; the site may use 700 for display-xl.
- Product card shadow/depth was not extractable — the cards appear flat (no box-shadow in extracted CSS). If shadows exist, they are very subtle.
- The secondary teal (#c1e6e6) and mint (#c5f7f0) usage is inferred from their frequency in the palette but exact component assignments (backgrounds, borders, hover states) are speculative.
- Star rating size and exact rendering (half-stars, empty state) could not be confirmed from extracted data.
- The social media icon colors (#3b5998, #1da1f2, etc.) are standard brand colors and may not reflect the site's actual implementation.
- The extracted palette includes several near-white shades (#f9fafb, #f9f9f9, #fafafa) — the exact canvas color may vary by section. #fafafa is used as the primary canvas, but some sections may use #ffffff or #f9f9f9.
- No animation or transition timing values were extractable from the static CSS analysis.
