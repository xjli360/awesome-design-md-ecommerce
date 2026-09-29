---
version: alpha
name: "Rocket Espresso"
source_url: "https://www.rocket-espresso.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Against four grades of gray — #58595b, #a7a9ac, #9ca3af, #eeeeee — one saturated crimson (#b92c32) does all the work: every primary call-to-action, every active state, every hot-metal accent on a palette otherwise held to near-monochrome restraint. The typeface system layers two modern grotesques — ABCMonumentGrotesk for editorial weight and display presence, aktiv-grotesk for body rhythm — with Eurostile appearing in precision-data roles, a nod to the same mid-century European industrial design vernacular that names the brand itself. Buttons hold {rounded.none} everywhere; nothing softens to a pill or an {rounded.md} card corner; even product thumbnails sit inside hard-edged frames. The visual posture is that of a machine you service rather than a product you consume: labelled ports, engraved knobs, hand-polished steel reproduced in flat UI through high-contrast grids, thin-rule separators at {colors.hairline}, and spec sheets that read more like engineering documents than marketing copy. Navigation is restrained — a white {colors.canvas} horizontal bar with no mega-menus, just direct links to machine families and support — keeping the browsing experience as uncluttered as the machines themselves. Product cards surface model names at large display scale in ABCMonumentGrotesk Bold, with secondary specs (boiler type, group count, bar rating) rendered in Eurostile uppercase at caption size against {colors.surface-soft}, creating a two-register hierarchy that separates desire from technical verification. The overall grammar runs deliberately cool: no lifestyle gradients, no warm-filter photography overlays, no rounded hero blobs — just machines photographed clean on white, dimensioned, named, and configured.

colors:
  primary: "#b92c32"
  primary-active: "#9a2228"
  primary-disabled: "#daa0a3"
  ink: "#58595b"
  body: "#58595b"
  muted: "#a7a9ac"
  muted-soft: "#9ca3af"
  hairline: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'ABCMonumentGrotesk Bold', 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'ABCMonumentGrotesk Bold', 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.10
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'ABCMonumentGrotesk Bold', 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'ABCMonumentGrotesk Regular', 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  title-sm:
    fontFamily: "'ABCMonumentGrotesk Regular', 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: 0
  body-md:
    fontFamily: "'aktiv-grotesk', 'ABCMonumentGrotesk Regular', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'aktiv-grotesk', 'ABCMonumentGrotesk Regular', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'aktiv-grotesk', 'ABCMonumentGrotesk Regular', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "Eurostile, 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.9px
    textTransform: uppercase
  model-id:
    fontFamily: "Eurostile, 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.6px
    textTransform: uppercase
  button-md:
    fontFamily: "'ABCMonumentGrotesk Bold', 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'ABCMonumentGrotesk Bold', 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'ABCMonumentGrotesk Regular', 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  footer-heading:
    fontFamily: "Eurostile, 'aktiv-grotesk', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1.2px
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
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
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
    linkHoverColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.display-sm}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    padding: "{spacing.xl}"
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
  hero-full:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    minHeight: 640px
    imagePosition: right
    paddingY: "{spacing.section}"
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    rowBorder: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
  model-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.model-id}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "4px 10px"
  category-tab:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    activeIndicator: "2px solid {colors.primary}"
    typography: "{typography.title-sm}"
    padding: "14px 0"
    gap: "{spacing.xl}"
  machine-configurator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    sectionBorder: "1px solid {colors.hairline}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    selectedBorder: "2px solid {colors.primary}"
    padding: "{spacing.xl}"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    linkColor: "{colors.on-primary}"
  callout-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    borderLeft: "3px solid {colors.primary}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    mutedColor: "{colors.muted}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.footer-heading}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Flat crimson `#b92c32` rectangle, zero border-radius, white ABCMonumentGrotesk Bold uppercase label at 14px with 0.6px letter-spacing. The hard corner is a deliberate engineering-object signature — no softening at any state. Active state shifts to `#9a2228`; disabled washes to `#daa0a3` while retaining white text. Used for all primary e-commerce actions: Add to Cart, Configure, Request a Quote.

**`button-secondary`** — White field with 1px solid `#58595b` border and identical uppercase label in ink. Used for secondary product actions such as Download Specs, Find a Dealer, or Compare — same geometry as primary, pure outline treatment with no fill on hover.

**`button-ghost`** — Transparent fill, 1px solid `#b92c32` border, crimson label. Appears inline within spec sections or editorial callouts where full button-primary weight would overwhelm surrounding text.

### Inputs

**`text-input`** — Zero-radius field, 1px `#eeeeee` border at rest tightening to 1px `#58595b` on focus. Placeholder text renders in `#a7a9ac`. No floating label animation — label sits above the field as a static `{typography.spec-label}` string. Used in dealer finder, newsletter, and support request forms.

### Navigation

**`nav-bar`** — White `#ffffff` horizontal bar, 72px tall, with a 1px `#eeeeee` border-bottom. Logo sits left at 32px height. Links in ABCMonumentGrotesk Regular 14px at `#58595b`; hover transitions link color to `#b92c32` with no underline. Cart icon and locale/region selector are right-aligned. No sticky behavior on scroll — the bar clears the viewport at page top only.

**`category-tab`** — Horizontal tab row for machine family filtering (Home Machines, Commercial, Grinders, Accessories). Inactive tabs render in `#a7a9ac`; active tab shifts to `#58595b` with a 2px solid `#b92c32` bottom underline anchored flush to the tab row's baseline. ABCMonumentGrotesk Regular 15px; gaps of `{spacing.xl}` between tabs; no pill treatment.

### Cards

**`product-card`** — Machine photography displayed full-bleed on an `#eeeeee` soft field, zero border-radius, 1px hairline border. Model name in ABCMonumentGrotesk Bold 24px with tight letter-spacing; secondary descriptor (e.g. "Dual Boiler · E61") in aktiv-grotesk 14px at `#a7a9ac`. A right-arrow Configure link in `#b92c32` sits flush at card bottom with no button chrome — text link only. Model badge floats top-left in Eurostile uppercase.

### Machine Detail

**`spec-table`** — Two-column grid on `#eeeeee` background. Left column uses Eurostile uppercase 11px at `#a7a9ac` for parameter names (BOILER VOLUME, PUMP PRESSURE, HEATING SYSTEM). Right column uses aktiv-grotesk 14px at `#58595b` for values. Rows separated by 1px `#eeeeee` rules; zero radius throughout. The typeface contrast between Eurostile labels and aktiv-grotesk values is the primary visual system on detail pages.

**`model-badge`** — Compact badge displaying machine model code (R58, Mozzafiato, R Nine One) in Eurostile uppercase 13px at `#a7a9ac`. White fill, 1px hairline border, hard corners. Appears on product cards, comparison tables, and breadcrumbs to disambiguate product families.

**`machine-configurator`** — Full-width panel on `#eeeeee` for color-way and grouphead selection on configurable machines. Section headings in Eurostile uppercase 11px at `#a7a9ac`; swatch option labels in aktiv-grotesk 14px at `#58595b`. Selected option border highlights to 2px solid `#b92c32`; unselected swatches hold 1px `#eeeeee` border. Padding `{spacing.xl}` on all sides.

### Editorial

**`callout-block`** — Inline editorial aside on `#eeeeee` surface with a 3px left border in `#b92c32`. Headline in ABCMonumentGrotesk Regular 18px; body in aktiv-grotesk 14px. Used for warranty callouts, hand-assembly claims, or certification notices within long-form product descriptions.

**`hero-full`** — Split-canvas hero: editorial headline in ABCMonumentGrotesk Bold 56px (tight -1.5px letter-spacing) occupies the left half; machine photography bleeds to the right edge. Subheadline in aktiv-grotesk 16px at `#a7a9ac` sits two lines below the display text, followed by a `button-primary`. Background: pure `#ffffff`. Minimum height 640px; 64px vertical padding top and bottom.

### Utility

**`promo-banner`** — 40px full-width strip in crimson `#b92c32`, centered aktiv-grotesk 14px in white. Single-line only; used for financing notices, limited-edition releases, or dealer-event announcements. No close button — persists for session.

**`footer`** — Dark `#58595b` background, full-width. Four-column link grid in aktiv-grotesk 14px white. Column headings in Eurostile uppercase 11px at `#a7a9ac` with 1.2px letter-spacing, matching the spec-label hierarchy used on product pages for visual continuity between detail and navigation contexts. Social icons right-aligned in last column. 64px vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger drawer; hero stacks vertically (image above headline); product grid single-column; spec-table scrolls horizontally; category-tabs overflow-x scroll without wrapping |
| Tablet | 744–1128px | Nav retains full links; hero maintains split layout with tighter image crop; product grid 2-column; machine-configurator moves below product image into a stacked accordion |
| Desktop | 1128–1440px | Full two-column hero; 3-column product grid; spec-table full-width fixed; configurator side panel at ~340px alongside machine imagery |
| Wide | > 1440px | Max-width container (~1380px) centered with white margin flanks; hero inner content constrained; grid gutters widen proportionally |

### Touch Targets

- All buttons minimum 48px height
- `category-tab` tap area padded to 48px tall even when visual text sits at 15px
- Nav links in mobile drawer padded to 56px row height for reliable tapping
- `model-badge` is display-only and non-interactive; no touch-target requirement
- Spec-table rows on mobile expand to 44px height for tappable accordion rows

### Collapsing Strategy

- Hero image stacks above headline text on mobile to preserve editorial legibility before photography loads
- `spec-table` becomes horizontally scrollable on mobile rather than stacking rows — preserves the label/value pairing that defines the table's purpose
- Footer four-column grid collapses to two columns at tablet, then a stacked accordion at mobile with Eurostile headings as accordion triggers
- `machine-configurator` moves from fixed side panel to a bottom sheet on mobile, triggered by a sticky crimson "Configure" bar anchored above the viewport bottom

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Eurostile variant (Regular, Extended, Bold Condensed) used in production could not be confirmed from static extraction; Regular assumed throughout
- No animation or transition timing values extracted; 200ms ease assumed for hover and active state transitions
- Exact desktop grid column count and gutter width unconfirmed; 12-column / 24px gutter assumed
- Presence or absence of a mega-menu on nav hover not determinable from color extraction alone
- Dark mode or alternate color scheme existence unknown; extraction returned light-mode tokens only
- Machine photography aspect ratios (product shots vs lifestyle vs detail) not extractable from palette data; 4:3 assumed for primary product cards
- No box-shadow or elevation tokens extracted; flat shadow-none assumed throughout
- Exact letter-spacing values for ABCMonumentGrotesk in display sizes not confirmed; values estimated from common grotesque display conventions
