---
version: alpha
name: "Fur"
source_url: "https://furyou.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fur is a body-care brand that treats grooming as a ritual of care, not a chore. The palette is anchored by a warm, botanical gold (`#beb132`) that appears on primary buttons and key accents, evoking honey, beeswax, and the brand's oil-based formulations. This gold sits against a deep navy ink (`#272d45`) used for body text and headlines, creating a sophisticated contrast that feels more apothecary than clinical. The canvas is a soft off-white (`#f9f9f9`) with subtle gray-blue surfaces (`#e5e5eb`, `#f4f4f6`) that keep the experience airy and calm. Accent teals (`#0e7a82`, `#b2f9e9`) and a muted slate (`#676986`) appear in product details, ingredient callouts, and secondary UI elements, reinforcing the brand's connection to natural ingredients and wellness. The typography relies on Superior Title Web for display and heading treatments — a serifed face with refined proportions that lends editorial warmth — while body copy and UI text fall back to system sans-serifs. Buttons use the gold with white text (`{colors.on-primary}`), and all corners are gently rounded (`{rounded.sm}` to `{rounded.md}`), never sharp, so the interface feels tactile and approachable. The overall mood is intimate, grounded, and quietly luxurious — a digital space that mirrors the experience of using the products themselves.

colors:
  primary: "#beb132"
  primary-active: "#a3962a"
  primary-disabled: "#ded9b0"
  ink: "#272d45"
  body: "#2c3e50"
  muted: "#676986"
  muted-soft: "#d3d4dd"
  hairline: "#dedede"
  hairline-soft: "#e5e5eb"
  canvas: "#f9f9f9"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-teal: "#0e7a82"
  accent-teal-light: "#b2f9e9"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  star-rating: "#beb132"
  error: "#c13515"
  success: "#0e7a82"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Superior Title Web', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Superior Title Web', Georgia, 'Times New Roman', serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Superior Title Web', Georgia, 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Superior Title Web', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Superior Title Web', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Superior Title Web', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.1px
  button-md:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "inherit, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
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
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focused:
    border: 1px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 1px 3px rgba(0,0,0,0.08)
  nav-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 0
  nav-link-active:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.base} 0"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.xs} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
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
    padding: 14px 32px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: 1px solid "{colors.hairline}"
  search-bar-focused:
    border: 1px solid "{colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  accordion-body:
    padding: "{spacing.md} 0 0"
  tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 16px
  ingredient-badge:
    backgroundColor: "{colors.accent-teal-light}"
    textColor: "{colors.accent-teal}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    border: 1px solid "{colors.hairline}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: 1px solid "{colors.hairline-soft}"
  cart-total:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand's warm gold (`{colors.primary}`) and white text. Used for "Add to Cart," "Subscribe," and key checkout actions. On hover, it darkens to `{colors.primary-active}`; when disabled, it fades to a pale gold (`{colors.primary-disabled}`). The button uses uppercase, semibold type (`{typography.button-md}`) with generous horizontal padding and a soft 8px radius that feels tactile without being playful.

**`button-secondary`** — An outlined variant on a white canvas with navy ink text. Used for secondary actions like "Learn More" or "View Ingredients." The active state shifts the background to the soft gray-blue surface (`{colors.surface-soft}`). Shares the same dimensions and typography as the primary button for visual consistency.

**`button-tertiary-text`** — A text-only link styled as a button, using the gold primary color. Used for inline actions like "Apply" or "Clear" in filters, or as a subtle "Edit" link in the cart. No background or border — just the text with hover underline.

**`button-pill`** — A fully rounded, compact button used for promotional badges, "Shop Now" strips, or mobile filters. Uses smaller uppercase type and fits in tighter spaces like category strips or hero overlays.

### Cards
**`product-card`** — The core product display unit on collection and search pages. A white card with a 12px radius, containing a product image (rounded top corners), a title in `{typography.title-sm}`, and a price in `{typography.body-md}`. The card has no border but gains a subtle shadow on hover. An optional `product-card-badge` in teal (`{colors.accent-teal}`) can appear on the image for "New" or "Best Seller" flags.

### Navigation
**`nav-bar`** — A fixed top bar at 72px height, white background, containing the brand logo, navigation links, and a cart icon. Links use uppercase, 14px type with 0.3px letter spacing. The active link or current page is indicated by the gold primary color. On scroll, the bar gains a light shadow for depth.

**`nav-link`** — Individual navigation items with transparent background and navy ink text. Active state switches to gold. No underline — the active state is implied by color alone, keeping the header clean.

### Forms
**`text-input`** — Standard text input fields for email, search, and address forms. A white background with a light gray border (`{colors.hairline}`). On focus, the border switches to gold. Error state uses a red border (`{colors.error}`). Disabled fields use the soft gray surface and muted text.

**`search-bar`** — A fully rounded pill input for site search, with a subtle border. On focus, the border turns gold. Used in the mobile nav and on search result pages.

### Footer
**`footer`** — A dark navy (`{colors.ink}`) footer section with white text for headings and muted gray-blue (`{colors.muted-soft}`) for links. Links turn gold on hover. Contains brand info, navigation, social links, and newsletter signup. Padding is generous at 48px top and bottom.

### Accordion
**`accordion`** — Collapsible sections used for product descriptions, ingredients, and FAQ. A white card with a 12px radius and a title in `{typography.title-sm}`. The body content appears below with standard body spacing. No borders — the card itself provides containment.

### Tabs
**`tab-active`** — Active tab indicator with a 2px gold bottom border and gold text. Used on product pages for "Description," "Ingredients," "How to Use" sections. Inactive tabs use muted gray text with no border.

### Badges & Tags
**`ingredient-badge`** — A pill-shaped badge in light teal (`{colors.accent-teal-light}`) with darker teal text, used to highlight key ingredients like "Aloe" or "Jojoba Oil" on product cards and detail pages.

**`rating-stars`** — Star icons in gold (`{colors.star-rating}`) at 16px, used on product cards and reviews. The same gold as the primary button, reinforcing the brand's signature color.

### Cart
**`cart-item`** — Individual line items in the cart drawer or page, with a white background and a soft bottom border. Contains product image, name, quantity selector, and price. The `quantity-selector` is a bordered input with 8px radius.

**`cart-total`** — The order total section, using `{typography.title-md}` in navy ink, with padding above for separation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger menu; product cards stack vertically; hero text reduces to `{typography.display-md}`; search bar moves to full-width below nav; footer links stack in a single column; buttons become full-width for easier tapping |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses `{typography.display-lg}`; side-by-side layout for product details (image left, info right); footer uses 2-3 columns |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero uses `{typography.display-xl}` with larger imagery; product detail page uses 60/40 split; footer uses 4 columns |
| Wide | > 1440px | Max-width container at 1440px with centered content; product grid can expand to 4 columns; hero uses larger imagery with more whitespace; all components maintain their desktop sizing |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px for touch accessibility
- Product card tap targets (title, price, image) are at least 48px tall
- Nav links have 8px vertical padding plus the 72px nav bar height for easy tapping
- Quantity selector buttons are 44x44px minimum
- Accordion headers are 48px tall for easy expansion

### Collapsing Strategy
- Top navigation collapses to a hamburger menu below 744px, with a slide-out drawer
- Product filters collapse into a modal or bottom sheet on mobile
- Product description tabs collapse into an accordion on mobile
- Footer navigation collapses from 4 columns to 1 column below 744px
- Hero sections reduce image size and stack content vertically on mobile
- Multi-column product grids collapse to single column on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, scale) could not be reliably extracted
- Error styling for form validation (inline messages, iconography) was inferred from common patterns
- Dark mode palette is not defined — the brand does not currently support it
- Sub-brand or seasonal color palettes (e.g., holiday, limited editions) are not captured
- Loading states (skeleton screens, spinners) were not observed on the live site
- Focus ring styles (outline, offset) for keyboard navigation were not visible
- Animation timing and easing curves (transitions, hover effects) are not specified
- The `slick` font-family declaration suggests a carousel library, but its styling is not documented
- `oke-widget-icons` references Okendo review widgets — their icon set and styling are not included
- Specific product swatch colors (for variants) are not captured — they vary by product
- The `#121212` scrim color is used for overlays but its opacity was not determined
- Button loading state (spinner replacement) is not defined
- Mobile bottom navigation or tab bar is not present on the current site
