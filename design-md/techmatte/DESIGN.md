---
version: alpha
name: "TechMatte"
source_url: "https://www.techmatte.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A blue-and-red voltage system built for utility-first mobile accessories, where #0e6eb8 acts as the primary anchor — a confident, mid-tone corporate blue that appears across primary buttons, category headers, and the site's top navigation bar. The brand's secondary heartbeat is #e94b35, a sharp safety-orange red used sparingly for sale badges, price-drop indicators, and limited-time callouts, creating a clear urgency hierarchy against the cooler blue backdrop. The palette relies heavily on a neutral spine of #808080 (muted text and secondary icons), #c4c4c4 (hairlines and dividers), and a clean white canvas, with #337ab7 serving as a lighter hover-state blue for interactive elements. Typography defaults to system sans-serif stacks (no custom font found), keeping the interface fast-loading and legible across the budget-electronics demographic. Product cards use soft {rounded.sm} corners, while primary CTAs and the search bar adopt {rounded.md} for a slightly friendlier feel without sacrificing the brand's no-nonsense, protective-film precision. The overall mood is functional and alert — a brand that sells screen protectors and car mounts with the same straightforward urgency as an auto-parts store, using color contrast (blue/orange) rather than typographic flourish to drive action.

colors:
  primary: "#0e6eb8"
  primary-active: "#0a5a9a"
  primary-disabled: "#8bb8e0"
  ink: "#222222"
  body: "#333333"
  muted: "#808080"
  muted-soft: "#a0a0a0"
  hairline: "#c4c4c4"
  hairline-soft: "#d8d8d8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#e94b35"
  accent-sale-hover: "#c93a28"
  accent-sale-disabled: "#f4a89c"
  link-hover: "#337ab7"
  star-rating: "#f5a623"
  badge-new: "#0e6eb8"
  badge-sale: "#e94b35"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 6px
  md: 10px
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
    rounded: "{rounded.md}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-sale-hover:
    backgroundColor: "{colors.accent-sale-hover}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
    padding: 4px 0
  button-text-link-hover:
    textColor: "{colors.link-hover}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.body}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-sale}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-sale}"
    fontWeight: 700
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 14px
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
  category-tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  category-tab-inactive:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.base}"
    minHeight: 300px
  hero-banner-cta:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: "12px 32px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in `{colors.primary}` with white text and `{rounded.md}` corners. On hover, it shifts to `{colors.primary-active}` for a darker, more grounded state. The disabled variant uses `{colors.primary-disabled}` to signal inactivity without visual noise. Used for "Add to Cart," "Shop Now," and primary form submissions.

**`button-secondary`** — An outlined variant with a `{colors.primary}` border and transparent fill, maintaining the same `{rounded.md}` shape and `{typography.button-md}` sizing. Hover fills the background with `{colors.surface-soft}` and darkens the border to `{colors.primary-active}`. Used for "Learn More," "View Details," and secondary checkout actions.

**`button-sale`** — A compact, high-urgency button in `{colors.accent-sale}` (safety orange-red) with smaller padding and `{typography.button-sm}`. Hover deepens to `{colors.accent-sale-hover}`. Used exclusively for limited-time offers, flash sales, and price-drop CTAs.

**`button-text-link`** — A minimal, borderless text button using `{typography.link}` in `{colors.primary}`. Hover shifts to `{colors.link-hover}`. Used for "See All," "Read Reviews," and inline navigation prompts.

### Cards
**`product-card`** — A white card with a `{colors.hairline-soft}` border and `{rounded.sm}` corners, containing a square product image, title, and price. Hover elevates with a subtle drop shadow and a `{colors.hairline}` border. The image area uses `{colors.surface-soft}` as a placeholder background. Price text uses `{typography.body-md}` with `fontWeight: 600`, while sale prices switch to `{colors.accent-sale}` and `fontWeight: 700`.

**`badge-new`** and **`badge-sale`** — Small, uppercase badges using `{typography.badge}` (11px, bold, uppercase) with `{rounded.xs}` corners. The "New" badge uses `{colors.badge-new}` (blue), while the "Sale" badge uses `{colors.badge-sale}` (orange-red). Positioned at the top-left of product card images.

### Navigation
**`top-nav`** — A 64px white bar with a `{colors.hairline}` bottom border, housing the brand logo and navigation links in `{typography.nav-link}`. Active links are underlined with a 2px `{colors.primary}` border-bottom and colored `{colors.primary}`. Inactive links remain `{colors.body}`. The nav is sticky on desktop, collapsing to a hamburger menu on mobile.

**`category-strip`** — A horizontal scrollable strip with `{colors.surface-soft}` background, containing pill-shaped category tabs. Active tabs fill `{colors.primary}` with white text; inactive tabs are white with a `{colors.hairline}` border. All tabs use `{rounded.full}` for a friendly, touch-friendly shape.

### Forms
**`text-input`** — A standard input field with `{colors.canvas}` background, `{colors.hairline}` border, and `{rounded.sm}` corners. On focus, the border thickens to 2px and turns `{colors.primary}`. Error state uses a 2px `{colors.accent-sale}` border. Height is 44px for comfortable touch interaction.

**`search-bar`** — A 40px input with `{colors.surface-soft}` background and `{colors.hairline}` border, using `{rounded.md}` corners. On focus, the background turns white and the border becomes a 2px `{colors.primary}` line. Uses `{typography.body-sm}` for placeholder and input text.

### Hero & Footer
**`hero-banner`** — A full-width section with `{colors.primary}` background and white text, using `{typography.display-lg}` for headline copy. Minimum height of 300px with generous `{spacing.section}` vertical padding. Contains a single `{colors.accent-sale}` CTA button for maximum contrast.

**`footer`** — A dark section with `{colors.ink}` background and white text, using `{typography.body-sm}`. Links are `{colors.muted-soft}` and hover to white. Padding is `{spacing.xl}` vertical with `{spacing.base}` horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), hamburger nav replaces top-nav, category-strip becomes horizontally scrollable, hero-banner min-height reduces to 200px, footer stacks links vertically |
| Tablet | 744–1128px | Two-column product grid (2 cards), top-nav remains but with condensed link text, category-strip shows 4-5 visible tabs, hero-banner min-height at 250px |
| Desktop | 1128–1440px | Three-column product grid (3 cards), full top-nav with all links visible, category-strip shows 6+ tabs, hero-banner at full 300px min-height |
| Wide | > 1440px | Four-column product grid (4 cards), max-width container at 1440px, hero-banner expands to 350px min-height with larger typography |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Category tabs in the strip are minimum 36px tall with 16px horizontal padding
- Search bar and text inputs are 40-44px tall
- Product card tap targets (image, title, price) are minimum 48px in their interactive zones
- Navigation links have 48px minimum tap area (padding + height)

### Collapsing Strategy
- Top navigation collapses to a hamburger icon below 744px, with a full-screen overlay menu
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Category strip becomes horizontally scrollable on mobile, with visible scroll indicators
- Footer link columns stack vertically on mobile, with expandable accordion sections for link groups
- Hero banner reduces typography size and min-height on mobile, with CTA button remaining full-width
- Product card badges reposition to top-left on all breakpoints, but reduce font size on mobile (10px)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font-family declarations were extracted from the live site; the system sans-serif stack is an assumption based on common e-commerce patterns. The brand may use a custom typeface not detectable in the extracted CSS.
- Hover states for `button-secondary`, `button-text-link`, and `product-card` are inferred from common interaction patterns, not extracted from live CSS.
- Error styling for forms (red border on `text-input-error`) is a standard convention, not confirmed from the live site.
- Dark mode is not implemented; no color tokens exist for dark backgrounds or inverted text.
- The extracted hex colors (#0e6eb8, #e94b35, #808080, #337ab7, #c4c4c4) appear to be a generic web palette — a corporate blue, a safety orange, and three neutrals. No distinctive brand-specific colors (pink, sage, terracotta, etc.) were found. The primary (#0e6eb8) and accent (#e94b35) are the most distinctive choices in the list and are used as the brand's core voltage.
- No Shopify-specific checkout colors (Shopify Pay green, Klarna pink, Afterpay black) were detected, suggesting the brand may use a custom checkout or a different e-commerce platform.
- Star rating color (#f5a623) is a common yellow-gold convention, not confirmed from extracted data.
- Spacing and rounded values are estimated based on common e-commerce design patterns; exact values may differ on the live site.
- No animation or transition timings were extracted; all motion is assumed to use 200-300ms ease-in-out where applicable.
- The `hero-banner` component's min-height and padding are estimates; the live site may use different proportions.
- No sub-brand or seasonal color palettes were detected.
