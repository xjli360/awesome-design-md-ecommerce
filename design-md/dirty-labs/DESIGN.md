---
version: alpha
name: "Dirty Labs"
source_url: "https://dirtylabs.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A science-first cleaning brand that wraps its laboratory rigor in a palette of deep navy (#014d93), soft sage (#bad3c0), and pale sky (#a9ccec) — colors that evoke a clean lab coat and a fresh rinse rather than the harsh chemical yellows or bleached whites of conventional laundry. The brand's primary voltage is a confident, almost academic blue (#014d93) that appears on every primary CTA, product badge, and header, while a secondary teal (#aadddd) and a warm off-white canvas (#f7f7f7) keep the experience approachable rather than sterile. Typography runs sofia-pro at moderate weights — display sits at 24–32px in weight 500/600, letting the brand's detailed ingredient science and product photography carry the emotional weight rather than heavy type. Product cards use softly rounded corners (`{rounded.md}` ~12px), while buttons and badges employ a tighter `{rounded.sm}` ~8px, suggesting precision without coldness. The checkout and utility areas introduce a restrained set of grays (#272727, #545454, #c7c7c7) that ground the pastel-adjacent palette, and a single accent red (#cb1f2b) appears sparingly on sale badges or error states — a deliberate jolt in an otherwise calm system. The overall feel is that of a modern chemistry lab that has been thoughtfully softened: beakers and bubbles rendered in watercolor tones, with every hex chosen to reinforce the promise of nontoxic efficacy.

colors:
  primary: "#014d93"
  primary-active: "#003d75"
  primary-disabled: "#a9ccec"
  ink: "#272727"
  body: "#545454"
  muted: "#737376"
  muted-soft: "#b4b4b4"
  hairline: "#c7c7c7"
  hairline-soft: "#e3e3e3"
  canvas: "#f7f7f7"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sage: "#bad3c0"
  accent-teal: "#aadddd"
  accent-sky: "#a9ccec"
  accent-red: "#cb1f2b"
  accent-warm: "#fff5bd"
  accent-gold: "#ffeb88"
  dark-ink: "#141414"
  secondary-gray: "#222222"

typography:
  display-xl:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-lg:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-md:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-lg:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  button-md:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  link:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'sofia-pro', 'Avenir', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.27
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-sage:
    backgroundColor: "{colors.accent-sage}"
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
  select-input:
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
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: 80px 0
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.accent-sky}"
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
  ingredient-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: 6px 12px
  rating-stars:
    color: "{colors.accent-gold}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: 16px 0
  cart-total:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  checkout-button:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, filled with deep navy `{colors.primary}` and white text. Used for "Add to Cart", "Subscribe", and primary form submissions. On hover, shifts to `{colors.primary-active}` (#003d75). Disabled state uses `{colors.primary-disabled}` (#a9ccec) with white text, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined or ghost variant on white canvas with navy text. Used for "Learn More", "View Ingredients", and secondary actions within product cards and content sections. The outline version uses a 1px solid `{colors.primary}` border.

**`button-tertiary-text`** — A text-only button with no background or border, used for "Cancel", "Skip", or inline navigation links within forms and modals. Hover adds a subtle underline.

**`button-pill-primary`** — A fully rounded pill variant of the primary button, used for subscription toggles, filter chips, and promotional badges. The pill shape (`{rounded.full}`) signals a toggleable or dismissible action.

**`button-pill-sage`** — A secondary pill using the soft sage `{colors.accent-sage}` background, used for ingredient tags, eco-certification badges, and "Learn About Ingredients" links. The sage tone reinforces the brand's natural, nontoxic positioning.

### Cards
**`product-card`** — A white card with `{rounded.md}` corners containing a product image, title, price, and optional badges. The card has a subtle shadow on hover (box-shadow: 0 2px 8px rgba(0,0,0,0.08)). Used on collection pages, search results, and "You May Also Like" sections.

**`product-card-title`** — The product name set in `{typography.title-sm}` with `{colors.ink}`. Truncates to two lines on mobile.

**`product-card-price`** — The price displayed in `{typography.body-md}` with `{colors.body}`. Sale prices appear in `{colors.accent-red}` with the original price struck through in `{colors.muted-soft}`.

### Badges
**`product-badge`** — A small sage-green badge (`{colors.accent-sage}`) used for "Best Seller", "Eco-Friendly", or "Plant-Based" labels. The uppercase `{typography.badge}` and tight `{rounded.xs}` corners give it a clinical, precise feel.

**`product-badge-sale`** — A red badge (`{colors.accent-red}`) reserved for sale and discount indicators. The red is the brand's only high-saturation accent, used sparingly to create urgency without breaking the calm palette.

**`product-badge-new`** — A teal badge (`{colors.accent-teal}`) for "New Arrival" or "Just Launched" labels. The teal bridges the navy primary and sage secondary, signaling freshness.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with white background (`{colors.canvas}`). Contains the brand logo, nav links, search icon, and cart icon. On scroll, receives a 1px bottom border in `{colors.hairline-soft}`.

**`nav-link-active`** — Active nav link styled in `{colors.primary}` with no underline. The active state is indicated by color alone, keeping the nav clean.

**`nav-link-inactive`** — Inactive nav link in `{colors.muted}` (#737376). Hover transitions to `{colors.ink}`.

### Forms
**`text-input`** — Standard text input with white background, `{rounded.sm}` corners, and 1px `{colors.hairline}` border. On focus, the border changes to `{colors.primary}` with a 2px stroke. Used for email signup, search, and address forms.

**`select-input`** — A styled select dropdown matching the text input dimensions and border. The dropdown arrow is a custom SVG in `{colors.muted}`.

### Footer
**`footer-section`** — A dark footer with `{colors.ink}` background and white text. Contains columns for "Shop", "Learn", "Support", and "Connect". Links use `{colors.accent-sky}` (#a9ccec) for a subtle, legible contrast against the dark background.

**`footer-link`** — Footer navigation links in sky blue (`{colors.accent-sky}`). Hover transitions to white.

### Misc
**`hero-section`** — Full-width hero banner with `{colors.canvas}` background, large headline in `{typography.display-xl}`, and a single `{colors.primary}` CTA button. The hero often features a lifestyle product photo with soft, natural lighting.

**`search-bar`** — A pill-shaped search bar (`{rounded.full}`) with white background and a magnifying glass icon in `{colors.muted}`. Used in the nav bar and on search result pages.

**`ingredient-badge`** — A small, fully rounded pill in `{colors.accent-sage}` used to display individual ingredient names (e.g., "Enzymes", "Plant Surfactants"). The badge style reinforces the brand's scientific transparency.

**`rating-stars`** — Star ratings displayed in `{colors.accent-gold}` (#ffeb88). Empty stars use `{colors.hairline}` (#c7c7c7).

**`quantity-selector`** — A compact horizontal control with minus/plus buttons and a central number display. Used on product pages and in the cart. Background is `{colors.surface-soft}` (#f4f4f4).

**`cart-item`** — A cart line item with product image, name, quantity selector, and price. Separated from other items by a 1px `{colors.hairline-soft}` border.

**`checkout-button`** — A prominent teal button (`{colors.accent-teal}`) used in the cart to proceed to checkout. The teal provides a visual departure from the primary navy, signaling a transition from browsing to purchasing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, stacked footer, reduced hero padding (40px), smaller display type (24px), buttons full-width |
| Tablet | 744–1128px | Two-column product grid, horizontal nav with dropdowns, two-column footer, hero padding 64px |
| Desktop | 1128–1440px | Three-column product grid, full horizontal nav, three-column footer, standard hero padding (80px) |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, expanded hero with larger imagery |

### Touch Targets
- All buttons and interactive elements minimum 44px height (48px preferred)
- Nav links minimum 44px tap area
- Quantity selector buttons minimum 40px tap area
- Search bar minimum 48px height

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px
- Product grid reduces columns: 4 → 3 → 2 → 1
- Footer columns stack: 4 → 2 → 1
- Hero text and CTA stack vertically below 744px
- Product card badges stack vertically on mobile (max 2 per row)
- Accordion sections collapse on all breakpoints, toggling on click

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted; only primary button hover is inferred from `primary-active`
- Error state styling for form inputs (border color, error message typography) not observed
- Success/confirmation state styling (e.g., "Added to Cart" toast) not observed
- Dark mode or high-contrast mode tokens not present
- Sub-brand or collection-specific palette variations (e.g., "Pet" line, "Kitchen" line) not confirmed
- Modal/overlay styling (background scrim opacity, close button placement) not extracted
- Loading state spinners or skeleton screen patterns not observed
- The extracted font list includes "Inter" and "swiper-icons" which may be used in specific components (e.g., carousels) but are not part of the primary brand typography
- Several extracted hex colors (#09aeec, #01c753, #3d85c6, #007aff, #007eff) appear to be Shopify checkout widget, social icon, or third-party service colors and are not included in the brand palette
- The extracted color list is heavily weighted toward grays and blues; the sage (#bad3c0) and teal (#aadddd) are the most distinctive brand-identifying colors beyond the primary navy
