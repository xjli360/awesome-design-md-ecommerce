---
version: alpha
name: "Flotec"
source_url: "https://www.floteconline.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Flotec's catalog pages arrive on a warm cream ground (#f0e7d8) rather than the cold white or steel gray typical of industrial distributors — a choice that reads less like a spec sheet and more like a reference catalog you'd keep on a workshop shelf. The primary brand signal is a deep burgundy-maroon (#590202), anchoring header elements and primary calls-to-action against that cream field; the pairing is unusually warm for hydraulics and pneumatics, where teal (#0d6a71) and rust-orange (#d64f38) appear as secondary signals marking technical categories and alert states. The sheer variety of extracted palette entries — pink (#d03c8e), violet (#7c6eb0), lime (#51ae32), canary (#ffed00) — reveals an industrial catalog architecture: each product-line or manufacturer is branded with its own category chip color, so the UI must accommodate dozens of swatches within a neutral scaffold without visual noise. Inter drives all UI type at modest weights; monospace stacks (Consolas, Menlo, SFMono-Regular) surface in part-number and specification fields where scannable fixed-width glyphs matter. Button geometry is crisp and utilitarian — `{rounded.xs}` or `{rounded.sm}`, never pill-shaped — since soft consumer curves would undercut the professional-procurement context. Product cards carry a flat, density-forward layout: thumbnail left, part number in mono type, short description, and an add-to-cart or request-quote action, all set on `{colors.surface-card}` with a `{colors.hairline}` border. The teal (#0d6a71) and green (#009879) appear in table-header stripes and availability badges, borrowing the classic industrial-catalog zebra convention. Navigation is category-heavy, reflecting a distributor model where hydraulics, pneumatics, fittings, valves, and seals each carry enough SKUs to justify their own mega-menu column. Overall, Flotec reads as a no-frills procurement tool that chose warmth over coldness — a small but distinguishing tonal decision in an otherwise conventions-bound product vertical.

colors:
  primary: "#590202"
  primary-active: "#3d0101"
  primary-disabled: "#b36b69"
  secondary: "#0d6a71"
  secondary-active: "#095558"
  accent-rust: "#d64f38"
  accent-orange: "#f18800"
  accent-green: "#009879"
  accent-teal: "#008693"
  ink: "#1d1d1b"
  body: "#545452"
  muted: "#7a8991"
  hairline: "#d9d9d9"
  canvas: "#f0e7d8"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"
  badge-danger: "#e30613"
  badge-warning: "#fdc300"
  badge-success: "#51ae32"
  badge-info: "#04bbef"
  table-stripe: "#cdeafa"
  mono-bg: "#f7f5f2"

typography:
  display-xl:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  part-number:
    fontFamily: "Consolas, 'SFMono-Regular', Menlo, Monaco, 'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  spec-mono:
    fontFamily: "Consolas, 'SFMono-Regular', Menlo, Monaco, 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.01em
  button-sm:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.02em
  nav-link:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  category-label:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  table-header:
    fontFamily: "'Inter', 'Inter Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.04em
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
    padding: 10px 20px
    height: 40px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary}"
    padding: 9px 19px
    height: 40px
  button-teal:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.secondary}"
    typography: "{typography.button-sm}"
    border: none
    padding: 6px 0px
  button-quote:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.secondary}"
    padding: 8px 12px
    height: 40px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.body}"
    padding: 8px 40px 8px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: none
  nav-top-utility:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.caption}"
    height: 32px
  nav-category-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 44px
  mega-menu:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    shadow: "0 4px 12px rgba(0,0,0,0.1)"
    padding: "{spacing.lg} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspect: "1/1"
    partNumberTypography: "{typography.part-number}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
  product-card-hover:
    border: "1px solid {colors.secondary}"
    shadow: "0 2px 8px rgba(13,106,113,0.15)"
  spec-table:
    headerBackground: "{colors.secondary}"
    headerText: "{colors.on-secondary}"
    headerTypography: "{typography.table-header}"
    stripeBackground: "{colors.table-stripe}"
    cellTypography: "{typography.spec-mono}"
    border: "1px solid {colors.hairline}"
    cellPadding: "{spacing.sm} {spacing.md}"
  category-chip:
    typography: "{typography.category-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    height: 22px
  badge-availability-in-stock:
    backgroundColor: "{colors.badge-success}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-availability-lead-time:
    backgroundColor: "{colors.badge-warning}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-availability-out-of-stock:
    backgroundColor: "{colors.badge-danger}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    accentBar: "4px solid {colors.accent-rust}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  part-number-display:
    typography: "{typography.part-number}"
    backgroundColor: "{colors.mono-bg}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  datasheet-link:
    textColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.accent-rust}"
  pagination:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.table-stripe}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xl} {spacing.xxl}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    checkboxAccent: "{colors.secondary}"
    sectionLabelTypography: "{typography.title-sm}"

## Components

### Buttons

**`button-primary`** — Deep burgundy (#590202) fill with white text at 14px/600 weight Inter, 4px radius corners, 40px height. Hover darkens to #3d0101; disabled state uses the muted rose (#b36b69). Used for primary purchase, RFQ, and account actions.

**`button-secondary`** — White fill with a 1.5px burgundy border and matching text; same radius and height as primary. Used for secondary actions like "Add to Comparison" or "Save for Later."

**`button-teal`** — Teal (#0d6a71) fill with white text; serves as the request-a-quote CTA and contact actions where a softer urgency is appropriate.

**`button-ghost`** — Transparent background, teal text, no border; inline links for "View Datasheet," "Download PDF," or catalog navigation.

### Search Bar

**`search-bar`** — Full-width on mobile, 400–600px capped on desktop, white fill with a hairline border that brightens to teal on focus. A search icon button sits right-inset in the field. Placeholder text at muted (#7a8991); results dropdown uses `surface-card` with `hairline` dividers and part numbers rendered in `part-number` monospace typography.

### Navigation

**`nav-top-utility`** — A 32px near-black (#1d1d1b) bar at the very top carrying account, cart, and contact links in 12px caption weight — common in industrial distributor UIs for utility controls.

**`nav-bar`** — 56px burgundy (#590202) bar with the Flotec wordmark and primary search. Text and icons are white. The brand's warmest anchor point.

**`nav-category-bar`** — 44px cream-ground (#f0e7d8) secondary bar with category links in body-weight Inter; bottom-bordered with hairline to separate from content. Mega-menu panels drop from this row.

**`mega-menu`** — Full-width white panel, no border radius, 4px bottom shadow. Category columns laid out in a 4–6 column grid with `category-label` uppercase headers in teal, sub-item links in `body-sm`.

### Product Card

**`product-card`** — White card with 1px hairline border and 4px radius. Layout: square product image top, then SKU/part number in Consolas monospace, product title in `title-sm`, short description in `body-sm`, availability badge, and a row of primary and secondary buttons at the bottom. On hover the border shifts to teal and a soft teal shadow appears.

### Spec Table

**`spec-table`** — Teal (#0d6a71) header row with uppercase white labels at 12px. Alternating rows use `table-stripe` (#cdeafa) for the zebra pattern. Cell content renders in `spec-mono` for scannable fixed-width spec values (pressure ratings, flow rates, thread types). A single outer border at `hairline` weight wraps the table.

### Category Chips & Badges

**`category-chip`** — Small 22px pills with 4px radius used on product listing pages to filter by product line; each manufacturer or line can take a distinct background color drawn from the extended catalog palette (#d03c8e for one brand, #7c6eb0 for another, etc.). Label always in white or near-black depending on contrast.

**`badge-availability-*`** — Three states: in-stock (lime #51ae32), lead-time (canary #fdc300 / ink text), out-of-stock (red #e30613). All 22px, 4px radius, 600-weight uppercase micro-label.

### Part Number Display

**`part-number-display`** — Inline pill with a light warm-gray fill (#f7f5f2), 1px hairline border, Consolas monospace at 13px. Used in product headers, search results, and spec tables wherever the SKU appears as a standalone element.

### Hero Banner

**`hero-banner`** — Full-width burgundy (#590202) section with a 4px rust-orange (#d64f38) left-edge accent bar on the headline block. Display text at 36px/700 weight, body copy at 15px/400. CTA buttons sit below in white (primary reversed) and teal variants.

### Footer

**`footer`** — Near-black (#1d1d1b) ground with a 4px burgundy top border as a brand close. Link text in light blue (#cdeafa) for contrast; column headers in white `title-sm`. Four-column layout on desktop collapsing to accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar full-width below logo; filter sidebar becomes bottom sheet; spec tables scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; utility nav condensed; mega-menu columns reduce to 3; filter sidebar as collapsible left panel |
| Desktop | 1128–1440px | Three-to-four column product grid; full mega-menu; filter sidebar always visible at 240px; spec tables full-width |
| Wide | > 1440px | Content capped at 1440px max-width; centered with canvas background; product grid expands to five columns where density warrants |

### Touch Targets

- All button and chip elements minimum 40px height on touch viewports
- Filter checkboxes padded to 44×44px touch area
- Product card tap target covers full card surface, not just the CTA button
- Pagination controls minimum 40px per page number

### Collapsing Strategy

- Mega-menu category navigation becomes a full-screen slide-in drawer on mobile, with back-navigation for subcategory levels
- Spec tables gain a horizontal scroll container with a sticky first column (attribute label) on narrow viewports
- Product card buttons stack vertically below 480px; side-by-side at 480px+
- Breadcrumb truncates middle segments with ellipsis, always showing root and current page

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed brand-owned typeface — Inter appears via framework default; official custom font (if any) is unknown
- No explicit spacing or grid token documentation extracted; values above are inferred from typical industrial catalog conventions
- The extended palette (#d03c8e, #7c6eb0, #ffed00, #afca0b, #243588, etc.) appears to be per-manufacturer category coloring in a distributor catalog; individual color semantics are unconfirmed
- Meta theme-color was absent, so primary nav color (#590202) is inferred as the intended brand color from its distinctiveness relative to the gray/teal cluster
- No animation or transition values extracted; micro-interaction specs (hover fade, dropdown easing) are unverified
- Logo lockup, wordmark geometry, and icon system details not extractable from color/font hints alone
- Whether the warm cream canvas (#f0e7d8) is a global background or section-specific is unconfirmed
