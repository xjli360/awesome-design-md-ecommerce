---
version: alpha
name: "CurrentBody"
source_url: "https://www.currentbody.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clinical-warm aesthetic built on a foundation of #f4f4f6 canvas and #00bbff — a vivid cyan that functions as the brand's singular voltage, appearing on primary CTAs, shipping badges, and category icons. The palette is dominated by a tight range of cool grays (#e5e5e5, #9ca3af, #d1d5db) that create a clean, medical-adjacent precision, punctuated by #be3a43 (a muted crimson used for sale badges and error states) and #83cc1c (a sharp lime green for "in stock" indicators and sustainability callouts). Typography runs ABCDiatype at moderate weights — display headlines sit at 24–32px in weight 500, trusting generous whitespace and the cyan accent over heavy bold. Product cards use softly rounded corners (`{rounded.md}` ~12px) with a white surface (`{colors.surface-card}`) and a thin #e5e7eb hairline, while the primary CTA button takes a full-height cyan rectangle at `{rounded.sm}`. The brand's voice is informative and reassuring — large hero sections pair a single product image with a headline and a cyan "Shop Now" button, and the persistent top bar ("Free Delivery Over £100") uses #00bbff text on a #222222 ink background, creating a high-contrast utility strip that reads as both offer and authority. The overall mood is that of a premium electronics showroom translated into a clean, high-DPI interface — cool gray, cyan, and white, with color used sparingly to direct attention.

colors:
  primary: "#00bbff"
  primary-active: "#0099d6"
  primary-disabled: "#b3eaff"
  ink: "#222222"
  body: "#505050"
  muted: "#9ca3af"
  muted-soft: "#c8c9c8"
  hairline: "#e5e7eb"
  hairline-soft: "#f4f4f6"
  canvas: "#f4f4f6"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-crimson: "#be3a43"
  accent-lime: "#83cc1c"
  accent-lime-soft: "#cdeba4"
  accent-navy: "#272d45"
  accent-navy-soft: "#2c3e50"
  star-rating: "#ffbdbd"
  sale-badge: "#be3a43"
  shipping-bar-bg: "#222222"
  shipping-bar-text: "#00bbff"

typography:
  display-xl:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'ABCDiatype', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
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
    rounded: "{rounded.sm}"
    padding: 14px 24px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: 1px solid "{colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 1px solid "{colors.muted}"
  button-accent-crimson:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.accent-crimson}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: 1px solid "{colors.hairline-soft}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  shipping-bar:
    backgroundColor: "{colors.shipping-bar-bg}"
    textColor: "{colors.shipping-bar-text}"
    typography: "{typography.caption}"
    height: 40px
    padding: 8px 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    border: 1px solid "{colors.hairline}"
  product-card-hover:
    boxShadow: 0 4px 12px rgba(0,0,0,0.08)
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: 1/1
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    color: "{colors.accent-crimson}"
  product-card-original-price:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    textDecoration: line-through
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-in-stock:
    backgroundColor: "{colors.accent-lime-soft}"
    textColor: "{colors.accent-lime}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 1px solid "{colors.primary}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    border-top: 1px solid "{colors.hairline}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
    padding: 4px 0
  footer-heading:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginBottom: "{spacing.lg}"
  category-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: 24px
    border: 1px solid "{colors.hairline}"
  category-card-hover:
    border: 1px solid "{colors.primary}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 1px solid "{colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: 16px
  accordion-content:
    padding: 0 16px 16px 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a solid cyan rectangle with white text. On hover, it shifts to `{colors.primary-active}` (#0099d6). The disabled state uses `{colors.primary-disabled}` (#b3eaff) with white text, signaling non-interactivity without removing the brand color entirely.

**`button-secondary`** — A white button with a thin `{colors.hairline}` border, used for secondary actions like "Learn More" or "View Details". On hover, the background shifts to `{colors.surface-soft}` and the border to `{colors.muted}`. Text remains `{colors.ink}`.

**`button-accent-crimson`** — A compact crimson button reserved for sale-related CTAs and clearance sections. Uses `{colors.accent-crimson}` (#be3a43) as background with white text, and `{typography.button-sm}` for a tighter fit.

### Cards
**`product-card`** — A white card with a thin `{colors.hairline}` border and `{rounded.md}` corners. Contains a square product image with `{rounded.sm}`, a title in `{typography.title-sm}`, and pricing information. On hover, a subtle box-shadow elevates the card. Sale prices are rendered in `{colors.accent-crimson}` with the original price struck through in `{colors.muted}`.

**`category-card`** — A larger card used for category navigation (e.g., "LED Masks", "Hair Devices"). On hover, the border shifts to `{colors.primary}`, creating a cyan outline that signals interactivity.

### Navigation
**`nav-bar`** — A fixed 72px white bar with a bottom hairline. Navigation links use `{typography.nav-link}` in `{colors.ink}`, with the active state highlighted in `{colors.primary}`. The bar includes a logo, category dropdowns, and a search icon.

**`shipping-bar`** — A persistent 40px utility strip at the very top of the page, using `{colors.shipping-bar-bg}` (#222222) with cyan text (`{colors.shipping-bar-text}`). Displays "Free Delivery Over £100" and other promotional messaging.

### Forms
**`text-input`** — A standard input field with a white background, `{rounded.sm}`, and a `{colors.hairline}` border. On focus, the border shifts to `{colors.primary}`. Error states use `{colors.accent-crimson}` for the border.

**`search-bar`** — A pill-shaped search input with `{rounded.full}`, used in the header and on search pages. On focus, the border shifts to `{colors.primary}`.

### Badges
**`badge-sale`** — A compact crimson badge with uppercase text, used to flag discounted products. Positioned at the top-left of product card images.

**`badge-in-stock`** — A lime green badge on a soft lime background, indicating product availability. Uses `{colors.accent-lime}` (#83cc1c) for text and `{colors.accent-lime-soft}` (#cdeba4) for background.

**`badge-new`** — A cyan badge used to highlight newly added products. Uses `{colors.primary}` as background with white text.

### Footer
**`footer`** — A full-width section on `{colors.canvas}` with a top hairline. Contains columns of links in `{colors.muted}`, with column headings in `{colors.ink}` using `{typography.title-sm}`. Links use `{typography.link}` and have 4px vertical padding for touch targets.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 col), nav collapses to hamburger, shipping bar text truncates, hero padding reduces to 32px, category cards stack vertically |
| Tablet | 744–1128px | Two-column product grid (2 col), nav shows top-level links, hero uses 48px padding, category cards in 2x2 grid |
| Desktop | 1128–1440px | Three-column product grid (3 col), full nav with dropdowns, hero uses 64px padding, category cards in 3x3 grid |
| Wide | > 1440px | Four-column product grid (4 col), max-width container at 1440px, hero content centered with max-width 1200px |

### Touch Targets
- All buttons and interactive elements maintain minimum 44x44px touch target
- Nav links have 48px minimum height for tap targets
- Product card CTAs ("Shop Now", "Add to Cart") are full-width on mobile for easy tapping
- Search bar has 48px height on all breakpoints
- Footer links have 44px minimum tap area (4px padding + 36px line height)

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Product filters collapse into a slide-out drawer on mobile
- Product description sections (details, reviews, FAQs) collapse into accordions on mobile and tablet
- Footer columns collapse to a single column on mobile, with accordion-style expandable sections
- Hero content stacks vertically on mobile (image above text) instead of side-by-side

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site CSS — the values above (e.g., `button-primary-active`, `product-card-hover`) are inferred from common patterns and should be verified against the actual design tokens.
- Error and validation styling for forms (error messages, success states, helper text) was not observed in the extracted data.
- Dark mode or high-contrast mode tokens are not present in the extracted palette — the brand may not support these yet.
- The `#ffbdbd` color (listed as `star-rating`) may be a stock-image dominant tone rather than an actual design token — its usage should be confirmed.
- Sub-brand or category-specific color variations (e.g., "LED Masks" vs "Hair Removal" sections) were not observed.
- The extracted font list includes `Open Sans` and `Noto Sans` as fallbacks, but `ABCDiatype` appears to be the primary brand font — the exact weight variants (Regular, Medium, Bold) and their specific usage rules are inferred.
- Animation and transition durations/easings were not extracted — the brand likely uses standard 200-300ms ease transitions for hover states.
- The `#acaba3` and `#b2b2b4` colors in the extracted list may be checkout-widget or social-icon colors rather than brand tokens — they are not included in the palette above.
- Shopify-specific UI elements (cart drawer, checkout button, payment icons) follow Shopify's default styling and are not part of the brand design system.
