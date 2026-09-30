---
version: alpha
name: "Welly"
source_url: "https://getwelly.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A bright, clinical-coded wellness brand that uses a deep teal (#0a413b) as its structural anchor — the color of a pharmacist’s apron or a vintage medicine bottle — then breaks the tension with a neon-lime accent (#c8e302) that reads as energy, not caution. The palette is deliberately small: a near-black ink (#121212), a single warm gray (#dedede), and two electric secondary greens (#009a87, #3effe9) that suggest healing and vitality without falling into pastel wellness cliché. White canvas (#ffffff) carries the bulk of the experience, with teal used for primary CTAs, navigation bars, and footer blocks — the brand trusts color-blocking over heavy typography to signal hierarchy. Buttons are softly rounded ({rounded.sm}) and pill-shaped search bars ({rounded.full}) give the interface a friendly, over-the-counter accessibility. Product cards use generous whitespace and a single hairline (#dedede) to separate items, avoiding the visual clutter common in supplement retail. The brand’s voice is direct and mildly playful — “Get better faster” — and the design mirrors that: clean enough to feel trustworthy, bright enough to not feel medicinal.

colors:
  primary: "#0a413b"
  primary-active: "#003e37"
  primary-disabled: "#a0c5c1"
  ink: "#121212"
  body: "#2d2d2d"
  muted: "#6b6b6b"
  muted-soft: "#a0a0a0"
  hairline: "#dedede"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-lime: "#c8e302"
  accent-teal: "#009a87"
  accent-cyan: "#3effe9"
  accent-green: "#00d300"
  badge-new: "#c8e302"
  badge-sale: "#0a413b"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0

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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-accent:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "#b0cc02"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  button-pill-accent:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid #d32f2f"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.title-md}"
    textColor: "{colors.accent-green}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
    opacity: 0.85
  search-bar-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-pill-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  rating-stars:
    color: "{colors.accent-lime}"
    fontSize: 16px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  accordion-header:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.md} 0"
  accordion-body:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    padding: "0 0 {spacing.md} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Subscribe", and "Shop Now" actions. Rendered in the brand's deep teal (#0a413b) with white text and a soft 8px radius. On hover, shifts to the darker active state (#003e37). Disabled state uses a muted teal (#a0c5c1) with white text, maintaining readability while signaling inactivity. Height is 44px with 12px/24px padding for comfortable tap targets.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". Uses a white background with a 2px teal border and teal text. Active state darkens the border and text to #003e37 with a light gray background. Maintains the same 44px height and 8px radius as the primary button for visual consistency.

**`button-accent`** — The high-energy variant reserved for promotional CTAs, limited-time offers, and loyalty program sign-ups. Uses the neon-lime (#c8e302) background with dark ink (#121212) text — the highest contrast combination in the system. Active state darkens to #b0cc02. Use sparingly to preserve its attention-grabbing power.

**`button-pill-primary`** and **`button-pill-accent`** — Compact, fully rounded pills (9999px radius) used for filter tags, category navigation, and inline subscription prompts. At 36px height with 10px/20px padding, these are smaller than full-size buttons but maintain the same color logic. The accent pill is particularly effective for "Best Seller" or "New" filter toggles.

### Cards
**`product-card`** — The primary product display unit, used in grid layouts, carousels, and search results. A white card with a 12px radius and 16px padding, containing a product image (8px radius), badge, title, and price. On hover, a subtle box shadow lifts the card. The badge uses the neon-lime background with uppercase 11px bold type for "NEW" or "SALE" indicators. Sale prices are rendered in the accent green (#00d300) to draw the eye.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height with a white background. Contains the brand logo on the left, navigation links in the center (Shop, Learn, About, Help), and utility icons (Search, Account, Cart) on the right. On scroll, gains a subtle box shadow. Active nav links are underlined in the brand teal. On mobile, collapses to a hamburger menu with a full-screen overlay drawer.

### Forms
**`text-input`** — Standard text input for search, email sign-up, and checkout forms. White background with a 1px hairline border and 8px radius. On focus, the border thickens to 2px and switches to the brand teal. Error state uses a red border (#d32f2f). Height is 44px with 12px/16px padding for comfortable typing.

### Hero
**`hero-section`** — The primary brand storytelling block, typically the first thing users see on the homepage. A deep teal (#0a413b) background with white text, using the largest display type (36px) for the headline and standard body copy for the subheading at 85% opacity. Contains a white pill-shaped search bar and one or two primary CTAs. Padding is 64px vertical and 24px horizontal.

### Footer
**`footer`** — A full-width footer in the brand teal with white text. Contains columns for product categories, company info, customer support, and social links. Footer links are white at 80% opacity, increasing to full opacity on hover. Uses body-sm typography (14px) for a clean, uncluttered appearance. Padding is 48px vertical and 24px horizontal.

### Category Pills
**`category-pill`** — Horizontal scrolling filter pills for product categories (First Aid, Pain Relief, Cold & Flu, etc.). Light gray background (#f5f5f5) with dark body text, fully rounded. Active state switches to the brand teal with white text. At 36px height with 8px/16px padding, these are compact enough to show 6-8 items on a single row.

### Accordion
**`accordion-header`** and **`accordion-body`** — Used for FAQ sections and product details. Headers use title-md (16px, semibold) with a chevron icon that rotates on expand. Body content uses body-sm (14px) with 16px bottom padding. No background or border — relies entirely on typographic hierarchy and spacing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card), hamburger nav, hero text shrinks to 24px, category pills scroll horizontally, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid, nav links visible but condensed, hero maintains 28px heading, category pills in a 2-row wrap |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links, hero at full 36px heading, category pills in a single row |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero content centered with wider padding |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Category pills at 36px height are supplemented with 8px padding for tap comfort
- Product card tap targets (Add to Cart, Quick View) are minimum 44x44px
- Nav bar icons (Search, Account, Cart) are 44x44px tap areas with 24px icons
- Accordion headers have 44px minimum tap height

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Hero section reduces heading size and stacks CTA buttons vertically below 744px
- Footer columns collapse to a single vertical stack below 744px
- Category pills switch from single-row scroll to 2-row wrap below 744px
- Search bar reduces from full-width to icon-only trigger below 600px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family declarations were found on the live site; Inter is assumed as a common modern sans-serif, but the actual brand font may differ. Verify with the brand team.
- Hover and active states for most components (beyond buttons) could not be reliably extracted from static CSS.
- Error state styling for forms (beyond the red border) is inferred — actual error messages, icons, and animation timing are unknown.
- Dark mode is not present on the live site and has not been designed.
- Sub-brand or seasonal color palettes (e.g., holiday promotions, limited-edition products) were not observed.
- The extracted hex list included several greens (#009a87, #3effe9, #00d300) that may serve specific functional roles (sale prices, progress bars, success states) but their exact usage could not be confirmed.
- Animation and transition timing values (durations, easing functions) were not extractable from the static analysis.
- The checkout flow (Shopify-powered) likely introduces additional UI components (payment buttons, address forms) that follow Shopify's default styling rather than the brand system.
