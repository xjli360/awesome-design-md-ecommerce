---
version: alpha
name: "Boulies"
source_url: "https://www.boulies.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep teal #108474 anchors Boulies, a brand that sells ergonomic seating and standing desks, as a signal of stability and focus rather than the neon aggression typical of gaming hardware. The palette is unusually restrained for the category: a near-black ink (#141414) for headlines, a warm charcoal body (#555555), and a soft off-white canvas (#f9fafb) that keeps product photography — glossy leather, matte mesh, aluminum legs — as the primary visual texture. The single accent voltage comes from a marigold yellow (#fbcd0a) used sparingly on sale badges, price highlights, and secondary CTAs, while a muted sage (#edf5f5) appears in background sections and feature callouts, lending a calm, almost editorial tone. Buttons carry a 4px radius ({rounded.xs}) rather than the pill shape common in ecommerce, and the top navigation sits at a compact 60px height with a thin 1px hairline (#dedede) separating it from the hero. The brand trusts its product silhouette over decorative flourishes — there are no hero illustrations, no gradient overlays, no decorative icons. Type runs Nunito Sans at moderate weights (400 body, 600–700 headings) with generous line spacing (1.5–1.6) that makes spec sheets and ergonomic descriptions feel readable rather than dense. The checkout flow uses Shopify's default widget colors (#c9161d for error states, #336ca8 for links), which clash slightly with the brand's cool teal — a pragmatic concession to platform constraints. Overall, Boulies reads as a furniture company that happens to serve gamers, not a gaming company that happens to sell chairs.

colors:
  primary: "#108474"
  primary-active: "#0d6b5d"
  primary-disabled: "#a3d4c9"
  ink: "#141414"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#8c8c8c"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f9fafb"
  surface-soft: "#edf5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fbcd0a"
  accent-yellow-active: "#e1b630"
  accent-red: "#c9161d"
  accent-blue: "#336ca8"
  badge-sale: "#fbcd0a"
  badge-new: "#108474"
  star-rating: "#fbcd0a"
  scrim: "#141414"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0
  body-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-lg:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-yellow-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 4px 0
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  top-nav-logo:
    height: 28px
  top-nav-cart-icon:
    width: 20px
    height: 20px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.base}"
  product-card-sale-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-new-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  feature-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} {spacing.base}"
  spec-table-row:
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-heading:
    textColor: "{colors.canvas}"
    typography: "{typography.title-md}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "10px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "10px 16px"
    height: 40px
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.body}"
    width: 36px
    height: 40px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
  accordion-content:
    typography: "{typography.body-md}"
    padding: "{spacing.md} 0"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  pagination-disabled:
    textColor: "{colors.muted-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the brand teal #108474 on a white background. State changes are subtle: active darkens to #0d6b5d, disabled fades to a muted sage #a3d4c9. The 4px radius ({rounded.xs}) is intentionally modest — no pill shapes, no gradients. Used for "Add to Cart", "Buy Now", and primary checkout flows. Height is 44px with 12px/24px padding.

**`button-secondary`** — An outlined variant with a white background and a 1px hairline border (#dedede). On active state, the border swaps to the primary teal and the background shifts to the soft sage surface (#edf5f5). Used for "Learn More", "Compare", and secondary product page actions.

**`button-accent-yellow`** — The marigold #fbcd0a variant reserved for sale promotions, limited-time offers, and "Shop Sale" CTAs. Text remains dark (#141414) for contrast. Active state darkens to #e1b630. Used sparingly — typically one per page.

**`button-text-link`** — A text-only button that mimics the link style but with 4px vertical padding for touch targets. Color is the primary teal, no background, no border. Used for "View Details", "Read Reviews", and inline navigation.

### Cards
**`product-card`** — A clean white card with an 8px radius ({rounded.sm}) and zero padding at the container level — spacing is handled by child elements. The image fills the top with a top-only radius (8px top, 0px bottom) and a 1:1 aspect ratio. Title uses title-md (18px, 600 weight), price uses body-md (15px, 400 weight). Badges are positioned absolutely over the image: sale badges use the yellow accent, new badges use the teal primary. No shadow — the card relies on content contrast against the off-white canvas.

**`feature-callout`** — A soft sage (#edf5f5) background panel with 8px radius and 24px padding. Used for ergonomic feature highlights, warranty information, and "Why Choose Boulies" sections. Text is body color (#555555) at 15px with 1.6 line height for readability.

### Navigation
**`top-nav`** — A compact 60px bar on a white background with a 1px bottom hairline (#dedede). Logo is 28px tall. Nav links use Nunito Sans 600 weight at 14px with 0.3px letter spacing. Cart icon is 20px square. No mega-menu — the brand uses a simple dropdown pattern for desktop. On mobile, the nav collapses to a hamburger with a full-screen overlay menu.

**`breadcrumb`** — Small caption text (12px) in muted gray (#7b7b7b). The active (current page) item switches to ink (#141414). No background, no border — just text with "/" separators.

### Forms
**`search-bar`** — A 40px tall input with 4px radius, white background, and 1px hairline border. On focus, the border swaps to the primary teal. Placeholder text uses body color (#555555). No icon inside the input — the search icon sits to the left as a separate element.

**`newsletter-input`** — Matches the search bar dimensions but sits inside the dark footer (#141414 background). The input itself remains white with a hairline border. The submit button is a 40px tall primary teal button using button-sm typography.

**`quantity-selector`** — A 40px tall horizontal control with a 1px hairline border and 4px radius. Contains a minus button (36px wide), the quantity value in body-md, and a plus button. Buttons are transparent with body-colored text.

### Footer
**`footer`** — A dark section (#141414) with 48px vertical padding and 32px horizontal padding. Headings are white in title-md, body text and links are muted-soft (#8c8c8c) in body-sm. Links hover to white. The newsletter signup sits in a prominent position, typically the first column. Social icons (not defined here) would use white at 20px.

### Product Detail
**`spec-table`** — A bordered table (1px hairline) with 8px radius. The header row uses the soft sage background (#edf5f5) with ink text in title-md. Body rows alternate with a subtle hairline-soft (#e9e9e9) bottom border. No zebra striping — the brand relies on the border alone for row separation.

**`accordion`** — Used for product descriptions, shipping info, and warranty details. Each item has a 1px bottom hairline border and 12px vertical padding. The header uses title-md (18px, 600 weight), and the expanded content uses body-md (15px, 400 weight) with 12px padding below. No icons — the accordion uses a simple "+" / "−" toggle.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), top-nav collapses to hamburger, hero padding reduces to 32px, spec tables stack vertically, accordions default open |
| Tablet | 744–1128px | Two-column product grid (2 cards), top-nav shows limited links (Shop, Sale, Support), hero uses 48px padding, spec tables remain horizontal but font scales down |
| Desktop | 1128–1440px | Three-column product grid (3 cards), full top-nav with all links visible, hero uses 64px padding, spec tables at full width |
| Wide | > 1440px | Max-width container at 1440px, product grid stays 3 columns but cards have more whitespace, hero content centered with max-width 1200px |

### Touch Targets
- All buttons and clickable elements minimum 44px height (WCAG 2.1 compliant)
- Quantity selector buttons are 36px wide × 40px tall — slightly under the 44px recommendation but acceptable for a non-primary control
- Top-nav links have 44px touch height via padding
- Mobile hamburger icon is 44px × 44px
- Accordion headers have 44px minimum touch height
- Pagination items are 32px × 32px with 4px padding — active state adds background

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px — all links move to a full-screen overlay with 60px top bar
- Product grid collapses from 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile)
- Spec tables collapse to stacked label-value pairs on mobile — each row becomes a two-line block
- Footer columns collapse from 4 columns (desktop) → 2 columns (tablet) → 1 column (mobile) with accordion-style expandable sections
- Hero section reduces padding and centers content on mobile — CTA button becomes full-width
- Breadcrumbs truncate on mobile — only show current page and one parent level
- Star ratings remain inline but reduce from 16px to 14px on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were not reliably extractable from the live site CSS — the values above (button-primary-active, button-secondary-active) are inferred from common patterns, not confirmed
- Error state styling for form inputs (red border, error message typography) could not be extracted — the #c9161d red is present in the palette but its usage context is uncertain
- Dark mode is not supported by the brand — no dark theme CSS was found
- Sub-brand or collection-specific palettes (e.g., "Master Series" vs "EP Series" chairs) may exist but were not detectable from the extracted data
- The exact font stack for Nunito Sans weights could not be confirmed — the site may use variable font or specific weight files
- Modal/dialog styling (cart drawer, quick view, size guide) was not extractable
- Loading states and skeleton screens were not present in the extracted CSS
- The checkout flow uses Shopify's default styling — brand-specific overrides may exist but were not detected
- Animation durations and easing curves were not extractable from the static CSS
- The mobile navigation overlay (hamburger menu) styling details (background opacity, transition, close button) could not be confirmed
- Product variant selector styling (swatches, dropdowns) was not reliably extractable
- The extracted color list contains many near-duplicate grays (#f5f5f5, #f6f6f6, #f9f9f9, #fafafa) — these likely represent different surfaces but their exact mapping is uncertain
- The #a89cc8 purple and #c1e6e6 light teal appear in the extracted colors but their usage context is unknown — possibly social icons or stock photography
