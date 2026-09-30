---
version: alpha
name: "Bond Manufacturing"
source_url: "https://www.bondmfg.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Steel geometry frames open flame — Bond Manufacturing's fire pits and patio heaters sit at the precise junction of fabricated metal and outdoor ritual, and the brand's digital identity holds that tension in a high-contrast industrial palette where near-black backgrounds let warm ember tones carry the visual heat. A combustion orange at approximately #e85d04 — the brand's single emotional accent — pulls primary CTAs out of the dark canvas the way a lit fire pit reads against a night yard: one point of warmth surrounded by structural dark. Product edges throughout the UI square off at {rounded.xs} to echo the machined-corner construction of the cast-iron and rolled-steel pieces in the catalog. Filter pills break the pattern by rounding to {rounded.full}, providing a softer visual counterpoint against an otherwise angular category grid.

  The buying journey is spec-forward, not lifestyle-aspirational. Homeowners arrive researching BTU output, fuel compatibility, and CSA certification status; the product page surfaces this data early in a tight specification table with uppercase labels in {colors.muted} and generous numerical values in {colors.ink}. Photography exists to show the product operating — fire lit, night setting, outdoor context — rather than to project a fantasy lifestyle. Navigation is catalog-flat across Fire Pits, Patio Heaters, Accessories, and Parts & Support, with no editorial content layer between the landing page and product grids. The Parts & Support section functions as a post-purchase retention surface, with a model-number lookup widget returning replacement burner rings, igniters, and grates — reinforcing the durability promise the hardware specs make upfront.

  Hero and footer sections invert to full-dark using {colors.surface-dark}, creating contained brand moments where white text and ember accents read against a pitch background — the digital equivalent of firelight contrast at night. Type runs at modest weights throughout, 400 to 600, trusting bold product imagery to carry compositional energy rather than heavy typographic declarations. The ember accent at {colors.accent} does nearly all the brand signaling; every other UI token is a functional neutral.

colors:
  primary: "#1c1c1c"
  primary-active: "#333333"
  primary-disabled: "#888888"
  accent: "#e85d04"
  accent-active: "#c74e03"
  accent-disabled: "#f4c09e"
  ink: "#1a1a1a"
  body: "#3a3a3a"
  muted: "#6b6b6b"
  hairline: "#d0d0d0"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f4f2"
  surface-card: "#ffffff"
  surface-dark: "#1c1c1c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  ember: "#e85d04"
  ember-soft: "#fff1e9"
  warning: "#f59e0b"

typography:
  display-xl:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-upper:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  spec-label:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.02em
  button-sm:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "'Inter', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.accent-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.hairline}"
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-sm}"
    captionTypography: "{typography.body-sm}"
    imageAspectRatio: "4/3"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.ember}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    paddingV: "{spacing.section}"
  category-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    overlineTypography: "{typography.caption-upper}"
    overlineColor: "{colors.muted}"
    titleTypography: "{typography.display-sm}"
    rounded: "{rounded.xs}"
    paddingH: "{spacing.xxl}"
    paddingV: "{spacing.xl}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted}"
    labelTypography: "{typography.spec-label}"
    valueColor: "{colors.ink}"
    valueTypography: "{typography.body-sm}"
    rowBorder: "1px solid {colors.hairline}"
    rowPaddingV: "{spacing.md}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"
  promo-badge:
    backgroundColor: "{colors.ember}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
    height: 40px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px"
    height: 44px
  parts-finder:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-md}"
    inputBorder: "1px solid {colors.hairline}"
    accentColor: "{colors.accent}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xl}"
  comparison-row:
    backgroundColor: "{colors.canvas}"
    alternateBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
  certification-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    paddingV: "{spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.caption-upper}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.on-dark}"
    borderTop: "1px solid {colors.primary-active}"

## Components

### Buttons

**`button-primary`** — Ember orange (`{colors.accent}`) background with white text at `{rounded.xs}`, 48px tall. This is the brand's single visual intensity point; it appears on "Add to Cart", "Shop Now", and "Find a Retailer" calls-to-action. Active state deepens to `{colors.accent-active}`; disabled state washes to `{colors.accent-disabled}`, preserving the hue family.

**`button-secondary`** — White background, 1.5px ink border, `{colors.ink}` text. Used alongside the primary CTA in two-button PDP layouts — typically "Add to Cart" + "Download Spec Sheet" or "Add to Cart" + "Where to Buy". On dark hero sections the `button-secondary-dark` variant replaces the border with a white 1.5px stroke against a transparent background.

**`button-ghost`** — Text-only, `{colors.muted}` color, no background or border. Reserved for low-priority secondary links like "View all accessories", "Back to category", or inline "Learn more" anchors within body copy.

### Navigation

**`nav-bar`** — 64px tall, white canvas background, 1px `{colors.hairline-soft}` bottom border. Logo anchored left; category links (Fire Pits, Patio Heaters, Accessories, Parts & Support) at `{typography.nav-link}` weight 500 float right alongside cart and search icons. On pages with dark hero photography, the nav can shift to `nav-bar-dark` — same height and structure but reversed to white-on-dark. Mobile collapses to a hamburger icon below 744px with a full-height slide-in drawer.

### Product Card

**`product-card`** — White card, 1px `{colors.hairline-soft}` border, `{rounded.xs}` corners, `{spacing.base}` internal padding. Product photography fills the top ~60% at a 4:3 ratio; model name renders in `{typography.title-sm}` weight 600 below; price and a one-line spec summary (BTU rating or fuel type) follow in `{typography.body-sm}`. A `promo-badge` ("SALE", "NEW", "CLEARANCE") overlays the image corner in `{colors.ember}` with `{typography.spec-label}` text when applicable.

### Hero

**`hero-dark`** — Full-bleed section on `{colors.surface-dark}` with a white `{typography.display-xl}` headline and optional ember-orange accent on a sub-headline or decorative rule. Designed for night-time product photography where the fire glow becomes the primary visual. CTA row pairs `button-primary` with `button-secondary-dark`. Vertical padding is `{spacing.section}` above and below copy; imagery bleeds to the container edge with no card border.

### Spec Table

**`spec-table`** — Two-column key-value layout used on every PDP to surface BTU output, fuel type, ignition type, material, weight, and dimensions. Row labels render in `{typography.spec-label}` — 12px, uppercase, letter-spaced, `{colors.muted}` — with values in `{typography.body-sm}` at `{colors.ink}`. Rows are separated by `{colors.hairline}` borders with `{spacing.md}` vertical padding. No background striping; the label/value contrast does the visual work.

### Spec Badge

**`spec-badge`** — Small rectangular chips for surfacing key certifications and stats inline on product cards and category pages ("CSA Certified", "50,000 BTU", "Auto Ignition"). Soft gray `{colors.surface-soft}` background, ink text, `{typography.caption-upper}` with tracking. Corners at `{rounded.xs}`.

### Category Banner

**`category-banner`** — Header strip at the top of each category listing page. Overline in `{typography.caption-upper}` (`{colors.muted}`), followed by the category name in `{typography.display-sm}`. Soft gray `{colors.surface-soft}` fill with right-side product image at desktop; stacks to headline-only on mobile.

### Filter Pills

**`filter-pill`** and **`filter-pill-active`** — Horizontal scrolling filter row on category pages for fuel type (Propane, Natural Gas, Wood), BTU range, and price band. Inactive pills have `{colors.surface-soft}` fill and a `{colors.hairline}` border; active pills invert to `{colors.ink}` background with `{colors.on-dark}` text. Both use `{rounded.full}` — the only curved element in an otherwise angular layout — to signal interactivity and soften the filter strip visually.

### Parts Finder

**`parts-finder`** — A functional widget unique to the Parts & Support section. Accepts a model number in a text input and returns matching replacement parts (burner rings, igniters, regulators, grates). The `{colors.accent}` ember orange highlights the search submit button and matched part CTAs. Background `{colors.surface-soft}`, heading `{typography.title-md}`, internal padding `{spacing.xl}`. This component is a key post-purchase retention surface — buyers who find parts easily become repeat customers.

### Comparison Row

**`comparison-row`** — Side-by-side product comparison table used when multiple fire pit models are rendered together. Alternates `{colors.canvas}` and `{colors.surface-soft}` row backgrounds; spec row labels in `{typography.spec-label}` at `{colors.muted}`; values in `{typography.body-sm}` at `{colors.ink}`. Column borders use `{colors.hairline}`. On mobile, collapses to a swipeable card stack (one product visible at a time) with sticky first-column labels.

### Certification Strip

**`certification-strip`** — A narrow horizontal band below the PDP spec table showing certification logos (CSA, UL) and compliance copy in `{typography.caption}` at `{colors.muted}`. `{colors.surface-soft}` background, top border `{colors.hairline}`, `{spacing.base}` vertical padding. Reinforces the safety and standards positioning that differentiates Bond from unbranded import competitors.

### Footer

**`footer`** — Full-width dark section on `{colors.surface-dark}`, white text throughout. Column headings in `{typography.caption-upper}`; navigation links in `{typography.body-sm}` at `{colors.muted}`, hovering to `{colors.on-dark}`. Bottom bar includes newsletter email input, social icons, and certification mark row. Separated from the body by a subtle `{colors.primary-active}` top border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline drops to `{typography.display-md}`; filter pills scroll horizontally; spec table full-width single column; comparison table becomes swipeable card stack |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories, sub-menus on tap; category banner retains headline but drops side image; filter pills in top horizontal row |
| Desktop | 1128–1440px | Three-column product grid; full nav with hover sub-menus; PDP splits 60/40 image gallery / spec detail; spec table full two-column width; parts finder expands inline |
| Wide | > 1440px | Max-width container centered at 1440px; four-column product grid; hero image bleeds to viewport edge outside container; footer columns spread to five |

### Touch Targets

- All buttons minimum 48px height
- Filter pills minimum 40px height with 16px horizontal padding
- Nav links minimum 44px tap target height
- Text inputs and parts finder search field minimum 48px height
- Product card CTA area full-width tap region on mobile (not limited to button bounds)

### Collapsing Strategy

- Category sub-navigation collapses from hover-dropdown to tap-accordion at tablet and below
- PDP spec table stays two-column down to 375px by reducing row padding to `{spacing.sm}`
- Hero dark section switches from side-by-side copy/image to stacked (copy above image) at mobile
- Comparison table converts from full grid to swipeable card stack at below 744px
- Footer four-column grid collapses to two columns at tablet, single-column accordion at mobile
- Parts Finder widget stacks vertically on mobile with full-width input and full-width submit button

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable from the live site — all palette values are estimated from outdoor/industrial brand category conventions and fire-product photography norms; the actual primary, accent, and surface values may differ significantly
- No font stacks were detected — typography falls back to Inter/Helvetica Neue; Bond Manufacturing may use a licensed display or industrial typeface not visible in static extraction
- No meta theme-color was present, consistent with a JS-token-loaded or anti-bot-protected site
- Bond Manufacturing sells through both DTC and major big-box retailers (Home Depot, Walmart, Costco); the DTC site may function more as a brand/parts hub than a primary purchase channel, which could shift the design posture toward catalog-reference rather than conversion-optimized
- Logo treatment, icon library style (line vs. filled), and any custom illustration system are unconfirmed
- Dark/light mode support, accessibility contrast ratios, and high-contrast mode behavior are unknown
- Mobile navigation structure (mega-menu vs. flat list vs. category tiles in drawer) could not be verified
