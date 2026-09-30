---
version: alpha
name: "Exploding Kittens"
source_url: "https://www.explodingkittens.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A game brand that weaponizes the warm, off-white canvas of #fcf8ee against the absolute black of #0f0f0f, creating a visual tension that mirrors the tension of drawing from a deck that might blow up in your face. The brand’s signature voltage comes from a blood-red #840815 that appears in product badges, card backs, and the iconic exploding kitten icon itself — a color so specific it reads as both playful and dangerous. Type runs Epilogue at moderate weights (400–600) for body and Instrument Sans for display headlines, with bebas-neue-pro reserved for explosive sale banners and limited-edition drops. The site uses a near-black #0c0c0c for primary text on the off-white canvas, with #767676 and #4d4d4d as muted stepping stones. Accent colors arrive like wild cards: a marigold #ffd045 for star ratings and “NEW” badges, a sage #aaccaa for expansion-pack headers, and a deep navy #272d45 for footer and legal text. Product cards float on the #fcf8ee canvas with soft shadows and {rounded.md} corners, while CTA buttons sit in full #840815 with white text — no ambiguity about which action detonates the game. The overall feel is a clean, slightly irreverent game shop: high contrast, generous whitespace, and color used as a surprise mechanic rather than decoration.

colors:
  primary: "#840815"
  primary-active: "#6a0611"
  primary-disabled: "#d4a0a5"
  ink: "#0c0c0c"
  body: "#282828"
  muted: "#4d4d4d"
  muted-soft: "#767676"
  hairline: "#e5e5e5"
  hairline-soft: "#f4f4f6"
  canvas: "#fcf8ee"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#ffd045"
  accent-sage: "#aaccaa"
  accent-navy: "#272d45"
  accent-teal: "#0e7a82"
  accent-pink: "#ed2987"
  accent-purple: "#90298d"
  accent-red-bright: "#df1e27"
  star-rating: "#ffd045"
  badge-new: "#ffd045"
  badge-sale: "#df1e27"
  footer-bg: "#272d45"
  footer-text: "#d3d4dd"

typography:
  display-xl:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Instrument Sans', 'Epilogue', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Epilogue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  display-bebas:
    fontFamily: "'bebas-neue-pro', sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 0.9
    letterSpacing: 1px
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
    padding: 14px 28px
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
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-sale:
    backgroundColor: "{colors.accent-red-bright}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-expansion:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.footer-text}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-marigold}"
    typography: "{typography.link}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.base} 0"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  category-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  cart-total:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary action button, rendered in deep blood-red #840815 with white text. Used for “Add to Cart,” “Buy Now,” and primary checkout flows. On hover, darkens to #6a0611 with a subtle scale transform. Disabled state uses a muted pink #d4a0a5 to indicate inactivity. All primary buttons use {rounded.sm} (8px) corners and 14px vertical padding for a substantial feel.

**`button-secondary`** — An outlined variant on the off-white canvas with dark ink text. Uses a 1.5px solid hairline border (#e5e5e5) that darkens to #4d4d4d on hover. Used for “Learn More,” “View Details,” and secondary cart actions. Active state fills with the hairline color.

**`button-accent-marigold`** — A high-energy accent button in #ffd045 with dark ink text. Reserved for limited-time offers, subscription upsells, and “NEW” product launches. The marigold creates strong contrast against the off-white canvas without the danger-signal of the primary red.

**`button-accent-sale`** — A bright red #df1e27 button used exclusively for clearance and sale events. White text, same sizing as primary. Creates urgency without competing with the primary brand red.

**`button-pill`** — A fully rounded variant of the primary button, used for filter tags, category pills, and mobile navigation. Smaller padding (10px 24px) and {rounded.full} corners make it feel like a game token.

### Cards
**`product-card`** — A white card floating on the off-white canvas with a subtle box shadow (0 2px 8px rgba(0,0,0,0.08)). The product image fills the top with {rounded.md} on top corners only. Title sits below in {typography.title-sm} with the price rendered in the brand red. A “NEW” or “SALE” badge overlays the top-left of the image. On hover, the card lifts with a deeper shadow and the CTA button appears.

### Navigation
**`top-nav`** — A fixed 72px bar on the off-white canvas. The Exploding Kittens logo (an exploding kitten icon + wordmark) sits left, with nav links in {typography.nav-link} centered. A search icon and cart icon sit right. On scroll, a thin 1px hairline border appears at the bottom. Mobile collapses to a hamburger menu with a full-screen overlay.

**`nav-link`** — Inline text links with 8px horizontal padding. Active state uses the brand red #840815. Hover adds a subtle underline animation.

### Badges
**`badge-new`** — A marigold #ffd045 pill with dark text, used to flag new products and expansions. Compact at 4px 8px padding with {rounded.xs} corners and uppercase 11px bold type.

**`badge-sale`** — A bright red #df1e27 pill with white text, used for clearance items. Same sizing as the new badge but with urgency color.

**`badge-expansion`** — A sage #aaccaa pill with dark text, used to denote expansion packs and add-ons. The sage green signals “additional content” without competing with the primary red.

### Forms
**`search-bar`** — A fully rounded input field on white background with a 1px hairline border. 48px height with 12px 20px padding. On focus, the border shifts to the brand red and a subtle ring appears. Placeholder text in {colors.muted-soft}.

**`quantity-selector`** — A compact 40px control with minus/plus buttons flanking a numeric display. Used in cart and product detail pages. The buttons have {rounded.sm} corners and the active state uses the brand red.

### Footer
**`footer`** — A deep navy #272d45 band at the bottom of every page. Links render in a muted gray-blue #d3d4dd and shift to marigold #ffd045 on hover. The footer contains site map links, social icons, and legal text. A thin 1px hairline in #676986 separates sections.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, hero banner reduces to 32px font, search bar collapses to icon-only |
| Tablet | 744–1128px | Two-column product grid, expanded nav links, hero banner at 36px, search bar full-width in nav |
| Desktop | 1128–1440px | Three-column product grid, full nav, hero banner at 48px, search bar in nav with icon |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero banner centered with larger margins |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links minimum 40px tap area
- Quantity selector buttons minimum 36px tap area
- Product card CTA buttons minimum 44px height
- Search icon minimum 44px tap area
- Cart icon minimum 44px tap area

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product grid collapses from 4 columns to 1 column on mobile
- Footer link columns collapse to single column below 744px
- Hero banner text reduces font size progressively
- Search bar becomes icon-only on mobile, expanding to full input on tap
- Category strip becomes horizontally scrollable on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from common patterns rather than extracted from the live site
- Error styling for form inputs (validation colors, error messages) could not be reliably extracted
- Dark mode is not present on the live site; all colors are light-mode only
- The extracted font list includes several Shopify widget fonts (oke-widget-icons) and fallbacks that may not be brand-specific
- The extracted hex list includes many colors that are likely from third-party widgets (Klarna, Afterpay, social icons) rather than the brand palette — the primary brand colors (#840815, #fcf8ee, #0f0f0f, #ffd045, #aaccaa, #272d45) were identified by frequency and distinctiveness
- Sub-brand palettes for specific game expansions (e.g., Zombie Kittens, Imploding Kittens) could not be extracted
- Animation durations, easing curves, and transition properties were not extracted
- Shadow values (box-shadow, drop-shadow) were not reliably extractable from the live site
- The bebas-neue-pro font family appears in limited contexts (likely sale banners and hero text) but exact usage rules are inferred
- Sainte-Colombe font appears in the extracted list but its usage context is unclear — may be used for decorative or limited-edition content
