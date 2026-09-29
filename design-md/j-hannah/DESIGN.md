---
version: alpha
name: "J. Hannah"
source_url: "https://jhannahjewelry.com"
captured_at: "2026-09-29T04:01:18.720420+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  J. Hannah's storefront CSS points to a restrained, materials-first aesthetic consistent with a Los Angeles fine-jewelry maker working in solid 14k gold and sterling silver. The theme declares an explicit --color-primary of rgba(65,54,34,1) (#413622, a dark warm bronze/umber) and --color-secondary of #393624, both warm near-blacks that read as ink rather than saturated brand color — likely standing in for text and dark UI chrome. --color-background is declared as white, and the palette includes soft off-whites (#fcfbf9, #f5f0e4, #fdfdfd) that are inferred as card and section surface tones layered over pure white. A cooler #1990c6/#136f99 pair appears only inside the Shopify accelerated-checkout button styles, so it is treated as a payment-provider default rather than a brand accent, though it is preserved here for CTA usability. #a82323 appears only in a low-opacity utility class and is mapped speculatively to an alert/error role pending confirmation. Typography evidence lists a serif family (Allegro) alongside Times fallbacks and a "folio-book" family, paired with a custom sans "JH Gothic" and Helvetica Neue fallbacks — interpreted here as serif display type over sans-serif UI/body text, matching the brand's "modern relic" positioning. Grid tokens (24-column desktop, 8-column at the "l" breakpoint, 16–20px insets) are carried through as spacing/layout guidance.

colors:
  primary: "#413622"
  secondary: "#393624"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6e6e6e"
  hairline: "#dddddd"
  surface-soft: "#f5f0e4"
  surface-card: "#fcfbf9"
  on-primary: "#ffffff"
  accent-cta: "#1990c6"
  accent-cta-hover: "#136f99"
  alert: "#a82323"
  overlay: "#00000080"
  skeleton: "#dedede"
typography:
  display-xl: {fontFamily: "Allegro, 'Times New Roman', serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Allegro, 'Times New Roman', serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'JH Gothic', 'Helvetica Neue', sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0.01em}
  body-md: {fontFamily: "folio-book, Times, serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0}
  body-sm: {fontFamily: "folio-book, Times, serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0}
  caption: {fontFamily: "'JH Gothic', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.04em}
  button-md: {fontFamily: "'JH Gothic', 'Helvetica Neue', sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.01em}
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
  button-primary: {backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", typography: "{typography.button-md}", rounded: "{rounded.none}", padding: "{spacing.md} {spacing.lg}"}
  button-secondary: {backgroundColor: "transparent", textColor: "{colors.primary}", border: "1px solid {colors.primary}", typography: "{typography.button-md}", rounded: "{rounded.none}", padding: "{spacing.md} {spacing.lg}"}
  button-cta-checkout: {backgroundColor: "{colors.accent-cta}", backgroundColorHover: "{colors.accent-cta-hover}", textColor: "{colors.on-primary}", typography: "{typography.button-md}", rounded: "{rounded.none}", padding: "{spacing.base} {spacing.xl}"}
  text-input: {backgroundColor: "{colors.canvas}", border: "1px solid {colors.hairline}", textColor: "{colors.ink}", typography: "{typography.body-md}", rounded: "{rounded.xs}", padding: "{spacing.sm} {spacing.md}"}
  nav-bar: {backgroundColor: "{colors.canvas}", textColor: "{colors.ink}", typography: "{typography.caption}", borderBottom: "1px solid {colors.hairline}", padding: "{spacing.base} {spacing.lg}"}
  product-card: {backgroundColor: "{colors.surface-card}", rounded: "{rounded.none}", padding: "{spacing.base}", titleTypography: "{typography.title-md}", priceTypography: "{typography.body-sm}", border: "1px solid {colors.hairline}"}
  product-media-gallery: {backgroundColor: "{colors.surface-soft}", arrowColor: "{colors.ink}", indicatorActiveColor: "{colors.primary}", indicatorInactiveColor: "{colors.hairline}", rounded: "{rounded.none}"}
  hero: {backgroundColor: "{colors.surface-soft}", textColor: "{colors.ink}", headingTypography: "{typography.display-xl}", bodyTypography: "{typography.body-md}", padding: "{spacing.section} {spacing.lg}"}
  footer: {backgroundColor: "{colors.primary}", textColor: "{colors.on-primary}", typography: "{typography.body-sm}", padding: "{spacing.xxl} {spacing.lg}"}
  badge: {backgroundColor: "{colors.alert}", textColor: "{colors.on-primary}", typography: "{typography.caption}", rounded: "{rounded.full}", padding: "{spacing.xxs} {spacing.sm}"}
  search: {backgroundColor: "{colors.surface-card}", border: "1px solid {colors.hairline}", textColor: "{colors.ink}", typography: "{typography.body-sm}", rounded: "{rounded.sm}", padding: "{spacing.sm} {spacing.base}"}

## Components

**button-primary** uses the declared bronze `--color-primary` (#413622) as a solid fill with white text, matching the uppercase, border-based `.dsm-inquiry-button` pattern observed in the CSS (flex layout, uppercase, inherited color/border). Rounding is set to none/square to align with the theme's otherwise unrounded, editorial feel; this squared treatment is proposed, not directly measured on rendered buttons.

**button-secondary** is an outline variant inferred from the same inquiry-button pattern (`border: 1px solid; color: inherit`), giving a lighter-weight action for secondary actions like "Learn more" without asserting a fill color not present in evidence.

**button-cta-checkout** isolates the Shopify accelerated-checkout button styling (`background-color:#1990c6`, hover `#136f99`, block padding `1em 2em`) as its own component so this third-party-styled control is not conflated with brand-authored buttons.

**text-input** is a proposed pattern; no input-field CSS was supplied, so border, radius, and padding follow the theme's general hairline/spacing tokens rather than observed input styles.

**nav-bar** assumes a white, top-aligned bar with a hairline bottom border, consistent with the light `--color-background` and neutral divider tones (#dddddd/#e6e6e6) present in the palette; actual nav markup/behavior was not in the supplied evidence.

**product-card** and **product-media-gallery** draw on the swiper-based carousel rules (`.swiper-button-prev/next`, navigation sizing) to justify a gallery component with arrow controls; the active/inactive indicator colors are proposed since no explicit pagination-dot CSS was supplied.

**hero** and **footer** are proposed compositional patterns using the warm cream surface and dark bronze/primary backgrounds respectively, extrapolated from the brand's stated warm neutral palette rather than any hero/footer selector in evidence.

**badge** and **search** are speculative utility components using the isolated alert red (#a82323) and card surface tones; their presence and exact styling on the live site were not confirmed in the supplied CSS.

## Responsive Behavior
| Breakpoint | Approx. width | Columns | Inset | Notes |
|---|---|---|---|---|
| m | small/mobile | — | — | token present, values not fully supplied |
| l | tablet-ish | 8 | 20px | `--page-section-spacing: 140px`, `--product-section-spacing: 120px` |
| xl / xxl | desktop | 24 (default) | 16px | `--index-section-spacing: 110px`, `--wrap: 1520px` |

This table is a **recommendation derived from declared CSS custom properties**, not measured rendered behavior. Touch targets for buttons and nav items should target a minimum 44px hit area (matching `--swiper-navigation-size: 44px` as a size cue); mobile nav collapse into a hamburger/drawer pattern is proposed, not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Extraction is static (CSS + text only); no DOM screenshots, computed styles, or interaction states (hover, focus, active, error) were captured beyond the few pseudo-classes present in source (e.g., `:hover` on the checkout button).
- Semantic color roles (ink, muted, hairline, surface-soft/card) are inferred from generic-sounding hex values and common Shopify theme conventions, not confirmed against rendered elements.
- Font availability, licensing, and exact weights/sizes for "Allegro," "JH Gothic," and "folio/folio-book" are unverified; fallback stacks are generic per instructions.
- Mobile/tablet layout, breakpoint pixel values beyond named tokens ("m","l","xl","xxl"), and collapse/drawer patterns were not observed and are proposed only.
- Component existence (search, badge, text-input) beyond what direct selectors evidenced is proposed for completeness, not confirmed present on the live site.
