---
version: alpha
name: "Extech Instruments"
source_url: "https://www.extech.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Extech Instruments leads with a deep teal (#008375) that reads more like precision-instrument lacquer than web brand color — the hue sits between aquamarine and forest, different enough from the clinical blues of medical instrumentation and the safety-orange of construction equipment to feel genuinely proprietary. Against near-black (#080808) navigation panels and dark charcoal body text (#323339), the teal fires at instrument-grade contrast, the same legibility logic behind a calibrated meter scale. A tiered family of teal derivatives — #80c1ba at midtone, #b3dad6 at near-wash, #004f46 and #00423b as pressed-state darks — provides system depth without reaching for a second hue. The exception is #ffc425, a saturated amber-yellow deployed sparingly as a caution accent, the visual equivalent of a warning indicator on an actual Extech meter.

  Typography runs two distinct tracks: Industry-Light carries display and heading weight, its geometric strokes lending a drafting-board precision that complements the instrument hardware photography on product pages. Museo Sans handles body copy with open apertures that improve scan-ability on spec-dense pages where accuracy figures, measurement ranges, and resolution values crowd the reading field. Helvetica Neue LT Std serves as the system fallback. Radii are kept deliberately tight throughout: `{rounded.xs}` and `{rounded.sm}` dominate the component layer because sharp corners communicate instrument accuracy and professional credibility. Product cards, spec callout panels, and data badges use `{rounded.xs}`; only filter pills and promotional chips reach for `{rounded.full}`.

  The dual audience — professionals and tradespersons named explicitly in the page title — shapes component hierarchy decisively. Search and product filtering appear prominently above the fold, with the full instrument taxonomy accessible: HVAC, electrical, environmental, thermal imaging, and safety instruments. Specification tables are treated as primary content rather than secondary detail, with key measurement values rendered large enough to scan without zooming. The palette's restraint — one primary teal, one amber warning accent, one full dark gray family — keeps the brand layer from competing with the hardware. Multi-function meters, clamp meters, and thermal cameras carry enough visual interest on their own; the system stays out of the way and lets the instruments speak.

colors:
  primary: "#008375"
  primary-active: "#004f46"
  primary-disabled: "#b3dad6"
  primary-dark: "#00423b"
  teal-mid: "#80c1ba"
  teal-pale: "#b3dad6"
  teal-blue: "#37aeb3"
  accent-yellow: "#ffc425"
  ink: "#080808"
  body: "#323339"
  muted: "#54565b"
  hairline: "#d1d0ce"
  hairline-soft: "#e0e0e0"
  hairline-faint: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-dark: "#1a1d20"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Industry', 'Helvetica Neue LT Std', 'Museo Sans', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Industry', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Industry', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Museo Sans', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Museo Sans', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Museo Sans', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Museo Sans', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Museo Sans', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-display:
    fontFamily: "'Industry', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  spec-label:
    fontFamily: "'Museo Sans', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  model-number:
    fontFamily: "'Industry', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Museo Sans', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Museo Sans', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Museo Sans', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Museo Sans', 'Helvetica Neue LT Std', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px

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
    padding: 11px 23px
    height: 44px
    border: "1.5px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    logoAccentColor: "{colors.primary}"
    searchBarBackground: "{colors.surface-dark}"
    borderBottom: none
  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 48px
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    imageBackground: "{colors.surface-soft}"
    imageAspect: "4/3"
    modelNumberTypography: "{typography.model-number}"
    modelNumberColor: "{colors.muted}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.primary-active}"
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.on-dark}"
    ctaVariant: "button-primary"
    minHeight: 480px
    padding: "{spacing.xxl} {spacing.section}"
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    valueTypography: "{typography.spec-display}"
    valueColor: "{colors.primary}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    padding: "{spacing.lg}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headerTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.spec-label}"
    borderColor: "{colors.hairline}"
    rowStripedBackground: "{colors.surface-soft}"
  measurement-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  warning-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  category-filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.muted}"
    iconColor: "{colors.teal-mid}"
    height: 44px
    padding: "10px 14px"
  product-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-sm}"
    titleColor: "{colors.ink}"
    modelTypography: "{typography.model-number}"
    modelColor: "{colors.muted}"
    priceTypography: "{typography.display-sm}"
    priceColor: "{colors.primary-active}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.teal-mid}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The main CTA renders at 44px height with Extech's teal (#008375) fill and white type in `{typography.button-md}` (Museo Sans semibold). Corners are `{rounded.xs}` — four pixels only, enough to soften without rounding. Hover state deepens to `{colors.primary-active}` (#004f46); disabled drops to `{colors.primary-disabled}` (#b3dad6), a pale teal that signals unavailability without visual noise. Used for "Add to Cart", "Get a Quote", and primary catalog CTAs.

**`button-secondary`** — White background with a 1.5px `{colors.primary}` border and matching teal text. Same height and radius as primary. Appears alongside the primary button for secondary actions: "Compare", "Download Datasheet", "View Accessories". On hover, the teal border color fills the background to echo the primary interaction pattern.

**`button-ghost`** — Transparent background with `{colors.hairline}` border and `{colors.body}` text. Used in filter toolbars, pagination controls, and utility actions that should not compete with the main product hierarchy. Height 36px to subordinate clearly to the 44px primary pair.

### Text Input

**`text-input`** — 44px height, `{rounded.xs}` corners, 1px `{colors.hairline}` border at rest. Focus ring switches to 1.5px `{colors.primary}` teal, matching the brand primary without introducing a new color token. Placeholder text in `{colors.muted}`. Applied to search fields, contact and quote-request forms, and model-number lookup inputs.

### Navigation

**`nav-bar`** — Near-black (#080808) top bar with white type and the Extech logo mark accented in `{colors.primary}` teal. Contains product category links, a dark-background search input (`{colors.surface-dark}`) with a teal search icon, and account/cart utilities at right. Height 64px. No bottom border — the near-black bar creates its own visual boundary against any page content below.

**`category-nav`** — Secondary navigation bar in `{colors.surface-soft}` with a 1px `{colors.hairline-soft}` bottom border. Lists instrument categories in `{typography.nav-link}`: HVAC, Electrical, Environmental, Thermal Imaging, Safety, and Accessories. Active category is indicated by a 2px solid `{colors.primary}` bottom border and `{colors.primary}` text color. On tablet and mobile, the bar scrolls horizontally with labels abbreviated.

**`breadcrumb`** — Small `{typography.caption}` trail in `{colors.muted}`, with chevron separator in `{colors.hairline}`. The current page segment renders in `{colors.ink}`. Positioned above product titles on all detail and category pages to reinforce navigation depth in a multi-level instrument taxonomy.

### Product Card

**`product-card`** — White card with `{rounded.xs}` corners and a 1px `{colors.hairline-soft}` border. Image area uses `{colors.surface-soft}` background at a 4:3 aspect ratio for consistent product photo framing across the catalog. Model number appears above the product name in `{typography.model-number}` (Industry-Light, uppercase, tracked) in `{colors.muted}`. Product name renders in `{typography.title-sm}`, price in `{typography.title-md}` in `{colors.primary-active}`. A full-width `button-primary` anchors the card bottom. Measurement or certification badges (`measurement-badge`) float over the image corner on hover.

### Hero Banner

**`hero-banner`** — Near-black (#080808) background with the display headline in `{typography.display-xl}` (Industry-Light 48px) in `{colors.on-dark}`, and a teal accent used in highlight spans or rule elements. Minimum 480px height. Subheadline in `{typography.body-md}`. Primary teal CTA button placed directly below the subheadline. On desktop, product or use-case photography occupies the right half; on mobile, the image collapses to a full-width banner behind the text block.

### Spec Components

**`spec-callout`** — Light gray (`{colors.surface-soft}`) card used to highlight a single measurement value: e.g., "±0.5°C" or "1000V CAT IV". The value renders in `{typography.spec-display}` (Industry-Light 36px) in `{colors.primary}` teal; the unit label below in `{typography.spec-label}` (11px Museo Sans, uppercase, tracked 0.8px) in `{colors.muted}`. Four to six callouts appear in a horizontal row on product detail pages, reducing to two-per-row on tablet and mobile. The format echoes the readout display aesthetic of the instruments themselves.

**`spec-table`** — Full-width specification table with a `{colors.surface-soft}` header row in `{typography.spec-label}` (uppercase, tracked). Body rows alternate between `{colors.canvas}` and `{colors.surface-soft}` for scan-ability across dense data. Border lines in `{colors.hairline}`. Columns cover range, resolution, accuracy, operating temperature, display type, and certifications. Treated as primary content on product detail pages, not collapsed behind a toggle by default.

### Badges

**`measurement-badge`** — Teal fill (`{colors.primary}`, white text, `{rounded.xs}`) used on product cards and search results to tag instrument classifications or certifications: "IP54", "CAT III", "Data Logging", "Bluetooth". Text in `{typography.badge}` (Museo Sans bold, 11px). Multiple badges can stack in a horizontal row below the product title.

**`warning-badge`** — Amber (#ffc425) background with dark `{colors.ink}` text, same shape and typography as `measurement-badge`. Used for "New Model", "Sale", or safety-rating callouts. The amber registers immediately as a caution signal, consistent with the physical instrument design language where yellow indicates caution or measurement-range limits.

### Filter Pills

**`category-filter-pill`** — Pill-shaped (`{rounded.full}`) filter chip in `{colors.surface-soft}` at rest; switches to `{colors.primary}` fill with `{colors.on-primary}` text when selected. Used on product listing pages to filter by measurement discipline, display type, or IP/CAT rating. Multiple selections are allowed simultaneously.

### Search

**`search-bar`** — Dark background (`{colors.surface-dark}`) input sitting inside the `nav-bar`, 44px height, `{rounded.xs}` corners, with a `{colors.teal-mid}` search icon at left. On desktop, focus expands to show an autocomplete dropdown in a white panel with results grouped by category. On mobile, tap opens a full-screen search overlay with the keyboard raised immediately.

### Product Detail Panel

**`product-detail-panel`** — Right-side panel on product detail pages. Product name in `{typography.display-sm}`, model number in `{typography.model-number}` in `{colors.muted}`, price in `{typography.display-sm}` in `{colors.primary-active}`. Contains quantity selector, primary "Add to Cart" button, and secondary "Request a Quote" button. Padded at `{spacing.xl}` with a 1px `{colors.hairline-soft}` border separating it from the specification content area at left.

### Footer

**`footer`** — Dark background (`{colors.surface-dark}`) with a 2px `{colors.primary}` teal top border as the single brand signal entering the footer. White body text, `{colors.teal-mid}` link color. Four-column grid on desktop: Product Categories, Support & Resources, About Extech, and Contact/Social. Collapses to accordion-style single column on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category-nav scrolls horizontally with abbreviated labels; search opens full-screen overlay; hero collapses to stacked text-over-image at 320px min-height; spec-callouts reflow to 2-per-row; spec-table scrolls horizontally |
| Tablet | 744–1128px | 2-column product grid; category-nav shows full labels if space permits; hero at 400px with text left, image right at reduced size; spec-callouts in 3-per-row; footer in 2-column grid |
| Desktop | 1128–1440px | 3–4 column product grid; full category-nav; hero at 480px+ with side-by-side layout; spec-callouts in 4–6 across; product detail panel floats right alongside image carousel |
| Wide | > 1440px | Max-width container centered at ~1400px; product grid holds at 4 columns; hero background bleeds edge-to-edge with content constrained to max-width |

### Touch Targets

- All buttons and interactive elements minimum 44px height
- Category filter pills padded to 36px effective touch height on mobile
- Nav items minimum 48px tap target in mobile drawer menu
- Product cards fully tappable as a single hit target — no dead zones between image and text
- Spec-table cells not interactive; no minimum tap height required

### Collapsing Strategy

- Top navigation collapses to hamburger at mobile breakpoint; category-nav moves inside the drawer as a secondary list
- Spec table preserves all columns and scrolls horizontally on mobile — data truncation is not acceptable for instrument specs
- Spec callout rows reflow from 4–6 across on desktop to 2-per-row on mobile; values remain large and legible
- Footer columns collapse to a single accordion column on mobile, with each section header tappable to expand
- Hero text block stacks above image on mobile; image becomes an aspect-ratio-locked banner below the headline

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white (#ffffff) canvas color not present in extracted palette; assumed as default page background — verify against live site rendering
- No custom icon set identified; Bootstrap Icons detected in font stacks, suggesting default icon system — brand-specific icon style, stroke weight, and fill treatment unconfirmed
- Exact button border-radius may differ from `{rounded.xs}` (4px); Bootstrap default is ~0.375rem (6px) — verify in browser devtools
- Product card hover state (box-shadow depth, transform lift, overlay behavior) not extractable from static color analysis
- Mobile nav drawer pattern not confirmed — hamburger-to-drawer vs. slide-in bottom sheet unclear
- Dark mode support unknown; #1a1d20 and #323339 suggest dark-surface usage but a full dark-mode token set is not confirmed
- Industry font weight range not fully confirmed — "Industry-Light" detected; whether Industry-Regular or Industry-Bold are used for emphasis is unverified
- Museo Sans exact weights used for heavy emphasis not extracted — semibold assumed at 600, bold at 700
- Price display formatting (sale price strike-through, currency symbol sizing, tax-included label) not confirmed
- Bootstrap utility colors (#198754, #0dcaf0, #d63384, #0d6efd) appear in the extracted palette and are likely framework defaults rather than intentional brand tokens — use with caution
