---
version: alpha
name: "Synology"
source_url: "https://www.synology.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A blue that feels more like a system signal than a brand flourish — #0067e6 anchors every primary action, from the login button to the DSM desktop's "Create" prompt, while a vast secondary palette of #2e3742, #606a72, and #c9d5e2 builds a technical, data-center-adjacent atmosphere. This is not a consumer brand reaching for warmth; it's a storage and networking company whose interface borrows the visual language of enterprise dashboards and server racks. The extracted hex set reveals an unusually wide range of accent colors — #5bc0de (info blue), #33d49b (success green), #edb758 (warning amber), #ea5053 (error red) — each mapped to a specific system state, suggesting a mature design system built for status indication and alerting rather than marketing polish. Typography runs Inter and Open Sans at modest weights (400–600), with display rarely exceeding 24px; the brand trusts dense data tables and sidebar navigation over hero imagery. Cards and modals use soft radii ({rounded.sm}–{rounded.md}), while buttons and badges adopt a slightly tighter {rounded.xs} that reads as precise and industrial. The canvas is #f5f5f5, not pure white — a deliberate shift that reduces glare across long DSM sessions. What emerges is a B2B interface that prioritizes legibility, state clarity, and information density over visual delight, with the blue #0067e6 acting as the single consistent wayfinding thread across a product line that spans NAS appliances, surveillance stations, and router management consoles.

colors:
  primary: "#0067e6"
  primary-active: "#0052c4"
  primary-disabled: "#b3d4ff"
  ink: "#2e3742"
  body: "#444444"
  muted: "#606a72"
  muted-soft: "#888888"
  hairline: "#c9d5e2"
  hairline-soft: "#dce4ec"
  canvas: "#f5f5f5"
  surface-soft: "#f3f6f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  info: "#5bc0de"
  success: "#33d49b"
  warning: "#edb758"
  error: "#ea5053"
  error-soft: "#fce4e4"
  success-soft: "#d4f5e4"
  warning-soft: "#fef3d6"
  info-soft: "#d9edf7"
  table-header: "#f2f6f9"
  table-stripe: "#f3f3f3"
  badge-default: "#aaaaaa"
  badge-active: "#5897fb"
  link: "#0078ff"
  link-hover: "#005bb5"
  scrim: "rgba(46, 55, 66, 0.6)"

typography:
  display-xl:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-lg:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  display-md:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  button-sm:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  link:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  table-header:
    fontFamily: "'Inter', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.3px
    textTransform: uppercase
  code:
    fontFamily: "'Courier New', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0

rounded:
  none: 0px
  xs: 3px
  sm: 6px
  md: 10px
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 36px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 36px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 36px
  button-ghost-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.xs}"
  button-icon-only:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
    height: 32px
    width: 32px
  button-icon-only-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-danger:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 36px
  button-danger-active:
    backgroundColor: "#d43f41"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary-disabled}"
  text-input-error:
    border: "1px solid {colors.error}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 8px 32px 8px 12px
    height: 36px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    height: 16px
    width: 16px
    border: "1px solid {colors.hairline}"
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
  toggle-switch:
    backgroundColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    height: 20px
    width: 36px
  toggle-switch-active:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  toggle-knob:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.full}"
    height: 16px
    width: 16px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    height: 48px
  nav-bar-link:
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    padding: 12px 16px
  nav-bar-link-active:
    textColor: "{colors.canvas}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
  sidebar-nav:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    width: 240px
  sidebar-nav-item:
    padding: 10px 16px
    rounded: "{rounded.sm}"
  sidebar-nav-item-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    rounded: "{rounded.sm}"
  sidebar-nav-item-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 1px 3px rgba(46, 55, 66, 0.08)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(46, 55, 66, 0.12)"
  status-badge:
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    height: 20px
  status-badge-success:
    backgroundColor: "{colors.success-soft}"
    textColor: "#1e8a5e"
  status-badge-warning:
    backgroundColor: "{colors.warning-soft}"
    textColor: "#b8860b"
  status-badge-error:
    backgroundColor: "{colors.error-soft}"
    textColor: "#c0392b"
  status-badge-info:
    backgroundColor: "{colors.info-soft}"
    textColor: "#31708f"
  status-badge-default:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
  data-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
  data-table-header:
    backgroundColor: "{colors.table-header}"
    textColor: "{colors.ink}"
    typography: "{typography.table-header}"
    padding: "10px 16px"
  data-table-row:
    padding: "10px 16px"
    borderBottom: "1px solid {colors.hairline-soft}"
  data-table-row-striped:
    backgroundColor: "{colors.table-stripe}"
  data-table-row-hover:
    backgroundColor: "{colors.surface-soft}"
  modal:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    boxShadow: "0 8px 32px rgba(46, 55, 66, 0.2)"
  modal-header:
    typography: "{typography.display-md}"
    padding: "0 0 {spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  modal-footer:
    padding: "{spacing.base} 0 0 0"
    borderTop: "1px solid {colors.hairline-soft}"
  toast:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
  toast-success:
    backgroundColor: "#1e8a5e"
  toast-error:
    backgroundColor: "#c0392b"
  toast-warning:
    backgroundColor: "#b8860b"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  progress-bar:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.full}"
    height: 6px
  progress-bar-fill:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.full}"
  progress-bar-fill-success:
    backgroundColor: "{colors.success}"
  progress-bar-fill-warning:
    backgroundColor: "{colors.warning}"
  progress-bar-fill-error:
    backgroundColor: "{colors.error}"
  tab-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline-soft}"
  tab-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
    padding: "10px 16px"
  tab-inactive:
    textColor: "{colors.muted}"
    padding: "10px 16px"
  tab-hover:
    textColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 12px 8px 36px"
    height: 36px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.primary}"
  breadcrumb-separator:
    textColor: "{colors.hairline}"
    padding: "0 6px"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  pagination-hover:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  dropdown-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} 0"
    boxShadow: "0 4px 12px rgba(46, 55, 66, 0.15)"
  dropdown-item:
    padding: "8px 16px"
  dropdown-item-hover:
    backgroundColor: "{colors.surface-soft}"
  dropdown-item-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
  dropdown-divider:
    borderTop: "1px solid {colors.hairline-soft}"
    margin: "4px 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.section}"
  footer-link:
    textColor: "{colors.hairline}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.canvas}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.hairline}"
  alert-banner:
    backgroundColor: "{colors.info-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    borderLeft: "3px solid {colors.info}"
  alert-banner-error:
    backgroundColor: "{colors.error-soft}"
    borderLeft: "3px solid {colors.error}"
  alert-banner-warning:
    backgroundColor: "{colors.warning-soft}"
    borderLeft: "3px solid {colors.warning}"
  alert-banner-success:
    backgroundColor: "{colors.success-soft}"
    borderLeft: "3px solid {colors.success}"
  loading-spinner:
    color: "{colors.primary}"
    height: 20px
    width: 20px
  skeleton-loader:
    backgroundColor: "{colors.hairline-soft}"
    rounded: "{rounded.xs}"
    height: 16px
  divider:
    borderTop: "1px solid {colors.hairline-soft}"
    margin: "{spacing.base} 0"
  divider-strong:
    borderTop: "1px solid {colors.hairline}"
    margin: "{spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across Synology's interface, from DSM login to package installation. Uses the brand's signature blue `#0067e6` on a white background with tight `{rounded.xs}` corners that feel precise and industrial. On hover, the background shifts to `{colors.primary-active}` (`#0052c4`), and on disabled state it fades to `{colors.primary-disabled}` (`#b3d4ff`). The 36px height is deliberate — compact enough for dense data table toolbars but tall enough for standalone forms. **`button-secondary`** — A white button with a `{colors.hairline}` border, used for cancel actions and secondary flows in modals and forms. Active state adds `{colors.surface-soft}` background. **`button-ghost`** — Transparent background with blue text, used for inline actions like "Add" or "Edit" within table rows. Hover reveals a soft `{colors.surface-soft}` background. **`button-danger`** — Uses `{colors.error}` (`#ea5053`) for destructive actions like volume deletion or user removal. Active state deepens to `#d43f41`. **`button-icon-only`** — A 32px square icon button for toolbar actions (refresh, filter, search). Hover reveals `{colors.surface-soft}` background.

### Navigation
**`nav-bar`** — The top-level application navigation, a dark `{colors.ink}` (`#2e3742`) bar at 48px height. Links are white with a `{colors.primary}` bottom border on the active state. This is the primary wayfinding element across DSM, Active Backup, and Surveillance Station. **`sidebar-nav`** — A 240px white sidebar for secondary navigation within applications. Active items use `{colors.surface-soft}` background with `{colors.primary}` text. Hover items also use `{colors.surface-soft}`. This pattern appears in DSM's Control Panel, File Station, and Package Center. **`tab-bar`** — Horizontal tabs with a `{colors.hairline-soft}` bottom border. Active tab uses `{colors.primary}` text and a 2px `{colors.primary}` bottom border. Inactive tabs are `{colors.muted}` and hover to `{colors.ink}`.

### Data Display
**`data-table`** — The core data presentation component, used extensively in DSM for file listings, user management, and storage pools. White background with `{colors.table-header}` (`#f2f6f9`) headers using uppercase `{typography.table-header}`. Rows have a `{colors.hairline-soft}` bottom border, with optional striping via `{colors.table-stripe}` (`#f3f3f3`). Hover state uses `{colors.surface-soft}`. **`product-card`** — Used on the Synology website for NAS model listings and on the Package Center. White card with `{rounded.md}` corners and a subtle `boxShadow`. Hover elevates the shadow to signal interactivity. **`status-badge`** — Small uppercase badges for system status indicators. Five variants map to the system state palette: success (`{colors.success-soft}` background, `#1e8a5e` text), warning (`{colors.warning-soft}` background, `#b8860b` text), error (`{colors.error-soft}` background, `#c0392b` text), info (`{colors.info-soft}` background, `#31708f` text), and default (`{colors.surface-soft}` background, `{colors.muted}` text).

### Forms
**`text-input`** — Standard 36px input with `{colors.hairline}` border and `{rounded.xs}` corners. Focus state adds a `{colors.primary}` border with a 2px `{colors.primary-disabled}` ring. Error state uses `{colors.error}` border. Disabled state uses `{colors.surface-soft}` background with `{colors.muted-soft}` text. **`select-input`** — Matches text-input dimensions with a 32px right padding for the dropdown arrow. **`checkbox`** — 16px square with `{rounded.xs}` corners. Checked state fills with `{colors.primary}`. **`toggle-switch`** — 36px wide, 20px tall pill-shaped toggle. Active state fills with `{colors.primary}`, knob is white and 16px.

### Feedback & Overlays
**`modal`** — White card with `{rounded.md}` corners and a strong `boxShadow`. Header uses `{typography.display-md}` with a `{colors.hairline-soft}` bottom border. Footer has a matching top border. Used for confirmations, settings dialogs, and package details. **`toast`** — Dark `{colors.ink}` background with white text for neutral notifications. Success variant uses `#1e8a5e`, error uses `#c0392b`, warning uses `#b8860b`. **`tooltip`** — Small dark tooltip with `{rounded.xs}` corners and `{typography.caption}` text. **`progress-bar`** — 6px tall pill-shaped bar. Default fill is `{colors.primary}`, with success/warning/error variants mapping to the system state palette. **`skeleton-loader`** — `{colors.hairline-soft}` placeholder with `{rounded.xs}` corners, 16px height by default.

### Navigation Aids
**`breadcrumb`** — `{typography.caption}` links in `{colors.primary}` separated by `{colors.hairline}` separators. Used in DSM's file paths and settings hierarchies. **`pagination`** — `{typography.body-sm}` page numbers. Active page uses `{colors.primary}` background with white text. Hover uses `{colors.surface-soft}` background. **`dropdown-menu`** — White card with `{rounded.sm}` corners and a `boxShadow`. Items are 8px 16px padding with `{colors.surface-soft}` hover. Active item uses `{colors.primary}` text.

### Layout & Structure
**`hero-section`** — Dark `{colors.ink}` background section used on marketing pages and the Synology website. White title with `{colors.hairline}` subtitle. **`footer`** — Dark `{colors.ink}` footer with white text and `{colors.hairline}` links that hover to white. **`divider`** — `{colors.hairline-soft}` horizontal rule with `{spacing.base}` vertical margin. Strong variant uses `{colors.hairline}`. **`alert-banner`** — Colored left-border alert with soft background. Four variants map to info, error, warning, and success states.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Sidebar collapses to bottom tab bar; data tables become scrollable horizontally; modals go full-width with 16px margins; product cards stack in single column; hero sections reduce padding to 32px |
| Tablet | 744–1128px | Sidebar remains visible but collapses to icon-only at 48px width; data tables show 4-6 columns with horizontal scroll; product cards display in 2-column grid; nav-bar links condense to icons |
| Desktop | 1128–1440px | Full sidebar at 240px; data tables show 8+ columns; product cards in 3-column grid; all nav-bar labels visible; modals center at 640px max-width |
| Wide | > 1440px | Max-width container at 1440px; data tables expand to full column count; product cards in 4-column grid; hero sections use larger typography (32px display) |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 36px height for touch accessibility
- Icon-only buttons are 32px minimum (slightly below 44px recommendation — acceptable for desktop-focused B2B interface)
- Toggle switches are 20px tall, 36px wide — adequate for desktop but may need enlargement for mobile
- Dropdown items have 32px minimum touch area (8px padding on 14px text)
- Sidebar navigation items have 36px touch height

### Collapsing Strategy
- Sidebar navigation collapses to icon-only at tablet breakpoint, fully hidden on mobile with a hamburger toggle
- Data tables become horizontally scrollable on mobile, with sticky first column for key identifiers (file name, user name)
- Top nav-bar links collapse to icons on tablet, then to a hamburger menu on mobile
- Product cards collapse from multi-column grid to single column on mobile
- Hero sections reduce vertical padding from 64px to 32px on mobile
- Modals become full-width (16px margins) on mobile, with scrollable content

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for many components (dropdown items, sidebar items, table rows) are inferred from common patterns — exact color values and transitions may differ
- Error states for forms (validation messages, error icons) were not fully extracted — only the error border color is confirmed
- Dark mode colors are not present in the extracted palette — Synology's DSM may support a dark theme, but no dark-mode tokens were found
- Animation durations and easing curves (transitions, loading states) were not extracted
- Icon set and icon sizing conventions are undocumented — the extracted fonts include FontAwesome, suggesting icon usage, but no specific icon tokens
- Sub-brand colors for Synology's product lines (DiskStation, RackStation, Surveillance Station, Mesh Router) may exist but were not extracted
- Typography scale for Japanese and Korean locales (NotoSansJP, NotoSansKR, MS PGothic, Meiryo) is present in font declarations but exact sizing and weight mappings are unknown
- The extracted hex list includes many framework-default blues (#107bff, #5897fb, #0078ff) that may be Bootstrap or jQuery UI remnants — the true primary is identified as #0067e6 based on frequency and distinctiveness
- Print and PDF export styling is not captured
- Focus ring styles (outline vs box-shadow, color, width) are inferred from common patterns
