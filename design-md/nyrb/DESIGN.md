---
version: alpha
name: "NYRB"
source_url: "https://www.nyrb.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, literary red — #d3232e — anchors the New York Review Books storefront, a color that reads as serious and intellectual rather than promotional, appearing on the primary add-to-cart button, the site header, and the small logo mark. This red is offset by a cool, authoritative blue (#243fa1) used sparingly for secondary actions and select navigation elements, creating a restrained two-color system that feels more like a university press than a commercial publisher. The canvas is a clean white (#ffffff), with a soft gray (#dedede) for hairline borders and dividers, and a muted sage green (#89bf87) that surfaces in category badges and sale indicators — an unexpected, almost botanical accent that prevents the palette from feeling cold. Typography runs Fira Sans at modest weights, with body copy set at 16px and a line height of 1.5 that prioritizes readability for long-form book descriptions and editorial content. The layout is columnar and generous — product grids use wide gutters, and individual book cards are given breathing room with soft shadows and rounded corners at {rounded.sm} (8px). There is no hero carousel or aggressive promotional module; instead, the homepage leads with a curated grid of recent releases and staff picks, trusting the cover art and the authority of the NYRB imprint to do the selling. The overall mood is that of a well-stocked independent bookstore translated into a clean, typographically rigorous web experience — quiet, confident, and utterly without trend-chasing.

colors:
  primary: "#d3232e"
  primary-active: "#b01e27"
  primary-disabled: "#f0b3b6"
  accent-blue: "#243fa1"
  accent-blue-active: "#1c3280"
  accent-green: "#89bf87"
  accent-green-active: "#6ea86c"
  ink: "#121212"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent-blue: "#ffffff"
  on-accent-green: "#121212"
  star-rating: "#d3232e"
  badge-sale: "#89bf87"
  badge-new: "#243fa1"
  error: "#c82222"
  error-bg: "#fce8e8"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  button-md:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.25px
  link:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "'Fira Sans', 'Lato', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
    color: "{colors.accent-green}"

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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    textDecoration: underline
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-accent-blue}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-accent-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-accent-green}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "2px solid {colors.error}"
    backgroundColor: "{colors.error-bg}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 14px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 0
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    boxShadow: "0 1px 4px rgba(0,0,0,0.08)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "3:4"
    objectFit: "contain"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.xxs} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-accent-green}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.display-sm}"
    textColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.canvas}"
    textDecoration: none
  footer-link-hover:
    textColor: "{colors.primary}"
    textDecoration: underline
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-accent-blue}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-accent-green}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.accent-blue}"
    textDecoration: underline
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  pagination-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    padding: "4px 10px"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 44px
    width: 44px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} 0 {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand red (#d3232e) with white text and 8px rounded corners. Used for "Add to Cart," "Checkout," and primary form submissions. On hover, the background shifts to a deeper red (#b01e27). The disabled state uses a pale pink (#f0b3b6) with white text, signaling unavailability without visual noise.

**`button-secondary`** — A white button with a 1px hairline border, used for "View Details," "Continue Shopping," and secondary actions that should not compete with the primary CTA. On hover, the border becomes the ink color and the background shifts to the soft surface tone. Height and padding match the primary button for alignment in forms.

**`button-tertiary-text`** — A text-only button in the brand red, used for "Cancel," "Clear Filters," and inline actions. On hover, the text underlines and shifts to the active red. No background or border — purely typographic.

**`button-accent-blue`** and **`button-accent-green`** — Smaller, compact buttons (36px height) used for category filters, "New" badges, and sale triggers. The blue variant (#243fa1) signals editorial picks or new arrivals; the green (#89bf87) signals discounts or special offers. Both use 8px rounded corners and smaller button typography.

### Cards
**`product-card`** — A white card with a soft drop shadow and 8px rounded corners, housing a book cover image (3:4 aspect ratio, `object-fit: contain`), the title in 16px semibold, the author in 13px muted caption, and the price. On hover, the shadow deepens to create a subtle lift effect. The card has no internal padding — spacing is handled by child element padding.

**`product-card-badge`** — An overlay badge pinned to the top-left of the product image, rendered in the green accent with uppercase 11px bold type. Used for "Sale," "Staff Pick," or "Signed Edition" flags.

### Navigation
**`nav-bar`** — A 64px white header with a 1px bottom hairline border. Navigation links are set in 14px uppercase with 0.5px letter spacing. The active link is colored in the brand red; inactive links are muted gray. A sticky variant adds a subtle box-shadow on scroll. The nav includes a full-width dropdown menu for category browsing.

**`nav-dropdown`** — A white dropdown panel with 8px rounded corners and a 4px/16px shadow, containing category links in body-sm type. Appears on hover or focus of parent nav items.

### Forms
**`text-input`** — A 44px tall input field with 8px rounded corners, a 1px hairline border, and 16px body type. On focus, the border becomes a 2px red stroke. Error state uses a 2px red border with a light red background (#fce8e8). The same structure applies to select inputs and textareas, with the textarea using a taller default height.

**`search-bar`** — A pill-shaped (full rounded) search input with a soft gray background and hairline border, 40px tall. On focus, the background turns white and the border becomes a 2px red stroke. The pill shape is the only full-radius element in the system, creating a subtle visual distinction for the search action.

### Footer
**`footer`** — A dark footer (#121212) with white text, using body-sm type for links and copyright. Links are white with no underline by default; on hover they turn red and underline. The footer is padded with 48px top/bottom and 24px left/right, creating a clear visual termination for the page.

### Badges
**`badge-new`** and **`badge-sale`** — Small, uppercase 11px bold badges with 4px rounded corners. The "New" badge uses the blue accent (#243fa1) with white text; the "Sale" badge uses the green accent (#89bf87) with dark text. Both use 2px vertical and 8px horizontal padding.

### Breadcrumbs
**`breadcrumb`** — A row of caption-sized links separated by slashes, with the current page rendered in ink and ancestor links in blue with underlines. Breadcrumbs sit above the page title on collection and product pages.

### Pagination
**`pagination`** — A row of numbered page links in body-sm type. The active page is a red pill with white text and 4px rounded corners. Inactive pages are muted gray with no background. On hover, inactive pages gain a soft gray background and shift to ink.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 column); nav collapses to hamburger menu; search bar moves to a full-width overlay; footer stacks vertically; hero section reduces padding to 32px; product card images reduce to 2:3 aspect ratio; breadcrumbs hide; pagination truncates to "Prev / Next" |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but "Shop" and "About" may collapse into a "More" dropdown; search bar remains in header but shrinks to 32px height; footer splits into two columns; hero section uses 48px padding |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; search bar at 40px height; footer uses four columns; hero section at full 64px padding; breadcrumbs visible |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px with auto margins; nav bar and footer expand to full width with content centered; hero section uses 80px padding for breathing room |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Icon buttons and quantity selector buttons are 44px x 44px.
- Product card links have a minimum tap area of 48px for the title and author lines.
- Nav links in mobile hamburger menu are 48px tall for easy tapping.
- Search bar is 40px tall on desktop, expanding to 48px on mobile for touch comfort.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- The category strip (if present) collapses into a horizontal scrollable row with snap points.
- The footer collapses from four columns to a single vertical stack.
- Breadcrumbs are hidden on mobile; the page title serves as the primary orientation cue.
- Product filters (if present) collapse into a "Filter" button that opens a modal or bottom sheet.
- The search bar collapses from a visible input to a search icon that expands on tap.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for many components (button-secondary, nav-dropdown items, footer links) are inferred from common patterns rather than extracted from the live site.
- Error styling for form inputs (error-bg, error border) is a best-guess based on the extracted #c82222 error color — the actual error message typography and iconography are unknown.
- The exact font stack for body text is uncertain — the extracted `!important` and `inherit` values suggest aggressive CSS specificity, but the intended fallback order (Fira Sans, Lato, serif) is an editorial assumption.
- Dark mode is not implemented; the system assumes a light canvas at all breakpoints.
- The accent green (#89bf87) may be a stock-image dominant tone rather than a brand color — its usage in badges and sale indicators is inferred from common e-commerce patterns.
- The accent blue (#243fa1) appears infrequently; it may be a secondary brand color or a legacy element from a previous design iteration.
- No extracted data for: focus ring styles, loading spinners, skeleton screens, toast notifications, modal overlays, or tooltip design.
- The `object-fit: contain` declaration was found on images, suggesting book covers are displayed without cropping — but the exact aspect ratio (3:4) is a standard trade paperback dimension, not a confirmed site value.
- Shopify platform defaults (checkout buttons, payment icons, cart drawer) may override some design tokens; the extent of customization is unknown.
- The meta theme-color is absent, meaning the browser chrome on mobile will default to white or system color — this may be intentional or an oversight.
