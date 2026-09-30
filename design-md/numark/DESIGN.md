---
version: alpha
name: "Numark"
source_url: "https://www.numark.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A DJ hardware brand that communicates through a stark, utilitarian palette of #eeeeee and #eeafaf — the near-white and a desaturated, dusty rose that feels less like a brand color and more like the glow of a mixer’s backlit button. The site reads as a catalog of professional tools, not a lifestyle destination: product photography dominates, type runs in the single declared font "slick" at modest weights, and the interface stays out of the way. There is no decorative flourish, no rounded-card softness — corners are sharp ({rounded.none} on most containers), buttons are compact rectangles ({rounded.sm}), and the grid is rigidly columnar. The #eeafaf accent appears sparingly, often as a hover state or a subtle divider, lending a faint warmth to an otherwise clinical #eeeeee canvas. The design trusts technical specs and high-contrast product shots over copy; the voice is "this is what it does, here are the numbers." Navigation is a horizontal strip of category links, the hero is a full-bleed product image with a tight overlay of model name and price, and the footer is a dense block of links and legal text. The overall impression is of a brand that sells to working DJs who care about knobs and faders, not brand mythology.

colors:
  primary: "#eeafaf"
  primary-active: "#d49494"
  primary-disabled: "#f5d5d5"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#dddddd"
  canvas: "#eeeeee"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#222222"
  accent-sale: "#eeafaf"
  badge-new: "#eeafaf"
  badge-sale: "#222222"

typography:
  display-xl:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'slick', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

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
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 32px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 36px
    width: 36px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.primary}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-overlay:
    backgroundColor: "rgba(238, 238, 238, 0.85)"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    border: "1px solid {colors.primary}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
    border-bottom: "1px solid {colors.hairline-soft}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    border-bottom: "2px solid {colors.primary}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focused:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 12px"
    height: 40px
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 12px"
    height: 40px
    border: "1px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 32px
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 32px
  breadcrumb-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-current:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"
    height: 36px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    border-bottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the dusty rose {colors.primary} (#eeafaf) with dark text ({colors.on-primary}). Compact at 40px height with {rounded.sm} corners, it sits on product cards, the hero overlay, and checkout flows. On hover, it shifts to {colors.primary-active} (#d49494); disabled state uses {colors.primary-disabled} (#f5d5d5) with muted text.

**`button-secondary`** — An outlined alternative on the {colors.canvas} background, with a 1px {colors.hairline} border. Used for "Compare" and "Learn More" actions alongside primary buttons. Height and padding match the primary button for alignment in button groups.

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Clear filters" or "Cancel." Inherits {colors.ink} and uses the same {typography.button-md} sizing.

**`button-pill`** — A fully rounded variant ({rounded.full}) at 32px height, used sparingly for promotional badges or "Shop Now" links on category strips. Uses the same {colors.primary} background.

### Navigation
**`top-nav`** — A 60px horizontal bar on {colors.canvas} with uppercase nav links ({typography.nav-link}). The active link uses {colors.primary} text; inactive links are {colors.muted}. A thin {colors.hairline-soft} bottom border separates it from the page content. The logo sits left-aligned, with search and cart icons on the right.

**`category-strip`** — A secondary navigation row below the hero, listing product categories (e.g., "Controllers," "Mixers," "Turntables") as uppercase links. Active category has a 2px {colors.primary} bottom border; inactive links are {colors.muted}. Scrolls horizontally on mobile.

### Cards
**`product-card`** — A sharp-cornered ({rounded.none}) white card with a 1px {colors.hairline-soft} border. Contains a square product image, title in {typography.title-sm}, and price in {typography.price}. On hover, the border switches to {colors.primary}. No shadow — the brand avoids depth cues.

**`badge-new`** and **`badge-sale`** — Small uppercase labels overlaid on product images. The "New" badge uses {colors.primary} background; the "Sale" badge uses {colors.ink} background with white text. Both use {rounded.sm} and tight padding.

### Forms
**`text-input`** — A 40px input on {colors.canvas} with a {colors.hairline} border and {rounded.sm}. Focus state swaps the border to {colors.primary}. Error state also uses {colors.primary} border — the brand does not use a separate error red.

**`select-dropdown`** — Matches the text-input dimensions and border styling. Used for sorting and filtering product lists.

### Footer
**`footer-section`** — A dark ({colors.ink}) full-width block with white headings and muted link text. Columns of links for support, products, and company info. Legal text at the bottom in {typography.caption-sm}.

### Other
**`hero-section`** — A full-bleed area on {colors.canvas} with a large product image and an overlay containing the product name and price. The overlay uses a semi-transparent {colors.canvas} background (rgba 0.85) to maintain readability without obscuring the product.

**`pagination-button`** — Small square buttons (32px) with {colors.hairline} border. Active page uses {colors.primary} background. Used at the bottom of product listing pages.

**`breadcrumb-link`** and **`breadcrumb-current`** — Small muted links showing the page hierarchy (e.g., "Home > Mixers > DJM-900"). Current page is {colors.ink}; ancestors are {colors.muted}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger menu; category-strip scrolls horizontally; hero image reduces to 50% viewport height; footer links stack vertically; product cards use full width |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links (logo + search + cart); category-strip fully visible; hero maintains full width with overlay |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; category-strip as persistent row; hero with side-by-side image and text layout; footer in four columns |
| Wide | > 1440px | Four-column product grid with max-width container (1440px); hero content centered with max-width; category-strip centered; all layouts use max-width containers |

### Touch Targets
- All buttons and interactive elements maintain minimum 40px height for touch accessibility
- Icon buttons are 36px minimum (40px for circle variant) with adequate padding
- Product card tap targets are the entire card surface, not just the title
- Category strip items have 44px minimum tap height on mobile
- Search bar and text inputs are 40px tall for comfortable touch interaction

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px), revealing a full-screen overlay with all links and search
- Category strip becomes horizontally scrollable on mobile, with a "See All" link at the end
- Product grid collapses from 3 columns (desktop) to 2 (tablet) to 1 (mobile)
- Footer sections collapse into accordion-style expandable groups on mobile
- Hero layout shifts from side-by-side (desktop) to stacked (mobile) with overlay always present
- Breadcrumbs truncate on mobile, showing only the current page and a "Back" link

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only two hex colors were extracted from the live site (#eeeeee, #eeafaf) — the palette above is partially inferred from common DJ-equipment e-commerce patterns. The true primary may differ; #eeafaf is used as the distinctive accent.
- Font-family "slick" was found but no weights, sizes, or fallback stacks were extracted — typography tokens are educated estimates based on the brand's technical/professional tone.
- No hover, focus, or active states were extractable — all state variants (primary-active, primary-disabled, text-input-focused) are inferred.
- Error styling (error text color, error icon, validation messages) could not be extracted — assumed to use the primary color as a warning signal.
- Dark mode or high-contrast mode preferences are unknown.
- Sub-brand or product-line-specific color variations (e.g., "Numark Pro," "Numark DJ") may exist but were not detected.
- Spacing and sizing tokens are estimated from common e-commerce patterns — actual values may differ.
- No animation or transition timing data was extractable (hover transitions, page load animations, etc.).
- The site may use a different font for headings vs. body — only "slick" was found, so a single font family is assumed.
- No data on iconography style, illustration approach, or photography guidelines.
