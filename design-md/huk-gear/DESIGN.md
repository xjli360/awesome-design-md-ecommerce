---
version: alpha
name: "Huk Gear"
source_url: "https://www.hukgear.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep-water blue #0f4c81 anchors Huk Gear, a performance fishing and hunting apparel brand that borrows the saturated confidence of marine-grade gear and the quiet precision of technical outerwear. The palette is built on a navy core — #0e4174 for hover states, #17314b for dark accents — that reads as both rugged and precise, like the hull of a center-console boat at dawn. A secondary accent of #45bea6 (a mint-teal that echoes clean water) and a safety-orange #ffaa47 for sale badges and urgency signals break the blue monotony, while a full spectrum of grays from #f7f7f7 canvas to #2c2d2e ink provides the neutral backbone. Typography runs a dual system: Manrope for clean, modern display and body text, and Oswald for condensed, uppercase utility labels and price tags — a nod to the bold signage on fishing gear packaging. Buttons are pill-shaped (`{rounded.full}`) and generously padded, with the primary CTA in #0f4c81 and white text, while secondary buttons invert to a white fill with navy border. Product cards use `{rounded.sm}` corners and a crisp white surface (`{colors.surface-card}`) against `{colors.hairline}` borders, with the product image bleeding edge-to-edge. The brand voice is direct and functional — "Built for the hunt" — and the design system mirrors that: no decorative flourishes, no soft shadows, just clear hierarchy, high-contrast text on white, and a color story that smells like saltwater and diesel.

colors:
  primary: "#0f4c81"
  primary-active: "#0e4174"
  primary-disabled: "#868d94"
  ink: "#2c2d2e"
  body: "#606060"
  muted: "#868d94"
  muted-soft: "#a7a5a5"
  hairline: "#dadce0"
  hairline-soft: "#e2e2e2"
  canvas: "#f7f7f7"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#ffaa47"
  accent-sale-active: "#e97f32"
  accent-water: "#45bea6"
  accent-error: "#c62a32"
  accent-link: "#0581ff"
  accent-link-active: "#006fe0"
  accent-star: "#ffaa47"
  badge-new: "#279a4b"
  badge-sale: "#c62a32"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Oswald', 'trade-gothic-next-condensed', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Oswald', 'trade-gothic-next-condensed', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Oswald', 'trade-gothic-next-condensed', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
  link:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Manrope', 'Work Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 0
  button-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-sale-active:
    backgroundColor: "{colors.accent-sale-active}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-icon-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-error}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    color: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  nav-link-inactive:
    color: "{colors.muted}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price}"
    color: "{colors.accent-error}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    height: 400px
  hero-banner-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.3
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 20px
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
  footer-link:
    color: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.accent-water}"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  rating-stars:
    color: "{colors.accent-star}"
    size: 16px
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
  accordion:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border-bottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The workhorse CTA across the site, rendered as a full-pill in Huk's deep navy #0f4c81 with white text. On hover it darkens to #0e4174, and in disabled state it fades to a muted gray #868d94. Used for "Add to Cart," "Shop Now," and primary checkout actions. The generous 14px vertical padding and 32px horizontal padding give it a solid, confident presence.

**`button-secondary`** — An outlined variant with a white fill and a 2px navy border. On hover the fill swaps to navy and text to white, creating a satisfying inversion. Used for "View Details" and secondary actions where the primary button is already present nearby.

**`button-tertiary-text`** — A text-only link styled as a button, with no background or border. Used for "Learn More" links within product descriptions and for cancel actions in forms. The text color is the primary navy, and on hover it darkens to the active state.

**`button-sale`** — A high-visibility orange pill (#ffaa47) with dark ink text, used exclusively for sale promotions and clearance call-to-actions. On hover it shifts to a deeper orange (#e97f32). This button is the brand's urgency signal, standing out against the predominantly blue palette.

**`button-icon-pill`** — A compact 40px circular button used for icon-only actions like search toggles, cart icons, and mobile menu triggers. Uses the primary navy fill with a white icon.

### Cards
**`product-card`** — The core product display unit, a white card with an 8px border radius and a soft hairline border. The product image bleeds to the top corners (matching the card's top radius) while the text section below uses standard padding. The title uses the `title-sm` token in ink, and the price uses the condensed Oswald `price` token for a distinctive retail look. Sale prices render in the error red (#c62a32) with the original price struck through in muted gray.

**`product-card-badge`** — Small uppercase labels pinned to the top-left of product images. A green badge (#279a4b) signals "New" arrivals, while a red badge (#c62a32) marks sale items. Both use the condensed Oswald `badge` typography at 11px with tight tracking.

### Navigation
**`nav-bar`** — A fixed 72px white bar with a soft bottom border. Navigation links are uppercase Manrope at 15px with 0.5px letter spacing. The active link is underlined with a 2px navy bar, while inactive links render in muted gray. The logo sits left-aligned, and utility icons (search, account, cart) sit right-aligned in a flex row.

**`nav-link-active`** — The active state uses the primary navy color with a 2px bottom border, creating a clear indicator of the current section.

**`nav-link-inactive`** — Inactive links render in the muted gray (#868d94) and transition to navy on hover.

### Forms
**`text-input`** — Standard text inputs with a white fill, 8px border radius, and a 1px hairline border. On focus the border thickens to 2px and turns navy. Error states use a 2px red border (#c62a32). The 48px height matches the button height for aligned form rows.

**`select-input`** — Dropdown selectors matching the text input styling, used for size, quantity, and filter selections.

**`search-bar`** — A full-pill search input with a white fill and hairline border. On focus the border becomes a 2px navy ring. Used in the site's header search and on search result pages.

### Filters
**`filter-chip`** — Pill-shaped filter toggles used on collection pages for size, color, and category filtering. The default state is a light gray fill (#f5f5f5) with a hairline border. When active, the chip fills with navy and text turns white. Multiple chips can be active simultaneously.

### Footer
**`footer-section`** — A deep navy (#0f4c81) footer with white text. Links are the standard `link` typography and turn to the water-teal accent (#45bea6) on hover. The footer includes columns for customer service, about, and social links, with a copyright line at the bottom in a lighter weight.

### Accordion
**`accordion`** — Used on product detail pages for description, sizing, and reviews sections. Each accordion header uses the `title-sm` token with a chevron icon that rotates on open. The content area uses `body-sm` in the body gray (#606060). Borders separate each accordion item.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav, hero banner height reduces to 250px, buttons go full-width, filter chips stack vertically |
| Tablet | 744–1128px | Two-column product grid, top nav collapses utility icons into a single "More" dropdown, hero banner at 320px, filter chips wrap in a horizontal scroll |
| Desktop | 1128–1440px | Three-column product grid, full top nav visible, hero banner at 400px, filter chips in a horizontal row with "Clear All" link |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero banner at 450px with parallax effect, expanded footer with newsletter signup |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px touch target (exceeds Apple HIG)
- Filter chips are 40px tall with 16px horizontal padding for comfortable tapping
- Product card tap targets (image, title, price) are the full card width
- Accordion headers are 48px tall for easy finger interaction
- Quantity selector +/- buttons are 40px squares

### Collapsing Strategy
- Top navigation links collapse into a hamburger menu below 744px
- Secondary navigation (categories) collapses into a select dropdown on mobile
- Product filters collapse into a slide-out drawer on mobile and tablet
- Footer columns stack vertically on mobile, with accordion-style expansion for each column
- Hero banner text overlay reduces font size and padding on mobile
- Product image galleries switch from thumbnail grid to single-image swipe on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list is heavily weighted toward blues and grays, with a few distinctive accents (#45bea6 mint-teal, #ffaa47 orange, #c62a32 red). The brand's true primary (#0f4c81) was identified as the most frequent and distinctive blue, but the live site may use additional accent colors not captured in the extraction (e.g., a specific green for camo patterns, or a tan for hunting lines).
- Font-family declarations included "Styrene A Web" and "Gill Sans" which may be used for specific sub-brands or legacy pages, but Manrope and Oswald were the most frequently observed and are treated as the primary system.
- Hover states for all components are inferred from common patterns (darkening primary, inverting secondary) and may differ from the actual implementation.
- Error styling for form validation (error messages, iconography) was not extracted and uses standard red (#c62a32) as a best-guess accent.
- Dark mode is not observed on the live site and is not supported in this system.
- The brand may use specific pattern fills or textures (camo, fish scales) in backgrounds or hero sections that are not captured in the color palette.
- Sub-brand palettes for "Huk Fishing" vs "Huk Hunting" may exist but were not distinguishable from the extraction.
- The extracted colors include potential Shopify checkout widget colors (#1829e6, #3f72e5) that should be verified against the actual brand palette.
