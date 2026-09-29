---
version: alpha
name: "Davinci Baby"
source_url: "https://davincibaby.com"
captured_at: "2026-09-28T09:06:04.367746+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  DaVinci Baby's storefront CSS shows a soft, pastel nursery palette built around a pale cyan canvas (#ddf7fc) and near-white header band (#f1fcfe), paired with a muted navy text color (#2e435a) used for both body copy and header labels. Primary calls-to-action use a yellow-green fill (#ddeb5a) with a large 31.5px radius that renders as a pill, hovering to a light sky blue (#98e8ff); a separate --accent-color token (#ff4b24) exists in the root variables but was not observed applied to a visible button, so it is treated here as a reserved accent for sale/callout use. Secondary buttons and links use plain black/white with sharper 6px corners, suggesting two coexisting button languages (soft pill primary vs. flat outline secondary). Headlines use a display face, "Bigola Display," set in lowercase at a modest 24px, while body and navigation copy use "Goldplay" with a very small 9px header label size, implying a compact, understated type hierarchy rather than bold display marketing type. Supporting swatches (gold, peach, deep blue/teal) likely serve product imagery, swatches, or category tags rather than UI chrome, and are mapped here as inferred decorative/secondary colors pending live verification.

colors:
  primary: "#ddeb5a"
  accent: "#ff4b24"
  ink: "#1a172c"
  body: "#2e435a"
  canvas: "#ddf7fc"
  muted: "#8a8a8a"
  hairline: "#dddddd"
  surface-soft: "#f1fcfe"
  surface-card: "#ffffff"
  on-primary: "#2e435a"
  highlight: "#98e8ff"
  gold: "#ffc657"
  peach: "#ffdccf"
  deep-blue: "#1990c6"
  deep-teal: "#136f99"
  near-black: "#121212"
typography:
  display-xl: {fontFamily: "'Bigola Display', sans-serif", fontSize: "24px", fontWeight: 400, lineHeight: 1.0, letterSpacing: "0.2px"}
  display-md: {fontFamily: "'Bigola Display', sans-serif", fontSize: "20px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "0.2px"}
  title-md: {fontFamily: "'Goldplay', sans-serif", fontSize: "16px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0em"}
  body-md: {fontFamily: "'Goldplay', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "normal"}
  body-sm: {fontFamily: "'Goldplay', sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "normal"}
  caption: {fontFamily: "'Goldplay', sans-serif", fontSize: "9px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0em"}
  button-md: {fontFamily: "'Goldplay', sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: "normal", letterSpacing: "normal"}
rounded:
  none: 0px
  xs: 2px
  sm: 6px
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
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.near-black}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    hairline: "{colors.hairline}"
    height-desktop: "100px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    accentColor: "{colors.gold}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    ctaBackground: "{colors.primary}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.deep-teal}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** — The dominant CTA pattern observed in CSS: yellow-green fill (#ddeb5a), navy text, and a 31.5px radius that produces a pill shape at typical button heights, here generalized to `rounded.full`. Hover state (#98e8ff) is directly observed. Proposed states: focus ring and disabled opacity are not observed and are inferred conventions.

**button-secondary** — A flatter, high-contrast alternate button (white background, black text/border, 6px radius) observed for secondary actions, inverting to solid black on hover. Likely used for "continue shopping," filters, or less-emphasized actions; exact placement is inferred.

**text-input** — No dedicated input CSS was captured, so field styling (border, radius, padding) is proposed by convention, using the observed hairline gray and card white background to stay consistent with the button/card system.

**nav-bar** — Header uses a distinct near-white surface (#f1fcfe) versus the pale cyan page canvas, with a very small 9px semibold label size and a 100px desktop height variable, both directly observed via CSS custom properties. Mobile collapse behavior (hamburger, drawer) was not observed.

**product-card** — Proposed pattern for crib/dresser/chair grid tiles, using white card surface against the cyan canvas for contrast, with gold as an inferred accent for price/sale callouts. Card radius and internal spacing are proposed, not measured from live grid markup.

**hero** — Home content ("more joy, less worry," "the crib for every milestone") suggests large lowercase display headlines on the canvas color; typography maps to the observed Bigola Display h1 style. Copy layout (image position, overlay) is not observed and is inferred.

**footer** — Assumed to share the header's soft surface tone and hairline dividers for visual continuity; no footer-specific selectors were present in the supplied evidence, so structure/copy hierarchy is proposed.

**badge** — Sale/new-drop labels ("New Drop!", "Sale") likely use the reserved accent-color token (#ff4b24) as a pill badge; this mapping is inferred since no badge-specific selector was captured.

**search** — Header includes a "Search" affordance in page text; styling is proposed to match the pill/rounded language of primary buttons, using card white and hairline border for input contrast against the cyan canvas.

**trust-badge** — Category-appropriate component for nursery furniture: safety/certification messaging (GREENGUARD Gold, CPSC/ASTM testing, lead/phthalate-safe paint) is prominent in page copy. Proposed as a small labeled chip using the deep-teal tone for a "certified/verified" feel, distinct from promotional badges.

## Responsive Behavior

A single root variable (`--screen-break: 768px`) was observed, indicating at least one mobile/desktop breakpoint. Proposed compact scale, extending from that evidence (not measured beyond the single value):

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | < 768px | Header height ~60px (`--header-height`, observed); nav likely collapses to a drawer/menu icon (not observed). |
| desktop | ≥ 768px | Header height 100px (`--header-height-desktop`, observed); horizontal nav assumed. |

Touch targets should follow a minimum 44×44px tappable area for primary/secondary buttons, even though the observed button padding (8px 23px, 6px 10px) is tighter — this is a proposed accessibility adjustment, not an observed site behavior. Collapse of multi-column product grids to single/double column on mobile is a standard e-commerce recommendation, not confirmed from the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is limited to static CSS custom properties and a subset of rule blocks; full stylesheet, JS-driven states, and live DOM were not inspected.
- Only one breakpoint variable (768px) was observed; tablet/desktop-large behavior is assumed, not measured.
- The root `--accent-color: #ff4b24` has no confirmed applied usage in the supplied rules; its role as badge/sale color is inferred.
- Product-card, hero, footer, search, and trust-badge components are proposed patterns based on page copy and general e-commerce convention, not observed selectors/layout.
- "Des Montilles" appears in the supplied font list but no rule referencing it was provided; it is omitted from typography tokens pending evidence of its actual usage.
- Custom font availability, licensing, and hosting for "Goldplay" and "Bigola Display" were not verified; system fallbacks (Helvetica, Arial, sans-serif) are assumed per standard `font-family` stacking.
- Mobile navigation interaction (drawer, hamburger, search overlay) and hover/focus states beyond the two captured button states were not observed.
- Rounded and spacing scales blend observed values (6px secondary radius, 8px/23px button padding) with conventional proposed increments to complete a usable system.
