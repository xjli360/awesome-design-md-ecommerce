---
version: alpha
name: "K18 Hair"
source_url: "https://www.k18hair.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  K18 Hair is a biomimetic haircare brand that speaks in the quiet authority of science, not the shout of beauty marketing. The brand’s canvas is a warm, almost parchment-like off-white (`#f1e8d9`), a color that appears as the meta theme-color and surfaces across the site as a grounding background tone — it feels like the inside of a vintage science journal, not a glossy beauty magazine. Against this, the brand deploys a restrained palette of near-blacks (`#141414`, `#111111`, `#121212`) for body copy and structural elements, creating a high-contrast, editorial reading experience. The primary brand voltage is a muted violet (`#655dc6`) that appears in CTAs, hover states, and key accents — it’s a color that suggests innovation and depth, not frivolity. Supporting accents include a sharp lime green (`#cfde3e`), a hot pink (`#f6418e`), and a deep blue (`#0457ce`), used sparingly for badges, ingredient callouts, and secondary actions. Typography is set in Inter, a clean, highly legible sans-serif that reinforces the brand’s scientific credibility. Headlines are set in bold weights with tight line heights, while body text runs at moderate sizes with generous leading. The interface is defined by soft, pill-shaped buttons (`{rounded.full}`) and cards with gentle rounding (`{rounded.lg}`), creating a tactile, approachable feel that contrasts with the clinical precision of the copy. The overall mood is one of quiet confidence — the brand trusts its science and lets the product speak, using whitespace, muted tones, and deliberate color pops to guide the eye without visual noise.

colors:
  primary: "#655dc6"
  primary-active: "#6450bb"
  primary-disabled: "#d9d9d9"
  ink: "#141414"
  body: "#333333"
  muted: "#545454"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#f1e8d9"
  surface-soft: "#f6f6f6"
  surface-card: "#fefefe"
  on-primary: "#ffffff"
  accent-green: "#cfde3e"
  accent-pink: "#f6418e"
  accent-blue: "#0457ce"
  accent-purple: "#a45cec"
  accent-red: "#df5657"
  link-blue: "#1990c6"
  link-blue-active: "#136f99"
  star-rating: "#007aff"
  badge-new: "#cfde3e"
  badge-sale: "#f6418e"

typography:
  display-xl:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.75px
  display-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.25px
  badge:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.full}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-tertiary-active:
    textColor: "{colors.primary-active}"
  button-pill-accent:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 36px
  icon-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-hover:
    backgroundColor: "{colors.surface-soft}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  textarea:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  select:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  radio-checked:
    border: "6px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-link-active:
    textColor: "{colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  logo:
    height: 32px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
  product-card-price:
    typography: "{typography.body-md}"
    fontWeight: 600
  product-card-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.base}"
  hero-title:
    typography: "{typography.display-xl}"
  hero-subtitle:
    typography: "{typography.display-sm}"
    color: "{colors.muted}"
  hero-cta:
    component: "{components.button-primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  search-icon:
    color: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.base}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.canvas}"
  footer-heading:
    typography: "{typography.title-sm}"
    color: "{colors.surface-card}"
  accordion:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  accordion-header:
    typography: "{typography.title-sm}"
  accordion-content:
    typography: "{typography.body-md}"
    color: "{colors.body}"
    padding: "{spacing.sm} 0"
  ingredient-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 12px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  rating-number:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  quantity-selector-button:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    height: 40px
    width: 40px
  quantity-selector-button-hover:
    backgroundColor: "{colors.hairline}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
  modal:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 32px rgba(0,0,0,0.12)"
  modal-overlay:
    backgroundColor: "rgba(20,20,20,0.6)"
  toast-success:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
  toast-error:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"
  badge-science:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button with the brand’s signature violet (`#655dc6`) background and white text. On hover, it shifts to a slightly deeper violet (`#6450bb`). The disabled state uses a light gray (`#d9d9d9`) background with muted text (`#888888`). Text is set in Inter Semi-Bold at 15px with 0.5px letter-spacing for a crisp, authoritative feel.

**`button-secondary`** — An outlined variant with a transparent background, a 2px solid black (`#141414`) border, and black text. On hover, the background fills with black and text inverts to the canvas color (`#f1e8d9`). Used for "Learn More" or "Add to Wishlist" actions where the primary button would be too dominant.

**`button-tertiary`** — A text-only button with the primary violet color and no background or border. On hover, the text deepens to `#6450bb`. Used for in-context actions like "View Details" or "Read More" within product cards or content sections.

**`button-pill-accent`** — A smaller, accent-colored pill button, typically using the brand’s lime green (`#cfde3e`) for "New" or "Shop Now" badges. Text is black (`#141414`) for high contrast against the bright background. Height is 36px for use in tighter spaces like product cards or category strips.

### Cards
**`product-card`** — A white (`#fefefe`) card with 20px rounding and 16px padding, containing a square product image with 12px rounding, a title in Inter Semi-Bold 16px, a price in 16px regular weight, and optional badges. On hover, a subtle box-shadow (`0 4px 12px rgba(0,0,0,0.08)`) lifts the card. Badges are pill-shaped and use the brand’s accent colors — green for "New," pink for "Sale," violet for "Science."

### Navigation
**`nav-bar`** — A 72px tall, fixed-position bar with the canvas background (`#f1e8d9`). Navigation links are set in Inter Medium at 14px with 0.25px letter-spacing. The active and hover states shift the link color to the primary violet (`#655dc6`). The logo sits at 32px height. On mobile, the nav collapses into a hamburger menu with a full-screen overlay.

### Forms
**`text-input`** — A standard input field with a white background, 12px rounding, 12px/16px padding, and a 1px solid `#dedede` border. On focus, the border thickens to 2px and turns primary violet. Error state uses a 2px red (`#df5657`) border. The height is 48px for comfortable touch targeting.

**`search-bar`** — A pill-shaped search input with 48px height, white background, and a 1px `#dedede` border. On focus, the border becomes 2px primary violet. The search icon is rendered in the muted gray (`#545454`). Used in the header and on the search results page.

### Footer
**`footer`** — A dark section with a near-black background (`#141414`) and light gray text (`#f6f6f6`). Links are set in Inter Medium at 14px with a muted gray (`#888888`) color, transitioning to the canvas color (`#f1e8d9`) on hover. Section headings use Inter Semi-Bold 16px in white. Padding is 64px top and bottom.

### Badges
**`badge-new`** — A lime green (`#cfde3e`) pill badge with black text, used to flag new products or collections. Text is Inter Bold at 11px, uppercase, with 0.5px letter-spacing. Padding is 4px 8px.

**`badge-sale`** — A hot pink (`#f6418e`) pill badge with white text, used for sale or promotional items. Same typography and sizing as the new badge.

**`badge-science`** — A violet (`#655dc6`) pill badge with white text, used to highlight products with biomimetic or scientific claims. Same typography and sizing.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero section reduces padding to 32px; buttons become full-width; search bar moves to a dedicated overlay; footer links stack in a single column |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but logo shrinks to 28px; hero uses 48px display font; side-by-side form layouts possible |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses 48px display font; multi-column footer; search bar visible in header |
| Wide | > 1440px | Max-width container at 1440px; content centered; product grid can expand to four columns; hero uses larger display sizes |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch target guidelines.
- Icon buttons are 40px x 40px with a 40px touch area.
- Product card links have a minimum 48px tap area.
- Accordion headers are 48px tall for easy tapping.
- Quantity selector buttons are 40px x 40px.

### Collapsing Strategy
- The top navigation collapses to a hamburger menu below 744px, with a full-screen overlay menu.
- The product grid collapses from 4 columns on wide screens to 3 on desktop, 2 on tablet, and 1 on mobile.
- The footer collapses from a 4-column layout on desktop to a single-column accordion on mobile.
- The hero section reduces vertical padding from 64px to 32px on mobile.
- Multi-step forms (e.g., checkout) collapse to single-step vertical layouts on mobile.
- Side-by-side product details (image + description) stack vertically below 744px.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover colors.
- Error styling for forms (e.g., error messages, error icons) is inferred from common patterns but not confirmed from the live site.
- Dark mode values are not present; the brand currently does not appear to support a dark theme.
- Sub-brand or collection-specific palettes (e.g., "K18 Professional" vs. "K18 Consumer") were not distinguishable.
- Loading states (spinners, skeleton screens) and their specific colors/sizes were not extracted.
- Animation durations, easing curves, and transition properties are not available.
- Focus ring styles (outline, offset, color) for keyboard navigation were not captured.
- The exact font weights for Inter (e.g., 400, 500, 600, 700) are inferred from common usage; the live site may use additional weights.
- The `swiper-icons` font family was found in declarations but its usage (likely for carousel navigation) was not fully mapped.
- Specific component spacing (e.g., gap between product cards, margin between sections) is estimated from common patterns.
- The brand’s icon set (SVG or font-based) was not extracted; only the search icon color is known.
- Print styles and reduced-motion preferences are not documented.
