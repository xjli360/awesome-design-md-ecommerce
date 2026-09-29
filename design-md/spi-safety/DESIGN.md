---
version: alpha
name: "SPI Safety"
source_url: "https://www.spisafety.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Four ANSI Z535-derived signal colors — #bd2426 safety red, #9bca3e hi-vis lime, #f68b1f safety orange, and #ee730a amber — sit alongside a corporate deep navy (#003681) that anchors the catalog with institutional authority. The palette is not decorative but regulatory: each color carries a specific hazard-communication meaning inherited from OSHA and ANSI standards, so UI designers cannot reassign them freely — danger is red, caution is orange, notice is navy-blue (#0051c3), and emergency-safe is green. SPI Safety's digital presence inherits this color grammar from physical safety signage and PPE labeling, giving the site a distinctly industrial vocabulary that consumer e-commerce rarely employs. Typography runs entirely on system stacks — Roboto, Segoe UI, Helvetica Neue, -apple-system — signaling a functional, procurement-first environment where engineers and safety managers search by ANSI classification and SKU rather than browse editorial content. The absence of a custom typeface is itself a design signal: this is a B2B catalog, not a lifestyle destination, and the system font reads as institutional neutrality rather than an oversight. Surfaces hold in light gray (#ebebeb, #dedede) against near-white canvas, with near-black text (#313131, #404040) carrying specification copy. Corners are minimal or sharp; industrial catalog conventions favor grid density and scannable rows over soft consumer padding. A hi-vis lime (#9bca3e) deployed for "in-stock" indicators and compliance callouts is the most chromatically distinctive element in the palette, standing out precisely because it mimics the reflective tape on high-visibility vests — on a warehouse monitor under fluorescent light, it remains unambiguous. Monospace type appears in SKU codes and part-number fields, treating procurement identifiers as machine-readable strings. The brand communicates fitness-for-purpose over visual aspiration: a safety officer buying cut-resistant gloves needs ANSI cut levels and reorder codes, not brand storytelling.

colors:
  primary: "#003681"
  primary-active: "#0045a6"
  primary-light: "#0051c3"
  primary-disabled: "#7aa3d0"
  danger: "#bd2426"
  danger-active: "#9e1e20"
  warning: "#f68b1f"
  warning-active: "#ee730a"
  notice: "#2f7bbf"
  safe: "#9bca3e"
  safe-active: "#7aaa20"
  ink: "#313131"
  body: "#404040"
  muted: "#666666"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#ebebeb"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  on-danger: "#ffffff"
  on-warning: "#ffffff"

typography:
  display-xl:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  compliance-tag:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  sku-code:
    fontFamily: "'Courier New', courier, monaco, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.3px
  spec-header:
    fontFamily: "Roboto, 'Helvetica Neue', Arial, -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.6px
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 40px
  button-danger:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-danger}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-warning}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary-light}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 38px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "3px solid {colors.warning}"
  nav-top-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-sm}"
    skuTypography: "{typography.sku-code}"
    priceTypography: "{typography.title-md}"
  safety-badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-danger}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  ansi-tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  in-stock-badge:
    backgroundColor: "{colors.safe}"
    textColor: "{colors.canvas}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  warning-tag:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-warning}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  notice-tag:
    backgroundColor: "{colors.notice}"
    textColor: "{colors.on-primary}"
    typography: "{typography.compliance-tag}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    accentBorderLeft: "4px solid {colors.warning}"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    hoverBorder: "1px solid {colors.primary-light}"
    padding: "{spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    inputTypography: "{typography.body-md}"
    buttonBackgroundColor: "{colors.warning}"
    buttonTextColor: "{colors.canvas}"
    buttonTypography: "{typography.button-md}"
    height: 44px
  spec-table:
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.spec-header}"
    rowBackgroundColor: "{colors.canvas}"
    rowAltBackgroundColor: "{colors.surface-soft}"
    cellTypography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.caption}"
    separator: "/"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    accentColor: "{colors.safe}"

## Components

### Buttons

**`button-primary`** — Deep navy (#003681) fill with white uppercase text at 14px/600 weight and 0.5px tracking; 2px corner radius ({rounded.xs}) reads as a functional catalog tool rather than a rounded consumer CTA. Active state shifts to #0045a6; disabled state bleeds to {colors.primary-disabled}. Used for primary procurement actions: "Add to Cart," "Request a Quote," "Order Now."

**`button-secondary`** — White canvas with a 1px navy border and navy uppercase text, matching the {typography.button-md} treatment. Communicates a lower-commitment action — "Download SDS," "View Full Specs," "Compare" — alongside the primary's harder "add to cart" weight. Hover state can darken border to {colors.primary-active}.

**`button-danger`** — #bd2426 fill inheriting the ANSI Z535 DANGER signal red. Reserved strictly for destructive or safety-critical UI actions such as removing items from a saved order or flagging a compliance issue. All uppercase treatment matches the button family for scan consistency.

**`button-warning`** — Safety orange (#f68b1f) fill for high-visibility promotional CTAs — clearance callouts, limited-availability alerts, or banner actions where the color's ANSI "caution" reading reinforces urgency rather than contradicts it. White uppercase text at {typography.button-md}.

### Search Bar

**`search-bar`** — A 44px-tall full-width input with a 2px navy border, flushed against an orange (#f68b1f) submit button on the right. The orange button is the highest-contrast interactive element on the page — deliberate for buyers on warehouse workstations under high ambient light. Input uses {typography.body-md}; the button inherits {typography.button-md} uppercase to remain legible at distance. The 2px border distinguishes search from standard text inputs at a glance.

### Navigation

**`nav-bar`** — Full-width deep navy (#003681) at 56px with a 3px safety-orange bottom border that serves as both a visual ground line and a brand-color accent. Links render in white {typography.nav-link} at 14px/500. A thinner black utility bar (`nav-top-bar`) at 32px sits above, carrying phone numbers, quick-order entry, and account shortcuts in 12px caption — a B2B staple that keeps transactional utilities visually separate from product navigation.

### Product Card

**`product-card`** — White canvas card with 1px #dedede border and 4px radius. The product image fills a 1:1 crop; below it the product title renders in {typography.title-sm} (15px/600) and the SKU in monospace {typography.sku-code}, making part numbers instantly copy-paste-ready for procurement systems. Price renders in {typography.title-md} at 18px/600. Compliance badge chips — `safety-badge`, `ansi-tag`, `in-stock-badge` — stack as flat zero-radius chips beneath the image in the ANSI signal-color hierarchy (red → orange → blue → green).

### Safety & Compliance Badges

**`safety-badge`** — #bd2426 red chip with all-caps {typography.compliance-tag} text (10px/700/0.8px tracking), zero corner radius. Carries ANSI DANGER-class ratings, hazard classification flags, or end-of-life product warnings. The hard corner signals regulatory context, not a design choice.

**`ansi-tag`** — Same flat geometry as `safety-badge` but in primary navy; references the ANSI/ISEA standard number directly (e.g., "ANSI Z87.1," "ISEA 105-2016"). Appears adjacent to or below the safety-badge on product cards.

**`in-stock-badge`** — Hi-vis lime (#9bca3e) chip, the most chromatically distinctive element in the entire UI. Signals available inventory without ambiguity across every monitor calibration and color-vision profile. Zero corner radius keeps it within the badge family.

**`warning-tag`** — Safety orange (#f68b1f) chip for CAUTION-class hazards or limited-stock alerts. Together with `safety-badge`, `notice-tag`, and `in-stock-badge`, it forms a four-color badge system that mirrors the physical ANSI Z535 signal-word hierarchy: red DANGER → orange WARNING → blue NOTICE → green SAFE.

### Hero

**`hero`** — Navy canvas with white display type ({typography.display-xl} at 32px/700). A 4px left-edge orange rule (`accentBorderLeft`) echoes the color-coding of safety tape and industrial signage, anchoring the content block without introducing imagery. Body copy in white 14px/400. CTA sits in `button-warning` (orange) for maximum contrast against the navy field; secondary action uses `button-secondary` with white border override. Vertical padding is {spacing.section} to give the hero mass without relying on a full-bleed photograph.

### Specification Table

**`spec-table`** — Navy header row (#003681) with white uppercase column labels in {typography.spec-header} (12px/700/0.6px tracking); alternating white and #ebebeb data rows in {typography.body-sm}. 1px #dedede cell borders. This is the most information-dense component in the catalog — used for cut levels (ANSI/ISEA 105), impact resistance ratings, arc-flash cal/cm², chemical-resistance matrices, and size charts. Column headers use uppercase to visually separate attribute labels from data values, which are mixed-case.

### Category Tile

**`category-tile`** — White card with 1px hairline border, 4px radius, and navy title text in {typography.title-sm}. Hover sharpens the border to 1px #0051c3. Tiles sit in a dense grid (4–6 columns at desktop) to surface the full PPE category tree — head protection, eye and face, hand, foot, fall protection, respiratory — without requiring vertical scroll. Icon or photo treatment sits above the label.

### Footer

**`footer`** — Near-black (#313131) canvas with white body links and section headings in {typography.title-sm}. Hi-vis lime ({colors.safe}) appears as an accent on the compliance certifications line or brand mark — the one context where the lime reads as institutional credibility (certified/approved) rather than inventory availability. Footer link groups cover product categories, regulatory resources, SDS sheets, and account/order-management utilities.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; search bar runs full width below the bar; spec tables scroll horizontally with sticky first column; category tiles reduce to 2-column grid; `nav-top-bar` collapses into hamburger menu |
| Tablet | 744–1128px | 2–3 column product grid; top-level nav categories visible, secondary utilities collapse; hero display type reduces to 24px; spec table columns condense to 4–5 visible with horizontal scroll |
| Desktop | 1128–1440px | Full `nav-bar` at 56px with `nav-top-bar` above; 4-column product grid; hero at full {typography.display-xl}; category tile grid 4–6 across; spec tables fully visible without scroll |
| Wide | > 1440px | Content max-width capped ~1400px, centered; hero background fills edge-to-edge while content block stays constrained; no new layout shifts |

### Touch Targets

- All buttons minimum 40px height; icon-only controls minimum 44×44px
- Mobile nav items 48px touch height — gloved-hand accessibility is a genuine end-user concern for buyers who are also production floor workers
- Badge chips in product cards are display-only at mobile; the entire card is the tap target
- Search submit button minimum 44px wide on mobile to accommodate imprecise finger input

### Collapsing Strategy

- `nav-top-bar` (phone, quick-order, account shortcuts) collapses into the hamburger drawer as a top section on mobile
- Multi-tier category navigation collapses depth-first: L3 subcategories hidden first, L2 on the smallest breakpoints, with an "All Categories" entry as fallback
- Specification tables use horizontal scroll with a sticky first column rather than stacking rows, preserving the meaning of multi-attribute comparison layouts
- Safety badge chips switch from horizontal wrap to vertical stack below product title on mobile to prevent badge truncation at narrow widths
- Hero accent border rule scales from 4px to 3px on mobile; headline drops from 32px to 22px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned a 522 Connection Timed Out during extraction; palette and font data derive from a partial crawl and may not represent the complete live design system
- No custom brand typeface detected; all fonts are system defaults — it is unclear whether a licensed font loads via JS after initial paint
- No meta theme-color found; mobile browser chrome tint color is unknown
- Exact nav-bar height, mega-menu structure, and hover/dropdown behavior could not be confirmed from the timeout response
- Button and card border-radius values are estimated from industrial catalog conventions; actual rendered values may be sharper (0px) or differ from the xs/sm tokens used here
- Logo dimensions, wordmark construction, and icon system (custom SVGs vs. third-party library such as Font Awesome) could not be extracted
- Dark-mode or high-contrast accessibility variant unknown
- Pricing display pattern (list price vs. contract/account price vs. "call for pricing") not confirmed
- Whether #9bca3e actually functions as an in-stock indicator or serves another UI role (e.g., promotional ribbon, brand accent) is inferred from safety industry conventions, not confirmed from a live page
