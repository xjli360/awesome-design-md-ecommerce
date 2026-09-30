---
version: alpha
name: "Zee.Dog"
source_url: "https://zeedog.com"
captured_at: "2026-09-28T04:46:27.983258+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Zee.Dog's storefront CSS exposes a neutral, product-forward palette dominated
  by whites, near-blacks, and a stepped gray scale (Tailwind-style gray-50
  through gray-900 custom properties), with a single saturated blue
  (#1990c6, darkening to #136f99 on hover) appearing only on the Shopify
  accelerated-checkout button. Because that blue is Shopify-payment
  boilerplate rather than confirmed brand styling, it is treated here as an
  inferred accent/primary rather than a verified brand color, reused across
  interactive states to keep the palette internally consistent. Grays
  (#f5f5f5, #e5e5e5, #dedede, #9ca3af, #737373) supply hairlines, soft
  surfaces, and muted text without introducing new hues.

  Typography is evidenced only by declared font-family stacks: Jost paired
  with system-ui/sans-serif fallbacks, and Roboto with the same fallback
  chain, alongside monospace stacks used for code-like UI (not modeled here).
  Jost is proposed as the heading/display family (its geometric character
  suits a "design-oriented" pet lifestyle brand) and Roboto as the body
  family; this pairing is inferred, not confirmed by selector-level
  font-family assignments to headings versus paragraphs.

  Corner radius tokens are consistently 4px (block, button, input, dropdown),
  so the design system below standardizes on a compact, understated radius
  scale rather than pill-shaped or sharp-cornered UI, reflecting a clean,
  utilitarian retail aesthetic appropriate to leashes, collars, and
  harnesses.

colors:
  primary: "#1990c6"
  primary-hover: "#136f99"
  ink: "#000000"
  ink-soft: "#333333"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#737373"
  hairline: "#dedede"
  surface-soft: "#f5f5f5"
  surface-card: "#f1f1f1"
  on-primary: "#ffffff"
  border: "#d1d5db"
  disabled-surface: "#e5e5e5"
  focus-ring: "#005fcc"
typography:
  display-xl: {fontFamily: "Jost, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Jost, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Jost, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Roboto, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Roboto, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Roboto, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1, letterSpacing: 0.1px}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.border}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.border}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairlineColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    overlayColor: "#00000033"
    typography: "{typography.display-xl}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  product-variant-swatch:
    borderColor: "{colors.border}"
    rounded: "{rounded.full}"
    size: "{spacing.lg}"
    selectedBorderColor: "{colors.primary}"

## Components

**button-primary** models the site's one confirmed vivid accent, the checkout blue, applied to primary calls-to-action like "Add to Cart" or "Shop Now." Hover state (proposed) darkens to `#136f99`, mirroring the observed `:hover` rule on the Shopify payment button.

**button-secondary** is a proposed outline/ghost variant for lower-emphasis actions (e.g., "View Details"), using the neutral border and ink text so it recedes next to the primary blue.

**text-input** covers search fields, newsletter signup, and account forms, using the shared 4px input radius token and neutral border color observed in the `:root` custom properties.

**nav-bar** represents the header/navigation shell implied by the extensive mega-menu category list (Dogs, Cats, Humans, Collections). Sticky/transparent header behavior is referenced by CSS variables (`--header-transparent-text-color`, `.header--transparent`) but exact scroll behavior is not verified here.

**product-card** is proposed for leash/harness/collar grid listings, pairing a soft card surface with the 4px block radius and title/price typography pairing.

**hero** is a proposed full-bleed banner pattern, justified by the transparent-header CSS hooks suggesting image-backed top sections; dark overlay uses the observed `#00000033` alpha black for text legibility over photography.

**footer** is a proposed dark-toned closing section for links, newsletter, and legal text, using the darker ink-soft neutral for contrast against the mostly white site body.

**badge** is proposed for "New," "Best Seller," or sale labels seen in navigation labels ("Best Sellers," "New Arrivals"), using the full-radius pill and primary color for visibility.

**search** models the storefront search affordance, using the soft gray surface consistent with the `--gray-50`/`--gray-100` tokens.

**product-variant-swatch** is proposed for color/pattern selection on collar and leash product pages (the catalog includes many named print/collection variants like Glitch, Prisma, Skull), using a circular swatch with a primary-colored selected-state ring.

## Responsive Behavior

Recommended breakpoints (not measured): mobile `<640px`, tablet `640–1024px`, desktop `1024–1400px` (aligning with the observed `--breakpoint-xl: 1200px` and `--breakpoint-hd: 1400px` tokens), and wide `>1400px` bounded by `--container-max-inner-width-const: 1800px`. Navigation is expected to collapse from the full mega-menu into a slide-in drawer below tablet width, using the observed `.back-button`/`.close-button` pattern as the drawer's close affordance. Touch targets should be a minimum 44px height, matching the accelerated-checkout button's clamped block-size (`clamp(25px, 44px, 55px)`). This section is a recommendation derived from token values, not an observed layout.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from static CSS custom properties, a font-family allowlist, and a color list extracted without confirmed selector-to-role mapping for most brand colors; the single saturated blue is sourced from generic Shopify checkout-button CSS and may not represent Zee.Dog's actual brand accent. Heading-vs-body font assignment (Jost vs. Roboto) is inferred from typical pairing conventions, not from confirmed `h1`/`p` selector rules. All pixel sizes in the typography scale beyond the 4px radius tokens are proposed, not measured. No interaction states (hover/focus/active), animations, or actual mobile breakpoint behavior were observed in a live browser; the responsive table above is a design recommendation only. Licensing and self-hosting availability of Jost and Roboto for production use were not verified in this evidence set.
