---
version: alpha
name: "Cozy Earth"
source_url: "https://cozyearth.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Cozy Earth is a luxury bedding and loungewear brand that wraps you in a quiet, earth-toned sanctuary. The brand's visual language is anchored by a warm, muted palette drawn from nature — the primary `#6F534A` (a rich, warm brown from the meta theme-color) grounds every CTA and key interaction, while supporting tones like `#8b645a`, `#5f4c40`, and `#493338` create a sense of depth and comfort. The canvas is a soft `#fafafa`, not a stark white, and surfaces are built with `#f4f4f6` and `#f3ece0` to feel tactile and lived-in. Typography leans on the elegant serif "September Spirit" for display headings, paired with the clean, modern sans-serif "Work Sans" for body text — a combination that feels both heirloom and contemporary. Buttons are softly rounded (`{rounded.sm}`) and generously padded, while product cards use `{rounded.lg}` to echo the plushness of the bedding itself. The brand avoids hard edges and aggressive contrasts; instead, it layers subtle neutrals like `#d8d8d8`, `#b0b7be`, and `#a09998` to create a calm, aspirational atmosphere. Accent colors like `#1a2f5b` (a deep navy) and `#8c2231` (a muted burgundy) appear sparingly in badges and sale tags, adding just enough tension without breaking the serene mood. Every design decision — from the `{spacing.section}` padding to the `{rounded.full}` search bar — reinforces the promise of life-changing comfort.

colors:
  primary: "#6F534A"
  primary-active: "#5f4c40"
  primary-disabled: "#bbb1a8"
  ink: "#2e2d2d"
  body: "#404040"
  muted: "#676986"
  muted-soft: "#a09998"
  hairline: "#d8d8d8"
  hairline-soft: "#e5e5eb"
  canvas: "#fafafa"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-navy: "#1a2f5b"
  accent-burgundy: "#8c2231"
  accent-olive: "#4e543d"
  accent-slate: "#58646d"
  accent-stone: "#7a898f"
  accent-warm: "#8b645a"
  badge-sale: "#8c2231"
  badge-new: "#1a2f5b"
  star-rating: "#2e2d2d"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'September Spirit', 'ABC Gaisyr', serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'September Spirit', 'ABC Gaisyr', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'September Spirit', 'ABC Gaisyr', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Work Sans', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-burgundy}"
  select-dropdown:
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
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
  product-card-image:
    rounded: "{rounded.lg}"
  product-card-hover:
    boxShadow: "0 4px 20px rgba(0, 0, 0, 0.08)"
  product-card-badge:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  product-card-sale-badge:
    backgroundColor: "{colors.accent-burgundy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  accordion-open:
    border: "1px solid {colors.primary}"
  rating-stars:
    color: "{colors.star-rating}"
    size: "16px"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    height: 40px
    border: "1px solid {colors.hairline}"
  size-swatch:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
    height: 40px
    border: "1px solid {colors.hairline}"
  size-swatch-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
  color-swatch-selected:
    outline: "2px solid {colors.primary}"
    outlineOffset: "2px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, used for "Add to Cart", "Shop Now", and checkout flows. Rendered in the brand's warm brown `{colors.primary}` with white text and a soft 8px radius. On hover, it deepens to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}`, a muted taupe that signals non-interactivity without visual noise.

**`button-secondary`** — An outlined alternative for secondary actions like "View Details" or "Learn More". Uses a white background with a subtle `{colors.hairline}` border. On hover, the background shifts to `{colors.surface-soft}` and the border becomes `{colors.ink}`.

**`button-tertiary-text`** — A text-only button for inline actions like "Cancel" or "Clear filters". Uses `{colors.primary}` text on a transparent background, matching the brand's preference for understated interactions.

**`button-pill-primary`** — A fully rounded pill variant for promotional banners, newsletter signups, or sticky mobile CTAs. Shares the same color system as `button-primary` but with a friendlier, more tactile silhouette.

**`button-pill-outline`** — The pill-shaped outline counterpart, used for "Subscribe" or "Get 15% Off" prompts. The transparent background and thin border keep it light and inviting.

### Cards
**`product-card`** — The core product display unit on collection pages and search results. A white card with 20px rounded corners (`{rounded.lg}`) that cradles the product image and metadata. On hover, a subtle box shadow lifts the card, suggesting the plushness of the product within. Badges for "New" (`{colors.accent-navy}`) and "Sale" (`{colors.accent-burgundy}`) are pinned to the top-left corner with tight 4px rounding.

**`product-card-image`** — The image container within a product card, inheriting the same 20px radius to create a seamless, pillowy frame for product photography.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px tall on a white canvas. Links use `{typography.nav-link}` — a 14px medium-weight sans-serif with subtle letter spacing. Active and hover states shift the link color to `{colors.primary}`, creating a quiet but clear wayfinding signal.

**`nav-link-active`** and **`nav-link-hover`** — Both use the same `{colors.primary}` treatment, keeping the interaction model simple and predictable.

### Forms
**`text-input`** — Standard text input for forms, search, and checkout fields. A white background with a `{colors.hairline}` border and 8px radius. On focus, the border transitions to `{colors.primary}`. Error states use `{colors.accent-burgundy}` for the border, paired with a caption in the same color.

**`select-dropdown`** — Matches the `text-input` styling for visual consistency across form elements. The dropdown arrow is rendered in `{colors.muted}`.

**`quantity-selector`** — A compact input for adjusting product quantities, with a 40px height and `{colors.hairline}` border. The plus/minus buttons are `{colors.muted}` with a hover state of `{colors.ink}`.

**`size-swatch`** and **`size-swatch-selected`** — Size selection pills for product detail pages. Unselected swatches have a white background and hairline border. The selected state inverts to `{colors.ink}` background with white text, creating a clear visual anchor.

**`color-swatch`** and **`color-swatch-selected`** — Circular color swatches at 32px. The selected state is indicated by a 2px `{colors.primary}` outline with a 2px offset, ensuring accessibility for colorblind users.

### Search
**`search-bar`** — A full-rounded search bar with a `{colors.surface-soft}` background, inviting exploration without visual weight. On focus, it expands to a white background with a `{colors.primary}` border, signaling active input.

### Hero
**`hero-section`** — The primary hero banner on the homepage and landing pages. Uses `{colors.surface-soft}` as a warm, neutral backdrop that lets product photography and the `{typography.display-xl}` serif headline take center stage. The `hero-cta` button is the brand's primary brown, padded generously at 14px 32px.

### Footer
**`footer`** — A dark footer on `{colors.ink}` background with white text. Links are rendered in `{colors.muted-soft}` (`#a09998`) and lighten to full white on hover, creating a subtle glow effect against the dark canvas.

### Accordion
**`accordion`** — Used for FAQ sections, product details, and size guides. A white card with a `{colors.hairline-soft}` border and 8px radius. When open, the border shifts to `{colors.primary}`, and the chevron icon rotates to indicate expanded state.

### Badges
**`product-card-badge`** — A small, uppercase badge for "New" or "Best Seller" labels. Uses `{colors.accent-navy}` background with white text, tight 4px rounding, and 0.5px letter spacing for a refined, editorial feel.

**`product-card-sale-badge`** — A sale-specific badge using `{colors.accent-burgundy}` to create urgency while staying within the brand's muted palette.

### Rating
**`rating-stars`** — Star ratings rendered in `{colors.star-rating}` (near-black) at 16px, appearing on product cards and review sections. The brand avoids yellow or gold stars, keeping the rating system monochromatic and elegant.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-up), nav collapses to hamburger, hero text reduces to `{typography.display-lg}`, buttons become full-width, product card badges stack vertically, search bar collapses to icon |
| Tablet | 744–1128px | Two-column product grid (2-up), nav links remain visible but condensed, hero uses `{typography.display-xl}` at 32px, product cards show 2-across, footer links stack in 2 columns |
| Desktop | 1128–1440px | Three-column product grid (3-up), full nav bar with all links, hero uses full `{typography.display-xl}` at 42px, product cards show 3-across, footer links in 4 columns |
| Wide | > 1440px | Max-width container at 1440px, product grid can expand to 4-up on collection pages, hero content centered with generous padding, whitespace scales proportionally |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Product card tap targets (image, title, price, swatches) are individually tappable with 48px minimum touch areas
- Color swatches are 32px with 44px touch padding to meet WCAG touch target recommendations
- Quantity selector plus/minus buttons are 40px with 44px touch padding
- Mobile nav hamburger icon is 48px x 48px

### Collapsing Strategy
- Top navigation collapses to a hamburger menu on mobile (< 744px), with a slide-out drawer for links
- Product filters collapse into a sticky bottom sheet on mobile, with a "Filter" button that triggers the overlay
- Product image galleries collapse from a 2-up grid on desktop to a single-image carousel on mobile
- Footer link columns collapse from 4 columns on desktop to 2 columns on tablet, then to a single column with accordion-style expand/collapse on mobile
- Size and color swatches wrap to multiple rows on mobile instead of a single horizontal scroll
- Hero sections reduce padding from `{spacing.section}` to `{spacing.xxl}` on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components (only primary/secondary buttons and nav links have extracted hover data)
- Error state styling for forms beyond border color (no extracted error text colors or iconography)
- Focus ring styles and keyboard navigation indicators
- Dark mode color tokens (the brand may not support dark mode)
- Sub-brand or collection-specific palettes (e.g., Bamboo vs. Mulberry Silk collections may have unique accent colors)
- Loading states and skeleton screen patterns
- Toast/notification component styling
- Modal/dialog overlay styling and animation
- Tooltip and popover component design
- Pagination and infinite scroll patterns
- Mobile bottom navigation or tab bar styling
- Checkbox and radio button custom styling
- Price display formatting (currency symbol, decimal places, sale price strikethrough)
- Image aspect ratios and cropping behavior across breakpoints
- Animation timing and easing curves
- Typography scale for legal text, footnotes, and fine print
- Icon set and icon sizing guidelines
- Spacing scale for micro-interactions (e.g., icon-to-text gaps)
