---
version: alpha
name: "Pupford"
source_url: "https://pupford.com"
captured_at: "2026-09-28T09:35:20.588702+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Pupford's storefront evidence shows a warm, pet-friendly palette built on
  a coral-orange primary (#e14f3d, with a closely related #e64b38 used by
  the Judge.me review widget) set against a soft cream surface (#fcf9e9)
  and a dark maroon ink (#572d2f / #592e2c) used for button text and nav
  hairlines. Base theme variables (--color-foreground: 18,18,18,
  --color-background: 255,255,255) indicate a near-black/white default
  Shopify scaffold underneath the branded coral system, so body copy is
  interpreted as dark near-black on white, inferred rather than directly
  observed. Headings and buttons consistently use the BuenosAires family
  (Bold, SemiBold, Book, Regular) at weight 700 with fully pill-shaped
  (border-radius:100px/999px) buttons, matching a friendly, rounded
  consumer-pet brand. Body/paragraph text likely falls back to Assistant
  sans-serif via a --font-body-family variable referenced in a promo
  component, though this mapping is inferred, not directly confirmed for
  all body copy. Accent chips in light blue (#a8c7fe) and light pink
  (#ffb3b9) appear as secondary CTA backgrounds, suggesting a playful
  secondary-action palette. Layout structure (grid, spacing) is proposed,
  not measured.

colors:
  primary: "#e14f3d"
  accent-review: "#e64b38"
  ink: "#572d2f"
  ink-alt: "#592e2c"
  body: "#121212"
  canvas: "#ffffff"
  muted: "#8a8a8a"
  hairline: "#d1d5db"
  surface-soft: "#fcf9e9"
  surface-card: "#f3f3f3"
  on-primary: "#fcf9e9"
  accent-blue: "#a8c7fe"
  accent-pink: "#ffb3b9"
  accent-yellow: "#fed34c"
  accent-green: "#2bb673"
  accent-navy: "#25384a"
typography:
  display-xl: {fontFamily: "'BuenosAires Bold', sans-serif", fontSize: 38px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  display-md: {fontFamily: "'BuenosAiresSemiBold', sans-serif", fontSize: 28px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  title-md: {fontFamily: "'BuenosAiresSemiBold', sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Assistant, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Assistant, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'BuenosAiresRegular', sans-serif", fontSize: 10px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.5px}
  button-md: {fontFamily: "'BuenosAires Regular', sans-serif", fontSize: 18px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
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
    padding: "{spacing.md} {spacing.xxl}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xxl}"
    border: "none"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xxl}"
    border: "3px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    borderBottom: "1px solid {colors.ink-alt}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  review-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent-review}"
    starColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"
  promo-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    padding: "{spacing.lg}"

## Components
**button-primary** renders the coral (#e14f3d) fill with cream text, matching the observed `.pf-button-1` rule; this is the primary add-to-cart / shop CTA. Hover/focus states are not observed and are proposed as a slight brightness shift, consistent with the birthday-button `:hover { filter: brightness(0.96) }` pattern seen elsewhere in the CSS.

**button-secondary** uses the cream surface with maroon ink text, mirroring `.pf-button-2`; intended for lower-emphasis actions (e.g. "Shop All") next to a primary CTA.

**button-outline** reflects `.pf-button-3`'s 3px coral border with transparent fill, proposed for tertiary or card-level actions such as "View Details."

**text-input** is inferred from general e-commerce convention; no explicit input styling was present in the supplied CSS, so border/radius values are proposed defaults using the observed hairline grey (#d1d5db).

**nav-bar** draws on `.header .list-menu__item`, which shows a 16px BuenosAiresSemiBold label with a maroon (#592e2c) top border — interpreted here as a bottom rule for a horizontal nav bar; exact nav layout (mega-menu columns for Dog Treats, Engage Chews, etc.) was present in text content but not in measurable CSS, so structural placement is proposed.

**product-card** is proposed to hold bestseller/bundle listings (e.g. "Freeze Dried Dog Training Treats, From $15.99"); no explicit card CSS was supplied, so padding/border are conservative proposed defaults.

**hero** uses the cream surface-soft background with the large 38px BuenosAires display type observed in `.pf-heading-*` rules, appropriate for the "Transform Your Pup's Behavior" hero copy referenced in the page text.

**footer** color is proposed using the darker navy (#25384a) present in the palette, which was not explicitly tied to a footer selector in the supplied CSS — treat as an inferred brand-adjacent dark surface for contrast rather than a confirmed footer style.

**badge** (e.g. "NEW", "Save 20%") uses the observed yellow accent (#fed34c) for promotional/sale flags visible in the bundle copy ("Save 15%", "Save 20%").

**search** styling is proposed; the header text mentions a "Search" affordance but no CSS was supplied for it.

**review-badge** maps directly to the Judge.me variables (`--jdgm-primary-color: #E64B38`, `--jdgm-star-color: #4E4E4E`), used for the "(791) Five Star Rating" element seen in page text.

**promo-banner** models the birthday/sitewide-discount banner (`.birthday-2026__body`, `.birthday-2026__button`), which explicitly uses cream/coral tones and a fully rounded CTA button — one of the few components with directly observed padding and radius values (border-radius: 999px).

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <600px | Single-column stacking, nav collapses to hamburger/drawer |
| Tablet | 600–1099px | 2-column product grids; nav-bar may partially collapse |
| Desktop | ≥1100px | Matches the one explicit CSS custom property observed, `--meteor-desktop-breakpoint: 1100px`, used as the desktop threshold |

Touch targets are recommended at a minimum 44px height, consistent with the birthday-button's `min-height: clamp(44px, 3.04vw, 59px)` rule, one of the few fluid/responsive values directly observed. All other breakpoint and collapse behavior is a proposed recommendation, not measured site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no live rendering, DOM inspection, or interaction testing was performed. The mapping of Assistant as the primary body font is inferred from its presence in the font list and a `var(--font-body-family)` reference, but no rule was supplied that directly assigns Assistant to body copy. Root theme variables (`--color-foreground: 18,18,18`, `--color-button: 18,18,18`) suggest a default black/white Shopify theme layer beneath the branded coral components, and it is unclear which layer governs most page surfaces. Spacing scale, product-card, search, and footer structures are proposed conventions, not observed measurements. Hover, focus, active, error, and mobile-menu states are largely unconfirmed, aside from the one explicit `:hover { filter: brightness(0.96) }` rule. Licensing and availability of the custom "BuenosAires" font family were not verified. Numeric color roles (e.g., which grey serves as "muted" vs. "hairline") are best-fit approximations from the supplied palette, not confirmed design-system labels.
