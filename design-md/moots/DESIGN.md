---
version: alpha
name: "Moots"
source_url: "https://moots.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A titanium bike brand that treats its raw material as finish, not substrate — the dominant hex is not a color but a near-black #121212 that reads as deep shadow on brushed metal, broken by the warm burn of #cc6633 that surfaces on weld details, logo marks, and accent callouts. The palette is a study in industrial restraint: #dedede and #f3f3f3 for light surfaces, #242833 and #101820 for dark structural elements, and the surprising #334fb4 — a cool cobalt that appears in select product badges and technical callouts, suggesting precision engineering rather than lifestyle warmth. Typography runs Assistant at moderate weights, with display sizes staying lean (likely 400–600 weight) to let the photography of hand-welded titanium frames carry the emotional weight. The site reads as a workshop catalog: generous whitespace around product imagery, hairline-thin borders in #c7c4b9 that suggest blueprint lines, and a muted olive #786f51 that surfaces in heritage badges and material callouts. There is no glossy hero — the brand trusts close-cropped macro shots of weld beads, raw titanium texture, and Colorado mountain backdrops over typographic heroism. Buttons are flat and angular (`{rounded.sm}`) rather than pill-shaped, and the navigation feels like a toolbelt — utilitarian, spaced for clarity, with the logo anchoring a left-aligned layout. The overall effect is a brand that says "we build things from metal" without ever shouting it.

colors:
  primary: "#cc6633"
  primary-active: "#b3592e"
  primary-disabled: "#e6b399"
  ink: "#121212"
  body: "#242833"
  muted: "#3f464d"
  muted-soft: "#40454d"
  hairline: "#c7c4b9"
  hairline-soft: "#e3e2dc"
  canvas: "#f3f3f3"
  surface-soft: "#f2f4f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#334fb4"
  accent-olive: "#786f51"
  accent-warm: "#cc6633"
  badge-heritage: "#786f51"
  badge-tech: "#334fb4"

typography:
  display-xl:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  title-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.15px
  body-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  caption-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-outline-light:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.canvas}"
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
    border: "2px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  logo:
    height: 32px
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "0 {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-heritage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-badge-tech:
    backgroundColor: "{colors.badge-tech}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} 0"
  hero-heading:
    typography: "{typography.display-xl}"
    color: "{colors.canvas}"
  hero-subheading:
    typography: "{typography.display-sm}"
    color: "{colors.hairline-soft}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "0 0 {spacing.lg} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  section-subheading:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.hairline-soft}"
  footer-link-hover:
    color: "{colors.canvas}"
  footer-heading:
    typography: "{typography.caption}"
    color: "{colors.canvas}"
    padding: "0 0 {spacing.sm} 0"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    padding: "{spacing.base} 0"
    typography: "{typography.body-md}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's warm accent #cc6633 on a white background. Uses uppercase Assistant at 14px/600 with 0.5px letter-spacing for a precise, engineered feel. Corners are subtly broken at {rounded.sm} (4px) — a deliberate departure from the pill shapes common in consumer brands. On hover, the background deepens to {colors.primary-active} (#b3592e); disabled state drops to a muted salmon {colors.primary-disabled} (#e6b399). The 44px height and 12px/28px padding create a compact, tool-like proportion.

**`button-secondary`** — An outlined variant with a 2px solid {colors.ink} border on a transparent background. The same uppercase typography and {rounded.sm} corners maintain consistency, while the active state inverts to a solid {colors.ink} fill with white text. Used for "Learn More" or "View Details" actions alongside primary buttons.

**`button-tertiary-text`** — A text-only button with no background or border, used for secondary actions like "Cancel" or "Skip." The uppercase typography and 0 padding-left/right keep it aligned with the button system while reducing visual weight.

**`button-outline-light`** — A light variant for use on dark backgrounds (hero sections, dark product cards). White border and text on transparent background, maintaining the 2px stroke and uppercase typography. Active state fills with white.

### Cards
**`product-card`** — The primary product presentation unit, a white card with a 1px {colors.hairline-soft} border and {rounded.sm} corners. The image occupies the top portion at a 4:3 aspect ratio with rounded top corners only. Below, the title uses {typography.title-sm} (16px/600) and the price uses {typography.body-md} (16px/400). On hover, the card lifts with a subtle box-shadow and the border strengthens to {colors.hairline}. Badges overlay the image at top-left using either {colors.badge-heritage} (#786f51, olive) for heritage models or {colors.badge-tech} (#334fb4, cobalt) for technical models.

**`product-card-badge`** — A small uppercase label positioned absolutely over the product image. Uses 11px/700 typography with 0.5px letter-spacing and {rounded.xs} (2px) corners. The olive variant signals "Handmade in Colorado" heritage; the cobalt variant signals technical features like "Titanium" or "Custom Geometry."

### Navigation
**`nav-bar`** — A fixed top navigation at 72px height with a white background and a 1px {colors.hairline-soft} bottom border. Links use uppercase Assistant at 14px/600 with 0.5px letter-spacing, colored {colors.muted} by default and {colors.ink} when active. The active state includes a 2px {colors.primary} bottom border. On scroll, the nav gains a subtle box-shadow. The logo sits left-aligned at 32px height.

**`nav-link`** — Individual navigation items with 8px/16px padding. The uppercase treatment and generous letter-spacing give the nav a technical, blueprint-like quality. Active links drop the muted color for {colors.ink} and gain the primary-colored underline.

### Forms
**`text-input`** — Standard text input with a white background, 1px {colors.hairline} border, and {rounded.sm} corners. The 48px height and 12px/16px padding provide comfortable touch targets. On focus, the border thickens to 2px {colors.primary}. Error state uses a 2px {colors.primary} border (the warm accent serves as both primary and error color, consistent with the brand's limited palette).

**`select-dropdown`** — Matches the text-input styling for visual consistency. The same 48px height, white background, and {rounded.sm} corners ensure form elements read as a unified system.

**`search-bar`** — A compact 44px search input with {rounded.sm} corners and a 1px {colors.hairline} border. On focus, the border thickens to 2px {colors.primary}. The smaller height (44px vs 48px for text inputs) distinguishes it as a utility element rather than a primary form field.

### Footer
**`footer`** — A dark section with {colors.ink} background and {colors.hairline-soft} text. Links use {typography.link} (14px/500) and hover to white. Section headings use {typography.caption} (13px/500, uppercase) in white. The 48px vertical padding provides breathing room for link columns and brand information.

### Filters
**`filter-chip`** — A pill-shaped filter toggle with {rounded.full} corners, a light gray background ({colors.surface-soft}), and a 1px {colors.hairline} border. Active state inverts to {colors.ink} background with white text. The 6px/16px padding and 14px body typography keep chips compact for horizontal filter strips.

### Accordion
**`accordion-trigger`** — A full-width clickable header with no background, {typography.title-sm} (16px/600), and a 1px {colors.hairline-soft} bottom border. Content panels use {typography.body-md} with {spacing.base} padding. Used for FAQ sections and product specifications.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, stacked filter chips, reduced hero heading to {typography.display-lg}, footer links collapse to single column |
| Tablet | 744–1128px | Two-column product grid, horizontal nav with dropdown menus, filter chips in horizontal scroll, hero maintains {typography.display-xl} with reduced padding |
| Desktop | 1128–1440px | Three-column product grid, full horizontal navigation, filter sidebar on collection pages, hero with full padding and background image |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, extended hero with parallax effect, additional whitespace around product cards |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch targets
- Navigation links have 44px minimum touch area (8px padding + 28px text height)
- Filter chips are 32px+ height with 16px horizontal padding for comfortable tapping
- Product card CTAs are 44px minimum height
- Accordion triggers have 48px minimum touch height

### Collapsing Strategy
- Navigation collapses to hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Filter chips collapse from horizontal strip to dropdown "Filter" button below 744px
- Footer link columns stack vertically below 744px
- Hero section reduces padding and heading size below 744px
- Product card badges reposition from absolute to inline below 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components could not be fully extracted from static analysis; the above are informed estimates based on common patterns
- Error state styling for forms (error messages, validation icons) was not visible in the extracted data
- Dark mode or high-contrast mode preferences are not documented
- Sub-brand or collection-specific color variations (e.g., limited edition bikes) may exist beyond the extracted palette
- Animation durations, easing curves, and transition properties are not captured
- Focus ring styles (outline, offset, color) for keyboard navigation are not documented
- The extracted font stack shows only "Assistant" — fallback stacks are inferred
- Spacing values for specific components (e.g., product card padding) are estimated based on common e-commerce patterns
- The extracted hex list includes #007aff (likely a system/checkout blue) which is not used in the brand palette
- Shopify-specific elements (cart drawer, checkout buttons, payment icons) follow platform defaults and are not customized in this design system
