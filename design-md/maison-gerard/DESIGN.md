---
version: alpha
name: "Maison Gerard"
source_url: "https://www.maisongerard.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The cobalt navy (#003399) at Maison Gerard's core reads not as digital blue but as something drawn from 18th-century Sèvres porcelain glaze — saturated, aristocratic, historically grounded. Against warm cream (#f4eee2) and amber (#b26840) — the latter precisely the hue of aged tortoiseshell and patinated brass — the palette reconstructs a European salon environment rather than a white-cube contemporary gallery. Typography doubles down on this historical-modernist tension: Futura (the 1927 Bauhaus face, in Light through Heavy weights) runs all display and navigation text, while Courier handles catalog annotation — lot numbers, provenance dates, edition marks — as if the gallery's inventory system predates digital typesetting. The pairing is dry and serious, never decorative. Cards carrying object photography use `{rounded.none}` — no softening, no friendliness — consistent with how auction house catalogs present works: images as evidence. `{colors.accent-amber}` appears in inquiry CTAs and selective hover states, warming the otherwise academic blue-and-cream field without softening it. Spacing reads institutional: generous padding in hero and exhibition sections at `{spacing.section}` compresses to tighter grids in inventory listings, prioritizing object count over atmospheric breathing room. The near-black `{colors.ink}` at #252525 keeps text dense and confident — this is a gallery that writes full provenance paragraphs, not bullet-point descriptors. Navigation runs uppercase Futura-Book at 12px with wide tracking, suggesting the aesthetic confidence of a private dealer who does not need to announce themselves loudly. The Courier face threading through metadata and provenance blocks is the most distinctive gesture: monospace type read alongside Futura display creates the tension between archival document and modernist monument that defines Maison Gerard's editorial voice.

colors:
  primary: "#003399"
  primary-active: "#002277"
  primary-disabled: "#99aad4"
  accent-amber: "#b26840"
  accent-amber-dark: "#8a4e2e"
  ink: "#252525"
  ink-soft: "#232221"
  body: "#4e4441"
  muted: "#808080"
  muted-light: "#afafaf"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#f4eee2"
  canvas-neutral: "#f3f3f3"
  surface-soft: "#f5f5f5"
  surface-card: "#fefefe"
  on-primary: "#fefefe"
  on-accent: "#fefefe"
  on-dark: "#f4eee2"

typography:
  display-xl:
    fontFamily: "'Futura-Heavy', 'Futura', 'Futura PT', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Futura-Bold', 'Futura', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Futura-Medium', 'Futura', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1px
  title-md:
    fontFamily: "'Futura-Medium', 'Futura', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
  title-sm:
    fontFamily: "'Futura-Book', 'Futura', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 1.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Futura-Book', 'Futura', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.1px
  body-sm:
    fontFamily: "'Futura-Light', 'Futura', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0.15px
  caption:
    fontFamily: "'Futura-Light', 'Futura', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0.3px
  catalog-label:
    fontFamily: "'Courier-Regular', 'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.02em
  catalog-bold:
    fontFamily: "'Courier-Bold', 'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.55
    letterSpacing: 0.02em
  catalog-italic:
    fontFamily: "'Courier-Italic', 'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.02em
    fontStyle: italic
  button-md:
    fontFamily: "'Futura-Medium', 'Futura', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Futura-Book', 'Futura', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  eyebrow:
    fontFamily: "'Futura-Book', 'Futura', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 2.5px
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
    padding: 14px 32px
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
  inquiry-button:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
  inquiry-button-active:
    backgroundColor: "{colors.accent-amber-dark}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    gap: "{spacing.md}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.catalog-label}"
    metaColor: "{colors.muted}"
    accentColor: "{colors.accent-amber}"
    hoverElevation: none
    hoverBorder: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: right
    imageOverlay: "linear-gradient(to right, rgba(244,238,226,0.90) 40%, transparent 100%)"
  exhibition-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.on-primary}"
    titleTypography: "{typography.display-sm}"
    padding: "{spacing.xxl} {spacing.section}"
    rounded: "{rounded.none}"
  artwork-detail:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.catalog-label}"
    metaColor: "{colors.muted}"
    provenanceTypography: "{typography.body-sm}"
    gap: "{spacing.xl}"
    rounded: "{rounded.none}"
    imageSide: left
    contentSide: right
  provenance-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.catalog-label}"
    accentColor: "{colors.accent-amber}"
    padding: "{spacing.lg}"
    borderLeft: "3px solid {colors.accent-amber}"
    rounded: "{rounded.none}"
  catalog-tag:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.catalog-label}"
    border: "1px solid {colors.hairline}"
    padding: "4px 10px"
    rounded: "{rounded.none}"
  inquiry-form:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    gap: "{spacing.lg}"
    rounded: "{rounded.none}"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.ink}"
  gallery-grid:
    columns: 3
    gap: "{spacing.lg}"
    backgroundColor: "{colors.canvas-neutral}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-light}"
    linkHoverColor: "{colors.accent-amber}"
    typography: "{typography.body-sm}"
    navTypography: "{typography.nav-link}"
    padding: "{spacing.section}"
    borderTop: none

## Components

### Buttons
**`button-primary`** — Flat cobalt navy (#003399) with hard corners (`{rounded.none}`); uppercase Futura-Medium at 12px with 1.8px letter-spacing gives CTAs the weight of printed labels rather than UI affordances. Active state darkens to #002277; disabled state washes to pale #99aad4. Used for primary navigation actions like "View All Works" and exhibition links.

**`button-secondary`** — Transparent background with 1px cobalt border; same uppercase type treatment. Deployed for secondary actions ("Download PDF", "View Press") alongside primary CTAs so the button pair reads as catalog column rather than competing hierarchy.

**`button-ghost`** — Same structure as secondary but with ink (#252525) border and text, reserved for use over cream canvas where the cobalt of secondary would compete with nearby primary elements.

**`inquiry-button`** — Amber (#b26840) fill replaces cobalt for all inquiry and contact-related CTAs. The warm shift marks these actions as relational rather than transactional, consistent with the private-gallery character of Maison Gerard where acquisition is a conversation, not a checkout.

### Inputs
**`text-input`** — Hard-cornered, neutral white field with 1px hairline border turning cobalt on focus — no glow, no shadow, just a line change. Futura-Book body text in the field; muted gray placeholder. The austerity matches a gallery inquiry form rather than a consumer signup.

### Navigation
**`nav-bar`** — 72px warm cream bar with hairline bottom border. Links run uppercase Futura-Book at 11px, 1.5px tracking — small, precise, deliberate. A logo wordmark sits left-anchored (likely Futura-Heavy); an "Inquire" or "Contact" CTA in cobalt sits right-aligned. No mega-menus or dropdown animations implied by the sparse palette.

### Product / Artwork Card
**`product-card`** — Portrait 3:4 image with zero border radius; the absence of rounding is the card's primary design statement. Title in Futura-Medium 16px; artist, date, and medium line in Courier-Regular 12px in muted gray — the monospace treatment of provenance data is the site's most distinctive typographic gesture, putting catalog documentation in typewriter face while the marketing layer stays in Futura. Amber color signals "Price on request" or acquisition prompts.

### Hero
**`hero`** — Cream canvas with a left-weighted gradient overlay protecting Futura-Heavy display text at 48px. Designed for full-bleed photography of a key object or installation. Right side bleeds photography to edge; subtitle in Futura-Book at 15px, 1.65 line-height reads as a sustained statement rather than a tagline.

### Exhibition Banner
**`exhibition-banner`** — Cobalt (#003399) full-width strip for current and upcoming exhibition announcements. Eyebrow in uppercase Futura-Book 10px at 2.5px tracking; title in Futura-Medium 22px, on-primary cream text. No photography — type and saturated color alone carry the weight of an opening announcement.

### Artwork Detail
**`artwork-detail`** — Split-panel layout: large image left, content panel right. Title in Futura-Bold 32px; metadata (artist, year, dimensions, medium, edition) in Courier-Regular 12px with muted color, stacked as a structured list. Provenance and exhibition history appear below in `{typography.body-sm}`. Amber inquiry button sits below the metadata stack.

### Provenance Block
**`provenance-block`** — Courier-Regular text block with 3px amber left border and soft gray background. Contains exhibition history, publication references, and ownership chain in the voice of a typed archival record. The border color ties archival content to the amber of the inquiry CTA, suggesting both are paths to acquisition.

### Catalog Tag
**`catalog-tag`** — Hairline-bordered label in Courier-Regular; used for medium descriptors, period tags ("Art Deco", "Mid-Century"), and material callouts. Sits alongside card metadata without competing for hierarchy.

### Gallery Grid
**`gallery-grid`** — Three-column grid on neutral gray (#f3f3f3) ground with 64px section padding. No hover overlays or image zooms; click navigates directly to detail. Gutter at 24px. Zero decorative borders between cells — the grid reads as a catalog spread.

### Inquiry Form
**`inquiry-form`** — Cream-background panel with hairline border and generous internal padding. Labels in uppercase title-sm (Futura-Book, 11px, 1.5px tracking); fields use the standard `text-input`. Deployed inline on artwork detail pages as a contextual contact surface, not a separate page.

### Footer
**`footer`** — Near-black (#252525) ground with warm cream text and muted-light (#afafaf) secondary links. Link hover shifts to amber — the only animated color change on the page. Navigation runs uppercase Futura nav-link style. Address block in Courier-Regular, consistent with the catalog treatment of documentary information.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column gallery grid; nav collapses to hamburger over cream overlay; hero image stacks below title text; artwork detail stacks image above content panel; inquiry form full-width |
| Tablet | 744–1128px | Two-column gallery grid; nav may abbreviate to key sections with overflow menu; hero remains full-bleed with gradient overlay |
| Desktop | 1128–1440px | Three-column gallery grid; full horizontal flat nav bar; split-panel artwork detail view; exhibition banner full-width |
| Wide | > 1440px | Container max-width ~1360px centered; optional four-column grid for inventory pages; hero image uses wider crop |

### Touch Targets
- All buttons minimum 44px height; inquiry-button and button-primary expand to full-width on mobile viewports
- Nav links expand to 48px tap height via increased vertical padding in mobile drawer
- Artwork cards span full column width; entire card surface is tappable
- Provenance block text remains 12px monospace — not scaled up on mobile; relies on legibility of Courier at small sizes

### Collapsing Strategy
- Primary nav reduces to logo + hamburger icon below 744px; drawer slides over cream canvas with hairline border
- Exhibition banner stacks eyebrow above title, centers text on narrow viewports
- Three-column gallery grid: collapses 3→2→1 at tablet then mobile breakpoints
- Artwork detail split panel: stacks image (full-width) above content column below 1128px
- Provenance block left-border and amber accent maintained at all breakpoints; no style degradation
- Footer columns stack vertically on mobile; address/contact block above social/newsletter row

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No logo SVG or wordmark extracted; Futura-Heavy assumed for logotype based on font stack — actual weight and sizing unconfirmed
- Several extracted colors (#00f3d4, #ff7fc1, #ffff00, #ff0000, #0000ff, #9215b6, #ff6600, #e4cd0e) appear to be browser focus-ring or form-validation states rather than brand palette entries — excluded from design tokens
- Exact nav section ordering and taxonomy not confirmed from extraction data
- No confirmed transition durations or easing curves; 150–200ms ease-in-out assumed as appropriate for gallery pacing
- Futura variant weight-to-numeric mappings (Light=300, Book=400, Medium=500, Bold=700, Heavy=800) inferred from convention — may differ in the actual embedded font files
- Mobile navigation pattern (hamburger vs. abbreviated horizontal) not directly confirmed
- No dark mode, night exhibition view, or high-contrast variant evidenced in extraction
