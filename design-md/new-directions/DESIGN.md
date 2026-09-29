---
version: alpha
name: "New Directions"
source_url: "https://www.ndbooks.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A small press that builds its digital presence on a foundation of deep, quiet grays — #111827 for the heaviest ink, #374151 for body text — against a stark white canvas (#ffffff). The palette is almost entirely achromatic, with the single exception of a pale, watery blue (#5bbad5) that appears in select links and accents, and a more saturated blue (#2d89ef) for interactive elements. This restraint is the brand's signature: the site trusts typography and generous whitespace over decorative color. Raleway, a geometric sans-serif with a subtle humanist warmth, carries the full typographic load at modest weights (400 for body, 600–700 for display). The design avoids hard corners in interactive elements — buttons use {rounded.sm} (8px), while search fields and badges use {rounded.full} (9999px) — but the overall grid and card structure is rectilinear, creating a tension between soft interaction points and a rigid editorial grid. The result is a site that feels like a well-designed book: quiet, confident, and entirely focused on the text.

colors:
  primary: "#5bbad5"
  primary-active: "#2d89ef"
  primary-disabled: "#9ca3af"
  ink: "#111827"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d1d5db"
  hairline-soft: "#e5e7eb"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#2d89ef"
  accent-red: "#e3342f"
  accent-dark: "#1f2937"
  border-strong: "#4b5563"
  dark-surface: "#1f2228"

typography:
  display-xl:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
    borderBottom: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 0
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} 0 {spacing.xxs} 0"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.xs} 0 0 0"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 32px
    height: 48px
  badge-new:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  footer-section:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    padding: 4px 0
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
    rounded: "{rounded.full}"
  category-tab-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    padding: 8px 16px
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Subscribe", and "Shop Now" actions. Uses the brand's pale blue accent (#5bbad5) on a white background with uppercase Raleway at 14px/600. On hover/active, shifts to a more saturated blue (#2d89ef). Disabled state drops to a muted gray (#9ca3af). All variants share an 8px corner radius and 44px height.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". Uses a 2px solid ink (#111827) border on a transparent background. On hover/active, inverts to a solid ink fill with white text. Shares the same 44px height and uppercase typography as the primary button.

**`button-ghost`** — A minimal text button for tertiary actions like "Cancel" or "Clear filters". No background, no border — just the body gray (#374151) at 12px/600 uppercase. Used in forms and filter panels where visual weight should be minimal.

### Cards
**`product-card`** — The core content unit for the book catalog. A rectilinear container with no border radius, relying on generous whitespace and a 3:4 aspect ratio product image. The title uses title-md (18px/600), the author sits in body-sm (14px/400) in muted gray (#6b7280), and the price returns to body-md (16px/400) in ink (#111827). No shadow, no border — the card is defined entirely by the grid.

**`product-card-image`** — The book cover image fills the full width of the card at a 3:4 aspect ratio. No border radius, no shadow. The cover art is the only decorative element on the card.

### Navigation
**`nav-bar`** — A fixed-height (72px) white bar with a thin bottom border (#e5e7eb). Contains the brand logo on the left and navigation links on the right. Links use uppercase Raleway at 14px/500 in muted gray (#6b7280), switching to ink (#111827) with a 2px bottom border on the active page.

**`nav-link`** — Individual navigation items with 8px/12px padding. Inactive state is muted gray; active state adds a 2px ink bottom border. No background change on hover — the brand trusts the text color shift alone.

### Forms
**`text-input`** — Standard text input for search, email signup, and checkout forms. White background with a 1px hairline border (#d1d5db). On focus, the border shifts to ink (#111827). Uses body-md (16px/400) for input text with 12px/16px padding.

**`search-bar`** — A pill-shaped search input (9999px radius) for the site search. Same structure as the text input but with full rounding and 20px horizontal padding. The pill shape is the only fully rounded element in the UI, creating a distinctive interaction point.

### Badges
**`badge-new`** — A small, fully rounded pill badge for "New" or "Just Published" labels. Uses the accent red (#e3342f) on white for urgency. 11px/700 uppercase Raleway with 2px/8px padding.

**`badge-sale`** — Similar structure to badge-new but uses the saturated blue (#2d89ef) for sale or discount indicators.

**`badge-category`** — A softer badge for category filters or tags. Uses a light gray background (#f9fafb) with muted gray text (#6b7280). 4px/12px padding for a slightly larger hit area.

### Footer
**`footer-section`** — A dark footer (#1f2228) with muted gray text (#9ca3af). Links sit in the same muted gray and shift to white on hover. The footer uses body-sm (14px/400) for all text, maintaining the brand's typographic hierarchy even in the darkest section of the site.

### Dividers
**`divider`** — A 1px line in hairline gray (#d1d5db) for strong visual separation between sections.

**`divider-soft`** — A 1px line in soft hairline gray (#e5e7eb) for subtle separation within sections.

### Category Strip
**`category-strip`** — A horizontal scrollable strip of category filters below the hero. Uses button-sm (12px/600 uppercase) in muted gray. Active categories invert to a solid ink pill (#111827) with white text, using full rounding (9999px) for a soft, tactile feel.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid for product cards; nav collapses to hamburger menu; hero text reduces to display-md (24px); category strip becomes horizontally scrollable with no visible overflow |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but reduce font size to 12px; hero uses display-lg (28px); category strip shows 4–5 visible tabs |
| Desktop | 1128–1440px | Three-column product grid; full nav with 14px links; hero uses display-xl (36px); category strip shows 6–8 visible tabs |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centers content; hero text scales to 40px; additional whitespace on left/right margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Category tabs have 32px minimum height with 16px horizontal padding
- Search bar maintains 48px height for easy thumb targeting
- Product card links have 44px minimum hit area, extending beyond the text bounds

### Collapsing Strategy
- Navigation links collapse into a hamburger menu below 744px
- Product grid collapses from 4 columns to 1 column below 744px
- Category strip becomes horizontally scrollable below 744px, with fade indicators on left/right edges
- Footer link columns collapse to a single column below 744px
- Hero section reduces padding from 80px to 40px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted from the static CSS; the active/hover variants documented above are inferred from common patterns and should be verified against the live site's interactive behavior
- Error states for form inputs (validation errors, required field indicators) were not present in the extracted data
- Dark mode preferences or alternate color schemes were not detected
- The exact font weight for Raleway in body text could not be confirmed; 400 is assumed based on common web typography patterns
- The brand's true primary color is ambiguous — the extracted palette contains multiple blues (#5bbad5, #2d89ef, #034ad8, #0284c7, #1a4db3) and one red (#e3342f), suggesting the site may use different accent colors for different sections or that some colors belong to third-party widgets (Shopify checkout, social icons). #5bbad5 was selected as primary because it is the most distinctive and least generic of the blues, but this should be verified against the brand's actual design guidelines
- Sub-brand or series-specific color palettes (e.g., for specific book collections or imprints) were not detected
- Animation and transition timings (hover transitions, page load animations) were not captured
- Focus ring styles and keyboard navigation indicators were not present in the extracted data
- The exact line-height values for body text are inferred from common web typography and may differ from the live site's actual implementation
- Shopify checkout widget colors may be mixed into the extracted palette; the accent red (#e3342f) and some blues may belong to payment buttons rather than the brand's design system
