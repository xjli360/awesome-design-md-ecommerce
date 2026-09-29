---
version: alpha
name: "ECM Records"
source_url: "https://www.ecmrecords.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue #003388 — the color of a late-night studio session, of ECM's own catalog spine, of Manfred Eicher's sleeve notes — anchors a system that is deliberately austere, almost monastic. The canvas is not pure white but a faintly violet-warmed #fcfbfe, while surfaces stack in #e9e6ed and #cfc8d8, giving the interface the texture of aged paper or a well-worn LP sleeve. Type runs Univers (the ECM house face) at modest weights and sizes — display sits at 18–24px in weight 400/500, never shouting, letting the album art and the music do the work. Buttons are flat rectangles with `{rounded.none}` corners, typically outlined or filled in the signature blue, and the only rounded element is the search field's `{rounded.xs}`. The nav bar is a thin strip of #1e1e1e with white text, and the entire layout breathes through generous `{spacing.xxl}` gutters. There is no hero carousel, no autoplay video, no gradient — just a grid of square album covers, each a miniature artwork, with the catalog number set in `{typography.caption}` beneath. The brand's voice is that of a curator who trusts the object: the cover, the tracklist, the liner notes. Even the shop cart icon is a simple line drawing. ECM Records is not a storefront; it is a library, and the design makes you slow down.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#8099bb"
  ink: "#1e1e1e"
  body: "#2f2f2f"
  muted: "#515151"
  muted-soft: "#767676"
  hairline: "#cfc8d8"
  hairline-soft: "#dcd7e2"
  canvas: "#fcfbfe"
  surface-soft: "#e9e6ed"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-gold: "#958e09"
  accent-purple: "#720eec"
  accent-blue: "#1e85be"
  accent-green: "#008a20"
  accent-red: "#aa0000"
  badge-new: "#00d084"
  star-rating: "#ffba00"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  display-lg:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
  display-sm:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.5px
  title-md:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
  body-md:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.25px
  body-sm:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.25px
  caption:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.5px
  caption-sm:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.25px
  nav-link:
    fontFamily: "'Univers LT Std', 'Univers', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 1px
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: "0 {spacing.xl}"
  nav-link-item:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.base}"
  nav-link-item-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "8px {spacing.md}"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} 0 0 0"
  product-card-subtitle:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  product-card-catalog:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted-soft}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px {spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px {spacing.xs}"
  badge-format:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px {spacing.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
  footer-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "10px {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "10px {spacing.md}"
    height: 44px
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "0 0 {spacing.lg} 0"
    borderBottom: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, a flat rectangle in ECM blue #003388 with white uppercase Univers text. No border radius, no shadow. On hover, it shifts to `{colors.primary-active}` (#002266). The disabled state fills with `{colors.primary-disabled}` (#8099bb). Used for "Add to Cart", "Checkout", and "Subscribe" actions.

**`button-secondary`** — An outlined variant with a 2px solid `{colors.primary}` border on a transparent background. Text is uppercase Univers in `{colors.primary}`. On hover, it fills solid with `{colors.primary}` and white text. Used for "View Details" and "Learn More" links.

**`button-tertiary-text`** — A text-only button with no background or border. Uses `{typography.button-md}` in `{colors.ink}`. On hover, text shifts to `{colors.primary}`. Used for "Cancel" and "Back to Catalog" links.

### Cards
**`product-card`** — A zero-padding, zero-radius container for album listings. The card is a simple wrapper around a square album cover image, with no border or shadow. Below the image, `{typography.title-sm}` displays the artist name, `{typography.caption}` shows the album title, and `{typography.body-sm}` shows the price. The catalog number sits in `{typography.caption-sm}` at `{colors.muted-soft}`. On hover, the album cover may receive a subtle 1px `{colors.primary}` border.

**`badge-new`** — A small, flat green (#00d084) badge with uppercase 10px Univers. Used to flag new releases. No border radius.

**`badge-sale`** — A red (#aa0000) badge for sale items. Same typography and zero-radius treatment.

**`badge-format`** — A neutral badge in `{colors.surface-soft}` with `{colors.muted}` text. Used to denote format (CD, Vinyl, Digital).

### Navigation
**`top-nav`** — A 56px-high dark bar (#1e1e1e) with white uppercase nav links. Links are spaced at `{spacing.base}` padding. The active link uses `{colors.primary}` text. The nav contains "Home", "Artists", "Catalog", "Shop", and "About" links. No hamburger menu on desktop; on mobile, links collapse into a vertical menu.

**`search-bar`** — A 40px-high input with `{rounded.xs}`, a 1px `{colors.hairline}` border, and `{typography.body-sm}`. On focus, the border switches to `{colors.primary}`. The search icon is a simple line drawing in `{colors.muted}`.

### Forms
**`text-input`** — A 44px-high, zero-radius input with a 1px `{colors.hairline}` border. Uses `{typography.body-sm}`. On focus, border becomes `{colors.primary}`. Used for email signup, checkout forms, and contact forms.

**`select-dropdown`** — Same dimensions and border as `text-input`, but with a dropdown arrow. Used for sorting and filtering (e.g., "Sort by: Newest", "Format: All").

### Footer
**`footer`** — A dark (#1e1e1e) section with white text. Contains links to "Privacy Policy", "Terms of Service", "Contact", and social media icons. Links use `{typography.link}` and turn `{colors.primary}` on hover. Padding is `{spacing.xxl}` top and bottom.

### Hero Section
**`hero-section`** — A full-width dark (#1e1e1e) section used for featured releases or announcements. Text is white, and the section uses `{spacing.section}` padding. No background image or video — just text and a `button-primary`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger; product grid becomes 1 column; hero section padding reduces to `{spacing.xl}`; search bar moves below nav; footer stacks links vertically. |
| Tablet | 744–1128px | Product grid shows 2 columns; top nav remains horizontal but link padding reduces; hero section uses `{spacing.xxl}` padding. |
| Desktop | 1128–1440px | Product grid shows 3 columns; full top nav with `{spacing.base}` link padding; hero section uses `{spacing.section}` padding. |
| Wide | > 1440px | Product grid shows 4 columns; max-width container at 1440px with auto margins; hero section uses `{spacing.section}` padding. |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height.
- Nav links have a minimum 44px touch area on mobile.
- Search bar has a 40px height, acceptable for touch.
- Product card images are tappable with no minimum size, but the entire card area is clickable.

### Collapsing Strategy
- On mobile, the top nav collapses into a hamburger menu with a vertical list of links.
- The search bar moves from the nav area to below the nav on mobile.
- The footer's multi-column link layout collapses to a single column on mobile.
- The product grid collapses from 3-4 columns to 1 column on mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components (only primary and secondary buttons have documented hover states).
- Error styling for form inputs (red border, error message text).
- Sub-brand or collection-specific color palettes (e.g., "ECM New Series" may have its own accent).
- Dark mode variant — the site uses a light canvas with a dark nav, but no system-level dark mode is implemented.
- Animation and transition specifications (ease, duration) for hover/focus states.
- Icon library details (social media icons, cart icon, search icon).
- Typography scale for mobile (font sizes may reduce on small screens).
- The extracted color list includes many framework defaults (WooCommerce blues, greens, reds) that are not part of the brand palette. The true brand colors are #003388 (primary), #1e1e1e (ink), #fcfbfe (canvas), and the violet-toned grays (#e9e6ed, #cfc8d8, #dcd7e2). The accent colors (#958e09, #720eec, #1e85be, #008a20, #aa0000) are used sparingly for badges and alerts.
