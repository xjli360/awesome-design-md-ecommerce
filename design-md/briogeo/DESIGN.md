---
version: alpha
name: "Briogeo"
source_url: "https://briogeohair.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clean, ingredient-forward haircare brand that lives at the intersection of natural wellness and clinical efficacy, Briogeo wraps its product story in a warm, approachable palette anchored by a vibrant coral-pink primary (#e61a4f) that pulses across CTAs, badges, and accent elements. The brand’s canvas is a soft off-white (#f8f8f8) rather than pure white, lending a tactile, almost paper-like warmth that distinguishes it from sterile beauty conventions. Secondary accents drift through a curated botanical spectrum — sage green (#14a34a), teal (#00a19b), lavender (#552e90), and blush (#eb80a8) — each tied to specific product families or ingredient stories (rose, charcoal, biotin, scalp care). Typography pairs a modern, slightly condensed sans-serif (Haffer SemiBold) for headlines with a warm serif (Tiempos) for body copy, creating a tension that feels both editorial and approachable. Buttons and cards use soft rounding (`{rounded.sm}` ~8px), while search bars and badges lean into pill shapes (`{rounded.full}`), reinforcing the brand’s friendly, non-clinical posture. The overall mood is clean but not cold — generous whitespace, muted hairlines (#dfdfdf), and a restrained use of the coral primary keep the focus on product photography and ingredient storytelling.

colors:
  primary: "#e61a4f"
  primary-active: "#d0021b"
  primary-disabled: "#f8a3b8"
  ink: "#444444"
  body: "#757575"
  muted: "#979797"
  muted-soft: "#b8c5d6"
  hairline: "#dfdfdf"
  hairline-soft: "#edf0f5"
  canvas: "#f8f8f8"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-rose: "#d74388"
  accent-blush: "#eb80a8"
  accent-lavender: "#552e90"
  accent-teal: "#00a19b"
  accent-sage: "#14a34a"
  accent-green: "#218246"
  accent-coral: "#ff585d"
  accent-orange: "#ff4713"
  accent-gold: "#ede757"
  accent-sky: "#bbe4ff"
  accent-blue: "#5b9ac5"
  accent-slate: "#597d95"
  accent-brown: "#936953"
  accent-purple: "#c964cf"
  accent-charcoal: "#5b7e96"
  star-rating: "#e61a4f"
  error: "#d0021b"
  success: "#14a34a"

typography:
  display-xl:
    fontFamily: "'Haffer SemiBold', 'Plus Jakarta Sans', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Haffer SemiBold', 'Plus Jakarta Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Haffer SemiBold', 'Plus Jakarta Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Haffer SemiBold', 'Plus Jakarta Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Tiempos', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Tiempos', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Tiempos', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  body-md:
    fontFamily: "'Plus Jakarta Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Plus Jakarta Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Plus Jakarta Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Plus Jakarta Sans', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Plus Jakarta Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Haffer SemiBold', 'Plus Jakarta Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Haffer SemiBold', 'Plus Jakarta Sans', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'Plus Jakarta Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Haffer SemiBold', 'Plus Jakarta Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'Plus Jakarta Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "'Plus Jakarta Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
    textColor: "{colors.accent-coral}"

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
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  select-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price-sale}"
    textColor: "{colors.accent-coral}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-new:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-badge-vegan:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  product-card-atc:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  hero-banner-overlay:
    backgroundColor: "{colors.ink}"
    opacity: 0.3
  ingredient-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  ingredient-badge-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  rating-stars:
    textColor: "{colors.star-rating}"
    fontSize: 14px
  rating-count:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: 16px 0
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: 0 0 16px 0
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted}"
  footer-heading:
    typography: "{typography.nav-link}"
    textColor: "{colors.ink}"
  social-icon:
    textColor: "{colors.ink}"
    fontSize: 20px
  newsletter-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 44px
  newsletter-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
  quantity-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 32px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  cart-remove:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  cart-total:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  checkout-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 52px
  breadcrumb-link:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-current:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
  pagination-button:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    height: 36px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  color-swatch-selected:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 40px
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  review-stars:
    textColor: "{colors.star-rating}"
    fontSize: 14px
  review-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  review-date:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted-soft}"
  modal-overlay:
    backgroundColor: "{colors.ink}"
    opacity: 0.5
  modal-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
  modal-close:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    height: 32px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  loading-spinner:
    textColor: "{colors.primary}"
    fontSize: 24px
  error-message:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  success-message:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand’s signature coral-pink (#e61a4f) with white text and soft 8px rounding. On hover/active, it deepens to a richer red (#d0021b). The disabled state uses a pale pink (#f8a3b8) to signal inactivity while maintaining brand cohesion. Text is set in Haffer SemiBold at 14px with 0.5px letter-spacing and uppercase for a confident, editorial feel.

**`button-secondary`** — An outlined or ghost variant on the off-white canvas (#f8f8f8) with dark ink (#444444) text. Maintains the same uppercase Haffer SemiBold typography and 8px rounding. Used for less prominent actions like “Learn More” or “View All.” The outline variant adds a 1px solid hairline (#dfdfdf) border.

**`button-pill-primary`** — A fully rounded pill variant of the primary button, used for quick-add actions on product cards and in search contexts. Smaller at 12px uppercase with tighter padding (10px 24px). The pill shape (`{rounded.full}`) reinforces the brand’s friendly, approachable posture.

### Cards
**`product-card`** — The core product display unit, a white card on the soft canvas with 8px rounding. Contains a product image (also softly rounded), a title in Tiempos serif at 16px, a price in Plus Jakarta Sans semibold, and optional badges (sale, new, vegan) that use the brand’s accent palette. A pill-shaped “Add to Cart” button appears on hover or as a persistent quick-action. Badges are small uppercase labels with 4px rounding and 2px 8px padding.

**`review-card`** — A white card for customer reviews, featuring star ratings in the brand coral (#e61a4f), review text in body-sm, and author/date metadata in muted tones. Uses 8px rounding and generous internal spacing.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on the off-white canvas. Navigation links are set in Haffer SemiBold at 13px uppercase with 0.3px letter-spacing. The active link uses the coral primary (#e61a4f). On scroll, the bar shrinks to 64px and gains a white background with a subtle bottom hairline. The search bar is a pill-shaped input with 44px height, white background, and placeholder text in muted gray (#979797).

**`footer`** — A full-width footer on the soft surface (#f5f5f5) with body text in muted gray (#757575). Links use the link typography (14px, medium weight) and are spaced generously. Includes a newsletter signup with a pill-shaped input and coral submit button, plus social icons in the brand ink.

### Forms
**`text-input`** — Standard text inputs at 48px height with white background, 8px rounding, and 12px 16px padding. On focus, the border shifts to the coral primary. Used for search, newsletter, and checkout forms.

**`select-dropdown`** — Matches the text-input styling with a custom dropdown arrow. Used for product sorting, quantity selection, and filter menus.

**`quantity-selector`** — A compact 40px control with minus/plus buttons flanking a numeric display. Uses the soft surface background (#f5f5f5) and 8px rounding. Buttons are transparent with 32px height and 4px rounding.

### Badges & Chips
**`product-card-badge`** — Small uppercase labels (11px, bold, 0.5px tracking) with 4px rounding. Color variants map to product attributes: coral for sale, sage for new, teal for vegan, and the primary coral-pink for bestseller or featured. Used as overlays on product images or inline below titles.

**`filter-chip`** — Pill-shaped filter options at 36px height with soft surface background. Active state fills with the coral primary and white text. Used in collection pages and search results for category, ingredient, and concern filtering.

**`ingredient-badge`** — Smaller pill badges (11px, regular weight) used to highlight key ingredients like “Rosehip Oil” or “Biotin.” Active state uses the coral primary. Arranged in horizontal scrollable strips on product detail pages.

### Hero & Content
**`hero-banner`** — Full-width hero sections with large display typography (Haffer SemiBold at 36px) on the soft surface. CTAs use the standard button-primary styling. An optional dark overlay (30% opacity) sits behind text for readability on photography. Used for seasonal campaigns, new launches, and brand storytelling.

**`accordion-header`** — Expandable sections for product details, ingredients, and usage instructions. Headers use Tiempos serif at 16px with 16px vertical padding. Content sections use body-sm in muted gray. The open/close indicator is a simple plus/minus icon in the brand ink.

### Feedback & Utility
**`loading-spinner`** — A coral (#e61a4f) spinning indicator used during async operations like add-to-cart and page transitions.

**`error-message`** — A red (#d0021b) banner with white text and 8px rounding for form validation errors and API failures.

**`success-message`** — A green (#14a34a) banner with white text for successful actions like adding to cart or subscribing to the newsletter.

**`tooltip`** — Small dark (#444444) labels with white text and 4px rounding, used for icon explanations and size guide hints.

**`modal-overlay`** — A 50% opacity dark scrim behind modals, with white modal content using 12px rounding and a close button in the top-right corner.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation, stacked footer, reduced hero typography (28px), full-width cards, search bar collapses to icon |
| Tablet | 744–1128px | Two-column product grid, persistent top nav with condensed links, two-column footer, hero text at 32px, filter sidebar collapses to horizontal chip strip |
| Desktop | 1128–1440px | Three-column product grid, full top nav with all links, three-column footer, hero at full 36px, persistent filter sidebar |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, expanded hero with larger imagery, additional whitespace in margins |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px touch target height
- Product card “Add to Cart” buttons are 36px on mobile, 44px on tablet and above
- Filter chips are 36px with 16px horizontal padding for easy tapping
- Quantity selector buttons are 32px with generous internal spacing
- Navigation links have 48px tap areas even when text is smaller

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile, with a slide-out drawer
- Product filters collapse to a horizontal chip strip on tablet, and to a “Filter” button that opens a modal on mobile
- Footer links collapse into accordion sections on mobile
- Product image galleries collapse to single-image carousels on mobile
- Multi-column content sections (ingredient lists, features) collapse to single-column stacks
- Search bar collapses to a magnifying glass icon that expands on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons could not be reliably extracted from the live site CSS
- Error state styling for form inputs (border color, iconography) was not consistently observed
- Focus ring styles (outline, offset, color) were not found in the extracted CSS
- Sub-brand or collection-specific color palettes (e.g., “Scalp Revival” vs. “Don’t Despair, Repair!”) may have additional accent colors not captured
- Dark mode or high-contrast mode styles were not present in the extracted data
- Animation and transition timing values (durations, easing functions) were not reliably extracted
- Dropdown menu styles for the navigation (mega menu, flyout) were not fully captured
- Mobile-specific typography sizes and line heights may differ from the desktop values listed
- The exact font weights for Haffer SemiBold (likely 600) and Tiempos (likely 400) are inferred from common usage
- Some accent colors may be used only in specific contexts (e.g., product imagery, ingredient icons) and not as general UI tokens
- The brand’s Shopify platform may introduce platform-specific components (cart drawer, checkout overlay) with their own styling
