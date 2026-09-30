---
version: alpha
name: "Finalmouse"
source_url: "https://finalmouse.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A stark, almost brutalist hardware brand that uses #121212 as its gravitational center — not the warm charcoal of lifestyle tech but a dead-black void that makes every product photograph feel like a museum specimen under glass. The #fafafa canvas provides the only relief, a clinical white that never warms into cream, while #dedede hairline strokes trace the edges of product cards and navigation bars with the precision of a CNC router. EB Garamond appears unexpectedly in display contexts, a serif anachronism that signals Finalmouse's self-conscious positioning as "art objects that happen to be mice" — the type sits at generous sizes (28–36px) with tight letter-spacing, creating a typographic tension against the otherwise monochrome, hyper-minimal layout. Buttons use {rounded.sm} corners, never pills, and the primary CTA is a thin-outlined rectangle in #121212 on white — no filled color, no gradient, no shadow. The brand refuses the gamer-aesthetic clichés of RGB strips and angular vents; instead, product cards float on {spacing.base} margins with only a product name, a price, and a single "Sold Out" or "Buy" badge in {rounded.xs} capsules. The overall effect is less "gaming peripheral store" and more "limited-edition sneaker drop" — scarcity is the design system's invisible eleventh color.

colors:
  primary: "#121212"
  primary-active: "#000000"
  primary-disabled: "#888888"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#fafafa"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-sold-out: "#121212"
  badge-new: "#121212"
  badge-sale: "#121212"
  star-rating: "#121212"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'EB Garamond', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'EB Garamond', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'EB Garamond', 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.ink}"
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-primary-disabled:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted-soft}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 8px 0
  badge-sold-out:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.base}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
    border: "1px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    padding: "{spacing.xs} 0"
  footer-link-hover:
    textColor: "{colors.ink}"
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action is a thin-outlined rectangle in #121212 on a transparent background, using uppercase sans-serif at 14px weight 600. On hover, the button fills solid black and text inverts to white — a simple, decisive state change with no animation or transition. The disabled state uses #999999 for both border and text, maintaining the same outline structure. This button appears on product detail pages for "Add to Cart" and on collection pages for "Notify Me" when items are sold out.

**`button-secondary`** — A solid black rectangle with white text, used for "Buy Now" on product pages and "View All" on collection headers. The hover state deepens to pure #000000. This button shares the same dimensions and typography as `button-primary` but fills the background, creating visual hierarchy through density rather than color.

**`button-tertiary-text`** — A text-only link styled as a button, used for "Learn More" and "Read the Story" links beneath hero sections. No border, no background — just uppercase sans-serif in #121212 with 8px vertical padding. This is the lightest CTA weight in the system.

### Badges
**`badge-sold-out`**, **`badge-new`**, **`badge-sale`** — All three badge variants share identical styling: a solid black capsule with 10px uppercase bold type in white, using {rounded.xs} corners (4px). Despite different semantic meanings, Finalmouse refuses color-coded badges — everything is monochrome. The badge sits in the top-left corner of product card images with {spacing.sm} offset from the edge. Sold-out items also overlay a semi-transparent scrim on the product image.

### Cards
**`product-card`** — A border-only card (1px #dedede) with no background fill, letting the white page canvas show through. The card has zero border-radius — Finalmouse uses hard corners for product imagery, reinforcing the museum-print aesthetic. On hover, the border shifts to #121212. The card contains a square aspect-ratio image, a product title in 14px weight 600, and a price in 16px weight 400. No ratings, no reviews, no color swatches — just the object and its name.

**`hero-section`** — A full-width white section with EB Garamond display type at 36px, used for launch announcements and collection headers. The hero contains a single headline, optional body copy in 16px sans-serif, and a `button-tertiary-text` link. No background images, no carousels, no video — the hero is typographic, relying on the brand's distinctive serif to create impact.

### Navigation
**`top-nav`** — A 64px white bar with a 1px #dedede bottom border. Navigation links are 13px uppercase sans-serif weight 600 with 0.5px letter-spacing. The active state is underlined with a 2px solid black bar. The nav contains the brand logo (typically set in EB Garamond or a custom wordmark), a "Shop" dropdown, "Support", and a cart icon. No search bar in the top nav — search is relegated to a dedicated page or footer.

**`nav-link`** — Individual navigation items with 8px vertical and 16px horizontal padding. The active state uses a 2px bottom border in #121212. Hover state is text color only — no background change.

### Forms
**`text-input`** — A 44px tall input with 1px #dedede border and {rounded.sm} corners. On focus, the border switches to #121212. Background is white, text is 14px #333333. Placeholder text uses #999999. No label styling is defined — Finalmouse typically uses floating labels or top-aligned labels in 12px uppercase.

**`search-bar`** — Identical to `text-input` in structure but used specifically on the search results page. The search bar includes a magnifying glass icon in #666666 on the left side, with 16px padding before the text input begins.

### Footer
**`footer`** — A white section with 1px #dedede top border, containing links in 14px #666666 that hover to #121212. The footer is divided into columns for "Products", "Support", "About", and "Legal". Social media icons appear as outlined squares (40x40px) with 1px #dedede borders, hovering to #121212 borders with a #f0f0f0 background fill. No newsletter signup, no decorative elements — just links and icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu. Product cards stack in single column. Hero type reduces to 28px. Footer columns stack vertically. Badges remain in top-left but scale to 8px type. |
| Tablet | 744–1128px | Top nav shows limited links (Shop, Support, Cart). Product cards display in 2-column grid. Hero type at 32px. Footer in 2-column layout. |
| Desktop | 1128–1440px | Full top nav with all links. Product cards in 3-column grid. Hero type at 36px. Footer in 4-column layout. |
| Wide | > 1440px | Max-width container at 1440px with auto margins. Product cards in 4-column grid. Hero type remains 36px but with increased line length. |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Icon buttons are 40x40px with 44px touch area via padding
- Product card tap targets include the entire card area, not just text
- Navigation links have 48px minimum touch height on mobile

### Collapsing Strategy
- Top navigation collapses to hamburger icon below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport shrinks
- Footer columns collapse from 4 → 2 → 1
- Hero section reduces padding from 64px to 32px on mobile
- Product card badges reduce font size from 10px to 8px on mobile
- Search bar moves from dedicated page to a slide-down panel on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors (#dedede, #fafafa, #121212) represent a monochrome palette — no accent color was detected. The brand may use a limited accent (e.g., a specific red for "Sold Out" or a blue for links) that wasn't captured in the extraction. If an accent exists, it's likely a single high-saturation color used sparingly.
- Font-family extraction returned Arial, EB Garamond, and Helvetica — EB Garamond is assumed for display roles, but exact weights and sizes for display typography are inferred from common usage patterns rather than extracted CSS.
- No hover states, focus states, or active states were extractable from the static HTML/CSS analysis. All interactive states in this document are inferred from the brand's visual language.
- No error styling, form validation states, or disabled input styling could be extracted.
- No dark mode or high-contrast mode variants were detected.
- The brand may use custom iconography (mouse silhouettes, product illustrations) that couldn't be analyzed.
- Animation and transition timing values (durations, easing curves) are not available.
- Shopify checkout styling (Shopify Pay button, cart drawer) uses platform defaults and may not reflect the brand's design system.
- The brand's "Sold Out" overlay pattern (semi-transparent scrim on product images) is inferred from common e-commerce patterns rather than extracted CSS.
- No sub-brand or collection-specific color variants were detected (e.g., limited edition mouse colors).
