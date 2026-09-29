---
version: alpha
name: "Coway"
source_url: "https://cowaymega.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The palette stacks from petroleum-navy (#17384c) at the structural base through a graduated column of sky tones — #377ca4, #007eb0, #6bc4e8, #d8e7ee — before dissolving into near-transparent ice (#eaf7fc, #f0f5f7) at the canvas layer; it is a chromatic argument that the product literally cleans what it contacts. Neutral slates (#303030, #5e5e5e, #919191) carry all editorial text, keeping the blue-spectrum range free to carry atmosphere rather than utility. Montserrat governs structure — display headlines run 600–700 weight from 28px to 48px — while DM Sans occupies the humane register: body copy, navigation labels, and specification tables where geometric softness matters more than authority. The pairing positions Coway exactly between a medical-grade certification brand and a considered home-goods label.

  Cards rest on a near-white canvas (#fafafa) with ice-tinted section washes (#f0f5f7, #eaf7fc) producing depth through value alone — no box shadows compete with product photography. The hero format favors a single purifier centered on a pale mist gradient with a CADR or PM2.5 figure set at 56px Montserrat 700 as the sole typographic drama; the statistic becomes the proof claim rather than a decorative element. Rounded corners sit at {rounded.md} (12px) for cards and inputs, {rounded.sm} (8px) for buttons, and {rounded.full} for pill-form certification badges and AQI indicator dots — firmly in calibrated-tech territory, neither sharp-cornered nor aggressively pillowed.

  A periwinkle drift (#899df1) and a warm slate-tan (#67503d) appear as sparse accent nodes — likely award-badge borders and lifestyle photography overlays — without disrupting the dominant blue-white register. Shopify's system greens (#008060) surface inside the native cart and checkout flows, where platform tokens briefly override brand tokens; outside those flows, all primary actions revert to deep navy. The footer inverts completely to petroleum-navy, with mist-blue links (#d8e7ee) and sky-hover (#6bc4e8) treating the brand's dominant hue as a closing anchor rather than leaving the page bottom to a system default.

colors:
  primary: "#17384c"
  primary-active: "#0f2535"
  primary-disabled: "#b0b9b7"
  ink: "#111111"
  body: "#303030"
  muted: "#5e5e5e"
  muted-soft: "#919191"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#fafafa"
  surface-soft: "#f0f5f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  sky: "#6bc4e8"
  mist: "#d8e7ee"
  ice: "#eaf7fc"
  medium-blue: "#377ca4"
  deep-teal: "#007eb0"
  periwinkle: "#899df1"
  warm-tan: "#67503d"
  status-error: "#d72c0d"
  status-success: "#008060"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  stat-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  title-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  label-caps:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
    padding: 12px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.primary}"
    borderWidth: 1px
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoHeight: 32px
    ctaButton: button-primary
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    imageBg: "{colors.ice}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-md}"
    captionTypography: "{typography.body-sm}"
    badgeTypography: "{typography.label-caps}"
    badgeBg: "{colors.primary}"
    badgeColor: "{colors.on-primary}"
    badgeRounded: "{rounded.full}"
  hero-banner:
    backgroundColor: "{colors.ice}"
    gradientFrom: "{colors.ice}"
    gradientTo: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    headlineColor: "{colors.ink}"
    bodyColor: "{colors.body}"
    statTypography: "{typography.stat-display}"
    statColor: "{colors.primary}"
    ctaButton: button-primary
    padding: "{spacing.section} 0"
  category-tab:
    backgroundColor: transparent
    activeTextColor: "{colors.primary}"
    inactiveTextColor: "{colors.muted}"
    activeUnderline: "2px solid {colors.primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
    gap: "{spacing.xl}"
  filter-badge:
    backgroundColor: "{colors.ice}"
    borderColor: "{colors.sky}"
    borderWidth: 1px
    textColor: "{colors.primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  aqi-indicator:
    backgroundColor: "{colors.surface-soft}"
    valueTypography: "{typography.stat-display}"
    labelTypography: "{typography.caption}"
    valueColor: "{colors.primary}"
    labelColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    dotSize: 10px
    dotRounded: "{rounded.full}"
  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    closeIconColor: "{colors.mist}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  award-badge:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.periwinkle}"
    borderWidth: 1px
    textColor: "{colors.body}"
    iconColor: "{colors.periwinkle}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.sky}"
    textColor: "{colors.ink}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    height: 44px
    padding: 10px 20px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.mist}"
    linkHoverColor: "{colors.sky}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    dividerColor: "{colors.medium-blue}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Deep petroleum-navy (#17384c) fill with white type at DM Sans 600/16px; sits at 48px tall with {rounded.sm} corners and 12px/28px padding. On hover the fill deepens to #0f2535 (`primary-active`); on disabled state it fades to neutral blue-gray (`primary-disabled`) with `cursor: not-allowed`. This is the primary commerce action button used for all CTAs outside the Shopify-native cart flow.

**`button-secondary`** — White fill with a 1px petroleum-navy border and matching navy text; mirrors `button-primary` dimensions exactly for grid pairing. Used for "Learn More," comparison-add, and secondary filter actions where the primary slot is occupied by "Add to Cart."

**`button-ghost`** — Transparent background with navy text at DM Sans 500/14px and {rounded.sm}; used for nav-overflow dropdowns, inline "View All" links, and modal dismiss actions where a bordered or filled button would be visually heavy.

### Text Input

**`text-input`** — Near-white fill (#fafafa) with a {colors.hairline} border at rest, transitioning to a {colors.primary} navy border on focus with no fill change; 44px tall, {rounded.sm}, DM Sans 400/16px. Placeholder renders at {colors.muted-soft}. Used for email capture fields, search in list contexts, and filter range inputs on PDPs.

### Nav Bar

**`nav-bar`** — 64px tall, canvas background with a 1px {colors.hairline} bottom border. Product category links run at `{typography.nav-link}` (DM Sans 500/14px); the Coway logo anchors left at 32px height. A `button-primary` CTA sits at the right end. The bar remains sticky on scroll with a solid background — no blur or opacity shift — ensuring legibility against the pale hero gradients below.

### Product Card

**`product-card`** — White surface with {rounded.md} corners and a {colors.hairline-soft} border; the image zone fills with {colors.ice} (#eaf7fc) as background so product silhouettes read cleanly before images load. Title and price both use `{typography.title-md}` with the price set in {colors.primary} navy to distinguish it from descriptive copy. Certification or "Bestseller" pill badges use `{typography.label-caps}` on {colors.primary} fill in {rounded.full} form, appearing top-left of the image zone.

### Hero Banner

**`hero-banner`** — A soft ice-to-canvas gradient (#eaf7fc → #fafafa) forms the section wash; the product image is centered with generous vertical breathing room. The headline runs at `{typography.display-xl}` (Montserrat 700/48px) in {colors.ink}. Below or beside it, a single performance stat — CADR rating, PM2.5 capture percentage, or coverage area — renders at `{typography.stat-display}` (Montserrat 700/56px) in {colors.primary}. This stat-as-claim pattern is Coway's primary visual signature: proof replaces persuasion.

### Category Tabs

**`category-tab`** — Horizontal tab strip anchored below the nav for Air Purifiers / Water Filters / Bidets. Inactive tabs render at {colors.muted} in `{typography.title-sm}`; the active tab gains a 2px solid {colors.primary} underline and its text shifts to {colors.primary}. No fill on any state — the canvas shows through — keeping the strip lightweight against ice section backgrounds below.

### Filter Badge

**`filter-badge`** — Pill-shaped ({rounded.full}) with {colors.ice} fill, a 1px {colors.sky} border, and {colors.primary} text at `{typography.label-caps}`. Used for technology callouts (True HEPA, HEPA-13, UV-C, Multi-Stage) on product cards and PDPs. The sky border telegraphs the clean-air color narrative without the visual weight of a filled chip.

### AQI Indicator

**`aqi-indicator`** — A metric display panel used on PDPs and comparison tables: {colors.surface-soft} background, {rounded.md} corners, the numeric value at `{typography.stat-display}` in {colors.primary}, labeled below in `{typography.caption}` at {colors.muted}. A 10px dot in {rounded.full} can carry a traffic-light hue (green/amber/red via inline style) for real-time air quality state without altering surrounding tokens.

### Promo Strip

**`promo-strip`** — Full-width 40px ribbon anchored above the nav bar; {colors.primary} fill with white `{typography.body-sm}` body text and a close icon rendered in {colors.mist} (#d8e7ee) to differentiate it from editorial content without sacrificing legibility on the dark background. Used for shipping thresholds, limited-time discounts, and model launch announcements.

### Award Badge

**`award-badge`** — Small inline badge for third-party certifications (AHAM Verifide, Energy Star, Good Housekeeping Seal). White card background with a 1px {colors.periwinkle} border and {colors.periwinkle} icon; `{typography.caption}` body text in {colors.body}. The periwinkle (#899df1) distinguishes award context from standard brand navy without importing a new visual vocabulary into the rest of the system.

### Search Bar

**`search-bar`** — Full-pill form ({rounded.full}) at 44px, canvas fill with a {colors.hairline} border that transitions to {colors.sky} on focus — distinguishing search interaction from standard text-input focus which uses primary navy. Icon in {colors.muted} at left; DM Sans 400/16px placeholder. Appears in the desktop nav layout and the mobile drawer overlay.

### Footer

**`footer`** — Full petroleum-navy inversion: {colors.primary} background, white body text at `{typography.body-sm}`, {colors.mist} links at rest and {colors.sky} links on hover. Section headings at `{typography.title-sm}` in white. Horizontal dividers use {colors.medium-blue} (#377ca4) to maintain column structure without harsh contrast on the dark surface. The footer closes every page in the deepest brand tone, creating chromatic bookending against the ice-tinted heroes above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; category tabs become a horizontal scroll strip; hero headline drops to `display-md` (28px); stat-display scales to 40px; promo strip wraps to 2 lines max |
| Tablet | 744–1128px | 2-column product grid; nav retains logo and primary CTA, secondary links in hamburger; hero shifts to 50/50 image-and-text split; category tabs visible but condensed |
| Desktop | 1128–1440px | 3-column product grid; full horizontal nav with category tabs inline; hero uses full-bleed background with centered content column capped at 1080px |
| Wide | > 1440px | Content column caps at 1440px and centers; hero stat scales to full `stat-display` (56px) paired beside headline; footer columns expand to 5 across |

### Touch Targets
- All buttons minimum 44×44px
- Category tab items minimum 44px tall with extended horizontal padding for tap zones
- Filter badge pills minimum 32px tall; stack vertically on mobile rather than wrapping mid-word
- Nav icons (cart, search, hamburger) minimum 44×44px tap area regardless of visible glyph size
- AQI indicator dots minimum 24px touch target with surrounding transparent padding

### Collapsing Strategy
- Product grid collapses 3→2→1 columns at Desktop→Tablet→Mobile breakpoints
- Nav bar category tabs collapse into horizontal scroll strip on Tablet, full accordion drawer on Mobile
- Hero banner switches from horizontal split (Desktop/Wide) to stacked image-over-text (Tablet/Mobile)
- Footer multi-column link grid collapses to single-column accordion sections on Mobile with {colors.medium-blue} dividers between sections
- Promo strip persists at all breakpoints; truncates to single line with ellipsis on Mobile before close icon

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `surface-card` (#ffffff) not directly in the extraction; inferred as standard Shopify product card background — actual site may use #fafafa or #f1f1f1 instead
- No custom icon or glyph library identified from static extraction; SVG icon system likely loaded via JS bundle
- Shopify system green (#008060) and error red (#d72c0d) appear in the extraction and may govern add-to-cart and error states — unclear whether Coway fully overrides these or accepts platform defaults
- Animation and transition timings (hover durations, hero fade-in) not extractable from static color/font pass
- Mobile navigation drawer design (open state, overlay scrim color, slide-vs-fade animation) not confirmed
- Dark-mode or high-contrast variant not observed in extraction
- #eeefbf (pale chartreuse) and #f0b743 (amber) appear in the extraction and may indicate filter-life warning states or seasonal promo contexts; usage not confirmed
- #67503d (warm tan) origin unclear — possibly product packaging photography bleed or lifestyle image overlay; not assigned a component role
- Exact hero layout proportions and whether CADR stats appear in a standard template or are editorial overrides requires live-site review
