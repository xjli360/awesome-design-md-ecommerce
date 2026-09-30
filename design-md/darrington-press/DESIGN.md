---
version: alpha
name: "Darrington Press"
source_url: "https://darringtonpress.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep indigo #003388 anchors Darrington Press as the primary brand voltage — a color that reads as midnight library cloth, not corporate blue — and it carries every primary CTA, navigation link, and footer block across the site. The palette is deliberately restrained: a near-black #2f2f2f for body text, a softer #242429 for secondary copy, and a warm off-white #e6e7e0 for the canvas that gives the whole experience a paper-stock feel rather than a sterile digital white. Accents arrive sparingly: a bright amethyst #6c1cff for hover states and secondary buttons, a marigold #f0b849 for badge highlights and sale markers, and a muted lavender #c4b7c8 that surfaces in dividers and subtle backgrounds. Typography runs system-native — the site trusts the user's OS stack (San Francisco, Roboto, Open Sans) at modest weights, with body text at 16px and a generous 1.6 line height that mimics the comfortable leading of a printed rulebook. Cards use soft {rounded.sm} corners, while CTAs and badges take {rounded.md} — nothing is pill-shaped, preserving a slightly formal, bookish character. The layout is a single-column spine on mobile, expanding to a two-column grid on desktop with a persistent left-hand navigation that echoes a table of contents. There is no hero carousel, no full-bleed photography; instead, product imagery sits inside bordered cards with {rounded.sm} corners, and every link carries an underline on hover rather than a color shift. The overall effect is that of a publishing house's digital reading room — quiet, legible, and built for long sessions of browsing game titles and lore.

colors:
  primary: "#003388"
  primary-active: "#6c1cff"
  primary-disabled: "#a6b1ff"
  ink: "#2f2f2f"
  body: "#242429"
  muted: "#43454b"
  muted-soft: "#abb8c3"
  hairline: "#c4b7c8"
  hairline-soft: "#d0ba8e"
  canvas: "#e6e7e0"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-marigold: "#f0b849"
  accent-amethyst: "#6c1cff"
  accent-lavender: "#c4b7c8"
  badge-new: "#cc1818"
  badge-sale: "#f0b849"
  link-underline: "#003388"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
  button-primary-hover:
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
    border: "2px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-tertiary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-new}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
    textDecoration: underline
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with deep indigo `#003388` and white text. On hover, it shifts to amethyst `#6c1cff`, creating a clear state change. Disabled state uses a muted lavender `#a6b1ff` with white text. All variants share `{rounded.sm}` corners and 44px height for consistent tap targets.

**`button-secondary`** — An outlined variant on the warm off-white canvas `#e6e7e0`, with a 2px indigo border. Hover fills the button with the primary indigo, inverting the color relationship. Used for "Learn More" and secondary actions alongside primary buttons.

**`button-tertiary`** — A text-only button with indigo text and no background. Hover adds a soft surface background `#f7f7f7` and shifts text to amethyst. Used for "Cancel" actions and inline links styled as buttons.

### Cards
**`product-card`** — White card with `{rounded.sm}` corners and 16px padding. Contains a product image with `{rounded.xs}`, title, price, and optional badges. On hover, a subtle box shadow lifts the card. The card body uses `{typography.body-sm}` for descriptions and `{typography.title-sm}` for product names.

**`product-card-image`** — The image container within a product card, using `{rounded.xs}` for a slight rounding that contrasts with the card's larger corner radius. Images are typically 3:4 aspect ratio for game boxes.

### Navigation
**`nav-bar`** — A 64px tall bar on the warm off-white canvas, containing the brand logo and navigation links. Links use `{typography.nav-link}` at 15px with 0.2px letter spacing. The active link gains a 2px indigo bottom border and indigo text; inactive links are muted gray `#43454b`.

**`nav-link-active`** / **`nav-link-inactive`** — Active state uses indigo text with an underline border; inactive uses muted gray. No background changes — the brand relies on color and underline for state differentiation.

### Forms
**`text-input`** — White input field with a 1px lavender `#c4b7c8` border and `{rounded.sm}` corners. On focus, the border thickens to 2px indigo. Error state uses a 2px red `#cc1818` border. All inputs are 44px tall with 12px horizontal padding.

**`search-bar`** — Similar to text-input but with a search icon inset. Uses the same 44px height and `{rounded.sm}` corners. Focus state mirrors the text-input pattern with a 2px indigo border.

### Badges
**`badge-new`** — A small red `#cc1818` badge with uppercase white text, used to mark newly released games. `{rounded.xs}` corners keep it compact at 2px vertical padding.

**`badge-sale`** — A marigold `#f0b849` badge with dark text, used for sale items and promotions. Same sizing and typography as the new badge, but with a warm, attention-grabbing color.

### Footer
**`footer-link`** — Muted gray `#43454b` text links with no underline by default. On hover, they turn indigo and gain an underline. The footer uses a darker background variant of the canvas, with links stacked vertically in columns.

**`divider`** / **`divider-soft`** — Horizontal rules at 1px height. The standard divider uses lavender `#c4b7c8`; the soft variant uses a warmer beige `#d0ba8e` for less visual weight in content areas.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; search bar moves below nav; footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid; nav remains horizontal but condensed; sidebar navigation appears on left for category pages |
| Desktop | 1128–1440px | Full two-column layout with persistent left nav; three-column product grid; search bar in top nav; footer expands to four columns |
| Wide | > 1440px | Max-width container at 1440px; content centered; left nav remains fixed; product grid expands to four columns |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Search bar and text inputs use 44px height
- Navigation links have 48px tap area (64px nav bar with centered links)
- Badges are minimum 20px height with 8px padding for tap targets
- Footer links use 36px minimum tap area

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Left sidebar navigation collapses to a dropdown or off-canvas drawer below 744px
- Product grids collapse from 4 columns to 2 columns on tablet, to single column on mobile
- Footer columns collapse from 4 to 2 on tablet, to single column on mobile
- Search bar collapses from inline to full-width below 744px, appearing below the nav

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is unusually large (30+ hex values) and likely includes checkout-widget colors (Klarna, Afterpay), social-icon colors, and stock-image dominant tones. The true brand palette was inferred from the most frequently occurring and distinctive colors (#003388, #2f2f2f, #e6e7e0, #6c1cff, #f0b849, #c4b7c8). Several colors (#ff0000, #360309, #1d0210, #3b003b) appear to be image-dominant or edge-case colors and were excluded.
- No custom font family was detected — the site relies entirely on system font stacks. The brand may use a custom typeface that is loaded via JavaScript or a CDN not captured in the CSS extraction.
- Hover states for all components are inferred from common patterns (color shift, underline, shadow) rather than extracted from live CSS.
- Error states for forms (validation messages, error icons) are not documented.
- Dark mode support is unknown — the palette is optimized for a warm off-white canvas.
- Sub-brand or product-line color variations (e.g., specific game series) are not captured.
- Animation timing, easing curves, and transition durations are not documented.
- The extracted font-family list includes WooCommerce and Pe-icon-7-stroke, suggesting the site may use a WordPress/WooCommerce backend, but this is not reflected in the design system.
- Meta theme-color was not present in the extracted hints, so the browser chrome color is unknown.
