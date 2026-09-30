---
version: alpha
name: "Three Spirit"
source_url: "https://threespiritdrinks.com"
captured_at: "2026-09-28T10:05:51.163791+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Three Spirit's observed palette centers on a warm off-white canvas (#f5f6ed) paired with near-black ink (#202020) for text, matching the site's CSS custom-property scheme for background and primary text. A saturated magenta-pink (#ff79f1) drives primary buttons and accent moments, set against dark (#202020) and light (#ffffff) surfaces for secondary buttons and cards. Supporting neutrals (#cbcbcb, #dedede, #c8c8c8, #777777) cover disabled states, hairlines, and muted text, while deep plum (#5c1162, #3a0d2e) and botanical greens (#3dbf2a, #57b847, #2fa81e) appear in the palette and are inferred here as elixir-category accent colors (Nightcap/plum, Social/green-adjacent) rather than confirmed UI roles.
  Typography is observed directly from CSS variables: 'PPMuseum' serves as the heading/accent face with a serif generic fallback, and 'ABCFavoritMono' serves as the body, subheading, and button face with a monospace generic fallback — both fallbacks are the generic keywords present in the supplied evidence, not specific named fallback fonts. Observed type scale values (11–64px) inform the proposed scale below. Buttons use pill radius (9999px, observed) and uppercase text-transform. This interpretation proposes a clean, editorial-meets-functional aesthetic: warm paper-like backgrounds, monospace utility text, and a single vivid accent color reserved for primary calls to action, echoing the brand's "botanical alchemy" positioning without inventing unobserved visual detail.

colors:
  primary: "#ff79f1"
  ink: "#202020"
  canvas: "#f5f6ed"
  body: "#202020"
  muted: "#777777"
  hairline: "#dedede"
  surface-soft: "#f3f0ed"
  surface-card: "#ffffff"
  on-primary: "#202020"
  on-dark: "#ffffff"
  accent-plum: "#5c1162"
  accent-plum-deep: "#3a0d2e"
  accent-green: "#3dbf2a"
  accent-green-alt: "#57b847"
  border-strong: "#343439"
  disabled-bg: "#cbcbcb"
  disabled-border: "#00000080"
  overlay-scrim: "#00000066"
typography:
  display-xl: {fontFamily: "'PPMuseum', serif", fontSize: "64px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "normal"}
  display-md: {fontFamily: "'PPMuseum', serif", fontSize: "40px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "normal"}
  title-md: {fontFamily: "'PPMuseum', serif", fontSize: "28px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "normal"}
  body-md: {fontFamily: "'ABCFavoritMono', monospace", fontSize: "16px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "normal"}
  body-sm: {fontFamily: "'ABCFavoritMono', monospace", fontSize: "14px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "normal"}
  caption: {fontFamily: "'ABCFavoritMono', monospace", fontSize: "12px", fontWeight: 400, lineHeight: 1.04, letterSpacing: "normal"}
  button-md: {fontFamily: "'ABCFavoritMono', monospace", fontSize: "15px", fontWeight: 400, lineHeight: 1, letterSpacing: "normal"}
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
    padding: "{spacing.xs} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.lg}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xxl}"
  badge:
    backgroundColor: "{colors.accent-plum}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  ingredient-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
**button-primary**: The pill-shaped magenta button (#ff79f1 background, #202020 text) is the observed primary CTA pattern, drawn directly from the `--ia-color-primary-button-*` variables; hover-state color swap to dark background is observed in CSS but exact transition timing is proposed.

**button-secondary**: A dark-fill/light-text inversion of the primary button, matching the `--ia-color-secondary-button-*` variables, used for lower-emphasis actions like "Shop all" links.

**text-input**: Proposed form field styling using the monospace body font and a light hairline border, consistent with the utilitarian, editorial feel of the observed typography but not directly measured from a form element.

**nav-bar**: Proposed top navigation using the canvas background and ink text, sized to the observed `--ia-page-padding-x: 64px` horizontal padding; sticky/scroll behavior is not observed.

**product-card**: Proposed card pattern for elixir/wine listings (e.g., "Livener 50cl £25.99") using a white surface against the warmer canvas, since product content in the excerpt implies grid-style listings; exact card dimensions are not observed.

**hero**: Proposed full-width hero using the largest observed heading size (64px desktop) for statements like "For feeling, flavour, and ritual"; background imagery/video is plausible given the brand's lifestyle tone but not confirmed in evidence.

**footer**: Proposed dark-ink footer inverting the site's light canvas, for contrast and to anchor secondary links (Learn, Impact Report, Stockists); not a directly observed layout.

**badge**: Proposed small pill label using the plum accent, suited to callouts like "Certified B-Corp" or "Non-GMO Project Verified" mentioned in page text; color role is inferred, not confirmed as a badge color in CSS.

**search/store-locator**: Proposed pill-shaped search/store-locator control referencing the "store locator" and "stockists" text found on the page; softly tinted background distinguishes it from primary actions.

**ingredient-tile**: A category-appropriate component for the "Rooted in botanical alchemy" ingredient list (Cacao, Lion's Mane, Schisandra, etc.), proposed as a soft-surface tile grid using body-sm copy beneath a serif title.

## Responsive Behavior
Recommendation only — no measured breakpoints were captured:
| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column stacks, nav collapses to menu icon, buttons full-width |
| Tablet | 640–1023px | 2-column product/ingredient grids, nav-bar padding reduces from {spacing.xxl} |
| Desktop | ≥1024px | Multi-column grids, desktop type scale (e.g., 64px display) applies, {spacing.xxl} page padding |

Touch targets should meet a 44px minimum height; the observed `--ia-button-min-height-desktop: 48px` suggests buttons already satisfy this on desktop, but mobile sizing is not confirmed. Navigation collapse into a hamburger/drawer pattern is a standard proposal, not an observed interaction.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS variables and a page-text excerpt only; no rendered layout, DOM structure, or interaction states were observed. Hover, focus, active, and disabled visuals beyond the explicit `.ia-button:disabled` rule are proposed. Breakpoint values, grid structures, and mobile navigation behavior are inferred conventions, not measured. Semantic assignment of plum and green palette entries to specific elixir/wine categories is an inference from adjacent product copy, not a confirmed design token mapping. 'PPMuseum' and 'ABCFavoritMono' are custom fonts whose licensing and public availability were not verified; only their generic CSS fallback keywords (serif, monospace) are used per instruction. All hex values are reused directly from the supplied observed palette.
