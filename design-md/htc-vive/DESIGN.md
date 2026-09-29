---
version: alpha
name: "HTC Vive"
source_url: "https://www.vive.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue-violet anchor at #3a4570 grounds a VR ecosystem that lives in the tension between deep tech and human wonder — the extracted palette reads like a control room at dusk, with #c4c8d8 and #e3e5ec as cool silver-grey walls, #0096db and #00b3e3 as live data streams, and #ff9900 as the single alert-status accent that punches through the blues. Roboto runs the interface in clean, unadorned weights — no display-serif flourish, no decorative gesture — because the hardware is the spectacle and the UI must disappear. Buttons carry {rounded.sm} corners that feel precise rather than pill-soft, and the primary action sits in #0096db, a cyan that reads as "connected" against the navy of #3a4570. The secondary palette introduces #f17b4f and #d43430 as purchase or urgency signals, while #ffc168 and #aaaaaa handle badges and secondary metadata. This is not a friendly consumer brand — it is an instrument panel for immersive computing, where every hex serves legibility and system status at a glance.

colors:
  primary: "#0096db"
  primary-active: "#0073a8"
  primary-disabled: "#a5aed1"
  ink: "#2c3a50"
  body: "#3a4570"
  muted: "#596677"
  muted-soft: "#878faf"
  hairline: "#c4c8d8"
  hairline-soft: "#dfe2ee"
  canvas: "#ffffff"
  surface-soft: "#e3e5ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-alert: "#ff9900"
  accent-warm: "#f17b4f"
  accent-error: "#d43430"
  accent-badge: "#ffc168"
  nav-deep: "#3a4570"
  nav-active: "#495588"
  link-cyan: "#2c9cdb"
  border-strong: "#a5abc4"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  link:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Roboto', 'Noto Sans JP', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 6px
  md: 12px
  lg: 20px
  xl: 28px
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
    border: "2px solid {colors.hairline}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.hairline}"
  button-accent:
    backgroundColor: "{colors.accent-alert}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.nav-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: "{colors.nav-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
  nav-link-hover:
    backgroundColor: "{colors.nav-active}"
    textColor: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(44,58,80,0.08)"
  hero-section:
    backgroundColor: "{colors.nav-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  badge-new:
    backgroundColor: "{colors.accent-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-spec:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  footer-section:
    backgroundColor: "{colors.nav-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.link-cyan}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  stepper-indicator:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 32px
  stepper-indicator-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    fontWeight: 600

## Components

### Buttons
**`button-primary`** — The primary call-to-action for purchase flows and key actions. Uses #0096db fill with white text and a 6px corner radius. On hover, darkens to #0073a8; disabled state drops to #a5aed1. Height is 44px with 12px/24px padding, using Roboto 600 at 15px with 0.3px letter spacing for a slightly technical, precise feel.

**`button-secondary`** — Outlined alternative for secondary actions like "Learn More" or "Compare Models". White background with a 2px #c4c8d8 border and ink text. Active state fills the background with #e3e5ec. Same 44px height and typography as primary.

**`button-accent`** — High-visibility action using #ff9900 (alert orange) for limited-time offers, pre-order prompts, or warranty upsells. Same dimensions as primary but with darker ink text for contrast.

**`button-ghost`** — Text-only button for tertiary actions like "Cancel" or "View Details". Transparent background, body-colored text, and 12px/16px padding. No border or fill until hover, where a subtle background shift would occur.

### Cards
**`product-card`** — White card with 12px rounded corners and a soft #dfe2ee border. Contains product imagery, title, spec badges, and price. On hover, the border darkens to #c4c8d8 and a subtle shadow lifts the card. Padding inside is 16px base spacing.

**`hero-section`** — Full-width banner anchored on #3a4570 navy with white text. Uses display-xl (32px/700) for headlines and a single primary CTA button. Section padding is 64px vertical, 32px horizontal.

### Navigation
**`nav-bar`** — Deep navy (#3a4570) top bar at 64px height. Navigation links are uppercase Roboto 500 at 14px with 0.5px tracking. Active link gets a #495588 background; hover matches. No rounded corners — the bar is a hard horizontal line.

**`nav-link-active`** — Active state for nav items. Background shifts to #495588, text stays white. No border or underline — the color change alone signals location.

### Forms
**`text-input`** — Standard input field with white background, 6px corners, and a 1px #c4c8d8 border. On focus, the border becomes 2px #0096db. Height is 44px with 10px/14px padding. Uses body-md Roboto for entered text.

### Badges
**`badge-new`** — Warm amber (#ffc168) badge for "New" or "Just Released" labels. Uppercase Roboto 700 at 11px with 0.5px tracking. 2px/8px padding, 2px corner radius. Ink text for contrast.

**`badge-sale`** — Red (#d43430) badge for sale or discount indicators. White text, same typography and dimensions as badge-new.

**`badge-spec`** — Neutral grey (#e3e5ec) badge for technical specs like "6GB RAM" or "120Hz". Muted text, caption typography, 4px/10px padding.

### Footer
**`footer-section`** — Deep navy (#3a4570) footer with white body-sm text. Links use #2c9cdb cyan and shift to white on hover. Section padding is 48px vertical, 32px horizontal.

### Spec Table
**`spec-table-row`** — Alternating rows for product specification tables. White background with a 1px #dfe2ee bottom border. Body-sm typography. Header rows use #e3e5ec background with title-sm weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; hero text reduces to display-lg; product cards stack vertically; spec tables scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero retains display-xl but with reduced padding |
| Desktop | 1128–1440px | Full three-column grid; expanded nav with all links; spec tables display inline |
| Wide | > 1440px | Max-width container at 1440px; hero section scales background imagery; product cards use 4-column grid |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height
- Nav links on mobile expand to 48px tap targets
- Product card CTAs are full-width on mobile for easy tapping
- Badges remain at minimum 20px height for touch

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product filter sidebar (if present) becomes a bottom sheet on mobile
- Spec tables collapse to stacked key-value pairs below 744px
- Footer link columns collapse to single column below 744px
- Hero section reduces vertical padding from 64px to 32px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and links are inferred from common patterns; exact extracted hover hexes were not available from the static extraction
- Error states for text inputs (border color, error message styling) not extracted
- Dark mode palette not present on the live site; no dark theme tokens available
- Sub-brand colors for VIVE Focus, VIVE Pro, or VIVE XR Elite not distinguishable in the extracted palette
- Font weight distribution across the typography system is inferred from Roboto's standard weights; exact weight usage per component not extracted
- The extracted palette includes #46aeda and #aaaaaa which may be Shopify widget or social icon colors rather than brand colors
- Animation timing, transition curves, and hover duration not extracted
- Dropdown menu styling (background, shadow, z-index) not available
- Modal/overlay styling (scrim opacity, close button position) not extracted
- The Japanese market site (vive.com/jp) may have different color or typography preferences; this design system is based on the global extraction
