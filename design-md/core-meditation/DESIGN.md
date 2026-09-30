---
version: alpha
name: "Core Meditation"
source_url: "https://www.hellocore.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Where most wellness apps crowd their surfaces with aspirational photography and gradient overlays, Core earns attention by subtraction — a near-black canvas (#0E0D0C) that reads less like a background and more like the moment just before a session begins. The brand's warmth arrives through a single amber-gold primary (#C49A5E) that appears as the active ring on the meditation timer, the progress glow, and the primary CTA — a deliberate focal restriction that makes each appearance feel like a signal rather than decoration. Surface layers step up in very small increments (from #0E0D0C through #1B1815 to #26211D) so the UI feels dimensioned without feeling cluttered; the eye rests rather than scans. Typography leans on a clean geometric sans — likely Inter or a close kin — set at modest weights: display copy sits at 28–32px in weight 300–400 rather than the bold-heavy registers that gyms and performance brands use. This lightness is a design argument: meditation practice does not shout. Body copy in warm cream (#F0E8DC) on the dark canvas achieves its contrast through temperature rather than stark black-on-white flip, preserving the sense of a candlelit room. Rounded corners use a gentle `{rounded.md}` (12px) on cards and inputs — soft enough to feel approachable, firm enough to avoid the bubbly excess of consumer wellness competitors. Breathing room is the true primary ingredient: `{spacing.section}` (64px) vertical gaps between feature rows signal that each practice area deserves uninterrupted space. The brand's restraint extends to interactive states — hover and active treatments shift luminance rather than hue, so the amber never becomes aggressive. A `{rounded.full}` pill shape on the session-launch button recalls the circular timer UI and creates visual continuity between the marketing surface and the in-app experience. All of this points to a product designed first for the moment the screen goes quiet.

colors:
  primary: "#C49A5E"
  primary-active: "#A87D42"
  primary-disabled: "#6B5535"
  primary-glow: "#C49A5E33"
  ink: "#F0E8DC"
  body: "#C8BFB3"
  muted: "#8A8078"
  hairline: "#2E2925"
  hairline-soft: "#231F1C"
  canvas: "#0E0D0C"
  surface-soft: "#1B1815"
  surface-card: "#26211D"
  surface-elevated: "#302B26"
  on-primary: "#0E0D0C"
  on-dark: "#F0E8DC"
  success: "#6BAF85"
  error: "#C46A5E"
  streak-amber: "#E8B86A"

typography:
  display-xl:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.1px
  caption-upper:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  timer-display:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 56px
    fontWeight: 200
    lineHeight: 1.0
    letterSpacing: -1px
  button-md:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-label:
    fontFamily: "'Inter', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 13px 31px
    height: 52px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: 14px 16px
    height: 52px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.nav-label}"
    borderTop: "1px solid {colors.hairline-soft}"
    height: 56px
    iconSize: 24px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.section}"
    paddingX: "{spacing.xl}"
    ctaLayout: centered
  session-timer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    timerTypography: "{typography.timer-display}"
    ringColor: "{colors.primary}"
    ringGlowColor: "{colors.primary-glow}"
    ringWidth: 3px
    ringSize: 240px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    subtitleColor: "{colors.body}"
    typography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageAspectRatio: 16/9
    border: "1px solid {colors.hairline-soft}"
  practice-category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  streak-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.streak-amber}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    border: "1px solid {colors.hairline}"
  section-label:
    textColor: "{colors.muted}"
    typography: "{typography.caption-upper}"
    paddingBottom: "{spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  feature-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.xl}"
    gap: "{spacing.xl}"
  progress-bar:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.primary}"
    height: 2px
    rounded: "{rounded.full}"
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    quoteTypography: "{typography.body-md}"
    authorTypography: "{typography.caption}"
    authorColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline-soft}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    linkColor: "{colors.body}"
    typography: "{typography.body-sm}"
    paddingY: "{spacing.section}"
    borderTop: "1px solid {colors.hairline}"

## Components

### Buttons
**`button-primary`** — A warm amber-gold pill (`{rounded.full}`) at 52px height, carrying `{colors.primary}` fill with near-black `{colors.on-primary}` text for contrast. The full pill shape deliberately echoes the circular timer ring in the product, creating a through-line between marketing and session UI. Active state drops to `{colors.primary-active}` (#A87D42) without any scale transform — the response is luminance-only, not theatrical. Disabled state uses `{colors.primary-disabled}` with `{colors.muted}` text to communicate unavailability without a jarring contrast shift against the dark canvas.

**`button-secondary`** — Transparent background with a `{colors.hairline}` 1px border at `{rounded.full}`, matching pill geometry. Paired in layouts with `button-primary` for subscribe/learn-more splits, the outline variant recedes visually so the amber CTA remains the single bright object. Hover state brightens border to `{colors.body}`.

**`button-ghost`** — No border, no background. Used for navigation-level actions (skip, dismiss, close) where adding visual weight would compete with the session content. Text in `{colors.body}` rather than full `{colors.ink}` so it reads as secondary without being invisible.

### Text Input
**`text-input`** — Dark `{colors.surface-card}` fill distinguishes the field from the `{colors.canvas}` page background while preserving the dark-mode continuity. A `{colors.hairline}` border at rest steps up to `{colors.primary}` on focus — the amber accent appearing only when the user is actively engaged mirrors how the timer ring activates at session start. Placeholder text in `{colors.muted}` (#8A8078) sits comfortably readable without suggesting pre-filled content.

### Navigation
**`nav-bar`** — Bottom tab bar for mobile, 56px tall with 24px icons. Inactive tabs render in `{colors.muted}`; active tab icon and label shift to `{colors.primary}`. A 1px `{colors.hairline-soft}` top rule separates bar from content without adding visual mass. Desktop expands to a top nav with the same muted/amber active state logic applied to horizontal text links.

**`section-label`** — Uppercase caption (`{typography.caption-upper}`) in `{colors.muted}` with a `{colors.hairline-soft}` bottom rule. Used above content grid sections (Today, Featured, New Releases) as the structural skeleton of the browse surface. Small letterSpacing of 0.8px gives legibility to the all-caps treatment without aggressive tracking.

### Product & Content Cards
**`product-card`** — `{colors.surface-card}` (#26211D) with a `{colors.hairline-soft}` 1px border and `{rounded.md}` (12px) corners. Images appear at 16:9 with no rounded clipping — the card border provides the shape. Title in `{colors.ink}` (warm cream) at `{typography.title-sm}` weight 500; subtitle/category label in `{colors.body}` (#C8BFB3) at `{typography.caption}`. Duration or difficulty metadata renders in `{typography.caption-upper}` with `{colors.muted}`. Card hover lifts to `{colors.surface-elevated}` background.

**`practice-category-chip`** — Horizontal scroll row of filter pills. Default state uses `{colors.surface-soft}` fill with `{colors.body}` text at `{typography.button-sm}`. Selected chip switches to `{colors.primary}` fill with `{colors.on-primary}` text — the only full amber-saturated UI element outside the primary CTA and timer ring, so the selection reads immediately.

### Session & Progress UI
**`session-timer`** — Full-bleed dark canvas with a 240px circular ring in `{colors.primary}` at 3px width. A radial glow using `{colors.primary-glow}` (amber at 20% opacity) creates soft luminance behind the ring without hard edges. The countdown renders in `{typography.timer-display}` (56px, weight 200) — the extreme thinness at large size embodies the idea that time opens rather than closes.

**`progress-bar`** — 2px track in `{colors.hairline}`, amber fill in `{colors.primary}`, `{rounded.full}` caps. Used inline on cards to show session completion percentage and within streaks UI. The minimal height keeps the indicator purely informational.

**`streak-badge`** — Small rectangular label with `{rounded.xs}` rounding and `{colors.surface-card}` fill. Text in `{colors.streak-amber}` at `{typography.caption-upper}` — a slightly brighter amber than the primary to feel celebratory. Appears on profile and home surfaces next to consecutive-day counts.

### Marketing & Structure
**`hero-section`** — Centered layout on `{colors.canvas}` with heading at `{typography.display-xl}` (weight 300, −0.5px tracking) and body copy at `{typography.body-md}` in `{colors.body}`. `{spacing.section}` (64px) vertical padding gives the hero breathing room that matches the app's own quiet aesthetic. Primary CTA sits centered below body copy; a ghost secondary option appears for users already subscribed.

**`feature-row`** — Alternating left/right image+text pairs in `{colors.surface-soft}` rounded containers (`{rounded.lg}`) with `{spacing.xxl}` (48px) internal padding. Heading at `{typography.display-sm}`, body at `{typography.body-md}` in `{colors.body}`. Dark-toned background containers differentiate these from the base canvas without requiring card borders.

**`testimonial-card`** — `{colors.surface-card}` fill, `{rounded.md}` corners, `{spacing.xl}` padding. Quote text at `{typography.body-md}` in `{colors.body}` for a soft, not-quite-full-contrast read; attribution in `{typography.caption}` at `{colors.muted}`. No quotation mark glyph decoration — the indentation and font treatment carry the context.

**`footer`** — `{colors.surface-soft}` background with `{colors.hairline}` top border, `{spacing.section}` vertical padding. All link text in `{colors.body}` at `{typography.body-sm}`; legal copy in `{colors.muted}`. No accent color appears in the footer — the amber is reserved for action states only.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; bottom tab nav at 56px; hero heading drops to `{typography.display-md}`; session timer scales to 200px ring; product cards in full-width vertical scroll |
| Tablet | 744–1128px | Two-column product grid; bottom nav retained; hero heading at `{typography.display-md}`; feature rows stack vertically; hero CTA remains centered |
| Desktop | 1128–1440px | Top horizontal nav replaces bottom tabs; three-column product grid; feature rows switch to horizontal image+text layout; hero heading at full `{typography.display-xl}` |
| Wide | > 1440px | Max content width caps at 1280px, centered with auto side margins; no additional layout changes; hero image treatment may expand to full-bleed behind text column |

### Touch Targets
- All interactive tap targets maintain a minimum 44×44px hit area regardless of visible element size
- Bottom nav icons padded to 48px tap height with `{spacing.sm}` gap between adjacent targets
- Category filter chips set to minimum 36px height with `{spacing.xs}` horizontal gap in scroll row
- Timer ring pause/play center tap zone: minimum 64px diameter

### Collapsing Strategy
- Desktop top nav collapses to hamburger at < 744px; primary CTA button persists in collapsed nav header
- Feature row images collapse below text at tablet and stack fully at mobile
- Footer multi-column link grid collapses to single stacked column at mobile; legal row always full-width single line
- Testimonial cards collapse from three-up grid to single-column vertical scroll at mobile with horizontal swipe affordance

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All colors are inferred from brand knowledge** — the live site returned zero extracted hex values; no colors were scraped. Every hex in this file is an approximation based on the brand's known dark-mode, warm-neutral aesthetic and should be verified against the live product before implementation.
- **Typography is unconfirmed** — no font-family stacks were extracted. The Inter assignment is a best-inference for the brand's geometric-humanist aesthetic; the actual font stack (possibly a custom or licensed face) should be inspected via browser DevTools on the live site.
- **Font weights and sizes are approximate** — with no CSS extraction, all `fontSize` and `fontWeight` values are editorial estimates calibrated to the brand's quiet, low-contrast register.
- **Dark-mode-first assumption** — Core is primarily an app experience; the web marketing surface may use a lighter canvas variant not accounted for here.
- **No theme-color meta extracted** — confirms JS-rendered or anti-bot-protected page; a live browser inspection session is required to recover true design tokens.
- **Component inventory is inferred** — specific components (streak-badge geometry, timer ring spec) are based on known app UI patterns rather than extracted DOM measurements.
