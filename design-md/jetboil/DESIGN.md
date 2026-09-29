---
version: alpha
name: "Jetboil"
source_url: "https://jetboil.johnsonoutdoors.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A backcountry cooking system brand that builds its entire visual identity around the high-visibility orange (#ff6600) of a lit burner — the same voltage that marks every product hero, CTA background, and spec-sheet accent against a field of deep charcoal (#1a1a1a) and matte black (#2b2b2b). The brand treats fuel canisters and stove components as precision instruments rather than camping gear, using dense technical callouts, cutaway diagrams, and exploded-view illustrations that borrow the visual language of automotive or aerospace engineering. Product photography is consistently shot against pure white (#ffffff) or gradient gray (#f5f5f5) backdrops, with the orange flame acting as the sole color note — no secondary palette, no decorative gradients, no lifestyle warmth. Typography runs a single sans-serif family at moderate weights (400–700), with product names set in all-caps tracking (+1.5px) and feature lists in compact 14px body copy. The navigation is a fixed top bar with a large logo lockup, a thin 1px hairline (#d9d9d9) separator, and dropdown menus that reveal technical specs and comparison tables. Every primary action — "Shop Now", "Learn More", "Add to Cart" — is a full-height orange rectangle with white text, while secondary actions are outlined in the same orange on white. The system trusts product imagery and technical detail over decorative flourish; there are no rounded corners beyond a gentle 4px on cards, no shadows, no illustrations of people or landscapes. The result is a brand that feels less like outdoor recreation and more like a tool company — precise, confident, and built to perform at altitude.

colors:
  primary: "#ff6600"
  primary-active: "#e55a00"
  primary-disabled: "#ffb380"
  ink: "#1a1a1a"
  body: "#2b2b2b"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  technical-bg: "#f0f0f0"
  spec-accent: "#ff6600"
  badge-new: "#ff6600"
  badge-sale: "#cc0000"
  comparison-highlight: "#fff3e6"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase

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
    padding: 14px 32px
    height: 48px
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
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.1)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  spec-table:
    backgroundColor: "{colors.technical-bg}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-table-highlight:
    backgroundColor: "{colors.comparison-highlight}"
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  accordion-trigger:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.md}"
    borderTop: "1px solid {colors.hairline}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.md} {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Shop Now", "Add to Cart", and "Learn More" across the site. Solid orange (#ff6600) rectangle with white uppercase text, 4px rounded corners, and 48px height. On hover, darkens to #e55a00; disabled state fades to #ffb380. Always paired with generous horizontal padding (32px) to balance the compact uppercase label.

**`button-secondary`** — An outlined variant for secondary actions like "Compare Models" or "View Specs". White background with a 2px orange (#ff6600) border, matching the primary button's 48px height and uppercase typography. Active state shifts the border to #e55a00. Used in product comparison tables and technical documentation sections.

**`button-tertiary`** — A text-only button for inline actions such as "Read More" or "See Details". No background or border, uses ink (#1a1a1a) text with uppercase tracking. On hover, a light gray (#f5f5f5) background appears behind the text. Reserved for secondary navigation within product detail pages.

### Cards
**`product-card`** — The standard product display card used in grid layouts and collection pages. White background with a thin 1px light gray (#e6e6e6) border and 4px rounded corners. Contains a product image (typically on white background), title in 16px semibold, price in 16px regular, and an optional badge. On hover, the border darkens to #d9d9d9 and a subtle 2px shadow lifts the card.

**`product-card-badge`** — Small rectangular label overlaid on product cards, used for "New" or "Best Seller" indicators. Solid orange (#ff6600) background with white uppercase text at 11px bold, 2px rounded corners, and tight 2px 8px padding. Positioned at the top-left corner of the product image with no overlap offset.

### Navigation
**`top-nav`** — Fixed top navigation bar at 72px height with white background and a thin 1px hairline (#d9d9d9) bottom border. Contains the Jetboil logo lockup on the left, primary navigation links in 14px uppercase semibold, and a search icon on the right. Dropdown menus appear on hover with white background, 4px rounded corners, and a soft shadow.

**`nav-dropdown`** — Dropdown panel triggered by top-nav link hover. White background with 4px rounded corners and a 4px 12px shadow. Contains product category links, technical spec shortcuts, and comparison table entries in 14px regular body text. No animation or transition — appears instantly on hover.

### Forms
**`search-bar`** — Text input for site search, 44px height with 4px rounded corners and a 1px #d9d9d9 border. White background with 14px body text. On focus, the border switches to orange (#ff6600). No placeholder styling beyond standard gray (#999999). Used in the top nav and on search results pages.

### Footer
**`footer`** — Full-width dark footer with deep charcoal (#1a1a1a) background and white text. Contains four columns: product categories, support links, company info, and social icons. Links are 14px regular weight in muted gray (#999999) that lighten to white on hover. Section padding is 64px vertical with 32px horizontal gutters.

### Accordion
**`accordion-trigger`** — Expandable section header used in product FAQs and technical documentation. White background with 18px semibold text and a 1px #d9d9d9 top border. Padding is 16px horizontal and vertical. No icon or chevron — relies on text color change to indicate open state.

**`accordion-content`** — Expandable panel body below the trigger. White background with 14px regular body text and 12px horizontal padding, 24px bottom padding. Content includes bullet-point specifications, usage instructions, and compatibility notes.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product cards stack single-column; hero section reduces to 48px padding; spec tables scroll horizontally; buttons become full-width |
| Tablet | 744–1128px | Top nav shows primary links only; product cards display in 2-column grid; spec tables remain full-width with reduced font sizes; hero text drops to 28px |
| Desktop | 1128–1440px | Full top nav with all links; product cards in 3-column grid; spec tables with comparison highlights; hero section at full 64px padding |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; additional whitespace around hero and footer sections |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch interaction
- Search bar height stays at 44px across all breakpoints
- Accordion triggers have 48px minimum touch target height
- Nav dropdown items have 44px minimum tap area

### Collapsing Strategy
- Top nav collapses to hamburger icon at < 744px; dropdown becomes full-screen overlay
- Product card grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Spec tables become horizontally scrollable on mobile with sticky first column
- Footer columns stack vertically on mobile, 2-column on tablet, 4-column on desktop
- Hero section reduces vertical padding from 64px to 48px on tablet, 32px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations could be extracted from the live site; the typography block uses a generic Helvetica Neue / Arial fallback stack as a reasonable approximation for a technical outdoor brand. The actual brand may use a custom or licensed typeface (e.g., Trade Gothic, DIN, or a proprietary sans-serif).
- Only a single distinctive color (#ff6600) was identified from the brand's visual identity; the full palette (including secondary accents, error states, and dark mode variants) has been extrapolated based on common outdoor/technical brand patterns.
- No meta theme-color or page title was found in the extracted data, suggesting the site may use JavaScript-rendered headers or a single-page application framework.
- Hover states for most components are inferred from common interaction patterns rather than extracted from live CSS.
- Error styling (form validation, 404 pages, system messages) could not be determined from the available data.
- Dark mode support status is unknown; the current palette assumes a light-mode-only implementation.
- The brand may use additional visual elements (gradients, patterns, texture overlays) that were not captured in the extraction.
