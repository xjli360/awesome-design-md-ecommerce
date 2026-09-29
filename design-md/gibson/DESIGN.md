---
version: alpha
name: "Gibson"
source_url: "https://www.gibson.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every color extracted from Gibson.com collapses into a spectrum of near-black and cool gray — #121212 underlaying the full canvas, #1c1c1c lifting card surfaces by a single stop, and #e7e7e7 carrying all readable type against that dark field. The absence of an accent hue is not an omission; it is the point: on a page built to showcase flame maple tops and carved mahogany bodies, no interface chrome should compete with the instrument. Inter Tight — the condensed, high-density variant of Inter — handles all typesetting, set at −1.5px tracking for large display heads and −0.2px for titles, keeping letterforms taut and vertical in the way a guitar neck is taut. Buttons carry no border radius ({rounded.none}): the CTA is a cold, sharp-cornered rectangle in {colors.primary} (#e7e7e7) with {colors.on-primary} (#121212) text, a photographic inversion that reads as authority on a dark field rather than friendliness on a white one. Navigation labels run in 13px uppercase Inter Tight at 1px letter-spacing — deliberately subordinate in visual weight to the photography beneath them — with a {colors.hairline} border as the only structural line separating chrome from content. Product pages operate on a grid of deep-black cards where every color input comes from the instrument photography itself: sunburst gradients, figured wood grain, chrome hardware. Spacing is pulled wide — {spacing.section} between content modules — giving the layout a gallery pacing that trusts the viewer to linger rather than herding them with dense UI scaffolding. The overall effect is less a product catalog and more a lit display case after closing: instruments visible, environment receding, interface making itself invisible.

colors:
  primary: "#e7e7e7"
  primary-active: "#ffffff"
  primary-disabled: "#4a4a4a"
  ink: "#e7e7e7"
  body: "#dedede"
  muted: "#c7c7c7"
  hairline: "#2a2a2a"
  canvas: "#121212"
  surface-soft: "#1c1c1c"
  surface-card: "#1c1c1c"
  on-primary: "#121212"
  on-dark: "#e7e7e7"
  overlay-scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.8px
  display-sm:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  title-lg:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  body-md:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  product-overline:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  price:
    fontFamily: "'Inter Tight', 'Inter', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.body}"
    backgroundColor: "{colors.surface-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    subtextColor: "{colors.muted}"
    overlineTypography: "{typography.product-overline}"
    nameTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.none}"
    imageAspect: "4/3"
    padding: "{spacing.base}"
  hero-block:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 80vh
    paddingVertical: "{spacing.section}"
    scrimColor: "{colors.overlay-scrim}"
    scrimOpacity: 0.5
  limited-badge:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.product-overline}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  sticky-add-to-cart:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 48px
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.body}"
    rowBorder: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.xxl}"
  category-filter-pill:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
  category-filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "8px 16px"

## Components

### Buttons
**`button-primary`** — A flat, zero-radius rectangle in {colors.primary} (#e7e7e7) with {colors.on-primary} (#121212) type set in uppercase Inter Tight, 15px at 0.5px letter-spacing. The inversion — light button on near-black canvas — gives CTAs authority without a bright accent hue. Active state brightens to {colors.primary-active} (#ffffff); disabled recedes to {colors.primary-disabled} (#4a4a4a) with {colors.muted} text, signaling unavailability without visual noise.

**`button-secondary`** — Transparent fill with a 1px solid {colors.primary} border and matching {colors.primary} text. Identical height (48px) and uppercase Inter Tight treatment as the primary button. Used for secondary actions — "Learn More," compare, or wishlist — where the full fill would read as overly heavy against the dark canvas.

**`button-ghost`** — No border, no fill, {colors.muted} (#c7c7c7) text in {typography.button-sm}. Reserved for the lowest-hierarchy actions such as "View All" in editorial sections where even a border would interrupt the dark field.

### Text Inputs
**`text-input`** — Rendered on {colors.surface-soft} (#1c1c1c) with a 1px {colors.hairline} (#2a2a2a) border and no border radius. Placeholder text sits at {colors.muted} (#c7c7c7). On focus, the border advances to {colors.body} (#dedede), providing clear affordance without introducing color. Height 48px aligns with buttons for inline form compositions like search and newsletter rows.

### Navigation
**`nav-bar`** — 64px fixed bar at {colors.canvas} (#121212), separated from page content by a single 1px {colors.hairline} border at the bottom. Category links use {typography.nav-label}: 13px uppercase Inter Tight at 1px letter-spacing, intentionally subdued so photography and product names below hold visual hierarchy. Logo anchors left; search icon and cart icon sit right at 24px each with 44px tap targets.

### Product Card
**`product-card`** — Zero border radius on {colors.surface-card} (#1c1c1c). Image renders at 4:3 aspect, full-bleed to card edge with no shadow or inset. Category overline in {typography.product-overline} / {colors.muted} sits above the model name in {typography.title-md} / {colors.ink}, with price below in {typography.price}. On hover, the image darkens via a CSS filter overlay rather than shifting the card's background — nothing in the chrome moves; only the photography reacts.

### Hero
**`hero-block`** — Full-bleed canvas (#121212) at minimum 80vh. Headline in {typography.display-xl} (56px, weight 700, −1.5px tracking) with a single subtitle line in {typography.body-md}, followed by stacked or inline button group. For hero sections set over photography, a {colors.overlay-scrim} gradient at 50% opacity maintains type contrast without boxing text inside a separate container. The photographic and typographic layers are kept on distinct z-planes so the instrument reads as present in the space, not framed.

### Limited Edition Badge
**`limited-badge`** — Transparent fill, 1px {colors.primary} border, {colors.primary} text in {typography.product-overline} (11px uppercase, 2px letter-spacing). The cold stamp quality of the letterform at zero radius reinforces product scarcity without warmth — this badge reads as a specification, not a celebration.

### Sticky Add-to-Cart
**`sticky-add-to-cart`** — Full-width bar fixed to the bottom of the viewport on product pages. {colors.canvas} background with a 1px {colors.hairline} top border. Holds the product name in {typography.title-md} at left, price in {typography.price} at center, and a button-primary at right. Appears after the hero image scrolls past the viewport fold; disappears when the page-level add-to-cart button re-enters view.

### Spec Table
**`spec-table`** — Two-column table: label column in {typography.caption} / {colors.muted}; value column in {typography.body-sm} / {colors.body}. Rows separated by 1px {colors.hairline} lines, no alternating row fill. Used for guitar specifications — scale length, nut width, body wood, finish type — where clean vertical scanning matters more than visual interest.

### Search
**`search-bar`** — Expands horizontally from the nav search icon on click, occupying the right half of the nav bar on desktop. Zero radius, {colors.surface-soft} fill, 1px {colors.hairline} border. Dismisses on Escape or outside-click. On mobile, drops below the nav bar as a full-width row with height 48px.

### Category Filter Pills
**`category-filter-pill`** / **`category-filter-pill-active`** — Used in collection pages to filter by guitar family or series. Inactive: transparent fill, 1px {colors.hairline} border, {colors.muted} text in {typography.nav-label}. Active: {colors.primary} fill, {colors.on-primary} text, no radius. The active state applies the same inversion logic as button-primary — light on dark rather than a colored accent.

### Footer
**`footer`** — {colors.surface-soft} (#1c1c1c) background with a 1px {colors.hairline} top border. Four-column link grid at desktop, single-column stack at mobile. All copy in {typography.body-sm} / {colors.muted}. Newsletter field uses text-input inline with button-secondary, stretching full width at mobile breakpoint.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger drawer; hero heading drops to {typography.display-md} (36px); product grid becomes single-column; sticky add-to-cart spans full width; search expands to full-width row below nav |
| Tablet | 744–1128px | Two-column product grid; hero heading at {typography.display-sm} (28px); nav shows top-level categories with overflow hidden; footer collapses to two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; nav fully expanded with all category labels visible; hero at full {typography.display-xl} (56px); spec table floats beside product imagery in two-column layout |
| Wide | > 1440px | Content columns cap at 1440px max-width and center; hero photography bleeds edge-to-edge behind the content cap; section gutter padding increases to maintain proportional breathing room |

### Touch Targets
- All tappable elements minimum 44×44px on mobile
- Nav icons maintain 44px tap area even when visually rendered at 24px
- Product cards expose the entire card surface as the tap region, not title or image independently
- Sticky add-to-cart button occupies the right half of the bar on mobile at minimum 48px height
- Filter pills minimum 44px height on mobile with adequate horizontal padding

### Collapsing Strategy
- Primary nav collapses to hamburger at < 744px; drawer slides from left over {colors.surface-soft} background with {colors.hairline} right border
- Collection filters collapse to a bottom sheet on mobile, triggered by a "Filter" button pinned above the product grid
- Spec table collapses to single-column label-above-value stack below 744px, maintaining {colors.hairline} row separators
- Footer link columns stack vertically below 744px; newsletter section moves above the link grid on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand accent color (gold, amber, red) was extracted — Gibson likely loads its signature warm tone via JavaScript or is protected behind anti-bot measures; all five extracted colors are grayscale (#121212 through #e7e7e7)
- Meta theme-color was absent, which would normally reveal the primary brand hue without JS execution
- Almarai font (Arabic script face) appears in the font stack, suggesting regional or localized variants exist; its role in the English-language design system is unclear and was not incorporated
- Exact button border-radius values could not be confirmed from extraction; {rounded.none} is inferred from the brand's dark, hard-edge aesthetic and consistent with observed Shopify theme patterns
- No extracted token for a sale or discount price color; standard practice would be a desaturated red but cannot be confirmed
- Breakpoint values are inferred from common Shopify theme breakpoints, not directly extracted from CSS
- Animation and transition timing values (hover states, drawer open, sticky bar appearance) were not extractable
