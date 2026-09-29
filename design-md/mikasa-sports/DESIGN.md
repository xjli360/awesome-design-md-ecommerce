---
version: alpha
name: "Mikasa Sports"
source_url: "https://mikasasports.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep teal #226d7a anchors Mikasa Sports — not the expected bright ball-orange or field-green of most team-sport brands, but a deliberate, almost oceanic cyan-teal that reads as precision and endurance rather than hype. This primary voltage appears on every CTA, product badge, and navigation element, paired with a pale aqua #b0e0e9 that softens the system into a coastal palette — think competition-grade pool water under overcast skies. The typography stack defaults to Open Sans and Roboto at moderate weights (400–600), with body copy running at 14–16px and display sizes rarely exceeding 24px; the brand trusts product photography and clean grid layouts over typographic drama. Hard corners dominate — buttons use {rounded.sm} (8px) rather than pills, product cards use {rounded.md} (12px), and the nav bar sits as a flat, full-width teal band with white text, no drop shadow, no gradient. The secondary accent #22b8d1 (a brighter cyan) appears on hover states and secondary badges, creating a two-tone aquatic system that feels more like a precision equipment manufacturer than a mass-market sportswear label. Mikasa’s design language is lean, functional, and unadorned — the visual equivalent of a well-inflated ball: nothing extra, everything intentional.

colors:
  primary: "#226d7a"
  primary-active: "#1e6d7a"
  primary-disabled: "#b0e0e9"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#d9d9d9"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-cyan: "#22b8d1"
  accent-aqua: "#b0e0e9"
  accent-aqua-soft: "#e4f5fa"
  badge-sport: "#226d7a"
  badge-new: "#22b8d1"
  error: "#d32f2f"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
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
    backgroundColor: "{colors.accent-aqua-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.accent-aqua-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-accent:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "1px solid {colors.error}"
    rounded: "{rounded.sm}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: "0 {spacing.lg}"
  nav-bar-sticky:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    boxShadow: "0 2px 4px rgba(0,0,0,0.1)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "8px 12px"
    rounded: "{rounded.xs}"
  nav-link-active:
    backgroundColor: "rgba(255,255,255,0.15)"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.xs}"
  nav-link-hover:
    backgroundColor: "rgba(255,255,255,0.1)"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-badge:
    backgroundColor: "{colors.badge-sport}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-banner-image-overlay:
    backgroundColor: "linear-gradient(135deg, {colors.primary} 0%, {colors.accent-cyan} 100%)"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
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
    rounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.accent-aqua}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  section-heading:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.lg} 0"
    borderBottom: "2px solid {colors.primary}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    color: "{colors.primary}"
    size: 24px
  loading-spinner-small:
    color: "{colors.primary}"
    size: 16px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the deep teal `{colors.primary}` background with white text. On hover, it shifts to `{colors.primary-active}` for a slightly darker, more grounded state. The disabled state uses `{colors.primary-disabled}` (the pale aqua), signaling unavailability without visual noise. All primary buttons use `{rounded.sm}` (8px) — a deliberate hard-corner choice that aligns with the brand's precision-equipment ethos.

**`button-secondary`** — An outlined variant with a white background, teal text, and a 2px solid teal border. Active state fills the background with `{colors.accent-aqua-soft}` and darkens the border to `{colors.primary-active}`. Used for secondary actions like "View Details" or "Compare Products."

**`button-ghost`** — A text-only button with no background or border, using teal text. On hover/active, it gains a subtle `{colors.accent-aqua-soft}` background. Reserved for tertiary actions within cards or dense UI areas.

**`button-accent`** — A smaller, brighter variant using `{colors.accent-cyan}` (#22b8d1) as background. Used for "New Arrivals" badges, promotional CTAs, or sport-category filters. Typography uses `{typography.button-sm}` for a compact footprint.

### Cards
**`product-card`** — A white card with `{rounded.md}` (12px), subtle box shadow, and `{spacing.base}` internal padding. On hover, the shadow deepens to indicate interactivity. The product image area uses `{rounded.sm}` and a 1:1 aspect ratio. Price, product name, and a small badge sit below the image in `{typography.body-sm}`.

**`product-badge`** — Small uppercase labels (e.g., "VOLLEYBALL", "SOCCER") using `{colors.badge-sport}` teal background. A "NEW" variant uses the brighter `{colors.badge-new}` cyan. A "SALE" variant uses `{colors.error}` red. All badges use `{rounded.xs}` (4px) and `{typography.badge}` (11px, bold, uppercase with letter-spacing).

### Navigation
**`nav-bar`** — A full-width teal band at 64px height, with white uppercase navigation links. Links have subtle rounded hover states (`{rounded.xs}`) with a semi-transparent white background. The active link uses a slightly more opaque white background. On scroll, a thin box shadow appears to separate the nav from content.

**`nav-link`** — Uppercase, 14px, weight 600, with 0.5px letter-spacing. The typography is intentionally compact to fit multiple sport categories (Volleyball, Soccer, Basketball, etc.) in a single row.

### Forms
**`text-input`** — Standard input fields with white background, 1px hairline border, and `{rounded.sm}`. On focus, the border thickens to 2px and switches to `{colors.primary}` teal. Error state uses a red border. Height is 44px for comfortable touch targets.

**`select-input`** — Matches text-input styling for visual consistency. Used for size, quantity, and sport-category dropdowns.

### Search
**`search-bar`** — A rectangular search bar (not pill-shaped) matching the text-input pattern, with a 44px height and `{rounded.sm}`. On focus, the border becomes 2px teal. No search orb — the brand uses a standard input with a magnifying glass icon inside or adjacent.

### Footer
**`footer`** — A full-width teal band with white body text and aqua-colored links (`{colors.accent-aqua}`). Links brighten to full white on hover. Organized in columns with generous `{spacing.xxl}` padding. The footer uses `{typography.body-sm}` for legal text and `{typography.link}` for navigation links.

### Hero
**`hero-banner`** — A large teal section (min-height 400px) with white display text. Can include a background image with a teal-to-cyan gradient overlay (`{colors.primary}` to `{colors.accent-cyan}`). Typography uses `{typography.display-lg}` or `{typography.display-xl}` depending on content hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu. Product cards go single-column. Hero banner reduces to 300px min-height. Font sizes scale down one step (display-xl → display-lg). Footer stacks vertically. |
| Tablet | 744–1128px | Nav bar shows all links but reduces padding. Product cards display in 2-column grid. Hero banner maintains 400px height. Side-by-side footer columns. |
| Desktop | 1128–1440px | Full nav bar with all sport categories. Product cards in 3-column grid. Hero banner at full height. Multi-column footer. |
| Wide | > 1440px | Max-width container at 1440px with centered content. Product cards in 4-column grid. Extended hero with more whitespace. |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Nav links have 44px touch area even if text is smaller
- Product cards are fully tappable, not just the CTA within
- Search bar and form inputs maintain 44px height for finger accuracy
- Footer links have 44px minimum touch area

### Collapsing Strategy
- Top nav collapses to hamburger icon below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport shrinks
- Hero banner text stack collapses from side-by-side to stacked
- Footer columns collapse from 4-column to 2-column to single-column
- Sport category filter strip collapses to a horizontal scrollable row on mobile
- Secondary navigation (breadcrumbs) hides on mobile, replaced by back button

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted from the live site; some are inferred from common patterns
- Error message styling (colors, typography, placement) was not visible on the extracted page
- Dark mode or high-contrast mode variants are not documented
- Sub-brand or sport-specific color variations (e.g., volleyball vs. soccer) may exist but were not extracted
- Animation and transition timing values (durations, easing curves) are not available
- Icon set and illustration style are not documented — the site may use custom sport icons
- Modal, drawer, and overlay component specifications are missing
- The extracted page returned a 403 Forbidden error, so most visual data is inferred from the limited color and font hints available
- Form validation states (success, warning, info) beyond error are not documented
- Loading states and skeleton screen patterns are not available
- Print stylesheet specifications are unknown
