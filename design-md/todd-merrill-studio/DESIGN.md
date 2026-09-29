---
version: alpha
name: "Todd Merrill Studio"
source_url: "https://toddmerrillstudio.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric violet (#720eec) lands in a palette that otherwise reads as gallery restraint — warm grays ascending from #eeeeee through #e4e4e4 to near-black #222222, surfaces tinted to barely-there lavender at #e9e6ed and the near-white #fcfbfe — and the contrast is not accidental. Todd Merrill Studio occupies the precise overlap between antique dealing and contemporary collecting: museum-quality mid-century American furniture, rare decorative arts, and new work from living designers, all presented in the flat, unembellished language of an institutional catalog. The digital environment inherits that register. Open Sans carries all text from display to caption, generally at weights that lean light rather than assertive — a 300-weight headline beneath a full-bleed object photograph trusts the photograph; the type is there to identify, not to persuade. Myriad Pro appears at display scale for exhibition titles and section headers, another sans-serif but with slightly more warmth in its proportions, a nod to the print catalogs the gallery has produced for decades. Letter-spacing opens wide on uppercase labels (0.08em on captions, 0.1em on section headers) so the institutional-signage convention reads through even at small sizes. The violet surfaces selectively on primary calls-to-action, focus rings on form fields, and the thin active underline in the nav. Nowhere does it appear as decoration or fill. Its supporting tints — lavender #e9e6ed used for category badges, faint #fcfbfe for metadata areas — carry the violet hue at a remove so the palette reads coordinated rather than accidental. A secondary crimson at #b81c23 flags condition notes and sold indicators, the same signal color museum conservators use for caution labels, immediately understood without explanation. All radii default to zero: contemporary art galleries do not round their corners. Frames are rectangular, pedestals are square, grid lines are strict. Buttons, inputs, dropdowns, and cards sit at `{rounded.none}` throughout. Spacing is generous and consistent; object images breathe inside wide margins, inquiry forms are set in low-contrast neutral panels so they do not compete with the merchandise. The overall architecture is a very precise neutral field interrupted at exactly one point by a decision in violet.

colors:
  primary: "#720eec"
  primary-active: "#5c0bc0"
  primary-disabled: "#cfc8d8"
  primary-surface: "#fcfbfe"
  ink: "#222222"
  dark: "#252525"
  body: "#444444"
  body-mid: "#515151"
  muted: "#888888"
  muted-soft: "#949494"
  hairline: "#e4e4e4"
  hairline-soft: "#eeeeee"
  border-strong: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#f5f5f5"
  surface-lavender: "#e9e6ed"
  on-primary: "#ffffff"
  link: "#0088cc"
  link-active: "#0077b3"
  alert-red: "#b81c23"
  alert-red-surface: "#f8b9b7"

typography:
  display-xl:
    fontFamily: "'Myriad Pro', 'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.02em
  display-md:
    fontFamily: "'Myriad Pro', 'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-lg:
    fontFamily: "'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.01em
  object-title:
    fontFamily: "'Myriad Pro', 'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 300
    lineHeight: 1.35
    letterSpacing: 0.01em
  body-md:
    fontFamily: "'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  caption-label:
    fontFamily: "'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  provenance-text:
    fontFamily: "Consolas, 'Courier New', Menlo, Monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.04em
  section-header:
    fontFamily: "'Open Sans', Helvetica, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
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
    padding: 12px 28px
    height: 44px
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
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 11px 27px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 40px
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    itemPadding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/5"
    titleTypography: "{typography.object-title}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    padding: "{spacing.sm} 0"
    gap: "{spacing.xs}"
    hoverImageScale: 1.02
    hoverTransition: "200ms ease"
  object-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    provenanceTypography: "{typography.provenance-text}"
    provenanceColor: "{colors.muted}"
    sectionDivider: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  inquiry-form:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    labelTypography: "{typography.caption-label}"
    labelColor: "{colors.muted}"
    inputStyle: "text-input"
    submitButton: "button-primary"
  hero-banner:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.title-lg}"
    minHeight: 480px
    overlayOpacity: 0.35
    textAlign: left
    padding: "{spacing.xxl} {spacing.section}"
  gallery-grid:
    columns: 3
    gap: "{spacing.lg}"
    columnsTablet: 2
    columnsMobile: 1
    itemComponent: "product-card"
  section-divider-header:
    typography: "{typography.section-header}"
    color: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.base}"
    marginBottom: "{spacing.xl}"
  category-badge:
    backgroundColor: "{colors.surface-lavender}"
    textColor: "{colors.primary}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  alert-badge:
    backgroundColor: "{colors.alert-red-surface}"
    textColor: "{colors.alert-red}"
    typography: "{typography.caption-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    height: 42px
    padding: "0 {spacing.base}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption-label}"
    headingColor: "{colors.canvas}"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — Flat violet (#720eec) fill with zero border-radius, all-caps spaced Open Sans at 14px/600 weight, 44px tall. The active state darkens to #5c0bc0; disabled desaturates to the lavender-gray `{colors.primary-disabled}`, reading as neutralized rather than grayed out. No shadow, no elevation — the gallery context treats drop-shadows as noise from a different design tradition.

**`button-secondary`** — White canvas with a 1px ink border, identical metrics to the primary. Used for secondary actions such as "View All" or filter resets; on hover the background shifts to `{colors.surface-soft}` without the border changing.

**`button-ghost`** — Transparent fill, 1px violet border, violet text, smaller at 12px/600. Appears inline in product cards or alongside body copy for soft CTAs: "Request Condition Report," "Download Catalog PDF." Its restraint keeps it from competing with primary buttons on the same page.

### Text Input & Forms
**`text-input`** — Zero border-radius, 42px height, 1px `{colors.hairline}` border that upgrades to 1px `{colors.primary}` violet on focus. Placeholder text in `{colors.muted}`. The flat, minimal styling ensures form fields recede visually behind gallery photography.

**`inquiry-form`** — Full inquiry panels sit in a `{colors.surface-soft}` (#f9f9f9) container with 1px hairline border and generous `{spacing.xl}` padding. Labels use `{typography.caption-label}` — uppercase, letter-spaced, muted gray — creating a documentation aesthetic closer to institutional records than retail checkout. The submit button is `button-primary` at full container width.

### Navigation
**`nav-bar`** — 64px white bar with 1px bottom hairline. Logo anchored left; nav links in Open Sans 13px/400 with 0.04em letter-spacing sit right or center. State change on hover is color-only — muted to ink — with no underline animation. Active section receives a 2px violet underline flush to the bottom of the bar.

**`nav-dropdown`** — Opens directly below the triggering link with no border-radius, 1px `{colors.hairline}` border, white background. Items at `{typography.nav-link}` with 8px vertical padding per row. No chevron, no slide animation — the menu appears and disappears at zero transition time.

### Product / Object Card
**`product-card`** — Portrait-ratio image at 4:5 with zero radius. On hover, the image scales to 1.02 with a 200ms ease transition; no overlay or scrim appears. Below the image: object title in `{typography.object-title}` (Myriad Pro 18px/300), then medium and approximate date in `{typography.caption}` muted gray, then maker or designer attribution. No price is displayed — inquiries are the conversion event. Cards have no border and no shadow; objects float on white canvas separated only by the grid gap.

**`object-detail-panel`** — Full-width detail layout on object pages. Title in `{typography.display-md}` (Myriad Pro 24px/300), body description in Open Sans 15px/400 at 1.6 line-height. Provenance, exhibition history, and condition notes render in `{typography.provenance-text}` — Consolas monospace at 12px — each section separated by a 1px hairline rule, echoing the catalog-entry format of the printed reference books the studio publishes.

### Hero
**`hero-banner`** — Near-black (#252525) background or a full-bleed photograph with a 0.35-opacity dark scrim. Title in `{typography.display-xl}` (Myriad Pro 36px/300) white, subtitle in `{typography.title-lg}` Open Sans white. Text is left-aligned with `{spacing.section}` horizontal padding and `{spacing.xxl}` vertical padding. Minimum 480px height. On mobile, the title drops to `{typography.display-md}` scale and height reduces to 300px.

### Gallery Grid
**`gallery-grid`** — Three columns on desktop with a `{spacing.lg}` (24px) gap and no visible grid lines. Each cell is a `product-card`. The tight gap without borders produces a mosaic that reads like a printed auction catalog page. No masonry offset — strict rows maintain the institutional grid logic.

### Section Divider Header
**`section-divider-header`** — Uppercase, letter-spaced 0.1em text at `{typography.section-header}` (Open Sans 13px/600). A 1px `{colors.hairline}` rule separates the header from the content below; `{spacing.xl}` margin-bottom provides breathing room before the first grid row. Used consistently for "Featured Works," "Artists," "In the Press," "Categories."

### Badges
**`category-badge`** — Lavender surface (#e9e6ed) with violet text at `{typography.caption-label}` uppercase. Zero radius. Tags object categories such as "Furniture," "Lighting," "Ceramics." The lavender tint reads as the violet brand color de-intensified, keeping badges visually coherent with primary actions.

**`alert-badge`** — Pale pink surface (#f8b9b7) with crimson (#b81c23) text at `{typography.caption-label}` uppercase. Zero radius. Flags condition annotations, sold status, reserved pieces, or editorial callouts. The red stands apart from the violet brand language, signaling a different register — caution or status rather than navigation.

### Search
**`search-bar`** — Same flat-border, zero-radius aesthetic as `text-input`. Appears in the nav bar or as a full-width element above gallery grids. Violet 1px outline on focus. No pill shape, no submit button — search executes on enter or after a debounce interval.

### Footer
**`footer`** — Near-black (#252525) background with `{typography.body-sm}` white body text and #949494 muted links that lighten to white on hover. Column headings in `{typography.caption-label}` white. Four to five columns on desktop: Gallery, Artists, Press, Contact, Newsletter. No top border — the dark band provides sufficient contrast against the white canvas above. Bottom row holds copyright in `{typography.caption}` at `{colors.muted-soft}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Gallery grid collapses to 1 column; hero title drops to `display-md`, min-height 300px; nav collapses to hamburger; inquiry form and search bar go full-width; section padding reduces to `spacing.xl` |
| Tablet | 744–1128px | Gallery grid becomes 2 columns; nav may condense to fewer primary links or hamburger; hero padding at `spacing.xl`; object detail panel stacks image above text |
| Desktop | 1128–1440px | 3-column gallery grid; full horizontal nav; hero at full `display-xl`; object-detail panel is 2-column (image left, detail right) |
| Wide | > 1440px | Max content width ~1320px centered; gallery grid holds at 3 columns; hero image expands via object-fit cover |

### Touch Targets
- Nav links: minimum 44px touch height via vertical padding expansion
- Buttons are 44px tall — no adjustment needed for touch
- Product cards: full image width is the tap target, no discrete button required
- Text inputs at 42px: add 2px padding on mobile to reach the 44px minimum
- Footer links: minimum 40px row height, add 2px on mobile if needed

### Collapsing Strategy
- Navigation: full horizontal → hamburger drawer at < 744px; drawer slides from right over a dark (#252525) overlay
- Gallery grid: 3 → 2 → 1 column at tablet and mobile breakpoints; gap reduces to `spacing.md` on mobile
- Object-detail panel: 2-column (image + text) → stacked single column below 744px, image first at full viewport width
- Inquiry form: contained panel on desktop → full-width card with reduced horizontal padding on mobile
- Footer: 5 columns → 2 columns at tablet → single stacked column at mobile; column headings become disclosure toggles on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font detected; Myriad Pro is extracted from font stacks but may be served via a licensed font service not captured in extraction — verify live `@font-face` declarations before shipping display type
- All radii defaulted to zero based on gallery/institutional convention and the absence of radius values in extraction; confirm against live computed styles
- Primary brand color assigned as #720eec (most distinctive extracted color, supported by lavender tint surfaces #e9e6ed and #fcfbfe); the large blue cluster (#0088cc, #0077b3, #149bdf, #0480be, #0044cc, #003388, #003399) likely reflects link and social-widget defaults rather than brand identity — verify the distinction in the live stylesheet
- No pricing, cart, or checkout UI observed; the site appears to operate on an inquiry-only model — no e-commerce token definitions included
- Logo dimensions, lockup type (wordmark vs. monogram), and clear-space rules not derivable from color/font extraction
- Animation timing curves, hover transition durations, and scroll behavior not captured
- Dark mode not detected; the site appears light-only
- No breakpoint values confirmed from extraction; widths in Responsive Behavior table are inferred from common gallery-site conventions
