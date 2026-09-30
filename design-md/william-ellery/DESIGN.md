---
version: alpha
name: "William Ellery"
source_url: "https://williamellery.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep forest-green (#022501) grounds the William Ellery storefront like a pine needle floor, while a pale sky-blue (#83c5e0) washes over secondary panels and product photography backdrops, creating a landscape of color that feels walked-in rather than designed. The cream canvas (#f9f7e9) reads as sun-bleached paper or well-worn trail map, and the brand uses it generously across backgrounds and card surfaces, letting the dark ink do the work of framing product silhouettes. A brass-toned accent (#c3a141) appears sparingly — on price tags, on sale badges, on the thin stroke of a cart icon — like a brass button on a waxed jacket. The single typeface is Jost, a geometric sans with a humanist warmth that avoids the coldness of pure grotesk; it runs at modest weights (400–600) across headings and body copy, never shouting. Product cards sit on `{rounded.sm}` corners with `{spacing.lg}` padding, and the primary CTA button — a solid block of `{colors.primary}` with `{colors.on-primary}` text — uses `{rounded.none}` corners, a deliberate break from the softness elsewhere that signals "this is the action." The footer collapses into a dense column of links on mobile, and the nav bar drops its search field behind a magnifying-glass icon, preserving the clean horizon line the brand values. There is no hero carousel; instead, a single full-bleed image anchors each collection page, the `{colors.primary}` overlay at 40% opacity pulling the photograph into the brand system. The overall effect is that of a field guide — authoritative, quiet, and built for the long haul.

colors:
  primary: "#022501"
  primary-active: "#121212"
  primary-disabled: "#dedede"
  ink: "#022501"
  body: "#121212"
  muted: "#5a5a5a"
  muted-soft: "#8a8a8a"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f9f7e9"
  surface-soft: "#f8f8e7"
  surface-card: "#ffffff"
  on-primary: "#f9f7e9"
  accent-brass: "#c3a141"
  accent-sky: "#83c5e0"
  accent-sky-soft: "#8bc3de"
  accent-terracotta: "#a83317"
  star-rating: "#c3a141"
  sale-badge: "#a83317"

typography:
  display-xl:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Jost', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill-accent:
    backgroundColor: "{colors.accent-brass}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.accent-terracotta}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 1px 3px rgba(2,37,1,0.08)"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 40px
  search-bar-focus:
    borderColor: "{colors.primary}"
    borderWidth: 1px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-hover:
    boxShadow: "0 4px 12px rgba(2,37,1,0.1)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "3:4"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  sale-badge:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    minHeight: 400px
  hero-overlay:
    backgroundColor: "{colors.primary}"
    opacity: 0.4
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
    hoverColor: "{colors.accent-brass}"
  footer-heading:
    color: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    textTransform: uppercase
    letterSpacing: 0.5px
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
    separatorColor: "{colors.hairline}"
  breadcrumb-current:
    color: "{colors.body}"
    fontWeight: 500

## Components

### Buttons
**`button-primary`** — The primary call-to-action is a solid, rectangular block of deep forest green (`{colors.primary}`) with cream text (`{colors.on-primary}`). Its zero-radius corners (`{rounded.none}`) are a deliberate departure from the site's softer interior elements, giving the action a decisive, no-nonsense quality. On hover, the button darkens to near-black (`{colors.primary-active}`), and in its disabled state it fades to a light gray (`{colors.primary-disabled}`) with muted text. The uppercase Jost button label at 15px with 0.5px letter-spacing reinforces the authoritative tone.

**`button-secondary`** — An outlined variant using the cream canvas background with dark green text. The border is 1px solid `{colors.primary}`. Hover fills the background with `{colors.surface-soft}`. Used for "Add to Wishlist" and secondary cart actions.

**`button-tertiary-text`** — A text-only link styled as a button, used for "View All" links in collection grids and "Learn More" in editorial sections. No background, no border — just the uppercase Jost label in `{colors.primary}`.

**`button-pill-accent`** — A small, fully rounded pill in brass (`{colors.accent-brass}`) used for sale callouts, "New Arrival" tags, and promotional badges. The dark green text on brass creates a warm, vintage-storefront feel.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.sm}` (4px) corners and no padding on the image area. The product image occupies the top portion at a 3:4 aspect ratio with its own `{rounded.sm}` on the top corners only. Below the image, the title sits in `{typography.title-sm}` and the price in `{typography.body-sm}` at `{colors.muted}`. On hover, a subtle box-shadow lifts the card. The card has no border — it relies on the contrast between the white surface and the cream canvas background.

**`sale-badge`** — A small, rectangular badge in terracotta (`{colors.accent-terracotta}`) with cream text. Positioned absolutely over the top-left corner of the product image. Uses `{typography.badge}` (11px uppercase Jost at 600 weight). No rounding — the sharp corner reinforces the urgency.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on the cream canvas background. The brand logo sits left-aligned, and navigation links use `{typography.nav-link}` — 14px uppercase Jost at 500 weight with 0.3px letter-spacing. On scroll, a subtle shadow (`0 1px 3px rgba(2,37,1,0.08)`) appears beneath the bar. The search icon is a standalone magnifying-glass glyph; on mobile, it expands into a full-width search field.

**`search-bar`** — An inline search field with `{rounded.none}`, set on `{colors.surface-soft}` with 8px vertical padding and 16px horizontal. On focus, a 1px solid `{colors.primary}` border appears. The placeholder text is `{colors.muted-soft}`.

### Forms
**`text-input`** — A rectangular input field on the cream canvas background with `{rounded.none}`. The default state has a 1px `{colors.hairline}` border. On focus, the border thickens to 2px `{colors.primary}`. Error state uses 2px `{colors.accent-terracotta}`. The input height is 48px with 12px vertical and 16px horizontal padding.

**`quantity-selector`** — A compact 44px tall input with `{rounded.none}` on a white background. Used on product detail pages for cart quantity adjustments. The minus and plus buttons sit flush against the input edges.

### Footer
**`footer`** — A full-width dark green (`{colors.primary}`) footer with cream text. Links are set in `{typography.link}` (14px Jost at 400 weight) and turn brass (`{colors.accent-brass}`) on hover. Section headings use `{typography.title-sm}` with uppercase transformation and 0.5px letter-spacing. The footer is divided into columns on desktop (Newsletter, Shop, About, Support) and collapses into an accordion on mobile.

**`accordion-trigger`** — Used in the mobile footer and product filters. A clickable row with the section title in `{typography.title-sm}` and a chevron icon that rotates on open. No background, no border — just the text and icon.

### Filters
**`filter-chip`** — A pill-shaped chip (`{rounded.full}`) on `{colors.surface-soft}` with body text. Used for size, color, and category filters on collection pages. Active state fills the chip with `{colors.primary}` and cream text. Height is 32px with 6px vertical and 16px horizontal padding.

**`breadcrumb`** — A simple text-based breadcrumb trail using `{typography.caption}` (13px Jost at 400 weight) in `{colors.muted}`. The current page is bolded at 500 weight in `{colors.body}`. Separators are `{colors.hairline}` slashes.

### Hero
**`hero-section`** — A full-bleed section with a minimum height of 400px, using `{colors.primary}` as the background color with cream text. A `{colors.primary}` overlay at 40% opacity sits over the background image to ensure text readability. The headline uses `{typography.display-xl}` (36px Jost at 500 weight). Padding is `{spacing.section}` (64px) top and bottom with `{spacing.lg}` (24px) on the sides.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; search icon expands to full-width field on tap; product cards go single-column; footer becomes accordion; hero section reduces to 300px min-height; filter chips wrap to two rows |
| Tablet | 744–1128px | Nav bar shows 4–5 links; product cards in 2-column grid; footer in 2-column layout; hero text reduces to 28px (`{typography.display-lg}`) |
| Desktop | 1128–1440px | Full nav bar with all links; product cards in 3-column grid; footer in 4-column layout; hero at full 400px min-height |
| Wide | > 1440px | Max-width container at 1440px with auto margins; product cards in 4-column grid; hero text scales to 42px |

### Touch Targets
- All interactive elements (buttons, links, filter chips, accordion triggers) have a minimum touch target of 44px height and 44px width where applicable.
- Nav bar links have 48px touch targets.
- Quantity selector buttons are 44px × 44px.
- Filter chips are 32px tall but have 44px clickable area via padding.

### Collapsing Strategy
- Primary nav collapses to hamburger menu at < 744px.
- Search bar collapses to icon-only at < 744px, expands on tap.
- Footer columns collapse to accordion at < 744px.
- Product filter sidebar collapses to a horizontal chip strip at < 744px, with a "Filters" button that opens a modal.
- Hero section reduces min-height from 400px to 300px on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (button-primary-hover, button-secondary-hover, product-card-hover) are inferred from common patterns, not extracted from the live site.
- Error styling for text inputs (text-input-error) is assumed based on the terracotta accent color — no form validation states were observed.
- Dark mode is not implemented; the brand uses a light-only palette.
- Sub-brand or seasonal palette variations (e.g., holiday collections) were not observed.
- The extracted hex list includes `#121212` and `#eeeeee` which may be Shopify framework defaults — they are used sparingly in the design system.
- Font sizes and line heights for typography tokens are estimated based on common Jost usage patterns; exact values from the live site could not be extracted.
- The `search-bar-focus` border width is assumed; no focus ring styles were observed.
- Animation durations and easing curves (e.g., for hover transitions, accordion open/close) were not extracted.
- The `hero-overlay` opacity (40%) is a reasonable assumption for readability; the exact value was not observed.
- Product card aspect ratio (3:4) is a common apparel standard; the exact ratio used on the site was not confirmed.
