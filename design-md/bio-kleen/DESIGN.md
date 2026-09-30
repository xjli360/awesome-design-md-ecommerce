---
version: alpha
name: "Bio-Kleen"
source_url: "https://biokleenhome.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, forest-floor green (#025f1d) anchors every primary action and headline across a site that feels more like a naturalist’s field guide than a cleaning-supply store. The brand’s signature move is a dense, saturated green gradient that runs from #012d0e at its darkest to #03912c at its brightest — a living chlorophyll spectrum that appears in the hero background, the primary button fill, and the product-badge accent. Against a canvas of #ffffff and surface cards of #f9f9f9, the green reads as clean, not clinical; the supporting palette is almost entirely grays (#f2f2f2, #e8e8e8, #d1d1d1, #646464, #303030) that recede quietly, letting the green and the product photography do the work. A single red alert (#eb5757) and a deeper error red (#e02b27) provide the only chromatic tension. Typography runs on brandon-grotesque for headlines — a geometric, slightly condensed sans-serif with a friendly, mid-century feel — and Open Sans for body copy, both set at modest weights (400–600) with generous line heights. Buttons are softly rounded rectangles (`{rounded.sm}` ~8px), product cards use a slightly deeper radius (`{rounded.md}` ~12px), and the search bar is a pill (`{rounded.full}`) that echoes the organic, enzyme-friendly brand promise. The overall mood is earnest, botanical, and unpretentious — a cleaning brand that trusts its green to signal efficacy without shouting.

colors:
  primary: "#025f1d"
  primary-active: "#012d0e"
  primary-disabled: "#b8d9b8"
  ink: "#111111"
  body: "#303030"
  muted: "#646464"
  muted-soft: "#777777"
  hairline: "#d1d1d1"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  accent-green-light: "#03912c"
  accent-red: "#eb5757"
  accent-red-dark: "#e02b27"
  link-blue: "#006bb4"

typography:
  display-xl:
    fontFamily: "'brandon-grotesque', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'brandon-grotesque', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'brandon-grotesque', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'brandon-grotesque', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'brandon-grotesque', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  button-md:
    fontFamily: "'brandon-grotesque', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'brandon-grotesque', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  nav-link:
    fontFamily: "'brandon-grotesque', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'brandon-grotesque', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
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
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 14px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.sm}"
  product-badge:
    backgroundColor: "{colors.accent-green-light}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  search-bar-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
    opacity: 0.85

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, filled with the brand green (#025f1d) and set in uppercase brandon-grotesque at 16px/600 weight. On hover, it deepens to #012d0e (`{colors.primary-active}`); disabled state drops to a muted green-gray (#b8d9b8) with lighter text. The 8px radius (`{rounded.sm}`) keeps it approachable without sacrificing authority.

**`button-secondary`** — An outlined variant with a white fill, green text, and a 2px green border. Active state swaps to the darker green border and a light gray (#f5f5f5) background. Used for secondary actions like "Learn More" or "View All" alongside primary buttons.

**`button-tertiary`** — A text-only link styled as a button, with no background or border. The green text and uppercase tracking match the primary button’s typography. Used for inline actions like "See details" within product cards.

### Navigation
**`nav-bar`** — A fixed-height (72px) white bar with a thin bottom border (#ebebeb). Navigation links are set in 15px uppercase brandon-grotesque with 0.3px letter spacing. The active link is underlined with a 2px green bar and green text. The logo sits left-aligned, typically as an SVG lockup.

**`nav-link-active`** — The active state for top-level navigation items. Green text (#025f1d) with a 2px bottom border in the same green. Inactive links remain dark (#111111) with no underline.

### Cards
**`product-card`** — A white card (#f9f9f9) with a 12px radius (`{rounded.md}`) and 16px padding. Product images sit in a smaller 8px radius container within the card. Body text is Open Sans 14px/1.55. The card may include a `product-badge` for "New" or "Best Seller" indicators.

**`product-badge`** — A small pill-shaped badge filled with the lighter green (#03912c), white uppercase text at 11px, and full rounding. Positioned over the top-left of the product image. Used sparingly — only for promotional or new-product flags.

### Forms
**`text-input`** — A standard input field with a white background, 1px gray border (#d1d1d1), and 8px radius. On focus, the border thickens to 2px and turns green (#025f1d). Error state swaps to a 2px red border (#eb5757). Height is 48px with 12px/16px padding.

**`search-bar-pill`** — A fully rounded search input with a light gray background (#f5f5f5) and muted placeholder text (#777777). No border — the pill shape and soft fill signal it’s a discoverability tool, not a form field. Height is 48px.

### Footer
**`footer`** — A dark green (#012d0e) full-width section with white text at 85% opacity for links. Typography is Open Sans 14px. The footer typically contains three to four columns of links, a newsletter signup, and social icons. Padding is 48px vertical, 24px horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero text reduces to 24px; footer columns stack |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but compact; hero uses 28px headline; footer splits into two rows |
| Desktop | 1128–1440px | Full three- or four-column product grid; expanded nav; hero at 36px with background gradient visible |
| Wide | > 1440px | Max-width container (1200px) centered; hero background extends full bleed; product cards may show hover overlays |

### Touch Targets
- All interactive elements (buttons, links, inputs) are at least 44px tall per WCAG guidelines.
- Primary buttons are 48px tall with 28px horizontal padding for comfortable tap targets.
- Product card tap targets (image, title, price, CTA) are each at least 48px tall.
- Nav links have a minimum 44px tap area even when text is smaller.

### Collapsing Strategy
- On mobile (<744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- Product grids collapse from 4 columns (desktop) to 2 (tablet) to 1 (mobile).
- The hero section reduces headline size and may stack the CTA below the text rather than alongside it.
- Footer columns collapse from 4 to 2 to a single stacked column on mobile.
- The search bar may move from the nav into a dedicated expandable search panel on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for most components are inferred from the extracted color palette and common patterns; the live site may use different transitions or shadows.
- Error and success states for forms (validation messages, success banners) were not extracted; red (#eb5757) is used as the error accent but may not match the brand’s exact error styling.
- The extracted font list includes brandon-grotesque and Open Sans as the likely primary typefaces, but exact font weights, sizes, and line heights are estimated from common usage patterns — the live site may differ.
- Dark mode is not supported and no dark-mode tokens were found.
- The extracted hex list is dominated by grays and greens; the brand’s secondary accent palette (if any) beyond red and blue could not be determined.
- Spacing values are estimated from common e-commerce patterns; the live site may use a different scale.
- The `button-primary-disabled` color (#b8d9b8) is an approximation based on a lightened primary; the actual disabled color may vary.
- No animation or transition timing data was extracted (hover transitions, page load animations, etc.).
- The brand’s icon system (if any) was not captured; social media icon colors may account for some of the extracted blues and grays.
