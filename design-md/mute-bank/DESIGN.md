---
version: alpha
name: "Mute Bank"
source_url: "https://www.mutebank.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record label and shop that feels like a dimly lit listening room — the palette is anchored on #cd0a0a, a blood-drop red that appears sparingly as the sole chromatic voltage against a field of near-blacks (#222222, #212121, #121212) and warm grays (#aaaaaa, #555555, #363636). The red never screams; it sits in small doses — a cart badge, a sale tag, a hover underline — while the rest of the interface recedes into the dark. The canvas is #fbf9ee, a parchment off-white that softens the contrast and keeps the storefront from feeling cold. Type runs proxima-nova at modest sizes with generous line-height, letting album titles and tracklists breathe in the negative space. The search bar, a pill-shaped dark field with white text, sits flush against the top edge like a club door. Product cards use soft corners ({rounded.md}) and thin hairlines (#dedede) that barely separate items, trusting the rhythm of square album art to do the layout work. The overall effect is restrained, almost archival — a shop that wants you to browse slowly, with the red acting as a quiet pulse rather than a call to action.

colors:
  primary: "#cd0a0a"
  primary-active: "#a00808"
  primary-disabled: "#f5a0a0"
  ink: "#222222"
  body: "#363636"
  muted: "#555555"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e6e6e6"
  canvas: "#fbf9ee"
  surface-soft: "#fef1ec"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#fbf9ee"
  accent-warm: "#ff7300"
  badge-sale: "#cd0a0a"
  badge-new: "#fcefa1"
  dark-bg: "#121212"
  dark-surface: "#212121"
  dark-hairline: "#363636"

typography:
  display-xl:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'proxima-nova', 'Arial', 'Verdana', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  search-bar:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-light:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    borderColor: "{colors.hairline}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  cart-icon:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 32px
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 24px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Checkout", and "Subscribe". Rendered in the brand's signature red (#cd0a0a) with white uppercase text. On hover, the background deepens to `{colors.primary-active}` (#a00808). Disabled state uses a washed-out pink `{colors.primary-disabled}` (#f5a0a0) with white text. The button has a subtle 8px border radius and 44px height, making it compact but not cramped.

**`button-secondary`** — A dark alternative for use on light backgrounds, primarily in the header and footer areas. Uses `{colors.dark-bg}` (#121212) as background with `{colors.on-dark}` (#fbf9ee) text. Same uppercase typography and 8px radius as the primary button. No border — relies on contrast against the canvas.

**`button-tertiary`** — A text-only button with no background or border, used for secondary actions like "View Details" or "Cancel". Inherits `{colors.ink}` (#222222) text color. On hover, the text color shifts to `{colors.primary}` (#cd0a0a) to indicate interactivity.

### Cards
**`product-card`** — The core content container for album releases and merchandise. A white card (`{colors.surface-card}`) with 12px rounded corners and no padding — the product image fills the top edge-to-edge. Product title, artist name, and price sit in `{typography.body-sm}` below the image. On hover, a subtle box shadow lifts the card slightly. No border; the card relies on the white surface against the parchment canvas for separation.

### Navigation
**`nav-bar`** — A 64px fixed-height bar at the top of the page. On the main storefront, it uses `{colors.canvas}` (#fbf9ee) background with `{colors.ink}` (#222222) text. On the checkout or dark-themed pages, `nav-bar-dark` switches to `{colors.dark-bg}` (#121212) with `{colors.on-dark}` (#fbf9ee) text. Navigation links use uppercase `{typography.nav-link}` with 0.5px letter-spacing. The active link is underlined in `{colors.primary}` (#cd0a0a).

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and checkout fields. Uses `{colors.canvas}` background with `{colors.ink}` text and a `{colors.hairline}` (#dedede) border. On focus, the border switches to `{colors.primary}` (#cd0a0a). Height is 48px with 12px vertical padding and 16px horizontal padding. Border radius is 8px.

### Search
**`search-bar`** — A pill-shaped search field with 9999px border radius, used on the main page. Background is `{colors.dark-bg}` (#121212) with white text, creating a high-contrast entry point. Height is 48px with 12px vertical and 20px horizontal padding. On light backgrounds, `search-bar-light` uses a white background with `{colors.hairline}` border.

### Badges
**`badge-sale`** — A small red badge (#cd0a0a) with white uppercase text, used to flag discounted items. 4px border radius, 4px vertical and 8px horizontal padding. Text is 11px bold with 0.5px letter-spacing.

**`badge-new`** — A pale yellow badge (#fcefa1) with dark text, used for new arrivals or pre-orders. Same dimensions and typography as the sale badge, but with a softer, less urgent color.

### Footer
**`footer`** — A dark section at the bottom of the page using `{colors.dark-bg}` (#121212) background. Text is `{colors.on-dark}` (#fbf9ee) in `{typography.body-sm}`. Contains links to social media, shipping info, and the label's catalog. Padding is 48px vertical and 24px horizontal. Social icons use `{colors.muted}` (#555555) with full border radius.

### Cart
**`cart-icon`** — A circular icon button in the header, rendered in `{colors.primary}` (#cd0a0a) with white text. 32px height with full border radius. Displays the item count as a small number. On hover, the background shifts to `{colors.primary-active}` (#a00808).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar moves below header; footer stacks vertically; badge text shrinks to 10px |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; search bar remains in header; footer splits into two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; search bar in header; footer in three columns |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; nav and footer centered with generous margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines
- Cart icon and social icons are 32px minimum with adequate padding
- Product cards have full-surface tap targets (no dead zones)
- Nav links have 48px tap height on mobile

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer
- The search bar moves from the header to a dedicated row below the nav on mobile
- Product grid collapses from 3-4 columns to 1 column on mobile
- Footer links collapse from a multi-column layout to a single vertical stack
- Badge text reduces to 10px on mobile to prevent overflow
- Category filters (if present) collapse into a horizontal scrollable strip on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons could not be reliably extracted from the live site
- Error styling for form inputs (validation messages, error borders) is not present in the extracted data
- Dark mode toggle behavior and associated color tokens are not documented
- Sub-brand or collection-specific color palettes (e.g., limited edition releases) are not captured
- The exact font weight for proxima-nova could not be confirmed — the extracted CSS only shows the font family name
- Active/visited states for navigation links are inferred from common patterns, not extracted
- The checkout flow uses Shopify's default styling, which may differ from the brand's design system
- Loading states and skeleton screens are not documented
- The `#ff7300` color appears in the extracted list but its usage context could not be determined — it may be a Shopify widget color or an unused accent
- The `#d3d3d3` and `#dadada` colors appear frequently but their specific role (border, background, text) is unclear without more context
