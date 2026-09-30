---
version: alpha
name: "CDJapan"
source_url: "https://www.cdjapan.co.jp"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dense, information-rich import marketplace that uses #0099cc as its primary voltage — a crisp cyan that reads as both technical and playful, appearing on every primary CTA, category header, and active navigation tab. The site carries the visual weight of a catalog from the early 2000s Japanese web: tight grids of product thumbnails, extensive metadata in {typography.caption} and {typography.body-sm}, and a deliberate use of #e82020 for sale badges and #d84000 for urgent price drops. The header stacks a global utility bar (#282828 background, white text) above a deep search bar with category dropdowns, then a horizontal nav strip of 20+ genre links — anime, J-pop, game music, DVD — each clickable and bordered by {colors.hairline}. Product cards use a clean white surface ({colors.surface-card}) with a soft shadow, a thumbnail, and a dense block of Japanese/English text: artist, title, format, release date, price, and stock status. The brand trusts typographic hierarchy over hero imagery — there is no full-bleed hero, no carousel; instead, the homepage leads with a grid of "Recommended Items" and "New Releases" in a 4-column layout. The palette leans cool and utilitarian: #5f5f5f body text, #888888 muted labels, #eeeeee and #f7f7f7 for alternating row backgrounds, and #d8d8d8 for borders and disabled states. Accent colors like #4f8300 (green "in stock" badges) and #eb3588 (pink "pre-order" badges) add semantic color without breaking the system. The overall mood is that of a well-organized specialty store — not luxurious, but trustworthy, exhaustive, and built for the collector who knows exactly what they want.

colors:
  primary: "#0099cc"
  primary-active: "#007399"
  primary-disabled: "#b3d9e6"
  ink: "#282828"
  body: "#5f5f5f"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#d8d8d8"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-alt: "#eeeeee"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale: "#e82020"
  price-drop: "#d84000"
  in-stock: "#4f8300"
  pre-order: "#eb3588"
  star-rating: "#eabe00"
  header-bg: "#282828"
  header-text: "#ffffff"
  link: "#007399"
  link-hover: "#005580"
  scrim: "#112222"

typography:
  display-xl:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  display-md:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', 'Hiragino Kaku Gothic Pro', 'Meiryo', 'MS PGothic', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px

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
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 32px
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
    padding: 7px 15px
    height: 32px
  button-secondary-active:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
    height: 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 36px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px rgba(0,153,204,0.2)"
  nav-bar:
    backgroundColor: "{colors.header-bg}"
    textColor: "{colors.header-text}"
    typography: "{typography.nav-link}"
    height: 36px
  nav-bar-link:
    backgroundColor: transparent
    textColor: "{colors.header-text}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-bar-link-hover:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.header-text}"
  category-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 40px
  category-nav-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px
  product-card-thumbnail:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    height: 180px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.sale}"
  badge-in-stock:
    backgroundColor: "{colors.in-stock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-pre-order:
    backgroundColor: "{colors.pre-order}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  search-bar-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px rgba(0,153,204,0.2)"
  footer:
    backgroundColor: "{colors.header-bg}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 32px 16px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.header-text}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Search". A solid cyan (#0099cc) rectangle with 4px rounded corners, white text in 13px bold Lato. On hover, it shifts to `{colors.primary-active}` (#007399). The disabled state uses `{colors.primary-disabled}` (#b3d9e6) with `{colors.muted}` text. Height is compact at 32px with 8px/16px padding, reflecting the dense information layout.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Add to Wishlist". White background with cyan text and a 1px `{colors.primary}` border. Hover state fills the background with `{colors.surface-alt}` (#eeeeee) and darkens text to `{colors.primary-active}`. Same 32px height and 13px bold typography as the primary.

**`button-sale`** — A compact, high-urgency badge-button for sale items. Uses `{colors.sale}` (#e82020) background with white text in 11px bold. Only 24px tall with 4px/8px padding, designed to sit inline within product card metadata. No hover state — the urgency is immediate.

### Cards
**`product-card`** — The core content unit of the site. A white card with 8px padding and 4px rounded corners, containing a thumbnail area, title, artist, format, release date, price, and stock status. The thumbnail area is 180px tall with a `{colors.surface-soft}` (#f7f7f7) background. Title uses `{typography.title-sm}` (14px bold, #282828), price uses `{typography.body-md}` (14px regular, #282828), and sale prices are rendered in `{colors.sale}`. Cards are arranged in a responsive grid (4 columns on desktop, 2 on tablet, 1 on mobile) with 8px gaps.

### Badges
**`badge-in-stock`** — A green (#4f8300) badge indicating immediate availability. Uses 10px bold uppercase text with 0.5px letter spacing, 2px/6px padding, and 2px rounded corners. Typically positioned in the top-right corner of product card thumbnails or inline next to price.

**`badge-pre-order`** — A pink (#eb3588) badge for upcoming releases. Same dimensions and typography as the in-stock badge, but with a distinct color to signal future availability. Often paired with a release date in `{typography.caption}`.

**`badge-sale`** — A red (#e82020) badge for discounted items. Same compact format, used both on thumbnails and in price rows. When a product has multiple badges (e.g., sale + pre-order), they stack horizontally with 4px gaps.

### Navigation
**`nav-bar`** — The topmost navigation layer, a 36px dark strip (#282828) spanning the full width. Contains utility links (Login, Cart, Wishlist, Help) in 12px bold white text with 8px/12px padding. Hover state adds a subtle white overlay at 10% opacity. The cart link includes a count badge using `{colors.sale}` background.

**`category-nav`** — A secondary horizontal strip below the search bar, 40px tall on white background. Contains 20+ genre links (Anime, J-pop, Game Music, DVD, etc.) in 12px bold dark text. The active category gets a 2px solid `{colors.primary}` bottom border. On mobile, this collapses into a horizontal scrollable strip with a "Categories" dropdown trigger.

### Forms
**`text-input`** — Standard form input for search, login, and checkout forms. 36px tall with 8px/12px padding, 4px rounded corners, and 1px `{colors.hairline}` (#d8d8d8) border. On focus, the border shifts to `{colors.primary}` with a 2px cyan box-shadow ring. Text is 14px Lato in `{colors.body}` (#5f5f5f).

**`search-bar`** — The primary search input, larger at 40px tall with the same styling as `text-input` but with a search icon on the left and a submit button on the right. The submit button uses `{colors.primary}` background. On focus, the same cyan ring appears. Placeholder text is `{colors.muted}` (#888888).

### Footer
**`footer`** — A dark (#282828) footer section with 32px/16px padding. Contains multiple columns of links in 12px/13px gray (#aaaaaa) text. Links lighten to white on hover. Includes copyright, payment icons, social links, and a language/location selector. The footer is divided into 4-5 columns on desktop, stacking vertically on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category nav becomes horizontal scroll with dropdown trigger; search bar collapses to icon-only; footer stacks vertically; utility nav hides behind hamburger menu |
| Tablet | 744–1128px | 2-column product grid; category nav shows first 8 items with "More" dropdown; search bar remains full; utility nav shows key links (Cart, Login) |
| Desktop | 1128–1440px | 4-column product grid; full category nav visible; search bar with autocomplete dropdown; full utility nav with all links |
| Wide | > 1440px | 5-column product grid; max-width container (1440px) centered; additional whitespace on sides; category nav may show sub-genres on hover |

### Touch Targets
- All buttons and links: minimum 44px touch target (achieved via padding on smaller elements)
- Product card thumbnails: full card is tappable, minimum 180px height
- Category nav items: 40px height with 12px/16px padding
- Search bar: 40px height, full-width on mobile
- Footer links: 44px minimum tap area via padding

### Collapsing Strategy
- Utility nav collapses to hamburger menu below 744px
- Category nav collapses to horizontal scroll with "Categories" dropdown trigger below 744px
- Product grid reduces columns: 4 → 2 → 1
- Search bar reduces to icon-only trigger on mobile, expanding to full overlay on tap
- Footer columns stack vertically below 744px
- Product detail page moves from 2-column (image + details) to single-column stack on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, border color) could not be reliably extracted from the live site
- Error state styling for form inputs (red border, error message typography) not observed
- Success/confirmation messaging (green toast, modal) not captured
- Loading states (skeleton screens, spinner colors) not documented
- Dark mode — the site does not appear to support it
- Sub-brand or promotional landing page palettes (e.g., seasonal campaigns) not extracted
- The extracted font list includes many fallbacks (Arial, Courier, Georgia, etc.) — the primary brand font appears to be Lato for UI text, but Japanese text rendering uses system fonts (Hiragino, Meiryo, MS PGothic). The exact font stack for Japanese vs. English text could not be fully disambiguated.
- The extracted color list is heavily weighted toward grays and blues — the brand's true primary (#0099cc) was selected as the most distinctive accent, but the palette may include additional brand-specific colors (e.g., for limited editions or artist collaborations) not visible in the extraction.
- Animation durations and easing curves (hover transitions, page load) not documented
- Modal/dialog overlay styling (background scrim opacity, close button placement) not captured
- The site uses FontAwesome and icomoon for icons — exact icon set and sizing conventions not documented
