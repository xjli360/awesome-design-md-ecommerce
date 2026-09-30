---
version: alpha
name: "Eco by Naty"
source_url: "https://naty.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A baby-care brand that leads with a deep forest-green primary (#436352) rather than the pastel pinks and powder blues the category defaults to — a deliberate signal that this is about safety and material science, not nursery decoration. The palette draws from the extracted live site: a warm off-white canvas (#f7f7f7) and a cooler white (#f6f6f6) layer beneath a strong ink (#2b2b2b) for body text, with a secondary green (#44695b) and a muted sage (#869791) that echo the brand's certified-safe positioning. A single high-voltage accent — a marigold yellow (#ffb400) — appears on badges, sale markers, and trust icons, while a restrained red (#c11432) is reserved for error states and critical warnings. Typography runs Futura Std (Book and Medium) across all headings and body copy, a geometric sans-serif that reads as modern, clean, and slightly European — no decorative serifs, no fuss. Buttons use the primary green at full saturation with white text, rounded at {rounded.sm}, while secondary actions invert to a white background with a green border. Product cards sit on white surfaces with soft shadows and {rounded.md} corners, each featuring a small green "Certified Safe" badge in {rounded.xs} that repeats the brand's core claim. The top navigation is a fixed white bar with the green logo mark, a search icon, and a cart indicator — the only color in the nav is the green logo, keeping the interface calm for shopping parents. The brand's voice is clinical but warm: "Made For Skin. Built For Trust." is not a tagline but a promise backed by the green system.

colors:
  primary: "#436352"
  primary-active: "#34715b"
  primary-disabled: "#b4b5b5"
  ink: "#2b2b2b"
  body: "#1a1a1a"
  muted: "#5e5e5e"
  muted-soft: "#7d7d7d"
  hairline: "#d6d6d6"
  hairline-soft: "#eeeeee"
  canvas: "#f7f7f7"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffb400"
  accent-red: "#c11432"
  sage: "#869791"
  secondary-green: "#44695b"
  badge-green: "#189a1b"
  badge-green-text: "#ffffff"
  error-text: "#c11432"
  link-blue: "#00597e"
  dark-ink: "#222222"
  deep-navy: "#073c52"

typography:
  display-xl:
    fontFamily: "'Futura Std Medium', 'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Futura Std Medium', 'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Futura Std Medium', 'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Futura Std Medium', 'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Futura Std Medium', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Futura Std Medium', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Futura Std Medium', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Futura Std Book', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
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
    padding: 12px 28px
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 26px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-pill-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
    textColor: "{colors.error-text}"
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  checkbox:
    backgroundColor: "{colors.surface-card}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    checkedBackground: "{colors.primary}"
    checkedBorder: "{colors.primary}"
    size: 20px
  radio:
    backgroundColor: "{colors.surface-card}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    checkedBackground: "{colors.primary}"
    checkedBorder: "{colors.primary}"
    size: 20px
  top-nav:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-logo:
    height: 32px
    width: auto
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  search-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    size: 24px
  cart-icon:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    size: 24px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    size: 18px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    shadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.badge-green-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "top-left"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "top-right"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 52px
  hero-secondary-cta:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: "12px 30px"
    height: 52px
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    iconColor: "{colors.primary}"
  certification-badge:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.badge-green-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.surface-card}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0 0"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0 {spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    padding: "0 0 {spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with the brand green (#436352) and white uppercase text. Used for "Add to Cart", "Shop Now", and "Subscribe" actions. On hover, shifts to a slightly deeper green (#34715b). Disabled state uses a muted gray (#b4b5b5) to signal inactivity. Height is 48px with 12px/28px padding and {rounded.sm} corners.

**`button-secondary`** — An outlined variant with a white background and 2px green border. Used for secondary actions like "Learn More" or "View Details". On hover, fills with the primary green and inverts text to white. Same 48px height as primary for alignment in forms.

**`button-tertiary-text`** — A text-only button with no background or border, used for inline actions like "Cancel" or "Read More". Uses the primary green color and button-md typography. Padding is minimal (8px vertical) to sit flush with surrounding text.

**`button-pill-accent`** — A pill-shaped button using the marigold yellow (#ffb400) accent color for promotional CTAs like "Sale" or "Limited Offer". Uses {rounded.full} for a friendly, rounded appearance. Text is dark ink (#2b2b2b) for contrast against the yellow.

### Cards
**`product-card`** — A white card with a 1:1 aspect ratio product image at the top, followed by the product title and price. Uses {rounded.md} corners and a subtle shadow (0 2px 8px rgba(0,0,0,0.08)). On hover, the shadow deepens to 0 4px 16px rgba(0,0,0,0.12). The image has rounded top corners only, creating a clean boundary between photo and text.

**`product-card-badge`** — A small green badge (#189a1b) with white uppercase text, positioned at the top-left of the product image. Used to indicate "Certified Safe" or "Eco Certified". Uses {rounded.xs} for a subtle, non-distracting shape.

**`product-card-sale-badge`** — A yellow badge (#ffb400) with dark text, positioned at the top-right of the product image. Used for sale or discount indicators. Same shape and size as the certification badge but in the accent color.

### Navigation
**`top-nav`** — A fixed white bar at 72px height with a 1px bottom border in the soft hairline (#eeeeee). Contains the brand logo (32px height), navigation links in uppercase Futura Std Book, a search icon, and a cart icon. Active nav links use the primary green with a 2px bottom border. Inactive links are muted gray.

**`cart-badge`** — A small circular badge (18px) filled with the primary green, displaying the cart item count in white caption-sm text. Positioned at the top-right of the cart icon.

### Forms
**`text-input`** — A standard input field with a white background, 1px hairline border (#d6d6d6), and {rounded.sm} corners. On focus, the border thickens to 2px and turns green. Error state uses a 2px red (#c11432) border with red text for the error message. Height is 48px with 12px/16px padding.

**`checkbox`** — A 20px square with {rounded.xs} corners. Unchecked state shows a 2px hairline border. Checked state fills with the primary green and shows a white checkmark. The border also turns green when checked.

**`radio`** — A 20px circle with {rounded.full}. Unchecked state shows a 2px hairline border. Checked state shows a filled green circle with a white dot in the center.

### Hero
**`hero-section`** — A full-width section with a soft gray background (#f6f6f6) and large display text. Contains a primary CTA button and an optional secondary outlined button. Padding is 64px top/bottom with 24px left/right. The hero typically features a product image or lifestyle photo alongside the text.

**`hero-cta`** — A larger version of the primary button (52px height, 14px/32px padding) used exclusively in the hero section for maximum visual weight.

**`hero-secondary-cta`** — An outlined button matching the hero CTA in size but with a transparent background and green border. Used for secondary hero actions like "Learn More".

### Badges & Trust Signals
**`trust-badge`** — A small horizontal badge with a soft gray background (#f6f6f6), muted text, and a green icon. Used to display trust signals like "Free Shipping", "30-Day Returns", or "Certified Safe". Padding is 8px/16px with {rounded.sm} corners.

**`certification-badge`** — A compact green badge (#189a1b) with white uppercase text, used on product detail pages to highlight certifications (e.g., "OEKO-TEX", "FSC Certified"). Uses {rounded.xs} and 4px/10px padding.

### Footer
**`footer`** — A dark footer with a deep ink background (#2b2b2b) and white text. Links are muted gray (#7d7d7d) and use the link typography. Section headings are white, uppercase, and use title-sm typography. Padding is 48px top/bottom with 24px left/right.

### Accordion
**`accordion`** — A collapsible section with a white background, 1px soft hairline border, and {rounded.sm} corners. The header uses title-sm typography in ink color. The content area uses body-sm in muted color with 8px top padding. Used for FAQ sections and product details.

### Dividers
**`divider`** — A 1px horizontal line in the soft hairline color (#eeeeee). Used between sections for subtle separation.
**`divider-strong`** — A 1px horizontal line in the standard hairline color (#d6d6d6). Used for more prominent visual breaks.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero text reduces to display-md; product cards stack vertically; top-nav collapses to hamburger menu; footer links stack; accordions expand by default |
| Tablet | 744–1128px | Two-column product grid; hero uses display-lg; top-nav shows limited links (Shop, About, Search, Cart); footer uses 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero uses display-xl; footer uses 4-column grid |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to 4 columns; hero has larger imagery |

### Touch Targets
- All buttons and interactive elements: minimum 48px height (exceeds Apple's 44px guideline)
- Icon buttons (search, cart): 48px tap area with 24px icon
- Checkbox and radio: 20px tap area, but wrapped in 44px minimum touch target
- Nav links: 72px tap area (full nav height)
- Accordion headers: 48px minimum tap height

### Collapsing Strategy
- Top nav: On mobile (< 744px), all navigation links collapse behind a hamburger menu icon. The logo and cart icon remain visible.
- Product grid: Reduces from 4 columns on wide to 3 on desktop, 2 on tablet, and 1 on mobile.
- Footer: Reduces from 4 columns on desktop to 2 on tablet, stacking vertically on mobile.
- Hero section: On mobile, the hero image moves above the text content; on desktop, they sit side by side.
- Accordions: On mobile, all accordions are expanded by default for easy reading; on desktop, they are collapsed.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be extracted from the live site; the active states listed are inferred from common patterns.
- Error styling for forms (validation messages, error icons) is not fully documented; only the border color change is captured.
- Dark mode is not supported by the brand; no dark mode tokens are defined.
- The brand's icon set (naty-icons) is referenced in font declarations but the individual icon glyphs and their usage are not documented here.
- Sub-brand or promotional color variations (e.g., seasonal campaigns, limited editions) are not captured.
- The exact font weights for Futura Std Book and Futura Std Medium are inferred; the brand may use additional weights (e.g., Light, Bold) that were not found in the extracted data.
- Animation and transition durations (e.g., button hover, card shadow change) are not specified; a default of 200ms ease-in-out is assumed.
- The brand's use of imagery and photography style (e.g., lifestyle vs. product-only) is not documented.
- Accessibility contrast ratios for text on various backgrounds have not been verified against WCAG standards.
- The checkout flow (if any) and its specific styling are not captured; the brand may use a third-party checkout that overrides these tokens.
