---
version: alpha
name: "Magid Glove & Safety"
source_url: "https://www.magidglove.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every SKU on magidglove.com carries a compliance certificate column before a color swatch — ANSI/ISEA cut levels, EN 388 pictograms, ASTM F2413 notation — signaling that the primary reader is a safety director writing a procurement spec, not a consumer comparing aesthetics. The brand has operated this way since 1946, and the design system reflects that institutional confidence. Engineering red (#cc0000) anchors every primary CTA, category header, and navigation underline; it reads as authoritative against the white catalog canvas because it echoes the urgency vocabulary already embedded in OSHA signage rather than courting lifestyle aspirations. Safety amber (#ff6600) handles the second tier of urgency — clearance callouts, stock alerts, the DANGER-tier hazard badge — creating a clear hierarchy between brand emphasis and operational warnings. Deep charcoal (#1a1a1a) and mid-gray (#666666) carry the dense specification prose that industrial buyers actually read: tensile strength ratings, dielectric class descriptions, arc rating tables measured in cal/cm².

  Typography runs on a high-legibility sans-serif stack — Helvetica Neue or Arial — at weight 600–700 for display and product titles, dropping to 400 for specification paragraphs. There is no decorative face, no script accent, no editorial experiment; every typographic decision asks whether a safety manager scanning on a factory-floor tablet can parse it in two seconds. Button labels set uppercase at weight 700 and 0.5px letter-spacing reinforce the workmanlike register without feeling aggressive.

  The rounded system stays conservative — {rounded.sm} on product cards, {rounded.xs} on compliance badges, {rounded.none} on the sticky filter rail — because authority in industrial procurement design comes from precision, not approachability. Compliance badges render in a muted {colors.compliance-badge-bg} tile with a 1px {colors.hairline} border, mimicking the ISO-standard label blocks printed on the physical product packaging. The product-finder widget breaks from this restraint just enough — a {rounded.md} container with a {colors.primary} accent border — to signal interactivity without abandoning the catalog grammar surrounding it. Generous {spacing.lg} gutters keep 5,000-plus SKUs scannable under a sticky category-filter rail organized by hazard type — cut, impact, chemical, arc flash, hi-vis — because safety professionals search by hazard category, not by garment form.

colors:
  primary: "#cc0000"
  primary-active: "#a30000"
  primary-hover: "#b30000"
  primary-disabled: "#f5a0a0"
  accent-amber: "#ff6600"
  accent-amber-soft: "#fff3e8"
  safety-yellow: "#ffd100"
  safety-yellow-surface: "#fffbe0"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  compliance-badge-bg: "#eef1f5"
  compliance-badge-text: "#2c3e50"
  success: "#2e7d32"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, 'Liberation Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  spec-table:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  compliance-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-active:
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
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-top-strip:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 32px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "3px solid {colors.primary}"
    logoHeight: 36px
    searchBarWidth: 320px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.none}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspect: "1:1"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.body-sm}"
    badgeRowGap: "{spacing.xs}"
  compliance-badge:
    backgroundColor: "{colors.compliance-badge-bg}"
    textColor: "{colors.compliance-badge-text}"
    typography: "{typography.compliance-label}"
    rounded: "{rounded.xs}"
    padding: "3px 6px"
    border: "1px solid {colors.hairline}"
  hazard-badge-danger:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.compliance-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hazard-badge-warning:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.compliance-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hazard-badge-caution:
    backgroundColor: "{colors.safety-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.compliance-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted-soft}"
    accentBar: "4px solid {colors.primary}"
    minHeight: 400px
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
  category-filter-rail:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    activeTextColor: "{colors.primary}"
    activeIndicator: "3px solid {colors.primary}"
    padding: "{spacing.base} {spacing.lg}"
    sticky: true
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.title-sm}"
    bodyTypography: "{typography.spec-table}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    stripedRowBackground: "{colors.surface-soft}"
  product-finder-widget:
    backgroundColor: "{colors.surface-soft}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    headlineTypography: "{typography.display-sm}"
    headlineColor: "{colors.primary}"
    bodyTypography: "{typography.body-md}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    height: 44px
    iconColor: "{colors.muted}"
  industry-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.hairline}"
  promo-banner:
    backgroundColor: "{colors.accent-amber-soft}"
    textColor: "{colors.ink}"
    borderLeft: "4px solid {colors.accent-amber}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
    borderTop: "4px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — The main action driver: solid #cc0000 fill, white uppercase type at weight 700 with 0.5px letter-spacing, 4px radius, 44px height. Hover shifts to #b30000; active to #a30000; disabled fades fill to #f5a0a0. Used for "Add to Cart," "Request a Quote," and primary search submission.

**`button-secondary`** — White fill with a 2px #cc0000 border and red text; same uppercase treatment as primary. Paired with `button-primary` in dual-CTA rows where "Download SDS Sheet" or "Compare" sits alongside "Add to Cart."

**`button-ghost`** — Transparent fill, 1px hairline border, ink text, lowercase button-sm type. Used for tertiary actions — filter resets, "View All," pagination controls — where visual weight must stay minimal inside dense catalog layouts.

**`button-amber`** — Safety amber (#ff6600) fill with white text; reserved for time-sensitive callouts like clearance events or limited-availability alerts so it reads as operationally distinct from the red brand primary.

### Navigation

**`nav-top-strip`** — A 32px dark charcoal (#1a1a1a) utility bar above the main nav carrying account links, order tracking, and a phone number in caption-weight type. Sets the professional register immediately on page load.

**`nav-bar`** — White bar, 64px tall, with a 3px #cc0000 underline rule at the bottom. Holds the Magid wordmark left, a 320px search bar center, and account/cart icons right. Category links use nav-link weight 600; the active category gets a red text color rather than an underline to avoid conflict with the bottom border rule.

**`nav-dropdown`** — Full-width panel with white background, 1px hairline border, and a 0 4px 16px rgba box shadow. No radius (rounded.none) — maintains the catalog grid aesthetic. Organized in two-column grids of protection-type links with small product imagery.

### Product Card

**`product-card`** — White card, 1px hairline border, 4px radius, 16px padding. Square 1:1 product image on a soft gray (#f5f5f5) tile to isolate gloves, glasses, or garments against a neutral field. Title in title-md (weight 700), price in the dedicated price scale (18px weight 700), and a compliance-badge row along the bottom edge. Badge row uses flexWrap so multiple certification chips stay legible at narrow widths.

### Compliance & Hazard Badges

**`compliance-badge`** — Small eef1f5-fill chip, 10px uppercase weight-700 label, 1px hairline border, 2px radius. Displays standard codes: "ANSI A4," "EN 388," "ATPV 12 cal/cm²." Renders in a flex row below product title on cards and in a dedicated "Certifications" block on PDP.

**`hazard-badge-danger`** — Red (#cc0000) fill, white text, same compliance-label typography. Reserved strictly for DANGER-tier arc flash and electrical hazards.

**`hazard-badge-warning`** — Amber (#ff6600) fill, white text. Chemical splash, cut A5–A9, high-heat environments.

**`hazard-badge-caution`** — Safety yellow (#ffd100) fill, ink text. Lower-severity caution indicators — minor abrasion, light heat.

### Hero Banner

**`hero-banner`** — Dark charcoal (#1a1a1a) full-width panel, minimum 400px, with a 4px left-edge #cc0000 accent bar on the headline block. Headline uses display-xl (36px weight 700), subhead uses body-md in muted-soft (#999999) for contrast reduction. CTA button renders in primary red fill. Background image or lifestyle photography bleeds to right; text block stays left-anchored with a hard left margin.

### Product Finder Widget

**`product-finder-widget`** — A soft-gray (#f5f5f5) container with a 2px #cc0000 border and 8px radius, standing out from the flat hairline-bordered cards that surround it. Display-sm headline in red ("Find the Right Glove"). Houses a cascading select sequence: hazard type → ANSI level → industry → then surfaces matching SKUs. The accent border signals it as a tool, not just content.

### Spec Table

**`spec-table`** — Full-width table with a 1px hairline outer border. Header row in surface-soft background with title-sm weight-600 labels; body rows in canvas white and alternating surface-soft stripes. Used extensively on PDPs for grip type, material, liner weight, EN standard performance scores, and temperature range data. No rounded corners.

### Category Filter Rail

**`category-filter-rail`** — Left-side sticky column on catalog pages, soft-gray background, no radius. Filter groups (protection type, ANSI cut level, size, industry, brand line) use title-sm weight-600 headers in ink; individual filter items use body-sm. Active selection shows a 3px red left-side indicator and red text. Stays fixed at the top of the viewport on scroll so buyers can refine a 200-result query without losing filter state.

### Footer

**`footer`** — Dark charcoal (#1a1a1a) full-width block with a 4px #cc0000 top border rule. Column headers in title-sm on-dark weight 600; body links in body-sm hairline-colored. Four columns: Products, Industries Served, Resources (SDS, Catalog, Compliance Guides), Company. Legal strip in caption weight at bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category filter rail collapses to a bottom-sheet drawer triggered by a fixed "Filter" button; nav-bar collapses to hamburger + logo + cart icon; hero banner becomes full-bleed stacked (image above, text below) |
| Tablet | 744–1128px | Two-column product grid; filter rail optionally shown as a top horizontal scroll strip; nav shows top-level category labels with tap-to-expand dropdowns; hero banner text overlaps image with 50% width text block |
| Desktop | 1128–1440px | Three-column product grid with sticky left filter rail (240px wide); full nav-bar with dropdown panels; hero banner at full 400px minimum height with 40/60 text/image split |
| Wide | > 1440px | Four-column product grid; content max-width capped at 1440px with centered layout; hero banner image extends to viewport edge while content column stays within max-width container |

### Touch Targets

- All interactive buttons minimum 44px height
- Compliance badge chips on mobile expand to 36px tap height via increased vertical padding
- Filter checkboxes minimum 44×44px touch area with invisible padding extension
- Nav hamburger target minimum 48×48px
- Product card entire surface is tappable on mobile; desktop restricts click to title and CTA

### Collapsing Strategy

- Product finder widget stacks selects vertically on mobile, becomes a modal bottom-sheet on tap
- Spec tables on PDP collapse to a show/hide accordion section on mobile; default expanded on desktop
- Compliance badge rows truncate to 3 visible badges + "+N more" chip on mobile product cards
- Nav top strip hides entirely on mobile to preserve vertical space
- Hero banner accent bar shifts from left-edge vertical rule to top-edge horizontal rule on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned HTTP 700 (anti-bot block); zero hex colors, font stacks, or CSS tokens were extracted from the live page
- Primary color (#cc0000) is derived from widely-visible brand identity (logo, trade show materials, product packaging photography) — treat as approximate until extracted from live CSS
- Accent amber (#ff6600) and safety yellow (#ffd100) are inferred from PPE industry conventions and Magid product photography; exact brand values unconfirmed
- Font stack is assumed Helvetica Neue / Arial system fallback — no custom typeface was confirmed; Magid may license a geometric sans (e.g., Proxima Nova, Source Sans) that was not detectable
- Exact nav-bar height, logo dimensions, and grid gutter values are estimated from industrial e-commerce conventions, not measured from live DOM
- Dark-mode or high-contrast accessibility variants are unknown
- Mobile-specific color overrides or reduced-palette behavior on native app (if any) are undocumented
