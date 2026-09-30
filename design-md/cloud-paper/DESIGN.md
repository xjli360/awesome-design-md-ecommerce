---
version: alpha
name: "Cloud Paper"
source_url: "https://cloudpaper.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A marigold #ffbd59 voltage cuts across a deep-indigo #232145 canvas — the brand's signature move is to let a single warm accent carry all interactive energy against a dark, almost nocturnal frame. Cloud Paper sells bamboo paper products (toilet paper, paper towels, tissues) through a Shopify storefront that reads more like a mission-driven publication than a CPG commodity site. The palette is deliberately restrained: a soft mint #ace6ce and its deeper sibling #86dbb8 appear in eco-badges and sustainability callouts, while #f7ebdb and #f9eddd warm up product photography backgrounds and testimonial cards. The brand avoids hard corners — buttons and cards use {rounded.sm} to {rounded.md} radii, and the primary CTA sits in that signature #ffbd59 with white text, creating a visual that says "approachable, not aggressive." Typography relies on Gilroy-medium for most body and heading text, with a clean sans-serif stack underneath. The overall mood is one of calm conviction: the indigo background on the top nav and footer creates a sense of depth and seriousness, while the marigold buttons and mint accents keep the experience from feeling heavy. Cloud Paper's design system is built around trust signals — plastic-free badges, tree-saving counters, and subscription toggle pills — all rendered in that same restrained palette so nothing competes for attention except the product itself.

colors:
  primary: "#ffbd59"
  primary-active: "#e5a33d"
  primary-disabled: "#ffe0a8"
  ink: "#232145"
  body: "#3a3a5c"
  muted: "#7a7a9a"
  muted-soft: "#a0a0ba"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f7ebdb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-ink: "#ffffff"
  accent-mint: "#ace6ce"
  accent-mint-strong: "#86dbb8"
  accent-warm: "#f9eddd"
  star-rating: "#ffbd59"
  scrim: "#232145"

typography:
  display-xl:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gilroy-medium', 'Inter', -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    padding: 11px 23px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-ink:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-item:
    backgroundColor: transparent
    textColor: "{colors.on-ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-item-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "4px 4px"
  subscription-toggle-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "4px 16px"
  subscription-toggle-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "4px 16px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  eco-badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  eco-badge-strong:
    backgroundColor: "{colors.accent-mint-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  testimonial-card:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 24px
    width: 24px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    width: 360px
  cart-item:
    padding: "{spacing.base} 0"
    border-bottom: "1px solid {colors.hairline-soft}"
  cart-total:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "14px 24px"
    height: 52px
    width: "100%"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in marigold #ffbd59 with white text. Used for "Add to Cart", "Subscribe & Save", and primary checkout flows. On hover, shifts to a slightly deeper gold #e5a33d. Disabled state uses a pale peach #ffe0a8 to maintain visual hierarchy without confusion. The 8px radius keeps the button friendly without being pill-shaped — a deliberate choice to distinguish primary actions from subscription toggles which use full pills.

**`button-secondary`** — A white button with indigo #232145 text, used for "Learn More" links, secondary product actions, and cancel flows. The outline variant adds a 2px indigo border for situations where the button needs more presence against a busy background. Ghost variant has no border or background, used in tight spaces like cart item controls.

**`button-pill-primary`** and **`button-pill-ink`** — Pill-shaped buttons reserved for subscription frequency toggles (monthly vs. one-time) and filter chips. The pill shape signals a toggle or selection state rather than a primary action. Primary pill uses marigold for the active state; ink pill uses the deep indigo for dark-background scenarios.

### Cards
**`product-card`** — A white card with 12px radius containing product imagery, title, price, and optional eco-badges. The image area uses 8px radius to create a subtle nested-corner effect. Cards sit on a white canvas with generous spacing between them — the brand trusts whitespace over borders to define product boundaries. The badge component uses mint #ace6ce for "Plastic-Free" or "Bamboo" tags, creating a visual shorthand for the brand's sustainability promise.

**`testimonial-card`** — A warm-toned card using #f9eddd background, used for customer reviews and social proof. The warm beige creates a visual break from the white product grid and signals a different content type — opinion rather than product. Text remains in the standard body color #3a3a5c.

### Navigation
**`nav-bar`** — A full-width indigo #232145 bar at 72px height. Navigation links are white with 8px horizontal padding. The active state (current page) uses marigold text to echo the primary button color. The nav bar is the brand's most consistent dark-surface element, creating a strong top anchor. On mobile, the nav collapses into a hamburger menu with a slide-out drawer maintaining the same indigo background.

### Forms
**`text-input`** — White input fields with a light gray #dedede border and 8px radius. On focus, the border thickens to 2px and shifts to marigold #ffbd59 — a subtle but clear focus indicator that doesn't rely on outline rings. Height is 48px for comfortable touch targeting. Used in email signup forms, address collection, and search.

**`subscription-toggle`** — A pill-shaped toggle group for choosing between one-time purchase and subscription. The active option fills with marigold; inactive options remain transparent with body-colored text. The entire toggle sits on a warm #f7ebdb background, creating a contained selection area that visually separates from surrounding content.

### Badges
**`eco-badge`** and **`eco-badge-strong`** — Small uppercase tags using mint green backgrounds. The standard variant uses #ace6ce for general eco-claims; the strong variant uses #86dbb8 for more emphatic statements like "100% Plastic-Free" or "Carbon Neutral Shipping". Both use indigo text for readability and brand consistency.

### Cart & Checkout
**`cart-drawer`** — A 360px slide-in drawer from the right side of the screen. White background with items separated by soft hairline #e8e8e8 borders. The checkout button spans full width and uses the primary button pattern. The quantity selector uses a bordered container with small square buttons for increment/decrement — a compact pattern that saves space in the cart layout.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero section reduces padding to 32px vertical; subscription toggle stacks vertically; cart drawer goes full-width |
| Tablet | 744–1128px | Nav remains expanded but with reduced link padding; product cards in 2-column grid; hero uses 48px vertical padding; subscription toggle remains horizontal |
| Desktop | 1128–1440px | Full nav with all links visible; product cards in 3-column grid; hero uses 64px vertical padding; maximum content width of 1128px centered |
| Wide | > 1440px | Content remains centered at 1128px max-width; additional whitespace on sides; product cards can stretch to 4-column if inventory warrants |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links have 44px minimum tap area (padding + height)
- Quantity selector buttons are 40px × 40px minimum
- Subscription toggle pills are 44px minimum height
- Cart drawer close button is 44px × 44px

### Collapsing Strategy
- Top nav links collapse into hamburger menu below 744px
- Product grid collapses from 3 columns to 2 at tablet, 1 at mobile
- Hero section reduces vertical padding by 50% on mobile
- Subscription toggle switches from horizontal to vertical layout below 480px
- Cart drawer shifts from overlay to full-width bottom sheet on mobile
- Footer link columns collapse to single column below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font-family list only included "Gilroy-medium" and "swiper-icons" — Gilroy is likely used for headings and body, but weight variants (light, regular, semibold, bold) could not be confirmed. The system assumes 500-weight for most text based on the "medium" designation, but actual weight usage may vary.
- Hover states for secondary buttons, text inputs, and nav links could not be extracted — the active/disabled states for primary buttons are inferred from common patterns, not verified from the live site.
- Error styling for form validation (border colors, error message typography, iconography) was not visible in the extraction.
- Dark mode is not present on the live site — the indigo nav and white canvas suggest no dark mode implementation exists.
- The extracted hex list included #007aff (likely a Shopify checkout or Apple Pay button color) and #121212 (near-black, possibly a text color or overlay) — these were not used in the primary palette as they appear to be third-party widget defaults.
- Sub-brand or promotional-specific colors (seasonal campaigns, limited editions) could not be identified.
- Animation and transition timing values (hover fade durations, drawer slide speeds, loading states) were not extractable from static CSS analysis.
- Iconography style and sizing conventions (SVG vs. icon font, stroke weights, icon grid) could not be determined beyond the presence of "swiper-icons" for carousel navigation.
