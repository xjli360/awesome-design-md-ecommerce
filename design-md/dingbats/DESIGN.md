---
version: alpha
name: "Dingbats*"
source_url: "https://www.dingbats-notebooks.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The asterisk after "Dingbats" isn't typographic whimsy — it marks the brand as something that demands a footnote, a product that earns its environmental claims through granular material disclosure rather than aspirational copy. The design system builds outward from a forest-floor palette: a deep forest teal (#108474) anchors every primary CTA and interactive state, while the canvas itself runs parchment-warm (#f7f5ef), closer to the first blank page of a new notebook than to clinical digital white. Lime (#adcd62) and golden yellow (#fbcd0a) read as cover-colour echoes — the same naturalistic pigments found in the physical product lineup reappear as accent tokens for badges, promotional strips, and sale signals, grounding the interface in the objects it sells. Dark forest (#1c3930) steps in for high-contrast display text and full-bleed hero and footer backgrounds, where the mid-tone teal would lose structural weight. A muted lavender (#a89cc8) surfaces occasionally as a tertiary accent, likely corresponding to a cover colourway brought into the UI.

  Typography leans on Poppins for display and headline work — a geometric sans that reads sharp without being sterile — with Nunito Sans handling body copy at comfortable reading sizes and generous 1.65 line-height. Both families carry enough warmth to avoid the cold minimalism that would fight the cream canvas. Barlow contributes uppercase label treatments for eco badges and filter chips, where tight tracking at small sizes aids legibility.

  Corners are softly rounded: `{rounded.sm}` (8px) on inputs and buttons, `{rounded.md}` (12px) on product cards, keeping the interface approachable without the pillow-softness that would undercut the brand's precision claims. Spacing follows a 4px base grid with generous section padding (64px) letting photography and cover colour breathe. Elevation is handled by hairline borders and surface-tint layering — no drop-shadow theatrics. The overall register is calm, unhurried, and oriented toward the physical world; the UI is a shop window, not a destination.

colors:
  primary: "#108474"
  primary-active: "#0c6558"
  primary-disabled: "#7ec2b9"
  accent-lime: "#adcd62"
  accent-gold: "#fbcd0a"
  forest-dark: "#1c3930"
  lavender: "#a89cc8"
  surface-teal-soft: "#c1e6e6"
  surface-teal-xsoft: "#edf5f5"
  ink: "#121212"
  body: "#555555"
  muted: "#7b7b7b"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#f7f5ef"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  label-upper:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Poppins', Arial, Helvetica, sans-serif"
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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 13px 23px
    height: 48px
  button-sm-accent:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 34px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.forest-dark}"
  announcement-bar:
    backgroundColor: "{colors.forest-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-strong}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    padding: "{spacing.md}"
    imageAspectRatio: "3/4"
    hoverBorderColor: "{colors.primary}"
  eco-badge:
    backgroundColor: "{colors.surface-teal-xsoft}"
    textColor: "{colors.primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.surface-teal-soft}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.forest-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 520px
    paddingX: "{spacing.section}"
  collection-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    height: 32px
  collection-filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: 6px 14px
    height: 32px
  notebook-cover-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  review-bar:
    starFillColor: "{colors.accent-gold}"
    starEmptyColor: "{colors.hairline}"
    typography: "{typography.caption}"
    ratingNumberTypography: "{typography.title-sm}"
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 52px
    width: "100%"
    hoverBackgroundColor: "{colors.primary-active}"
  footer:
    backgroundColor: "{colors.forest-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-teal-soft}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    paddingY: "{spacing.section}"

## Components

### Buttons
**`button-primary`** — Forest teal (#108474) fill on cream canvas, Poppins Semi-Bold 15px with 0.2px tracking, 48px height, `{rounded.sm}`. Active state deepens to #0c6558; disabled washes to #7ec2b9 with white text retained. This is the sole conversion-weight button: Add to Cart, Checkout, Subscribe, and primary collection CTAs all use this variant.

**`button-secondary`** — Transparent fill with a 1.5px teal border and teal text, matching the 48px height of primary for side-by-side pairing. Transitions to a faint teal surface tint on hover. Used for secondary CTAs such as "View Collection," "Explore Range," or "Learn More" where primary would compete.

**`button-ghost`** — Hairline-bordered, ink-coloured text, transparent fill, `{rounded.sm}`. Carries minimal visual weight for tertiary actions: Continue Shopping, wishlist toggles, and pagination links.

**`button-sm-accent`** — Compact 34px lime (#adcd62) variant with ink text and `{rounded.xs}`. Used on editorial collection cards or promotional strips where teal would compete with rich product photography. Lime reads as energetic without breaking the nature-palette logic.

### Text Input
**`text-input`** — Cream canvas background blends with the page surface; 1px hairline border at rest sharpens to a 1px teal focus ring matching primary. 48px height aligns with button height for clean inline search-plus-submit layouts. Placeholder text in muted grey (#7b7b7b); entered text in ink (#121212).

### Navigation
**`nav-bar`** — 64px tall, cream canvas, separated from content by a 1px soft hairline. Logo in forest dark (#1c3930) maximises contrast against the warm ground. Nav links at Poppins Medium 14px with `{spacing.lg}` gaps; no underline at rest, teal underline on hover. Cart, search, and account icons at 24px ink-coloured. On scroll the bar stays fixed and gains a subtle box-shadow rather than a colour change.

**`announcement-bar`** — A 36px forest-dark (#1c3930) strip pinned above the sticky nav. White caption-strong text carries rotating messages: free shipping thresholds, sustainability certifications, and seasonal campaigns. Sits above the nav z-layer; hidden on mobile to recover vertical space.

### Product Card
**`product-card`** — 3:4 portrait image ratio frames notebook covers at natural proportions. 1px hairline-soft border at rest transitions to a 1px teal border on hover with no scale transform, keeping focus on the cover art. Title in Poppins Semi-Bold 15px; price in Poppins Bold 18px below. Eco, sale, and new badges overlay the top-left corner of the product image. Notebook cover swatches appear below the title in a `{spacing.xs}`-gapped flex row, truncating beyond six with a "+N" caption-style link.

### Badges
**`eco-badge`** — Soft teal surface (#edf5f5) with teal text (#108474) and a 1px teal-soft border, Barlow uppercase 11px at 0.8px tracking. Applied to any product with recycled, FSC-certified, or vegan material claims — the most frequently appearing badge in the catalog.

**`sale-badge`** — Golden yellow (#fbcd0a) fill with ink text; high contrast against both cream and dark photography backgrounds. Uppercase Barlow label-upper type.

**`new-badge`** — Solid teal fill, white Barlow uppercase text. Applied sparingly to new collection arrivals to avoid devaluing the signal.

### Hero Banner
**`hero-banner`** — Forest dark (#1c3930) full-bleed background with product or lifestyle photography layered at reduced opacity or cropped to one side. Headline in Poppins Bold 48px white; sub-copy in Nunito Sans Regular 16px at 1.65 line-height, also white. Minimum 520px height on desktop. Primary CTA button sits `{spacing.md}` below the sub-copy. No decorative borders or gradients; the cover photography carries all the visual energy.

### Collection Filters
**`collection-filter-chip`** / **`collection-filter-chip-active`** — Pill-shaped `{rounded.full}` filter chips sort the catalog by notebook type, size, paper ruling, and cover theme. Inactive state: light grey surface with a hairline border and body-coloured caption-strong text. Active state: solid teal fill with white text, same border-radius and height (32px). Chips sit in a horizontally scrolling row on mobile, a wrapping flex row on desktop.

### Notebook Cover Swatch
**`notebook-cover-swatch`** — 32px circular swatch for in-page colour selection on product detail pages. Selected state gains a 2px ink ring offset by a 2px transparent gap (implemented via box-shadow ring), visually floating the ring away from the swatch fill colour. Swatches sit in a flex row with `{spacing.xs}` (4px) gaps; on touch viewports each swatch expands to 40px diameter for tap comfort.

### Review Bar
**`review-bar`** — Golden yellow (#fbcd0a) star fill against hairline-grey empty stars. Rating number in Poppins Semi-Bold 15px; review count in Nunito Sans caption. Powered by the JudgeMe widget; Dingbats* tokens applied via CSS variable overrides on `.jdgm` selectors to avoid custom widget development.

### Add to Cart
**`add-to-cart`** — Full-width 52px teal button, slightly taller than the standard 48px to assert hierarchy on the product detail page. Hover deepens to primary-active (#0c6558) with a 150ms ease transition. Disabled state uses primary-disabled (#7ec2b9). Sits sticky above the mobile safe area when the user scrolls past the standard button position.

### Footer
**`footer`** — Forest dark (#1c3930) full-bleed with white body text and surface-teal-soft (#c1e6e6) link colour for legibility against the dark background. Four-column layout on desktop: Shop, About, Sustainability, Contact. Column headings in Poppins Semi-Bold 15px; links in Nunito Sans 14px. Section padding 64px top and bottom. Social icons use white fill at 20px, not brand social colours — those are restricted to share-button overlays only.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-in drawer from left; hero headline scales to `{typography.display-md}` (28px); add-to-cart sticky to bottom safe area; filter chips scroll horizontally; announcement bar hidden |
| Tablet | 744–1128px | Two-column product grid; nav collapses to logo + icon row; hero min-height reduces to 380px; product card images at 3:4 ratio retained; announcement bar visible |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav bar with all links visible; announcement bar visible; hero at full 520px min-height; filter chips in wrapping flex row |
| Wide | > 1440px | Max content width 1440px centred with auto side margins; hero background full-bleed with constrained text column; four-column product grid maintained; footer four columns maintained |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Filter chips expand from 32px to 36px height on touch viewports
- Notebook cover swatches expand from 32px to 40px diameter on touch viewports
- Cart, search, and account nav icons padded to 44×44px tap zones with 24px visual icon
- Announcement bar links minimum 36px tap height

### Collapsing Strategy
- Primary nav collapses to hamburger at < 1024px; drawer slides from left, overlaying canvas with a 40% opacity forest-dark (#1c3930) scrim
- Announcement bar hidden at < 744px to recover vertical space
- Footer four columns collapse to two columns at tablet, then single accordion-expandable list at mobile
- Collection filter sidebar (if present on desktop) converts to a modal bottom sheet on mobile with a teal Apply button
- Cover swatch rows truncate beyond six swatches with a "+N more" text link in caption style

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Font weights not confirmed from CSS extraction — Poppins and Nunito Sans roles are identified but specific weight assignments (400/600/700) are inferred from common DTC stationery conventions, not extracted values
- Barlow appears in the font stack but its exact scope (badge labels, filter chips, or legacy copy) could not be confirmed from available hints; label-upper role is inferred
- Baskerville appears in the stack and likely serves editorial or blog body copy, but no specific rule set was extractable
- No button border-radius values extracted — `{rounded.sm}` (8px) inferred from visual conventions typical of eco/stationery Shopify stores at this price point
- Lavender (#a89cc8) appears in the extracted palette but specific usage (cover colourway accent, promo element, or legacy) could not be confirmed
- Social icon colours (#3b5998, #1da1f2, #dd4b39, #e60023, #0073b1) are third-party brand tokens from share widgets, not Dingbats* brand tokens, and are excluded from the palette
- Hover transition durations and easing curves not extractable from static hints — 150ms ease assumed for micro-interactions, 200ms ease for larger state changes
- Dark-mode palette not defined; site appears to be light-mode-only based on the warm cream theme-color
- Exact mega-menu or fly-out nav structure unconfirmed — slide-in drawer assumed from Shopify defaults
- Hero image treatment (full bleed, side-by-side, or overlay) could not be confirmed without live render; forest-dark background with overlaid photography is the most common pattern for this brand category
