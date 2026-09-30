---
version: alpha
name: "Eggtronic"
source_url: "https://www.eggtronic.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A teal-and-aqua electronics brand that wraps its accessories in a surprising softness — #226d7a as the primary anchor, a deep teal that reads more like a tidepool than a tech spec, paired with a pale cyan #b0e0e9 that floods backgrounds and card surfaces. The palette is almost aquatic: #e4f5fa as the lightest canvas wash, #22b8d1 as a bright accent that pops against the deeper teal, and #1e6d7a as the active-state variant. Typography runs a conservative stack of Arial, Open Sans, Roboto, and sans-serif fallbacks — no proprietary brand typeface, suggesting a lean design operation that prioritizes clarity over typographic distinction. Buttons and badges use pill-shaped radii (`{rounded.full}`) that make even a charging-cable add-to-cart feel approachable, while product cards take a gentler curve (`{rounded.md}`) to frame device photos. The brand's voice is direct and utility-first — product titles in `{typography.title-md}` at 16px, specs in `{typography.body-sm}` at 14px — but the color story keeps it from feeling cold. The teal primary (#226d7a) appears on every primary CTA, the top nav background, and footer accents, while the pale cyan (#b0e0e9) softens the page chrome. It's a system that says "we sell phone cables and chargers" without shouting, using color temperature rather than typographic weight to signal warmth.

colors:
  primary: "#226d7a"
  primary-active: "#1e6d7a"
  primary-disabled: "#b0e0e9"
  ink: "#1a1a2e"
  body: "#2d3748"
  muted: "#718096"
  muted-soft: "#a0aec0"
  hairline: "#e2e8f0"
  hairline-soft: "#edf2f7"
  canvas: "#ffffff"
  surface-soft: "#e4f5fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-bright: "#22b8d1"
  accent-pale: "#b0e0e9"
  badge-new: "#22b8d1"
  badge-sale: "#226d7a"
  star-rating: "#226d7a"
  error: "#e53e3e"
  success: "#38a169"

typography:
  display-xl:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.25px
  link:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Open Sans', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.25px

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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-pill-accent:
    backgroundColor: "{colors.accent-bright}"
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
    backgroundColor: "{colors.canvas}"
  text-input-error:
    border: "1px solid {colors.error}"
    backgroundColor: "{colors.canvas}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-link-active:
    backgroundColor: "rgba(255,255,255,0.15)"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
    fontWeight: 600
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
    opacity: 0.85
  footer-link-hover:
    opacity: 1
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    height: 40px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in deep teal `{colors.primary}` (#226d7a) with white text and a pill-shaped `{rounded.full}` radius. On hover and active states, the background shifts to `{colors.primary-active}` (#1e6d7a) for a subtle darkening effect. The disabled state uses `{colors.primary-disabled}` (#b0e0e9), the pale cyan, which visually desaturates the button while maintaining the brand's aquatic palette. Height is 44px with 12px/28px padding, using `{typography.button-md}` at 15px semibold.

**`button-secondary`** — An outlined variant with a white background, `{colors.primary}` text, and a 2px solid border in the same teal. Active state fills the background with `{colors.surface-soft}` (#e4f5fa) and darkens the border to `{colors.primary-active}`. Used for "Learn More" and secondary product actions alongside primary CTAs.

**`button-tertiary-text`** — A text-only button with no background or border, using `{colors.primary}` text and `{typography.button-md}`. Used for "View All" links and inline actions where a full button would be visually heavy.

**`button-pill-accent`** — A smaller, brighter pill button using `{colors.accent-bright}` (#22b8d1) for promotional badges, "New Arrivals" filters, or sale callouts. Height is 36px with 8px/20px padding and `{typography.button-sm}`.

### Cards
**`product-card`** — A white card with `{rounded.md}` (12px) corners, 16px padding, and a subtle drop shadow (`0 1px 3px rgba(0,0,0,0.08)`). On hover, the shadow deepens to `0 4px 12px rgba(0,0,0,0.12)` to signal interactivity. The product image sits inside a `{rounded.sm}` (8px) container with a 1:1 aspect ratio. The title uses `{typography.title-sm}` in `{colors.ink}`, and the price is rendered in `{typography.body-md}` at 600 weight in `{colors.primary}`.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, filled with `{colors.primary}` (#226d7a) and white text. On scroll, the bar transitions to a white background with `{colors.ink}` text and a subtle bottom shadow. Navigation links use `{typography.nav-link}` at 14px semibold with 8px/16px padding. The active state adds a semi-transparent white background (`rgba(255,255,255,0.15)`) with `{rounded.sm}`.

### Forms
**`text-input`** — Standard text inputs with white background, `{colors.body}` text, and a 1px `{colors.hairline}` border with `{rounded.sm}` (8px). On focus, the border thickens to 2px and switches to `{colors.primary}`. Error state uses a red border (`{colors.error}`). Height is 44px with 10px/16px padding.

**`search-bar`** — A pill-shaped search input (`{rounded.full}`) at 48px height with a white background, `{colors.body}` text, and a 1px hairline border. Focus state thickens the border to 2px `{colors.primary}`. Used in the navigation and on category pages.

### Badges
**`badge-new`** — A small pill badge using `{colors.accent-bright}` (#22b8d1) background with white text, `{typography.badge}` (11px uppercase semibold), and `{rounded.full}`. Used to flag newly added products.

**`badge-sale`** — Same shape as `badge-new` but using `{colors.primary}` (#226d7a) background. Used for discount callouts.

**`badge-out-of-stock`** — Uses `{colors.muted-soft}` (#a0aec0) for a neutral, low-contrast out-of-stock indicator.

### Footer
**`footer`** — A full-width footer with `{colors.primary}` background, white text, and 48px/24px padding. Links use `{typography.link}` at 14px with 0.85 opacity, increasing to full opacity on hover. The footer contains site navigation, legal links, and social icons.

### Category Chips
**`category-chip`** — Filter chips for product categories, using `{colors.surface-soft}` (#e4f5fa) background with `{colors.primary}` text and `{rounded.full}`. Active state fills the chip with `{colors.primary}` and white text. Height is 32px with 6px/16px padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces full nav bar, category chips stack vertically, footer collapses to stacked links, product cards use full-width images, search bar reduces to icon-only |
| Tablet | 744–1128px | Two-column product grid, nav bar shows condensed links (icons + labels), category chips wrap in a horizontal scroll, footer splits into two columns |
| Desktop | 1128–1440px | Three-column product grid, full nav bar with all links visible, category chips display in a single row, footer uses four-column layout |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, nav bar spans full width with increased padding, footer columns expand |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Category chips at 32px height are below the 44px recommendation — consider increasing to 36–40px on mobile
- Product card tap targets (add-to-cart, quick-view) are at least 44px × 44px
- Nav bar links have 48px minimum touch area (64px bar height with 8px padding)
- Quantity selector buttons at 40px height — borderline for touch, acceptable with adequate spacing

### Collapsing Strategy
- Top nav collapses from full link text to icon-only on tablet, then to hamburger menu on mobile
- Product grid collapses from 4 columns (wide) → 3 (desktop) → 2 (tablet) → 1 (mobile)
- Category chip strip collapses from single row to horizontal scroll on tablet, then to vertical stack on mobile
- Footer collapses from 4 columns → 2 columns → stacked single column
- Search bar collapses from full input to icon-only on mobile, expanding on tap
- Product card image and text layout remains consistent across breakpoints — only the grid column count changes

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components were inferred from common patterns — the live site's actual hover transitions, focus rings, and active states could not be extracted
- Error states for forms (validation messages, error icons) were not present in the extracted data
- The font-family declarations found (Arial, Open Sans, Roboto, sans-serif) are generic — the brand may use a custom typeface that wasn't loaded on the extracted page (which returned a 403 Forbidden error)
- The extracted hex colors are limited to 5 values and may not represent the full brand palette — missing secondary accents, gradient stops, and semantic colors (success, warning, info)
- No dark mode or high-contrast mode tokens were found
- The 403 Forbidden page means the extracted data may not reflect the actual product pages, checkout flow, or marketing content
- Spacing and typography scale values are estimated based on common e-commerce patterns — the brand's actual spacing system may differ
- No animation or transition timing values were extracted (ease curves, durations)
- Icon system (SVG vs icon font, stroke weights, sizes) was not captured
- Product card hover states (quick-add, wishlist, zoom) are speculative
- No data on modal, drawer, or overlay components
- Checkout flow components (cart, payment forms, shipping selectors) were not accessible
