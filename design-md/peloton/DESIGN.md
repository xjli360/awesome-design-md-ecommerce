---
version: alpha
name: "Peloton"
source_url: "https://www.onepeloton.com"
captured_at: "2026-09-28T04:10:53.896515+00:00"
evidence_status: "historical_partial_css_evidence"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A dark, high-contrast fitness ecosystem built on a near-black canvas (#181a1d) and a single red voltage (#df1c2f) that fires across every primary CTA, leaderboard metric, and live-class indicator. The brand treats black as its signature — not as a background default but as an intentional stage for motion, data, and the glow of instructor faces. Inter runs at clean, utilitarian weights (400–600) with generous tracking on body copy, while brandon-grotesque appears in hero headlines and marketing lockups, lending a geometric, athletic warmth. The extracted palette reveals a system built for legibility under gym lighting: high-contrast grays (#65666a, #888b93) for secondary text and muted UI, a cool blue (#84b6e1) for linked content and informational badges, and a soft off-white (#f5f7f9) for surface cards that sit on the dark canvas. Red appears in two distinct strengths — the primary action red (#df1c2f) and a deeper, hover-weight red (#d00c2a) — suggesting a two-state button system without opacity tricks. The meta theme-color of #000000 confirms the brand commits to full black in browser chrome, a rare and intentional choice. Rounded corners are restrained: buttons and inputs use {rounded.sm} (8px), cards use {rounded.md} (12px), and only the profile avatar and live-class thumbnail use {rounded.full}. The overall mood is premium, focused, and slightly theatrical — a dark room where the only thing that matters is the workout.

colors:
  primary: "#df1c2f"
  primary-active: "#d00c2a"
  primary-disabled: "#f5a0a8"
  ink: "#181a1d"
  body: "#222529"
  muted: "#65666a"
  muted-soft: "#888b93"
  hairline: "#e4e6e7"
  hairline-soft: "#f5f7f9"
  canvas: "#ffffff"
  surface-soft: "#f5f7f9"
  surface-card: "#ffffff"
  surface-dark: "#181a1d"
  surface-dark-card: "#222529"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#84b6e1"
  link-active: "#5a9bd5"
  success: "#07bc0c"
  warning: "#f1c40f"
  error: "#e74c3c"
  leaderboard-red: "#df1c2f"
  leaderboard-green: "#4cd964"
  leaderboard-blue: "#3498db"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'brandon-grotesque', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'brandon-grotesque', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'brandon-grotesque', Inter, -apple-system, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.25px
  caption-sm:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.25px
  badge:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.25px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: 2px solid "{colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: 2px solid "{colors.ink}"
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-pill-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  icon-button-circle:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  icon-button-dark:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  top-nav-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    borderBottom: 2px solid "{colors.primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-dark:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.muted}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-dark:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.md}"
    aspectRatio: 4/3
  leaderboard-row:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  leaderboard-row-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  metric-badge:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  metric-badge-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  live-class-thumbnail:
    rounded: "{rounded.full}"
    height: 48px
    width: 48px
  class-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  class-card-dark:
    backgroundColor: "{colors.surface-dark-card}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 6px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 6px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.on-dark}"

## Components

### Buttons
**`button-primary`** — The primary action button across the Peloton ecosystem, used for "Start Your Free Trial", "Join Class", and "Add to Cart". Rendered in the signature red (#df1c2f) with white text and an 8px rounded corner. On hover, shifts to the deeper red (#d00c2a). When disabled, fades to a soft pink (#f5a0a8) with white text, signaling unavailability without visual noise. Height is 44px with 12px/24px padding, using Inter 600 at 15px with 0.25px tracking for a clean, athletic read.

**`button-secondary`** — Outlined button for secondary actions like "View Details" or "Compare Models". Uses a transparent background with a 2px hairline border (#e4e6e7) and ink text (#181a1d). On active state, the border deepens to full ink and the background takes a soft surface tint (#f5f7f9). Same 44px height and typography as primary for visual alignment.

**`button-dark`** — Used on dark canvas sections (footer, dark mode product pages). Identical dimensions to `button-primary` but with a near-black background (#181a1d) and white text. Appears in the bottom nav of the Peloton app and on the Bike/Tread product detail pages where the hero section is full-bleed dark.

**`button-pill-red`** — A compact, fully rounded pill for inline actions like "Join Now" on class cards or "Live" badges. Uses the primary red with white text, 36px height, and 8px/20px padding. Typography is `button-sm` (13px, 600 weight) for tighter spacing in card layouts.

### Cards
**`product-card`** — The standard product card for hardware (Bike, Tread, Row) on a white canvas. Features a 4:3 image area with 12px rounded corners, 16px padding, and body-sm typography for descriptions. Price and CTA sit at the bottom with consistent 16px spacing. The dark variant (`product-card-dark`) uses the dark surface card color (#222529) for the Peloton app's dark mode and the "Shop" section on dark backgrounds.

**`class-card`** — Used in the class library and schedule views. Smaller than product cards, with a thumbnail, class title, instructor name, duration, and difficulty badge. The dark variant appears in the app's dark mode. Both use 12px rounded corners and body-sm for metadata.

**`live-class-thumbnail`** — A fully circular thumbnail (48px) for instructor avatars in live class listings. The `{rounded.full}` value creates the perfect circle, and the image is cropped to a 1:1 aspect ratio.

### Navigation
**`top-nav`** — The primary navigation bar at 64px height on white canvas. Uses uppercase nav-link typography (Inter 600, 14px, 0.25px tracking) for a clean, athletic feel. The active state has a 2px red bottom border and red text. The dark variant (`top-nav-dark`) appears on the app's dark mode and marketing pages with full-bleed black headers.

**`nav-link-active`** and **`nav-link-inactive`** — Active links use primary red (#df1c2f) with a 2px bottom border; inactive links use muted gray (#65666a). Both use the same typography for consistent alignment.

### Forms
**`text-input`** — Standard text input for forms (login, signup, shipping). 48px height with 12px/16px padding, 1px hairline border, and 8px rounded corners. On focus, the border becomes 2px solid primary red. The dark variant (`text-input-dark`) uses the dark surface card background (#222529) with white text and a muted border (#65666a) for dark mode forms.

**`select-input`** — Dropdown select matching the text input dimensions and styling. Uses the same 48px height, 8px rounded corners, and hairline border.

### Data Display
**`leaderboard-row`** — Used in the live class leaderboard to display member rankings. Standard rows use a soft surface background (#f5f7f9) with ink text. The active row (the current user) uses the primary red background with white text, creating a clear visual anchor in the scrolling list.

**`metric-badge`** — Small data badges for workout metrics (output, resistance, cadence). Uses dark surface card background (#222529) with white text, 4px rounded corners, and uppercase badge typography (11px, 600 weight, 0.5px tracking). The red variant (`metric-badge-red`) uses the primary red for live metrics or personal best indicators.

**`progress-bar`** and **`progress-bar-fill`** — Used for class progress, workout completion, and achievement tracking. The track is a 6px tall pill shape in hairline gray (#e4e6e7), and the fill is the primary red. The full rounded value creates the pill shape.

### Footer
**`footer`** — The site footer uses the dark surface background (#181a1d) with white text and 48px vertical padding. Footer links use the muted-soft gray (#888b93) and shift to white on hover. The footer contains four columns: Products, About, Community, and Support, each with a title and link list.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack vertically; class cards show 1 per row; leaderboard hides member names, shows only rank and output; footer collapses to accordion sections |
| Tablet | 744–1128px | Two-column product grid; class cards show 2 per row; top-nav shows 4-5 links; leaderboard shows rank, name, and output; footer shows 2-column grid |
| Desktop | 1128–1440px | Three-column product grid; class cards show 3-4 per row; full top-nav with all links; leaderboard shows all columns; footer shows 4-column grid |
| Wide | > 1440px | Max-width container at 1440px; product grid can show 4 columns; class cards show 4-5 per row; leaderboard expands to show additional metrics |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height (Apple HIG compliant)
- Icon buttons are 40px circles with 40px touch targets
- Product card CTAs are 44px tall for easy tapping
- Leaderboard rows are 44px tall minimum
- Navigation links have 44px tap areas even when text is smaller

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product comparison table collapses to stacked cards on mobile
- Class filter bar collapses to a single "Filter" button with modal overlay
- Footer link columns collapse to accordion sections on mobile
- Leaderboard collapses to essential columns (rank, output) on mobile, with expandable row details

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- The extracted color list is heavily polluted with framework defaults (Shopify checkout colors, notification toast colors, social media brand colors). The true brand palette likely has fewer than 10 colors, but the extraction returned 30+. The primary red (#df1c2f) and near-black (#181a1d) are the most distinctive and likely correct; the blues (#3498db, #5ac8fa, #007aff) are almost certainly iOS/Shopify defaults and should be used with caution.
- Font sizes and line heights are estimated from common patterns for Inter and brandon-grotesque; exact values from the live site's CSS were not extracted.
- Hover states for secondary buttons, text inputs, and links are inferred from common patterns; exact colors may differ.
- Error states for form inputs (red border, error message styling) were not extracted.
- Dark mode colors for the app are inferred from the dark surface colors in the palette; the exact dark mode palette may have additional tokens.
- The leaderboard and metric badge components are based on the Peloton app's known UI; the web version may differ.
- Animation timing and easing curves were not extracted.
- The brandon-grotesque font may be used only in marketing hero sections, not in the app UI; Inter appears to be the primary UI font.
- The extracted font stack includes "inherit" and "sans-serif !important", suggesting some inline styles override the system; the exact cascade is unclear.
