---
version: alpha
name: "Humanscale (Arms)"
source_url: "https://www.humanscale.com/products/monitor-arms"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Forty distinct grays — from near-black #2f2d2d to barely-off-white #f5f5f5 — build the visual platform for every monitor arm listing, then a single chartreuse (#abbd26) cuts through like a calibration mark on an engineering drawing: CTA buttons, hover rails, active filter states, nothing else. This restraint is structural; Humanscale's design language descends from industrial ergonomics rather than consumer marketing, and the product pages reflect that — every visual choice earns its place against payload specs and range-of-motion data. Archer, a bracketed slab serif, carries display headlines and product names, lending mass to an otherwise austere grid; it pairs against NeueMontreal and Rand for body copy and UI labels, creating a slab-over-geometric hierarchy that reads simultaneously as technical documentation and premium editorial. The secondary palette plays two distinct roles: sky blue (#51b5e0, #6cc1e5) handles configurator states and informational affordances, while deep teal (#3c5956) anchors environmental photography crops and section dividers — both are navigational signals, never decorative. A muted sage (#9aab8b) functions as a tertiary neutral in comparison grids, softening dense data rows without competing with the chartreuse primary. Corners are tight throughout — product cards and filter chips sit at {rounded.xs} to {rounded.sm}, echoing machined-component precision rather than consumer softness. Payload ratings, cable routing specs, and reach dimensions live in condensed-type data tables set in Conv_UniversLTStd-BoldCn, repurposing the visual grammar of engineering documentation as product marketing. Trust is earned through specification completeness, not lifestyle imagery; the chartreuse CTA is the only moment the brand raises its voice.

colors:
  primary: "#abbd26"
  primary-active: "#9eb300"
  primary-hover: "#b1c233"
  primary-disabled: "#d6d8d9"
  accent-blue: "#51b5e0"
  accent-blue-light: "#6cc1e5"
  accent-teal: "#3c5956"
  accent-sage: "#9aab8b"
  ink: "#2f2d2d"
  body: "#58595b"
  muted: "#7d7d7d"
  muted-soft: "#9a9a9a"
  hairline: "#d1d3d4"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-mid: "#efefef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Archer, 'Roboto Slab', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Archer, 'Roboto Slab', Georgia, serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Archer, 'Roboto Slab', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "NeueMontreal-Regular, Rand, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "NeueMontreal-Regular, Rand, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "NeueMontreal-Regular, Rand, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "NeueMontreal-Regular, Rand, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "NeueMontreal-Regular, Rand, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  eyebrow:
    fontFamily: "Rand-Bold, NeueMontreal-Regular, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "Conv_UniversLTStd-BoldCn, 'Arial Narrow', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Rand-Bold, NeueMontreal-Regular, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "Rand-Bold, NeueMontreal-Regular, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "NeueMontreal-Regular, Rand, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
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
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    hoverBorderColor: "{colors.primary}"
    hoverTextColor: "{colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 44px
    focusBorderColor: "{colors.primary}"
    focusBorderWidth: 2px
  text-input-error:
    borderColor: "{colors.accent-blue}"
    focusBorderColor: "{colors.accent-blue}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.lg} {spacing.xl}"
  product-family-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    borderBottom: "2px solid transparent"
    padding: "{spacing.sm} {spacing.base}"
  product-family-tab-active:
    textColor: "{colors.ink}"
    borderBottomColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageAspect: "4/3"
    titleTypography: "{typography.title-md}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
    hoverBorderColor: "{colors.primary}"
    hoverBorderWidth: 2px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 540px
    ctaSpacing: "{spacing.xl}"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.primary}"
  spec-badge:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.ink}"
    headerTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    bodyTextColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rowAlternateColor: "{colors.surface-soft}"
    cellPadding: "{spacing.sm} {spacing.base}"
  configurator-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    selectedBorderColor: "{colors.primary}"
    selectedBorderWidth: 2px
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
  section-divider:
    borderColor: "{colors.hairline}"
    accentColor: "{colors.primary}"
    accentWidth: 40px
    marginVertical: "{spacing.section}"
  download-cta:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.base} {spacing.lg}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  teal-section-banner:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-dark}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    linkColor: "{colors.hairline}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.eyebrow}"
    headingColor: "{colors.on-dark}"
    borderTop: "3px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Chartreuse (#abbd26) fill, white uppercase label in Rand-Bold 14px at 0.8px tracking, zero border-radius. Height is 48px with 14px/28px vertical/horizontal padding. Hover lifts one shade to #b1c233; active deepens to #9eb300; disabled adopts hairline-gray fill (#d6d8d9) with muted text. This CTA appears exclusively for transactional actions — Add to Cart, Request Quote, Configure — and is never placed in navigation or editorial contexts.

**`button-secondary`** — Transparent background with 1px ink (#2f2d2d) border and matching uppercase Rand-Bold typography. Used for adjacent secondary actions like "Download Spec Sheet" or "Compare Models." On hover, both the border and label text transition to chartreuse (#abbd26) without fill — preserving the flat surface language.

**`button-ghost`** — No background, no border, chartreuse (#abbd26) text in button-md. Reserved for tertiary in-page links and "Learn More" anchors embedded within specification or editorial sections. Never used as a standalone CTA where a primary or secondary button is present.

### Text Input

**`text-input`** — Square corners ({rounded.none}), 1px hairline border (#d1d3d4), 44px height. Focus upgrades the border to 2px chartreuse (#abbd26) with no shadow — keeping the interaction language consistent with the selected-state pattern used across configurator selectors. Error state uses accent blue (#51b5e0) to avoid false-positive association with the primary action color.

### Navigation

**`nav-bar`** — White canvas, 72px height, 1px hairline bottom border. The Humanscale wordmark sits left in Archer; product category links in NeueMontreal-Regular 14px span the center rail. Dropdown panels open below with a 2px chartreuse top accent border over a full-width white surface padded at 24px/32px. Active category text shifts to chartreuse; no underline decoration on hover.

**`product-family-tab`** — A secondary horizontal rail sitting directly below the main nav-bar; carries Monitor Arms sub-family labels (M/Connect, M2, M/Flex, etc.) in NeueMontreal SemiBold 15px. Inactive tabs render in muted gray (#7d7d7d) text against a transparent 2px bottom border. Active tab uses ink text (#2f2d2d) with a solid chartreuse 2px bottom border. On mobile the rail becomes a horizontally scrollable pill row.

### Product Card

**`product-card`** — 1px hairline border, {rounded.xs} corners, white surface. Product image occupies the top third at 4:3 aspect ratio; title below in title-md (18px NeueMontreal SemiBold, ink); model number or capacity callout in body-sm (muted #7d7d7d). A "View Product" link in chartreuse button-sm type anchors the card footer. On hover, the border upgrades to 2px chartreuse — no elevation, no shadow, consistent with the flat machined-surface aesthetic.

### Hero Banner

**`hero-banner`** — Near-black (#2f2d2d) background with full-bleed product photography. Eyebrow label in uppercase eyebrow type (11px Rand-Bold, 1.5px tracking) set in chartreuse. Headline in Archer display-xl (48px, weight 700); body copy in NeueMontreal body-md at a dimmed white (#bbbbbb). CTA pair: primary chartreuse button left, secondary ghost button right, 32px gap between. Minimum height 540px on desktop; on mobile the layout stacks image over text and buttons stretch full width.

### Filter Chip

**`filter-chip`** — Surface-soft (#f5f5f5) fill, 1px hairline border, {rounded.xs} corners, 12px NeueMontreal caption type. Used on the monitor arms listing page to narrow by weight capacity, panel count, mount type, and finish. Active state inverts to solid chartreuse fill with white text; no intermediate selected-hover state. The chip row is horizontally scrollable on mobile rather than wrapping.

### Spec Badge

**`spec-badge`** — Surface-mid (#efefef) fill, {rounded.xs} corners, Conv_UniversLTStd-BoldCn 13px uppercase. Carries abbreviated spec callouts — "UP TO 20 LBS", "360° ROTATION", "SINGLE/DUAL" — as inline chips within product description blocks and listing grid cards. They never link; they annotate.

### Spec Table

**`spec-table`** — Borderless outer container; internal rows separated by 1px hairline (#d1d3d4). Header row in surface-soft (#f5f5f5) with spec-label type (condensed, uppercase, ink). Body rows alternate between white and surface-soft. Left column (spec name) in spec-label; right column (value) in body-sm at #58595b. Cell padding is 8px vertical / 16px horizontal. Covers payload capacity, reach range, tilt/pan/rotation limits, cable management options, and BIFMA certification status.

### Configurator Selector

**`configurator-selector`** — White fill, 1px hairline border, {rounded.xs}. Selected state upgrades border to 2px chartreuse (#abbd26). Label in body-sm (14px); secondary value or subtext in caption gray. Used for finish selection (polished aluminum, graphite, white), cable management toggle, and mount type (desk clamp vs. grommet). Selectors arrange in a 2- or 3-column grid beneath the product hero on desktop, collapsing to a single-column stack on mobile.

### Download CTA

**`download-cta`** — Surface-soft (#f5f5f5) fill, 1px hairline border, zero radius. A chartreuse down-arrow or document icon sits left of an uppercase Rand-Bold label. Used for spec-sheet PDF and installation-guide downloads; appears in the product detail Resources section below the spec table and again in the page footer. Height aligns to 48px to meet touch target minimums.

### Teal Section Banner

**`teal-section-banner`** — Deep teal (#3c5956) full-width background, used as a section break between product families and sustainability or support content. Eyebrow in chartreuse uppercase; headline in Archer display-md (32px, weight 600); body in NeueMontreal body-md at near-white. Used sparingly — typically one instance per main product page, anchoring a competitive or performance claim (e.g., "Up to 79% more weight capacity"). On mobile, padding reduces from {spacing.section} to {spacing.xl} and headline scales down to display-sm.

### Footer

**`footer`** — Near-black (#2f2d2d) background with a 3px chartreuse top border as the single brand signal. Column headings in uppercase eyebrow type (#ffffff); links in body-sm at hairline gray (#d1d3d4). Legal copy in caption at muted-soft (#9a9a9a). Standard 4-column desktop layout collapses to an accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks text over image with full-width CTA buttons; filter chips scroll horizontally in a single row; spec table scrolls horizontally with sticky first column; nav collapses to hamburger slide-in panel; configurator selectors stack single-column; footer becomes accordion |
| Tablet | 744–1128px | Two-column product grid; hero maintains side-by-side layout with display-xl reduced to ~36px; filter chips wrap to two rows; configurator selectors in 2-column grid; product-family-tab rail shows condensed labels |
| Desktop | 1128–1440px | Three-column product grid; full hero at 540px min-height; filter chip row single-line with horizontal overflow scroll; spec table full-width; 4-column footer |
| Wide | > 1440px | Content capped at 1440px max-width, centered with symmetric gutters; product grid may expand to 4 columns; hero background bleeds edge-to-edge behind contained content block |

### Touch Targets

- Filter chips minimum 44px height tap zone regardless of visual height
- Configurator selector cells minimum 44px height
- Nav hamburger 44×44px tap zone
- Download CTA row minimum 48px height
- Product card "View Product" link padded to 44px vertical tap zone
- All form inputs (text-input) minimum 44px height

### Collapsing Strategy

- Horizontal spec tables gain sticky first column on mobile with horizontal overflow scroll
- Multi-column configurator selector grids collapse to single-column stack below 744px
- Hero CTA pair stacks vertically on mobile with 100% width stretch
- Navigation mega-dropdown converts to full-screen slide-in drawer on mobile
- Product-family-tab rail converts to horizontally scrollable pill row on mobile
- Teal section banner padding reduces from {spacing.section} to {spacing.xl} on mobile; headline shifts from display-md to display-sm
- Footer 4-column layout converts to tap-to-expand accordion sections on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white (#ffffff) canvas not observed in hex extraction; assumed from standard product-page defaults — verify against live site background
- Exact nav-bar height (72px) and logo dimensions are estimates; not confirmed from static extraction
- Hover animation timing (transition duration, easing) not extractable from hex/font scan — assume 150ms ease-out for color and border transitions
- Price typography scale (MSRP size, weight, color; sale vs. list differentiation) not captured
- Tiempos (editorial serif) and HaveHeart (decorative) families detected but no product-page usage context found — likely confined to marketing editorial or blog content
- Archer-Light usage context not confirmed; used here only for fallback stacking, not as an independent type role
- Mobile breakpoint pixel values (744px, 1128px) are category-norm estimates; exact Humanscale breakpoints not confirmed
- Dark-mode or high-contrast variant not observed in extraction
- Product image background (pure white studio vs. surface-soft #f5f5f5) not confirmed
- Form validation error states beyond border-color change (error message typography, icon treatment) not captured
