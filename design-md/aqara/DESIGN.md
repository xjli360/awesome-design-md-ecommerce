---
version: alpha
name: "Aqara"
source_url: "https://aqara.com"
captured_at: "2026-09-28T09:08:17.302314+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Aqara's homepage evidence shows a light, high-contrast interface built on white canvas
  (#ffffff) with near-black text tones (#1d1d1f, #121212) rather than pure black, consistent
  with an Apple-adjacent visual language reinforced by the site's own Apple Home messaging.
  The single strong accent is #4660ff, applied to nav-link hover/active states and icon
  hover backgrounds, so it is mapped here as the primary interactive color. Secondary neutrals
  (#767676, #6e6e73, #86868b) supply muted labels and captions, while soft grays (#f7f8fa,
  #f8f9fb, #f4f5f7) form card and pill backgrounds such as the language trigger and language
  card. Hairlines and dividers are inferred from light borders like #e8e8ed and #eaeaea, not
  explicitly observed as border declarations. Typography uses the observed system-font stack
  (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial) with Chinese
  fallbacks (PingFang SC, Microsoft YaHei), matching a bilingual storefront. Corner radii
  range from fully rounded pills (999px, 50%) on buttons/icons to 8–12px on menus and cards,
  suggesting a soft, rounded, Apple-influenced product UI. Additional palette colors (red,
  orange, blue, green) are treated as inferred status/badge accents pending further evidence.

colors:
  primary: "#4660ff"
  ink: "#1d1d1f"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#e8e8ed"
  surface-soft: "#f8f9fb"
  surface-card: "#f4f5f7"
  on-primary: "#ffffff"
  text-secondary: "#6e6e73"
  text-tertiary: "#939393"
  border-soft: "#dcdce2"
  border-mid: "#d2d2d7"
  accent-blue-soft: "#e7ebff"
  accent-blue-soft-2: "#eef1ff"
  link-blue: "#007aff"
  accent-red: "#ff3636"
  accent-orange: "#ff860c"
  accent-orange-soft: "#ffefe0"
  accent-green: "#0f9d58"
  accent-amber: "#f59e0b"
typography:
  display-xl: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', PingFang SC, 'Microsoft YaHei', Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', PingFang SC, 'Microsoft YaHei', Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', PingFang SC, 'Microsoft YaHei', Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', PingFang SC, 'Microsoft YaHei', Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', PingFang SC, 'Microsoft YaHei', Arial, sans-serif", fontSize: "15px", fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', PingFang SC, 'Microsoft YaHei', Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', PingFang SC, 'Microsoft YaHei', Arial, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  full: 9999px
spacing:
  none: 0px
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.border-soft}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.text-tertiary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.border-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeColor: "{colors.primary}"
    typography: "{typography.body-md}"
    hairline: "{colors.hairline}"
    position: "sticky-top (observed: position sticky, z-index 2000)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    mutedText: "{colors.muted}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    typography: "{typography.title-md}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    controlBackground: "rgba(255,255,255,0.1) with backdrop-filter blur (observed on slider-btn)"
    controlTextColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.text-secondary}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-orange-soft}"
    textColor: "{colors.accent-orange}"
    rounded: "{rounded.full}"
    typography: "{typography.caption}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    clearButtonBackground: "rgba(0,0,0,0.06) (observed)"
    clearButtonHoverBackground: "rgba(0,0,0,0.10) (observed)"
    rounded: "{rounded.full}"
    typography: "{typography.body-sm}"
  device-category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    subtitleColor: "{colors.muted}"
    rounded: "{rounded.lg}"
    hoverAccent: "{colors.primary}"
    padding: "{spacing.lg}"
    typography: "{typography.body-md}"

## Components
**button-primary** carries the brand's single strong accent (#4660ff) as a filled pill, proposed for primary CTAs such as "了解更多" (learn more) actions; the full-radius shape is inferred from the fully-rounded icon-btn/lang-trigger pattern actually observed elsewhere in the CSS.

**button-secondary** uses a light neutral surface with a soft border, intended for lower-emphasis actions beside a primary button; background and border colors are drawn from observed surface-card and border-soft tokens, but the component itself is a proposed pairing, not directly observed.

**text-input** is proposed for the "全屋智能定制" contact form (name/phone fields referenced in page text); background and border values reuse observed neutral tokens since no input-specific CSS was supplied.

**nav-bar** reflects directly observed rules: sticky positioning, z-index 2000, the system font stack, 16px link size, and the #4660ff hover/active color — this is the most evidence-grounded component in the set.

**product-card** is proposed to represent the many device tiles (sensors, switches, cameras, gateways) implied by the product-matrix text; no explicit card CSS was supplied, so padding, radius, and border are inferred defaults consistent with the site's soft, boxed presentation elsewhere (e.g., lang-card's 8px radius).

**hero** approximates the homepage's large video/slider banner ("空间，因智能而不同"); the frosted, semi-transparent control button (rgba white background with backdrop-filter blur) is directly observed on `.slider-btn`, while overall hero typography size is proposed.

**footer** is inferred from the long link-list structure in the page text (产品中心, 技术支持, 关于我们, etc.); colors reuse observed muted and surface tokens, but footer-specific CSS was not supplied.

**badge** is proposed for "新品"/status labels seen near product names (e.g., new arrivals like H1 Elite); the orange pairing (#ff860c on #ffefe0) is inferred from the palette's warm accent pair, not a confirmed badge rule.

**search** reflects the observed `.search-box-clear` button styling (transparent black overlays, circular shape) combined with an inferred rounded input field, since only the clear-button state was present in evidence.

**device-category-tile** is a category-appropriate proposed component representing the room/category navigation (客厅, 卧室, 厨房, 智能网关, 传感监测, etc.); no direct CSS was supplied for these tiles, so styling is inferred from the site's general soft-surface, rounded-corner pattern.

## Responsive Behavior
The following breakpoints are a **recommendation only**; no responsive/mobile CSS or viewport behavior was present in the supplied evidence.

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| mobile | <768px | Nav collapses to `.mobile-nav-link` / `.mobile-accordion` pattern referenced in selectors; single-column product/category tiles. |
| tablet | 768–1199px | Two-column product grid; dropdown menus may convert to accordions. |
| desktop | ≥1200px | Full horizontal nav with hover dropdowns as observed (`.dropdown-menu`, `.lang-dropdown`). |

Touch targets should be a minimum 40px (matching the observed `.icon-btn` 40×40px sizing). Dropdown/accordion collapse behavior is proposed based on the presence of `.mobile-accordion-link` selectors, not confirmed interaction observation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, animation, or real breakpoint behavior was observed. Color-to-role mapping (e.g., which gray is "body" vs "muted") is inferred from selector context, not confirmed by visual inspection. Several palette colors (accent-red, accent-green, accent-amber, link-blue) have no accompanying selector evidence and are held as unassigned/inferred accents. Typography sizes beyond the few directly observed (16px nav-link, 15px sub-link, 14px caption text) are proposed placeholders. Font rendering relies on system fonts and Chinese web-safe fonts (PingFang SC, Microsoft YaHei, 宋体, 黑体); no custom/proprietary font files or licensing were observed or verified. Mobile menu, form validation states, and hover/focus states beyond those explicitly styled (nav-link hover, icon-btn hover, search-clear hover) are not observed and are marked proposed throughout.
