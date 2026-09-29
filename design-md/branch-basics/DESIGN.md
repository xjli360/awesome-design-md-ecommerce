---
version: alpha
name: "Branch Basics"
source_url: "https://branchbasics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A cleaning brand that trusts a single red-orange voltage — #ff5742 — to cut through a landscape of muted grays, off-whites, and warm charcoal. That accent appears on the primary CTA, on the "Shop Now" button in the hero, and on the tiny dot that marks the active step in a product carousel; everywhere else, the palette stays deliberately quiet, with #f6f6f6 and #fafafa as the canvas and #141412 as the ink. The brand runs Brown as its display face — a rounded, slightly condensed sans-serif that feels domestic rather than clinical — paired with Inter for body copy, a move that splits the difference between friendly and legible. Product photography is bright, flat-lit, and compositionally simple: a bottle of concentrate against a white background, a spray nozzle isolated on a marble slab. The site uses generous vertical spacing (section-level gaps of 64px or more) and soft card radii ({rounded.md} ~12px) to keep the experience from feeling like a hardware store. The checkout flow, powered by Shopify, introduces a secondary accent — #4efac0, a minty teal — on the "Pay now" button and on progress indicators, a surprising shift that signals transaction completion with a different emotional register than the red-orange of browsing.

colors:
  primary: "#ff5742"
  primary-active: "#e63e2a"
  primary-disabled: "#ffb3a6"
  ink: "#141414"
  body: "#545454"
  muted: "#868a89"
  muted-soft: "#9da1a0"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#fafafa"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-mint: "#4efac0"
  accent-blue: "#0018ff"
  accent-green: "#00b84a"
  accent-red: "#e61b1b"
  badge-new: "#ff5742"
  badge-sale: "#0018ff"

typography:
  display-xl:
    fontFamily: "'Brown', Helvetica, 'Inter', system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Brown', Helvetica, 'Inter', system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Brown', Helvetica, 'Inter', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Brown', Helvetica, 'Inter', system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Brown', Helvetica, 'Inter', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Brown', Helvetica, 'Inter', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Helvetica', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-lg:
    fontFamily: "'Brown', Helvetica, 'Inter', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Brown', Helvetica, 'Inter', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Brown', Helvetica, 'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', 'Helvetica', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Brown', Helvetica, 'Inter', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', 'Helvetica', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    padding: 14px 28px
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
    padding: 13px 27px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-mint:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-active:
    borderColor: "{colors.primary}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  text-input-error:
    borderColor: "{colors.accent-red}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 80px 0
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  search-bar-active:
    borderColor: "{colors.primary}"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-panel:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  rating-stars:
    color: "{colors.ink}"
    size: 16px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-mint:
    backgroundColor: "{colors.hairline}"
    fillColor: "{colors.accent-mint}"
    rounded: "{rounded.full}"
    height: 4px
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    activeColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, filled with #ff5742 and white text. Used for "Add to Cart", "Subscribe & Save", and primary checkout actions. On hover, shifts to `{colors.primary-active}` (#e63e2a). Disabled state uses `{colors.primary-disabled}` (#ffb3a6) with reduced opacity. The button uses `{rounded.sm}` (8px) — not pill-shaped — to keep the brand feeling grounded and practical rather than overly friendly.

**`button-secondary`** — White background with `{colors.ink}` text, used for "Learn More" and secondary product actions. Has a 1px `{colors.hairline}` border. Hover adds a subtle shadow. The outline variant (`button-secondary-outline`) uses a transparent background with a 2px `{colors.ink}` border for use on dark or colored surfaces.

**`button-mint`** — A secondary accent button using `{colors.accent-mint}` (#4efac0) with dark text. Reserved for checkout confirmation steps and "Complete Order" actions. This color shift from red-orange to mint teal signals a transition from browsing to purchasing.

**`button-pill-primary`** — A smaller, fully rounded variant (`{rounded.full}`) used for filter tags, category pills, and mobile navigation items. Uses `{typography.button-sm}` with tighter padding.

### Cards
**`product-card`** — White card with `{rounded.md}` (12px) corners and a 1:1 aspect ratio product image. The image sits flush to the top with `{rounded.md}` on top corners, while the bottom section contains title, price, and optional badge. Cards have a subtle shadow on hover. The badge uses `{colors.primary}` background with white uppercase text for "NEW" or "BEST SELLER" labels.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height on desktop, collapsing to 64px on scroll. White background with centered logo and left/right link groups. The logo uses `{typography.display-sm}` in `{colors.ink}`. On mobile, the nav collapses to a hamburger menu with a full-screen overlay drawer.

### Forms
**`text-input`** — White input field with `{rounded.sm}` corners and 1px `{colors.hairline}` border. Focus state shows a 2px `{colors.primary}` border. Error state uses `{colors.accent-red}` (#e61b1b) border with red helper text below. Input labels use `{typography.caption}` in `{colors.muted}`.

### Footer
**`footer-section`** — Dark footer with `{colors.ink}` background and white text. Contains four columns: product links, company info, support, and newsletter signup. Links use `{colors.muted-soft}` (#9da1a0) and lighten to white on hover. The newsletter input uses a dark variant of `{text-input}` with a `{colors.primary}` submit button.

### Accordion
**`accordion-trigger`** — Used for FAQ sections and product details. The trigger is a full-width clickable row with `{typography.title-sm}` and a chevron icon that rotates on open. The panel below uses `{typography.body-md}` with `{colors.body}` text and 16px bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to `{typography.display-lg}`; buttons become full-width; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav links reduce to icon-only; hero uses `{typography.display-xl}` at smaller scale; footer shows two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with text links; hero uses full `{typography.display-xl}`; footer shows four columns |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid can expand to four columns; hero uses larger padding |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile
- Icon-only buttons have a minimum touch area of 44x44px
- Accordion triggers have 48px minimum height for easy tapping
- Quantity selector buttons are 40x40px minimum
- Product card CTAs are 48px tall

### Collapsing Strategy
- Top nav collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer columns collapse from 4 to 2 on tablet, 1 on mobile
- Hero section reduces padding from 80px to 48px on mobile
- Multi-step checkout collapses to single-page scroll on mobile
- Accordion panels are collapsed by default on all breakpoints

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site; the above states are inferred from common patterns
- Error styling for forms (validation messages, error icons) is not fully documented
- Dark mode is not present on the live site and is not defined
- Sub-brand or seasonal color palettes (e.g., holiday collections) could not be extracted
- Animation and transition timing values (durations, easing curves) are not available
- The exact font weight for "Brown" is uncertain; the extracted CSS shows "Brown" but does not specify weights beyond 500 and 700
- The `#4efac0` mint accent appears only in the checkout flow and may be a Shopify theme default rather than a brand color
- The `#0018ff` blue appears in extracted colors but its usage is unclear — may be a link color or a secondary accent
- Spacing values for specific components (e.g., gap between product cards) are inferred from common patterns
- The exact line-height and letter-spacing values for typography are estimated from common web practices, as the extracted CSS did not include these properties
