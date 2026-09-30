---
version: alpha
name: "Trotec Laser"
source_url: "https://www.troteclaser.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The machine sits flush-left in every product hero — a matte-black laser cutter against a pure white field — and the only chromatic relief from that restraint is the brand's signature flat crimson (#E4002B), deployed once per viewport: on the logo mark, on the primary CTA, on a category badge edge. No gradient softens it. No illustration accompanies it. The visual language is unmistakably Central European industrial: specification photography lit from directly above to expose material texture — acrylic, anodized aluminum, Baltic birch — as direct evidence of what the machine produces. Navigation is structured by application type (Engravers, Cutters, Markers, Software) rather than by SKU catalog, which signals a B2B sales motion where the buyer's production workflow defines the discovery path. Rounded corners are nearly absent: cards and input fields sit at `{rounded.xs}` to `{rounded.none}`, a deliberate mechanical precision that reads as instrument-grade rather than consumer-friendly. The "add to cart" paradigm doesn't exist here — the primary conversion action is "Request a Demo" or "Get a Quote," a dark crimson button standing alone at the bottom of a dense spec sheet. Typography runs in a weight-modulated corporate sans-serif stack; display headings step from 48px to 32px with tight letter-spacing, while body text holds at 16px/1.6 to support long technical parameter tables without fatigue. Spacing follows a disciplined 8px grid with generous 80–96px section breaks, giving comparison tables and feature grids room to function as reference documents rather than marketing copy. The footer is architecturally dense — country selectors, product family links, compliance logos, and support routing — because the buyer relationship is long, multi-touch, and global. Trotec's restraint is the message: a brand so confident in its machinery that the interface refuses to compete with it.

colors:
  primary: "#E4002B"
  primary-active: "#B5001E"
  primary-disabled: "#F0A0A8"
  primary-light: "#FDE8EC"
  ink: "#1A1A1A"
  body: "#2D2D2D"
  muted: "#5F5F5F"
  muted-soft: "#8C8C8C"
  hairline: "#DDDDDD"
  hairline-soft: "#EEEEEE"
  canvas: "#FFFFFF"
  surface-soft: "#F4F4F4"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A1A"
  surface-dark-secondary: "#2D2D2D"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  link: "#E4002B"
  success: "#2E7D32"
  warning: "#F57C00"
  error: "#C62828"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Arial, 'Liberation Sans', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.96px
  display-lg:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.28px
  display-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.88px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  spec-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.26px
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-category:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 1px
    textTransform: uppercase
  table-header:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 12px
  xl: 24px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
    border: none
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.ink}"
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 0
    borderBottom: "2px solid {colors.primary}"
  button-sm-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
  text-input-label:
    typography: "{typography.caption-label}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  form-select:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 40px 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    position: sticky
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    categoryLabel: "{typography.nav-category}"
    linkTypography: "{typography.body-sm}"
    borderTop: "2px solid {colors.primary}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
    padding: "{spacing.xl} 0"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    imageBackground: "{colors.surface-soft}"
    hoverBorderColor: "{colors.ink}"
    hoverBoxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    minHeight: 600px
    padding: "{spacing.section-lg} 0"
    imagePosition: right
    imageFill: "60% of viewport width"
  hero-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} 0"
    borderBottom: "1px solid {colors.hairline}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    headerTypography: "{typography.table-header}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    rowHeight: 48px
    stripedRowBackground: "{colors.surface-soft}"
    rounded: "{rounded.none}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.display-md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    rounded: "{rounded.none}"
  application-category-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.nav-category}"
    titleTypography: "{typography.title-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    hoverAccentBar: "3px solid {colors.primary}"
    padding: "{spacing.xl}"
  material-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "6px 14px"
    border: "1px solid {colors.hairline}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  demo-request-form:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-md}"
    inputBackground: "{colors.surface-dark-secondary}"
    inputBorder: "1px solid rgba(255,255,255,0.2)"
    inputTextColor: "{colors.on-dark}"
    submitButton: "{components.button-primary}"
    padding: "{spacing.section}"
    rounded: "{rounded.none}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    separator: "/"
  section-label:
    textColor: "{colors.primary}"
    typography: "{typography.caption-label}"
    marginBottom: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "#AAAAAA"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.caption-label}"
    linkTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section} 0"
  footer-legal:
    backgroundColor: "#111111"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    height: 56px
  country-selector:
    backgroundColor: "{colors.surface-dark-secondary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"
    border: "1px solid rgba(255,255,255,0.15)"
  pagination:
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 36px
    minWidth: 36px

## Components

### Buttons

**`button-primary`** — Flat crimson (#E4002B) with no border radius, 48px tall, 600-weight label at 15px with 0.3px tracking. The hard square corner is a deliberate engineering-catalog signal; there is no softness anywhere in the primary CTA. Hover darkens to `{colors.primary-active}` (#B5001E); disabled washes to `{colors.primary-disabled}`. Used exclusively for high-intent actions: "Request a Demo," "Get a Quote," "Download Brochure."

**`button-secondary`** — White fill with a 1.5px ink border and matching square corners. Paired with `button-primary` in hero sections where two CTAs appear side-by-side. On dark backgrounds, `button-secondary-dark` replaces ink with white border and white text.

**`button-ghost`** — No border, no fill; crimson text with a 2px crimson underline replacing the bottom border. Used in-line within spec descriptions or beneath media blocks for "Learn More" patterns without visual weight competing with product imagery.

### Navigation

**`nav-bar`** — 72px sticky bar on white, with a 1px `{colors.hairline}` bottom rule separating it from content. Logo sits left, application-category links center, utility actions (search, language selector, contact) right. At scroll depth, a subtle drop shadow activates. A dark variant (`nav-bar-dark`) is used on full-bleed dark hero pages.

**`nav-mega-menu`** — Drops on application-category hover: white panel, full viewport width, 2px crimson top accent rule, category group labels in `{typography.nav-category}` (12px, 700, uppercase, 1px tracking), links in `{typography.body-sm}`. Machine thumbnail imagery appears in a right column alongside the link clusters. Closes on outside click or Escape.

### Product Cards

**`product-card`** — White surface, 1px hairline border, zero radius, full `{spacing.xl}` internal padding. Machine image sits in a `{colors.surface-soft}` background zone occupying the top 55% of the card. Title in `{typography.title-md}`, a two-line max-power / work-area spec summary in `{typography.spec-value}`, and a crimson ghost link to the detail page. On hover, border steps to ink weight and a 16px box shadow activates — no scale transform, no slide; a professional registry does not bounce.

**`product-card-badge`** — Crimson filled, zero-radius, uppercase 11px label flush to the top-left corner of the product image zone. Used for "NEW," "BESTSELLER," or series-family labels. Only one badge per card.

### Specification Components

**`spec-table`** — Full-width bordered table, no radius. Header row uses `{colors.surface-soft}` fill, `{typography.table-header}` (uppercase, 700, 12px). Odd data rows alternate with `{colors.surface-soft}` for scanability across wide parameter sets (work area, laser power, speed, positioning accuracy). Cell padding is 14px 16px; row height holds at 48px minimum.

**`spec-badge`** — Grid of isolated stat tiles used in the "Technical Highlights" section. Each tile carries a `{typography.spec-label}` descriptor line above a `{typography.display-md}` value. Border and tight padding keep the tile reading as a hardware data sheet cell rather than a marketing callout.

### Hero

**`hero`** (dark) — Full-bleed `{colors.surface-dark}` (#1A1A1A) section, 600px minimum height, 96px vertical padding. Title in `{typography.display-xl}` white, subtitle in `{typography.display-sm}`, body copy in `{typography.body-md}`. The laser machine photograph bleeds to the right viewport edge at 60% width. One `button-primary` and one `button-secondary-dark` CTA sit in a horizontal pair below the copy. No overlay, no particle effect; the machine photograph is the entire visual argument.

**`hero-light`** — White-field variant for interior pages (software, service, material libraries). Same typographic scale, no dark overlay; bottom hairline rule separates from the first content section.

### Application Category Cards

**`application-category-card`** — Grid of industry/application tiles (Signage, Packaging, Textiles, Architecture…). 1px hairline border, zero radius, `{spacing.xl}` padding. Category label in `{typography.nav-category}` crimson, title in `{typography.title-md}` ink. Hover state activates a 3px crimson left accent bar and brings the border to full ink weight — a directional device reinforcing left-to-right scan.

### Material Filter

**`material-chip`** — Pill-adjacent filter chips at `{rounded.sm}` (4px) — the only softly rounded element on the page, allowed because it lives inside a tool interface (material library filter) rather than primary brand chrome. Inactive: soft surface fill. Active: crimson fill, white text.

### Demo Request Form

**`demo-request-form`** — Dark-surface section (`{colors.surface-dark}`), used as a full-width conversion module at the bottom of product detail pages. Title in `{typography.display-md}` white. Inputs use `{colors.surface-dark-secondary}` fill with semi-transparent white borders — they recede into the dark field so the crimson submit button is the only punctuation. No inline validation decorations compete with the CTA.

### Announcement Bar

**`announcement-bar`** — 40px full-width crimson strip pinned above the nav. White `{typography.caption}` text, centered. Carries event promotions, trade-show schedules, or regional promotion codes. Dismissible with an X on the right edge.

### Footer

**`footer`** — `{colors.surface-dark}` with a 3px crimson top rule as the only brand color on the dark field. Four-column link grid with `{typography.caption-label}` group headings (uppercase, tracked) and `{typography.body-sm}` links at #AAAAAA, brightening to white on hover. Country/language selector row sits above the column grid, using `{colors.surface-dark-secondary}` pill selectors. `footer-legal` strip below carries compliance marks, privacy link, and copyright in muted caption type on near-black.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout. Nav collapses to hamburger with full-screen slide-over panel. Hero stacks text above machine image, image bleeds edge-to-edge below. Spec tables scroll horizontally. Product card grid goes 1-up. Demo form stacks all inputs. Section padding reduces from 96px to 48px. |
| Tablet | 744–1128px | Nav retains top bar with abbreviated link labels; mega-menu still full-width but single-column clusters. Hero splits 50/50. Product grid 2-up. Spec badges wrap to 2×3 grid. Application category cards 2-up. |
| Desktop | 1128–1440px | Full mega-menu with image column. Hero at 40/60 text-to-image split. Product grid 3-up. Spec table at full width with all columns visible. Section padding at 96px. |
| Wide | > 1440px | Max content width caps at 1440px, centered. Hero machine image can scale beyond 60% into remaining whitespace. Product grid optionally 4-up. Extra whitespace added to spec sections for data-sheet readability. |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- `button-primary` and `button-secondary` hold 48px height on all breakpoints
- `material-chip` minimum 44px height on mobile (padding increases)
- Nav hamburger tap target 44×44px with 8px outer padding
- Spec table rows expand to 52px minimum on touch devices for row selection

### Collapsing Strategy

- Mega-menu collapses to accordion panels inside the hamburger slide-over; category labels become accordion toggles
- Spec table column groups: on mobile, secondary spec columns (accuracy, repeatability) collapse behind an expand row; primary specs (power, work area, speed) always visible
- Footer four-column grid stacks to single-column accordion on mobile; country selector moves to top of footer
- Application category cards collapse from 4-up grid to 2-up then 1-up with horizontal scroll suppressed
- Demo form fields reorder to name → email → company → phone → message on mobile, submit button goes full-width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site (JS-rendered tokens, possible anti-bot protection); primary (#E4002B) is inferred from widely documented Trotec brand materials and logo references — verify against brand guide before production use
- No font families were extracted; typography stack defaults to Helvetica Neue / Arial system sans-serif; Trotec may use a licensed corporate typeface (possibly custom or a Neue Haas variant) — confirm with asset inspection
- Exact nav height, mega-menu column count, and sticky behavior unconfirmed without live DOM access
- Product card hover transition timing and easing values unknown
- Dark/light nav variant trigger scroll depth unconfirmed
- Animation and transition durations across all interactive components unavailable
- Breakpoint values are best-estimate based on typical B2B machinery site conventions; confirm against actual CSS media queries
- Icon system (SVG set, stroke weight, sizing grid) not extractable without site access
- Form validation error states and inline messaging patterns unconfirmed
- Print stylesheet existence and spec-sheet PDF generation flow unknown
