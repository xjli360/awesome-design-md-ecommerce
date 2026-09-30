---
version: alpha
name: "RavPower"
source_url: "https://www.ravpower.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A utility-focused power electronics brand that communicates reliability through a restrained palette anchored on a deep teal (#108474) — the single brand voltage that carries every primary CTA, cart button, and category badge. The site reads as a technical catalog first, retail store second: dense product grids, spec-heavy cards, and a navigation system that prioritizes product categories (Power Banks, Chargers, Cables, Wall Chargers) over brand storytelling. Type runs Nunito Sans at modest weights — body copy sits at 14–16px in weight 400, with product titles at 18–20px in weight 600, trusting the product photography and technical specifications to do the selling rather than typographic flourish. The extracted palette reveals a secondary accent system — a warm amber (#f77b08) for sale badges and price highlights, a cautionary red (#d61f1f) for error states and sold-out indicators, and a muted olive (#6b762d) that appears in footer and secondary information blocks, suggesting a brand that doesn't shy away from functional color coding. Cards use soft rounding ({rounded.sm} ~8px), buttons use slightly tighter radii ({rounded.xs} ~4px), and the search bar sits as a full-width input with a pill-shaped submit button — a pragmatic layout that puts product discovery above visual polish. The footer is dense with support links, warranty information, and trust badges (SSL, PayPal, Klarna), reinforcing the brand's positioning as a reliable hardware vendor rather than a lifestyle accessory. The overall mood is industrial, direct, and confidence-inspiring — every pixel exists to answer "will this charger work for my device?" rather than "does this feel premium?"

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a3d4cb"
  ink: "#282928"
  body: "#454645"
  muted: "#747474"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#f77b08"
  accent-red: "#d61f1f"
  accent-olive: "#6b762d"
  accent-teal-light: "#e5f8fb"
  accent-cyan: "#14bedc"
  star-rating: "#fbcd0a"
  badge-sale: "#f77b08"
  badge-new: "#108474"
  badge-sold-out: "#d61f1f"
  footer-bg: "#282928"
  footer-text: "#bbbbbb"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  link:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
    textTransform: uppercase
  price-md:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-sm:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  spec-value:
    fontFamily: "'Nunito Sans', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-pill-search:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-price-sale:
    color: "{colors.accent-red}"
  product-card-price-compare:
    typography: "{typography.price-sm}"
    color: "{colors.muted}"
    textDecoration: "line-through"
  product-card-rating:
    color: "{colors.star-rating}"
    fontSize: "14px"
  product-card-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "8px"
    left: "8px"
  product-card-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "24px 16px"
    border: "1px solid {colors.hairline-soft}"
  category-tile-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: "400px"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    marginTop: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.caption-bold}"
    textTransform: "uppercase"
    letterSpacing: "1px"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    height: "32px"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  accordion-content:
    padding: "0 0 {spacing.base} 0"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: "44px"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    width: "44px"
    height: "44px"
  quantity-selector-input:
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    width: "48px"
    textAlign: "center"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Shop Now," and checkout entry points. Rendered in the brand teal (#108474) with white text and a tight 4px radius, it communicates reliability without softness. On hover, it deepens to `{colors.primary-active}` (#0d6b5e); disabled state uses `{colors.primary-disabled}` (#a3d4cb) with reduced opacity.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details." Uses a white background with a 2px teal border and teal text. On hover, the background shifts to `{colors.surface-soft}` (#f9fafb) and the border deepens to `{colors.primary-active}`.

**`button-amber`** — Reserved for urgency-driven actions: sale promotions, limited-time offers, and clearance call-to-actions. The warm amber (#f77b08) creates visual contrast against the teal-dominant system, drawing immediate attention to time-sensitive content.

**`button-pill-search`** — A fully rounded search submit button that sits inside the search bar. Uses the brand teal with white text and `{rounded.full}` to create a clear visual distinction between the rectangular input field and the circular action trigger.

### Cards
**`product-card`** — The primary product display unit, used in grid layouts across category pages and search results. A white card with a 1px soft hairline border and 8px rounding. Contains a square product image, title in `{typography.title-md}`, price in `{typography.price-md}`, and an optional star rating in `{colors.star-rating}` (#fbcd0a). On hover, the border strengthens and a subtle shadow appears. Sale prices render in `{colors.accent-red}` (#d61f1f) with the original price struck through in `{colors.muted}`.

**`product-card-badge`** — Absolute-positioned badges that overlay the product image at the top-left corner. Three variants exist: sale (amber background), new (teal background), and sold-out (red background). All use uppercase 11px bold type with tight 4px rounding.

**`category-tile`** — A clickable tile used for department navigation (Power Banks, Chargers, Cables, etc.). Uses a soft gray background (#f9fafb) with a subtle border. On hover, the entire tile inverts to the brand teal with white text, creating a strong visual feedback loop.

### Navigation
**`top-nav`** — A fixed 64px header with white background and a thin bottom border. Navigation links use uppercase 14px semibold type with 0.25px letter spacing. The active page is indicated by a 2px teal underline and teal text color. The nav includes a full-width search bar and a cart icon with a badge count.

**`nav-link-active`** — The active navigation state uses `{colors.primary}` text with a 2px bottom border in the same teal, creating a clear visual anchor for the current section.

### Forms
**`text-input`** — Standard text input used for search, newsletter signup, and checkout forms. A white field with a 1px hairline border and 4px rounding. On focus, the border switches to the brand teal. Error states use a red border (#d61f1f) with an accompanying error message in `{typography.caption}`.

**`select-input`** — Used for product filtering (sort by, capacity, compatibility) and address forms. Matches the text input styling with a custom dropdown arrow in `{colors.muted}`.

**`quantity-selector`** — A three-part control for adjusting cart quantities. Consists of a decrement button, a centered numeric input, and an increment button. All three elements share a 44px height with the buttons at 44px width and the input at 48px width.

### Footer
**`footer`** — A dense, dark footer (#282928) with light gray text (#bbbbbb). Organized into columns with uppercase section headings in white. Contains support links, warranty information, company info, and a newsletter signup form. Trust badges (SSL, PayPal, Klarna, Afterpay) sit in a row with soft gray backgrounds.

**`footer-link`** — Standard footer link in light gray. On hover, the text brightens to white, providing clear interactive feedback against the dark background.

### Search
**`search-bar`** — A full-width search input with a soft gray background (#f9fafb) and a 1px hairline border. The input field is rectangular with 8px rounding, while the submit button uses `{rounded.full}` to create a distinct visual separation between the text entry zone and the action trigger.

### Accordion
**`accordion`** — Used for product specifications, FAQ sections, and mobile navigation menus. Each accordion item has a title in `{typography.title-md}` with 16px vertical padding and a bottom border. The content area collapses/expands with a smooth transition. The expand/collapse icon uses `{colors.muted}` and switches to `{colors.primary}` on open.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-up), hamburger nav replaces top nav, search bar collapses to icon-only, footer stacks vertically, hero banner reduces to 300px min-height, product cards use full-width with no side padding |
| Tablet | 744–1024px | Two-column product grid (2-up), top nav shows condensed links (Power Banks, Chargers, More), search bar remains full-width but reduces padding, footer uses 2-column layout, hero banner at 350px min-height |
| Desktop | 1024–1440px | Three-column product grid (3-up), full top nav with all categories visible, search bar at standard width, footer uses 4-column layout, hero banner at 400px min-height |
| Wide | > 1440px | Four-column product grid (4-up) with max-width container at 1440px, all elements at maximum comfortable width, hero banner at 450px min-height with full-width background |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Product card tap targets (title, image, price) are each independently tappable with minimum 48px touch zones
- Quantity selector buttons are 44px x 44px, exceeding the 44px minimum
- Accordion headers have 48px touch targets (16px padding top and bottom on a 16px text line)
- Footer links use 44px minimum touch height with 8px vertical padding

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer containing all category links, account links, and search
- Product grid collapses from 4 columns to 3 to 2 to 1 as viewport narrows, with product cards maintaining their aspect ratio
- Footer collapses from 4 columns to 2 columns to a single stacked column
- Hero banner text reduces from `{typography.display-xl}` (32px) on desktop to `{typography.display-lg}` (28px) on mobile
- Search bar collapses from full-width input with button to an icon-only trigger that opens a modal overlay on mobile
- Product specification tables collapse to stacked label-value pairs on mobile
- Multi-image product galleries collapse from row layout to single-image swipeable carousel on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and cards were inferred from common e-commerce patterns; actual hover transitions (duration, easing) could not be extracted
- Error styling for form validation (error message typography, iconography, animation) was not visible in the extracted data
- Dark mode support: no evidence of a dark mode toggle or alternate palette was found in the extracted colors or markup
- Sub-brand or promotional campaign palettes (holiday, clearance, bundle deals) may use additional accent colors not present in the extracted list
- The extracted font list includes "JudgemeIcons" and "JudgemeStar" which are icon fonts for the Judge.me review platform; the actual review widget styling (star size, spacing, alignment) could not be determined
- Checkout flow styling (Shopify checkout, Klarna, Afterpay) uses platform-default colors that were filtered from the extracted palette; the brand's custom checkout styling is unknown
- Loading states, skeleton screens, and spinner animations were not captured
- The extracted color list includes several near-duplicate grays (#eeeeee, #ececec, #e9e9e9, #f2f2f2, #dadada) — the exact usage of each could not be determined; the palette above consolidates them into the most likely functional roles
- The olive green (#6b762d) and cyan (#14bedc) appear in the extracted list but their specific usage context (badges, links, secondary CTAs) is inferred from common e-commerce patterns rather than confirmed from the live site
- Font weights for Nunito Sans beyond 400 and 600 were not confirmed; 700 is assumed for display headings based on common usage
- The "Baskerville" font declaration found in the extracted list may be used for decorative or logo text; its specific application could not be determined
