---
version: alpha
name: "Drift Records"
source_url: "https://www.driftrecords.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record shop that feels like a well-kept listening room, where the brand voltage comes from a single gilded note: #ab8c52, a muted brass that appears in the browser chrome, hover states, and the occasional accent line — never loud, always intentional. The canvas is #f5f2ec, a warm off-white that reads as aged paper rather than sterile digital white, and the ink is #212121, a near-black that keeps body text grounded. Type runs a curious two-face system: PPMonumentExtended-Regular for display headlines — a condensed, architectural sans that gives track listings and section titles a printed-matter gravity — and YoungSerif-Regular for body copy, a serif with a gentle hand-drawn quality that softens the grid. The palette is restrained but not minimal: #e8d4ae and #806430 extend the brass family into highlights and secondary surfaces, while #fadada appears as a blush accent on sale badges or limited-edition markers, a small warmth against the otherwise earthy, ochre-leaning scheme. Buttons are pill-shaped, cards have soft corners, and the overall feel is that of a shop that values the object — the vinyl sleeve, the liner notes, the paper stock — over the algorithm. The nav is a single horizontal strip, the search bar is a rounded input with a brass-toned icon, and every product card sits on a #fcfbf9 surface with a #d9d9d9 hairline, as if each record is displayed on its own light box.

colors:
  primary: "#ab8c52"
  primary-active: "#9a7e4a"
  primary-disabled: "#e8d4ae"
  ink: "#212121"
  body: "#2e2e2e"
  muted: "#636262"
  muted-soft: "#a09e99"
  hairline: "#d9d9d9"
  hairline-soft: "#ece7db"
  canvas: "#f5f2ec"
  surface-soft: "#f7f4ef"
  surface-card: "#fcfbf9"
  surface-strong: "#f2f2f2"
  on-primary: "#ffffff"
  accent-blush: "#fadada"
  accent-gold: "#fab84f"
  accent-error: "#d20000"
  badge-new: "#fab240"
  badge-sale: "#fadada"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'PPMonumentExtended-Regular', 'Helvetica', 'Arial', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'PPMonumentExtended-Regular', 'Helvetica', 'Arial', sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'PPMonumentExtended-Regular', 'Helvetica', 'Arial', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'YoungSerif-Regular', 'Georgia', 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'YoungSerif-Regular', 'Georgia', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'YoungSerif-Regular', 'Georgia', 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'YoungSerif-Regular', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Helvetica', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.15px
  badge:
    fontFamily: "'Helvetica', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'YoungSerif-Regular', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-pill-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-error}"
    textColor: "{colors.accent-error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline-soft}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  search-icon:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    height: 20px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    height: 280px
  product-card-info:
    padding: "{spacing.md} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-artist:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.base}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    maxWidth: 600px
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    height: 36px
    border: "1px solid {colors.hairline}"
  add-to-cart-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "12px 32px"
    height: 48px
  add-to-cart-button-active:
    backgroundColor: "{colors.primary-active}"
  cart-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    height: 24px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 18px
    minWidth: 18px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and primary form submissions. Rendered as a pill-shaped button with a brass fill and white text. On hover, the fill deepens to `{colors.primary-active}` (#9a7e4a). In its disabled state, the background fades to `{colors.primary-disabled}` (#e8d4ae) and the cursor becomes not-allowed.
**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Save for Later". Uses the canvas background with a single hairline border and ink text. On hover, the background shifts to `{colors.surface-soft}` (#f7f4ef). The border remains visible in both states.
**`button-tertiary-text`** — A text-only button for inline actions like "Clear filters" or "Cancel". Uses the primary brass color for the text, no background, and no border. The text underlines on hover.
**`button-pill-gold`** — A smaller, brighter pill used for promotional badges or limited-time offers. Uses `{colors.accent-gold}` (#fab84f) as the background with ink text. This is the only button that breaks the brass family — it signals urgency or specialness.

### Navigation
**`nav-bar`** — A fixed top bar at 64px height, using the warm canvas background and a soft hairline bottom border. Navigation links are set in uppercase Helvetica with 0.5px letter spacing. The active link is underlined with a 2px brass line. The bar contains the shop logo, main nav links (New Arrivals, Genres, Sales, About), a search icon, and a cart icon with a brass badge.
**`nav-link-active`** — The currently selected navigation item. The text color shifts to brass and a 2px brass underline appears. The rest of the link styling remains uppercase Helvetica.
**`nav-link-inactive`** — Default navigation links in muted gray. On hover, the text color shifts to the ink value.

### Cards
**`product-card`** — The primary record display component. A white card on a warm canvas background with a soft hairline border and 8px rounded corners. Each card contains a square-format product image (280px height, top corners rounded) and a text block below with the artist name (muted, caption), album title (title-sm, ink), and price (body-sm, body). On hover, the border turns brass and a subtle shadow lifts the card.
**`product-card-hover`** — The hover state adds a brass border and a 4px/12px shadow. The cursor changes to pointer. No other visual change — the brand trusts the border color shift as sufficient feedback.

### Forms
**`text-input`** — Standard text input for search, newsletter signup, and checkout forms. Uses the warm canvas background, a hairline border, and 8px rounded corners. On focus, the border shifts to brass. In error state, the border turns red (#d20000) and the text color matches.
**`search-bar`** — A pill-shaped search input with a soft surface background and a lighter hairline border. The search icon sits to the left in brass. On focus, the border turns brass and the background may lighten slightly. The placeholder text is in muted-soft.

### Badges
**`badge-new`** — A small gold badge used on new arrival records. Uses `{colors.badge-new}` (#fab240) as the background with ink text, set in uppercase Helvetica at 11px with 0.5px letter spacing.
**`badge-sale`** — A blush-toned badge for sale items. Uses `{colors.badge-sale}` (#fadada) as the background with ink text. Same typography as the new badge.
**`badge-out-of-stock`** — A neutral badge for unavailable items. Uses a strong surface background with muted text. The same uppercase typography applies.

### Footer
**`footer`** — A dark footer section using the ink color as background and warm canvas for text. Links are set in muted-soft and turn brass on hover. The footer contains the shop name, a short about paragraph, navigation links, social media icons, and a newsletter signup form. Padding is generous at 48px top and bottom.

### Hero
**`hero-section`** — The top-of-page hero area for landing pages and collection launches. Uses the warm canvas background with generous 64px vertical padding. The title is set in display-xl (PPMonumentExtended-Regular, 32px) and the subtitle in body-md (YoungSerif-Regular, 16px) with a max width of 600px for readability. No background image — the brand lets the typography and whitespace carry the weight.

### Filters
**`filter-chip`** — A pill-shaped filter option used in genre or category strips. Uses a soft surface background with a hairline border and caption typography. The active state fills the chip with brass and white text. Multiple chips can be active simultaneously.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu. Product cards go to single column (1-up). Hero padding reduces to 32px. Search bar moves below nav. Filter chips wrap to two rows. Footer stacks vertically. |
| Tablet | 744–1128px | Nav shows all links but reduces font size to 12px. Product cards display in 2-up grid. Hero padding at 48px. Search bar remains in nav. Filter chips show in a horizontal scrollable strip. |
| Desktop | 1128–1440px | Full nav with 14px links. Product cards in 3-up grid. Hero at full 64px padding. Search bar centered in nav. Filter chips in a single row with overflow. |
| Wide | > 1440px | Max content width of 1440px, centered. Product cards in 4-up grid. Additional whitespace on sides. Hero content max-width at 800px. |

### Touch Targets
- All buttons and links: minimum 44px height, 44px width where applicable.
- Filter chips: minimum 32px height, 44px width for tap targets.
- Cart icon and search icon: minimum 44px tap area (icon is 24px with 10px padding).
- Nav links: minimum 44px tap area on mobile.
- Product cards: entire card is tappable, minimum 280px height.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger menu. The drawer slides in from the left, showing all nav links in a stacked layout with 48px tap targets.
- The search bar moves from the nav to a dedicated row below the nav on mobile.
- Filter chips collapse from a single row to a two-row wrap on mobile, with a "Show all filters" button that opens a modal.
- The footer collapses from a multi-column layout to a single column on mobile.
- Product cards collapse from multi-column grids to single column on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product card images (zoom, overlay, or color shift) could not be extracted from the static CSS.
- Error styling for form validation beyond the text-input error state (e.g., inline error messages, success states) was not found.
- The exact font weights for PPMonumentExtended-Regular and YoungSerif-Regular are assumed to be 400 (Regular) as no weight variants were declared. The brand may use additional weights (e.g., Bold, Light) that were not present in the extracted CSS.
- Dropdown menu styling (e.g., genre selectors, sort-by options) was not captured.
- Modal/dialog styling for cart preview, quick view, or mobile nav was not found.
- Dark mode or high-contrast mode styles were not present in the extracted data.
- The extracted color list is large (30+ colors) and includes likely checkout-widget colors (e.g., #f39f83, #8191a4) and social-icon colors. The primary palette above focuses on the most distinctive and frequent brand colors (#ab8c52, #f5f2ec, #212121, #e8d4ae, #806430). The remaining colors may be used for third-party integrations or one-off components.
- Animation and transition durations (e.g., button hover, card lift) were not specified in the extracted CSS.
- The exact Shopify platform integration (cart drawer, checkout button, product variant selector) styling was not fully captured.
