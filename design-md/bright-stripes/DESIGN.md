---
version: alpha
name: "Bright Stripes"
source_url: "https://brightstripes.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A confetti-burst of a brand, where #fe3bae — a hot pink that reads like a highlighter dipped in bubblegum — is the primary voltage, flashing across buttons, badges, and the theme-color meta tag. The palette is a carnival of accents: #5bc6ce (a minty teal), #fcd94c (marigold yellow), #d96bff (violet), and #f5634c (coral red), all set against a warm off-white canvas of #fafefb and #f8efe6. Typography layers two distinct personalities: the hand-drawn, retro-sign-painter feel of MotelCalifornia-Regular for display headlines, and the clean, rounded sans-serif of Quicksand for body and buttons. The brand’s signature design move is the pill-shaped CTA — a `{rounded.full}` button in primary pink that says “Shop Now” or “Get Inspired” — and the liberal use of `{rounded.lg}` on product cards and image frames, creating a soft, approachable, almost edible quality. Every surface feels like a craft table: `{colors.surface-card}` is a warm cream (#fffaf6), `{colors.surface-soft}` is a barely-there blush (#fdf6ed), and `{colors.hairline}` is a gentle #dedede that never feels harsh. The nav bar is a clean white strip with a centered logo and a search icon, while the footer is a dense, organized grid of links in `{colors.muted}` (#6a6a6a). The brand trusts color and rounded geometry over heavy typography; there is no hard corner anywhere, and the overall mood is one of joyful, accessible creativity — a digital craft box that invites you to open it.

colors:
  primary: "#fe3bae"
  primary-active: "#ed3293"
  primary-disabled: "#ffb3d9"
  ink: "#444444"
  body: "#565a5b"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#dedede"
  hairline-soft: "#f7f7f7"
  canvas: "#fafefb"
  surface-soft: "#fdf6ed"
  surface-card: "#fffaf6"
  on-primary: "#ffffff"
  accent-teal: "#5bc6ce"
  accent-yellow: "#fcd94c"
  accent-violet: "#d96bff"
  accent-coral: "#f5634c"
  accent-green: "#01ad63"
  accent-orange: "#fd692a"
  accent-gold: "#f7d945"
  star-rating: "#fcd94c"
  sale-badge: "#f5634c"
  new-badge: "#5bc6ce"

typography:
  display-xl:
    fontFamily: "'MotelCalifornia-Regular', 'Tenor Sans', 'Quicksand', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'MotelCalifornia-Regular', 'Tenor Sans', 'Quicksand', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'MotelCalifornia-Regular', 'Tenor Sans', 'Quicksand', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  link:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Quicksand', 'Tenor Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px

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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 16px
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-coral}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  nav-bar-sticky:
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    fontWeight: 700
  badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: "2px 8px"
  badge-category:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginTop: "{spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.canvas}"
    typography: "{typography.link}"
    textDecoration: none
  footer-link-hover:
    color: "{colors.primary}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.base} 0"
  category-tab:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button in the brand's signature hot pink (#fe3bae). Uses `{typography.button-md}` (Quicksand 16px, weight 600) in white. On hover, it deepens to `{colors.primary-active}` (#ed3293). The disabled state fades to `{colors.primary-disabled}` (#ffb3d9). This button drives all major actions: "Shop Now", "Add to Cart", "Subscribe".

**`button-secondary`** — An outlined variant with a white fill and a 2px solid border in `{colors.primary}`. Text is the same hot pink. On hover, the background shifts to `{colors.surface-soft}` and the border to `{colors.primary-active}`. Used for secondary CTAs like "Learn More" or "View Details".

**`button-tertiary-text`** — A text-only button with no background or border. Text is `{colors.primary}`. Used for less prominent actions like "Cancel" or "See All".

**`button-accent-teal`** and **`button-accent-yellow`** — Alternate primary buttons using the brand's accent colors (#5bc6ce and #fcd94c). The teal variant uses white text; the yellow uses dark ink (#444444) for contrast. These appear in themed sections or promotional banners.

### Cards
**`product-card`** — A softly rounded (`{rounded.lg}`) card on a warm cream background (`{colors.surface-card}`). Contains a square product image with `{rounded.md}`, a title in `{typography.title-sm}`, and a price in bold `{colors.primary}`. A subtle shadow (`0 2px 8px rgba(0,0,0,0.06)`) lifts the card; on hover, the shadow deepens to `0 4px 16px rgba(0,0,0,0.12)`. Badges for "Sale" or "New" overlay the top-left corner.

### Navigation
**`nav-bar`** — A clean, white (`{colors.canvas}`) header bar 72px tall. The brand logo sits centered, with navigation links in `{typography.nav-link}` (Quicksand 15px, weight 600) on either side. A search icon and cart icon float to the right. On scroll, a subtle shadow appears (`0 2px 8px rgba(0,0,0,0.08)`).

**`search-bar`** — A pill-shaped input field on a soft blush background (`{colors.surface-soft}`) with a 1px `{colors.hairline}` border. On focus, the border thickens to 2px and turns `{colors.primary}`. Placeholder text is `{colors.muted}`.

### Badges
**`badge-sale`** — A small, uppercase badge in coral red (`{colors.sale-badge}`) with white text. Used to flag discounted items. `{rounded.sm}` corners keep it friendly.

**`badge-new`** — A minty teal (`{colors.new-badge}`) badge for new arrivals. Same shape and typography as the sale badge.

**`badge-category`** — A pill-shaped badge in marigold yellow (`{colors.accent-yellow}`) with dark ink text. Used in category filters or tags.

### Forms
**`text-input`** — A standard input field on a white background with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border becomes 2px `{colors.primary}`. Error state uses a 2px `{colors.accent-coral}` border.

**`newsletter-input`** and **`newsletter-button`** — A paired input and button for email signups. The input is a pill shape with a hairline border; the button is a primary pink pill. They sit side by side in the footer.

### Footer
**`footer`** — A dark section (`{colors.ink}`) with white text. Links are white with no underline by default, turning `{colors.primary}` on hover. The layout is a multi-column grid of links, social icons, and the newsletter signup.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in 1 column; hero section reduces padding; footer links stack vertically; search bar becomes full-width |
| Tablet | 744–1128px | Nav bar shows limited links; product cards in 2 columns; hero maintains 2/3 width; footer uses 2-column grid |
| Desktop | 1128–1440px | Full nav bar; product cards in 3-4 columns; hero at full width with centered content; footer uses 4-column grid |
| Wide | > 1440px | Max-width container at 1440px; content centered; product cards may show 5 columns |

### Touch Targets
- All buttons and interactive elements maintain a minimum height of 44px (48px preferred).
- Icon buttons are 40x40px.
- Search bar and text inputs are 48px tall.
- Category tabs are 36px+ tall with 8px+ padding.

### Collapsing Strategy
- On mobile, the top nav collapses into a hamburger menu with a slide-out drawer.
- The category strip becomes a horizontally scrollable row on mobile.
- Product cards stack from multi-column to single-column below 744px.
- The footer grid collapses from 4 columns to 2, then to a single stack on mobile.
- Hero sections reduce padding and may stack image and text vertically.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components were inferred from common patterns; exact extracted values were not available.
- Error styling for forms (error messages, validation icons) was not extracted.
- Dark mode is not present on the live site; no dark palette is defined.
- Sub-brand or seasonal color palettes (e.g., holiday collections) were not extracted.
- The exact font weights and sizes for MotelCalifornia-Regular and Tenor Sans are inferred from typical usage; the extracted CSS may have used system fallbacks.
- The `Myriad Pro Regular` font declaration was found but not used in any visible component; it may be a legacy or fallback.
- The `Omletta` font declaration was found but not used in any visible component; it may be a legacy or fallback.
- Animation and transition durations/easings were not extracted.
- The exact spacing values for padding and margins in components are inferred from common patterns; the extracted CSS did not provide precise values.
- The star rating component's exact size and spacing were not extracted.
- The newsletter signup's success/error states were not extracted.
- The cart and checkout flow (Shopify platform) was not analyzed; its colors may include Shopify defaults.
