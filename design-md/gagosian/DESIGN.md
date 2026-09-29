---
version: alpha
name: "Gagosian"
source_url: "https://gagosian.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  GagosianHeadline — the gallery's proprietary display serif — carries a stroke contrast so acute it reads simultaneously as a declaration about power and restraint. Where most institutional websites default to neutral grotesques across every surface, Gagosian commissions type that could hang adjacent to a Koons or a Serra without embarrassment. The palette enforces that same discipline: #111111 is the primary ground for every headline, navigation rail, and CTA, while the surrounding color field is constructed from seventeen graduated grays and near-whites — #b2b2b2 down to #fafafa — functioning as invisible infrastructure so no interface chrome competes with seven-figure reproductions. Two outlier colors do specific editorial work: #574a32, a warm tobacco brown, surfaces in archival and print-adjacent contexts where the gallery's long institutional history needs to breathe against pure digital white; #39549d, a deep slate blue, handles linked states and secondary interactive layers without borrowing from the generic hyperlink blue (#2563eb) that appears in raw body copy. GTAmerica handles all body and UI work at weights 400–600 — its geometric neutrality a deliberate foil to the headline's drama. Spacing is monumental: section rhythm begins at 64px and exhibition grids breathe at 48px column gutters, because Gagosian's physical architecture (Britannia Street, Grosvenor Hill, West 24th Street) is defined by vast negative space, and the digital system evokes that register. Rounded corners are effectively absent — `{rounded.none}` or at most `{rounded.xs}` on form fields — because a softened corner reads as a commercial concession on a brand that prices work in the millions. Modal overlays use a near-black #161a1c scrim at high opacity rather than the blue-tinted darks common to consumer platforms. The gallery publishes Gagosian Quarterly, a print-quality editorial product, and the digital design imports that DNA directly: wide text measures, small-caps artist-credit lines in `{typography.caption-sc}`, and a footer built like a magazine masthead rather than a link directory.

colors:
  primary: "#111111"
  primary-active: "#000000"
  primary-disabled: "#888888"
  ink: "#111111"
  body: "#444444"
  muted: "#838383"
  muted-soft: "#b2b2b2"
  hairline: "#d5dee2"
  hairline-mid: "#909090"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#fafafa"
  surface-panel: "#f0f4f7"
  on-primary: "#ffffff"
  accent-warm: "#574a32"
  accent-slate: "#39549d"
  link: "#2563eb"
  scrim: "#161a1c"
  dark-canvas: "#1e2428"
  mid-dark: "#242c31"
  mid-text: "#5e6266"

typography:
  display-xl:
    fontFamily: "'GagosianHeadline', Georgia, 'Times New Roman', serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'GagosianHeadline', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.75px
  display-md:
    fontFamily: "'GagosianHeadline', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'GagosianHeadline', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  editorial-pull:
    fontFamily: "'GagosianHeadline', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.5px
  title-md:
    fontFamily: "'GTAmerica', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'GTAmerica', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'GTAmerica', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GTAmerica', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'GTAmerica', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sc:
    fontFamily: "'GTAmerica', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'GTAmerica', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "'GTAmerica', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'GTAmerica', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.04em
    textTransform: uppercase
  mono:
    fontFamily: "Consolas, 'Courier New', Liberation Mono, Menlo, Monaco, monospace"
    fontSize: 13px
    fontWeight: 400
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
    padding: 14px 32px
    height: 48px
    border: none
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-mid}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-mid}"
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  mobile-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderTop: "1px solid {colors.hairline}"
    rowHeight: 48px
  exhibition-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/5"
    titleTypography: "{typography.display-sm}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.caption-sc}"
    metaColor: "{colors.muted}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    rounded: "{rounded.none}"
    gap: "{spacing.lg}"
  artist-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "1/1"
    nameTypography: "{typography.title-md}"
    nameColor: "{colors.ink}"
    creditTypography: "{typography.caption-sc}"
    creditColor: "{colors.muted}"
    rounded: "{rounded.none}"
    hoverUnderlineColor: "{colors.primary}"
  artwork-figure:
    backgroundColor: "{colors.surface-soft}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    creditTypography: "{typography.caption-sc}"
    creditColor: "{colors.mid-text}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
  hero-editorial:
    backgroundColor: "{colors.dark-canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.on-primary}"
    subheadTypography: "{typography.display-md}"
    subheadColor: "{colors.on-primary}"
    metaTypography: "{typography.caption-sc}"
    metaColor: "{colors.muted-soft}"
    overlay: "linear-gradient(to top, {colors.scrim} 0%, transparent 60%)"
    rounded: "{rounded.none}"
    textPosition: bottom-left
  search-bar:
    backgroundColor: "{colors.surface-panel}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: none
    placeholderColor: "{colors.muted}"
    iconColor: "{colors.muted}"
    height: 44px
    padding: "12px {spacing.base}"
  section-divider:
    borderTop: "1px solid {colors.hairline}"
    marginY: "{spacing.section}"
    labelTypography: "{typography.caption-sc}"
    labelColor: "{colors.muted}"
  editorial-pull-quote:
    typography: "{typography.editorial-pull}"
    textColor: "{colors.ink}"
    borderLeft: "3px solid {colors.accent-warm}"
    paddingLeft: "{spacing.xl}"
    marginY: "{spacing.xxl}"
  press-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sc}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "4px {spacing.sm}"
  fair-listing-row:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.caption-sc}"
    metaColor: "{colors.muted}"
    activeAccentColor: "{colors.accent-slate}"
    padding: "{spacing.lg} 0"
  inquiry-form:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline-mid}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl}"
    headlineTypography: "{typography.title-md}"
    headlineColor: "{colors.ink}"
    labelTypography: "{typography.caption-sc}"
    labelColor: "{colors.muted}"
    inputBackgroundColor: "{colors.canvas}"
    inputBorder: "1px solid {colors.hairline-mid}"
    inputFocusBorder: "1px solid {colors.primary}"
    inputTypography: "{typography.body-md}"
    submitBackgroundColor: "{colors.primary}"
    submitTextColor: "{colors.on-primary}"
    submitTypography: "{typography.button-md}"
    submitRounded: "{rounded.none}"
  modal-overlay:
    scrimColor: "{colors.scrim}"
    scrimOpacity: 0.92
    contentBackground: "{colors.canvas}"
    rounded: "{rounded.none}"
    closeIconColor: "{colors.on-primary}"
  footer-masthead:
    backgroundColor: "{colors.mid-dark}"
    textColor: "{colors.muted-soft}"
    linkColor: "{colors.canvas}"
    linkHoverColor: "{colors.on-primary}"
    bodyTypography: "{typography.body-sm}"
    sectionLabelTypography: "{typography.caption-sc}"
    sectionLabelColor: "{colors.muted}"
    legalTypography: "{typography.caption}"
    legalColor: "{colors.mid-text}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — A stark #111111 block, 48px tall, zero border-radius, uppercase GTAmerica at 14px/500 weight with 0.06em tracking. The letter-spacing and uppercase treatment shift these controls from consumer CTAs into editorial directives; on hover the background moves to #000000 (`{colors.primary-active}`). Disabled state uses #888888 with no spinner or animation — the gallery assumes users read context rather than relying on loading affordances. Width is auto by default; specific surfaces (inquiry form footer) stretch it full-column.

**`button-secondary`** — White fill with a 1px #111111 border and the same uppercase typographic treatment as the primary. Used for secondary exhibition actions ("View All Works", "Read Essay") where the gallery needs a visible but deferential control that doesn't interrupt image-dominant layouts. The border is the entire visual weight — no shadow, no fill change on hover beyond a subtle `{colors.surface-soft}` tint.

**`button-ghost`** — Transparent background, 1px `{colors.hairline-mid}` border, 12px uppercase text. Appears in filter toolbars and inline editorial controls where the control must be structurally present but visually near-invisible against the white canvas.

### Navigation
**`nav-bar`** — 64px tall, white background with a 1px `{colors.hairline}` bottom border. The GAGOSIAN wordmark renders in `{typography.display-sm}` via GagosianHeadline — set text, not an image file — which gives the nav immediate typographic authority without a separate logo asset. Links are uppercase GTAmerica at 13px/0.04em tracking. On desktop the full link set is horizontal; on mobile a single text label ("Menu") replaces all links, toggling a `{mobile-menu}` overlay.

**`mobile-menu`** — Full-viewport slide-in from the right, white background, links stacked at 48px row height in `{typography.nav-link}` styling. Transition is a linear 200ms translate with no easing decoration.

### Cards
**`exhibition-card`** — Full-bleed photography at 4:5 aspect ratio with zero border-radius. Below the image: artist name in `{typography.display-sm}` (GagosianHeadline), exhibition title in `{typography.body-sm}` (GTAmerica, often italic), gallery location and date in `{typography.caption-sc}` at `{colors.muted}`. Cards sit flush to the grid edge with no shadow, border, or card-level hover transform — the image itself carries all the visual weight.

**`artist-card`** — Square 1:1 portrait against a white ground, artist name in `{typography.title-md}`, birth year and nationality in `{typography.caption-sc}`. Used in the alphabetical artist index. Hover state underlines the name in `{colors.primary}` — no elevation, no transform.

**`artwork-figure`** — Museum-standard figure block: image at natural aspect ratio with `{colors.surface-soft}` background padding, title and medium in `{typography.caption}` below, credit line ("© Estate of...") in `{typography.caption-sc}` at `{colors.mid-text}`. Used in press, publication, and article contexts.

### Hero
**`hero-editorial`** — Full-viewport image with a `linear-gradient(to top, {colors.scrim} 0%, transparent 60%)` overlay. Headline in `{typography.display-xl}` (GagosianHeadline, white) anchored bottom-left; exhibition meta in `{typography.caption-sc}` sits one line above the headline. A single static frame per hero — no carousel, no slide indicators, no autoplay — consistent with the gallery's refusal of spectacle at the interface level.

### Editorial
**`editorial-pull-quote`** — `{typography.editorial-pull}` (GagosianHeadline 36px) with a 3px `{colors.accent-warm}` left border and 32px left padding. The tobacco-brown (#574a32) rule is the only warm color in an otherwise neutral typographic field, making pull quotes physically warm against the page grid without introducing a color system that competes with artwork reproduction.

**`section-divider`** — A 1px `{colors.hairline}` top rule with an optional uppercase `{typography.caption-sc}` label in `{colors.muted}`. Segments exhibition chronology, press index, and artist biography page sections. No decorative element, no gradient — the line alone is sufficient.

### Search
**`search-bar`** — 44px height, `{colors.surface-panel}` fill (light blue-gray #f0f4f7), no visible border, `{rounded.xs}` corner radius. The panel color lifts the search control off the white canvas without a hard border line; the blue-gray references the cooler end of the site's gray scale. Placeholder text in `{colors.muted}` GTAmerica body-md. No search-button orb — submission is keyboard-triggered (Enter) or via a minimal magnifier icon.

### Listings
**`fair-listing-row`** — Horizontal row with a 1px `{colors.hairline}` bottom border, no background fill. Left: fair or event title in `{typography.title-sm}`, location and booth in `{typography.caption-sc}`. Right: date range. The `{colors.accent-slate}` (#39549d) dot or inline label marks the current/active fair. Used on the Art Fairs index page to distinguish the present season from historical participation.

**`press-badge`** — Small inline label in `{typography.caption-sc}` on `{colors.surface-soft}` with a 1px `{colors.hairline}` border. No color variation by category — press type is conveyed by label text alone ("Interview", "Review", "Catalog"), not by badge color, preserving palette restraint.

### Forms
**`inquiry-form`** — The gallery's primary conversion surface for artwork inquiries and newsletter signup. White background, 1px `{colors.hairline-mid}` border, zero border-radius, 48px all-sides padding. Field labels in small-caps `{typography.caption-sc}` / `{colors.muted}` sit above each input. The submit button runs full-width in `{colors.primary}` at the form base. No inline validation decoration — errors appear as plain `{typography.caption}` text in `{colors.muted}` below the offending field.

### Footer
**`footer-masthead`** — Dark `{colors.mid-dark}` (#242c31) background topped by a 3px `{colors.primary}` rule — the masthead convention from print. Link columns use `{typography.body-sm}` in near-white (`{colors.canvas}`); column headings use `{typography.caption-sc}` / `{colors.muted}`. The bottom bar carries social links and legal text in `{typography.caption}` / `{colors.mid-text}`. The dark footer reads as a deliberate close of the white editorial page, not a standard web-footer afterthought.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column exhibition grid; nav collapses to wordmark + text "Menu" toggle; hero headline drops to `{typography.display-md}`; section padding reduces to `{spacing.xl}`; pull quotes collapse to inline |
| Tablet | 744–1128px | Two-column exhibition grid; nav shows primary links only (Exhibitions, Artists, Art Fairs); section padding at `{spacing.xxl}`; hero at `{typography.display-lg}` |
| Desktop | 1128–1440px | Three- or four-column exhibition grid; full horizontal nav; hero at full `{typography.display-xl}` scale; editorial measures capped at 720px |
| Wide | > 1440px | Grid max-width constrained to 1440px with auto side margins; type scale unchanged; body text column capped at 780px for readability; footer columns expand horizontal whitespace |

### Touch Targets
- All navigation links minimum 48px touch height on mobile
- Inquiry and newsletter form inputs minimum 48px height across all breakpoints
- Exhibition cards are full-column-width tap targets — no separate "View" button overlaid on the image on mobile
- Fair listing rows minimum 48px touch height
- Footer link rows minimum 44px height on mobile

### Collapsing Strategy
- Navigation: full horizontal link list → primary-section links only → wordmark plus single "Menu" text toggle
- Exhibition grid: 4-column → 3-column → 2-column → 1-column at mobile breakpoint
- Hero headline scale: `{typography.display-xl}` → `{typography.display-lg}` (tablet) → `{typography.display-md}` (mobile); always left-aligned, never centered
- Editorial pull quotes: hidden on mobile below 744px (text reflowed inline without the accent-warm border rule)
- Footer masthead: 4-column link grid → 2-column → single stacked column on mobile, with the 3px top rule preserved at all widths

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- GagosianHeadline is a proprietary typeface; weight variants, OpenType feature set (small-caps native vs. synthesized, oldstyle figures, ligatures), and exact stroke contrast metrics are not publicly documented
- GTAmerica weight and style variants served in the web build are unconfirmed — only the font-family name was extracted; numeric weights are inferred from common GTAmerica web licensing patterns (Regular 400, Medium 500, Bold 600)
- Exact nav height, grid breakpoint pixel values, and column gutter measurements were not extractable from static extraction; the 64px nav and three-tier breakpoints are informed estimates
- Hover transition durations and easing functions could not be confirmed — 200ms linear is assumed from the minimal visual character of the brand
- Dark-mode palette, if any, was not confirmed; the site appeared to serve a single light theme
- The precise component contexts for accent-warm (#574a32) and accent-slate (#39549d) are inferred from color-frequency analysis and editorial convention; exact component assignments would require deep session interaction with authenticated pages
- Gagosian Quarterly editorial layout (drop-cap rules, footnote typesetting, print-to-web image sizing) was not captured in the static extraction
