---
version: alpha
name: "Hismile"
source_url: "https://www.hismileteeth.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Hismile is a vibrant, unapologetically playful oral-care brand that rejects clinical sterility in favor of candy-bright energy and Gen Z-friendly confidence. The palette is anchored by a shocking pink `#ff9cdc` and electric yellow `#ffd801` that feel more like a dessert brand than a toothpaste company — a deliberate signal that whitening and hygiene can be fun. Supporting accents of mint green `#7ae28d`, teal `#59cdc9`, and lavender `#d298f9` appear in product badges, gradient backgrounds, and limited-edition packaging, creating a rainbow ecosystem that makes each SKU feel collectible. The canvas is a warm off-white `#fffee9` rather than pure white, softening the overall feel, while ink text sits at `#222222` for strong readability against bright backgrounds. Typography leans on two distinct voices: PP Right Grotesk for bold, oversized headlines that shout confidence, and Pulp for clean, approachable body copy. Rounded corners are generous — buttons use `{rounded.sm}` (8px) while product cards and modals take `{rounded.md}` (12px) or `{rounded.lg}` (20px) — reinforcing a tactile, squishy, "friendly" feel. The brand makes heavy use of pill-shaped elements (`{rounded.full}`) for CTAs, search bars, and swatch badges, mirroring the shape of a toothpaste tube or a smile. Every design decision — from the `#ff3b30` error red to the `#4caf50` success green — feels lifted from a mobile game or a direct-to-consumer snack brand, not a dental aisle. The result is a system that prioritizes joy, shelf standout, and shareability over traditional "clean white" healthcare tropes.

colors:
  primary: "#ff9cdc"
  primary-active: "#e87bbf"
  primary-disabled: "#ffd1e8"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#929292"
  hairline: "#cccccc"
  hairline-soft: "#e0e0e0"
  canvas: "#fffee9"
  surface-soft: "#f2f2f7"
  surface-card: "#ffffff"
  on-primary: "#222222"
  accent-yellow: "#ffd801"
  accent-green: "#7ae28d"
  accent-teal: "#59cdc9"
  accent-lavender: "#d298f9"
  badge-yellow: "#ffef29"
  badge-green: "#4caf50"
  error: "#ff3b30"
  star-rating: "#ffd801"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'PP Right Grotesk', 'PP Right Grotesk Narrow Medium', Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'PP Right Grotesk', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'PP Right Grotesk', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'PP Right Grotesk', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Pulp', 'Circular', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Pulp', 'Circular', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Pulp', 'Circular', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Pulp', 'Circular', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Pulp', 'Circular', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0
  badge:
    fontFamily: "'Pulp', 'Circular', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Pulp', 'Circular', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Pulp', 'Circular', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  link:
    fontFamily: "'Pulp', 'Circular', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Pulp', 'Circular', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 52px
    border: "2px solid {colors.hairline}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-pill-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 0px
    border: "1px solid {colors.hairline-soft}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  product-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 56px
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheadline:
    typography: "{typography.display-sm}"
    textColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  star-rating:
    color: "{colors.star-rating}"
    fontSize: 16px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The flagship CTA, rendered in Hismile's signature pink `#ff9cdc` with dark `#222222` text for high contrast. Uses a pill shape (`{rounded.full}`) and generous 52px height to feel tactile and pressable. On hover, shifts to `{colors.primary-active}` (`#e87bbf`); disabled state fades to `{colors.primary-disabled}` (`#ffd1e8`) with muted text. **`button-secondary`** — An outlined variant on a warm canvas background, with a 2px hairline border and full pill rounding. Used for "Learn More" or secondary actions alongside the primary. **`button-accent-yellow`** — A high-energy alternative CTA using the brand's signature yellow `#ffd801`, often deployed for "Shop Now" or limited-edition drops. **`button-pill-ghost`** — A minimal ghost button with a thin border, used for filters, tags, or tertiary actions in dense UI.

### Cards
**`product-card`** — A white card with soft `{rounded.lg}` (20px) corners and a subtle hairline border. Contains product imagery, title, price, and a star rating. Hover state adds a drop shadow and slight scale. **`product-card-badge`** — A small pill badge overlaid on product cards, using `{colors.accent-yellow}` for "Best Seller" or "New" labels. Uses `{typography.badge}` (11px uppercase). **`product-swatch`** — A 32px circular swatch for flavor/color selection (e.g., Mint, Charcoal, Watermelon). Uses `{rounded.full}` and a thin border.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height on a warm canvas background `#fffee9`. Logo sits left, nav links center, cart icon right. Active link uses pink underline. On mobile, collapses to a hamburger menu with a full-screen overlay. **`nav-link-active`** — Active state with pink text and a 2px bottom border in `{colors.primary}`.

### Forms
**`text-input`** — Standard input with 48px height, `{rounded.sm}` corners, and a 1px hairline border. On focus, border thickens to 2px and turns pink. Placeholder text uses `{colors.muted}`. Error state uses `{colors.error}` border and helper text.

### Search
**`search-bar`** — A pill-shaped search field (`{rounded.full}`) at 56px height, used in the hero and mobile nav. Includes a magnifying glass icon and placeholder text. On focus, border highlights in pink.

### Footer
**`footer`** — A soft gray section (`{colors.surface-soft}`) with muted text. Contains columns for product categories, support, social links, and newsletter signup. Uses `{spacing.xxl}` padding top/bottom.

### Badges
**`badge-new`** — A green pill badge (`#7ae28d`) for new arrivals. **`badge-sale`** — A red pill badge (`#ff3b30`) with white text for discounts. Both use `{typography.badge}` and `{rounded.full}`.

### Accordion
**`accordion`** — Used for FAQ sections and product details. White card with `{rounded.sm}`, a 1px soft border, and expand/collapse chevron. Active state shows pink highlight on the header.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack; hero text shrinks to 28px; search bar moves to top; buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero maintains 36px headline; side-by-side form layouts |
| Desktop | 1128–1440px | Three-column grid; full nav with dropdowns; hero at 48px; search bar in nav; product cards show hover effects |
| Wide | > 1440px | Max-width container (1440px) centered; extra whitespace; four-column product grid; larger hero imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility.
- Product card tap targets (swatches, add-to-cart) are at least 32px with 8px padding.
- Nav links have 48px tap area on mobile.
- Accordion headers are 48px tall for easy tapping.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses to a hamburger icon; the full menu becomes a slide-in overlay from the left.
- Product filters collapse into a single "Filter" button that opens a bottom sheet.
- The footer's four-column layout collapses to a single column with expandable accordion sections.
- Product image galleries switch from horizontal scroll to a single-image swipe carousel.
- Multi-step checkout collapses to a single-page form with accordion sections.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover and active states for all components (shadows, scale transforms) could not be reliably extracted from static CSS.
- Error state styling for text inputs (icon, helper text color, border animation) is inferred from the `#ff3b30` error token but not verified.
- Dark mode tokens are not present on the live site; all surfaces assume the warm light canvas `#fffee9`.
- Sub-brand or limited-edition palette variations (e.g., charcoal, watermelon) may introduce additional accent colors not captured here.
- Typography scale for mobile (e.g., `display-xl` at smaller viewports) is estimated; exact responsive font-size breakpoints are not documented.
- Animation timing and easing curves (e.g., button press, card hover, nav transition) are not specified.
- Icon set and stroke weights are not defined; the brand likely uses custom illustrations and 24px/32px icons.
- Accessibility contrast ratios for some color combinations (e.g., `#ffd801` on `#fffee9`) may need verification against WCAG standards.
