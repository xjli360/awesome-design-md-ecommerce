---
version: alpha
name: "Kauer Guitars"
source_url: "https://www.kauerguitars.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Boutique handcrafting shows up first in the palette — a wall of near-total ink (#040404, #111111, #1e1e1e) that photographs instruments the way a recording studio frames a performer: total blackout except for the subject. Kauer builds short-run electrics out of Sacramento, and the void-dark canvas makes sunburst finishes and carved tops read as if backlit from within. Against that darkness, #f94877 fires as the single brand voltage — a hot signal pink that carries every primary CTA and active UI state, sharp enough to be unmistakable on any dark surface. The deep navies #112233 and #112255 occupy a transitional register between the void-black backgrounds and the muted grays (#aaaaaa) that carry secondary text, giving the layout layered depth without introducing true chroma. Typography relies entirely on the Arial / Helvetica Neue system stack — no licensed display font, no custom wordmark weight. The instruments carry the visual authority; text exists only to name, price, and direct. Headings land in the 28–36px range at weight 700, body copy at 16px/400, and button labels run in tight uppercase with expanded letter-spacing, a nod to the knurled-knob notation of guitar hardware. Two fluorescent accent tones punctuate the dark stage: lime green (#7dbb00, #84bd00) and orange (#ff6600), appearing to mark availability statuses or category chips — sticker-fluorescent energy that boutique gear shops use to tag "IN STOCK" or short-run windows. `{rounded.xs}` corners suit the machined-metal aesthetic; nothing curves like a consumer marketplace. The extracted palette is diluted by social-share widgets contributing Facebook (#3b5998), Twitter (#55acee), Instagram (#e4405f), LinkedIn (#0976b4), and YouTube (#e52d27) blues and reds — none of those are Kauer brand hues. The true brand signal condenses to dark stage, one pink voltage, and two fluorescent accent tones.

colors:
  primary: "#f94877"
  primary-active: "#cc2127"
  primary-disabled: "#e99292"
  ink: "#222222"
  body: "#272727"
  muted: "#aaaaaa"
  hairline: "#e1e1e1"
  canvas: "#fafafa"
  surface-soft: "#eeeeee"
  surface-card: "#fbfbfb"
  on-primary: "#fafafa"
  dark-bg: "#040404"
  dark-surface: "#1e1e1e"
  dark-mid: "#111111"
  navy: "#112233"
  navy-deep: "#112255"
  accent-green: "#7dbb00"
  accent-green-alt: "#84bd00"
  accent-orange: "#ff6600"
  social-facebook: "#3b5998"
  social-twitter: "#55acee"
  social-instagram: "#e4405f"
  social-youtube: "#e52d27"
  social-linkedin: "#0976b4"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px

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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 42px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.canvas}"
    padding: 11px 23px
    height: 42px
  button-ghost-pink:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 11px 23px
    height: 42px
  text-input:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.navy}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    typography: "{typography.body-md}"
    focusBorderColor: "{colors.primary}"
  search-input:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.navy}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    typography: "{typography.body-md}"
    iconColor: "{colors.muted}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.navy}"
    logoColor: "{colors.canvas}"
    linkHoverColor: "{colors.primary}"
  model-category-tab:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.canvas}"
    activeBorder: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.none}"
  product-card:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.canvas}"
    imageBackground: "{colors.dark-mid}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.canvas}"
    mutedColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  product-gallery:
    backgroundColor: "{colors.dark-mid}"
    thumbnailBorder: "2px solid transparent"
    thumbnailActiveBorder: "2px solid {colors.primary}"
    thumbnailRounded: "{rounded.xs}"
    gap: "{spacing.sm}"
  hero-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    subColor: "{colors.muted}"
    ctaButton: "button-primary"
    overlay: "linear-gradient(to bottom, transparent, {colors.dark-bg})"
    padding: "{spacing.section} {spacing.xl}"
  badge-in-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.dark-bg}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-limited:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.dark-bg}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  social-share-bar:
    gap: "{spacing.sm}"
    iconSize: 32px
    facebook: "{colors.social-facebook}"
    twitter: "{colors.social-twitter}"
    instagram: "{colors.social-instagram}"
    youtube: "{colors.social-youtube}"
    linkedin: "{colors.social-linkedin}"
  footer-dark:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.muted}"
    linkColor: "{colors.canvas}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.navy}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Signal pink (#f94877) CTA with tight uppercase tracking and a flat `{rounded.xs}` corner that reads as machined rather than soft. Hovers to a deeper red-adjacent #cc2127 and disables to muted salmon #e99292. Height locks at 42px with 24px horizontal padding; expands to full width on mobile. The uppercase letter-spacing (1.2px) directly echoes the engraved-knob notation found on guitar control panels.

**`button-secondary`** — Transparent background with a 1px white border and white uppercase label, designed for dark-canvas contexts where a pink fill would compete with instrument photography. Hover state can introduce a white fill with dark text for contrast.

**`button-ghost-pink`** — Pink border and pink text on transparent, used as an alternative secondary CTA when a pure white border reads too close to the page edge. Useful adjacent to hero imagery where the pink fills are already active.

### Inputs

**`text-input`** — Dark-surfaced field (#1e1e1e) with a navy (#112233) border that upgrades to primary pink on focus. Placeholder in #aaaaaa. `{rounded.xs}` corners reinforce the panel-instrument aesthetic. No drop shadows or glow effects — the border color shift is the only focus signal.

**`search-input`** — Same dark field treatment as `text-input` with a leading magnifier icon in muted gray (#aaaaaa). Lives in the navigation bar or a shop filter sidebar. Border upgrades to pink on focus.

### Navigation

**`nav-bar`** — Near-total-black (#040404) bar with a 1px navy (#112233) bottom rule separating it from the hero content below. Logo anchors left in white. Nav links render in 14px/600 with 0.3px tracking; hover state reveals a primary pink underline or color shift. Height 60px. On mobile, secondary links collapse to a hamburger icon while the logo remains visible.

**`model-category-tab`** — Horizontal tab strip used to switch between guitar model families (e.g. Daylighter, Banshee, Super Chief). Inactive tabs render in `{colors.muted}` (#aaaaaa), active tab promotes to `{colors.canvas}` with a 2px pink (#f94877) bottom border. No background fill on any state — the border line is the only indicator.

### Product Display

**`product-card`** — Dark surface (#1e1e1e) card with `{rounded.xs}` corners. Image region sits on #111111 to create a second depth layer. Model name in 15px/600 white, price in 20px/700 white, secondary spec text (wood, pickups, finish) in 14px muted gray. Availability and sale badges anchor to the image top-left corner. Card gap follows `{spacing.sm}` in the grid.

**`product-gallery`** — Full-width primary image on #111111 background with a horizontal thumbnail strip below. Active thumbnail gains a 2px pink (#f94877) border; inactive thumbnails have a transparent border placeholder to prevent layout shift on selection. Gap between thumbnails is `{spacing.sm}`.

**`hero-dark`** — Full-viewport dark scene (#040404) with a bottom-gradient overlay that fades instrument photography into the background color. Heading at 36px/700 in white, sub-copy at 16px/400 in #aaaaaa, one `button-primary` CTA. Vertical padding of `{spacing.section}` (64px) top and bottom. On mobile, heading drops to `{typography.display-md}` (28px).

### Badges

**`badge-in-stock`** — Lime green (#7dbb00) chip with near-black text on `{rounded.xs}`. High-contrast signal for immediate availability; fluorescent against the dark card surface.

**`badge-sale`** — Pink (#f94877) chip with white text; matches the primary brand CTA color for visual urgency. Used on discounted or promotional pricing.

**`badge-limited`** — Orange (#ff6600) chip with near-black text. Short-run inventory or near-sold-out items. All three badge types share the same `{typography.badge}` scale and `{rounded.xs}` corner.

### Social & Footer

**`social-share-bar`** — Row of brand-colored icon buttons at 32px visual size (40px tap target): Facebook #3b5998, Twitter/X #55acee, Instagram #e4405f, LinkedIn #0976b4, YouTube #e52d27. These colors are imported from third-party widget libraries and are not Kauer brand palette entries.

**`footer-dark`** — Near-black (#040404) footer with a 1px navy (#112233) top rule. Columns of links in #aaaaaa that shift to white on hover and to #f94877 on secondary-action hover. `{typography.body-sm}` throughout. `{spacing.xxl}` vertical padding with `{spacing.xl}` horizontal.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero heading drops to display-md (28px); category tabs scroll horizontally with fade-edge indicators |
| Tablet | 744–1128px | Two-column product grid; nav shows primary model links, hamburger for secondary pages; hero retains full-bleed image |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all model categories visible; hero at full display-xl (36px) with copy alongside image |
| Wide | > 1440px | Container max-width ~1400px centered on page; hero image bleeds edge-to-edge behind constrained content; product grid can expand to four columns |

### Touch Targets

- All buttons minimum 42px tall; `button-primary` expands to full-width on mobile viewports
- Nav hamburger icon tap target: 44×44px regardless of visual icon size
- Product card thumbnail strip: minimum 48px height per thumbnail on touch devices
- Social share icons: 40px tap target padded around 32px visual icon
- Category tabs: minimum 44px tap height with horizontal scroll on mobile

### Collapsing Strategy

- Navigation collapses below 744px; logo remains left-anchored, hamburger opens a full-height dark drawer
- Category tab strip becomes horizontally scrollable at < 744px with left/right fade-gradient overflow indicators
- Product gallery thumbnails stack below the primary image on mobile rather than rendering as a side rail
- Badge overlays remain on product card images at all breakpoints, scaling with card width
- Footer columns stack vertically on mobile with `{spacing.xl}` gap between each section

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; the full site likely loads a web font via JS that was not captured — Arial/Helvetica Neue is the fallback only; actual display type may differ
- Exact border-radius values are unconfirmed; `{rounded.xs}` (4px) inferred from boutique instrument brand conventions and the machined-hardware aesthetic
- Social-share widget colors (#3b5998, #55acee, #e4405f, #0976b4, #e52d27) are third-party brand palette entries, not Kauer-owned colors — listed in `colors:` only to support social-share-bar component rendering
- Lime green (#7dbb00, #84bd00) and orange (#ff6600) usage context is inferred as badge/availability indicators; exact placement in the UI is unconfirmed from static extraction
- No meta theme-color provided; #040404 assumed as primary background and mobile browser chrome color
- Animation timing, easing curves, and hover transition durations not extractable from palette/font data
- Precise navigation height, logo dimensions, and grid gutter widths are estimated from genre conventions rather than extracted measurements
- Mobile breakpoints are inferred; actual breakpoints may differ if the site uses a custom grid system
