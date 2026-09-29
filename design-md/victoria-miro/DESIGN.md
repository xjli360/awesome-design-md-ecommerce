---
version: alpha
name: "Victoria Miro"
source_url: "https://www.victoria-miro.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Powder blue (#a5d3ef) sits at the top of the Victoria Miro color stack — an unexpected softness for a gallery showing Chantal Joffe, Isaac Julien, and Yayoi Kusama. The color is not decorative; it almost certainly marks the hover or active state on navigation links, the quiet chromatic signal that something is interactive. Against a dominant white canvas, this restraint places the full visual weight on the reproduced artworks — no competing brand color contests a Kusama accumulation or an Ofili canvas. The second blue, #2d89ef, functions as a more direct action color: links within body copy, a selected filter state, or a pressed indicator. Body text resolves to #222222, a near-black that reads printed rather than screen-native — the site behaves like a bound catalogue, not a storefront. Typography was not extractable from the live crawl; the site likely loads type tokens via JavaScript or behind bot-protection. Based on the catalogue-print sensibility common to galleries of this institutional standing, the type system almost certainly runs a restrained neo-grotesque — Helvetica Neue or an equivalent — at light weights for display headings and regular for body copy. Exhibition titles follow art-world editorial convention and appear in italic. All corners run sharp (`{rounded.none}`): no softening gestures, no pill buttons, no rounded cards. Layout uses strict vertical rhythm and generous white margins, treating each artist page as a monograph. White negative space is the dominant visual element — images of artwork float in it, and text sits recessed enough that the eye reads image first, label second.

colors:
  primary: "#a5d3ef"
  primary-active: "#2d89ef"
  primary-disabled: "#d6eaf7"
  ink: "#222222"
  body: "#333333"
  muted: "#666666"
  hairline: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#222222"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.08em
    textTransform: uppercase
  artist-name:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  exhibition-title:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
    fontStyle: italic
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.04em

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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    opacity: 0.85
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    activeUnderline: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    gap: "{spacing.md}"
  hero-full-bleed:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 80vh
    padding: "{spacing.xxl} {spacing.xl}"
  artist-listing-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.artist-name}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    imageAspect: "4/5"
    hoverImageScale: 1.02
  exhibition-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.exhibition-title}"
    dateTypography: "{typography.caption}"
    rounded: "{rounded.none}"
    imageAspect: "3/2"
    archivedOpacity: 0.6
  artwork-viewer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    titleTypography: "{typography.title-md}"
    captionColor: "{colors.muted}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  gallery-highlight:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.section}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl}"
    rounded: "{rounded.none}"
  tag-label:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  section-divider:
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    marginY: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — A flat ink rectangle with no radius, letter-spaced uppercase text at 13px weight 400. The deliberate inversion from a brand-color CTA is the defining choice: at Victoria Miro, the artworks carry chromatic energy and the UI recedes to ink-on-white. Hover reduces opacity to 0.85; active tightens further; keyboard focus uses a 2px `{colors.primary}` outline offset from the element so the blue accent appears only for accessibility, not aesthetics.

**`button-secondary`** — Identical typographic spec with a 1px `{colors.ink}` border and transparent fill. Sits alongside primary for secondary actions ("View Works" beside "Enquire"). Hover fills to `{colors.surface-soft}` — barely perceptible, consistent with the gallery's dislike of aggressive UI feedback.

### Navigation
**`nav-bar`** — White background with a hairline bottom border at `{colors.hairline}`. Logo wordmark sits left; all section links right at 13px with modest letter-spacing — no weight differentiation between sections. The active section gains a 1px underline in `{colors.primary}` rather than a bold weight change, keeping the visual noise at a minimum. On scroll the bar sticks but retains its white fill with no elevation shadow.

### Artist Listing Card
**`artist-listing-card`** — Portrait-format image (4:5 aspect) with artist name below in `{typography.artist-name}` (weight 300, 22px) and a subdued year or medium line in `{typography.caption}`. No hover overlay or title reveal — the image scales to 1.02× on hover via a smooth transition. No border, no shadow, no radius; images sit directly on the white canvas like prints laid out for review.

### Exhibition Card
**`exhibition-card`** — Landscape image (3:2) with exhibition title in `{typography.exhibition-title}` (italic, weight 300) below, followed by artist name and date range in `{typography.caption}`. Archived or past exhibitions carry 0.6 opacity on the image to signal historical distance without removing them from the grid.

### Artwork Viewer
**`artwork-viewer`** — Full-bleed or max-width-constrained image centered on a white field, with a discreet caption block below: title in `{typography.title-md}`, medium and year in `{typography.caption}` at `{colors.muted}`. Padding of `{spacing.xl}` on all sides gives the work room. No decorative chrome — a minimal close affordance for modal contexts only, positioned unobtrusively in the corner.

### Gallery Highlight
**`gallery-highlight`** — A full-width section band in `{colors.primary}` (#a5d3ef), used sparingly for fair announcements, prize shortlist notices, or residency features. Text in `{colors.ink}` at `{typography.body-md}`. The powder blue as a background reads institutional without aggression — closer to a washed linen ground than a saturated marketing band.

### Footer
**`footer`** — Ink-black background with white text in `{typography.body-sm}`. Links for each gallery location (London Wharf Road, London Mayfair, Venice), a newsletter sign-up field, and social links rendered as text labels rather than icon glyphs — consistent with the gallery's editorial register. No decorative dividers; columns separate by whitespace alone.

### Tag Label
**`tag-label`** — Used for medium categories ("Painting", "Film", "Photography") or art fair names in exhibition filter interfaces. Hairline border, no fill, muted text, no radius. Sits alongside artist names or as selectable filters; selected state inverts to `{colors.ink}` fill with `{colors.canvas}` text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger with slide-in drawer; artist grid drops to 1 column; artwork images are full-bleed edge-to-edge with caption stacked below |
| Tablet | 744–1128px | Two-column artist grid; nav links may abbreviate or collapse secondary items; hero imagery scales to viewport height; exhibition cards 2-col |
| Desktop | 1128–1440px | Three or four-column artist/artwork grid; full nav visible; artist biography and image sit side-by-side |
| Wide | > 1440px | Max-width container (~1440px) centered on white; grid may extend to five columns; outer margins remain generous canvas white |

### Touch Targets
- All interactive elements (nav links, artist cards, artwork thumbnails, buttons) maintain minimum 44×44px touch target even when the visible label is smaller
- The hamburger menu icon uses a 44×44px tap region with no visible bounding box
- Footer links use at minimum `{spacing.xl}` vertical padding between rows to prevent mis-taps on dense address blocks

### Collapsing Strategy
- Navigation: full horizontal link row collapses to hamburger with white slide-in drawer; same typographic treatment as desktop, no weight or size change
- Artist grid: 4-col → 3-col → 2-col → 1-col across breakpoints; portrait aspect preserved at all sizes
- Exhibition cards: 3-col → 2-col → 1-col; image always above text on all breakpoints, never beside
- Artwork viewer: two-column (image left, caption right) on desktop collapses to stacked single column on tablet and mobile, caption below image
- `gallery-highlight` band: padding reduces from `{spacing.section}` to `{spacing.xxl}` on mobile; body text remains same size

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families extracted from the live site — the entire type stack is inferred from institutional gallery conventions; actual webfont name, weights, and variable-font axes are unknown
- Only three hex values were extracted; secondary states (link hover, text selection, focus rings, input active borders) are derived rather than confirmed
- No spacing, sizing, or breakpoint tokens extracted; all values follow catalogue-layout conventions
- Whether #2d89ef (`{colors.primary-active}`) is used for interactive links, a selected-state indicator, or another specific component is not confirmed from extraction
- Icon library presence, glyph style, and weight unknown — galleries of this type often use only minimal directional arrows
- Navigation depth (flat links vs. flyout panels for Artists, Exhibitions, etc.) not confirmed
- Mobile menu transition style (slide, fade, full-screen overlay) not confirmed
- Print stylesheet presence — likely given the catalogue orientation, but not verified
