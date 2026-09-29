---
version: alpha
name: "The Ruptured Duck"
source_url: "https://www.therupturedduck.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The name is hardware before it is branding — the brass honorable-discharge lapel pin every returning WWII GI wore on his civilian coat, nicknamed the "Ruptured Duck" by the men who earned it. That same literalism runs through every design decision on the site. The primary color is #566f54, olive drab straight from the Army field-gear palette, carried all the way through to the meta theme-color — not an approximation of military green but the actual shade. Flag primaries appear untinted: #ff0000 and #0000ff show up as raw period colors, the way they appear on service ribbons and unit patches, without the softening or desaturation a consumer lifestyle brand would apply. The canvas is white, the ink is #121212 — deep enough to feel archival — and charcoal (#444444) carries body text, separating it clearly from both the near-black headlines and the light hairline (#dedede) grid. No custom typeface was captured in extraction, which means the site likely falls back to a Shopify system stack; given the subject matter a serif display treatment in the Georgia register is specified here while flagged as unconfirmed in Known Gaps. Body type is system sans at 15px, the workhorse scale for dense catalog copy: condition grades, period codes, provenance notes, item numbers. Buttons are uppercase and letter-spaced, echoing the stenciled labeling on period equipment crates; they sit on {rounded.xs} corners — four pixels only, sharp enough to read as administrative rather than friendly. The product photograph is the primary artifact — a militaria listing lives or dies on the close-up of a maker's mark or a legible condition shot — so the UI acts as a neutral mount. Cards carry a single-pixel hairline, no drop shadow, no color fill. A SOLD badge in pure #ff0000 stamps over unavailable items with the bluntness of a rubber stamp on a requisition form. The footer grounds the page in near-black (#121212) with a three-pixel olive-primary top rule, the one moment the brand color holds structural weight rather than interactive weight.

colors:
  primary: "#566f54"
  primary-active: "#3d5440"
  primary-disabled: "#a3b8a1"
  ink: "#121212"
  body: "#444444"
  muted: "#6e6e6e"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#ff0000"
  accent-blue: "#0000ff"
  overlay-scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  condition-grade:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  catalog-label:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "system-ui, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 10px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    metaTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    imageAspect: "4/3"
    padding: "{spacing.base}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
  condition-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.condition-grade}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  period-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.catalog-label}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "3px 8px"
  sold-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.condition-grade}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    minHeight: 320px
    padding: "{spacing.section} {spacing.xl}"
    overlayColor: "{colors.overlay-scrim}"
    overlayOpacity: 0.55
  category-grid-item:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.primary}"
    padding: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    height: 44px
    placeholderColor: "{colors.muted}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.body}"
  item-number-label:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.primary-disabled}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Olive-drab (#566f54) fill, white text, {rounded.xs} corners. The uppercase letter-spaced label echoes period stencil labeling on equipment crates. Active state darkens to #3d5440; disabled washes to #a3b8a1. Height is fixed at 44px for consistent tap targets.

**`button-secondary`** — White canvas fill, dark ink text, single-pixel {colors.hairline} border. Used for secondary actions like "Contact Us," "Ask a Question," or filter resets — situations where a primary CTA is already present and the secondary must not compete visually.

### Condition Badge
**`condition-badge`** — Olive primary fill with white uppercase text at {typography.condition-grade} scale — e.g., "EXCELLENT," "VERY GOOD," "GOOD." Appears as a corner overlay on product card thumbnails to communicate grading at a glance. The olive fill ties condition directly to the brand's primary color, ensuring it reads as authoritative data rather than decorative annotation.

### Period Tag
**`period-tag`** — Neutral {colors.surface-soft} pill carrying era designations ("WW2," "KOREA," "VIETNAM") in {typography.catalog-label} all-caps. Pairs with `condition-badge` beneath the product card image. The deliberately neutral background keeps the tag from competing with condition information.

### Product Card
**`product-card`** — A 4:3 image fills the top tier; condition-badge and period-tag appear as overlays or sub-image labels. Title renders in {typography.title-sm}, supporting metadata in {typography.body-sm}. Price sits prominently in {typography.price-display} at {colors.primary}, the one moment of brand color in an otherwise neutral card frame. A single hairline border, no shadow — the object does the selling.

### Sold Badge
**`sold-badge`** — Pure #ff0000 fill, white text, the same uppercase {typography.condition-grade} scale as the condition badge. Stamped as a corner overlay on unavailable listings. The raw red reads as an administrative marker — closer to a rubber "SOLD" stamp on a requisition sheet than a designed UI element.

### Hero Banner
**`hero-banner`** — Full-bleed section with a {colors.overlay-scrim} at 0.55 opacity over period photography or olive-primary fill when no image is available. Headline in {typography.display-xl} white serif. Used on the homepage and major category landing pages (US Militaria, German Third Reich, etc.).

### Search Bar
**`search-bar`** — Light {colors.surface-soft} fill, hairline border that sharpens to {colors.primary} on focus. Sits inline in the nav on desktop; collapses to a search icon on mobile. Placeholder text in {colors.muted}; height 44px.

### Breadcrumb
**`breadcrumb`** — Muted gray caption-scale trail, hairline separators, active segment stepping up to {colors.body}. Particularly important on a deep catalog site where a user might navigate from Home → US Militaria → Air Corps → Leather Flying Jackets.

### Item Number Label
**`item-number-label`** — Surface-soft chip with a hairline border and muted caption typography, carrying internal item reference numbers. Positioned below the product title, it signals a dealer-grade catalog system to serious collectors who may reference item numbers in correspondence.

### Category Grid Item
**`category-grid-item`** — Surface-soft tile with a hairline border and {typography.title-sm} label. On hover, border switches to {colors.primary}, signaling navigability with minimal visual noise. Used on landing and collection pages to browse top-level categories.

### Footer
**`footer`** — Near-black (#121212) background anchored by a 3px {colors.primary} top rule — the one structural use of olive in the composition. White body copy, primary-disabled (#a3b8a1) for links to avoid harshness against the dark ground. Standard Shopify footer columns: navigation, policies, contact.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; search collapses to icon; nav drops to hamburger drawer; hero text scales to display-md; condition and period badges stack under image rather than overlay |
| Tablet | 744–1128px | Two-column product grid; side-by-side product detail layout (image left, info right); nav links visible without hamburger |
| Desktop | 1128–1440px | Three-column product grid; sticky nav with search bar inline; hero at full min-height 320px; category grid at 4 columns |
| Wide | > 1440px | Content max-width ~1400px centered with lateral padding; four-column product grid; hero gains lateral breathing room |

### Touch Targets
- All interactive controls minimum 44×44px tap area on mobile
- Condition and period badges padded to minimum 44px height on touch viewports even if visually compact
- Nav hamburger icon at least 44×44px touch zone
- Price and "Add to Cart" affordances vertically separated by at least {spacing.base} to prevent mis-taps

### Collapsing Strategy
- Navigation: full labeled links on desktop/tablet → icon hamburger with slide-in drawer on mobile
- Product grid: 4-col wide → 3-col desktop → 2-col tablet → 1-col mobile
- Hero: full overlay photography on desktop → reduced height with cropped image on mobile, text left-aligned
- Breadcrumb: ellipsis-truncated to "Home > … > [Current]" on viewports narrower than 480px
- Filter/sort controls: inline toolbar on desktop → collapsible drawer triggered by "Filter" button on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font families were detected in extraction — all typeface specifications are inferred from category conventions and Shopify defaults; actual fonts on the live site may differ
- Only six colors extracted; interior-page accent colors (hover states, form validation, sale pricing, discount badges) are interpolated from palette logic and not confirmed
- No border-radius values were captured from CSS — {rounded.xs} / {rounded.sm} assignments reflect a sharp-corner inference from catalog-style UI norms, not measured values
- Icon set and glyph library unknown — period-insignia iconography would be on-brand but is unconfirmed
- Exact grid layout (columns, gap, list-view toggle) on collection pages not confirmed from extraction
- Mobile navigation structure (drawer vs. accordion vs. full-screen overlay) not confirmed
- Discount or sale badge color treatment beyond the sold-state unknown
- Typography scale for product detail page (long-form provenance copy, specifications table) not confirmed
