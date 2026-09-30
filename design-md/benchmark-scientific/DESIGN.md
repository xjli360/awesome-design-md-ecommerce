---
version: alpha
name: "Benchmark Scientific"
source_url: "https://www.benchmarkscientific.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Benchmark Scientific's interface runs a Bootstrap 3 chassis dressed in two uncommonly vivid brand overlays — a lime-chartreuse `#8fd300` that surfaces on callout badges, promo banners, and category highlights, and a cyan-teal `#0198ab` that anchors links, nav accents, and primary CTAs. The rest of the palette is composed almost entirely from Bootstrap's native state system — success greens (`#5cb85c`, `#3c763d`), danger reds (`#d9534f`, `#a94442`), warning ambers (`#f0ad4e`, `#8a6d3b`), info blues (`#5bc0de`, `#31708f`) — giving the interface a dense, information-prioritized character that serves purchasing managers and lab technicians over lifestyle browsers. A deep navy `#044a80` and Bootstrap's link blue `#337ab7` handle corporate hierarchy, while near-black `#080808` and mid-gray `#555555` carry body text across dense product listings. Typography anchors on Roboto for UI copy and reaches for Reem Kufi at display scale — an unexpected pairing that gives top-level headings a geometric, slightly calligraphic weight while keeping body copy scannable at specification density. Monospace stacks (Consolas, Courier New, Menlo, Monaco) surface in product-specification tables and part-number fields, signaling technical precision where the audience requires it. Corners stay tight throughout at `{rounded.xs}` (4px) — squared components signal professional seriousness rather than consumer warmth. The `#8fd300` lime accent and the `#044a80` navy create a bookend motif: a 4px lime bar tops the hero banner and a matching 4px lime stripe crowns the footer, stitching the page into a coherent frame. The overall register is dense, navigable, and functional: a catalog built for someone who needs to find the correct centrifuge rotor before the sample degrades.

colors:
  primary: "#0198ab"
  primary-active: "#017a8a"
  primary-disabled: "#80ccda"
  accent: "#8fd300"
  accent-dark: "#96bf0d"
  brand-navy: "#044a80"
  link: "#337ab7"
  link-active: "#286090"
  ink: "#080808"
  body: "#555555"
  muted: "#777777"
  muted-mid: "#9d9d9d"
  hairline: "#e7e7e7"
  hairline-light: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-muted: "#e5e5e5"
  on-primary: "#ffffff"
  success: "#5cb85c"
  success-text: "#3c763d"
  success-bg: "#dff0d8"
  success-border: "#d6e9c6"
  warning: "#f0ad4e"
  warning-text: "#8a6d3b"
  warning-bg: "#fcf8e3"
  danger: "#d9534f"
  danger-text: "#a94442"
  danger-bg: "#f2dede"
  info: "#5bc0de"
  info-text: "#31708f"
  info-bg: "#d9edf7"
  info-border: "#bce8f1"

typography:
  display-xl:
    fontFamily: "'Reem Kufi', 'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Reem Kufi', 'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  mono:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  part-number:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, monospace"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
  badge:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  label:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0
  button-md:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  button-sm:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    padding: 8px 16px
    height: 36px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 7px 15px
    height: 36px
    border: "1px solid {colors.hairline}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
    border: none
  button-accent-hover:
    backgroundColor: "{colors.accent-dark}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  button-navy:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.button-md}"
    border: none
    padding: 0
  button-sm-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    height: 28px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    outlineFocus: "0 0 0 3px rgba(1,152,171,0.25)"
    placeholderColor: "{colors.muted}"
  nav-bar-top-stripe:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    padding: "0 {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 50px
    logoZone: left
    searchZone: center
    ctaZone: right
    activeLinkIndicator: "{colors.accent}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-light}"
    padding: "{spacing.base}"
    imageAspect: "4/3"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    partNumberTypography: "{typography.part-number}"
    partNumberColor: "{colors.muted}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.primary}"
    ctaTypography: "{typography.button-md}"
    badgeStack: top-left
  hero-banner:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    accentBar: "{colors.accent}"
    accentBarHeight: 4px
    accentBarPosition: top
    padding: "{spacing.xxl} {spacing.xl}"
    minHeight: 320px
  category-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  promo-badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  alert-success:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.success-border}"
    padding: "12px 20px"
    iconColor: "{colors.success}"
  alert-warning:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.warning-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.warning}"
    padding: "12px 20px"
  alert-danger:
    backgroundColor: "{colors.danger-bg}"
    textColor: "{colors.danger-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.danger}"
    padding: "12px 20px"
  alert-info:
    backgroundColor: "{colors.info-bg}"
    textColor: "{colors.info-text}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.info-border}"
    padding: "12px 20px"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBg: "{colors.surface-soft}"
    rowAltBg: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    keyTypography: "{typography.label}"
    keyColor: "{colors.body}"
    valueTypography: "{typography.mono}"
    valueColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    cellPadding: "8px 12px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: "6px 12px"
    height: 40px
    buttonBg: "{colors.primary}"
    buttonColor: "{colors.on-primary}"
    buttonRounded: "{rounded.xs}"
    placeholderColor: "{colors.muted}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.body}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted-mid}"
    padding: "{spacing.sm} 0"
  footer:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-muted}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderTop: "4px solid {colors.accent}"
    columns: 4

## Components

### Buttons

**`button-primary`** — The main CTA renders in teal `#0198ab` with white text at `{typography.button-md}`, 4px radius (`{rounded.xs}`), and a 36px height following Bootstrap's default button sizing. Hover darkens to `#017a8a` (`colors.primary-active`); disabled washes to `#80ccda` (`colors.primary-disabled`) with `cursor: not-allowed`. Used for "Add to Cart," "View Details," and primary form submissions.

**`button-accent`** — Lime-chartreuse `#8fd300` fill with near-black `#080808` text for maximum contrast against the vivid ground. Hover shifts to `#96bf0d` (`colors.accent-dark`). Used for promotional CTAs, "Shop the Category," and homepage feature callouts where the brand wants maximum visual interrupt.

**`button-navy`** — Deep navy `#044a80` fill for institutional-weight actions: Request Quote, Contact Sales, Download Catalog. Signals a slower, relationship-oriented flow versus the teal transactional CTAs.

**`button-secondary`** — White background, `#555555` text, 1px `#e7e7e7` border. Sits alongside `button-primary` in product-detail sidebars for secondary actions like "Download SDS" or "View Manual." Hover lightens the border to `#eeeeee` with a subtle background shift to `{colors.surface-soft}`.

**`button-sm-outline`** — Small 28px outlined teal button used in product list rows for inline actions (Compare, Quick View). Transparent background, 1px `{colors.primary}` border, `{typography.button-sm}` text.

**`button-link`** — Transparent, link-blue `#337ab7` text, no padding. Used for inline text actions and "See all results" anchors within content blocks.

### Inputs

**`text-input`** — Standard Bootstrap form control: white background, 1px `#e7e7e7` border, 36px height, 4px radius, `{typography.body-md}` Roboto. Focus ring shifts border to `{colors.primary}` teal with a soft `rgba(1,152,171,0.25)` box-shadow halo. Part-number and catalog-search fields use the same control with a `{typography.mono}` Consolas font override to visually anchor technical strings.

### Navigation

**`nav-bar-top-stripe`** — A 36px teal `#0198ab` announcement bar sitting above the main nav. White `{typography.caption}` text carries shipping thresholds, trade-program callouts, or limited-time offers. Collapses on mobile to recover vertical space.

**`nav-bar`** — 50px deep-navy `#044a80` primary navigation bar: logo left, category links and search center, account/cart icons right. `{typography.nav-link}` 14px Roboto medium in white. The active category link gains a 3px lime-`#8fd300` bottom border as an understated active indicator that echoes the hero accent bar.

**`breadcrumb`** — 12px muted `#777777` text, "/" separator in `#9d9d9d`, with the current-page segment stepping up to `#555555`. Sits between nav-bar and page H1 with `{spacing.sm}` vertical padding. Provides the primary spatial orientation cue in deep category hierarchies.

### Product Cards

**`product-card`** — White card, 1px `#eeeeee` border, 4px radius, `{spacing.base}` padding on all sides. Product image at top in a 4:3 aspect-ratio zone against `{colors.surface-soft}` background. Below the image: part number in 12px Consolas (`{typography.part-number}`) in `{colors.muted}`, product title in `{typography.title-sm}` Roboto semibold, price in `{typography.title-md}` teal `#0198ab`. A `button-primary` CTA anchors the card bottom. Category and "New" badges (`category-badge`, `new-badge`) stack in the image's top-left corner.

### Hero Banner

**`hero-banner`** — Deep navy `#044a80` full-width banner with a 4px lime `#8fd300` top accent bar — the brand's clearest visual signature. Display headline in `{typography.display-xl}` Reem Kufi white; subtitle in `{typography.body-md}` Roboto white. Minimum height 320px; padding `{spacing.xxl}` vertical, `{spacing.xl}` horizontal. A CTA button zone typically renders `button-primary` and `button-accent` side by side, the teal/lime pairing reinforcing brand recognition.

### Alerts

**`alert-success`** / **`alert-warning`** / **`alert-danger`** / **`alert-info`** — Full Bootstrap 3 contextual alert set, all at `{rounded.xs}` with 12px/20px padding. Success: `#dff0d8` bg / `#3c763d` text / `#d6e9c6` border. Warning: `#fcf8e3` / `#8a6d3b` / amber border. Danger: `#f2dede` / `#a94442` / red border. Info: `#d9edf7` / `#31708f` / `#bce8f1` border. FontAwesome glyphs prefix each message. Used throughout checkout flows, product availability notices, and compliance warnings.

### Spec Table

**`spec-table`** — Two-column key-value layout for product technical specifications. Header row and alternating body rows use `#f5f5f5` (`{colors.surface-soft}`). Keys render in 13px bold Roboto (`{typography.label}`) in `#555555`; values render in 13px Consolas (`{typography.mono}`) in `#080808`. Row and column borders use 1px `{colors.hairline}`. Used for centrifuge speeds, temperature ranges, rotor compatibility matrices, and catalog part-number cross-references.

### Search

**`search-bar`** — 40px tall, white background, 2px solid `#0198ab` border at `{rounded.xs}`, with a teal square-cornered submit button flush to the right. Input uses `{typography.body-md}` Roboto with `#777777` placeholder text. Appears in the `nav-bar` at compact width and expands to full-width below the nav on category landing pages.

### Footer

**`footer`** — Deep navy `#044a80` background crowned by a 4px lime `#8fd300` top border, mirroring the hero banner's accent bar motif and creating a visual bookend on long catalog pages. Section headings in `{typography.title-sm}` white; link lists in `{typography.body-sm}` muted `#e5e5e5`, brightening to white on hover. Four-column grid on desktop; collapses to two columns on tablet and a single accordion stack on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; top teal stripe hidden; search bar expands to full width below nav; hero headline drops to `display-md`; spec tables switch to stacked key-above-value layout |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only with overflow in hamburger; hero at full height; footer collapses to two columns |
| Desktop | 1128–1440px | Three- to four-column product grid; full two-tier nav visible; sidebar category filters rendered inline left; spec tables in two-column layout |
| Wide | > 1440px | Container max-width ~1200px, centered with canvas gutters; layout identical to Desktop; no additional grid columns |

### Touch Targets

- All buttons minimum 36px height; 44px recommended for mobile overrides on key CTAs
- Nav links minimum 44px tap target achieved via vertical padding expansion
- Product card CTAs stretch to full card width on mobile for easy thumb reach
- Form inputs override to 44px height on mobile (Bootstrap default 36px)
- Badge/filter chips minimum 36px height on mobile with 8px horizontal spacing between chips

### Collapsing Strategy

- Top teal announcement stripe (`nav-bar-top-stripe`) hidden below 744px to recover vertical space
- Primary nav collapses to Bootstrap `navbar-collapse` hamburger drawer on mobile
- Left-rail category filters collapse to a slide-up bottom-sheet drawer on mobile, triggered by a sticky "Filter" button
- Spec tables switch from two-column grid to stacked key-above-value card format on screens below 744px
- Four-column footer: 4 → 2 (tablet) → 1 (mobile) with Bootstrap collapse accordion per section
- Product card grid: 4-up (wide) → 3-up (desktop) → 2-up (tablet) → 1-up (mobile)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; primary brand CTA color `#0198ab` inferred from most distinctive non-Bootstrap hex in extraction
- Reem Kufi loaded via Google Fonts; exact weight variants (400 vs. 700) and which page elements use it vs. Roboto not confirmed from static extraction alone
- `#8fd300` and `#96bf0d` both appear — likely base/hover variants of the lime accent; exact per-state mapping unconfirmed
- Bootstrap 3 state palette (`success`, `warning`, `danger`, `info`) dominates the extraction; true brand-custom color count is limited to approximately 3–4 tones (`#0198ab`, `#8fd300`, `#044a80`, `#96bf0d`)
- Product photography treatment — white background, shadow style, aspect ratio — not confirmed from extraction
- Price display format, currency symbols, and B2B/tiered-pricing display patterns not available
- Icon system relies on FontAwesome + Bootstrap Glyphicons; no custom icon set observed
- Mobile nav drawer interaction pattern (slide-in vs. overlay vs. push) not confirmed
- No motion or animation tokens extractable from static analysis
- Form validation UX details (inline vs. toast, timing) not observed
