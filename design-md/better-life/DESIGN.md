---
version: alpha
name: "Better Life"
source_url: "https://cleanhappens.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A marigold-yellow #ffc617 voltage cuts across a near-black #101010 and charcoal #252627 field — a cleaning brand that treats its packaging and site as a kitchen-counter product display rather than a chemical-utility catalog. The yellow appears on primary CTAs, badge accents, and the hero's central graphic element, reading as citrus-clean optimism against the deep ink of the body text and nav. Type runs Jost, a geometric sans-serif with open apertures and a friendly, approachable weight distribution — display sizes sit at moderate 500–600 weights rather than heavy 700+ punches, letting product photography and the brand's signature "Better Ingredient" messaging carry the hierarchy. Cards and buttons use soft 8px radii ({rounded.sm}) that feel sanitary without being clinical; there are no pill-shaped extremes or hard 90-degree corners on interactive elements. The palette includes a muted silver #a7a7a7 for secondary text and hairline borders, a warm gray #606f7b for body copy, and a clean white canvas that makes the yellow and charcoal pop like a well-staged pantry. The Shopify platform underpins a straightforward product-grid layout with category filters, a persistent top nav, and a footer dense with ingredient philosophy and social proof — the design trusts its color contrast and typographic clarity over decorative flourishes.

colors:
  primary: "#ffc617"
  primary-active: "#e0ad0a"
  primary-disabled: "#ffe899"
  ink: "#101010"
  body: "#3d4852"
  muted: "#606f7b"
  muted-soft: "#a7a7a7"
  hairline: "#dae1e7"
  hairline-soft: "#eef2f6"
  canvas: "#ffffff"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#101010"
  on-dark: "#ffffff"
  accent-pink: "#ef228b"
  accent-blue: "#2f70ee"
  accent-green: "#38c172"
  badge-yellow: "#ffc617"
  badge-text: "#101010"

typography:
  display-xl:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Jost', 'Segoe UI', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  button-secondary-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
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
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.badge-yellow}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 36px
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  social-icon:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 36px

## Components

### Buttons
**`button-primary`** — The brand's main action button, a marigold-yellow (#ffc617) filled rectangle with 8px rounded corners and uppercase Jost in weight 600. On hover, the background darkens to #e0ad0a; on disabled, it fades to a pale yellow #ffe899 with muted text. Used for "Add to Cart", "Shop Now", and primary form submissions.
**`button-secondary`** — An outlined variant with a white fill and ink (#101010) text, sharing the same uppercase button-md typography and 8px radius. Used for "Learn More" links, secondary CTAs, and cancel actions. The outline is a 1.5px solid hairline (#dae1e7) that darkens on hover.
**`button-secondary-outline`** — A transparent-background version of the secondary button, used when the button sits on a colored surface (e.g., hero section overlays). The outline remains ink (#101010) and the text stays ink; on hover, the fill becomes a light tint of the primary yellow.

### Cards
**`product-card`** — A white card with 8px rounded corners, containing a product image (also 8px rounded at the top), a title in title-sm, and a price in body-md. The card has no border but uses a subtle box-shadow (0 1px 3px rgba(0,0,0,0.08)) to lift off the canvas. On hover, the shadow deepens slightly (0 4px 12px rgba(0,0,0,0.12)).
**`product-card-image`** — The image container within a product card, cropped to a 1:1 aspect ratio with object-fit: contain to show the full product packaging. The image itself has 8px rounded corners at the top only, matching the card's radius.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height, white background, with nav links in uppercase Jost weight 600 at 14px. The logo sits left-aligned, the links are centered or right-aligned depending on viewport. On scroll, a 1px bottom hairline (#dae1e7) appears. The cart icon and search icon are positioned at the far right.
**`nav-link-active`** — The active page link uses ink (#101010) color with no underline; the inactive links use muted (#606f7b). There is no background change on hover — only a color shift to ink.

### Forms
**`text-input`** — A standard text input with white background, 8px rounded corners, 44px height, and 14px horizontal padding. The border is 1px solid hairline (#dae1e7). On focus, the border shifts to primary yellow (#ffc617) with a 2px stroke, and the placeholder text remains muted (#a7a7a7). Used for email signup, search, and checkout fields.

### Badges
**`badge-new`** — A small yellow pill badge (8px horizontal padding, 2px vertical) with uppercase 11px weight-700 text. Used to flag new products or collections. The yellow (#ffc617) on black (#101010) text provides high contrast at small sizes.
**`badge-sale`** — A pink (#ef228b) badge with white text, same typography and padding as the new badge. Used for sale or promotional items. The pink is the brand's secondary accent color, appearing only in badges and limited promotional elements.

### Hero
**`hero-section`** — The full-width hero area with a soft gray (#f8f9fa) background, large display-xl headline (36px, weight 600), and a primary CTA button. The hero may include a product image or lifestyle photography on the right side. The background color provides gentle contrast against the white canvas without competing with the yellow CTA.
**`hero-cta`** — A larger version of the primary button (48px height, 36px horizontal padding) used specifically in the hero section to draw maximum attention. Same yellow fill, uppercase typography, and 8px radius.

### Footer
**`footer-section`** — A dark footer with ink (#101010) background and white text. Links use the muted-soft (#a7a7a7) color for readability against the dark background. The footer contains columns for "Shop", "Learn", "About", and social links. Social icons are 36px circles with muted-soft fill, becoming white on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 item), nav collapses to hamburger menu, hero text reduces to 24px, buttons become full-width, footer stacks vertically |
| Tablet | 744–1128px | Two-column product grid (2 items), nav links remain visible but condensed, hero uses 28px display, side-by-side footer columns |
| Desktop | 1128–1440px | Three-column product grid (3 items), full nav with all links, hero at 36px display, standard button widths |
| Wide | > 1440px | Four-column product grid (4 items), max-width container (1440px) centered, hero may include additional decorative elements |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px to meet WCAG touch-target guidelines.
- Icon buttons (cart, search, hamburger) are 44px × 44px minimum, even if the visible icon is smaller.
- Product card tap targets (title, image, price) are the full card width, not individual text links.
- Footer links have 12px vertical padding to create comfortable tap spacing.

### Collapsing Strategy
- On mobile (< 744px), the top nav collapses into a hamburger menu with a slide-out drawer. The logo remains centered.
- The product grid collapses from 3–4 columns to 1 column on mobile, with full-width cards.
- The footer's multi-column layout collapses to a single column on mobile, with accordion-style sections for "Shop", "Learn", and "About".
- The hero section's side-by-side layout (text + image) collapses to stacked on mobile, with the image below the text.
- Category filter tabs collapse into a horizontal scrollable strip on mobile, with no wrapping.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font list includes `opw-*` font-family declarations (likely from a Shopify app or widget) — these are not part of the brand's core typography and have been excluded. The primary brand font is Jost.
- Hover and focus states for all components were inferred from common patterns; actual extracted hover colors are not available.
- Error styling for form inputs (border color, error message typography) could not be reliably extracted from the live site.
- The extracted color list includes several generic web colors (#38c172, #2f70ee, #ef228b) that may be from Shopify checkout widgets, social icons, or stock photography — these have been noted as accent colors but may not be part of the core brand palette.
- Dark mode styling is not present on the live site and has not been defined.
- Sub-brand or seasonal color palettes (e.g., holiday collections, limited editions) are not captured.
- The exact spacing scale was inferred from common Shopify patterns; the extracted site did not provide explicit spacing tokens.
- Animation and transition durations (e.g., button hover, card shadow) are not specified — a default 200ms ease-in-out is assumed.
