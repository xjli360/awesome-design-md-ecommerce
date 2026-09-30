---
version: alpha
name: "Realforce"
source_url: "https://www.realforce.co.jp/en"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A monochrome precision instrument for the keyboard obsessive, built around a single extracted hex — #313131, a deep charcoal that reads as machined aluminum rather than generic gray. Every surface on realforce.co.jp/en carries this same near-black weight: the product photography backgrounds, the spec-table borders, the footer band, the keycap legends on their flagship electrostatic capacitive boards. There is no brand color in the conventional sense — no accent hue, no gradient, no warm tone — only the cold, exacting neutrality of industrial design rendered in digital form. Typography runs the system stack at its most utilitarian: -apple-system and Helvetica Neue at 400 weight, never decorative, never expressive. Headlines sit at 22–28px with generous line height (1.6–1.8), letting the product images do the selling while the type recedes into documentation. Buttons are hard-cornered rectangles ({rounded.none}) with 1px hairline borders, not pills — this is a brand that sells to engineers and typists who value actuation force over visual charm. The nav bar is a thin 48px strip of {colors.ink} text on {colors.canvas}, no logo lockup, no dropdowns, just a sparse row of links that says: we assume you know what you're looking for. Product cards use {rounded.sm} (4px) — the only concession to softness — and stack spec data in a monochrome table that reads like a datasheet. The entire experience is an anti-Airbnb: where Airbnb uses {rounded.full} and {colors.primary} to say "come in, stay a while," Realforce uses {rounded.none} and {colors.ink} to say "this is a tool. Use it."

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#8c8c8c"
  ink: "#1a1a1a"
  body: "#313131"
  muted: "#6a6a6a"
  muted-soft: "#8c8c8c"
  hairline: "#d4d4d4"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  link: "#0066cc"
  link-hover: "#004499"
  error: "#cc0000"
  success: "#2e7d32"
  badge-new: "#313131"
  badge-sale: "#cc0000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'Segoe UI', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
  button-text-hover:
    backgroundColor: transparent
    textColor: "{colors.link-hover}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 12px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-spec:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 2px 8px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    fontWeight: 600
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  spec-table-row-alt:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-image:
    rounded: "{rounded.none}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-current:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 12px 16px
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 16px

## Components

### Buttons
**`button-primary`** — A hard-cornered rectangle in {colors.primary} (#313131) with white text, used for primary actions like "Add to Cart" and "Buy Now." On hover, the background shifts to {colors.primary-active} (#1a1a1a) for a subtle darkening effect. The disabled state uses {colors.muted-soft} (#8c8c8c) with white text, signaling the action is unavailable without visual noise. No border, no shadow, no animation — the button is a flat, functional slab.
**`button-secondary`** — An outlined variant with a 1px {colors.hairline} border on {colors.canvas} background and {colors.ink} text. Active state fills the background with {colors.surface-soft} (#f5f5f5). Used for "Learn More" and "View Details" actions where the primary button would be too heavy. Padding is 11px 23px to account for the border offset, keeping the total height at 44px.
**`button-text`** — A text-only link styled as a button, using {colors.link} (#0066cc) with no background or border. Hover state shifts to {colors.link-hover} (#004499). Used for "Read More" links in spec sections and "View All" in category strips.

### Cards
**`product-card`** — A white card with {rounded.sm} (4px) corners and a 1px {colors.hairline-soft} border. The product image sits at the top with matching {rounded.sm} corners. Below, the title uses {typography.title-md} in {colors.ink}, the price uses {typography.body-md} in {colors.body}, and optional spec lines use {typography.caption} in {colors.muted}. No shadow, no elevation — the card is a flat container for structured product data.
**`product-card` (hover)** — On hover, the border shifts from {colors.hairline-soft} to {colors.hairline} for a subtle visual cue. No scale, no lift, no shadow — the interaction is minimal and functional.

### Navigation
**`nav-bar`** — A 48px high strip of white background with {colors.ink} text. Links use {typography.nav-link} (14px, 500 weight, uppercase with 0.3px letter spacing). The active link uses {colors.primary} (#313131) text color. No logo lockup, no dropdown indicators, no search bar in the top nav — the bar is a sparse, utilitarian row of links. On mobile, the nav collapses to a hamburger menu with a full-screen overlay.
**`nav-link`** — Each link has 12px 16px padding and no background. Active state uses {colors.primary} text. No underline, no border-bottom, no pill background — the only indicator of the current page is the text color change.

### Forms
**`text-input`** — A hard-cornered rectangle with a 1px {colors.hairline} border on {colors.canvas} background. Text uses {typography.body-md} (15px) in {colors.ink}. Focus state shifts the border to {colors.primary} (#313131). Error state uses a 1px {colors.error} (#cc0000) border. Placeholder text uses {colors.muted-soft} (#8c8c8c). No rounded corners, no shadow, no icon padding — the input is a bare rectangle.
**`select-input`** — Matches the text-input styling with a 1px {colors.hairline} border and {rounded.none}. The dropdown arrow is a simple SVG chevron in {colors.muted}. On focus, the border shifts to {colors.primary}.

### Tables
**`spec-table`** — A borderless table with alternating row backgrounds: {colors.canvas} for even rows and {colors.surface-soft} (#f5f5f5) for odd rows. Headers use {typography.caption} (13px) at 600 weight with a {colors.surface-soft} background. Cells use {typography.body-sm} (14px) in {colors.body}. No vertical borders, no horizontal rules — the alternating background is the only structural cue.

### Footer
**`footer`** — A full-width band in {colors.primary} (#313131) with white text. Links use {typography.caption} (13px) in {colors.on-primary}. The footer is divided into columns with no visible separators — just stacked text links with 8px vertical spacing. Copyright text sits at the bottom in {colors.muted-soft} (#8c8c8c) on the dark background.

### Badges
**`badge`** — A small, hard-cornered rectangle in {colors.badge-new} (#313131) with white uppercase text at 11px / 600 weight. Used for "NEW" labels on product cards. Padding is 2px 8px. No rounded corners, no shadow — the badge is a flat, functional label.
**`badge-sale`** — Same shape and typography as the standard badge, but uses {colors.badge-sale} (#cc0000) background for sale or clearance items.

### Hero
**`hero-section`** — A full-width section with {colors.canvas} background and {colors.ink} text. The headline uses {typography.display-xl} (28px, 400 weight, 1.6 line height). Below, a subheadline uses {typography.body-md} (15px) in {colors.body}. The hero image is a full-bleed, hard-cornered product shot with no overlay or gradient. No CTA button in the hero — the brand trusts the product image to pull the user in.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu. Product cards stack in single column. Hero image scales to full width with reduced padding. Spec tables become stacked label-value pairs. Footer columns stack vertically. |
| Tablet | 744–1128px | Nav bar shows all links with reduced padding. Product cards display in 2-column grid. Hero section uses 50/50 split for image and text. Spec tables remain in table format with horizontal scroll. |
| Desktop | 1128–1440px | Full nav bar with standard padding. Product cards in 3-column grid. Hero section uses 60/40 split with larger image. Spec tables display in full width. Footer columns display in 4-column layout. |
| Wide | > 1440px | Max-width container at 1440px with centered content. Product cards in 4-column grid. Hero section max-width at 1200px. All other layouts remain at desktop scale. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Nav links have 48px touch targets (12px padding on 24px text height).
- Product card images are tappable with no minimum size requirement — the card itself is the touch target.
- Badges are not interactive and have no minimum touch target.

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px. The hamburger icon is a simple three-line SVG in {colors.ink} with no background or border.
- Product card grids collapse from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Spec tables collapse to stacked label-value pairs below 744px. Each row becomes a block with the label in {typography.caption} (600 weight) and the value in {typography.body-sm}.
- Footer columns collapse from 4 columns (desktop) to 2 columns (tablet) to a single stack (mobile).
- Hero section collapses from side-by-side layout (desktop) to stacked layout (mobile) with the image above the text.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color was extracted from the live site (#313131). All other colors in the palette are inferred from common web patterns (white canvas, gray borders, standard link blue) and may not match the actual brand implementation.
- No font-family declarations beyond the system stack were found. The brand may use a custom typeface (e.g., Noto Sans JP for Japanese text) that was not captured in the extraction.
- Hover and active states for buttons and links are inferred from common patterns, not extracted from the live site.
- Error and success states for forms are based on standard web conventions, not the brand's actual implementation.
- The badge system (colors, typography, usage) is inferred from common e-commerce patterns, not extracted.
- No dark mode or high-contrast mode data was extracted.
- No animation or transition timing data was extracted (hover transitions, page transitions, loading states).
- The nav bar height (48px) and structure are inferred from common patterns; the actual site may use different dimensions or include additional elements (search, cart icon, language selector).
- No data for mobile-specific interactions (swipe gestures, pull-to-refresh, bottom sheets).
- The brand's Japanese-language site (realforce.co.jp) may use different typography and spacing than the English site.
- No extracted data for the checkout flow, cart drawer, or mini-cart component.
- The product card hover state (border color change) is inferred; the actual site may use a different interaction (shadow, scale, overlay).
