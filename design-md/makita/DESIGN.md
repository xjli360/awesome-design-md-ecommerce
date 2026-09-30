---
version: alpha
name: "Makita"
source_url: "https://makitatools.com"
captured_at: "2026-09-28T04:19:54.764562+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Makita's observed CSS evidence surfaces a legacy jQuery UI theme rather than
  the primary brand stylesheet, so this interpretation treats the small set of
  directly observed brand signals — the teal #008290, the secondary teal
  #67b2b1, near-black #1d1716, and layered neutrals from #f5f5f5 through
  #999999 — as the anchor palette, while jQuery UI chrome colors (#cccccc,
  #aaaaaa, #212121, #cd0a0a) are treated as legacy widget artifacts, not brand
  intent. The custom MakitaSans and MakitaSansCondensed family names confirm a
  proprietary condensed/standard sans pairing typical of industrial tool
  brands: condensed weights for punchy headlines and model numbers, regular
  weights for body copy, with Arial/Helvetica/Verdana as system fallbacks.

  The proposed system leans into an industrial, high-contrast, tool-catalog
  aesthetic: teal as the singular brand accent against black/white/gray
  neutrals, sharp low-radius corners suggesting tool housings and metal
  fasteners, and a dense grid appropriate for large SKU catalogs. Color role
  assignments (ink, muted, hairline, surface tiers) are inferred from
  frequency and typical UI function, not confirmed by page context.

colors:
  primary: "#008290"
  secondary: "#67b2b1"
  ink: "#1d1716"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#d6d6d6"
  surface-soft: "#f5f5f5"
  surface-card: "#e6e6e6"
  on-primary: "#ffffff"
  accent-red: "#eb1c24"
  link: "#0044cc"
  focus-ring: "#5e9ed6"
  warning: "#ffa500"
  border-strong: "#999999"
typography:
  display-xl: {fontFamily: "MakitaSansCondensed_Black, Arial, sans-serif", fontSize: 48px, fontWeight: 900, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "MakitaSansCondensed_ExtraBold, Arial, sans-serif", fontSize: 32px, fontWeight: 800, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "MakitaSans_SemiBold, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "MakitaSans_Regular, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "MakitaSans_Regular, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "MakitaSans_Light, Arial, sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "MakitaSansCondensed_SemiBold, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.5px}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    focusBorder: "{colors.focus-ring}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeIndicator: "{colors.primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    accent: "{colors.primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.secondary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    rowHairline: "{colors.hairline}"
    labelTypography: "{typography.body-sm}"
    valueTypography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** uses the observed teal (#008290) as a solid fill with white text, sized for catalog CTAs like "Add to Cart" or "Find a Dealer." Hover/pressed states are proposed, not observed, and would likely darken the teal slightly.

**button-secondary** proposes an outlined variant for lower-emphasis actions (e.g., "Compare," "View Specs"), keeping the teal as the sole accent so the interface reads as single-hue-branded against neutral chrome.

**text-input** models a simple bordered field using the light hairline gray, with a blue focus ring drawn from the observed #5e9ed6 — this focus color is inferred from adjacent palette values, not confirmed as an actual focus style on the live site.

**nav-bar** is a proposed white header bar with dark text and a teal underline/indicator for the active section, consistent with an industrial catalog site's need for dense top-level navigation across tool categories.

**product-card** presumes a light gray card surface for SKU tiles in listing grids, with condensed-weight titles and standard-weight pricing/spec text, bordered by the hairline gray for grid separation.

**hero** proposes a near-black banner treatment with a large condensed display headline and teal accent detailing, appropriate for tool-launch or campaign banners; no actual hero markup or imagery was observed.

**footer** mirrors the hero's dark background for a bookended dark/light rhythm, with secondary-teal links for wayfinding and small body text for legal/copyright rows — a common pattern, not a confirmed layout.

**badge** proposes a small red pill (from the observed #eb1c24) for stock/status flags such as "New" or "Sale," since red appears in the palette but its actual usage context on the site is unverified.

**search** and **spec-table** round out catalog-specific needs: a soft-gray search field for product lookup, and a specification table pattern (label/value rows separated by hairlines) suited to power-tool datasheets — both are inferred utility components appropriate to the category, not observed markup.

## Responsive Behavior

Recommended (not measured) breakpoints:

| Breakpoint | Width | Layout intent |
|---|---|---|
| mobile | <480px | single-column, stacked nav, full-width cards |
| tablet | 480–1024px | 2-column product grid, collapsed nav into drawer |
| desktop | 1024–1440px | 3–4 column grid, persistent top nav |
| wide | >1440px | max-width container, extra gutter, 4+ column grid |

Touch targets should be at least 44×44px for buttons and nav items. Primary navigation is expected to collapse into a hamburger/drawer pattern below tablet width. All figures are proposed defaults for a tool-catalog site, not measured from Makita's live responsive behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Supplied CSS evidence is dominated by a legacy jQuery UI theme file; no first-party layout, grid, or component CSS was provided, so all component structures above are inferred/proposed, not observed.
- Color-to-role mapping (ink, muted, hairline, surface tiers) is inferred from typical frequency/usage patterns in UI frameworks, not confirmed against actual Makita page regions.
- Font sizes, weights, letter-spacing, and line-heights in the typography scale are proposed design values; only the font-family *names* (MakitaSans_*, MakitaSansCondensed_*) were observed in evidence, with no confirmed size/weight pairings.
- Custom font availability, licensing, and actual rendering (e.g., whether MakitaSansCondensed_Black is loaded/used for headlines) were not verified.
- No responsive breakpoints, hover/focus/active states, or mobile navigation behavior were observed; all such guidance above is a recommendation only.
- Red, orange, and blue palette entries (#eb1c24, #ffa500, #0044cc, #5e9ed6) may originate from unrelated legacy or third-party widget styling rather than current brand usage; their assigned roles here are speculative.
