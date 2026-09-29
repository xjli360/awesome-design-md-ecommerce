---
version: alpha
name: "Ravensburger"
source_url: "https://www.ravensburger.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue (#0058a2) anchors Ravensburger's digital presence with the authority of a 140-year-old puzzle and game maker — this is the blue of a clear winter sky over Lake Constance, not a generic corporate navy. The palette extends into a darker marine (#002c58) for depth, a warm stone-gray (#58504d) for body text that reads as solid and trustworthy, and a crisp near-white (#fffffe) canvas that lets product photography breathe. A restrained accent of signal red (#cd0a1e) appears sparingly — on sale badges, error states, and the occasional call-to-action — while a secondary green (#0b7c39) marks in-stock availability and positive confirmations. The typography runs Roboto at moderate weights (400 for body, 500 for navigation, 700 for headlines), a workhorse sans-serif that prioritizes legibility across puzzle instructions, game rules, and product descriptions. Cards and buttons use a soft 8px rounding ({rounded.sm}) that suggests approachability without sacrificing the precision the brand is known for — every puzzle piece must fit exactly, and the interface mirrors that philosophy. The navigation bar sits at a substantial height, carrying the logo, search, account, and cart in a single persistent row, while category dropdowns reveal the breadth of the catalog: puzzles, games, crafts, and gifts. Product cards feature a clean white background with the product image dominating the frame, price and age recommendation set in {typography.body-sm}, and a prominent "Add to Cart" button in the primary blue. The overall mood is one of quiet competence — this is a brand that knows its audience values quality, tradition, and the satisfaction of completing something difficult.

colors:
  primary: "#0058a2"
  primary-active: "#002c58"
  primary-disabled: "#90c2e7"
  ink: "#231914"
  body: "#58504d"
  muted: "#737578"
  muted-soft: "#beb7ad"
  hairline: "#c9cdd0"
  hairline-soft: "#dedbd6"
  canvas: "#fffffe"
  surface-soft: "#f2f2f2"
  surface-card: "#fffffd"
  on-primary: "#fffffe"
  accent-red: "#cd0a1e"
  accent-red-active: "#e31937"
  accent-green: "#0b7c39"
  accent-green-active: "#0a5a2a"
  badge-sale: "#cd0a1e"
  badge-new: "#0058a2"
  star-rating: "#664d03"
  scrim: "#231914"

typography:
  display-xl:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.25px
  badge:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Roboto, Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.25px

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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-red-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-primary}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 0
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
    objectFit: "cover"
  product-card-info:
    padding: "{spacing.md} {spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
  product-card-age:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    height: 400px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  category-tile-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    height: 44px
    width: 44px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-md}"
    padding: "{spacing.base} 0"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's deep blue (#0058a2) with white text. Used for "Add to Cart", "Shop Now", and primary checkout flows. On hover, shifts to the darker marine (#002c58). Disabled state uses the muted blue (#90c2e7) to signal non-interactivity while maintaining brand consistency.

**`button-secondary`** — An outlined variant with a white background and blue text, used for secondary actions like "View Details" or "Save for Later". The 2px border matches the primary blue, and on hover the background shifts to the soft surface tone (#f2f2f2) with the darker active blue text.

**`button-accent-red`** — Reserved for high-urgency actions such as "Clearance Sale" or "Limited Offer" entry points. Uses the signal red (#cd0a1e) background with white text, and darkens to (#e31937) on hover. This button should be used sparingly to maintain its urgency signal.

**`button-pill-primary`** — A compact, fully rounded variant used for filter tags, category pills, and quick-select options. Smaller typography and padding make it suitable for inline use within product listing filters and search refinement bars.

### Cards
**`product-card`** — The primary content container for the product catalog. Features a clean white surface with no padding on the image area, allowing the product photography to bleed to the top corners. Information section below uses standard spacing tokens. The card has no border, relying on the soft background of the surrounding grid for separation.

**`category-tile`** — Used on the homepage and category landing pages to represent product categories (Puzzles, Games, Crafts, Gifts). A soft gray background that inverts to the primary blue on hover, creating a clear interactive signal. The tile contains an icon or image and the category name.

**`hero-banner`** — Full-width promotional banner typically featuring seasonal campaigns, new collections, or brand storytelling. The deep blue background provides a dramatic canvas for white typography and product imagery. A subtle scrim overlay ensures text readability against varying image content.

### Navigation
**`nav-bar`** — Persistent top navigation bar at 72px height, containing the logo, main category links, search, account icon, and cart. A subtle bottom border provides visual separation from the page content. Active nav items are underlined with a 2px primary blue border.

**`nav-dropdown`** — Mega-menu style dropdowns that appear on hover over main category links. White background with standard body typography for subcategory links. Categories are organized in columns with descriptive text for each section.

**`breadcrumb`** — Secondary navigation pattern used on product detail and category pages. Small caption typography in muted gray, with the final (current) item rendered in ink color. Chevron separators between items.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and account forms. Clean white background with a light gray border that thickens to a 2px blue border on focus. Error state swaps the border to signal red (#cd0a1e) to clearly communicate validation issues.

**`search-bar`** — A pill-shaped search input with a soft gray background, used in the navigation bar. On focus, expands to a white background with a blue border, and typically triggers a dropdown with suggested results.

**`quantity-selector`** — A compact input group for adjusting product quantities on the product detail page. Consists of a minus button, a numeric display, and a plus button in a horizontal row. The outer container has a light border, while the buttons have a soft gray background.

### Badges
**`badge-sale`** — A small, uppercase red badge overlaid on product images to indicate discounted pricing. Uses the signal red (#cd0a1e) for urgency, with white text in bold 11px uppercase.

**`badge-new`** — A blue badge used to highlight newly added products or collections. Matches the primary brand color to signal freshness and newness without the urgency of the red sale badge.

**`badge-out-of-stock`** — A neutral gray badge indicating product unavailability. Uses the muted-soft color (#beb7ad) to clearly communicate the status without drawing excessive attention.

### Footer
**`footer`** — Full-width footer in the darkest blue (#002c58) with white text. Contains multiple columns of links (Help, About, Shop, Legal), social media icons, and a newsletter signup. Links have reduced opacity (0.8) that returns to full opacity on hover. The footer provides a strong visual anchor at the bottom of every page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger menu replaces nav links; search bar collapses to icon; footer stacks vertically; hero banner reduces to 250px height |
| Tablet | 744–1128px | Two-column product grid; nav links show top-level categories only; search bar remains visible but compact; footer displays in two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; expanded search bar; footer in four columns |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; additional whitespace on sides; hero banner expands to 500px height |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets extend to full card area on mobile
- Quantity selector buttons are 44px × 44px minimum
- Nav dropdown items have 48px tap targets on touch devices
- Filter and sort controls use 40px minimum height

### Collapsing Strategy
- Main navigation collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Product description and details use accordion pattern on mobile (vs. tabbed on desktop)
- Footer columns collapse to a single column on mobile, with accordion-style section headers
- Hero banner text overlay reduces font size and padding on smaller screens
- Category tiles shift from 4-column grid to 2-column on tablet, single column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is heavily weighted toward blues and grays, with red and green appearing as secondary accents. The true brand palette may include additional accent colors (e.g., for seasonal campaigns or sub-brands) that could not be reliably extracted.
- Font-family declarations included "cafeteria", "molle", and "myriad" which appear to be legacy or unused declarations; Roboto and Verdana are the primary working fonts. The exact font stack hierarchy and any variable font configurations could not be determined.
- Hover and focus states for most components are inferred from common patterns; the actual transition durations, easing functions, and shadow depths used by the live site are unknown.
- Error state styling for forms (error messages, iconography, animation) could not be extracted.
- The checkout flow (cart page, shipping, payment) uses third-party widgets (Shopify Pay, Klarna, etc.) whose styling is outside the brand's direct control and could not be documented.
- Dark mode or high-contrast mode color overrides are not present in the extracted data.
- The exact spacing between product card grid items (gap) and the container max-width could not be determined from the extraction.
- Star rating colors (#664d03) appear in the extraction but may be from third-party review widgets rather than intentional brand design tokens.
- The brand's illustration style, icon set, and photography treatment guidelines are not captured in the extracted data.
