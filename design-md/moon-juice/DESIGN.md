---
version: alpha
name: "Moon Juice"
source_url: "https://moonjuice.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep violet-magenta (#2e3192) anchors Moon Juice — not as a background but as the brand’s primary voltage, appearing on buttons, badges, and the top nav bar, while a warm off-white canvas (#fafaf8) and a pale cream (#eceadd) create a soft, grounded atmosphere. The palette is unexpectedly playful: a highlighter-yellow (#fff88a) and a marigold (#ffcf2a) punctuate cart icons, sale badges, and accent text, while a minty teal (#00caaa) and a lime (#b5de57) appear in product highlights and ingredient callouts. Typography mixes a clean, modern sans (Basis in four weights) with a decorative serif (Gelica) for headlines and a condensed display face (Deutsch Gothic) for bold promotional text, plus a monospaced Typewriter for editorial notes and ingredient lists. The overall mood is apothecary-meets-wellness-boutique: clinical enough to feel trustworthy, warm enough to feel approachable. Buttons use tight 4px radii ({rounded.xs}) rather than pills, giving the interface a precise, editorial feel. Product cards float on white with subtle shadows, and the search bar sits inside a full-width banner rather than a standalone orb. The checkout flow shifts to a deep charcoal (#2e2930) theme, signaling a deliberate mode change from browse to purchase.

colors:
  primary: "#2e3192"
  primary-active: "#272d45"
  primary-disabled: "#9a9db1"
  ink: "#2e2930"
  body: "#3a303d"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#d3d4dd"
  hairline-soft: "#e5e5eb"
  canvas: "#fafaf8"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#fff88a"
  accent-marigold: "#ffcf2a"
  accent-teal: "#00caaa"
  accent-lime: "#b5de57"
  accent-sand: "#eceadd"
  accent-terracotta: "#cf9567"
  accent-charcoal: "#2e2930"
  accent-deep-navy: "#272d45"
  accent-midnight: "#2c3e50"
  accent-ice: "#b2f9e9"
  accent-pale-gray: "#e5e5e5"
  accent-warm-gray: "#edeae3"
  accent-light-gray: "#f4f4f6"
  accent-mist: "#c0bfc1"
  accent-silver: "#dedede"
  accent-soft-white: "#eeeeee"
  accent-eggshell: "#ececec"
  accent-teal-dark: "#0e7a82"
  accent-link-blue: "#007aff"
  accent-near-black: "#121212"

typography:
  display-xl:
    fontFamily: "'Gelica', 'Deutsch Gothic', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Gelica', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Deutsch Gothic', 'FuturaCondensedExtraBold', sans-serif"
    fontSize: 32px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: 1px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Basis Medium', 'Basis Regular', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Basis Bold', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Basis Medium', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Basis Bold', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  body-lg:
    fontFamily: "'Basis Regular', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Basis Regular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Basis Regular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Basis Light', sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Basis Light', sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.35
    letterSpacing: 0.15px
  badge:
    fontFamily: "'Basis Bold', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Basis Medium', sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  typewriter:
    fontFamily: "'Typewriter', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  typewriter-bold:
    fontFamily: "'Typewriter Bold', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Basis Medium', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Basis Medium', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "'Basis Regular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Basis Medium', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-marigold:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-accent:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  top-nav-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  search-bar-expanded:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 16px 20px
    height: 56px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-terracotta}"
  product-card-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-vegan:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  hero-banner:
    backgroundColor: "{colors.accent-sand}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    rounded: "{rounded.none}"
    padding: 64px 24px
  hero-banner-image:
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 32px
    height: 48px
  section-heading:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  section-subheading:
    typography: "{typography.body-lg}"
    textColor: "{colors.muted}"
  ingredient-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  ingredient-badge-highlight:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  footer:
    backgroundColor: "{colors.accent-charcoal}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.accent-pale-gray}"
  footer-heading:
    typography: "{typography.nav-link}"
    textColor: "{colors.canvas}"
  newsletter-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  newsletter-submit:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 48px
  cart-icon:
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  cart-icon-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    height: 20px
  account-icon:
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  mobile-menu-toggle:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 40px
  mobile-menu-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  mobile-menu-link:
    typography: "{typography.nav-link}"
    textColor: "{colors.ink}"
  mobile-menu-link-active:
    typography: "{typography.nav-link}"
    textColor: "{colors.primary}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: 0 0 16px 0
  rating-stars:
    textColor: "{colors.accent-marigold}"
  review-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  review-card-author:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  review-card-date:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    textColor: "{colors.primary}"
  error-message:
    backgroundColor: "{colors.accent-terracotta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  success-message:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
  tooltip:
    backgroundColor: "{colors.accent-charcoal}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  modal-overlay:
    backgroundColor: "{colors.accent-near-black}"
    opacity: 0.6
  modal-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 24px
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
    height: 32px
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    height: 24px
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    height: 4px
  checkbox:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.xs}"
    height: 20px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    height: 20px
  radio:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    rounded: "{rounded.full}"
    height: 20px
  radio-checked:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 20px
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 24px
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 20px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, using the deep violet (#2e3192) background with white text. Tight 4px corners ({rounded.xs}) give it a precise, editorial feel rather than a friendly pill. On hover, it shifts to the darker navy (#272d45). The disabled state uses a muted periwinkle (#9a9db1). Secondary buttons invert the scheme with a white background and violet text, and on hover gain a soft gray (#f7f7f8) background. Accent buttons in highlighter-yellow (#fff88a) and marigold (#ffcf2a) are used for promotional actions like "Shop the Sale" or "Get 20% Off" — these use dark ink (#2e2930) text for contrast. Pill-shaped variants ({rounded.full}) exist for smaller, inline actions like "Add to Cart" on product cards, using either violet or teal (#00caaa) backgrounds. Ghost buttons have no background and only violet text, used for secondary links like "Learn More" or "View Details".

### Text Inputs & Forms
**`text-input`** — Standard text fields use a white background, 4px corners, and 16px Basis Regular text. On focus, the border shifts to the primary violet. Textareas follow the same pattern with a larger height. Select inputs use a custom dropdown arrow in violet. Checkboxes and radio buttons are custom-styled with violet fill when selected, using 4px corners for checkboxes and full rounding for radios. Toggle switches use a pill shape with a white knob sliding over a gray track that turns violet when active. Quantity selectors for product pages use a soft gray background with violet +/- buttons.

### Navigation
**`top-nav`** — A fixed 72px white bar with the Moon Juice logo centered or left-aligned, navigation links in uppercase Basis Medium at 14px, and cart/account icons on the right. Links are spaced generously with 24px gaps. The active link uses violet text; inactive links use muted gray (#676986). On scroll, the nav compresses to 56px. The mobile menu toggle is a simple hamburger icon that opens a full-height white panel with stacked navigation links. The cart icon includes a yellow badge (#fff88a) showing item count.

### Product Cards
**`product-card`** — A white card with 8px rounding ({rounded.sm}) containing a product image, title in Basis Bold 16px, price in Basis Regular 16px, and an optional sale price in terracotta (#cf9567). Badges appear in the top-left corner using yellow (#fff88a) for general promotions, marigold (#ffcf2a) for sales, teal (#00caaa) for new arrivals, and lime (#b5de57) for vegan/plant-based labels. A small "Add to Cart" button appears on hover or is always visible on mobile. Cards use subtle shadows and a 1px hairline border (#d3d4dd).

### Hero Banners
**`hero-banner`** — Full-width sections using a warm sand background (#eceadd) with large Gelica or Deutsch Gothic headlines. The primary CTA button uses the violet scheme. Hero images are full-bleed with no rounding. Some hero variants use a split layout with text on one side and product photography on the other. The banner padding is generous at 64px top and bottom.

### Badges & Tags
**`product-card-badge`** — Small, uppercase labels in Basis Bold 11px with tight tracking (0.5px). They use 4px corners and minimal padding (2px 8px). The color system includes yellow (promo), marigold (sale), teal (new), and lime (vegan/plant-based). Ingredient badges use a pill shape ({rounded.full}) with soft gray background and caption text, or teal background for highlighted ingredients like "Ashwagandha" or "Adaptogens".

### Footer
**`footer`** — A deep charcoal (#2e2930) background with white and pale gray (#e5e5e5) text. Links are in Basis Regular 14px with generous vertical spacing. The newsletter signup combines a white text input with a marigold (#ffcf2a) submit button. The footer includes columns for Shop, Learn, Help, and Social links, plus legal text in caption size.

### Reviews
**`review-card`** — White cards with 8px rounding containing star ratings (marigold stars), reviewer name, date, and review text. Used on product detail pages in a scrollable horizontal strip or grid. The date uses caption styling in muted gray.

### Accordions
**`accordion-header`** — Used on product pages for "Details", "How to Use", and "Ingredients" sections. Headers are clickable with a plus/minus icon in violet, using title-md typography. Content panels expand with smooth animation and use body-md text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top nav collapses to hamburger menu; product cards stack vertically; hero banners use stacked text/image; footer columns stack; search bar moves to full-width banner; quantity selector becomes full-width |
| Tablet | 744–1128px | Two-column product grids; top nav shows limited links (Shop, Learn, Account); hero banners use side-by-side layout; footer shows 2-column grid; search bar is prominent but not full-width |
| Desktop | 1128–1440px | Full top nav with all links; 3-4 column product grids; hero banners use split layout with large typography; footer shows 4-column grid; search bar is compact in nav |
| Wide | > 1440px | Max-width container (1440px) centered; product grids can show 4-5 columns; hero banners use maximum typography scale; whitespace increases proportionally |

### Touch Targets
- All buttons and interactive elements are minimum 44px height on mobile
- Product card "Add to Cart" buttons are 48px height on touch devices
- Navigation links have 48px touch areas even if text is smaller
- Accordion headers are 48px minimum height
- Quantity selector buttons are 44px x 44px
- Cart and account icons are 44px x 44px

### Collapsing Strategy
- Top nav collapses from full links to hamburger menu at 744px breakpoint
- Product grids reduce columns: 4 → 3 → 2 → 1 as viewport shrinks
- Hero banners switch from side-by-side to stacked at 744px
- Footer columns collapse from 4 → 2 → 1
- Search bar expands from compact nav element to full-width banner below 744px
- Product detail pages switch from 2-column (images + info) to single-column stack
- Review strips switch from horizontal scroll to vertical stack on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only active/disabled states for primary buttons. Secondary, ghost, and accent button hover states are inferred from common patterns but not verified from live site CSS.
- **Error styling**: Error message component uses terracotta background based on extracted color (#cf9567) but exact error text styling, border colors, and iconography are unknown.
- **Focus states**: Focus ring styles (color, width, offset) for keyboard navigation were not extracted. Assumed primary violet with 2px offset based on common patterns.
- **Dark mode**: No dark mode tokens were found. The footer uses a dark background but the site appears to be light-mode only.
- **Sub-brand palettes**: Moon Juice may have seasonal or collection-specific color variations (e.g., "Sleep", "Beauty", "Brain" collections) that were not captured.
- **Animation/transition**: Timing functions, durations, and easing curves for hover states, accordion expansions, and page transitions were not extracted.
- **Shadow tokens**: Box-shadow values for product cards, modals, and dropdowns were not reliably extracted. Assumed subtle shadows based on visual inspection.
- **Icon system**: The site uses custom icons (cart, account, search, social) but their specific SVG paths, sizes, and stroke weights were not extracted.
- **Typography scale edge cases**: The extracted font declarations include "futura-pt" and "gelica" as web fonts, but exact fallback stacks and weight mappings for all text styles are inferred.
- **Checkout theme**: The meta theme-color (#2e2930) suggests a dark checkout flow, but specific checkout component styles (Shopify checkout overrides) were not extracted.
- **Accessibility**: Color contrast ratios for text on backgrounds were not verified. The yellow (#fff88a) on white may have contrast issues for small text.
