---
version: alpha
name: "Toro"
source_url: "https://www.toro.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The bull's charge has run the same crimson since 1914 — no consumer hardware brand in the turf-care category maintains a single hue with such uncompromising physical consistency across a product line spanning compact trimmer heads and 15-foot fairway cylinder mowers. Toro red (≈ #CC0000) is not deployed as a brand accent layered over a neutral field; it is structural, appearing on fuel caps, wheel-well housings, and every panel seam that ships from a Toro factory, which means the digital interface must carry that same saturation precisely on every primary CTA, category badge, and active-nav indicator — no softened tint, no secondary hue competing for attention. The canvas is working white, unadorned by gradient or illustration, with full-bleed equipment photography carrying all the visual weight. The machine itself is the hero object; the design system exists to frame it and route the buyer to a dealer.

  Type runs at clean, moderate weights — display headings step up to bold at restrained sizes because the brand sells torque ratings and deck widths rather than aspiration, so copy is specification-led and direct. Navigation carries a wide mega-menu that reflects the catalog's genuine complexity: residential, professional, golf, and construction segments share a single domain, forcing the system to surface clear segment selectors near the top of the hierarchy. Card-level PRO / RESIDENTIAL / GOLF badges handle the bifurcation, reading as manufacturer classification rather than marketing tier.

  Dealer locator surfaces as a first-class utility — a ZIP-code input and map interface live in the header rather than the footer, reflecting the primarily dealer-channeled distribution model. Product pages run heavy on specification tables and downloadable PDFs (operator manuals, parts diagrams), styled as a data-dense manufacturer portal rather than a lifestyle DTC experience. Corner radii are minimal throughout: buttons carry a tight `{rounded.xs}` rather than the pill forms that consumer lifestyle brands favor, and product cards sit at `{rounded.none}` to `{rounded.xs}`. Spacing is generous in section rhythm — wide horizontal padding, significant vertical breathing room between content bands — preventing the spec-heavy layout from feeling cramped despite its information density. The overall effect is competence signaled through restraint: red on white, equipment photography, sparse ornamentation, and a navigation hierarchy built for a buyer who already knows what they need.

colors:
  primary: "#CC0000"
  primary-active: "#A50000"
  primary-disabled: "#E8A0A0"
  primary-dark: "#8B0000"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#6B6B6B"
  muted-soft: "#9A9A9A"
  hairline: "#E0E0E0"
  hairline-soft: "#EFEFEF"
  canvas: "#FFFFFF"
  surface-soft: "#F5F5F5"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A1A"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  badge-pro: "#1A1A1A"
  badge-residential: "#CC0000"
  badge-golf: "#2D6A2D"
  warning: "#F5A623"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.75px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
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
    padding: 12px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
    padding: 11px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "2px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xl} {spacing.xxl}"
    columnGap: "{spacing.xxl}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageFit: cover
    titleTypography: "{typography.title-sm}"
    captionTypography: "{typography.body-sm}"
    captionColor: "{colors.muted}"
  segment-badge:
    rounded: "{rounded.none}"
    typography: "{typography.badge}"
    padding: "{spacing.xxs} {spacing.sm}"
  segment-badge-pro:
    backgroundColor: "{colors.badge-pro}"
    textColor: "{colors.on-dark}"
  segment-badge-residential:
    backgroundColor: "{colors.badge-residential}"
    textColor: "{colors.on-primary}"
  segment-badge-golf:
    backgroundColor: "{colors.badge-golf}"
    textColor: "{colors.on-primary}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 520px
    imageFit: cover
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingHorizontal: "{spacing.xxl}"
    paddingVertical: "{spacing.section}"
    ctaSpacingTop: "{spacing.xl}"
  dealer-locator-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    height: 52px
    inputBackgroundColor: "{colors.canvas}"
    inputTextColor: "{colors.ink}"
    inputRounded: "{rounded.xs}"
    inputTypography: "{typography.body-md}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.sm} {spacing.base}"
    alternateRowColor: "{colors.surface-soft}"
    sectionHeaderTypography: "{typography.title-sm}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    ctaBackgroundColor: "{colors.canvas}"
    ctaTextColor: "{colors.primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
  category-grid-item:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    hoverBorderBottom: "3px solid {colors.primary}"
    padding: "{spacing.lg}"
    imageHeight: 180px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.label}"
    headingColor: "{colors.muted-soft}"
    padding: "{spacing.section} {spacing.xxl}"
    borderTop: "4px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    iconColor: "{colors.muted}"
    submitButtonColor: "{colors.primary}"
  model-number-lookup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    labelTypography: "{typography.label}"
    labelColor: "{colors.muted}"
    accentColor: "{colors.primary}"

## Components

### Buttons

**`button-primary`** — The workhorse CTA, Toro red (#CC0000) fill with white uppercase label text at 0.5px letter-spacing. The squared-off `{rounded.xs}` corner (4px) signals industrial precision; hover intensifies to `{colors.primary-active}` (#A50000). Used for all primary conversion actions: "Find a Dealer," "Add to Cart," "Request a Demo." The disabled state uses a desaturated red tint (`{colors.primary-disabled}`) rather than a gray, keeping the brand color visible even when the action is unavailable.

**`button-secondary`** — White canvas with a 2px red border and red uppercase label, matching `button-primary` geometry exactly. Used for secondary actions adjacent to a primary CTA — "Compare Models," "Download Specs." On hover the button inverts to red fill with white label, matching the primary active state without requiring a separate active-color token.

**`button-ghost`** — Transparent fill, 1px `{colors.hairline}` border, ink-colored uppercase label at `{typography.button-sm}`. Used for tertiary actions in dense layouts: filter controls, pagination triggers, secondary nav links that warrant button affordance.

### Navigation

**`nav-bar`** — 72px fixed bar on white with the Toro red wordmark and bull logo at left, a right-side utility rail carrying global search, a dealer-locator shortcut icon, and account/cart links in `{typography.nav-link}`. A 1px `{colors.hairline}` bottom border separates the bar from page content. On scroll the bar gains a drop shadow to maintain legibility when it overlaps full-bleed hero imagery below.

**`mega-menu`** — Triggered on hover below the nav bar, separated from it by a 3px Toro red top accent line that serves as the visual hinge between navigation and content. Links organize in a three-to-four column grid: each column carries a `{typography.title-sm}` heading in `{colors.primary}` and a `{typography.body-sm}` link list below. Segment identifiers (RESIDENTIAL, PROFESSIONAL, GOLF, CONSTRUCTION) act as primary column anchors, letting users orient by application before drilling into product category. The white background and `{spacing.xxl}` padding keep the sprawling catalog readable without visual compression.

### Product Cards

**`product-card`** — Hairline border on white surface, 4px corner radius, consistent image well above the fold line. The title renders in `{typography.title-sm}` ink, a short descriptor in `{typography.body-sm}` muted, a brief spec preview (deck width, engine type) in `{typography.caption}`, and a segment badge floated at the upper-left corner of the image region. Hover lifts the card with a soft box shadow; the corner radius and background do not change on interaction.

**`segment-badge`** — Flat rectangular chips with `{rounded.none}`, uppercase tracking from `{typography.badge}`, and segment-specific fills: `{colors.badge-pro}` black for PRO, `{colors.badge-residential}` red for RESIDENTIAL, `{colors.badge-golf}` deep green for GOLF. These badges function as manufacturer taxonomy markers — they should read as classification, not promotional tier.

### Hero

**`hero-banner`** — Full-bleed equipment photography at a minimum 520px height, typically 60–70vw on desktop. Text overlay is left-aligned over the darker region of the image or a semi-transparent scrim, maintaining `{colors.on-dark}` white legibility. The headline runs `{typography.display-xl}` at 1–2 lines maximum; a short supporting sentence in `{typography.body-md}` follows; a `button-primary` and optional `button-secondary` sit `{spacing.xl}` below the body copy. Category-level heroes often append a segment-selector tab strip immediately beneath the CTA block to let users redirect without scrolling.

### Dealer Locator

**`dealer-locator-bar`** — A `{colors.primary}` red strip 52px tall, pinned immediately below the main nav or embedded as a band within hero zones. Contains a white text input at `{rounded.xs}` accepting ZIP code or city, followed by a white-on-red "Find Dealer" label-button. This surface is elevated in the hierarchy because Toro's primary purchase path is through a dealer network rather than direct e-commerce; a user who cannot locate a dealer cannot buy. The input uses `{colors.ink}` text on white to remain legible against the surrounding red strip.

### Spec Table

**`spec-table`** — Two-column key-value grid with alternating rows in `{colors.surface-soft}` and `{colors.canvas}`. Labels render in `{typography.spec-label}` at `{colors.muted}`, values in `{typography.spec-value}` at `{colors.ink}`. Column-spanning section headers in `{typography.title-sm}` break the table into named groups (Engine, Cutting Deck, Drive System, Dimensions). Row separation comes from alternating backgrounds rather than drawn borders, keeping the grid visually lighter than a fully bordered table. A "Download Full Specs (PDF)" link in `{colors.primary}` anchors below.

### Promo Banner

**`promo-banner`** — Full-width Toro red section used mid-page between product categories. Centered white headline at `{typography.display-sm}`, short supporting body text at `{typography.body-md}`, and a white-fill CTA with red label at `{rounded.xs}`. The red field is itself the signal — this component requires minimal supporting imagery and is typically used for seasonal promotions, financing offers, or trade-in events. Avoid stacking two `promo-banner` instances without a white-canvas section between them.

### Footer

**`footer`** — Dark `{colors.surface-dark}` background with a 4px `{colors.primary}` top border as the sole decorative element. Four-column link grid with `{typography.label}` uppercase headings in `{colors.muted-soft}` and `{typography.body-sm}` links that lighten to `{colors.on-dark}` on hover. Legal copy, copyright, and social icons run in a sub-footer strip in `{typography.caption-sm}`. The dark footer provides strong visual termination after white and light-gray page content and the red top border closes the loop with the red nav logo.

### Search

**`search-bar`** — Inline text input in `{colors.surface-soft}` with a 1px `{colors.hairline}` border, a search-icon glyph at left in `{colors.muted}`, and a `{colors.primary}` submit-button icon at right. On focus the border transitions to `{colors.primary}`. Used in the global header overlay (full-screen takeover on mobile) and within product catalog filter panels as an inline search-within filter.

### Model-Number Lookup

**`model-number-lookup`** — Dedicated input for parts and support routing. A `{typography.label}` field label in `{colors.muted}` identifies the input ("Enter Model Number"), the text input sits in `{colors.surface-soft}` with a hairline border, and a red CTA routes to the model-specific parts and support results. This component is placed on the global site navigation utility bar, not only on the support section, because model-specific lookup is the primary entry to Toro's service and parts infrastructure.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; mega-menu collapses to hamburger drawer with accordion segments; hero drops to 320px min-height with full-width text block; product cards stack full-width; dealer-locator-bar becomes a full-width input with stacked button; spec tables scroll horizontally within a fixed container |
| Tablet | 744–1128px | Two-column product grid; nav bar retains logo and search icon but collapses segment links to hamburger; hero crops to landscape ratio with left-aligned text overlay; category-grid-item goes three-up; mega-menu becomes a side-drawer |
| Desktop | 1128–1440px | Full nav bar with mega-menu on hover; four-column product grid; hero at full 520px+ height; footer runs four-column link grid; spec table fits without horizontal scroll |
| Wide | > 1440px | Max-width container (~1440px) centered on wider viewports; hero image scales with object-fit cover; side margins grow rather than content stretching; no new layout zones introduced |

### Touch Targets

- All interactive controls minimum 44×44px on mobile, including nav icons, badge chips, and filter toggle buttons
- Dealer-locator input expands to full-width at < 744px with 52px height to accommodate thumb input
- Product card CTA links padded to full card-width tap zone on mobile
- Mega-menu becomes a full-screen drawer on mobile; all segment headers are 48px-height accordions
- Spec table rows maintain 44px minimum height when horizontally scrolled on mobile

### Collapsing Strategy

- Mega-menu collapses to hamburger plus full-screen segment-first accordion drawer; each segment expands to its category link list
- Four-column footer collapses to single-column stacked accordion on mobile, with each link-group as an expandable section
- Spec tables retain two-column key-value structure but allow horizontal scroll within the table container rather than reflowing to a single column
- Promo banners maintain full-width red treatment but reduce internal padding to `{spacing.xl}` and reduce the headline to `{typography.display-md}` on mobile
- Category grid collapses from four-up on desktop to two-up on tablet to single-up on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the live site loads design tokens via JavaScript or is behind bot-protection; all color values in this file are derived from Toro's widely-documented brand identity (red as primary brand color since 1914) and are not pixel-sampled from the live site. Exact hex values may differ from the production design system.
- **No font families extracted** — the typeface stack (`'Helvetica Neue', Helvetica, Arial, sans-serif`) is a fallback assumption. Toro may license a geometric sans-serif (Proxima Nova, Klavika, or a custom face) that could not be identified without live extraction.
- **Golf badge color** — `{colors.badge-golf}` (#2D6A2D) is estimated from industry convention for turf/golf; no extracted confirmation exists.
- **Warning/utility accent** — `{colors.warning}` (#F5A623) is inferred from equipment-safety conventions common in the category; not confirmed.
- **Button and card radius specifics** — `{rounded.xs}` (4px) is estimated from Toro's utilitarian aesthetic; the live site may use fully square (0px) corners on some components.
- **Nav height, mega-menu column count, and hero minimum height** — structural estimates based on catalog complexity and general brand category norms; require live inspection to confirm.
- **Dark mode** — no information available on whether Toro runs a dark theme; none modeled here.
- **Exact promo and seasonal color treatments** — Toro runs seasonal campaigns (fall cleanup, spring prep) that may introduce temporary secondary palette extensions; these are not modeled.
