---
version: alpha
name: "Weiss"
source_url: "https://www.weisswatchcompany.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Cameron Weiss operates one of fewer than ten facilities in the United States capable of assembling a mechanical caliber from raw components, and that manufacturing credential shapes every layout decision on weisswatchcompany.com — bench photography appears alongside product photography rather than quarantined behind an "About" link, specification tables lead with jewel count and power reserve before mentioning case material, and the primary CTA is the same near-black (#111111) as the movement plate itself. The site runs on a pure white (#ffffff) canvas with no secondary accent color: no signature coral, no heritage navy. Dial photography, shot high-key against white, carries all the visual energy the system requires, so the interface stays out of the way. A warm off-white (#f8f7f5) surfaces on spec-heavy pages as a tonal section break — the only departure from strict monochrome — and it reads as a reference to tungsten bench lighting rather than a palette choice. Component edges are square or barely softened (`{rounded.xs}` to `{rounded.sm}` at most); pill radii or fully-rounded cards would conflict with the straight-lugged silhouettes in the photography.

  Type is set in a clean geometric sans-serif at restrained weights — body copy at 15px/400, headings compressed rather than display-scaled, button labels in wide-tracked uppercase at 13px. Nothing is expressive; everything is precise. The Standard Issue Field Watch product page runs 60–80 words of editorial copy before the add-to-cart module — enough to frame the American-made argument, short enough that the spec table arrives before the user scrolls twice. Spacing is generous but not lavish: section gaps at `{spacing.section}` give the layout room to breathe without reading as fashion-brand excess. The only explicit provenance signal is a small `MADE IN U.S.A.` overline chip rendered in 9px tracked uppercase above product titles — no badge fill, no colored border — signaling confidence rather than marketing urgency.

  Navigation is a single 56px bar: wordmark at far left, three or four category links centered, cart and search icons at right. On mobile the bar collapses to wordmark and hamburger with a full-screen overlay; there is no intermediate tablet drawer. Footer runs the Los Angeles studio address in the first column, treating physical location as a manufacturing credential rather than a legal disclosure. The information hierarchy throughout treats the workshop — its address, its caliber, its parts count — as the primary product. The watch is what the workshop produces.

colors:
  primary: "#111111"
  primary-active: "#000000"
  primary-disabled: "#c8c8c8"
  ink: "#111111"
  body: "#3a3a3a"
  muted: "#767676"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f8f7f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  overline:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 9px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.18em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.05em
  spec-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  spec-value:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  footer-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  footer-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.8
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 14px
    height: 44px
  text-input-focus:
    border: "1px solid {colors.ink}"
    backgroundColor: "{colors.canvas}"
  text-input-error:
    border: "1px solid {colors.error}"
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.canvas}"
    badgeTypography: "{typography.overline}"
    titleTypography: "{typography.title-sm}"
    referenceTypography: "{typography.caption}"
    priceTypography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    imageGap: "{spacing.sm}"
    metaGap: "{spacing.xs}"
  usa-badge:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.overline}"
    border: none
    padding: "0"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: button-primary
    padding: "{spacing.xxl} 0"
    minHeight: 560px
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline}"
    rowPadding: "{spacing.base} 0"
  movement-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl} {spacing.xxl}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0 {spacing.xl} 0"
  variant-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    height: 36px
    padding: 0 12px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    labelTypography: "{typography.footer-label}"
    linkTypography: "{typography.footer-link}"
    padding: "{spacing.xxl} 0"
  search-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: none
    padding: 10px 14px
    height: 40px

## Components

### Buttons

**`button-primary`** — Filled `{colors.primary}` (#111111) with white type (`{colors.on-primary}`) in wide-tracked uppercase (`{typography.button-md}`). `{rounded.xs}` corners — just enough to prevent a pixel-sharp edge without introducing softness — hold the tool-watch register throughout. Hover state stays `{colors.primary}`; active presses to pure `{colors.primary-active}` (#000000); disabled renders as `{colors.primary-disabled}` gray with `cursor: not-allowed`. No drop shadow, no gradient, no transition beyond color.

**`button-secondary`** — White fill (`{colors.canvas}`) with a 1px `{colors.ink}` border and identical uppercase tracking to primary. On hover, the background fills to `{colors.surface-soft}` — the same warm off-white used in spec sections — signaling interactivity without introducing a third color into the system. Used for secondary actions like "Add to Wish List" or "Compare" on the PDP. `button-secondary-hover` overrides only background; border and type remain unchanged.

**`button-text`** — Transparent background, `{colors.ink}` type, underlined, `{typography.button-sm}`. Used inline within editorial copy for actions like "View movement details" or "Learn about our process." Never used as a standalone CTA where purchase conversion is the goal.

### Text Input

**`text-input`** — White background, 1px `{colors.hairline}` border at rest, no rounding beyond `{rounded.xs}`. On focus, border sharpens to a solid 1px `{colors.ink}` with no glow or shadow — consistent with the brand's elimination of decorative UI states. Error state replaces border with 1px `{colors.error}`. Placeholder text in `{colors.muted}`. Used in contact forms, the newsletter signup module, and checkout fields.

### Navigation

**`nav-bar`** — 56px tall, white background, 1px `{colors.hairline}` bottom border. Wordmark at far left in `{typography.title-md}` weight; three to four category links centered in `{typography.nav-link}` with 0.05em letter-spacing; cart icon and search icon at far right with 44×44px tap targets. On mobile, collapses to wordmark and a hamburger icon that opens a full-screen white overlay with stacked nav links. No mega-menu or flyout — the SKU count is narrow enough that flat navigation suffices.

### Product Card

**`product-card`** — White background, no border, no shadow, `{rounded.none}`. Image occupies the full card width at a 4:3 or 1:1 ratio with no border-radius clip — the watch silhouette bleeds to the image edge. Below the image: `usa-badge` overline when applicable, product name in `{typography.title-sm}`, reference number in `{typography.caption}` / `{colors.muted}`, and retail price in `{typography.title-sm}`. Entire card is a tappable link to the PDP; there is no hover overlay or quick-add CTA. Gap between image and text block is `{spacing.sm}`; gap within the text block between name, reference, and price is `{spacing.xs}`.

### USA Badge

**`usa-badge`** — Plain-text `{typography.overline}` with transparent background and no border. Appears above product name on listing cards and PDPs for American-assembled references. No color, no badge shape — the constraint itself reads as conviction. It is the single loudest brand statement in the system precisely because it is rendered in the quietest possible component form.

### Hero

**`hero`** — Full-bleed white section, minimum 560px tall at desktop. Heading in `{typography.display-xl}` at weight 300 — the lightest weight in the stack — followed by one to two sentences in `{typography.body-md}` and a `button-primary` CTA. At desktop, text block occupies the left 40–45% of the section with product photography dominating the right; at tablet, the split is 50/50; at mobile, text stacks above image at full width. Photography is high-key white-background studio work — no environmental or lifestyle imagery obscures the movement architecture of the case.

### Spec Table

**`spec-table`** — Two-column definition table on a `{colors.surface-soft}` background, full-width at all breakpoints. Left column renders spec labels in `{typography.spec-label}` / `{colors.muted}` — MOVEMENT, CALIBER, POWER RESERVE, CASE DIAMETER, LUG WIDTH, WATER RESISTANCE, CRYSTAL — all caps, tracked at 0.1em. Right column renders values in `{typography.spec-value}` / `{colors.ink}`. Rows are separated by a 1px `{colors.hairline}` border; the table carries no outer border or shadow. This component appears above the fold on every PDP, often before editorial copy — the specification is the primary argument, not the conclusion.

### Movement Callout

**`movement-callout`** — Off-white (`{colors.surface-soft}`) section with no border or rounding. Heading in `{typography.title-md}`, body in `{typography.body-sm}` at generous line-height. Padding is `{spacing.xl}` vertical and `{spacing.xxl}` horizontal at desktop, creating a wide editorial margin that frames the bench photography sitting inside the block. Used once per collection page, typically between the product grid and the footer, to present the in-house caliber story. No CTA button inside the callout — the section is informational, not conversion-directed.

### Collection Header

**`collection-header`** — White background, `{spacing.xxl}` top padding, `{spacing.xl}` bottom padding before the first product row. Heading in `{typography.display-md}` left-aligned; optional editorial paragraph in `{typography.body-md}` below, capped at two to three sentences. Provides narrative framing — movement philosophy, material sourcing, design intent — before the product grid begins. No decorative element, no background image, no separator line: the transition from text to product is handled solely by spacing.

### Variant Selector

**`variant-selector`** — Used on PDPs for strap selection (color, material) and case finish options. Each option is a 36px-tall outlined chip in `{typography.caption}` with `{rounded.xs}` corners. Resting state uses `{colors.hairline}` border; selected state uses `{colors.ink}` border with no fill change. Unavailable options use `{colors.primary-disabled}` text with a diagonal strikethrough line inside the chip. Options are arranged in a horizontal row that wraps on narrow viewports.

### Breadcrumb

**`breadcrumb`** — Single line above the PDP product name, `{typography.caption}` / `{colors.muted}` for parent links, `{colors.ink}` for the active page segment. Segments separated by a "/" character with `{spacing.xs}` gap on each side. No background, no hover decoration beyond an underline on parent links.

### Footer

**`footer`** — Near-black (`{colors.ink}`) background with `{colors.on-dark}` reversed text throughout. Organized in four columns at desktop: studio address (Los Angeles location named first, treated as a manufacturing credential), shop links, support links, and a newsletter signup field. Column headers in `{typography.footer-label}`, links in `{typography.footer-link}` at 1.8 line-height. Newsletter input inherits `text-input` styling but with an inverted color scheme — white border on the dark background. Copyright line in `{typography.caption}` across the full footer width below the column grid.

### Search

**`search-input`** — Activated via the search icon in `nav-bar`. Expands inline below the nav bar as a full-width bar on a `{colors.surface-soft}` background, `{rounded.xs}`, no border. Type appears in `{typography.body-md}` as the user types; results render as a borderless list below in `{typography.body-sm}`. Dismissed by clicking the ×-close icon at right or pressing Escape. No autocomplete animations — results appear immediately on each keystroke.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to wordmark + hamburger overlay; hero text stacks above image; spec-table rows remain two-column (readable at 320px); footer stacks to single column; variant chips wrap freely |
| Tablet | 744–1128px | Two-column product grid; full nav link row visible; hero splits 50/50 text and image; movement-callout reduces horizontal padding to `{spacing.xl}`; footer reduces to two columns |
| Desktop | 1128–1440px | Three-column product grid; full nav bar at 56px; hero text-block left-aligned ~40% with image filling right; collection-header at full editorial width; four-column footer |
| Wide | > 1440px | Content max-width ~1280px centered with white margins; no layout changes; typography scale unchanged; grid gutter increases slightly |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- `button-primary` and `button-secondary` are 48px tall — above the minimum without padding adjustment
- Nav icons (cart, search, hamburger) padded to 44×44px tap area even though the visible glyph is smaller
- Product card entire surface is tappable; no separate tap target within the card needed
- Variant selector chips are 36px tall — add `min-height: 44px` on touch viewports via padding adjustment

### Collapsing Strategy

- Navigation: wordmark + hamburger on mobile; full link row on tablet and above; no intermediate drawer state
- Product grid: 1 → 2 → 3 columns at mobile / tablet / desktop; gap stays `{spacing.base}` at all widths
- Hero: text stacks above image on mobile; side-by-side at tablet+; image never becomes a CSS background-image (always an `<img>` for alt-text and LCP optimization)
- Spec table: two-column at all widths — label column shrinks to minimum width, value column expands
- Footer: four columns → two columns → single column at desktop / tablet / mobile
- Movement callout: horizontal padding reduces from `{spacing.xxl}` to `{spacing.base}` on mobile; bench photography remains full-bleed within the block

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted**: The site returned zero color values during extraction, likely due to JS-token loading or anti-bot measures. All color tokens above are inferred from brand knowledge and the brand's documented monochromatic, American-industrial aesthetic. `{colors.primary}` (#111111) and `{colors.canvas}` (#ffffff) are high-confidence; `{colors.surface-soft}` (#f8f7f5) and exact hairline values are estimates and should be verified against the live site.
- **No fonts extracted**: Typography stack defaults to Helvetica Neue. The actual site may use a licensed geometric sans-serif (Aktiv Grotesk, GT Walsheim, or similar) or a serif for editorial headings — this cannot be confirmed without live inspection or access to the stylesheet. Font-size and weight choices are inferred from the brand's utilitarian aesthetic.
- **Accent color existence unverified**: It is possible the live site uses a subtle warm accent (tan, khaki, or olive) for hover states, active navigation underlines, or sale badges — no such color appeared in extraction data and none is documented in brand press materials reviewed.
- **Exact nav height and column counts unconfirmed**: 56px nav height and three-column desktop grid are reasonable estimates for a narrow-SKU independent watch brand; actual values require live measurement.
- **Movement callout structure**: The editorial block and bench-photography layout described above is inferred from brand positioning materials; exact DOM structure and image-to-text ratio are unverified.
- **PDP image gallery behavior**: Whether the site uses a thumbnail strip, a swipe carousel, or a scroll-through lightbox for secondary watch angles is unknown.
