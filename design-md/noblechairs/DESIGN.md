---
version: alpha
name: "noblechairs"
source_url: "https://www.noblechairs.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A German engineering ethos poured into a gaming chair — the brand's visual system is built around a deep, commanding #141414 ink that anchors every product page, while #003399 provides a precise, authoritative accent that appears in logo marks, spec badges, and select navigation elements. The palette is deliberately restrained: a near-black canvas (#141414) against stark white (#ffffff) creates maximum contrast for product photography, with #cbccce and #dfe0e1 serving as subtle surface tones for cards and panels. The extracted #198754 (a muted green) and #cc1420 (a controlled red) appear in status indicators and warranty badges, not as brand colors — they're functional signals within a system that prioritizes clarity over decoration. Montserrat runs throughout at moderate weights (400–600), never exceeding 700, keeping the typography clean and legible against the dark backdrop. Buttons carry {rounded.sm} corners — a precise, industrial radius that mirrors the chair's aluminum base and armrest details. The hero section uses full-bleed product imagery with minimal overlay text, trusting the chair's silhouette and the #141414 field to create drama. The overall feel is that of a premium automotive cockpit translated into a digital storefront: dark, focused, and built around the object itself.

colors:
  primary: "#003399"
  primary-active: "#002266"
  primary-disabled: "#bacbe6"
  ink: "#141414"
  body: "#373b3e"
  muted: "#6f5b1f"
  muted-soft: "#cbccce"
  hairline: "#dfe0e1"
  hairline-soft: "#e8e3d4"
  canvas: "#ffffff"
  surface-soft: "#f5f0e8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#198754"
  accent-red: "#cc1420"
  accent-gold: "#8b7227"
  badge-warning-bg: "#fff3cd"
  badge-warning-text: "#664d03"
  badge-success-bg: "#d1e7dd"
  badge-success-text: "#0f5132"
  badge-error-bg: "#f5d0d2"
  badge-error-text: "#7a0c13"
  hero-overlay: "#141414"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
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
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-ghost-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 36px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 36px
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
    border: "2px solid {colors.accent-red}"
  select-input:
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
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  logo:
    height: 32px
    width: auto
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-section:
    backgroundColor: "{colors.hero-overlay}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: "600px"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.display-sm}"
    color: "{colors.muted-soft}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "16px 40px"
    height: "56px"
  feature-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
  spec-table-row:
    padding: "{spacing.sm} {spacing.base}"
    borderBottom: "1px solid {colors.hairline-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  footer-heading:
    color: "{colors.canvas}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    padding: "{spacing.base}"
    typography: "{typography.title-sm}"
  accordion-content:
    padding: "{spacing.base}"
    typography: "{typography.body-sm}"
  loading-spinner:
    color: "{colors.primary}"
    size: "32px"
  error-message:
    backgroundColor: "{colors.badge-error-bg}"
    textColor: "{colors.badge-error-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  success-message:
    backgroundColor: "{colors.badge-success-bg}"
    textColor: "{colors.badge-success-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  warning-message:
    backgroundColor: "{colors.badge-warning-bg}"
    textColor: "{colors.badge-warning-text}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Configure Now", and primary checkout flows. Rendered in {colors.primary} (#003399) with white text and {rounded.sm} corners, it carries a 14px uppercase Montserrat weight-600 label with 0.5px letter-spacing. On hover, the background shifts to {colors.primary-active} (#002266); the disabled state uses {colors.primary-disabled} (#bacbe6) with reduced opacity. **`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "Compare Models". Uses a white background with a 2px {colors.ink} border, matching the primary button's height and typography. On hover, the background fills with {colors.ink} and text inverts to white. **`button-ghost`** — A text-only button for tertiary actions within cards and modals. Transparent background with {colors.ink} text; hover reveals a {colors.surface-soft} background. **`button-accent-green`** and **`button-accent-red`** — Functional buttons for status-related actions (e.g., "In Stock" confirmation, "Remove" in cart). Smaller at 36px height with {typography.button-sm} sizing, using {colors.accent-green} and {colors.accent-red} respectively.

### Cards
**`product-card`** — The core product display unit, a white card with a 1px {colors.hairline-soft} border and {rounded.md} corners. The image occupies the top with a 4:3 aspect ratio and rounded top corners only. Below, the title uses {typography.title-sm} and the price uses {typography.price} (24px weight-600). On hover, the border strengthens to {colors.hairline} and a subtle box-shadow lifts the card. An optional **`product-card-badge`** sits absolutely positioned at the top-left, using {colors.primary} background with white uppercase badge text. **`feature-badge`** — A pill-shaped tag for highlighting product features like "German Engineering" or "5-Year Warranty". Uses {colors.surface-soft} background with {typography.caption} uppercase styling and {rounded.full} corners.

### Navigation
**`nav-bar`** — A fixed 72px white bar with a subtle bottom border in {colors.hairline-soft}. Navigation links use {typography.nav-link} (13px uppercase Montserrat weight-500 with 0.5px letter-spacing). Active links render in {colors.primary}, inactive in {colors.body}. The logo sits left-aligned at 32px height. On scroll, the bar gains a sticky class with a stronger {colors.hairline} border. **`nav-link-active`** and **`nav-link-inactive`** — Define the active and inactive states for navigation items, with the active state using {colors.primary} for emphasis.

### Forms
**`text-input`** — Standard input field with white background, {colors.ink} text, and a 1px {colors.hairline} border. Focus state thickens the border to 2px {colors.primary}. Error state uses 2px {colors.accent-red}. Height is 48px with 12px 16px padding. **`select-input`** — Matches the text input dimensions and styling, used for configuration dropdowns (e.g., chair color, material).

### Hero
**`hero-section`** — A full-width section with a {colors.hero-overlay} (#141414) background, minimum 600px height, and generous section padding. The title uses {typography.display-xl} (48px weight-600) in white, with a subtitle in {typography.display-sm} (22px) in {colors.muted-soft}. The hero CTA button is larger at 56px height with 16px 40px padding, using {colors.primary} background.

### Footer
**`footer`** — A dark section using {colors.ink} background with {colors.muted-soft} text. Links use {typography.link} and hover to white. Section headings use {typography.title-sm} with uppercase transformation. Padding is generous at {spacing.xxl} horizontally and {spacing.lg} vertically.

### Feedback Messages
**`error-message`**, **`success-message`**, **`warning-message`** — Alert banners using the corresponding badge background/text color pairs. Each uses {typography.body-sm} with {rounded.sm} corners and {spacing.md} {spacing.base} padding. These appear for form validation, cart updates, and stock notifications.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hero section reduces to 400px min-height; product cards stack in single column; nav-bar collapses to hamburger menu; typography scales down (display-xl becomes 32px); footer links stack vertically |
| Tablet | 744–1128px | Two-column product grid; hero maintains 500px min-height; nav links remain visible but reduce font size to 12px; side-by-side spec tables |
| Desktop | 1128–1440px | Three-column product grid; full hero at 600px; all nav links visible; spec tables with full padding |
| Wide | > 1440px | Max-width container at 1440px; hero content centered with 1200px max-width; product grid can expand to four columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets extend to full card area
- Mobile hamburger menu icon is 48px x 48px
- Accordion headers are 48px minimum tap height
- Filter checkboxes and radio buttons are 24px x 24px with 44px tap padding

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Footer link columns stack vertically below 744px
- Hero content text reduces to single column below 744px
- Spec tables convert to stacked rows on mobile
- Accordion replaces tabbed content on mobile
- Secondary navigation (sub-categories) collapses to a select dropdown below 744px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex colors are heavily polluted with Bootstrap utility classes and Shopify widget colors — the true brand palette likely has fewer, more intentional colors. The primary #003399 and ink #141414 are confident picks; the remaining greens, reds, golds, and blues may be functional or framework defaults.
- No extracted hover states, focus rings, or active states for any component — these are inferred from common patterns.
- Font weights beyond the extracted "Montserrat" stack are assumed (400, 500, 600) — actual usage may include 700 for display.
- No dark mode variant detected — the site appears to be light-mode only with a dark hero section.
- Animation and transition durations are not extracted — a standard 200-300ms ease-in-out is assumed.
- No extracted data for modal, tooltip, or dropdown component styling.
- The extracted #d63384 (pink) and #0d6efd (Bootstrap blue) are almost certainly framework/widget artifacts and should not be used as brand colors.
- No extracted spacing or rounded values — these are inferred from common e-commerce patterns and may differ from actual implementation.
- No extracted typography scale beyond the font-family declaration — sizes, weights, and line-heights are estimated based on industry standards for the gaming/peripheral market.
