---
version: alpha
name: "Stalogy"
source_url: "https://stalogy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Where most notebook brands sell atmosphere, Stalogy sells method — the name itself is an engineered compound, collapsing "Standard" and "Technology" into a single word, and that compression shows in every design decision on the site. The signature canvas is not white but #f4f4e9, a warm cream hovering between office paper and engineering drafting stock, giving product pages the faint warmth of something freshly laid on a light table rather than rendered on a screen. Four categorical accent colors — blue (#0099ff), green (#00cc33), yellow (#ffcc33), and red (#ff0033) — function as pure taxonomy rather than decoration: each hard-coded to a product family, operating less like brand colors and more like industrial standards markings that help specifiers navigate a dense catalogue with no ambiguity.

  Typography is deliberately uncommissioned: Helvetica Neue and Arial carry all Latin copy at weights that never exceed 500, while Yu Mincho and Hiragino Mincho ProN handle Japanese text with matching economy. No custom display fonts, no variable font experiments, no gradient fills anywhere on the site — the visual language defers entirely to system resources and trusts product photography to carry emotional weight. The result reads like a precision tool catalogue rather than lifestyle content.

  Corner radii sit at {rounded.none} for all primary containers and nearly all interactive surfaces. This is a rectilinear system — angular, methodical, consistent with the brand's engineering self-image. The sole softening is the color swatch selector, which uses {rounded.full} as a precise visual counter-signal against the surrounding grid. Buttons render nearly flat against the page with thin neutral borders on secondary actions, and form controls share the same low-contrast, matter-of-fact treatment. Spacing is modular and disciplined: section padding opens generously at {spacing.section} to let product photography breathe, while component-level padding stays compact at {spacing.sm} and {spacing.md}.

  The hairline neutral #c3c5c4 divides the catalogue into sections with a rule barely thicker than a printed stroke. When color appears — and it does, crisply and without apology — it arrives at full saturation: no tints, no opacity washes, no pastels. A yellow badge is #ffcc33 at 100%; a green category marker is #00cc33 without dilution. This commitment to pure, unapologetic accent color against a restrained cream ground is Stalogy's only extravagance.

colors:
  primary: "#0099ff"
  primary-active: "#003388"
  primary-disabled: "#b3d4fc"
  ink: "#222222"
  body: "#777777"
  muted: "#8c8c8c"
  hairline: "#c3c5c4"
  hairline-soft: "#e1e1e1"
  canvas: "#f4f4e9"
  surface-soft: "#e3e3c7"
  surface-card: "#f5f5f5"
  surface-white: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#0099ff"
  accent-green: "#00cc33"
  accent-yellow: "#ffcc33"
  accent-red: "#ff0033"
  accent-orange: "#ec912d"
  accent-cyan: "#00b7e7"
  accent-navy: "#003388"
  scrim: "#222222"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.4px
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-ja:
    fontFamily: "'Yu Mincho', YuMincho, 'Hiragino Mincho ProN', 'Hiragino Kaku Gothic ProN', Meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0.05em
  caption:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  label:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.3px
  product-name:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  spec-label:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 40px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "10px {spacing.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
    focus-border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logo-typography: "{typography.title-md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    image-aspectRatio: "1 / 1"
    name-typography: "{typography.product-name}"
    price-typography: "{typography.price}"
    caption-typography: "{typography.body-sm}"
    padding: "{spacing.sm}"
    hover-borderColor: "{colors.hairline}"
    hover-shadow: "0 2px 8px rgba(0,0,0,0.06)"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 480px
    heading-typography: "{typography.display-xl}"
    subheading-typography: "{typography.display-sm}"
    body-typography: "{typography.body-md}"
    paddingY: "{spacing.section}"
    paddingX: "{spacing.xl}"
    layout: "split — product image left 55%, copy + CTA right 45%"
  color-category-tag:
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "2px {spacing.xs}"
    height: 20px
    variant-blue:
      backgroundColor: "{colors.accent-blue}"
      textColor: "{colors.on-primary}"
    variant-green:
      backgroundColor: "{colors.accent-green}"
      textColor: "{colors.on-primary}"
    variant-yellow:
      backgroundColor: "{colors.accent-yellow}"
      textColor: "{colors.ink}"
    variant-red:
      backgroundColor: "{colors.accent-red}"
      textColor: "{colors.on-primary}"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    selected-border: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  category-rule:
    height: 3px
    variant-blue:
      backgroundColor: "{colors.accent-blue}"
    variant-green:
      backgroundColor: "{colors.accent-green}"
    variant-yellow:
      backgroundColor: "{colors.accent-yellow}"
    variant-red:
      backgroundColor: "{colors.accent-red}"
  product-specs-row:
    backgroundColor: transparent
    borderBottom: "1px solid {colors.hairline-soft}"
    label-typography: "{typography.spec-label}"
    value-typography: "{typography.body-sm}"
    label-textColor: "{colors.muted}"
    value-textColor: "{colors.ink}"
    paddingY: "{spacing.sm}"
    paddingX: "{spacing.base}"
    alternating-backgroundColor: "{colors.canvas}"
  search-bar:
    backgroundColor: "{colors.surface-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 36px
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    icon-color: "{colors.muted}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    separator-color: "{colors.hairline}"
    active-textColor: "{colors.ink}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    link-textColor: "{colors.hairline}"
    link-hover-textColor: "{colors.surface-white}"
    heading-typography: "{typography.title-sm}"
    heading-textColor: "{colors.surface-card}"
    paddingY: "{spacing.section}"
    borderTop: none
  pagination:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    active-backgroundColor: "{colors.ink}"
    active-textColor: "{colors.on-dark}"
    border: "1px solid {colors.hairline}"
    size: 32px

## Components

### Buttons
**`button-primary`** — A flat, square-cornered ({rounded.none}) rectangle in #0099ff, the sole digital call-to-action blue. Letter-spaced uppercase Helvetica Neue at 13px gives it a functional, catalogue-stamp quality — no gradient, no shadow, no hover animation beyond a state color swap to #003388. Disabled state bleaches the fill to #b3d4fc. The shape reads as a printed label rather than a software button.

**`button-secondary`** — Transparent background with a 1px #c3c5c4 hairline border and the same uppercase button typography. Hover fills the surface with {colors.surface-soft}, the ecru tint, maintaining the warm-paper feel on interactive surfaces. No border-radius at any state.

**`button-accent-yellow`** — Used for promotional or seasonal CTAs where the full blue primary would compete with product imagery. Full #ffcc33 fill with {colors.ink} text (not white — yellow does not provide sufficient contrast for white type). Same square geometry and tracked uppercase as primary.

### Inputs
**`text-input`** — White surface against the warm canvas, 1px hairline border at rest. Focus state thickens and darkens the border to {colors.ink} without box-shadow or glow. The single-pixel upgrade is an editorial, print-derived affordance — precise rather than digital-soft.

**`search-bar`** — Compact 36px inline bar, borderless icon on the left in {colors.muted}, text at {typography.body-md}. Square cornered. Sits inline in the nav-bar at desktop widths; collapses to full-width below the nav on mobile. No search-orb or pill shape — rectilinear like everything else.

### Navigation
**`nav-bar`** — 56px height on the {colors.canvas} cream ground, separated from page content by a single 1px {colors.hairline} rule. Logo at left in {typography.title-md} (uppercase tracked Helvetica). Category links in {typography.nav-link} with no underline at rest; hairline underline appears on hover. Utility icons (search, cart, language) sit at right as 24px SVGs with 44px tap targets.

### Product Display
**`product-card`** — Square-cornered tile with a 1px soft hairline border. Product image fills a 1:1 aspect-ratio container at the top. Below: product name in {typography.product-name}, a one-line descriptor in {typography.body-sm} at {colors.body}, price in {typography.price}. A category-rule color stripe may appear at the card's top edge to signal product-line membership. Hover lifts with a very soft shadow (0 2px 8px rgba 6%) and border darkens to {colors.hairline}.

**`color-category-tag`** — Small flat chip in one of the four pure accent colors, designating product-line classification. Blue, green, yellow (dark text), and red variants each map to a discrete product family; they never mix or appear together on a single item. Tags appear adjacent to product names, in catalogue filter rails, and on category header pages. Their sharpness — no border-radius, full saturation — makes them read as industrial classification stickers rather than decorative labels.

**`color-swatch`** — 20px circular swatches for variant selection, spaced at {spacing.xs} in a horizontal row. Selected state uses a 2px {colors.ink} outer ring with a 2px gap between ring and swatch edge — a precise double-ring that reads as a mechanical selector, not a soft UI affordance.

**`category-rule`** — A 3px horizontal bar in one of the four accent colors, appearing at the top of catalogue sections, above category headings, and optionally at the top edge of product cards. Provides instant visual wayfinding across a dense product grid without requiring text labels.

**`product-specs-row`** — Two-column alternating rows (canvas tint / white) in a borderless specification table. Muted label in {typography.spec-label} at left; value in {typography.body-sm} at right. The spec table is the primary communication format for Stalogy products — notebook ruling, paper weight, page count, cover material — documented with the same precision as engineering datasheets.

**`hero-banner`** — Split layout: product image occupies the left 55% of the container at full height, copy and CTA occupy the right column on the {colors.canvas} ground. Heading in {typography.display-xl}, subhead in {typography.display-sm}, body in {typography.body-md}. No decorative illustration, no background pattern. The image column bleeds to the container edge; the copy column has {spacing.xl} inner padding. A category-rule stripe may run along the top of the banner to signal the featured product line.

**`breadcrumb`** — Lightweight trail in {typography.caption} and {colors.muted}. Slash separator in {colors.hairline}. Final active crumb in {colors.ink} with no underline. Sits above the page heading at {spacing.sm} top margin.

**`footer`** — Dark {colors.scrim} (#222222) ground with strict typographic hierarchy. Column headings in {typography.title-sm} (uppercase tracked) at {colors.surface-card}. Links in {typography.body-sm} at {colors.hairline}, brightening to {colors.surface-white} on hover. No imagery, no gradient, no decorative rule — a pure information footer.

**`pagination`** — 32px square page-number chips with 1px {colors.hairline} border. Active chip fills solid {colors.ink} with {colors.on-dark} numerals. Previous and Next rendered as bare text arrows (← →) in {typography.button-sm} at {colors.body}. Square geometry throughout; no rounded corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero stacks vertically (image top, copy below) at full viewport width; search drops to full-width strip below nav; color-category-tags become horizontal-scroll filter chips |
| Tablet | 744–1128px | Two-column product grid; full nav links visible without hamburger; hero maintains split layout at reduced padding; spec tables remain two-column |
| Desktop | 1128–1440px | Three- or four-column product grid; search bar inline in nav; hero at full 480px min-height; category sidebar appears in catalogue views; product-specs-row label column widens |
| Wide | > 1440px | Content max-width 1360px centered with auto side margins; product grid may reach 5 columns; hero padding grows proportionally; footer expands to 5 columns |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target even when visually smaller (color swatches at 20px, pagination chips at 32px)
- Nav utility icons padded to 44px tap area despite 24px rendered size
- Color-category-tag filter chips in mobile scroll strip are at least 36px tall with {spacing.sm} horizontal padding
- Product card hover states convert to tap states with no delay on touch devices

### Collapsing Strategy
- Hamburger menu slides in from left as a full-height drawer on {colors.canvas} background, matching page ground
- Product category filters collapse into a bottom-sheet modal on mobile, triggered by a sticky filter bar at the bottom of the viewport
- Spec tables remain fully visible at all breakpoints — never collapsed into accordions, as product specification is primary content for this brand
- Category-rule stripes maintain full container width at all breakpoints; height stays fixed at 3px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web fonts detected — the site relies entirely on system stacks (Helvetica Neue, Arial for Latin; Yu Mincho, Hiragino Mincho ProN for Japanese). Precise weights and optical sizing for Japanese copy cannot be confirmed without live computed style inspection.
- Meta theme-color is absent; mobile browser chrome color is unknown.
- The four accent colors (#0099ff, #00cc33, #ffcc33, #ff0033) appear systematically in extraction but their precise product-line-to-color mapping cannot be confirmed from extraction alone.
- No animation or transition timing values extractable — motion assumed minimal (under 150ms, ease-in-out) consistent with the catalogue aesthetic.
- Exact grid gutter widths and max-width breakpoints not confirmed; values estimated from catalogue conventions.
- Cart, account, and checkout UI patterns not observed in extraction.
- Whether Georgia is used for editorial prose sections distinct from Helvetica UI copy could not be confirmed.
- #ec912d (orange) and #00b7e7 (cyan) appear in the extracted palette but their precise usage context — product line accent, promotional badge, or seasonal color — is unconfirmed.
