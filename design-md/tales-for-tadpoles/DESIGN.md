---
version: alpha
name: "Tales for Tadpoles"
source_url: "https://talesfortadpoles.ie"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A children's bookstore that wraps itself in a warm, storybook palette anchored on #f9f6f0 — a soft, cream-washed canvas that feels like aged paper under good light. The brand's true voltage comes from two distinctive reds: #d8385a, a berry-coral that appears on primary buttons and sale badges, and #a62f48, a deeper, more grounded crimson used for hover states and secondary accents. These sit against a supporting cast of muted greys (#a29f9b, #d5d5d5, #e6e6e6) that form the structural bones — borders, dividers, secondary text — while #bedcd2, a pale sage, surfaces in badge backgrounds and category tags, adding a gentle, organic counterpoint to the reds. The typography leans on Josefin Sans for display headings — its geometric, slightly playful letterforms evoke a modern fairy-tale quality — paired with Georgia and Courier for body text, lending a literary, printed-book feel. Corners are softly rounded ({rounded.sm} on buttons, {rounded.md} on cards), never pill-shaped, preserving a sense of crafted, physical object-ness. The overall mood is generous and unhurried: generous whitespace, a restrained use of the red accent (never more than one per view), and a footer that reads like a colophon, with tiny type and a warm #faf4e8 background. This is a brand that trusts its colors to tell the story — the red is the exclamation point, the cream is the page, and the sage is the quiet nod to nature and nurture.

colors:
  primary: "#d8385a"
  primary-active: "#a62f48"
  primary-disabled: "#fdd0d0"
  ink: "#1e1e1e"
  body: "#313131"
  muted: "#4e4e4e"
  muted-soft: "#a29f9b"
  hairline: "#d5d5d5"
  hairline-soft: "#e6e6e6"
  canvas: "#f9f6f0"
  surface-soft: "#faf4e8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#bedcd2"
  accent-marigold: "#f1c142"
  badge-red: "#cc0000"
  badge-soft-red: "#ffecef"
  error: "#c60808"
  error-soft: "#fdd0d0"

typography:
  display-xl:
    fontFamily: "'Josefin Sans', Georgia, 'Times New Roman', Times, serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Josefin Sans', Georgia, 'Times New Roman', Times, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Josefin Sans', Georgia, 'Times New Roman', Times, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Josefin Sans', Georgia, 'Times New Roman', Times, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Josefin Sans', Georgia, 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Josefin Sans', Georgia, 'Times New Roman', Times, serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Josefin Sans', Georgia, 'Times New Roman', Times, serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Josefin Sans', Georgia, 'Times New Roman', Times, serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Courier New', Courier, monospace"
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 12px
  button-text-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  text-input-error:
    borderColor: "{colors.error}"
    boxShadow: "0 0 0 2px {colors.error-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.primary}"
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-category:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
  search-bar-focus:
    borderColor: "{colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-link-hover:
    textColor: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    padding: "{spacing.md} 0"
  category-tab-active:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  category-tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 44px
  newsletter-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "6px 12px"
    height: 36px
  quantity-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    height: 28px
  rating-stars:
    color: "{colors.accent-marigold}"
    size: 16px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and checkout flows. Rendered in the brand's berry-coral {colors.primary} with white text and a soft 8px corner radius. On hover, shifts to the deeper {colors.primary-active} (#a62f48). Disabled state uses a pale pink {colors.primary-disabled} (#fdd0d0) with muted text, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined variant on the cream canvas background, with {colors.primary} text and a thin border. Used for "Learn More" links, secondary checkout options, and filter resets. Active state adopts the warmer {colors.surface-soft} background and deeper red text.

**`button-text`** — A borderless, backgroundless link-style button for inline actions like "Clear Filters" or "Cancel". Uses {colors.primary} text that deepens to {colors.primary-active} on hover. No padding beyond 8px horizontal to keep it visually lightweight.

### Cards
**`product-card`** — The core product display unit, a white card with a 12px rounded corner and a soft shadow on hover. The image area occupies the top portion with its own rounded top corners, while the title uses {typography.title-sm} in {colors.ink} and the price appears in {colors.primary} at {typography.body-md} weight. Badges overlay the top-left of the image area.

**`review-card`** — A customer review card with a white background, 12px rounded corners, and 16px padding. Star ratings render in {colors.accent-marigold} (#f1c142) at 16px. Review body text uses {typography.body-sm} in {colors.body}.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 64px height on the cream {colors.canvas} background. Navigation links are set in Josefin Sans at 15px with 0.3px letter spacing, uppercase. The active page link uses {colors.primary}, while hover links shift to {colors.primary-active}. The cart icon badge uses {colors.badge-red} (#cc0000) for the count indicator.

**`category-strip`** — A horizontal scrollable strip of category pills below the hero or above the product grid. Inactive pills use {colors.surface-soft} background with {colors.muted} text; the active pill uses {colors.accent-sage} (#bedcd2) background with {colors.ink} text. All pills are fully rounded and padded 6px 16px.

### Forms
**`text-input`** — Standard text input fields for search, newsletter signup, and checkout forms. White background, 8px rounded corners, 44px height, and {typography.body-md} in Georgia. On focus, gains a 2px {colors.primary} border with a soft pink glow. Error state uses {colors.error} (#c60808) border with a pale red glow.

**`newsletter-input`** — A dedicated email input paired with a {colors.primary} submit button. The input matches the standard text-input styling but sits flush against the button in a horizontal layout. The button uses {typography.button-sm} for a more compact fit.

### Badges
**`badge-sale`** — A small, high-contrast badge using {colors.badge-red} (#cc0000) background with white text. Set in Courier New at 11px uppercase, with 4px rounded corners and 2px 8px padding. Appears on the product card image overlay.

**`badge-new`** — A gentler badge using {colors.accent-sage} (#bedcd2) background with {colors.ink} text. Same typography and sizing as the sale badge but communicates new arrivals rather than discounts.

**`badge-category`** — A pill-shaped category label used in filter bars and product metadata. Uses {colors.surface-soft} background with {colors.muted} text, fully rounded with 4px 12px padding.

### Footer
**`footer`** — A warm, colophon-style footer on {colors.surface-soft} (#faf4e8) background with {colors.muted} text. Section headings use {typography.title-sm} in {colors.ink}. Links are set in {typography.link} and shift to {colors.primary} on hover. The divider between sections uses {colors.hairline-soft} at 1px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger menu; product cards stack single-column; hero text reduces to {typography.display-lg}; category strip becomes horizontally scrollable; footer stacks vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; hero maintains {typography.display-xl} but with reduced padding; footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-4 column grid; hero at full width with generous padding; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; hero centered with max-width 1200px; product cards maintain 4-column grid with increased gap |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Category strip pills are at least 36px tall with 16px horizontal padding
- Nav links have 48px minimum touch area (including padding)
- Quantity selector buttons are 28px tall but sit within a 36px container for adequate tap area
- Search bar maintains 40px height with generous padding

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon below 744px, with a slide-out drawer menu
- Product grid reduces columns: 4 → 3 → 2 → 1 as viewport narrows
- Hero section reduces padding and font size below 744px, with the CTA button stacking below the text
- Footer columns collapse from 4 to 2 to 1, with dividers appearing between stacked sections
- Category strip becomes horizontally scrollable with visible scroll indicators below 744px
- Newsletter form remains inline on tablet and above, stacks vertically on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: While button and link hover colors were inferred from the extracted palette, specific hover transitions (duration, easing) were not observable from static extraction. A 150ms ease-in-out is assumed but not confirmed.
- **Focus states**: Focus ring styles for keyboard navigation were not extracted. The text-input focus style is an educated guess based on the primary color and its light variant.
- **Error states**: Error text styling, validation messages, and form error patterns were not observed. The error color (#c60808) was extracted but its usage context is inferred.
- **Dark mode**: No dark mode implementation was detected. The brand appears to be light-mode only.
- **Typography scale**: Font sizes and weights are inferred from the extracted font declarations and typical usage patterns for a children's bookstore. Exact scale values (especially for display and title sizes) may vary from the live site's implementation.
- **Spacing scale**: The spacing tokens are a standard design-system scale. Exact padding and margin values used on the live site may differ, particularly for section spacing and card padding.
- **Component states**: Disabled states for inputs, loading states for buttons, and empty states for product grids were not observable.
- **Sub-brand or seasonal palettes**: No evidence of holiday, seasonal, or promotional color variants was found. The brand may introduce temporary palettes for events like Christmas or Back to School.
- **Animation and motion**: No animation timing, easing curves, or transition patterns were extracted. The brand may use subtle fade-ins, slide-ups, or hover animations that are not captured in static CSS extraction.
- **Iconography**: Icon style, stroke weight, and color usage were not extracted. The brand likely uses custom or Shopify-standard icons for cart, search, and navigation.
- **Checkout flow**: Shopify's default checkout styling may override brand colors. The extracted palette includes some Shopify Pay and Klarna widget colors that were filtered, but the exact checkout styling is unknown.
