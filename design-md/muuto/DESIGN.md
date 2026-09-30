---
version: alpha
name: "Muuto"
source_url: "https://www.muuto.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Muuto is a Scandinavian design brand rooted in the belief that great design should be accessible, human, and quietly joyful. The brand’s palette is anchored by a warm, almost off-white canvas (`#f9f8f2`) that feels like natural light on a matte wall, with a secondary canvas of `#efeeeb` and `#eeecea` that adds subtle depth without breaking the calm. The primary ink is a deep, soft charcoal (`#282828`) rather than a harsh black, used for body text and key structural lines, while a secondary ink (`#574846`) introduces a faint brown warmth that keeps the brand from feeling cold or sterile. Accent colors are used sparingly but deliberately: a muted teal (`#7bc7c7`), a dusty sage (`#b7d692`), a pale sky blue (`#e2f1fd`), and a soft clay (`#ca8268`) appear in product details, badges, and seasonal collections. These accents never shout — they sit at 30–50% saturation, as if filtered through a Scandinavian winter light. The typography is built on a dual-axis system: EuclidFlex (a geometric sans-serif with a humanist touch) for headlines and navigation, and Spectral (a serif with a literary, editorial feel) for body copy and product descriptions. This pairing gives Muuto a voice that is both modern and timeless, like a design magazine that happens to sell furniture. The brand avoids hard corners wherever possible — buttons use `{rounded.sm}` (8px), cards use `{rounded.md}` (12px), and the hero search bar uses `{rounded.full}` (9999px) — creating a tactile, approachable feel. The overall mood is one of deliberate restraint: generous whitespace, muted tones, and a focus on materiality and form over decoration. Every hex value in the system — from the hairline `#d9d9d9` to the surface-soft `#eeecea` — is chosen to feel like it belongs in a softly lit room, not a sterile grid.

colors:
  primary: "#7bc7c7"
  primary-active: "#39a4d6"
  primary-disabled: "#d9d9d9"
  ink: "#282828"
  body: "#574846"
  muted: "#7d7b76"
  muted-soft: "#ababab"
  hairline: "#d9d9d9"
  hairline-soft: "#e9e7e4"
  canvas: "#f9f8f2"
  surface-soft: "#efeeeb"
  surface-card: "#ffffff"
  surface-strong: "#eeecea"
  on-primary: "#ffffff"
  on-dark: "#f9f8f2"
  accent-teal: "#7bc7c7"
  accent-sage: "#b7d692"
  accent-sky: "#e2f1fd"
  accent-clay: "#ca8268"
  accent-ochre: "#50431c"
  accent-pine: "#223333"
  accent-mint: "#b6d98f"
  accent-lime: "#dee2a1"
  accent-forest: "#117744"
  accent-stone: "#cfccc8"
  accent-warm-gray: "#d7c6c0"
  star-rating: "#282828"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Spectral', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Spectral', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  caption-sm:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
  badge:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Spectral', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'EuclidFlex', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
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
  section: 80px

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
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    border: "1px solid {colors.hairline}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-tab-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
  search-field-segment:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: 8px 16px
  category-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
  category-tab-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-image:
    rounded: "{rounded.md}"
    objectFit: cover
  product-card-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  hero-search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "16px 24px"
    height: 56px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.on-dark}"
    typography: "{typography.link}"
  newsletter-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  newsletter-button:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"
    height: 44px
  accordion-header:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.lg} 0"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  swatch:
    rounded: "{rounded.full}"
    height: 32px
  swatch-active:
    rounded: "{rounded.full}"
    height: 32px
    border: "2px solid {colors.ink}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the Muuto experience, used for "Add to Cart", "Shop Now", and key conversion points. Rendered in the brand's muted teal (`{colors.primary}`) with white text and a soft 8px radius (`{rounded.sm}`) that feels tactile without being playful. On hover, the background shifts to a deeper sky blue (`{colors.primary-active}`), and in its disabled state it fades to a light gray (`{colors.primary-disabled}`) with muted text. The button uses EuclidFlex at 14px/500 weight with subtle letter-spacing, maintaining the brand's restrained editorial tone.

**`button-secondary`** — A bordered alternative to the primary button, used for "Learn More", "View Details", and secondary actions. It sits on the canvas background with a 1px hairline border (`{colors.hairline}`) and ink text, creating a clean, minimal appearance that doesn't compete with the primary CTA. On hover, the border darkens and a subtle background fill appears. The padding is intentionally 1px less on each side than the primary to account for the border, keeping both buttons at the same 44px height.

**`button-tertiary-text`** — A text-only button used for inline actions like "Clear filters", "Cancel", or "See all". It has no background or border, relying solely on the ink color and EuclidFlex typography for hierarchy. On hover, the text color shifts slightly to the muted body tone, providing a subtle interactive cue without visual weight.

**`button-pill`** — A fully rounded button (`{rounded.full}`) used for promotional badges, "New Arrivals" tags, and seasonal callouts. It uses the primary teal background with white text and a smaller font size (12px/500), making it feel like a friendly tag rather than a heavy button. The pill shape is a deliberate departure from the standard 8px radius, used only for special moments.

### Navigation
**`top-nav`** — The primary navigation bar, fixed at 72px height on a white canvas (`{colors.canvas}`). It carries the Muuto logo on the left, a centered category strip, and utility icons (search, account, cart) on the right. The nav links are set in EuclidFlex uppercase at 14px with 0.5px letter-spacing, creating a clean, architectural rhythm. The bar has a subtle bottom border (`{colors.hairline-soft}`) that separates it from the page content without adding visual noise.

**`nav-tab-active`** — The active state for navigation items, indicated by a 2px bottom border in the ink color. This replaces the common underline or background fill, keeping the navigation clean and typographically driven. The active tab retains the same font weight as inactive tabs, relying solely on the border for state indication.

**`category-strip`** — A horizontal scrolling strip of product categories (e.g., "Seating", "Tables", "Lighting", "Textiles") that sits below the top nav on collection pages. Each category is a pill-shaped chip (`{rounded.full}`) that toggles between inactive (transparent, muted text) and active (soft surface background, ink text) states. The strip has generous horizontal padding and a subtle fade on the edges to indicate scrollability.

### Cards
**`product-card`** — The core product display component, used on collection pages, search results, and related-product sections. It consists of a square-format image with `object-fit: cover` and a 12px rounded radius (`{rounded.md}`), followed by product name, designer name (in caption style), and price. The card has no background fill — it sits directly on the page canvas, relying on the image and typography for structure. On hover, the image scales slightly (105%) and a subtle shadow appears, but the overall effect remains restrained.

**`product-card-badge`** — A small badge overlaid on the product card image, used for "New", "Sale", or "Exclusive" labels. It uses the sage green accent (`{colors.accent-sage}`) with ink text, set in EuclidFlex uppercase at 11px with 0.5px letter-spacing. The badge has a 4px radius (`{rounded.xs}`) and minimal padding, making it feel like a discreet tag rather than a promotional shout.

### Forms
**`search-bar-pill`** — The primary search input, used in the hero section and the sticky search bar. It's a fully rounded pill (`{rounded.full}`) on a soft surface background (`{colors.surface-soft}`) with ink text and a search icon on the left. The placeholder text is set in Spectral body-sm, maintaining the brand's editorial feel even in utility components. On focus, the background shifts to white and a subtle ring appears.

**`newsletter-input`** — The email input used in the footer for newsletter signup. It has a soft surface background with a 1px hairline border and an 8px radius (`{rounded.sm}`), matching the button radius for visual consistency. The adjacent submit button is a solid ink-colored button with white text, creating a clear visual hierarchy between input and action.

**`filter-chip`** — A toggleable filter option used on collection pages for attributes like color, material, or price range. It's a pill-shaped chip (`{rounded.full}`) with a hairline border and ink text in the inactive state, and a solid ink background with white text in the active state. The chip has 6px vertical padding and 14px horizontal padding, making it compact enough for dense filter rows.

### Footer
**`footer`** — The site footer, rendered on a deep ink background (`{colors.ink}`) with light text (`{colors.on-dark}`). It contains four columns: "Shop" (product categories), "About" (brand info), "Support" (customer service), and "Follow" (social links). Each column has a caption-style heading in EuclidFlex uppercase, followed by Spectral body-sm links. The footer also includes the newsletter signup form and a bottom bar with legal links and payment icons.

### Hero
**`hero-section`** — The full-width hero banner used on the homepage and campaign pages. It has a soft surface background (`{colors.surface-soft}`) with a large display headline (EuclidFlex 48px/300 weight), a supporting body paragraph in Spectral, and a pill-shaped search bar. The hero uses generous vertical padding (80px top and bottom) and a subtle gradient overlay on background images to ensure text readability. The overall effect is spacious, calm, and inviting — like walking into a well-lit showroom.

### Accordion
**`accordion-header`** — Used on product detail pages for sections like "Description", "Materials", "Dimensions", and "Shipping". The header is a simple title-sm text with a bottom hairline-soft border, and a plus/minus icon on the right. On click, the content panel slides open with a smooth transition. The accordion pattern keeps product pages clean and scannable, allowing users to access details without overwhelming the visual hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Top nav collapses to hamburger menu; product cards go to single column (100% width); hero section reduces padding to 48px; search bar becomes full-width; category strip becomes horizontally scrollable; footer columns stack to 2 columns; product card images reduce to 3:4 aspect ratio |
| Tablet | 744–1128px | Top nav remains expanded but with reduced link spacing; product cards display in 2-column grid; hero padding reduces to 64px; category strip shows 4-5 visible categories; footer columns display in 2x2 grid; product card images maintain 1:1 aspect ratio |
| Desktop | 1128–1440px | Full top nav with all categories visible; product cards in 3-column grid; hero at full padding (80px); category strip shows 6-7 visible categories; footer in 4-column layout; product card images at 1:1 with generous whitespace |
| Wide | > 1440px | Content max-width caps at 1440px with centered layout; product cards in 4-column grid; hero content max-width at 1128px; category strip shows all categories; all components scale proportionally within the max-width constraint |

### Touch Targets
- All interactive elements (buttons, links, chips) have a minimum touch target of 44x44px on mobile and tablet
- Icon buttons (search, cart, account) are 40x40px with 8px internal padding, exceeding the 44px minimum
- Filter chips are 32px tall with 6px vertical padding, meeting the 44px touch target when accounting for padding
- Product card links have a full-card tap target on mobile, with a minimum height of 200px
- Accordion headers have a 48px minimum tap height on all devices

### Collapsing Strategy
- Top navigation collapses to a hamburger menu at 744px, with a slide-in drawer for category links
- Category strip becomes horizontally scrollable on mobile, with fade indicators on both edges
- Product grid collapses from 4 columns (wide) to 3 columns (desktop) to 2 columns (tablet) to 1 column (mobile)
- Footer collapses from 4 columns (desktop) to 2 columns (tablet) to stacked single column (mobile)
- Hero section reduces vertical padding from 80px to 48px on mobile, and the search bar becomes full-width
- Product detail accordions remain expanded on desktop (showing all sections) but collapse on mobile to save vertical space
- Filter sidebar collapses to a bottom sheet on mobile, triggered by a "Filter" button in the sticky header

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for buttons and interactive elements could not be fully extracted — the primary-active color (#39a4d6) is an educated guess based on the brand's accent palette, but actual hover transitions (duration, easing, color stops) remain unknown
- Error states for form inputs (validation colors, error message typography, border colors) were not present in the extracted data — a red accent (#ca8268 clay is the closest warm tone, but it's not a traditional error color)
- Dark mode values are entirely absent — the brand may not support dark mode, or it may use a different set of muted tones that weren't captured
- Sub-brand or collection-specific palettes (e.g., "Muuto x [Designer]" collaborations) may introduce additional accent colors beyond the 25 extracted hex values
- Focus ring styles (color, width, offset, border-radius) were not reliably extracted — the brand likely uses a subtle ink-colored ring, but the exact specification is unknown
- Loading states (skeleton screens, spinner colors, animation timing) were not captured in the extraction
- The exact font weights for EuclidFlex and Spectral beyond 300, 400, 500, 600, and 700 are unknown — the brand may use additional weights (e.g., 200, 800) for specific contexts
- The `object-fit: contain` declaration found in the CSS hints suggests some product images use contain rather than cover, but the specific use cases (e.g., fabric swatches, room shots) are unclear
- The meta theme-color (#ffffff) suggests a white browser chrome on mobile, but the brand may use different theme colors for specific pages or campaigns
- Animation and transition specifications (duration, easing curves, stagger delays) were not extracted — the brand likely uses subtle 200-300ms transitions with ease-in-out, but exact values are unknown
