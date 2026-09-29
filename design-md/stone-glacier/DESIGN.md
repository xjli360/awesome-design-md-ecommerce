---
version: alpha
name: "Stone Glacier"
source_url: "https://www.stoneglacier.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A backcountry hunting brand that builds its entire visual language around #111111, a near-black that reads as absolute authority against the white canvas of snowfields and alpine granite. The palette is deliberately austere — #111111 for all primary text and heavy structural elements, #d9d9d9 for secondary copy and muted labels, and a single accent of #4469af that appears only in navigation links and selectable UI states, a cool blue that echoes the high-altitude sky rather than any corporate identity. The brand's true voltage comes from #c8232c, a desaturated crimson used sparingly for sale badges, inventory warnings, and the cart count — it lands like a blood spot on snow, impossible to ignore. Type runs Barlow at generous sizes (display at 32px with 1.2 line height, body at 16px with 1.5) set in weights 400–700, with Figtree appearing as a secondary face for product descriptions and technical specs. Cards and buttons use {rounded.sm} (8px) — enough softness to feel intentional, not enough to suggest anything recreational. The product grid is ruthlessly square: 1:1 aspect ratio on thumbnails, tight {spacing.sm} gutters, and no decorative borders except a {hairline} (#dedede) that separates the footer from the body. Every component is built for gloved hands — {spacing.lg} padding on all touch targets, 48px minimum button height, and a sticky top nav that never collapses below 64px. The search bar is a full-width input with {rounded.sm} corners and a #4469af focus ring, not a pill — this is a tool, not a toy. The brand trusts its product photography (always on-location, always in low-angle golden hour) to carry the emotional weight, keeping the UI as transparent as possible.

colors:
  primary: "#111111"
  primary-active: "#363636"
  primary-disabled: "#777777"
  ink: "#111111"
  body: "#363636"
  muted: "#696969"
  muted-soft: "#a1a1a1"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#4469af"
  accent-blue-hover: "#0081c3"
  accent-red: "#c8232c"
  accent-red-hover: "#c72e2f"
  accent-green: "#1b9500"
  sale-badge-bg: "#c8232c"
  sale-badge-text: "#ffffff"
  inventory-warning: "#cc6633"
  social-facebook: "#4469af"
  social-twitter: "#00aced"
  social-instagram: "#c8232c"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  product-name:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  product-price:
    fontFamily: "'Barlow', 'Figtree', monospace, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
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
    padding: 14px 32px
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
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-accent-red-hover:
    backgroundColor: "{colors.accent-red-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
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
    focusBorder: "2px solid {colors.accent-blue}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "2px solid {colors.accent-red}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.accent-blue}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.product-name}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    aspectRatio: "1/1"
    rounded: "{rounded.sm}"
    objectFit: "cover"
  product-card-name:
    typography: "{typography.product-name}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.product-price}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  sale-badge:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  inventory-badge:
    backgroundColor: "{colors.inventory-warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  new-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
    hoverTextColor: "{colors.on-primary}"
  social-icon:
    height: 32px
    width: 32px
    rounded: "{rounded.full}"
  social-icon-facebook:
    backgroundColor: "{colors.social-facebook}"
    textColor: "{colors.on-primary}"
  social-icon-twitter:
    backgroundColor: "{colors.social-twitter}"
    textColor: "{colors.on-primary}"
  social-icon-instagram:
    backgroundColor: "{colors.social-instagram}"
    textColor: "{colors.on-primary}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: "16px 40px"
    height: 56px
  cart-count:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    height: 20px
    minWidth: 20px
    padding: "0 6px"

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the site. Solid #111111 fill with white text, 48px height, and {rounded.sm} corners. On hover, shifts to #363636; disabled state uses #777777 with reduced opacity. Used for "Add to Cart", "Checkout", and primary form submissions.

**`button-secondary`** — Outlined variant with a 2px #111111 border on white canvas. Text and border both use {colors.ink}. Active state fills with {colors.surface-soft} (#f6f6f6). Used for "View Details", "Compare", and secondary actions in product cards.

**`button-accent-red`** — High-emphasis CTA reserved for urgency actions: "Shop Sale", "Limited Stock", and the hero CTA. Uses #c8232c fill with white text, hover shifts to #c72e2f. Always paired with {typography.button-md} or {typography.button-lg}.

**`button-pill`** — Compact, fully rounded button for filter tags, category pills, and mobile navigation toggles. 40px height with {rounded.full}, uses {typography.button-sm}. Appears in the category strip and mobile filter drawer.

### Cards
**`product-card`** — The core product display unit. White background, no padding on the image container, {rounded.sm} on the whole card. Image forces 1:1 aspect ratio with `object-fit: cover`. Product name sits below in {typography.product-name} (16px, weight 600), price in {typography.product-price} (16px, weight 400, {colors.muted}). Cards have no shadow — the brand relies on the photography and the grid rhythm alone.

**`product-card` badges** — Three badge types overlay the top-left corner of the product image: `sale-badge` (#c8232c), `new-badge` (#1b9500), and `inventory-badge` (#cc6633). All use {typography.badge} (11px, weight 700, uppercase) with {rounded.xs} and 4px/8px padding.

### Navigation
**`nav-bar`** — Fixed top navigation at 72px height, white background with a single {colors.hairline} bottom border. Logo sits left, nav links center (or right on mobile), cart icon with `cart-count` badge far right. Links use {typography.nav-link} (14px, weight 600, uppercase, 0.5px letter spacing). Active page gets a 2px bottom border in {colors.ink}.

**`nav-link`** — Uppercase, 14px, weight 600, with 0.5px letter spacing. Active state uses {colors.ink} with underline; inactive uses {colors.muted}. No hover color change — the brand trusts the uppercase weight to signal clickability.

### Forms
**`text-input`** — Standard input field at 48px height with {rounded.sm}, 1px {colors.hairline} border, and 12px/16px padding. Focus state swaps to a 2px {colors.accent-blue} (#4469af) border. Error state uses 2px {colors.accent-red} (#c8232c). Placeholder text in {colors.muted-soft}.

**`search-bar`** — Full-width search input with {colors.surface-soft} background, 1px {colors.hairline} border, and {rounded.sm}. Focus state mirrors text-input with the {colors.accent-blue} ring. No pill shape — this is a functional tool, not a decorative element.

### Footer
**`footer`** — Full-width dark section with #111111 background and white text. Links in {colors.muted-soft} (#a1a1a1) that hover to white. Social icons are 32px circles with brand-specific colors: Facebook (#4469af), Twitter (#00aced), Instagram (#c8232c). Padding uses {spacing.section} (64px) top and bottom, {spacing.xl} (32px) sides.

### Hero
**`hero-section`** — Full-width hero with #111111 background, white text, and a minimum height of 400px. Uses {typography.display-xl} (32px, weight 700) for the headline. The hero CTA is `button-accent-red` at 56px height with {typography.button-lg} (18px, weight 600). Background may feature a full-bleed product image with a dark scrim overlay.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product grid goes 1 column; hero min-height reduces to 300px; search bar moves below nav; footer stacks vertically |
| Tablet | 744–1128px | Product grid shows 2 columns; nav links remain visible but reduce font size to 12px; hero text scales to 28px |
| Desktop | 1128–1440px | Product grid shows 3 columns; full nav with all links; hero at full 400px min-height; search bar in nav |
| Wide | > 1440px | Product grid shows 4 columns; max-width container at 1440px; hero may expand to 500px min-height |

### Touch Targets
- All buttons and interactive elements maintain minimum 48px height and 44px width on mobile.
- Nav links have 44px minimum tap area even when text is smaller.
- Cart count badge is 20px minimum — always tappable.
- Search bar input field is 48px tall with 16px padding for easy tapping.

### Collapsing Strategy
- Primary nav collapses to a hamburger menu below 744px. The hamburger icon uses a 44x44px touch target.
- Product filters collapse into a slide-out drawer on mobile, triggered by a "Filter" button with a badge showing active filter count.
- Footer link columns stack vertically on mobile, with each section becoming an accordion that expands on tap.
- Secondary navigation (breadcrumbs, category sub-nav) hides entirely on mobile, replaced by a "Back" button and the page title.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components could not be reliably extracted from the live site CSS. The active/disabled states provided are best guesses based on common patterns.
- Error styling for forms (error messages, validation icons) was not observed. The `text-input-error` border color is inferred from the accent-red palette.
- Dark mode is not supported — the site uses a white canvas exclusively.
- The exact font stack order between Barlow and Figtree is unclear; the extracted CSS showed both but did not specify which is primary for which context. The typography block assumes Barlow as the primary display face and Figtree as a secondary body face, but this may be reversed.
- Sub-brand or collection-specific palettes (e.g., "Stone Glacier Pro" or "Guide Series") were not observed.
- Loading states, skeleton screens, and empty states were not captured.
- The `object-fit: cover` declaration was found on images but the exact selectors are unknown — assumed for product card images and hero backgrounds.
- Checkout flow colors (Shopify Pay buttons, Klarna badges) were filtered from the extracted palette but may appear in the live site's cart and checkout pages.
- The accent-blue (#4469af) may be a Shopify default rather than a brand choice — it appears only in navigation links and focus rings, not in any brand logo or marketing material.
