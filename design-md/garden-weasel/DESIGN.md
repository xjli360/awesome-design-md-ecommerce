---
version: alpha
name: "Garden Weasel"
source_url: "https://gardenweasel.com"
captured_at: "2026-09-28T09:55:20.058520+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Garden Weasel's storefront CSS shows a utilitarian, high-contrast system built on Shopify's default color-variable scaffold (#ffffff background, #121212 foreground) overlaid with brand-specific accents. The dominant brand signal is #c00321, a saturated red used for hover underlines and utility-menu links, paired with #129174, a deep green reserved for the mega-menu's promotional call-to-action button. Navigation text uses #383838 with mr-eaves-sans, a licensed display/sans face set in bold, uppercase, tightly tracked styling for menu items and buttons — this is the only typeface with direct rule evidence. Assistant appears in the site's font-family list but without a confirmed selector, so its role as body copy is inferred. Warm neutral #eae4dd and light grays (#f3f3f3, #dedede, #cccccc) suggest a soft, earthy surface system appropriate for a garden-tools catalog, contrasted against near-black ink (#121212, #231f20, #232323) for legibility. Checkout-widget blues (#1990c6, #136f99) and #334fb4 appear only in third-party Shopify payment CSS and are treated as secondary/system accents rather than core brand color. This interpretation proposes a rugged-but-tidy retail UI: red for primary action and emphasis, green for secondary promotional CTAs, warm neutrals for card surfaces, and bold uppercase mr-eaves-sans for navigation and headings.

colors:
  primary: "#c00321"
  secondary: "#129174"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#383838"
  muted: "#cccccc"
  hairline: "#dedede"
  surface-soft: "#f3f3f3"
  surface-card: "#eae4dd"
  on-primary: "#ffffff"
  dark: "#231f20"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  link-blue: "#334fb4"
typography:
  display-xl: {fontFamily: "mr-eaves-sans, sans-serif", fontSize: 48px, fontWeight: 800, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "mr-eaves-sans, sans-serif", fontSize: 32px, fontWeight: 800, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "mr-eaves-sans, sans-serif", fontSize: 19px, fontWeight: 800, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "mr-eaves-sans, sans-serif", fontSize: 12px, fontWeight: 800, lineHeight: 1.3, letterSpacing: 0.5px}
  button-md: {fontFamily: "mr-eaves-sans, sans-serif", fontSize: 19px, fontWeight: 800, lineHeight: 1.1, letterSpacing: 0px}
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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.muted}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  mega-menu-panel:
    backgroundColor: "{colors.canvas}"
    surfaceColor: "{colors.surface-soft}"
    ctaBackground: "{colors.secondary}"
    ctaTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"

## Components

**button-primary** — Solid red (#c00321) fill mapped from the observed hover/link accent color, used for primary storefront actions such as "Add to Cart" or "Shop Now." Uppercase mr-eaves-sans styling matches evidenced nav/button rules. Hover/active/disabled states are proposed, not observed.

**button-secondary** — Uses the evidenced #129174 mega-menu button background, repurposed as a secondary CTA (e.g., "Learn More," "View Project"). This color only appears in mega-menu button CSS, so its broader secondary-button role is an inferred extension.

**text-input** — A plain white field with a light hairline border (#dedede), proposed for search and account forms since no dedicated input CSS was supplied. Focus-ring styling is not observed and is proposed here as a thin primary-colored outline.

**nav-bar** — Reconstructed directly from `.header__inline-menu` rules: white background, bold uppercase 15px mr-eaves-sans labels in #383838, with red underline on hover. Sticky/scroll behavior is not confirmed by the evidence and is treated as proposed.

**product-card** — A warm #eae4dd card surface (inferred from the observed neutral palette, not a confirmed card rule) intended to house tool thumbnails, names, and prices, matching the earthy, outdoor-tool retail category. Border and radius values are proposed defaults.

**hero** — A full-width banner using light neutral background and large mr-eaves-sans display type, suited to campaign messaging like "Solutions from the Ground Up." Imagery treatment and overlay gradients are not present in evidence and are omitted rather than invented.

**footer** — Dark ink (#231f20) background with white text, referencing the brand's newsletter-signup block evidenced in CSS (`.footer-block__brand-info .newsletter-form__button`), which itself uses a white button with black text — footer background darkness is inferred to create contrast with that light button.

**badge** — A small pill label (e.g., "New," "Best Seller") using an ink border on white, styled in bold uppercase caption type consistent with the mr-eaves-sans utility-menu treatment. Entirely proposed; no badge component was present in the supplied CSS.

**search** — White field with a muted border, proposed to align with the site's visible "Search" cart/account icons in the header markup, though no dedicated search input styling was supplied.

**mega-menu-panel** — Directly informed by the evidenced `.mega-menu__image-button` rules: white/light panel background, green CTA button, uppercase bold labeling. This matches the site's extensive shop-by-category/project/solution mega-menu structure referenced in the page text.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior (no media queries were supplied):

| Breakpoint | Width      | Nav behavior                         | Grid columns |
|-----------|------------|----------------------------------------|--------------|
| Mobile    | < 480px    | Hamburger + drawer menu (proposed)     | 1            |
| Tablet    | 480–1024px | Collapsed inline menu / drawer         | 2            |
| Desktop   | > 1024px   | Full inline mega-menu (as evidenced)   | 3–4          |

Touch targets should be at minimum 44×44px for cart, search, and menu-drawer close controls. The evidenced `.menu-drawer__close-button-back` implies an existing mobile drawer pattern; its full responsive collapse logic is not observed and is proposed here as a standard slide-in drawer with a back button.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS/HTML extraction only; no rendered layout, spacing rhythm, or actual grid measurements were observed.
- The mapping of Assistant to body copy is inferred from the font-family list; no selector directly ties Assistant to a body rule.
- Root `--color-foreground: 18,18,18` (#121212) and nav-text `#383838` may represent the same conceptual "ink" role at different specificity — this document treats them as distinct (ink vs. body) but the actual design intent is unconfirmed.
- Colors #334fb4, #1990c6, #136f99, and #ffff00 appear primarily in third-party Shopify checkout/payment-widget CSS, not confirmed brand-authored styles; their inclusion as accents is speculative.
- Hover, focus, active, and disabled states for buttons and inputs are proposed conventions, not extracted from evidence.
- Mobile menu-drawer interaction, breakpoint values, and grid-column counts are not observed; the responsive table above is a recommendation only.
- Font licensing/availability for "mr-eaves-sans" was not verified; it is treated strictly as an observed CSS value, not a confirmed licensed/hosted asset.
- No explicit product-card, hero, or badge selectors were present in the supplied CSS; those components are constructed from general palette/typography inference for category fit (gardening tools e-commerce).
