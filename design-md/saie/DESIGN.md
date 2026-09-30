---
version: alpha
name: "Saie"
source_url: "https://saiehello.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Saie is a clean makeup brand that radiates a soft, approachable confidence through a palette anchored in warm neutrals and punctuated by a signature electric lime (#e6ef00). The brand's visual language is built on a foundation of creamy off-whites (#f2f2f2, #f2f3f2) and gentle greiges (#d7d3cf, #a9a096), with a sophisticated secondary palette of dusty mauves (#91889d, #9387a0) and warm taupes (#8f7a64, #c79f7c) that echo the natural tones of skin and earth. The typography system pairs the refined serif of VictorSerif and Ordinary-Display for editorial moments with the clean readability of Ordinary-Text and Open Sans for body copy, creating a tension that feels both elevated and everyday. Signature design moves include generous use of soft rounded corners ({rounded.sm} to {rounded.lg}) that make every interaction feel gentle and tactile, a persistent accent of the brand's lime green across CTAs and badges that provides unexpected energy against the muted backdrop, and a reliance on negative space and soft hairlines (#dedede, #e5e5e5) rather than heavy borders. The overall effect is one of effortless polish — a brand that trusts its product photography and clean layout over aggressive typography or loud patterns, making the experience feel like a calm, well-edited vanity rather than a cluttered drugstore aisle.

colors:
  primary: "#e6ef00"
  primary-active: "#dce319"
  primary-disabled: "#f2f3f2"
  ink: "#1b2121"
  body: "#444444"
  muted: "#707070"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#f2f2f2"
  surface-soft: "#f2f3f2"
  surface-card: "#ffffff"
  on-primary: "#1b2121"
  accent-mauve: "#91889d"
  accent-mauve-soft: "#c0c0da"
  accent-taupe: "#8f7a64"
  accent-taupe-soft: "#a9a096"
  accent-warm: "#d0af91"
  accent-warm-light: "#efe0c1"
  accent-sand: "#d7d3cf"
  badge-new: "#e6ef00"
  star-rating: "#1b2121"
  error: "#ff6b6b"

typography:
  display-xl:
    fontFamily: "'Ordinary-Display', 'VictorSerif', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Ordinary-Display', 'VictorSerif', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Ordinary-Display', 'VictorSerif', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Ordinary-Text', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02px
  title-sm:
    fontFamily: "'Ordinary-Text', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Ordinary-Text', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Ordinary-Text', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Ordinary-Text', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03px
  button-md:
    fontFamily: "'Ordinary-Text', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Ordinary-Text', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Ordinary-Text', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Ordinary-Text', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Ordinary-Text', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(0,0,0,0.04)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "0 {spacing.base} {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.accent-sand}"
  footer-link-hover:
    color: "{colors.surface-card}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0"
  accordion-body:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "1px solid {colors.hairline}"
  swatch-selected:
    border: "2px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "0 12px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in the signature lime (#e6ef00) with dark ink (#1b2121) text for high contrast. Uses uppercase tracking with 0.5px letter-spacing and a soft 8px radius. On hover, shifts to the slightly warmer `primary-active` (#dce319); disabled state drops to the muted canvas tone (#f2f3f2) with muted text.

**`button-secondary`** — An outlined variant on the canvas background with a subtle hairline border. Maintains the same uppercase button typography and 8px radius. Active state darkens the border to ink and fills with the soft surface tone.

**`button-tertiary`** — A text-only button with no background or border, used for secondary actions like "View All" or "Skip". Relies on the uppercase button typography and ink color, with underline on hover.

**`button-pill`** — A fully rounded variant of the primary button, used for filter tags, category toggles, and compact CTAs. Uses the smaller button-sm typography and full pill radius.

### Cards
**`product-card`** — A clean white card with a subtle shadow (1px/3px at 4% opacity) and 12px rounded corners. The product image sits flush to the top with rounded top corners, followed by the title in title-sm and price in body-sm. On hover, the shadow deepens to 4px/12px at 8% opacity for a gentle lift effect.

**`review-card`** — A bordered card with a soft hairline and 12px radius, used for customer reviews. Contains the star rating component, reviewer name, and body text. Padding is consistent at 16px.

### Navigation
**`nav-bar`** — A fixed-height 72px bar on the canvas background with a soft bottom hairline. Contains the brand logo, nav links in uppercase 13px text, and utility icons (search, account, cart). On scroll, gains a subtle box-shadow and becomes sticky.

**`nav-link-active`** — The active navigation state uses a 2px bottom border in the brand's lime green, signaling the current section without heavy visual weight.

### Forms
**`text-input`** — Standard input fields on canvas background with a hairline border and 8px radius. On focus, the border transitions to ink (#1b2121). Error state uses the error red (#ff6b6b) border. Padding is generous at 12px vertical / 16px horizontal for comfortable typing.

**`select-input`** — Matches the text-input styling for visual consistency across form elements.

**`quantity-selector`** — A compact horizontal control with decrement/increment buttons flanking a central numeric display. Uses the same hairline border and 8px radius as other inputs, with buttons that have no individual radius for a seamless inline appearance.

### Badges
**`badge-new`** — A small uppercase label in the brand's lime green, used to flag new arrivals. Compact padding (2px/8px) with 4px radius for a subtle but noticeable accent.

**`badge-sale`** — An error-red variant for sale or clearance items, maintaining the same structure and typography as the new badge.

### Footer
**`footer`** — A dark inversion of the brand, using the ink (#1b2121) background with soft sand (#d7d3cf) text. Links are in the sand tone and transition to white on hover. Section padding is generous at 48px vertical.

### Accordion
**`accordion`** — Collapsible content panels used for product details, FAQ, and shipping information. Each panel has a clickable header in title-sm and a body section in body-sm with muted text. Uses the canvas background with a soft hairline border and 8px radius.

### Swatches
**`swatch`** — Circular color swatches at 32px diameter with a hairline border. The selected state adds a 2px ink border for clear indication. Used in product variant selection for foundation shades, lip colors, and other makeup products.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack full-width; hero reduces to 300px min-height; search bar moves to overlay; footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid; nav links truncate to icons; hero maintains 400px height; search bar remains visible but compact |
| Desktop | 1128–1440px | Three-column product grid; full nav links visible; hero at full height; search bar expanded with placeholder text; footer in multi-column layout |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero content centered with generous margins; all components at their largest comfortable size |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Product card tap targets extend to full card area
- Quantity selector buttons are 40px minimum
- Swatch circles are 32px with 44px tap area via padding
- Nav bar icons have 44x44px tap targets

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product filters collapse to a slide-out drawer on mobile
- Footer multi-column layout stacks to single column below 744px
- Hero content reduces font sizes and padding on mobile
- Product image galleries collapse to single-image swipe on mobile
- Accordion panels are always collapsed by default on mobile, with first panel open on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for tertiary buttons and text links (underline vs. color change)
- Error message styling for form validation (text color, background, iconography)
- Loading states for buttons (spinner integration, disabled opacity)
- Success/confirmation states (add-to-cart animation, toast notifications)
- Sub-brand or collection-specific color palettes (e.g., limited editions)
- Dark mode color tokens and component adjustments
- Focus ring styles for keyboard navigation (color, width, offset)
- Tooltip and popover component specifications
- Modal/dialog overlay styling (scrim opacity, animation)
- Dropdown menu specifications (shadow, padding, item states)
- Skeleton loading placeholder colors and animation
- Print stylesheet specifications
- Accessibility contrast ratios for all color combinations
- Typography scale for mobile-specific font sizes
- Icon library specifications (stroke width, sizes, color inheritance)
