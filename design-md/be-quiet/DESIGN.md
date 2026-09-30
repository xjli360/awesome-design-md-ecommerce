---
version: alpha
name: "Be Quiet!"
source_url: "https://www.bequiet.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The brand insists on lowercase in its own name — "be quiet!" arrives without a capital letter, as if raising your voice would betray the product. Against a near-black canvas (#1a1a1a to #222222), the signature orange (#ee7f00) functions as the sole thermal event in the visual system: it fires on primary CTAs, active navigation underlines, product-line badges, and compatibility highlights, while everything else recedes into charcoal grays (#929395, #55595c, #373a3c) and a cool light-gray panel (#eceeef). Open Sans carries the full typographic load at weights 400 through 700 — there is no custom display face, no editorial headline font. The brand relies on engineering density rather than typographic spectacle, pushing spec tables, socket-compatibility matrices, and TDP ratings through the same body grid that carries marketing copy. Surface panels favor #eceeef over pure white, creating a slightly industrial separation that recalls specification sheets rather than lifestyle lookbooks. The component system shows clear Bootstrap lineage but deliberately darkened: greens (#5cb85c), ambers (#f0ad4e), reds (#d9534f), and teals (#5bc0de) survive exclusively as status and compatibility flags — thermal tier chips, warranty badge variants, LED support indicators — rather than primary UI chrome. Corner radii are minimal, {rounded.xs} to {rounded.sm}, consistent with precision-machined hardware; pill shapes appear only on filter chips and small rating labels. Product pages are structured around horizontal comparison tables and layered technical diagrams where a CPU cooler's TDP, fan RPM, socket list, and noise floor must coexist in a single scannable row without visual chaos. Navigation is persistent with a dark background, using #ee7f00 as the active-state underline rather than a typographic weight shift. The footer is architecturally deep — PSU calculator, cooler compatibility check, support portals, regulatory certifications — because be quiet!'s audience expects thorough reference infrastructure, not lifestyle curation. The emotional register is controlled and systematic: German precision engineering, proud of specification depth over visual flair.

colors:
  primary: "#ee7f00"
  primary-active: "#c96b00"
  primary-disabled: "#f5c07a"
  ink: "#222222"
  body: "#373a3c"
  muted: "#55595c"
  muted-soft: "#929395"
  hairline: "#818a91"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#eceeef"
  surface-dark: "#1a1a1a"
  surface-mid-dark: "#222222"
  surface-elevated-dark: "#4c4c4c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  status-success: "#5cb85c"
  status-success-dark: "#116600"
  status-warning: "#f0ad4e"
  status-danger: "#d9534f"
  status-info: "#5bc0de"
  status-info-dark: "#31708f"
  link: "#0275d8"
  link-active: "#025aa5"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', -apple-system, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.4px
    textTransform: uppercase
  badge:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 10px
  xl: 16px
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
    height: 40px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    hoverTextColor: "{colors.primary}"
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    border: "1px solid {colors.on-dark}"
    hoverBackgroundColor: "{colors.surface-elevated-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
    border: "1px solid {colors.hairline}"
    focusBorderColor: "{colors.primary}"
    focusOutline: none
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 44px 8px 12px
    height: 38px
    border: "1px solid {colors.hairline}"
    iconButtonBackground: "{colors.primary}"
    iconButtonColor: "{colors.on-primary}"
    iconButtonWidth: 38px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 56px
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 3px
    logoAreaWidth: 180px
    dropdownBackgroundColor: "{colors.surface-mid-dark}"
    dropdownBorderTop: "2px solid {colors.primary}"
  nav-bar-secondary:
    backgroundColor: "{colors.surface-mid-dark}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    height: 36px
    linkHoverColor: "{colors.on-dark}"
    borderBottom: "1px solid {colors.surface-elevated-dark}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.primary}"
    hoverBorderColor: "{colors.primary}"
    badgePosition: top-left
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    accentColor: "{colors.primary}"
    overlayOpacity: 0.55
    minHeight: 480px
    contentMaxWidth: 600px
    ctaBackground: "{colors.primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    alternateRowBackground: "{colors.surface-soft}"
    borderColor: "{colors.hairline-soft}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.ink}"
    rowHeight: 40px
    rounded: "{rounded.none}"
    headerBackgroundColor: "{colors.surface-card}"
    headerTypography: "{typography.title-sm}"
  compatibility-badge:
    backgroundColor: "{colors.status-success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  status-chip-warning:
    backgroundColor: "{colors.status-warning}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  status-chip-danger:
    backgroundColor: "{colors.status-danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  status-chip-info:
    backgroundColor: "{colors.status-info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  product-series-badge:
    backgroundColor: "{colors.surface-mid-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
    borderLeft: "3px solid {colors.primary}"
  product-category-tab:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.primary}"
    borderBottom: "2px solid transparent"
    activeBorderBottom: "2px solid {colors.primary}"
    padding: 12px 16px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    separatorCharacter: "/"
  psu-calculator-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.title-md}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    inputBorderColor: "{colors.surface-elevated-dark}"
    inputBackgroundColor: "{colors.surface-elevated-dark}"
    inputFocusBorderColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.surface-mid-dark}"
    textColor: "{colors.muted-soft}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary}"
    borderTopColor: "{colors.primary}"
    borderTopWidth: 3px
    padding: "{spacing.xxl} 0"
    columnGap: "{spacing.xxl}"
---

## Components

### Buttons

**`button-primary`** — Solid orange (#ee7f00) fill with white uppercase text at `{typography.button-md}` (700 weight, 0.5px letter-spacing), 2px radius (`{rounded.xs}`), 40px tall. Hover deepens to `{colors.primary-active}` (#c96b00) with no transition animation — a direct, mechanical state change that mirrors the brand's no-fuss engineering posture. Disabled state drains to washed amber `{colors.primary-disabled}` (#f5c07a) at the same dimensions. The uppercase + letter-spacing treatment positions CTAs as technical imperatives rather than polite invitations.

**`button-secondary`** — White canvas fill with 1px `{colors.hairline}` border, dark ink text, same uppercase button typography. On hover, both border and text shift to `{colors.primary}` orange without changing the fill, giving a restrained paired option for use alongside primary on light surfaces.

**`button-ghost-dark`** — Transparent with a 1px white border and white `{typography.button-sm}` text; used exclusively on dark-panel sections such as hero banners, promotional strips, and the dark-background calculator card. Hover fills to `{colors.surface-elevated-dark}` (#4c4c4c), keeping the hit target visible against dark backgrounds.

### Navigation

**`nav-bar`** — Near-black (#1a1a1a) persistent top bar, 56px tall. Active navigation items receive a 3px orange bottom indicator (`{colors.primary}`) rather than a background fill or bold-weight shift — a subtle but consistent active signal that reads even against the dark background. Dropdowns open on `{colors.surface-mid-dark}` (#222222) with a 2px orange top border echoing the indicator pattern. Logo area reserves 180px on the left. The bar does not change on scroll.

**`nav-bar-secondary`** — A slimmer 36px utility strip in `{colors.surface-mid-dark}` sitting above or below the primary nav for account links, language/region selectors, and dealer-locator shortcuts. Text in `{colors.muted-soft}` (#929395) brightens to full white on hover. A subtle 1px `{colors.surface-elevated-dark}` bottom border separates it from page content.

### Forms

**`text-input`** — Standard 38px input on white canvas with `{colors.hairline}` border and 2px radius. Focus replaces the border color with `{colors.primary}` orange and removes the browser outline — no glow or box-shadow, consistent with the brand's minimal ornamentation. Placeholder text in `{colors.muted-soft}` (#929395).

**`search-bar`** — Extends `text-input` with a fixed 38px orange icon-button flush to the right edge, containing a white search glyph. The icon button background is `{colors.primary}` with `{colors.on-primary}` icon. On focus, the outer border shifts to `{colors.primary}`, visually unifying input and button as a single active unit.

### Product Card

**`product-card`** — White card with `{colors.hairline-soft}` (#eeeeee) border and 4px radius (`{rounded.sm}`). Product images sit on `{colors.surface-soft}` (#f5f5f5) to isolate hardware renders from the card background. Product name uses `{typography.title-sm}` in `{colors.ink}`; category or series subtitle in `{typography.body-sm}` at `{colors.muted}`. Price renders in `{colors.primary}` orange at `{typography.title-md}`. On hover, the card border upgrades to `{colors.primary}` for an orange frame effect — no shadow, no lift. Status and series badges anchor to the top-left corner.

### Hero Banner

**`hero-banner`** — Full-width dark panel (`{colors.surface-dark}`, #1a1a1a) with a 55% opacity photo overlay. Headline in `{typography.display-xl}` white (36px, 700); subhead in `{typography.display-sm}` white (20px, 600). Minimum height 480px with content constrained to 600px width. The single CTA uses `button-primary` orange, producing the intended high-contrast pop against the dark background. Product-specific hero panels typically use diagonal or angled photography suggesting airflow and motion — the image does visual work that the typography alone cannot.

### Spec Table

**`spec-table`** — Dense horizontal grid with alternating `{colors.surface-soft}` and `{colors.canvas}` rows, 40px row height, zero border radius (`{rounded.none}`). Column headers use `{typography.title-sm}` on a `{colors.surface-card}` (#eceeef) background. Row labels run in 12px uppercase `{typography.spec-label}` at `{colors.muted}`; values in `{typography.spec-value}` (14px, regular). Borders are `{colors.hairline-soft}`. Socket compatibility cells embed inline `compatibility-badge` chips. The table accommodates 20+ spec rows without visual breakdown — scannability is the primary constraint, decoration secondary.

### Status and Compatibility Chips

**`compatibility-badge`** / **`status-chip-warning`** / **`status-chip-danger`** / **`status-chip-info`** — Four chip variants on Bootstrap-derived signal colors, all sharing `{typography.badge}` (11px, uppercase, 700 weight) and 2px radius. Success green (#5cb85c) signals verified socket or system compatibility; amber (#f0ad4e) marks conditional or limited support; red (#d9534f) flags direct incompatibility; teal (#5bc0de) delivers informational notes such as mounting kit requirements. These chips appear primarily inside spec tables, on product card corners, and in configurator results — never as primary UI decoration.

### Product Series Badge

**`product-series-badge`** — Dark (#222222) label with no border radius, white badge text, and a 3px `{colors.primary}` left border that acts as the series accent. Used inline on product cards and listing headers to indicate product family (e.g., Dark Rock, Pure Rock, Straight Power, Pure Power). The hard-left accent line echoes the active-indicator pattern from the nav bar, giving the badge a systematic relationship to the rest of the orange-line vocabulary.

### Product Category Tabs

**`product-category-tab`** — Underline-style tabs on a transparent background. Active state shifts text from `{colors.body}` to `{colors.primary}` and draws a 2px orange bottom border at full tab width; inactive tabs show a 2px transparent border to avoid layout shift on activation. Typography is `{typography.nav-link}` (14px, 600). Padding 12px vertical, 16px horizontal. Used in product listing pages to toggle between CPU coolers, cases, PSUs, and fans without a full page reload.

### Breadcrumb

**`breadcrumb`** — Caption-size (`{typography.caption}`, 12px) trail in `{colors.muted}` (#55595c) with "/" separators at `{colors.hairline}`. The current page segment renders in `{colors.ink}` (#222222) as the active crumb. Presents on all product and category pages, sitting below the secondary nav bar and above the page headline.

### PSU Calculator Card

**`psu-calculator-card`** — Dark promotional card (`{colors.surface-dark}`, #1a1a1a) surfacing the wattage calculator tool directly in category pages and the homepage. Section heading in `{typography.title-md}` white with `{colors.primary}` accent. Input fields use `{colors.surface-elevated-dark}` (#4c4c4c) fill and border on the dark background; focus border shifts to `{colors.primary}`. Rounded at `{rounded.sm}` (4px) with `{spacing.xl}` (32px) interior padding. The card's enclosed dark environment lets it stand apart from the page canvas without a visible outer border.

### Footer

**`footer`** — Multi-column dark footer in `{colors.surface-mid-dark}` (#222222), anchored at the top by a 3px `{colors.primary}` orange border — the brand's signature full-width orange rule, repeated across section dividers and active nav indicators. Section headings in `{typography.title-sm}` white; link lists in `{typography.body-sm}` at `{colors.muted-soft}`, brightening to `{colors.primary}` on hover. Content columns cover product families, support resources, interactive tools (PSU calculator, cooler compatibility check), social links, and legal/regulatory certifications. The footer's breadth signals that be quiet!'s customers expect a reference hub, not a brand story.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger replaces horizontal nav-bar; hero text scales to display-md; spec tables collapse to stacked label–value pairs; product cards go single-column; PSU calculator card fills full width; search-bar expands to full width below nav |
| Tablet | 744–1128px | Two-column product grid; nav retains horizontal links but condenses item spacing; hero banner drops to 360px min-height; spec tables retain full horizontal columns; secondary nav-bar abbreviates to icons |
| Desktop | 1128–1440px | Three- to four-column product grid; full spec table layout; hero banner 480px; breadcrumb fully visible; secondary nav-bar expanded; category tabs visible above listing grids |
| Wide | > 1440px | Container max-width capped at 1440px, centered; hero background extends edge-to-edge while content column stays centered; footer expands to five or six columns across |

### Touch Targets

- All buttons minimum 40px tall; primary CTAs expand to 44px on mobile
- Navigation hamburger icon minimum 44×44px tap area
- Breadcrumb links expand to 32px line-height on mobile for easier tapping
- Spec table rows expand to 44px on mobile when interactive (configurator rows, clickable filters)
- Compatibility chips and series badges minimum 28px height on mobile, grouped with 8px gaps

### Collapsing Strategy

- Primary horizontal nav collapses to hamburger at < 744px; mega-menu category dropdowns become full-screen slide-in overlays
- Footer multi-column grid stacks to single column below 744px with accordion expand per section — collapsed by default to reduce scroll depth
- Spec tables switch from horizontal grid to stacked key–value pairs below 744px, with label above value in a two-row cell
- Product category tabs convert to a horizontally scrollable strip on mobile with no line-wrap; active tab scrolls into view on load
- Hero banner text overlay moves below the image on mobile at < 480px width rather than overlaying it, preventing contrast failures on varied photography

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom brand typeface — Open Sans identified from font stacks but display weight distribution and exact size hierarchy not captured; weights 400/600/700 and size scale inferred from common Bootstrap-era e-commerce patterns
- Dark-mode versus mixed-theme split not determinable from extraction — the palette includes both near-black (#1a1a1a) and near-white (#f5f5f5, #eceeef) tokens, suggesting a mixed-theme layout (dark nav/hero, light content body) rather than a full dark-mode site
- Many extracted colors (#5cb85c, #f0ad4e, #d9534f, #0275d8, #5bc0de and their darker variants) are Bootstrap 3 default semantic colors — site uses Bootstrap as its UI framework; these are preserved as status/badge tokens only, not brand primaries
- Exact breakpoint pixel values not confirmed from static extraction — 744px and 1128px are estimated from common Bootstrap grid patterns
- Product configurator and PSU calculator input UI (sliders, multi-select dropdowns, wattage results readout) not captured; token assignments in `psu-calculator-card` are inferred
- Specific font sizes for product names and pricing in listing grids not directly extracted — title-sm and title-md assignments are best estimates
- Icon set unknown — `iconfont` appears in the font-family stack suggesting a custom icon font, but glyph names and usage patterns are not available
- Animation and transition timing (hover easing, dropdown open speed, tab indicator transitions) not extractable from static analysis
- Product comparison table column-freeze behavior (sticky first column on horizontal scroll) is assumed but not confirmed
