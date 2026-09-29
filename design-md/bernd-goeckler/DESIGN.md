---
version: alpha
name: "Bernd Goeckler"
source_url: "https://www.bgoecklerantiques.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep forest green (#116600) pressed against warm parchment (#e8e6de) is the visual argument Bernd Goeckler Antiques makes before a single object is shown — an unusual chromatic pairing that reads less like a retail color system and more like the interior of a well-appointed cabinet: hunting-lodge green meeting aged linen. The blush rose (#eeaacc) surfaces as a tertiary accent, the kind of dusty pink one finds in French Empire porcelain or faded chinoiserie wallpaper, never loud, always contextually exact. The canvas tone (#fafafa) is barely-white — warm enough to keep the antiquarian mood without going cream — while the ground neutrals stack from near-black (#222222) through charcoal (#343434) and mid-gray (#5c5c5c) to soft (#9e9e9e), a graduated ink wash rather than a hard contrast stack. Typography is the more telling signal: classicobold and classicoregular coexist with Josefin Sans and neutraface-light, a deliberate layering of geometric sans and serif-adjacent display cuts that suggests a house with distinct zones — specimen labels in one register, auction-house headers in another. Button and form elements use Josefin Sans at tracked uppercase, carrying an Art Deco drafting-room formality. Barlow handles longform descriptions at comfortable reading weight. Rounded corners throughout lean toward the hard end — `{rounded.xs}` and `{rounded.sm}` dominate; there are no pill shapes here, only the squared precision of a frame-maker's edge. Spacing is generous: individual object pages breathe at `{spacing.section}` vertical rhythm, letting photography (presumably studio-lit on neutral ground) do the persuasion. The overall grammar is low-volume, high-specificity — the digital equivalent of a quietly lit gallery on the upper east side where objects speak without labels and prices are disclosed on inquiry.

colors:
  primary: "#116600"
  primary-active: "#0d4f00"
  primary-disabled: "#8ab38a"
  primary-hover: "#145e00"
  accent-rose: "#eeaacc"
  accent-rose-muted: "#f5cde0"
  ink: "#222222"
  body: "#343434"
  muted: "#6e6e6e"
  muted-soft: "#9e9e9e"
  hairline: "#d4d4d4"
  hairline-soft: "#e2e2e2"
  canvas: "#fafafa"
  surface-warm: "#e8e6de"
  surface-warm-alt: "#e8e6dd"
  surface-card: "#ffffff"
  surface-soft: "#eeeeee"
  on-primary: "#fafafa"
  text-mid: "#5c5c5c"
  text-light: "#acacac"
  scrim: "#303030"

typography:
  display-xl:
    fontFamily: "'classicobold', 'Josefin Sans', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.02em
  display-lg:
    fontFamily: "'classicobold', 'Josefin Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0.01em
  display-md:
    fontFamily: "'classicoregular', 'Josefin Sans', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  caption-accent:
    fontFamily: "'neutraface-light', 'Barlow', sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.05em
  label-mono:
    fontFamily: "monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  button-md:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.14em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Josefin Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1em
    textTransform: uppercase
  price-display:
    fontFamily: "'classicoregular', 'Barlow', sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  object-title:
    fontFamily: "'classicobold', 'Josefin Sans', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.01em

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
    padding: 12px 28px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: "1.5px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 9px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: 10px 14px
    focusBorderColor: "{colors.primary}"
  text-input-label:
    typography: "{typography.title-sm}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    paddingHorizontal: "{spacing.xl}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-logo:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "4/5"
    padding: "{spacing.base}"
  product-card-title:
    typography: "{typography.object-title}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.md}"
  product-card-meta:
    typography: "{typography.caption}"
    textColor: "{colors.text-mid}"
    marginTop: "{spacing.xs}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.body}"
    marginTop: "{spacing.sm}"
  product-card-hover:
    borderColor: "{colors.primary}"
    boxShadow: "0 2px 16px rgba(17, 102, 0, 0.08)"
  hero-section:
    backgroundColor: "{colors.surface-warm}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xxl}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 700px
  hero-subline:
    typography: "{typography.body-md}"
    textColor: "{colors.text-mid}"
    marginTop: "{spacing.lg}"
    maxWidth: 540px
  object-detail-header:
    backgroundColor: "{colors.canvas}"
    paddingVertical: "{spacing.xxl}"
  object-detail-title:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
  object-detail-period:
    typography: "{typography.title-sm}"
    textColor: "{colors.primary}"
    marginBottom: "{spacing.sm}"
  object-detail-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    lineHeight: 1.75
    marginTop: "{spacing.lg}"
  object-detail-provenance:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.base}"
    marginTop: "{spacing.xl}"
  provenance-label:
    typography: "{typography.label-mono}"
    textColor: "{colors.text-light}"
    textTransform: uppercase
    letterSpacing: 0.08em
  category-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.text-mid}"
    typography: "{typography.caption-accent}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"
  period-tag:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  accent-rose-tag:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  divider-ornamental:
    borderTop: "1px solid {colors.hairline}"
    marginVertical: "{spacing.xxl}"
  section-label:
    typography: "{typography.title-md}"
    textColor: "{colors.primary}"
    letterSpacing: 0.12em
    marginBottom: "{spacing.lg}"
  inquiry-form:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxl}"
    border: "1px solid {colors.hairline}"
  inquiry-form-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.surface-soft}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xxl}"
  footer-nav-link:
    typography: "{typography.nav-link}"
    textColor: "{colors.text-light}"
    letterSpacing: 0.1em
  footer-address:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    lineHeight: 1.8
  pagination-control:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 36px
    width: 36px
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: "none"
    rounded: "{rounded.xs}"

## Components

### Buttons
**`button-primary`** — The primary CTA uses deep forest green (#116600) fill with near-white (#fafafa) Josefin Sans type at tracked uppercase, height 44px, virtually square corners (`{rounded.xs}`). On hover it deepens to #145e00 with no border radius change, communicating restraint over animation. The disabled state uses the desaturated sage #8ab38a to signal unavailability without visual noise.

**`button-secondary`** — A transparent-background, green-bordered ghost variant at the same height and tracking as `button-primary`. On hover, the warm parchment surface (#e8e6de) fills the interior, anchoring the interaction in the brand's material palette rather than defaulting to generic gray. Used for secondary actions like "Add to Inquiry" or "Save Object."

**`button-ghost`** — Hairline-bordered, muted-text, all-caps micro-label for tertiary actions (filter toggles, pagination controls). Sits at 36px height; keeps visual weight minimal so primary CTAs dominate.

### Navigation
**`nav-bar`** — 72px tall, #fafafa canvas, 1px hairline bottom border. Logo renders in `{typography.display-md}` using classicoregular, centered or left-anchored depending on viewport. Nav links use Josefin Sans tracked uppercase at 13px — active state gets a 2px solid green underline and primary-green text color. No dropdown mega-menus implied; category navigation is flat.

### Product / Object Grid
**`product-card`** — Hard-cornered (`{rounded.none}`), thin hairline border, 4:5 image ratio for portrait-oriented antique photography. The title uses `{typography.object-title}` (classicobold 22px), period attribution in `{typography.caption}` at muted mid-gray, price in `{typography.price-display}` (classicoregular 20px). On hover the border shifts to primary green with a very soft green-tinted shadow — a refined signal rather than a lift effect.

### Object Detail
**`object-detail-period`** — Small Josefin Sans uppercase label in primary green (#116600) runs above the main title as a period/style classifier (e.g., "EMPIRE PERIOD · CIRCA 1810"). Functions as the entry point that contextualizes everything below. **`object-detail-provenance`** — Separated by a hairline top border, monospace micro-label (`{typography.label-mono}`) announces "PROVENANCE" or "EXHIBITED" in a near-invisible gray before the body text. This archival ledger quality distinguishes serious object documentation from generic e-commerce description blocks.

### Badges and Tags
**`period-tag`** — Transparent-fill, green-border, green-text pill-adjacent tag (technically `{rounded.xs}`, not a pill) for period or movement labels. **`accent-rose-tag`** — The blush #eeaacc fill signals featured, newly acquired, or curated sub-collection membership. Used sparingly — one or two per page maximum. **`category-badge`** — Warm parchment fill with hairline border for typological classifiers (Bronze, Porcelain, Furniture, Drawings).

### Hero
**`hero-section`** — Warm parchment (#e8e6de) background with `{spacing.section}` vertical padding. Headline in classicobold 48px, subline in Barlow at comfortable reading width (540px max). A single `button-primary` or `button-secondary` CTA sits below the subline. No video backgrounds; the parchment ground implies the objects are the spectacle.

### Inquiry Form
**`inquiry-form`** — Warm parchment surface, `{rounded.sm}` corner, thin hairline border; functions as a contained module that can appear in a sidebar or centered modal. Title in classicoregular 28px. Fields use `{text-input}` with `{text-input-label}` above each in Josefin Sans uppercase micro-label style. Submits via `button-primary`.

### Footer
**`footer`** — Near-black scrim (#303030) full-width band. Navigation links in tracked Josefin Sans uppercase against `{colors.text-light}`. Address and contact in Barlow caption weight at `{colors.muted-soft}`. No imagery; structured like a printed colophon.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column object grid; nav collapses to hamburger or vertical drawer; hero headline drops to display-lg (36px); inquiry form goes full-width; footer stacks into single column |
| Tablet | 744–1128px | Two-column object grid; nav shows primary categories inline, secondary in overflow menu; hero padding reduces to `{spacing.xl}`; detail page splits into 1-column with stacked image/text |
| Desktop | 1128–1440px | Three-column object grid; full nav bar at 72px; hero at full `{spacing.section}` padding; detail page at 2-column (60/40 image/text split) |
| Wide | > 1440px | Max content width clamped at ~1400px, centered with auto side margins; grid may expand to 4 columns; hero max-width constraint applied to text block |

### Touch Targets
- All buttons minimum 44px height on mobile to meet accessibility minimums
- Product cards: full card surface is tappable, not just the title link
- Pagination controls expand to 44×44px on mobile despite 36px desktop size
- Nav links in mobile drawer: minimum 48px row height with `{spacing.base}` horizontal padding

### Collapsing Strategy
- Category filters collapse to a horizontal scrolling chip row on mobile, not a modal — keeps browsing in-flow
- Object detail provenance/condition sections collapse to accordion on mobile with Josefin Sans uppercase toggle labels
- Inquiry form moves from sidebar to a bottom-sheet or full-page route on mobile
- Footer navigation collapses to four labelled accordion groups on mobile to prevent wall-of-links presentation

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed font licensing details for classicobold/classicoregular — these appear to be custom or licensed variants; fallback stack should be verified with foundry
- neutraface-light detected in font stacks but no components clearly associated with it in extraction; may be used for large-display callouts or print-style bylines not captured
- No interaction states for mobile nav drawer confirmed (slide-in vs. full-overlay vs. push behavior unknown)
- Exact image treatment (zoom-on-hover, lightbox behavior, zoom-to-region for detail shots) not extractable from static hints — assume standard lightbox given product category
- Price display policy unclear — site may show prices publicly or use "Inquire" gating; both component variants should be built
- No confirmed dark-mode or print stylesheet detected
- #b3d4fc (light periwinkle blue) and #089edd (medium blue) appear in the extracted palette but could not be associated with a specific UI component; may be legacy or third-party widget colors (e.g., chat widget, map embed)
- Grid density (objects per row at desktop) unconfirmed; three-column assumption is based on category norms, not measured extraction
