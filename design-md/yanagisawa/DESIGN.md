---
version: alpha
name: "Yanagisawa"
source_url: "https://www.yanagisawasax.co.jp"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A precision instrument maker whose digital presence mirrors the exacting craft of its saxophones — the extracted palette reveals a system built on deep indigo (#0062cc) as the primary voltage, a color that reads as both technical authority and artistic depth, far from the expected brass-and-gold clichés of wind instrument branding. The site operates on a clean hierarchy of slate grays (#545b62 for body text, #dae0e5 for hairline strokes) against a white canvas, with #1e7e34 and #117a8b appearing as secondary accents that suggest the verdant patina of aged instrument cases and the cool breath of polished metal. The typography stack defaults to system-native faces — Segoe UI, Roboto, Helvetica Neue — a pragmatic choice that prioritizes legibility across devices over decorative flourish, much like a saxophone's keywork prioritizes function before form. Buttons carry the full indigo weight at 48px height with 12px rounded corners, while secondary actions slip into outline mode with the same slate body color. The nav bar sits at 64px, a compact but confident header that lets the product imagery — the true hero of this brand — command the viewport. There is no extraneous ornament; every pixel serves the object. The brand's voice is not loud; it is the quiet hum of a perfectly tuned instrument waiting to be played.

colors:
  primary: "#0062cc"
  primary-active: "#004085"
  primary-disabled: "#b3d7ff"
  ink: "#1d2124"
  body: "#545b62"
  muted: "#818182"
  muted-soft: "#d6d8db"
  hairline: "#dae0e5"
  hairline-soft: "#c8cbcf"
  canvas: "#ffffff"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#1e7e34"
  accent-teal: "#117a8b"
  accent-yellow: "#d39e00"
  accent-red: "#bd2130"
  badge-green: "#155724"
  badge-red: "#721c24"
  badge-yellow: "#856404"
  badge-blue: "#004085"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 11px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.body}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  button-pill-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-limited:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "14px 32px"
    height: 52px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  section-heading:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    marginBottom: "{spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    margin: "{spacing.lg} 0"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  loading-spinner:
    borderColor: "{colors.hairline}"
    borderTopColor: "{colors.primary}"
    height: 32px
    width: 32px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, saturated in #0062cc indigo with white text and 12px rounded corners. On hover it deepens to #004085, and in its disabled state it fades to #b3d7ff — a pale blue that signals inactivity without competing with the active state. The 48px height and 24px horizontal padding give it a solid, grounded presence against any background. **`button-secondary`** — An outlined variant that uses the same 48px height but swaps fill for a white background with a 2px #dae0e5 hairline border. Text reads in #545b62 body gray. On hover the border thickens in perception by shifting to #545b62 and the background takes a whisper of #f8f9fa. **`button-tertiary-text`** — A text-only link styled as a button, using #0062cc for the label and no background or border. The active state shifts to #004085. Used for "Learn more" and "View details" actions where a full button would compete with the product imagery. **`button-pill-primary`** and **`button-pill-outline`** — Fully rounded 40px pills for secondary actions like filter tags or quick-select options. The filled version carries the indigo primary; the outline version uses a 1px hairline border and body text color.

### Cards
**`product-card`** — The core content container for saxophone listings, built as a white card with a 1px #dae0e5 border and 8px rounded corners. On hover, the border shifts to #0062cc and a subtle 4px shadow lifts the card from the page. The image area uses 4px rounding and a 4:3 aspect ratio that favors landscape instrument photography. Title sits in 16px semibold, price in 16px regular body gray, with 8px vertical gaps between elements. **`badge-new`**, **`badge-sale`**, **`badge-limited`** — Small uppercase labels pinned to the top-left of product images. Green (#1e7e34) for new arrivals, red (#bd2130) for sale items, yellow (#d39e00) for limited editions. All use 11px bold type with 4px rounding and 2px/8px padding.

### Navigation
**`top-nav`** — A 64px white header with a 1px bottom hairline. Navigation links use 15px semibold type in #545b62 body gray, with the active page marked by a 2px #0062cc underline and indigo text. The height is compact enough to keep the focus on product content while providing clear site orientation. **`nav-link-active`** and **`nav-link-inactive`** — Define the two states explicitly, with the active state carrying the brand's primary color as both text and underline indicator.

### Forms
**`text-input`** — Standard 48px text fields with 8px rounding, a 1px hairline border, and 16px body type. On focus the border doubles to 2px and turns #0062cc. Error state uses a 2px #bd2130 border. **`select-input`** — Matches the text input dimensions and styling, with a custom dropdown arrow in #545b62. **`textarea`** — A taller variant of the text input, starting at 120px height with 12px internal padding for comfortable multi-line entry.

### Footer
**`footer`** — A dark anchor for the site, using #1d2124 as the background with #d6d8db text at 14px. Links sit in the same muted gray and lift to white on hover. The section uses 48px vertical padding and 24px horizontal padding, creating a breathing room that contrasts with the compact nav bar above.

### Hero & Sections
**`hero-section`** — The top-of-page brand statement, using a #f8f9fa soft gray background with 32px display type in 700 weight. The CTA button sits at 52px height with 32px horizontal padding — slightly larger than standard buttons to anchor the hero composition. **`section-heading`** — 24px semibold headings with 24px bottom margin, used to organize product categories and informational sections. **`divider`** — A single-pixel #dae0e5 line with 24px vertical margin, used sparingly to separate content blocks without visual noise.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically at full width; hero padding reduces to 32px; buttons expand to full width; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but font-size drops to 14px; hero uses 28px display type; side margins at 24px |
| Desktop | 1128–1440px | Three-column product grid; full nav with 15px links; hero uses 32px display type; content max-width at 1128px centered; side margins at 32px |
| Wide | > 1440px | Four-column product grid; content max-width extends to 1280px; hero type scales to 36px; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons are 40x40px with 40px touch radius
- Product card tap targets (title, image, price) are each independently tappable with minimum 44px hit areas
- Nav links in mobile hamburger menu expand to 48px height for easy finger targeting
- Form inputs maintain 48px height for comfortable touch entry

### Collapsing Strategy
- Top nav collapses to a hamburger icon at < 744px, revealing a full-height overlay menu
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Hero section reduces vertical padding from 64px to 32px on mobile
- Footer link columns collapse from 4 to 2 on tablet, to 1 on mobile
- Badge labels truncate to icons only on mobile (e.g., "NEW" becomes a colored dot)
- Secondary navigation (breadcrumbs, sub-category filters) hides on mobile, accessible via a "Filter" button

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex colors are dominated by Bootstrap utility classes (primary blue, success green, info teal, warning yellow, danger red) and their hover/active variants. The brand's true primary may be a more distinctive color not captured in the extraction — the live site likely uses custom brand colors that are applied via CSS variables or inline styles not captured in the DOM scan. The #0062cc primary is the most distinctive non-gray color in the list and is used as the primary, but this may not match the brand's actual identity.
- No custom font declarations were found beyond system-native stacks. The brand may use a proprietary typeface (e.g., a Japanese typeface for the Japanese market) that is loaded via JavaScript or @font-face not captured in the extraction.
- Hover, active, focus, and disabled states for all components are inferred from common patterns and may not match the live site's exact implementations.
- Error, success, warning, and info toast/alert styling is not captured.
- Dark mode or high-contrast mode variants are not documented.
- The brand's logo, iconography, and illustration style are not represented in the extracted data.
- Animation durations, easing curves, and transition properties are not captured.
- The site may use a Japanese-language version with different typography and spacing requirements.
- Product detail page layout (specifications table, gallery, configurator) is not documented.
- Cart and checkout flow components are not captured.
- The brand may use a sticky header or floating action elements not reflected in the extraction.
