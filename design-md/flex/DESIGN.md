---
version: alpha
name: "Flex"
source_url: "https://flexpowertools.com"
captured_at: "2026-09-28T10:13:39.395409+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Flex Power Tools presents itself through a stark, high-contrast palette: pure black (#000000) and white (#ffffff) frame the layout, punctuated by an aggressive safety-green accent (#00ff00, with a hover state at #00f200) used for the store's `--swiper-theme-color` and `.btn-primary` background. This green-on-black combination signals jobsite energy and battery-platform branding (the "24V" system callouts). Supporting grays (#c8c8c8, #dadada, #6c6c6c, #767676, #f4f4f4) appear across disabled states, secondary buttons, and select-menu chrome, and are mapped here to muted text, hairlines, and soft surfaces — this mapping is inferred from usage context, not confirmed as a formal design-token system.

  Typography centers on 'Poppins' for body copy and all heading levels (`.h1`-`.h5`), set bold and uppercase for headings, with body text carrying an unusually heavy 600 weight. 'Roboto Condensed' is reserved for interactive elements — buttons and select controls — at 700 weight, uppercase, tight line-height, giving CTAs a compact, technical feel appropriate to an industrial tools brand. Numeric type scale values beyond what's observed in buttons (16px/15px line-height) are proposed extrapolations, not measured page observations.

colors:
  primary: "#00ff00"
  primary-hover: "#00f200"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#6c6c6c"
  muted-alt: "#767676"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#eeeeee"
  on-primary: "#000000"
  on-dark: "#c8c8c8"
  disabled: "#c8c8c8"
  disabled-dark: "#6c6c6c"
  overlay-dark: "#000000"
typography:
  display-xl: {fontFamily: "'Poppins', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Poppins', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Poppins', sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "'Poppins', sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Poppins', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Roboto Condensed', sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 15px, letterSpacing: 0.5px}
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
    hover: {backgroundColor: "{colors.primary-hover}"}
    disabled: {backgroundColor: "{colors.disabled}", accentBar: "{colors.disabled-dark}"}
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    textColor-onDark: "{colors.canvas}"
    accentColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xs} {spacing.sm}"
    border: "none"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    focus: {borderColor: "{colors.primary}"}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
    activeIndicator: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    ctaComponent: "button-primary"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkHover: "{colors.primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-alt}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  rating-badge:
    backgroundColor: "{colors.overlay-dark}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** — The site's dominant CTA style, observed directly from `.btn-primary`: black uppercase Roboto Condensed text on a bright green (#00ff00) fill, no border, 44px height. Hover darkens toward #00f200; disabled state drops to gray (#c8c8c8) with a darker gray accent bar (#6c6c6c). This is the highest-confidence component in the spec.

**button-secondary** — Inferred from `.btn-secondary` and its `--white`/`--fluroscent` modifiers: a border-less, background-less text button sharing the same Roboto Condensed uppercase treatment, with color variants for dark and light backgrounds. Exact padding/rounding is proposed, as no box metrics were observed.

**text-input** — Not directly observed in the supplied CSS; proposed using the site's hairline gray and body typography to remain visually consistent with the black/white/green system. Focus-state green border is a proposed pattern echoing the primary accent.

**nav-bar** — Proposed structure based on the extensive product/category taxonomy in the page text (Tools, Attachments, Combo Kits, Trades, Support, etc.), styled with the observed white canvas and black ink; no header CSS rules were supplied, so layout specifics are inferred.

**product-card** — Proposed container for featured-tool listings (e.g., drill driver, circular saw, reciprocating saw kits seen in page text), using observed hairline borders and card-surface grays, with title/body typography drawn from the confirmed heading and body styles.

**hero** — Proposed full-bleed dark section reflecting the jobsite video/banner content described in the page text ("Power the Jobsite," "Stacked Lithium"), using black background, white text, and green accent call-outs consistent with observed button coloring.

**footer** — Proposed dark footer matching the black canvas seen in `.f-selectmenu-button` and `[data-bv-show]` dark chrome, with muted gray body text (#c8c8c8, as observed in the select-menu text color) and green link-hover states for brand consistency.

**badge** — Proposed light-gray pill using `surface-card` and `muted` tones, intended for labels like "New!" or category tags referenced in the page text (e.g., "New! 3-DRAWER Tool Box").

**search** — Proposed light input treatment for the site's visible "Search Search" control, styled consistently with text-input; no dedicated search CSS was supplied.

**rating-badge** — Directly grounded in observed CSS: `[data-bv-show=inline_rating]` shows a black (#000000), 32px-tall, 16px-radius pill with green (#0f0) bold text — used here for Bazaarvoice-style product review ratings, a category-relevant trust signal for power tools.

## Responsive Behavior
Recommended breakpoints (not measured from live site): mobile ≤640px, tablet 641–1024px, desktop 1025–1920px (the CSS `max-width:1920px` on `body` suggests a capped, centered desktop container). Nav and category menus should collapse to a hamburger/drawer pattern below 1024px given the deep product taxonomy observed in page text. Touch targets should be a minimum 44px, matching the observed `.btn-primary` height. All breakpoint values and collapse behavior are proposed conventions, not confirmed site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS and text extraction only; no live rendering, DOM inspection, or interaction testing was performed. Semantic color roles (muted, hairline, surface-soft/card, on-dark) are inferred from selector context and usage patterns, not from an explicit design-token source. Font sizes for headings, cards, hero, and inputs are proposed estimates — only the `.btn-primary` (16px/15px) and select-menu (18px) sizes were directly observed. Mobile navigation, drawer, and collapse behavior were not observed and are proposed conventions only. 'Poppins' and 'Roboto Condensed' availability/licensing (self-hosted vs. Google Fonts) was not verified. Rounded-corner values are a generic proposed scale, as no `border-radius` values appeared in the supplied CSS evidence.
