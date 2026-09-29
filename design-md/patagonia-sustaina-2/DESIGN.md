---
version: alpha
name: "Patagonia"
source_url: "https://patagonia.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Patagonia's product pages carry more environmental disclosure text than most brands carry marketing copy — the Footprint Chronicles data block, the Fair Trade certification badge, the repair-guide link — and the design system absorbs all of it without visual noise because it runs at #020202 on white, with almost no intermediate color decisions to make. The site is a strict black-and-white-plus-photography system, where the only permitted chromatic intrusion is the brand's well-documented archive yellow (≈ #f9c623), pulled from decades of Synchilla and Baggies colorways and used sparingly as a badge accent or seasonal campaign wash. Avenir Next LT W02 — extracted in Bold, Light, and Medium cuts — does the entire typographic job: display headlines run in Bold at generous sizes, product names in Medium at 16–18px, and secondary metadata in Light at 13px, creating a three-tier weight hierarchy that reads as a magazine layout rather than a product grid.

  Navigation is utilitarian by design: a white bar at standard height, black wordmark left-aligned, product category links in medium weight without any hover animations beyond a simple underline, and a persistent shopping cart count in a small circular badge. No mega-menu gradients, no animated flyouts — category expansions drop as flat white panels with tight typographic lists. The search field is borderless with a bottom underline only, consistent with the brand's hostility toward decorative chrome.

  Product cards follow a 4-up grid on desktop with aspect-ratio-locked landscape photography, a thin-weight product name in {typography.body-md}, price in {typography.body-sm}, and color swatch dots in {rounded.full} at 12px diameter. Out-of-stock swatches carry a single diagonal line rather than a color wash — an information-dense choice that saves space without sacrificing legibility. Badges like "Fair Trade" and "Recycled" sit as flat {rounded.xs} chips in {colors.ink} with {colors.on-primary} text, never rounded pills, consistent with the brand's preference for rectangular discipline. The cart drawer slides from the right as a full-height panel, and the checkout redirect page (the extracted title was "Hang Tight! Routing to checkout…") maintains the same black-on-white system with a centered wordmark and a simple loading state — the one moment where the brand intentionally strips all navigation and product context to focus the transaction.

colors:
  primary: "#020202"
  primary-active: "#333333"
  primary-disabled: "#999999"
  ink: "#020202"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-yellow: "#f9c623"
  accent-yellow-on: "#020202"
  badge-fair-trade: "#020202"
  badge-sale: "#d9251c"
  badge-sale-on: "#ffffff"
  scrim: "rgba(0,0,0,0.5)"

typography:
  display-xl:
    fontFamily: "'Avenir Next LT W02 Bold', 'AvenirNextLTW02-Medium', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Avenir Next LT W02 Bold', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Avenir Next LT W02 Bold', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Avenir Next W02 Light', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir Next W02 Light', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir Next W02 Light', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-sale:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  eyebrow:
    fontFamily: "'AvenirNextLTW02-Medium', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.2px
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
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 23px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottom: "1px solid {colors.ink}"
    borderTop: none
    borderLeft: none
    borderRight: none
    rounded: "{rounded.none}"
    padding: 8px 0
    placeholderColor: "{colors.muted}"
  text-input-focus:
    borderBottom: "2px solid {colors.ink}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 10px 12px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
  nav-dropdown-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/3"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} 0"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price}"
    colorSwatchSize: 12px
    colorSwatchGap: "{spacing.xs}"
  product-card-badge:
    backgroundColor: "{colors.badge-fair-trade}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  product-card-badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-sale-on}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
  color-swatch:
    size: 16px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "1px solid {colors.hairline}"
    outOfStockDiagonal: true
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    overlayScrim: "linear-gradient(to right, rgba(0,0,0,0.55) 40%, transparent 80%)"
    ctaComponent: button-primary
  campaign-eyebrow:
    textColor: "{colors.accent-yellow}"
    typography: "{typography.eyebrow}"
    marginBottom: "{spacing.sm}"
  sustainability-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.accent-yellow-on}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "none"
    borderBottom: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    iconColor: "{colors.ink}"
    height: 44px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    headerTypography: "{typography.title-md}"
    itemTitleTypography: "{typography.body-sm}"
    itemPriceTypography: "{typography.price}"
    checkoutButton: button-primary
  cart-count-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    size: 18px
  footprint-chronicle-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    borderLeft: "4px solid {colors.ink}"
  product-grid:
    columns-desktop: 4
    columns-tablet: 3
    columns-mobile: 2
    gap: "{spacing.lg}"
    padding: "0 {spacing.xl}"
  size-selector-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 40px
    width: 48px
  size-selector-button-selected:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
  size-selector-button-unavailable:
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
    diagonal: true
  accordion-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption-bold}"
    columns: 4
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "none"

## Components

### Buttons
**`button-primary`** — Flat black (`{colors.primary}`) rectangle with no border radius whatsoever — `{rounded.none}` is enforced globally on interactive elements. Text renders in uppercase Medium weight at 15px with 0.5px letter-spacing, giving CTAs the feel of a trail marker rather than a consumer-web affordance. Active state darkens to `{colors.primary-active}` (#333333); disabled drops to `{colors.primary-disabled}` without opacity tricks.

**`button-secondary`** — White fill with a 1px black border, same rectangular geometry. Used for secondary actions like "Add to Wishlist" or "Find in Store." Hover fills to `{colors.surface-soft}` without border change.

**`button-text-link`** — Transparent background, underline decoration, inherits surrounding `{typography.body-sm}`. Used inline in product descriptions for repair guides, environmental disclosures, and Worn Wear links.

### Inputs
**`text-input`** — Bottom-border only, no visible container box. The borderless aesthetic extends into form fields: only a 1px hairline below the field signals interactivity. On focus the border weights to 2px black. Placeholder text renders in `{colors.muted}`. Used for search, email signup, and checkout fields.

**`select-input`** — The one exception to the borderless rule: dropdowns carry a full `{colors.hairline}` border to signal the presence of options. No rounded corners.

### Navigation
**`nav-bar`** — 60px white bar, wordmark left at 28px height, utility icons (search, account, cart) right-aligned, primary category links centered or slightly left-of-center depending on viewport. No box-shadow; a single `{colors.hairline}` bottom border provides separation. Cart count renders in `cart-count-badge`, a black pill.

**`nav-dropdown-panel`** — White full-width panel dropping below the nav with generous `{spacing.xl}` padding. Content is pure typographic lists in `{typography.body-sm}` — no images, no promotional tiles, no mega-menu photography. Category headings in `{typography.caption-bold}` uppercase eyebrow style.

### Product Cards
**`product-card`** — No card container or shadow; products float on the page grid with no enclosing box. Image is 4:3 landscape, no rounded corners. Below the image: product name in `{typography.body-md}` Light weight, price in `{typography.price}` Medium weight, color swatches as 12px `{rounded.full}` dots. Fair Trade and Recycled certifications appear as flat `{rounded.xs}` dark chips via `product-card-badge`.

**`color-swatch`** — 16px circle with a 1px `{colors.hairline}` ring by default. Selected swatch gets a 2px `{colors.ink}` ring with a 2px white gap between swatch and ring. Out-of-stock swatches render their color at reduced opacity with a 1px diagonal slash — no additional label needed.

### Hero
**`hero-banner`** — Full-bleed photography with a left-side scrim fading from 55% black opacity to transparent at 80% of the panel width. Headline in `{typography.display-xl}` white, preceded by a `campaign-eyebrow` in `{colors.accent-yellow}` at 11px uppercase tracked. Minimum 560px height; aspect ratio unlocked on mobile. The CTA button uses `button-primary` in its white variant on dark contexts (backgroundColor flips to white, textColor to ink) — Patagonia frequently inverts the button on hero panels rather than introducing a new component.

### Sustainability Components
**`footprint-chronicle-block`** — The brand-signature disclosure module: a `{colors.surface-soft}` block with a 4px left rule in `{colors.ink}`, carrying supply-chain data, environmental impact metrics, and recycled-materials percentages. Title in `{typography.title-sm}`, body in `{typography.body-sm}`. Appears below product description on most apparel PDPs.

**`sustainability-badge`** — Flat `{colors.accent-yellow}` chip in `{rounded.xs}` with `{typography.badge}` uppercase text in `{colors.accent-yellow-on}` (black). Variants include "Fair Trade Certified," "Recycled," "Bluesign Approved," and "RDS Certified Down."

### Size Selector
**`size-selector-button`** — 48×40px flat rectangle, `{colors.hairline}` border, no radius. Selected state inverts to black fill and white text. Unavailable sizes render muted with a CSS diagonal line overlay — no red or crossed-circle icon.

### Footer
**`footer`** — Black background (`{colors.ink}`), four-column link grid in `{typography.body-sm}` white. Column headings in `{typography.caption-bold}` uppercase. Social links as plain text rather than icon buttons. Environmental mission statement appears in a full-width strip above the four-column grid in Light weight, larger body text.

### Accordion
**`accordion-item`** — Bottom-border-only dividers in `{colors.hairline}`, no background tint on expanded state. Used for product features, care instructions, materials, and shipping details. Expand/collapse via a simple plus/minus toggle right-aligned.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid becomes 2-up. Nav collapses to hamburger menu with full-height slide-in drawer. Hero headline drops to `{typography.display-md}`. Cart drawer width stretches to 100vw. Footprint Chronicle block padding reduces to `{spacing.base}`. |
| Tablet | 744–1128px | Product grid renders 3-up. Nav retains full category links at slightly smaller font. Hero minimum height reduces to 420px. |
| Desktop | 1128–1440px | Full 4-up product grid. Nav at full height with dropdown panels. All spacing tokens at their defined values. |
| Wide | > 1440px | Content column max-width locked at ~1440px, canvas bleeds white on sides. Product grid stays 4-up; hero image scales to fill but text block does not grow beyond desktop values. |

### Touch Targets
- All buttons enforce a minimum 48px height on mobile
- Color swatch tap targets padded to 32×32px touch area around the 16px visual dot
- Size selector buttons expand to full minimum-tap height; 48×48px minimum on mobile
- Nav icons in collapsed mobile bar hit 44×44px minimum

### Collapsing Strategy
- Category navigation collapses to hamburger at < 744px; opens as a full-height left-side drawer pushing content
- Product filters shift from left-rail sidebar to a bottom sheet modal on mobile, triggered by a "Filter & Sort" sticky button
- Footprint Chronicle block remains visible on mobile but compresses vertically
- Accordion pattern takes over all product detail tabs below 744px; tabs are not used on mobile
- Footer four-column grid collapses to single-column accordion on mobile with `{colors.hairline}` dividers

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#020202) was extracted from the live site; the site almost certainly loads its color tokens via JS or a CDN-hosted CSS bundle not captured by static extraction. All colors beyond #020202 are derived from widely-documented Patagonia brand history and visual inspection — treat as confident approximations, not extracted values.
- Accent yellow (#f9c623) is informed by Patagonia's decades-long product colorway history (Synchilla, Classic Retro-X) and campaign photography, not a direct extraction.
- Exact border-radius values could not be confirmed; the `{rounded.none}` dominance is consistent with the brand's observed rectangular component discipline but not pixel-verified.
- The meta theme-color was absent, suggesting a dynamic or deferred PWA manifest — no reliable brand color locked in the document head.
- Actual checkout and cart page color behavior could not be observed (extraction hit the "routing to checkout" redirect screen only).
- Icon set style (outline vs. filled, stroke weight) could not be determined from the extraction data.
- Exact button height (48px used here) and padding values are brand-reasonable estimates, not extracted measurements.
