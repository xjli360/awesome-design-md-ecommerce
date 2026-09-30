---
version: alpha
name: "Nimble"
source_url: "https://www.gonimble.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A tech brand that wraps its sustainable-materials mission in a cyan #00bbff voltage — the single electric accent that charges every primary CTA, progress indicator, and product-highlight badge against a mostly neutral canvas of #cacac8, #dedede, and #ffffff. The palette reads like a workshop floor: warm browns (#5f3f3f, #64162e) for leather-goods accents, muted sage (#708270) for plant-based materials, and a deep navy (#081d4e) for footer authority, all grounded by a near-black #212322 for body text. Acumin Pro runs the typography at moderate weights — display sits at 24–32px in weight 400/600 rather than heavy 700+ — letting material textures and product photography carry the emotional load. Buttons are softly rectangular ({rounded.sm} ~6px), product cards use a gentle {rounded.md} ~12px, and the search bar adopts a pill shape ({rounded.full}) that echoes the brand's "smooth, rounded" product design language. The nav bar stays transparent-to-white on scroll, with a thin {colors.hairline} bottom border that separates without shouting. Badges appear in both {colors.primary} cyan for "New" and a warm {colors.primary-active} #0064cd for "Bestseller," while sustainability callouts use a sage #708270 chip. The overall feeling is conscientious but not precious — a workshop aesthetic where every corner has a purpose and every color has a material origin story.

colors:
  primary: "#00bbff"
  primary-active: "#0064cd"
  primary-disabled: "#b0bfbf"
  ink: "#212322"
  body: "#454545"
  muted: "#505357"
  muted-soft: "#a5a5a5"
  hairline: "#cacac8"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#5f3f3f"
  accent-sage: "#708270"
  accent-maroon: "#64162e"
  accent-navy: "#081d4e"
  badge-new: "#00bbff"
  badge-bestseller: "#0064cd"
  badge-sustainable: "#708270"
  star-rating: "#dad55e"
  error: "#003eff"

typography:
  display-xl:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'acumin-pro', 'Acumin Pro', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
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
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
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
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-pill-cyan:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 7px 19px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline-soft}"
  search-bar-pill-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0px 0px"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-sustainable:
    backgroundColor: "{colors.badge-sustainable}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-badge-bestseller:
    backgroundColor: "{colors.badge-bestseller}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    maxWidth: 720px
  hero-subheading:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    maxWidth: 560px
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.canvas}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.canvas}"
  sustainability-chip:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  rating-stars:
    color: "{colors.star-rating}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0px"
    borderBottom: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with {colors.primary} cyan and white text. On hover, shifts to {colors.primary-active} #0064cd for a deeper, more confident state. Disabled state drops to {colors.primary-disabled} #b0bfbf with muted text. Used for "Add to Cart," "Shop Now," and primary form submissions. The {rounded.sm} ~6px radius keeps the button feeling modern and slightly softened without being pill-like.

**`button-secondary`** — An outlined variant with a white fill, {colors.ink} text, and a {colors.hairline} border. Active state thickens the border to {colors.ink} and adds a {colors.surface-soft} background. Used for "Learn More," "View Details," and secondary checkout actions. Height matches primary at 44px for alignment in forms.

**`button-tertiary-text`** — A text-only button in {colors.primary} cyan with no background or border. Used for inline actions like "Cancel," "Clear filters," or "See all." Hover state adds a subtle underline.

**`button-pill-cyan`** — A fully pill-shaped variant ({rounded.full}) in {colors.primary} with white text, shorter at 36px. Used for filter tags, category chips, and "New" promotional badges. The pill shape echoes the brand's product design language of smooth, rounded edges.

**`button-pill-outline`** — The outlined counterpart to the pill button, with a transparent fill, {colors.ink} text, and a {colors.hairline} border. Used for inactive filter states and secondary tag selections.

### Cards
**`product-card`** — A clean white card with {rounded.md} ~12px corners and no shadow by default (shadow appears on hover). The image area uses {rounded.md} on top corners only, creating a natural break between photography and text content. Title uses {typography.title-sm} at 16px/500 weight, price uses {typography.body-md} at 16px/400. Padding is {spacing.base} on sides and bottom, with {spacing.xs} between title and price.

**`product-badge`** — Small uppercase labels in {colors.primary} cyan for "New" items, {colors.badge-sustainable} sage for eco-friendly materials, and {colors.badge-bestseller} blue for top sellers. Uses {typography.badge} at 11px/600 with 0.5px letter spacing and {rounded.xs} ~4px corners. Padding is tight at 4px 8px to sit cleanly on product images.

### Navigation
**`nav-bar`** — A 72px white bar with a thin {colors.hairline-soft} bottom border. The logo sits left, navigation links center or right, and the cart icon with count badge sits at the far right. On scroll, a subtle box-shadow replaces the border. Active nav links get a 2px {colors.primary} underline.

**`nav-link-active`** — Active state with {colors.ink} text and a 2px {colors.primary} bottom border. Inactive links use {colors.muted} #505357 for reduced visual weight.

### Forms
**`text-input`** — Standard 44px input with {rounded.sm} ~6px corners, a {colors.hairline} border, and {colors.canvas} background. Focus state swaps the border to {colors.primary} cyan. Error state uses {colors.error} #003eff blue border (distinct from the cyan primary). Used for email signup, search queries, and checkout fields.

**`select-dropdown`** — Matches text-input dimensions and styling, with a custom chevron icon in {colors.muted}. The dropdown panel uses {colors.canvas} with a subtle shadow.

**`quantity-selector`** — A compact input group with minus/plus buttons flanking a numeric input. Uses {rounded.sm} corners and a {colors.hairline} border. Buttons are 40px square with {colors.surface-soft} background.

### Footer
**`footer`** — A deep navy (#081d4e) section that anchors the page. Text is white, links use {typography.link} at 14px/400. Column headings use {typography.title-sm} in white. The background color provides high contrast for the sustainability messaging and legal links. Padding is generous at {spacing.xxl} vertical.

### Sustainability Elements
**`sustainability-chip`** — A pill-shaped label in {colors.accent-sage} #708270 with white text. Used to call out recycled materials, plastic-free packaging, or carbon-neutral shipping. The sage green is the brand's visual shorthand for "good for the planet."

**`rating-stars`** — A warm yellow (#dad55e) star icon set. The color is warm enough to feel inviting but not so saturated that it competes with the primary cyan. Used on product cards and review sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack full-width; hero text reduces to {typography.display-lg} (28px); buttons become full-width; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains two-column layout; sidebar filters become horizontal strip |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses full display-xl (32px); filters in left sidebar; product cards show hover shadow |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; additional whitespace on sides; hero text can scale to 36px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons (cart, search, menu) use 40px minimum touch area
- Product card tap targets extend to full card width on mobile
- Quantity selector buttons are 44px square on touch devices
- Filter chips use 36px height with 8px gaps for easy tapping

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Footer columns stack vertically below 744px, with accordion-style expand/collapse for each section
- Product filters collapse to a horizontal scroll strip on tablet, then to a "Filter" button with modal overlay on mobile
- Hero section reduces from two-column (text + image) to single-column stack below 744px
- Product image galleries collapse from thumbnail strip to dot indicators on mobile
- Search bar collapses from full-width to icon-only on mobile, expanding on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (especially product cards, footer links, and sustainability chips) could not be reliably extracted from the static HTML/CSS
- Error state styling for forms (beyond border color) — no error message typography or iconography was visible
- Dark mode or high-contrast mode variants — not present in extracted styles
- Sub-brand or collection-specific color palettes (e.g., limited-edition drops, collab collections)
- Animation timing and easing curves for transitions (hover, scroll, modal open/close)
- Modal and overlay component styling (cart drawer, search overlay, mobile menu)
- Dropdown menu styling for nav (mega-menu or simple dropdown not visible in extracted markup)
- Checkout flow component states (Shopify checkout is typically embedded and uses its own design system)
- Loading states and skeleton screen patterns
- Form validation message styling (success, warning, info)
- Tooltip and popover component styling
- The extracted color list is heavily weighted toward grays and blues — the brand's true accent palette may include additional colors not captured in the extraction (e.g., a specific green for plant-based materials, a warm tone for leather goods)
- Font weight variations beyond 400 and 600 were not confirmed — Acumin Pro may support 300 and 700 weights that the brand uses sparingly
