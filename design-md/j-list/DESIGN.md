---
version: alpha
name: "J-List"
source_url: "https://www.jlist.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-catalog anime and Japanese pop-culture storefront that runs on a high-contrast, information-dense grid anchored by a deep-navy ink (#163959) and a single red voltage (#bd2426) that marks every add-to-cart, sale badge, and critical action. The palette is surprisingly industrial for a hobbyist brand — the extracted hexes show a heavy reliance on cool grays (#404040, #595959, #737373) and crisp whites (#ebebeb, #dedede) that give the site the feel of a well-organized warehouse rather than a fan-art gallery. Blue accents (#62a1d8, #2f7bbf, #0051c3) appear in navigation and link states, while a muted green (#9bca3e, #bada7a, #516b1d) signals stock availability and pre-order status. The type system defaults to system fonts (Arial, Helvetica Neue, Roboto) with a monospace fallback for code-like elements, suggesting an engineer-built experience that prioritizes load speed and readability over brand typography. Buttons are sharp-cornered (`{rounded.none}`) for primary actions and softly rounded (`{rounded.sm}`) for secondary, creating a visual hierarchy that says "this is a functional tool, not a toy." The product grid is dense — thumbnails at 200px with tight 8px gutters — and each card carries a red price badge, a green stock indicator, and a small-font title in 13px body text. The overall effect is utilitarian, trustworthy, and built for the power user who knows exactly what they want.

colors:
  primary: "#bd2426"
  primary-active: "#a01e1f"
  primary-disabled: "#e8a0a1"
  ink: "#163959"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#62a1d8"
  accent-blue-dark: "#2f7bbf"
  accent-blue-deep: "#0051c3"
  stock-green: "#9bca3e"
  stock-green-dark: "#516b1d"
  stock-green-light: "#bada7a"
  sale-orange: "#f68b1f"
  sale-orange-dark: "#c16508"
  sale-orange-deep: "#904b06"
  badge-red: "#de5052"
  badge-red-dark: "#521010"
  link-blue: "#0051c3"
  link-hover: "#2f7bbf"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.3px
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  mono:
    fontFamily: "Courier, monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
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
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 6px 12px
    height: 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
    rounded: "{rounded.sm}"
  nav-link-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
    rounded: "{rounded.sm}"
  nav-link-accent:
    backgroundColor: transparent
    textColor: "{colors.accent-blue-dark}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px
  product-card-image:
    rounded: "{rounded.sm}"
    height: 200px
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.primary}"
    marginTop: "{spacing.xs}"
  product-card-stock:
    typography: "{typography.caption-bold}"
    textColor: "{colors.stock-green-dark}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-preorder:
    backgroundColor: "{colors.sale-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.link}"
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.sm}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-md}"
    padding: "{spacing.xl} {spacing.base}"
    height: 300px
  hero-banner-cta:
    backgroundColor: "{colors.sale-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.sm}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.link-blue}"
  breadcrumb-current:
    typography: "{typography.caption-bold}"
    textColor: "{colors.body}"

## Components

### Buttons
**`button-primary`** — The workhorse action across the site, rendered in the brand's signature red (#bd2426) with sharp zero-radius corners that signal urgency and decisiveness. On hover, it deepens to `{colors.primary-active}` (#a01e1f) with no border or shadow shift — the color change alone carries the feedback. The disabled state fades to a pale rose (#e8a0a1) with `{colors.on-primary}` text still legible. Used for "Add to Cart," "Checkout," and "Sign Up" flows.

**`button-secondary`** — A white button with a 1px `{colors.hairline}` border and `{rounded.sm}` corners, used for "View Details," "Cancel," and secondary checkout actions. The active state fills the background with `{colors.hairline-soft}` (#ebebeb) to provide a subtle press effect without competing with the primary button's red.

**`button-ghost`** — A text-only button with no background or border, used for "Learn More," "Read Reviews," and inline navigation within product cards. Hover adds a faint `{colors.surface-soft}` background at 8px padding to create a touch target without visual weight.

**`button-small`** — A compact 28px-tall red button for inline actions like "Add to Wishlist," "Compare," and quantity adjusters in the cart. Uses `{typography.button-sm}` at 12px/600 weight to fit tight spaces while maintaining the brand's red urgency.

### Navigation
**`nav-bar`** — A fixed 56px white bar at the top of every page, carrying the J-List logo on the left, category links in the center, and search + account icons on the right. The bar uses a 1px `{colors.hairline}` bottom border to separate it from content. On scroll, it gains a subtle `box-shadow: 0 2px 4px rgba(0,0,0,0.08)` for depth.

**`nav-link`** — Standard navigation links in 14px/600 weight with `{colors.ink}` text and 8px horizontal padding. The active state adds a light gray `{colors.surface-soft}` background with `{rounded.sm}` to indicate the current section without using an underline or heavy border.

**`nav-link-accent`** — A blue-tinted variant (`{colors.accent-blue-dark}`) used for premium or exclusive category links (e.g., "Limited Edition," "Pre-Order Now") to differentiate them from standard browsing links.

### Search
**`search-bar`** — A pill-shaped input (`{rounded.full}`) with 16px left padding and a search icon, rendered at 40px height. The placeholder text uses `{colors.muted}` (#595959) and the input border is `{colors.hairline}`. On focus, the border switches to `{colors.accent-blue}` (#62a1d8) and the background remains white — no shadow or glow, keeping the interface clean.

### Cards
**`product-card`** — A 200px-wide white card with `{rounded.sm}` and 8px padding, containing a thumbnail image, title in `{typography.body-sm}`, price in red `{typography.price-sm}`, and a stock indicator in green `{typography.caption-bold}`. The card has no border — it relies on the white-on-white grid with 8px gutters for separation. Hover adds a 1px `{colors.hairline}` border and a subtle `translateY(-2px)` lift.

**`product-card-image`** — The top section of the card, a 200px-tall image container with `{rounded.sm}` at the top corners. Images are cropped to 1:1 aspect ratio and use `object-fit: cover`. A badge overlay (sale, new, pre-order, out-of-stock) sits at the top-left with 4px offset.

### Badges
**`badge-sale`** — A red (#de5052) uppercase badge in 11px/700 weight with `{rounded.xs}` (2px) corners and 2px/6px padding. Used on product cards to flag discounts, clearance items, or limited-time offers. The text is white and tightly tracked at 0.5px.

**`badge-new`** — A blue (#62a1d8) variant for newly added products, using the same sizing and typography as the sale badge but with a different color to distinguish the signal type.

**`badge-preorder`** — An orange (#f68b1f) variant for items available for pre-order, matching the same badge structure but using the brand's accent orange to indicate future availability.

**`badge-out-of-stock`** — A gray (#737373) variant for unavailable items, using the same badge structure but with muted tones to visually deprioritize the product without removing it from the grid.

### Footer
**`footer`** — A deep-navy (#163959) full-width footer with white text in `{typography.body-sm}`, containing three columns: customer service links, company information, and social media icons. Links use `{colors.accent-blue}` (#62a1d8) for visibility against the dark background. The footer has 32px vertical padding and a 48px top margin from the content above.

### Hero
**`hero-banner`** — A 300px-tall dark (#163959) banner with white display text, used for seasonal promotions, new arrivals, and category spotlights. The background may feature a product image at 50% opacity. A single CTA button in orange (`{colors.sale-orange}`) sits below the headline, using the same zero-radius corners as the primary button but in a contrasting color to draw attention.

### Pagination
**`pagination`** — A horizontal row of numbered page links in `{typography.body-sm}` with `{rounded.sm}`. The active page uses `{colors.primary}` background with white text; inactive pages use transparent background with `{colors.body}` text. Previous/Next arrows sit at the ends with the same styling.

### Breadcrumbs
**`breadcrumb`** — A horizontal navigation trail in `{typography.caption}` (12px) with `{colors.muted}` text and ">" separators. Links use `{colors.link-blue}` (#0051c3) and the current page uses `{typography.caption-bold}` in `{colors.body}`. No background or border — just text on the canvas.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card wide); nav-bar collapses to hamburger menu; search bar moves below nav; hero banner reduces to 200px height; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows top-level categories only (secondary in hamburger); search bar remains in nav but shrinks to 32px height; hero banner at 250px |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all categories visible; search bar at full 40px height; hero banner at 300px; footer in three columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px centered; all elements scale proportionally; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px on mobile
- Product card tap targets expand to the full card area (not just the title/price)
- Nav-bar hamburger icon is 48x48px with 8px internal padding
- Pagination page numbers are 40x40px minimum on mobile
- Category strip tabs have 44px minimum height with 12px horizontal padding

### Collapsing Strategy
- Nav-bar collapses to hamburger menu at < 744px, with a slide-out drawer containing all categories and account links
- Category strip collapses to a horizontal scrollable row at < 744px, with the active category pinned to the left
- Product grid collapses from 3 columns to 2 at tablet, and 1 at mobile
- Footer collapses from 3 columns to a single stacked column at < 744px
- Search bar collapses from a full-width input to an icon-only button at < 744px, expanding to a full overlay on tap
- Hero banner text and CTA stack vertically at < 744px instead of the desktop side-by-side layout

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs, select inputs, and search bars could not be reliably extracted from the live site — the extracted CSS may not have included `:focus` or `:hover` pseudo-class styles
- Error state styling for form inputs (red border, error message typography) was not present in the extracted data
- Dark mode or high-contrast mode variants are not defined — the site appears to ship a single light theme
- Sub-brand or seasonal color palettes (e.g., holiday themes, limited-edition drops) could not be extracted
- The exact font stack for the site is system-default (`-apple-system, Arial, BlinkMacSystemFont, Helvetica Neue, Oxygen, Roboto, Segoe UI, Ubuntu, courier, monaco, monospace, sans-serif!important`) — no custom web font was detected, which is unusual for a DTC brand and may indicate the extraction missed a loaded font file
- Animation and transition durations (e.g., button hover, card lift, nav-bar scroll shadow) were not present in the extracted CSS
- The extracted hex colors include a wide range of blues, grays, and accent colors that may include Shopify checkout widgets, social media icons, or stock image dominant tones — the true brand palette may be more limited than the 22 colors listed
- No meta theme-color was found, suggesting the site may not have a browser chrome color set
- The site was behind Cloudflare's "Attention Required" page at extraction time, which may have affected the completeness of the design data captured
