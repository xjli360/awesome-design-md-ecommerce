---
version: alpha
name: "Arctic"
source_url: "https://www.arctic.de"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Bright mint green (#6ed59f) against deep-navy (#242e39) — Arctic's color system reads like a server-room status LED: one saturated accent does all the signaling while the near-black substrate recedes completely. The palette extends methodically to three supporting accents that each carry a distinct product-state function: coral (#f27f7f) for warnings and out-of-stock notices, ice blue (#76bce7) for informational callouts and compatibility chips, and amber (#fcc679) for ratings and promotional banners. A darker forest green (#2c5540) anchors hover and active states for primary actions, pulling the mint back toward credibility rather than candy. Pale mint (#e2f7ec) surfaces as a chip tint — the brand's green reduced to a whisper for category labels and filter tags that need presence without weight. Lato runs the entire type system at weights 400 and 700, no display face, no italic: product headings and thermal-resistance spec rows share exactly the same geometric skeleton, which reads as deliberate parsimony given the engineering "Value Quality Performance" positioning. Cards and inputs sit at `{rounded.sm}` (8px) — firm enough to feel machined, never cold or institutional. Navigation and footers ground permanently in dark-base (#242e39) and dark-deep (#161c22), while product listing areas surface on near-white (#f9f9f9) to give studio renders and technical photography maximum contrast. The overall register sits between aggressive gaming-peripheral neon and antiseptic enterprise-IT white — a dark-tech aesthetic calibrated for repeat buyers who compare airflow CFM and static pressure before checkout.

colors:
  primary: "#6ed59f"
  primary-active: "#2c5540"
  primary-disabled: "#d4e2e2"
  ink: "#111111"
  body: "#1c1c1c"
  muted: "#798490"
  muted-light: "#bcc1c7"
  hairline: "#e6e6e6"
  hairline-strong: "#bec0c2"
  canvas: "#f9f9f9"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#1c1c1c"
  dark-base: "#242e39"
  dark-deep: "#161c22"
  dark-mid: "#233342"
  dark-muted: "#4a545b"
  dark-text: "#798490"
  accent-ice: "#76bce7"
  accent-coral: "#f27f7f"
  accent-amber: "#fcc679"
  accent-mint-soft: "#e2f7ec"
  accent-forest: "#2c5540"

typography:
  display-xl:
    fontFamily: "'Lato', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Lato', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
  label-upper:
    fontFamily: "'Lato', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Lato', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0
  spec-label:
    fontFamily: "'Lato', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Lato', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  price-lg:
    fontFamily: "'Lato', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1
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
    padding: 12px 24px
    height: 44px
    hoverBackground: "{colors.primary-active}"
    hoverTextColor: "#ffffff"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "#ffffff"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.dark-base}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.dark-base}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
    hoverBackground: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    hoverTextColor: "{colors.ink}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  search-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline-strong}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 40px 10px 14px
    height: 40px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.dark-base}"
    textColor: "#ffffff"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "none"
    activeUnderlineColor: "{colors.primary}"
    dropdownBackground: "{colors.dark-deep}"
    dropdownTextColor: "#ffffff"
    dropdownHoverBackground: "{colors.dark-mid}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    imageBackground: "{colors.canvas}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-lg}"
    priceColor: "{colors.ink}"
    badgeBackground: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.caption-bold}"
    badgeRounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero-dark:
    backgroundColor: "{colors.dark-base}"
    textColor: "#ffffff"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.dark-text}"
    accentLineColor: "{colors.primary}"
    accentLineWidth: 4px
    padding: "{spacing.xxl} 0"
  hero-split:
    backgroundColor: "{colors.dark-deep}"
    textColor: "#ffffff"
    headlineTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.dark-text}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
  category-badge:
    backgroundColor: "{colors.accent-mint-soft}"
    textColor: "{colors.accent-forest}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-promo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-warning:
    backgroundColor: "{colors.accent-coral}"
    textColor: "#ffffff"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-info:
    backgroundColor: "{colors.accent-ice}"
    textColor: "#ffffff"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  spec-table:
    backgroundColor: "{colors.canvas}"
    rowAltBackground: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    cellPadding: 10px 14px
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.body-sm}"
    sectionTitleTypography: "{typography.caption-bold}"
    sectionTitleColor: "{colors.muted}"
    checkboxActiveColor: "{colors.primary}"
    checkboxBorderColor: "{colors.hairline-strong}"
    dividerColor: "{colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline-strong}"
  rating-stars:
    starFillColor: "{colors.accent-amber}"
    starEmptyColor: "{colors.hairline}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  product-gallery-thumb:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    activeBorder: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
  cart-summary:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-lg}"
    dividerColor: "{colors.hairline}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
    ctaTypography: "{typography.button-md}"
  footer:
    backgroundColor: "{colors.dark-deep}"
    textColor: "#ffffff"
    linkColor: "{colors.muted-light}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.caption-bold}"
    headingColor: "#ffffff"
    bodyTypography: "{typography.body-sm}"
    dividerColor: "{colors.dark-mid}"
    bottomBarBackground: "{colors.dark-base}"
    bottomBarTextColor: "{colors.muted}"
    bottomBarTypography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — Mint green (#6ed59f) fill with dark `{colors.on-primary}` text, 44px height, `{rounded.sm}` corners, weight-700 label at 14px. On hover, background deepens to forest green (#2c5540) and text flips to white — a two-step shift that signals depth without requiring animation. The active variant (`button-primary-active`) holds the forest green permanently. Disabled state uses pale mint (#d4e2e2) with muted text and a not-allowed cursor; it does not add opacity so the palette remains coherent at reduced prominence.

**`button-secondary`** — Transparent with a 2px solid dark-base (#242e39) border on light surfaces; the `button-secondary-on-dark` variant inverts to a 2px solid primary (#6ed59f) border on dark backgrounds, filling with mint on hover for a contained flash of the brand accent. Both share `{typography.button-md}` weight 700. Used for "Compare", "Download Driver", and filter-apply actions that sit alongside a primary CTA.

**`button-ghost`** — Text-only, no border, muted gray color. Used for contextual low-priority actions: clear-filter links, "Show all" triggers, and secondary nav actions where adding visual weight would crowd dense product listing pages.

### Product Card

**`product-card`** — White surface, 1px hairline border, `{rounded.sm}` corners. Border upgrades to 1px primary-green on hover without a box-shadow, keeping the interaction firm and flat. Image area renders on `{colors.canvas}` (#f9f9f9) to isolate product renders that often arrive with pure-white backgrounds. Title runs `{typography.title-sm}` weight 700; price runs `{typography.price-lg}` at 24px bold. Promo and NEW badges occupy the top-left corner in `{rounded.xs}` chips — mint for promotions, amber for new arrivals, coral for stock warnings. Entire card surface is a tappable link.

### Navigation

**`nav-bar`** — Fully opaque dark-base (#242e39) at 64px height, white type at `{typography.nav-link}` weight 700. The active product category receives a bottom-border underline in mint (#6ed59f) — the only decorative element on the bar. Mega-menu dropdowns open against dark-deep (#161c22) with hover rows highlighted in dark-mid (#233342), creating a three-depth tonal stack without any blur or transparency. No sticky shrink behavior; the bar holds fixed height and opacity at all scroll positions.

### Spec Table

**`spec-table`** — The most typographically specific component. Labels use `{typography.spec-label}` (11px, uppercase, 0.8px letter-spacing, weight 700, muted gray) while values use `{typography.spec-value}` (13px, weight 400). Alternating rows use `{colors.surface-soft}` (#eeeeee) for scanability at a glance. Used on product detail pages for airflow (CFM), static pressure (mm H₂O), noise level (dBA), and thermal resistance values — the data-heavy content that Arctic's audience actually reads before purchasing.

### Badges

**`category-badge`** — Pale mint (#e2f7ec) background with dark forest text (#2c5540) in `{typography.label-upper}` uppercase. Used in category navigation and product-list filter chips to identify product families (Fan, CPU Cooler, Case, Thermal Compound, Mount). **`badge-promo`** uses full primary green. **`badge-warning`** uses coral (#f27f7f) for out-of-stock and low-inventory flags. **`badge-info`** uses ice blue (#76bce7) for compatibility notices such as socket support. **`badge-new`** uses amber (#fcc679) with dark ink text for new product launches.

### Hero Sections

**`hero-dark`** — Full-bleed dark-base (#242e39) with white headline at `{typography.display-xl}` and body copy at `{typography.body-md}` in muted dark-text (#798490). A 4px mint accent line (`{colors.primary}`) anchors the left edge of the headline block as the sole decorative element — a structural gesture rather than an ornament. **`hero-split`** drops to dark-deep (#161c22) with a product render positioned to overlap the bottom edge of the hero, appropriate for featured product launches and seasonal cooling campaigns.

### Filter Sidebar

**`filter-sidebar`** — Light canvas background with section headers in `{typography.caption-bold}` uppercase muted text. Checkboxes and range sliders use `{colors.primary}` mint when active. Dividers are `{colors.hairline}` (#e6e6e6). On mobile the sidebar collapses into a full-screen overlay drawer triggered by a filter button; on tablet it becomes a collapsible accordion above the product grid.

### Footer

**`footer`** — Two-tone dark foundation: main body on dark-deep (#161c22) with link columns in `{typography.body-sm}`, link color defaulting to muted-light (#bcc1c7) and turning mint on hover. Column headings run `{typography.caption-bold}` uppercase white. The bottom bar lifts one shade to dark-base (#242e39) for legal/copyright text in `{typography.caption}` muted gray — a clear visual separation between navigation links and legal boilerplate without an explicit rule.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar becomes full-screen overlay drawer; nav collapses to hamburger with accordion sub-items; hero headline scales to `{typography.display-md}`; spec tables scroll horizontally with sticky first-column labels; cart summary becomes sticky bottom bar |
| Tablet | 744–1128px | Two-column product grid; filter sidebar renders as collapsible accordion above grid; nav retains top bar with condensed labels; hero may stack text and image vertically |
| Desktop | 1128–1440px | Three-column product grid; filter sidebar fixed at 240px left; full nav with mega-menu dropdowns; hero runs `{typography.display-xl}` |
| Wide | > 1440px | Content max-width capped at 1440px and centered; product grid may extend to four columns; hero image scales to fill without cropping |

### Touch Targets

- All buttons minimum 44px height, 44px width
- Navigation items on mobile minimum 48px tap height
- Filter checkboxes padded to 40px tap area
- Product card entire surface is a single tappable link, not just the title or image
- Gallery thumbnails minimum 40px on each axis with `{spacing.xs}` gap

### Collapsing Strategy

- Mega-nav dropdowns collapse to hamburger with accordion sub-items below 1024px
- Filter sidebar collapses to full-screen overlay drawer below 744px
- Spec table scrolls horizontally with sticky first-column label below 744px
- Hero split stacks to image-above, text-below below 744px
- Cart summary sidebar collapses to sticky bottom bar on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom display or campaign typeface found; only Lato was extracted. It is unclear whether Arctic uses a bespoke face for offline campaigns or product launch visuals not loaded on the main catalog pages.
- Icon system not extractable from color/font hints; Arctic likely maintains a custom SVG icon set for product category glyphs — actual shapes, stroke weights, and filled vs. outline treatment are unknown.
- Exact border-radius values not confirmed from CSS; `{rounded.sm}` (8px) is inferred from the engineering-utilitarian aesthetic and is an estimate.
- Precise nav height (64px) is estimated; live measurement from rendered DOM was not available.
- No CSS transition timing (duration, easing curves) extracted — animation values are absent from the provided hints.
- Whether dark navy surfaces represent a permanent brand choice or a togglable dark mode is unconfirmed; no theme-color meta tag was present.
- Product photography art direction (lifestyle vs. pure render vs. white-background studio) is not determinable from color extraction alone.
- Mobile breakpoint pixel values are inferred from hardware e-commerce category norms; Arctic's actual CSS breakpoint thresholds may differ.
