---
version: alpha
name: "Artifact Uprising"
source_url: "https://www.artifactuprising.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every page defaults to a parchment canvas — #f4f2ed rather than white — so the brand declares its proximity to physical paper before a single product is visible. That warm off-white is not a background choice; it is the thesis: a screen surface that mimics the paper stock being sold. The primary CTA color, a muted coffee brown at #6e5b4f, is equally unusual for an e-commerce context; most DTC peers lean on blue or black for action buttons, but Artifact Uprising treats its call-to-action as another tonal element in a room-temperature palette rather than an interrupt. Crimson Pro handles all display weight — headlines arrive at 38–48px in regular or semibold, set with minimal negative tracking — while Acumin Pro governs navigation, labels, and body copy in tight all-caps or compact 14px runs, producing the serif-leads/sans-follows hierarchy of a well-designed photo book interior. Border-radius is nearly absent: product cards use {rounded.none} or a bare {rounded.xs}, so the imagery — open book spreads, unboxing sequences shot in low natural light — supplies all the softness without competing geometry. A pale sage wash, #e1f0ef, surfaces in callout bands and icon-background fields as the sole accent departure from warm-neutral; it reads like the endpaper color of a handmade album. The dark charcoal-teal #293234 anchors the footer and structural text, a color with enough green in it to feel organic rather than corporate. Grays stay warm: hairlines at #d2d2d0 rather than cool #cccccc. Section padding is generous — 64px between editorial rows — echoing the blank-page breathing room that defines the physical products. The blues surfacing in extracted data (#3377cc, #337ab7, #225ac9) are Bootstrap-default link and anchor colors unlikely to represent branded design choices; interactive energy in the brand's own UI runs entirely through the brown and charcoal registers. Label typography is set in Acumin Pro all-caps with wide letterSpacing (0.10–0.12em), treating product categorization the way a colophon handles edition information — present but subordinate to the image.

colors:
  primary: "#6e5b4f"
  primary-active: "#5a4840"
  primary-hover: "#7d6a5e"
  primary-disabled: "#c4b5ad"
  ink: "#1a1a1a"
  body: "#4f4f4f"
  muted: "#757575"
  muted-soft: "#959595"
  hairline: "#d2d2d0"
  hairline-soft: "#e1e1e1"
  canvas: "#f4f2ed"
  surface-soft: "#fefefe"
  surface-card: "#ffffff"
  surface-warm: "#f4f2ed"
  sage-wash: "#e1f0ef"
  ink-dark: "#293234"
  stone: "#8b9898"
  on-primary: "#fefefe"
  error: "#b33a2f"
  error-deep: "#cb0000"
  link: "#3377cc"

typography:
  display-xl:
    fontFamily: "'Crimson Pro', 'Crimson Text', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Crimson Pro', 'Crimson Text', Georgia, serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Crimson Pro', 'Crimson Text', Georgia, serif"
    fontSize: 30px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Crimson Pro', 'Crimson Text', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.32
    letterSpacing: 0
  editorial-pull:
    fontFamily: "'Crimson Pro', 'Crimson Text', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
    fontStyle: italic
  title-md:
    fontFamily: "'acumin-pro', Lato, 'Century Gothic', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'acumin-pro', Lato, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.04em
  body-md:
    fontFamily: "'acumin-pro', Lato, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'acumin-pro', Lato, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'acumin-pro', Lato, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  nav-link:
    fontFamily: "'acumin-pro', Lato, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.06em
  label-caps:
    fontFamily: "'acumin-pro', Lato, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'acumin-pro', Lato, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-lg:
    fontFamily: "'acumin-pro', Lato, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  price:
    fontFamily: "'acumin-pro', Lato, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-soft}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    hoverColor: "{colors.primary}"
    hoverDecoration: none
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.primary}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.editorial-pull}"
    bodyTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-lg}"
    paddingY: "{spacing.section}"
    imageOverlay: "rgba(244,242,237,0.25)"
    rounded: "{rounded.none}"
  editorial-band:
    backgroundColor: "{colors.sage-wash}"
    textColor: "{colors.ink-dark}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.stone}"
    paddingY: "{spacing.section}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.body}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.muted}"
    gap: "{spacing.sm}"
    padding: "{spacing.sm}"
  product-card-hover:
    imageScale: 1.02
    titleColor: "{colors.primary}"
  collection-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  category-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-caps}"
    marginBottom: "{spacing.xs}"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price}"
  price-original:
    textColor: "{colors.muted-soft}"
    typography: "{typography.price}"
    textDecoration: line-through
  price-sale:
    textColor: "{colors.error}"
    typography: "{typography.price}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    height: 44px
    padding: 0 16px
  testimonial-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    quoteTypography: "{typography.editorial-pull}"
    quoteColor: "{colors.ink-dark}"
    attributionTypography: "{typography.caption}"
    attributionColor: "{colors.muted}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  section-label:
    textColor: "{colors.stone}"
    typography: "{typography.label-caps}"
    marginBottom: "{spacing.lg}"
  divider:
    color: "{colors.hairline}"
    height: 1px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  image-caption:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    marginTop: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.ink-dark}"
    textColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.on-primary}"
    paddingY: "{spacing.section}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    marginBottom: "{spacing.md}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    height: 40px
    paddingX: "{spacing.base}"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 44px
    width: 100px
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "16px 0"
  accordion-body:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "0 0 16px 0"

## Components

### Buttons

**`button-primary`** — A square-cornered ({rounded.none}) block set in Acumin Pro all-caps at 14px with 0.10em tracking, filled in warm coffee brown (#6e5b4f) with off-white text. The sharp geometry echoes the cut edges of paper stock rather than the friendlier pill shapes common to lifestyle brands. Hover shifts to #7d6a5e; active presses to #5a4840; disabled desaturates to #c4b5ad while maintaining the same text color and corner treatment.

**`button-secondary`** — Transparent fill with a 1px #1a1a1a border and matching ink text, matching `button-primary` in height (48px) and typographic treatment. On hover, border and text shift to the brand brown (#6e5b4f) so the two button tiers share color language. Used for secondary product actions — "Save to wishlist," optional add-ons.

**`button-ghost`** — Same construction as `button-secondary` but border and label use {colors.primary} from the start, reserved for editorial CTAs within content bands where the ink border would read too heavy against a light or sage-wash background.

### Text Input

**`text-input`** — Flat rectangle with no border-radius, 1px {colors.hairline} stroke at rest, 1px {colors.primary} on focus. Background is near-white {colors.surface-soft} rather than pure white, keeping the form field warm against the parchment canvas. Placeholder text sits at {colors.muted-soft}. Height 48px matches button height for consistent inline row alignment.

### Navigation

**`nav-bar`** — 64px tall, canvas background with a single 1px hairline bottom border. Links are Acumin Pro 14px/500 with 0.06em letterSpacing — wide enough to read as considered, not so wide as to feel spaced out. No dropdown shadows; sub-menus open as flat overlays on the same parchment. Active links gain an underline in {colors.primary} rather than a filled background chip.

### Product Card

**`product-card`** — No border-radius. Image occupies a 4:5 aspect ratio container; on hover, image scales to 1.02× while the title color transitions to {colors.primary}. Below the image: a {typography.label-caps} category label in {colors.muted}, then the product name in {typography.title-md}, then the price in {typography.price}. No card elevation or drop shadow — the grid separation is spatial, not visual layering.

### Hero

**`hero`** — Full-width band on {colors.canvas} with 64px vertical padding. Headline in {typography.display-xl} (Crimson Pro 48px/400), followed by a subhead in {typography.editorial-pull} (22px italic Crimson Pro), then a {typography.body-md} paragraph, then a `button-primary`. Photography is overlaid with a semi-transparent warm wash (rgba 244,242,237 at 0.25 opacity) to ensure legibility without draining image warmth.

### Editorial Band

**`editorial-band`** — A full-width section using the pale sage {colors.sage-wash} as background, reserved for story-driven content: process descriptions, material sourcing callouts, or gift guides. Headline in {typography.display-md} (Crimson Pro 30px/600), body in {typography.body-md}, with a {typography.label-caps} section label in {colors.stone} above the headline as an entry point.

### Badges & Labels

**`collection-badge`** — Square-cornered tag with canvas fill and 1px hairline border, label in {typography.label-caps}. Used to annotate product format (Layflat, Softcover, Square). `sale-badge` uses the same geometry but fills with {colors.error} (#b33a2f) in white text, appearing inline with the price rather than overlaid on the image.

### Testimonial Card

**`testimonial-card`** — Flat card on {colors.surface-warm} with 1px hairline border and 32px padding. Quote text in {typography.editorial-pull} (Crimson Pro italic 22px), attribution in {typography.caption} at {colors.muted}. Cards tile horizontally in a three-column grid on desktop and stack on mobile.

### Footer

**`footer`** — Dark {colors.ink-dark} (#293234) footer with off-white hairline-soft text. Column headings in {typography.label-caps} with {colors.on-primary}; body links in {colors.hairline} lightening to full white on hover. 64px vertical padding maintains the brand's generous spatial rhythm even in the footer.

### Promo Banner

**`promo-banner`** — A slim 40px banner above the nav, filled with {colors.primary} and white text in {typography.label-caps}. Single-line messaging only: free shipping threshold, limited offer. No close button — it scrolls away with the page.

### Accordion

**`accordion-header`** / **`accordion-body`** — Used on product detail pages for materials, sizing, and care. Header is Acumin Pro 14px/600 in ink on canvas with a 1px hairline bottom border; no background color change on open. Body text is {typography.body-sm} in {colors.body}. No animation duration specified — defers to browser default for understated transition.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen overlay on canvas background; hero headline scales to display-md (30px); section padding reduces to spacing.xxl (48px); promo banner wraps to two lines at 36px tall |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links, dropdowns retained; hero switches to side-by-side image/text layout; editorial bands maintain full-width but body copy column narrows to 60% |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with sub-menus; hero at full 48px headline; section spacing at spacing.section (64px); testimonial cards in three-column row |
| Wide | > 1440px | Content max-width caps at 1440px with auto side margins; hero image bleeds edge-to-edge behind the content column; product grid stays at four columns with increased card gap |

### Touch Targets

- All interactive elements maintain a minimum 44px height (buttons, inputs, accordion headers, nav links)
- Product card tap target covers the full card surface, not just the title text
- Quantity selector (+/−) buttons are minimum 44×44px hit areas even though the visual component is narrower
- Nav hamburger icon expands to 48×48px tap area via padding

### Collapsing Strategy

- Navigation collapses to hamburger below 744px; the overlay uses full canvas background with nav links at display-sm scale for thumb-reach legibility
- Testimonial card rows collapse to single-column at mobile with full-width cards
- Footer columns (4 across on desktop) collapse to 2×2 on tablet and single-column stacked on mobile, with accordions optional for link groups
- Editorial bands maintain full-width at all breakpoints; internal copy column narrows proportionally
- Hero transitions from side-by-side (text left, image right) on desktop to stacked (image above, text below) on mobile, with image aspect ratio cropped to 16:9 at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-owned custom typeface confirmed; Crimson Pro/Crimson Text and Acumin Pro are inferred from font-family stacks but the actual font loading (webfont service, subsetting, weight axes) could not be verified
- Multiple blue values (#3377cc, #337ab7, #225ac9, #4990e2, #4a90e2) appear in extracted data; these are likely Bootstrap or third-party widget defaults rather than brand color choices — no blue has been used as a design token
- Meta theme-color not set; mobile browser chrome color is indeterminate
- Exact button border-radius on live site not confirmed — {rounded.none} is inferred from brand aesthetic rather than extracted CSS
- Animation and transition durations (hover fades, accordion open/close, cart drawer slide) not extractable from static snapshot
- Dark mode variant, if any, not observed
- Icon system (line vs. filled, stroke weight, grid size) not confirmed from extraction
- Exact grid column count and gutter widths not measured from live layout
