---
version: alpha
name: "Marrow Fine"
source_url: "https://www.marrowfine.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Marrow Fine trades on a specific warmth — the parchment cream ground (#f5f2ec) and hand-poured gold (#ab8c52) together read less like a jewelry counter and more like a gilded letter discovered inside a grandmother's keepsake box. The "Modern Heirlooms" positioning is literal in the palette: deep burgundy #643335 surfaces as an ancestral accent alongside a burnished secondary gold (#806430) and whisper-blush (#e6cdc5), as if each diamond is already carrying the memory of something worn and loved before it reaches the customer. Type runs in Jost at measured weights — display text sits light-to-medium rather than bold, letting the gold tokens do the emotional lifting; Poppins handles running body copy with slightly warmer geometry. Buttons use a gold-leaf fill on warm ink, with generous {rounded.sm} radii that feel artisanal rather than corporate. Product photography is set against {colors.canvas}, an off-white that reads almost linen in contrast to the gold-dust card surfaces ({colors.surface-soft}). The blush register — #debeb3, #e6cdc5, #a28586 — forms a secondary emotional layer for editorial moments and hover overlays, while the darker burgundy family (#643335, #532a2c, #201111) grounds the brand with depth and sobriety. Navigation is low-profile, nearly hairline, trusting the cream-and-gold product imagery to carry page authority without heavy UI chrome. Badge treatments, "new arrival" labels, and price callouts use uppercase Jost at micro scales with wide letter-spacing, signaling precision over exclamation. The overall tension is between softness and permanence: soft blush tones and airy spacing against the weight of fine metal and the promise that a piece will outlast its buyer — that is the specific emotional register Marrow Fine is designed to hold.

colors:
  primary: "#ab8c52"
  primary-active: "#806430"
  primary-disabled: "#e8d4ae"
  primary-dark: "#9a7e4a"
  accent-burgundy: "#643335"
  accent-burgundy-deep: "#532a2c"
  accent-burgundy-dark: "#351517"
  accent-burgundy-ink: "#201111"
  accent-burgundy-mid: "#6e383a"
  blush-mid: "#e6cdc5"
  blush-soft: "#debeb3"
  blush-muted: "#a28586"
  ink: "#212121"
  ink-dark: "#282c2e"
  body: "#2e2e2e"
  muted: "#646464"
  muted-warm: "#a49c8b"
  muted-cool: "#a09e99"
  hairline: "#d9d9d9"
  hairline-warm: "#ece7db"
  canvas: "#f5f2ec"
  surface-soft: "#f0ebe2"
  surface-card: "#fcfbf9"
  surface-warm: "#f7f4ef"
  surface-light: "#f7f7f7"
  surface-sage: "#f5f8f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale: "#ce6266"
  gold-sand: "#e8d4ae"

typography:
  display-xl:
    fontFamily: "'Jost', sans-serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.04em
  display-lg:
    fontFamily: "'Jost', sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.03em
  display-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.02em
  display-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.01em
  body-md:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.01em
  micro-label:
    fontFamily: "'Jost', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  badge:
    fontFamily: "'Jost', sans-serif"
    fontSize: 9px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.14em
    textTransform: uppercase
  price-display:
    fontFamily: "'Jost', sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  price-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  button-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Jost', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.08em
  footer-link:
    fontFamily: "'Poppins', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.6
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-warm}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    borderBottom: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted-warm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-warm}"
    logoColor: "{colors.ink}"
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-warm}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageBackground: "{colors.surface-warm}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    captionColor: "{colors.muted-warm}"
    captionTypography: "{typography.caption}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  product-card-badge-new:
    backgroundColor: "{colors.accent-burgundy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
    overlayTint: "rgba(245,242,236,0.55)"
  editorial-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    accentColor: "{colors.primary}"
  category-tile:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.micro-label}"
    labelColor: "{colors.primary}"
    rounded: "{rounded.none}"
    hoverOverlay: "rgba(171,140,82,0.08)"
  gemstone-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderUnselected: "2px solid {colors.hairline}"
    gap: "{spacing.xs}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    backgroundSelected: "{colors.surface-soft}"
    padding: 8px 14px
  ring-size-guide-link:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    textDecoration: underline
  pdp-sticky-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline-warm}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.base} {spacing.xl}"
    height: 72px
  collection-filter-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.micro-label}"
    borderBottom: "1px solid {colors.hairline-warm}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} 0"
  announcement-bar:
    backgroundColor: "{colors.accent-burgundy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.micro-label}"
    height: 36px
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  wishlist-icon:
    size: 20px
    colorDefault: "{colors.muted-warm}"
    colorActive: "{colors.accent-burgundy}"
    strokeWidth: 1.5px
  footer:
    backgroundColor: "{colors.ink-dark}"
    textColor: "{colors.surface-light}"
    linkTypography: "{typography.footer-link}"
    headlineTypography: "{typography.micro-label}"
    headlineColor: "{colors.primary}"
    linkColor: "{colors.muted-warm}"
    borderTop: "1px solid {colors.body}"
    padding: "{spacing.section} {spacing.xl}"
  search-overlay:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline-warm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline-warm}"
    headerTypography: "{typography.display-sm}"
    subtotalTypography: "{typography.price-display}"
    width: 420px
  trust-badge-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-warm}"
    iconColor: "{colors.primary}"
    typography: "{typography.caption}"
    padding: "{spacing.lg} 0"
    borderTop: "1px solid {colors.hairline-warm}"
    borderBottom: "1px solid {colors.hairline-warm}"

## Components

### Buttons

**`button-primary`** — Flat gold fill (#ab8c52) with no border radius, fully uppercase Jost at 13px/0.12em tracking. The squared-off geometry signals craft and intention over digital softness. Hover darkens to #806430 with no transition delay; disabled state washes to the gold-sand (#e8d4ae) with warm-gray label, keeping the dusty palette rather than breaking to neutral grays.

**`button-secondary`** — Transparent fill with a 1px ink border and the same uppercase Jost treatment. On hover, the background lifts to `{colors.surface-soft}` rather than filling with color, keeping secondary actions visually subordinate. Works on both cream and white surfaces without variant changes.

**`button-ghost`** — No border, no fill, underline-only treatment in brand gold. Used inline for "view details," size guides, and editorial CTAs where a bordered button would feel too heavy. The underline is `1px solid {colors.primary}`, not a browser default text-decoration.

### Text Input

**`text-input`** — Sharp-cornered, `{rounded.none}`, on the parchment canvas (#f5f2ec). A single bottom-or-full 1px hairline border transitions from `{colors.hairline}` to `{colors.primary}` on focus — a gold glow rather than the blue that framework defaults would inject. Placeholder text renders in `{colors.muted-warm}` (#a49c8b), preserving the warm ambient tone.

### Navigation

**`nav-bar`** — 64px tall, cream-ground, hairline bottom border in `{colors.hairline-warm}`. Logo centered or left with minimal mark. Nav links use Jost 13px with 0.08em tracking — not bold, not underlined — letting the gold accent hover state (color flip to `{colors.primary}`) carry the interaction feedback. On scroll, background transitions to `{colors.surface-card}` (#fcfbf9) for subtle depth separation.

**`nav-dropdown`** — Flat panel, no rounded corners, paper-white surface with a fine warm border. Category imagery sits left; text links right. No shadows — the separation is achieved by the thin border alone, consistent with the brand's refusal of heavy UI chrome.

**`announcement-bar`** — Deep burgundy (#643335) strip spanning full width above the nav. White micro-label Jost text for promotions, shipping notices, or seasonal messages. The burgundy here is the sharpest contrast moment in the UI — it lands as urgent without being garish.

### Product Card

**`product-card`** — No border, no shadow, squared corners. Image container uses `{colors.surface-warm}` (#f7f4ef) as a neutral linen-toned background for jewelry photography. Title renders in `{typography.title-sm}` (Jost 14px/500), price in `{typography.price-sm}`, metal/stone descriptor in `{typography.caption}` and `{colors.muted-warm}`. On hover, the image scales subtly (transform: scale 1.02) with no overlay mask. Badge placement is top-left, flush to the image edge.

**`product-card-badge`** — Gold fill for "bestseller" or "low stock." Burgundy fill for "new arrival." Both use `{typography.badge}` — 9px all-caps Jost at 0.14em tracking. Flat rectangle, no radius.

### PDP Components

**`gemstone-swatch`** — 20px circles in `{rounded.full}`, gapped at `{spacing.xs}`. Selected state gets a 2px gold border; unselected gets 2px hairline. No text label beside each swatch — color name appears in a small caption line below the row.

**`pdp-sticky-bar`** — 72px bar fixed to bottom viewport on scroll past the hero image. Cream background, top hairline border in warm tone. Product name left in `{typography.title-sm}`, price right in `{typography.price-display}` (Jost 20px), add-to-cart button filling the remaining space on mobile.

**`ring-size-guide-link`** — Inline gold underline link in `{typography.caption}` placed directly below the size selector row. Text: "Find my ring size." The underline is continuous, not on-hover-only, making the affordance always visible — an important UX detail for first-time fine jewelry buyers.

### Cart & Utility

**`cart-drawer`** — 420px right-side slide-in panel, cream ground, left border hairline warm. Header in `{typography.display-sm}` ("Your Cart"), subtotal block in `{typography.price-display}`. No close button icon box — just an "×" in `{typography.title-md}` top-right. The muted interior palette ensures gold button CTAs read with high contrast.

**`trust-badge-strip`** — Full-width strip between product description and related products. Three or four icons (certification, free shipping, returns, lifetime care) with muted-warm text captions. Icon strokes in `{colors.primary}` (gold) to reinforce craft credibility without breaking the neutral palette.

### Footer

**`footer`** — Near-black background (#282c2e) contrasting with the cream body. Four columns: shop links, about, customer care, newsletter capture. Column headers in `{typography.micro-label}` gold (#ab8c52), link rows in `{typography.footer-link}` muted-warm. Newsletter input inverted: dark border on dark field, white text, gold submit button. Instagram icon links render as `{colors.primary}` on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + bag icon; hero text scales to `{typography.display-lg}`; pdp-sticky-bar becomes full-width bottom bar; cart drawer becomes full-width bottom sheet |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + condensed links + icons; hero uses 50/50 text-image split; announcement bar wraps to two lines if needed |
| Desktop | 1128–1440px | Three-column product grid; full nav with dropdowns; hero at full `{typography.display-xl}`; pdp layout splits into 60/40 image/detail columns |
| Wide | > 1440px | Four-column product grid; max content width ~1400px centered; hero image bleeds full width with text panel constrained to content grid |

### Touch Targets

- All buttons minimum 48px tall on mobile
- Gemstone swatches expand tap area to 36px × 36px even though visual circle is 20px
- Nav hamburger icon 44px × 44px tap zone
- Cart icon, search icon, wishlist icon each minimum 44px tap zones in mobile nav strip

### Collapsing Strategy

- Product filters collapse behind "Filter & Sort" drawer on mobile and tablet, revealing a bottom sheet with checkboxes
- Footer four-column layout stacks to single-column with accordion sections (tap to expand) on mobile
- PDP metal/stone selectors that exceed one row reflow to a horizontal scroll strip rather than wrapping
- Ring size grid converts from 4-per-row to 3-per-row on mobile with larger touch targets
- Editorial strip switches from side-by-side image/text to stacked image-above-text on tablet and below
- Collection category tiles collapse from 4-across to 2-across on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact logo typeface treatment (whether the brand wordmark uses a custom Jost variant or a separate display face) could not be confirmed from extraction
- Animation/transition timing values (easing curves for hover states, drawer open/close duration) not extractable from static scan
- Specific icon library (whether SVG custom icons or a licensed set like Feather or Phosphor) not identified
- Mobile-specific typography scale (whether display sizes reduce proportionally or use a separate defined scale) not confirmed
- Exact grid gap and column gutter values for the product grid were not captured; values in components are inferred from spacing scale
- Whether Poppins is limited to body copy only or also used for some UI labels is ambiguous from available data
- Custom font weights beyond standard 300/400/500 (e.g., whether a Jost 200 extralight is used for display) not confirmed
