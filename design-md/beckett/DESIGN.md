---
version: alpha
name: "Beckett"
source_url: "https://www.beckett.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The teal-and-gold slab label on a BGS 9.5 Pristine — that physical artifact, pulled from the flip of a poly bag — is the exact visual grammar Beckett's digital platform inherits. A signature #069697 teal runs every primary CTA and active state, deepening to #057b7c on press, while #b6975b bronze-gold marks the premium tier: Pristine grade callouts, high-tier auction lots, and top-shelf subscription features. The canvas oscillates between near-black (#1c1b1e) hero sections and a cool light gray (#f4f4f4) data surface, creating a magazine-and-spreadsheet dual register appropriate for an audience that collects and prices simultaneously. Helvetica Neue carries all the typographic weight — no custom brand face in sight — which forces the color system to do the identity work alone; the teal family spans three steps from the dark anchor (#057b7c) through mid-brand (#069697) to an airy highlight (#54c4c8) and a near-white mint wash (#ddf3f4), providing depth without a second typeface. Navy (#14233c) backstops hero headlines and institutional trust-tier content, reading as authority rather than consumer cheerfulness. Status semantics are strict: #198754 green signals authentic and verified, while the full gray ramp — from #454547 body copy through #646467 muted labels to #a2a2a3 placeholder text — serves the dense population report tables and pricing grids that are Beckett's functional core. Corner radii are restrained: {rounded.sm} on buttons and cards, {rounded.xs} on grade badges, reflecting a data-first register that does not over-soften professional edges. The light blue family (#eaf6ff, #0dcaf0, #007ded) surfaces in informational alerts and subscription upsell banners, kept deliberately distinct from the teal brand system so promotional and editorial content never blend with navigation.

colors:
  primary: "#069697"
  primary-active: "#057b7c"
  primary-disabled: "#ddf3f4"
  accent-gold: "#b6975b"
  accent-teal-mid: "#54c4c8"
  accent-teal-wash: "#ddf3f4"
  accent-sky: "#0dcaf0"
  accent-blue: "#206fb6"
  accent-blue-vivid: "#007ded"
  status-success: "#198754"
  status-info-bg: "#eaf6ff"
  navy: "#14233c"
  ink: "#1c1b1e"
  body: "#454547"
  muted: "#646467"
  muted-light: "#737375"
  hairline: "#e7e7e8"
  hairline-soft: "#d9d9d9"
  canvas: "#f4f4f4"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-dark: "#1c1b1e"
  surface-mid-dark: "#39393b"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  placeholder: "#a2a2a3"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  grade-display:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  price-display:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  table-header:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  badge-label:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, Helvetica, sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.accent-teal-wash}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.on-dark}"
    padding: 11px 23px
    height: 44px
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.placeholder}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.surface-mid-dark}"
  nav-bar-link-active:
    textColor: "{colors.accent-teal-mid}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: 10px 44px 10px 14px
    height: 44px
    iconColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspectRatio: "2/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-meta:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  grade-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  grade-badge-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  grade-badge-success:
    backgroundColor: "{colors.status-success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  grade-slab-display:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
    padding: "{spacing.lg}"
  grade-slab-number:
    typography: "{typography.grade-display}"
    textColor: "{colors.accent-gold}"
  hero-banner:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
  hero-banner-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
    accentBarWidth: 4px
    accentBarColor: "{colors.primary}"
  population-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTypography: "{typography.table-header}"
    headerTextColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rowHoverBackgroundColor: "{colors.accent-teal-wash}"
  price-guide-row:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    priceTypography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  info-alert:
    backgroundColor: "{colors.status-info-bg}"
    textColor: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-sky}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-tier-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.hairline}"
    padding: "{spacing.xl}"
  subscription-tier-card-featured:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-light}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.accent-teal-mid}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The #069697 teal fill button drives all primary conversions: submit-a-card CTAs, marketplace checkout, and subscription upgrades. Padding is 12px 24px at 44px height, {rounded.sm}, {typography.button-md} weight 600. Active deepens to {colors.primary-active}; disabled washes to the mint {colors.primary-disabled} with {colors.muted} text to maintain shape without implying affordance.

**`button-secondary`** — White fill, 2px teal border, teal text, matching button-primary dimensions. Pairs with a primary CTA to offer a lower-commitment action — "View Pop Report" alongside "Grade This Card." Active state fills {colors.accent-teal-wash} to confirm selection without full teal saturation.

**`button-ghost`** — Transparent fill, white text, 1px white border, same 44px height. Used only on dark backgrounds (hero-banner, hero-banner-dark) where a teal fill would lose contrast against navy or near-black. Never appears on light surfaces.

**`button-gold`** — #b6975b fill, white text, identical shape to button-primary. Reserved for Pristine-tier grading submissions, top-tier subscription upgrades, and auction house entry points — signals premium without overusing the primary teal.

### Text Input & Search

**`text-input`** — White background, 1px {colors.hairline} border, {rounded.sm}, 44px height. Focus ring upgrades to 2px {colors.primary} teal with no outline offset. Placeholder in {colors.placeholder} (#a2a2a3). Used across account forms, grading submission flows, and filter inputs on price guide and pop report pages.

**`search-bar`** — Same geometry as text-input but with a {colors.primary} magnifier icon inset 14px from the right. Persists in the top nav on desktop, expanding on focus; collapses to an icon button on mobile. Drives the card-name and set lookup that is the core entry point for Beckett's pricing database.

### Navigation

**`nav-bar`** — 60px tall, {colors.ink} near-black background with a subtle {colors.surface-mid-dark} bottom border. Links render in {typography.nav-link} 14px weight 500 white; active and hover states flip to {colors.accent-teal-mid}. The Beckett wordmark anchors left. Primary nav: Grading, Marketplace, Price Guide, Magazine. Right cluster: search icon, account, and a {button-primary}-sized Subscribe CTA.

### Product Card

**`product-card`** — White surface, 1px {colors.hairline} border, {rounded.sm}, 2:3 image aspect ratio to fit vertical card orientation naturally. Title in {typography.title-sm}, price in {typography.price-display}, set/year/grade metadata in {typography.caption} at {colors.muted}. A grade badge overlays the upper-left corner of the card image.

### Grade Badges

**`grade-badge`** / **`grade-badge-gold`** / **`grade-badge-success`** — Three-state {rounded.xs} label badges: teal for standard BGS numeric grades, gold (#b6975b) for Pristine/10 designations, green (#198754) for authenticated-only (no grade) submissions. {typography.badge-label} at 11px uppercase weight 700 with 0.3px tracking keeps them legible at card-grid density without overwhelming the card image.

### Grade Slab Display

**`grade-slab-display`** / **`grade-slab-number`** — The digital counterpart of the physical grading slab: {colors.navy} background, 2px {colors.primary} teal border, {rounded.md}. The numeric grade renders via {typography.grade-display} at 48px weight 700 in {colors.accent-gold}, directly mirroring the gold foil numeral on physical BGS slabs. Sub-grades (Corners, Edges, Surface, Centering) run below in {typography.body-sm} at {colors.muted-light}.

### Hero Banners

**`hero-banner`** — Full-width {colors.navy} fill, {spacing.section} vertical padding. Headline in {typography.display-xl} white, sub-copy in {typography.body-md} at reduced opacity. A {button-primary} and {button-ghost} CTA pair sits below. On desktop a graded card image panel bleeds in from the right edge of the container.

**`hero-banner-dark`** — Near-black (#1c1b1e) variant for secondary category pages and service landing sections. A 4px {colors.primary} vertical accent bar runs left of the headline block — a minimal structural anchor that establishes hierarchy without requiring background imagery.

### Population & Price Tables

**`population-table`** — Dense data grid, {colors.surface-soft} header row with uppercase {typography.table-header} labels in {colors.muted}. Cells use {typography.body-sm} and {colors.ink}. Row hover flips the background to {colors.accent-teal-wash} (#ddf3f4) — the palest step in the teal ramp, confirming brand system at interaction without breaking reading flow.

**`price-guide-row`** — Single horizontal price entry: card name left-aligned in {typography.body-sm}, grade center, sale value right in {typography.title-sm} weight 600. Bottom hairline separator, no full border box. Tightly spaced to accommodate dozens of comparable sales in a single viewport.

### Subscription Cards

**`subscription-tier-card`** / **`subscription-tier-card-featured`** — Standard tier: white, 2px {colors.hairline} border, {rounded.md}. Featured tier flips to {colors.navy} background with 2px {colors.primary} teal border, making the tier hierarchy immediately readable without needing a "Recommended" label. Feature lists use a teal checkmark icon; pricing numerals in {typography.price-display} with gold tint on the premium tier.

### Info Alert

**`info-alert`** — {colors.status-info-bg} (#eaf6ff) background, {colors.accent-blue} text, {colors.accent-sky} border. Used for authentication status notices, service windows, and account nudges. The blue family is deliberately separate from the teal brand system so users parse these as status, not navigation or CTA.

### Footer

**`footer`** — {colors.ink} background, {colors.muted-light} body text, {colors.accent-teal-mid} link color. Four-column grid on desktop: Grading, Marketplace, Resources, Company. A newsletter signup row sits above the column grid — text-input on dark field with a teal submit button — before the copyright bar closes at the bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column card grid; nav collapses to hamburger icon with teal active state; search expands full-width below logo row; hero headline drops to display-md; grade slab sub-grades stack vertically |
| Tablet | 744–1128px | Two-column card grid; nav shows icon buttons with labels on hover; hero switches to stacked layout; population tables become horizontally scrollable with sticky first column |
| Desktop | 1128–1440px | Three to four-column card grid; full nav with text labels; hero full-bleed with card image panel right; all price guide columns visible |
| Wide | > 1440px | Container max-width 1440px centered; side margins fill with {colors.surface-soft}; hero background extends edge-to-edge behind the constrained content |

### Touch Targets

- All buttons minimum 44×44px hit area
- Nav icon buttons padded to 44×44px tap zone
- Grade badge links on product cards get 8px expanded hit area beyond visible label
- Population table rows minimum 44px height for comfortable mobile browsing
- Search bar expands to full viewport width on mobile at 44px height

### Collapsing Strategy

- Primary nav folds into a slide-in drawer on tablet and below; Subscribe CTA remains pinned in the collapsed header bar
- Population report table converts to per-row accordion cards on mobile, hiding low-priority columns (print run, submission date) behind a disclosure toggle
- Subscription tier cards stack vertically on mobile with the featured navy card first
- Footer four-column grid collapses to two columns at tablet, single accordion column at mobile
- Hero card imagery panel hidden on mobile; hero becomes headline-and-CTA on color fill only

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; Helvetica Neue and system stack are the only font families in extraction — brand may be licensing Helvetica Neue for web with no custom variable font loaded
- Exact button border-radius values not confirmed from CSS extraction; {rounded.sm} 8px is inferred from visual density of the site's component grid
- Dark-surface color override tokens not extracted; the site uses dark nav and hero sections alongside light content areas but no systematic dark-mode token set was confirmed
- Grade slab interior layout detail (sub-grade row proportions, population count placement) inferred from physical BGS slab conventions, not confirmed from component-level extraction
- Icon set not extractable from hex/font pass; likely a standard library (Font Awesome or similar) with {colors.primary} teal fill applied via CSS
- #0dcaf0 sky blue and #007ded vivid blue frequency unclear — may be Bootstrap framework info/link defaults rather than intentional brand tokens; treat as utility-tier rather than primary palette
- Animation and transition values (hover fade speed, drawer slide timing) not captured; no motion design tokens defined
