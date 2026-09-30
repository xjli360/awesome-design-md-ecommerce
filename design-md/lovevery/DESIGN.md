---
version: alpha
name: "Lovevery"
source_url: "https://lovevery.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A child-development brand that uses color as a cognitive signal, where #131c66 (a deep navy) anchors the system not as a background but as a primary action color — an unusual choice for a brand aimed at babies and toddlers, who are typically surrounded by pastels. The navy sits alongside #b85bbf (a warm magenta), #bbdc00 (a chartreuse green), and #ff9955 (a tangerine orange), creating a palette that feels like a carefully curated toy box rather than a nursery. The brand's typography runs BrownPro across headings and body text, a rounded geometric sans-serif that reads as friendly without being childish — it has the weight and structure of a serious educational tool. Product photography is the real hero: crisp, well-lit images of wooden toys and play kits on white backgrounds, with the occasional #f7f3f7 (a blush-tinted off-white) surface to soften the experience. The site uses generous whitespace and {rounded.lg} corners on cards and buttons, creating a calm, unhurried browsing rhythm that mirrors the brand's "stage-based play" philosophy — nothing is rushed, everything has its moment. The checkout flow, powered by Shopify, introduces a secondary blue (#202ea8) for payment actions, but the core brand navy remains the dominant interactive color across the main shopping experience.

colors:
  primary: "#131c66"
  primary-active: "#202ea8"
  primary-disabled: "#e5e7eb"
  ink: "#131c66"
  body: "#514f4e"
  muted: "#6e757c"
  muted-soft: "#9ca3af"
  hairline: "#dcd7d2"
  hairline-soft: "#e5e7eb"
  canvas: "#ffffff"
  surface-soft: "#f5f7fc"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-magenta: "#b85bbf"
  accent-chartreuse: "#bbdc00"
  accent-tangerine: "#ff9955"
  accent-teal: "#60cbc2"
  accent-yellow: "#fedb00"
  accent-green: "#1cc286"
  accent-cyan: "#03b2cb"
  accent-mint: "#4edcca"
  surface-blush: "#f7f3f7"
  surface-mint: "#effaf9"
  surface-indigo: "#eef2ff"

typography:
  display-xl:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'BrownPro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
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
    padding: 14px 28px
    height: 48px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-accent-magenta:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-chartreuse:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
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
  text-input-error:
    border: "2px solid {colors.accent-tangerine}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0
  product-card-image:
    rounded: "{rounded.lg} {rounded.lg} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.xl}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.base} 0"
  badge-new:
    backgroundColor: "{colors.accent-chartreuse}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-tangerine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-stage:
    backgroundColor: "{colors.accent-magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
  footer-heading:
    typography: "{typography.title-md}"
    textColor: "{colors.on-primary}"
  accordion-trigger:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  testimonial-card:
    backgroundColor: "{colors.surface-blush}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  testimonial-author:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0 0 0"
  step-indicator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 32px
    padding: "0 12px"
  step-indicator-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the deep navy {colors.primary} with white text. Used for "Add to Cart", "Subscribe", and "Shop Now" actions. On hover, it shifts to {colors.primary-active} (#202ea8) for a subtle state change. The disabled state uses {colors.primary-disabled} (#e5e7eb) with muted text, signaling the action is unavailable. All primary buttons use {rounded.sm} (8px) corners — soft enough to feel approachable, not so round as to feel toy-like.

**`button-secondary`** — An outlined variant with a white background and navy text, used for "Learn More" and "View Details" actions. The 2px border matches {colors.primary} and shifts to {colors.primary-active} on hover. This button sits alongside primary buttons in hero sections and product grids, offering a clear visual hierarchy without competing for attention.

**`button-accent-magenta`** and **`button-accent-chartreuse`** — Brand-specific accent buttons used for promotional calls-to-action, stage-specific offers, and seasonal campaigns. The magenta variant (#b85bbf) is used for "Play Kits" and subscription flows, while the chartreuse (#bbdc00) appears on sale banners and limited-time offers. Both use white or navy text depending on contrast requirements.

**`button-pill`** — A fully rounded pill button used for filter tags, stage selectors, and compact actions. Uses {rounded.full} with tighter padding (10px 24px) and smaller typography. Appears in the product filter strip and the "Find Your Stage" quiz flow.

### Cards
**`product-card`** — The primary product display unit, featuring a full-bleed image with {rounded.lg} (20px) corners on the top, and a clean white bottom section for title and price. The card has no background color of its own — it inherits the white canvas and relies on the product image for visual weight. Titles use {typography.title-md} (18px, weight 600) and prices use {typography.body-md} (16px, weight 400) in {colors.body}.

**`testimonial-card`** — A customer review card on a {colors.surface-blush} (#f7f3f7) background, with {rounded.lg} corners and generous padding. The body text uses {typography.body-md} in {colors.body}, and the author attribution sits below in {typography.caption} in {colors.ink}. These cards appear in a horizontal scroll strip on the homepage and product pages.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height, white background with a subtle bottom border in {colors.hairline-soft}. The logo sits left-aligned, with nav links in {typography.nav-link} (15px, weight 600). Active links receive a 2px bottom border in {colors.primary}. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

**`nav-link-active`** — The active state for navigation links, using {colors.primary} text and a 2px bottom border in the same color. This creates a clear "you are here" indicator without relying on background fills.

### Forms
**`text-input`** — Standard text input fields with a white background, 1px {colors.hairline} border, and {rounded.sm} corners. On focus, the border thickens to 2px and switches to {colors.primary}. Error states use a 2px {colors.accent-tangerine} (#ff9955) border — a warm, non-alarming error color that fits the brand's friendly tone.

**`quantity-selector`** — A compact input group for adjusting product quantities, with a 1px {colors.hairline} border and {rounded.sm} corners. The increment/decrement buttons sit on a {colors.surface-soft} background, creating a clear visual separation from the numeric input.

### Badges
**`badge-new`** — A small, uppercase badge on a {colors.accent-chartreuse} background with navy text. Used to flag new products, new play kits, and recently added items. The {rounded.xs} (4px) corners keep it subtle and non-distracting.

**`badge-sale`** — A sale badge on a {colors.accent-tangerine} background with white text. Used for promotional pricing and limited-time offers. Same {rounded.xs} corners as the new badge for consistency.

**`badge-stage`** — A pill-shaped badge on a {colors.accent-magenta} background with white text, used to indicate which developmental stage a product belongs to (e.g., "0-12 Weeks", "5-6 Months"). The {rounded.full} shape and larger padding make it feel like a tag rather than a label.

### Footer
**`footer-section`** — The site footer uses the deep navy {colors.primary} as its background, with white text throughout. Links use {typography.link} (14px, weight 400, underlined on hover) and headings use {typography.title-md} (18px, weight 600). The footer includes columns for "Shop by Stage", "About", "Support", and social links, with generous {spacing.xxl} padding top and bottom.

### Accordion
**`accordion-trigger`** — Used on product detail pages and the FAQ section. The trigger is a full-width clickable area with {typography.title-md} text, a white background, and a bottom border in {colors.hairline-soft}. The expanded state rotates a chevron icon 180 degrees. The content area uses {typography.body-md} with {spacing.sm} top padding and {spacing.base} bottom padding.

### Step Indicator
**`step-indicator`** — Used in the subscription flow and "Find Your Stage" quiz. Each step is a pill-shaped indicator on a {colors.surface-soft} background with {colors.muted} text. The active step switches to {colors.primary} background with white text. Steps are connected by a thin {colors.hairline} line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero section reduces padding to {spacing.xl}; buttons go full-width; testimonial cards show 1 per view; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero uses {spacing.section} padding; testimonial cards show 2 per row; footer shows 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; hero uses {spacing.section} padding with larger heading; testimonial cards show 3 per row; footer shows 4-column grid |
| Wide | > 1440px | Max-width container at 1440px; product grid can show 4 columns; hero uses larger display-xl typography; all layouts centered with generous margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px
- Product card images are tappable and link to product detail pages
- Accordion triggers have a minimum height of 48px for easy tapping
- Quantity selector buttons are 40x40px minimum
- Nav bar links have 44px minimum tap area

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses to a hamburger menu with a full-screen overlay
- Product filters collapse into a slide-out drawer on mobile
- Footer columns collapse from 4 columns to a single column on mobile
- Testimonial cards switch from horizontal scroll to vertical stack on mobile
- Hero sections reduce padding and font sizes on mobile
- Product images switch from landscape to square aspect ratio on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list includes many Shopify checkout and payment widget colors (e.g., #6366f1, #818cf8, #a5b4fc, #c7d2fe, #e0e7ff, #eef2ff are likely Shopify Pay or Klarna/Afterpay brand colors). These have been excluded from the core palette but may appear in checkout flows.
- The font-family declarations included "BradfordLLWeb-MediumItalic" which may be used for specific editorial content or pull quotes — not included in the core typography system as it wasn't confirmed as a primary face.
- Hover states for secondary buttons, text inputs, and links are inferred from common patterns — exact transition durations, shadow depths, and micro-interactions were not extractable.
- Error states for forms (validation messages, error icons) were not observed — the error border color is an educated guess based on the accent-tangerine color.
- Dark mode is not supported — the brand uses a light-only color system.
- The "Find Your Stage" quiz flow was not fully analyzed — its component states (progress bar, radio buttons, result cards) are not documented here.
- Sub-brand palettes for "Lovevery Play Kits" vs "Lovevery Books" vs "Lovevery The Play Gym" may exist but were not distinguishable from the extracted data.
- Animation timing, easing curves, and scroll behavior were not extractable from static analysis.
- The checkout flow uses Shopify's default styling with some brand overrides — exact component tokens for the checkout page are not included.
