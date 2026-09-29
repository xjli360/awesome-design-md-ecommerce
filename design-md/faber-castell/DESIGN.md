---
version: alpha
name: "Faber-Castell"
source_url: "https://www.fabercastell.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep forest green (#05301a) anchors a brand that has been making art supplies since 1761, and the weight of that history shows in how confidently the system uses restraint. The primary green appears on buttons, navigation bars, and category headers — not as an accent but as a structural color that says "this is serious craft." A warm off-white (#f6f6f0) serves as the canvas, softer than pure white, evoking the tooth of fine paper. Red (#c60808) arrives sparingly: sale badges, error states, the occasional price-drop flag — a single sharp note against the green-and-cream harmony. The extracted palette is heavy on grays (#707170, #787878, #aaaaaa, #d5d5d5) used for borders, muted text, and secondary surfaces, creating a quiet hierarchy where the green and red do all the emotional work. Typography defaults to system sans-serif (Arial, sans-serif) with no custom brand font detected — the brand lets its product photography and packaging design carry personality instead. Cards use soft rounding ({rounded.sm}) while buttons are pill-shaped ({rounded.full}), a contrast that makes CTAs feel tactile and intentional. The overall mood is workshop-meets-gallery: clean enough for a professional illustrator, warm enough for a child's first pencil set.

colors:
  primary: "#05301a"
  primary-active: "#042614"
  primary-disabled: "#8a9e8f"
  ink: "#111111"
  body: "#444444"
  muted: "#707170"
  muted-soft: "#a4a4a4"
  hairline: "#d5d5d5"
  hairline-soft: "#e6e6e6"
  canvas: "#f6f6f0"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#c60808"
  accent-red-soft: "#fdd0d0"
  accent-gold: "#eedd22"
  accent-gold-soft: "#f6f0c0"
  badge-sale: "#c60808"
  badge-new: "#05301a"
  star-rating: "#eedd22"
  link-blue: "#1199ff"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 6px
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
  button-tertiary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.full}"
  button-pill-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "inherit"
    typography: "{typography.nav-link}"
    padding: "8px 16px"
    rounded: "{rounded.sm}"
  nav-link-active:
    backgroundColor: "rgba(255,255,255,0.15)"
    textColor: "inherit"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-banner-overlay:
    backgroundColor: "rgba(5, 48, 26, 0.6)"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  category-tile-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
    border: "2px solid {colors.primary}"
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.lg}"
    rounded: "{rounded.sm}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with forest green (#05301a) and white text. Pill-shaped ({rounded.full}) with 44px height and 28px horizontal padding. On hover, darkens to `{colors.primary-active}` (#042614). Disabled state uses a muted green-gray `{colors.primary-disabled}` (#8a9e8f). Used for "Add to Cart," "Shop Now," and primary form submissions.

**`button-secondary`** — Outlined variant on the cream canvas (#f6f6f0). Green text with a 2px green border, same pill shape and height. On hover, fills solid green and inverts to white text. Used for "Learn More," "View Details," and secondary actions.

**`button-tertiary`** — Text-only button with no background or border. Green text on hover gains a light gray background (`{colors.surface-soft}`). Used for "Cancel," "Skip," and inline navigation links that need button semantics.

**`button-pill-red`** — Small, urgent pill in accent red (#c60808) with white text. Used exclusively for sale badges, clearance flags, and limited-time offers. Compact at 8px vertical padding.

### Cards
**`product-card`** — White card with a soft shadow (`0 1px 3px rgba(0,0,0,0.08)`) and 6px rounding. The product image sits flush to the top corners (`{rounded.sm} {rounded.sm} 0 0`). On hover, the shadow deepens to `0 4px 12px rgba(0,0,0,0.12)`. Contains product name (body-sm), price (title-sm), and optional badge overlays in the top-left corner.

**`category-tile`** — White tile with 6px rounding and a light shadow. On hover, gains a 2px green border. Used on the homepage to display product categories (e.g., "Colored Pencils," "Markers," "Art Sets") with a thumbnail image and title.

### Navigation
**`nav-bar`** — Fixed-height 56px bar in forest green (#05301a) with white uppercase nav links. On scroll, transitions to a white bar with dark text and a subtle bottom shadow. Links have 8px vertical and 16px horizontal padding with 6px rounding on hover/active states.

**`nav-link`** — Uppercase, 14px, weight 600, with 0.5px letter spacing. Active state adds a semi-transparent white overlay (`rgba(255,255,255,0.15)`) on the green bar, or a green underline on the white scrolled bar.

### Forms
**`text-input`** — Cream canvas background with a 1px hairline border (#d5d5d5) and 6px rounding. On focus, gains a 2px green border. Error state switches to a 2px red border. Height is 44px to match button height for aligned form rows.

**`select-dropdown`** — Matches text-input styling but includes a custom dropdown arrow. Uses the same 44px height, 6px rounding, and focus/error states.

### Badges
**`badge-sale`** — Red (#c60808) background, white uppercase 11px text, 2px rounding. Compact at 2px vertical and 8px horizontal padding. Positioned absolutely on product cards in the top-left corner.

**`badge-new`** — Green (#05301a) background, same typography and sizing as sale badge. Used for new arrivals and recently launched products.

**`badge-out-of-stock`** — Gray (#eeeeee) background with muted (#707170) text. Communicates unavailability without alarm.

### Footer
**`footer`** — Full-width forest green band with white text at 80% opacity for links. Links return to full opacity on hover. Padding is 48px top and bottom. Contains columns for "Shop," "About," "Support," and "Connect" with standard link styling.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack full-width; hero banner text reduces to 24px; footer columns stack vertically |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero banner uses 28px display text; footer shows two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all links; hero banner at 32px display text; footer in four columns |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to four columns; hero banner centered with 40px max-width content area |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Nav links have 48px minimum touch area (8px padding on 14px text)
- Product card tap targets (Add to Cart, Quick View) are at least 44x44px
- Search bar is 40px tall with 16px horizontal padding for easy thumb access
- Accordion headers are 44px tall with generous 24px horizontal padding

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px; the green bar remains but links hide behind a slide-out drawer
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer columns collapse from 4 to 2 at tablet breakpoint, then stack vertically on mobile
- Category tiles collapse from a 4-column grid to a horizontal scrollable strip on mobile
- Hero banner reduces padding from 64px to 32px on mobile; overlay text shrinks proportionally

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font detected; the site uses system sans-serif (Arial/Helvetica). A brand font may exist for print or packaging but is not present in the web CSS.
- Hover and focus states for most components were inferred from common patterns; the live site may use different transitions or color shifts.
- Error state styling for forms (red border) was assumed based on the presence of #c60808 in the palette; exact error message typography and iconography were not extracted.
- Dark mode is not present on the live site; no dark palette tokens are defined.
- The extracted color list is heavily gray with only two distinctive brand colors (green #05301a and red #c60808). The gold (#eedd22) appears in the palette but its usage context (star ratings, badges, or decorative elements) could not be confirmed.
- Shopify checkout widgets (Shopify Pay, Klarna, Afterpay) may introduce additional colors not captured in the brand palette.
- Sub-brand palettes (Faber-Castell 9000, Pitt Artist Pen, Castell 9000) may use different accent colors that were not extracted from the main site.
- Animation durations, easing curves, and transition properties were not extracted from the live CSS.
- Focus ring styling (outline color, width, offset) for keyboard accessibility was not found in the extracted data.
- The meta theme-color tag was absent, meaning the browser chrome/task bar color is not explicitly set.
