---
version: alpha
name: "NEB (New England Biolabs)"
source_url: "https://www.neb.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The warmest background in molecular biology supply belongs to NEB — a cream-parchment ground (#f9f7f4, #f4f0e9) that evokes the field notebooks of bench scientists who built the company from a 1974 Massachusetts operation into the world's largest collection of DNA-modifying enzymes. While most scientific suppliers default to clinical white, this off-white canvas carries a slight yellowish warmth, a quiet reference to the physical culture of laboratory science where protocols live in spiral-bound notebooks and reagent labels age to yellowed permanence on freezer shelves. Navigation stays sparse and utilitarian: a system-font stack (Arial / Helvetica Neue / Roboto) with no proprietary typeface load detected, letting product data carry the page rather than brand expression. Typography is set at restrained weights — body text at 400, labels at 500, headers at 600 — and sizes don't stretch past 28px even at display scale, calibrated for a catalog audience that scans enzyme names and fidelity ratings rather than lifestyle headlines. The blue-gray muted palette (#94a3b8, #e2e8f0) handles borders and secondary text, creating a slate-cool foil to the warm ground — a tension between the warmth of the canvas and the precision of scientific data. Components built for the catalog context: product cards surface molecular weight, concentration, and activity units at the same visual weight as price; protocol-download links sit as bordered inline elements alongside product actions; and a persistent top-bar search accommodates alphanumeric enzyme naming conventions (M0491S, R0101L) that no consumer auto-suggest was ever built to anticipate. Badges carry specificity rather than marketing urgency — "Hot Start," "High Fidelity," "Epigenetics" — functioning as functional filter tags over promotional callouts. Rounded corners stay at {rounded.xs} and {rounded.sm}, reinforcing a precision-instrument aesthetic rather than the consumer-friendly softness of retail DTC brands.

colors:
  primary: "#1e5c9a"
  primary-active: "#154d84"
  primary-disabled: "#a3c4e0"
  primary-error-text: "#c0392b"
  ink: "#1a202c"
  body: "#2d3748"
  muted: "#718096"
  muted-soft: "#94a3b8"
  hairline: "#e2e8f0"
  hairline-soft: "#bbbbbb"
  canvas: "#f9f7f4"
  surface-soft: "#f4f0e9"
  surface-card: "#f8fafc"
  surface-strong: "#e2e8f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-teal: "#0e7c7b"
  badge-hot-start: "#d97706"
  badge-hifi: "#16a34a"
  badge-epigenetics: "#7c3aed"
  badge-neutral: "#475569"
  warning: "#f59e0b"
  error: "#dc2626"
  success: "#16a34a"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.32
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  mono-sku:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.5px
  spec-label:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  label-badge:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-utility:
    fontFamily: "Arial, 'Helvetica Neue', Roboto, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
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
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary}"
    padding: 9px 19px
    height: 40px
  button-outline-muted:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "2px solid {colors.primary}"
    padding: 8px 12px
    height: 40px
    placeholderColor: "{colors.muted-soft}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    focusBorder: "1px solid {colors.primary}"
    iconColor: "{colors.muted-soft}"
    padding: 8px 40px 8px 12px
    height: 40px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    logoMaxHeight: 40px
  nav-utility-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-utility}"
    borderBottom: "1px solid {colors.hairline}"
    height: 32px
    linkColor: "{colors.primary}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    hoverBorder: "1px solid {colors.primary}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-sku-label:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.mono-sku}"
  product-spec-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.spec-label}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    altRowBackground: "{colors.canvas}"
  badge-application:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.badge-neutral}"
    typography: "{typography.label-badge}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "2px 8px"
  badge-hot-start:
    backgroundColor: "{colors.badge-hot-start}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-high-fidelity:
    backgroundColor: "{colors.badge-hifi}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-epigenetics:
    backgroundColor: "{colors.badge-epigenetics}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  protocol-download-link:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "6px 12px"
    iconColor: "{colors.primary}"
  concentration-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.primary}"
    selectedBackground: "{colors.surface-card}"
    padding: "{spacing.sm} {spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
    borderBottom: "1px solid {colors.hairline}"
  tool-picker-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    hoverBackground: "{colors.surface-soft}"
    hoverBorder: "1px solid {colors.primary}"
    padding: "{spacing.lg}"
    iconSize: 32px
  data-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    borderBottom: "2px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.hairline-soft}"
  citation-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    linkColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    linkColor: "{colors.primary}"
    padding: "{spacing.xxl} 0"

---

## Components

### Buttons

**`button-primary`** — The primary call to action uses `{colors.primary}` (estimated science blue; the actual brand blue was not extractable due to bot-protection on the site). Corners sit at `{rounded.sm}` (8px), precise without the rigidity of a zero-radius button. On hover the background shifts to `{colors.primary-active}`; disabled state desaturates to `{colors.primary-disabled}`. Height is 40px — slightly compact relative to consumer norms, calibrated for the catalog audience comfortable with dense data layouts where generous padding would waste vertical space.

**`button-secondary`** — An outlined variant with `{colors.primary}` border and text on `{colors.canvas}` background. Shares rounded and padding with the primary. Used for secondary product actions such as "Add to Favorites" or "Compare Products," where the primary slot is occupied by "Add to Cart."

**`button-outline-muted`** — Small borderlined utility button (32px height) for inline catalog actions: "View Protocol," "Download SDS," "Copy Citation." Sits in `{colors.body}` text on `{colors.canvas}` with `{colors.hairline}` border at `{rounded.xs}`. This is the workhorse of the product detail page, appearing in clusters without competing with the primary purchase CTA.

### Search

**`search-bar`** — The enzyme catalog search is the primary navigation instrument, accommodating alphanumeric product codes (M0491S, R0101L) that require exact-match logic alongside keyword queries. The field renders at 40px height with a magnifier icon at right, `{colors.hairline-soft}` border sharpening to `{colors.primary}` on focus. Placeholder text at `{colors.muted-soft}` hints at SKU format. No pill shaping — `{rounded.xs}` only, consistent with the precision-instrument aesthetic across the rest of the interface. Typically anchored to the top nav bar as a persistent element.

### Product Card

**`product-card`** — The core catalog unit. On `{colors.surface-card}` with a 1px `{colors.hairline}` border and `{rounded.xs}` (4px) corners, the card surfaces product name in `{typography.title-md}`, SKU in `{typography.mono-sku}` (monospace for alphanumeric alignment across card grids), application badges below the name, and price/unit size in `{typography.body-sm}`. On hover the border shifts to `{colors.primary}` with a soft shadow. The card deliberately avoids lifestyle photography — molecular diagrams or flat color fields only.

**`product-sku-label`** — Inline monospace label rendering the NEB product code (e.g., "M0491S"). Uses `{typography.mono-sku}` at `{colors.muted}`, visually subordinate to the product name but immediately scannable for researchers who navigate the catalog by memorized SKU prefixes.

**`product-spec-row`** — Alternating-row table for enzyme specifications: activity units, concentration (units/mL), molecular weight, storage temperature, unit definition. Background alternates between `{colors.surface-soft}` and `{colors.canvas}`, typography in `{typography.spec-label}` monospace to maintain column alignment. This is the densest information component in the system; horizontal scroll is required on narrow viewports.

### Badges

**`badge-application`** — Neutral bordered tags for application categories: PCR, Cloning, Epigenetics, Next Generation Sequencing, CRISPR. Background `{colors.surface-soft}`, `{typography.label-badge}` uppercase at 11px. These serve as filter-chip affordances in the catalog sidebar and as taxonomy labels on product cards.

**`badge-hot-start`** — Amber-orange (`{colors.badge-hot-start}`) filled badge for Hot Start enzyme variants, indicating the product includes a proprietary activation mechanism. White text in `{typography.label-badge}` at `{rounded.xs}`.

**`badge-high-fidelity`** — Green (`{colors.badge-hifi}`) for High Fidelity products such as Q5 and Phusion lines, signaling reduced error rate specifications. Both colored badges use `{rounded.xs}` to stay grid-aligned rather than going pill-shaped.

**`badge-epigenetics`** — Purple (`{colors.badge-epigenetics}`) for methylation-sensitive and epigenetics-focused products. Color-coded badge taxonomy is functional — it maps to product application families, not promotional tiers.

### Navigation

**`nav-bar`** — 64px tall on `{colors.canvas}` with a 1px `{colors.hairline}` bottom border. Logo at left, product-category megamenu links in `{typography.nav-link}`, search bar anchored right. No drop shadow — the hairline border alone provides elevation separation. Above the main nav, a 32px `{colors.surface-soft}` utility bar carries account, cart, distributor finder, and contact links in `{typography.nav-utility}` at `{colors.muted}`.

**`nav-dropdown`** — Megamenu panels organized by application area: Polymerases, Ligases, Restriction Enzymes, DNA Assembly, RNA Biology, Epigenetics. `{colors.canvas}` background, 1px border, `{rounded.xs}`, 12px blur shadow. Product links displayed in multi-column grid; featured tools (NEBcloner, NEBcutter) may appear as highlighted cards within the dropdown.

### Hero

**`hero-banner`** — Category and landing page heroes use `{colors.surface-soft}` (the warmer parchment) as ground, not photography. Molecular diagram or product illustration centered, headline in `{typography.display-xl}`, supporting copy in `{typography.body-md}`. Full padding at `{spacing.section}` vertical and `{spacing.xxl}` horizontal. No gradient, no video — flat warm ground only, consistent with the scientific-catalog aesthetic that deprioritizes lifestyle storytelling.

### Tool Picker

**`tool-picker-card`** — NEB's bioinformatics selector tools (NEBcloner, NEBcutter, Double Digest Finder, Enzyme Finder) surface as card grids on the Tools & Resources landing. Each card is `{colors.canvas}` with `{rounded.sm}` corners, a product-category icon at 32px, title in `{typography.title-md}`, short descriptor in `{typography.body-sm}`. On hover the background fills to `{colors.surface-soft}` and border shifts to `{colors.primary}`. The card grid is typically three columns at desktop.

### Protocol Download

**`protocol-download-link`** — An inline bordered element that lives within product detail pages alongside the product action cluster. Uses `{colors.surface-soft}` background with `{colors.primary}` text and a download icon at `{colors.primary}`. This appears in dense product-data contexts where a full-height primary button would break the visual rhythm of the specification area. Multiple protocol links may appear stacked (English, French, Spanish PDF variants).

### Citation Block

**`citation-block`** — NEB includes usage citations on product pages for publications that used the specific enzyme. The block sits in `{colors.surface-soft}` with `{typography.caption}` at `{colors.body}`, formatted as a compact bibliographic entry with DOI link in `{colors.primary}`. This component is unique to scientific supply brands and carries significant trust signal for research-audience visitors.

### Data Table

**`data-table-header`** — Sticky header row for specification and comparison tables. `{colors.surface-soft}` background, `{typography.title-sm}` labels, 2px `{colors.hairline}` bottom border. Column headers align left for text, right for numeric fields to enable scanning.

### Footer

**`footer`** — `{colors.surface-soft}` background with 1px `{colors.hairline}` top border. Four-column link grid (Products, Tools & Resources, Support, Company) in `{typography.body-sm}`, links in `{colors.primary}`. Bottom bar carries copyright, legal links, and social icons in `{colors.muted}`. A secondary row may carry regional/language selectors for international research audiences.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger drawer; search bar moves to full-width row below logo; product grid becomes single column; product-spec-row tables scroll horizontally with sticky property-name column; tool-picker-cards stack single column; hero-banner padding reduces to `{spacing.xl}` vertical |
| Tablet | 744–1128px | Two-column product grid; megamenu replaced with accordion-style nav drawer; hero-banner at reduced padding; search bar remains in sticky top bar at reduced width; concentration-selector options stack vertically |
| Desktop | 1128–1440px | Three to four column product grid; full megamenu nav active; hero-banner at full `{spacing.section}` padding; tool-picker-card grid in 3 columns; data-table at full column width |
| Wide | > 1440px | Max-width container centered at ~1400px; canvas flanks fill with `{colors.canvas}`; product grid holds at four columns maximum; hero-banner content centered within max-width constraint |

### Touch Targets

- Minimum 44×44px for all interactive elements on mobile (buttons, badge-filter chips, nav links)
- Concentration-selector option rows expand to full-width with increased padding on mobile
- Protocol-download-link height increases to 44px on mobile
- Search-bar height increases to 48px on mobile for keyboard-accessible focus area
- Badge-application filter chips minimum height 36px on mobile, spaced with `{spacing.xs}` gap
- Data table row heights increase to minimum 48px on touch viewports for scroll-interaction comfort

### Collapsing Strategy

- Megamenu → slide-in drawer at tablet/mobile; application-category headers become accordion toggles
- Product filter sidebar → bottom-sheet modal on mobile with sticky "Apply Filters" CTA button
- Product-spec-row tables → horizontal scroll containers with sticky first column (property name label)
- Four-column product grid → two columns at tablet → single column at mobile
- Tool-picker-card grid → two columns at tablet → single column at mobile
- Breadcrumb truncates middle segments with ellipsis on mobile, preserving root and current-page nodes
- Citation-block collapses to two visible entries with "Show all N citations" expand trigger on mobile
- Nav-utility-bar hides on mobile (account/cart folded into hamburger drawer)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Primary brand color not extracted** — the site returned a Cloudflare security check page during extraction; no interactive or CTA colors (primary blue, link blue, hover states, active states) were captured. All `{colors.primary}` values are estimated from the observed blue-gray palette direction and scientific-brand convention. Verify the actual NEB hex values before shipping any component using primary color.
- **Warm canvas tones may partly reflect the security-check page** — #f9f7f4 and #f4f0e9 differ from Cloudflare's typical white-and-blue default, suggesting they may be genuine NEB surface colors that carried through to the blocked page; however this cannot be confirmed without a clean site load.
- **Blue-gray muted tones (#94a3b8, #e2e8f0, #bbbbbb) are likely Cloudflare/Tailwind UI chrome** — these slate-family values are common to browser-rendered security-check pages and may not represent NEB's actual hairline or muted palette.
- **No brand typeface detected** — only system font stacks (Arial, Helvetica Neue, Roboto) were found. NEB may use a licensed typeface that did not load during extraction. All typography tokens are system-font fallback stacks only.
- **Badge color palette estimated** — orange, green, and purple application-category badge colors were not extracted from live DOM; they are inferred from common NEB product-tier conventions (Hot Start, High Fidelity, Epigenetics).
- **No meta theme-color defined** — NEB has not declared a PWA or browser-chrome theme color; mobile browser chrome appearance is undefined.
- **No animation or transition data captured** — hover and focus transition durations and easing functions are unspecified; defaults should be 150–200ms ease-in-out until confirmed.
- **Cart, checkout, and account flows not observed** — component patterns for the purchase funnel (cart drawer, quantity selector, checkout form, order confirmation page) are absent from this spec.
- **No breakpoint confirmation** — responsive breakpoints are estimated from common catalog-site conventions; NEB's actual grid breakpoints were not extractable.
