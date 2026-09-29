---
version: alpha
name: "Barefoot Sound"
source_url: "https://www.barefootsound.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A studio-monitor manufacturer that builds its visual identity around the precision and materiality of its own products — the palette is drawn directly from the anodized aluminum, brushed steel, and matte black enclosures of the monitors themselves. The dominant hex #d0d0d0 (a cool, mid-tone silver-gray) acts as the brand's neutral canvas, while #2a2a2a and #1e1e1e provide deep, near-black surfaces that evoke the anechoic chambers and acoustically treated rooms where these monitors live. The brand's voltage comes from two accents: #1863dc, a confident engineering blue used sparingly for interactive elements and technical callouts, and #178087, a teal that appears in product highlights and secondary CTAs — both colors feel lab-tested rather than market-tested. Typography runs Lato at moderate weights (400–700), with display sizes staying lean at 24–32px and body copy at 15–16px; there is no decorative type, no script, no display face — every character serves clarity. Corners are almost universally sharp: `{rounded.none}` on cards, `{rounded.xs}` (4px) on buttons, and only the occasional `{rounded.sm}` (8px) on input fields. The brand trusts its product photography — extreme macro shots of tweeter domes, waveguide contours, and amplifier heatsinks — to carry the emotional weight, keeping UI chrome minimal and structural. The result is a system that feels less like a consumer electronics storefront and more like a precision instrument catalog: quiet, dense with information, and utterly unapologetic about its technical audience.

colors:
  primary: "#1863dc"
  primary-active: "#0757fe"
  primary-disabled: "#949494"
  ink: "#1e1e1e"
  body: "#2a2a2a"
  muted: "#555555"
  muted-soft: "#949494"
  hairline: "#d0d0d0"
  hairline-soft: "#eeeeee"
  canvas: "#f0f0f0"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#178087"
  accent-orange: "#de4528"
  accent-green: "#00d084"
  steel: "#d0d0d0"
  dark-steel: "#444444"
  deep-charcoal: "#1e1f26"
  badge-error: "#de4528"
  badge-success: "#00d084"

typography:
  display-xl:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0
  spec-label:
    fontFamily: "'Lato', 'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
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
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-accent-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
  product-card-image:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "12px 24px"
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
  spec-table-row:
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  pagination-button-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  pagination-button-disabled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in `{colors.primary}` (#1863dc) with white text on a sharp `{rounded.xs}` (4px) corner. Hover state shifts to `{colors.primary-active}` (#0757fe), a deeper, more saturated blue that feels like a button being pressed into a metal chassis. Disabled state drops to `{colors.primary-disabled}` (#949494), a mid-gray that signals non-interactivity without visual noise.

**`button-secondary`** — An outlined variant using `{colors.ink}` (#1e1e1e) for both text and a 2px border on a transparent background. Active state inverts to a solid `{colors.ink}` fill with white text. Used for "Learn More" and "Compare" actions where the primary blue would compete with adjacent UI.

**`button-tertiary-text`** — A text-only link styled as a button, using `{colors.primary}` for the text and no background or border. Reserved for secondary actions within product cards and spec tables where space is tight.

**`button-accent-teal`** and **`button-accent-orange`** — Specialty buttons for promotional or alert contexts. The teal variant (`{colors.accent-teal}` #178087) appears on "New Arrival" banners and pre-order flows; the orange variant (`{colors.accent-orange}` #de4528) is reserved for "Sale" and limited-edition drops. Both use the same `{rounded.xs}` geometry as the primary button.

### Cards
**`product-card`** — A completely flat, border-only container with `{rounded.none}` and a 1px `{colors.hairline-soft}` (#eeeeee) stroke. The card relies entirely on its content — product photography, title, price, and optional badge — for visual hierarchy. Hover state thickens the border to `{colors.hairline}` (#d0d0d0), a subtle cue that the card is interactive. No shadow, no elevation, no gradient.

**`product-card-badge`** — A small, `{rounded.xs}` pill attached to the top-left of the product image, using `{colors.accent-teal}` for "New" and `{colors.accent-orange}` for "Sale". Typography is `{typography.badge}` (11px, uppercase, 700 weight) with tight 2px vertical padding.

### Navigation
**`top-nav`** — A 72px fixed-height bar on `{colors.canvas}` (#f0f0f0) with a single `{colors.hairline}` bottom border. Navigation links use `{typography.nav-link}` (14px, 600 weight, uppercase, 0.5px letter spacing) — the uppercase treatment gives the nav a technical, engineering-catalog feel. Active links render in `{colors.primary}`, inactive in `{colors.muted}` (#555555).

**`nav-link-active`** and **`nav-link-inactive`** — No background change, no underline, no pill — just a color shift from muted to primary. The brand trusts the user to know where they are through page context rather than persistent visual indicators.

### Forms
**`text-input`** — A 44px-tall input with `{rounded.xs}`, a 1px `{colors.hairline}` border, and `{colors.canvas}` background. Focus state thickens the border to 2px of `{colors.primary}`, a clear but understated interaction cue. Error state uses a 2px `{colors.badge-error}` (#de4528) border — no icon, no background tint, just the line.

**`select-input`** — Identical geometry to `{text-input}` but with a custom dropdown arrow (not specified here, but assumed to be a chevron in `{colors.muted}`). No rounded corners on the dropdown menu itself — `{rounded.none}`.

**`textarea`** — Same border and background treatment as `{text-input}`, but without a fixed height. Padding is consistent at 12px 16px.

### Hero
**`hero-section`** — A full-width section on `{colors.ink}` (#1e1e1e) with white text, using `{typography.display-xl}` (32px, 700 weight) for the headline and `{typography.body-md}` (16px) for the subtitle in `{colors.muted-soft}` (#949494). The hero CTA is a standard `{button-primary}` placed below the subtitle. No background image overlay, no gradient — the dark canvas is the backdrop.

### Spec Table
**`spec-table`** — A flat, border-only table with `{rounded.none}` and a 1px `{colors.hairline-soft}` stroke. Rows are separated by the same hairline. Labels use `{typography.spec-label}` (11px, uppercase, 700 weight, 0.5px letter spacing) in `{colors.muted}`, while values use `{typography.spec-value}` (22px, 700 weight) in `{colors.ink}`. The contrast between the tiny label and the large value creates a technical, data-sheet rhythm.

### Footer
**`footer`** — A dark section on `{colors.ink}` with text in `{colors.muted-soft}` (#949494). Links use `{typography.link}` (14px, 400 weight) and shift to white on hover. No social icons, no newsletter signup — just links, legal text, and the brand name in the bottom-left corner.

### Badges
**`badge-new`**, **`badge-sale`**, **`badge-out-of-stock`** — Small `{rounded.xs}` labels with 2px vertical padding, using `{typography.badge}` (11px, uppercase, 700 weight). Green for new, orange for sale, gray for out-of-stock. These are the only decorative elements in the system — everything else is structural.

### Search & Filters
**`search-bar`** — A 44px input with `{rounded.xs}`, matching `{text-input}` geometry. Focus state uses the same 2px `{colors.primary}` border. No search icon inside the input by default — the brand may place a magnifying glass icon to the left or right depending on layout.

**`filter-chip`** — A `{rounded.full}` pill with a 1px `{colors.hairline}` border on `{colors.canvas}`. Active state fills with `{colors.primary}` and inverts the text to white. Used in category and spec-filter strips above product grids.

### Pagination
**`pagination-button`** — A `{rounded.xs}` square button (approximately 32px × 32px) with a 1px `{colors.hairline}` border. Active state fills with `{colors.primary}`; disabled state drops to `{colors.muted-soft}` text and `{colors.hairline-soft}` border. No rounded corners on the pagination container — just a flat row of buttons.

### Accordion
**`accordion-header`** — A full-width clickable row with `{colors.ink}` text in `{typography.title-sm}` (16px, 600 weight) and a `{colors.hairline-soft}` bottom border. No background change on hover — the cursor change is the only affordance. The body uses `{typography.body-sm}` (14px) with `{colors.body}` (#2a2a2a) text and standard padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger; product cards go single-column; hero section reduces padding to 32px vertical; spec tables scroll horizontally; filter chips wrap to two rows; footer stacks links vertically |
| Tablet | 744–1128px | Top nav shows 4–5 links; product cards in 2-column grid; hero padding at 48px vertical; spec tables remain full-width; filter chips in single row with horizontal scroll |
| Desktop | 1128–1440px | Full top nav with all links; product cards in 3-column grid; hero padding at 64px vertical; spec tables at max 800px width centered; filter chips in single row |
| Wide | > 1440px | Content max-width at 1440px centered; product cards in 4-column grid; hero padding at 80px vertical; all other layouts scale proportionally |

### Touch Targets
- All interactive elements (buttons, links, inputs, chips) maintain a minimum 44px × 44px touch target on mobile
- Filter chips use 36px height on mobile (below the 44px guideline) — this is a known gap
- Pagination buttons are 32px × 32px on all breakpoints — below the 44px touch target on mobile
- Product card CTAs ("Add to Cart", "Learn More") are 44px tall on all breakpoints

### Collapsing Strategy
- Top nav collapses to a hamburger menu at < 744px, with the full link list in a slide-out drawer
- Product card grids collapse from 4 columns (wide) → 3 (desktop) → 2 (tablet) → 1 (mobile)
- Spec tables collapse to horizontally scrollable containers on mobile, with the first column (label) frozen
- Filter chip strips collapse from single row → horizontally scrollable row → wrap to two rows on the smallest screens
- Footer link columns collapse from 4 columns (desktop) → 2 columns (tablet) → single column (mobile)
- Hero sections reduce vertical padding by 50% on mobile but maintain full-width layout

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from the extracted palette and common patterns — the live site may use different transitions, durations, or color shifts
- Error styling for forms (text-input-error) is assumed based on the extracted `#de4528` — the actual error state may include icons, helper text, or background tints
- Dark mode is not present in the extracted data — the brand may not support it, or it may be toggled via a mechanism not captured
- The extracted font list includes "Indie Flower", "Oswald", and "Oxygen" — these are likely from third-party widgets or checkout flows, not the brand's primary type system. Lato is the assumed primary based on frequency and brand context
- The extracted hex list contains many generic web colors (#00d084, #0693e3, #ff9900, #02e49b) that are likely from Shopify Pay, Klarna, or social icon sets — these have been excluded from the primary palette but retained as accent/badge tokens where they appeared frequently
- Sub-brand or product-line-specific palettes (e.g., for the "MicroMain" vs. "Footprint" series) are not captured — the brand may use different accent colors per product line
- The `{rounded.full}` token is defined but rarely used in components — the brand may use pill shapes for filter chips and search bars, but the extracted data suggests a strong preference for `{rounded.xs}` and `{rounded.none}`
- Animation and transition timings (hover fade, menu slide, card entrance) are not specified — the brand likely uses 150–300ms ease-in-out transitions based on common practice
- The brand's logo and icon system (if any) is not captured — the top nav may include a logo mark with specific dimensions and spacing
- Checkout flow components (cart, checkout button, payment form) are not included — the brand may use a third-party checkout (Shopify, etc.) with its own design system
