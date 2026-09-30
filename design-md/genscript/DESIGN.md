---
version: alpha
name: "GenScript"
source_url: "https://www.genscript.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  GenScript's interface anchors on deep-water navy (#000a46) as its ink register, then lifts through stacked temperature zones of blue — from procurement-trust #004b95 through the activating #1d73dd CTA blue — constructing a gradient-of-authority visual language that mirrors the precision hierarchy scientists expect from a reagent supplier. The accent system provides the real differentiation: #5fb035 biology-green appears on success badges, category chips, and iconography, functioning as a chromatic shorthand for "life science approved," while electric mint #65e5d1 and near-neon cyan #09ffeb surface in feature callouts and hover states, evoking the luminescent glow of gel electrophoresis under a UV transilluminator.

  Typography runs a disciplined dual-track: Montserrat at compressed weights anchors display headings with blueprint authority, while Figtree carries body copy in open, legible forms suited for researchers reading dense spec sheets under deadline. DIN 2014 surfaces in data-dense contexts — catalog IDs, purity percentages, sequence notation — lending those fields an industrial precision that reads as native to laboratory documentation. Poppins appears in broader marketing overlays where its rounded geometry softens the hard-science register for a wider audience.

  Interaction geometry is deliberately restrained: buttons sit at `{rounded.xs}` to `{rounded.sm}`, product cards at `{rounded.sm}`, and nav dividers are sharp rectilinear, all signaling scientific rigor rather than consumer warmth. Form inputs use `{rounded.xs}` with a cool hairline border, consistent with ERP and LIMS-style interfaces researchers recognize from their lab software stack. Product cards carry white surfaces with a thin left-edge green accent stripe — a fast category-routing cue across a catalog spanning peptides, plasmids, antibodies, and CRISPR tools. The dense two-tier top navigation, packed with service sub-categories, reflects a B2B procurement reality: GenScript's buyer arrives knowing exactly which synthesis service or assay kit they need, and the UI rewards that expertise with depth over discovery.

colors:
  primary: "#1d73dd"
  primary-hover: "#0b6fdf"
  primary-active: "#004b95"
  primary-disabled: "#3f90d4"
  accent-green: "#5fb035"
  accent-teal: "#1c7490"
  accent-mint: "#65e5d1"
  accent-cyan: "#09ffeb"
  teal-mid: "#0590b1"
  indigo: "#1d41dd"
  ink: "#000a46"
  body: "#333333"
  muted: "#a7a7a7"
  muted-soft: "#bbbbbb"
  hairline: "#d3d3d3"
  hairline-soft: "#c3c8cb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  navy-deep: "#000a46"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Figtree', 'Montserrat', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Montserrat', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "'Figtree', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.1px
  data-label:
    fontFamily: "'din2014', 'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
  catalog-id:
    fontFamily: "'din2014', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.8px
  badge:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Figtree', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.3px

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
    padding: 12px 28px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: "1.5px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-green-accent:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
  button-outline-dark:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.primary}"
    padding: 10px 44px 10px 14px
    height: 44px
    iconColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
  nav-bar-utility:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderRadius: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    accentBar: "3px solid {colors.accent-green}"
    accentBarPosition: left
    padding: "{spacing.base}"
    imagePadding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    captionTypography: "{typography.body-sm}"
    catalogTypography: "{typography.catalog-id}"
    shadow: "0 1px 4px rgba(0,10,70,0.08)"
    hoverShadow: "0 4px 16px rgba(29,115,221,0.12)"
  service-category-card:
    backgroundColor: "{colors.surface-soft}"
    borderRadius: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
    padding: "{spacing.xl}"
    hoverBorder: "1px solid {colors.primary}"
    hoverShadow: "0 4px 16px rgba(29,115,221,0.12)"
  hero-banner:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.accent-mint}"
    layout: left-weighted
    minHeight: 480px
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
  announcement-strip:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 36px
    textAlign: center
  data-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderRadius: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.data-label}"
    padding: 4px 8px
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    borderRadius: "{rounded.full}"
    border: "1px solid {colors.primary}"
    typography: "{typography.badge}"
    padding: 4px 12px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  accreditation-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    borderRadius: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.caption}"
    padding: 8px 12px
    logoHeight: 24px
  quote-request-banner:
    backgroundColor: "{colors.surface-soft}"
    borderLeft: "4px solid {colors.accent-green}"
    borderRadius: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
  stat-counter:
    backgroundColor: "transparent"
    numberTypography: "{typography.display-xl}"
    numberColor: "{colors.accent-mint}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-mint}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "1px solid rgba(255,255,255,0.1)"
    padding: "{spacing.section} {spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Solid #1d73dd fill with white Montserrat 600 type at 15px, 44px tall, `{rounded.xs}` radius. The deliberate sharpness — no pill softening — signals scientific procurement context rather than consumer delight. Hover advances to `{colors.primary-hover}` (#0b6fdf), active depresses to `{colors.primary-active}` (#004b95), and disabled uses `{colors.primary-disabled}` at 60% opacity. Most common CTA text: "Get a Quote," "Order Now," "Learn More."

**`button-secondary`** — White canvas with a 1.5px `{colors.primary}` border and matching blue type; identical 44px height and Montserrat stack. Converts to `{colors.surface-soft}` background on hover with border darkened to `{colors.primary-active}`. Deployed alongside `button-primary` in hero dual-CTA pairings and quote request panels.

**`button-green-accent`** — `{colors.accent-green}` (#5fb035) fill, identical geometry to `button-primary`. Appears on biology-specific synthesis CTAs and promotional banners where the green-equals-life-science visual grammar carries category context directly into the action element.

**`button-outline-dark`** — Transparent background with 1px `{colors.hairline}` border and `{colors.ink}` type, 36px compact height. Used for secondary actions in data tables, filter panels, and product card utility rows where a full-weight button would add visual noise.

### Search

**`search-bar`** — Full-width input at `{rounded.xs}` with hairline border and a `{colors.primary}` magnifier icon anchored to the right. Focus ring upgrades to a 1.5px primary-blue border. Placeholder text in `{colors.muted}`. On desktop spans the full header interior width; on mobile collapses to an icon button that expands inline on tap.

### Navigation

**`nav-bar`** — Two-tier structure: a 36px `nav-bar-utility` strip in `{colors.navy-deep}` carrying phone number, region selector, and account links in `{typography.caption}` white; beneath it, the primary 64px white nav with the GenScript wordmark at left, mega-menu dropdowns for Services (Gene Synthesis, Peptide Synthesis, Antibody Engineering, Protein Expression, CRISPR), Tools, Resources, and Community, then search and cart icons at right. Mega-menu panels open full-bleed in `{colors.surface-soft}` with `{colors.primary}` category icons.

**`nav-bar-utility`** — The 36px dark-navy strip above the primary nav. White `{typography.caption}` type carries promotion text, country selector, and login shortcut. Often hosts turnaround-time callouts or free-shipping thresholds.

### Product Cards

**`product-card`** — White surface at `{rounded.sm}` with 1px `{colors.hairline}` border and a 3px `{colors.accent-green}` left accent bar functioning as category signal. Product image occupies the upper third in a uniform 1:1 ratio with `{spacing.sm}` internal padding. Title in `{typography.title-sm}` ink; catalog ID in `{typography.catalog-id}` muted monospace; price or "Contact for Pricing" label in `{typography.body-sm}`. Hover lifts with `0 4px 16px rgba(29,115,221,0.12)` shadow. Footer row contains a compact `button-primary` CTA.

**`service-category-card`** — Soft-surface card at `{rounded.sm}` with `{spacing.xl}` padding containing a 40px `{colors.primary}` icon, title in `{typography.title-md}`, body in `{typography.body-sm}`, and a text CTA in `{colors.primary}` using `{typography.button-sm}`. Hover state introduces a 1px `{colors.primary}` border and blue-tinted glow shadow. Used in 3–4 column grids on homepage and service landing pages.

### Hero

**`hero-banner`** — Full-bleed `{colors.navy-deep}` band with left-weighted two-column layout: headline in `{typography.display-xl}` white, supporting paragraph in `{typography.body-md}` at 80% white opacity, then a stacked `button-primary` and `button-secondary` pair. Right column carries a scientific illustration or laboratory photograph. An `{colors.accent-mint}` rule or glyph punctuates the headline block. Minimum height 480px on desktop.

### Badges and Labels

**`data-badge`** — Compact `{rounded.xs}` chip in `{colors.surface-soft}` with 1px `{colors.hairline}` border; DIN 2014 `{typography.data-label}` type. Carries purity percentages, turnaround time, yield specifications, and catalog numbers on product detail pages.

**`category-chip`** — Pill-shaped `{rounded.full}` filter tag with `{colors.primary}` border and type on `{colors.surface-soft}`; active state inverts to solid primary fill and `{colors.on-primary}` type. Used in catalog filter sidebars and service navigation.

**`accreditation-badge`** — Small white card with 1px `{colors.hairline}` border carrying ISO, CAP, or quality-certification logos alongside `{typography.caption}` label text in `{colors.muted}`. Appears in a horizontal trust row above or within the footer.

### Utility Sections

**`announcement-strip`** — 36px full-width band in `{colors.accent-green}` with centered `{colors.on-primary}` `{typography.body-sm}` copy. Carries time-sensitive promotions ("50% off gene synthesis — order by Friday") at the very top of the page stack, above the utility nav tier.

**`quote-request-banner`** — `{colors.surface-soft}` panel with a 4px `{colors.accent-green}` left border at `{rounded.sm}`. Title in `{typography.title-md}`, body in `{typography.body-sm}`, single `button-primary` CTA. Appears inline on product pages and at section breaks on service landing pages.

**`stat-counter`** — Appears within `hero-banner` or a secondary dark band. Large milestone numbers in `{typography.display-xl}` `{colors.accent-mint}` with descriptor labels in `{typography.caption}` `{colors.on-primary}` — communicating scale credentials ("4M+ Genes Synthesized," "250,000+ Customers Served," "98% On-Time Delivery").

### Footer

**`footer`** — `{colors.navy-deep}` background with a multi-column link grid. Column headings in `{typography.title-sm}` `{colors.on-primary}`; links in `{typography.body-sm}` at 70% white opacity, hovering to `{colors.accent-mint}`. Bottom bar carries copyright, legal links, and a row of `accreditation-badge` elements. Social icons in `{colors.accent-mint}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; nav collapses to hamburger drawer; search becomes icon that expands full-width; service cards stack vertically; product grid 1-column; hero shifts to stacked (text above, image below); announcement strip wraps to 2 lines if needed; utility nav hides phone and region |
| Tablet | 744–1128px | 2-column product grid; service cards 2-column; nav shows logo + search icon + hamburger; hero maintains two columns but scales to `{typography.display-md}`; stat counters in 2-column grid |
| Desktop | 1128–1440px | Full two-tier nav with mega-menu dropdowns; 3–4 column product grid; service cards 3-column; hero full two-column at `{typography.display-xl}`; stat counters in 4-column horizontal row |
| Wide | > 1440px | Max-width container (1440px) centered; hero image panel expands proportionally; footer columns spread to 6; catalog grid up to 5 columns |

### Touch Targets
- All primary CTAs minimum 44px height; on mobile stretched to full container width
- Category chips minimum 36px height with `{spacing.md}` horizontal padding
- Nav utility icons (search, cart, hamburger) minimum 44×44px tap area
- Product card fully tappable via wrapper anchor
- Footer links minimum 36px line-height for accurate touch on dense link lists
- Data-badge chips minimum 32px height when interactive (filter context)

### Collapsing Strategy
- Utility nav strip: hides region selector and phone number on mobile; retains login link only
- Mega-menu dropdowns: replaced by slide-in drawer with nested accordion sections on mobile and tablet
- Search: icon-only on tablet and below, expands to inline full-width input on tap
- Stat counter row: 2×2 grid on tablet, 2-column stack on mobile
- Product card accent bar: left edge on desktop; top edge on mobile for horizontal card variant
- Service category card grid: 4→3→2→1 columns across wide/desktop/tablet/mobile breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Body text mid-tone (#333333) inferred from standard B2B practice; no mid-gray text color was present in extracted palette
- Exact typographic division between Montserrat and Figtree across specific page zones not confirmed by extraction — both fonts are present in the stack but zone-specific usage is inferred
- #09ffeb (electric cyan) appears in extraction but specific UI role (animation, data visualization, or hover glow) is unconfirmed
- No error or form validation color (red/amber) captured from extraction; absent from design system above
- No dark-mode palette detected; dark-mode support unconfirmed
- Exact mega-menu layout — icon sets, column count, hover behavior — not extractable; structure inferred from page title taxonomy
- Animation and transition durations for hover states, mega-menu reveals, card shadow lifts not captured
- DIN 2014 weight variants (Regular, Narrow, Wide) in active use not determinable from extraction
- Mobile hamburger drawer animation style and overlay behavior not confirmed
- Pricing display pattern for catalog products (list price vs. "Contact for Pricing" threshold) not confirmed
