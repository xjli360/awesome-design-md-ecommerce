---
version: alpha
name: "Marian Goodman Gallery"
source_url: "https://www.mariangoodman.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Acid yellow (#ffff80) appears with the abruptness of a Post-it note on a museum wall — a single high-voltage accent in a system that otherwise runs entirely on near-black (#111111), white (#ffffff), and gallery gray. The signal red (#da291c, deepening to #c52f24 on press) is the gallery's primary interactive color, marking current exhibition status, active navigation states, and the handful of CTAs that move users from browsing to inquiry. Typography is where the real design argument lives: Apercu — a geometric grotesque with the cleanliness of constructed letterforms — handles all navigational, institutional, and administrative text, while EB Garamond carries the curatorial register; this is not a decorative pairing but a structural one that maps the distinction between logistics and argument defining how a serious gallery communicates — exhibition dates, city slugs, and press archive labels in Apercu, wall-text prose and artist biography excerpts in EB Garamond. The two fonts rarely share a line. Corner radii are absent — {rounded.none} prevails everywhere except a minimal 2px softening on input fields. Depth arrives not from elevation or shadow but from hairline rules at {colors.hairline} (#eaeaea) separating sections of the grid. Exhibition cards carry a full-bleed image, an artist name in Apercu medium, a title in EB Garamond italic, and a date range — no price, no rating star, no review count. The institutional blue (#175ea9) surfaces only in legacy link contexts; the yellow (#ffff80) reserves itself for three specific hover states across the site — search suggestion rows, footer links, and pagination arrows — each a flash of the unexpected in an otherwise monochrome interaction model. Mid-grays (#5d5d5d for secondary labels, #777777 for tertiary metadata) carry gallery locations and past exhibition bylines without competing with the artwork images that define every hero moment. The spatial system is generous: section breaks at {spacing.section} (64px), side margins wider than any comparable site of comparable traffic, and image-to-text ratios weighted heavily toward the image.

colors:
  primary: "#da291c"
  primary-active: "#c52f24"
  primary-disabled: "#eab5b2"
  ink: "#111111"
  body: "#3a3a3a"
  muted: "#5d5d5d"
  muted-soft: "#777777"
  hairline: "#eaeaea"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-yellow: "#ffff80"
  accent-blue: "#175ea9"
  scrim: "#111111"

typography:
  display-xl:
    fontFamily: "'EBGaramond', 'EB Garamond', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
    fontStyle: italic
  display-lg:
    fontFamily: "'EBGaramond', 'EB Garamond', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'EBGaramond', 'EB Garamond', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Apercu', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-md:
    fontFamily: "'Apercu', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.04em
  body-md:
    fontFamily: "'EBGaramond', 'EB Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Apercu', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Apercu', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  label-caps:
    fontFamily: "'Apercu', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Apercu', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Apercu', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.04em
  exhibition-title:
    fontFamily: "'EBGaramond', 'EB Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
    fontStyle: italic
  exhibition-byline:
    fontFamily: "'Apercu', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em

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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: none
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 10px 12px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.title-lg}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    linkHoverColor: "{colors.primary}"
    linkActiveColor: "{colors.primary}"
    position: sticky
  exhibition-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.exhibition-title}"
    bylineTypography: "{typography.exhibition-byline}"
    bylineColor: "{colors.ink}"
    dateTypography: "{typography.caption}"
    dateColor: "{colors.muted}"
    gap: "{spacing.sm}"
    padding: "{spacing.base} 0"
    rounded: "{rounded.none}"
    hoverImageScale: 1.02
    hoverImageTransition: 300ms ease-out
  artist-card:
    backgroundColor: transparent
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.caption}"
    subtitleColor: "{colors.muted}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} 0"
    borderBottom: "1px solid {colors.hairline}"
    hoverTitleColor: "{colors.primary}"
  hero-exhibition:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    imagePosition: cover
    titleTypography: "{typography.display-xl}"
    bylineTypography: "{typography.title-lg}"
    bylineColor: "{colors.canvas}"
    dateTypography: "{typography.label-caps}"
    dateColor: "{colors.canvas}"
    overlayGradient: "linear-gradient(to top, rgba(17,17,17,0.6) 0%, transparent 60%)"
    paddingBottom: "{spacing.section}"
    minHeight: 80vh
  current-exhibition-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  press-listing-item:
    backgroundColor: transparent
    titleTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
    linkHoverColor: "{colors.primary}"
  location-tag:
    textColor: "{colors.muted-soft}"
    typography: "{typography.label-caps}"
    backgroundColor: transparent
    padding: 0
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-md}"
    rounded: "{rounded.none}"
    inputBorderBottom: "1px solid {colors.ink}"
    suggestTypography: "{typography.body-sm}"
    suggestColor: "{colors.ink}"
    suggestHoverBackground: "{colors.accent-yellow}"
    overlayPadding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.canvas}"
    linkHoverColor: "{colors.accent-yellow}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.muted-soft}"
    padding: "{spacing.xxl} 0"
    columns: 4
  section-divider:
    borderTop: "1px solid {colors.hairline}"
    margin: "{spacing.section} 0"
  pagination-arrow:
    backgroundColor: transparent
    iconColor: "{colors.ink}"
    hoverBackground: "{colors.accent-yellow}"
    rounded: "{rounded.none}"
    height: 40px
    width: 40px
    transition: background 150ms ease

## Components

### Buttons

**`button-primary`** — A flat rectangular red button (#da291c) with zero border radius and uppercase Apercu at 13px with 0.08em letter-spacing. The fill darkens to #c52f24 on active press; the disabled state washes to pale rose (#eab5b2) with unchanged text and `cursor: not-allowed`. This button appears primarily in inquiry submission and mailing list contexts — not e-commerce.

**`button-secondary`** — Ink border on a transparent field, uppercase Apercu tracking matching the primary. On hover the entire button inverts: ink fill, white text, no intermediate state. Used for archive filters, exhibition wayfinding CTAs, and modal dismiss actions.

**`button-ghost`** — Textless container; a red uppercase Apercu inline link. Deployed in "Read more" chains within EB Garamond prose, where the uppercase weight creates visual separation from the surrounding text body without adding a box element.

### Navigation

**`nav-bar`** — A 60px sticky white bar with a 1px hairline at the base. Gallery name in `title-lg` Apercu at left; primary links (Artists, Exhibitions, Art Fairs, Publications, Press, About) in `nav-link` at right. Hover shifts link color to red (#da291c). No dropdown mega-menu: secondary navigation surfaces as a secondary horizontal row on interior pages, styled identically but sitting below the primary bar. Collapses to a hamburger icon at mobile breakpoint.

### Cards

**`exhibition-card`** — Full-bleed image at 4:3 aspect ratio; below it, artist name in `exhibition-byline` (Apercu 14px/500), exhibition title in `exhibition-title` (EB Garamond 22px italic), and date range in `caption`. No shadow, no border, no card surface color. The only motion on the page: image scales to 102% on hover over 300ms ease-out. Grid columns and gutters are managed by the parent container.

**`artist-card`** — Used in alphabetical listing views: a hairline-bottomed row with artist name in `title-md` and a nationality or birth-year annotation in `caption`. On hover the name shifts to red. No thumbnail in list view — photography appears only in artist detail hero contexts.

### Hero

**`hero-exhibition`** — Full-viewport-width image with a gradient scrim (black at bottom, transparent at 60% height). Exhibition title in `display-xl` (EB Garamond 48px italic) renders above the gradient; artist byline in `title-lg` and a `label-caps` date string sit above the title. No CTA button appears in the primary hero — the entire image acts as the link to the exhibition page. Minimum height is 80vh.

### Functional UI

**`text-input`** — Hairline border at {colors.hairline}, 2px radius ({rounded.xs}), `body-sm` Apercu placeholder in {colors.muted-soft}. Focus brings the border to full ink black (#111111). Used in press inquiry and mailing list forms.

**`search-overlay`** — A full-screen white panel overlaying the nav. A single `display-md` EB Garamond input spans the full width with an ink-black bottom border — no box, no filled background. Suggestions list below in `body-sm` Apercu; each suggestion row fills with #ffff80 (`accent-yellow`) on hover, the most legible deployment of that color in the system.

**`press-listing-item`** — A hairline-separated row: publication or article title in `body-md` EB Garamond, publication name and date in `caption` Apercu at {colors.muted}, no box. Link hover brings the title to red. Used across the press archive with identical styling at all breakpoints.

**`current-exhibition-badge`** — Flat red label chip, no radius, uppercase 11px Apercu in white. Applied to exhibition listing items marked as currently open. No icon, no dot prefix — the red fill is the sole signal.

**`footer`** — Near-black (#111111) fill with four columns across desktop: gallery locations (New York, Paris, London) in `label-caps` with addresses in `body-sm`; navigation links in `body-sm`; newsletter signup with a `text-input` and `button-primary`; legal credits in `caption` at the bottom edge. Link hover color is #ffff80 — one of two reliably confirmed deployments of the yellow accent. Collapses to a single stacked column at mobile.

**`pagination-arrow`** — Square 40×40 transparent buttons with ink SVG arrows for exhibition archive and press list pagination. Background fills with #ffff80 on hover at 150ms ease — the interaction mirrors the search suggestion hover and footer link hover, establishing the yellow as a consistent hover-state signal across the three lowest-frequency interactions in the system.

**`section-divider`** — A 1px hairline rule at {colors.hairline} with {spacing.section} (64px) vertical margin. No decorative element; used to separate thematic grid sections on listing pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column exhibition grid; nav collapses to hamburger with ink-fill slide-in drawer; hero text scales to `display-md`; footer stacks to single column; artist list maintains flat scroll |
| Tablet | 744–1128px | Two-column exhibition grid; nav remains horizontal but tertiary items drop to sub-row; press listing reduces side padding |
| Desktop | 1128–1440px | Three-column exhibition grid; full nav visible; hero at full viewport height (80vh minimum); footer four-column layout |
| Wide | > 1440px | Content constrained to 1440px max-width with increased side margins; typography scale unchanged; hero image crops from center |

### Touch Targets

- All nav links padded to minimum 44×44px tap area on mobile
- Exhibition cards span full column width with native image aspect ratio maintained
- Footer links increase vertical padding to {spacing.lg} between items in stacked mobile layout
- Search overlay input occupies full screen width with large tap area; dismiss via top-right close icon at 44×44px

### Collapsing Strategy

- Primary nav collapses entirely below 744px; hamburger opens a full-height drawer with {colors.ink} background and white `nav-link` text
- Three-column exhibition grid steps to two columns at tablet, one at mobile — no carousel fallback; scroll is the navigation model
- Artist alphabetical list remains a flat scroll at all breakpoints; no accordion grouping by letter assumed
- Hero image always covers full width; text block anchors to bottom-left on desktop, bottom-full-width on mobile with reduced padding

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Apercu weight range not confirmed from extraction; Regular (400) and Medium (500) assumed; Bold (700) may exist but was not observed in extracted font stacks
- Exact letter-spacing and line-height values for EB Garamond at display sizes are editorial estimates; extraction did not yield computed CSS values
- The role of #175ea9 (institutional blue) is ambiguous — likely scoped to external link text or legacy press archive entries rather than an active system token
- Confirmed deployment contexts for #ffff80 are speculative; search hover, footer link hover, and pagination hover are inferred from gallery interaction patterns rather than extracted rules
- Mobile nav drawer color scheme not confirmed from extraction; ink fill assumed from brand character
- Animation timing curves and durations not extractable; 300ms ease-out and 150ms ease values are industry estimates
- Grid column counts, gutter widths, and maximum page-width constraints were not extracted; values above are inferred from contemporary-gallery layout conventions
- EB Garamond italic usage in exhibition titles is inferred from gallery typographic norms; actual font-style rules were not captured
