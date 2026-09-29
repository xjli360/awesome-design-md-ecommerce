---
version: alpha
name: "Oars + Alps"
source_url: "https://www.oarsandalps.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A rugged-yet-refined men's grooming brand that speaks in the elemental language of the outdoors — deep navy-blues like `#025776` and `#012b3a` anchor the system, while a single high-voltage coral `#d02e2e` (our `{colors.primary}`) ignites every call-to-action, badge, and accent. The palette is unapologetically masculine and grounded: a near-black `#1f2021` serves as the `{colors.ink}` for body copy, set against a warm off-white canvas `#f6f6f6` that softens the digital experience into something tactile, like well-worn canvas. A secondary teal `#69ced7` and a fresh green `#56ad6a` appear in product badges and sustainability cues, hinting at the brand's active, outdoor ethos. Typography leans on the proprietary Fabriga family — a geometric sans-serif with subtle humanist warmth — set at moderate weights (400–600) that never shout; the brand trusts its product photography and generous whitespace over typographic muscle. Signature design moves include pill-shaped buttons (`{rounded.full}`) that feel ready for the trail, softly rounded product cards (`{rounded.md}` at 12px), and a persistent top nav with a transparent-to-solid scroll transition that mirrors the brand's own adaptability — from trailhead to town. The entire system reads as honest, durable, and unpretentious: a grooming brand that doesn't smell like a nightclub, but like cedar, sea salt, and clean air.

colors:
  primary: "#d02e2e"
  primary-active: "#b32525"
  primary-disabled: "#f2b3b3"
  ink: "#1f2021"
  body: "#3d3f41"
  muted: "#5a5d60"
  muted-soft: "#717171"
  hairline: "#cccccc"
  hairline-soft: "#e6e6e6"
  canvas: "#f6f6f6"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#69ced7"
  accent-green: "#56ad6a"
  accent-teal-dark: "#037ca8"
  accent-navy: "#025776"
  accent-navy-deep: "#012b3a"
  badge-sale: "#d02e2e"
  badge-new: "#56ad6a"
  badge-sustainable: "#69ced7"
  star-rating: "#1f2021"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.25px
  link:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Fabriga', 'Fabrica Regular', 'Roboto', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill-accent:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  top-nav-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.accent-navy}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0 0 16px 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.08)"
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.xxs} {spacing.base}"
  product-card-badge:
    typography: "{typography.badge}"
    color: "{colors.on-primary}"
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    position: "absolute"
    top: "8px"
    left: "8px"
  hero-section:
    backgroundColor: "{colors.accent-navy-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: "400px"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "14px 40px"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
    maxWidth: "480px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
    hoverColor: "{colors.on-primary}"
  footer-heading:
    typography: "{typography.caption}"
    color: "{colors.on-primary}"
    textTransform: uppercase
    letterSpacing: "1px"
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
  badge-sustainable:
    backgroundColor: "{colors.badge-sustainable}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
  accordion-header:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
    padding: "{spacing.sm} 0"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0 0"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "8px 16px"
    height: "44px"
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
    gap: "2px"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "12px 20px"
    height: "48px"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: "48px"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered as a pill-shaped button in the signature coral `#d02e2e` (`{colors.primary}`). Uses Fabriga 600 weight at 16px with tight tracking. On hover, shifts to `{colors.primary-active}` (`#b32525`). The disabled state fades to a soft pink `{colors.primary-disabled}` (`#f2b3b3`). Always paired with white text for maximum contrast against the deep navy and charcoal backgrounds it typically sits on.

**`button-secondary`** — A ghost-style pill button with a transparent fill and a `{colors.hairline}` border that darkens to `{colors.ink}` on hover. Used for "Learn More" and "View Details" actions where the primary button would overwhelm. Maintains the same 48px height and full rounding as the primary for visual consistency.

**`button-tertiary-text`** — A minimal text-only button with no background or border, used for secondary actions like "Cancel" or "Skip". Inherits the same typography as primary buttons but sits flush with surrounding content. Hover state adds subtle underline.

**`button-pill-accent`** — A smaller, darker pill button using `{colors.accent-navy}` (`#025776`) as background, used for subscription CTAs and "Add to Cart" in product cards. Same full rounding but tighter padding (10px 24px) to fit compact layouts.

### Cards
**`product-card`** — The primary product display unit, a white card with 12px rounding (`{rounded.md}`) and a subtle drop shadow. The image area occupies the top half with matching top rounding, while text content sits below with 16px horizontal padding. On hover, the shadow deepens and a subtle scale transform (1.02) signals interactivity. Badges overlay the image at top-left with 8px offset.

**`product-card-badge`** — A small, sharp-cornered (`{rounded.xs}`) label pinned to product card images. Uses uppercase Fabriga 600 at 11px with 0.5px letter spacing. Color variants map to badge type: `{colors.primary}` for sale, `{colors.accent-green}` for new arrivals, `{colors.accent-teal}` for sustainable materials.

### Navigation
**`top-nav`** — A 72px fixed header with transparent background that transitions to solid `{colors.canvas}` on scroll. Navigation links use uppercase Fabriga 500 at 14px with 0.5px letter spacing. The active page is marked by a 2px `{colors.primary}` underline. The nav houses the brand logo (left), category links (center), and utility icons (right: search, account, cart).

**`nav-link-active`** — Active navigation state with bold underline in brand coral. Inactive links render in `{colors.muted}` (`#5a5d60`) and shift to `{colors.ink}` on hover.

### Forms & Inputs
**`search-bar`** — A full-rounded pill input with 1px `{colors.hairline}` border and 44px height. On focus, the border thickens to 2px and shifts to `{colors.accent-navy}`. Includes a magnifying glass icon at left and optional clear button on text entry.

**`newsletter-input`** — A 48px pill input paired with a matching `{colors.primary}` submit button. The input uses `{typography.body-sm}` for placeholder text. The submit button uses `{typography.button-sm}` for a balanced proportion.

**`quantity-selector`** — A compact pill-shaped control with minus/plus buttons flanking the quantity value. Uses `{typography.body-md}` for the number and `{typography.body-sm}` for the buttons. Maintains the brand's signature full rounding.

### Hero
**`hero-section`** — The primary brand storytelling unit, using a deep navy `{colors.accent-navy-deep}` (`#012b3a`) background with white text. The hero typically features a full-bleed lifestyle image with a left-aligned text overlay containing a headline (`{typography.display-xl}`), subtitle in `{colors.muted-soft}`, and a primary CTA. Minimum height of 400px with generous padding.

### Footer
**`footer`** — A dark section using `{colors.ink}` (`#1f2021`) as background with `{colors.muted-soft}` text. Column headings use uppercase Fabriga caption with 1px letter spacing. Links hover to white. Includes newsletter signup, social icons, and legal text in a stacked layout.

### Accordion
**`accordion`** — Used for FAQ sections and product descriptions. Each item has a clickable header with `{typography.title-sm}` and a chevron icon that rotates on expand. Content area uses `{typography.body-sm}` with `{colors.body}` text. Borders separate items with `{colors.hairline-soft}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; top-nav collapses to hamburger; product cards stack full-width; hero text centers; footer columns stack; buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; top-nav shows limited links with "More" dropdown; hero maintains left-alignment with reduced padding; footer shows 2-column layout |
| Desktop | 1128–1440px | Full 4-column product grid; complete top-nav visible; hero at full height with 64px section padding; footer shows 4-column layout |
| Wide | > 1440px | Max-width container (1440px) centers content; hero scales to max 600px height; product grid maintains 4 columns with increased gap |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons use 40px × 40px minimum touch area
- Product card tap targets (title, price, add-to-cart) have minimum 48px hit areas
- Accordion headers have 48px minimum tap height
- Mobile hamburger menu icon uses 44px × 44px touch target

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with slide-out drawer overlay
- Product filters collapse to a "Filter" button that opens a bottom sheet on mobile
- Footer multi-column layout collapses to single-column accordion on mobile
- Hero text overlay shifts from left-aligned to centered on mobile
- Product image galleries collapse from thumbnail strip to dot indicators on mobile
- Multi-step checkout collapses to single-page scroll on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components (button-secondary, nav-links, product-card) are inferred from common patterns but not verified from live site inspection
- Error states for form inputs (validation styling, error message placement) not extracted
- Dark mode color overrides not present on the live site
- Sub-brand or seasonal palette variations (holiday, limited edition) not documented
- Focus ring styles (outline, offset, color) not reliably extracted from CSS
- Loading states (skeleton screens, spinner designs) not observed
- Toast/notification component styling not present in extracted data
- Tooltip and popover styling not available
- Modal/dialog overlay styling (backdrop blur, animation) not extracted
- Specific font weights for Fabriga (400, 500, 600, 700) are inferred — actual available weights may vary
- Line-height values for display typography are estimated based on common brand patterns
- Letter-spacing values for uppercase text are estimated from typical brand usage
- Product card shadow values are approximated from common e-commerce patterns
- Animation timing and easing curves not extracted from the live site
