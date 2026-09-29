---
version: alpha
name: "Natalist"
source_url: "https://natalist.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A clinical warmth defines Natalist, where a sharp cerulean accent (#00b2ff) cuts through a palette of slate grays (#4a5464, #728197, #dcdfe5) and near-black (#121212, #23282f). The brand lives in the tension between medical credibility and emotional comfort — the primary blue reads as diagnostic precision, while the soft gray scale and generous whitespace soften the experience into something approachable. Typography layers a monospaced voice (DM Mono) for data-heavy moments — cycle tracking, symptom logs, test results — against the clean humanist readability of DM Sans for body copy, with PP Agrandir reserved for display moments that feel editorial rather than clinical. Phosphor icons, thin and geometric, replace the usual chunky illustrations, reinforcing the brand's preference for information clarity over decorative fluff. Button radii stay tight at {rounded.sm} (8px), never pill-shaped, preserving a subtle seriousness — this is not a wellness app with confetti, it's a fertility and pregnancy support system. The near-black ink (#121212) on white canvas creates high contrast for medical legibility, while the muted slate (#728197) handles secondary text and captions without competing for attention. Cards and surfaces use the lightest gray (#dcdfe5) for hairline borders, keeping the layout airy but structured. The brand's design language suggests a lab coat worn by someone who remembers your name — precise, trustworthy, and quietly human.

colors:
  primary: "#00b2ff"
  primary-active: "#0099e0"
  primary-disabled: "#b3e6ff"
  ink: "#121212"
  body: "#4a5464"
  muted: "#728197"
  muted-soft: "#c1c8d1"
  hairline: "#dcdfe5"
  hairline-soft: "#eef0f3"
  canvas: "#ffffff"
  surface-soft: "#f7f8fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#d32f2f"
  success: "#2e7d32"
  warning: "#ed6c02"

typography:
  display-xl:
    fontFamily: "'PP Agrandir', 'DM Sans', -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'PP Agrandir', 'DM Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'DM Sans', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  data-display:
    fontFamily: "'DM Mono', 'DM Sans', monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  data-small:
    fontFamily: "'DM Mono', 'DM Sans', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'DM Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'DM Sans', sans-serif"
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-active:
    textColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.error}"
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  checkbox:
    rounded: "{rounded.xs}"
    border: "2px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
  radio-checked:
    border: "6px solid {colors.primary}"
  top-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  data-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.data-display}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  data-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.data-small}"
    textTransform: uppercase
  data-table-row-hover:
    backgroundColor: "{colors.surface-soft}"
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 8px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "8px 12px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for key actions like "Add to Cart", "Start Your Journey", and "Subscribe". Rendered in the brand's cerulean (#00b2ff) with white text and an 8px corner radius. On hover, shifts to a deeper active state (#0099e0). The disabled state uses a pale blue (#b3e6ff) to maintain visual consistency while signaling non-interactivity. Button text is set in DM Sans 15px/600 with 0.3px letter spacing for a slightly more deliberate read than body copy.

**`button-secondary`** — An outlined variant for secondary actions like "Learn More" or "View Details". Uses a white background with a 2px cerulean border, matching the primary button's height and padding. On hover, the border deepens to the active blue and the background shifts to the softest gray (#f7f8fa). This button lives alongside the primary in paired CTAs, never as a standalone hero action.

**`button-tertiary`** — A text-only button for inline actions like "Cancel" or "Skip". No background, no border — just the cerulean text on canvas. Used in forms and modals where visual weight would compete with the primary action. Hover state shifts to the deeper active blue.

### Navigation
**`top-nav`** — A fixed 64px white bar carrying the brand logo on the left and navigation links on the right. Nav links are set in DM Sans 14px/600 with 0.3px letter spacing, uppercase — a deliberate choice that reads as more clinical and authoritative than sentence case. The active link is underlined with a 2px cerulean border. The nav collapses to a hamburger menu on mobile, with the drawer sliding in from the right.

**`nav-link-active`** — The active state for top navigation items. Uses the cerulean primary color with a 2px bottom border, creating a clear visual anchor for the current section. Inactive links remain in the near-black ink (#121212).

### Cards
**`product-card`** — A white card with 12px corner radius and 16px padding, used across product listings and subscription flows. The card contains an image (also 12px rounded), a title in DM Sans 18px/600, a body price in 16px/400 slate (#4a5464), and an optional badge. Cards sit on a soft gray background (#f7f8fa) in listing views, creating subtle separation from the canvas.

**`product-card-badge`** — A small cerulean pill with white text, set in 11px/700 uppercase DM Sans with 0.5px letter spacing. Used for "New", "Best Seller", or "Subscription Only" labels. Positioned absolutely over the top-left of the product image, with 4px corner radius for a crisp rather than pill-shaped appearance.

### Forms
**`text-input`** — Standard text input for forms, name fields, and search. White background, 48px height, 12px/16px padding, 8px corner radius, and a 1px hairline border (#dcdfe5). On focus, the border thickens to 2px cerulean. Error state uses a 2px red border (#d32f2f). Labels sit above the input in 13px/500 DM Sans in muted slate (#728197).

**`checkbox`** and **`radio`** — Small interactive elements with 4px corner radius for checkboxes and full roundness for radios. Default state shows a 2px hairline border. Checked state fills with cerulean — checkboxes get a solid fill, radios get a 6px inner circle. These are used extensively in symptom tracking, quiz flows, and subscription preference forms.

### Data Display
**`data-table`** — A bordered table with 8px corner radius, used for cycle tracking, lab results, and subscription history. Headers use the soft gray background (#f7f8fa) with uppercase 13px DM Mono text in slate (#4a5464). Body cells use 16px DM Mono for data precision. Rows highlight on hover with the soft gray background. The monospaced font choice is deliberate — it signals that the data is precise, measurable, and trustworthy.

**`progress-bar`** — A thin 8px pill-shaped bar used in onboarding flows, quiz completion, and subscription milestones. The track is hairline gray (#dcdfe5), the fill is cerulean (#00b2ff). No text overlay — the bar communicates progress purely through visual proportion.

### Feedback
**`tooltip`** — A dark near-black (#121212) tooltip with white text, 8px corner radius, and 8px/12px padding. Used for clarifying medical terms, explaining test results, or providing context on form fields. Text is set in 13px/500 DM Sans. Appears on hover with a 200ms fade-in.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav collapses to hamburger; product cards stack vertically; data tables become scrollable horizontally; hero section padding reduces to 32px; search bar moves below hero |
| Tablet | 744–1128px | Two-column product grid; top-nav remains expanded but reduces link spacing; hero uses 48px padding; data tables show 3-4 columns before scroll |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links; hero uses 64px padding; data tables show full columns; sidebars appear on product detail pages |
| Wide | > 1440px | Max-width container at 1280px; product grid expands to four columns; hero uses 80px padding; additional whitespace around content blocks |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Checkboxes and radios use a 44px hit area even though the visual element is smaller.
- Hamburger menu icon is 48px × 48px.
- Product card CTAs are at least 44px tall.
- Search bar maintains 48px height across all breakpoints.

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px, with a slide-in drawer from the right.
- Product grids collapse from 4 columns (wide) → 3 columns (desktop) → 2 columns (tablet) → 1 column (mobile).
- Data tables collapse to horizontal scroll on mobile, with the first column pinned.
- Hero sections collapse from side-by-side (image + text) to stacked on mobile.
- Footer links collapse from multi-column to single-column accordion on mobile.
- Sidebars on product detail pages collapse to below-the-fold sections on tablet and mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color palette is heavily weighted toward blues and grays, which may reflect the site's current state but could be missing a secondary accent color (e.g., a sage green or warm pink common in fertility/wellness brands). The extracted list did not return any distinctive non-blue accent — the cerulean (#00b2ff) was selected as primary based on its prominence and distinctiveness within the extracted set.
- Hover and focus states for all components are inferred from common patterns and may not match the live site exactly.
- Error and success color values (#d32f2f, #2e7d32, #ed6c02) are Material Design defaults — the brand may use custom error/success colors not captured in the extraction.
- Font weights for DM Mono and PP Agrandir are assumed based on common usage — the live site may use additional weights (e.g., DM Mono 300, PP Agrandir 800).
- The extracted font list includes "Phosphor" and "Phosphor-Light" with `!important` flags — these are likely icon fonts. Their exact usage (icon sizes, stroke widths, color application) could not be determined.
- PP Agrandir may be a variable font — the specific axis settings (weight, width) could not be extracted.
- Dark mode styling is not present in the extracted data — the brand may not support it, or it may be gated behind user preference.
- Sub-brand or campaign-specific palettes (e.g., for "Natalist Fertility" vs. "Natalist Pregnancy") could not be identified.
- Animation and transition timing values (durations, easing curves) were not extracted.
- The meta theme-color (#121212) matches the ink color, suggesting the brand treats the browser chrome as part of the design system — but its exact application across pages could not be verified.
