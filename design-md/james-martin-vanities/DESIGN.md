---
version: alpha
name: "James Martin Vanities"
source_url: "https://jamesmartinvanities.com"
captured_at: "2026-09-29T04:07:49.453225+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This specification derives from Shopify theme CSS and on-page text for James
  Martin Vanities, a bathroom-vanity and furniture retailer. The observed
  palette centers on near-black text (#242424, #000000) over white and
  off-white canvases (#ffffff, #fcfcfc, #f8f3ec, #faf7f5), with warm neutral
  accents (#b3a284, #e8d2d2) that suit product photography of wood and stone
  vanities. Status colors (#28a745, #dc3545, #eb9247) and a Swiper UI accent
  (#007aff) appear in theme/vendor CSS and are treated as functional rather
  than brand colors. No explicit brand accent hex was present in the supplied
  rules; the primary action color below is inferred from the dominant dark
  neutral used across button and header contexts, not confirmed from a
  captured swatch. Typography is limited to "Open Sans" with "Segoe UI" and
  "helvetica" fallbacks; no display/serif webfont was observed, so headings
  reuse the same sans stack at heavier weights. The interpretation favors a
  quiet, gallery-like layout: generous white space, soft warm-neutral section
  backgrounds, thin hairlines, and restrained button treatments appropriate to
  a luxury home-fixtures catalog.

colors:
  primary: "#242424"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#e6e6e6"
  surface-soft: "#f8f3ec"
  surface-card: "#fcfcfc"
  on-primary: "#ffffff"
  accent-brass: "#b3a284"
  blush: "#e8d2d2"
  cream: "#faf7f5"
  success: "#28a745"
  danger: "#dc3545"
  warning: "#eb9247"
  info: "#54708b"
  interactive-blue: "#007aff"
typography:
  display-xl: {fontFamily: "'Open Sans', 'Segoe UI', helvetica, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Open Sans', 'Segoe UI', helvetica, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Open Sans', 'Segoe UI', helvetica, sans-serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "'Open Sans', 'Segoe UI', helvetica, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Open Sans', 'Segoe UI', helvetica, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Open Sans', 'Segoe UI', helvetica, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.25px"}
  button-md: {fontFamily: "'Open Sans', 'Segoe UI', helvetica, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.6, letterSpacing: "0.5px"}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    height: "80px"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-brass}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  collection-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    captionTypography: "{typography.title-md}"
    padding: "{spacing.lg}"

## Components

**button-primary** is proposed as a solid dark (near-black) fill with white text, matching the theme's `--primary-btn-bg-color` pattern referenced in CSS, though the actual hex behind that variable was not captured; the dark-neutral value is used as a reasonable stand-in.

**button-secondary** mirrors the theme's `.btn--secondary` rule, which explicitly sets a transparent background with a border and text color both equal to the primary button color — this pattern is directly evidenced in the CSS.

**text-input** is a proposed pattern for filters, search, and account forms; border and sizing follow the observed light hairline tone (#e6e6e6) since no input-specific CSS was supplied.

**nav-bar** reflects the observed `.overlay-header` rules forcing a white background; height and border are proposed since no exact header metrics were in the evidence.

**product-card** is proposed for vanity/collection listings (e.g., Addison, Kinnsden, Bellshire), using the near-white card surface and title weight consistent with the sans-serif stack; card imagery would rely on `object-fit: contain` as seen in the CSS.

**hero** models the homepage's large collection-intro banners ("Heirloom Elegance," "The New Nautical") with a warm cream background option, since such tones appear in the palette for editorial sections.

**footer** is proposed as a dark, high-contrast band for support links (customer care email/phone) and legal links (Cookie Policy, Privacy, CA Privacy) that were listed in the page text.

**badge** is a proposed small label (e.g., "2026," "New") using the warm brass tone as a soft brand accent rather than a loud alert color.

**search** reflects the presence of a "Search" navigation action; visual treatment is proposed, not measured.

**collection-tile** is a category-appropriate component for the many named collections (Alicante, Auburn, Brookfield, etc.) shown in navigation, using soft warm backgrounds to differentiate lifestyle imagery blocks.

## Responsive Behavior
Recommended, not measured from live rendering:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <600px | Single-column collection grid, nav collapses to menu icon, touch targets ≥44px |
| tablet | 600–1024px | Two-column product/collection grids, header remains fixed per observed `.sticky-header` classes |
| desktop | 1024–1440px | Multi-column mega-menu (matches long flat collection list in nav), max content width ~1280px |
| wide | >1440px | Hero and lookbook imagery scale up; side padding increases to `{spacing.xxl}` |

Interactive controls (search, cart, nav toggles) should maintain a minimum 44×44px touch target; the mega-menu with dozens of collection names should collapse into an accordion on mobile, per typical patterns for this class of Shopify navigation, though this behavior itself was not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Extraction is static: no rendered screenshots, computed styles, or JavaScript-driven states (hover, mega-menu expansion, cart drawer) were observed.
- The `--primary-btn-bg-color` and related CSS custom properties are referenced but their resolved hex values were not present in the supplied evidence; `primary` is an inferred stand-in from the dark-neutral palette.
- Font weights beyond default (400/600) are assumed for headings; no explicit `font-weight` values for h1–h3 were supplied.
- All numeric type sizes, spacing scale, and rounded values are proposed conventions, not measured from the live site's computed CSS.
- Mobile menu/collapse behavior, cart drawer, and swiper carousel visual states were not observed; only vendor default Swiper CSS variables were present.
- Custom font licensing/availability is not verified; only generic system font names ("Open Sans," "Segoe UI," "helvetica") appeared in the CSS, with standard sans-serif fallback assumed safe.
- Status colors (#28a745, #dc3545, #28a745-adjacent, #eb9247) may originate from third-party Shopify apps rather than core brand styling; their semantic use here (success/danger/warning) is inferred, not confirmed.
