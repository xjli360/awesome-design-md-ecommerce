---
version: alpha
name: "Hume Band"
source_url: "https://www.humeband.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric indigo (#4721fb) runs every primary interaction on Hume Band — the buy CTA, the app-sync trigger, the firmware-update pulse — a single vivid voltage against a deep navy (#041d55) foundation that reads as technical authority rather than health-app softness. The palette then branches in two directions: health metrics surface in teal (#00d4b4, #00a896), reading biometric data in the same visual register as medical instrumentation, while activity goals and streaks get the orange signal (#f76a0c), warm and urging against the cooler tones. A bright cyan trace (#34e2e4) appears as data-visualization line color in heart-rate graphs, the kind of oscilloscope aesthetic that positions the band as a precision tool rather than a wellness accessory.

  Typography runs entirely on system font stacks — -apple-system, BlinkMacSystemFont, Segoe UI — keeping the UI feeling native and snappy across iOS and Android companion apps. Weight discipline is tight: display headings at 700, body at 400, with 600 reserved for metric callouts and stat labels where the number itself carries meaning. The monospace stack (Courier New) appears selectively in spec tables, referencing data sheets and technical documentation. No custom display typeface means the brand invests in color and structural rhythm rather than typographic signature.

  Corners are soft but purposeful — {rounded.md} for data cards, {rounded.full} for pill-shaped sync buttons and achievement badges, with harder {rounded.xs} edges on data-dense rows where information density matters. The deep charcoal-teal (#283236) serves as a secondary dark surface, dark enough to make teal and orange pop without reaching full black. Light backgrounds — #edf2f7 as the page canvas, #e7f8f0 for health-positive confirmation states — keep the layout airy despite the data density typical of wearable companion apps.

  Product cards use deep navy (#041d55) as backdrop for hero imagery, letting the watch face become the literal focal point. Orange (#f76a0c) and teal (#00d4b4) re-appear as iconographic fills in the feature grid — activity, sleep, heart rate — giving each pillar a distinct color identity without fragmenting the system. Purple (#7a00df) surfaces as a premium-tier or upgrade signal. This is a palette built for dashboards and data confidence.

colors:
  primary: "#4721fb"
  primary-active: "#3200c8"
  primary-disabled: "#bdb5fd"
  navy: "#041d55"
  navy-mid: "#003388"
  teal: "#00d4b4"
  teal-dark: "#00a896"
  teal-soft: "#e7f8f0"
  orange-accent: "#f76a0c"
  cyan-trace: "#34e2e4"
  purple-premium: "#7a00df"
  ink: "#1a1a1a"
  body: "#283236"
  muted: "#4a5568"
  muted-light: "#555555"
  hairline: "#eeeeee"
  hairline-mid: "#eaeaea"
  canvas: "#edf2f7"
  surface-soft: "#e8edf3"
  surface-dark: "#283236"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  error: "#dc3232"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  metric-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  metric-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "'Courier New', Courier, monospace"
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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 50px
    states:
      hover: backgroundColor "{colors.primary-active}"
      disabled: backgroundColor "{colors.primary-disabled}"

  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 50px

  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 50px

  button-pill:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px

  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    states:
      focus: border "2px solid {colors.primary}"
      error: border "2px solid {colors.error}"

  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logo:
      color: "{colors.navy}"
    cta:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.md}"
      typography: "{typography.button-sm}"

  product-card:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    overflow: hidden
    imageAspect: "1:1"
    contentPadding: "{spacing.lg}"
    badge:
      backgroundColor: "{colors.teal}"
      textColor: "{colors.on-dark}"
      typography: "{typography.metric-label}"
      rounded: "{rounded.full}"
      padding: 4px 10px
    title:
      typography: "{typography.title-md}"
      color: "{colors.on-dark}"
    price:
      typography: "{typography.display-sm}"
      color: "{colors.on-dark}"

  hero-section:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    minHeight: 600px
    padding: "{spacing.section}"
    headline:
      typography: "{typography.display-xl}"
      color: "{colors.on-dark}"
    subheadline:
      typography: "{typography.body-md}"
      color: "{colors.muted-light}"
      maxWidth: 540px
    cta-primary:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.md}"
      typography: "{typography.button-md}"
    cta-secondary:
      backgroundColor: transparent
      textColor: "{colors.teal}"
      border: "1px solid {colors.teal}"
      rounded: "{rounded.md}"
      typography: "{typography.button-md}"
    accentLine:
      color: "{colors.cyan-trace}"

  metric-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"
    borderLeft: "4px solid {colors.teal}"
    metric:
      typography: "{typography.metric-display}"
      color: "{colors.teal}"
    label:
      typography: "{typography.metric-label}"
      color: "{colors.muted}"

  feature-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    iconColorActivity: "{colors.orange-accent}"
    iconColorHealth: "{colors.teal}"
    iconColorSleep: "{colors.primary}"
    title:
      typography: "{typography.title-md}"
      color: "{colors.ink}"
    body:
      typography: "{typography.body-sm}"
      color: "{colors.muted}"

  data-chart:
    backgroundColor: "{colors.surface-dark}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    lineColor: "{colors.cyan-trace}"
    fillTeal: "{colors.teal}"
    fillOrange: "{colors.orange-accent}"
    axisColor: "{colors.muted-light}"
    label:
      typography: "{typography.caption}"
      color: "{colors.muted-light}"
    value:
      typography: "{typography.metric-label}"
      color: "{colors.on-dark}"

  sync-status:
    backgroundColor: "{colors.teal-soft}"
    textColor: "{colors.teal-dark}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    typography: "{typography.caption}"
    border: "1px solid {colors.teal}"
    states:
      syncing:
        backgroundColor: "{colors.surface-soft}"
        textColor: "{colors.muted}"
      error:
        backgroundColor: "#fff0f0"
        textColor: "{colors.error}"

  achievement-badge:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    size: 64px
    border: "3px solid {colors.orange-accent}"
    iconColor: "{colors.orange-accent}"
    caption:
      typography: "{typography.caption}"
      color: "{colors.muted}"

  spec-table:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    rowAlternate: "{colors.canvas}"
    header:
      backgroundColor: "{colors.navy}"
      textColor: "{colors.on-dark}"
      typography: "{typography.metric-label}"
    label:
      typography: "{typography.spec-label}"
      color: "{colors.muted}"
    value:
      typography: "{typography.body-sm}"
      color: "{colors.ink}"

  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} 0"
    logoColor: "{colors.on-dark}"
    divider: "1px solid rgba(255,255,255,0.1)"
    link:
      typography: "{typography.body-sm}"
      color: "{colors.muted-light}"
      hover: color "{colors.teal}"
    copyright:
      typography: "{typography.caption}"
      color: "{colors.muted-light}"

## Components

### Buttons
**`button-primary`** — Electric indigo (#4721fb) background with white text at {typography.button-md} (16px/600). Sits 50px tall with {rounded.md} corners and 14px/28px padding. Hover shifts to primary-active (#3200c8); disabled drops to the washed indigo (#bdb5fd), maintaining shape without inviting click.

**`button-secondary`** — White card surface with a 2px indigo border and indigo text — signals secondary priority without losing the brand color thread. Matches primary dimensions for consistent pairing in hero sections where buy and learn-more CTAs sit side by side.

**`button-navy`** — Deep navy (#041d55) fill for sections where indigo would compete with a dark background, typically hero overlays and dark-band feature rows.

**`button-pill`** — Teal (#00d4b4) pill at {rounded.full} for sync prompts, app-download triggers, and inline feature confirmations. Smaller at button-sm typography, sized for inline placement within cards and stat panels.

### Text Input
**`text-input`** — White card surface with a hairline (#eeeeee) border at rest; focus snaps to a 2px solid indigo ring. At 48px tall with {rounded.sm} corners it targets a comfortable thumb tap. Error state swaps border to error red (#dc3232) with no fill change, keeping the error cue peripheral rather than alarming.

### Navigation
**`nav-bar`** — White bar at 72px tall with a hairline bottom border for structural grounding. Logo in deep navy (#041d55); nav links at {typography.nav-link} 500-weight; the buy CTA is a compact indigo chip at {rounded.md} and button-sm typography — present at all viewport widths.

### Product Card
**`product-card`** — Navy (#041d55) dark-canvas card makes the physical watch photograph the sole focal point. Teal pills in the corner label key differentiators ("7-Day Battery", "ECG") in all-caps {typography.metric-label}. Price reads at display-sm in white against dark, anchoring purchase decision without a separate price section.

### Hero Section
**`hero-section`** — Full-width navy section with display-xl headline in white and subheadline in muted-light (#555555) at max-width 540px for legibility. Two CTAs stack or sit inline: indigo primary, teal-outlined secondary. A cyan trace line (#34e2e4) used as a decorative horizontal rule replicates the oscilloscope-graph aesthetic from the band's health display UI.

### Metric Badge
**`metric-badge`** — White card with a 4px teal left-border as a data-positive stripe. The metric number sits at metric-display (56px/700) in teal, the label in all-caps metric-label in muted gray. Used across "Stats at a Glance" strips to present battery life days, heart-rate accuracy percentage, and daily step counts.

### Feature Card
**`feature-card`** — Soft blue-gray (#e8edf3) cards arranged in a three-column grid. Activity features carry the orange (#f76a0c) icon fill; health/biometric features carry teal (#00d4b4); sleep tracking carries indigo (#4721fb). This three-color icon system creates rapid visual scanning across the feature set without additional label work.

### Data Chart
**`data-chart`** — Dark surface (#283236) panel with cyan trace line (#34e2e4) for heart-rate waveforms, teal bar fills for step and activity data, and orange fills for calorie or goal-completion bars. Axis labels at caption typography in muted-light gray. This component mirrors the band's physical display, bridging physical product and companion app visually.

### Sync Status
**`sync-status`** — A {rounded.full} pill using the teal-soft mint background (#e7f8f0) with teal-dark text (#00a896) for connected/synced state. Transitions to neutral canvas/muted when actively syncing and to light-red/error for connection failures — three states covering all band-connectivity conditions without custom iconography.

### Achievement Badge
**`achievement-badge`** — 64px circle at {rounded.full} in deep navy with a 3px orange ring (#f76a0c). The orange border signals active or unlocked achievement; an outlined (no fill) variant at reduced opacity indicates locked. Caption below uses {typography.caption} in muted gray. Creates a gamification layer within the health-tracking system.

### Spec Table
**`spec-table`** — White surface with alternating canvas (#edf2f7) row shading and a navy header strip. Spec label column uses the monospace stack (Courier New) at spec-label — a deliberate reference to data sheets and technical documentation. Value column in body-sm regular. Table gains horizontal scroll on mobile; the label column is sticky.

### Footer
**`footer`** — Deep navy (#041d55) footer with white logo and muted-light (#555555) link text. Links shift to teal (#00d4b4) on hover. A 10%-opacity white rule divides link column groups. Copyright in caption/muted-light. Mirrors the nav header's navy-to-white logic, bookending the page in the brand's darkest tone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero headline drops to display-md (32px); nav collapses to hamburger, indigo CTA remains visible; product cards stack full-width; metric badges arrange in 2×2 grid; data charts retain horizontal scroll at 280px min-width |
| Tablet | 744–1128px | Two-column feature card grid; nav shows primary links, hides secondary; hero gets 50/50 text–image split; product card grid goes 2-up; spec table retains full layout |
| Desktop | 1128–1440px | Three-column feature grid; full 72px nav bar; hero at 600px min-height with side image bleed; spec table centered at 800px max-width |
| Wide | > 1440px | Content max-width 1280px centered; hero adds edge-to-edge navy bleed; metric badge row expands to 4-up horizontal strip |

### Touch Targets
- All buttons minimum 50px tall, 44px wide
- Nav hamburger icon region minimum 44×44px
- Achievement badges at 64px diameter — tap-accurate on smallest phone sizes
- Sync status pills padded to minimum 36px tall for reliable thumb tap
- Spec table rows minimum 44px tall on mobile for row selection

### Collapsing Strategy
- Desktop nav links collapse to a hamburger drawer at < 744px; indigo CTA chip stays visible at all widths
- Three-column feature grid → two-column at tablet → single-column at mobile
- Metric badge row (4-up wide) → 2×2 at desktop/tablet → vertical stack at mobile
- Data chart does NOT collapse to a narrower format — biometric graphs require minimum 280px width to be readable; chart receives horizontal scroll wrapper on mobile
- Spec table gains horizontal scroll on mobile; label column is position-sticky left
- Footer link columns stack vertically at mobile with section-level spacing between groups

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; all font stacks resolve to system UI (Apple, Segoe, Roboto). A brand-specific geometric sans or humanist sans may load via JavaScript or a CDN bundle not captured in extraction.
- Pure white (#ffffff) does not appear explicitly in the extracted palette — used as surface-card based on assumption; extraction may have filtered it as a framework default.
- Primary color selected as #4721fb (electric indigo) based on distinctiveness heuristic; Hume Band may weight orange (#f76a0c) or teal (#00d4b4) as the hero CTA color — confirm against brand guidelines or live CTA rendering.
- Shadow and elevation tokens (box-shadow values, z-index layers) were not captured; depth layering assumed from standard card patterns for the category.
- Animation and transition timing for sync-status pulse, data-chart line-draw entry, and achievement-badge unlock ring animation are not documented.
- Dark-mode surface palette beyond #283236 and #1a1a1a is unconfirmed; the site may maintain a distinct dark-mode token set not captured in extraction.
- Meta theme-color was absent — unusual for a modern smartwatch brand; may indicate no PWA manifest or the color is set dynamically via JavaScript.
- Purple (#7a00df) appears in the extracted palette but its role (premium tier, legacy UI element, third-party widget) could not be confirmed from extraction alone.
