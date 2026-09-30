---
version: alpha
name: "Seville Classics"
source_url: "https://www.sevilleclassics.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Crimson at the OS level — Seville Classics sets #c82423 as its meta theme-color, meaning the browser chrome itself blushes red before a single pixel of the page loads. That signal carries through every primary CTA, sale badge, and urgency stripe, while the companion navy #003399 grounds the navigation bar, category headers, and structural promotional banners in a palette that reads simultaneously as authority and utility. The dual-anchor approach — warm red for action, cool navy for structure — runs through a type system that contrasts Playfair Display's editorial serif weight in hero headlines against Lato's workmanlike clarity in body copy and Source Sans Pro's crisp precision at UI scale. Buenard, a distinctive old-style serif with ink-trap cuts, surfaces in display-level lockups where the brand signals craft and permanence over commodity efficiency.

  The warm neutrals extracted from the live site — #5b544f, #403b37, and #54585b — are not generic product-page grays. They carry the warmth of wood grain and powder-coated steel, the material language of a well-organized garage or workshop. Canvas pages sit at #fafafa rather than clinical pure white, adding just enough warmth to keep the experience livable, while hairlines at #dedede hold the grid visible without sharpness.

  Cards use minimal rounding ({rounded.xs} at 4px) — enough to avoid the harshness of raw 0px corners without softening the brand's functional seriousness. Form elements and search bars follow the same discipline. The grid is generous and informational, with category-driven navigation pointing users toward storage systems, workbenches, and garage organizers rather than editorial storytelling. Product imagery dominates at full bleed or in tight 4:3 crops; the physical presence of steel shelving, rolling workbenches, and pegboard panels does the persuasion work. A persistent promo bar — rendered in navy or swapped to red for urgency — sits above the primary navigation, carrying free-shipping thresholds in Source Sans Pro at 13px, compressed but readable.

colors:
  primary: "#c82423"
  primary-active: "#b2201f"
  primary-disabled: "#e89898"
  navy: "#003399"
  navy-active: "#002277"
  ink: "#121212"
  body: "#403b37"
  muted: "#5b544f"
  muted-light: "#54585b"
  hairline: "#dedede"
  hairline-soft: "#dddada"
  canvas: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-navy: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Playfair Display', Georgia, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Buenard', Georgia, serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', 'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Source Sans Pro', 'Lato', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Source Sans Pro', 'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Lato', 'Source Sans Pro', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.25px
  promo-bar:
    fontFamily: "'Source Sans Pro', 'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Source Sans Pro', 'Lato', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-lg:
    fontFamily: "'Lato', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
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
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.navy-active}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.navy}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  promo-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.promo-bar}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageBorderRadius: "{rounded.xs}"
    padding: "{spacing.base}"
    shadow: "0 1px 4px rgba(0,0,0,0.10)"
    shadowHover: "0 4px 12px rgba(0,0,0,0.16)"
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  category-chip-active:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-primary
    padding: "{spacing.section} {spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-light}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    submitButtonBackground: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
    height: 44px
  price-display:
    saleColor: "{colors.primary}"
    originalColor: "{colors.muted-light}"
    priceTypography: "{typography.price-lg}"
    strikeTypography: "{typography.price-sm}"
    textDecoration: line-through
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons
**`button-primary`** — Saturated crimson (#c82423) fill with white uppercase Source Sans Pro labels at 15px/700 weight and 0.5px tracking inside a 44px-tall rectangle with {rounded.xs} (4px) corners. Active state deepens to #b2201f; disabled drains to the washed #e89898. This is the universal "Add to Cart" and primary CTA button across the site — high contrast, unambiguous.

**`button-secondary`** — Navy (#003399) fill with identical white uppercase labels and matching {rounded.xs} geometry. Used for "Shop Now" actions in hero modules and category landing pages, providing structural hierarchy beneath the crimson primary without competing with it.

**`button-outline`** — Transparent background with a 2px crimson border and matching crimson label text. Appears on product detail pages for secondary actions — wishlist, compare, or "Learn More" in editorial callout blocks — where a filled button would overpower surrounding content.

### Inputs & Search
**`text-input`** — White surface-card background with a 1px {colors.hairline} border that thickens to a 2px {colors.navy} focus ring — the navy focus state signals the brand's structural color rather than its action color, keeping the two roles semantically separate. Lato body-md at 16px/400. Height fixed at 42px.

**`search-bar`** — A paired input-and-submit unit: the text field sits in white with a hairline border and {rounded.xs} corners, while the submit trigger is a crimson icon-button flush to the right edge. The contrast between the white field and the red button makes the search entry point immediately scannable in the navigation zone.

### Navigation
**`nav-bar`** — #fafafa canvas with a 1px {colors.hairline} bottom rule, 72px tall. Navigation links use Lato at 14px/700 with light letter-spacing; on hover, a crimson underline appears. Logo anchors the left. Right cluster holds a search icon, a cart counter badge with a red pip, and an account icon. The overall register is clean and restrained, letting product photography carry visual weight on category pages.

**`promo-bar`** — A 36px stripe pinned above the nav-bar in {colors.navy} with white Source Sans Pro at 13px/600. Carries free-shipping thresholds, seasonal discount codes, and brand announcements. Swaps to {colors.primary} red for time-sensitive offers, leveraging the same red/navy polarity used across the brand.

### Product Card
**`product-card`** — White card with {rounded.xs} corners and a soft 0 1px 4px shadow at 10% black that lifts to 4px 12px at 16% on hover. Product image fills the top zone in a 4:3 crop with matching corner radius. Below the image: a badge row (sale or new), the product title in Lato title-sm at 16px/700, a price-display unit, and a full-width button-primary. The tight vertical rhythm keeps comparison grids scannable across four columns.

**`sale-badge`** — Crimson pill with white uppercase 11px/700 Source Sans Pro, {rounded.xs} radius, 3px vertical padding. Positioned as an absolute overlay on the product card image, top-left corner. Appears on any item below its original price.

**`new-badge`** — Identical geometry to sale-badge but in navy, distinguishing new arrivals from discounted items. The two badges never co-occur on the same product.

### Hero Banner
**`hero-banner`** — Full-width section in {colors.navy} with a 48px Playfair Display headline in white (display-xl), followed by a Lato body-md subhead at 16px/400. The primary CTA is button-primary (crimson) left-aligned on desktop. The right half carries a lifestyle or product photograph; on mobile the image stacks below the text block. Top/bottom padding is {spacing.section} (64px), horizontal padding {spacing.xl} (32px) expanding at wider viewports.

### Price Display
**`price-display`** — Sale price renders in {colors.primary} crimson using price-lg (22px/700 Lato). The struck original price sits immediately to the right in {colors.muted-light} (#54585b) using price-sm (16px/700) with CSS line-through. The crimson-on-warm-gray contrast draws the eye to the savings delta and reinforces the primary color's role as the brand's signal of value.

### Category Chip
**`category-chip`** — Soft {colors.surface-soft} gray background with {colors.body} text at Source Sans Pro 12px/400. Used as browseable filters for storage type, material, and dimensions in sidebar or horizontal filter rails. Active state swaps to {colors.navy} background with {colors.on-navy} white text — same navy/white contrast as the promo bar.

### Footer
**`footer`** — Near-black {colors.ink} (#121212) background with {colors.surface-soft} body text and {colors.hairline-soft} (#dddada) inactive link color. Section headings use Lato title-sm at 16px/700 in {colors.surface-soft}. Four-column grid on desktop covering Help, Company, Policies, and Social. Bottom bar carries copyright in Lato caption at 12px. No red appears in the footer — the footer is a structural zone, governed by the navy/dark palette.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart; hero headline drops to display-sm (24px Buenard); promo-bar text truncates to single static line; search moves to full-screen overlay |
| Tablet | 744–1128px | Two-column product grid; horizontal nav with icon-only right cluster; hero switches to side-by-side text+image; footer in two-column grid |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with text links visible; hero at full display-xl (48px); footer in four-column grid |
| Wide | > 1440px | Content capped at 1440px max-width with auto margins; product grid extends to five columns on collection pages |

### Touch Targets
- All buttons minimum 44px height, minimum 44px tap width
- Nav icons and hamburger minimum 44×44px including invisible padding
- Product cards are full-surface tap zones on mobile — the entire card links to PDP
- Cart and account header icons padded to 48px tap area on mobile
- Filter chips minimum 36px height with 8px horizontal gap between chips

### Collapsing Strategy
- Primary navigation becomes a side-drawer at < 744px; top-level categories render as accordion sections inside the drawer with {colors.hairline} dividers
- Promo bar condenses from a rotating carousel to a single static message on mobile, with overflow text hidden via ellipsis
- Product card "Add to Cart" button goes full-width below the price on mobile; on the collection grid it collapses to a cart-icon overlay on the card image
- Footer collapses from four columns to two on tablet, and to single-column accordion on mobile
- Search bar transitions from inline header placement to a full-screen overlay triggered by the search icon on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius values were not extractable from the live site; {rounded.xs} (4px) is inferred from the brand's functional, non-decorative aesthetic
- Buenard weight usage on the live site is unclear; 700 is assumed for display contexts as it is the primary weight in the Google Fonts package
- Precise split between Playfair Display and Buenard for hero vs. sub-display roles is inferred from font-stack ordering, not confirmed via DOM inspection
- Box-shadow values for product cards are estimated; actual values were not present in the extraction
- Hover/transition animation durations were not captured
- Icon set style (SVG library, stroke weight, glyph family) could not be determined from color and font extraction alone
- Mobile nav drawer background color is assumed to be {colors.canvas}; not confirmed
- Whether the promo bar cycles multiple messages (carousel) or shows a single static string could not be determined from the extraction
