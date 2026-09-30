---
version: alpha
name: "Mee-go"
source_url: "https://mee-go.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, confident blue (#003399) anchors Mee-go as the single brand voltage across a site that sells pushchairs, car seats, and nursery furniture — a category where trust and safety are the real products. That primary blue, paired with a secondary #003388, appears on every primary CTA, navigation bar, and product badge, creating a consistent visual anchor that reads as dependable without feeling cold. The palette is unusually large for a DTC brand — the extracted list runs to 27+ colors — but the core is disciplined: a warm off-white canvas (#e3ddd8) softens what could be a sterile blue-and-white scheme, while accents like #cd2653 (a muted crimson) and #f0b849 (a warm gold) appear on sale badges and promotional ribbons. Typography leans on Montserrat for headings and Open Sans for body copy, both at moderate weights (400–600) that avoid the heavy-handedness of traditional parenting brands. Product cards use soft corners ({rounded.md} ~12px) and generous whitespace, with the primary blue reserved for the "Add to Cart" button and the checkout flow. The site's voice is straightforward and reassuring — no whimsy, no pastels — treating the purchase of a car seat or cot with the seriousness it deserves while the warm beige canvas keeps the experience from feeling clinical.

colors:
  primary: "#003399"
  primary-active: "#003388"
  primary-disabled: "#b3c6e6"
  ink: "#111111"
  body: "#2f2f2f"
  muted: "#43454b"
  muted-soft: "#abb8c3"
  hairline: "#d5d6d7"
  hairline-soft: "#e3ddd8"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#cd2653"
  accent-warning: "#f0b849"
  accent-success: "#4ab866"
  accent-error: "#cc1818"
  badge-new: "#007cba"
  badge-sold-out: "#32373c"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Montserrat', 'Open Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 12px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-active:
    textColor: "{colors.on-primary}"
    borderBottom: "2px solid {colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-sale}"
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sold-out:
    backgroundColor: "{colors.badge-sold-out}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  category-tile-active:
    border: "2px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Basket," "Buy Now," and checkout progression. Rendered in the brand's deep blue (#003399) with white text, a subtle 6px corner radius, and 48px height for comfortable tap targets. On hover, shifts to the darker active state (#003388). When disabled, fades to a pale blue (#b3c6e6) with reduced opacity.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Save for Later." Uses a white background with a 2px blue border and blue text. Maintains the same 48px height and 6px radius as the primary button for visual consistency.

**`button-tertiary`** — A text-only button for inline actions like "Clear filters" or "Cancel." No background or border, only the primary blue text. Used sparingly to avoid visual noise.

**`button-sale`** — A compact, high-visibility button for sale items and promotional banners. Uses the muted crimson (#cd2653) background with white text and a smaller 13px font. Appears on product cards and in the sale navigation section.

### Cards
**`product-card`** — The core product display unit, a white card with 12px rounded corners and 16px padding. Contains a product image with 6px rounded corners, the product name in 16px medium weight, and pricing in the primary blue. Sale prices render in the accent crimson. Cards sit on a soft gray (#f2f2f2) background in grid layouts with 24px gaps.

**`category-tile`** — Used for navigation through product categories (Pushchairs, Car Seats, Nursery Furniture). A white card with 12px rounded corners and 24px padding, displaying a category image and title. The active state adds a 2px blue border.

### Navigation
**`nav-bar`** — The primary navigation bar, fixed at 64px height with the brand's deep blue background. Contains the logo, category links in white 14px medium weight, and a search icon. Links underline on hover with a 2px white bottom border.

**`nav-link`** — Navigation links use 14px Montserrat at 500 weight with 0.2px letter spacing. White text on the blue nav bar, with active state indicated by a white underline.

### Forms
**`text-input`** — Standard form input for search, checkout fields, and newsletter signup. White background with a 1px light gray border (#d5d6d7), 6px rounded corners, and 16px body text. On focus, the border thickens to 2px and turns the primary blue.

**`search-bar`** — A pill-shaped search input (9999px radius) for the header search. White background with a light gray border, 40px height, and 16px padding. Used for quick product searches.

### Badges
**`badge-sale`** — A small uppercase label for sale items. Crimson background (#cd2653) with white text, 4px rounded corners, and tight 2px/8px padding. Appears as an overlay on product card images.

**`badge-new`** — A blue (#007cba) badge for new arrivals. Same dimensions and typography as the sale badge but in a distinct blue to avoid confusion.

**`badge-sold-out`** — A dark gray (#32373c) badge for out-of-stock items. Uses the same badge pattern but with reduced opacity on the product card to signal unavailability.

### Footer
**`footer`** — A dark footer (#111111) with light gray text (#abb8c3) in 14px body size. Contains link columns for customer service, product categories, and company information. Links are 14px with standard hover underlines. The footer spans the full viewport width with 64px top and bottom padding.

### Hero
**`hero-banner`** — The homepage hero section, a full-width banner on a soft gray (#f2f2f2) background. Uses the 36px display font for headlines with a primary blue CTA button. Padding is generous at 64px vertical and 32px horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, reduced hero padding (32px), stacked footer columns |
| Tablet | 744–1128px | Two-column product grid, expanded nav links, 48px hero padding |
| Desktop | 1128–1440px | Three-column product grid, full nav bar, 64px hero padding |
| Wide | > 1440px | Max-width container at 1440px, centered content, four-column product grid |

### Touch Targets
- All buttons and interactive elements maintain minimum 48px height for touch accessibility
- Product cards have 16px minimum tap targets for "Add to Basket" and "Quick View"
- Navigation links have 44px minimum touch area
- Search bar is 40px tall with 16px padding for easy tapping

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer link columns stack vertically on mobile, with accordion-style expand/collapse for each section
- Hero banner reduces padding and font size on mobile (display-xl drops to 24px)
- Search bar collapses to an icon on mobile, expanding to full-width on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list includes many colors that appear to be framework defaults (WordPress theme colors, WooCommerce widget colors) — the true brand palette is likely smaller than the 27+ colors extracted. The primary blue (#003399) and warm beige (#e3ddd8) are confirmed brand colors; others may be inherited from the theme.
- Hover states for buttons and links beyond the primary-active color are inferred, not extracted from live CSS.
- Error states for form inputs (validation, error messages) are not available from the extraction.
- Typography weights and sizes are estimated based on common patterns for the font families found; exact values may differ on the live site.
- Dark mode is not supported and no dark mode colors were extracted.
- The extracted font list includes many fallback fonts and system fonts — the primary brand fonts are likely Montserrat (headings) and Open Sans (body), but exact usage ratios are inferred.
- No animation or transition timing data was extracted.
- The site may use a custom Shopify or WooCommerce theme; component spacing and padding may vary by page template.
