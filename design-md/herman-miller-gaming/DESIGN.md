---
version: alpha
name: "Herman Miller Gaming"
source_url: "https://www.hermanmiller.com/gaming"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A red alert (#d74039) against a near-white field (#fafafa) — the brand's primary voltage is an urgent, automotive-grade crimson that appears nowhere in the Herman Miller office-furniture palette. This is the signal that the gaming line is a different machine: darker, faster, built for extended sessions rather than conference-room meetings. The extracted palette runs from near-black (#1b1b1b) through charcoal (#252525) to warm grays (#616161, #c6c6c6, #e4e4e4, #ebebeb), with a secondary red (#e22d00) and a deep burgundy (#8a223b) that suggest a racing stripe or a cockpit accent. Söhne, the typeface, carries the whole system — a geometric sans with moderate contrast that reads as precise without being cold. Buttons use {rounded.sm} (8px) corners, not the pill shapes of consumer gaming peripherals; the brand trusts a sharper, more architectural edge. The canvas is white (#fafafa), not black, which creates a surprising tension: the reds and charcoals pop harder against a bright ground than they would against a dark one. This is a gaming brand that refuses to look like a gaming brand — no neon, no gradients, no cyberpunk. Just red, white, and black, with Söhne doing the talking.

colors:
  primary: "#d74039"
  primary-active: "#e22d00"
  primary-disabled: "#ebebeb"
  ink: "#1b1b1b"
  body: "#252525"
  muted: "#616161"
  muted-soft: "#c6c6c6"
  hairline: "#e4e4e4"
  hairline-soft: "#ebebeb"
  canvas: "#fafafa"
  surface-soft: "#fafafa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e22d00"
  accent-burgundy: "#8a223b"
  accent-bright-red: "#ff3d3d"

typography:
  display-xl:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.5px
  link:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Söhne, arial, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "4/3"
  product-card-content:
    padding: "{spacing.base} {spacing.base} {spacing.lg}"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.display-md}"
    color: "{colors.body}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "2px solid {colors.ink}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "2px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  section-divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  color-swatch-primary:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  color-swatch-burgundy:
    backgroundColor: "{colors.accent-burgundy}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  color-swatch-ink:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 32px
    width: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Configure", and "Shop Now" actions. Renders as a solid red (#d74039) rectangle with 8px corners and white Söhne text at 15px/500 weight. On hover, shifts to a brighter red (#e22d00). Disabled state uses the lightest gray (#ebebeb) with muted text (#616161) — no red visible at all, signaling the action is unavailable.

**`button-secondary`** — An outlined alternative for secondary actions like "Learn More" or "View Details". Uses a white fill with a 2px black (#1b1b1b) border. Hover state darkens the background to near-white (#fafafa). Same 48px height and 8px corners as the primary button, maintaining visual rhythm.

**`button-tertiary`** — A text-only button for subtle actions like "Cancel" or "Clear Filters". No background, no border — just Söhne 15px/500 in black. Hover adds a near-white (#fafafa) background. Used where a full button would compete with the primary CTA.

**`button-pill-primary`** — A smaller, fully rounded variant reserved for filter tags, category pills, and compact actions. Uses the primary red with white text at 13px/500. The pill shape (`{rounded.full}`) distinguishes it from the standard 8px-corner buttons.

**`button-pill-outline`** — The outlined companion to the pill primary, used for inactive filter states and deselected options. Transparent fill with a thin gray (#e4e4e4) border.

### Navigation
**`top-nav`** — A fixed 64px bar on a white canvas (#fafafa) with a single-pixel bottom border (#e4e4e4). Navigation links are set in Söhne 14px/500 with 0.5px letter spacing and uppercase — a deliberate choice that reads as more editorial than gaming. The active link switches to the primary red (#d74039). The logo sits left, links center, and utility icons (search, cart, account) right.

**`nav-link`** — Uppercase Söhne 14px/500 with 0.5px tracking. Padding of 8px top/bottom and 16px left/right. Active state inherits `{colors.primary}`. No underline, no background — just color change.

### Cards
**`product-card`** — The primary product presentation unit, used on collection pages and search results. A white card with 8px corners and no border — the image provides the edge. The image area occupies the top 4:3 ratio with rounded top corners only. Below, content padding of 16px sides and 24px bottom. Title uses Söhne 16px/500, price uses 16px/400. A small red badge (`{rounded.xs}`, 4px padding) can overlay the image for "New" or "Sale" indicators.

**`product-card-badge`** — A compact 11px/600 uppercase label in white on red (#d74039). 4px corners, 4px/8px padding. Used sparingly — only for "New", "Sale", or "Exclusive" flags. The small size keeps it from competing with the product image.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. White background, 16px Söhne body text, 8px corners, 48px height. Default state has a 1px gray (#e4e4e4) border. Focus state thickens to 2px black (#1b1b1b). Error state uses 2px red (#d74039). Padding of 12px vertical and 16px horizontal.

**`select-dropdown`** — Matches the text-input dimensions and styling: 48px height, 8px corners, 1px gray border. Uses the same 16px/400 Söhne body text. The dropdown arrow is rendered as a custom icon, not the browser default.

### Hero
**`hero-section`** — Full-width white (#fafafa) section with 64px vertical padding. The headline uses 48px/700 Söhne with -1px letter spacing — the most dramatic type treatment in the system. Subheadline at 28px/600. A single primary CTA button sits below. No background image or gradient — the hero relies on product photography placed beside or behind the text.

### Footer
**`footer`** — The only dark section in the system, using a near-black (#1b1b1b) background with white (#fafafa) text. Links are set in Söhne 14px/400 in a warm gray (#c6c6c6), shifting to white on hover. 48px vertical padding. Organized in columns with no borders — just type on dark.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; top-nav collapses to hamburger; hero headline drops to 32px; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links; hero headline at 40px |
| Desktop | 1128–1440px | Three-column product grid; full top-nav visible; hero at full 48px headline |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to four columns |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons in the top-nav (search, cart, account) are 44x44px tap targets
- Product card CTAs are full-width on mobile (48px height)
- Filter pills are 36px height with 24px padding for easy tapping

### Collapsing Strategy
- Top navigation links collapse into a hamburger menu below 744px
- Product grid reduces from 3 columns to 2 at tablet, 1 at mobile
- Hero section reduces vertical padding from 64px to 40px on mobile
- Footer columns stack vertically below 744px
- Product card badges shift from top-left to top-right on mobile to avoid overlap with image edges

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components are inferred from common patterns; actual extracted hover colors are not available
- Error state styling for forms (error messages, iconography) is not extracted
- Dark mode is not present on the live site; no dark palette tokens exist
- The extracted font-family list ("Söhne, arial, helvetica, sans-serif") may be incomplete — actual site may use additional weights or variable font axes not captured
- Button loading states, success states, and disabled-secondary states are not documented
- The extracted hex list includes colors that may belong to Shopify checkout widgets, social icons, or stock photography — the true brand palette may be narrower than the 11 colors listed
- Sub-brand or regional palette variations (e.g., Japanese market site may use different colors) are not captured
- Animation durations, easing curves, and transition properties are not extracted
- Icon system (SVG library, stroke weights, sizes) is not documented
- Focus ring styles (outline, offset, color) are not captured from the live site
