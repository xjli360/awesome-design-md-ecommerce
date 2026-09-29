---
version: alpha
name: "Grizzl-E"
source_url: "https://grizzl-e.com"
captured_at: "2026-09-28T09:10:08.966444+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Grizzl-E's evidence points to a clean, utilitarian e-commerce interface built on Inter and system-ui fallbacks, styled with Tailwind-derived utility classes (text-body-s, text-h1, etc.) rather than a bespoke type scale. The observed palette centers on a near-black ink (#18181b) over white and off-white canvases (#ffffff, #fafafa, #f4f4f5), with zinc-toned grays (#27272a, #52525b, #71717a, #a1a1aa) for secondary text and borders. A saturated blue (#2563eb / #0267ff family) reads as the primary interactive/brand accent given its repetition alongside lighter blue tints (#eff6ff, #dbeafe, #ced8f7) used for soft surfaces and badges. A rose/crimson family (#be123c, #e11d48, #f43f5e) and an emerald family (#10b981, #22c55e) also recur, inferred as status or promotional accents (e.g., sale, in-stock) rather than primary brand color, since no single hue is confirmed as "the" brand color from the excerpt alone. The interpretation proposes a rugged-but-modern industrial commerce aesthetic: dense product grids, weather/durability badges, and app-control callouts, matching the "Made in Canada," all-weather charger positioning. Typography sizes below are proposed extrapolations from the small observed scale (11–24px) into a fuller display range; no custom or licensed webfont beyond system/Inter stacks is confirmed.

colors:
  primary: "#2563eb"
  ink: "#18181b"
  canvas: "#ffffff"
  body: "#27272a"
  muted: "#71717a"
  hairline: "#e4e4e7"
  surface-soft: "#f4f4f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-blue-soft: "#eff6ff"
  accent-blue-tint: "#dbeafe"
  accent-blue-deep: "#1e3a8a"
  accent-rose: "#e11d48"
  accent-rose-deep: "#be123c"
  accent-emerald: "#10b981"
  accent-emerald-deep: "#064e3b"
  border-strong: "#d4d4d8"
  border-soft: "#e5e7eb"
typography:
  display-xl: {fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.2, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Ubuntu, sans-serif", fontSize: "24px", fontWeight: 700, lineHeight: 1.3, letterSpacing: "0px"}
  body-l-medium: {fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Ubuntu, sans-serif", fontSize: "16px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Ubuntu, sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Ubuntu, sans-serif", fontSize: "11px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Ubuntu, sans-serif", fontSize: "11px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.1px"}
  button-md: {fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Ubuntu, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.4, letterSpacing: "0px"}
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
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    height: 60px
    textColor: "{colors.body}"
    typography: "{typography.body-l-medium}"
    borderColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.body-l-medium}"
    priceTypography: "{typography.title-md}"
    metaTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-l-medium}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderColor: "{colors.border-strong}"
  badge:
    backgroundColor: "{colors.accent-blue-soft}"
    textColor: "{colors.accent-blue-deep}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** is proposed as the core purchase/CTA action ("Buy now," "Shop now"), using the inferred brand blue against white text with a small radius consistent with the compact utility-class scale observed.

**button-secondary** covers outline-style actions like "Show All News" or "Find Installer," proposed as an unfilled variant sharing the primary blue for text and border, unobserved in live markup but consistent with typical dual-CTA hero patterns.

**text-input** models newsletter/search fields; background, border, and padding are inferred defaults since no explicit form styling was present in the supplied CSS.

**nav-bar** uses the one directly observed layout token, `--nav-height: 60px`, giving a confirmed height; background and typography weight are inferred from the general white-canvas, medium-weight text pattern.

**product-card** represents the charger grid ("Grizzl-E Classic," "Duo Connect," etc.), pairing a card surface color with title/price/meta type from the observed body-l-medium, title-md, and body-sm classes; card geometry (radius, padding) is proposed.

**hero** models the homepage banner ("Charge Smarter at Home"), using the darkest observed ink as a proposed dark hero treatment; no live hero styling was confirmed, so background choice is an inferred interpretation rather than an extracted value.

**footer** reflects the deep multi-column footer (Services/Support/Company) implied by the text content; dark ink background and muted-gray link color are proposed, not confirmed from CSS.

**badge** covers small labels like "Most Popular," "For 2 EVs," or "Portable" seen tagging products; a soft blue pill is proposed using the observed light-blue tint and deep-blue ink pairing already present in the palette.

**search** is a proposed pattern for site/product search, not confirmed present, styled consistent with the neutral surface-soft background used elsewhere.

**spec-callout** is a category-specific component for charger spec highlights (amperage, temperature range, charge time) seen in the "Fast, Easy Home Charging" section; styled as a soft card with primary-blue accent text for key numbers like "~7.5 hours" or "-30°C to +50°C."

## Responsive Behavior

Proposed breakpoints (not measured): mobile ≤ 640px, tablet 641–1024px, desktop ≥ 1025px. Nav collapses to a hamburger/menu button below tablet width, given the fixed 60px nav-height token suggests a persistent compact bar across breakpoints. Product grids are recommended to shift from a single column (mobile) to 2–3 columns (tablet) to 4 columns (desktop). Touch targets for buttons and badges should maintain a minimum 44px hit area even where visual padding is smaller (e.g., the 11–13px body/caption scale). This section is a recommendation based on common patterns for the observed utility-class system, not an observed mobile layout.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived from static CSS/text extraction only; no rendered layout, hover/focus/active states, animations, or real mobile breakpoints were observed. Color role assignments (primary brand blue, rose and emerald as status accents) are inferred from repetition and typical e-commerce conventions, not from confirmed brand guidelines. Typography sizes for display-xl, display-md, and the "proposed" button-md/caption values extend beyond the small observed 11–24px range and should be treated as extrapolated, not measured. The nav-bar height (60px) is the only confirmed layout dimension; all other spacing, radius, and component padding values are proposed defaults from the design system, not extracted measurements. Font availability, licensing, and whether Inter is self-hosted or loaded via a third-party service were not verified from the supplied evidence.
