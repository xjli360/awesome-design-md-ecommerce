---
version: alpha
name: "Allen & Heath"
source_url: "https://www.allen-heath.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A professional audio engineering brand that uses a single, unapologetic dark gray — `#313131` — as its primary identity color, a choice that signals the brand’s refusal to perform for consumer aesthetics. This near-black ink runs through every primary button, navigation bar, and product badge, creating a system where the only visual drama comes from the gear itself: brushed aluminum faders, backlit channel strips, and the red glow of a recording light. The typography stack is a pragmatic sans-serif cascade — `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif` — with no custom brand typeface, reinforcing the idea that the interface should disappear behind the work. Corners are tight: primary buttons use `{rounded.sm}` (8px), product cards use `{rounded.md}` (12px), and the only `{rounded.full}` token appears on small badge indicators, not on interactive elements. The canvas is pure white (`#ffffff`), and the body text sits at `#3f3f3f`, a softer ink that keeps long technical documentation readable. There is no gradient, no decorative illustration, no brand mascot — the design system is a clean, dark-on-light chassis built to hold high-density control surfaces, spec tables, and firmware download links. The brand’s visual authority comes from restraint: `#313131` is the only color that ever feels like a primary, and it never needs to be louder than the product it frames.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#1a1a1a"
  body: "#3f3f3f"
  muted: "#6a6a6a"
  muted-soft: "#929292"
  hairline: "#d4d4d4"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red: "#c8102e"
  accent-amber: "#f5a623"
  accent-green: "#2ecc71"
  badge-neutral: "#313131"
  badge-live: "#c8102e"
  link-blue: "#0052cc"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.15px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px

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
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-download:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-sub:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    height: 44px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.on-primary}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    opacity: 0.8
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-spec:
    typography: "{typography.spec-value}"
    textColor: "{colors.muted}"
  badge:
    backgroundColor: "{colors.badge-neutral}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-live:
    backgroundColor: "{colors.badge-live}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subtitle:
    typography: "{typography.body-md}"
    textColor: "{colors.on-primary}"
    opacity: 0.85
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.spec-value}"
    border: "1px solid {colors.hairline-soft}"
  spec-table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    padding: "{spacing.sm} {spacing.md}"
  spec-table-row:
    padding: "{spacing.sm} {spacing.md}"
    borderBottom: "1px solid {colors.hairline-soft}"
  spec-table-row-hover:
    backgroundColor: "{colors.surface-soft}"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "8px 16px"
  tab-inactive-hover:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.body}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in `{colors.primary}` (`#313131`) with white text and `{rounded.sm}` corners. On hover, the background deepens to `{colors.primary-active}` (`#1a1a1a`). The disabled state uses `{colors.primary-disabled}` (`#a0a0a0`), a mid-gray that signals non-interactivity without visual noise. **`button-secondary`** — An outlined variant with a `{colors.primary}` border on a white canvas, used for secondary actions like "Learn More" or "Compare Models." **`button-tertiary`** — A text-only button with no background or border, used for inline actions like "Cancel" or "View Details." **`button-download`** — A green-accented button (`{colors.accent-green}`) reserved exclusively for firmware and software download actions, visually distinct from the neutral primary system.

### Navigation
**`nav-bar`** — A fixed-height 56px bar in `{colors.primary}` with uppercase nav links in white. The active link is underlined with a 2px white border; inactive links sit at 0.8 opacity. **`nav-bar-sub`** — A secondary white bar below the primary nav, separated by a `{colors.hairline}` border, used for product-category sub-navigation. **`nav-link-active`** and **`nav-link-inactive`** — State tokens that control the link appearance within the nav bar.

### Cards
**`product-card`** — A white card with `{rounded.md}` corners and a soft `{colors.hairline-soft}` border. On hover, the border strengthens to `{colors.hairline}` and a subtle box shadow lifts the card. The image area uses a 4:3 aspect ratio with `{rounded.sm}` corners. The title uses `{typography.title-sm}` in `{colors.ink}`, and the spec line below uses `{typography.spec-value}` in `{colors.muted}`.

### Badges
**`badge`** — A small, uppercase, fully rounded pill in `{colors.primary}` with white text. **`badge-live`** — A red variant (`{colors.badge-live}`) used to indicate live or recording status on products. **`badge-new`** — An amber variant (`{colors.accent-amber}`) with dark text for "New" or "Updated" indicators.

### Forms
**`text-input`** — A standard input field with a `{colors.hairline}` border and `{rounded.sm}` corners. On focus, the border thickens to 2px `{colors.primary}`. Error state uses a 2px `{colors.accent-red}` border. **`select-input`** — Matches the text-input styling for consistency across form elements.

### Hero
**`hero-section`** — A full-width section with `{colors.primary}` background and white text, padded with `{spacing.section}` vertical and `{spacing.lg}` horizontal. The title uses `{typography.display-xl}` and the subtitle sits at `{typography.body-md}` with 0.85 opacity.

### Tables
**`spec-table`** — A bordered table for technical specifications. The header row uses `{colors.surface-soft}` background with `{typography.spec-label}`. Data rows use `{typography.spec-value}` with a `{colors.hairline-soft}` bottom border. Hovering a row triggers a `{colors.surface-soft}` background highlight.

### Tabs
**`tab-active`** — A filled tab in `{colors.primary}` with white text and `{rounded.sm}` corners. **`tab-inactive`** — A soft gray tab (`{colors.surface-soft}`) with muted text, which on hover shifts to `{colors.hairline-soft}` background and `{colors.body}` text.

### Footer
**`footer-section`** — A `{colors.primary}` footer with white text at `{typography.body-sm}`. Links are white at 0.8 opacity, increasing to full opacity on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav-bar collapses to hamburger menu; product cards stack vertically; hero padding reduces to `{spacing.xl}`; spec tables become scrollable horizontally; search bar moves to full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows top-level links only (dropdown for sub-nav); hero uses `{typography.display-lg}`; spec tables remain readable with reduced padding |
| Desktop | 1128–1440px | Three-column product grid; full nav-bar with sub-nav visible; hero uses `{typography.display-xl}`; standard spec-table padding |
| Wide | > 1440px | Max-width container (1440px) centered; four-column product grid; additional whitespace around hero and footer |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility.
- Nav-bar links have a minimum 48px tap area (including padding).
- Product cards have a minimum 72px tap area for the entire card surface.
- Badges are excluded from touch-target requirements as they are decorative indicators.

### Collapsing Strategy
- On mobile, the primary nav-bar collapses to a hamburger icon; the sub-nav is hidden entirely and accessible via a "Products" dropdown.
- The product grid collapses from 4 columns (wide) → 3 (desktop) → 2 (tablet) → 1 (mobile).
- The hero section reduces vertical padding from `{spacing.section}` to `{spacing.xl}` on mobile.
- Spec tables become horizontally scrollable on mobile, with the first column (spec label) frozen.
- Footer links collapse from a multi-column layout to a single vertical stack on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (`#313131`) was extracted from the live site; the full color palette (including accent red, amber, green, and link blue) is inferred from common audio-industry conventions and may not match the exact brand values. A full CSS audit is needed.
- No custom brand typeface was detected; the system uses a standard system-font stack. The brand may use a proprietary font on marketing materials that was not present in the extracted CSS.
- Hover, focus, and active states for all components are inferred from common patterns; the actual brand implementation may differ.
- Error and success messaging styling (toast, inline validation, modal dialogs) was not extracted.
- Dark mode or high-contrast mode tokens are absent; the brand may not support these yet.
- Spacing and sizing tokens are based on common design-system conventions; the actual brand values may vary.
- The `rounded` token values are inferred; the brand may use different radii for specific contexts.
- No animation or transition timing tokens were extracted (ease curves, durations).
- The brand's iconography style (stroke weight, filled vs outlined) was not determined.
- No data on the brand's use of imagery, photography style, or illustration guidelines.
