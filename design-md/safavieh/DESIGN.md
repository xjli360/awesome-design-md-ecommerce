---
version: alpha
name: "Safavieh"
source_url: "https://safavieh.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Safavieh's most telling design decision is its primary: deep regal indigo (#221155), a color that most home-furnishings competitors relegate to a footer accent while defaulting to beige or slate for their main CTAs. Against a near-white canvas of #fcfcfc and #f9f9f9, that indigo reads almost Ottoman — a chromatic echo of the Persian rug heritage the brand has cultivated since 1914, made visible in every button, announcement strip, and footer block. The companion voltage is #fdd314, a warm marigold gold that stops just short of brash; it fires on sale badges, accent CTAs, promotional banners, and footer link hovers, creating a jewel-tone duality that feels deliberate rather than accidental. Secondary deep blue (#003399) surfaces in selected navigation and link states, extending the cool-register palette without diluting the indigo anchor.

  Type architecture runs two distinct tracks. Cormorant Garamond handles every display moment — collection names, editorial headlines, hero callouts — at light-to-medium weights and generous letter-spacing, letting the letterforms open up rather than press. Montserrat carries all functional UI: navigation labels at weight 600 with a 0.04em letter-space, body copy at 14px/1.6, and all-caps button labels at weight 700 with 0.10em tracking. The pairing avoids the common trap of mixing a serif and a grotesque at equal visual authority; Cormorant takes the spacious editorial register, Montserrat delivers the grid discipline that a large-SKU catalog requires.

  Component geometry is angular throughout — {rounded.none} on buttons, inputs, product cards, and filter chips. This flatness keeps rug and furniture photography in full command: any soft corner radius would compete with the organic medallion patterns and pile textures that are the actual product. Spacing follows an 8-point grid with {spacing.section} section breaks maintaining visual calm across dense category grids. The hero plants on {colors.primary} indigo with a {typography.display-xl} Cormorant headline and a marigold accent button, signaling that promotions are announced with ceremony rather than whispered. Navigation runs two tiers — a slim #221155 announcement strip above a #fcfcfc main bar — keeping promotional messaging physically separate from wayfinding. The footer mirrors the top strip exactly, completing a frame that brackets the entire shopping experience in the brand's indigo-gold axis.

colors:
  primary: "#221155"
  primary-active: "#150a38"
  primary-disabled: "#9087b5"
  accent-gold: "#fdd314"
  accent-gold-active: "#e6bc00"
  secondary-navy: "#003399"
  ink: "#2d2d2d"
  body: "#505050"
  muted: "#8c8c8c"
  hairline: "#abb8c3"
  hairline-soft: "#e0e0e0"
  canvas: "#fcfcfc"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#221155"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'Times New Roman', Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Cormorant Garamond', 'Times New Roman', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.015em
  display-sm:
    fontFamily: "'Cormorant Garamond', 'Times New Roman', Georgia, serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.28
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.05em
  title-sm:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.06em
    textTransform: uppercase
  body-md:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  button-md:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.10em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-was:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  tag-label:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  announce-strip:
    fontFamily: "'Montserrat', Arial, Tahoma, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 46px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 46px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 46px
  button-gold-active:
    backgroundColor: "{colors.accent-gold-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.on-primary}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 46px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  announce-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announce-strip}"
    height: 36px
    paddingX: "{spacing.base}"
    linkColor: "{colors.accent-gold}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 40px
  nav-mega-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "2px solid {colors.primary}"
    paddingY: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    wasPriceTypography: "{typography.price-was}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.sm}"
    hoverShadow: "0 4px 16px rgba(34,17,85,0.10)"
  sale-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-accent}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.accent-gold}"
    ctaTextColor: "{colors.on-accent}"
    ctaTypography: "{typography.button-md}"
    minHeight: 520px
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
  editorial-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    accentColor: "{colors.accent-gold}"
    paddingY: "{spacing.section}"
  promo-ribbon:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-accent}"
    typography: "{typography.announce-strip}"
    paddingY: "{spacing.sm}"
    paddingX: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 44px
    iconColor: "{colors.primary}"
    submitBackgroundColor: "{colors.primary}"
    submitIconColor: "{colors.on-primary}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    overlay: "rgba(34,17,85,0.30)"
    hoverOverlay: "rgba(34,17,85,0.55)"
    aspectRatio: "3/4"
  pagination:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 36px
    width: 36px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    linkColor: "{colors.accent-gold}"
    linkHoverColor: "{colors.canvas}"
    borderTop: "3px solid {colors.accent-gold}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Full-width or inline CTA on {colors.primary} indigo fill, all-caps Montserrat at 0.10em tracking, sharp {rounded.none} corners throughout. Hover/active state deepens to {colors.primary-active} (#150a38); disabled washes to {colors.primary-disabled}. Used for primary actions: "Add to Cart", "Shop Now", "Apply Filters".

**`button-gold`** — The accent CTA reserved for hero banners, promotional modules, and top-of-funnel entry points where the {colors.accent-gold} marigold creates maximum contrast against {colors.primary} indigo backgrounds. Active state shifts to {colors.accent-gold-active}. Text in {colors.on-accent} keeps the dark indigo readable against the bright fill.

**`button-secondary`** — Outlined variant: {colors.canvas} background with 1px {colors.primary} border and indigo text. Matches button-primary height (46px) for side-by-side pairing. Used for secondary actions like "Save to Favorites", "Compare", "View More".

**`button-ghost`** — Inverted outline for use on dark/indigo surfaces — transparent background with 1px white border and white text. Appears in hero banners alongside `button-gold` where two CTAs are needed.

### Navigation

**`announce-strip`** — 36px tall {colors.primary} bar at the very top of the viewport. Montserrat 12px/600 weight in white with {colors.accent-gold} link text for promotional links. Contains shipping thresholds, sale announcements, account links.

**`nav-bar`** — 64px {colors.canvas} bar with 1px {colors.hairline-soft} bottom border. Logo left-aligned at 40px height. Main category links in `{typography.nav-link}` Montserrat 600 with hover underline in {colors.primary}. Utility icons (search, wishlist, cart) right-aligned.

**`nav-mega-panel`** — Full-width dropdown with {colors.canvas} background and a 2px {colors.primary} top accent border. Section headings in `{typography.title-sm}` (all-caps Montserrat), body links in `{typography.body-sm}`. Grid of 4–6 columns with featured category imagery.

### Product Cards

**`product-card`** — Square image at 1:1 aspect ratio, no border radius, thin whitespace padding at {spacing.sm}. Title in `{typography.body-md}`, price in `{typography.price-display}` weight 700, sale/was price struck through in `{typography.price-was}`. On hover, a subtle box-shadow `rgba(34,17,85,0.10)` lifts the card off the grid. Sale badges (`sale-badge`) and new-arrival badges (`new-badge`) pin to the top-left corner of the image.

### Search

**`search-bar`** — Full-width or inline rectangle at 44px height, 1px {colors.hairline} border, {rounded.none}. Submit button is a {colors.primary} filled square with white icon flush right, creating a compound input-plus-button form. Focuses with 1px {colors.primary} border.

### Hero & Editorial

**`hero-banner`** — Full-bleed {colors.primary} indigo panel, minimum 520px tall. Cormorant Garamond `{typography.display-xl}` headline in white, Montserrat `{typography.body-md}` supporting copy in white at reduced opacity, and a `button-gold` CTA. Side-by-side layout on desktop (copy left, lifestyle image right), stacked on mobile.

**`editorial-banner`** — {colors.surface-soft} background with `{typography.display-md}` Cormorant Garamond headline, body in `{typography.body-md}`, and a thin {colors.accent-gold} decorative rule below the headline. Used for mid-page brand story modules.

### Taxonomy & Filters

**`category-tile`** — Portrait 3:4 tiles with full-bleed photography and `rgba(34,17,85,0.30)` indigo overlay. Title in `{typography.title-sm}` white at bottom-left. Hover deepens overlay to `rgba(34,17,85,0.55)`. No border radius — the rectangular grid mirrors the rug geometry of the products.

**`filter-chip`** — Flat rectangular chips on {colors.surface-soft}, 1px {colors.hairline} border, `{typography.caption}` text. Active state flips to full {colors.primary} fill with white text. Used for size, color, material, style, and price-range filters in the left-rail PLP sidebar.

### Commerce Utilities

**`sale-badge`** — {colors.accent-gold} rectangle with {colors.on-accent} text in `{typography.tag-label}` (10px all-caps Montserrat). Pins top-left on product card imagery.

**`promo-ribbon`** — Full-width {colors.accent-gold} bar with {colors.on-accent} text, used between page sections to announce time-limited offers. Distinct from `announce-strip` (which is indigo and lives above the nav).

### Footer

**`footer`** — Full-width {colors.primary} indigo ground, 3px {colors.accent-gold} top border as a visual bookmark. Four-column link grid with `{typography.title-sm}` white headings and `{typography.body-sm}` {colors.accent-gold} links. Newsletter signup uses `text-input` on the dark surface with adjusted border to `rgba(255,255,255,0.3)`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks copy above image; nav collapses to hamburger; filter chips move into a bottom-sheet drawer |
| Tablet | 744–1128px | Two-column product grid; mega-nav simplifies to fly-out; hero runs side-by-side at reduced text size |
| Desktop | 1128–1440px | Three- or four-column product grid; mega-nav full-width panel; hero at full display-xl scale; left-rail filter sidebar visible |
| Wide | > 1440px | Grid max-width capped at 1440px, centered; hero image fills remaining viewport width; category tiles expand proportionally |

### Touch Targets

- All buttons minimum 46px tall, 44px minimum width on mobile
- Filter chips expand to minimum 40px touch height on mobile
- Nav links in hamburger menu minimum 48px row height
- Add-to-Cart and primary CTAs full-width on screens below 480px

### Collapsing Strategy

- Mega-nav collapses to hamburger at < 1024px; categories accessible via accordion slide-out drawer
- Left-rail filters collapse to a "Filter & Sort" sticky bar that opens a full-screen modal on mobile
- Category tiles reduce from 4-across to 2-across at tablet and 1-across (horizontal scroll strip) on mobile
- Announce strip hides on screens below 375px to preserve vertical space
- Footer compresses from 4-column to 2-column at tablet, single accordion-expanded column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Several extracted hex values (#f78da7, #cf2e2e, #ff6900, #fcb900, #7bdcb5, #00d084, #8ed1fc, #0693e3, #9b51e0, #81d742, #dd3333, #bb0000) match the WordPress/Gutenberg block editor's default color palette exactly — these are almost certainly CMS editor colors, not brand tokens, and were excluded from the palette
- Exact button border-radius and hover transition durations not confirmed from live site; {rounded.none} inferred from brand positioning and rug-geometry visual language
- Cormorant Garamond and Montserrat confirmed as font stacks from extraction, but precise weight variants per section (light vs regular vs semibold for Cormorant) were not enumerable; weights above represent likely mapping
- No confirmed hover/focus ring color for interactive elements beyond the primary indigo
- Mobile navigation structure (hamburger vs tabs) not confirmed; accordion drawer pattern assumed from category depth
- Custom icon set or icon library not identifiable from extraction — icon style (line vs filled, stroke weight) unknown
- Price formatting details (currency symbol size, sale price color treatment) inferred from standard e-commerce patterns, not confirmed from live DOM
