---
version: alpha
name: "Laura Davidson"
source_url: "https://www.lauradavidson.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The teal #00b4b3 sits unexpectedly at the center of a brand that sells office chairs — not the corporate navy or warm leather brown one might expect, but a clear, pool-depth cyan that reads as confident rather than decorative. Against a near-black ink of #222222 and a warm espresso accent of #382110, the teal functions as both a product-line signal and the one moment of personality in an otherwise clean, utility-forward system. Laura Davidson's site runs on Squarespace with a system font stack — Helvetica Neue leading into Roboto and Arial — which gives the typography a purposeful plainness that keeps the furniture photography uncontested. There are no aggressive display fonts competing with chair silhouettes; weight and size do the hierarchy work instead. A lighter teal variant #5adfcb carries hover states and secondary accents, creating a monochromatic depth within the primary hue family rather than reaching for a contrasting pop. The surface palette is minimal: a white canvas, a single soft-gray surface at #f6f6f6, and a hairline that keeps product grid cells separated without visual noise. Product cards favor generous whitespace over dense information packing — consistent with a mid-to-premium ergonomic market where the buyer spends time comparing, not scanning. Rounded corners sit at a modest 6–8px throughout, projecting functional solidity rather than consumer softness; the brand is selling work tools, not lifestyle accessories. CTAs pull the teal primary at full saturation so that each "Add to Cart" or "Shop Now" carries the same chromatic authority as the brand mark itself. The warm brown #382110 appears sparingly — likely in heritage-adjacent lifestyle photography or leather finish callouts — grounding the otherwise cool palette with a material reference that reinforces the furniture positioning.

colors:
  primary: "#00b4b3"
  primary-active: "#009695"
  primary-disabled: "#a8e3e3"
  primary-hover: "#00cac9"
  accent-teal-light: "#5adfcb"
  ink: "#222222"
  body: "#3e3e3e"
  muted: "#6b6b6b"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  warm-dark: "#382110"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#cc2127"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.3px
  price-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 16px
  xl: 24px
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
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
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
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: "10px {spacing.base}"
    height: 44px
  text-input-error:
    border: "1px solid {colors.error}"
    textColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
  nav-bar-link-hover:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
  product-card-hover:
    border: "1px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    minHeight: 480px
  hero-cta-row:
    gap: "{spacing.base}"
    marginTop: "{spacing.lg}"
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  sale-badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  feature-callout-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} 0"
    gap: "{spacing.xxl}"
  product-detail-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  product-detail-price:
    typography: "{typography.price-lg}"
    textColor: "{colors.ink}"
  product-detail-label:
    typography: "{typography.label-upper}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    keyTypography: "{typography.body-sm}"
    valueTypography: "{typography.body-sm}"
    keyColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    linkColor: "#aaaaaa"
    linkHoverColor: "{colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"
  footer-legal:
    backgroundColor: "#111111"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    borderTop: "1px solid #333333"
    padding: "{spacing.base} {spacing.xl}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    buttonSize: 36px
    typography: "{typography.body-md}"
  swatch-selector:
    borderActive: "2px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
    size: 32px
    rounded: "{rounded.full}"
    gap: "{spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "10px {spacing.base}"
    iconColor: "{colors.muted}"

## Components

### Buttons
**`button-primary`** — Flat rectangular button (#00b4b3 fill, white text, uppercase tracking) with no border-radius, projecting a utilitarian confidence rather than consumer softness. Hover lightens to #00cac9; active darkens to #009695. The disabled state drains saturation to #a8e3e3 with white text preserved. All states maintain the uppercase letter-spacing to preserve brand voice.

**`button-secondary`** — White canvas with a 1px #222222 border and matching uppercase type. On hover the inversion is complete: background floods to ink (#222222), text turns white. This binary flip feels decisive rather than gradual — appropriate for a considered purchase environment.

**`button-ghost`** — A teal-outlined variant for tertiary actions like "Learn More" or "Compare." The 1px primary-color border echoes the primary CTA's hue without competing with it, useful on white cards or surface-soft sections.

### Text Inputs
**`text-input`** — Borderless-feeling at rest (1px #e0e0e0 hairline), activating to a 1px #00b4b3 focus ring on focus. No border-radius keeps the field consistent with the button geometry. Height is 44px for comfortable mobile tap targeting.

### Navigation
**`nav-bar`** — 72px tall, white canvas, 1px bottom hairline at #e0e0e0. Logo sits left; category links center or right depending on screen width. Link text runs at 14px/400 weight with 0.3px tracking — readable but not typographically dominant. Hover states add a 2px #00b4b3 underline rather than a color change, reinforcing the teal as the single accent system.

### Product Cards
**`product-card`** — Clean white cards with a 1px soft-hairline border at rest, upgrading to 1px primary (#00b4b3) on hover so the teal performs selection-state duty. Image fills a 4:3 aspect ratio at top; title in `title-sm` (15px/600) and price in `price-md` below. No hard shadows — the border handles separation. Category badges sit top-left over the image in teal, sale badges in #cc2127 error red.

### Hero Banner
**`hero-banner`** — Surface-soft (#f6f6f6) background rather than a full-bleed photography hero, which keeps loading fast and lets product imagery carry the page further down. Display type runs at 42px/300 weight — a light display cut that reads elegantly large without shouting. CTA buttons sit in a flex row with `{spacing.base}` gap, primary teal left, secondary outline right.

### Feature Callout Strip
**`feature-callout-strip`** — A slim horizontal band (top and bottom hairline borders, `{colors.surface-soft}` fill) listing trust signals like "Free Shipping," "Ergonomic Warranty," and "Assembly Included" in small uppercase body text. Runs full-width below the hero; items are evenly spaced with `{spacing.xxl}` gap between them.

### Product Detail
**`product-detail-title`** runs at 28px/400 — restrained for a hero element, but consistent with the brand's preference for whitespace over typographic weight. **`product-detail-label`** in `label-upper` (11px/700/uppercase/1.4px tracking) marks section headers like "COLOR," "SIZE," "DESCRIPTION." The spec table alternates a surface-soft background with 1px hairline row borders; key labels in muted gray, values in ink.

### Quantity Selector & Swatches
**`quantity-selector`** — Three-cell strip (minus / count / plus) with a 1px hairline border and square corners, 36px tall buttons. **`swatch-selector`** uses circular 32px chips (border-radius 9999px) with a 2px primary border on the active state — the only `{rounded.full}` element in the system, distinguishing color selection from the otherwise orthogonal geometry.

### Footer
**`footer`** — Dark ink (#222222) background with `label-upper` column headings in muted-off-white and body-sm links at #aaaaaa, hovering to teal. A second sub-footer row at #111111 carries legal copy at 12px. The dark footer provides contrast closure to a largely white, airy page above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav drawer; hero type drops to display-sm (22px); feature strip collapses to 2-column grid; sticky add-to-cart bar pins to bottom |
| Tablet | 744–1128px | 2-column product grid; nav links may truncate to icon+label or partial show; hero runs 2-column text+image layout |
| Desktop | 1128–1440px | 3-column product grid; full horizontal nav; hero at full 42px display-xl; feature strip runs single row |
| Wide | > 1440px | Max-width container (1440px) centered; side padding grows to `{spacing.xxl}`; product grid may expand to 4 columns |

### Touch Targets
- All buttons minimum 44px tall (text-input and button-primary at 44–48px)
- Swatch chips 32px with 8px gap — may need to grow to 40px on mobile
- Quantity selector buttons 36px wide × 44px tall on mobile
- Nav links in hamburger drawer padded to minimum 48px row height

### Collapsing Strategy
- Nav collapses to hamburger at < 744px; drawer slides in from left
- Feature callout strip reflows to 2×2 grid on mobile, single row on desktop
- Product detail: image gallery stacks above description on mobile, side-by-side on desktop (60/40 split)
- Footer columns stack vertically on mobile, 3–4 column grid on desktop
- Spec table stays full-width at all breakpoints; horizontal scroll if overflow on very narrow viewports

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font detected — Squarespace system font stack (Helvetica Neue → Roboto → Arial) is assumed; if the brand uses a licensed typeface loaded via @font-face, the typography tokens should be updated
- Many extracted hex values (#3b5998, #0063dc, #ea4c89, #007ee5, etc.) are recognizable social media platform colors from share buttons; they are not brand palette entries and have been excluded
- Meta theme-color is absent — primary teal inferred as the brand color from its distinctiveness in the extracted list, but no explicit brand color statement was found
- Exact button border-radius not confirmed from live extraction — square (0px) corners are inferred from the utilitarian office furniture category positioning
- No pricing tiers, sale mechanics, or promotional badge logic confirmed from extraction
- Animation and transition durations not captured — hover transitions assumed at 150–200ms ease standard Squarespace defaults
- Mobile navigation pattern (hamburger vs. collapsed tabs) not confirmed from static extraction
