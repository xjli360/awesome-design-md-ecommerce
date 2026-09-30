---
version: alpha
name: "Eppendorf"
source_url: "https://www.eppendorf.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every working scientist has a drawer full of tubes named after this brand — the 1.5 mL polypropylene microcentrifuge tube, genericized into scientific vernacular decades before "googling" was a verb — and the same bright saturated blue (#009ee0) that bands every Eppendorf pipette handle dominates the brand's digital surface. Primary actions, navigation indicators, and CTA buttons fire in that oxygen-rich azure; on a white (#ffffff) canvas that evokes cleanroom protocols and lab-coat fabric, the color reads as both instrument-grade precision and institutional trust. The typographic register stays narrow and controlled — a clean corporate sans-serif at conservative weights — because the product is a centrifuge or a 5000 µL pipette calibrated to four decimal places, and the design defers to specification copy rather than editorial flourish. Product cards expose SKU strings, volume ranges, and speed ratings with the same unhesitating confidence as a datasheet; category labels sit in small-caps uppercase to echo instrument panel legends. Navigation runs deep — product lines subdivide by application domain (genomics, cell culture, protein research), then by product family, then by individual model — and the mega-menu tier inherits soft surface washes ({colors.surface-soft}) to visually bracket the taxonomy without hierarchical confusion. Corner radii trend toward the conservative end ({rounded.sm} at 8px for cards, {rounded.xs} at 4px for badges), reinforcing the sense of calibrated engineering over organic warmth. Application-note PDFs, certificates of conformance, and instrument protocols receive dedicated download-card components marked with a left-border rule in {colors.primary}, an accent that echoes the instrument's grip color and flags the asset as an official Eppendorf document. A specification table component renders parameter rows in a monospaced stack so that RPM ceilings, temperature ranges, and tube-capacity figures read with the same visual authority as a printed DIN datasheet. The footer operates as a compliance substrate — WEEE markings, regulatory country selectors, and ISO certifications close the page under a full-bleed hairline that terminates the white grid with the formality of a calibration certificate.

colors:
  primary: "#009ee0"
  primary-active: "#0078aa"
  primary-hover: "#007ec3"
  primary-disabled: "#99d6f3"
  primary-light: "#e5f5fc"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#6b7280"
  hairline: "#dde2e8"
  hairline-soft: "#eef1f4"
  canvas: "#ffffff"
  surface-soft: "#f2f7fb"
  surface-card: "#ffffff"
  surface-section: "#f7f9fc"
  on-primary: "#ffffff"
  accent-teal: "#00b4a0"
  accent-amber: "#f5a623"
  error: "#d0021b"
  success: "#2e8b57"

typography:
  display-xl:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  spec-value:
    fontFamily: "'Roboto Mono', 'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  legal:
    fontFamily: "'Source Sans Pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
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
    padding: 10px 20px
    height: 44px
    hover:
      backgroundColor: "{colors.primary-hover}"
    active:
      backgroundColor: "{colors.primary-active}"
    disabled:
      backgroundColor: "{colors.primary-disabled}"
      textColor: "{colors.canvas}"
      cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary}"
    padding: 9px 19px
    height: 44px
    hover:
      backgroundColor: "{colors.primary-light}"
    active:
      borderColor: "{colors.primary-active}"
      textColor: "{colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 10px 16px
    hover:
      textColor: "{colors.primary-active}"
      textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 10px 12px
    height: 44px
    focus:
      borderColor: "{colors.primary}"
      outline: "2px solid {colors.primary-light}"
    error:
      borderColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
    activeIndicator:
      color: "{colors.primary}"
      height: 3px
      borderRadius: 0
    utilityIconColor: "{colors.muted}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    sectionBackground: "{colors.surface-soft}"
    borderTop: "3px solid {colors.primary}"
    categoryLabel:
      typography: "{typography.label-caps}"
      textColor: "{colors.muted}"
    itemHover:
      textColor: "{colors.primary}"
    padding: "{spacing.xl} {spacing.xxl}"
    shadow: "0 8px 24px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    imageRadius: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.body-sm}"
    captionColor: "{colors.muted}"
    hover:
      borderColor: "{colors.primary}"
      shadow: "0 4px 16px rgba(0,158,224,0.12)"
  hero-banner:
    backgroundColor: "{colors.surface-section}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section} 0"
    imagePosition: right
    accentBar:
      color: "{colors.primary}"
      width: 4px
      height: 100%
  download-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderLeft: "4px solid {colors.primary}"
    padding: "{spacing.base} {spacing.lg}"
    titleTypography: "{typography.title-sm}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    iconColor: "{colors.primary}"
    hover:
      backgroundColor: "{colors.surface-soft}"
  application-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-nav-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    active:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
    hover:
      backgroundColor: "{colors.primary-light}"
      textColor: "{colors.primary}"
  specification-table:
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.label-caps}"
    headerColor: "{colors.muted}"
    rowBorder: "1px solid {colors.hairline-soft}"
    alternateRowBackground: "{colors.surface-section}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.body}"
    padding: "{spacing.sm} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    iconColor: "{colors.muted}"
    focus:
      borderColor: "{colors.primary}"
      outline: "2px solid {colors.primary-light}"
    submitButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.none}"
      width: 44px
  product-series-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    paddingBottom: "{spacing.sm}"
    borderBottom: "2px solid transparent"
    active:
      textColor: "{colors.primary}"
      borderBottom: "2px solid {colors.primary}"
    hover:
      textColor: "{colors.body}"
  configurator-swatch:
    size: 36px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    active:
      border: "2px solid {colors.primary}"
      shadow: "0 0 0 3px {colors.primary-light}"
    tooltip:
      typography: "{typography.caption}"
      backgroundColor: "{colors.ink}"
      textColor: "{colors.canvas}"
      rounded: "{rounded.xs}"
  footer:
    backgroundColor: "#1a1a1a"
    textColor: "#c8cdd4"
    linkColor: "#c8cdd4"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.label-caps}"
    headingColor: "{colors.canvas}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"
    legalTypography: "{typography.legal}"
    legalColor: "#7a8290"
    dividerColor: "#2e3238"

## Components

### Buttons

**`button-primary`** — Filled Eppendorf Blue (#009ee0) with white label, 4px radius, and 44px height. Hovers to #007ec3 and presses to #0078aa. Disabled state washes to the 40%-opacity tint (#99d6f3); cursor becomes not-allowed to communicate the constraint without hiding the element.

**`button-secondary`** — White fill with a 1.5px blue border and matching blue label. On hover, the background lifts to the primary-light tint (#e5f5fc), reinforcing the blue family without filling the button. Used alongside button-primary in hero CTAs — "Request Quote" paired with "Find a Distributor."

**`button-ghost`** — Transparent background, blue label, no border. Reserved for inline navigation actions and tertiary flows (e.g., "View all accessories"). Hover applies an underline rather than a background fill to keep it visually subordinate.

### Text Input

**`text-input`** — 44px tall with a 1px #dde2e8 border and 4px radius. On focus the border jumps to Eppendorf Blue and a 2px primary-light outer glow confirms keyboard focus. Validation errors swap the border to `{colors.error}` (#d0021b). Placeholder renders in #6b7280 at the body-md scale.

### Navigation

**`nav-bar`** — 64px white bar, 1px hairline bottom border. The Eppendorf wordmark sits left at 32px height; right side carries search, language selector, and cart icon in muted gray. Active top-level items grow a 3px Eppendorf Blue underline indicator flush with the bar's bottom edge. No hover backgrounds — only the indicator and color shift distinguish state.

**`mega-menu`** — Opens below the nav-bar with a 3px Eppendorf Blue top border, deep white panel, and 8px drop shadow. Left column lists application categories (Genomics, Cell Biology, Clinical) in `{typography.label-caps}` muted gray; right columns expand product families in `{typography.body-sm}`. Section backgrounds alternate to `{colors.surface-soft}` to delineate the taxonomy tier without hard borders.

### Product Card

**`product-card`** — White card, 1px hairline border, 8px radius. Product image sits in a soft-fill (#f2f7fb) region at the top, maintaining visual consistency across photography and on-white instrument renders. Title renders in `{typography.title-md}` weight 600; SKU and short descriptor in `{typography.body-sm}` muted. Hover lifts the border to Eppendorf Blue with a 12px blue-tinted shadow — the single animation budget for the card.

### Hero Banner

**`hero-banner`** — Full-width section on a #f7f9fc wash. Headline in `{typography.display-xl}` weight 700, body copy in `{typography.body-md}`. A 4px vertical Eppendorf Blue accent bar runs left of the headline block, echoing the instrument's grip stripe. Product photography or instrument render positions right; on mobile the image drops below the text block.

### Download Card

**`download-card`** — Compact white card with a 4px Eppendorf Blue left border distinguishing it from generic content cards. Title in `{typography.title-sm}`, file metadata (PDF, 1.2 MB, updated date) in `{typography.caption}` muted. A download icon renders in `{colors.primary}` right-aligned. Hover fills the background with `{colors.surface-soft}`. Used for application notes, certificates of conformance, and product brochures.

### Application Badge

**`application-badge`** — Compact pill on a primary-light (#e5f5fc) fill, label in `{typography.label-caps}` at the primary-active blue. Tags products with application domains: "PCR," "Cell Culture," "Centrifugation." Multiple badges stack horizontally below the product title on catalog pages.

### Category Nav Pill

**`category-nav-pill`** — Surface-soft rounded pill for horizontal application-filter rows. Inactive state is neutral gray-on-fog; active swaps to solid Eppendorf Blue fill with white text. Used above product listing grids as horizontal filter chips.

### Specification Table

**`specification-table`** — Two-column table: parameter label left in `{typography.body-sm}`, value right in `{typography.spec-value}` (Roboto Mono). Header row carries a `{colors.surface-soft}` background with `{typography.label-caps}` category spans (e.g., "Centrifugation Performance"). Alternating rows use `{colors.surface-section}` to aid scanning across dense parameter lists. This component is the primary information vehicle for centrifuge speed, temperature range, tube capacity, and pipette accuracy specifications.

### Search Bar

**`search-bar`** — 44px input with 1px hairline border and a flush-right attached submit button in Eppendorf Blue. The submit button carries zero radius on the join edge, creating a compound shape. Search icon renders inside the input at `{colors.muted}` until typing begins. Focus ring matches `text-input` behavior.

### Configurator Swatch

**`configurator-swatch`** — 36px circle swatches for pipette color selection (Eppendorf offers instruments in multiple handle colors). Inactive shows a 2px hairline border; active state grows a 3px Eppendorf Blue ring with a 3px primary-light halo. Hover triggers a tooltip in `{typography.caption}` on a dark (#1a1a1a) background with 4px radius.

### Footer

**`footer`** — Deep charcoal (#1a1a1a) panel with a 3px Eppendorf Blue top border — the sole brand color on the dark surface. Column headings in `{typography.label-caps}` white; links in #c8cdd4 turning to Eppendorf Blue on hover. A sub-footer row carries legal text in `{typography.legal}` at #7a8290: WEEE compliance icon, ISO certification badges, privacy policy, and country/language selector.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; mega-menu becomes full-screen slide-over drawer; hero image drops below headline; specification table scrolls horizontally; product-card grid collapses to 1 column; nav-bar hides text labels, shows hamburger |
| Tablet | 744–1128px | 2-column product grid; mega-menu becomes accordion within drawer; hero moves to 50/50 split; download cards reflow to 2-column grid |
| Desktop | 1128–1440px | 3-column product grid; full mega-menu panel; hero returns to image-right layout; specification table full-width with sticky left label column |
| Wide | > 1440px | Max-width container (1320px) centered; hero gains extra horizontal padding; 4-column product grid; footer columns expand to 5-up |

### Touch Targets

- All interactive elements (buttons, nav links, filter pills, swatch selectors) maintain a minimum 44×44px touch target
- Download card full row is tappable, not just the icon
- Configurator swatches use 44px tap zones despite 36px visual size via invisible padding
- Mega-menu drawer items have 48px row height on mobile

### Collapsing Strategy

- Top-level navigation collapses behind a hamburger at < 744px; mega-menu content restructures to accordion panels inside a full-screen drawer
- Horizontal category-nav-pill rows become a horizontally scrolling strip with overflow hidden and momentum scrolling
- Specification tables gain horizontal scroll on mobile with a sticky first column (parameter label)
- Hero accent bar hides on mobile; headline and body stack full-width above the product image
- Footer collapses from 5-column grid to 2-column accordion on mobile, with legal sub-row stacking vertically

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All colors are approximate brand-knowledge inferences** — the eppendorf.com site returned HTTP 403 at extraction time; no CSS tokens, theme colors, or hex values were extracted from the live site. Eppendorf Blue (#009ee0) is an approximation based on widely reproduced instrument photography and brand materials; actual brand hex may differ by ±15% luminosity.
- **All font families are inferred** — no font stacks were extracted. Source Sans Pro is a plausible corporate sans-serif that matches the brand's visual register; Eppendorf may license a different typeface entirely.
- **Dark mode / alternate surface palette** — unknown; the brand operates in a science-institutional register that may have a specific dark-lab UI mode for instrument software interfaces.
- **Exact button radius values** — live CSS not available; 4px (rounded.xs) is estimated from visual inspection of publicly available screenshots.
- **Product configurator interaction states** — Eppendorf's pipette configuration tool may have additional state colors (volume lock, calibration indicator) not captured here.
- **Animation / motion tokens** — transition durations, easing curves, and scroll-triggered behaviors are entirely unspecified due to extraction failure.
- **E-shop vs. corporate site distinction** — Eppendorf separates its shop subdomain from the marketing site; component tokens here target the main marketing/catalog surface and may not match the e-commerce checkout UI.
- **Secondary brand palette for product lines** — sub-brands or product families (Mastercycler, Centrifuge 5425) may carry distinct accent colors not represented in this system.
