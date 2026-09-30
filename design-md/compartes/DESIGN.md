---
version: alpha
name: "Compartes"
source_url: "https://compartes.com"
captured_at: "2026-09-29T03:55:25.314562+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Compartés presents itself as a heritage Los Angeles chocolatier (est. 1950) repositioned as a modern luxury-gifting brand, evidenced by CSS variables named --color-cocoa, --color-chocolate, and --color-cream-tint, and by button/body classes built on the Figtree sans-serif. The observed palette centers on deep umber-browns (#31261d, #1a1612) against warm off-white canvases (#fefefd, #f9f6f0, #f2e9db), with a muted tan (#94795d) for secondary text and hairlines, and a warm gold (#c9a75a, #e6cd8f) reserved for accents befitting "award-winning" and "private reserve" language. A burgundy (#622128) and a deep navy (#101c40) also appear in the palette; their exact UI role is unmeasured, so they are treated here as inferred seasonal/accent colors rather than primary brand colors. Typography pairs the utilitarian Figtree for UI/body copy with Adobe Kepler serif families (display, subhead, caption, with Georgia/Charter/Palatino fallbacks) for editorial headings, matching the site's "House of Compartés" storytelling tone. Notably, --radius-scale is set to 0 in the observed CSS, flattening most corners except a pill-shaped filter radius (9999px) — this interpretation keeps a broader rounded scale available but flags it as proposed beyond those two confirmed states.

colors:
  primary: "#31261d"
  ink: "#1a1612"
  canvas: "#fefefd"
  body: "#31261d"
  muted: "#94795d"
  hairline: "#1a16121a"
  surface-soft: "#f2e9db"
  surface-card: "#f9f6f0"
  on-primary: "#fefefd"
  accent-gold: "#c9a75a"
  accent-gold-soft: "#e6cd8f"
  accent-burgundy: "#622128"
  accent-navy: "#101c40"
  overlay-dark: "#00000080"
typography:
  display-xl: {fontFamily: "'kepler-std-display', Georgia, serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'kepler-std-subhead', Georgia, serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.3px"}
  title-md: {fontFamily: "'Figtree', sans-serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0"}
  body-md: {fontFamily: "'Figtree', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0.01em"}
  body-sm: {fontFamily: "'Figtree', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0"}
  caption: {fontFamily: "'kepler-std-caption', Palatino, serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.05em"}
  button-md: {fontFamily: "'Figtree', sans-serif", fontSize: "11.5px", fontWeight: 550, lineHeight: 1, letterSpacing: "0.1em"}
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
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    height: "68px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    borderColor: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  customization-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.accent-gold}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** renders the dark cocoa-brown fill (`#31261d`) with cream text, uppercase Figtree label, and letter-spacing matching the observed `--button-cta-tracking` variable; the observed `.btn:hover` rule darkens the background, so a hover state to `{colors.ink}` is proposed but not separately tokenized here.

**button-secondary** is an outlined variant for lower-emphasis actions (e.g., "Explore →" links), using the same ink-brown for border and text on a transparent fill; hover/focus fill behavior is proposed, not observed.

**text-input** uses the soft card surface and a faint hairline border, sized for compact concierge/contact forms; focus-ring styling was not present in the supplied CSS and is therefore left undefined.

**nav-bar** reflects the two observed `--nav-h` states (68px expanded, 54px alternate), suggesting a collapsing header on scroll; exact collapse trigger and mobile drawer behavior are inferred from variable names only, not confirmed interaction.

**product-card** groups chocolate-bar/truffle/box imagery with a title in Figtree and a thin hairline border on the warm card surface (`#f9f6f0`), appropriate for the dense collection grids described in the page content.

**hero** uses the largest Kepler-serif display size on the soft cream background, matching the editorial "Discover Our Story" / seasonal-campaign banners referenced in the text; exact hero image treatment is not in the CSS evidence.

**footer** inverts to the primary cocoa-brown with cream text, consistent with `.btn` inversion logic seen elsewhere, housing concierge contact details and legal/social links.

**badge** is a small pill using the gold accent, proposed for "New," "Sale," or "Limited Edition" labels seen throughout the merchandising copy; no literal badge selector was present in evidence.

**search** takes the pill radius token (`--radius-filter: 9999px`), the one confirmed rounded value beyond zero, applied here to a search/filter field consistent with the flavor/diet filter chips mentioned in navigation copy.

**customization-panel** is the category-appropriate addition for Compartés' heavy emphasis on "Custom Chocolate" and corporate branding (logos, colors, proofs); it uses a gold border to distinguish bespoke-gifting sections from standard product browsing, though its visual treatment is proposed rather than directly observed.

## Responsive Behavior

| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column stacks; nav collapses to icon/menu; touch targets ≥44px |
| Tablet | 640–1024px | 2-column product grids; nav-bar may switch between the two observed heights |
| Desktop | 1024–1400px | Grid widths approach the observed `--width-1400` container |
| Wide | ≥1400px | Content capped near `--width-1600`; generous section spacing (`{spacing.section}`) |

This table is a recommendation based on the presence of width/nav CSS variables, not measured rendered behavior. Mobile menu, hamburger animation, and gesture support were not present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from a static CSS/text snapshot only; no rendered layout, computed styles, or interaction states were observed. The mapping of `--color-cocoa` vs `--color-chocolate` to specific hex values is inferred from naming and hover-darkening convention, not confirmed. Burgundy (`#622128`) and navy (`#101c40`) appear in the palette but their functional role (seasonal theme, badge, or unused legacy token) is unverified. Rounded-corner values beyond `0` (observed `--radius-scale: 0`) and the pill `9999px` filter radius are proposed defaults, not evidenced. All pixel sizes for typography not explicitly present in the CSS (e.g., display-xl, display-md, title-md) are proposed, editorially consistent estimates. Kepler serif font family availability, licensing, and actual glyph rendering were not verified — Georgia/Charter/Palatino fallbacks are assumed per the CSS fallback stack. No mobile menu, hover, focus, or form-validation states were observed; all such states above are labeled proposed.
