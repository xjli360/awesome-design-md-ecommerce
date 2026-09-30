---
version: alpha
name: "Things From Another World"
source_url: "https://www.tfaw.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A comic-book retailer that wears its midnight-blue #3c596c like a storefront awning over a deep #110011 interior — the palette reads as a dimly lit back-issue room where fluorescent fixtures hum over long boxes. The brand's primary voltage comes from #137ac6, a cobalt that snaps across CTAs and category headers, while #cc3727 (a stop-sign red) appears sparingly on sale badges and clearance markers, never allowed to dominate. Typography splits between Didact Gothic for display — a geometric sans with open counters that feels like a 1990s comic-shop sign painted on glass — and Barlow Semi Condensed for body, a workhorse that packs character names and price lines into tight grid cells without crowding. The site's architecture is a dense grid of cover-art thumbnails, each one a 200px-square portal into a specific universe, with the search bar acting as the single navigational constant. There are no soft corners: cards use `{rounded.none}` and buttons use `{rounded.sm}`, preserving the sharp, collectible-card feel of the merchandise itself. The canvas is `#ffffff` but it's used sparingly — most surfaces are tinted `{colors.surface-soft}` (#f4f4f4) or the deep `{colors.ink}` (#110011), making the white feel like a spotlight on a comic panel rather than a page background. The overall effect is a store that knows its inventory is the decoration: the design gets out of the way, dims the lights, and lets the four-color covers glow.

colors:
  primary: "#137ac6"
  primary-active: "#0f64a3"
  primary-disabled: "#8bbce0"
  ink: "#110011"
  body: "#2e2e2e"
  muted: "#3c596c"
  muted-soft: "#68a8e0"
  hairline: "#3c596c"
  hairline-soft: "#68a8e0"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#cc3727"
  accent-red-soft: "#e88a7d"
  badge-new: "#137ac6"
  badge-sale: "#cc3727"
  scrim: "#110011"

typography:
  display-xl:
    fontFamily: "'Didact Gothic', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'Didact Gothic', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.3px
  title-lg:
    fontFamily: "'Barlow Semi Condensed', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow Semi Condensed', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Barlow Semi Condensed', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow Semi Condensed', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow Semi Condensed', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Barlow Semi Condensed', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow Semi Condensed', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Barlow Semi Condensed', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Barlow Semi Condensed', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Barlow Semi Condensed', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
  section: 64px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    height: 40px
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
    padding: 9px 19px
    height: 40px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 14px
    height: 30px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-bar-link:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: 12px 16px
  nav-bar-link-active:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: 12px 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-title:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
  product-card-price:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    height: 320px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  search-bar-icon:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    height: 20px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 32px 16px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 10px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in `{colors.primary}` (#137ac6) with white text and a subtle `{rounded.sm}` corner. On hover, it shifts to `{colors.primary-active}` (#0f64a3). The disabled state uses `{colors.primary-disabled}` (#8bbce0) to signal non-interactivity while maintaining brand continuity. Text is uppercase Barlow Semi Condensed at 14px weight 600.

**`button-secondary`** — An outlined-style button on a white canvas with `{colors.ink}` (#110011) text, used for secondary actions like "View Details" or "Add to Wishlist." Shares the same `{rounded.sm}` and uppercase typography as the primary button, but with a 1px `{colors.hairline}` border.

**`button-accent-red`** — A compact, high-urgency button reserved for clearance and sale actions. Uses `{colors.accent-red}` (#cc3727) as background with white text, smaller padding (6px 14px), and `{typography.button-sm}`. Appears only on product cards and category filters where price reduction needs immediate visual weight.

### Cards
**`product-card`** — The fundamental inventory unit: a sharp-cornered (`{rounded.none}`) white card containing a cover-art thumbnail, title, price, and optional badge. No shadow — the card relies on the contrast between `{colors.surface-card}` and the `{colors.surface-soft}` (#f4f4f4) grid background to define its boundaries. The title uses `{typography.title-md}` in `{colors.ink}`, while the price sits below in `{typography.body-sm}` in `{colors.body}` (#2e2e2e).

**`product-card-badge`** — A small, tight badge affixed to the top-left corner of a product card. Two variants exist: the default `{colors.badge-new}` (#137ac6) for new arrivals, and `{colors.badge-sale}` (#cc3727) for discounted items. Both use `{typography.badge}` (10px uppercase Barlow Semi Condensed) with `{rounded.xs}` (2px) corners.

### Navigation
**`nav-bar`** — A persistent top navigation bar at 48px height, rendered in `{colors.ink}` (#110011) with white text. Links are uppercase Barlow Semi Condensed at 14px weight 600, with 12px 16px padding. Active links receive a `{colors.muted}` (#3c596c) background to indicate current section without relying on underlines or borders.

**`nav-bar-link`** — Individual navigation items within the bar. Inactive links are transparent background with white text; active links switch to `{colors.muted}` background. The bar itself has no rounding — it spans the full viewport width.

### Forms
**`text-input`** — A standard form input with white background, `{colors.body}` text, and `{rounded.sm}` corners. Padding is 8px 12px with a height of 40px. The border uses `{colors.hairline}` (#3c596c) at 1px, shifting to `{colors.primary}` on focus. Placeholder text is `{colors.muted-soft}` (#68a8e0).

**`search-bar`** — The primary search interface, a 44px-tall input with white background, `{rounded.sm}` corners, and a magnifying-glass icon in `{colors.muted}` (#3c596c). The input field uses `{typography.body-md}` (15px Barlow Semi Condensed) with placeholder text in `{colors.muted-soft}`. On focus, the border shifts to `{colors.primary}`.

### Footer
**`footer`** — A full-width footer in `{colors.ink}` (#110011) with text in `{colors.muted-soft}` (#68a8e0). Links use `{typography.link}` (14px Barlow Semi Condensed) and inherit the muted-soft color, with hover transitioning to `{colors.canvas}` (#ffffff). Padding is 32px 16px with a `{spacing.section}` (64px) top margin when following content.

### Tags & Dividers
**`category-tag`** — A small, pill-like tag used for filtering comic categories (e.g., "Marvel," "DC," "Image"). Default state is `{colors.surface-soft}` background with `{colors.muted}` text and `{rounded.sm}` corners. Active state switches to `{colors.primary}` background with white text. Both use `{typography.caption}` (12px Barlow Semi Condensed weight 500).

**`divider`** — A 1px horizontal rule in `{colors.hairline}` (#3c596c) used between major sections. A softer variant (`divider-soft`) uses `{colors.hairline-soft}` (#68a8e0) for less visual weight within card grids.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger menu; hero-banner height reduces to 200px; search-bar moves below nav; category-tags wrap to two rows |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows top-level links only; hero-banner at 280px; search-bar remains in header; category-tags display in a horizontal scroll strip |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with all links visible; hero-banner at 320px; search-bar centered in header; category-tags in a fixed row |
| Wide | > 1440px | Four-column product grid with max-width container at 1440px; nav-bar and hero-banner remain at full width; additional whitespace on sides; category-tags expand to show sub-genres |

### Touch Targets
- All buttons and links maintain a minimum 44px height for touch accessibility
- Search-bar input is 44px tall with 16px padding for comfortable tapping
- Category-tags have 10px horizontal padding and 4px vertical padding, with 8px gap between tags
- Nav-bar links have 12px vertical padding within a 48px bar, ensuring adequate tap area
- Product-card badges are at least 20px tall with 6px horizontal padding

### Collapsing Strategy
- Nav-bar collapses to a hamburger menu at < 744px, with a slide-out drawer for full navigation
- Product grid collapses from 4 columns to 1 column as viewport narrows
- Hero-banner text reduces from `{typography.display-xl}` (32px) to `{typography.display-md}` (24px) on mobile
- Category-tag strip switches from a fixed row to a horizontally scrollable container on tablet and below
- Footer link columns stack vertically on mobile, with each section separated by a `{spacing.base}` (16px) gap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text-input and search-bar could not be reliably extracted; the border-color change to `{colors.primary}` is an assumption based on common patterns
- Error styling (validation messages, error borders, error icons) was not present in the extracted data and should be defined by the implementation team
- Dark mode is not supported by the extracted palette; the site appears to be light-mode only
- Sub-brand or franchise-specific color variations (e.g., Marvel section vs. DC section) were not detected
- The exact font weights for Didact Gothic and Barlow Semi Condensed beyond the extracted declarations are assumed; Didact Gothic typically ships with weight 400 only
- Spacing values for component internals (e.g., gap between product-card title and price) were inferred from common grid patterns rather than extracted
- The hero-banner height of 320px is an assumption based on typical comic-store hero dimensions; the extracted data did not include explicit height values
- The `{colors.primary-disabled}` value (#8bbce0) is a calculated lighter variant of the primary, not extracted from the live site
- The `{colors.accent-red-soft}` value (#e88a7d) is a calculated lighter variant of the accent red, not extracted from the live site
