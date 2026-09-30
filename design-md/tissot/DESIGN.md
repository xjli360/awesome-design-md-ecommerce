---
version: alpha
name: "Tissot"
source_url: "https://www.tissotwatches.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  At #00a1e0, Tissot's primary blue runs brighter than almost any other watch brand allows itself — closer to the electric cyan of airline booking software than the navy restraint typical of horology — and this chromatic boldness is the brand's sharpest design declaration: Swiss Made credentials can coexist with accessibility-first, utilitarian interface logic. Three signal colors partition the full interface language: the primary cyan-blue for all CTAs, links, and navigational highlights; #008827 green marking T-Touch Solar and eco-positioned lines; #eb0000 red firing on sale states, clearance badges, and error messaging. This traffic-light vocabulary suits an audience making practical, value-conscious purchase decisions rather than purely aspirational ones. The canvas sits at #f9f9f9 rather than pure white, giving watch photography just enough warmth to lift product isolation without drifting toward a cream that would age the brand. Typography runs entirely on system stacks — Helvetica Neue and Arial on desktop, -apple-system on iOS — a notable absence of custom font investment that shifts the reading environment toward specification-and-price comparison rather than mood-setting. The palette's structural tones carry the mechanical register: #383d41 for primary body text, #1d2124 for headlines, and deep #005474 and #007cad for hover and active states — ranges that read as instrument-grade without claiming fine-jewellery territory. Rounded values stay conservative throughout: {rounded.xs} at 4px on buttons and inputs, expanding to {rounded.full} only on badge pills. This geometric discipline reinforces precision-instrument positioning and separates Tissot clearly from the rounder, friendlier arcs of fashion jewelry and lifestyle accessories operating at similar price points.

colors:
  primary: "#00a1e0"
  primary-active: "#007cad"
  primary-dark: "#005474"
  primary-deep: "#006a94"
  primary-disabled: "#94e1ff"
  primary-light: "#b8e5f6"
  primary-subtle: "#a1ddf3"
  primary-pale: "#61d2ff"
  signal-green: "#008827"
  signal-green-dark: "#004714"
  signal-green-mid: "#005518"
  signal-red: "#eb0000"
  signal-red-dark: "#7a0000"
  signal-red-mid: "#b80000"
  info-teal: "#0c5460"
  info-teal-mid: "#117a8b"
  warning-gold: "#856404"
  warning-gold-mid: "#d39e00"
  ink: "#1d2124"
  body: "#383d41"
  muted: "#818182"
  muted-dark: "#545b62"
  hairline: "#d6d8db"
  hairline-soft: "#dae0e5"
  hairline-mid: "#c8cbcf"
  canvas: "#f9f9f9"
  surface-soft: "#f9f9f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.3px
  specs-label:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, BlinkMacSystemFont, 'Liberation Sans', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    hoverBackgroundColor: "{colors.primary-light}"
    hoverTextColor: "{colors.primary-active}"
    hoverBorderColor: "{colors.primary-active}"
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    borderColor: "{colors.on-dark}"
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-mid}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
    focusBorderColor: "{colors.primary}"
    placeholderColor: "{colors.muted}"
  text-input-error:
    borderColor: "{colors.signal-red}"
    textColor: "{colors.signal-red-dark}"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoWidth: 120px
    activeLinkColor: "{colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.lg} {spacing.xl}"
    headingColor: "{colors.ink}"
    headingTypography: "{typography.specs-label}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    imageBackground: "{colors.canvas}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    borderColor: "{colors.hairline-soft}"
    borderWidth: 1px
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 480px
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    overlayColor: "rgba(29,33,36,0.45)"
    ctaGap: "{spacing.lg}"
  collection-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  collection-badge-sale:
    backgroundColor: "{colors.signal-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  collection-badge-solar:
    backgroundColor: "{colors.signal-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  collection-badge-limited:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  price-regular:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-sale:
    textColor: "{colors.signal-red}"
    typography: "{typography.price-display}"
  price-was:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    textDecoration: line-through
  watch-specs-table:
    backgroundColor: "{colors.canvas}"
    labelColor: "{colors.muted-dark}"
    labelTypography: "{typography.specs-label}"
    valueColor: "{colors.ink}"
    valueTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    rowPadding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline-mid}"
    typography: "{typography.caption}"
    linkColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-mid}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    height: 42px
    iconColor: "{colors.muted}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-sm}"
  product-filter-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline-mid}"
    borderWidth: 1px
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorderColor: "{colors.primary}"
  alert-info:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-dark}"
    borderColor: "{colors.primary-subtle}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  alert-success:
    backgroundColor: "{colors.signal-green}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  alert-danger:
    backgroundColor: "{colors.signal-red}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary-light}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.specs-label}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Flat rectangular CTA in Tissot's primary #00a1e0 with white uppercase text at 16px/600 weight and 0.5px letter-spacing; the minimal {rounded.xs} (4px) corner reinforces precision-instrument positioning over lifestyle softness. Hover darkens to {colors.primary-active} (#007cad); disabled state fades to {colors.primary-disabled} (#94e1ff) with white text retained throughout for contrast compliance.

**`button-secondary`** — Transparent fill with a 1px {colors.primary} border and matching text, using the same {rounded.xs} geometry as the primary; hover fills to {colors.primary-light} and shifts text to {colors.primary-active}, providing visual confirmation without committing to the full primary weight. Used for secondary actions like "Add to Wishlist" or "Compare."

**`button-ghost-dark`** — White border and white text on dark hero backgrounds; same uppercase 16px/600 weight and {rounded.xs} geometry as the primary family, applied where the hero's dark overlay makes colored fills invisible.

### Navigation

**`nav-bar`** — 64px white bar with a 1px {colors.hairline} bottom border separating it from content. Links at 14px/600 with 0.3px tracking in {colors.ink}, transitioning to {colors.primary} on active state. The Tissot logotype renders at approximately 120px wide. The top stripe is a clean white with no tint, reflecting the precision-manufacture brand register.

**`nav-dropdown`** — Full-width flyout panel that replaces the nav hairline with a 2px {colors.primary} rule as the sole structural accent. Section headings use {typography.specs-label} (uppercase 12px/700) in {colors.ink}; body links at {typography.body-sm} in {colors.body}. Watch category thumbnails appear in a constrained image grid, giving the menu a catalog feel over a lifestyle-editorial feel.

### Product Card

**`product-card`** — 1px {colors.hairline-soft} bordered card on a white surface; image zone uses {colors.canvas} (#f9f9f9) as isolation background for watch photography rendered on neutral grey. Title at {typography.title-sm} (16px/600); price at {typography.price-display} (22px/700). Promotional badges float top-left as pill stacks using {rounded.full}. On hover, the card lifts to a 4px box-shadow at 10% opacity — the only animated state on the card, keeping the interaction language precise rather than playful.

### Badge System

**`collection-badge-new`** — {rounded.full} pill in {colors.primary} with white 11px/700 uppercase text; signals catalog freshness while reinforcing the primary blue brand signal.

**`collection-badge-sale`** — Identical pill geometry in {colors.signal-red} (#eb0000); part of the tri-signal system where red is reserved exclusively for commercial urgency, never used decoratively.

**`collection-badge-solar`** — {colors.signal-green} (#008827) for T-Touch Solar and sustainability-positioned SKUs, completing the traffic-light triple that partitions the Tissot catalog into navigation, commerce, and ecology lanes.

**`collection-badge-limited`** — {colors.ink} pill for limited-edition and special series, differentiating collectible positioning from the three primary signal colors without introducing a fourth hue.

### Price Display

**`price-sale`** + **`price-was`** — Sale price renders in {colors.signal-red} at 22px/700; the crossed-out original price appears immediately below or beside it in {colors.muted} at 14px with `text-decoration: line-through`. The pairing always renders together on discounted SKUs, preserving the value-signal that drives Tissot's entry-point positioning in the Swiss watch market.

### Watch Specs Table

**`watch-specs-table`** — Two-column key/value table with {colors.canvas} background used on product detail pages; row labels run in {typography.specs-label} (12px uppercase/700/0.8px tracking) in {colors.muted-dark}, values in {typography.body-sm} in {colors.ink}. 1px {colors.hairline} row separators, {rounded.xs} outer container. Standard rows: case diameter, water resistance (ATM), movement calibre, glass material, strap/bracelet width, and power reserve where applicable.

### Hero Banner

**`hero-banner`** — Full-bleed watch photography with a {colors.ink} overlay at 45% opacity; minimum 480px height on desktop. Campaign title at {typography.display-xl} (32px/700) in white; campaign subtitle at {typography.body-md} in white at reduced opacity. CTA pair — typically one `button-primary` and one `button-ghost-dark` — sits below the subtitle with {spacing.lg} vertical gap. Hero text is left-aligned and contained within the page grid, not centered over the full image.

### Product Filter Pills

**`product-filter-pill`** — {rounded.full} pill with 1px hairline border and {colors.ink} text at rest; on active selection, fills to {colors.primary} with white text, using the same uppercase 13px/600 type as `button-sm`. Filters for case material, strap type, movement, and price range render as a scrollable horizontal strip on mobile.

### Alert Banners

**`alert-info`** — Soft {colors.primary-light} (#b8e5f6) background with {colors.primary-dark} text and {colors.primary-subtle} border; used for shipping notices and stock updates. **`alert-success`** and **`alert-danger`** use the full-saturation signal colors ({colors.signal-green} and {colors.signal-red} respectively) with white text, applying the same chromatic vocabulary as the badge system to feedback states.

### Search

**`search-bar`** — 42px inline field, {rounded.sm} (8px) — slightly rounder than buttons, signaling an open/exploratory affordance. 1px {colors.hairline-mid} border with {colors.primary} focus ring; magnifier icon in {colors.muted} left of placeholder text. Placed in the nav-bar on desktop; expands to a full-width overlay sheet on mobile.

### Footer

**`footer`** — {colors.ink} (#1d2124) background with a 2px {colors.primary} top rule as the sole chromatic accent, mirroring the nav-dropdown pattern. Section headings in {typography.specs-label} (uppercase/700); body links in {colors.primary-light} (#b8e5f6). Four-column grid on desktop collapses to stacked accordion sections on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero min-height reduces to 300px; watch specs table scrolls horizontally inside a scroll-snap container; footer becomes stacked accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category links with "More" overflow toggle; hero at 380px min-height; filter pills scroll horizontally |
| Desktop | 1128–1440px | Three-column product grid; full mega-dropdown nav; hero at 480px with left-aligned text panel and CTA pair; specs table renders full-width |
| Wide | > 1440px | Four-column product grid; content max-width ~1400px centered; hero image scales behind the content container constraint |

### Touch Targets

- All primary and secondary CTAs: minimum 44×44px tap area
- Nav hamburger icon: minimum 44×44px
- Product card: entire card surface is tappable including image zone
- Filter pills: minimum 36px height, 12px horizontal padding to pad narrow labels
- Footer accordion headers: minimum 48px height for comfortable thumb tap
- Badge pills: display-only, no tap target required

### Collapsing Strategy

- Navigation: hamburger slide-in drawer on mobile, horizontal primary links on tablet+, mega-dropdown panel on desktop
- Product filters: off-canvas drawer triggered by "Filter" button on mobile, sticky left sidebar on desktop
- Watch specs table: horizontal scroll container with scroll-snap on mobile; full visible table on tablet+
- Footer: stacked accordion sections on mobile (heading taps reveal link lists); four-column static grid on desktop
- Hero CTA pair: stacks vertically on mobile with full-width buttons; renders as an inline row on tablet+

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; all typography uses system font stacks (Helvetica Neue/Arial/-apple-system). Tissot may use a licensed geometric sans on production that was not surfaced in the static crawl.
- Meta theme-color not set; #00a1e0 assumed as the intended browser chrome tint on Android but cannot be confirmed from extraction.
- Exact button and input corner radii not extracted from CSS; {rounded.xs} (4px) inferred from the utilitarian brand register and common watch-retail patterns.
- Hover transition timing and easing curves (button fill speed, card shadow transition) not available from static extraction.
- Spacing rhythm internal to the product card (image-to-title gap, title-to-price gap) not confirmed; values inferred from standard grid conventions.
- Dark mode or alternate color scheme unknown — no dark-mode media query tokens detected in the crawl.
- The crawled URL is the Japanese regional store; EN/EU/US stores may carry regional typographic or layout overrides not reflected here.
- Exact nav-bar height (64px) inferred; confirmed measurement not available from extraction.
- Animation states for the mega-dropdown (entrance direction, duration) not extractable from the static snapshot.
