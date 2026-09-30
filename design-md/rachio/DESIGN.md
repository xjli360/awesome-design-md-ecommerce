---
version: alpha
name: "Rachio"
source_url: "https://www.rachio.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Electric sky-water blue (#21a8ff) placed directly against a near-black teal void (#00202c) — that single pairing carries the brand's core argument before a word is read: smart irrigation is data, not gardening. Rachio's primary typeface is Figtree, a geometric sans with softened terminals that reads simultaneously as approachable consumer product and credible hardware interface; at weight 700 it anchors display headlines without going severe, and at 400 it handles long-form feature copy without fatigue. The palette is unusually broad for a consumer hardware brand — thirty extracted colors moving from the electric primary through two greens (#45c371 garden-fresh, #2b5232 deep-forest), a full register of earth tones (#dfad72 amber, #c76928 rust, #d1bbb0 warm sand), and several blue-grays (#334d5a, #b4c3c9, #6e94b1) that shift with surface depth. Rather than fight this breadth the system organizes it as biomes: water-blue (#21a8ff) governs all interactive states, greens carry lawn-health and savings metrics, earth tones ground outdoor photography and seasonal context badges.

  Card corners land at `{rounded.md}` (12px) — soft enough to read as consumer product without losing the precision a connected hardware device demands. Buttons use `{rounded.sm}` (8px), not pill-shaped and not rectangular, occupying the middle zone between smart-home warmth and tech authority. The primary CTA in #21a8ff hits loud against dark-canvas hero sections built on #00202c, a water-on-night-sky contrast that is literal and brand-appropriate at once. Navigation stays low in visual mass: a white bar with muted gray labels and a single high-contrast action. Product cards clip device photography against clean white canvas, letting industrial design breathe. Zone and schedule status chips use the green palette (#45c371, #8ea153) — green means active, on-schedule, thriving — while alert and warning states pull from the amber-rust register (#dfad72, #c76928). The result is a smart-home interface that knows it lives outdoors, where the lawn is the product's live performance dashboard.

colors:
  primary: "#21a8ff"
  primary-active: "#0090e8"
  primary-disabled: "#a8d8ff"
  ink: "#00202c"
  body: "#334d5a"
  muted: "#6b7280"
  hairline: "#b4c3c9"
  canvas: "#ffffff"
  surface-soft: "#f0f4f6"
  surface-card: "#ffffff"
  surface-dark: "#00202c"
  surface-mid: "#0c2738"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  green: "#45c371"
  green-deep: "#2b5232"
  green-dark: "#133008"
  green-mid: "#8ea153"
  green-sage: "#c7ccb0"
  earth-amber: "#dfad72"
  rust: "#c76928"
  sand: "#d1bbb0"
  olive: "#6b6c13"
  blue-steel: "#6e94b1"
  hairline-dark: "#30464b"

typography:
  display-xl:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  label:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  stat-display:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  button-md:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Figtree Fallback', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
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
    rounded: "{rounded.sm}"
    padding: 13px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "1.5px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 48px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 9px 18px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    ctaButton: "{components.button-primary}"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
    minHeight: 560px
    paddingVertical: "{spacing.section}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    shadowColor: "rgba(0,32,44,0.10)"
    shadowBlur: 16px
    imageBackground: "{colors.surface-soft}"
    nameTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    badgeRounded: "{rounded.xs}"
    badgeBackground: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.label}"
  zone-chip-active:
    backgroundColor: "{colors.green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  zone-chip-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  device-stat-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    numberTypography: "{typography.stat-display}"
    numberColor: "{colors.primary}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    padding: "{spacing.lg}"
  savings-badge:
    backgroundColor: "{colors.green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: 5px 12px
  schedule-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    accentColor: "{colors.primary}"
    activeIndicatorColor: "{colors.green}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 14px 16px
    borderLeft: "3px solid {colors.primary}"
  feature-flag-badge:
    backgroundColor: "{colors.earth-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  alert-banner:
    backgroundColor: "{colors.rust}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  dark-section:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.green}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.blue-steel}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    dividerColor: "{colors.hairline-dark}"
    padding: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — The primary CTA fills with Rachio blue (#21a8ff) on an 8px-rounded 48px-tall pill using Figtree 600. On `:hover` it darkens to `button-primary-active` (#0090e8); disabled state washes to #a8d8ff with white text that still meets contrast minimums. Used for all hero CTAs, add-to-cart, and checkout confirmation actions.

**`button-secondary`** — White fill with a 1.5px blue border and blue label; mirrors primary dimensions exactly so button pairs align without height jitter. On hover the border brightens by matching `primary-active`. Used on product comparison rows and secondary feature CTAs alongside a dark hero CTA.

**`button-ghost`** — Transparent fill with a 1.5px white border; lives exclusively inside dark-canvas (`surface-dark`, `surface-mid`) hero and banner sections where the blue primary CTA sits alongside a softer secondary action such as "Learn More" or "Watch Video."

**`button-sm`** — 36px-tall compact variant in Rachio blue for in-card or in-table actions — "Shop Now", "Add Zone", "View Schedule" — where full-size buttons would overwhelm the surrounding density.

### Inputs

**`text-input`** — White fill, 1px hairline border (#b4c3c9) at rest, transitions to a 2px primary-blue border on focus with no color change to the label. Figtree 16px Regular placeholder fades to #6b7280. Height 48px matches button height for inline form rows such as the email signup in the footer.

### Navigation

**`nav-bar`** — 64px white bar with a 1px hairline bottom border. Links render in Figtree 500 15px using ink (#00202c). The brand mark sits far left; the primary CTA button (`button-primary`) anchors the far right. On scroll the bar may receive a soft drop shadow. Mobile collapses behind a hamburger icon that opens a full-height drawer.

### Product & Device Cards

**`product-card`** — White card at `rounded.md` (12px) with a 10% ink shadow at 16px blur. Device photography sits on a `surface-soft` (#f0f4f6) background panel in the upper half; pricing and name render below in `title-md` and `title-sm`. Badges float top-left with `label` typography in uppercase, filled with Rachio primary for new products or `earth-amber` for seasonal models. Add-to-cart uses a full-width `button-primary` at card base.

**`device-stat-card`** — A data-display tile used in app-integration and features sections. The large metric (gallons saved, zones watered, scheduling efficiency) renders in `stat-display` (40px 700) in primary blue. A two-line caption in `caption` and `muted` sits below. The card sits on white with a `hairline` border and `rounded.md` corners; at 2×2 grid on desktop, these tiles visualize the brand's core ROI promise.

### Zoning & Scheduling UI

**`zone-chip-active`** — Full-radius pill (#45c371 green fill, white Figtree caption) indicating a currently running or scheduled zone. The green maps directly to the lawn-health visual language established in photography.

**`zone-chip-inactive`** — Same geometry but `surface-soft` fill with `muted` text; used for zones not in the current schedule window. Together the two chip states give the app UI a scannable at-a-glance zone map.

**`schedule-row`** — A list-item component for displaying irrigation schedule entries: `surface-soft` background at `rounded.sm`, a 3px left accent bar in `primary` blue, schedule name in `body-sm`, and time label in `caption` with `muted` text. Active schedules show a `zone-chip-active` inline; paused schedules show `zone-chip-inactive`.

### Badges & Labels

**`savings-badge`** — Green full-radius pill with uppercase `label` typography in white; used on hero sections and product cards to surface gallons-saved or cost-reduction claims. Reads as a certification mark rather than a promotional sticker.

**`feature-flag-badge`** — Earth-amber (#dfad72) flat rectangle at `rounded.xs` with ink-colored `label` uppercase text; applied to new features, bundle inclusions, or seasonal product variants. The warm amber avoids the urgency of red while still drawing the eye.

**`alert-banner`** — Rust (#c76928) inline banner at `rounded.sm` for watering restrictions, offline device warnings, or weather-hold notifications. Full-width on mobile; inline within the content column on desktop.

### Sections

**`hero-dark`** — Full-bleed section on `surface-dark` (#00202c) with a minimum height of 560px. Heading in `display-xl` white, subhead in `body-md` at `on-dark`, followed by a `button-primary` (blue) and a `button-ghost` (white outline) CTA pair. Photography or device render overlaps on the right half at desktop width.

**`dark-section`** — Mid-page alternating dark panel on `surface-mid` (#0c2738); slightly lighter than the hero to create visible rhythm on long scroll pages. Heading in `display-md`, accent metrics in `green`, body in `on-dark`.

**`footer`** — Four-column link grid on `ink` (#00202c) background. Column headings in `title-sm` white; links in `body-sm` at `blue-steel` (#6e94b1) with primary-blue hover. A `hairline-dark` (#30464b) rule separates the link grid from the legal/social row below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger drawer; hero stacks copy above device image; product cards go full-width; stat cards 1×2 grid; zone chips wrap horizontally |
| Tablet | 744–1128px | Two-column product grid; hero shows side-by-side at reduced image size; nav abbreviates to icon+label for secondary links; stat cards 2×2 grid |
| Desktop | 1128–1440px | Three-column product grid; full hero split layout; five-link nav visible; stat tiles at 4-up row |
| Wide | > 1440px | Max content width 1320px centered; hero image scales up; footer shifts to 5-column grid; generous lateral whitespace at `spacing.section` each side |

### Touch Targets

- All buttons minimum 48px tall with 44px minimum tap width
- Zone chips minimum 36px tall with 12px horizontal padding — enlarge on mobile to 40px
- Nav hamburger icon minimum 44×44px tap area
- Schedule rows minimum 56px tall on mobile for reliable thumb tap
- Form inputs minimum 48px tall; labels always visible above field (no floating-label collapse on mobile)

### Collapsing Strategy

- Primary nav collapses: links → hamburger drawer at < 744px; "Shop" CTA button persists in the bar at all breakpoints
- Hero layout: side-by-side → stacked (copy above, image below) at < 1128px
- Product grid: 3 col → 2 col at 744px → 1 col at < 520px
- Stat card grid: 4-up row → 2×2 → 1-up stack
- Footer: 4-col → 2-col → 1-col stacked with accordion-style link sections on mobile
- Zone chip rows: horizontal scroll container on mobile rather than wrapping to multi-row

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; mobile browser chrome color is unverified — defaulting to `surface-dark` (#00202c) as the likely candidate
- Exact nav height and scroll-sticky behavior could not be confirmed from static extraction; 64px is an estimate
- Shopify theme-layer typography scale (fluid clamp sizes) not extractable — fixed px values used throughout; implement clamp() scaling for display sizes in production
- Specific icon library or illustration system not identified; Rachio may use a proprietary device + nature icon set not accessible via static scrape
- Animation and transition timings (sprinkler-sweep loaders, schedule timeline animations) not captured — no motion tokens defined
- Dark-mode color mapping not confirmed; the extracted palette suggests dark-mode support is plausible but no `prefers-color-scheme` tokens are defined here
- App-store screenshot UI (zone map, watering history charts) uses a separate design system not reflected in the marketing site extraction
