---
version: alpha
name: "Thaddaeus Ropac"
source_url: "https://ropac.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The palette holds five nearly identical warm grays and then breaks twice — a brick red (#c52f24) held in reserve for primary interactions and hover states, and a near-neon yellow (#ffff80) that reads as deliberate as a Dan Flavin fluorescent installation against a white plinth room. The ground is the warm off-white #eeebe9 rather than clinical white, giving artwork photography a very slight warmth that pure #ffffff would flatten into uniformity. All type runs in Formale-Grotesque, a tight-aperture European grotesque with enough personality to feel institutional without feeling cold — the face a Documenta catalogue might choose for its running text. Weight distribution is deliberately conservative: display sizes hold at 300–400 rather than 700, signaling that photography commands hierarchy and text only names. The red never crowds artwork reproduction; it surfaces on links, focus rings, and occasional accent rules, holding down the interactive layer without competing for the eye's first landing. The yellow (#ffff80) functions more like a selection glaze than a structural brand color — possibly marking current navigation states or exhibition highlights rather than CTAs. Corners are uncompromisingly square ({rounded.none}), rejecting the consumer-product radius vocabulary entirely. Navigation runs as plain horizontal text: artist names, exhibition titles, fair appearances, publications — each a flat link rather than a card. The gallery's four cities (Salzburg, Paris, London, Seoul) appear in text rather than imagery of physical spaces, keeping visual attention on the work itself. Individual exhibition pages breathe with generous vertical spacing ({spacing.section}), press-release prose treated as first-class content alongside installation photography that bleeds to the full viewport edge. The muted gray cluster (#515656 through #636969) provides a five-stop neutral scale that handles caption credits, secondary navigation, ruled lines, and disabled states without introducing any new hue into the system. The result is a site that feels closer to a printed museum catalogue than a commercial destination.

colors:
  primary: "#c52f24"
  primary-active: "#a82720"
  primary-disabled: "#e8a09c"
  accent-yellow: "#ffff80"
  ink: "#515656"
  body: "#636969"
  muted: "#777777"
  muted-warm: "#636a68"
  warm-gray-mid: "#606464"
  hairline: "#d4d0ce"
  canvas: "#ffffff"
  surface-soft: "#eeebe9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 72px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  exhibition-title:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  nav-primary:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  nav-artist:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.3px
  caption-italic:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 11px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.45
    letterSpacing: 0
  button-md:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  label-uppercase:
    fontFamily: "'Formale-Grotesque', sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.8px
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 27px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-link:
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    textDecoration: underline
    hoverColor: "{colors.primary}"
  text-input:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "none"
    borderBottom: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 0
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-primary}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-primary}"
    borderBottom: "1px solid {colors.primary}"
  exhibition-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-md}"
    subtitleTypography: "{typography.caption}"
    subtitleColor: "{colors.muted}"
    captionTypography: "{typography.caption-italic}"
    captionColor: "{colors.muted}"
    rounded: "{rounded.none}"
    gap: "{spacing.md}"
  artist-list-item:
    textColor: "{colors.ink}"
    typography: "{typography.nav-artist}"
    hoverColor: "{colors.primary}"
    padding: "{spacing.xs} 0"
    borderBottom: "1px solid {colors.hairline}"
  hero-fullbleed:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    captionTypography: "{typography.caption}"
    overlayOpacity: 0.0
    padding: "0"
    minHeight: "85vh"
  artwork-caption:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    italicVariant: "{typography.caption-italic}"
    gap: "{spacing.xs}"
  section-label:
    textColor: "{colors.muted}"
    typography: "{typography.label-uppercase}"
    marginBottom: "{spacing.lg}"
  exhibition-title-block:
    textColor: "{colors.ink}"
    typography: "{typography.exhibition-title}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.body}"
    gap: "{spacing.sm}"
  filter-tag:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 6px 12px
    hoverBorderColor: "{colors.ink}"
    hoverColor: "{colors.ink}"
  filter-tag-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.ink}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 6px 12px
  search-field:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.ink}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    placeholderColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.accent-yellow}"
    padding: "{spacing.section} {spacing.xl}"
  press-release-body:
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    maxWidth: 720px
  city-selector:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    gap: "{spacing.lg}"
    separator: " / "
  highlight-bar:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"
  publication-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"

## Components

### Buttons

**`button-primary`** — A flat rectangular block in brick red (#c52f24) with all-caps Formale-Grotesque at 12px / 1.2px tracking. No border radius ({rounded.none}), 44px tall, 28px horizontal padding. Hover and active darken to #a82720; disabled state uses the pale coral (#e8a09c) with white text still legible. This button appears sparingly — enquiry forms, newsletter sign-up — never in content listing pages.

**`button-secondary`** — Transparent fill, 1px ink border, same uppercase typographic treatment as primary. Sits alongside `button-primary` in enquiry and purchase contexts where a "learn more" or "download press release" option is needed. Hover inverts to ink-fill with white text.

**`button-ghost`** — Transparent, no border, primary red text with underline. Used for inline contextual actions within press-release text or artist-biography blocks — functionally a styled text link but carrying the button-md uppercase treatment.

### Navigation

**`nav-bar`** — White canvas bar at 60px tall with a 1px hairline border bottom. Main links in `nav-primary` (14px, regular weight) spaced as a flat horizontal list. The gallery name or logo sits far left; city selector and language switcher anchor the right. On active route the link acquires a red underline rule and `{colors.primary}` text. No dropdowns visible on scroll — the bar remains sticky.

**`city-selector`** — A compact inline list of city names (SALZBURG / PARIS / LONDON / SEOUL) in `label-uppercase`, separated by " / " and set in `{colors.muted}`. The current city switches to `{colors.ink}` weight. Functions as both a geographic orientation marker and a navigation filter for exhibitions and events tied to each space.

### Cards

**`exhibition-card`** — No radius, no shadow. A 4:3 image sits above a text block: exhibition title in `title-md`, artist name and date range in `caption-italic` at `{colors.muted}`. Cards sit in a tight grid (typically 3-up on desktop) with consistent `{spacing.md}` gutter. No hover overlay on the image — the whole card becomes a link, underline appearing under the title text only.

**`publication-card`** — Portrait 3:4 image, lighter surface background `{colors.surface-soft}`. Title in `title-sm`, edition/date detail in `caption`. Used in the publications and editions section; the portrait format references book-cover conventions. No border, no shadow, no radius.

**`artist-list-item`** — Artist names displayed as a flat alphabetical list in `nav-artist` (20px, weight 300), each row bordered below by a 1px hairline rule. Hover turns the name to primary red. This list format, rather than a card grid, is intentional: it signals encyclopedic depth and resists hierarchical curation.

### Exhibition & Artwork

**`hero-fullbleed`** — A full-viewport-width, minimum-85vh image block with no overlay scrim. Title text in `display-xl` (72px, weight 300) appears either positioned over the image in white or below it in ink, depending on image luminosity. Caption in `caption` holds artist name, exhibition title, dates. Padding is zero — the image meets the nav-bar edge directly.

**`exhibition-title-block`** — Artist name in `exhibition-title` (28px, weight 300), exhibition subtitle or date range in `body-md` at `{colors.body}`, with `{spacing.sm}` gap between. Used as the opening text block on exhibition detail pages before the main image sequence.

**`artwork-caption`** — Two-line structure: artwork title and date in `caption-italic`, then medium and dimensions on the next line in `caption`. Both lines in `{colors.muted}`. Gap between elements is `{spacing.xs}`. This component is the workhorse of any artwork-listing or installation-view page.

**`press-release-body`** — Long-form text set in `body-md` at 1.65 line height, capped at 720px max-width for readability, text color `{colors.body}` (slightly lighter than full ink). This is the primary reading environment for critical and curatorial prose — no pull-quotes, no callouts, just sustained running text with occasional italic in `caption-italic` for referenced artwork titles.

### Filtering & Search

**`filter-tag`** and **`filter-tag-active`** — Hairline-bordered rectangular chips in `label-uppercase` (10px, 1.8px tracking). Inactive state is muted text on transparent ground; active state inverts to ink background with white text. No radius on either state. Used to filter exhibitions by city, artist, or medium.

**`search-field`** — Full-width text field, no visible border except a 1px ink underline, set in `display-sm` (24px). The oversized type makes partial query text read as a headline during composition. Placeholder "Search" in `{colors.muted}`. Results appear below as plain text rows matching `artist-list-item` style.

### Utility

**`highlight-bar`** — A narrow full-width bar in `{colors.accent-yellow}` (#ffff80) carrying a short label in `label-uppercase` at ink color. Used sparingly — fair announcements, opening-night notices, or site-wide alerts — making it visually jarring in the best gallery-sense of the word.

**`footer`** — Ink-background block with white body text at `body-sm`. Navigation links in white, hover state transitions to `{colors.accent-yellow}` — the only place yellow appears as an interactive signal. City addresses, social links, and legal text in a multi-column layout at `{spacing.section}` vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column exhibition grid; nav collapses to hamburger; hero drops to 100vw × 60vh; `display-xl` scales to 36px; artist list remains full-width flat rows; press-release body fills 100% with `{spacing.base}` side padding |
| Tablet | 744–1128px | Two-column exhibition grid; nav bar retains horizontal links with city selector hidden behind a secondary menu; hero at 75vh; `display-xl` scales to 52px |
| Desktop | 1128–1440px | Three-column exhibition grid; full nav bar with city selector; hero at 85vh minimum; standard type scale active; press-release capped at 720px centered |
| Wide | > 1440px | Grid stays three-column but columns widen; hero image scales to fill; max content width caps at 1440px with auto side margins; no new layout zones introduced |

### Touch Targets

- All artist-list-item rows expand to minimum 48px hit height on touch breakpoints via increased vertical padding
- Filter tags increase to minimum 44px tall on mobile
- Nav links in the collapsed mobile menu rendered at minimum 48px height
- Search field height bumps to 52px on touch to ease tap accuracy

### Collapsing Strategy

- City selector moves from inline nav-bar to a secondary sheet or submenu below the hamburger at tablet and below
- Exhibition grid collapses from 3 → 2 → 1 column at desktop → tablet → mobile breakpoints
- Artwork-caption text remains unchanged across breakpoints (11px is already minimal; no further reduction)
- Footer multi-column layout collapses to a single stacked column on mobile with `{spacing.xxl}` between sections
- `highlight-bar` remains full-width at all breakpoints; font size does not scale

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-active` (#a82720) and `primary-disabled` (#e8a09c) are derived by darkening/lightening the extracted #c52f24; no direct extraction
- `hairline` (#d4d0ce) is interpolated — the extraction captured no explicit border or divider color; a mid-value between `surface-soft` and `muted` was used
- Font weight distribution across Formale-Grotesque variants is inferred from gallery conventions; no weight-specific CSS tokens were captured in extraction
- Whether #ffff80 is a structural brand color or a single-use campaign accent is unclear from extraction alone; it may be seasonal
- No explicit spacing or layout grid values were extracted; all spacing tokens follow an 8px base-unit system by convention
- Icon set and glyph style are unknown — no SVG or icon-font references captured
- Dark-mode or alternate-theme variants not observed in extracted data
- Specific type sizes for mobile breakpoint overrides are inferred; no responsive CSS custom-property values were captured
