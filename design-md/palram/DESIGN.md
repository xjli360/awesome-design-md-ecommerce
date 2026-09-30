---
version: alpha
name: "Palram"
source_url: "https://www.palramcanopy.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Twin-wall polycarbonate panels diffuse July noon into something closer to late-afternoon light — that optics principle carries straight through Palram's interface, which lives in soft whites and one assertive garden green rather than the high-contrast brutalism that dominates hardware retail. The primary green (#2d7e34) reads as natural authority, not decoration: it marks every CTA, every category badge, every structural accent with the confidence of a brand that has been extruding polycarbonate since 1963. Body copy and product specs sit on a clean `#ffffff` canvas with generous gutters, letting dimensional drawings and product photography carry the persuasive weight that consumer brands assign to lifestyle imagery. Navigation is dense and functional — six to eight top-level categories organized horizontally with dropdown mega-panels — because the buyer arriving at Palram already knows what a lean-to greenhouse is and needs to compare 6×8 vs. 8×12 footprints rather than be sold on gardening as a concept. Product cards present model numbers prominently alongside common names, a signal that trade and prosumer audiences are co-equals with residential buyers. Rounded corners stay minimal: `{rounded.xs}` to `{rounded.sm}` at most. The panels are angular, the structures are rectilinear, and the UI respects that geometry — no soft pill shapes, no consumer-brand friendliness theater. A lighter green tint (`{colors.surface-green}`) appears behind category modules and promotional strips, giving a greenhouse-glass warmth without pastels. An amber accent (`{colors.accent-amber}`) marks new SKUs and clearance badges, cutting visually against the green without introducing a third brand axis. The overall register is confident and encyclopedic — a system built for product comparison rather than aspirational lifestyle.

colors:
  primary: "#2d7e34"
  primary-active: "#1e5c24"
  primary-disabled: "#a8d5ac"
  primary-light: "#e8f5e9"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dddddd"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  surface-green: "#eef7ef"
  on-primary: "#ffffff"
  accent-amber: "#e07c24"
  error: "#d32f2f"
  footer-bg: "#1a2e1b"
  footer-text: "#c8ddc9"

typography:
  display-xl:
    fontFamily: "'Montserrat', 'Arial', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', 'Arial', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', 'Arial', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', 'Arial', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', 'Arial', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  spec-label:
    fontFamily: "'Montserrat', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  model-number:
    fontFamily: "'Courier New', 'Courier', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Montserrat', 'Arial', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', 'Arial', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
  nav-link:
    fontFamily: "'Montserrat', 'Arial', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
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
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-green}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
    textColor: "{colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 36px
  top-utility-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.spec-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.10)"
    padding: "{spacing.lg}"
    columnGap: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 16px
    height: 44px
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitRounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    modelTypography: "{typography.model-number}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    hoverBorderColor: "{colors.primary}"
    hoverBoxShadow: "0 2px 12px rgba(45,126,52,0.12)"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  product-badge-new:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.section}"
    overlay: "rgba(0,0,0,0.45)"
    heightDesktop: 480px
    heightMobile: 320px
    ctaComponent: button-primary
  category-tile:
    backgroundColor: "{colors.surface-green}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    iconSize: 40px
    hoverBorderColor: "{colors.primary}"
  specs-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowHeight: 40px
    altRowBackgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  promo-banner:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary-active}"
    typography: "{typography.body-sm}"
    borderLeft: "4px solid {colors.primary}"
    padding: "{spacing.base} {spacing.lg}"
  pagination:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    size: 36px
  compare-toggle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    checkedBackgroundColor: "{colors.primary}"
    checkedTextColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    minHitArea: 40px
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.section}"
    borderTop: "4px solid {colors.primary}"

## Components

### Buttons

**`button-primary`** — Rectangular with 4px radius (`{rounded.xs}`), uppercase tracking at `{typography.button-md}`, filled in garden green `{colors.primary}`. Active state deepens to `{colors.primary-active}` with no transition easing — the instant snap matches the brand's assembly-instruction directness. Disabled state uses the washed `{colors.primary-disabled}` tint with `cursor: not-allowed`; no opacity shift.

**`button-secondary`** — White fill with a 2px green border; the outline echoes polycarbonate panel framing profiles. On hover the interior fills with `{colors.surface-green}`, preserving legibility while confirming activation. Used for secondary CTAs like "Download Specs" alongside a primary "Add to Cart."

**`button-ghost`** — Transparent background for inline tertiary actions such as "View all accessories" or "Compare models." Renders in `{typography.button-sm}` at `{colors.ink}`; underline appears on hover. No border, no fill.

### Navigation

**`top-utility-bar`** — A 36px strip in `{colors.primary}` sitting above the nav bar. Contains micro-copy at `{typography.caption}` for free-shipping thresholds, dealer locator, and language/region toggle. Sets the brand color before any product content appears.

**`nav-bar`** — 64px white bar with 1px hairline underline. Logo left-anchored at 36px height. Nav links flat-weighted at `{typography.nav-link}` 600; the active category gains a 2px underline in `{colors.primary}`. Cart and account icons right-anchored; search bar centered.

**`nav-dropdown`** — Full-width mega-panel on category hover, structured in two to four columns of subcategories with small product thumbnails and dimension callouts. Each column headed by a `{typography.spec-label}` uppercase label. Rendered on a white card with 1px hairline border and a soft 10% opacity shadow lift.

### Forms

**`text-input`** — 48px tall, `{rounded.xs}` radius, 1px hairline border at rest. Focus switches border to `{colors.primary}`. Error state colors border and helper text `{colors.error}`. Labels sit above the field, left-aligned in `{typography.caption}`, never floating.

**`search-bar`** — Full-width bar with an attached submit button flush-right: the input takes `{rounded.xs}` on the left two corners, the submit button gets `{rounded.none}` forming a rectangular connected block. Submit fills `{colors.primary}` with a magnifier icon in `{colors.on-primary}`.

### Product Card

**`product-card`** — 1px hairline border, `{rounded.xs}` radius, 4:3 product image above a text block. Model number renders in `{typography.model-number}` (monospace, 12px) directly above the common name in `{typography.title-sm}`. Price at `{typography.title-md}` weight 600. Hover elevates border to `{colors.primary}` with a soft green-tinted shadow. A `product-badge` pinned to the image corner carries "IN STOCK" or size-range text in primary green; `product-badge-new` uses `{colors.accent-amber}` for new SKUs.

### Specs Table

**`specs-table`** — Two-column key/value table for product specification panels (footprint, ridge height, panel thickness, UV protection class, warranty). Labels in `{typography.spec-label}` uppercase; values in `{typography.body-sm}`. Alternating rows between `{colors.surface-soft}` and `{colors.canvas}`. Appears inline on PDPs below the image carousel.

### Category Tiles

**`category-tile`** — Soft green-tinted card (`{colors.surface-green}`) with a 40px product silhouette icon, title in `{typography.title-sm}`, and a hairline border that switches to `{colors.primary}` on hover. Arranged in a 4-column grid on homepage to route buyers directly to Greenhouses, Carports, Sheds, and Pergolas without lifestyle interstitials.

### Hero Banner

**`hero-banner`** — Full-bleed product photography with a 45% dark scrim. Title in `{typography.display-xl}` white, supporting copy in `{typography.body-md}`, CTA button left-anchored using `button-primary`. 480px tall on desktop, 320px on mobile. No carousel or video autoplay — one image, one message per seasonal campaign.

### Promo Banner

**`promo-banner`** — Inline alert strip in `{colors.primary-light}` with a 4px left border in `{colors.primary}`. Used for shipping thresholds, seasonal promotions, and warranty callouts inline within the browse or PDP flow without modal interruption.

### Compare Toggle

**`compare-toggle`** — Checkbox-style toggle that appears on product card hover, enabling multi-SKU comparison. Idle: hairline border, `{colors.muted}` label text. Checked: fills `{colors.primary}`. A sticky "Compare (N)" bar docks to viewport bottom when two or more items are selected, with a "Compare Now" `button-primary`.

### Footer

**`footer`** — Deep forest background (`{colors.footer-bg}`), 4px `{colors.primary}` top border. Column headings in `{colors.canvas}` at `{typography.title-sm}`; link text in muted green `{colors.footer-text}` at `{typography.body-sm}`. Columns cover: Products, Resources (assembly guides, CAD files, installation videos), Support, and Company. Bottom row carries copyright, social icons, and certification logos (ISO, ASTM).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-screen overlay drawer and accordion subcategory expansion; hero 320px tall; specs table gains horizontal scroll; search bar expands to full width below nav |
| Tablet | 744–1128px | Two-column product grid; nav stays horizontal but mega-dropdown collapses to two columns; category tiles shift to 2×2 grid |
| Desktop | 1128–1440px | Three- to four-column product grid; full mega-nav; hero 480px; specs table inline on PDP |
| Wide | > 1440px | Content capped at 1400px max-width, centered; nav and footer gutters expand symmetrically; hero background extends edge-to-edge behind capped content column |

### Touch Targets

- All buttons and interactive tiles minimum 44×44px
- Product card tap target covers full card surface, not title text only
- Compare toggle minimum 40px hit area regardless of visual checkbox size
- Navigation drawer links minimum 48px row height
- Pagination controls minimum 44px square

### Collapsing Strategy

- Mega-nav collapses to slide-in overlay drawer on mobile; subcategory groups become accordion rows
- Specs table wraps in a horizontally scrollable container below 480px viewport width
- Category tile grid: 4-col → 2-col → 1-col at mobile
- Footer columns collapse to stacked accordions on mobile with expand/collapse chevrons
- Hero: headline → supporting copy → CTA button stacks single-column; image becomes background only
- Product card model number hidden on mobile to reduce text density; surfaced in expanded detail view

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — site appears to load design tokens via JavaScript or sits behind anti-bot protection; all palette values are cautiously inferred from publicly visible brand presence and must be verified against live computed styles before shipping
- **No font families extracted** — Montserrat + Open Sans are plausible inferences for this product category but are unconfirmed; Palram may use a licensed or OEM typeface not identifiable from brand memory
- **Primary green exact hex** — #2d7e34 is a cautious inference; the actual brand green may differ by 10–20 lightness units; verify against CSS or brand style guide
- **Accent amber exists or not** — #e07c24 is assumed from common hardware/outdoor sector conventions; may not appear in the actual Palram palette
- **Button radius** — 4px (`{rounded.xs}`) is inferred from the brand's rectilinear product geometry; actual value could be 0px (fully square) or up to 8px
- **Footer background tint** — `{colors.footer-bg}` (#1a2e1b) is inferred as a deep forest green; may be a neutral near-black with no green undertone
- **palramcanopy.com scope** — unclear whether this domain is the primary e-commerce property or a regional/campaign subdomain; design tokens may differ from palram.com's main system
- **Nav height and utility bar presence** — 64px + 36px is estimated; exact dimensions and whether the utility bar is present on palramcanopy.com specifically are unconfirmed
