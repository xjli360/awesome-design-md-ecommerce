---
version: alpha
name: "Matador"
source_url: "https://matadorup.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A brand built on the tension between deep wilderness and clean minimalism, Matador uses a primary green (#108474) that reads as alpine lake water rather than corporate emerald — it appears on CTAs, badges, and the signature Packable Hip Pack logo, always on a near-white canvas (#fafafa, #f9fafb). The palette is overwhelmingly neutral: six distinct grays from #eeeeee down to #4d4d4d create a quiet hierarchy where product photography does the heavy lifting. A single accent, marigold (#fbcd0a), appears only on sale badges and limited-edition markers, never competing with the green. Type runs Montserrat at moderate weights — display headlines sit at 600 weight, body at 400, with no heavy 700+ anywhere except the logo lockup. The brand avoids hard corners: buttons use {rounded.sm} (8px), product cards use {rounded.md} (12px), and the signature flat-pack pouches are photographed with soft shadows that echo the {rounded.lg} (20px) on hero modules. There is no hero video, no autoplay — just still photography of gear against granite, snow, and sandstone, with the green acting as the only synthetic color in frame.

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#a3d4c9"
  ink: "#1a1a1a"
  body: "#555555"
  muted: "#808080"
  muted-soft: "#b3b3b3"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#fbcd0a"
  accent-sale-text: "#1a1a1a"
  badge-new: "#c2ad7b"
  star-rating: "#1a1a1a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.accent-sale-text}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 32px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-info:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.accent-sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-module:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-heading:
    typography: "{typography.caption}"
    color: "{colors.canvas}"
    textTransform: uppercase
    letterSpacing: "0.5px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    typography: "{typography.caption}"
    color: "{colors.ink}"
  review-stars:
    color: "{colors.star-rating}"
    size: 16px
  review-count:
    typography: "{typography.caption-sm}"
    color: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with alpine green (#108474) and white uppercase Montserrat at 14px/600. Hover shifts to a deeper forest green (#0d6b5c). Disabled state uses a muted sage (#a3d4c9). All primary buttons use 8px corner radius and 44px height — tall enough for gloved fingers, short enough to sit comfortably in a product card.

**`button-secondary`** — Outlined variant on a white canvas with a thin hairline border (#dedede). Hover thickens the border to muted gray (#808080). Used for "Learn More" and "Add to Wishlist" — never for primary purchase actions. Same 44px height and uppercase treatment as primary.

**`button-tertiary-text`** — Text-only link styled as a button, using the primary green as the text color. No background, no border. Used in navigation dropdowns and accordion footers. Hover underlines.

**`button-sale`** — A compact, high-contrast badge-button using marigold (#fbcd0a) with black text. Only appears on sale items and limited drops. Shorter at 32px height, smaller uppercase type at 12px/600.

### Cards
**`product-card`** — A white card with 12px rounded corners and no shadow — the brand relies on the product photography to create depth. The image occupies the top with its own top-rounded corners, followed by a padded info section containing the title (14px/600) and price (14px/400). Badges sit as small overlays on the image, using either primary green for "NEW" or marigold for "SALE".

**`hero-module`** — A large content block with 20px rounded corners on a soft gray background (#f5f5f5). Contains a 36px display headline and 16px body copy. Used for collection headers and brand storytelling sections. No gradient, no overlay — just type and whitespace.

### Navigation
**`top-nav`** — A 64px white bar with a thin bottom border (#e9e9e9). Navigation links are uppercase 13px/600 in muted gray, with the active page indicated by a 2px green underline. The logo sits left, cart and search icons right. On mobile, the nav collapses into a hamburger with a full-screen drawer.

**`nav-link-active`** — Uppercase 13px/600 with a 2px solid green bottom border. The active state is the only place the brand uses a colored underline — no bold weight change, no background fill.

**`breadcrumb`** — Small 13px/500 gray links separated by slashes. The current page is rendered in black. Used on product detail and collection pages to provide orientation without visual weight.

### Forms
**`search-bar`** — A 40px input with soft gray background (#f5f5f5) and thin hairline border. On focus, the border swaps to primary green and the background returns to white. Type is 14px/400 in body gray. No search button — the icon sits inside the input as a prefix.

**`quantity-selector`** — A compact 40px input with minus/plus buttons flanking a centered number. White background, hairline border, 8px corners. Used on product detail pages for cart quantity adjustment.

### Footer
**`footer`** — A dark section (#1a1a1a) with white text. Column headings are uppercase 13px/500 with 0.5px letter spacing. Links are 14px/400 in light gray (#b3b3b3). The footer contains four columns: Shop, Support, About, and Social. Bottom bar includes copyright and legal links in smaller type.

### Accents
**`review-stars`** — Black star icons at 16px, rendered inline with the review count in muted gray. No colored stars — the brand avoids decorative color in functional UI elements.

**`accordion-header`** — A 16px/600 title with a thin bottom border, clickable to expand content below. Used on product detail pages for description, specs, and shipping info. No chevron animation — just a plus/minus toggle.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid, hamburger nav, product cards stack full-width, hero module reduces padding to 24px, footer collapses to single column |
| Tablet | 744–1128px | Two-column product grid, top nav condenses (some links hidden behind "More" dropdown), hero module uses 48px padding |
| Desktop | 1128–1440px | Three-column product grid, full top nav visible, hero module at 64px padding, max-width container at 1128px |
| Wide | > 1440px | Max-width container pinned at 1128px with auto margins, product grid remains three-column, hero module background extends edge-to-edge |

### Touch Targets
- All buttons and interactive elements minimum 44px height (exceeds Apple HIG 44pt recommendation)
- Icon buttons are 40x40px with 44px tap area via transparent padding
- Product card tap targets (title, price, image) are the full card area
- Accordion headers have 44px minimum tap height
- Quantity selector buttons are 40x40px

### Collapsing Strategy
- Top nav links beyond "Shop", "Explore", "About" collapse into a "More" dropdown at tablet
- Full top nav collapses to hamburger icon at mobile breakpoint
- Footer four-column layout collapses to two columns at tablet, single column at mobile
- Product grid reduces from three columns to two at tablet, one at mobile
- Hero module side-by-side layout (image + text) stacks vertically at tablet and below
- Accordion content collapses by default on all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex list is heavily weighted toward grays and near-whites (15+ neutral tones) — the true brand palette likely has fewer gray steps. The primary green (#108474) and marigold (#fbcd0a) are the only distinctive colors; no secondary palette (e.g., deep blue, rust, or tan) was detected.
- Font-family declarations included "Baskerville" and "Barlow" in addition to Montserrat and Nunito Sans — these may be used for editorial content or legacy pages. Only Montserrat and Nunito Sans appeared consistently. Baskerville may be a serif option for long-form product descriptions.
- No hover states for secondary buttons, text links, or icon buttons could be reliably extracted — the above uses reasonable defaults (border darkening, underline).
- No error state styling (form validation, out-of-stock messaging) was found in the extracted data.
- No dark mode or high-contrast mode tokens exist in the extracted palette.
- The "JudgemeIcons" and "JudgemeStar" font declarations indicate a third-party review widget (Judge.me) — its styling may not match the brand's native design language.
- No animation or transition timing values (ease, duration) were extractable from static CSS.
- No sub-brand or collection-specific color variations were detected (e.g., "Ultralight" vs "Freerun" lines may have distinct accents).
- Shopify checkout widget colors (Afterpay, Klarna, PayPal) were filtered from the extracted list but may still appear on product pages — these are not brand colors.
