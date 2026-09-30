---
version: alpha
name: "Billykirk"
source_url: "https://billykirk.com"
captured_at: "2026-09-29T04:05:46.310904+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Billykirk presents itself as a heritage American leather and canvas goods
  maker (est. 1999), and the extracted CSS reflects a restrained, workshop-like
  aesthetic rather than a flashy retail theme. The core color system is built
  from a warm off-white canvas (#f7f6f2), black ink text, and a single dark
  oxblood/umber accent (#362424) that recurs consistently across the Judge.me
  review widget variables and the theme's color-scheme accent token — this is
  treated here as the brand primary, though its exact application to buttons
  versus links is inferred rather than directly observed. Supporting neutrals
  (#dddddd, #f4f4f4, #ffffff, #6b7280-style grays) suggest a grayscale-first UI
  with the brown accent reserved for emphasis, reviews, and interactive states.
  Typography evidence includes Arbutus Slab, a slab serif well suited to a
  leather-goods heading voice, alongside Jost and Nunito Sans as likely
  sans-serif body/UI faces; other listed families (Roboto, Segoe UI, social
  icon fonts) are treated as system fallbacks or third-party app fonts, not
  brand type. Interface geometry (0px radii on observed buttons) points to a
  squared-off, utilitarian button language, which this spec extends
  conservatively into a small radius scale for proposed components.

colors:
  primary: "#362424"
  ink: "#000000"
  canvas: "#f7f6f2"
  body: "#333333"
  muted: "#6b7280"
  hairline: "#dddddd"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-strong: "#cccccc"
  sale-accent: "#ad0000"
  highlight: "#fbcd0a"
typography:
  display-xl: {fontFamily: "'Arbutus Slab', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Arbutus Slab', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Jost', sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Nunito Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Nunito Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Jost', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.4px}
  button-md: {fontFamily: "'Jost', sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  material-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"

## Components
- **button-primary**: The main call-to-action treatment (Add to Cart, Shop Now), using the dark oxblood accent as fill with white text, matching the `--jdgm-write-review-bg-color: #362424` pattern seen on the review widget. Square corners are proposed to match the observed `border-radius: 0px` on other themed buttons; hover states are proposed, not observed.
- **button-secondary**: An outlined variant for lower-emphasis actions (e.g. "View Details"), following the `.theme-button--secondary` rule set which explicitly swaps to background/border/text driven by the color-scheme text token (black) rather than the accent — hover-to-accent color shift is defined in CSS and reused here.
- **text-input**: Form fields (newsletter signup, search) proposed with a light hairline border and card-white background; no explicit input styling was present in the supplied CSS, so sizing and radius are proposed.
- **nav-bar**: A canvas-colored header bar referencing the site's sticky header behavior (`--sticky-header-height: 66px`) and logo width tokens (130–180px), implying a compact, logo-led horizontal navigation; exact link layout is inferred.
- **product-card**: Grid tile for collection/category pages (Cordovan, Satchels, Wallets, etc.), with a white card surface, hairline divider, and title/price typography pairing; card shadow/elevation is not evidenced and thus omitted.
- **hero**: A full-width introductory banner using the soft off-white surface and large slab-serif display type, appropriate to the "USA based Leather & Canvas Goods... Since 1999" positioning; copy alignment and imagery treatment are proposed.
- **footer**: Uses the dark accent as background with white text for contrast, consistent with the `on-primary` token; sitemap columns (Shop, About, Journal) are inferred from the observed navigation taxonomy, not from footer-specific CSS.
- **badge**: A small sale/promo label using the observed red (#ad0000) as an inferred sale color, since no explicit `.badge` CSS was supplied; this mapping should be treated as a plausible convention, not a confirmed one.
- **search**: A modal or inline search field referenced by the repeated "Search Submit" text in page copy; visual styling is proposed to match text-input.
- **material-tag**: A category-appropriate pill component for labeling leather type or collection (e.g. "Cordovan," "Canvas"), reflecting the brand's material-forward merchandising (Cordovan is a named collection); this is a proposed, unobserved pattern suited to a leather-goods catalog.

## Responsive Behavior
This is a recommended structure, not measured site behavior:

| Breakpoint | Width        | Layout notes (proposed) |
|-----------|--------------|--------------------------|
| xs        | 0–479px      | Single-column product grid, collapsed hamburger nav |
| sm        | 480–767px    | 2-column product grid, sticky header retained |
| md        | 768–1023px   | 2–3 column grid, inline search reveal |
| lg        | 1024–1279px  | Full horizontal nav, 3–4 column grid |
| xl        | 1280px+      | Max-width container, 4 column grid |

Touch targets for buttons and nav links should be at least 44×44px. The header's sticky height (`66px`, observed as a CSS variable) should be preserved at all breakpoints. Mobile nav collapse into a drawer/menu is a standard Shopify-theme convention here, not a confirmed observation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Colors were extracted from static CSS custom properties and computed rules; some hex values (e.g. social icon brand colors like Facebook/Twitter/Pinterest blue) were excluded from the palette as non-brand and are not part of this spec.
- The primary accent (#362424) is inferred from Judge.me widget variables and the `--color-scheme-accent` token; its precise application across all interactive states (links, hover, focus) was not directly observed in interaction.
- No explicit numeric type scale was supplied (`--type-scale-n0/n2/n7` are undefined tokens), so all font sizes are proposed, not measured.
- Border-radius values beyond the observed `0px` button case are proposed defaults, not confirmed site behavior.
- Mobile/responsive layout, hover/focus states, and animation timing were not observed directly; all interaction and breakpoint guidance is a design recommendation.
- Custom font availability, licensing, and actual font-weight rendering (Arbutus Slab, Jost, Klein Regular, Glacial) were not verified; fallback stacks are assumed generic sans/serif.
- Sale/highlight color roles (#ad0000, #fbcd0a) are inferred from generic palette presence, not from confirmed badge or promotional CSS selectors.
