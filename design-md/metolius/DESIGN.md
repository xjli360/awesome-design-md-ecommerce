---
version: alpha
name: "Metolius"
source_url: "https://www.metoliusclimbing.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A climbing-hardware brand that works in the gap between alpine severity and gym-friendly color, anchored on a warm off-white canvas (#f5f3ee) that reads like sun-bleached limestone rather than sterile gallery white. The brand voltage lives in two accents: a deep forest-teal (#108474) that appears on primary CTAs, product badges, and category headers, and a signal-red (#e4002b) reserved for sale markers, warning labels, and the brand’s own logo mark — a deliberate tension between the organic and the urgent. Type runs Archivo Narrow at condensed widths for headlines (tight tracking, 80–90% of standard character spacing) and Nunito Sans for body copy, creating a system that feels both technical and approachable: the narrow face echoes the verticality of a crack climb, while the rounder sans keeps instructional text legible at small sizes. Product cards use soft corners (`{rounded.sm}`) on a near-white surface (#f9fafb) with a subtle hairline (#dedede) that suggests precision without severity. The checkout flow introduces a marigold accent (#fbcd0a) for promotional banners and a muted lavender (#a89cc8) for limited-edition colorways — signals that Metolius treats gear as both tool and object of desire. Navigation is compact: a sticky top bar with the logo left, category links center, and a search icon right, all on the canvas color with no background fill, letting product photography carry the visual weight. The brand’s design ethos is “climb-ready clarity” — every element that can be reduced to a line or a pill shape is, from the search bar to the add-to-cart button, and the generous whitespace (`{spacing.section}` between major blocks) gives the eye the same rest a climber gets between pitches.

colors:
  primary: "#108474"
  primary-active: "#0d6b5c"
  primary-disabled: "#a3d4c9"
  ink: "#151515"
  body: "#444444"
  muted: "#7b7b7b"
  muted-soft: "#939393"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f5f3ee"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#e4002b"
  accent-marigold: "#fbcd0a"
  accent-lavender: "#a89cc8"
  accent-teal-light: "#c1e6e6"
  accent-green: "#279a4b"
  accent-orange: "#fb9e5b"
  star-rating: "#fbcd0a"
  sale-badge: "#e4002b"
  logo-mark: "#e4002b"

typography:
  display-xl:
    fontFamily: "'Archivo Narrow', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Archivo Narrow', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Archivo Narrow', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
  button-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    color: "{colors.star-rating}"
    fontSize: 14px
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted}"
  footer-link-hover:
    color: "{colors.primary}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with forest-teal (#108474) and white text. Used for "Add to Cart," "Shop Now," and primary checkout flows. On hover it deepens to `{colors.primary-active}` (#0d6b5c), and on disabled it fades to a muted teal (#a3d4c9). The 8px corner (`{rounded.sm}`) and 44px height keep it substantial without feeling heavy.

**`button-secondary`** — An outlined variant on the warm canvas background, with a 2px ink (#151515) border. Used for "View Details," "Learn More," and secondary actions. On hover the fill swaps to ink and text inverts to canvas, creating a crisp reversal that signals interactivity without competing with the primary.

**`button-tertiary`** — A text-only button in the primary teal, used for "Read Reviews" and "Compare" links within product cards. No background or border — just the color and hover underline to keep the UI clean.

**`button-sale`** — A red (#e4002b) filled button reserved for clearance and limited-time offers. Same dimensions and corner radius as `button-primary`, but the red signals urgency and discount. Used sparingly — never more than one per page.

### Cards
**`product-card`** — The core product display unit, a white (#ffffff) card on the soft surface (#f9fafb) with 8px rounded corners. The product image sits at the top with matching corner radius, followed by the title in `{typography.title-sm}`, the price in `{typography.price}`, and a row of star ratings (marigold #fbcd0a). A subtle shadow or border is absent — the card relies on the contrast between white and the warm canvas background for separation. Hover state adds a 1px hairline (#dedede) border to define the edge.

**`sale-badge`** — A small red pill (2px vertical padding, 8px horizontal) positioned at the top-left of product-card images. Uses `{typography.badge}` (11px, bold, uppercase) to announce "SALE" or the discount percentage. The red (#e4002b) is the same as the logo mark, creating a visual thread between brand identity and promotional signals.

**`new-badge`** — A teal (#108474) pill badge for new arrivals. Same dimensions and typography as the sale badge, but the teal signals freshness rather than urgency. Never appears on the same card as the sale badge.

### Navigation
**`nav-bar`** — A sticky top bar at 64px height on the warm canvas background. The Metolius logo (red #e4002b) sits left, category links (Climbing Gear, Training, Apparel, etc.) run center in uppercase `{typography.nav-link}`, and a search icon and cart icon sit right. No background fill — the canvas shows through, and the bar is separated from content by a 1px hairline (#dedede) bottom border. On scroll, the bar gains a subtle shadow to float above content.

**`search-bar`** — A full-rounded pill (40px height) with a 1px hairline border, placed in the nav bar or as a full-width hero element on the search page. The pill shape echoes climbing carabiners and quickdraws — a subtle product-language connection. On focus, the border switches to 2px primary teal.

### Forms
**`text-input`** — Standard form fields for checkout, account creation, and contact forms. White background, 1px hairline border, 8px corners, 44px height. On focus the border thickens to 2px primary teal (#108474). Labels sit above the field in `{typography.caption}` with muted (#7b7b7b) color. Error states use a red (#e4002b) border and helper text.

### Footer
The footer spans full-width on the warm canvas background, with links in `{typography.link}` at muted (#7b7b7b) that hover to primary teal. Social icons (Instagram, YouTube, Facebook) appear in a row, using the brand's extracted social colors (#3b5998 for Facebook, etc.). A marigold (#fbcd0a) accent bar runs across the top of the footer for promotional banners ("Free Shipping on Orders Over $50"). The copyright line sits at the bottom in `{typography.caption-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack single-column; search bar moves to full-width below nav; section padding reduces to 32px; buttons go full-width; footer links stack vertically |
| Tablet | 744–1128px | Nav bar shows 4–5 category links with overflow menu; product cards in 2-column grid; search bar remains in nav but shrinks to icon-only on scroll; section padding at 48px |
| Desktop | 1128–1440px | Full nav bar with all categories; product cards in 3-column grid; search bar visible as pill; section padding at 64px |
| Wide | > 1440px | Max-width container at 1440px centered; product cards in 4-column grid; additional whitespace on sides |

### Touch Targets
- All buttons and interactive elements minimum 44px height (WCAG compliant)
- Nav bar hamburger icon 48x48px tap area
- Product card tap targets (title, image, button) minimum 44px
- Search icon and cart icon 44x44px tap areas
- Footer links minimum 44px tap height (padding added on mobile)

### Collapsing Strategy
- Nav bar: category links collapse into hamburger menu below 744px; search icon remains visible, cart icon remains visible
- Product filters: collapse into a "Filter" button that opens a slide-in panel on mobile
- Footer: multi-column layout collapses to single column below 744px; social icons remain in a row
- Product images: secondary images collapse to a single thumbnail strip on mobile; swipe gestures replace hover zooms

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and active states for all components were inferred from brand logic, not extracted from the live site — the extracted CSS did not include pseudo-class styles
- Error state styling for forms (red borders, helper text colors) is assumed based on convention; actual error hex values were not found in extraction
- Dark mode is not present on the live site — no dark-mode tokens exist in the extracted data
- Sub-brand or collection-specific palettes (e.g., "Metolius Training" vs. "Metolius Apparel") were not distinguishable from the extraction
- Font weights for Archivo Narrow and Nunito Sans were inferred from typical usage; the extracted font-family declarations did not include weight values
- The extracted color list includes several generic web colors (#eeeeee, #f2f2f2, #fafafa, #aaaaaa, #888888, #121212) that are likely framework defaults or stock-image tones — the true brand palette was identified by the distinctive teal (#108474), red (#e4002b), marigold (#fbcd0a), and lavender (#a89cc8) that stand out from the gray spectrum
- Shopify Pay, Klarna, and Afterpay widget colors may be present in the extraction but were not isolated as brand tokens
- The Baskerville font declaration found in extraction may be used for editorial content or blog posts, but was not confirmed as a system font — it is not included in the typography block pending verification
- Star rating component details (empty state color, half-star rendering) were not extracted
- Loading states, skeleton screens, and animation timing values were not found in the extraction
