---
version: alpha
name: "Rogue Fitness"
source_url: "https://www.roguefitness.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A black-and-steel ecosystem built for maximum force transfer — #3000ba, a deep electric violet that reads as neither corporate nor playful, serves as the brand's single voltage spike against a near-monochrome palette of #222927, #303634, and #212121. This is not a gym brand that uses red for urgency or green for "go" — it uses violet because the brand is the authority, not the cheerleader. The canvas is #f8f8f8, not pure white, giving the entire site a workshop-floor patina that matches the raw steel of a Monster rack or a Ohio barbell. Type runs Industry Ultra at display sizes — a condensed, squared-off sans that looks stamped into metal — paired with Roboto Condensed for body and navigation, creating a two-tier system where headlines shout and everything else steps back. Corners are nearly all hard: buttons use {rounded.sm} (4px), cards use {rounded.xs} (4px), and only the search bar and badge pills break to {rounded.full}. The color #c2003a appears as a limited alert accent, #53b82e as a stock-status green, but neither competes with the violet — the system trusts that one color to carry every primary CTA, every "Shop Now" link, every add-to-cart button. Spacing is generous but not luxurious: {spacing.lg} (24px) between sections, {spacing.base} (16px) inside cards, and {spacing.section} (64px) between major page blocks. The nav bar sits at 60px, dense with category links and a search bar that collapses on mobile. This is a brand that sells 500-pound squat racks — the design doesn't need to be friendly. It needs to be credible.

colors:
  primary: "#3000ba"
  primary-active: "#260095"
  primary-disabled: "#9880dd"
  ink: "#222927"
  body: "#303634"
  muted: "#666b69"
  muted-soft: "#7d827f"
  hairline: "#d2d2d2"
  hairline-soft: "#e9e9e9"
  canvas: "#f8f8f8"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#c2003a"
  accent-red-active: "#ea0000"
  stock-green: "#53b82e"
  stock-green-active: "#5bbd15"
  badge-warning-bg: "#fff3cd"
  badge-warning-text: "#2d2d2d"
  link-blue: "#005cb2"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Industry Ultra', 'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Industry Ultra', 'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 36px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Industry Ultra', 'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 28px
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Industry Ultra', 'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 22px
    fontWeight: 900
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', 'Roboto', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Roboto Condensed', 'Arial Narrow', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
  top-nav:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  top-nav-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
  top-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  sub-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
  sub-nav-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  sub-nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 0px
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  product-card-badge-stock:
    backgroundColor: "{colors.stock-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: 64px 24px
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 32px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
  badge-warning:
    backgroundColor: "{colors.badge-warning-bg}"
    textColor: "{colors.badge-warning-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
  badge-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart," "Shop Now," and "View Details" on product cards and hero sections. Rendered in the brand violet {colors.primary} with white text, hard 4px corners, and uppercase Roboto Condensed at 700 weight. On hover, shifts to {colors.primary-active} (#260095); disabled state uses {colors.primary-disabled} (#9880dd). Height is 44px with 12px vertical padding.

**`button-secondary`** — Used for secondary actions like "Learn More" or "Compare" on category pages. White background with {colors.ink} text, same 44px height and uppercase treatment. Active state uses {colors.surface-soft} background. Outline variant (`button-outline`) uses a transparent background with a 1px solid {colors.hairline} border.

**`button-pill`** — A pill-shaped variant reserved for filter tags, category pills, and mobile navigation chips. Uses {rounded.full} with smaller padding (8px 20px) and {typography.button-sm}. Outline version available for unselected filter states.

### Cards
**`product-card`** — The primary product display unit across catalog, search results, and category pages. A white card with {rounded.xs} corners, no padding at the container level — the image fills the top edge-to-edge with {rounded.xs} applied to the image wrapper. Title uses {typography.title-sm} at 16px, price uses {typography.price} at 18px bold. Badges overlay the top-left corner of the image.

**`product-card-badge`** — Small uppercase pill badges that communicate product status. Three variants: default (violet background for "New" or "Bestseller"), sale (red background {colors.accent-red} for "Sale" or "Clearance"), and stock (green background {colors.stock-green} for "In Stock" or "Low Stock"). All use {typography.badge} at 11px uppercase with 0.5px letter-spacing.

### Navigation
**`top-nav`** — The primary site navigation, a dark bar at 60px height on {colors.ink} background. Links are uppercase Roboto Condensed at 15px, white by default, switching to {colors.primary} on active/current page. The Rogue logo sits left, category links span the center, and the search bar + cart icon sit right.

**`sub-nav`** — A secondary navigation bar at 48px height on white background, used for category sub-pages (e.g., "Bars," "Plates," "Racks"). Links are muted by default, switching to {colors.ink} for the active section. No background color change on hover — only text color shifts.

### Forms
**`text-input`** — Standard text input for search, account forms, and checkout fields. White background, 44px height, 4px corners, 10px 16px padding. Focus state uses a 2px solid {colors.primary} border (not defined in tokens but standard across the site).

**`search-bar`** — The site search input, rendered as a pill with {rounded.full} on white background at 40px height. Placeholder text in {colors.muted}. On focus, text switches to {colors.ink} and a subtle shadow appears. Typically paired with a magnifying glass icon in {colors.muted}.

### Footer
**`footer`** — A dark footer section on {colors.ink} background with 48px padding top/bottom. Links are {colors.muted-soft} by default, switching to white on hover. Organized in columns: "Shop," "Support," "About," and "Connect." Includes social icons and a copyright line in {colors.muted}.

### Hero
**`hero-banner`** — Full-width hero sections on homepage and campaign pages. Dark background ({colors.ink}) with white text using {display-xl} at 48px. CTA button uses {button-primary} sizing but with 32px horizontal padding for visual weight. May include a secondary tagline in {typography.body-md} below the headline.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product cards go single-column; hero text reduces to {display-lg} (36px); search bar hides behind icon; footer columns stack |
| Tablet | 744–1128px | Top nav shows limited links (5-6); product cards in 2-column grid; sub-nav scrolls horizontally; hero maintains full-width but text reduces to {display-md} (28px) |
| Desktop | 1128–1440px | Full nav visible; product cards in 3-4 column grid; sub-nav fully visible; hero at full size |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-5 column grid; hero content centered with max-width |

### Touch Targets
- All buttons and links maintain minimum 44px height for touch accessibility
- Product card tap targets (title, price, image) are at least 48px
- Filter pills and badge pills are minimum 32px height
- Search bar is 40px height on all breakpoints

### Collapsing Strategy
- Top nav collapses to hamburger at < 744px; flyout menu slides from left
- Sub-nav scrolls horizontally on tablet and mobile; no wrapping
- Product grid collapses from 5 columns (wide) to 1 column (mobile)
- Footer columns stack at < 744px; accordion pattern for mobile (expandable sections)
- Hero banner reduces font size progressively; CTA button remains full-width on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs, links, and buttons are inferred from common patterns — exact color values for focus rings, shadows, and transitions were not extractable from static CSS
- Error state styling for forms (red borders, error message typography) not observed
- Dark mode or high-contrast mode tokens not present in extracted data
- Sub-brand palettes (Rogue Monster, Rogue Ohio, Rogue Echo) may use distinct accent colors — not captured
- The extracted hex list includes several colors (#aaaeb7, #c6c7c8, #939594, #959595) that appear to be stock-image dominant tones or checkout-widget colors — not included in the core palette
- Font weights for Industry Ultra (900) and Roboto Condensed (700) are confirmed; exact weights for Open Sans body text (400) are inferred
- Spacing values for card padding, grid gaps, and section margins are estimated from layout patterns — exact values may vary by page
- Animation durations, easing curves, and transition properties not extracted
- Icon system (SVG vs icon font, stroke weights, sizes) not documented
- Print stylesheet and reduced-motion preferences not observed
