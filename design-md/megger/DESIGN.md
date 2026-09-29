---
version: alpha
name: "Megger"
source_url: "https://www.megger.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The casing of a Megger insulation resistance tester is near-black resin banded in high-visibility orange — the contrast ratio that survives a darkened switchgear room translates directly into the brand's digital identity. Near-black #313131 anchors every heading, nav rail, and data row; orange (`{colors.primary}`) delivers the single voltage point across primary CTAs, active states, and product-category callouts without supplementary accents competing for attention. Typography runs on a resolved system-font stack — Arial, Roboto, Segoe UI — which reads as deliberate rather than economical in a B2B catalog built for field engineers: no custom kerning, no variable-weight display face, just a clean 400–700 weight ladder that lets specification ranges, test voltages, and safety ratings render without friction.

  The grid is dense by necessity. Megger product lines — insulation testers, earth-ground analyzers, power-quality monitors, transformer-diagnostic systems — each arrive with long specification lists and multiple model variants per family. Horizontal spec tables (`spec-table`) are a first-class UI pattern, presenting resistance ranges, test voltages, measurement categories, and IP ratings in tight 11px uppercase `{typography.spec-label}` headers over 40px striped rows. Product cards carry `{colors.primary}` category badges at `{rounded.xs}` corners, a short descriptor line, and a ghost-link CTA that highlights orange only on hover — keeping listing grids scannable without visual noise. Safety callouts (`alert-safety`, `alert-warning`) use a left-border treatment borrowed directly from IEC printed literature: a 4px `{colors.danger}` or `{colors.warning}` stripe against `{colors.surface-soft}` fill signals electrical hazard inline without interrupting prose flow. Corner radii stay minimal throughout at `{rounded.xs}`–`{rounded.sm}`; nothing exceeds `{rounded.md}`, reflecting the orthogonal precision of the physical hardware itself.

colors:
  primary: "#f47920"
  primary-active: "#d46410"
  primary-disabled: "#f9c89a"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#6b6b6b"
  hairline: "#d9d9d9"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#1e1e1e"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  danger: "#cc2200"
  warning: "#f0a500"
  success: "#2a7a3b"
  link: "#1a6ab5"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  category-badge:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
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
    hover:
      backgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
    hover:
      backgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 0
    hover:
      textColor: "{colors.primary-active}"
      textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 12px
    height: 44px
    focus:
      border: "2px solid {colors.primary}"
      outline: none
    placeholder:
      textColor: "{colors.muted}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    leadingIconColor: "{colors.muted}"
    focus:
      border: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
    activeIndicator:
      color: "{colors.primary}"
      height: 2px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    border: "1px solid {colors.hairline}"
    shadow: "0 4px 16px rgba(0,0,0,0.10)"
    rounded: "{rounded.none}"
    columnGap: "{spacing.xl}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    padding: "{spacing.sm} 0"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    imageBackground: "{colors.surface-soft}"
    hover:
      shadow: "0 4px 20px rgba(0,0,0,0.10)"
      borderColor: "{colors.primary}"
    badgeTypography: "{typography.category-badge}"
    badgeBackground: "{colors.primary}"
    badgeColor: "{colors.on-primary}"
    badgeRounded: "{rounded.xs}"
    titleTypography: "{typography.title-sm}"
    descTypography: "{typography.body-sm}"
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 480px
    padding: "48px 64px"
    overlayOpacity: 0.55
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.hairline-soft}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    headerColor: "{colors.muted}"
    cellTypography: "{typography.body-sm}"
    cellColor: "{colors.ink}"
    stripeBackground: "{colors.surface-soft}"
    rowHeight: 40px
    rounded: "{rounded.xs}"
  category-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
    active:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      border: "1px solid {colors.primary}"
  application-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
    border: "1px solid {colors.hairline}"
  download-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    iconColor: "{colors.primary}"
    iconSize: 24px
    titleTypography: "{typography.body-sm}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    hover:
      borderColor: "{colors.primary}"
      backgroundColor: "{colors.surface-soft}"
  alert-safety:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    borderLeft: "4px solid {colors.danger}"
    padding: "{spacing.base}"
    iconColor: "{colors.danger}"
  alert-warning:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    borderLeft: "4px solid {colors.warning}"
    padding: "{spacing.base}"
    iconColor: "{colors.warning}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
    linkHover: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    dividerColor: "#3a3a3a"
    padding: "48px 0"
    bottomBarTypography: "{typography.caption}"

---

## Components

### Buttons

**`button-primary`** — Solid `{colors.primary}` orange fill at `{rounded.xs}` corners, 44px tall, `{typography.button-md}` label in white. Hover darkens immediately to `{colors.primary-active}` with no transition delay — the instant-response feel matches the hardware it supports. Disabled state uses `{colors.primary-disabled}` wash with `not-allowed` cursor; no opacity-based fade, since engineers reading disabled UI states expect clear categorical signals.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, identical height and corner radius to primary. On hover, background shifts to `{colors.surface-soft}`. Used for secondary actions on product detail pages — "Add to Compare", "Request Quote" — positioned beside a primary CTA without competing with it.

**`button-ghost`** — Transparent background, `{colors.primary}` label text, typically arrow-appended ("View Product →", "Download PDF →"). No border, no minimum height — scales inline with surrounding `{typography.body-sm}` or `{typography.body-md}` copy. Hover underlines and shifts to `{colors.primary-active}`. Used throughout product cards and download cards to keep grid layouts visually clean.

### Inputs & Search

**`text-input`** — 44px tall, 1px `{colors.hairline}` border, `{rounded.xs}` corners. Focus ring promotes border to 2px `{colors.primary}` to match the orange active system. Placeholder text at `{colors.muted}`. Used in dealer-locator forms, quote-request flows, and account management. No floating label — label text sits statically above the field.

**`search-bar`** — Shares geometry with `text-input` but carries a leading magnifier glyph in `{colors.muted}`. Appears in the global nav header and as a full-width element above product listing grids. Focus upgrades the border to `{colors.primary}` without a flash of outline — consistent with the input system.

### Navigation

**`nav-bar`** — 64px white bar with 1px `{colors.hairline}` bottom border. Logo left-anchored at 32px height; primary category links in `{typography.nav-link}` across the center; search icon and a "Contact" or "Where to Buy" `button-primary` at far right. The active category link carries a 2px `{colors.primary}` underline indicator flush to the bar's bottom edge. Collapses to a hamburger icon at mobile breakpoint.

**`mega-menu`** — Full-width dropdown panel at `{rounded.none}` — no soft corners, edges flush with viewport. White fill, 1px `{colors.hairline}` border, soft box shadow. Columns organize by product family with `{typography.title-sm}` section heads in `{colors.ink}` and `{typography.nav-link}` item links in `{colors.body}`. At tablet the panel becomes a stacked accordion inside a side drawer.

**`breadcrumb`** — Caption-scale trail in `{colors.muted}` with `/` separators; terminal segment renders in `{colors.ink}` to confirm current location. Present on all product detail, application, and support pages. Enables engineers deep-linking to spec sheets to orient quickly within the product hierarchy.

### Product Components

**`product-card`** — White card at `{rounded.sm}` with 1px `{colors.hairline}` border. A 4:3 image region on `{colors.surface-soft}` occupies the top; a `{colors.primary}` category badge with `{typography.category-badge}` uppercase label and `{rounded.xs}` sits top-left of the image. Below the image: product name in `{typography.title-sm}`, a one-line descriptor in `{typography.body-sm}` at `{colors.muted}`, and a ghost-link CTA in `{colors.primary}`. On hover the card shadow lifts and the border transitions to `{colors.primary}`, providing selection feedback without animation complexity.

**`spec-table`** — The workhorse component of every product detail page. Header row in `{typography.spec-label}` on `{colors.surface-soft}`; data rows alternate white and `{colors.surface-soft}` at 40px row height in `{typography.body-sm}`. May render 20–40 rows covering measurement range, accuracy class, test voltage, CAT rating, IP protection, and certifications. At mobile the table enters a horizontal scroll container with the left label column sticky.

**`category-filter`** — Pill-shaped filter chip at `{rounded.full}` for product listing pages. Default: `{colors.surface-soft}` fill, 1px `{colors.hairline}` border, `{colors.body}` label. Active: `{colors.primary}` fill, `{colors.on-primary}` label, border matches fill. Chips arrange horizontally in a row above the product grid; at mobile the row becomes horizontally scrollable.

**`application-badge`** — Flat rectangular label at `{rounded.xs}` for market-segment tagging: Utilities, Railways, Renewables, Industrial, Civil. `{colors.surface-soft}` fill, `{colors.body}` text in `{typography.caption}`, 1px `{colors.hairline}` border. Displayed as a horizontal strip below hero banners and as sidebar filter groups in the mega-menu.

### Documentation & Safety

**`download-card`** — A document-row card: 24px file-type icon in `{colors.primary}` left-aligned, document title in `{typography.body-sm}`, file size and format note in `{typography.caption}` at `{colors.muted}`. On hover border highlights to `{colors.primary}` and background shifts to `{colors.surface-soft}`. Used across the literature library, software download hub, and product detail document tabs.

**`alert-safety`** — A left-bordered callout block following IEC inline warning conventions: 4px `{colors.danger}` left stripe, `{colors.surface-soft}` fill, `{rounded.xs}`. Icon and heading in `{colors.danger}`, body in `{typography.body-sm}` at `{colors.body}`. Appears within product descriptions, installation guides, and compliance documentation wherever electrical hazard potential exists.

**`alert-warning`** — Structurally identical to `alert-safety` but left stripe and icon use `{colors.warning}` amber. Used for caution-level notices below electrical-hazard threshold — battery warnings, storage-temperature limits, calibration reminders.

### Page Structure

**`hero-banner`** — Dark `{colors.surface-dark}` base with a product or application photograph at 55% overlay. `{typography.display-xl}` headline in `{colors.on-dark}`, subhead in `{typography.body-md}` at `{colors.hairline-soft}`, and a single `button-primary` CTA. Minimum 480px tall on desktop. Used on homepage, product-family landing pages (Insulation Testing, Earth & Ground, Power Quality), and campaign pages.

**`footer`** — Full-width `{colors.surface-dark}` footer. Four-column grid: Product Families, Markets, Support, Company. Column heads in `{typography.title-sm}` white; links in `{typography.body-sm}` at `{colors.hairline-soft}` with `{colors.primary}` hover. Horizontal divider at `#3a3a3a` separates the column grid from the bottom bar. Bottom bar carries copyright notice in `{typography.caption}` and a region/language selector.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger drawer; product grid drops to 1 column; spec tables become horizontally scrollable with frozen first column; hero banner reduces to 280px tall; category filter chips scroll horizontally; footer columns stack as accordion |
| Tablet | 744–1128px | Product grid at 2 columns; mega-menu becomes stacked accordion in side drawer; hero at 360px; download cards stack vertically; breadcrumb truncates middle segments |
| Desktop | 1128–1440px | Full mega-menu; 3–4 column product grid; hero at 480px; spec tables full-width with sticky column header; all footer columns visible |
| Wide | > 1440px | Content max-width 1400px centered; hero background bleeds edge-to-edge; outer gutters fill with canvas color; product grid caps at 4 columns |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Category filter chips expand padding to `10px 18px` on mobile for reliable tap
- Product cards are fully tappable — the entire card surface is the tap target, no nested tap conflicts with the ghost CTA
- Nav hamburger button 48×48px minimum hit area
- Download card rows minimum 48px tall on mobile
- Spec table rows minimum 44px on touch for row-selection interactions

### Collapsing Strategy

- Primary navigation: full top bar → hamburger icon + slide-in drawer at < 744px
- Mega-menu columns: multi-column panel → stacked accordion sections inside drawer
- Product grid: 4-col → 3-col at 1128px → 2-col at 744px → 1-col at < 744px
- Spec table: fixed-column layout → horizontal scroll container with frozen label column at < 744px
- Application badge strip: horizontal pill row → 2×2 grid wrap at mobile
- Footer: 4-col grid → 2-col at tablet → stacked accordion with expand/collapse at mobile
- Hero CTA button: maintains `button-primary` at all breakpoints; hero text stack reduces from `display-xl` to `display-md` on mobile

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Color palette severely limited**: Only `#313131` was extracted from the live site; the anti-bot challenge page ("Just a moment...") blocked full rendering. The orange primary (`{colors.primary}`) at approximately `#f47920` is derived from brand knowledge — Megger's physical hardware, product imagery, and historical marketing materials consistently feature a strong amber-orange accent — but the precise web hex was not confirmed by live extraction.
- **No meta theme-color**: The `<meta name="theme-color">` tag was absent or inaccessible; mobile browser chrome bar tint is unconfirmed.
- **Custom typography unconfirmed**: No custom font family was detected; all stacks resolved to system fonts. Megger may load a licensed typeface (or a web-licensed version of a humanist sans) via JavaScript after the anti-bot challenge resolves — this cannot be confirmed without a successful page render.
- **Secondary and accent palette inferred**: Danger red (`{colors.danger}`), warning amber (`{colors.warning}`), success green (`{colors.success}`), and link blue (`{colors.link}`) are derived from B2B instrument-industry conventions and IEC color coding practices, not extracted values.
- **Dark footer hex unconfirmed**: `{colors.surface-dark}` at `#1e1e1e` is estimated; the actual footer background could differ.
- **Component interaction timings**: Hover transition durations, easing curves, and focus-ring animation behavior could not be measured from the blocked page load.
- **Icon system**: Megger uses product-category and application icons across navigation and product cards; the specific style (outline, filled, illustrated) and grid size were not assessable.
- **E-commerce vs. catalog distinction**: Whether the site includes a transactional cart or routes to distributors for purchase could not be confirmed, which may affect the prominence and styling of CTA components.
