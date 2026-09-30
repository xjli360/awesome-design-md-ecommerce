---
version: alpha
name: "Midea"
source_url: "https://www.midea.com/us"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Eight distinct blues — #1f94d2, #0083de, #0092d8, #00b0f0, #37a6f3, #077dce, #2b85c3, #498ff2 — layer across hero modules, CTA buttons, interactive badges, and link states to build visual depth from a single hue family rather than contrast from opposing colors. The primary is #1f94d2, a sky-toned technical blue that reads as mechanical precision without the coldness of navy. Against it, a differentiated surface hierarchy — #f7f7f7 base, #e9f4fb blue-wash panels, crisp white cards — creates the layering typical of appliance catalog retail without requiring color noise. Red (#ec1c24) appears exclusively for promotional badges and urgency callouts, keeping it semantically loaded rather than decorative; amber (#faad14) handles star ratings and warning states; green (#52c41a) confirms success states like cart additions and compatibility checks.

  Typography is set in BeausiteClassic, a geometric sans-serif with an unusually wide weight range — Light through Ultrablack — allowing Midea to run hero headlines at near-display weight without switching to a separate display typeface. The Ultrablack cut appears at the largest category-lockup sizes; Regular and Medium handle UI labels and navigation prose. HCo Gotham serves as a secondary system face for dense specification text. Buttons carry a mid-radius ({rounded.sm}) rather than pill shapes, reading as action-oriented and technical rather than soft. Product cards take a {rounded.md} with a shallow shadow, keeping the catalog register of an appliance configurator. The blue-wash surface ({colors.surface-blue-wash}) is the brand's most distinctive UI device — it backgrounds specification panels and feature comparison tables, marking them as authoritative content rather than promotional copy.

  Pricing and BTU figures carry typographic weight via the price-display scale; copy density is high throughout product detail and comparison views. White space tightens around feature lists rather than expanding for atmosphere — the system behaves as a specification-forward catalog where clarity of wattage, coverage area, and energy-rating number is the primary UX value. The red-on-white promotional badge ({colors.accent-red} on {colors.canvas}) is the only place urgency surfaces visually; everything else defers to the blue system for hierarchy and trust.

colors:
  primary: "#1f94d2"
  primary-hover: "#0083de"
  primary-active: "#077dce"
  primary-disabled: "#79bfe4"
  accent-red: "#ec1c24"
  accent-amber: "#faad14"
  accent-green: "#52c41a"
  accent-orange: "#ff7700"
  ink: "#313131"
  body: "#707070"
  muted: "#858585"
  muted-soft: "#adadad"
  hairline: "#d6d6d6"
  hairline-soft: "#c2c2c2"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-blue-wash: "#e9f4fb"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'BeausiteClassic-Ultrablack', 'BeausiteClassic-Bold', sans-serif"
    fontSize: 52px
    fontWeight: 900
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'BeausiteClassic-Bold', sans-serif"
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.13
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'BeausiteClassic-Bold', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'BeausiteClassic-Bold', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'BeausiteClassic-Medium', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'BeausiteClassic-Medium', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "'BeausiteClassic-Regular', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'BeausiteClassic-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'BeausiteClassic-Regular', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-lg:
    fontFamily: "'BeausiteClassic-Medium', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'BeausiteClassic-Medium', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'BeausiteClassic-Medium', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  nav-link:
    fontFamily: "'BeausiteClassic-Medium', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'BeausiteClassic-Bold', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  tag:
    fontFamily: "'BeausiteClassic-Bold', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'HCo Gotham', 'BeausiteClassic-Regular', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
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
    padding: 13px 28px
    height: 48px
    hoverBackgroundColor: "{colors.primary-hover}"
    activeBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: 1.5px solid {colors.primary}
    padding: 12px 27px
    height: 48px
    hoverBackgroundColor: "{colors.surface-blue-wash}"
    hoverBorder: 1.5px solid {colors.primary-hover}

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 0
    textDecoration: underline

  button-cta-large:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 40px
    height: 56px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    focusBorder: 1.5px solid {colors.primary}
    padding: 11px {spacing.base}
    height: 44px

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    activeTextColor: "{colors.primary}"
    logoHeight: 32px
    dropdownBackgroundColor: "{colors.canvas}"
    dropdownBorderRadius: "{rounded.sm}"
    dropdownShadow: 0 4px 16px rgba(0,0,0,0.10)

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: 1px solid {colors.hairline}
    shadow: 0 2px 8px rgba(0,0,0,0.07)
    hoverShadow: 0 6px 20px rgba(31,148,210,0.13)
    imageAspectRatio: 1/1
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.body-sm}"
    badgePosition: top-left

  hero-banner:
    backgroundColor: "{colors.surface-blue-wash}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaVariant: button-primary
    minHeight: 480px
    imageSide: right
    contentPadding: "{spacing.xxl} {spacing.xxl}"

  spec-panel:
    backgroundColor: "{colors.surface-blue-wash}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.md}"
    border: 1px solid {colors.primary-disabled}
    padding: "{spacing.lg}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.title-sm}"

  promo-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.tag}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  energy-rating-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.tag}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.hairline}
    padding: 4px 10px

  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    focusBorder: 1.5px solid {colors.primary}
    height: 44px
    iconColor: "{colors.primary}"
    padding: 0 {spacing.base}

  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.md}"
    border: 1px solid {colors.hairline}
    hoverBorderColor: "{colors.primary}"
    hoverShadow: 0 4px 14px rgba(31,148,210,0.15)"
    padding: "{spacing.lg}"
    imageHeight: 140px
    activeAccentColor: "{colors.primary}"

  rating-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    starColor: "{colors.accent-amber}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 8px

  feature-chip:
    backgroundColor: "{colors.surface-blue-wash}"
    textColor: "{colors.primary-active}"
    typography: "{typography.tag}"
    rounded: "{rounded.full}"
    padding: 5px 14px
    border: 1px solid {colors.primary-disabled}

  comparison-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-blue-wash}"
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.spec-label}"
    borderColor: "{colors.hairline}"
    checkColor: "{colors.accent-green}"
    crossColor: "{colors.accent-red}"
    rowAlternateColor: "{colors.surface-soft}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    dividerColor: "#484848"
    padding: "{spacing.xxl} 0"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"

## Components

### Buttons
**`button-primary`** — Solid #1f94d2 fill with white type at `{typography.button-md}`, 48px tall with `{rounded.sm}` corners and 28px horizontal padding. Hover darkens to `{colors.primary-hover}` (#0083de), active state steps further to `{colors.primary-active}` (#077dce), and disabled washes to `{colors.primary-disabled}`. This is the canonical CTA used across hero banners, add-to-cart flows, and product configurators.

**`button-secondary`** — White fill with a 1.5px `{colors.primary}` border and primary-colored type, same sizing as primary. Hover surfaces a `{colors.surface-blue-wash}` tint behind the label to signal interactivity without a fill change. Used for secondary actions like "Learn More" or "Compare" alongside a primary CTA.

**`button-ghost`** — Transparent with primary-colored underlined text at `{typography.button-sm}`. No border, no padding — used inline within specification panels and feature lists where space is constrained and link-style affordance is appropriate.

**`button-cta-large`** — A taller (56px), wider variant using `{typography.button-lg}` for hero and campaign landing modules. Same blue fill system as primary, padding expands to 40px horizontal.

### Text Input
**`text-input`** — Rests on `{colors.canvas}` with a `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border steps to 1.5px `{colors.primary}` to signal active editing. Placeholder text runs in `{colors.muted}`. Height is 44px — slightly shorter than buttons to reflect form-field density.

### Navigation Bar
**`nav-bar`** — White bar at 64px tall with a bottom hairline, logo at 32px height left-aligned. Main category links use `{typography.nav-link}` in `{colors.ink}`; the active link shifts to `{colors.primary}`. Mega-menu dropdowns appear in white cards with `{rounded.sm}` and a 10% opacity shadow, keeping sub-navigation light and scannable.

### Product Card
**`product-card`** — White surface with `{rounded.md}`, a single-pixel hairline border, and a 7% opacity ambient shadow. On hover, the shadow warms toward `{colors.primary}` at 13% opacity, creating a blue-tinted lift. Product name renders in `{typography.title-sm}`, price in `{typography.price-display}`, and subordinate specs (BTU, coverage) in `{typography.body-sm}` with `{colors.body}` tone. Promo badges float top-left using `{colors.accent-red}` fills.

### Hero Banner
**`hero-banner`** — `{colors.surface-blue-wash}` background panels with product imagery right-aligned and headline copy in `{typography.display-xl}`. Minimum height 480px desktop; subhead renders in `{typography.body-md}` at `{colors.body}`. The primary CTA sits below the subhead. The blue-wash background is the brand's clearest signature: it distinguishes hero content from the white product grid without introducing a different color family.

### Spec Panel
**`spec-panel`** — Blue-wash panels (`{colors.surface-blue-wash}`) with a `{colors.primary-disabled}` border used for specification data, feature comparison rows, and energy rating tables. Labels in `{typography.spec-label}` at `{colors.muted}`; values in `{typography.title-sm}` at `{colors.ink}`. The panel reads as authoritative data, not promotion.

### Badges
**`promo-badge`** — Sharp `{rounded.xs}` red (`{colors.accent-red}`) fills with white uppercase `{typography.tag}` text. Reserved strictly for sale pricing and limited-time offers. **`energy-rating-badge`** — Neutral `{colors.surface-soft}` with hairline border; same tag typography in ink. Used for ENERGY STAR status and EER ratings. **`feature-chip`** — `{colors.surface-blue-wash}` fill with primary-toned type on a `{rounded.full}` pill; marks included features on product cards.

### Comparison Table
**`comparison-table`** — Full-width table with blue-wash (`{colors.surface-blue-wash}`) header row, alternating `{colors.surface-soft}` and white body rows. Check marks in `{colors.accent-green}`, X marks in `{colors.accent-red}`, all cell text at `{typography.spec-label}`. Used on category pages to let shoppers differentiate BTU, coverage area, and feature sets across three to five models.

### Search Bar
**`search-bar`** — `{colors.surface-soft}` fill at 44px tall with `{rounded.sm}`, hairline border, and a `{colors.primary}` search icon on the right. Focus state upgrades border to `{colors.primary}`. Sits in the nav bar on desktop and expands to full-width on mobile.

### Rating Chip
**`rating-chip`** — Compact `{colors.surface-soft}` pill at `{rounded.xs}` holding amber stars (`{colors.accent-amber}`) and a numeric score at `{typography.caption}`. Appears beneath product titles on cards and at the top of PDPs.

### Footer
**`footer`** — Dark `{colors.ink}` background with white section headings in `{typography.title-sm}` and body links in `{typography.body-sm}` at `{colors.muted-soft}`, brightening to `{colors.canvas}` on hover. Column dividers use a mid-gray (#484848) to add structure without competing with link legibility.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero banner stacks image above copy; spec panels scroll horizontally; comparison table hidden behind "Compare" drawer |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only, sub-menus in drawer; hero shifts to side-by-side at reduced headline size using `{typography.display-lg}` |
| Desktop | 1128–1440px | Three- to four-column product grid; full mega-menu nav; hero at full `{typography.display-xl}`; comparison table visible inline |
| Wide | > 1440px | Content max-width ~1440px centered; hero image scales proportionally; grid locks at four columns with increased card padding |

### Touch Targets
- All buttons minimum 44×44px; primary and secondary buttons are 48px tall by spec
- Nav items in mobile drawer minimum 48px tall with `{spacing.base}` vertical padding
- Product card interactive area covers the full card face; tappable region not limited to title
- Filter checkboxes and radio selects minimum 44px hit area regardless of visual size
- Icon-only controls (search, cart, wishlist) padded to 44px square

### Collapsing Strategy
- Mega-menu navigation folds into a full-height side drawer on mobile with accordion category expansion
- Horizontal spec-panel rows reflow into stacked key-value pairs below 744px
- Comparison table converts to a swipeable card carousel on mobile, showing two products at a time
- Hero banner image moves above headline copy on mobile; CTA button stretches to full width
- Category tile grid shifts from four columns (desktop) → two (tablet) → one (mobile)
- Footer columns stack vertically with accordion expand/collapse per section on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius values not confirmed from CSS inspection; `{rounded.sm}` (8px) is inferred from visual screenshots
- BeausiteClassic is a licensed proprietary font — exact font-weight numeric values (e.g. 100/300/400/500/900) are inferred from weight-name suffixes (Light, Regular, Medium, Bold, Ultrablack); confirm against actual font files
- HCo Gotham usage scope uncertain — may be limited to a specific content region or legacy page; treat as secondary/fallback only
- No dark-mode color set detected; site appears to be light-only
- Hover and focus state colors for secondary button and text-input not directly observed; inferred from primary color system
- Mobile navigation drawer animation timing and easing not extractable from static analysis
- Exact shadow values for product cards and dropdowns estimated from visual inspection; confirm with dev tools measurement
- Icon system (iconfont-midea) glyph set and naming conventions unknown; custom icon font requires separate design handoff
- Promotional pricing display rules (original vs. sale price formatting, strike-through style) not fully documented
- Cart and checkout UI components not extracted; Shopify default components may override brand styling in those flows
