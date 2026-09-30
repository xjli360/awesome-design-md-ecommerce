---
version: alpha
name: "Evolv"
source_url: "https://www.evolvsports.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A climbing brand that builds its visual identity around the raw, unpolished texture of the sport itself, using a near-monochrome base of #1a1a1a ink on #f4f4f4 canvas punctuated by a single, urgent accent: #e54601, a burnt-orange that reads like rust, chalk dust, and desert sandstone compressed into one signal. The brand avoids the glossy, aspirational sheen common in outdoor gear marketing; instead, it leans into a utilitarian, almost industrial palette — #4e5154 and #595959 for secondary text, #bfbfbf and #d3d3d3 for borders and dividers — that feels like it was lifted from a climbing gym’s hold bin or a well-worn crash pad. Typography is split between Effra (a geometric sans-serif with a slight humanist warmth) and CommitMono (a monospace that appears in technical specs and product details), creating a deliberate tension between approachable product copy and precise, code-like specifications. Buttons and CTAs use the full {rounded.sm} radius, while product cards and badges adopt a tighter {rounded.xs} that suggests precision engineering rather than friendliness. The navigation bar is a thin, dark strip — {colors.ink} background with white text — that stays out of the way, letting product photography and the orange accent do the heavy lifting. The overall effect is a brand that trusts its audience to appreciate subtlety: a muted palette that lets the #e54601 accent land like a chalked hand on a hold, and a typographic system that treats product specs with the same seriousness as marketing copy.

colors:
  primary: "#e54601"
  primary-active: "#cb2f12"
  primary-disabled: "#e5b3b3"
  ink: "#1a1a1a"
  body: "#2a2b2d"
  muted: "#4e5154"
  muted-soft: "#595959"
  hairline: "#d3d3d3"
  hairline-soft: "#e6e6e6"
  canvas: "#f4f4f4"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#1f495b"
  accent-teal: "#31738f"
  accent-purple: "#af5bd7"
  error: "#dd4124"
  success: "#2b69b2"

typography:
  display-xl:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Effra', 'Helvetica', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.25px
    textTransform: uppercase
  mono-body:
    fontFamily: "'CommitMono', 'Source Code Pro', 'monospace', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  mono-caption:
    fontFamily: "'CommitMono', 'Source Code Pro', 'monospace', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
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
    padding: 12px 24px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.muted}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 24px
  button-tertiary-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.lg}"
  nav-bar-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
  nav-bar-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} 0 0 0"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    height: 36px
    border: "1px solid {colors.hairline}"
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0"
    border-bottom: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's signature burnt-orange {colors.primary} on a white background. Text is set in {typography.button-md} with a weight of 600, giving it enough heft to stand out against the muted palette. On hover or active, the background shifts to {colors.primary-active}, a deeper, more rusted orange. The disabled state uses {colors.primary-disabled}, a pale pinkish-beige that signals unavailability without visual noise. Padding is generous at 12px 24px, with a height of 44px and a {rounded.sm} corner radius that feels precise but not aggressive.

**`button-secondary`** — An outlined alternative that uses the white {colors.canvas} background with a 1px {colors.hairline} border and {colors.ink} text. On active, the background shifts to {colors.surface-soft} and the border thickens to {colors.muted}. This button is used for less critical actions like "View Details" or "Cancel," maintaining the brand's utilitarian restraint.

**`button-tertiary`** — A text-only button with no background or border, used for inline actions like "Clear Filters" or "Learn More." On hover, the text color switches to {colors.primary}, providing a subtle visual cue without the weight of a full button.

### Cards
**`product-card`** — The primary product display unit, a white card with {rounded.xs} corners and {spacing.sm} padding. The product image sits flush within the card, also using {rounded.xs}. Below, the title uses {typography.title-sm} in {colors.ink}, and the price is set in {typography.body-sm} in {colors.muted}. The card has no shadow or border, relying on the contrast between the white surface and the {colors.canvas} background to define its boundaries.

**`badge-new`** — A small, uppercase label in {colors.primary} with white text, using {typography.badge} (11px, 700 weight, 0.5px letter spacing). The {rounded.xs} corners and tight 2px 8px padding make it feel like a tag affixed to the product. Variants include `badge-sale` (using {colors.error}) and `badge-out-of-stock` (using {colors.muted}).

### Navigation
**`nav-bar`** — A thin, dark strip at 56px height with a {colors.ink} background and white text. Links are set in {typography.nav-link} (14px, 500 weight, uppercase with 0.25px letter spacing) with 8px 12px padding. The active state shifts the text color to {colors.primary}, creating a subtle orange underline effect without an actual underline. The bar is intentionally low-contrast and minimal, letting the product content dominate.

**`search-bar`** — A pill-shaped input field with {rounded.full} corners, white background, and a 1px {colors.hairline} border. On focus, the border switches to {colors.primary}, providing a clear but restrained visual cue. The 44px height and 10px 20px padding make it comfortable for both desktop and mobile use.

### Forms
**`text-input`** — A standard input field with {rounded.xs} corners, 44px height, and 10px 14px padding. The default state uses a {colors.hairline} border; on focus, it switches to {colors.primary}. Error states use {colors.error} (#dd4124) for the border, providing a clear but not alarming signal. The typography is {typography.body-md} (16px, 400 weight), ensuring readability across devices.

### Footer
**`footer`** — A dark section with {colors.ink} background and {colors.muted-soft} text, padded generously with {spacing.xxl} on top and bottom. Links are set in {typography.link} (14px, 400 weight) in white, providing clear contrast against the dark background. The footer is divided into columns for navigation, support, and legal links, with no decorative elements — just clean, functional hierarchy.

### Hero
**`hero-section`** — A full-width dark section with {colors.ink} background and white text, used for category headers and promotional banners. The title uses {typography.display-xl} (36px, 700 weight) with a slight negative letter-spacing, and the subtitle uses {typography.body-md} in {colors.muted-soft}. The section padding is {spacing.section} (64px) on top and bottom, creating a dramatic visual break from the content below.

### Filters
**`filter-chip`** — A pill-shaped filter option with {rounded.full} corners, white background, and a 1px {colors.hairline} border. Text is set in {typography.button-sm} (13px, 600 weight). The active state inverts the colors: {colors.ink} background with white text. These chips are used in a horizontal strip above product grids, allowing users to quickly toggle between categories like "Men's," "Women's," "Shoes," and "Harnesses."

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger menu; hero-section padding reduces to {spacing.xl}; filter chips wrap to two rows; search-bar becomes full-width; product-card padding reduces to {spacing.xs} |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows limited links (Home, Shop, About); filter chips remain in single row with horizontal scroll; hero-section uses {spacing.xxl} padding |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; filter chips in single row; hero-section uses full {spacing.section} padding; search-bar is centered with max-width |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; nav-bar remains full; hero-section uses larger typography (display-xl at 40px) |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Filter chips are 36px tall with 16px horizontal padding, exceeding the 44px touch target when including surrounding whitespace
- Nav-bar links have 8px vertical padding, making the effective touch area 56px (the full nav-bar height)
- Product-card links and buttons are at least 44px tall

### Collapsing Strategy
- Nav-bar collapses to a hamburger menu on mobile, with a slide-out drawer for full navigation
- Product grids collapse from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Filter chips collapse from a single horizontal row to a two-row wrap on mobile
- Hero-section padding reduces from 64px to 32px on mobile, with typography scaling down proportionally
- Footer columns collapse from 4 to 2 on tablet, and to a single column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for many components (e.g., product-card, footer links) could not be reliably extracted from the static HTML/CSS
- Error state styling for forms (e.g., validation messages, icon placement) was not observed
- Dark mode or high-contrast mode variants are not documented — the brand may not support them
- The extracted color list includes several blues (#1f495b, #31738f, #2b69b2, #1976d2) that may be framework defaults or widget colors; the brand's true secondary palette may be narrower
- Font weights for Effra and CommitMono are inferred from common usage; the brand may use additional weights (e.g., 300, 800)
- Animation and transition durations (e.g., button hover, card hover) were not extracted
- Spacing values for specific components (e.g., gap between product cards, margin between sections) are estimated from general patterns
- The brand may use a different primary font for headings vs. body text; the extracted font list shows both Effra and CommitMono, but their exact roles are inferred
- Checkout flow components (cart, payment forms) were not observed and may use a different design system
