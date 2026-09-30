---
version: alpha
name: "Kendra Scott"
source_url: "https://www.kendrascott.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The Color Bar — Kendra Scott's in-store ritual of choosing stones, metals, and settings — maps directly onto the digital surface system: soft lavender (#eddeff), blush peach (#ffe9cb), mint (#b5e5e1), and dusty mauve (#d9c3d2) cycle through section backgrounds the way gemstones swap between bezels. The canvas runs warm cream (#ede8e3) rather than clinical white, which makes the gem-toned pastels read as curated atmosphere rather than promotional noise. Deep plum (#4d3159) carries primary action weight — CTA buttons, the footer ground, active states — a saturated jewel-dark from which white type emerges with precision. The same plum that anchors the footer reverses the entire color system into a terminal jewel-box, lavender links glowing against the field.

  Typography runs two distinct voices. Cormorant, a high-contrast old-style serif, takes all display and editorial moments — collection names, hero headlines, campaign copy — at loose tracking and restrained weight, so the letter shapes function like engraved text on precious metal. Brandon Grotesque handles navigation, body, pricing, and buttons in tracked uppercase, offering legibility at small sizes without tipping into fashion-magazine obscurity. The proprietary KendraScott font holds the wordmark: a calligraphic signature that reads as personal rather than corporate.

  Promotional voltage arrives in chromatic yellow (#f1e02b) on markdown and sale badges — bright enough to cut through warm cream without deploying red-alarm urgency. Free-shipping and loyalty-tier banners run deep navy (#192f5d), signaling institutional trust rather than emotional pressure. Component corners stay nearly sharp ({rounded.none} on buttons, {rounded.xs} at most on small badges) — the precision of fine metalwork rather than consumer apparel softness. Four tinted surface zones — peach (#fce5d4), warm cream (#ffe9cb), lavender (#eddeff), mint (#b5e5e1) — tile the homepage in interchangeable panels that mirror the gem-swatch logic of the physical Color Bar experience.

colors:
  primary: "#4d3159"
  primary-active: "#3a2445"
  primary-disabled: "#d9c3d2"
  navy: "#192f5d"
  navy-mid: "#2a557d"
  navy-steel: "#437191"
  ink: "#1a1918"
  body: "#3d3b3a"
  muted: "#5c5c5c"
  hairline: "#d1d1d1"
  hairline-soft: "#eeeeee"
  canvas: "#ede8e3"
  surface-soft: "#fcf6de"
  surface-card: "#ffffff"
  surface-peach: "#fce5d4"
  surface-warm: "#ffe9cb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-lavender: "#eddeff"
  accent-amber: "#f9e7a7"
  accent-mint: "#b5e5e1"
  accent-mauve: "#d9c3d2"
  badge-promo: "#f1e02b"
  badge-promo-text: "#1a1918"
  sale-orange: "#e7772f"
  footer-bg: "#4d3159"
  error: "#963636"

typography:
  display-xl:
    fontFamily: "'Cormorant', 'big-caslon-fb', Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant', 'big-caslon-fb', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant', 'big-caslon-fb', Georgia, serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  logo-display:
    fontFamily: "'KendraScott', 'Cormorant', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  title-lg:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  title-md:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.4px
  title-sm:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.5px
  body-md:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-lg:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'brandon-grotesque', Inter, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
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
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 0
    borderBottom: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.logo-display}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-promo-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    priceSaleColor: "{colors.sale-orange}"
    priceOriginalColor: "{colors.muted}"
    rounded: "{rounded.none}"
    padding: "{spacing.md}"
  product-card-badge:
    backgroundColor: "{colors.badge-promo}"
    textColor: "{colors.badge-promo-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    overlayMode: split-image-text
  color-bar-swatch:
    size: 32px
    borderRadius: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderDefault: "2px solid transparent"
    shadowSelected: "0 0 0 2px {colors.canvas}"
  collection-tile:
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    overlayGradient: "linear-gradient(to top, rgba(26,25,24,0.55), transparent)"
  promo-badge:
    backgroundColor: "{colors.badge-promo}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.sale-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  category-pill:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  loyalty-badge:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  personalization-panel:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  personalization-upsell:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  gem-surface-peach:
    backgroundColor: "{colors.surface-peach}"
  gem-surface-lavender:
    backgroundColor: "{colors.accent-lavender}"
  gem-surface-mint:
    backgroundColor: "{colors.accent-mint}"
  gem-surface-warm:
    backgroundColor: "{colors.surface-warm}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-lavender}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.title-md}"
    itemTypography: "{typography.body-sm}"
    totalLabelTypography: "{typography.title-lg}"
    totalPriceTypography: "{typography.price-lg}"
    borderLeft: "1px solid {colors.hairline}"

## Components

### Buttons

**`button-primary`** — Deep plum (#4d3159) fill with white Brandon Grotesque uppercase tracked at 1.5px on sharp-cornered ({rounded.none}) 48px-tall blocks. Hover darkens to `primary-active` (#3a2445); disabled collapses fill to soft mauve (#d9c3d2). The zero-radius corner signals metalwork precision rather than consumer softness.

**`button-secondary`** — Transparent fill framed by a single 1px plum border, converting to full plum fill on hover with text inverting to white. Same 48px height and uppercase tracking as the primary, making the two variants read as matched siblings across a single action hierarchy.

**`button-ghost`** — No fill, no side border; a 1px bottom line under ink-colored text only. Appears on "Shop Now" inline links and "View All" section footers, where weight would compete with adjacent content.

### Text Inputs

**`text-input`** — Warm cream canvas (#ede8e3) fill with a 1px hairline border that upgrades to plum on focus. Sharp corners match the button register throughout. Placeholder runs muted gray (#5c5c5c). Used across search typeaheads, email capture bars, and all engraving and personalization fields on product pages.

### Navigation

**`nav-bar`** — Warm cream canvas at 64px, the KendraScott calligraphic wordmark center-anchored or left-aligned per context, with Brandon Grotesque uppercase navigation links at 13px and 1px letter-spacing. A soft hairline separates it from content. A 40px navy (`#192f5d`) promo strip stacks above on load or scroll-up, carrying free-shipping thresholds or sitewide offers in white caption type.

### Product Cards

**`product-card`** — White surface card with a soft yellow (#fcf6de) image zone. Product name in Brandon Grotesque semi-bold 14px; price in regular 14px beneath. Sale price renders in orange (#e7772f) with the crossed-out original in muted gray. A badge pins to the image corner: chrome-yellow (#f1e02b) pill for discovery signals ("NEW," "BEST SELLER") or a flat orange rectangle for percentage-off callouts.

### Hero Banner

**`hero-banner`** — Split layout at desktop: full-bleed photography left, editorial text right on warm cream. Cormorant Display 52px light-weight headline followed by Brandon Grotesque body copy and a full `button-primary` CTA. Collapses to stacked (image above, text block below) at mobile widths.

### Color Bar Swatches

**`color-bar-swatch`** — 32px circles representing gemstone choices on product pages and the homepage Color Bar feature. The selected swatch carries a 2px plum ring inset by a matching 2px canvas halo ({rounded.full}, `shadowSelected`), making the selection state readable against any of the four gem-toned page backgrounds.

### Collection Tiles

**`collection-tile`** — Full-bleed imagery with a bottom-anchored linear gradient darkening to ~55% opacity, overlaid with Cormorant 30px headline in white. Used on the homepage to partition product worlds — Earrings, Necklaces, Sets — carrying the gem-tile visual logic into section-level navigation.

### Badges

**`promo-badge`** — Pill-shaped ({rounded.full}) chrome-yellow (#f1e02b) fill with near-black uppercase 11px text. Signals discovery, novelty, and best-seller status. **`sale-badge`** is a sharp-cornered orange (#e7772f) rectangle at the same type scale with white text. The pill/rectangle distinction cleanly separates editorial discovery cues from price-reduction urgency.

### Personalization Panel

**`personalization-panel`** — Soft yellow cream (#fcf6de) surface at 32px padding ({spacing.xl}), hosting Color Bar swatches, metal-type toggles, and engraving text inputs. Title in Brandon Grotesque semi-bold 16px over body-sm descriptive copy. A hairline border defines it from the product page without adding chromatic noise.

**`personalization-upsell`** — A narrower amber-tinted (#f9e7a7) strip inside or below the panel, calling out "Add Personalization" or complementary add-ons in body-sm at {spacing.base} padding.

### Footer

**`footer`** — Full-bleed deep plum (#4d3159) ground reversing the entire color system. Navigation links glow lavender (#eddeff) against the dark field; column headings run white Brandon Grotesque semi-bold 14px uppercase. Four-column grid on desktop collapses to a single-column accordion on mobile, with brand social icons and a newsletter input rendered in the same warm-reversed style.

### Cart Drawer

**`cart-drawer`** — Slides in from the right over warm cream canvas, separated from the page by a single left hairline. Line items in body-sm; total label in title-lg (Brandon Grotesque 20px semi-bold); total price in price-lg (18px semi-bold). Full-width `button-primary` at drawer footer drives to checkout.

### Gem Surface Tiles

`gem-surface-peach`, `gem-surface-lavender`, `gem-surface-mint`, `gem-surface-warm` — Four interchangeable section-background tints mirroring the Color Bar's stone hues. Used by the homepage layout engine to separate editorial regions without borders or drop shadows, creating the colorblock rhythm the brand deploys across seasonal campaigns.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hero stacks (image over text), 2-up product grid, nav collapses to hamburger with wordmark centered, Color Bar swatches scroll horizontally, footer becomes single-column accordion |
| Tablet | 744–1128px | 3-up product grid, hero retains split at reduced text-column width, promo banner collapses to single scrolling line |
| Desktop | 1128–1440px | 4-up product grid, hero at 50/50 split, full horizontal nav with category flyouts visible |
| Wide | > 1440px | Container max-width ~1440px centered, hero widens photography proportion, accessories grid expands to 5-up |

### Touch Targets

- All primary and secondary buttons minimum 48px height
- Color Bar swatches minimum 44px tap zone (32px visual with surrounding padding)
- Cart and wishlist icon triggers minimum 44×44px
- Hamburger menu rows minimum 48px height
- Swatch radio inputs minimum 44×44px hit zone on mobile

### Collapsing Strategy

- Navigation: hamburger below 744px; full horizontal link row with flyout categories at ≥ 744px
- Product grid: 1-up below 480px, 2-up 480–744px, 3-up 744–1128px, 4-up at ≥ 1128px
- Personalization panel: full-width bottom sheet on mobile, inline sidebar column on desktop
- Footer: accordion single-column on mobile, 4-column grid on desktop
- Hero: stacked full-bleed image + text block on mobile, side-by-side editorial split at ≥ 744px
- Gem surface tiles: full-width stacked panels on mobile, multi-column grid on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- KendraScott custom font weight range and variable-font axes not confirmed; stroke contrast and stylistic alternates unknown
- Exact button border-radius uncertain — site may apply 2–4px rather than fully sharp; {rounded.none} is a best estimate pending visual audit
- Hover/focus transition timing and easing curves not extracted
- No dark-mode evidence found; dark-mode token set entirely absent
- Animated Color Bar gem-select behaviors (shimmer, confetti, stone rotation) not documented
- Nav height on scroll-shrink state not confirmed (64px may reduce on scroll)
- Whether `brandon-grotesque` loads via Adobe Fonts subscription or self-hosted WOFF2
- Product image aspect ratio (square 1:1 vs portrait 3:4) not confirmed from extraction
- Exact flyout/mega-menu layout and animation for desktop nav categories not captured
- Payment badge colors (#016fd0, #f79e1b, #bd3d44) excluded as third-party assets; not brand tokens
