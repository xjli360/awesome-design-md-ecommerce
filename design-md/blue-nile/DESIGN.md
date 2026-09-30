---
version: alpha
name: "Blue Nile"
source_url: "https://bluenile.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every product page on Blue Nile reads like a certification document first and a display case second — cut grade, clarity, table percentage, and depth ratio are all surfaced before lifestyle photography appears — which makes the interface's design task clarification through restraint rather than aspiration through ornament. The deep navy primary (#002D62) carries institutional authority without opulence; paired with a warm champagne gold (#C9A055), it positions the brand in the same register as a private banking letterhead rather than a heritage jeweler with centuries of mystique to lean on. Layouts breathe on generous white canvas (#FFFFFF) and a pale warm surface (#F8F7F4) that recalls the muted warmth of a velvet display board. Serif display type sets headlines with understated gravitas while a clean geometric sans-serif handles the dense specification tables and side-by-side comparison tools that are Blue Nile's actual competitive signature. Rounded corners are conspicuously absent on primary CTAs — square-cornered buttons signal a precision instrument, not a consumer-friendly checkout — while `{rounded.xs}` appears modestly on form inputs and `{rounded.sm}` on informational chips. The diamond search and filter panel, built around shape, carat range, cut grade, color, clarity, and certification lab, dominates UX hierarchy: this site is fundamentally a research engine that also fulfills orders. Trust signals — GIA certification marks, 30-day return indicators, and lifetime warranty callouts — cluster near every price point and repeat through the checkout flow, because the entire brand proposition rests on overcoming the legitimate skepticism of purchasing a significant stone from a screen. Gold (`{colors.gold-accent}`) is used as icon stroke and divider line, never as a solid fill, keeping the luxury register restrained rather than decorative.

colors:
  primary: "#002D62"
  primary-active: "#001F46"
  primary-disabled: "#99AECB"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#6B6B6B"
  muted-soft: "#9A9A9A"
  hairline: "#E5E5E0"
  hairline-soft: "#F0EFEA"
  canvas: "#FFFFFF"
  surface-soft: "#F8F7F4"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  gold-accent: "#C9A055"
  gold-light: "#E8D5A3"
  gold-muted: "#9B7A3C"
  trust-green: "#2E7D32"
  error: "#C62828"

typography:
  display-xl:
    fontFamily: "'Caslon', 'Adobe Caslon Pro', Georgia, 'Times New Roman', serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Caslon', 'Adobe Caslon Pro', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Caslon', 'Adobe Caslon Pro', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.17
    letterSpacing: -0.25px
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    border: "1px solid {colors.primary}"
    height: 48px
  button-gold:
    backgroundColor: "{colors.gold-accent}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 11px 14px
    height: 44px
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    iconColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    imageAspect: "1:1"
    padding: "{spacing.base}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    hoverBorder: "1px solid {colors.primary}"
  diamond-filter:
    backgroundColor: "{colors.canvas}"
    borderRight: "1px solid {colors.hairline}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    activeColor: "{colors.primary}"
    sliderTrackColor: "{colors.primary}"
    sliderHandleBackgroundColor: "{colors.canvas}"
    sliderHandleBorder: "2px solid {colors.primary}"
    checkboxActiveColor: "{colors.primary}"
    width: 260px
    sectionPadding: "{spacing.lg} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline-soft}"
    altRowBackgroundColor: "{colors.surface-soft}"
    padding: "{spacing.sm} {spacing.base}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconColor: "{colors.gold-accent}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    border: "1px solid {colors.hairline}"
  gia-cert-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: "4px {spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.gold-accent}"
    ctaTextColor: "{colors.canvas}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xxl}"
  education-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headingTypography: "{typography.display-sm}"
    headingColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    linkColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.section}"
  ring-builder-step:
    backgroundColor: "{colors.canvas}"
    stepIndicatorActiveColor: "{colors.primary}"
    stepIndicatorInactiveColor: "{colors.hairline}"
    stepTypography: "{typography.spec-label}"
    titleTypography: "{typography.display-sm}"
    titleColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    accentColor: "{colors.gold-accent}"
    height: 40px
    padding: "0 {spacing.lg}"
  footer:
    backgroundColor: "#0A1A30"
    textColor: "#C8D0DC"
    headingTypography: "{typography.spec-label}"
    headingColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    linkColor: "#C8D0DC"
    dividerColor: "#1E3050"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — A square-cornered navy rectangle carrying all-caps tracked type, the same language as a government form or appraisal certificate. This register is deliberate: Blue Nile built its brand on legible authority, not warmth. Active state deepens to `{colors.primary-active}`; disabled washes to a muted powder `{colors.primary-disabled}` with no change in shape.

**`button-secondary`** — Outlined in navy on white, mirroring the primary in shape and typography but stepping back in weight. Carries secondary actions like "Save to Wishlist," "Compare," or "Add to Registry" without competing with the purchase CTA.

**`button-gold`** — Champagne gold fill (`{colors.gold-accent}`) reserved for highest-value conversion moments: the ring builder's final step, engagement-ring landing-page heroes, and holiday promotion CTAs. Adds warmth without decorative excess — still square-cornered, still all-caps.

### Navigation

**`nav-bar`** — White bar with a 1px `{colors.hairline}` bottom border, 64px tall to maximize the product viewport below. The wordmark sits left in `{colors.primary}`; a horizontal category strip (Diamonds, Engagement, Wedding Bands, Jewelry, Gifts) runs center; search, account, and cart icons cluster right. Flyout menus on desktop carry thumbnail imagery and subcategory grids.

### Product Cards

**`product-card`** — Square imagery top-cropped to 1:1, framed by a thin `{colors.hairline}` border with zero border-radius — the card reads as a data record, not a display object. Below the image: stone descriptor in `{typography.spec-label}` uppercase, price in `{typography.price-display}`, and a compact row of the three most critical specs. On hover the border steps to `{colors.primary}` to confirm interactivity without animating.

### Diamond Filters

**`diamond-filter`** — The fixed 260px left-rail panel is the backbone of the shopping experience. Range sliders govern carat and price; checkbox grids handle shape (with small silhouette icons), cut, color, clarity, and certification lab. Active selections in `{colors.primary}`; slider handles are white with a navy 2px border. This panel is the primary reason users return to Blue Nile over a physical retailer.

### Specification Tables

**`spec-table`** — Two-column key/value layout rendering the full diamond certificate: 15–20 rows covering table %, depth %, girdle, fluorescence, culet, symmetry, and polish. Labels in `{typography.spec-label}` uppercase; values in `{typography.body-sm}`. Alternating rows use `{colors.surface-soft}` and `{colors.canvas}` for scan-ability across dense data.

### Trust Signals

**`trust-badge`** — Soft-background chips in `{colors.surface-soft}` with a gold icon stroke (`{colors.gold-accent}`) carrying return policy, free shipping threshold, and warranty callouts. They appear as a horizontal band above the fold on product pages and repeat in the checkout summary sidebar.

**`gia-cert-badge`** — An outlined navy micro-badge confirming GIA grading report number. Links through to the GIA public lookup. Placed immediately below the price — its proximity to the price is intentional, anchoring trust at the moment of sticker shock.

### Hero & Education

**`hero-banner`** — Full-bleed navy background with a white serif display headline and a gold CTA. Used on engagement ring landing pages and seasonal campaign pages. Photography, if present, bleeds to the right on desktop; on mobile the image stacks below the copy. The typographic hierarchy — display serif for the headline, sans for the body — does the persuasive work without illustration.

**`education-callout`** — Warm soft-background bands (`{colors.surface-soft}`) explaining the 4Cs, grading scales, or ring-sizing guidance. Heading in `{typography.display-sm}` serif, body in `{typography.body-md}` sans, with `{colors.primary}` text links to deep-dive articles. These panels appear between product grids to slow browsing and build confidence.

### Ring Builder

**`ring-builder-step`** — A multi-step wizard guiding: choose a setting → choose a diamond → review. Step indicators are small navy dots (active) and hairline dots (inactive). Each step exposes a browsable grid, a persistent summary panel showing current selections and running price, and a "Next" primary button. The ring builder is the highest-revenue flow on the site and deserves no visual clutter.

### Promotional & Footer

**`promo-banner`** — A slim 40px navy bar pinned to the very top of the viewport for time-sensitive messaging (free overnight shipping, seasonal promotions). White body text with gold accents for offer callouts. Dismissible on mobile.

**`footer`** — Deep midnight (#0A1A30) background, darker than `{colors.primary}`, with muted slate link columns. Four columns on desktop: Company, Help, Diamond Education, and Policies. A bottom row carries trust-mark logos (BBB, GIA partner seal, press mentions). All link typography in `{typography.body-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column diamond grid; filter panel slides in as full-screen drawer triggered by "Filter" button; nav collapses to hamburger + search icon; spec table hides tertiary rows behind "Show more" |
| Tablet | 744–1128px | Two-column diamond grid; filter panel toggles as collapsible sidebar at 220px; nav shows top-level categories horizontally with overflow into "More" |
| Desktop | 1128–1440px | Three-column diamond grid with fixed 260px filter sidebar; full nav with flyout menus; product page shows image gallery left, spec panel and CTA right |
| Wide | > 1440px | Content capped at 1440px, centered with generous side padding; four-column diamond grid; hero-banner text column max-width 640px |

### Touch Targets

- All filter checkboxes and range-slider handles minimum 44px interactive hit area
- Diamond shape icon selectors 56×56px on mobile
- Nav drawer items full-width tap zones at 56px height
- CTA buttons maintain 48px height across all breakpoints
- Wishlist and compare icon buttons minimum 44×44px

### Collapsing Strategy

- Diamond filter panel is the primary collapsing surface: full-screen drawer on mobile, toggle sidebar on tablet, fixed left rail on desktop
- Ring builder step labels compress from text + number to number-only dots below 744px; summary panel moves from sticky side rail to sticky bottom bar
- Spec tables hide tertiary rows (polish, culet, girdle detail) behind "Show all specs" below 744px
- Education callout sections reduce padding from `{spacing.section}` to `{spacing.xl}` on mobile
- Footer four-column grid becomes a single-column accordion on mobile with section headings as tap targets

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (likely JS-injected design tokens or anti-bot protection); all palette values are derived from Blue Nile's widely-observed brand identity and must be verified against the live computed stylesheet
- Exact font families were not extracted; display serif is estimated as a Caslon or Garamond variant consistent with the brand's positioning — verify via the live site's `@font-face` declarations or a brand guide
- Gold accent value (#C9A055) is approximate; actual brand gold may be cooler or warmer — extract from the SVG logo or a brand asset package
- Primary navy (#002D62) is a widely-cited estimate; confirm against `background-color` computed value on the primary CTA
- Hover and focus-ring animation durations (filter panel open/close, card hover transitions) are not specified and should be observed live
- Ring-builder step-transition animations and the diamond 360° viewer interaction model are not captured here
- Mobile promo-banner dismiss behavior and cookie persistence are not specified
