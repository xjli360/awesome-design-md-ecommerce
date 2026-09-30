---
version: alpha
name: "Colored Organics"
source_url: "https://coloredorganics.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A muted, earthy palette anchored by a deep navy blue (#006fcf) that serves as the primary brand voltage across CTAs, navigation accents, and footer backgrounds — a deliberate departure from the pastel pinks and mint greens typical of baby clothing. The supporting palette draws from natural fibers and organic dyes: sage greens (#8f9685, #89907e), warm clay (#9e8575), and a single burst of tangerine (#f48120) used sparingly for sale badges and promotional flags. The brand's typography layers two distinct voices — the clean, modern sans-serif of Averta for product titles and navigation, and the refined serif of Mrs Eaves for editorial body copy, with Baginda Script reserved for logo marks and decorative headings. Rounded corners are generous but not pill-shaped: product cards use {rounded.md} (12px), buttons use {rounded.sm} (8px), and the search bar uses {rounded.lg} (20px), creating a soft, approachable feel that mirrors the organic cotton textures the brand sells. The canvas is a warm off-white (#fcfcfc) rather than pure white, and the surface-soft (#f0f0f0) provides subtle depth without harsh contrast. The overall effect is a brand that feels grounded in nature — not through literal leaf motifs or earth tones, but through a restrained palette that lets the product photography of babies in organic onesies carry the emotional weight. The checkout flow introduces a secondary accent (#128522, a forest green) for success states and confirmation messaging, reinforcing the "organic" promise without shouting.

colors:
  primary: "#006fcf"
  primary-active: "#0058a6"
  primary-disabled: "#b3d4f0"
  ink: "#231f20"
  body: "#383838"
  muted: "#747c83"
  muted-soft: "#a6a6a6"
  hairline: "#dedede"
  hairline-soft: "#dfdfdf"
  canvas: "#fcfcfc"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#8f9685"
  accent-sage-light: "#c9d4dd"
  accent-clay: "#9e8575"
  accent-tangerine: "#f48120"
  accent-tangerine-active: "#d96a0a"
  accent-forest: "#128522"
  accent-error: "#e9563b"
  accent-error-strong: "#e22c19"
  accent-marigold: "#dfa652"
  accent-rose: "#80565b"
  accent-teal: "#9ebfbf"
  accent-charcoal: "#556270"

typography:
  display-xl:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Mrs Eaves', 'Georgia', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Mrs Eaves', 'Georgia', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Averta', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  logo-script:
    fontFamily: "'Baginda Script', 'Brush Script MT', cursive"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 0
  button-tangerine:
    backgroundColor: "{colors.accent-tangerine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 20px
    height: 36px
  button-tangerine-active:
    backgroundColor: "{colors.accent-tangerine-active}"
  button-sale-badge:
    backgroundColor: "{colors.accent-tangerine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  button-out-of-stock:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-error}"
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  select-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
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
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(35,31,32,0.08)"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} {spacing.base}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  mobile-menu-icon:
    textColor: "{colors.ink}"
    height: 24px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    backgroundColor: "{colors.canvas}"
  search-icon:
    textColor: "{colors.muted}"
    height: 20px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginTop: "{spacing.xs}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-error}"
    fontWeight: 600
  product-card-compare-at-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  product-card-badge:
    backgroundColor: "{colors.accent-tangerine}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-sold-out-badge:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    position: "absolute"
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  product-card-color-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    border: "2px solid {colors.hairline}"
  product-card-color-swatch-active:
    border: "2px solid {colors.ink}"
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 40px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    height: 400px
  hero-banner-overlay:
    backgroundColor: "rgba(35,31,32,0.3)"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  section-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
    hoverColor: "{colors.canvas}"
  footer-heading:
    typography: "{typography.caption}"
    textColor: "{colors.canvas}"
    textTransform: uppercase
    letterSpacing: "1px"
    marginBottom: "{spacing.base}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 48px
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  accordion-open:
    borderColor: "{colors.primary}"
  accordion-content:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    padding: "{spacing.base} {spacing.lg}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-active:
    textColor: "{colors.ink}"
    fontWeight: 600
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    margin: "0 {spacing.xs}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 44px
  quantity-selector-button:
    textColor: "{colors.muted}"
    height: 44px
    width: 44px
  quantity-selector-button-hover:
    textColor: "{colors.ink}"
    backgroundColor: "{colors.surface-soft}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  size-selector-active:
    border: "2px solid {colors.ink}"
    backgroundColor: "{colors.surface-soft}"
  size-selector-disabled:
    textColor: "{colors.hairline}"
    border: "1px dashed {colors.hairline}"
    cursor: not-allowed
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  trust-badge-icon:
    textColor: "{colors.accent-forest}"
    height: 20px
  review-stars:
    textColor: "{colors.accent-marigold}"
    height: 16px
  review-stars-empty:
    textColor: "{colors.hairline}"
    height: 16px
  review-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  review-author:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    fontWeight: 600
  review-date:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted-soft}"
  loading-spinner:
    color: "{colors.primary}"
    height: 24px
    width: 24px
  loading-spinner-on-dark:
    color: "{colors.canvas}"
    height: 24px
    width: 24px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-sage:
    backgroundColor: "{colors.accent-sage-light}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  tooltip-arrow:
    color: "{colors.ink}"
  modal-overlay:
    backgroundColor: "rgba(35,31,32,0.5)"
  modal-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  modal-close:
    textColor: "{colors.muted}"
    height: 24px
    width: 24px
  modal-close-hover:
    textColor: "{colors.ink}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
  cart-drawer-header:
    typography: "{typography.title-md}"
    padding: "{spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  cart-drawer-item:
    padding: "{spacing.base} {spacing.lg}"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-drawer-footer:
    padding: "{spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  cart-drawer-checkout-button:
    backgroundColor: "{colors.accent-forest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 24px"
    height: 48px
  cart-drawer-continue-shopping:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"
  cart-item-quantity:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
  cart-item-remove:
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption-sm}"
    hoverColor: "{colors.accent-error}"
  empty-state:
    typography: "{typography.body-md}"
    textColor: "{colors.muted}"
    padding: "{spacing.xxl}"
  empty-state-icon:
    textColor: "{colors.hairline}"
    height: 48px
    width: 48px
  error-state:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-error}"
    padding: "{spacing.base}"
  error-state-icon:
    textColor: "{colors.accent-error}"
    height: 24px
    width: 24px
  success-state:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-forest}"
    padding: "{spacing.base}"
  success-state-icon:
    textColor: "{colors.accent-forest}"
    height: 24px
    width: 24px
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    height: 40px
  announcement-bar-link:
    textColor: "{colors.canvas}"
    textDecoration: underline
  category-grid-item:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    height: 200px
  category-grid-item-hover:
    backgroundColor: "{colors.accent-sage-light}"
  category-grid-item-image:
    rounded: "{rounded.md}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"
  filter-chip-hover:
    border: "1px solid {colors.muted}"
  filter-clear:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
  sort-select:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's deep navy blue (#006fcf) and white text. Uses Averta at 15px with 0.3px letter spacing for a slightly refined feel. On hover, darkens to #0058a6. Disabled state fades to a light blue (#b3d4f0). Padding is 12px top/bottom, 28px left/right, creating a comfortable 44px height.

**`button-secondary`** — An outlined variant with a white fill and navy blue border. Matches the primary button's 44px height and 15px type size. Active state uses the lighter surface-soft background (#f0f0f0) and the darker primary-active border. Used for "Add to Wishlist" and secondary checkout actions.

**`button-tertiary-text`** — A text-only button with no background or border. Uses the primary blue for color and the same button-md typography. Used for "View All" links and "Learn More" prompts within content sections.

**`button-tangerine`** — A smaller, accent-colored button using the brand's tangerine orange (#f48120). At 36px tall with 8px/20px padding, it's used for promotional CTAs like "Shop the Sale" and "Limited Edition." Active state darkens to #d96a0a.

**`button-sale-badge`** — A compact, non-interactive badge for marking sale prices. Uses the tangerine background with uppercase badge typography (11px, 0.5px letter spacing). Positioned absolutely on product cards, typically top-left with 8px padding.

**`button-out-of-stock`** — A disabled-looking button using muted-soft gray (#a6a6a6) for out-of-stock products. Matches the tangerine button's 36px height but communicates unavailability through color alone.

### Cards
**`product-card`** — The primary product display container. A white card with 12px rounded corners and body-sm typography for descriptions. The product image occupies the top portion with rounded top corners only, creating a natural visual hierarchy. The title uses title-sm (16px, 600 weight) with 8px top margin, and the price uses body-md (16px serif) below it.

**`product-card-sale-price`** — When a product is on sale, the price switches to the error red (#e9563b) with 600 weight. The original price appears as `product-card-compare-at-price` with line-through styling in muted-soft gray.

**`product-card-badge`** — A tangerine badge positioned absolutely at top-left of the card image. Uses 11px uppercase bold type with 4px/8px padding and 4px rounded corners. Common labels: "SALE," "NEW," "BESTSELLER."

**`product-card-sold-out-badge`** — Same positioning and size as the sale badge, but uses the muted gray (#747c83) background to indicate unavailability without the urgency of the tangerine.

**`product-card-color-swatch`** — A 24px circular swatch with a 2px hairline border. Active state switches to a 2px ink-colored border. Used in a horizontal strip below the product title to show available colorways.

**`review-card`** — A bordered card (1px hairline-soft) with 12px rounded corners and 16px padding. Contains the review text in body-sm, the author name in caption weight 600, and the date in caption-sm muted-soft. Star ratings use the marigold accent (#dfa652) for filled stars and hairline for empty stars.

### Navigation
**`nav-bar`** — A fixed 72px header with white background and uppercase Averta navigation links at 14px with 0.5px letter spacing. On scroll, gains a subtle box shadow (2px, 8px blur, 8% opacity ink). The active nav link is underlined with a 2px primary blue border.

**`nav-link`** — Navigation items with 8px/16px padding. Hover state shifts text to primary blue. Active state adds the blue bottom border. The uppercase treatment and letter spacing give the navigation a considered, editorial feel.

**`mobile-menu-icon`** — A 24px hamburger icon in ink color, shown below 744px viewport width. Toggles a full-screen overlay menu.

**`breadcrumb`** — Small caption text (13px) in muted gray, with the active (current) page in ink at 600 weight. Separators are hairline-colored with 4px horizontal margin.

**`pagination`** — Circular pagination buttons (36px diameter) with body-sm type. Active page uses the primary blue fill with white text. Hover state uses surface-soft background. Non-active pages are muted gray text with no background.

### Forms
**`text-input`** — A 48px tall input with white background, 12px/16px padding, and a 1px hairline border. Uses Mrs Eaves body-md for the input text (16px serif). Focus state gains a 2px primary blue border. Error state uses a 2px error red border (#e9563b). Labels use caption typography in muted gray with 4px bottom margin.

**`select-dropdown`** — Matches the text-input dimensions and styling but includes a dropdown arrow icon. Uses the same 48px height and body-md type.

**`size-selector`** — A 44px tall pill-shaped button for size selection (XS, S, M, L, XL). Active state uses a 2px ink border with surface-soft background. Disabled sizes use a dashed hairline border with hairline text color and not-allowed cursor.

**`quantity-selector`** — A 44px tall horizontal control with minus/plus buttons on either side (44px wide each) and the quantity number in the center. Uses a 1px hairline border and 8px rounded corners. Button hover shifts to ink color with surface-soft background.

**`filter-chip`** — A pill-shaped filter toggle (full rounded) with 6px/16px padding and a 1px hairline border. Active state fills with primary blue and white text. Hover state darkens the border to muted gray. Used in collection pages for size, color, and price filters.

### Footer
**`footer`** — A dark section with ink background (#231f20) and white text. Uses 48px top/bottom padding and 64px left/right. Links are muted-soft gray (#a6a6a6) and hover to white. Section headings use caption typography (13px, 500 weight) with 1px letter spacing and uppercase transformation.

**`newsletter-input`** — A 48px tall white input matching the text-input styling but placed within the dark footer. The submit button is a primary blue button of the same height, placed immediately adjacent.

### Special States
**`loading-spinner`** — A 24px spinning indicator in primary blue. A white variant (`loading-spinner-on-dark`) is used on dark backgrounds.

**`tooltip`** — A dark (ink) background tooltip with white text in caption size. Uses 4px rounded corners and 4px/8px padding. The arrow points down from the tooltip body, matching the ink background color.

**`modal-overlay`** — A 50% opacity black scrim (#231f20) over the page content. The modal card is white with 12px rounded corners and 32px padding. The close button is a 24px X icon in muted gray, hovering to ink.

**`cart-drawer`** — A 400px wide slide-in panel from the right. The header uses title-md with a bottom hairline border. Each cart item has 16px/24px padding with a soft hairline separator. The footer contains a forest green (#128522) checkout button — the only place this accent color appears as a primary action, signaling completion and confirmation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces full nav, hero height reduces to 250px, footer stacks vertically, filter chips collapse to a "Filter" button that opens a modal, product cards use full-width images |
| Tablet | 744–1128px | Two-column product grid, nav links collapse to icons with labels, hero height at 350px, footer uses two-column layout, filter chips show inline but wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid, full nav with uppercase links, hero at 400px, footer uses four-column layout, filter chips show in a sidebar on collection pages |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px centered, hero at 450px with parallax effect, footer uses four-column layout with wider gutters |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card CTAs ("Add to Cart") are 40px tall with 10px/16px padding
- Filter chips are 36px tall with 6px/16px padding
- Quantity selector buttons are 44px × 44px for easy tapping
- Mobile navigation links have 48px touch targets
- Cart drawer remove buttons are 36px tall with adequate padding

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Footer columns collapse from four to two at tablet, to single column at mobile
- Product grid collapses from four columns to three at desktop, two at tablet, one at mobile
- Filter sidebar collapses to a modal trigger button below 744px
- Hero banner text overlay collapses to a single heading and CTA at mobile (subheadings hidden)
- Size selector grid collapses from 5 items per row to 3 at mobile
- Review cards collapse from 3-column grid to single column at mobile
- Accordion sections (product details, shipping info) remain collapsed by default on all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; exact transition durations and easing curves are unknown (likely 200-300ms ease-in-out)
- Focus ring styles for keyboard navigation are not specified; likely uses a 2px primary blue outline offset by 2px
- Error message styling for form validation (color, position, iconography) is not fully extractable from the color list alone
- Dark mode is not present on the live site; no dark mode tokens are defined
- The exact font weights for Averta (regular, medium, semibold, bold) are inferred from common usage; the site may use additional weights
- Mrs Eaves may have italic variants for emphasis; not confirmed
- Baginda Script usage is limited to the logo; decorative heading sizes are estimated
- The tangerine accent (#f48120) may have additional usage in hover states or active states not captured
- The forest green (#128522) appears in checkout; its exact role in the broader system (success messages, confirmation pages) is inferred
- Animation specifications (page transitions, card hover lifts, menu slide durations) are not documented
- The extracted color list includes many grays that may be Shopify default widget colors rather than intentional brand colors; the 10+ gray variants suggest some are framework artifacts
- The primary blue (#006fcf) is the most distinctive non-gray color in the extracted list; its usage as the primary brand color is an informed decision based on frequency and placement in the extracted data
- The accent colors (sage, clay, tangerine, marigold, rose, teal) are selected from the extracted list based on their distinctiveness from the gray/blue spectrum; their exact roles in the design system are inferred from common ecommerce patterns
