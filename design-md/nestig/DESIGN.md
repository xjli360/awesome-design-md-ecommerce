---
version: alpha
name: "Nestig"
source_url: "https://nestig.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A nursery brand that builds its visual language around a deep, confident navy (#173482) and a warm, blush-adjacent clay (#e6c9c1), a pairing that reads as both heirloom-solid and tender. The palette is unusually generous — a full spectrum of muted earth tones (#965f44, #bf7f4c, #c1996c), soft pinks (#e2c4c9, #e7bacc), and airy blues (#8fbed4, #c2e6fa, #aac4e7) that suggest a brand unafraid of color in a category that often defaults to all-white or all-gray. The primary navy (#173482) carries CTAs and key structural elements, while the clay (#e6c9c1) appears in secondary surfaces and accent blocks, creating a warm counterpoint. The type system leans on Matter and Gooper for display moments — Matter brings a geometric, almost architectural precision to headings, while True North Script introduces a hand-lettered, personal note in hero titles and badges. Assistant serves as the workhorse body face, keeping product descriptions and navigation legible at small sizes. Rounded corners are restrained: cards and inputs use a soft 8px (`{rounded.sm}`), while badges and small decorative elements may go fully pill-shaped (`{rounded.full}`). The canvas is a warm off-white (#f9f5f2) rather than pure white, giving every page a lived-in, nursery-at-dusk quality. Nestig trusts its color blocks and generous product photography over heavy typographic hierarchy — the brand feels like a room you want to sit in, not a catalog you scan.

colors:
  primary: "#173482"
  primary-active: "#0f2560"
  primary-disabled: "#aac4e7"
  ink: "#110c0d"
  body: "#2c3e50"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#f9f5f2"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-clay: "#e6c9c1"
  accent-rose: "#e2c4c9"
  accent-sky: "#8fbed4"
  accent-gold: "#c1996c"
  accent-terracotta: "#bf7f4c"
  accent-sage: "#b2f9e9"
  accent-marigold: "#e9d84c"
  error: "#b63636"
  star-rating: "#c1996c"
  scrim: "#0a0a0a"

typography:
  display-xl:
    fontFamily: "'Matter', 'Gooper', Georgia, serif"
    fontSize: 42px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Matter', 'Gooper', Georgia, serif"
    fontSize: 34px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Matter', 'Gooper', Georgia, serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Matter', 'Gooper', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  script-display:
    fontFamily: "'True North Script', cursive"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  button-md:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Assistant', Geneva, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px

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
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.accent-clay}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-clay:
    backgroundColor: "{colors.accent-clay}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
  checkbox:
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    checkedBackground: "{colors.primary}"
    checkedBorder: "2px solid {colors.primary}"
  radio:
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    checkedBorder: "6px solid {colors.primary}"
  toggle:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    activeBackground: "{colors.primary}"
    knobColor: "{colors.on-primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  mobile-nav-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.base} {spacing.base} {spacing.xs} {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  hero-section:
    backgroundColor: "{colors.accent-clay}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-script-overlay:
    typography: "{typography.script-display}"
    textColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  badge-new:
    backgroundColor: "{colors.accent-marigold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 8px"
  badge-sustainability:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "3px 8px"
  rating-stars:
    color: "{colors.star-rating}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.accent-sky}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-expanded:
    backgroundColor: "{colors.surface-soft}"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    fillColor: "{colors.primary}"
  stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    buttonColor: "{colors.primary}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"
  modal:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    scrimColor: "{colors.scrim}"
    scrimOpacity: 0.6
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0 {spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the brand's deep navy (#173482) with white text. Used for "Add to Cart", "Shop Now", and primary form submissions. On hover, shifts to a darker navy (`{colors.primary-active}`). Disabled state uses a muted blue (`{colors.primary-disabled}`) with white text. All primary buttons maintain a consistent 48px height and 8px rounded corners.

**`button-secondary`** — A warm alternative CTA using the clay accent (`{colors.accent-clay}`) with dark ink text. Used for "Learn More", "View Details", and secondary actions in hero sections and product cards. Active state deepens to rose (`{colors.accent-rose}`). Height and corner radius match the primary button for visual consistency.

**`button-outline`** — A transparent button with a 2px navy border and navy text. Used for "Save for Later", "Compare", and tertiary actions where a filled button would feel too heavy. Maintains the same 48px height and 8px corner radius as filled variants.

**`button-pill-primary`** and **`button-pill-clay`** — Fully pill-shaped buttons used for badges, tags, and compact actions like "Quick Add" or filter toggles. The pill shape (`{rounded.full}`) distinguishes these from standard CTAs. Used in product cards, category strips, and promotional banners.

### Cards
**`product-card`** — A white card with an 8px rounded corner, no padding at the container level — the image fills the top with `{rounded.sm}` applied to the top corners only. The title uses `{typography.title-sm}` with 16px horizontal padding and 12px top padding. The price sits below in `{typography.body-md}` with 4px top padding and 16px bottom padding. Badges overlay the image area at the top-left corner.

**`product-card-badge`** — A gold (`{colors.accent-gold}`) pill badge with uppercase, 11px bold type. Used for "Best Seller", "New", or "Eco-Friendly" labels. Positioned absolutely over the product image with 8px inset from the top-left.

### Navigation
**`nav-bar`** — A 72px white bar with a soft bottom border (`{colors.hairline-soft}`). Navigation links use 15px weight-600 type with 0.2px letter spacing. The active link is underlined with a 2px navy border. On hover, links shift to navy. The mobile drawer uses the same white background and link styling, stacked vertically.

**`search-bar`** — A fully pill-shaped search input with a 1px hairline border. On focus, the border thickens to 2px and shifts to navy. The placeholder text uses `{colors.muted-soft}`. Height is 48px with 12px vertical and 20px horizontal padding.

### Forms
**`text-input`** — Standard form input with 8px rounded corners, 1px hairline border, and 12px/16px padding. On focus, the border becomes a 2px navy line. Error state uses a 2px red (`{colors.error}`) border. The placeholder is `{colors.muted-soft}`.

**`checkbox`** and **`radio`** — Checkboxes use 4px rounded corners with a 2px hairline border. Checked state fills the background with navy. Radio buttons are fully circular with a 2px hairline border; checked state shows a 6px navy inner circle.

**`toggle`** — A pill-shaped toggle with a hairline gray background. Active state fills with navy. The circular knob is white.

### Footer
**`footer`** — A deep navy (`{colors.primary}`) footer with white text. Links use 14px weight-500 type and shift to sky blue (`{colors.accent-sky}`) on hover. The footer spans the full width with 64px vertical padding and 24px horizontal padding.

### Badges
**`badge-new`** — A marigold (`{colors.accent-marigold}`) pill badge used for new arrivals. Uses uppercase 11px bold type with 3px/8px padding.

**`badge-sale`** — A red (`{colors.error}`) pill badge for sale items. White text on red background.

**`badge-sustainability`** — A sage green (`{colors.accent-sage}`) pill badge for eco-friendly or sustainable products. Dark ink text.

### Accordion
**`accordion`** — A white, 8px rounded container with a 1px soft hairline border. The header uses `{typography.title-sm}`. Expanded state shifts the background to `{colors.surface-soft}`. Used for FAQ sections, product details, and shipping information.

### Tabs
**`tab-active`** and **`tab-inactive`** — Active tabs use a navy fill with white text and 8px rounded corners. Inactive tabs use a soft surface background with muted text. Both use `{typography.button-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav replaces full nav bar, hero section reduces to 32px vertical padding, product cards stack full-width, footer links stack vertically, search bar collapses to icon-only |
| Tablet | 744–1128px | Two-column product grid, nav bar shows 4-5 primary links with hamburger for overflow, hero section uses 48px vertical padding, footer uses 3-column layout |
| Desktop | 1128–1440px | Three-column product grid, full nav bar visible, hero section at full 64px vertical padding, footer uses 4-column layout, search bar full-width in header |
| Wide | > 1440px | Max-width container at 1440px, centered layout with generous margins, four-column product grid, hero section may include full-bleed imagery |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Product card tap targets (title, price, add-to-cart) are spaced at least 8px apart
- Nav links have a minimum 48px tap area on mobile
- Checkbox and radio touch targets are 44px x 44px (includes invisible padding)
- Accordion headers have a minimum 48px tap height

### Collapsing Strategy
- On mobile, the full nav bar collapses to a hamburger menu with a slide-in drawer
- The search bar collapses to a magnifying glass icon that expands to full-width on tap
- Product filters collapse to a "Filter" button that opens a bottom sheet
- The footer's multi-column layout collapses to a single column with accordion-style section headers
- Hero sections reduce vertical padding by 50% on mobile
- Product image galleries switch from horizontal thumbnails to dot indicators

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font list includes "inherit" and "oke-widget-icons" (Okendo review widget), which are not brand fonts — these were excluded from the typography system
- True North Script appears in the extracted fonts but its exact usage context (hero headlines, badges, or decorative elements) could not be confirmed from the extraction alone
- Hover and focus states for many components are inferred from common patterns rather than extracted from the live site
- Error, success, and warning color tokens for form validation were not extracted — only a single red (#b63636) was found
- Dark mode tokens are absent; the brand appears to use a light-only palette
- The exact font weights for Matter and Gooper could not be extracted — weights shown are based on typical usage in similar DTC brands
- Spacing values (padding, margins, gaps) are estimated from common e-commerce patterns rather than extracted from the live site
- The star-rating color (#c1996c) is inferred from the extracted gold accent — actual rating implementation may vary
- The extracted color list includes 30+ colors, many of which may be from third-party widgets (Okendo reviews, Shopify checkout, social icons) rather than the brand's core palette — the primary navy and clay accent were selected as the most distinctive and frequently occurring brand colors
- No animation or transition timing values were extracted
- The brand's Shopify platform is confirmed, but specific theme information was not extracted
