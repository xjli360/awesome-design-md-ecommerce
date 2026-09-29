---
version: alpha
name: "Rode"
source_url: "https://www.rode.com"
captured_at: "2026-09-28T09:34:18.216500+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  RØDE's storefront CSS exposes a neutral, near-monochrome interface built on white canvases (#ffffff) and near-black ink (#14181a, used as --text-default), with a graduated grey system (#5b5e5f, #9c9c9c, #dddddd, #e7e7e8, #f2f2f2, #f9f9f9) handling secondary text, borders and soft surfaces. A saturated indigo (#3e34d3), present with 20% and 10% alpha variants, is the strongest signal of an interactive/primary accent — Tailwind-style alpha suffixes typically mark a token reused for hover states, focus rings or highlighted UI, so it is mapped here as primary (inferred). Button CSS references --action-primary and --action-on-primary as CSS variables without resolved hex values; on-primary is inferred as white given the button-dark inversion pattern (dark background, black text on light). A cluster of saturated hues (#e84751, #fc63a3, #6ab5ed, #7fd649, #eb9341, #59ae31) appears tied to "neon" gradient text classes and hotspot markers, suggesting product-highlight or color-swatch accents rather than core UI color — kept as secondary accents. Typography is inferred primarily from the explicit "Inter" font-family entry with system-ui/Arial/Helvetica fallbacks; only the body-md size (16px/24px/400) is directly observed in CSS, all other sizes are proposed.

colors:
  primary: "#3e34d3"
  primary-soft: "#3e34d333"
  ink: "#14181a"
  canvas: "#ffffff"
  body: "#14181a"
  muted: "#9c9c9c"
  hairline: "#dddddd"
  surface-soft: "#f9f9f9"
  surface-card: "#f2f2f2"
  on-primary: "#ffffff"
  border-dark: "#262627"
  text-secondary: "#5b5e5f"
  accent-info: "#6ab5ed"
  accent-success: "#59ae31"
  accent-warning: "#eb9341"
  accent-danger: "#e84751"
  accent-pink: "#fc63a3"
typography:
  display-xl: {fontFamily: "Inter, system-ui, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Inter, system-ui, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.375px}
  title-md: {fontFamily: "Inter, system-ui, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.5, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Inter, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.15px}
  button-md: {fontFamily: "Inter, system-ui, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0.1px}
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
    backgroundColor: "{colors.on-primary}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    mutedTextColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.border-dark}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  color-swatch-selector:
    backgroundColor: "{colors.surface-card}"
    activeBorderColor: "{colors.primary}"
    inactiveBorderColor: "{colors.hairline}"
    rounded: "{rounded.full}"
    size: "{spacing.xl}"
    gap: "{spacing.xs}"

## Components
**button-primary** models the observed `.btn` rule, which sets background and border to `var(--action-primary)` with `var(--action-on-primary)` text; hover inverts the pair per the `button:hover,.btn:hover` rule. Mapped to the inferred indigo primary token.

**button-secondary** is a proposed outline variant not directly present in the CSS excerpt, inverting the primary button for lower-emphasis actions such as "Learn More" links alongside the observed `.btn-learnmore` muted-grey text treatment.

**text-input** is proposed; no form-field CSS was supplied, so border, radius and padding follow the site's general hairline/spacing tokens rather than measured values.

**nav-bar** is inferred from the presence of a persistent product/utility navigation implied by the page text ("Products Apps User Guides Support…"); background and border use the observed white canvas and grey hairline.

**product-card** reflects the catalog structure implied by "Featured Products" listings; card border and radius are proposed, while title/body typography reuse the `.product-name`/`.product-tagline` size variables (`--h2`, `--h6`) mapped conceptually to title-md and body-sm.

**hero** models the large promotional banners described in the page text (e.g. "Colour Your Story," "Video Unlocked"); dark background and inverted text are proposed based on the dark button/footer pattern seen elsewhere in the CSS, not a captured hero screenshot.

**footer** uses the same dark-surface/light-text inversion as `.btn-dark`, extended to the site-wide footer implied by the long link list ("Company, Support, Legacy Products…"); exact footer background was not directly sampled.

**badge** is proposed for merchandising labels (e.g. "New," category tags); it borrows the soft surface-card grey and caption typography for a low-contrast pill treatment.

**search** is proposed; no search-input CSS was supplied, so its pill shape and soft background are stylistic inferences consistent with the surface tokens.

**color-swatch-selector** is the category-appropriate component, directly motivated by the "vibrant new colours," "Your Sound, Your Style, Your Story" and "bold new colours" campaign copy for RØDE's Wireless GO and mic lines; it proposes a circular swatch pattern with an active-state ring in the primary indigo, though the actual swatch UI markup was not present in the supplied CSS.

## Responsive Behavior
This is a proposed breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| sm | ≥ 640px | Single-column product grid, stacked hero text |
| md | ≥ 768px | Two-column product grid, nav collapses to hamburger below this point |
| lg | ≥ 1024px | Three/four-column product grid, full horizontal nav-bar |
| xl | ≥ 1280px | Max-width content container, section padding increases to `{spacing.section}` |

Touch targets should be at least 44×44px for buttons and swatch selectors; the nav-bar is expected to collapse into a mobile drawer below `md`, and product-card grids to reflow to single column below `sm`. None of this was directly observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This interpretation is built from a static CSS/text extraction and carries several limitations. CSS custom properties such as `--action-primary`, `--action-on-primary`, `--h2`, `--h6`, and `--Weight-SemiBold` were referenced in selectors but never resolved to concrete values in the supplied evidence, so their color/size mappings (primary, on-primary, title sizing) are inferred rather than confirmed. No component screenshots, computed styles, or DOM layout were available, so hero, nav-bar, footer, search and text-input structures are proposed patterns based on page copy and adjacent CSS, not observed markup. All typography sizes except body-md (16px/24px/400, directly observed on `body`) are proposed estimates. Font licensing and self-hosting status for Inter/Roboto were not verified — only their presence in the font-family stack is confirmed. Mobile/responsive behavior, hover/focus states beyond the button rules shown, and interaction patterns (e.g. accordion, hotspot behavior) are inferred from partial selector names only.
