---
version: alpha
name: "Aardvark Jewellery"
source_url: "https://www.aardvarkjewellery.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The name arrives before the aesthetic does — Aardvark, the first animal alphabetically, chosen for a studio handcrafting engagement rings, signals that this brand leads with personality rather than prestige. Its primary voltage is #7d3cff, a saturated violet that most bridal boutiques would classify as too digital and too confrontational; Aardvark anchors every CTA, interactive focus ring, and hover state in it without apology. Against a canvas carrying the faintest purple undertone (#fbfbfb and #fbf9ff), the interface reads simultaneously romantic and graphic — a maker's studio that knows exactly which century it lives in.

  Display headlines run in marlide-display-variable, a calligraphic variable-axis font whose flowing stroke geometry echoes the organic forms of hand-forged bands without collapsing into overt script sentiment. Body copy runs in Lora — a serif whose ink-trap geometry and bracketed strokes suit a craftsperson comfortable with the weight of traditional materials. Together the type pair spans from editorial hero sweep to practical four-column ring-size charts without tonal inconsistency. Navigation and UI labels fall back to Arial for precision readability at small sizes.

  The palette beyond the core purple is deliberately generous for a bridal category: hot pink at #ff438e and #ff1070 for promotional surfaces, warm cream at #fbeed5 and soft gold at #ffcc66 that reference precious metal warmth without mimicking it, mint green at #71dc99 for success and sustainability moments, and a near-black navy at #2b333f that grounds the entire ink scale. Error and urgency states borrow #cc0000 and the deep rose cluster (#dc0058, #a90044). Spacing breathes at {spacing.section} between content blocks — unusual generosity for a bridal e-commerce context. Individual ring cards carry {rounded.md} corners, soft enough to suggest craft provenance, precise enough to read as a curated gallery. Primary buttons favour {rounded.sm} — direct and functional. Pill-shaped secondary actions at {rounded.full} handle softer navigation like "Browse by metal" or "Book a consultation." Every form input transitions its border from the neutral hairline slate (#73859f) to full primary purple on focus, binding every interaction back to the brand's single chromatic commitment.

colors:
  primary: "#7d3cff"
  primary-active: "#6020d0"
  primary-disabled: "#9f6fff"
  primary-light: "#fbf9ff"
  accent-pink: "#ff438e"
  accent-pink-strong: "#ff1070"
  accent-gold: "#ffcc66"
  accent-cream: "#fbeed5"
  accent-mint: "#71dc99"
  accent-yellow: "#fef94a"
  sale-badge: "#dc0058"
  sale-badge-deep: "#a90044"
  ink: "#2b333f"
  body: "#494949"
  muted: "#888888"
  hairline: "#73859f"
  hairline-soft: "#90a0b3"
  canvas: "#fbfbfb"
  surface-soft: "#f3f3f3"
  surface-card: "#fbf9ff"
  surface-cream: "#fbeed5"
  on-primary: "#ffffff"
  error: "#cc0000"
  success: "#399d14"

typography:
  display-xl:
    fontFamily: "'marlide-display-variable', 'Lora', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'marlide-display-variable', 'Lora', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'marlide-display-variable', 'Lora', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.02em
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  eyebrow:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.15em
    textTransform: uppercase
  price-display:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
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
    states:
      hover: "backgroundColor {colors.primary-active}"
      disabled: "backgroundColor {colors.primary-disabled}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
    states:
      hover: "backgroundColor {colors.primary-light}"
  button-pill:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
    height: 36px
    states:
      selected: "backgroundColor {colors.primary}, textColor {colors.on-primary}, border none"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.surface-soft}"
    logoTypography: "{typography.display-sm}"
    activeLinkColor: "{colors.primary}"
    activeLinkDecoration: "underline 2px {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    imageAspectRatio: "4/5"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    badgePosition: "top-left, offset {spacing.sm}"
    hoverEffect: "image scale 1.04, shadow 0 8px 24px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
    ctaGap: "{spacing.sm}"
    minHeight: 580px
    layout: "asymmetric 45/55 text/image split"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    linkColor: "{colors.accent-yellow}"
    linkHoverColor: "{colors.canvas}"
  gemstone-badge:
    backgroundColor: "{colors.accent-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    border: "1px solid {colors.hairline-soft}"
  sale-badge:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  ring-filter-bar:
    backgroundColor: "{colors.surface-soft}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    gap: "{spacing.sm}"
    padding: "{spacing.sm} {spacing.base}"
    activePillBackgroundColor: "{colors.primary}"
    activePillTextColor: "{colors.on-primary}"
    activePillRounded: "{rounded.full}"
    inactivePillTextColor: "{colors.body}"
  consultation-cta:
    backgroundColor: "{colors.accent-cream}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
    borderLeft: "4px solid {colors.primary}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    accentBorderLeft: "3px solid {colors.primary}"
  product-gallery:
    mainImageRounded: "{rounded.md}"
    thumbnailBorder: "2px solid transparent"
    thumbnailBorderActive: "2px solid {colors.primary}"
    thumbnailRounded: "{rounded.xs}"
    thumbnailSize: 72px
    thumbnailGap: "{spacing.xs}"
    zoomButtonBackground: "rgba(0,0,0,0.35)"
    zoomButtonColor: "{colors.on-primary}"
    zoomButtonRounded: "{rounded.full}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.eyebrow}"
    paddingY: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Vivid purple (#7d3cff) fill with white text at {typography.button-md} uppercase tracking, 48px tall, {rounded.sm} corners. Hover deepens to #6020d0; disabled retreats to the lighter #9f6fff. Used for all primary purchase actions: "Add to Bag," "View Ring," "Book Appointment."

**`button-secondary`** — Transparent background with a 2px purple border and primary-coloured label. Hover fills the surface with the purple-tinted {colors.primary-light}. Pairs with the primary button in two-CTA hero rows and on the consultation section.

**`button-pill`** — {rounded.full} pill at 36px height for filter and sort selections (metal type, stone, shape, price range). Resting state carries a 1px hairline border; selected state fills with {colors.primary}, inverts the label to white. {typography.button-sm} uppercase throughout.

### Text Input

**`text-input`** — 48px tall, {rounded.sm}, slate-blue hairline border (#73859f) that converts to a 2px solid primary purple on focus. Placeholder text in {colors.muted}. Body text uses {typography.body-md} Lora for consistency with the surrounding editorial type. Applies across the search overlay, ring enquiry forms, and ring-size calculators.

### Navigation

**`nav-bar`** — 72px tall on {colors.canvas} with a thin {colors.surface-soft} bottom separator. The studio name renders in {typography.display-sm} marlide-display-variable. Nav links in {typography.nav-link} Arial; current-page link gains a 2px underline in {colors.primary}. Announcement bar sits above the nav, purple-filled, carrying site-wide promotions in {typography.caption} white with yellow links.

### Product Card

**`product-card`** — Portrait 4:5 ring photograph with {rounded.md} corners, scaling to 1.04 with a soft shadow on hover. Title in {typography.title-sm} Lora; price in {typography.price-display} Lora. Gemstone, sale, or new badges overlay the top-left corner of the image with {spacing.sm} inset. Clicking anywhere on the card navigates to the product detail page.

### Hero Banner

**`hero-banner`** — Asymmetric split layout (roughly 45/55 text/image) at minimum 580px height. An eyebrow label in {typography.eyebrow} uppercase purple precedes the main headline in {typography.display-xl} marlide-display-variable. Supporting copy in {typography.body-md} Lora. Two-button CTA row — primary plus secondary — sits below the subhead with {spacing.sm} gap between buttons.

### Announcement Bar

**`announcement-bar`** — A 40px {colors.primary} strip pinned above the nav. Promotional copy renders in {typography.caption} white. Inline links use {colors.accent-yellow} (#fef94a) for contrast and warmth — the brand's brightest accent colour, deployed sparingly for maximum legibility on the purple ground.

### Gemstone & Status Badges

**`gemstone-badge`** — Warm cream background ({colors.accent-cream}) with a hairline border in {colors.hairline-soft}; used to label stone type (diamond, sapphire, moissanite) on product cards and detail pages. {rounded.xs} keeps it compact. `sale-badge` mirrors the geometry in deep rose ({colors.sale-badge} #dc0058); `new-badge` uses the primary purple — same shape, three distinct signals.

### Ring Filter Bar

**`ring-filter-bar`** — A {colors.surface-soft} tray with {rounded.sm} containing a horizontal run of {typography.caption} filter pills. Each inactive pill sits flush in the tray background; selected pills fill with {colors.primary} in {rounded.full} shape, inverting the label. Handles metal, stone, shape, and price-range filters on collection listing pages.

### Consultation CTA

**`consultation-cta`** — Warm cream panel ({colors.accent-cream}) with a 4px left border accent in {colors.primary}. The headline uses {typography.display-sm} marlide-display-variable; body copy uses {typography.body-md} Lora. {rounded.md} on the card and {spacing.xxl} internal padding give it visual weight without competing with the product photography. Appears at the foot of most collection and about pages.

### Testimonial Card

**`testimonial-card`** — {colors.surface-card} background (the barely-purple off-white) with {rounded.md} and {spacing.xl} padding. Quote in {typography.body-md} Lora italic; author attribution in {typography.caption} uppercase Arial with {colors.muted} tone. A 3px left-edge rule in {colors.primary} visually groups the card within a testimonial grid.

### Product Gallery

**`product-gallery`** — Main image with {rounded.md} corners. Thumbnail strip (72px squares, {rounded.xs}, {spacing.xs} gap) sits below or beside the main image. Active thumbnail gains a 2px solid {colors.primary} border; inactive thumbnails are transparent-bordered. A zoom button in the top-right corner of the main image carries {colors.on-primary} icon on a semi-transparent scrim, {rounded.full}.

### Footer

**`footer`** — Full-width {colors.ink} (#2b333f) background with no top border — the colour break is sufficient. Column headings in {typography.eyebrow} white uppercase; body links in {typography.body-sm} Lora at {colors.hairline-soft} (#90a0b3) brightening to full white on hover. Vertical padding at {spacing.section} on each side. Newsletter input field uses {typography.body-sm} with a hairline border that pulses to primary purple on focus.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks vertically with image above the headline; nav collapses to a full-screen slide-over drawer; filter bar scrolls horizontally; product grid is 2 columns; badge strip wraps to two lines if needed |
| Tablet | 744–1128px | Hero shifts to 50/50 split; product grid expands to 3 columns; filter bar wraps to two rows before scrolling; consultation CTA goes 60/40 text/form layout |
| Desktop | 1128–1440px | Full asymmetric hero (45/55 text/image); product grid at 4 columns; nav links fully visible inline; consultation CTA renders side-by-side with a contact form |
| Wide | > 1440px | Content constrained to a 1440px max-width container with auto side margins; hero image scales within its column but text column stays left-anchored to the grid margin |

### Touch Targets

- All buttons minimum 48px height, 44px minimum tap width
- Nav drawer line items at 56px height on mobile
- Gallery thumbnails minimum 64px × 64px with 8px gaps
- Filter pills minimum 36px height with at least 16px horizontal padding
- Product cards tap the full card face — no isolated link-only zone

### Collapsing Strategy

- Primary navigation collapses to a full-screen slide-over drawer on mobile and tablet, triggered by a hamburger icon in the right slot of the nav-bar; the drawer shows the primary purple active indicator on the current item
- Ring filter bar converts to a horizontally scrollable pill row on mobile; a "Filters" sheet-trigger button opens a bottom sheet at < 744px for the full filter set
- Hero headline scales from {typography.display-xl} (56px) to 36px on tablet and 28px on mobile via fluid type scaling; marlide-display-variable's variable axis can interpolate smoothly
- Product grid increases from 2 columns at mobile to 3 at 744px and 4 at 1128px via CSS grid `auto-fill` with a minimum column width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Variable font axis range for marlide-display-variable not confirmed — weight and optical-size axes unknown without accessing the font binary directly
- Exact button border-radius not pixel-verified from extraction; {rounded.sm} (8px) inferred from category conventions for a craft-oriented brand
- Navigation structure not confirmed — number of top-level menu items, mega-menu vs. simple dropdown unknown
- Hover and focus transition durations and easing curves not extracted
- Product image aspect ratio (4:5) is an inference from bridal jewelry e-commerce norms, not a measured value
- Whether the brand uses a bespoke icon set or a standard library (Heroicons, Feather, etc.) is unknown
- Grid gutter widths and column counts not verified from CSS extraction
- Primary-active state (#6020d0) is derived (darkened) from the extracted primary; no explicit active-state hex was found in the palette
- Dark mode support status unknown — no dark-mode token set could be confirmed
- VideoJS detected in font stacks — indicates video content on at least one page; video player skin colours not captured
