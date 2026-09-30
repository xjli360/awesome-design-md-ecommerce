---
version: alpha
name: "Tingley Rubber"
source_url: "https://www.tingleyrubber.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Waterproof workwear demands a visual language that communicates protection instantly — Tingley achieves this through safety-red (#ea1921) CTAs set against a deep navy foundation (#272d45), while an unexpected purple-gray mid-tone (#676986) threads through body copy and secondary UI, giving the catalog a more refined register than most PPE competitors. The palette is a study in functional signal hierarchy: red fires for primary actions, safety-yellow (#ffcf2a) marks hazard callouts and promotional banners, a teal accent (#00caaa) flags technology features like ANSI ratings, and a soft mint (#b2f9e9) surfaces on compliance-verified product cards. The dark-to-light navy range — from deep #272d45 through slate #2c3e50 to the muted purple-gray #9a9db1 — forms an industrial chromatic foundation that eschews the typical black-and-safety-orange convention without sacrificing authority. Type runs on Arial throughout, a deliberate functional choice that signals no-frills professionalism: this is a brand that would rather display waterproofing specs than typographic finesse. Buttons are sharp-cornered ({rounded.xs}), not pill-shaped; the UI vocabulary is angular and worksite-ready rather than consumer-friendly. Product cards carry ASTM and ANSI compliance badges in cardinal red and certification-green (#4bb543), embedding regulatory data directly into the browse experience. A four-color badge matrix — red for hazard class, green for certification, teal for material spec, yellow for caution — encodes an entire regulatory vocabulary without prose. The overall composition reads as a PPE catalog that has quietly systematized its safety-signal language: each color carries a meaning, each component a function, nothing is purely decorative.

colors:
  primary: "#ea1921"
  primary-active: "#c41118"
  primary-disabled: "#f7a0a3"
  ink: "#121212"
  body: "#272d45"
  muted: "#676986"
  muted-light: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f8"
  surface-card: "#f4f4f6"
  surface-mid: "#d3d4dd"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  navy-deep: "#272d45"
  navy-mid: "#2c3e50"
  accent-yellow: "#ffcf2a"
  accent-teal: "#00caaa"
  accent-mint: "#b2f9e9"
  accent-green: "#4bb543"
  accent-periwinkle: "#899df1"
  accent-teal-deep: "#0e7a82"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px

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
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    border: "2px solid {colors.primary}"
    height: 44px
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    border: "2px solid {colors.on-dark}"
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.primary}"
  text-input-search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 40px 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    logoColor: "{colors.on-dark}"
  nav-utility-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 36px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "1/1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-sm}"
    hoverBorderColor: "{colors.primary}"
  safety-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  compliance-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  spec-badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  warning-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero-banner:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 480px
    paddingVertical: "{spacing.section}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    imageHeight: 200px
  alert-strip:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    padding: 8px 16px
  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    padding: 8px 16px
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.caption-bold}"
    border: "1px solid {colors.hairline}"
    rowStripeColor: "{colors.surface-soft}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-light}"
    activeColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: 32px 48px

## Components

### Buttons

**`button-primary`** — Uppercase Arial at 15px/700 on a sharp-edged ({rounded.xs}) cardinal-red (#ea1921) background, 44px tall with 24px horizontal padding. The all-caps tracking and square corners signal worksite functionality over consumer persuasion. Hover deepens to #c41118; disabled state washes to #f7a0a3. Use exclusively for primary commerce actions: Add to Cart, Shop Now, Find a Distributor.

**`button-secondary`** — White fill with a 2px red (#ea1921) border and red text, matched to primary in height and typography. Communicates an alternative action alongside the primary CTA without visual competition. A dark-surface variant (`button-secondary-dark`) uses a transparent fill and white border for use on navy hero and footer areas.

**`button-ghost`** — Transparent with muted-purple (#676986) text at 13px uppercase, used for tertiary actions like "Compare," "See All," or filter resets where visual weight must stay low.

### Text Inputs

**`text-input`** — White canvas fill with a 1px hairline border (#dbdde4), 44px height, and {rounded.xs} corners consistent with the button vocabulary. Focus swaps to a 1px red (#ea1921) border with no fill change. The search variant (`text-input-search`) carries a right-aligned search icon in its 40px right-padding zone and uses the soft surface-card (#f4f4f6) fill to distinguish it from form inputs.

### Navigation

**`nav-bar`** — Deep navy (#272d45) at 60px height with white type and icons. Primary nav links run 14px/700 Arial with 0.3px tracking. Directly above, a `nav-utility-bar` in brand red (#ea1921) at 36px height carries shipping thresholds, login links, and cart count in 12px/700 uppercase — a two-register nav system that separates utility from commerce navigation, common in B2B-adjacent PPE ecommerce.

### Product Card

**`product-card`** — White canvas card with 1px hairline border and {rounded.xs} radius. Product image occupies a 1:1 aspect-ratio zone at top. Below: product name in 16px/700 Arial, price in matching weight, and a horizontal row of badge chips (safety-badge, compliance-badge, spec-badge) denoting ASTM ratings, ANSI classes, and material specs. Hover lifts a red border highlight; no shadow elevation.

### Badge System

**`safety-badge`** — Cardinal-red (#ea1921) chip in 11px/700 uppercase Arial with 3px/8px padding and {rounded.xs}. Used for OSHA and ASTM hazard-class labels. Three additional variants form the complete regulatory vocabulary: **`compliance-badge`** in certification-green (#4bb543) for approved certifications, **`spec-badge`** in teal (#00caaa) for material and technology specs, and **`warning-badge`** in safety-yellow (#ffcf2a) with black ink for caution callouts. The four-color matrix encodes regulatory data without prose on every product card and in listing filters.

### Hero Banner

**`hero-banner`** — Full-bleed deep navy (#272d45) section at minimum 480px tall. Display headline in 40px/700 Arial white; supporting line at 16px/400 body-md. A `button-primary` (red) anchors the CTA zone. Product photography shows boots and rainwear in outdoor or industrial settings at high contrast against the dark field. Vertical padding is {spacing.section} (64px) on each side.

### Category Tile

**`category-tile`** — Soft surface-card (#f4f4f6) background with 1px hairline border and a category image at 200px height. Title in 16px/700 Arial below. Hover transitions the border color to primary red (#ea1921), providing clear selection feedback. Used in the homepage category grid and mega-menu dropdown panels.

### Alert and Promo Strips

**`alert-strip`** — Full-width safety-yellow (#ffcf2a) band in 12px/700 uppercase Arial with black ink (#121212). Deployed for site-wide safety notices, recall callouts, or regulatory change announcements — the yellow signals informational urgency without using the red reserved for commerce. **`promo-strip`** — Identical geometry in primary red (#ea1921) with white text, for promotional messaging like seasonal discounts or free-shipping thresholds.

### Spec Table

**`spec-table`** — White canvas body with surface-card (#f4f4f6) header row and alternating surface-soft (#f7f7f8) row stripes. 1px hairline borders throughout. Header cells in 12px/700 uppercase Arial ({typography.caption-bold}); body cells in 14px/400 ({typography.body-sm}). Used for the extensive product detail specification sheets covering dielectric ratings, chemical resistance grades, waterproof membrane specs, and ASTM compliance levels — typically the largest content block on any product page.

### Breadcrumb

**`breadcrumb`** — Transparent background, muted-purple (#676986) text at 12px/400, with muted-light (#9a9db1) separators. The active (current page) segment uses body navy (#272d45). Sits between the utility nav and page headline on all category and product pages.

### Footer

**`footer`** — Deep navy (#272d45) matching the nav bar. Column headings in 16px/700 white Arial; links in 14px/400 at hairline-soft (#e5e5eb). 32px top padding, 48px horizontal padding. A thin red or hairline-soft rule separates the link columns from the legal and copyright row, maintaining the two-tone navy/red register carried through the full page shell.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger icon replacing full nav; hero drops to 320px min-height with stacked headline and CTA; badge chips wrap below product title; spec tables scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav collapses to icon bar with flyout panel; hero shifts to side-by-side text/image; spec tables scroll horizontally with sticky label column |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with mega-menu dropdowns; hero at full 480px; spec tables fully visible |
| Wide | > 1440px | Max-content container (~1400px) centered; flanking whitespace fills at canvas white; nav utility bar locks to full viewport width |

### Touch Targets
- All interactive elements maintain 44×44px minimum, matching button and input heights
- Badge chips on product cards are display-only on mobile; tapping the card opens the product detail page, not badge-filtered results
- Nav hamburger target is minimum 44×44px; the flyout fills full viewport width with accordion category tree
- Quantity steppers in cart are 44px square with visible +/− labels at 18px/700

### Collapsing Strategy
- Mega-menu nav collapses to a single hamburger with accordion-style category tree at mobile, maintaining the same two-level hierarchy
- The two-strip nav (utility bar + main bar) merges to a single dark bar at mobile, surfacing only cart and account icons alongside the logo and hamburger
- Alert-strip and promo-strip stack vertically if both are active; promo-strip stacks below alert-strip
- Product filters shift from a left sidebar (desktop) to a modal drawer (mobile/tablet) triggered by a "Filter & Sort" button above the grid
- Spec tables become horizontally scrollable at tablet and below, with the first column (spec label) sticking left

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom typeface detected — site relies entirely on system Arial; a custom wordmark or display font may exist as an SVG logo asset not captured in CSS font stacks
- Font stacks include `oke-widget-icons` (Okendo reviews widget) and `swiper-icons` (carousel library) — neither represents brand typography
- A `serif ! important` stack was detected; likely injected by a third-party script, not a deliberate brand choice
- No meta theme-color is set — mobile browser chrome color and PWA splash behavior are unconfirmed
- Nav-bar height (60px) and utility-bar height (36px) are estimated from typical Shopify PPE patterns; exact values not confirmed from live CSS
- The periwinkle (#899df1) and deep-teal (#0e7a82) colors appear in extraction but their specific UI roles — possibly hover states, icon fills, or secondary badge types — were not confirmed
- Accent-mint (#b2f9e9) surface application is inferred; exact usage context (product card highlight, feature callout background) not confirmed
- Hover transition durations, box-shadow values, and focus-ring styles not extractable from static color extraction
- Logo SVG color scheme not confirmed; white-on-navy assumption follows standard practice for dark nav bars but should be verified
