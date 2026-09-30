---
version: alpha
name: "YellowKorner"
source_url: "https://www.yellowkorner.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every YellowKorner print ships with a literal yellow corner sticker (#ffcf0b) — a physical brand mark that names the company and injects warmth into what is otherwise a controlled, near-black editorial system. The primary canvas is white, but the dominant emotional register is set by ink (#0d0d0d): dark hero sections, dark footers, and dark overlays create the atmosphere of a gallery space after closing time. Against that field, forest green (#008827) carries every purchase action — add to basket, wishlist icon, quantity selector — a color too deliberate and cool to read as promotional, closer in feel to the ink stamp on an edition certificate than to a sale button. Arizona, the bracketed editorial serif, dominates display type at scale; its fine wedge serifs carry exhibition-wall authority at 48px and collapse gracefully to scholarly body copy at 16px. Gravity, a low-contrast humanist geometric, handles nav labels and UI chrome with the discretion of a museum placard. Libre Baskerville appears in long-form editorial contexts — artist statements, collection essays — leaning into the classical provenance the brand wants to signal for photographic works positioned as investable objects. A warm gold (#baa85a) surfaces on limited-edition callouts and premium tier flags; #a6070f crimson handles promotional and sale messaging; tints of sand (#e5debf) and pale mint (#a7d6b4) appear as filter-chip fills drawn from the palette of the photographs themselves — still lifes, botanical studies, cityscapes. Corner radii are almost entirely absent: product frames and image cells run square (`{rounded.none}`) to mirror physical print mounts, while only buttons and inputs adopt a restrained `{rounded.xs}`. The yellow corner mark — 12×12px, #ffcf0b, bottom-right of every product card — is the one decorative flourish the system permits itself, and it earns that permission by being structurally honest: it is the brand's name, rendered as a physical fact made digital.

colors:
  primary: "#008827"
  primary-active: "#064d1b"
  primary-disabled: "#a7d6b4"
  accent-yellow: "#ffcf0b"
  accent-yellow-pale: "#ffe8a1"
  accent-gold: "#baa85a"
  accent-gold-dark: "#675e35"
  accent-gold-deep: "#8b6b0a"
  accent-red: "#a6070f"
  accent-red-dark: "#5d0a0e"
  accent-teal: "#125a66"
  accent-teal-dark: "#005518"
  ink: "#0d0d0d"
  ink-soft: "#212428"
  body: "#444444"
  muted: "#878888"
  muted-dark: "#4d4d4d"
  hairline: "#d9d9d9"
  hairline-light: "#aeaeae"
  canvas: "#ffffff"
  surface-soft: "#d0d0d1"
  surface-warm: "#e5debf"
  surface-mint: "#a7d6b4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Arizona', 'Libre Baskerville', 'Fago Office Serif', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Arizona', 'Libre Baskerville', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Arizona', 'Libre Baskerville', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Arizona', 'Libre Baskerville', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gravity', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gravity', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Noto Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gravity', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  edition-label:
    fontFamily: "'Gravity', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Gravity', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gravity', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gravity', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gravity', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  price-display:
    fontFamily: "'Arizona', 'Libre Baskerville', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  editorial-body:
    fontFamily: "'Libre Baskerville', 'Fago Office Serif', Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.75
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
    rounded: "{rounded.xs}"
    padding: 12px 28px
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 44px
  text-input-dark:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.muted-dark}"
    borderFocused: "1px solid {colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspect: "3/4"
    titleTypography: "{typography.title-sm}"
    artistTypography: "{typography.body-sm}"
    artistColor: "{colors.muted}"
    priceTypography: "{typography.price-display}"
    editionTypography: "{typography.edition-label}"
    editionColor: "{colors.muted}"
    gap: "{spacing.xs}"
  yellow-corner-mark:
    backgroundColor: "{colors.accent-yellow}"
    width: 12px
    height: 12px
    position: bottom-right corner of product card image
    rounded: "{rounded.none}"
  hero-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} 0"
  edition-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  artist-nameplate:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textTransform: uppercase
    letterSpacing: 0.6px
  editorial-block:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.editorial-body}"
    maxWidth: 680px
    padding: "{spacing.section} 0"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    width: 240px
  lightbox-overlay:
    backgroundColor: "rgba(13,13,13,0.92)"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
    columnGap: "{spacing.xl}"

## Components

### Buttons
**`button-primary`** — Forest green (#008827) fill with uppercase Gravity at 14px and 0.6px letter-spacing; reads authoritative rather than promotional, signaling a gallery-grade purchase rather than a flash-sale impulse. Active state deepens to #064d1b; disabled renders in pale mint (#a7d6b4) at full opacity to remain visible without misleading. Corner radius `{rounded.xs}` is the most curvature applied to any surface element on the page.

**`button-secondary`** — White fill with a 1px solid ink border; used for secondary actions like "View artist" or "Add to wishlist" when paired inline with a primary CTA. Mirrors primary in height and padding to maintain rhythm in two-button rows.

**`button-ghost`** — Transparent background with a 1px white border and white uppercase Gravity label; appears exclusively over dark hero sections and the near-black (#0d0d0d) hero overlay so the editorial atmosphere remains intact. On hover the border and text shift to accent-yellow (#ffcf0b) for a brief brand-signature flash.

### Text Inputs
**`text-input`** — Hard square corners (`{rounded.none}`), 1px hairline (#d9d9d9) border that sharpens to full ink on focus with no box-shadow decoration. The zero-radius signals the grid discipline the rest of the UI maintains. A dark variant (`text-input-dark`) sits inside the footer newsletter signup on the near-black background.

### Navigation
**`nav-bar`** — 64px white bar with a 1px hairline bottom rule, Gravity 13px/500 for top-level links. Deliberately compact so the product grid below reads as the destination. At scroll zero over a hero, swaps to `nav-bar-dark`: background becomes #0d0d0d, links become white, creating a seamless transition into hero imagery without a floating transparent hack.

### Product Card
**`product-card`** — Portrait 3:4 aspect with zero corner radius on both image cell and card wrapper — physical prints have no rounded corners, and neither do their digital representations. Below the image: artist name in muted uppercase body-sm with 0.6px tracking; title in title-sm at normal sentence case; price in `{typography.price-display}` (Arizona 18px) gives edition-catalog gravitas. The `yellow-corner-mark` (12×12px, #ffcf0b) is pinned to the bottom-right corner of the image — the brand's physical hallmark translated without reinterpretation.

### Badges
**`edition-badge`** — Warm gold (#baa85a) rectangular chip, uppercase Gravity at 10px/700, 3px 8px padding, zero radius. Applied to limited-run or artist-signed works. `sale-badge` follows identical geometry in crimson (#a6070f). `new-badge` uses primary green (#008827) for newly added works. All three badges align to the top-left of the product card image, stacked vertically when multiple apply.

### Category Chips
**`category-chip`** — Pill-shaped (`{rounded.full}`), light gray (#d0d0d1) fill, body gray (#444444) 12px Gravity label. Active state inverts to ink fill with canvas text. Used in the horizontal scrolling filter strip above the product grid; on desktop the strip is sticky below the nav bar.

### Artist Nameplate
**`artist-nameplate`** — No container or background, muted (#878888) small-caps uppercase with 0.6px letter-spacing. Functions as a byline beneath the product title in cards and as the primary identification line on artist profile pages above the display-md name heading.

### Hero
**`hero-dark`** — Full-bleed near-black (#0d0d0d) section; Arizona display-xl (48px/400 weight) heading in white with minimal letter-spacing (-0.5px). Body subhead in Noto Sans 15px/1.6 at on-dark white. No image overlay or gradient — sections rely on typographic hierarchy rather than blending photography with text.

### Editorial Block
**`editorial-block`** — White section capped at 680px measure; Arizona display-md (32px) heading followed by Libre Baskerville editorial-body (15px/1.75) for artist biographies and collection essays. The generous line-height and classical serif register position the accompanying photography as art-world, not retail.

### Lightbox Overlay
**`lightbox-overlay`** — 92% opacity near-black scrim (`rgba(13,13,13,0.92)`) with white close icon and caption text in caption-size Gravity; zero radius on the image cell. Large-format print inspection mode where the photograph fills ~90% of viewport height. Keyboard-navigable between works in the same series.

### Filter Sidebar
**`filter-sidebar`** — 240px white sidebar with a 1px right hairline border; category tree in Noto Sans 13px; active checkboxes use primary green (#008827) fill; price range slider thumb fills in primary green. On tablet the sidebar becomes a collapsible drawer triggered from a "Filter" button above the grid.

### Footer
**`footer`** — Near-black (#0d0d0d) with muted (#878888) section-label text and canvas-white (#ffffff) links. Four-column grid on desktop. Newsletter input uses `text-input-dark`. The YellowKorner logotype appears in accent-yellow (#ffcf0b) at the foot of the leftmost column — the one moment of full brand-color saturation in an otherwise monochromatic environment.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, filter sidebar becomes bottom-sheet drawer, nav collapses to hamburger, hero heading drops to display-sm (24px), category chips horizontally scroll |
| Tablet | 744–1128px | Two-column product grid, filter sidebar appears as collapsible left drawer, nav shows top-level categories only with overflow menu |
| Desktop | 1128–1440px | Three-column product grid, filter sidebar pinned at 240px left, full nav with category dropdowns and search inline |
| Wide | > 1440px | Four-column product grid, max-width container 1440px centered, gutters expand to `{spacing.xxl}` on each side |

### Touch Targets
- All buttons and inputs minimum 44×44px height
- Category chips minimum 32px height; strip is horizontally scrollable with momentum on mobile
- Yellow corner mark is decorative only — not interactive, no tap target
- Nav links padded to 44px tap zone despite 13px visual label size
- Wishlist and share icon buttons minimum 40×40px with 8px hit-area extension via padding
- Filter checkboxes minimum 24×24px visual, 44×44px touch target

### Collapsing Strategy
- Product grid collapses 4 → 3 → 2 → 1 column at 1440, 1128, and 744px breakpoints
- Filter bar: sticky horizontal scroll strip on mobile and tablet; sidebar pin on desktop
- Artist biography: collapsed to 3 lines with "Lire la suite" expand toggle on mobile
- Hero heading: display-xl (48px) → display-md (32px) → display-sm (24px) below 744px
- Footer: 4-column grid → 2-column → 1-column stacked; each column becomes an accordion on mobile
- Editorial block measure: 680px max-width with 24px horizontal padding on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- White (#ffffff) canvas color not found in extracted palette; assumed as primary gallery background from convention and page structure
- Exact button corner radius not confirmed from live extraction; `{rounded.xs}` (4px) is inferred from gallery-minimal design conventions
- Arizona font weight range not confirmed; weight 400 assumed throughout serif display scales — may support 300–700 variable axis
- Gravity font weight range not confirmed; weights 500 and 600 assumed for UI labels
- `#125a66` teal and `#005518` deep green usage context unknown — may be hyperlink state or secondary editorial accent; not assigned to components
- `#9f8d42` and `#d39e00` golden tones appear in extracted palette but context (hover states, price variants, promotional tiers) could not be determined
- Exact product card hover state (frame appear, subtle scale, overlay opacity) not extractable from static snapshot
- Mega-menu or category dropdown structure and column layout not confirmed
- Mobile-specific type scale not extracted; breakpoint downscaling is inferred
- Checkout, account, and wishlist flows may use a simplified palette subset not visible in front-end extraction
- Fago Office Serif role is ambiguous — may be a legacy editorial font or CMS-injected body face; Libre Baskerville used in preference
