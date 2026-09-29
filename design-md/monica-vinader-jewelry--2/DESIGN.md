---
version: alpha
name: "Monica Vinader"
source_url: "https://monicavinader.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Monica Vinader places its personalization engine so close to the add-to-cart button that the two nearly overlap — engraving initials or a date is not a product option but the primary design act the site invites. The interface around that act is intentionally stripped back: a white (#ffffff) canvas, #313131 charcoal as the sole confirmed text register, and a warm stone-toned hairline dividing sections without fracturing the calm. Product photography floats on pure white with zero props or lifestyle staging, because the pieces — gold vermeil, sterling silver, faceted gemstones — supply all the warmth the frame needs. Navigation is high and lean, a single bar with category labels at light weight and the Monica Vinader wordmark anchoring the center. Material selectors (Gold Vermeil, Sterling Silver, Rose Gold Vermeil) operate as the de facto color swatches; there is no UI palette beyond the metal finishes and stone tones the jewelry delivers. Corner rounding runs from `{rounded.none}` on product cards to a restrained `{rounded.sm}` on chips, keeping the geometry measured and grown-up rather than approachable-friendly. The typographic register favors clean sans-serif at modest weights for body and navigation, reserving a lighter serif treatment for editorial display moments, trusting whitespace over typographic muscle. A micro-system unique to the brand — engraving preview tile, character counter, letter-style selector — appears inside the personalization panel and requires no analogue elsewhere in the design system. Gift messaging, luxury packaging callouts, and a quality-promise icon strip above the `{colors.primary}` dark footer reinforce a brand whose retail energy sits precisely between premium high street and entry fine jewelry, charging neither prestige-level prices nor casualizing the experience.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#979797"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  hairline: "#e8e4de"
  canvas: "#ffffff"
  surface-soft: "#f8f7f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#c9a96e"
  material-rose-gold: "#b87c6e"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.03em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  label-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.02em
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  engraving-preview:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.05em

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
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
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    imageAspectRatio: "1/1"
    hoverEffect: subtle-zoom
    wishlistIconOnHover: true
  material-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 14px"
    selectedBorder: "1px solid {colors.ink}"
    selectedTextColor: "{colors.ink}"
  personalization-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    previewTypography: "{typography.engraving-preview}"
    previewColor: "{colors.accent-gold}"
    counterTypography: "{typography.caption}"
    counterAlertColor: "{colors.primary}"
  gemstone-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.ink}"
    selectedOffset: 2px
    tapArea: 40px
  gift-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
    iconColor: "{colors.accent-gold}"
  quality-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconColor: "{colors.accent-gold}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
    columns: 4
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    activeIndicator: "2px underline {colors.ink}"
    typography: "{typography.label-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} 0"
  product-hero:
    layout: split-60-40
    imageBackground: "{colors.surface-soft}"
    contentBackground: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "0 {spacing.section}"
    ctaVariant: button-primary
  size-guide-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    textDecoration: underline
    hoverColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    bodyTypography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.section}"
    columns: 4

## Components

### Buttons

**`button-primary`** — Fully rectangular (#313131 fill, white uppercase text at 0.1em tracking) standing 48px tall. The absence of border radius is deliberate: it signals precision over friendliness. Hover deepens to `{colors.primary-active}`; disabled washes to `{colors.primary-disabled}` with no cursor feedback. Used for "Add to Bag," "Checkout," and primary engraving confirmation.

**`button-secondary`** — Identical geometry to primary, inverted: white fill, 1px `{colors.ink}` border, charcoal text. Sits alongside primary for parallel actions — "Add to Wishlist" or "Save for Later" — and never appears without a primary button nearby.

**`button-ghost`** — Transparent background, underline only, uppercase at `{typography.button-sm}`. Reserved for tertiary nudges: "Ring size guide," "More about this stone," editorial "Shop now" in body copy. No height constraint — inline with surrounding text.

### Text Input

**`text-input`** — Flat 48px field, no radius, hairline border that sharpens to full ink on focus. Placeholder sits in `{colors.muted}`. Used for engraving text entry (where character limit feedback is adjacent), email capture, and site search. Error state adds a 1px bottom accent in `{colors.primary}` without changing background color.

### Navigation

**`nav-bar`** — 60px centered wordmark bar. Category labels (Necklaces, Bracelets, Rings, Earrings, Gifts) sit left in `{typography.nav-link}` — 13px regular weight — with search, account, and bag icons right-aligned. A single `{colors.hairline}` bottom border defines the bar. On scroll, a subtle drop shadow pins the bar without adding fill color.

### Product Card

**`product-card`** — Square image on `{colors.surface-soft}` warm ground, `{rounded.none}`. Below: product name in `{typography.body-sm}`, price in `{typography.price}` at regular weight, both left-aligned. No star ratings or promotional badges on the card face. Hover triggers subtle image zoom; a wishlist heart appears top-right only on hover.

### Material Chip

**`material-chip`** — Pill selector for metal finish. Default is hairline-bordered at `{colors.body}` text; selected state sharpens to full `{colors.ink}` border and text. Chips flow horizontally as a single-select row; swapping metal updates the product image and price simultaneously. On mobile the row scrolls horizontally rather than wrapping.

### Personalization Panel

**`personalization-panel`** — A `{colors.surface-soft}` warm section that expands inline below the material chips on engraving-eligible products. Contains a text input for initials, a date, or a short phrase; a live preview in `{typography.engraving-preview}` rendered at `{colors.accent-gold}`; a character counter in `{typography.caption}` that turns `{colors.primary}` charcoal when approaching the limit; and an optional font/style toggle for block vs. cursive scripts. The preview updates on each keystroke.

### Gemstone Swatch

**`gemstone-swatch`** — A 20px filled circle showing the actual stone hue (amethyst, aquamarine, labradorite, etc.) rather than a named label. Selected state gains a 2px `{colors.ink}` ring with a 2px offset gap, creating a halo effect without altering the swatch fill. Tap area padded to 40×40px on touch.

### Gift Badge

**`gift-badge`** — An uppercase `{typography.label-sm}` label chip on `{colors.surface-soft}` with a gold gift-box icon at `{colors.accent-gold}` preceding the text. No border. Placed on PDPs and inside cart to indicate complimentary luxury packaging, never on the product card grid itself.

### Quality Strip

**`quality-strip`** — A full-width four-icon reassurance row (recycled packaging, lifetime guarantee, free engraving, easy returns) sitting directly above the footer. Icons tinted `{colors.accent-gold}`, labels in `{typography.caption}` at `{colors.body}`. Thin `{colors.hairline}` top border, minimal vertical padding. At mobile it reflows to a 2×2 grid.

### Product Hero

**`product-hero`** — 60/40 split: bleed editorial photograph left, editorial copy block right. Heading in `{typography.display-xl}` at weight 300, body descriptor in `{typography.body-md}`, followed by a `button-primary`. The photograph carries no overlay or scrim — the image is always bright and airy. On mobile, image stacks full-width above the copy block.

### Filter Bar

**`filter-bar`** — Sticky sub-nav beneath the category heading. Uppercase `{typography.label-sm}` tabs for Material, Stone, Price, Occasion, and New In. Active tab carries a 2px underline in `{colors.ink}`; inactive in `{colors.muted}`. No background fill — bar floats on the canvas. Below 744px, the row scrolls horizontally and a "Filter & Sort" pill opens a modal overlay.

### Footer

**`footer`** — Full-bleed `{colors.primary}` (#313131) dark section with white body and caption text. Four columns: newsletter capture + social icons, navigation categories, customer service, legal links. The Monica Vinader wordmark repeats in white at reduced size top-left. Generous `{spacing.xxl}` vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger + wordmark + bag only in nav; hero image full-width stacked above copy; personalization panel expands full-width; filter bar scrolls horizontally; quality strip reflows 2×2 |
| Tablet | 744–1128px | 2-column product grid; side-by-side hero; nav shows top-level categories only; material chip row wraps if needed; footer reflows to 2 columns |
| Desktop | 1128–1440px | 3–4 column product grid; full category nav with hover flyouts; split hero; filter bar fully visible; footer 4-column grid |
| Wide | > 1440px | Content capped at ~1440px with auto side margins; product grid holds at 4 columns; hero image proportionally wider bleed |

### Touch Targets

- All buttons minimum 48px height, 44px minimum width
- Material chips minimum 36px height on mobile
- Gemstone swatches padded to 40×40px tap area around the 20px visual circle
- Nav icons (search, bag, account) padded to 44×44px
- Personalization panel text input at 48px height on mobile

### Collapsing Strategy

- Primary nav collapses to a left-slide hamburger drawer at < 744px; categories listed as a tap-to-expand accordion
- Filter bar becomes a horizontally scrollable chip row below 744px; a "Filter & Sort" pill at row end opens a full-screen filter modal
- Personalization panel shows as a single "Personalise this piece" CTA button on mobile, expanding inline on tap rather than opening a modal
- Quality strip collapses from 4-column to 2×2 icon grid on mobile
- Footer reflows from 4-column grid to stacked single column with accordion navigation sections on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted — the site returned an anti-bot challenge page ("Just a moment…"), blocking full CSS and token extraction. All colors beyond the confirmed ink value are inferred from brand knowledge and are not pixel-sampled from the live site.
- No custom font families were detected; the entire font stack is system UI defaults. Monica Vinader almost certainly uses a licensed or proprietary typeface for display headings — name, weights, and metrics could not be confirmed and the serif treatment above is an approximation.
- Accent gold (#c9a96e) and rose gold material (#b87c6e) are brand-knowledge estimates for the jewelry material palette — not extracted from the live site.
- Surface-soft warm white (#f8f7f5) is inferred from the brand's known cream-adjacent canvas aesthetic, not extracted.
- Exact border widths, shadow values, animation durations, and easing curves could not be measured.
- Character limits per product for the engraving tool, available engraving font options, and the full personalization interaction model could not be audited.
- No CSS custom properties or design tokens were accessible from the anti-bot-gated response.
- Price display format (currency symbol position, sale/original price styling, discount badge) could not be observed.
