---
version: alpha
name: "Wilderness Systems"
source_url: "https://www.wildernesssystems.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep green (#108474) anchors Wilderness Systems not as a background but as the brand's central current — it floods the primary navigation bar, fills the "Shop Now" CTA, and appears as the dominant color in product imagery overlays, evoking the shadowed undersides of river canopies rather than a corporate identity. The palette draws from the extracted site: a secondary forest green (#277158) sits alongside a bright lime accent (#d2de31) that appears in sale badges and size-selector highlights, while a warm yellow (#fbcd0a) surfaces in star ratings and promotional ribbons. The typography stack runs Geologica for headlines — a geometric sans with subtle ink traps that suggest both precision and outdoor durability — paired with Inter for body copy, creating a clean information hierarchy across product detail pages. Cards use a soft {rounded.sm} corner radius (8px), avoiding the extreme pill shapes of lifestyle brands in favor of a more grounded, tool-like feel. The footer and secondary surfaces use a light gray (#f9fafb) that keeps the experience airy despite the heavy green palette, and product swatches appear as small circular thumbnails with {rounded.full} clipping. The overall mood is one of capable adventure — the greens are never military or camouflage, but rather the living green of riverbank vegetation, and the yellow accents read as safety-bright rather than playful.

colors:
  primary: "#108474"
  primary-active: "#0c5132"
  primary-disabled: "#c1e6e6"
  ink: "#1a1a1a"
  body: "#3a4d4d"
  muted: "#557777"
  muted-soft: "#6a7282"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  accent-lime: "#d2de31"
  accent-yellow: "#fbcd0a"
  accent-blue: "#7b8cde"
  accent-deep-blue: "#1a4daf"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  rating-star: "#fbcd0a"
  badge-sale: "#d2de31"
  badge-new: "#7b8cde"
  scrim: "#0a0a0a"

typography:
  display-xl:
    fontFamily: "'Geologica', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Geologica', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Geologica', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Geologica', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Geologica', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Geologica', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Geologica', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Geologica', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Geologica', 'Inter', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.1
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
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
  nav-bar-link-active:
    textColor: "{colors.on-primary}"
    borderBottom: "2px solid {colors.accent-lime}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  hero-cta:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  rating-stars:
    color: "{colors.rating-star}"
    fontSize: 16px
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand's deep green (#108474) with white text and an 8px corner radius. On hover, it darkens to the active forest shade (#0c5132). When disabled, it fades to a pale mint (#c1e6e6) to signal non-interactivity without introducing a gray. The button uses Geologica at 15px with 0.5px letter spacing, giving it a slightly technical, outdoor-gear feel.

**`button-secondary`** — An outlined variant with a white fill and a 2px solid border in the primary green. Text remains green, and on hover the border deepens to the active shade while the background shifts to the soft surface gray (#f9fafb). Used for secondary actions like "Learn More" or "View Details" alongside primary CTAs.

**`button-accent-lime`** — A high-visibility accent button using the lime green (#d2de31) with dark text. This appears on sale badges, promotional banners, and quick-add actions. It's shorter (36px) and uses the smaller button typography, making it suitable for inline use within product cards and collection grids.

### Navigation
**`nav-bar`** — A 72px-tall bar filled with the primary green (#108474), housing the brand logo on the left and navigation links in white. Active links are underlined with a 2px lime (#d2de31) border-bottom. The bar uses Geologica for link text at 14px with 0.5px letter spacing, maintaining the technical outdoor tone. On mobile, the bar collapses to a hamburger menu with a full-screen overlay.

**`nav-bar-link`** — Navigation links with 8px horizontal padding, white text, and a subtle hover state that adds opacity. Active page links gain the lime underline to provide clear wayfinding without relying on bold weights.

### Product Cards
**`product-card`** — A white card with an 8px corner radius containing a product image (top-rounded), title, and price. The image area fills the full card width with no internal padding, while title and price sit on 16px horizontal padding. Cards are displayed in responsive grids (2 columns on mobile, 3 on tablet, 4 on desktop) with 16px gaps between them.

**`badge-sale`** — A small uppercase badge in lime green (#d2de31) with dark text, 4px corner radius, and 4px/8px padding. Positioned absolutely over the top-left of product images to flag discounts or promotions.

**`badge-new`** — Identical sizing and positioning to the sale badge, but uses the soft blue (#7b8cde) with white text to denote new arrivals or recently added products.

### Forms
**`text-input`** — A standard input field with white background, 1px hairline border (#dedede), 8px corner radius, and 44px height. On focus, the border thickens to 2px and switches to the primary green (#108474). Placeholder text uses the muted color (#557777). Used across search, newsletter signup, and checkout forms.

### Hero
**`hero-section`** — A full-width section with the primary green background, white text, and generous vertical padding (64px). The hero headline uses display-xl (48px Geologica) with tight leading, and the CTA button uses the lime accent for maximum contrast against the green. The hero may include background imagery overlaid with a green scrim, with the text and CTA centered or left-aligned depending on the page.

### Footer
**`footer`** — A dark footer on the ink (#1a1a1a) background with white and muted-gray (#6a7282) text. Links start muted and brighten to full white on hover. The footer is divided into columns for product categories, support links, and social icons, with the brand logo and copyright at the bottom. Vertical padding matches the section token (64px).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards stack in 2 columns; hero text reduces to display-lg; footer columns stack vertically |
| Tablet | 744–1128px | Nav links remain visible but compact; product cards in 3 columns; hero maintains display-xl but with reduced padding |
| Desktop | 1128–1440px | Full nav with all links; product cards in 4 columns; hero at full size with 64px padding |
| Wide | > 1440px | Max-width container (1440px) centered; hero may include full-bleed background imagery |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (WCAG touch target compliance)
- Nav links have 16px vertical padding to ensure adequate tap area
- Color swatches are 32px with 8px touch padding
- Search bar maintains 44px height on all breakpoints

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product grids reduce columns: 4 → 3 → 2 as viewport narrows
- Footer columns stack vertically below 744px
- Hero section reduces vertical padding and font size on mobile
- Secondary navigation (category filters) collapses to a dropdown on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for most components were inferred from the primary-active color; actual site hover effects may include opacity changes, underlines, or shadow shifts not captured in extraction
- Error state styling for form inputs (red borders, error messages) could not be extracted — placeholder uses primary-active as a fallback
- Dark mode is not present on the live site; all colors assume light mode only
- Font sizes and line heights are estimated based on typical Geologica/Inter pairings at the extracted brand scale; actual site values may vary by 1-2px
- The extracted color list includes several generic web colors (#eeeeee, #f2f2f2, #bbbbbb) that likely represent framework defaults or checkout widgets — the true brand palette is centered on the greens (#108474, #277158) and the lime accent (#d2de31)
- Sub-brand or collection-specific palettes (e.g., fishing vs. touring kayaks) were not extractable
- Animation durations, easing curves, and transition properties are not documented
- The extracted font list includes JudgemeIcons and JudgemeStar, which are review-widget icon fonts, not brand typography
- Shopify checkout button colors and payment-widget colors (Afterpay, Klarna) are present in the extracted hex list but are not part of the brand design system
