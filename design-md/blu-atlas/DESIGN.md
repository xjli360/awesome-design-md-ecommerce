---
version: alpha
name: "Blu Atlas"
source_url: "https://bluatlas.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A men's grooming brand that wraps its natural-ingredient promise in a high-contrast monochrome shell, where #141414 ink sits against #f6f6f6 canvas and the only color permission comes from product photography and the occasional green (#006400) or orange (#ee9441) accent in ingredient callouts. The site runs Instrument Sans and Instrument Serif — a contemporary sans/serif pair that gives editorial weight to product descriptions without feeling like a luxury fashion house. Buttons are flat, full-width rectangles with {rounded.sm} corners, no gradient, no shadow — the brand trusts its product shots and ingredient lists to do the selling. The top nav is a simple left-aligned logo with right-aligned utility links (Search, Account, Cart) in {colors.muted} text, and the product grid uses generous {spacing.xxl} gutters that let each bottle breathe. What stands out is the absence of typical men's-brand signifiers: no dark leather textures, no brushed metal, no "rugged" typography. Instead, Blu Atlas uses clean white space, serif body text at 16px, and a restrained palette where #c8c8c8 hairline lines separate sections. The brand's voice is clinical but warm — like a dermatologist who happens to write poetry about vitamin C serums.

colors:
  primary: "#141414"
  primary-active: "#000000"
  primary-disabled: "#545454"
  ink: "#141414"
  body: "#545454"
  muted: "#8b8b8b"
  muted-soft: "#c8c8c8"
  hairline: "#c8c8c8"
  hairline-soft: "#e2e2e2"
  canvas: "#f6f6f6"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#006400"
  accent-orange: "#ee9441"
  accent-bright-green: "#3ed660"
  accent-red: "#8b0000"

typography:
  display-xl:
    fontFamily: "'Instrument Serif', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Instrument Serif', Georgia, 'Times New Roman', serif"
    fontSize: 34px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Instrument Serif', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.15px
  badge:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Instrument Sans', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px

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
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.ink}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link:
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  nav-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  ingredient-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  rating-stars:
    textColor: "{colors.ink}"
    fontSize: 14px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site. A solid black (#141414) rectangle with {rounded.sm} corners and white text in Instrument Sans 15px/600. Used for "Add to Cart", "Subscribe & Save", and checkout flows. On hover, shifts to pure black (#000000) for subtle depth. Disabled state uses #545454 with reduced opacity, signaling the action is unavailable without visual noise. Full-width on mobile, auto-width on desktop.

**`button-secondary`** — A white button with dark text, used for secondary actions like "Learn More" or "View Ingredients". Same dimensions as primary but with a 1px hairline border (#c8c8c8) that disappears on hover as the button fills with #141414. The hover transition is a clean 200ms ease — no bounce, no scale.

**`button-outline`** — An outlined variant for tertiary actions in content-heavy sections. Transparent background with a 1px hairline border and dark text. Used in ingredient detail sections and FAQ accordion headers where a full button would compete with the content.

**`button-ghost`** — Text-only button for utility actions like "Clear filters" or "Cancel". No background, no border, just Instrument Sans 15px/600 in {colors.ink}. Hover adds a subtle underline or opacity shift.

### Cards
**`product-card`** — The core product display unit. A white card with {rounded.md} corners containing a product image, title in {typography.title-sm}, price in {typography.body-sm} at {colors.body}, and an optional badge. Cards sit in a responsive grid with {spacing.lg} gaps. No shadow — the brand relies on the product photography and clean layout for hierarchy. On hover, the image may scale 1.02x with a 300ms ease transform.

**`product-card-badge`** — A small green (#006400) pill badge with white uppercase text, positioned at the top-left of the product image. Used for "NEW", "BEST SELLER", or "LIMITED EDITION" labels. The badge is 11px/700 with 0.5px letter spacing, designed to be read at a glance without dominating the product photo.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on {colors.canvas} background. The logo sits left-aligned, with navigation links (Shop, Learn, About) and utility icons (Search, Account, Cart) right-aligned. Links use {typography.nav-link} at 14px/500 with 0.2px letter spacing. The active page link shifts from {colors.muted} to {colors.ink}. On scroll, a 1px bottom border in {colors.hairline-soft} appears.

**`nav-link`** — Navigation text links in {colors.muted} with {typography.nav-link}. Active state uses {colors.ink}. No underline decoration — the brand signals active state through color change alone.

### Forms
**`text-input`** — Standard text input for email signups, search, and checkout forms. A {colors.canvas} background with 1px {colors.hairline} border, {rounded.sm} corners, and 12px/16px padding. Focus state swaps the border to {colors.ink} for clear active indication. Error state would use {colors.accent-red} (#8b0000) border, though this wasn't confirmed on the live site.

**`select-input`** — Dropdown select styled identically to text inputs, used for quantity selectors and filter dropdowns. Same dimensions, border, and focus behavior.

### Footer
**`footer-section`** — A dark footer with {colors.ink} background and white text. Contains columns for product categories, customer service, and social links. Links use {colors.muted-soft} (#c8c8c8) at 14px/500. The footer is generously padded with {spacing.section} top and bottom, creating a clear visual break from the content above.

**`footer-link`** — Footer text links in {colors.muted-soft} with {typography.link}. On hover, shifts to white for clear interactive feedback.

### Hero
**`hero-section`** — The full-width hero area on the homepage and collection pages. Uses {colors.canvas} background with {typography.display-xl} in Instrument Serif 42px/400. The hero typically features a large product shot or lifestyle image on one side, with headline and {hero-cta} on the other. Padding of {spacing.section} top and bottom creates breathing room.

**`hero-cta`** — The primary button in hero sections, slightly wider than standard {button-primary} at 14px/32px padding. Same black background and white text, but with a more prominent visual weight to anchor the hero composition.

### Badges and Tags
**`ingredient-badge`** — Small pill-shaped tags used in ingredient lists and product detail sections. {colors.surface-soft} background with {colors.body} text in 12px/400. Used for labels like "Vitamin C", "Hyaluronic Acid", "Aloe Vera". The pill shape ({rounded.full}) with 6px/14px padding makes them feel like friendly, approachable tags rather than clinical labels.

**`rating-stars`** — Star rating display in {colors.ink} at 14px. Used on product cards and product detail pages. The brand uses a 5-star scale with half-star increments, rendered as inline SVG or Unicode characters.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero stacks vertically; buttons go full-width; font sizes reduce by 2-4px |
| Tablet | 744–1128px | Two-column product grid; nav shows limited links; hero maintains side-by-side layout at 50/50; buttons auto-width |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at 60/40 split; standard button sizing |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered; increased whitespace |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets include the entire card surface, not just the title/price
- Nav hamburger icon is 48px × 48px with 12px padding around the icon
- Quantity selectors in cart are 44px × 44px minimum
- Accordion headers are 48px tall with full-width tap targets

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-in drawer from the left
- Product grid collapses from 4 columns → 3 → 2 → 1 as viewport shrinks
- Hero section stacks vertically below 744px, with image above text
- Footer columns collapse from 4 → 2 → 1 column layout
- Ingredient badges wrap to multiple rows instead of a single horizontal scroll
- Accordion sections remain collapsed by default on mobile to reduce vertical scroll

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons were inferred from common patterns; the live site may use different transitions or color shifts
- Error states for form inputs (validation, error messages) were not observed on the live site
- The extracted hex list includes #8b0000 (red) and #006400 (green) which may be Shopify checkout widget colors rather than brand colors — their usage as accent colors is speculative
- Active/visited states for links were not confirmed
- Dark mode is not supported and was not observed
- Sub-brand or seasonal color palettes (if any) were not extracted
- The extracted font stack includes "Inter" which may be a system fallback rather than a primary brand font — Instrument Sans and Instrument Serif appear to be the intended pair
- Loading states (skeleton screens, spinners) were not observed
- Focus ring styles for keyboard navigation were not confirmed
- The brand's actual primary color may be a shade not captured in the extracted hex list — the extracted list appears dominated by generic web and checkout colors, with #141414 (black) being the most distinctive and likely primary
- Animation durations and easing curves were not extracted from the live site
