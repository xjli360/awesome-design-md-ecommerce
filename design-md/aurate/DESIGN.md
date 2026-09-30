---
version: alpha
name: "Aurate"
source_url: "https://auratenewyork.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The decision to anchor a fine jewelry brand on deep forest green — #304038, the most distinctive hue in the extracted palette — is the first signal that Aurate operates outside jewelry's conventional white-and-gold script. This bottle-green primary carries every major CTA and structural marker, resting against warm parchment canvases (#efeae6, #f5f2f0) that photograph gold with the same enveloping warmth a gallery uses for illuminated manuscripts. The sustainability argument is inscribed in the color system itself: sage progressions move from #bfccb8 through #739487 to #42544f, a three-stop botanical gradient that reads as though the brand is literally rooted in the material ethics it argues on its sourcing pages. Gold in this system is amber, not yellow — #b26118 carries the mid-tone, #994707 the deeper rust-orange, and #ffd196 the pale champagne highlight; together they describe real gold across 10k, 14k, and 18k alloys, warm and variable, rather than the flat cartoon-yellow most jewelry brands reach for. The cream canvas tones (#ece6e2, #f5f2f0) function as a photography environment: low-contrast, warm-tinted, archival. Type structure leans on a serif-first display hierarchy consistent with editorial fine jewelry — large letterforms at low weight against the cream canvas, with generous tracking on uppercase labels and near-zero tracking on running body text; navigation and utility text drop to the system sans-serif stack, reserving the editorial register for moments where the brand is speaking rather than routing. Corner radius is architecturally conservative: pill shapes ({rounded.full}) appear on filter tags and sustainability callouts; product cards land on softer {rounded.sm} corners; the primary CTA takes {rounded.xs}, projecting confidence and structure over softness. Spacing is deliberately wide — {spacing.section} breathing room between content bands, narrow editorial columns flanked by large margins, and a product grid that never crowds more than two items per row on mobile.

colors:
  primary: "#304038"
  primary-active: "#272727"
  primary-disabled: "#bfccb8"
  gold: "#b26118"
  gold-deep: "#994707"
  gold-pale: "#ffd196"
  sage: "#739487"
  sage-light: "#bfccb8"
  sage-deep: "#42544f"
  mint-tint: "#e6f7f4"
  ink: "#1c1c1c"
  body: "#272727"
  muted: "#5f6a66"
  muted-soft: "#9b9b9b"
  hairline: "#e8e8e8"
  hairline-soft: "#eaeaea"
  canvas: "#fdfcfc"
  surface-soft: "#f5f2f0"
  surface-card: "#efeae6"
  surface-warm: "#ece6e2"
  on-primary: "#fdfcfc"
  error: "#ea0202"

typography:
  display-xl:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: 0.01em
  display-md:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.005em
  title-md:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  label-uppercase:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  price-display:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.05em

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
    padding: 0
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "4/5"
    rounded: "{rounded.sm}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.gold-deep}"
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 640px
    padding: "{spacing.section} {spacing.xxl}"
  sustainability-badge:
    backgroundColor: "{colors.mint-tint}"
    textColor: "{colors.sage-deep}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    padding: "6px 12px"
  material-pill:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    borderColorSelected: "{colors.primary}"
    backgroundColorSelected: "{colors.primary}"
    textColorSelected: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  karat-selector:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    borderColorSelected: "{colors.gold}"
    textColor: "{colors.body}"
    textColorSelected: "{colors.gold-deep}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  product-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.xl}"
    gap: "{spacing.lg}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  collection-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorActive: "{colors.primary}"
    backgroundColorActive: "{colors.primary}"
    textColorActive: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  wishlist-icon:
    backgroundColor: transparent
    iconColor: "{colors.muted}"
    iconColorActive: "{colors.primary}"
    size: 20px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.sage-light}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    padding: "{spacing.section} {spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Forest-green (#304038) fill with white uppercase spaced lettering, flat {rounded.xs} corners, and a full 48px touch height. Pressed state deepens to near-black (#272727); disabled state desaturates to the pale sage (#bfccb8) with {colors.muted} text. The 0.1em letter-spacing on {typography.button-md} gives the label an editorial cadence that echoes fine-jewelry tagging conventions rather than tech-startup boldness.

**`button-secondary`** — White fill with a 1px forest-green border and matching green uppercase text. Shares the same 48px height and {rounded.xs} corners as the primary, creating a coherent size system where the two can sit side by side in add-to-cart / save-for-later pairings without competing weights. Hover inverts to the primary fill.

**`button-ghost`** — Transparent background with underlined ink-colored label in {typography.button-md}. Used for tertiary actions such as "learn more" and editorial navigation links where a full button container would interrupt the reading flow of a content band.

**`button-gold`** — Amber fill (#b26118) reserved for high-priority promotional CTAs — limited-edition releases, gift prompts, and sale countdowns. Shares {rounded.xs} geometry and {typography.button-md} lettering with the primary family to maintain size cohesion while signaling a distinct editorial register.

### Text Input

**`text-input`** — Clean white field with a thin {colors.hairline} border that sharpens to {colors.primary} on focus. At {rounded.xs} it reads architectural rather than approachable. Placeholder text in {colors.muted-soft} lightens the empty state without injecting brand color; the 48px height aligns with all button targets for consistent form rows.

### Navigation

**`nav-bar`** — White bar at 64px, separated from page content by a {colors.hairline-soft} bottom border rather than a drop shadow. Nav links at 13px with 0.05em letter-spacing are set in the system sans-serif — legible but not dominant. Logo and category links sit to the left; account, search, and cart icons anchor the right, following standard Shopify jewelry nav conventions.

### Product Card

**`product-card`** — The 4:5 portrait aspect ratio is chosen for necklace and earring shots on a warm parchment backdrop. Card background matches {colors.surface-card} (#efeae6) so the image and container share the same creamy warmth rather than creating a hard edge. Title in {typography.body-sm} and price in {typography.price-display} (20px serif, weight 400) establish a size-first hierarchy; sale prices shift to {colors.gold-deep} (#994707) — an amber accent that reads as a price event without an alarm red.

### Hero Banner

**`hero-banner`** — Full-width editorial band on {colors.surface-soft} (#f5f2f0) with headline in {typography.display-xl} (52px, weight 300 serif). The deliberate light weight at large size reads as editorial luxury: type recedes into the image rather than competing with it. A single-sentence subline in {typography.body-md} sits between the headline and a {button-primary} CTA, keeping the text hierarchy to three clear levels.

### Sustainability Badge

**`sustainability-badge`** — A pill-shaped callout ({rounded.full}) on {colors.mint-tint} (#e6f7f4) with {colors.sage-deep} (#42544f) text, used to label recycled gold, conflict-free stones, and B-Corp status. The pill shape distinguishes it from the product card's {rounded.sm} corners — it reads as a certification label rather than a content container. {typography.label-uppercase} at 0.12em tracking makes the text scannable in the context of dense product description copy.

### Material & Karat Selectors

**`material-pill`** — Horizontal scrollable pill row on product detail pages for metal finish selection (yellow gold, white gold, rose gold). Resting state uses {colors.surface-warm} background with {colors.hairline} border; selected state inverts to {colors.primary} fill with white text, mirroring the button-primary language so the selection feels like a decision rather than a filter. {rounded.full} shape signals these are toggles, not inputs.

**`karat-selector`** — Rectangular chip group for 10k / 14k / 18k gold grade selection. Uses {rounded.sm} corners to visually distinguish it from the pill-style material selector, making the two controls scannable as separate decision layers. Selected state highlights the border in {colors.gold} (#b26118) and shifts label text to {colors.gold-deep} — a gold-on-gold affirmation rather than a hard color inversion.

### Promo Banner

**`promo-banner`** — A slim forest-green bar (#304038) pinned above or below the nav, carrying sitewide promotions in centered {typography.label-uppercase} white text. Shares the same {colors.primary} as the CTA buttons, so the promotional message reads as structural brand communication rather than an interruptive sale alert.

### Collection Filters

**`collection-filter-pill`** — Scrollable horizontal filter bar on collection pages. Resting pills use {colors.surface-soft} with a {colors.hairline} outline; active selections fill with {colors.primary}. At {rounded.full} these are clearly filter tags rather than navigation links. {typography.caption} at 12px keeps the filter bar compact, preventing it from overwhelming the product grid beneath.

### Footer

**`footer`** — Full-width forest-green band (#304038) with white body text and {colors.sage-light} (#bfccb8) link accents — the sage color creates a tonal echo of the green palette while maintaining accessible contrast against the dark background. Section headings in {typography.label-uppercase} (0.12em tracking) organize the newsletter capture, sustainability links, and support columns into a four-column grid on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + cart icon; hero banner stacks text below image at reduced type scale; material and karat selectors scroll horizontally; promo banner wraps to two lines |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories inline with secondary categories in dropdown; hero banner returns to side-by-side layout at reduced min-height (480px) |
| Desktop | 1128–1440px | Three-column product grid; full nav with hover dropdowns for collections; hero banner at full 640px min-height; product detail panel splits 60/40 image-to-content with sticky right panel |
| Wide | > 1440px | Content columns max at 1400px with auto side margins; four-column product grid in broad collections; hero typography scales to display-xl at full 52px with generous leading |

### Touch Targets

- All buttons maintain 48px minimum height across breakpoints
- Karat and material selector chips have 44px minimum tap height on mobile despite compact visual size
- Nav icons (search, cart, account) are padded to 44×44px touch targets regardless of icon visual size
- Wishlist icon on product card has a 36px minimum tap target via padding expansion on mobile
- Promo banner text links padded to 44px vertical tap target on mobile

### Collapsing Strategy

- Navigation: full horizontal bar on desktop collapses to a hamburger drawer on mobile; drawer uses {colors.primary} as its background fill for full-brand immersion
- Product filters: horizontal scroll bar on mobile; left-rail sticky sidebar from tablet up
- Hero banner: stacked image-above / text-below on mobile; side-by-side from tablet up
- Product detail page: single-column scroll on mobile; sticky right-rail content panel at 1128px+
- Footer: single-column accordion on mobile with sections collapsed; four-column grid on desktop with all sections expanded by default

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom webfont not captured — the site loads its display typeface (likely an editorial serif such as Freight Display Pro or a licensed Shopify-compatible equivalent) via theme JavaScript; all extracted font stacks are system fallbacks. Serif display tokens use Georgia as a placeholder.
- Font weight and size values for live headings and product page type cannot be confirmed without executing the page JavaScript; all typographic scale values are inferred from fine-jewelry editorial conventions.
- Hover and focus transition timing and easing not capturable from static CSS extraction.
- Box-shadow values for product cards, modals, and dropdowns not detected in extraction.
- Mobile nav drawer animation direction, overlay opacity, and transition duration are inferred, not extracted.
- Exact letter-spacing and line-height values for live nav and product page headings are unconfirmed.
- Dark-mode or seasonal theme variants (if any) not detected in extraction.
- Ring and chain product selectors (size, chain length) may use distinct UI patterns not covered here.
