---
version: alpha
name: "Perfora"
source_url: "https://perfora.co.in"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Perfora's electric blue — an approximate #0055FF saturated enough to read as a charging indicator on a phone rather than a mouthwash label — is the single design decision that separates the brand from every legacy oral care SKU on the Indian market. Where competitors default to clinical teal, pharmaceutical aqua, or the kind of white that implies sterilisation, Perfora's primary sits closer to digital product language: the blue of a premium wearable, a fintech app, a gaming peripheral. The brand's canvas is pure white, and the electric blue carries almost the entire tonal weight of the UI — product cards, CTA buttons, nav accents, and pricing callouts all draw from this one voltage rather than splitting attention across a broader palette. Product photography does the rest: clean backgrounds, close-cropped shots of brush handles and whitening strip packaging, occasionally a model against a lifestyle setting. Typography runs in a geometric sans-serif — most likely Gilroy or a near equivalent — at weights 500–700 for headlines and 400 for body copy. Display sizes are confident without being theatrical: a 40–48px headline at weight 700 feels like product design copy rather than fashion editorial. Corner radii are moderate; pill shapes appear on filter chips and trust badges while product cards and inputs use a softer 8–12px radius, keeping the UI approachable without dissolving into the rounded-everything aesthetic common to wellness peers. The overall effect is a brand that has decided clinical credibility and consumer-electronics excitement are not opposites: every session at perfora.co.in reads like unboxing a gadget, not refilling a prescription.

colors:
  primary: "#0055FF"
  primary-active: "#003DCC"
  primary-disabled: "#99BBFF"
  primary-light: "#E8EEFF"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#E5E5E5"
  hairline-soft: "#F0F0F0"
  canvas: "#FFFFFF"
  surface-soft: "#F7F8FF"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  success: "#00B37E"
  warning: "#F5A623"
  error: "#E02020"
  star: "#F5A623"
  badge-sale: "#FF3B30"
  badge-sale-text: "#FFFFFF"
  badge-new: "#0055FF"
  badge-new-text: "#FFFFFF"
  badge-bestseller-bg: "#F5A623"
  badge-bestseller-text: "#FFFFFF"

typography:
  display-xl:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-upper:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.2px
  button-md:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gilroy', 'Neue Haas Grotesk', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    padding: 14px 28px
    height: 48px
    states:
      hover: "backgroundColor: {colors.primary-active}"
      disabled: "backgroundColor: {colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
    states:
      hover: "backgroundColor: {colors.primary-light}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    linkTypography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoHeight: 32px
    cartIconAccent: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    imageBg: "{colors.surface-soft}"
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    shadow: "0 2px 12px rgba(0,0,0,0.06)"
    badgePosition: top-left
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    layout: split-50-50
    imagePosition: right
    padding: "{spacing.xxl} 0"
    ctaButtonStyle: button-primary
  category-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 8px 18px
    states:
      active: "backgroundColor: {colors.primary}; textColor: {colors.on-primary}; border: 1px solid {colors.primary}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.badge-sale-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-bestseller:
    backgroundColor: "{colors.badge-bestseller-bg}"
    textColor: "{colors.badge-bestseller-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  trust-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    layout: horizontal-scroll
    height: 40px
    iconSize: 16px
    items:
      - "Free Delivery Above ₹499"
      - "COD Available"
      - "30-Day Returns"
      - "Clinically Tested"
  review-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    ratingColor: "{colors.star}"
    reviewTypography: "{typography.body-sm}"
    authorTypography: "{typography.caption}"
    border: none
  subscription-banner:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg} {spacing.xl}"
    ctaBorder: "1.5px solid {colors.primary}"
  product-image-gallery:
    backgroundColor: "{colors.surface-soft}"
    thumbnailBorder: "2px solid {colors.primary}"
    thumbnailRounded: "{rounded.sm}"
    thumbnailSize: 72px
    mainImageRounded: "{rounded.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"


## Components

### Buttons

**`button-primary`** — Solid electric blue (`{colors.primary}`) fill with white text, 48px tall, 8px radius. The primary CTA appears on add-to-cart, checkout confirm, and all top-level conversion actions; on hover it steps to `primary-active` (#003DCC) without changing shape. The disabled state desaturates to `primary-disabled` (#99BBFF), preserving button geometry so the affordance reads correctly even when inactive.

**`button-secondary`** — White background with a 1.5px `primary` blue border and matching blue label, same height and radius as primary. Used for secondary product actions — compare, wishlist, view-more — and modal cancel flows. Hover fills with `primary-light` (#E8EEFF) to confirm interactivity without committing to the full primary weight.

**`button-ghost`** — Transparent fill, 1px `hairline` border, ink text. Reserved for lowest-priority utility actions: applying coupon codes, optional newsletter subscribe, navigation sub-actions. Restrained styling keeps these from competing with blue CTAs on the same screen.

**`button-pill-primary`** — Full `{rounded.full}` radius in `primary` blue with `{typography.button-sm}` type and compact padding. Appears on filter strips and mobile quick-add overlays. Shares hover/active colour progression with the primary button; the pill shape visually separates it from rect CTAs so the two can coexist without ambiguity.

**`category-pill`** — Resting state is white with a thin `hairline` border; active state fills `primary` blue with white text. These scroll horizontally on mobile across product listing pages (Brushes, Whitening, Accessories, Travel Kits). The `{rounded.full}` radius gives the filter row a distinct visual register from the 12px-radius product cards directly beneath.

### Navigation

**`nav-bar`** — 64px tall, white background, 1px `hairline` bottom border. Logo sits left at 32px height. Nav links use `{typography.nav-link}` (14px/500) spaced across the centre on desktop; a hamburger icon opens a full-height slide-in drawer on mobile. Cart and search icons sit right with a count bubble in `primary` blue. The bar is sticky on scroll and remains visible throughout long PDP pages.

### Product Display

**`product-card`** — White card with a 1px `hairline-soft` border, `{rounded.md}` (12px) radius, and a subtle 2px/6% opacity shadow. The product image zone uses `surface-soft` (#F7F8FF) — the faint blue tint links photography back to the brand primary without colour-grading the actual images. Title in `{typography.title-sm}` (16px/600), price in `{typography.price-display}` (22px/700), MRP in struck-through `{typography.body-sm}` muted. Badges pin top-left at `{rounded.xs}` radius.

**`product-image-gallery`** — Vertical thumbnail column (72px squares, `{rounded.sm}`) with a 2px `primary` blue border on the active thumb. Main image fills the right at `{rounded.lg}` (20px) against the `surface-soft` background. Tapping the main image cycles through angles inline; no modal lightbox is assumed by default.

**`hero-section`** — 50/50 split layout: copy block left, product image right. Background is `surface-soft` (#F7F8FF), lifting the hero from the body canvas without a hard colour change. The `{typography.display-xl}` headline (48px/700/−0.5px tracking) reads as product-design copy; a short `{typography.body-md}` sentence precedes the primary CTA. The electric blue button is the sole saturated element in the hero, making the conversion action visually unambiguous.

### Trust & Social Proof

**`trust-strip`** — A full-bleed `primary` blue band at 40px height carrying four `{typography.caption-upper}` (11px/700/uppercase) messages in white. On desktop the four items sit spaced in a static row; on mobile the strip scrolls horizontally as a marquee. White on blue delivers maximum contrast; the uppercase tracking (+0.8px) keeps the small text legible against the saturated background.

**`review-card`** — Floated on `surface-soft` at `{rounded.md}` radius, no border, `{spacing.lg}` internal padding. Amber star row (`{colors.star}`, #F5A623) sits above the review body in `{typography.body-sm}`. Reviewer name and verified label render in `{typography.caption}` (12px/500). Cards form a 3-column grid on desktop, collapsing to a horizontal scroll strip on mobile.

**`badge-sale`** / **`badge-new`** / **`badge-bestseller`** — Three variants sharing `{typography.badge}` (11px/700/uppercase) and `{rounded.xs}` (4px) radius. Sale uses red (#FF3B30), New uses brand blue (#0055FF), Bestseller uses amber (#F5A623); white text passes WCAG AA on all three. Badges stack vertically when multiple apply to a single card.

### Promotional & Utility

**`subscription-banner`** — Light `primary-light` (#E8EEFF) background with `primary-active` (#003DCC) heading text and a blue-bordered secondary CTA. Used for subscription upsell in the cart and on PDP pages. The blue tint on the white-canvas page provides clear visual separation without a full-colour interrupt; `{rounded.md}` keeps the container feeling inline rather than intrusive.

**`footer`** — Dark `{colors.ink}` (#111111) background with white link columns in `{typography.body-sm}`, column headings in `{typography.title-sm}`. Section dividers are a slightly lighter #333333. Link hover transitions to `{colors.primary}` blue — the single brand accent that appears inside the dark footer — maintaining brand presence at the page bottom.


## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger plus sticky bottom bar with cart CTA; hero stacks image above copy; trust-strip runs as horizontal marquee; category pills horizontal-scroll strip; primary CTA buttons go full-width in hero and PDP |
| Tablet | 744–1128px | 2-column product grid; nav shows logo, search, and cart only — categories move to a secondary sub-bar below; hero returns to split layout; gallery thumbnails move to a horizontal row below the main image |
| Desktop | 1128–1440px | 3–4 column product grid; full nav with category links visible; hero 50/50 split; review cards in 3-column grid; sticky add-to-cart rail in PDP right column |
| Wide | > 1440px | Content max-width ~1320px centred; horizontal section padding scales to `{spacing.xxl}`; hero headline may step up toward a larger display size |

### Touch Targets

- All buttons maintain a minimum 48px height on mobile
- Category pills override to minimum 44px height on mobile
- Cart, search, and hamburger icons use minimum 44×44px tap areas with invisible padding
- Gallery thumbnails expand to minimum 56px on mobile

### Collapsing Strategy

- Product grid: 4-col → 3-col → 2-col → 1-col
- Review grid: 3-col → 2-col → horizontal scroll on mobile
- Navigation: full category links → icon bar + hamburger → sticky bottom cart bar on mobile
- Hero: side-by-side → stacked image-first on mobile
- Trust strip: static spaced row → horizontal marquee on mobile
- Category pills: wrap on tablet, horizontal scroll with edge fade on mobile


## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: The live site (perfora.co.in) appears to load design tokens via JavaScript or returns restricted responses to automated crawlers. All color values in this file are derived from brand knowledge, not live CSS extraction — treat as approximate until validated in DevTools.
- **Primary blue is estimated**: `#0055FF` is an informed approximation of Perfora's signature electric blue. The actual value may differ slightly (likely range: #0050FF–#005CE5); confirm via DevTools > Computed > background-color on a primary CTA.
- **Font families unconfirmed**: No font-family stacks were extracted. Gilroy is the most probable primary typeface based on Perfora's brand materials and packaging; Neue Haas Grotesk or Inter are the next candidates. Verify under DevTools > Network > Fonts on the live site.
- **Typography scale unverified**: All `fontSize` and `fontWeight` values are reasoned from visual comparison with Indian DTC peers; validate against live computed styles before implementation.
- **Product-line sub-palettes**: Perfora differentiates product categories (whitening, brushes, accessories) with variant-specific colour cues on packaging. These sub-palette tokens are absent here pending live extraction.
- **Dark mode**: Unknown whether Perfora implements a dark mode variant; this system assumes light mode only.
- **Icon library style**: The nav and marketing sections likely use a custom or licensed icon set; stroke weight, fill style, and size grid cannot be confirmed without site access.
- **Animation tokens**: Transition durations and easing curves (hover states, drawer open, add-to-cart micro-animations) are not derivable without live site inspection.
