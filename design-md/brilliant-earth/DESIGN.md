---
version: alpha
name: "Brilliant Earth"
source_url: "https://brilliantearth.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The brand color is the argument — sage-toned primary CTAs at approximately `#4a7560` sit inside a near-white room, making ethical provenance a visual sensation before a word of copy lands. Where most fine jewelry retail chooses black or gold as its signature hue, Brilliant Earth chose the color of a forest canopy, and that single decision inflects every interactive element: navigation hover states, form focus rings, and "add to cart" pulses all carry this particular green. The sole extracted hex, `#313131` charcoal, grounds the type system — dark enough to read as authoritative without the coldness of pure black — and sits against a warm cream canvas (`{colors.surface-soft}`) that suggests parchment rather than clinical white. Product photography works on these warm fields: a solitaire diamond ring against `{colors.surface-soft}` or `{colors.surface-warm}` reads as specimen photography borrowed from natural-history catalogs rather than retail merchandising. Typography splits register: a refined serif governs display headlines and category banners — weight 300–400, generous tracking, unhurried pacing — while a humanist sans-serif handles all functional text: prices, filter labels, checkout fields. This split carries the brand's dual identity as both editorial authority on gemstones and efficient transactional tool for the high-stakes engagement-ring purchase. The ring builder — Brilliant Earth's signature interactive feature — requires dense filter chips, step indicators, and carousels to coexist with the brand's preference for negative space; the resolved system uses `{rounded.xs}` on filter badges and `{rounded.sm}` on cards, reserving `{rounded.full}` for filter pill controls only. Product cards carry a "Beyond Conflict Free" or "Lab Grown" provenance mark at the same hierarchy level as the price, treating sourcing credentials as specification data rather than footnote.

colors:
  primary: "#4a7560"
  primary-active: "#385a49"
  primary-disabled: "#a4c0b3"
  ink: "#313131"
  body: "#484848"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#e2ddd8"
  hairline-soft: "#eeebe7"
  canvas: "#ffffff"
  surface-soft: "#faf9f7"
  surface-warm: "#f5f0ea"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  gold-accent: "#b9a882"
  sage-tint: "#eef4f0"
  footer-text: "#e8e4df"
  link: "#4a7560"
  error: "#b94040"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'Domaine Display', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.04em
  display-lg:
    fontFamily: "'Cormorant Garamond', 'Domaine Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.03em
  display-md:
    fontFamily: "'Cormorant Garamond', 'Domaine Display', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.02em
  display-sm:
    fontFamily: "'Cormorant Garamond', 'Domaine Display', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.01em
  body-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  caption-upper:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  label-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.08em
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em

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
    rounded: "{rounded.xs}"
    padding: "14px 32px"
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "13px 31px"
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "10px 14px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption-upper}"
    headingColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    imageRounded: "{rounded.xs}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    headlineColor: "{colors.ink}"
    subheadColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xl}"
    ctaGap: "{spacing.md}"
  category-banner:
    backgroundColor: "{colors.surface-warm}"
    labelTypography: "{typography.caption-upper}"
    titleTypography: "{typography.display-md}"
    labelColor: "{colors.primary}"
    titleColor: "{colors.ink}"
    padding: "{spacing.xxl} {spacing.xl}"
  stone-badge:
    backgroundColor: "{colors.sage-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary-disabled}"
    padding: "3px 8px"
  ethical-source-mark:
    backgroundColor: "{colors.sage-tint}"
    textColor: "{colors.primary-active}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    iconColor: "{colors.primary}"
    padding: "{spacing.xs} {spacing.sm}"
  certification-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary-disabled}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    iconColor: "{colors.gold-accent}"
    padding: "{spacing.xs} {spacing.sm}"
  ring-builder-step:
    backgroundColor: "{colors.canvas}"
    stepIndicatorActive: "{colors.primary}"
    stepIndicatorInactive: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} {spacing.xl}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    height: 34px
  filter-pill-active:
    backgroundColor: "{colors.sage-tint}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    height: 34px
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-tag-note:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  swatch-selector:
    size: 24px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  education-strip:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    iconColor: "{colors.gold-accent}"
    padding: "{spacing.lg} {spacing.section}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline-soft}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.footer-text}"
    linkColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption-upper}"
    headingColor: "{colors.muted-soft}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — Sage green `{colors.primary}` fill with white letterforms in all-caps `{typography.button-md}` at 0.1em letter-spacing — the tracking doing luxury-register work without a serif. Border radius is a deliberate `{rounded.xs}` (4px): precise but not blunt, avoiding both pill-softness and the cold right-angle of legacy jewelers. Hover drops to `{colors.primary-active}`, a deeper forest green; disabled state uses `{colors.primary-disabled}`, a washed sage that recedes without becoming gray.

**`button-secondary`** — Outlined variant with `{colors.canvas}` background, `{colors.primary}` border and text, matching the primary in height (48px) and typography. Deployed alongside `button-primary` in hero sections and ring-builder flows where two equal-weight choices coexist.

**`button-ghost`** — Text-only with underline decoration, no background or border. Used for "Learn More" and editorial cross-links. `{typography.button-sm}` in `{colors.ink}` — the subdued option that avoids visual competition with product imagery.

### Navigation
**`nav-bar`** — White canvas bar at 68px height with a `{colors.hairline-soft}` bottom border. Logo sits left; primary navigation categories (Engagement Rings, Wedding Bands, Fine Jewelry, Gemstones, Education) center-aligned at `{typography.nav-link}` in tracked lowercase. Right cluster holds search, wishlist, and account/cart icons. Education occupies equal nav-level real estate with shopping categories — an unusual structural choice that signals the brand's dual identity.

**`nav-dropdown`** — Full-width mega-menu panels on `{colors.canvas}` with `{spacing.xl}` internal padding. Links in `{typography.body-sm}` grouped under `{typography.caption-upper}` section headers in `{colors.primary}`. Rightmost column features an editorial image or curated product shot within each category; no promotional banner treatment.

### Product Cards
**`product-card`** — Square-ratio image panel on `{colors.surface-soft}` warm cream with `{rounded.xs}` on the image container. Below: stone type in `{typography.caption}`, product name in `{typography.title-sm}`, price in `{typography.price-display}`. An ethical-source-mark badge optionally overlays at the bottom-left corner of the image. The outer card uses `{rounded.sm}` with no heavy elevation shadow — a quiet separation from the canvas rather than a lifted layer.

### Ring Builder
**`ring-builder-step`** — Stepped horizontal progress bar at page top: active step dot in `{colors.primary}`, inactive in `{colors.hairline}`. Each panel uses `{typography.title-md}` for the step title followed by `filter-pill` / `filter-pill-active` filter chips for options (stone shape, carat weight, metal, setting style). Right half of the viewport shows the live ring preview with a sticky configuration summary — stone, metal, carat, price — pinned to the bottom of the panel using `{typography.caption}` and `{typography.price-display}`.

### Badges and Chips
**`stone-badge`** — Small rectangular label on `{colors.sage-tint}` with `{colors.primary}` text, `{typography.label-sm}` all-caps tracking. Appears on product grid cards to identify stone type (Diamond, Ruby, Sapphire) or quality tier.

**`ethical-source-mark`** — "Beyond Conflict Free" or "Lab Grown" provenance chip with a small icon in `{colors.primary}`. Rendered in `{colors.sage-tint}` background; used on product cards and PDPs to surface sourcing credentials at the same visual weight as the price.

**`certification-chip`** — Certification authority labels (GIA, IGI) with `{colors.gold-accent}` icon accent. White background, sage border, `{typography.caption}` body. Appears in product specification zones and educational pages.

### Filter Interface
**`filter-pill`** — Default: `{colors.canvas}` background, `{colors.hairline}` border, `{colors.body}` text, `{rounded.full}`. Selected / `filter-pill-active`: `{colors.sage-tint}` background, `{colors.primary}` border and text. Used throughout the ring builder and collection filter trays for shape, metal, price, and style parameters.

### Education Strip
**`education-strip`** — A `{colors.surface-warm}` horizontal band beneath product grids. Three to four icon-plus-headline pairs ("Conflict-Free Promise", "Free Shipping", "Lifetime Warranty") in `{typography.body-sm}` with `{colors.gold-accent}` icon tones. The warm field distinguishes this from both the product canvas and the footer, creating a gentle mid-page pause.

### Footer
**`footer`** — Dark `{colors.ink}` background with `{colors.footer-text}` near-white body and link text. Section headings in `{typography.caption-upper}` at `{colors.muted-soft}` for separation. Four-column layout on desktop. The dark register of the footer signals seriousness and closure without importing any of the gold-and-black luxury signifiers common to fine jewelry competitors.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-screen drawer; ring builder reflows to vertical step stack; filter pills scroll horizontally in an overflow tray; hero headline scales to `display-md` |
| Tablet | 744–1128px | Two-column product grid; primary nav links visible, secondary icons only; hero uses text-left / image-right split; ring builder sidebar becomes bottom-anchored drawer |
| Desktop | 1128–1440px | Three-column product grid; full mega-menu `nav-dropdown` panels; ring builder shows side-by-side step panel and live preview; hero full-bleed |
| Wide | > 1440px | Max-width container 1440px centered; four-column product grid; hero imagery bleeds to viewport edge with inner content constrained to grid |

### Touch Targets
- Icon buttons (search, wishlist, account) minimum 44×44px hit area on mobile
- Filter pills minimum 34px height; horizontal tray with `-webkit-overflow-scrolling: touch`
- `swatch-selector` uses 32px touch-target wrapper around the 24px visual swatch
- Ring builder step dots minimum 40px tap area with centered label below

### Collapsing Strategy
- Primary navigation collapses to hamburger at < 744px; mega-menu panels become full-screen left-edge drawer slides
- Ring builder step tabs reflow from horizontal to vertical accordion; preview panel stacks below all controls on mobile
- Education strip collapses from 4-column to 2-column at tablet, single column at mobile with centered text
- Footer columns collapse to labeled `details`/`summary` accordions at < 744px
- Product filter sidebar becomes a modal bottom sheet triggered by a `button-secondary` "Filter & Sort" button; active filter count shown as a badge

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Color palette**: Only `#313131` was extracted from the live site; anti-bot protection returned "Just a moment…" before full page load. Sage green primary `#4a7560` and all warm-cream surface tones are inferred from widely-observed brand visual identity — actual hex values may differ by 5–15%.
- **Typography**: No font families were extractable; the site appears to load fonts via JavaScript or a CDN with bot protection. The display serif stack (Cormorant Garamond / Domaine Display) is inferred from the fine-jewelry editorial register Brilliant Earth is known to occupy — actual font name and foundry may differ.
- **Ring builder interaction states**: Hover, focus, drag, and multi-step selection states within the interactive ring configurator could not be inspected; values are extrapolated from the static brand palette.
- **Animation and motion tokens**: No transition durations, easing curves, or scroll-triggered animation parameters were recoverable.
- **Spacing grid**: Base 4px/8px grid assumption; actual design token values are unconfirmed.
- **Dark mode**: No evidence of a dark-mode variant from available extraction data.
- **Icon set**: Weight, stroke style, and fill conventions for the custom wishlist, ring-builder step, and ethical-source icons could not be inspected.
- **Lab-grown vs. natural diamond visual differentiation**: Whether the site uses distinct color or badge treatment to visually distinguish lab-grown from natural diamond listings could not be confirmed.
