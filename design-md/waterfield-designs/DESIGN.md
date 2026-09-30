---
version: alpha
name: "WaterField Designs"
source_url: "https://www.sfbags.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Near-black (#111111) serves as both the navigation canvas and the meta theme-color — a declaration that this shop photographs dark waxed canvas and bridle leather and refuses to soften that with a white header. The telling detail is sage green (#aaccaa): it surfaces in hover states, category chips, and selection indicators, a color sitting equidistant between military green and aged patina, indexing to WaterField's actual material vocabulary rather than a Pantone trend sheet. The primary CTA runs in deep teal (#108474), saturated and purposeful without aggression, while sharp gold (#f5cc15) punctuates badge callouts and promotional announcements. Between sage, teal, and gold, the brand has assembled a three-note palette specific enough to function as a signature. A desaturated mint (#c5f7f0, #edf5f5) provides the teal family's surface-weight version for feature bands, and a soft lavender (#a89cc8) marks a lighter product line — likely gift-oriented — with its own distinct register.

  Type opens with Nunito Sans at display and navigation scales: a rounded humanist sans that gives the dark-canvas layout friendliness without loosening its precision. Lato carries body copy, labels, and interface text with high x-height legibility and neutral authority. Baskerville punctuates editorial moments — material callouts, provenance lines, the kind of sentence that ends "hand-cut in San Francisco" — a serif flag that the brand takes craft heritage seriously. Corner geometry is restrained: cards round to `{rounded.xs}`, preserving the sharp-folded aesthetic of the products themselves, while primary buttons step to `{rounded.sm}` to read as interactive rather than structural. There are no full pill buttons here. Generous section padding and wide photography gutters signal quality through absence rather than ornament — the layout's job is to step aside. The combined result is a Shopify storefront that reads less like a theme and more like an in-house build.

colors:
  primary: "#108474"
  primary-active: "#0b6b5f"
  primary-disabled: "#c1e6e6"
  ink: "#111111"
  body: "#3a3a3a"
  muted: "#7b7b7b"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  nav-canvas: "#111111"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  surface-teal: "#edf5f5"
  surface-mint: "#c5f7f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sage: "#aaccaa"
  sage-deep: "#707977"
  accent-gold: "#f5cc15"
  lavender: "#a89cc8"
  teal-light: "#c1e6e6"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  editorial:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.1px
  price:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Lato', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.nav-canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "none"
  nav-link-hover:
    textColor: "{colors.sage}"
    borderBottom: "2px solid {colors.sage}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageRounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
    borderColor: "{colors.hairline}"
  hero-banner:
    backgroundColor: "{colors.nav-canvas}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
    ctaButton: "button-primary"
  hero-banner-light:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  category-chip-active:
    backgroundColor: "{colors.sage}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.sage}"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
    padding: 6px 14px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-limited:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  promo-band:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: 10px {spacing.base}
    textAlign: center
  feature-callout:
    backgroundColor: "{colors.surface-mint}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.teal-light}"
  material-tag:
    backgroundColor: "transparent"
    textColor: "{colors.sage-deep}"
    typography: "{typography.caption}"
    border: "1px solid {colors.sage}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: 8px 14px
  review-strip:
    backgroundColor: "{colors.surface-soft}"
    starColor: "{colors.accent-gold}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    ratingTypography: "{typography.title-md}"
    padding: "{spacing.lg} {spacing.xl}"
  customization-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    optionTypography: "{typography.body-sm}"
  editorial-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.editorial}"
    accentColor: "{colors.sage-deep}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.sage}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Deep teal (#108474) fill, white text, 48px tall, uppercase Nunito Sans 700 with 0.5px letter-spacing. Serves every add-to-cart, checkout, and primary CTA. Active state darkens to #0b6b5f; disabled collapses to the light teal surface (#c1e6e6) with muted text, keeping the teal family coherent even in unavailable states.

**`button-secondary`** — White canvas with a 1px teal border and teal text; matches primary in height and typography so the two can pair side-by-side without visual hierarchy confusion. Used for "View Details," filter application, and secondary modal actions.

**`button-ghost-dark`** — Transparent background with white border and white text, deployed exclusively on dark (#111111) hero and banner sections where a fill button would create an awkward color island. Maintains the uppercase Nunito Sans voice of all WaterField button variants.

### Navigation
**`nav-bar`** — 64px bar in near-black (#111111), with all links in white Nunito Sans 600 at 14px. Hover shifts any link to sage green (#aaccaa) with a 2px sage underline — the most direct expression of the brand's palette in the interface. The dark nav creates a visual bookend with the dark footer, framing the white product canvas as the content zone.

### Cards & Product Listings
**`product-card`** — White card, 4px radius (`{rounded.xs}`), 1px light hairline border, generous internal padding. Product title in `title-md` (Nunito Sans 600/18px); price in the dedicated `price` scale (Nunito Sans 700/18px). On hover, a soft drop shadow lifts the card without any color change — the brand's restrained interaction vocabulary. No image overlays or quick-add buttons in the default state; the product photography is given uninterrupted space.

**`category-chip`** — Soft gray surface pills used as filter toggles and collection markers. Active state fills with sage green (#aaccaa) and swaps the border to match — the same sage that appears in nav hovers, creating consistent brand-color recognition across filtering and navigation contexts.

### Hero
**`hero-banner`** — Full-bleed dark (#111111) section with white `display-xl` heading and a `button-primary` CTA. Used for the homepage above-fold and major product launches. `hero-banner-light` swaps in the soft teal surface (#edf5f5) for secondary campaign panels — the teal family present at surface weight, lighter in tone, used for seasonal promotions or secondary category features.

### Badges & Promotional Signals
**`badge-new`** — Teal (#108474) fill, consistent with the primary action color, signaling availability and recency without secondary color vocabulary. **`badge-sale`** — Sharp gold (#f5cc15) fill with dark text; reads as a premium callout rather than a markdown flag, consistent with WaterField's positioning. **`badge-limited`** — Near-black fill for scarcity messaging; uses restraint rather than red urgency, which would undercut the craft-brand register.

**`promo-band`** — Full-width gold (#f5cc15) strip for shipping thresholds and time-limited announcements. The gold grounds urgency without alarm-red, reinforcing the idea that WaterField promotions are events rather than discounts.

### Material & Craft Detail Components
**`feature-callout`** — Mint surface (#c5f7f0) panel with a teal hairline border, used on product detail pages to highlight material certifications, construction notes, and warranty terms. The mint reads as the teal brand color dialed to background weight, keeping the brand palette present throughout the purchase flow.

**`material-tag`** — Inline label with sage-deep text (#707977) and a sage border (#aaccaa), applied to material and color variant selectors (e.g. "Waxed Canvas," "Full-Grain Leather," "Kodra Nylon"). Keeps variant selection visually tied to the craft material vocabulary rather than defaulting to generic swatch circles.

**`customization-panel`** — White panel within product pages for selecting dimensions, color options, or hardware finish. Section title in `title-md`, option labels in `body-sm`. A 1px hairline border separates the panel from the photography zone; accordion-collapses to sub-sections on mobile.

**`editorial-strip`** — Soft gray (#f9f9f9) horizontal band using Baskerville in the `editorial` scale for provenance copy, material sourcing paragraphs, and brand heritage statements. Sage-deep (#707977) is used for pull-quote accents. This component gives the brand its craft-heritage voice in a typographic register that body copy cannot achieve.

### Review & Social Proof
**`review-strip`** — Light gray (#f9f9f9) background panel aggregating star ratings (gold, #f5cc15) and review count via the Judgeme widget. Typography stays at `body-sm` — informational rather than persuasive — positioned below the add-to-cart zone on product pages.

### Search & Footer
**`search-bar`** — 40px, surface-soft fill, hairline border, `{rounded.sm}` to distinguish it from the flat card grid. Focus state swaps border to teal (#108474), connecting the focused input to the primary brand color.

**`footer`** — Near-black (#111111) matching the nav bar, with sage green (#aaccaa) link colors. The dark-on-dark bookend frames the entire product canvas. Column headings in `title-sm` Nunito Sans; link lists in `body-sm` Lato. The sage links are the footer's only color break, carrying the brand palette to the lowest point on every page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-width sage-highlighted links; hero type scales to `display-md`; promo-band wraps to two lines; product-card padding reduces to `{spacing.sm}`; customization-panel collapses to accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category links, secondary dropdowns under overflow; hero allows split text + image layout |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with all category dropdowns; hero at full `display-xl`; editorial-strip shows two-column prose layout |
| Wide | > 1440px | Grid and content max-width caps at ~1440px with auto side margins; hero photography bleeds edge-to-edge while text container remains constrained |

### Touch Targets
- All buttons minimum 48px tall (matches `button-primary` and `button-secondary` defined heights)
- Category chips expand to minimum 36px touch height on mobile via additional vertical padding
- Nav links in hamburger menu expand to full-width tap targets with 52px row height
- Product cards are fully tappable — no nested interactive elements in the default card face
- Material-tag variant selectors pad to 36px touch height on mobile

### Collapsing Strategy
- Navigation: hamburger menu below 744px; all primary categories become full-width accordion list items with sage active indicator
- Product filters: left-rail panel on desktop; slide-up sheet on mobile, triggered by a "Filter" button row
- Feature callout panels: stack vertically on mobile; side-by-side image + text on desktop
- Customization panel: collapses to labeled accordion sections on mobile to preserve vertical space for product photography
- Footer columns: collapse to accordion sections below 744px; headings become tappable expand/collapse triggers

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom or licensed brand font — Nunito Sans and Lato inferred from CSS font-stack extraction; WaterField may use a self-hosted variant with different weight ranges not visible in sampling
- Baskerville usage scope uncertain — present in the font stack but could function as a serif fallback rather than an intentional editorial face; confirm in actual editorial section markup
- Lavender (#a89cc8) context unconfirmed — could mark a specific product line (e.g. gaming or lifestyle accessories), a promotional UI element, or an isolated collection accent
- Exact nav dropdown structure not confirmed — number of mega-menu columns, hover vs. click activation, and active category indicator depth require live inspection
- Mobile CSS breakpoint values estimated from category conventions; no confirmed breakpoint pixel values extracted from source
- Animation and easing values not extractable — hover transitions, drawer open/close, and page transition timing are unspecified
- Dark-mode behavior ambiguous — meta theme-color #111111 may indicate a dark-nav-only pattern or a full dark-mode toggle; requires JS state inspection
- Box-shadow depth values for `product-card-hover` are approximated; exact shadow spread and opacity not confirmed from extraction
- Gold accent split (#f5cc15 vs #fbcd0a) — both values appear in extraction; which maps to sale badges versus promo-band versus star ratings is unconfirmed
