---
version: alpha
name: "Lehmann Maupin"
source_url: "https://www.lehmannmaupin.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Univers LT W01 — a Swiss-modernist grotesque from the 1950s — carries every typographic moment on the Lehmann Maupin site, from 45-weight display headers through 55 Roman body copy: a face so resolutely neutral that the artworks it frames read as the only objects on screen with personality. The palette is almost entirely achromatic. Warm near-black (#232221) holds the ink register; bone whites (#fefefe, #f3f3f3) spread across the canvas; a long chromatic ramp of cool grays (#9ba2a7, #afafaf, #727272, #b3b3b3) dissolves across navigation chrome and hairline rules. Against that monochrome field, pure #ffff00 detonates — a raw, unmodulated yellow deployed in hover states and interactive moments as electric signal rather than decorative accent. It is a gallery-world move: the color that marks where attention should land without committing to any art movement's chromatic allegiances. The deep blues (#003399, #0000ff) resolve to link states, functional inheritance rather than designed gestures. All corners run sharp — {rounded.none} is the structural default — reinforcing the institutional flatness of a space that has presented Tracey Emin, Do Ho Suh, and Hernan Bas across four cities. Spacing breathes at gallery-wall scale rather than e-commerce urgency, with {spacing.section} gutters letting each exhibition image claim its territory uninterrupted. Type hierarchies rely entirely on weight variation within the Univers family: 45 Light at large scale versus 65 Bold for micro-labels and uppercase navigation tabs, with the 55 Oblique reserved for artwork title lines, where convention demands italicization. The gallery trusts the single-family system to carry all design work without mixing a secondary face. The footer collapses into a tight typographic grid of newsletter capture, four location addresses, and fine-print legal — all in Univers 45 Light at 11–12px, rendering the gallery's global infrastructure as almost incidental to the primary experience of the work.

colors:
  primary: "#ffff00"
  primary-active: "#e6e600"
  primary-disabled: "#ffffb3"
  ink: "#232221"
  body: "#4e4441"
  muted: "#727272"
  muted-light: "#afafaf"
  hairline: "#b3b3b3"
  hairline-soft: "#d4d4d4"
  canvas: "#fefefe"
  surface-soft: "#f3f3f3"
  surface-card: "#f5f5f5"
  on-primary: "#111111"
  on-dark: "#fefefe"
  cool-gray: "#9ba2a7"
  link: "#003399"
  near-black: "#111111"

typography:
  display-xl:
    fontFamily: "'Univers LT W01_45 Light1475944', 'Univers LT W01_45 Light1475950', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Univers LT W01_45 Light1475944', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Univers LT W01_55 Roman1475956', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Univers LT W01_55 Roman1475956', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Univers LT W01_65 Bold1475968', 'Univers LT W01_65 Bold_1475974', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "'Univers LT W01_55 Roman1475956', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Univers LT W01_55 Roman1475956', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-oblique:
    fontFamily: "'Univers LT W01_55 Obliq1475962', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    fontStyle: oblique
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Univers LT W01_45 Light1475944', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
  micro-label:
    fontFamily: "'Univers LT W01_65 Bold1475968', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Univers LT W01_55 Roman1475956', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Univers LT W01_45 Light1475944', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  nav-active:
    fontFamily: "'Univers LT W01_65 Bold1475968', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 28px
    height: 44px
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 27px
    height: 44px
    hoverBackgroundColor: "{colors.primary}"
    hoverBorderColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  button-text-link:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    hoverColor: "{colors.primary}"
    borderBottom: "none"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.cool-gray}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    activeTypography: "{typography.nav-active}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  sub-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    height: 40px
    borderBottom: "1px solid {colors.hairline-soft}"
  exhibition-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/3"
    rounded: "{rounded.none}"
    artistTypography: "{typography.title-sm}"
    titleTypography: "{typography.body-oblique}"
    dateTypography: "{typography.caption}"
    artistColor: "{colors.ink}"
    titleColor: "{colors.body}"
    dateColor: "{colors.muted}"
    captionSpacing: "{spacing.sm}"
    hoverImageOpacity: 0.85
  artist-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "1/1"
    rounded: "{rounded.none}"
    nameTypography: "{typography.title-md}"
    nameColor: "{colors.ink}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    hoverOverlay: "{colors.primary}"
    hoverOverlayOpacity: 0.1
  exhibition-hero:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    artistTypography: "{typography.display-sm}"
    dateTypography: "{typography.body-sm}"
    imageObjectFit: cover
    overlayGradient: "linear-gradient(to top, rgba(35,34,33,0.80) 0%, transparent 55%)"
    minHeight: 600px
  artwork-caption:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    artistTypography: "{typography.title-sm}"
    titleTypography: "{typography.body-oblique}"
    mediumTypography: "{typography.caption}"
    dimensionsTypography: "{typography.caption}"
    spacing: "{spacing.sm}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-light}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.ink}"
    inactiveBorderBottom: "2px solid transparent"
    typography: "{typography.title-sm}"
    height: 48px
    borderBottom: "1px solid {colors.hairline}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-md}"
    placeholderColor: "{colors.cool-gray}"
    rounded: "{rounded.none}"
    overlayOpacity: 1
    closeIconColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.micro-label}"
    height: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    labelTypography: "{typography.micro-label}"
    linkColor: "{colors.muted-light}"
    linkHoverColor: "{colors.primary}"
    padding: "{spacing.xxl} 0"
  newsletter-input:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.cool-gray}"
    border: "none"
    borderBottom: "1px solid {colors.muted-light}"
    focusBorderBottom: "1px solid {colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"

## Components

### Buttons

**`button-primary`** — A sharp-cornered dark rectangle (#232221 fill, white label) with uppercase Univers 55 Roman set at 13px and 1.2px letter-spacing. On hover, the background flashes to pure yellow (#ffff00) and the label switches to near-black (#111111), a sudden jolt that reads as voltage rather than warmth. No shadow, no radius, no transition flourish beyond the color swap.

**`button-secondary`** — Same geometry, ghost treatment: transparent fill with a 1px ink border. Hover mirrors the primary: the outline dissolves into a yellow fill with dark label. Both button types run at 44px height, a comfortable touch target that doesn't telegraph e-commerce urgency.

**`button-text-link`** — Uppercase spaced label with no underline at rest. Used for inline navigation actions ("View Exhibition", "Read More"). On hover, label color shifts from #232221 to #ffff00 as the only motion.

### Navigation

**`nav-bar`** — White canvas bar at 64px, logotype left, primary navigation links center or right in Univers 45 Light 14px. Active section switches to Univers 65 Bold, same size — weight shift alone marks selection without color or underline. A 1px hairline rule (#b3b3b3) separates the bar from page content. On exhibition and artist pages a secondary `sub-nav` drops below in surface-soft (#f3f3f3) for section tabs.

**`filter-bar`** — Horizontal tab row for browsing states (Current / Upcoming / Past, or All / Painting / Sculpture). Each tab is micro-label uppercase; the active tab gains a 2px bottom border in ink (#232221), inactive tabs have a 2px transparent bottom border for stable height. No pill or chip treatment — pure typographic distinction.

### Exhibition & Artwork

**`exhibition-card`** — The primary browsing unit. Artwork image fills a 4:3 frame with no border or shadow; on hover the image dims to 85% opacity. Below the image: artist name in title-sm uppercase (11px bold, 0.8px tracking), title line in body-oblique (14px oblique, conventional italicization for artwork titles), date range in caption (12px light, muted color). No card border, no background tint — the card is just image plus caption block on the white canvas.

**`artwork-caption`** — Appears beside or below a single artwork in the detail view. Artist name uppercase, then oblique title, then medium and dimensions in caption weight. All on transparent background, sitting directly against the page canvas. Spacing between lines uses {spacing.sm}.

**`artist-card`** — Square 1:1 portrait image with name below in title-md (18px roman) and optionally nationality/birth-year in caption. On hover a faint yellow tint (#ffff00 at 10% opacity) overlays the image, the lightest possible signal that the card is interactive.

### Hero

**`exhibition-hero`** — Full-bleed photographic banner, minimum 600px tall, with a gradient scrim (dark near-black to transparent, rising from the bottom 55%) that grounds white display-xl type. Artist name sits in display-sm (24px roman), exhibition title in display-xl (48px light), date range in body-sm below. The sparse type floats above the image rather than sitting in a lockup box.

### Utility

**`announcement-bar`** — A pure yellow (#ffff00) bar 36px tall pinned above the nav, running micro-label uppercase in near-black. Used for fair announcements, openings, or time-sensitive gallery news. The yellow bar is the loudest single element on the entire site.

**`search-overlay`** — A full-screen white overlay at full opacity. A single text input renders in display-md (32px light) with cool-gray placeholder text. No rounded corners, no container border — the cursor blinks in a near-empty white field. Close control sits top-right in ink color.

**`footer`** — Near-black (#232221) full-width footer. Four column groups: gallery locations with address blocks, navigation links, social links, newsletter capture. All type in body-sm (14px) and micro-label uppercase. Link default is muted-light (#afafaf), hover flips to yellow (#ffff00). The `newsletter-input` uses no visible box — only a 1px bottom rule that brightens to yellow on focus.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column exhibition grid; nav collapses to hamburger icon; hero height drops to 420px; display-xl scales to 28px; filter-bar scrolls horizontally |
| Tablet | 744–1128px | Two-column exhibition grid; nav links visible but condensed; hero at 500px; sub-nav tabs visible |
| Desktop | 1128–1440px | Three-column exhibition grid; full nav with all primary links; hero at 600px minimum |
| Wide | > 1440px | Grid expands to four columns; max content width ~1400px centered; hero scales to viewport with image reposition |

### Touch Targets

- All buttons minimum 44px height, matching the defined component height
- Nav links minimum 44px tap height via padding, regardless of 14px type size
- Filter-bar tabs minimum 44px height
- Exhibition cards have no minimum — the image is the tap target and is naturally large

### Collapsing Strategy

- Primary nav collapses to a full-screen overlay on mobile, not a compact dropdown — the menu opens as a white layer with large-type links in display-sm
- Sub-nav and filter-bar shift to horizontally scrollable single rows below 744px with no visible scroll indicator, matching gallery convention
- Exhibition hero switches from bottom-anchored text to center-anchored on mobile to avoid overlap with cropped image edges
- Footer columns stack vertically on mobile; newsletter input moves above location blocks

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact nav height and logo dimensions not confirmed from extraction; 64px is an estimate from typical gallery site conventions
- Animation timing and easing for hover color transitions (#ffff00 flash) not extractable from static crawl
- Whether #007aff appears as a native UI control default (iOS Safari tap highlight) or an intentional brand color is ambiguous; treated here as system UI default and excluded from palette
- Dark mode treatment unknown — the site likely has none given the gallery's static-white aesthetic, but not confirmed
- Exact grid column counts and gutter widths at each breakpoint not extracted; values above are inferred from gallery layout conventions
- Price display formatting and inquire-to-purchase flow components not observed in extraction; artwork-caption handles available metadata only
- Hover video previews on exhibition cards (common in gallery sites) not confirmed present or absent
