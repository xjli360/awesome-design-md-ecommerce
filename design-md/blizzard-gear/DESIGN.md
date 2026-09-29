---
version: alpha
name: "Blizzard Gear"
source_url: "https://gear.blizzard.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A storefront built for the Warcraft, Overwatch, and Diablo faithful, where #790002 — a deep, dried-blood crimson — serves as the brand's primary voltage, appearing on CTAs, sale badges, and cart indicators against a canvas of #efefef and #dedede. The palette reads as a night-ops briefing: #2a2c32 and #232a39 form the nav and footer surfaces, while #f4bf2a (a muted gold) and #0074e0 (a cold alliance blue) act as faction-specific accents across product badges and category tags. Cards and containers use `{rounded.sm}` (8px) corners — crisp enough to feel precise, soft enough to avoid a military-hard edge. The typography, likely a system sans-serif stack, runs at moderate weights with generous line-height on body copy to keep long product descriptions readable against the dark backgrounds. Search bars and filter pills adopt `{rounded.full}` for a quick, friendly tap target, while the primary button sits at `{rounded.sm}` with a 48px height that feels substantial without overwhelming the grid. The overall mood is one of controlled intensity: the crimson never bleeds into the layout, the gold never glitters too brightly, and the white space around product images feels like a museum vitrine for collector's editions and faction-logo tees.

colors:
  primary: "#790002"
  primary-active: "#5c0001"
  primary-disabled: "#d9a0a0"
  ink: "#121212"
  body: "#2a2c32"
  muted: "#6a6a6a"
  muted-soft: "#8a8a8a"
  hairline: "#d9d9da"
  hairline-soft: "#e5e5e5"
  canvas: "#efefef"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#f4bf2a"
  accent-blue: "#0074e0"
  accent-red: "#bd3d44"
  dark-surface: "#232a39"
  dark-surface-strong: "#2b374c"
  dark-ink: "#192f5d"
  success-green: "#abf7b1"

typography:
  display-xl:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  link:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Blizzard Global', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
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
    rounded: "{rounded.sm}"
    padding: 14px 24px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-pill-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: "0 {spacing.lg}"
  nav-link-active:
    textColor: "{colors.accent-gold}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    margin: "{spacing.sm} 0 {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-faction:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 10px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "0 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.dark-surface-strong}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-gold}"
  hero-banner:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  cart-icon:
    textColor: "{colors.on-primary}"
    height: 24px
  cart-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the store, used for "Add to Cart", "Pre-Order", and "Checkout" flows. On hover, it deepens to `{colors.primary-active}` (#5c0001) and on disabled it fades to `{colors.primary-disabled}` (#d9a0a0) with reduced opacity. The 48px height and `{rounded.sm}` corners give it a solid, confident presence against the light canvas.

**`button-secondary`** — A bordered alternative for "View Details" and "Learn More" links within product cards. The 2px `{colors.hairline}` border keeps it visually lighter than the primary, while the active state swaps the border to `{colors.primary}` for emphasis. Hover fills the background with `{colors.surface-soft}`.

**`button-ghost`** — A text-only button used in navigation dropdowns and filter bars. No background or border, relying solely on `{colors.ink}` for legibility. Hover adds a subtle `{colors.surface-soft}` background for touch feedback.

**`button-pill-gold`** — A special accent button reserved for limited-time offers, battle-pass promotions, and Blizzard's seasonal events. The `{rounded.full}` pill shape and `{colors.accent-gold}` background signal urgency and exclusivity. Used sparingly to maintain its impact.

### Cards
**`product-card`** — The primary product display unit, a white card on `{colors.canvas}` with `{rounded.sm}` corners and 16px padding. The image sits at `{rounded.xs}` (4px) to keep focus on the product photography. Title uses `{typography.title-sm}` and price is rendered in `{colors.primary}` for immediate visual scanning. Hover state adds a subtle `{colors.hairline-soft}` border.

### Badges
**`badge-sale`** — A compact, high-contrast badge for discount indicators. The `{colors.primary}` background with white uppercase text at 11px fits neatly into the top-left corner of product images. Padding is tight (2px 8px) to avoid obscuring the product.

**`badge-new`** — A gold badge for "New Arrivals" and "Just Released" tags. Uses `{colors.accent-gold}` to differentiate from sale badges and to align with Blizzard's premium event styling.

**`badge-faction`** — A pill-shaped badge for faction-specific merchandise (Alliance, Horde, Overwatch teams). The `{colors.accent-blue}` is a starting point; actual faction colors may vary by game universe. The `{rounded.full}` shape makes it feel like a collectible pin.

### Navigation
**`nav-bar`** — A dark (`{colors.dark-surface}`) top bar at 64px height, housing the Blizzard logo, game franchise links, and utility icons (search, cart, account). Links are uppercase with 0.5px letter spacing for a gamer-branded feel. The active link uses `{colors.accent-gold}` to indicate the current section.

**`nav-link`** — Navigation items with generous horizontal padding (24px) for easy tapping. Hover state adds a subtle underline or background tint. The uppercase treatment and 600 weight give the nav a sense of authority.

### Forms
**`text-input`** — Standard input fields for search, email signup, and checkout forms. The 48px height matches button dimensions for consistent form rows. Focus state swaps to a 2px `{colors.primary}` border for clear keyboard focus indication.

**`search-bar`** — A full-rounded pill input for the main site search, placed in the nav bar or hero section. The `{rounded.full}` shape and 48px height make it feel approachable and quick. Focus state uses the primary crimson border.

**`filter-pill`** — Toggleable filter chips for product category pages (e.g., "T-Shirts", "Collectibles", "Hoodies"). Active state fills with `{colors.primary}` and white text, creating a clear selected/unselected distinction.

### Footer
**`footer`** — A dark (`{colors.dark-surface-strong}`) footer with links to support, privacy policy, and franchise pages. Links are `{colors.muted-soft}` on default and shift to `{colors.accent-gold}` on hover, maintaining the brand's accent hierarchy. Section padding (64px) gives breathing room for multi-column layouts.

### Hero
**`hero-banner`** — A full-width promotional banner for game launches and seasonal sales. The dark background (`{colors.dark-surface}`) makes product imagery and the `{colors.accent-gold}` CTA button pop. The title uses `{typography.display-xl}` at 32px for maximum impact.

### Cart
**`cart-icon`** — A simple icon in the nav bar, colored `{colors.on-primary}` for visibility against the dark nav. The accompanying `cart-badge` shows item count in a `{rounded.full}` pill with `{colors.primary}` background, positioned at the top-right of the icon.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards go single-column; hero banner reduces padding to 32px; search bar moves to a toggle icon; footer stacks vertically |
| Tablet | 744–1128px | Nav shows top-level links only; product cards display in 2-column grid; hero banner uses 48px padding; filter pills wrap to two rows |
| Desktop | 1128–1440px | Full nav with all links; 3-column product grid; hero banner at full padding (64px); filter pills in a single horizontal row |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 4 columns; hero banner may include background video or large imagery |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility.
- Filter pills are at least 40px tall with 16px horizontal padding for comfortable tapping.
- Nav links have 24px horizontal padding and 48px touch area.
- Search bar and text inputs are 48px tall for easy focus on mobile.

### Collapsing Strategy
- On mobile, the top navigation collapses into a hamburger menu with a slide-out drawer.
- The product filter strip collapses into a single "Filter" button that opens a modal or bottom sheet.
- The footer's multi-column layout collapses to a single column with expandable sections.
- Hero banner content stacks vertically, with the CTA button placed below the title and subtitle.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The exact font family could not be extracted from the live site; "Blizzard Global" is inferred from Blizzard's known brand guidelines. Fallback stacks are provided but should be verified against the actual CSS.
- Hover and focus states for many components (e.g., `product-card`, `nav-link`, `footer-link`) are inferred from common patterns and should be validated against the live store.
- Error states for form inputs (validation messages, error borders) were not observed and are not included.
- Dark mode preferences or themes are not accounted for; the current palette assumes a light canvas with dark nav/footer.
- The `badge-faction` color is a placeholder; actual faction colors (e.g., Horde red, Alliance blue, Overwatch orange) should be defined per game universe.
- The `hero-banner` may include video backgrounds or parallax effects that are not captured in the component tokens.
- Checkout flow components (payment forms, address fields, order summary) were not extracted and may have separate styling from the main store.
- The `quantity-selector` assumes a simple bordered input; the live site may use a stepper with plus/minus buttons.
