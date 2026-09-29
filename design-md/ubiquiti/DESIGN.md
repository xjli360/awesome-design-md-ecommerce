---
version: alpha
name: "Ubiquiti"
source_url: "https://ui.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep blue (#0193d7) cuts through a black-and-white technical canvas like a signal light in a server room — that single cyan accent is the brand voltage for every primary CTA, status indicator, and active-state glow across the UniFi ecosystem. The site runs UI Sans at clean, moderate weights with generous tracking, treating typography as infrastructure rather than decoration: display heads sit at 24–32px in weight 600, body text at 15–16px in weight 400, and every button reads in a crisp 14px medium weight. The meta theme-color of #000000 signals the brand's commitment to dark-mode-first thinking — the canvas is black, not white, and the entire layout reads like a network dashboard where information density is a feature, not a flaw. Navigation is a persistent top bar with product-family dropdowns (UniFi, UISP, AmpliFi, etc.), each entry acting as a portal into a hardware ecosystem rather than a marketing page. Cards use tight `{rounded.sm}` corners (4px), buttons use `{rounded.md}` (8px), and the only `{rounded.full}` treatment appears on search inputs and status badges — a deliberate restraint that keeps the interface feeling precise and engineered. The brand trusts dark surfaces (`{colors.canvas}` = #000000), soft surface cards (`{colors.surface-card}` = #1a1a1a), and hairline borders (`{colors.hairline}` = #2a2a2a) to create depth without shadows, a visual language that mirrors the rack-mounted hardware it sells.

colors:
  primary: "#0193d7"
  primary-active: "#0177b0"
  primary-disabled: "#004466"
  ink: "#ffffff"
  body: "#c8c8c8"
  muted: "#808080"
  muted-soft: "#5a5a5a"
  hairline: "#2a2a2a"
  hairline-soft: "#1f1f1f"
  canvas: "#000000"
  surface-soft: "#121212"
  surface-card: "#1a1a1a"
  on-primary: "#ffffff"
  success: "#00b300"
  warning: "#ffa500"
  error: "#e53935"
  badge-new: "#0193d7"
  badge-beta: "#808080"

typography:
  display-xl:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.15px
  body-md:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.25px
  badge:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.4px
  link:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'UI Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 10px 24px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 10px 24px
    height: 40px
    border: "1px solid {colors.hairline}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 10px 24px
    height: 40px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 10px 16px
    height: 40px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px rgba(1, 147, 215, 0.2)"
  text-input-error:
    border: "1px solid {colors.error}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 8px 0
    boxShadow: "0 8px 24px rgba(0, 0, 0, 0.4)"
  nav-dropdown-item:
    padding: 8px 16px
    hoverBackgroundColor: "{colors.surface-soft}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
    border: "1px solid {colors.hairline}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(1, 147, 215, 0.15)"
  product-card-image:
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 12px 32px
    height: 48px
  status-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 10px
    height: 22px
    border: "1px solid {colors.hairline}"
  status-badge-success:
    backgroundColor: "{colors.success}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 10px
    height: 22px
  status-badge-warning:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 10px
    height: 22px
  status-badge-error:
    backgroundColor: "{colors.error}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 10px
    height: 22px
  tag-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
    height: 20px
  tag-beta:
    backgroundColor: "{colors.badge-beta}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 2px 8px
    height: 20px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    borderTop: "1px solid {colors.hairline}"
  footer-link:
    textColor: "{colors.body}"
    typography: "{typography.link}"
    hoverTextColor: "{colors.primary}"
  toggle-switch:
    backgroundColor: "{colors.muted-soft}"
    rounded: "{rounded.full}"
    height: 24px
    width: 44px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
  toggle-switch-thumb:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
  progress-bar:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 4px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
    height: 4px
  tooltip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
    boxShadow: "0 4px 12px rgba(0, 0, 0, 0.3)"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the brand cyan `{colors.primary}` with white text. On hover it shifts to `{colors.primary-active}` (#0177b0), and in its disabled state it fades to a muted teal `{colors.primary-disabled}` (#004466) with `{colors.muted}` text. All primary buttons use `{rounded.md}` (8px) corners and `{typography.button-md}` for a clean, technical feel. The height is fixed at 40px with 10px vertical padding and 24px horizontal padding.

**`button-secondary`** — An outlined variant on `{colors.surface-card}` background with a `{colors.hairline}` border and white text. Used for secondary actions like "Learn More" or "Compare Models." On hover the border shifts to `{colors.primary}` and the background lightens slightly. Disabled state uses `{colors.muted}` text and `{colors.hairline-soft}` border.

**`button-tertiary`** — A text-only button in `{colors.primary}` with no background or border. Used for inline actions like "View All" or "See Details." On hover the text shifts to `{colors.primary-active}` and a subtle underline appears. The transparent background ensures it works on any surface.

**`button-ghost`** — A minimal button with transparent background and `{colors.body}` text, used for utility actions like "Cancel" or "Dismiss." On hover the background becomes `{colors.surface-soft}` and text shifts to `{colors.ink}`. No border, no shadow — pure functional minimalism.

**`button-pill`** — A compact pill-shaped variant using `{rounded.full}` for search filters, category tags, and quick-apply actions. Uses `{typography.button-sm}` at 12px with tighter padding (8px 20px) and a shorter 36px height. The pill shape signals a toggle-able or dismissible action.

### Navigation
**`nav-bar`** — A persistent 64px top bar on `{colors.canvas}` with a `{colors.hairline}` bottom border. Navigation links use `{typography.nav-link}` at 14px weight 500 with 0.3px letter spacing. The bar contains the Ubiquiti logo on the left, product-family links (UniFi, UISP, AmpliFi, etc.) in the center, and utility icons (search, account, cart) on the right. On scroll the bar remains fixed with a slight backdrop blur.

**`nav-dropdown`** — A floating panel on `{colors.surface-card}` with `{rounded.md}` corners and a deep shadow (`boxShadow: 0 8px 24px rgba(0, 0, 0, 0.4)`) that lifts it off the dark canvas. Each item has 8px vertical padding and 16px horizontal padding, with a `{colors.surface-soft}` hover state. The dropdown appears on hover over nav links and contains product sub-categories, documentation links, and feature highlights.

**`search-bar`** — A full-rounded input field on `{colors.surface-card}` with a `{colors.hairline}` border and 40px height. The pill shape (`{rounded.full}`) distinguishes it from standard text inputs and signals a global search action. On focus the border shifts to `{colors.primary}` with a subtle cyan glow. Placeholder text uses `{colors.muted}`.

### Cards
**`product-card`** — A hardware product card on `{colors.surface-card}` with `{rounded.sm}` (4px) corners and a `{colors.hairline}` border. Contains a product image at 4:3 aspect ratio with `{rounded.xs}` corners, a title in `{typography.title-sm}`, specs in `{typography.body-sm}`, and a price or status badge at the bottom. On hover the border shifts to `{colors.primary}` and a cyan shadow appears (`boxShadow: 0 4px 12px rgba(1, 147, 215, 0.15)`). Padding is 16px on all sides.

**`hero-section`** — The full-width hero area on `{colors.canvas}` with `{spacing.section}` vertical padding and `{spacing.lg}` horizontal padding. Uses `{typography.display-xl}` for the headline and `{typography.body-md}` for supporting text. The hero CTA is a `{colors.primary}` button at 48px height with 12px 32px padding. Background may include a subtle gradient or product imagery.

### Forms
**`text-input`** — A standard input field on `{colors.surface-card}` with `{rounded.md}` corners and a `{colors.hairline}` border. Height is 48px with 12px 16px padding. On focus the border becomes `{colors.primary}` with a 2px cyan ring (`boxShadow: 0 0 0 2px rgba(1, 147, 215, 0.2)`). Error state uses `{colors.error}` border. Disabled state uses `{colors.surface-soft}` background and `{colors.muted}` text.

**`select-input`** — A dropdown select styled identically to `text-input` with a custom chevron icon in `{colors.muted}`. Uses the same 48px height, `{rounded.md}` corners, and focus/error states. The dropdown panel matches `nav-dropdown` styling.

### Status & Badges
**`status-badge`** — A small pill-shaped badge (`{rounded.full}`) at 22px height with 2px 10px padding. Uses `{typography.badge}` at 11px uppercase with 0.3px letter spacing. Default state is neutral (`{colors.surface-card}` background, `{colors.body}` text, `{colors.hairline}` border). Success, warning, and error variants use their respective colors as background with white or black text for contrast.

**`tag-new`** and **`tag-beta`** — Compact 20px height badges for signaling product status. `tag-new` uses `{colors.badge-new}` (cyan) background, `tag-beta` uses `{colors.badge-beta}` (gray) background. Both use `{typography.badge}` with 2px 8px padding and `{rounded.full}`.

### Interactive Elements
**`toggle-switch`** — A 44x24px pill-shaped toggle with `{rounded.full}`. The track is `{colors.muted-soft}` in off state and `{colors.primary}` in active state. The thumb is a 20x20px white circle. Transition is 200ms ease. Used for settings, filters, and feature toggles.

**`progress-bar`** — A 4px tall bar with `{rounded.full}`. The track is `{colors.hairline}` and the fill is `{colors.primary}`. Used for loading states, setup wizards, and device adoption progress.

**`tooltip`** — A floating label on `{colors.surface-card}` with `{rounded.sm}` corners, 6px 12px padding, and a deep shadow. Uses `{typography.caption}` at 13px. Appears on hover over icons, truncated text, and technical specs. Positioned above or below the target element with a 4px gap.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout, nav collapses to hamburger menu, product cards stack vertically, hero text reduces to `{typography.display-md}`, search bar moves to bottom of nav, footer links stack |
| Tablet | 744–1128px | Two-column product grid, nav shows top-level links only (dropdowns become tap-to-open), hero uses `{typography.display-lg}`, sidebar filters become horizontal scroll |
| Desktop | 1128–1440px | Full nav with dropdowns, three-column product grid, hero at full `{typography.display-xl}`, sidebar filters visible, multi-row footer |
| Wide | > 1440px | Max-width container at 1440px, centered content, additional whitespace on sides, hero may include full-width product imagery |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44x44px touch target
- Nav links on mobile expand to full-width tap targets (min 48px height)
- Toggle switches sized at 44x24px with 20px thumb for easy finger manipulation
- Search bar on mobile expands to full width with 48px height
- Dropdown items on tablet/mobile have 48px minimum height for tap targets

### Collapsing Strategy
- Top nav collapses to hamburger menu at < 744px, with a slide-out drawer from the left
- Product family dropdowns become accordion-style sections in mobile nav
- Hero section reduces vertical padding from `{spacing.section}` to `{spacing.xl}` on mobile
- Product card grid shifts from 3 columns to 2 columns at tablet, to 1 column at mobile
- Footer link columns collapse to a single stacked list at mobile
- Sidebar filters collapse to a horizontal scrollable strip at tablet, to a bottom sheet at mobile
- Search bar collapses from a full input to an icon button at mobile, expanding to full-width on tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#0193d7) was extracted from the live site; additional colors (primary-active, primary-disabled, success, warning, error, and all surface/ink/muted values) are inferred from common design-system patterns and may not match the exact live implementation
- Font-family "UI Sans" was extracted but no font weights, sizes, or line heights were found; all typography values are estimated based on common technical brand patterns and may differ from actual site implementation
- No hover states, focus states, or active states were extracted; all interactive state colors are inferred
- No border-radius values were extracted; all rounded tokens are estimated based on the brand's technical aesthetic
- No spacing values were extracted; all spacing tokens follow a standard 4px/8px grid
- Dark mode is the default (canvas is #000000) but no light mode colors were extracted; if a light mode exists, all surface and text colors would need to be inverted
- No error, success, or warning colors were extracted; these are common web standards and may differ from the brand's actual palette
- No icon system or illustration style was captured; the brand likely uses custom hardware illustrations and technical icons
- No animation or transition timing values were extracted; all transitions use standard 200ms ease
- No shadow values were extracted; all box-shadow values are estimated for depth on dark surfaces
- No font-display or @font-face declarations were captured; the actual font loading strategy is unknown
