---
version: alpha
name: "Barker Air & Hydraulics"
source_url: "https://www.barkerair.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Amber voltage on charcoal iron — #ffc700 reads as a warning beacon under warehouse fluorescents, and Barker Air & Hydraulics deploys it against the extracted dark charcoal (#3f3f3f) with the same deliberate logic as a valve handle or high-vis stripe: unmistakable in peripheral vision, unambiguous under load. This is an unusual color contract for the hydraulics and pneumatics distribution category, where most suppliers default to safety red or corporate navy; Barker's amber-on-charcoal sidesteps both conventions and reads simultaneously as industrial caution stripe and specialist confidence without borrowing from either. On-primary text runs dark (#3f3f3f) rather than white — a practical accessibility call that holds legibility under direct light or degraded display conditions in the field settings where this brand's actual audience makes procurement decisions. Typography tokens were not recoverable from the live page, which appears to load assets through a JS bundle, so the spec below defaults to a geometric system sans across all scales. Component geometry stays hard-edged: {rounded.xs} and {rounded.sm} dominate, with no pill CTAs or softly curved cards — the vocabulary of industrial procurement portals, parts catalogues, and technical specification sheets rather than consumer e-commerce. Navigation sits on a deep charcoal ground ({colors.nav-bg}) with amber reserved for active states and hover highlights, a physical-world logic where amber means "active circuit" and dark means "at rest." Product cards use the white canvas surface with a thin hairline border and no drop shadow, letting part numbers and technical specifications carry visual weight instead of decorative chrome. Quote-request CTAs break the pattern with a full amber band across the viewport — the single moment the brand turns the signal to maximum intensity. Spacing stays functional rather than generous: internal padding at {spacing.sm} to {spacing.base} inside cards and buttons, section breaks at {spacing.section}. The system is built for scanning, not browsing — optimized to move a hydraulics technician from part search to quote request in the fewest possible steps.

colors:
  primary: "#ffc700"
  primary-active: "#e6a800"
  primary-dark: "#cc9e00"
  primary-disabled: "#ffe380"
  ink: "#1a1a1a"
  body: "#3f3f3f"
  muted: "#767676"
  muted-soft: "#a0a0a0"
  hairline: "#d4d4d4"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#3f3f3f"
  nav-bg: "#2a2a2a"
  on-primary: "#3f3f3f"
  on-dark: "#ffffff"
  tag-bg: "#fff3cc"
  tag-text: "#7a5a00"
  error: "#c0392b"
  success: "#27ae60"
  amber-stripe: "#ffc700"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.02em
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.02em
  nav-label:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  part-number:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.05em
  table-cell:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  table-header:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.04em
    textTransform: uppercase
  tag-label:
    fontFamily: "system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.06em
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-ghost-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderFocusColor: "{colors.primary}"
    errorBorderColor: "{colors.error}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderFocusColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 42px
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-label}"
    height: 60px
    activeTextColor: "{colors.primary}"
    borderBottom: "3px solid {colors.primary}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-label}"
    indicatorColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    partTypography: "{typography.part-number}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    padding: "{spacing.base}"
    ctaTextColor: "{colors.primary}"
    ctaTypography: "{typography.button-sm}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    accentBar: "4px solid {colors.amber-stripe}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    padding: "{spacing.xxl} {spacing.xl}"
  category-tile:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "2px solid transparent"
    hoverBorderColor: "{colors.primary}"
    accentColor: "{colors.primary}"
    padding: "{spacing.base} {spacing.lg}"
  part-number-badge:
    backgroundColor: "{colors.tag-bg}"
    textColor: "{colors.tag-text}"
    typography: "{typography.part-number}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  quote-cta-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.nav-bg}"
    ctaTextColor: "{colors.on-dark}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    padding: "{spacing.xl} {spacing.section}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    borderColor: "{colors.hairline}"
    borderFocusColor: "{colors.primary}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
    height: 46px
  data-table-row:
    backgroundColor: "{colors.canvas}"
    altRowBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.table-cell}"
    borderColor: "{colors.hairline}"
    headerBackgroundColor: "{colors.surface-dark}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.table-header}"
  tag:
    backgroundColor: "{colors.tag-bg}"
    textColor: "{colors.tag-text}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  availability-badge:
    inStockBackgroundColor: "{colors.success}"
    inStockTextColor: "{colors.on-dark}"
    outBackgroundColor: "{colors.error}"
    outTextColor: "{colors.on-dark}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  footer:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary}"
    linkHoverColor: "{colors.primary-active}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The amber `#ffc700` button at 44px height carries `{colors.on-primary}` dark text for field-condition legibility; white text on this yellow would fail WCAG AA at small sizes. Hover and active states deepen to `{colors.primary-active}` (`#e6a800`) without animation easing — the transition is immediate and direct, matching the industrial character. Disabled state washes to `{colors.primary-disabled}` with muted body text, preserving amber character at reduced signal strength. Radius stays at `{rounded.xs}` (2px) — enough to soften the pixel corner without suggesting consumer friendliness.

**`button-secondary`** — Deep charcoal `{colors.nav-bg}` with `{colors.on-dark}` white text at the same 44px height as primary, creating a high-contrast inverted pair that works on both light and dark surfaces. Active state shifts to `{colors.body}` (`#3f3f3f`), one step lighter than the base charcoal. This button never competes with the amber primary — it recedes and lets the amber CTA lead.

**`button-ghost`** — Transparent fill with a 2px amber border and amber text, used for tertiary actions on white surfaces where full amber fill would overload the page. Hover fills to `{colors.primary}` with `{colors.on-primary}` text — the ghost becomes solid rather than darkening the border. Applied in side-by-side CTA contexts: primary action amber-fill, secondary action ghost.

### Text Inputs

**`text-input`** — White field at 42px height with `{rounded.xs}` radius and `{colors.hairline}` border at rest. Focus state swaps to an amber `{colors.primary}` border with no box shadow — sharp and functional rather than glowing. Placeholder text sits in `{colors.muted-soft}`. Error state raises border to `{colors.error}` red. The `select-input` shares identical geometry, with a system-native dropdown arrow.

### Navigation

**`nav-bar`** — 60px charcoal bar (`{colors.nav-bg}`) anchored by a 3px amber bottom border that doubles as brand signal and active-zone indicator. Link labels in `{typography.nav-label}` at weight 600 in `{colors.on-dark}` white; active links shift to `{colors.primary}` amber. The amber bottom border runs the full width of the bar, not just the active link — it frames the nav as an active system state rather than a selection indicator. On mobile, collapses to a hamburger icon with an amber accent.

**`nav-link-active`** — Amber `{colors.primary}` text with a 2px underline indicator in the same color. The underline indicator reinforces the active state without the full-width border treatment used at the nav-bar level.

### Product Display

**`product-card`** — White surface with a 1px `{colors.hairline}` border and no elevation. Hover state raises border to `{colors.primary}` amber — the only visual change, no lift or shadow. Part numbers render in `{typography.part-number}` monospace for density scanning; product title in `{typography.title-sm}` weight 600; supporting body in `{typography.body-sm}`. CTA link text in `{colors.primary}`. The deliberate absence of drop shadows keeps pages scannable — elevation would compete with the amber brand signal on hover.

**`part-number-badge`** — A zero-radius tag on warm amber-tinted `{colors.tag-bg}` with darkened amber `{colors.tag-text}` in `{typography.part-number}` monospace. Applied inline next to descriptions or inside search results for rapid part identification. Never pill-shaped — the hard edges align with the rest of the system geometry.

**`availability-badge`** — A matched-geometry tag for stock status: `{colors.success}` green for in-stock, `{colors.error}` red for unavailable. Uses `{typography.tag-label}` uppercase at 11px. Zero radius, same padding as the part-number badge. These are the only non-amber status colors in the system and carry critical procurement information.

**`data-table-row`** — Alternating white and `{colors.surface-soft}` rows with `{colors.hairline}` dividers. Column headers use a `{colors.surface-dark}` charcoal background with `{colors.on-dark}` white text in `{typography.table-header}` uppercase at weight 700 — the dark header bar echoes the nav and footer charcoal, creating a consistent dark-frame vocabulary across the page. Technical spec tables are the primary reading surface for this audience and should never truncate or collapse cell content.

**`tag`** — Warm amber-tinted tag (`{colors.tag-bg}`) with darkened amber `{colors.tag-text}` and uppercase `{typography.tag-label}`. Used for product category labels, series designations, and specification highlights. Zero radius throughout.

### Structural

**`hero-banner`** — Deep charcoal canvas (`{colors.surface-dark}`) with the headline in `{typography.display-xl}` white, a left-edge 4px amber accent bar (`{colors.amber-stripe}`), supporting copy in `{typography.body-md}` white, and an amber fill CTA button. This is the brand at full saturation: the only surface where all three elements — dark ground, amber accent, white type — appear simultaneously at full opacity. The accent bar is the signature layout device; it should appear on all hero-level content, not just the home page hero.

**`category-tile`** — Dark charcoal tile matching `{colors.nav-bg}` with a transparent 2px border that switches to `{colors.primary}` amber on hover. Title in `{typography.title-sm}` white. No scale transform, no shadow — only the border color change. The hover interaction is zero-latency and binary, fitting the industrial expectation of switches rather than dimmers. Typically arranged in a 3–4 column grid on desktop.

**`quote-cta-strip`** — Full-viewport amber band (`{colors.primary}`) with dark `{colors.on-primary}` headline text in `{typography.display-md}` and a supporting body line in `{typography.body-md}`. The CTA button inverts to `{colors.nav-bg}` charcoal with `{colors.on-dark}` white text — the one place primary and secondary swap context roles. This strip appears once per product or category page near the bottom, and its amber fills signal maximum urgency. It should not be used more than once per page.

**`search-bar`** — 46px inline search field with `{rounded.xs}` radius, hairline border at rest, amber `{colors.primary}` border on focus, and an amber submit button with `{colors.on-primary}` dark text. Supporting part-number lookups means alphanumeric input is the common case; consider enabling monospace rendering for input content when the search is scoped to part number fields.

**`footer`** — Charcoal `{colors.nav-bg}` base with a 3px amber top border echoing the nav-bar treatment — the page is bookended in the same charcoal-with-amber-threshold motif. Section headings in `{typography.title-sm}` white; body links in `{colors.primary}` amber with `{colors.primary-active}` hover. Padding at `{spacing.xxl}` vertical gives the footer structural weight appropriate to a B2B supplier with contact, compliance, and catalogue navigation to surface.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger with amber icon; hero-banner height reduces to 260–300px; category-tiles stack vertically one per row; data-tables scroll horizontally inside a wrapper — column content never wraps or truncates; quote-cta-strip stacks headline above CTA button |
| Tablet | 744–1128px | Two-column product card grid; nav-bar shows condensed link set with overflow in hamburger; hero-banner at mid height with display-md headline; category-tiles in 3-column row; data-tables at full width |
| Desktop | 1128–1440px | Three or four-column product grid; full nav-bar with all primary links visible; hero-banner at full 480–560px height; category-tiles in 4–5 column row |
| Wide | > 1440px | Content constrained to ~1320px max-width, centered with flanking whitespace; no layout changes beyond centering; quote-cta-strip background extends edge-to-edge while content container stays at max-width |

### Touch Targets

- All buttons minimum 44px height to meet WCAG 2.5.5 touch-target guidance
- Nav links padded to a minimum 44px tap height even if visual label is smaller
- Product card entire surface is tappable on mobile — not just the part-number or CTA link
- Form inputs at 42px height; select inputs match at 42px
- Availability badges and tags are display-only; they do not require tap-target sizing
- Data-table rows on mobile should support 44px minimum row height for row-level tap actions

### Collapsing Strategy

- Navigation collapses to a hamburger menu at < 744px; the amber accent on the hamburger icon preserves brand signal in compressed layout
- Category tiles reflow from multi-column grid to single-column stacked list below 744px
- Data-tables gain a horizontal scroll wrapper on mobile — technical specification content must not reflow, truncate, or collapse; preserve column fidelity and add a scroll hint indicator
- Hero-banner subtext is limited to 2 visible lines on mobile; overflow is hidden to protect CTA button fold position
- Quote-cta-strip headline reduces from `{typography.display-md}` to `{typography.display-sm}` on mobile; CTA button stacks below the text block rather than sitting inline
- Product card grid goes from 4-column → 2-column at tablet → 1-column at mobile
- Footer columns collapse to a single stacked accordion layout on mobile with `{colors.primary}` amber expand indicators

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families were recoverable from the live site — assets appear to load through a JavaScript bundle or behind anti-bot protection; the typography spec defaults to a system-ui sans stack and the `part-number` field defaults to `Courier New` monospace; both must be validated against the real rendered fonts before production use
- Only 2 hex colors were extracted (#ffc700, #3f3f3f); the full palette including secondary UI states, error, success, and warning colors is inferred from brand logic rather than confirmed from the live site
- No meta theme-color is set; browser chrome ambient color on mobile is undefined
- Platform is not Shopify; the CMS or frontend framework is unconfirmed — component structure and radii are estimated from B2B hydraulics/pneumatics category norms, not observed DOM markup or CSS variables
- Exact button corner radius, input height, and nav height are estimated; no CSS custom properties or design tokens were extractable from the live page
- Icon system, illustration usage, and product photography art direction are unconfirmed
- Whether the brand uses a custom typeface loaded via @font-face (hidden in the JS bundle) or a licensed web font is unknown — the monospace part-number treatment may be a brand convention or a rendering artifact
