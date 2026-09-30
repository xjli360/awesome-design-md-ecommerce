---
version: alpha
name: "Retro Games UK"
source_url: "https://www.retrogames.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A khaki-and-cream palette — #98937d as the dominant ground, #d6c9b9 as the warm secondary — that reads like a faded 1980s game manual left in a cardboard box in a loft for thirty years. The site’s visual language is built on a low-contrast, almost sepia-toned canvas where #d7caba and #bea98e layer like old cartridge labels, and the only real voltage comes from #cd783f, a burnt-orange accent that punches through the muted field on price tags, add-to-cart buttons, and sale badges. Typography defaults to system sans-serif (Arial, Helvetica) with Times New Roman reserved for product descriptions and historical copy, creating a deliberate tension between the utilitarian nav and the nostalgic body text. Borders are thin and soft — #aaaaaa hairline dividers, #888888 secondary strokes — and cards carry a gentle {rounded.sm} radius that never competes with the product photography. The overall effect is that of a well-organized charity shop: orderly, slightly dusty, and utterly sincere.

colors:
  primary: "#cd783f"
  primary-active: "#b5662f"
  primary-disabled: "#e0b08a"
  ink: "#444444"
  body: "#636051"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#aaaaaa"
  hairline-soft: "#d7caba"
  canvas: "#d6c9b9"
  surface-soft: "#d7caba"
  surface-card: "#e8ddd0"
  on-primary: "#ffffff"
  accent-sale: "#cd783f"
  accent-stock: "#4d4b3f"
  badge-new: "#98937d"
  badge-rare: "#cd783f"
  star-rating: "#cd783f"
  footer-bg: "#4d4b3f"
  footer-text: "#cdcee3"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Times New Roman, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Times New Roman, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: 1px solid "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
  product-card-hover:
    boxShadow: "0 2px 8px rgba(0,0,0,0.1)"
  product-card-image:
    rounded: "{rounded.xs}"
  product-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
  product-price-sale:
    typography: "{typography.title-sm}"
    textColor: "{colors.accent-sale}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-rare:
    backgroundColor: "{colors.badge-rare}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.caption}"
    padding: 32px 16px
  footer-link:
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 48px 16px
  category-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: 1px solid "{colors.hairline}"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    border: 1px solid "{colors.hairline}"
    height: 32px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in burnt-orange #cd783f on white text. Used for "Add to Cart", "Buy Now", and primary checkout flows. On hover, darkens to #b5662f; disabled state fades to a muted peach #e0b08a. All primary buttons carry a gentle {rounded.sm} radius and 10px vertical padding for a compact, confident footprint.
**`button-secondary`** — A card-toned alternative (#e8ddd0) with dark ink text, used for "View Details", "Wishlist", and secondary actions. Shares the same dimensions and radius as primary but relies on the surface-card background for visual separation. No border — the contrast against the khaki canvas is sufficient.
**`button-tertiary-text`** — A text-only button in the primary orange, used for "Clear filters", "See all", and inline actions. No background, no border — just the accent color and bold Arial type.

### Cards
**`product-card`** — The core inventory unit: a warm cream surface (#e8ddd0) with {rounded.sm} corners and 12px internal padding. Product images sit in a {rounded.xs} frame above title, platform badge, and price. On hover, a subtle box-shadow lifts the card from the page — the only shadow in the system. Price is always rendered in the accent orange, while sale prices double down with an additional "SALE" badge.
**`product-card-image`** — Square-ratio product photography with a slight {rounded.xs} radius, framed by the card background. No border — the image bleeds naturally into the card's warm tone.

### Navigation
**`nav-bar`** — A 56px fixed-height bar in the khaki canvas (#d6c9b9), carrying category links in bold Arial. Active links gain a 2px bottom border in the accent orange; inactive links sit in muted gray. The bar collapses to a hamburger menu below 744px.
**`nav-link-active`** — Bold ink text with a 2px orange underline, signaling the current section.
**`nav-link-inactive`** — Muted gray (#888888) text with no underline, reverting to ink on hover.

### Forms
**`text-input`** — A cream card-toned input field with a 1px hairline border (#aaaaaa) and {rounded.xs} corners. On focus, the border thickens to 2px and turns orange — the only focus indicator in the system. Internal padding is 8px vertical, 12px horizontal for comfortable text entry.
**`search-bar`** — A pill-shaped input ({rounded.full}) in the same cream card tone, with a 1px hairline border. Used for site-wide product search. The rounded ends echo the soft, approachable feel of the brand.

### Badges
**`badge-new`** — A small khaki (#98937d) uppercase label with white text, indicating newly listed inventory. {rounded.xs} corners and 2px vertical padding keep it unobtrusive.
**`badge-rare`** — An orange (#cd783f) variant of the badge, reserved for rare or collectible items. Same dimensions and typography as the new badge, but with higher visual urgency.
**`badge-sale`** — Identical to rare in color and form, used for discounted items. The orange consistently signals "special attention required."

### Footer
**`footer`** — A dark khaki (#4d4b3f) footer with light blue-gray (#cdcee3) text, providing a clear visual boundary from the warm canvas above. Links are underlined on hover. The footer contains site map, social links, and legal text in 13px Arial caption type.

### Hero
**`hero-section`** — A full-width banner in the khaki canvas, using 28px bold Arial for headline text. Content is centered with generous vertical padding (48px). No background image — the brand trusts the warm canvas and product photography to carry the visual weight.

### Category Chips
**`category-chip`** — Pill-shaped filter chips in cream card tone with a hairline border. Active chips invert to orange background with white text. Used for platform filters (NES, SNES, Mega Drive, etc.) and condition filters (Boxed, Loose, Manual).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack single-column; hero padding reduces to 32px; search bar moves below nav; category chips wrap to two rows |
| Tablet | 744–1128px | Nav links visible but condensed; product cards in 2-column grid; hero at 40px padding; category chips in a horizontal scrollable strip |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-column grid; hero at 48px padding; category chips in a full-width row |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; additional whitespace on sides; hero text scales to 32px |

### Touch Targets
- All buttons and links: minimum 40px height
- Category chips: minimum 32px height
- Search bar: 40px height
- Nav links: 44px tap area (padding added on mobile)
- Quantity selector: 32px height, 32px width per button

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Category chip strip becomes horizontally scrollable below 744px
- Product grid reduces from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer links stack vertically on mobile
- Hero text reduces from 28px to 22px on mobile
- Search bar moves from inline nav position to below nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be extracted; only primary button and product card hover are confirmed
- Error states for form inputs (validation, required fields) are unknown
- Dark mode or high-contrast mode is not present on the live site
- The extracted color list is heavily weighted toward warm neutrals; the brand may have additional accent colors for seasonal or promotional use that were not visible during extraction
- Font sizes and line heights are inferred from common web patterns and the brand's general aesthetic; exact values may vary
- The system font stack (Arial, Helvetica, Times New Roman) may be supplemented with web fonts on certain pages not captured in the extraction
- Spacing values are estimated based on visual proportions; the brand may use a different scale
- The brand's logo and iconography style could not be extracted
- Checkout flow styling (payment forms, confirmation pages) is not represented in the extracted data
