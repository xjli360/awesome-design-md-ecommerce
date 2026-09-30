---
version: alpha
name: "Resident Music"
source_url: "https://www.resident-music.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A record store that lets its inventory do the talking, Resident Music builds its web presence on a muted sage-and-stone palette anchored by #8a947c — a dusty olive-green that reads more like a vintage book spine than a brand color. The canvas is #f3f3f3, a warm off-white that avoids the sterile hospital glow of pure white, while #d8dbde provides a soft silver hairline that frames product grids without shouting. Two accents break the calm: #adaa1d, a chartreuse-yellow that appears on sale badges and price highlights, and #f6343f, a sharp red reserved for sold-out indicators and limited-stock warnings. Typography runs a split personality: the system stack (San Francisco, Arial, Helvetica Neue) handles body text at modest 14–16px sizes, while `resident-hand`, a proprietary script font, appears on logos and hero headers to inject the warmth of a hand-lettered in-store chalkboard. Product cards use {rounded.sm} (8px) corners — soft enough to feel approachable, tight enough to keep the focus on album art. The nav bar sits at 56px, compact for a store that prioritizes browse density over brand theater. Search is a full-width bar with a magnifying-glass icon in #3f4244, the darkest ink on the site, and category filters collapse into a horizontal scroll strip on mobile. The overall effect is that of a well-organized crate-digging experience: quiet, tactile in spirit, and utterly deferential to the records.

colors:
  primary: "#8a947c"
  primary-active: "#686f5d"
  primary-disabled: "#d0d4cb"
  ink: "#3f4244"
  body: "#5b5c5e"
  muted: "#787e7e"
  muted-soft: "#b0b7bd"
  hairline: "#d8dbde"
  hairline-soft: "#e8eae5"
  canvas: "#f3f3f3"
  surface-soft: "#f5f6f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#adaa1d"
  accent-sale-soft: "#f1ee7d"
  accent-danger: "#f6343f"
  accent-danger-soft: "#fdd6d9"
  accent-stock: "#008a2e"
  accent-gold: "#ae8626"
  accent-script: "#3a4c59"

typography:
  display-xl:
    fontFamily: "'resident-hand', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  display-md:
    fontFamily: "'resident-hand', 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, 'Segoe UI', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-accent-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 28px
  button-accent-danger:
    backgroundColor: "{colors.accent-danger}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    height: 28px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-card-badge-sold-out:
    backgroundColor: "{colors.accent-danger}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
  footer-link:
    textColor: "{colors.hairline}"
    typography: "{typography.link}"
  category-filter-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-filter-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-filter-inactive:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  pagination:
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Pre-Order", and "Checkout" flows. Rendered in {colors.primary} (#8a947c) with white text on a compact 40px height. On hover, shifts to {colors.primary-active} (#686f5d). Disabled state uses {colors.primary-disabled} (#d0d4cb) to signal inactivity without visual noise.

**`button-secondary`** — An outlined variant used for "View Details", "Wishlist", and secondary cart actions. White background with {colors.ink} text and a 1px {colors.hairline} border. Active state fills with {colors.hairline-soft} (#e8eae5). Shares the same 40px height and {rounded.sm} corners as the primary button.

**`button-accent-sale`** — A compact pill badge-button used to flag sale items and discount percentages. Uses {colors.accent-sale} (#adaa1d) background with dark ink text, 28px height, and {rounded.sm} corners. Appears overlaid on product card images or inline in price rows.

**`button-accent-danger`** — Reserved for "Sold Out", "Low Stock", and "Last Copy" warnings. Uses {colors.accent-danger} (#f6343f) background with white text. Same dimensions as the sale accent button. Never interactive — purely informational.

### Navigation
**`nav-bar`** — A fixed-position top bar at 56px height, white background, containing the store logo (rendered in `resident-hand` script), main category links, and a search icon. Links use {typography.nav-link} at 14px/500 weight. On scroll, gains a subtle bottom shadow from {colors.hairline}. Mobile collapses to a hamburger menu.

**`breadcrumb`** — Used on product detail and category pages to show navigation depth (e.g., "Home / Vinyl / Rock / Album Title"). Rendered in {colors.muted} (#787e7e) at {typography.caption} size. The active (last) segment uses {colors.ink} (#3f4244). Separators are "/" in {colors.hairline}.

### Cards
**`product-card`** — The core inventory unit: a white card with {rounded.sm} corners containing album artwork, artist name, title, format badge, and price. Artwork fills the top portion with matching corner radius. Text below uses {typography.body-sm} for artist/title and {typography.title-sm} for price. Sale prices render in {colors.accent-sale}. Sold-out items overlay a {colors.accent-danger} badge.

**`product-card-badge`** — A small uppercase label (11px/700 weight) pinned to the top-left of product card images. Sale badges use {colors.accent-sale} background; sold-out badges use {colors.accent-danger}. Padding is tight at 2px 6px with {rounded.xs} corners.

### Forms
**`text-input`** — Standard form input for search, newsletter signup, and account forms. White background, 40px height, {rounded.sm} corners, and {typography.body-sm} text. Focus state adds a 2px {colors.primary} border. Placeholder text uses {colors.muted-soft} (#b0b7bd).

**`search-bar`** — A full-width input field with a magnifying-glass icon on the left. Same dimensions as `text-input` but typically placed in a dedicated search section or overlay. On mobile, expands to fill the viewport width.

### Footer
**`footer`** — A dark section using {colors.ink} (#3f4244) background with {colors.muted-soft} (#b0b7bd) body text. Contains store info, social links, newsletter signup, and legal text. Links use {colors.hairline} (#d8dbde) for legibility against the dark background. Padding uses {spacing.section} (64px) top and bottom.

### Filters
**`category-filter-strip`** — A horizontally scrollable row of filter pills below the nav bar. Inactive pills use {colors.hairline-soft} background with {colors.ink} text. Active pills switch to {colors.primary} background with white text. All pills use {rounded.full} for a pill shape and {typography.button-sm} for text.

### Pagination
**`pagination`** — Numbered page links at the bottom of browse pages. Inactive links use {colors.ink} text with no background. The active page number uses {colors.primary} background with white text. All items share {rounded.sm} corners and {typography.button-sm} sizing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes single-column; search bar expands full-width; category filters become a horizontal scroll strip; footer stacks vertically |
| Tablet | 744–1128px | Nav shows 4–5 category links; product grid uses 2–3 columns; search bar remains full-width but gains a dedicated search page; footer splits into 2 columns |
| Desktop | 1128–1440px | Full nav with all categories; product grid uses 4 columns; search bar sits in nav; footer uses 4 columns; breadcrumbs visible |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 5 columns; category filter strip gains overflow dropdown |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height on mobile
- Category filter pills are 36px tall with 16px horizontal padding
- Product card tap targets (add to cart, wishlist) are 40px minimum
- Nav hamburger icon is 44x44px

### Collapsing Strategy
- Nav links collapse into hamburger menu below 744px
- Category filter strip collapses to a single "Filters" button with dropdown on mobile
- Product card metadata (format, release date) collapses into a tooltip on mobile cards
- Footer columns collapse to a single vertical stack below 744px
- Breadcrumbs truncate to "Home / ... / Current Page" on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- Hover and focus states for text inputs and links were not reliably extracted from the live site; focus rings and hover underlines are inferred from common patterns
- Error and validation styling (form errors, out-of-stock messages) was not observed; red (#f6343f) is assumed for error text based on its use in sold-out badges
- Dark mode is not implemented on the live site; no dark palette tokens exist
- The `resident-hand` font family was detected in CSS but no @font-face declaration or variable font weight/width data was extracted; assumed to be a single-weight script face
- Sub-brand or promotional palettes (e.g., Record Store Day, exclusive variants) were not captured
- Animation and transition durations were not extracted; default to 200ms ease for all interactive states
- The extracted hex list included several Shopify checkout-widget colors (#008a2e for success, #f6343f for error) that may not be part of the brand's intentional palette; they are included as accent tokens with caveats
