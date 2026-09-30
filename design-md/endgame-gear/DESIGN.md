---
version: alpha
name: "Endgame Gear"
source_url: "https://www.endgamegear.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Chrome-yellow at #fdc415 — the meta theme-color itself, hardcoded to the <meta> tag as if declaring a brand registration — is the single warm frequency Endgame Gear allows into an otherwise near-black (#141414) world. The contrast is the visual thesis: a dark-room gaming monitor rendered in HTML, where yellow fires only on CTAs, hover states, and performance callouts, never softened into warmth or lifestyle friendliness. Deep navy (#003399) anchors the footer and secondary interactions; a saturated green (#6eb80f) marks competitive pricing and spec-tier achievements; hard red (#ec2913) signals scarcity or warnings — each used at full saturation against the dark canvas like indicator lights on a motherboard. The palette is diagnostic, not decorative. Type lives in two faces with distinct jurisdictions. Aguda-Regular carries display work, product names, specifications, and price numerals — a geometric, engineered face that gives the interface a custom hardware feel rather than an off-the-shelf storefront. Source Sans Pro Regular handles all body copy, nav links, UI labels, and badge text, providing legibility without softening the overall register. Button labels and badges run in uppercase Source Sans Pro at 700 weight with tracked letterSpacing, reinforcing the brand's preference for command-mode language over conversational copy. Corner radii stay tight at {rounded.xs} (4px) throughout interactive surfaces — product cards, inputs, badges, buttons — resisting the pill-friendly roundness of consumer lifestyle brands. Product cards sit on the #141414 canvas with a full-bleed product image and a 2px yellow border on hover, the same selection signal echoed in gallery thumbnails and category tabs. Award certification chips in yellow (#fdc415), green sale percentages, and red scarcity flags stack in card corners as a unified badge system differentiated only by voltage color. The footer drops to a full-width navy (#003399) block — the only large-area color besides hero photography — with white type and yellow link hovers. The experience reads like a product specification sheet that also sells.

colors:
  primary: "#fdc415"
  primary-active: "#fdca2c"
  primary-disabled: "#fdd044"
  primary-muted: "#fff3cd"
  on-primary: "#141414"
  accent-blue: "#003399"
  accent-blue-bright: "#0d6efd"
  accent-green: "#6eb80f"
  accent-green-mid: "#7dbf27"
  accent-red: "#ec2913"
  ink: "#141414"
  ink-inverse: "#ffffff"
  body: "#373b3e"
  muted: "#cbccce"
  hairline: "#dfe0e1"
  canvas: "#ffffff"
  canvas-dark: "#141414"
  surface-soft: "#ededed"
  surface-card: "#ffffff"
  navy-footer: "#003399"
  gold-dark: "#654e08"

typography:
  display-xl:
    fontFamily: "'Aguda-Regular', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Aguda-Regular', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Aguda-Regular', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Source-Sans-Pro-Regular', 'Source Sans Pro', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Source-Sans-Pro-Regular', 'Source Sans Pro', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Source-Sans-Pro-Regular', 'Source Sans Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source-Sans-Pro-Regular', 'Source Sans Pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Source-Sans-Pro-Regular', 'Source Sans Pro', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label-caps:
    fontFamily: "'Source-Sans-Pro-Regular', 'Source Sans Pro', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Source-Sans-Pro-Regular', 'Source Sans Pro', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Source-Sans-Pro-Regular', 'Source Sans Pro', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Source-Sans-Pro-Regular', 'Source Sans Pro', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  spec-value:
    fontFamily: "'Aguda-Regular', sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0
  price-display:
    fontFamily: "'Aguda-Regular', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.1
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
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
    opacity: 0.6
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.ink-inverse}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.ink-inverse}"
    hoverBorderColor: "{colors.primary}"
    hoverTextColor: "{colors.primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.ink-inverse}"
    typography: "{typography.nav-link}"
    height: 64px
    accentColor: "{colors.primary}"
    linkHoverColor: "{colors.primary}"
    logoFont: "{typography.display-sm}"
  hero-banner:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.ink-inverse}"
    headlineFont: "{typography.display-xl}"
    subFont: "{typography.body-md}"
    ctaColor: "{colors.primary}"
    minHeight: 560px
    imageOverlayOpacity: 0.4
  product-card:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.ink-inverse}"
    titleFont: "{typography.title-sm}"
    priceFont: "{typography.price-display}"
    captionFont: "{typography.caption}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "1/1"
    hoverBorderColor: "{colors.primary}"
    hoverBorderWidth: 2px
    padding: "{spacing.md}"
  spec-badge:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.muted}"
    valueColor: "{colors.ink-inverse}"
    valueFont: "{typography.spec-value}"
    labelFont: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  award-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  sale-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink-inverse}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  scarcity-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.ink-inverse}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px
    iconColor: "{colors.body}"
    focusBorderColor: "{colors.primary}"
    focusBorderWidth: 1px
  product-gallery:
    backgroundColor: "{colors.canvas-dark}"
    thumbnailBorderColor: "{colors.hairline}"
    activeThumbnailBorderColor: "{colors.primary}"
    activeThumbnailBorderWidth: 2px
    thumbnailRounded: "{rounded.xs}"
  performance-chip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  category-tab:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    activeBorderColor: "{colors.primary}"
    activeBorderWidth: 2px
    activeBorderPosition: bottom
  comparison-table:
    headerBackgroundColor: "{colors.canvas-dark}"
    headerTextColor: "{colors.ink-inverse}"
    rowBackgroundColor: "{colors.surface-card}"
    alternateRowColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    recommendedAccentColor: "{colors.primary}"
    recommendedBorderWidth: 2px
    headerFont: "{typography.title-sm}"
    bodyFont: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.navy-footer}"
    textColor: "{colors.ink-inverse}"
    linkColor: "{colors.ink-inverse}"
    linkHoverColor: "{colors.primary}"
    headingFont: "{typography.title-sm}"
    bodyFont: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
    newsletterInputBorderColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — Chrome-yellow (#fdc415) fill with near-black (#141414) text, {rounded.xs} radius (4px), and uppercase Source Sans Pro at 15px/700 weight with 0.5px letter-spacing. Hover transitions to `primary-active` (#fdca2c); disabled state softens to `primary-disabled` (#fdd044) at reduced opacity. The all-caps treatment reads as a command — "ADD TO CART," "BUY NOW" — rather than an invitation.

**`button-secondary`** — Transparent background with #141414 text and a 1px `{colors.hairline}` border; on dark-canvas sections the `button-secondary-dark` variant reverses to white text, white border, and a yellow hover state for both text and border. Shares the uppercase button-md typography and {rounded.xs} radius. Used for "Learn More," "Compare," and "View All" actions.

**`button-ghost`** — Text-only, no border, no fill. Yellow (#fdc415) label in uppercase button-sm. Used inline in product description blocks and spec panels for low-hierarchy actions such as "Download Full Specs" or "See All Sensors."

### Navigation
**`nav-bar`** — Full-width dark bar (#141414) at 64px height. The logo renders in Aguda-Regular display-sm (24px) with the yellow #fdc415 accent mark. Nav links are Source Sans Pro 600/15px in white, shifting to yellow on hover with no underline. Product category dropdowns (Mice, Mousepads, Keyboards, Headsets) open as mega-menu panels inheriting the dark background. On mobile, a white hamburger icon opens a full-viewport-height drawer with the same dark fill and accordion category structure.

### Product Card
**`product-card`** — Dark canvas (#141414) card with a full-bleed product image at 1:1 aspect ratio, 4px rounded corners. Product name in title-sm (Source Sans Pro 600/16px, white), price in price-display (Aguda-Regular 28px, white). On hover, a 2px yellow (#fdc415) border wraps the card perimeter — the primary interactive selection signal, consistent with gallery thumbnails and category tabs. No drop shadows; depth is implied by the dark background against the page canvas. Award, sale, and scarcity badges stack in the card's top-left corner.

### Hero Banner
**`hero-banner`** — Full-viewport-width dark section (minimum 560px height) with product photography as a background or right-side panel. Headline in display-xl Aguda-Regular (48px, white), sub-copy in body-md Source Sans Pro. A 0.4 opacity scrim over background images keeps white text legible. A row of `spec-badge` tiles below the headline displays sensor model, DPI ceiling, weight, and polling rate at a glance. The primary CTA renders as a `button-primary` in yellow below the spec row.

### Spec Badge
**`spec-badge`** — Dark (#141414) tile with a label-caps uppercase muted label above a spec-value numeral in Aguda-Regular (22px, white). Used in horizontal rows beneath product headlines to display DPI, IPS, weight (grams), and polling rate (Hz). The Aguda-Regular numeral anchors the spec visually against the Source Sans Pro label, creating a clear two-tier hierarchy that reads like a technical datasheet.

### Award / Sale / Scarcity Badges
**`award-badge`** — Yellow (#fdc415) chip with #141414 uppercase label-caps text; carries editorial designations like "GAME CHANGER" or "EDITOR'S CHOICE." **`sale-badge`** uses brand green (#6eb80f) for percentage-off callouts. **`scarcity-badge`** uses hard red (#ec2913) for "LOW STOCK" or countdown-driven urgency. All three share {rounded.xs} corners and label-caps typography — the badge system is unified in structure, differentiated only by voltage color.

### Search Bar
**`search-bar`** — Soft-surface (#ededed) field at 40px height with {rounded.xs} corners, muted placeholder text, and a search icon in body-gray (#373b3e). Focus adds a 1px yellow (#fdc415) border. On desktop it sits in the nav at constrained width; on mobile it expands to a full-width overlay with a close icon.

### Product Gallery
**`product-gallery`** — Main image against the dark canvas (#141414); thumbnail strip below with 1px hairline borders at rest. The active thumbnail switches to a 2px yellow (#fdc415) border — carrying the same yellow-as-selection language used on product cards and category tabs across the entire browsing surface.

### Performance Chip
**`performance-chip`** — Yellow (#fdc415) {rounded.xs} chip with #141414 uppercase label-caps text. Used in hero sections and collection banners to flag sensor models ("PAW3395"), polling rates ("8000Hz POLLING"), or certifications. Distinct from `award-badge` in that it describes a technical property rather than an editorial accolade.

### Comparison Table
**`comparison-table`** — Header row in dark canvas (#141414) with white Aguda-label text. Data rows alternate between white (#ffffff) and surface-soft (#ededed). The recommended model column receives a 2px yellow left border to mark the brand-preferred choice without disrupting row legibility. Spec values in body-sm Source Sans Pro; model names in title-sm. On mobile the table gains horizontal scroll with the first column (model name) sticky.

### Category Tab
**`category-tab`** — Horizontal filter strip for collection pages (All, Wired, Wireless, Large, Medium, Small). Inactive tabs in muted (#cbccce) Source Sans Pro 600/16px; active tab in yellow (#fdc415) with a 2px yellow bottom-border underline. Background remains transparent, allowing the page canvas to show through.

### Footer
**`footer`** — Full-width deep navy (#003399) block. Section headings in title-sm Source Sans Pro 600/white; link lists in body-sm Source Sans Pro 400/white. Link hover color is yellow (#fdc415), carrying the primary interaction color into the footer. Newsletter input uses a `text-input` with a yellow `button-primary` inline to its right. Social icons are white at rest, shift to yellow on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav drawer, search expands to full overlay, hero headline drops to display-md (32px), spec-badge row scrolls horizontally with snap |
| Tablet | 744–1128px | 2-column product grid, nav collapses to icon+label, hero splits to side-by-side layout, comparison table horizontally scrollable |
| Desktop | 1128–1440px | 3–4 column product grid, full mega-menu nav, hero at full 560px min-height, spec-badge row inline beneath headline |
| Wide | > 1440px | Content capped at ~1400px max-width centered; hero background image expands full-bleed but text column stays within container; product grid stays 4-column |

### Touch Targets
- All interactive elements minimum 44×44px (buttons, inputs, gallery thumbnails, nav hamburger)
- Product card entire surface tappable on mobile; no isolated sub-element links
- Spec-badge chips in horizontal scroll rows carry 12px horizontal padding between items to prevent mis-taps
- Badge chips in card corners are non-interactive decorations; tap target is the full card

### Collapsing Strategy
- Nav mega-menus become full-screen drawer with accordion category sections on mobile
- Hero spec-badge row switches from inline grid to horizontal scroll-snap on mobile
- Comparison table gains horizontal scroll with model-name column sticky at mobile breakpoint
- Footer collapses from 4-column to 2-column at tablet, single-column at mobile; newsletter row stacks vertically
- Product gallery thumbnail strip switches to dot-indicator pagination on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Aguda-Regular is a proprietary or licensed typeface; only the Regular cut is confirmed from the font-family stack — bold and light weights assumed unavailable or non-existent in this face
- Source-Sans-Pro-Regular is the only confirmed body cut; italic and semibold weights assumed from the standard Source Sans Pro family but not confirmed via extraction
- #0d6efd in the extracted palette is Bootstrap's default link color and likely bleeds through from a framework default; intentional brand usage as a standalone token is unconfirmed — assigned to `accent-blue-bright` but treat as provisional
- Box-shadow values, elevation layers, and transition timing curves are not capturable from hex/font extraction — recommend 150ms ease-out as a default for snappy gaming-context interactions
- Exact grid gutter widths and max-content-width breakpoints not confirmed; 1400px max-width and 24px gutters recommended as defaults
- Mobile navigation drawer behavior (slide-in from left vs. full-overlay fade) not confirmed from extraction
- Form validation error/success token styling beyond `accent-red` is inferred from Bootstrap palette bleed-through; brand-custom states not confirmed
- Product image background treatment (pure black vs. subtle gradient or texture) not determinable from color extraction alone
