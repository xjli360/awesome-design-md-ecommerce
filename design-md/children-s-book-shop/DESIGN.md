---
version: alpha
name: "The Children's Book Shop"
source_url: "https://www.childrensbookshop.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep red storefront — #842222 — anchors the identity of this Hay-on-Wye children's bookstore, a color that reads less like a brand choice and more like a weathered brick wall or a well-loved book spine. The palette is deliberately restrained: warm parchment tones (#ddddd0, #eeeee0) form the canvas, while a sharp accent yellow (#fff580) appears sparingly for price tags, sale badges, and small interactive flourishes. The site trusts its inventory photography over decorative imagery — every page is a grid of book covers, each one a miniature artwork that carries the visual weight. Typography runs a simple sans-serif stack at modest sizes, never competing with the covers themselves. Navigation is flat and categorical (Picture Books, Middle Grade, Young Adult, Events), with the deep red appearing in the top bar and primary buttons. The overall mood is that of a quiet, serious shop where the books are the decoration — the design steps back and lets the inventory speak.

colors:
  primary: "#842222"
  primary-active: "#882222"
  primary-disabled: "#c5c5c5"
  ink: "#222222"
  body: "#333333"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#c5c5c5"
  hairline-soft: "#ddddd0"
  canvas: "#ddddd0"
  surface-soft: "#eeeee0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fff580"
  accent-yellow-dark: "#ffdd33"
  accent-green: "#10ff10"
  badge-sale: "#fff580"
  badge-new: "#10ff10"

typography:
  display-xl:
    fontFamily: "sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  button-md:
    fontFamily: "sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.xl}"
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    textColor: "{colors.accent-yellow}"
    typography: "{typography.nav-link}"
    borderBottom: "3px solid {colors.accent-yellow}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1.5"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    marginTop: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    textColor: "{colors.accent-yellow}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.xl}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.md} 0"
  category-tab:
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.full}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.md}"
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the deep red `#842222` with white text. Used for "Add to Cart", "Buy Now", and "Subscribe" actions. On hover, shifts to the slightly darker `#882222` active state. Disabled state fades to `#c5c5c5` with white text. The button has a subtle 8px rounded corner (`{rounded.sm}`) and 44px height, making it substantial without being heavy.

**`button-secondary`** — An outlined variant using the same deep red for text and border against the parchment canvas (`{colors.canvas}`). Used for "Learn More", "View Details", and secondary checkout actions. The 2px border maintains visual weight parity with the primary button.

**`button-tertiary`** — A text-only button in the brand red, used for "Read More" links within product descriptions and category navigation. No background or border — just the typography and color, with hover underline.

### Cards
**`product-card`** — The core inventory display unit. A white card (`{colors.surface-card}`) with soft 8px rounding, containing a book cover image at a 1:1.5 aspect ratio, the title in 18px semibold, and the price in the brand red. Cards sit on the warm parchment background (`{colors.canvas}`) with 16px padding and 16px gap between them in a responsive grid.

**`product-card-title`** — Book titles rendered in 18px semibold sans-serif, with 8px top margin from the image. Truncated to two lines with an ellipsis overflow.

**`product-card-price`** — Prices displayed in the brand red `#842222` at 16px regular weight, with 4px top margin from the title. Sale prices appear in the accent yellow badge.

### Badges
**`badge-sale`** — A bright yellow (`#fff580`) pill badge with uppercase 11px bold text, used to flag discounted books. The yellow is intentionally high-contrast against both the white card and the parchment background.

**`badge-new`** — A green (`#10ff10`) pill badge for new arrivals. Same typography and sizing as the sale badge, but in a fresh green that signals new inventory.

### Navigation
**`nav-bar`** — A 64px deep red (`{colors.primary}`) top bar spanning the full viewport width. Contains the shop name on the left and primary navigation links on the right. The bar is flat — no shadow, no gradient — matching the storefront's honest, unadorned character.

**`nav-link`** — White text links in 16px semibold, with 8px vertical and 16px horizontal padding. Active state shifts to the accent yellow (`{colors.accent-yellow}`) with a 3px yellow underline.

**`category-tab`** — Rounded pill tabs for filtering by age group or genre. Inactive tabs are muted gray text on the parchment background. Active tabs fill with the brand red and white text, creating a clear selected state.

### Forms
**`text-input`** — White input fields with a 1px `#c5c5c5` border and 8px rounding. Used for search, newsletter signup, and checkout forms. On focus, the border thickens to 2px and shifts to the brand red. Height is 44px to match button parity.

**`search-bar`** — A full-rounded pill input for site search, placed prominently in the nav bar or hero section. White background with a subtle border, 44px height, and placeholder text in the muted gray.

### Footer
**`footer`** — A deep red footer matching the nav bar, containing the shop's address (Hay-on-Wye), opening hours, and links to About, Events, and Contact pages. Links appear in the accent yellow for visibility against the dark background. Padding is generous at 48px vertical and 24px horizontal.

### Hero
**`hero-section`** — A full-width banner using the soft parchment surface (`{colors.surface-soft}`), typically featuring a seasonal reading promotion or event announcement. Contains a headline in 32px bold, a subtitle, and a primary button. No background image — the hero relies on typography and the warm surface color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu. Product cards go to single column. Hero text reduces to 24px. Category strip becomes horizontal scroll. Footer stacks links vertically. |
| Tablet | 744–1128px | Nav links remain visible but compact. Product cards in 2-column grid. Category strip shows 4-5 visible tabs with overflow scroll. |
| Desktop | 1128–1440px | Full nav with all category links. Product cards in 3-4 column grid. Category strip shows all tabs. Hero has larger typography. |
| Wide | > 1440px | Max-width container at 1280px with centered content. Product cards in 4-5 column grid. Additional whitespace around hero. |

### Touch Targets
- All buttons and links: minimum 44px height, 44px width for icon-only targets
- Category tabs: minimum 40px height with 16px horizontal padding
- Product cards: entire card is tappable, minimum 120px height
- Search bar: 44px height with 20px horizontal padding
- Nav links: 48px minimum touch area (padding + height)

### Collapsing Strategy
- Mobile nav: full-width hamburger menu with vertical link stack, 64px tall header
- Category strip: horizontal scroll with snap points, "See All" option at end
- Product grid: single column on mobile, 2 columns on tablet, 3-4 on desktop
- Footer: single column on mobile, 2 columns on tablet, 3 columns on desktop
- Hero: full-width on all sizes, reduced padding on mobile (32px instead of 64px)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons, links, and cards could not be reliably extracted from static HTML/CSS analysis
- Error styling for form validation (red borders, error messages) was not present in extracted data
- Dark mode or high-contrast mode variants are not documented — the site appears to use a single light theme
- The specific sans-serif font family could not be identified beyond the generic `sans-serif` declaration — likely a system font stack or a web font loaded via JavaScript
- Sub-brand or seasonal color palettes (holiday, summer reading, etc.) were not found
- Loading states, skeleton screens, and empty state designs are undocumented
- The accent green `#10ff10` appears in extracted colors but its specific usage context (beyond "new" badges) is unclear — may be a checkout widget color rather than a brand color
- Animation and transition timing values (hover transitions, page transitions) were not extractable
- The site's meta theme-color is absent, suggesting no browser chrome theming is implemented
- Checkout flow components (cart, payment form, order confirmation) were not analyzed in detail
