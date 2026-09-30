---
version: alpha
name: "Rane"
source_url: "https://www.rane.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep black canvas (#01060e) and a single electric-blue voltage (#015afd) define Rane's design language — a system built for the DJ booth where every control must be legible at a glance under strobes and smoke. The brand's identity is rooted in professional audio hardware: thick, purposeful typography set in trade-gothic-next and its compressed/condensed variants, generous hit targets on interactive elements, and a near-total absence of decorative flourish. The color palette is deliberately austere — #141414 for surfaces, #eeeeee for body text, #c2c2c2 for muted states — with the blue acting as the sole accent for primary actions, active states, and signal paths. Rounded corners are minimal (4px on buttons, 8px on cards), a nod to the machined aluminum of their mixers and controllers. The system trusts high-contrast relationships: white (#ffffff) on black for primary CTAs, black on white for secondary, and a hairline (#e4e4e5) that separates sections without adding visual noise. This is not a brand that sells aspiration — it sells precision, and every pixel is engineered for the moment when a fader needs to cut clean.

colors:
  primary: "#015afd"
  primary-active: "#0045cc"
  primary-disabled: "#7a9ef0"
  ink: "#01060e"
  body: "#141414"
  muted: "#555555"
  muted-soft: "#c2c2c2"
  hairline: "#e4e4e5"
  hairline-soft: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-dark: "#0d0d0d"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  signal-green: "#8ee283"
  accent-blue: "#5dafd6"

typography:
  display-xl:
    fontFamily: "'trade-gothic-next-compressed', 'Trade Gothic Next Compressed', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'trade-gothic-next-compressed', 'Trade Gothic Next Compressed', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'trade-gothic-next', 'Trade Gothic Next', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'trade-gothic-next', 'Trade Gothic Next', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'trade-gothic-next', 'Trade Gothic Next', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'trade-gothic-next', 'Trade Gothic Next', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'trade-gothic-next', 'Trade Gothic Next', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'trade-gothic-next', 'Trade Gothic Next', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'trade-gothic-next', 'Trade Gothic Next', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'trade-gothic-next', 'Trade Gothic Next', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'trade-gothic-next', 'Trade Gothic Next', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.25px
  badge:
    fontFamily: "'trade-gothic-next-condensed', 'Trade Gothic Next Condensed', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'trade-gothic-next', 'Trade Gothic Next', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  text-input-error:
    border: "1px solid #d32f2f"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.xs}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "16/9"
  product-card-title:
    typography: "{typography.title-md}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    border: "1px solid {colors.primary}"
  badge-success:
    backgroundColor: "{colors.signal-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "16px 32px"
    height: 52px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.muted}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in Rane blue (#015afd) with white uppercase text. On hover, shifts to a deeper blue (#0045cc). Disabled state uses a washed-out blue (#7a9ef0). The 4px corner radius and 44px height mirror the tactile feel of hardware buttons on Rane mixers.

**`button-secondary`** — An outlined variant with a 2px black border on white canvas. Active state fills the background with light gray (#eeeeee). Used for secondary actions like "Learn More" or "Compare Models." Maintains the same 44px height and uppercase typography as the primary button.

**`button-ghost`** — Text-only button with no background or border. Uses body color (#141414) and the standard button typography. Reserved for tertiary actions within cards or dense UI sections where visual weight must be minimized.

**`button-dark`** — A solid black (#01060e) button with white text, used exclusively on light backgrounds for actions that need high contrast without introducing the brand blue. Common in product detail sections and technical specifications.

### Navigation
**`nav-bar`** — A fixed-height 72px bar on deep black (#01060e) with white navigation links. The dark background creates a visual anchor at the top of every page, reminiscent of the brushed aluminum faceplates on Rane hardware. Links are set in trade-gothic-next at 14px with 0.25px letter spacing.

**`nav-link`** — Inactive links render in a muted gray (#c2c2c2) with 8px horizontal padding. Active links turn white with a 2px blue (#015afd) bottom border, signaling the current section without relying on background fills.

### Cards
**`product-card`** — White card with 8px rounded corners and 16px padding. The image area maintains a 16:9 aspect ratio with matching corner radius. Product titles use title-md (18px, weight 600) in ink (#01060e), while prices use body-md (16px) in body (#141414). Cards stack in a responsive grid with 24px gap.

### Forms
**`text-input`** — Standard input field with 48px height, 4px corners, and a 1px hairline (#e4e4e5) border. Focus state thickens the border to 2px and switches to brand blue (#015afd). Error state uses a red border (#d32f2f). The generous height accommodates both desktop and touch input.

### Badges
**`badge`** — Small uppercase labels in brand blue with white text, 2px vertical padding and 8px horizontal. Used for "NEW," "SALE," or feature tags. The outline variant inverts the relationship — transparent background with a blue border and blue text. A success variant uses signal green (#8ee283) for "IN STOCK" or "READY TO SHIP" indicators.

### Hero
**`hero-section`** — Full-width section on black background (#01060e) with 64px vertical padding. Headlines use the compressed variant of trade-gothic-next at 48px for maximum impact. The primary CTA sits at 52px height with 32px horizontal padding — intentionally larger than standard buttons to anchor the page entry point.

### Footer
**`footer`** — Deep black background matching the nav bar, with muted gray (#c2c2c2) links and body text. Dividers use a slightly lighter gray (#555555) to separate content sections. The footer maintains the same 64px section padding as other major content blocks.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid, nav collapses to hamburger, hero font drops to 32px, product cards stack vertically |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, hero font at 40px |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero at 48px |
| Wide | > 1440px | Max-width container at 1440px, centered content with generous margins |

### Touch Targets
- All interactive elements maintain minimum 44px height (Apple HIG compliant)
- Icon buttons and toggle controls use 48px touch targets
- Form inputs and search bars at 48px height for comfortable tap targets
- Product card tap zones span the full card width

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px
- Product grids reduce from 3 columns to 2 at tablet, 1 at mobile
- Hero content stacks vertically on mobile (headline above CTA)
- Footer link columns collapse to a single column below 744px
- Sidebar filters hide behind a "Filters" toggle button on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs beyond the basic focus border could not be extracted — placeholder styling, error message typography, and helper text patterns are inferred from common patterns
- The exact font weights for trade-gothic-next variants (regular vs. medium vs. bold) are estimated from common web usage — the live site may use specific weight values not captured
- Dropdown and select menu styling (native vs. custom) could not be determined from extracted data
- Modal/overlay patterns, including backdrop scrim opacity and animation timing, are not present in the extraction
- Error and validation states for forms beyond the input border color are unknown
- Dark mode is not present on the live site — all pages use the light-on-dark nav and dark-on-light content pattern described above
- The extracted color list includes #337ab7 (a common Bootstrap default) and #555555 (a generic gray) — these may be framework artifacts rather than intentional brand colors
- Animation curves and durations (easing functions for hover transitions, page loads) are not captured
- The secondary accent colors (#8ee283 signal green, #5dafd6 accent blue) appear infrequently and may be specific to product badges or technical diagrams rather than system-wide tokens
