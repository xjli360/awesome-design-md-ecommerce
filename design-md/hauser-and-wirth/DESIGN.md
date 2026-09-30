---
version: alpha
name: "Hauser & Wirth"
source_url: "https://www.hauserwirth.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every pixel on hauserwirth.com serves the same purpose as the white wall in one of their gallery spaces — to recede so completely that the artwork becomes the only thing you see. The digital identity runs on a strict monochrome axis: deep carbon black (#111111) letterforms set against a pure white canvas, with no decorative color accent competing for attention. Type is the primary architectural element; large-scale display headings in a refined grotesque serif carry the editorial weight that a lesser brand would assign to illustration or iconography. Navigation collapses to bare text links with generous negative space, reflecting the gallery's conviction that restraint is itself a curatorial statement. Artist pages open with full-bleed artwork photography — no rounded corners (`{rounded.none}`), no drop shadows, no overlaid gradient scrims — images bleed edge to edge at maximum fidelity the way a work on paper is presented unmatted. Exhibition listings and press releases follow a strict typographic grid reminiscent of the Swiss International Style: column rules, flush-left body copy at comfortable measure, and a header hierarchy that communicates urgency through scale alone rather than color. The footer spans the full page width in near-black, providing the only chromatic shift in the entire layout. Interactive affordances — buttons, form fields, hover states — are expressed through weight change and underline rather than background fill, keeping the palette unbroken. The overall effect is a digital environment that feels less like a commercial website and more like a well-designed institution catalogue: authoritative, unhurried, and completely confident that the work speaks for itself without promotional scaffolding.

colors:
  primary: "#111111"
  primary-active: "#000000"
  primary-disabled: "#999999"
  ink: "#111111"
  body: "#333333"
  muted: "#666666"
  hairline: "#dddddd"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-footer: "#111111"
  on-primary: "#ffffff"
  on-footer: "#ffffff"
  accent-rule: "#111111"
  press-link: "#111111"

typography:
  display-xl:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.01em
  caption-italic:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.5
    letterSpacing: 0
  artwork-title:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.3
    letterSpacing: 0
  label-uppercase:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.05em
    textTransform: uppercase
  nav-link:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  footer-link:
    fontFamily: "'GT America', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 12px
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
  section: 80px
  hero: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
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
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
    rounded: "{rounded.none}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 10px 0
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoStyle: wordmark-only
    padding: "0 {spacing.xl}"
  nav-link-hover:
    textColor: "{colors.muted}"
    textDecoration: none
  mobile-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xl}"
  exhibition-hero:
    layout: full-bleed
    imageRounded: "{rounded.none}"
    overlayColor: transparent
    captionTypography: "{typography.caption-italic}"
    captionColor: "{colors.muted}"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.ink}"
    titlePosition: below-image
  artist-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    imageRounded: "{rounded.none}"
    nameTypography: "{typography.title-md}"
    nameColor: "{colors.ink}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    hoverBehavior: name-underline
  exhibition-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/2"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.artwork-title}"
    subtitleColor: "{colors.body}"
    dateTypography: "{typography.caption}"
    dateColor: "{colors.muted}"
    locationTypography: "{typography.label-uppercase}"
    locationColor: "{colors.muted}"
  artwork-caption:
    backgroundColor: transparent
    artistTypography: "{typography.title-sm}"
    artistColor: "{colors.ink}"
    titleTypography: "{typography.artwork-title}"
    titleColor: "{colors.body}"
    detailTypography: "{typography.caption}"
    detailColor: "{colors.muted}"
    padding: "{spacing.sm} 0 0 0"
  section-divider:
    height: 1px
    backgroundColor: "{colors.hairline}"
    margin: "{spacing.section} 0"
  section-label:
    typography: "{typography.label-uppercase}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.lg}"
    borderTop: "1px solid {colors.accent-rule}"
    paddingTop: "{spacing.md}"
  press-listing:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    sourceTypography: "{typography.caption}"
    sourceColor: "{colors.muted}"
    border: "none"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.lg} 0"
  footer:
    backgroundColor: "{colors.surface-footer}"
    textColor: "{colors.on-footer}"
    typography: "{typography.footer-link}"
    padding: "{spacing.section} {spacing.xl}"
    linkHoverColor: "{colors.muted}"
  newsletter-signup:
    backgroundColor: "{colors.canvas}"
    inputBorder: "1px solid {colors.hairline}"
    inputBorderFocus: "1px solid {colors.ink}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-md}"
    rounded: "{rounded.none}"
    labelTypography: "{typography.label-uppercase}"
    labelColor: "{colors.muted}"
  location-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "4px {spacing.sm}"
  tag-chip:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "4px {spacing.sm}"

## Components

### Buttons
**`button-primary`** — A strictly sharp-cornered rectangle (`{rounded.none}`) filled in deep carbon (`{colors.primary}`), with uppercase tracking text (`{typography.button-md}`) in white. Active state darkens to pure black; disabled state falls to mid-gray. No shadow, no gradient — the button reads as a typographic element before it reads as an interactive affordance.

**`button-secondary`** — Same geometry as the primary but inverted: white fill (`{colors.canvas}`) with a 1px hairline border in ink, maintaining the hard rectangular silhouette. Hover state fills the interior with off-white (`{colors.surface-soft}`) without altering the border.

**`button-text-link`** — No background, no border, no padding. Underlined body-small text that functions as an inline affordance inside editorial copy. The underline is the only signal.

### Navigation
**`nav-bar`** — A white horizontal bar 64px tall, separated from page content by a single hairline (`{colors.hairline}`). The wordmark sits flush left. Primary nav links center in modest 14px regular weight — no bold, no color differentiation from the surrounding field. A hamburger icon appears at the right edge on mobile. No mega-menu backgrounds; dropdowns, if present, inherit the white canvas.

### Cards
**`artist-card`** — Square-cropped portrait image at 4:5 aspect ratio with zero rounding. Name in `{typography.title-md}` sits immediately below with a single line for birth year, nationality, or represented gallery location in caption gray. On hover, the artist name underlines; no overlay, no lift, no scale — the image stands undecorated.

**`exhibition-card`** — Landscape 3:2 image, no rounding, no shadow. Exhibition title in `{typography.title-md}`, followed by artist name in italic `{typography.artwork-title}`, date range in small caption, and location in uppercase tracking label. The entire card links without a visible CTA button.

### Exhibition Hero
**`exhibition-hero`** — A full-bleed image that spans the viewport edge-to-edge with no horizontal padding. The image carries no overlay, gradient, or text on top of it. Title, artist name, and date are typeset below the image in the page grid, allowing the artwork to exist at full resolution uncompromised. Captions use `{typography.caption-italic}` in `{colors.muted}`.

### Artwork Caption
**`artwork-caption`** — Three-tier typographic block below artwork thumbnails: artist name in medium weight (`{typography.title-sm}`), title in italic (`{typography.artwork-title}`), and medium/dimensions/year in small caption gray. No container, no background — pure typography on canvas.

### Section Labels
**`section-label`** — A thin top rule (`{colors.accent-rule}`) above an uppercase tracked label in `{colors.muted}`. Introduces sections like "Current Exhibitions", "Artists", "Publications". Spacing between the rule and text is `{spacing.md}`.

### Footer
**`footer`** — Full-width near-black block (`{colors.surface-footer}`) with white links in `{typography.footer-link}`. Column layout organizes gallery locations, social links, legal copy, and newsletter signup. The footer is the only zone in the design where the background shifts from white, providing a clear terminal boundary.

### Newsletter
**`newsletter-signup`** — Minimal form: an uppercase label, a borderless or single-rule input field, and a black submit button. No decorative container, no illustration.

### Tags and Location Badges
**`tag-chip`** and **`location-badge`** — Hairline-bordered rectangular chips in uppercase tracking at 11px. Used to filter exhibitions by gallery location (New York, London, Los Angeles, Somerset, Zürich). No fill, tight padding — these read as index markers rather than buttons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; nav collapses to full-screen overlay menu; exhibition hero image fills 100vw; artist cards 1-up; typography scales down to display-md for headers |
| Tablet | 744–1128px | Two-column artist/exhibition grids; nav bar retains text links for primary items; hero image fills viewport width |
| Desktop | 1128–1440px | Three- or four-column grids for artist and exhibition listings; full horizontal nav with all links visible; constrained max-width content column with generous side gutters |
| Wide | > 1440px | Content column max-width caps around 1440px and centers; image tiles may expand to a 5-column grid; hero images fill 100% of the capped container |

### Touch Targets
- All nav links and card tap targets extend to minimum 44×44px via padding, despite visually compact type
- Bottom navigation or drawer trigger on mobile sits in the lower-right zone for thumb access
- Filter/location chips sized to at least 36px height on mobile with expanded touch padding

### Collapsing Strategy
- Primary navigation collapses at the tablet breakpoint to a hamburger icon; the revealed panel renders full-screen with large display-type links
- Multi-column exhibition and artist grids reduce from 4 → 3 → 2 → 1 column as viewport narrows
- Footer columns stack vertically on mobile with section headings acting as accordion triggers
- The section-label rule and uppercase label stack responsively, maintaining their top-rule visual signature at every breakpoint

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Extraction completely failed**: the live site at hauserwirth.com was intercepted by a Vercel security checkpoint; extracted colors (#0070f3, #3291ff) and fonts are Vercel system UI tokens, not Hauser & Wirth brand assets — they have been discarded entirely
- **Exact typeface**: GT America is inferred from the gallery's known design vocabulary; the production site may use a licensed variant, a custom cut, or an alternate grotesque such as Neue Haas Grotesk or Suisse Int'l — requires direct CSS inspection
- **Precise color values**: all hex values in this file are derived from widely-observed gallery-brand conventions (monochrome, white-canvas dominant), not from pixel-extracted site data; the production palette may include warm-tinted whites or off-blacks that differ from pure #111111/#ffffff
- **Accent/highlight color**: it is unknown whether the site uses any chromatic accent for hover states, active indicators, or promotional banners — no extractable data was available
- **Exact nav height and grid gutters**: inferred from gallery-site conventions; production measurements require DevTools inspection
- **Animation and transition specs**: hover transition timing, image-load fade behavior, and scroll-driven effects could not be captured
