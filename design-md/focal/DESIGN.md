---
version: alpha
name: "Focal"
source_url: "https://www.focal.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A precision audio brand where the interface steps back to let product photography and technical specifications command attention, built on a restrained palette anchored by #111827 ink and #2563eb accent — the single blue voltage that appears only in primary CTAs, active navigation states, and select technical callouts. The system runs Gotham at moderate weights (400–500 for body, 700 for display) with monospace fallbacks for specifications and pricing, signaling engineering rigor without sacrificing readability. Product pages use generous white space (#ffffff canvas) and hairline-thin #e5e7eb borders to separate technical specifications, creating a clean, almost architectural grid that mirrors the precision of the company's studio monitors. The #2563eb accent is deployed sparingly — it never appears in decorative elements, only in functional affordances like "Add to Cart" buttons and product configuration selectors, maintaining a sense of purposeful restraint. Secondary text at #6b7280 and #9ca3af provides hierarchy without competing with the hero imagery, while #f8f8f8 surface-soft backgrounds create subtle section breaks in long-form product descriptions. The overall impression is that of a technical catalog rendered with editorial care — the brand trusts its product's physical design to do the emotional work, and the interface exists primarily to organize information with clarity.

colors:
  primary: "#2563eb"
  primary-active: "#1d4ed8"
  primary-disabled: "#93c5fd"
  ink: "#111827"
  body: "#374151"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#d1d5db"
  hairline-soft: "#e5e7eb"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#2563eb"
  accent-blue-hover: "#1d4ed8"
  star-rating: "#f59e0b"
  error: "#dc2626"
  success: "#16a34a"
  badge-new: "#2563eb"
  badge-sale: "#dc2626"
  footer-bg: "#1f2937"
  footer-text: "#d1d5db"

typography:
  display-xl:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "'SFMono-Regular', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "'SFMono-Regular', 'Consolas', 'Liberation Mono', monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "1px solid {colors.error}"
    rounded: "{rounded.sm}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.08)"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.price-sm}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
  hero-title:
    typography: "{typography.display-xl}"
    marginBottom: "{spacing.lg}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-value}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  spec-table-row:
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-label:
    typography: "{typography.spec-label}"
    color: "{colors.muted}"
    padding: "{spacing.md} {spacing.base}"
  spec-table-value:
    typography: "{typography.spec-value}"
    color: "{colors.body}"
    padding: "{spacing.md} {spacing.base}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.footer-text}"
  footer-link-hover:
    color: "{colors.canvas}"
  footer-heading:
    typography: "{typography.micro-label}"
    color: "{colors.canvas}"
    marginBottom: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
  breadcrumb:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  breadcrumb-active:
    color: "{colors.ink}"
    typography: "{typography.caption}"
  breadcrumb-separator:
    color: "{colors.hairline}"
    padding: "0 {spacing.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "0 0 {spacing.base} 0"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline-soft}"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  rating-count:
    typography: "{typography.caption}"
    color: "{colors.muted}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm} 0 0 {rounded.sm}"
    padding: "10px 14px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "0 {rounded.sm} {rounded.sm} 0"
    padding: "10px 20px"
    height: 44px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in #2563eb with white text and {rounded.sm} corners. Used exclusively for "Add to Cart", "Buy Now", and primary form submissions. On hover, shifts to #1d4ed8 (`{colors.primary-active}`). Disabled state uses #93c5fd (`{colors.primary-disabled}`) with white text, signaling the action is unavailable without visual noise.
**`button-secondary`** — An outlined variant with white background, ink text, and a 1px #d1d5db border. Used for secondary actions like "Learn More", "Configure", and "Compare". Active state fills the border to ink. Hover adds a subtle shadow.
**`button-tertiary-text`** — A text-only button in #2563eb with no background or border. Used for inline actions like "View Details", "Read Reviews", and "See All Specifications". Active state shifts to #1d4ed8.

### Cards
**`product-card`** — A clean white card with {rounded.md} corners and no background fill beyond the product image. The image occupies the top portion at a 4:3 aspect ratio with rounded top corners. Title uses {typography.title-sm} and price uses {typography.price-sm}, both left-aligned with {spacing.base} padding. On hover, a subtle box shadow lifts the card. Badges (New, Sale) appear as small {rounded.xs} pills in the top-left corner of the image area.
**`product-card-badge`** — A compact {rounded.xs} pill in #2563eb with white text, set in {typography.badge} (11px, uppercase, 0.5px letter-spacing). Used for "New", "Limited Edition", and "Award Winner" flags. Sale badges use #dc2626 instead.

### Navigation
**`nav-bar`** — A 72px white bar with a 1px #e5e7eb bottom border. Links are set in {typography.nav-link} (14px, uppercase, 0.5px letter-spacing). Active links show a 2px #2563eb bottom border and ink color; inactive links use #6b7280. The bar becomes sticky on scroll with a subtle shadow.
**`breadcrumb`** — A secondary navigation path using {typography.caption} (13px, 0.2px letter-spacing) in #6b7280. Active (current) segment uses ink. Separators are #d1d5db with {spacing.sm} horizontal padding.

### Forms
**`text-input`** — A 44px tall input with white background, {rounded.sm} corners, and a 1px #d1d5db border. Focus state thickens the border to 2px and shifts to #2563eb. Error state uses a 1px #dc2626 border. Placeholder text uses {colors.muted-soft}.
**`select-dropdown`** — Matches text-input styling with a custom dropdown arrow. Used for product configuration (color, size, model) and filtering.
**`quantity-selector`** — A horizontal control with increment/decrement buttons flanking a central value display. All segments share {rounded.sm} corners and a 1px #d1d5db border. Buttons use {surface-soft} background.

### Footer
**`footer`** — A dark section (#1f2937 background) with white text at {typography.body-sm}. Links use #d1d5db and shift to white on hover. Section headings use {typography.micro-label} (12px, uppercase, 0.3px letter-spacing) in white. The newsletter input combines a standard text input (left, {rounded.sm} left corners) with a primary button (right, {rounded.sm} right corners) for a seamless join.

### Product Detail
**`spec-table`** — A bordered table with {rounded.sm} corners and 1px #e5e7eb row dividers. Labels use {typography.spec-label} (12px, uppercase, monospace) in #6b7280. Values use {typography.spec-value} (14px, monospace) in #374151. Each row has {spacing.md} vertical padding.
**`accordion`** — A vertically stacked disclosure pattern with a 1px #e5e7eb bottom border per item. Headers use {typography.title-sm} (16px, 500 weight). Content uses {typography.body-sm} (14px) in #374151 with {spacing.base} bottom padding.
**`tab-bar`** — A horizontal tab strip with a 1px #e5e7eb bottom border. Active tab shows a 2px #2563eb bottom border and ink text. Inactive tabs use #6b7280 text. All tabs use {typography.nav-link} (14px, uppercase).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; product cards stack vertically; nav-bar collapses to hamburger menu; spec-table becomes stacked rows; hero section reduces padding to 48px; font sizes scale down one step (display-xl → display-lg); footer links stack in single column |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows top-level links only; spec-table remains full-width but reduces horizontal padding; hero uses 60px section padding; search bar moves to nav-bar |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with dropdowns; spec-table uses two-column layout; hero uses 80px section padding; side-by-side product detail layout |
| Wide | > 1440px | Max-width container at 1440px; four-column product grid; additional whitespace around hero; spec-table can expand to three-column layout for complex products |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height
- Icon-only buttons use 44x44px touch targets even if the visible icon is smaller
- Product card CTAs are at least 44px tall with 16px horizontal padding
- Accordion headers are 48px tall for easy tapping
- Tab labels have 16px horizontal padding and 12px vertical padding

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px, with a full-screen overlay menu
- Product filters collapse to a "Filter" button that opens a bottom sheet on mobile
- Spec tables collapse to label-value pairs stacked vertically on mobile
- Footer link columns collapse to a single column on mobile, with accordion-style section headers
- Product image galleries collapse to a single-column swipeable carousel on mobile
- Tab bars collapse to a horizontal scrollable strip on mobile (no wrapping)
- Accordion content collapses by default on all breakpoints, expanding on click

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary buttons, text inputs, and select dropdowns could not be reliably extracted from static CSS; the active states above are inferred from common patterns
- Error styling for forms (error messages, error iconography) was not visible in the extracted data; #dc2626 is assumed for error borders based on convention
- Dark mode styling is not present on the live site; no dark mode tokens are defined
- Sub-brand or product-line-specific color palettes (e.g., for K2, Utopia, or other headphone lines) were not extractable; the system uses a single brand palette
- Animation and transition durations/easings were not extractable; a standard 200ms ease-in-out is assumed for all interactive states
- Dropdown menu styling for navigation (mega menu, flyout) was not visible in the extracted HTML/CSS
- The extracted hex list is dominated by grays (#6b7280, #111827, #374151, #d1d5db, #e5e7eb, #4b5563, #9ca3af, #555555, #1f2937) with a single blue accent (#2563eb) and two near-whites (#f8f8f8, #f3f4f6). This is consistent with a technical/audio brand but the palette is generic — the brand's true visual identity may include additional accent colors (e.g., copper, orange, or green for specific product lines) that were not present in the extracted CSS
- Font-family declarations included Gotham, monospace fallbacks, and system fonts; exact font weights and sizes for all typography tokens were inferred from common patterns rather than extracted from live CSS
- Checkout flow styling (cart, payment, confirmation) was not extractable; the brand may use a third-party checkout that introduces its own design system
