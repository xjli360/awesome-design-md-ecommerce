---
version: alpha
name: "Poster Store"
source_url: "https://posterstore.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  What immediately distinguishes the Poster Store interface is how little it asks you to notice it — flat black type on white, hairline dividers barely thicker than a photocopy, and a product grid that reads closer to a museum print shop's light table than a conversion-optimised storefront. The philosophy is zero-competition: every CTA, filter, and navigation link is rendered in {colors.primary} black or {colors.muted} grey against a clean {colors.canvas} white so that a vermillion abstract print or a pale sage botanical can exhaust the viewport without being undercut by brand chrome. Shape vocabulary leans toward the hard-cornered — {rounded.none} on buttons and inputs, almost architectural in its refusal of pill-shapes — which gives the configurator widgets (size selectors, frame pickers, paper-type toggles) a design-tool quality that flatters the audience of print buyers who care about paper weight and margin widths. Typography is set in a neutral grotesque at modest weights; display headings sit at weight 500 rather than the aggressive 700 favoured by promotional retail, trusting that a 36px title against 64px of white breathing room communicates hierarchy through space rather than mass. Product cards are frameless or nearly so, aligned to a tight four-column grid with {spacing.lg} gaps, each card showing an image in portrait 3∶4 ratio — the same proportion as the prints themselves — followed by title and price in two spare lines of text. Filter and category navigation live in a slim horizontal strip above the grid, labels switching from {colors.muted} to {colors.ink} with a hairline underline as the only affordance for active state. The frame configurator page is where the design takes its most considered form: size chips, frame-colour swatches, and quantity selectors are all held in clean bordered rectangles at the same height, creating a specification sheet aesthetic that makes selecting a 50×70 cm oak-frame feel like specifying a bespoke print order rather than adding to a shopping cart. Footer typography stays at caption scale in {colors.muted}, a deliberate step back that keeps the editorial calm intact all the way to the page edge.

colors:
  primary: "#000000"
  primary-active: "#1a1a1a"
  primary-disabled: "#bbbbbb"
  ink: "#111111"
  body: "#333333"
  muted: "#767676"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-warm: "#e8e0d5"
  error: "#cc2200"

typography:
  display-xl:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.22
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.28
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  micro-label:
    fontFamily: "'Neue Haas Grotesk', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 14px 24px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 23px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoAlign: center
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    overflow: hidden
  product-card-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.none}"
    padding: 3px 7px
  size-selector-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 14px
    height: 40px
  size-selector-chip-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 14px
    height: 40px
  frame-option-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 8px 12px
  frame-option-chip-selected:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 8px 12px
  color-swatch:
    width: 28px
    height: 28px
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
    selectedRing: "2px solid {colors.canvas}"
  category-filter-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "1px solid {colors.ink}"
    typography: "{typography.body-sm}"
    padding: "8px 0"
    marginRight: "{spacing.lg}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    minHeight: 440px
  editorial-banner:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
  print-grid:
    columns: 4
    gap: "{spacing.lg}"
    paddingHorizontal: "{spacing.xl}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    gap: "{spacing.xs}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    buttonWidth: 40px
    height: 40px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    headingTypography: "{typography.micro-label}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Full-width or content-width black rectangle, no border-radius, uppercase tracking at 0.8px. The stark hard corner and monochrome fill make the CTA read as a deliberate editorial choice rather than a default; hover state shifts to `{colors.primary-active}` (near-black #1a1a1a) for a barely perceptible depth signal. Disabled state uses `{colors.primary-disabled}` (mid-grey #bbbbbb) without opacity hacks so assistive tools can still compute contrast cleanly.

**`button-secondary`** — Same rectangular geometry and uppercase typography as primary, but inverted: `{colors.canvas}` fill with a 1px `{colors.ink}` border. Used for secondary actions like "Save to wishlist" or "View more" at the base of category pages. On hover the border weight stays 1px but opacity reduces slightly.

**`button-text`** — Underlined body-sm text, transparent background, no border. Functions as inline navigation within the product description ("See all sizes in this series") without drawing visual weight away from the artwork photography.

---

### Inputs and Search

**`text-input`** — Hard-cornered, 48px height, 1px hairline border that sharpens to 1px ink on focus. No shadow, no glow — the only focus affordance is the border colour change from `{colors.hairline}` to `{colors.ink}`. Placeholder text in `{colors.muted}`.

**`search-bar`** — Set into the top navigation at a reduced 40px height with `{colors.surface-soft}` fill. Magnifier icon in `{colors.muted}` sits inline left; typing clears the icon. Autocomplete suggestions drop beneath in a `{colors.canvas}` panel with `{colors.hairline}` border and `{typography.body-sm}` results lines.

---

### Navigation

**`nav-bar`** — White background, 60px height, centred logo wordmark in `{typography.title-md}` weight. Left cluster holds category links in `{typography.nav-link}` 13px; right cluster holds search, wishlist, and cart icons at 20px stroke weight. A 1px `{colors.hairline}` bottom border is the only division from page content. On scroll the bar compresses to 48px with the logo staying centred.

**`category-filter-tab`** — Horizontal strip of category names (Botanical, Abstract, Typography, Photography, etc.) sitting below the nav-bar in a `{colors.surface-soft}` band. Inactive labels in `{colors.muted}`, active label switches to `{colors.ink}` with a 1px bottom border underline. No pill shape, no background fill change.

**`breadcrumb`** — Caption-scale path in `{colors.muted}` with "/" separators. The final (current) segment renders in `{colors.ink}` without a link. Sits 16px above the product title on PDP and above the grid heading on category pages.

---

### Product Card

**`product-card`** — Frameless card with 3∶4 portrait image filling the full column width, no crop shadow or overlay. Below the image: print title in `{typography.body-sm}` and price in `{typography.price-display}` (18px weight 500) sit in two left-aligned lines with `{spacing.sm}` gap. Hover state reveals a quick-add or "Select size" button overlaid at image bottom as a full-width `{colors.primary}` bar. `{rounded.none}` throughout.

**`product-card-badge`** — A minimal uppercase label ("NEW", "BESTSELLER", "LIMITED") in `{typography.micro-label}` sitting at the top-left corner of the card image, `{colors.surface-soft}` background at 80% opacity, no border-radius. Used sparingly — appearing on fewer than 10% of cards so that the badge retains signal value.

---

### Configurator Widgets

**`size-selector-chip`** — Rectangular chip, 40px height, 1px `{colors.hairline}` border. Available sizes listed as dimension strings ("30×40 cm", "50×70 cm"). Selected state: `{colors.ink}` fill, `{colors.on-primary}` text, no radius change. Out-of-stock sizes render with strikethrough text and `{colors.primary-disabled}` text, border remains.

**`frame-option-chip`** — Identical geometry to size chips but slightly shorter padding. Labels name the finish ("No frame", "White", "Black", "Oak"). Selected state upgrades the border to 2px `{colors.ink}` rather than inverting fill, preserving the text legibility of frame-name labels.

**`color-swatch`** — 28px full-circle (`{rounded.full}`) swatches for paper colour or mat variants. Normal border: 1px `{colors.hairline}`. Selected: 2px `{colors.ink}` border with a 2px `{colors.canvas}` ring gap — the classic swatch selection halo.

**`quantity-stepper`** — Inline minus/number/plus widget, 40px height, 1px `{colors.hairline}` border, hard-cornered. Minus and plus buttons each 40px wide; number display centred in `{typography.title-sm}`. The component reads as a specification field, consistent with the product-configurator register of the PDP.

---

### Editorial and Marketing

**`hero-section`** — Full-bleed `{colors.surface-soft}` background panel, 440px minimum height, centred or left-aligned heading in `{typography.display-xl}` weight 500. Used on the homepage and seasonal collection pages. No overlaid text on imagery — copy and image sit side by side in a two-column split to preserve print legibility.

**`editorial-banner`** — Mid-page band in `{colors.accent-warm}` (a warm off-white #e8e0d5), used for curated collection callouts ("Interior styles", "New arrivals for winter"). Heading in `{typography.display-md}`, body copy in `{typography.body-md}`, CTA button in primary style. The warm tone provides a gentle visual pause between grid sections without introducing a foreign colour into the palette.

---

### Footer

**`footer`** — Four-column link grid at desktop, column headings in `{typography.micro-label}` uppercase, links in `{typography.body-sm}` `{colors.muted}` that shift to `{colors.ink}` on hover. 1px `{colors.hairline}` top border. Newsletter email field and submit button sit in a fifth narrower column. Bottom strip carries legal text in `{typography.caption}` `{colors.muted}`.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Print grid collapses to 2 columns; nav condenses to logo + hamburger + cart; size/frame chips reflow to wrapping flex rows; hero section goes single-column stacked image-over-text |
| Tablet | 744–1128px | 3-column print grid; nav shows logo + top-level category links + icons, secondary links hidden; configurator chips in 2-column grid; hero stays two-column split |
| Desktop | 1128–1440px | 4-column print grid; full nav visible with category strip beneath; hero full-bleed 440px; PDP uses 2-column split (image left 55%, configurator right 45%) |
| Wide | > 1440px | Grid max-width caps at 1400px, centred; hero image enlarges proportionally; footer columns gain additional whitespace padding |

### Touch Targets

- All chips (size, frame, colour swatch) have a minimum tap target of 44×44px even when visually smaller via padding
- Cart and wishlist icon buttons in nav are 44×44px touch areas regardless of icon stroke size
- Quantity stepper buttons are 44px wide on touch viewports
- Bottom-of-card quick-add button spans full card width at mobile for easy tap

### Collapsing Strategy

- Navigation collapses to hamburger at < 744px; drawer slides in from left with full category hierarchy
- Category filter strip scrolls horizontally on mobile with no wrap; fades at edges to indicate overflow
- Configurator chips wrap to multiple rows rather than scroll horizontally — configurability is the core action and must remain fully visible without gesture exploration
- Footer collapses to single-column accordion on mobile; each section heading is a tap target to expand links

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Extraction blocked by Vercel Security Checkpoint**: the live crawl returned Vercel's bot-protection page rather than posterstore.com. All extracted hex values (#0070f3, #3291ff) and font stacks are from Vercel's checkpoint UI, not from the brand — they have been discarded entirely.
- **Actual brand palette unconfirmed**: the black/white/grey palette above is inferred from widely-observed Scandinavian minimal print-shop conventions and publicly visible Poster Store marketing imagery; no hex values have been confirmed from source CSS.
- **Typeface unconfirmed**: "Neue Haas Grotesk" is a plausible choice for the brand register but the actual loaded webfont (could be GT America, Söhne, Inter, or a custom cut) was not extractable. Font-family fallback chain is a safe system-font approximation only.
- **Primary CTA colour**: assumed black — could be a dark charcoal or a brand-specific near-black that differs from pure #000000.
- **Frame configurator exact interaction model**: hover/selection states for frame chips are inferred from common configurator patterns; actual animation curves, shadow depth, and transition timing are unknown.
- **Promotional or sale badge colour**: unknown whether discount badges use a red, black, or accent tone — defaulted to `{colors.surface-soft}` / `{colors.ink}` conservatively.
- **Logo treatment**: wordmark vs. typeset logotype and exact weight/spacing not confirmed.
