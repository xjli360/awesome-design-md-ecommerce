---
version: alpha
name: "Black Diamond"
source_url: "https://blackdiamondequipment.com"
captured_at: "2026-09-29T04:18:22.092265+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Black Diamond's storefront evidence shows a utilitarian, mountain-hardware aesthetic built on a near-monochrome base (black #000000/#121212, white #ffffff, and mid-grays #f7f7f7/#dedede/#8c8c8c) punctuated by a single burnt-orange accent (#cd4c1d, with a near-duplicate #cd4c1e/#bd461b appearing in related contexts). This orange drives CTAs such as the featured-blog button and testimonial hover states, darkening to black on hover rather than shifting hue. A secondary utility blue (#1990c6, hover #136f99) appears only on the Shopify-native accelerated checkout button, so it is treated as a platform default rather than a brand color, kept available but not promoted to primary UI. Error/alert reds (#dc2626, #ef4444, #fef2f2) are inferred as form-validation colors from generic class naming.
  Typography is clearly role-split in the CSS: Futura Extra Bold drives buttons, Futura Semi Bold drives heading levels h0–h5, and Neue Haas Unica handles denser UI copy like product titles and form submit labels. Jost and Instrument Sans are present in the font manifest but have no confirmed selector role, so they are treated as inferred secondary/body candidates. The resulting interpretation favors bold, condensed display type, flat rectangular controls, and generous whitespace consistent with a technical outdoor-gear catalog, with rounded corners kept minimal (0–4px) given the observed 0px radius on the checkout button.

colors:
  primary: "#cd4c1d"
  primary-hover: "#bd461b"
  ink: "#000000"
  ink-soft: "#121212"
  canvas: "#ffffff"
  body: "#333d47"
  muted: "#5c5f62"
  hairline: "#dedede"
  surface-soft: "#f7f7f7"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  border-subtle: "#d8d8d8"
  border-strong: "#949494"
  accent-blue: "#1990c6"
  accent-blue-hover: "#136f99"
  danger: "#dc2626"
  danger-surface: "#fef2f2"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "Futura Semi Bold, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Futura Semi Bold, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Neue Haas Unica, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "Neue Haas Unica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Neue Haas Unica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Neue Haas Unica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Futura Extra Bold, sans-serif", fontSize: 19px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-subtle}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    overlay: "{colors.overlay-scrim}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  pack-spec-table:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"

## Components
**button-primary** applies the observed `#cd4c1d` background from the featured-blog CTA, paired with the Futura Extra Bold button font-family rule found on `.button`; hover-to-black is an observed pattern from `.featured-blog-info .featured-blog-button a:hover` and is proposed as the default primary interaction across the site, not confirmed for every instance.

**button-secondary** is inferred: no outline-button CSS was supplied, so a white-fill/black-border/black-text treatment is proposed to complement the solid primary button without introducing a new hue.

**text-input** proposes a light hairline border (`#dedede`-family) and white fill; no input-specific selectors were in evidence, so padding and radius are proposed defaults suited to a dense e-commerce nav/search context.

**nav-bar** is inferred from the mega-menu text content (Men's/Women's/Mountain/Climb/Ski categories) implying a persistent top navigation; visual styling (white background, black text) is proposed since no nav CSS block was supplied.

**product-card** typography draws on the confirmed `.product-info-content h2` rule (Neue Haas Unica, weight 600); background and radius are proposed for a grid-based catalog card appropriate to backpacks/outdoor gear listings.

**hero** is proposed for homepage banner treatment; dark background with white text is inferred from `.featured-heading h1, .featured-heading h3 { color:#ffffff }`, implying imagery-backed sections with light text overlays.

**footer** uses the dark ink-soft tone as a plausible footer background given the newsletter form CSS present (`.footer-block__newsletter`); actual footer background color was not directly supplied and is treated as inferred.

**badge** is a proposed component for sale/outlet callouts ("40% Off Past Season Ski Gear") seen in page text, using the primary orange as a promotional accent consistent with the CTA color.

**pack-spec-table** is a category-appropriate proposed component for backpack/travel product pages to present volume, weight, and capacity specs in a light, hairline-bordered table, matching the muted surface tones observed elsewhere on the site.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:
| Breakpoint | Width | Nav | Grid |
|---|---|---|---|
| Mobile | <768px | Collapsed hamburger, single-column product grid | Stacked cards |
| Tablet | 768–1023px | Condensed mega-menu, 2-column grid | Touch targets ≥44px |
| Desktop | ≥1024px | Full mega-menu with category flyouts | 3–4 column grid |

Touch targets for buttons and nav items should maintain a minimum 44×44px hit area; mega-menu flyouts should collapse to accordions below tablet width. None of this was observed in rendered layout — it is a conventional recommendation based on the category list depth evidenced in page text.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or interaction states (hover/focus/active beyond the two hover rules shown) were observed. The mapping of Futura Semi Bold to all heading levels and Futura Extra Bold to all buttons is confirmed by selector; however, root font-size and therefore exact rem-to-px conversions for body copy were not resolvable from the supplied `1.5rem` body rule, so body-md's 16px is a proposed estimate. Jost and Instrument Sans appear in the font manifest with no confirmed selector, so their role in the type system is unverified. The blue accelerated-checkout blue (#1990c6/#136f99) is Shopify-platform styling, not confirmed brand color, and is retained only as a secondary/utility token. Custom font licensing and self-hosting availability (Futura, Neue Haas Unica) were not verified. Mobile menu behavior, cart drawer interaction, and product-page layout for backpacks specifically were not observed in the supplied evidence.
