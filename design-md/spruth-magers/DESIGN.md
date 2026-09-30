---
version: alpha
name: "Sprüth Magers"
source_url: "https://spruethmagers.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  #ff1900 — a red so saturated it tips from gallery signage into emergency transmission — is the single chromatic decision Sprüth Magers makes with conviction; everything else concedes to a white ground and NeueHaasGroteskText Pro rendered at a restraint that most digital interfaces would misread as underdesign. The typeface choice is the tell: not a custom logotype face, not a geometric display sans, but Linotype's systematic revival of the Haas Grotesk drawings that preceded Helvetica — Swiss-institutional correctness that places the gallery in the lineage of Basel and Zurich design offices rather than art-fair booth graphics. Navigation accumulates artist names in tight roman at 12–13px; the sheer volume of names is the flex, not the type scale. Headings rarely exceed 20px. Hierarchy operates through weight differential and column positioning rather than size jumps — a modernist confidence that the roster (Barbara Kruger, Rosemarie Trockel, Andreas Gursky, Ed Ruscha) requires no amplification.

  The color logic is nearly binary: #ff1900 against #ffffff, with #003388 appearing as a structural secondary for links and interactive states. The neutral scaffolding — #4f5b5f for body copy, #707070 for metadata, #bdc3c7 for hairlines — keeps infrastructure invisible against gallery-scale photography. The {rounded.none} discipline is total: no border-radius anywhere. Every container, every button, every image frame is a hard rectangle, aligning the digital surface with the flat, gridded architecture of the gallery's printed materials and institutional announcements.

  Spacing follows an editorial-magazine cadence: dense internal padding (8–12px) within navigation elements, generous section breathing room at 48–64px, full-bleed image modules that press to the viewport edge. The footer condenses into a compact, information-rich block — three office locations set at 11px — functioning less as a digital footer and more as an institutional letterhead colophon. Press entries, exhibition PDFs, and artist CVs share the same weight and size as body text, deliberately blurring the boundary between live site and permanent archive. Nothing on the surface invites lingering; the design assumes the visitor already knows why they are there.

colors:
  primary: "#ff1900"
  primary-active: "#cc1400"
  primary-disabled: "#ff8e80"
  secondary: "#003388"
  secondary-active: "#002266"
  ink: "#32373c"
  body: "#4f5b5f"
  muted: "#707070"
  hairline: "#bdc3c7"
  hairline-soft: "#c7c7cd"
  canvas: "#ffffff"
  surface-soft: "#eaedf2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'NeueHaasGroteskText Pro', 'Neue Haas Grotesk', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.4px
  display-md:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-item:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  nav-label:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  press-entry:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  credit:
    fontFamily: "'NeueHaasGroteskText Pro', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 10px
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
    rounded: "{rounded.none}"
    padding: 8px 16px
    height: 34px
    border: none
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
    border: "1px solid {colors.ink}"
    padding: 7px 15px
    height: 34px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-item}"
    height: 48px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
    sectionLabelTypography: "{typography.nav-label}"
    sectionLabelColor: "{colors.muted}"
  nav-item-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-item}"
  artist-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-sm}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    imageFit: cover
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  exhibition-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.body-sm}"
    metaColor: "{colors.body}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    rounded: "{rounded.none}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    imageFit: cover
    captionTypography: "{typography.credit}"
    captionColor: "{colors.muted}"
    padding: "0"
    titlePlacement: below-image
  press-entry:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.press-entry}"
    linkColor: "{colors.secondary}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.sm} 0"
  image-caption:
    textColor: "{colors.muted}"
    typography: "{typography.credit}"
    padding: "{spacing.xs} 0"
  exhibition-filter-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-label}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} 0"
    gap: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
    focusBorder: "1px solid {colors.ink}"
  section-divider:
    borderTop: "1px solid {colors.hairline}"
    margin: "{spacing.xxl} 0"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
    locationTypography: "{typography.caption}"
    locationLabelTypography: "{typography.nav-label}"
    locationLabelColor: "{colors.muted}"
  social-link:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    textDecoration: none
    hoverTextColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — A sharp-edged rectangle (`{rounded.none}`) filled with `{colors.primary}` (#ff1900) and `{colors.on-primary}` white text set at `{typography.button-md}` (13px, weight 400). On hover the background snaps immediately to `{colors.primary-active}` (#cc1400) — no easing, no lift, consistent with the gallery's refusal of decorative transitions. The disabled state fades to `{colors.primary-disabled}` (#ff8e80). There are no drop shadows, gradients, or icon embellishments anywhere in the button system.

**`button-secondary`** — An outlined variant with a 1px `{colors.ink}` border and transparent fill; hover inverts fill to solid ink with `{colors.canvas}` text. Used for PDF downloads, exhibition text links, and secondary navigation actions. Hard corners only, same 34px height as primary.

**`button-text-link`** — Inline `{colors.primary}` text with underline, no background, no padding block. The primary mechanism for navigating body copy, press entries, and artist cross-references throughout editorial sections.

### Navigation
**`nav-bar`** — A 48px-tall horizontal bar on `{colors.canvas}` with a single 1px `{colors.hairline}` bottom border. The logotype renders in `{colors.primary}` red at left; section headings (ARTISTS, EXHIBITIONS, NEWS, ABOUT) in `{typography.nav-label}` (11px/uppercase) at `{colors.muted}` — subordinate identifiers rather than navigation anchors in their own right. Active and hovered nav items shift to `{colors.primary}` with no underline or background shift. On wide viewports an artist-name submenu can unfurl beneath the Artists section, making the navigation bar the densest information plane on the site.

**`nav-item-active`** — Active state is purely a color shift to `{colors.primary}` with identical `{typography.nav-item}` weight; no decorative underline or indicator bar. The red is sufficient signal.

### Cards
**`artist-card`** — Zero-radius image frame, artist name in `{typography.title-sm}` (13px/500 weight), nationality or birth year in `{typography.caption}` at `{colors.muted}`. No card surface, no shadow, no hover lift — images are the currency, and the grid relies on negative space rather than framing. Gap between image and name text is `{spacing.sm}`.

**`exhibition-card`** — Exhibition title at `{typography.title-md}` (14px/500), venue name and date range at `{typography.body-sm}` in `{colors.body}`, short description at `{typography.body-sm}` in `{colors.muted}`. In stacked list views each card is separated by a 1px `{colors.hairline}` top rule flush to the left edge of the text column — no card box, no colored background. Full flat white.

### Hero
**`hero`** — Full-bleed image with zero padding, no overlay scrim, no gradient. When a title is present it appears as a `{typography.display-xl}` line below the image frame rather than composited over the photograph — an editorial-magazine convention that protects the image's integrity. `{image-caption}` appears at `{typography.credit}` (10px/400) in `{colors.muted}`, flush left, with `{spacing.xs}` top gap from the image edge.

### Press & Archive
**`press-entry`** — Each press listing is a hairline-topped row at zero background: publication title or headline in `{typography.press-entry}` (13px/400 weight) in `{colors.body}`, date and external link in `{colors.secondary}` (#003388). No cards, no thumbnails — the listings accumulate as a ledger or annotated bibliography. The visual register is closer to a gallery's printed press kit than a content feed.

### Filter Tabs
**`exhibition-filter-tab`** — A horizontal inline row for filtering exhibitions by status (Past / Current / Upcoming). Inactive labels use `{typography.nav-label}` in `{colors.muted}`; the active tab carries only a 2px bottom border in `{colors.primary}` with no background fill, no pill, no box. Tabs sit flush to the section grid with `{spacing.lg}` horizontal gap between items.

### Footer
**`footer`** — White ground, 1px `{colors.hairline}` top border, internal padding `{spacing.xl}` vertical. The three office locations (Berlin, London, Los Angeles) each appear as a `{typography.nav-label}` city slug in `{colors.muted}` followed by the street address in `{typography.caption}` (11px/400). Social links sit inline at the same caption scale, turning `{colors.primary}` on hover with no underline. The overall block reads as an institutional letterhead colophon — dense, factual, zero decorative embellishment.

### Search
**`search-bar`** — Full-width rectangular input, 1px `{colors.hairline}` border that sharpens to `{colors.ink}` on focus. No internal icon; the label "SEARCH" precedes the field as a `{typography.nav-label}` run-in label outside the input boundary. Placeholder text in `{colors.muted}` at `{typography.body-md}`.

### Section Divider
**`section-divider`** — A single 1px `{colors.hairline}` horizontal rule with `{spacing.xxl}` margin above and below. The visual grammar for separating content modules — no colored bands, no padded backgrounds, no decorative spacing objects.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; artist and exhibition grids reduce to single column; hero image is 100vw cropped to 3:4 portrait; footer location blocks stack vertically one per row |
| Tablet | 744–1128px | Two-column grids for artists and exhibitions; nav shows primary section labels only, artist submenu behind a tap; press entries remain single-column |
| Desktop | 1128–1440px | Three- or four-column exhibition and artist grids; full horizontal nav with submenu capability; press entries shift to two-column layout |
| Wide | > 1440px | Content area max-width capped at approximately 1320px; side margins grow symmetrically; hero images remain full-bleed behind the gutter constraint |

### Touch Targets
- All nav items receive minimum 44px tap height on mobile via vertical padding despite 13px type
- Artist card images are fully tappable — no separate call-to-action element required
- Filter tab rows expand to full-width swipeable horizontal scroll on mobile
- Footer location links maintain minimum 44px tap area through line-height expansion

### Collapsing Strategy
- Primary nav (Artists, Exhibitions, News, About) persists as labeled items in a scrollable horizontal strip on tablet; artist submenu only on desktop
- Exhibition filter tabs collapse to a native `<select>` element on viewports below 480px
- Press entry two-column grid collapses to single column below 744px
- Footer columns (Berlin / London / Los Angeles) stack to one-per-row on mobile; address text truncates to city and country line only

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Many extracted hex values (#428bca, #5bc0de, #5cb85c, #f0ad4e, #d9534f, #7dd667, #2980b9, #357935, etc.) match Bootstrap 3 and WordPress Gutenberg editor palette defaults exactly — these are almost certainly CMS framework artifacts, not brand tokens; the meaningful palette is likely just #ff1900, #003388, near-black, and neutral greys
- Whether #003388 is a deliberate brand secondary or a CMS default link color is ambiguous from extraction alone
- Exact display heading sizes for exhibition and artist pages could not be confirmed; values estimated from Swiss/International modernist gallery norms
- Hover transition timing and easing functions not available from static extraction
- Precise grid column counts, gutter widths, and column-gap values not measured
- Logo SVG dimensions and exact logotype typesetting (tracking, capitalization, weight) not extracted
- Dark-mode or inverse-color alternate theme not confirmed
- Whether NeueHaasGroteskText Pro is served as a web font or system-fallback could not be confirmed from extraction; Arial/Helvetica may be the operative rendering on most devices
