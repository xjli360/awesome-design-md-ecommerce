---
version: alpha
name: "Hydrow"
source_url: "https://hydrow.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dark, immersive fitness canvas where #000 sets the stage and #0070f3 — a precise, electric blue — becomes the single point of focus, the only color that breaks the void. This is not a cheerful gym brand; it's a performance interface for rowing, where every pixel serves the athlete's flow state. The blue appears in primary CTAs, progress indicators, and the subtle glow of the start button, never overwhelming but always purposeful. Typography runs system-native (-apple-system, Segoe UI, sans-serif) at moderate weights — no custom display face, no decorative flourishes, just clean hierarchy that gets out of the way. Cards and buttons use tight radii ({rounded.sm} at 8px), avoiding the pill-shaped friendliness of consumer marketplaces; this is a tool, not a toy. The secondary accent #3291ff provides hover states and link underlines, a lighter sibling that adds dimension without competing. White text on dark backgrounds carries all primary messaging, with muted grays for secondary info. The overall effect is one of controlled intensity — a cockpit for the body, not a social feed.

colors:
  primary: "#0070f3"
  primary-active: "#3291ff"
  primary-disabled: "#003380"
  ink: "#ffffff"
  body: "#e0e0e0"
  muted: "#888888"
  muted-soft: "#555555"
  hairline: "#333333"
  hairline-soft: "#1a1a1a"
  canvas: "#000000"
  surface-soft: "#111111"
  surface-card: "#1a1a1a"
  on-primary: "#ffffff"
  error: "#ff3333"
  success: "#00cc66"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  metric-display:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  metric-value:
    typography: "{typography.display-lg}"
    textColor: "{colors.primary}"
  metric-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  progress-bar-track:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    border: "1px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.body}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  workout-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline}"
  workout-card-active:
    border: "1px solid {colors.primary}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with {colors.primary} blue on a dark canvas. Used for "Start Workout", "Subscribe", and "Get Started" actions. On hover, shifts to {colors.primary-active} (#3291ff) for a brightening effect. Disabled state uses {colors.primary-disabled} (#003380) with muted text, signaling the action is unavailable without confusion.

**`button-secondary`** — An outlined button on {colors.surface-card} background with a {colors.hairline} border. Used for "Learn More" and secondary navigation paths. Active state fills to {colors.surface-soft}. Maintains the same 48px height and {rounded.sm} corners as the primary button for consistent rhythm.

**`button-ghost`** — A text-only button with no background or border. Used for "Cancel", "Skip", and inline actions within cards. Relies on {colors.ink} white text and the same {typography.button-md} sizing for alignment with other button variants.

### Navigation
**`nav-bar`** — A fixed 64px bar on pure black {colors.canvas} with a subtle {colors.hairline} bottom border. Navigation links use uppercase {typography.nav-link} at 14px with 0.5px letter-spacing for a technical, performance-oriented feel. Active links glow {colors.primary}, inactive links sit at {colors.muted} gray.

**`nav-link-active`** / **`nav-link-inactive`** — Active links inherit the brand blue; inactive links fade to muted gray. No background fill or underline — the color shift alone signals state, keeping the interface clean and minimal.

### Cards
**`product-card`** — A dark card on {colors.surface-card} (#1a1a1a) with {rounded.sm} corners. Used for rower product displays, pricing tiers, and feature highlights. On hover, the card shifts to {colors.surface-soft} and gains a hairline border for depth without breaking the dark theme.

**`workout-card`** — A more interactive card variant for workout library items. Includes a {colors.hairline} border by default, switching to {colors.primary} blue border when selected or active. Padding is tight at 16px to maximize content density in scrolling lists.

### Forms
**`text-input`** — Dark input fields on {colors.surface-card} with a {colors.hairline} border. Focus state swaps the border to {colors.primary} blue for clear visual feedback. Error state uses {colors.error} red border. All inputs maintain 48px height and {rounded.sm} corners for consistency with buttons.

### Metrics & Progress
**`metric-display`** — A data container for workout metrics (strokes per minute, split time, distance). Uses {colors.surface-soft} background with {rounded.sm} corners. The metric value uses {typography.display-lg} in {colors.primary} blue, while the label sits below in {colors.muted} caption text — creating clear hierarchy in data-dense interfaces.

**`progress-bar-track`** / **`progress-bar-fill`** — Ultra-thin 4px progress bars with {rounded.full} pill shape. Track is {colors.hairline} gray, fill is {colors.primary} blue. Used for workout completion, subscription trials, and loading states.

### Badges
**`badge`** — Small {colors.primary} blue badges with white text in uppercase 11px type. Used for "NEW", "BESTSELLER", and "LIVE" indicators. The {rounded.xs} (4px) corners keep them sharp and technical rather than playful.

**`badge-outline`** — An outlined variant with transparent background and {colors.primary} blue border. Used for secondary labels like "PREMIUM" or "RECORDED" where the filled badge would compete with other UI elements.

### Footer
**`footer`** — Full-width dark footer on {colors.canvas} with a {colors.hairline} top border. Links use {colors.body} (#e0e0e0) at rest and shift to {colors.primary} on hover. The footer maintains the brand's dark aesthetic while providing clear separation from main content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; metric displays stack vertically; buttons go full-width; hero text reduces to {typography.display-md} |
| Tablet | 744–1128px | Two-column product grids; nav remains visible with condensed links; metric displays in 2x2 grid; sidebars collapse |
| Desktop | 1128–1440px | Full multi-column layouts; expanded nav with all links visible; metric displays in row; workout cards in 3-column grid |
| Wide | > 1440px | Max-width containers at 1440px; content centered; additional whitespace on sides; larger hero imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons and controls use 48px touch targets even when visual size is smaller
- Card tap targets span the full card width, not just text labels
- Bottom nav items on mobile use 56px height for thumb-friendly reach

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px, with full-screen overlay
- Secondary navigation (workout filters, category strips) collapses to horizontal scroll with fade edges
- Metric displays stack vertically on mobile, switching from row to column layout
- Product comparison tables convert to stacked card layout below 744px
- Footer link columns collapse to single column with accordion expansion on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted colors are limited to two blues (#0070f3, #3291ff) and black (#000) from the security checkpoint page — the actual brand palette likely includes additional grays, whites, and potentially accent colors for workout metrics, heart rate zones, and leaderboard elements that couldn't be captured
- Font family declarations are system-native fallbacks; the actual brand may use a custom typeface (e.g., a bespoke sans-serif for performance branding) that wasn't served on the checkpoint page
- Hover and active states for all components are inferred from common patterns, not extracted from live CSS
- Error, success, and warning color tokens are estimated based on standard fitness-app conventions, not extracted from the live site
- Dark mode is the default and only observed state; no light mode or theme-switching data was available
- Component spacing (padding, margins, gaps) is estimated from common grid systems; exact values may differ on the live site
- Animation and transition timing (hover effects, page transitions, loading states) were not captured
- Iconography style (stroke weight, size, color usage) could not be extracted from the checkpoint page
- Typography scale beyond display and body sizes is inferred; actual heading hierarchy may differ
- The meta theme-color of #000 confirms the dark-first approach, but secondary brand colors for sub-brands (Hydrow Wave, Hydrow Pro) were not available
