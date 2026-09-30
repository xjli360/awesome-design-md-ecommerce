---
version: alpha
name: "Rega Research"
source_url: "https://www.rega.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Britain still builds precision analogue hardware in volume, and Rega's site states it without ceremony before the first scroll ends — a near-black canvas (#0a0a0a) carrying studio photography of turntable platters, tonearms, and amplifier fascias, with #cc4b37 — a warm brick-red — held in reserve for the single primary call to action per page and for the flush rectangular award callouts that accumulate across product listings. Nothing on this site rounds; buttons, input fields, and product cards all sit at {rounded.none}, as if softer geometry would imply tolerance in the engineering. Work Sans does the typographic work at weight 600 for display headings and 400 for body prose, spanning a scale from 42px at the largest display level down to 11px uppercase labels tracked at 1px letter-spacing — the brand favours readable hierarchy through product specification tiers rather than decorative step-down gradation. Dark-UI (#1e2023) shoulders the footer and hero backgrounds, creating a second tonal register beneath the main white canvas; between them a warm-grey palette drawn from #d9d8d6 and #f4f4f3 surfaces in specification tables and sidebar containers without disrupting the near-black and white primary contrast axis. Product pages give the technical spec table the same visual priority as the product photograph: a pivot-to-spindle tolerance or bearing housing diameter is treated as a headline feature, not supplemental copy buried below the fold. Award badges — Rega hardware wins industry press recognition at high frequency — appear as flat, solid rectangles in the primary brick-red rather than rosettes or rendered foil, consistent with an engineering organisation that communicates results rather than prestige. The site's navigation is a single flat 64px bar with no animated reveals, no mega-menu, and a pull-right search field: the same principle of mass-removal that defines Rega's physical products governs every page layout.

colors:
  primary: "#cc4b37"
  primary-active: "#a83a28"
  primary-disabled: "#e8a99f"
  ink: "#0a0a0a"
  body: "#45464b"
  muted: "#767676"
  muted-soft: "#9e9ea0"
  hairline: "#cacaca"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f4f4f3"
  surface-card: "#ffffff"
  surface-mid: "#d9d8d6"
  on-primary: "#ffffff"
  link: "#1779ba"
  dark-ui: "#1e2023"
  mid-ui: "#3b3b3b"
  warm-gray: "#808185"
  stock-green: "#116600"

typography:
  display-xl:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  label:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1px
    textTransform: uppercase
  spec-key:
    fontFamily: "'Work Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.5
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
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
    border: "1px solid {colors.ink}"
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    border: "1px solid {colors.primary}"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: 1/1
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    accentColor: "{colors.primary}"
  award-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  product-badge:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.canvas}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    keyTypography: "{typography.spec-key}"
    valueTypography: "{typography.body-sm}"
    keyColor: "{colors.body}"
    valueColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rowHeight: 44px
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label}"
    borderBottom: "1px solid {colors.hairline}"
    activeUnderline: "2px solid {colors.primary}"
    height: 44px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
  series-header:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    accentBorder: "3px solid {colors.primary}"
    padding: "{spacing.section} 0"
  footer:
    backgroundColor: "{colors.dark-ui}"
    textColor: "{colors.warm-gray}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.surface-mid}"
    borderTop: "2px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Solid #cc4b37 fill with no border-radius, uppercase Work Sans at weight 600 and 0.5px letter-spacing, white text, 48px height. The hover state shifts to #a83a28 with no animated transition; Rega avoids motion decoration on interactive elements. The disabled state desaturates to a pale salmon (#e8a99f) while keeping white label text. Used sparingly — typically one per product page, placed immediately beneath the product headline or adjacent to the price display.

**`button-secondary`** — White fill with a 1px solid #0a0a0a border, sharing the same uppercase {typography.button-md} as primary. Appears alongside the primary button for secondary actions such as "Download Specification Sheet" or "Find a Dealer." On hover the border colour shifts to {colors.primary} while the fill stays white.

**`button-ghost`** — Transparent fill, 1px solid #cc4b37 border, brick-red label text. Used for lower-hierarchy CTAs inside product description prose blocks or in the series-header band where a solid fill would compete with dark background photography. Converts to a filled primary button treatment on mobile where contrast requirements increase.

### Text Input & Search

**`text-input`** — Square-cornered at {rounded.none}, 44px height, 1px #cacaca border at rest. Focus state upgrades the border to 1px #0a0a0a with no box-shadow or glow. No icon prefix in the standard form-field variant. Used in the dealer-locator form and contact/support pages.

**`search-bar`** — Shares geometry and border treatment with text-input but sits on a #f4f4f3 background fill and appears in the top-right of the nav-bar. A search icon is inset at the right edge of the field; placeholder text in {colors.muted}. Expands inline rather than opening a modal overlay.

### Navigation

**`nav-bar`** — Single horizontal strip at 64px, white fill, 1px #cacaca underline. Links in Work Sans 500 at 15px carry no underline decoration at rest; the colour shifts to #cc4b37 on hover and active states. The Rega wordmark sits left-aligned; the search bar pulls to the far right. No mega-menu; subcategory pages are reached through the category-strip that appears immediately below the nav-bar on interior pages.

**`category-strip`** — A 44px surface-soft (#f4f4f3) band running edge-to-edge beneath the nav-bar on product-listing and series pages. Uppercase {typography.label} tabs for each product category (Turntables, Tonearms, Cartridges, Amplifiers, Digital, etc.). The active tab carries a 2px #cc4b37 bottom stroke; inactive tabs are {colors.body} with a hover shift to {colors.ink}.

**`breadcrumb`** — Single line above the product title in {typography.caption} at {colors.muted}, with "/" separators in {colors.hairline}. The final crumb (current page) renders in {colors.ink} at weight 500. Collapses to Home › Category at mobile widths.

### Product & Listing Cards

**`product-card`** — Hard-edged at {rounded.none}, 1px #e6e6e6 border, 1:1 image aspect ratio filling the full card width. Below the image: product name in {typography.title-sm}, one-line category label in {typography.label} at {colors.muted}, and price in {typography.title-md}. Award badges in {colors.primary} stack beneath the product name on decorated SKUs, each badge carrying the publication name and star rating in {typography.label} white uppercase. On hover the card border steps up to 1px {colors.hairline} and the product name shifts to {colors.primary}.

### Hero

**`hero`** — Full-width {colors.dark-ui} (#1e2023) background with full-bleed product photography, headline in {typography.display-xl} at {colors.canvas}, and a single supporting line in {typography.body-md}. The CTA button renders in {colors.primary} at 48px height against the dark background. Minimum height 560px on desktop. On the homepage, the hero presents the current flagship product; on series pages (e.g. Planar 3, Io) it carries the series name at {typography.display-xl} weight 600 with a 3px #cc4b37 left-border accent.

### Series Header

**`series-header`** — Dark-UI background band used at the top of each product series landing page, carrying the series name in {typography.display-md} and a one-paragraph description in {typography.body-md}. A 3px left-edge border in {colors.primary} distinguishes it from the hero component. The band does not contain product photography; imagery is deferred to the product-card grid below.

### Badges

**`award-badge`** — Solid #cc4b37 fill, {rounded.none}, uppercase {typography.label} in white. Carries the award body name and year (e.g. "WHAT HI-FI 5 STARS 2024"). Multiple badges on the same product stack vertically with {spacing.xs} gap. The absence of icons, stars, or rosette graphics is intentional — the text statement is treated as sufficient.

**`product-badge`** — Same rectangular geometry as award-badge but in #1e2023 fill; used for series-generation labels such as "NEW", "Mk3", or "Limited Edition". Positioned as an overlay on the product image top-left corner on listing cards.

### Spec Table

**`spec-table`** — Two-column layout on {colors.surface-soft}, key column in {typography.spec-key} at weight 500 and {colors.body}, value column in {typography.body-sm} at {colors.ink}. Rows separated by 1px #cacaca hairlines, each row 44px tall. On product detail pages at desktop widths, the spec table occupies a 50% column rendered side-by-side with the product image — not collapsed below it. Row count can run to 20+ specifications; no truncation with "show more."

### Footer

**`footer`** — Full-width {colors.dark-ui} (#1e2023) block opening with a 2px #cc4b37 top border. Body text in {colors.warm-gray} at {typography.body-sm}; links lighten to {colors.surface-mid} (#d9d8d6) on hover. Four-column grid at desktop: Products, Support, About, Dealers. The Rega logotype in white sits above the column grid at the far left. The bottom row carries copyright copy in {colors.muted-soft} and a small list of legal links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to wordmark + hamburger; hero drops to 320px min-height; spec-table scrolls horizontally; product-card grid is 1-up; category-strip scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; spec-table stacks below product image; series-header reduces to {typography.display-sm}; full nav links visible if space allows, else hamburger |
| Desktop | 1128–1440px | Three-column product grid; spec-table side-by-side with product image at 50/50 split; full nav-bar with all category links; search-bar visible inline |
| Wide | > 1440px | Content container max-width 1440px centered; four-column product grid on listing pages; hero photography bleeds full-width with text column constrained to 640px |

### Touch Targets

- All buttons minimum 48px height; button-sm minimum 44px
- Nav links in collapsed mobile menu minimum 48px tap height with full-width tap zone
- Product card tap target covers full card surface including image, not only the text region
- Search icon in nav-bar padded to 44×44px touch area
- Breadcrumb links minimum 36px tap height with extended padding

### Collapsing Strategy

- Primary nav collapses to hamburger below 744px; opens as a full-screen overlay in {colors.dark-ui} with links in {typography.display-sm} white
- Category-strip becomes a horizontally scrollable single-row tab bar below 744px; active tab scrolls into view on load
- Spec table switches from side-by-side to stacked (product image above, table below) below 744px; horizontal scroll enabled if table columns overflow
- Footer four-column grid collapses to single stacked column below 744px; column headings retain {typography.label} uppercase styling as section dividers

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius values not extracted from CSS; {rounded.none} is inferred from visual brand aesthetic — actual computed values may include 1–2px rounding not visible at typical zoom
- #1779ba, #3adb76, and #ffae00 in the extraction are almost certainly Foundation CSS framework defaults (primary blue, success green, warning yellow) and are excluded from the brand palette; their actual usage context on Rega pages is unconfirmed
- #116600 and #76bc21 appear in extraction and may represent stock-availability indicator colours; their precise UI context (badge background, dot, text colour) is not confirmed
- Work Sans presence is confirmed from the font-family stack, but whether a subset, full variable-weight build, or self-hosted version is served is unknown — fallback rendering on Helvetica/Arial may shift heading metrics
- Hover and focus state transition timings (duration, easing) not measured; transitions are assumed instantaneous based on brand aesthetic
- Exact grid gutter widths, column counts, and max-content-width breakpoints not extracted from DOM inspection
- Mobile navigation pattern (full-screen overlay vs. slide-in drawer) inferred from common patterns for this site type, not confirmed from extraction
- Price formatting, currency display, and whether a "Where to Buy" flow vs. direct checkout is used varies by region; not reflected in component spec
