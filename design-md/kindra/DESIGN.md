---
version: alpha
name: "Kindra"
source_url: "https://ourkindra.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, confident wineberry (#6e1d46) anchors Kindra's visual identity — a shade that reads as both botanical and clinical, neither pastel-pink nor sterile-white, signaling a brand that treats vaginal health as a serious, beautiful category rather than a whispered embarrassment. The extracted palette is dominated by framework defaults (Bootstrap blues, grays, greens), but that singular wineberry — appearing as the most distinctive non-generic hex — becomes the brand's primary voltage, used across CTAs, section headers, and product badges. The site runs on a clean white canvas with generous vertical spacing, letting product photography and ingredient storytelling breathe. Typography defaults to system fonts (Helvetica Neue, Arial, -apple-system) with no custom brand typeface detected, suggesting a pragmatic, accessible approach that prioritizes legibility over typographic personality. Buttons carry {rounded.sm} corners — soft but not pill-shaped — and the primary CTA in wineberry against white text creates a crisp, authoritative contrast. The overall mood is warm clinical: trustworthy enough for medical claims, warm enough for intimacy. Product cards use {rounded.md} with subtle shadow, while the nav bar stays transparent until scroll, then gains a white background with {colors.hairline} bottom border. The brand's voice in copy is direct, educational, and destigmatizing — the design follows suit, with no gimmicks, no excessive ornament, just clear hierarchy and that one unforgettable wineberry pulse.

colors:
  primary: "#6e1d46"
  primary-active: "#5a1738"
  primary-disabled: "#cba0b5"
  ink: "#1d2124"
  body: "#383d41"
  muted: "#545b62"
  muted-soft: "#818182"
  hairline: "#dae0e5"
  hairline-soft: "#ececf6"
  canvas: "#ffffff"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-warning: "#d39e00"
  accent-success: "#1e7e34"
  accent-info: "#117a8b"
  accent-error: "#bd2130"
  star-rating: "#d39e00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.2px
  badge:
    fontFamily: "Helvetica Neue, Arial, -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0px
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
    rounded: "{rounded.sm}"
  text-input-error:
    border: "2px solid {colors.accent-error}"
    rounded: "{rounded.sm}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.lg}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    typography: "{typography.body-md}"
    padding: "0 {spacing.lg} {spacing.lg}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: "16px"
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
    rounded: "{rounded.xs}"
    height: 32px
    width: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with wineberry {colors.primary} and white text. Uses {typography.button-md} at 15px with 0.3px letter spacing for a slightly elevated, intentional feel. On hover/active, shifts to {colors.primary-active} (#5a1738). Disabled state uses {colors.primary-disabled} (#cba0b5), a muted pinkish-wine that signals non-interactivity without visual noise. Height is 44px with {rounded.sm} corners — soft but not pill-shaped, maintaining a clinical precision.

**`button-secondary`** — Outlined variant with a 2px solid {colors.primary} border on white background. Text remains wineberry. Active state darkens the border to {colors.primary-active} and adds a light {colors.surface-soft} background. Used for "Learn More" and secondary product actions where the primary CTA is already present.

**`button-tertiary-text`** — Pure text button with no background or border, using {colors.primary} text. Used for inline actions like "View Details" in product listings or "Skip" in multi-step flows. Padding is minimal (8px 0) to keep the text aligned with surrounding content.

### Text Inputs
**`text-input`** — Standard form field with white background, {colors.hairline} border, and {rounded.sm} corners. Height 48px with 12px 16px padding for comfortable touch targets. Focus state swaps to a 2px {colors.primary} border, creating a clear visual anchor. Error state uses 2px {colors.accent-error} (#bd2130) border. Used across checkout, account forms, and quiz flows.

**`select-input`** — Dropdown variant matching the text-input dimensions and styling. The chevron icon (not defined in tokens) is {colors.muted} by default, shifting to {colors.primary} on focus.

### Navigation
**`nav-bar`** — Transparent background by default with 72px height, allowing hero imagery to bleed to the top edge. On scroll, gains a white background with a 1px {colors.hairline} bottom border. Navigation links use {typography.nav-link} at 14px with 0.2px letter spacing — compact enough for multiple links, spacious enough for touch. The cart icon and account icon sit at the right edge, using {colors.ink} with hover states in {colors.primary}.

### Product Cards
**`product-card`** — White card with {rounded.md} (12px) corners, subtle box-shadow (not tokenized but standard at 0 2px 8px rgba(0,0,0,0.08)), and {spacing.base} padding. The product image sits at the top with {rounded.sm} (8px) corners, creating a clear visual separation from the text below. Title uses {typography.title-sm} (16px, 600 weight), price uses {typography.body-sm} in {colors.muted}. A "NEW" or "SALE" badge can overlay the image top-left using {badge-new} or {badge-sale} respectively.

### Badges
**`badge-new`** — Small wineberry pill with white uppercase text at 11px, 700 weight, 0.5px letter spacing. Used to flag new product launches or recently added items. {rounded.xs} (4px) keeps it compact and unobtrusive.

**`badge-sale`** — Same dimensions as badge-new but using {colors.accent-error} (#bd2130) for urgency. Appears on discounted products or limited-time offers.

### Hero Section
**`hero-section`** — Full-width section with {spacing.section} (64px) vertical padding, white background. The heading uses {typography.display-xl} (32px, 700 weight, -0.5px letter spacing) for maximum impact. Subheading uses {typography.body-md} (16px) in {colors.body} (#383d41) for readability. A single primary CTA button sits below, with optional secondary link. On mobile, the hero compresses to 48px padding and the heading drops to 28px.

### Footer
**`footer`** — Light gray background ({colors.surface-soft}, #f8f9fa) with {colors.body} text at {typography.body-sm}. Links use {colors.muted} with hover state in {colors.primary}. Organized in columns for desktop (3-4 columns), collapsing to a single column on mobile. Includes legal text, social links, and a newsletter signup form.

### Accordion
**`accordion`** — Used for FAQ sections and product details. White background with 1px {colors.hairline} border and {rounded.sm} corners. Header uses {typography.title-sm} (16px, 600 weight) with {spacing.base} horizontal and {spacing.lg} vertical padding. Content area uses {typography.body-md} with the same horizontal padding and {spacing.lg} bottom padding. A chevron icon rotates on open/close states.

### Quantity Selector
**`quantity-selector`** — Compact control for product detail pages. White background with 1px {colors.hairline} border, 40px height. Two square buttons (32x32) flank a central numeric display. Buttons use {colors.surface-soft} background with {colors.ink} text and {rounded.xs} corners. Used for cart adjustments and subscription frequency selection.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero padding reduces to 48px; nav-bar height drops to 56px; product cards stack full-width; footer collapses to single column; accordions become default for product specs; font sizes scale down 2-4px |
| Tablet | 744–1128px | Two-column product grid; nav-bar remains at 72px; hero maintains 64px padding; footer shows 2 columns; side-by-side layout for product detail (image left, details right) |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero at max width 1128px centered; footer shows 3-4 columns; multi-step checkout visible |
| Wide | > 1440px | Content max-width capped at 1440px; extra whitespace on sides; hero can accommodate larger imagery; product grid can expand to 4 columns if content allows |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target
- Nav links have 48px minimum height for easy tapping
- Quantity selector buttons are 32x32px with 4px internal padding — meets touch target with surrounding whitespace
- Accordion headers are full-width with 48px minimum height
- Product card CTAs are 44px tall with full-width tap area

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px, with slide-in drawer from left
- Product grid collapses from 3 columns (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 to 2 to 1
- Hero section collapses from side-by-side (image + text) to stacked on mobile
- Product detail page collapses from 2-column to single-column below 744px
- Multi-step checkout collapses to single-page accordion on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; system fonts only (Helvetica Neue, Arial, -apple-system). The brand may use a custom font loaded via JavaScript or a service not captured in the extraction.
- Extracted hex colors are heavily dominated by Bootstrap framework defaults (blues, grays, greens, reds, yellows). The true brand palette likely includes additional accent colors not captured. The wineberry (#6e1d46) is the most distinctive non-framework color and is used as primary, but secondary brand colors (if any) could not be reliably extracted.
- Hover and active states for most components are inferred from common patterns rather than extracted from live CSS.
- Error styling for forms (validation messages, error icons) not captured.
- Dark mode or high-contrast mode variants not detected.
- Sub-brand or product-line-specific color variations not captured (e.g., for different product categories like supplements vs. topicals).
- Animation and transition timing values (durations, easing curves) not extracted.
- Shadow tokens (box-shadow, drop-shadow) not captured from live site.
- Icon set and illustration style not documented — the brand may use custom illustrations or icons not captured in the extraction.
- Checkout widget colors (Shopify Pay, Klarna, Afterpay) may be present in the extracted palette but are not part of the brand design system.
- Social media icon colors not captured as brand tokens.
- Stock image dominant tones may have influenced the extracted color list.
