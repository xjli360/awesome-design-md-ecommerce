---
version: alpha
name: "McFarlane Toys"
source_url: "https://mcfarlane.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A comic-book voltage runs through every pixel of McFarlane Toys — the brand's deep navy `#003388` anchors a system that feels less like a toy store and more like a collector's display case. That blue, pulled straight from Todd McFarlane's Spawn-era cape shadows, appears on every primary button, navigation bar, and product badge, while a neon-lime `#8dc63f` — the exact green of a symbiote's eye — serves as the single accent that signals price drops, limited editions, and "new arrival" flags. The palette is deliberately restrained: four grays (`#555d66`, `#32373c`, `#949494`, `#d8d8d8`) handle all text hierarchy and borders, with `#eeeeee` as the soft canvas and `#ebebeb` as the hairline that separates product grids. Typography runs system-native (`-apple-system`, `BlinkMacSystemFont`, `Roboto`, `Segoe UI`, `Ubuntu`, `Cantarell`, `Helvetica Neue`, `sans-serif`) at modest weights — no custom brand font, no display face, just clean legibility that lets the product photography do the talking. Buttons are sharp-cornered (`{rounded.sm}`) and dense, with 48px heights and tight 12px horizontal padding that mirrors the compact, panel-like feel of a comic page. Product cards use `{rounded.none}` — every edge is a hard 0px, reinforcing the "in-the-box" display aesthetic. The nav bar sits at 72px with a `{colors.canvas}` background and `{colors.ink}` text, but the real signature is the "Limited Edition" badge: `{colors.primary}` background, `{colors.on-primary}` text, `{rounded.sm}`, and a 2px `{colors.primary-active}` border that glows like a variant cover's foil stamp. Search is a full-width bar with `{rounded.sm}` corners and a `{colors.primary}` submit button — no pill shapes, no soft curves, just utilitarian precision. The footer collapses into a single-column stack on mobile, with `{colors.muted}` links and `{colors.hairline}` dividers that echo the brand's no-fuss, all-product ethos.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#8099cc"
  ink: "#32373c"
  body: "#555d66"
  muted: "#949494"
  muted-soft: "#d8d8d8"
  hairline: "#ebebeb"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f8f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#8dc63f"
  accent-green-active: "#6ea82e"
  accent-red: "#cf2e2e"
  accent-orange: "#ff6900"
  accent-yellow: "#fcb900"
  badge-new: "#8dc63f"
  badge-limited: "#003388"
  badge-sale: "#cf2e2e"
  star-rating: "#fcb900"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, Roboto, 'Segoe UI', Ubuntu, Cantarell, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.27
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
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
    height: 48px
  button-accent:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-green-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
  product-card-image:
    rounded: "{rounded.none}"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.accent-red}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
    height: 48px
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
  hero-banner-accent:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the entire site. Solid `{colors.primary}` fill with white text, `{rounded.sm}` corners, and 48px height. On hover/active, shifts to `{colors.primary-active}` (`#002266`). Disabled state uses `{colors.primary-disabled}` (`#8099cc`) with reduced opacity. Used for "Add to Cart", "Pre-Order", and "Shop Now" actions.

**`button-secondary`** — Outlined variant for secondary actions like "View Details" or "Compare". White fill with `{colors.primary}` text and a 1px `{colors.primary}` border. Active state inverts to `{colors.primary}` fill with white text. Same 48px height and `{rounded.sm}` corners as primary.

**`button-accent`** — Reserved for promotional or limited-time actions. Uses `{colors.accent-green}` (`#8dc63f`) fill with dark `{colors.ink}` text. Active state shifts to `{colors.accent-green-active}` (`#6ea82e`). Typically paired with "Limited Time" or "New Arrival" badges.

### Badges
**`badge-new`** — Green badge (`{colors.badge-new}`) with dark text, signaling newly added products. `{rounded.sm}` corners and uppercase `{typography.badge}` type. Positioned at the top-left corner of product card images.

**`badge-limited`** — Navy badge (`{colors.badge-limited}`) with white text, used for limited edition or exclusive items. Same shape and typography as `badge-new`, but the dark background creates a more premium, collectible feel.

**`badge-sale`** — Red badge (`{colors.badge-sale}`) with white text, indicating discounted pricing. Uses the same `{rounded.sm}` and uppercase badge typography. Always paired with `product-card-sale-price` styling.

### Cards
**`product-card`** — The primary product display unit. White background, `{rounded.none}` (hard corners), and a subtle `{colors.hairline}` border on hover. The image container also uses `{rounded.none}`, reinforcing the "in-box" display aesthetic. Price is rendered with `{typography.title-sm}` in `{colors.ink}`, while sale prices switch to `{colors.accent-red}`.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height. White background with `{colors.ink}` text for brand name and `{colors.muted}` for secondary links. Active nav links use `{colors.primary}` text color. The bar includes a search icon that expands into `search-bar` on click.

**`category-strip`** — Horizontal scrollable strip below the hero banner. `{colors.surface-soft}` background with pill-shaped category tabs. Active tabs use `{colors.primary}` fill, inactive tabs are transparent with `{colors.muted}` text.

### Forms
**`text-input`** — Standard input field with `{rounded.sm}` corners, 48px height, and 12px horizontal padding. Focus state adds a 2px `{colors.primary}` border. Used for search, newsletter signup, and checkout forms.

**`search-bar`** — Full-width search input with `{rounded.sm}` corners and a `{colors.primary}` submit button. The input field uses `{typography.body-md}` and placeholder text in `{colors.muted}`. On mobile, collapses to an icon that expands on tap.

### Footer
**`footer-link`** — Muted text links (`{colors.muted}`) using `{typography.link}`. Hover state shifts to `{colors.primary}`. Links are separated by `{colors.hairline}` dividers. The footer stacks into a single column on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), collapsed nav to hamburger, stacked footer, search bar becomes icon-only |
| Tablet | 744–1128px | Two-column product grid (2 cards), expanded nav with dropdowns, two-column footer |
| Desktop | 1128–1440px | Three-column product grid (3 cards), full nav with all links visible, three-column footer, hero banner at full width |
| Wide | > 1440px | Four-column product grid (4 cards), max-width container at 1440px, hero banner constrained to container |

### Touch Targets
- All buttons and interactive elements maintain minimum 48px height for touch accessibility
- Nav links have 44px minimum touch target width
- Category tabs in the strip have 44px minimum height
- Badges remain at their defined size (small) but are positioned with 8px padding from card edges to avoid accidental taps

### Collapsing Strategy
- Nav bar collapses to hamburger menu on mobile (< 744px), with a slide-out drawer
- Category strip becomes horizontally scrollable on mobile, with visible scroll indicators
- Product grid collapses from 4 columns (wide) to 1 column (mobile)
- Footer collapses from 3 columns (desktop) to 1 column (mobile), with accordion-style expandable sections
- Search bar collapses to icon-only on mobile, expanding to full-width on tap
- Hero banner reduces font size on mobile (`{typography.display-md}` instead of `{typography.display-xl}`)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted; only primary button active/disabled states are confirmed
- Error styling for form inputs (validation states, error messages) is not present in extracted data
- Dark mode is not supported; all extracted colors assume light theme
- Sub-brand or franchise-specific palettes (Spawn, Mortal Kombat, DC, etc.) are not captured — the extracted colors represent the main McFarlane Toys site only
- The extracted hex list includes many colors that appear to be from WordPress admin UI (`#f78da7`, `#cf2e2e`, `#ff6900`, `#fcb900`, `#7bdcb5`, `#00d084`, `#8ed1fc`, `#0693e3`, `#abb8c3`) — these have been filtered out as framework defaults, but some may be intentional brand accents
- FontAwesome icon font is declared but no icon-specific styling (sizes, colors, hover states) could be extracted
- Animation and transition durations (button hover, card hover, nav dropdown) are unknown
- The `#330011`, `#334455`, `#112288`, `#331166`, `#336622`, `#223366`, `#112266` colors in the extraction appear to be WordPress theme defaults or stock image tones, not intentional brand colors — they have been excluded from the palette
- No custom brand font exists; the system uses native OS fonts exclusively
- Checkout flow styling (Shopify Pay, Klarna, Afterpay widgets) could not be extracted
