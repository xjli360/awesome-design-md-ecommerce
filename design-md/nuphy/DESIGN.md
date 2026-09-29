---
version: alpha
name: "NuPhy"
source_url: "https://nuphy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Switch-gap glow given a hex value — #03c9a0 runs through NuPhy's near-black canvas (#111111) the way backlit legends bleed through PBT keycaps: constrained, bright on axis, instantly legible against dark. The brand pairs this mint teal with a secondary gold (#ffcf2a) on sale flags and drop-launch badges, a color combination that echoes the RGB presets keyboard communities already memorize. Roboto Condensed carries display headlines and button labels with compressed geometry that suits keyboard spec copy — tenkeyless form factors, south-facing switch sockets, gasket-mount flex — while Roboto regular handles product descriptions at comfortable reading weight. Corner radii sit in the {rounded.sm}–{rounded.md} range throughout: product cards at 8px, primary buttons at 8px, modal overlays at 12px. There are no pill shapes at macro UI scale; the geometry reads as engineering-adjacent rather than consumer-soft. The dark UI dominates hero and navigation zones, but product listing sections flip to a near-white ({colors.canvas} at #f7f7f8) so switch photography and colorway shots can breathe in accurate light. A slate-blue (#676986) and deep navy (#272d45) appear in secondary navigation tiles and bundle sections, signaling a catalog range running beyond the core teal-accented hero models. Interactive blues (#1279ec, #1471f2) handle inline links and account flows without competing with brand teal. Cart drawer, filter panels, and search overlay inherit the dark canvas, keeping commerce UI consistent with studio-black product photography. Spec tables and switch-comparison grids use Roboto Condensed at small sizes with generous letter-spacing — technical data formatted to match the precision of a switch actuation force curve.

colors:
  primary: "#03c9a0"
  primary-bright: "#00deb0"
  primary-disabled: "#9ae9d9"
  accent-gold: "#ffcf2a"
  accent-slate: "#676986"
  accent-navy: "#272d45"
  link: "#1279ec"
  link-active: "#0f6ad2"
  error: "#e41919"
  ink: "#1d1d1f"
  body: "#525252"
  muted: "#757575"
  muted-soft: "#9a9db1"
  hairline: "#e5e5e5"
  hairline-soft: "#d3d4dd"
  canvas: "#f7f7f8"
  surface-soft: "#f4f4f6"
  surface-card: "#f3f3f3"
  dark-canvas: "#111111"
  dark-surface: "#121212"
  dark-raised: "#1d1d1f"
  dark-hairline: "#303030"
  dark-muted: "#9a9db1"
  on-primary: "#111111"
  on-dark: "#f7f7f8"

typography:
  display-xl:
    fontFamily: "'Roboto Condensed', Roboto, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Roboto Condensed', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Roboto Condensed', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Roboto Condensed', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Roboto Condensed', Roboto, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto Condensed', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto Condensed', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Roboto Condensed', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0

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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-bright}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.dark-hairline}"
    padding: 13px 27px
    height: 48px
  button-ghost-teal:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.dark-raised}"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.dark-muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.dark-hairline}"
    padding: 12px 16px
    height: 48px
  text-input-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.dark-hairline}"
  nav-bar-logo:
    textColor: "{colors.primary}"
    typography: "{typography.display-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageBg: "{colors.dark-canvas}"
    padding: "{spacing.base}"
    shadow: "0 2px 12px rgba(0,0,0,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-display}"
    textColor: "{colors.error}"
  hero:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
  hero-eyebrow:
    textColor: "{colors.primary}"
    typography: "{typography.spec-label}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-hot:
    backgroundColor: "{colors.error}"
    textColor: "#ffffff"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.dark-raised}"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.dark-muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.dark-hairline}"
    iconColor: "{colors.dark-muted}"
    height: 40px
  spec-chip:
    backgroundColor: "{colors.dark-raised}"
    textColor: "{colors.dark-muted}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    border: "1px solid {colors.dark-hairline}"
  spec-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.primary}"
  switch-selector:
    backgroundColor: "{colors.dark-raised}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.dark-hairline}"
    activeAccent: "{colors.primary}"
  cart-drawer:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-dark}"
    borderLeft: "1px solid {colors.dark-hairline}"
    headerTypography: "{typography.title-md}"
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.dark-muted}"
    linkColor: "{colors.dark-muted}"
    linkHoverColor: "{colors.primary}"
    borderTop: "1px solid {colors.dark-hairline}"
    typography: "{typography.body-sm}"

## Components

### Buttons

**`button-primary`** — Mint teal ({colors.primary}) fill with dark ink ({colors.on-primary}) text, uppercase Roboto Condensed at 14px/700 with 0.8px tracking, 8px corner radius, 48px height. Hover transitions to the brighter {colors.primary-bright}. Disabled state uses washed {colors.primary-disabled} with {colors.muted} text. Padding is generous (14px vertical, 28px horizontal), matching a full-width CTA slot on narrow mobile product pages.

**`button-secondary`** — Transparent fill with a 1px {colors.dark-hairline} border for use on dark canvases; text inherits {colors.on-dark}. On hover, a {colors.dark-raised} fill appears. Used for "Learn More" and "Compare" CTAs placed alongside the primary teal action.

**`button-ghost-teal`** — Transparent fill with a 1px teal border and {colors.primary} text, same sizing as button-primary. Used for secondary product actions on light-background listing sections where a solid teal fill would overweight the grid.

**`button-gold`** — {colors.accent-gold} fill with {colors.ink} dark text. Reserved for limited-drop announcements, flash-sale banners, and launch-day hero overlays where yellow signals urgency without reaching for the error red.

### Product Card

**`product-card`** — {colors.surface-card} card with 8px radius and a soft shadow on a {colors.canvas} grid. The image zone uses a {colors.dark-canvas} background so switch and keycap photography reads cleanly across colorways. Title in {typography.title-sm}, price in {typography.price-display}; sale price overrides to {colors.error}. Badge overlays (badge-new, badge-sale, badge-hot) anchor to the top-left corner of the image zone with {spacing.xs} inset.

### Navigation

**`nav-bar`** — Full-width {colors.dark-canvas} sticky bar at 64px height with a 1px {colors.dark-hairline} bottom border that appears on scroll. Logo rendered in {colors.primary} teal via {typography.display-sm} Roboto Condensed. Nav links in {typography.nav-link} Roboto {colors.on-dark}; active category state gains a 2px bottom border in {colors.primary}. Cart and search icon slots at 24px with {colors.dark-muted} fill, transitioning to {colors.on-dark} on hover.

### Hero

**`hero`** — Full-bleed {colors.dark-canvas} section with {spacing.section} vertical padding. Eyebrow line in {typography.spec-label} uppercase teal ({colors.primary}) sits above the headline. Headline in {typography.display-xl} Roboto Condensed 48px/700, {colors.on-dark}. Subhead copy in {typography.body-md} at ~70% opacity. Primary CTA is button-primary; secondary action is button-secondary or button-ghost-teal depending on surrounding contrast. Product imagery typically bleeds to the right half of the layout on desktop.

### Badges

**`badge-new`** — {colors.primary} teal fill, {colors.on-primary} dark text, uppercase Roboto Condensed 10px/700, 4px radius. Applied to product cards at launch window.

**`badge-sale`** — {colors.accent-gold} fill, {colors.ink} text, same type spec. Triggers on any markdown greater than 0%, placed in the same top-left image zone slot as badge-new.

**`badge-hot`** — {colors.error} fill, white text. Reserved for high-velocity drops and sell-out velocity warnings; not used for routine discounts.

### Spec Chips

**`spec-chip`** / **`spec-chip-active`** — Small dark chips ({colors.dark-raised}, 1px {colors.dark-hairline} border) used in product-page filter rows for switch type, layout size, and connectivity. Uppercase Roboto Condensed 11px in {colors.dark-muted}. Active state fills with {colors.primary} and flips text to {colors.on-primary}. Filter rows scroll horizontally on mobile without wrapping.

### Search

**`search-bar`** — {colors.dark-raised} background, 1px {colors.dark-hairline} border, 40px height, 8px radius, magnifier icon in {colors.dark-muted}. On focus, border transitions to 1px {colors.primary} and a full-screen overlay drops behind on mobile.

### Cart Drawer

**`cart-drawer`** — Slides in from the right over a 40% black scrim. {colors.dark-surface} background, 1px left border in {colors.dark-hairline}. Header in {typography.title-md} {colors.on-dark}. Line items use {typography.body-sm}. Checkout CTA is button-primary at full drawer width.

### Color Swatch Selector

**`color-swatch`** — 20px circles ({rounded.full}) representing keyboard colorways. Active state adds a 2px gap ring plus a 2px {colors.primary} outer border. Swatches stack horizontally with {spacing.xs} gap; overflow scrolls on mobile.

### Switch Selector

**`switch-selector`** — Card-style selector ({colors.dark-raised}, 1px {colors.dark-hairline} border, {rounded.sm}) listing switch variant options (linear, tactile, clicky) with name and actuation force. Active option gains a left-edge accent bar in {colors.primary}.

### Footer

**`footer`** — {colors.dark-canvas} background with a 1px {colors.dark-hairline} top border. Column headers in {typography.title-sm} {colors.on-dark}. Link text in {colors.dark-muted}, transitioning to {colors.primary} on hover. Social icons at 20px, {colors.dark-muted}. Newsletter input uses text-input. Bottom bar carries legal text in {typography.caption} {colors.dark-muted}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero headline drops to {typography.display-md} (32px); hero CTA goes full-width; spec-chip rows scroll horizontally without wrapping; cart drawer covers full viewport width |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only, mega-menu hidden; hero shifts to two-column layout (copy left, product image right); filter sidebar collapses to horizontal top filter bar |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with mega-menu dropdown panels; hero at full {typography.display-xl} 48px; spec comparison table fully expanded inline |
| Wide | > 1440px | Content capped at 1440px max-width, centered; hero section gains additional horizontal padding; product grid may expand to five columns on wide catalog pages |

### Touch Targets

- All buttons minimum 48×48px tap target
- Color swatches expand from 20px to 32px on mobile
- Nav hamburger icon: 44×44px minimum tappable zone
- Spec chip filter pills: minimum 36px height on mobile, placed in a full-width horizontal scroll row
- Cart quantity stepper buttons: 40px minimum tap area per side

### Collapsing Strategy

- Mega-menu dropdowns become a full-screen left-edge drawer at tablet breakpoint and below
- Product filter sidebar collapses into a slide-up bottom sheet on mobile
- Spec comparison table becomes horizontally scrollable on tablet and mobile; first column (feature name) is sticky
- Hero two-column layout stacks vertically on mobile: copy above, product image below
- Footer multi-column grid collapses to single column with accordion-expand sections on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface confirmed — Roboto and Roboto Condensed inferred from extracted font-family stacks; NuPhy may serve an additional licensed condensed display face not declared in CSS
- Dark-mode vs. light-mode switching logic not observable from static extraction; canvas context (#111111 vs #f7f7f8) may respond to OS preference or a manual site toggle
- Exact corner radii not measured from computed CSS; 8px and 12px values are inferred from visual category and Shopify theme defaults filtered out
- Animation and transition specs (hero parallax, product card hover lift, drawer slide easing) not extractable from color and font scraping
- The slate-blue (#676986) and deep navy (#272d45) usage context is uncertain — may be product-line colorway identifiers tied to specific keyboard models rather than semantic UI tokens
- Mega-menu structure and category depth not confirmed; keyboard product taxonomy (by layout, switch, connectivity) may differ from what the extracted palette implies
- Switch-comparison and spec-table component structure is inferred from keyboard category conventions, not confirmed from DOM extraction
