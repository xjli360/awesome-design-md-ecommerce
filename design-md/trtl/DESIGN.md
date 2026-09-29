---
version: alpha
name: "Trtl"
source_url: "https://trtltravel.com/"
captured_at: "2026-09-29T04:11:18.887114+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from Trtl's live storefront at trtltravel.com, a Shopify-hosted DTC site selling travel pillows, sleep masks, and travel accessories. The supplied palette is dominated by neutral grounding tones — near-black inks (#000000, #1a1a1a, #161616), warm off-whites (#ffffff, #fdfdfd, #f7f7f7), and mid-greys (#707070, #87888a, #dddddd) — with a deep navy (#243b61) reading as the strongest candidate for a primary brand color given its saturation relative to the surrounding neutrals. Warm accent tones (#fad951 yellow, #d6b473 gold) likely carry promotional "% OFF" badges and birthday-campaign styling seen in the page copy, while #dd2222 is inferred as a sale/urgency accent. A darker navy (#16233a) is proposed as a footer/deep-surface tone, consistent with the multi-navy family present in the palette.
  Font evidence includes a long list of families (Inter, Work Sans, Satoshi, IBM Plex Sans/Mono, Plus Jakarta Sans, Lora, PT Sans, Roboto Condensed, IntroExtraBold), typical of a Shopify theme plus third-party review/app scripts. This spec treats Inter as the probable UI/body workhorse and IntroExtraBold as a probable bold display face for hero headlines, both clearly labeled as inferred choices rather than confirmed live observations. Layout, spacing, and rounded values below are proposed conventions for a travel-comfort e-commerce brand, not measured from rendered pages.

colors:
  primary: "#243b61"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#87888a"
  hairline: "#dddddd"
  surface-soft: "#f7f7f7"
  surface-card: "#fdfdfd"
  on-primary: "#ffffff"
  accent-yellow: "#fad951"
  accent-gold: "#d6b473"
  danger: "#dd2222"
  surface-deep: "#16233a"
  border-soft: "#e5e5e5"
typography:
  display-xl: {fontFamily: "IntroExtraBold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "IntroExtraBold, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "IBM Plex Mono, monospace", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  review-stars:
    activeColor: "{colors.accent-gold}"
    inactiveColor: "{colors.hairline}"
    typography: "{typography.caption}"
    textColor: "{colors.muted}"

## Components
**button-primary**: The main add-to-cart / shop-now action, using the inferred navy primary against white text. Proposed hover/active states (slight darken or opacity shift) are not confirmed from static CSS.

**button-secondary**: An outlined variant for lower-emphasis actions such as "Compare our pillows" or quiz entry points; border and text share the primary navy, background stays white.

**text-input**: Used for newsletter signup and search fields; a light hairline border on white keeps it visually quiet against the neutral canvas, consistent with the light greys observed in the palette.

**nav-bar**: A white top bar housing category links (PILLOWS, ACCESSORIES, TRAVEL WEAR, BUNDLES, CLEARANCE) with a thin bottom hairline; sticky/scroll behavior is proposed, not observed.

**product-card**: Represents bestseller tiles (e.g., "TRTL TRAVEL PILLOW," bundle products) with price, strikethrough compare-price, review count, and an add-to-cart button; card background is a near-white surface distinct from pure canvas white for subtle depth.

**hero**: The homepage banner promoting the "13th Birthday" 20%-off campaign; a deep navy background with large display type is proposed to match the brand's presumed premium/travel-comfort positioning, though the live hero's actual background is not confirmed from the supplied evidence.

**footer**: Dark navy footer containing support links, trust badges (100-day guarantee, free shipping), and newsletter signup, mirroring the deep-surface tone used in the hero for visual bookending.

**badge**: Small pill labels for "SAVE 20%/30%/50%" and "20% OFF" ribbons on product tiles and hero slides, using the yellow accent for visibility against both light and dark surfaces.

**search**: A lightweight input pattern for the site's product/category search, styled consistently with text-input but on the soft-grey surface tone to differentiate it from form fields on white sections.

**review-stars**: Given the heavy reliance on review counts and ratings text (e.g., "Rated 4.7 out of 5 — 1704 Reviews") throughout the excerpt, a star-rating component using the gold accent for filled stars and hairline grey for empty ones is proposed as category-appropriate for a review-driven DTC storefront.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured from live responsive behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | <480px | Single-column product grid, stacked hero text, hamburger nav |
| Small tablet | 480–768px | 2-column product grid, condensed nav links |
| Tablet | 768–1024px | 2–3 column grid, full nav bar with dropdowns |
| Desktop | 1024–1440px | 3–4 column grid, full mega-menu categories |
| Wide | >1440px | Max-width container centered, generous section padding |

Touch targets should be at least 44px tall for buttons and nav items on mobile. Category navigation (PILLOWS, ACCESSORIES, TRAVEL WEAR, BUNDLES, CLEARANCE, COLLECTIONS, EXPLORE) is proposed to collapse into a slide-out drawer below tablet width. None of this reflects confirmed live breakpoints or interaction states.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS/text extraction only; no rendered layout, hover states, animations, or actual mobile behavior were observed.
- The specific role of each supplied hex (e.g., whether #243b61 is truly the primary brand color versus an incidental UI tone) is inferred from relative saturation and context, not confirmed via labeled design tokens.
- Font family list includes numerous icon fonts (Font Awesome variants) and a broad set of text families (Inter, Work Sans, Satoshi, IBM Plex Sans/Mono, Plus Jakarta Sans, Lora, PT Sans, Roboto Condensed, IntroExtraBold); which are actually applied to headings versus body versus third-party review widgets is not determinable from the supplied evidence.
- Typography sizes, weights, and line-heights are proposed conventions, not measured from computed styles.
- Rounded and spacing scales are standard proposed conventions, not extracted from site CSS variables.
- Custom or licensed font availability (e.g., IntroExtraBold, Satoshi) has not been verified for redistribution or licensing terms.
- Component states (hover, focus, disabled, loading) are proposed patterns only; no interactive states were present in the supplied evidence.
