---
version: alpha
name: "Ugmonk"
source_url: "https://ugmonk.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Two temperatures define the Ugmonk surface — a warm near-ivory (#fafaf2, #f8f6f1) that reads like uncoated stock under diffuse light, and a dark olive-black (#2d2f24) that anchors both deepest ink and primary CTAs, sitting closer to a forest-floor green than true black when examined at high contrast. GTPressuraMonoLight, the geometric monospace pulled directly from the live font stack, carries display headings and product names; it projects an instrument-quality editorial gravity that Avenir Next — handling body copy and navigation — alone would not achieve. The golden amber pair (#ffd879, #ffd160) arrives with restraint: highlight accents, warm badge washes on product chips, and hover-state emphasis rather than dominant CTA color. Corners on cards and buttons are sharp ({rounded.none}) to minimally soft ({rounded.sm}), deferring entirely to the objects being framed rather than asserting brand softness through geometry. Section cadence is wide — photography bleeds to the grid edge, a single product claims a full-bleed viewport slice, and negative space carries the structural load while the chrome stays minimal. The dark panel variant (#1a1a1a, #121212) surfaces in footer sections and hero inversions, framing warm-toned product photography against a backdrop closer to a gallery wall than a tech storefront. This combination — warm parchment against olive-black with amber as the single accent frequency — maps precisely to the Analog index-card productivity system and walnut desk trays that Ugmonk is built around: objects designed to be placed on a desk and stopped thinking about, in the best sense of the phrase.

colors:
  primary: "#2d2f24"
  primary-active: "#1a1a1a"
  primary-disabled: "#8a8c80"
  accent: "#ffd879"
  accent-deep: "#ffd160"
  accent-soft: "#faefc2"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#5a5a5a"
  mid: "#404040"
  hairline: "#dedede"
  canvas: "#fafaf2"
  surface-soft: "#f8f6f1"
  surface-card: "#fcfcfc"
  dark-panel: "#1a1a1a"
  dark-panel-raised: "#262626"
  on-primary: "#fafaf2"
  on-accent: "#2d2f24"
  on-dark: "#fafaf2"

typography:
  display-xl:
    fontFamily: "'GTPressuraMonoLight', 'Andale Mono WT', 'Andale Mono', 'Courier New', monospace"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'GTPressuraMonoLight', 'Andale Mono WT', 'Andale Mono', monospace"
    fontSize: 34px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'GTPressuraMonoLight', 'Andale Mono WT', 'Andale Mono', monospace"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  price-display:
    fontFamily: "'GTPressuraMonoLight', 'Andale Mono WT', 'Andale Mono', monospace"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  mono-label:
    fontFamily: "'GTPressuraMonoLight', 'Andale Mono WT', 'Andale Mono', monospace"
    fontSize: 11px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.04em
    textTransform: uppercase
  section-eyebrow:
    fontFamily: "'Avenir Next', Avenir, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.14em
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
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
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
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
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageRounded: "{rounded.none}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    hoverShadow: "0 4px 20px rgba(0,0,0,0.08)"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.section-eyebrow}"
    eyebrowColor: "{colors.muted}"
    ctaMarginTop: "{spacing.xl}"
    paddingY: "{spacing.section}"
  hero-dark:
    backgroundColor: "{colors.dark-panel}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.section-eyebrow}"
    eyebrowColor: "{colors.muted}"
    paddingY: "{spacing.section}"
  product-badge:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.on-accent}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.section-eyebrow}"
    eyebrowColor: "{colors.muted}"
    paddingY: "{spacing.section}"
  section-eyebrow-label:
    textColor: "{colors.muted}"
    typography: "{typography.section-eyebrow}"
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  compare-price:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textDecoration: line-through
  analog-callout:
    backgroundColor: "{colors.accent-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.xxl}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    accentBorder: "3px solid {colors.accent}"
  footer:
    backgroundColor: "{colors.dark-panel}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted}"
    headingTypography: "{typography.mono-label}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.dark-panel-raised}"
    paddingY: "{spacing.section}"
  image-caption:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 40px
  tag-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.mid}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  tag-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.mono-label}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  testimonial-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    quoteTypography: "{typography.display-sm}"
    attributionTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — A sharp-cornered ({rounded.none}) dark olive (#2d2f24) block at 48px tall with uppercase letter-spaced labels at 13px. The hover/active state deepens to near-black (#1a1a1a); disabled state uses the desaturated olive (#8a8c80) with no opacity trick. Horizontal padding is generous (32px each side) to maintain the quiet weight the brand uses for all primary actions: "Add to Cart", "Shop Now", "Learn More".

**`button-secondary`** — Same geometry as primary but inverted: transparent fill with a 1px olive border. Used for secondary product actions, newsletter opt-outs, and navigation-adjacent CTAs where the dark primary would compete with photography.

**`button-accent`** — The amber (#ffd879) filled variant with olive text (#2d2f24), reserved for limited-edition launches, the Analog system introductory CTA, or seasonal promotion moments. Its appearance is rare and therefore carries signal weight.

**`button-ghost-dark`** — White-bordered transparent button for use on dark-panel (#1a1a1a) hero sections. Appears in inverted hero and footer CTA contexts.

### Text Input

**`text-input`** — Sharp corners, 1px hairline border (#dedede), transitions to a 1px olive focus ring on activation. Height 48px, matching the primary button height so inline form rows align without vertical adjustment. Used in newsletter capture modules and checkout fields.

### Navigation

**`nav-bar`** — 60px tall on the warm ivory canvas (#fafaf2), with a hairline-weight border-bottom (#dedede) separating it from the page. Navigation links sit at 14px Avenir Next, 0.02em tracked. The logo treatment uses the mono display type at small scale. Cart icon and account links right-aligned. No megamenu — Ugmonk's category depth is shallow enough for a flat link list.

### Product Card

**`product-card`** — No border radius anywhere. The product image occupies the full card width flush to the edge; title in Avenir Next 500 at 15px, price in GTPressuraMonoLight at 18px. A compare-at price in muted (#5a5a5a) with strikethrough appears when items are on sale. Hover state lifts the card with a soft diffuse shadow (0 4px 20px rgba(0,0,0,0.08)) rather than any border or color change, preserving the flat aesthetic until interaction occurs.

### Hero Sections

**`hero`** — Full-bleed, warm ivory background with headlines in GTPressuraMonoLight at 52px. An uppercase eyebrow label in Avenir Next 11px at 0.14em tracking precedes the headline. Body copy at 16px Avenir Next. CTA button (button-primary or button-accent) follows with 32px top margin. Designed for single-product launches and the Analog system introduction.

**`hero-dark`** — Same structure swapped to the dark panel (#1a1a1a). Text shifts to on-dark (#fafaf2). Used for seasonal launches, limited-edition colorways, or the homepage above-fold when product imagery is light-toned and needs a dark surround.

### Callouts & Badges

**`product-badge`** — A sharp rectangular chip in warm amber wash (#faefc2) with olive text, using the mono-label type at 11px uppercase. Labels include "New", "Limited", "Analog" — appears top-left on product card images.

**`analog-callout`** — A section-spanning block in the warm amber wash (#faefc2) with a 3px solid amber (#ffd879) left border accent. Display-sm mono headline + body-md prose. Used to introduce the Analog card system with a persistent warm-toned anchor that distinguishes it from standard product grid sections.

**`section-eyebrow-label`** — Uppercase 11px Avenir Next at 0.14em tracking in muted gray (#5a5a5a). Precedes every section headline across the site. Acts as a wayfinding label: "Desk Setup", "The Analog System", "New Arrivals".

**`tag-chip` / `tag-chip-active`** — Used in collection filter rows. Inactive chips sit on surface-soft (#f8f6f1) in mid gray (#404040); active state inverts to the dark olive primary with ivory text. No radius, same rectangular geometry as all buttons.

### Commerce

**`price-tag`** — GTPressuraMonoLight 18px on its own line below the product title. The monospace rendering aligns decimal points in grid layouts without additional column tricks.

**`compare-price`** — Muted gray (#5a5a5a) Avenir Next 14px with line-through decoration, displayed inline alongside or beneath the current price when sale pricing applies.

**`quantity-selector`** — 40px tall, sharp corners, hairline border, plain Avenir Next body. Minus/plus controls are text glyphs rather than icon SVGs. Sits immediately above the add-to-cart button in the product detail layout.

### Testimonial & Social Proof

**`testimonial-block`** — Surface-soft (#f8f6f1) panel with the quote in GTPressuraMonoLight display-sm. Attribution line in caption-sized Avenir Next. No quotation mark decorations — the mono type already reads as a pulled quote. Used in single-product feature pages for the Analog system and Gather desk organizer.

### Footer

**`footer`** — Dark panel (#1a1a1a) with section headings in mono-label uppercase (11px GTPressuraMonoLight), body links in body-sm Avenir Next in muted (#5a5a5a). A 1px raised-dark border-top (#262626) separates it from the last page section. Column layout: 4 columns on desktop, 2 on tablet, stacked on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to display-sm (24px); nav collapses to hamburger with slide-in drawer; section padding reduces to spacing.xl (32px); product cards full-width; quantity selector and add-to-cart stack vertically |
| Tablet | 744–1128px | 2-column product grid; hero remains display-md (34px); nav links visible but compressed; analog-callout padding reduces to spacing.xl; footer collapses to 2-column |
| Desktop | 1128–1440px | 3-column product grid; full nav; hero at display-xl (52px); analog-callout at full xxl padding; footer 4-column |
| Wide | > 1440px | Max-width container (~1320px) centered; grid gutters widen; hero photography bleeds full viewport width while text stays in container; no scaling of type beyond desktop values |

### Touch Targets

- All buttons minimum 48px tall (matching defined height tokens)
- Quantity selector 40px tall — borderline; pad tap area with invisible 8px extension on mobile
- Navigation links minimum 44px tap height via line-height inflation on mobile drawer
- Product cards: full-card tap area, not just title/image region
- Tag-chip filters: minimum 36px height on mobile, 8px vertical padding floor

### Collapsing Strategy

- Navigation: flat link list on desktop → hamburger drawer on mobile; cart icon always visible
- Product grid: 3-col → 2-col → 1-col at tablet and mobile breakpoints
- Analog callout: side-by-side text/image → stacked text-above-image on mobile
- Footer: 4-col → 2-col → 1-col; column heads become accordion toggles on mobile
- Hero: full-bleed photography with text overlay on desktop → image-above, text-below stacked layout on mobile with reduced headline size
- Section eyebrow labels remain visible at all breakpoints — they are structural, not decorative

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- GTPressuraMonoLight weight and variant availability not confirmed beyond the font-family stack declaration — no @font-face or CDN URL extracted; exact weight integer (300 assumed from "Light") should be verified against loaded font files
- Avenir Next variant weights (400, 500, 600, 700) in use across the site not fully enumerated; only 400 and 500 confirmed as likely from extracted stack
- #112233 (dark navy) appears in the extracted color palette but its role is ambiguous — likely a Shopify-injected color (admin bar, payment icon, or iframe element) rather than a brand color; excluded from the design system
- Button border-radius values are approximated as 0px (none) based on brand aesthetic analysis; no CSS custom properties or computed values were extracted to confirm
- Hover and focus state colors for links and navigation items not confirmed beyond inference
- Dark mode or theme toggle support unknown — site appears to be light-only but no definitive evidence
- Exact product card image aspect ratio (likely 1:1 or 4:3) not extractable from palette/font hints; verify against live grid
- Specific collection filter UI (sidebar vs. inline chips vs. dropdown) not confirmed from available extraction data
- Animation/transition timing values (easing curves, durations for hover states, drawer open) not available from static extraction
