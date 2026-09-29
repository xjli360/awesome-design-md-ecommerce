---
version: alpha
name: "Music Direct"
source_url: "https://www.musicdirect.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep-blue #003399 voltage runs through Music Direct like a master tape through a reel-to-reel — it is the primary color for every add-to-cart button, category header, and top-nav link, and it reads as both authoritative (audiophile-grade) and cool (midnight vinyl). The site operates on a bright white canvas with generous {spacing.section} breathing room between product rows, letting the album art and turntable photography carry the emotional weight. Typography leans on icomoon for iconography and a system sans-serif stack for body copy, with display headlines set at 24–32px in medium weight — enough presence to announce a 180g pressing without shouting. Product cards use a clean white surface with a subtle {rounded.sm} corner and a thin {colors.hairline} border, mimicking the sleeve of a record jacket. The search bar is a full-width pill at {rounded.full} with a magnifying-glass icomoon glyph, and the footer stacks three columns of links under a dark {colors.ink} background, grounding the page after all that white. The overall mood is one of precision and warmth — a listening room, not a warehouse.

colors:
  primary: "#003399"
  primary-active: "#002266"
  primary-disabled: "#b3c6e6"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  badge-new: "#cc0000"
  badge-sale: "#cc0000"
  star-rating: "#ffa500"
  link: "#003399"
  link-hover: "#002266"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0
  link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary-active}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
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
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
    border: "1px solid {colors.hairline}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginTop: "{spacing.md}"
  category-strip:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  category-tab-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and "Sign Up". On hover, it shifts to `{colors.primary-active}` for a subtle depth cue. The disabled state uses `{colors.primary-disabled}` with full opacity, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Wishlist". It inherits the primary blue for its text and border, and on hover the background fills with `{colors.surface-soft}` while the border deepens to `{colors.primary-active}`. The `{rounded.sm}` corners keep it consistent with the primary button.

**`button-pill`** — A compact, fully rounded button used for filter tags, quick-add actions, and promotional badges. Its smaller padding and font size let it sit comfortably inline with product metadata or inside a category strip.

### Cards
**`product-card`** — The core product display unit, used on category pages, search results, and featured collections. Each card holds an album or equipment image, a title in `{typography.title-sm}`, and a price in `{typography.body-md}`. On hover, a subtle box shadow lifts the card off the page, and the border transitions from `{colors.hairline-soft}` to `{colors.hairline}`. A `{product-card-badge}` can be overlaid on the top-left corner for "New Arrival" or "Sale" flags.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height, containing the brand logo on the left, category links in the center, and utility icons (search, account, cart) on the right. The active nav link is underlined with a 2px `{colors.primary}` border. On mobile, the category links collapse into a hamburger menu.

**`category-strip`** — A horizontal scrollable strip of category tabs (e.g., "Vinyl", "Turntables", "Speakers", "Accessories") sitting below the nav bar. Each tab is a text-only button with `{rounded.none}` and a bottom-border active state. The strip has a thin bottom hairline to separate it from the hero or product grid.

### Forms
**`text-input`** — Used in search, newsletter signup, and checkout forms. The default state has a 1px `{colors.hairline}` border; on focus, the border thickens to 2px and turns `{colors.primary}`. Padding is generous at 10px 16px to accommodate both text and iconography.

**`search-bar-pill`** — The primary search input, styled as a pill with a light gray background and a subtle border. On focus, the border becomes 2px `{colors.primary}`. It sits in the nav bar on desktop and expands to full width on mobile.

### Footer
**`footer`** — A dark `{colors.ink}` background footer with three columns of links (Customer Service, About Us, Connect) and a copyright line. Links are `{colors.muted-soft}` and lighten to white on hover. The footer uses `{spacing.xxl}` vertical padding to create a grounded, weighty base for the page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger; product cards stack in single column; hero section reduces padding to {spacing.lg}; search bar becomes full-width; footer columns stack vertically. |
| Tablet | 744–1128px | Product cards display in 2-column grid; nav bar shows limited category links with a "More" dropdown; hero uses 2-column layout for image and text. |
| Desktop | 1128–1440px | Product cards in 3-column grid; full nav bar visible; hero uses full-width layout with larger imagery. |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; additional whitespace around hero and category strips. |

### Touch Targets
- All buttons and links have a minimum touch target of 44x44px.
- Category strip tabs have 48px height for easy tapping.
- Search bar pill has 44px height.
- Product card images are tappable to product detail pages.

### Collapsing Strategy
- Nav bar category links collapse into a hamburger menu below 744px.
- Category strip becomes horizontally scrollable on mobile, with a "See All" link at the end.
- Footer columns stack into a single column below 744px.
- Product grid reduces from 4 columns to 1 column as viewport shrinks.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#003399) was reliably extracted from the live site. All other colors in the palette are inferred from common e-commerce patterns and may not match the exact brand implementation.
- No secondary or accent colors were extracted. The badge and star-rating colors are generic defaults.
- Font-family declarations were limited to "icomoon" for iconography. The body and heading font stacks are system defaults; the actual brand typeface (if any) is unknown.
- Hover, focus, and active states for all components are estimated based on standard interaction patterns.
- Error states for forms (validation, error messages) were not observed.
- Dark mode or high-contrast mode preferences are not accounted for.
- The exact spacing and sizing of the nav bar, hero, and footer are based on typical DTC audiophile site conventions, not extracted measurements.
- No data on sub-brand or promotional color variants (e.g., holiday themes, limited editions).
