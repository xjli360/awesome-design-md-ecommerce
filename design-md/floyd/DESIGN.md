---
version: alpha
name: "Floyd"
source_url: "https://floydhome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Floyd is a Detroit-born furniture brand that builds with architectural honesty — every joint exposed, every material declared. The palette is anchored in a deep, near-black ink (`#231e1e`) that reads as the brand's structural spine, appearing on the page background, primary text, and the site's `theme-color` meta tag. Against this gravity, the canvas shifts to a warm off-white (`#f8f6ed`) that feels more like raw linen than sterile white — a deliberate move away from the cool, clinical whites of most DTC furniture brands. Signature accents arrive as restrained voltage: a safety-orange (`#ff5436`) used for CTAs and price highlights, a cooler red (`#ef4123`) for sale badges, and a single electric blue (`#1351ee`) that appears on select interactive elements. The secondary palette reads like a material library — warm greige (`#d8d4c4`), stone (`#7e7b71`), and concrete (`#9e998f`) — colors that echo the plywood, powder-coated steel, and felt that Floyd uses in their actual products. A surprising lime (`#d5fa44`) and forest green (`#386641`) appear as accent swatches, likely tied to limited-edition collections or plant-adjacent lifestyle photography. Typography is where Floyd asserts its design credibility most clearly: Floyd Gothic (a bespoke sans-serif) carries display and body copy with a slightly condensed, industrial feel, while Floyd Inktrap (a serif with deliberate ink-traps at stroke junctions) is reserved for editorial moments — product stories, the "Our Story" page, and collection narratives. GT America Mono appears for technical details (dimensions, materials, care instructions) and Inter serves as a system fallback. The brand avoids hard corners on interactive elements (`{rounded.sm}` at 8px for buttons, `{rounded.md}` at 12px for cards) but never goes pill-shaped — the radii are present but understated, like a chamfered edge on a steel frame. The overall feeling is one of designed permanence: furniture that isn't trying to disappear, but to be lived with and repaired.

colors:
  primary: "#ff5436"
  primary-active: "#ef4123"
  primary-disabled: "#f8a08e"
  ink: "#231e1e"
  body: "#333333"
  muted: "#7e7b71"
  muted-soft: "#9e998f"
  hairline: "#d8d4c4"
  hairline-soft: "#e8e8e8"
  canvas: "#f8f6ed"
  surface-soft: "#fbf6f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#1351ee"
  accent-lime: "#d5fa44"
  accent-green: "#386641"
  sale-red: "#ef4123"
  star-rating: "#231e1e"
  scrim: "#1a1817"

typography:
  display-xl:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -1.2px
  display-lg:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.72px
  display-md:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -0.56px
  display-sm:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.22px
  title-md:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-sm:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0
  body-sm:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'GT America Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0.48px
    textTransform: uppercase
  button-md:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.56px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0.48px
    textTransform: uppercase
  link:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0
  nav-link:
    fontFamily: "'Floyd Gothic', Inter, -apple-system, system-ui, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.30
    letterSpacing: 0.28px
    textTransform: uppercase
  editorial-body:
    fontFamily: "'Floyd Inktrap', Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.70
    letterSpacing: 0
  editorial-heading:
    fontFamily: "'Floyd Inktrap', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.28px
  badge:
    fontFamily: "'GT America Mono', 'Courier New', monospace"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0.60px
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
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 14px 0
  button-pill:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-active:
    border: "1px solid {colors.ink}"
  text-input-error:
    border: "1px solid {colors.primary}"
  text-input-disabled:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
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
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.ink}"
  product-card-sale-badge:
    backgroundColor: "{colors.sale-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.40
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "0 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-active:
    border: "1px solid {colors.ink}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.hairline}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "0 0 {spacing.base}"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 48px
  cart-item:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  cart-total:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
  material-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: "2px solid {colors.hairline}"
  material-swatch-active:
    border: "2px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Checkout", and key conversion points. Rendered in Floyd's signature safety-orange (`{colors.primary}`) with white text and an 8px rounded corner (`{rounded.sm}`). The active state shifts to a deeper red (`{colors.primary-active}`), while the disabled state fades to a muted coral (`{colors.primary-disabled}`). Button text is always uppercase with 0.56px letter-spacing, reinforcing the brand's industrial typographic voice.

**`button-secondary`** — An outlined variant used for "Learn More", "View Details", and secondary actions. Features a 2px solid ink border on the warm canvas background, with the same uppercase button typography. On hover/active, the button inverts to a solid ink fill with canvas text, creating a satisfying tactile reversal.

**`button-tertiary`** — A text-only button with no background or border, used for "Cancel", "Skip", and inline actions within forms and modals. Maintains the same uppercase button typography and ink color, with padding only on the left and right to keep alignment with other form elements.

**`button-pill`** — A fully rounded variant (`{rounded.full}`) reserved for promotional badges, filter chips, and quick-add actions in the shopping experience. Uses the brand's ink color as background with canvas text, and a smaller uppercase button typography (`{typography.button-sm}`) to fit tighter UI contexts.

### Cards
**`product-card`** — The primary product display unit across collection pages and search results. A white card (`{colors.surface-card}`) with 12px rounded corners (`{rounded.md}`) and no border — the card floats on the warm canvas background. The image area occupies the top portion with rounded top corners, while the title and price sit below with base-16px padding. Sale items display a red badge (`{colors.sale-red}`) in monospace uppercase at the top-left of the image.

**`cart-item`** — A horizontal card within the cart drawer or page, showing product image, title, quantity selector, and price. Uses a white background with a soft hairline bottom border to separate items. The quantity selector is a bordered input with 8px rounding, matching the brand's form language.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height on the warm canvas background. Contains the Floyd logo (left), primary navigation links (center), and utility icons for search, account, and cart (right). On scroll, a 1px hairline bottom border appears to create visual separation from page content. Navigation links are uppercase with 0.28px letter-spacing, using the Floyd Gothic font at 500 weight.

**`nav-link-active`** — The current page or section indicator, rendered in full ink color with no underline or background — Floyd trusts typographic weight and color over decorative indicators.

**`nav-link-inactive`** — Non-active navigation links rendered in muted stone (`{colors.muted}`), with hover transitioning to full ink.

### Forms
**`text-input`** — Standard text input used across checkout, account forms, and newsletter signups. A warm canvas background with a hairline border and 8px rounding. On focus, the border switches to solid ink. Error states use the primary orange-red border to draw attention. Disabled inputs fade to a soft hairline background with muted text.

**`search-bar`** — A dedicated search input with the same styling as text inputs but with zero horizontal padding (content is inset via the input itself). Used in both the nav-bar search overlay and the dedicated search page.

### Footer
**`footer-section`** — A full-width footer with the brand's ink background, creating a dramatic inversion from the warm canvas of the main content area. Links are rendered in hairline (`{colors.hairline}`) and transition to white on hover. The footer uses body-sm typography for link lists and includes the brand's monospace caption for section headers like "Support", "Company", and "Legal".

### Hero
**`hero-section`** — The full-width hero area on the homepage and collection landing pages. Uses the warm canvas background with display-xl typography for headlines. Product photography sits full-bleed within the hero, with a subtle scrim overlay at 40% opacity to ensure text readability. The hero section uses section-level vertical padding (`{spacing.section}`) to create breathing room.

### Badges & Swatches
**`product-card-sale-badge`** — A small red badge with monospace uppercase text, 4px rounding, and tight padding. Used exclusively on sale items within product cards.

**`material-swatch`** — Circular color/material indicators (32px) used on product detail pages for options like frame color or upholstery. A hairline border contains the swatch, with the active state switching to an ink border. Swatch colors map to the brand's material palette (e.g., powder-coated steel, plywood, felt).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1-up), nav collapses to hamburger, hero text reduces to display-md, product cards stack vertically, footer links stack, search bar moves to overlay |
| Tablet | 744–1128px | Two-column product grid, nav links reduce to icons-only for utility items, hero maintains display-lg, product cards in 2-up grid, footer links in 2-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav link text visible, hero at display-xl, product cards in 3-up grid, footer links in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px with centered content, four-column product grid on collection pages, hero content constrained to 1200px |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px touch target height
- Product card tap targets extend to full card width for easy mobile selection
- Quantity selector buttons are 48px × 48px minimum for finger-friendly increment/decrement
- Material swatches are 44px minimum on mobile (up from 32px on desktop)
- Accordion triggers are full-width with 48px minimum height

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a full-screen overlay drawer
- Product filters collapse to a bottom sheet on mobile, with a "Filters" button triggering the overlay
- Product description and details collapse into accordion sections on mobile and tablet
- Footer link columns collapse to a single column on mobile, with accordion-style section headers
- The search bar collapses to an icon in the nav bar on mobile, opening a full-screen search overlay
- Multi-column product grids reduce to single column on mobile, 2-up on tablet

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for most components could not be reliably extracted — secondary button hover (fill inversion) is inferred from common patterns, but exact timing and easing values are unknown
- Error state styling for forms (error messages, validation icons) was not consistently present in the extracted data
- Dark mode or high-contrast mode specifications are not available — the brand currently operates in a single light theme
- Sub-brand or collection-specific color palettes (e.g., limited-edition drops) may exist but were not captured
- Animation and transition timing values (duration, easing curves) for hover, focus, and page transitions are missing
- Focus ring styles (outline color, offset, width) for keyboard accessibility were not consistently present
- The exact font weights available for Floyd Gothic and Floyd Inktrap beyond what's used in the typography scale are unknown
- Loading, empty, and error states for components like product cards, search results, and cart are not documented
- Print stylesheet specifications are not available
- The brand's icon system (SVG library, stroke weights, sizing conventions) was not extracted
- Modal and dialog overlay specifications (backdrop blur, animation, close button placement) are inferred from common patterns
