---
version: alpha
name: "Quoizel"
source_url: "https://quoizel.com"
captured_at: "2026-09-28T09:37:16.634235+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Quoizel's stylesheet evidence points to a warm, editorial lighting-catalog aesthetic built on a
  neutral canvas with a single teal-blue accent. The observed palette centers on white (#ffffff)
  and near-black ink (#151f24) for structure, with a muted teal (#2c7590) and its lighter tint
  (#72a8bc) appearing as the most distinct non-neutral hues, inferred here as the primary brand
  accent. Warm off-white surfaces (#f5f4f2, #dedbd4, #eceae6) recur in submenu and section
  backgrounds, suggesting a soft, gallery-like layering rather than stark white blocks. Typography
  pairs a serif display face, ivyora-text, for all headings (h1-h6, weight 400) with a sans-serif
  body face, area-normal, at a confirmed 16px/1.5 base -- a classic "heritage brand" contrast
  between editorial serif headlines and clean sans utility text. area-extended appears reserved
  for condensed or emphasized UI labels (inferred use in buttons/nav). Several palette entries
  (status reds/greens, alert blues) are attributed to third-party widget styling (e.g. a wishlist
  app) rather than brand identity, and are excluded from primary role assignments. This
  interpretation favors restrained neutrals, generous whitespace implied by section-level content
  (Signature, Platinum, Charleston, Naturals, Artisan Glass, Coastal Armour edits), and serif
  headline emphasis to match a "since 1930" heritage lighting positioning.

colors:
  primary: "#2c7590"
  ink: "#151f24"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#e0e0e0"
  surface-soft: "#f5f4f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-light: "#72a8bc"
  neutral-warm: "#b2aca7"
  navy-deep: "#1d3540"
  black: "#000000"
typography:
  display-xl: {fontFamily: "ivyora-text, serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "ivyora-text, serif", fontSize: 34px, fontWeight: 400, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "ivyora-text, serif", fontSize: 22px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "area-normal, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "area-normal, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "area-normal, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.3px}
  button-md: {fontFamily: "area-extended, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    submenuBackground: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  collection-tile:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    descriptionTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.black}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** — A solid teal-accent call-to-action (e.g. "Explore all lighting"), using the
inferred primary color against white text. Hover/active states are not observed in the static CSS
and are proposed only.

**button-secondary** — An outlined variant using the near-black ink border on white, intended for
lower-emphasis actions such as "Browse this collection" links seen throughout the edits content.
Proposed pairing; no explicit secondary-button CSS was captured.

**text-input** — A minimal-border field for search/newsletter/account forms, styled from the
generic hairline gray and body sans-serif font. No focus-state styling was observed; treated as
proposed.

**nav-bar** — Reflects the confirmed `--color-submenu: rgb(245 244 242)` token used on
`.header__underlay`, giving the mega-menu (Indoor Lighting, Outdoor Lighting, Our Edits, Discover
Quoizel, Customer Care) a warm off-white drop-down surface against a white top bar. Multi-level
menu depth (drawer animation indices found in evidence) confirms a nested/animated menu system,
though exact transitions are not verified here.

**product-card** — Based on the confirmed `.product-card__content { background-color:#fff }` rule.
Card titles use the serif heading family; price/meta text uses the smaller sans body style. Border
and radius values are proposed, not measured.

**collection-tile** — A category-appropriate component for Quoizel's "Our Edits" merchandising
(Signature, Platinum, Charleston, Naturals, Artisan Glass, Coastal Armour), using the warm
surface-soft background to visually separate curated collection groupings from standard product
grids. Entirely proposed layout, grounded only in the text content structure.

**hero** — A full-bleed introductory band ("Crafted with Purpose, Designed to Inspire") using the
dark ink background with large serif display type, matching the confirmed `ivyora-text` h1 styling
and inferred heritage-brand tone. Background choice (ink vs. photographic) is inferred, not
observed.

**footer** — Dark ink background with light text, consistent with the site's dark-surface color
role (`#151f24` recurs with alpha variants in evidence, e.g. `#151f24e6`, `#151f24a6`), suggesting
this tone is reused for overlays and footer/header dark states. Proposed layout only.

**badge** — Derived directly from observed `.swym-header-icon-count` CSS: white text on black
circular badge, 18px min-width, 11px/600 font — used here as the canonical cart/wishlist count
indicator.

**search** — A lightweight input/icon combo inferred from the "Search Search" nav label; no
dedicated search-field CSS was present in evidence, so styling is proposed from the shared
text-input pattern.

## Responsive Behavior

Recommended (not measured) breakpoint table:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <768px | Single-column product grids, collapsed hamburger nav, stacked hero text |
| tablet | 768–1023px | 2-column product/collection grids, condensed mega-menu |
| desktop | 1024–1439px | Full mega-menu with submenu flyouts, 3–4 column grids |
| wide | ≥1440px | Max-width content container, increased section padding |

Touch targets should target a minimum 44×44px hit area for nav, cart, and badge icons. The
multi-level "Indoor Lighting / Outdoor Lighting / Our Edits" mega-menu should collapse to an
accordion pattern on mobile. This table is a proposed recommendation based on typical Shopify
storefront patterns and the presence of `--menu-drawer-animation-index` tokens; no actual
responsive/mobile rendering was observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/text extraction and does not reflect a rendered
or interactive audit. Specific gaps:

- No live layout, spacing, or grid measurements were observed; all `spacing` and `rounded` values
  are proposed defaults, not extracted from computed styles.
- Color **role** assignments (primary, muted, hairline, etc.) are inferred from usage context
  (e.g. `--color-submenu`, `.product-card__content`) rather than an explicit design-token export;
  several palette entries (status reds/greens/blues) appear tied to a third-party widget (likely
  Swym wishlist) and were deliberately excluded from brand-role mapping.
- Font availability, licensing, and exact weight/style ranges for `ivyora-text`, `ivyora-display`,
  `area-normal`, and `area-extended` were not verified; only generic sans-serif/serif fallbacks are
  confirmed safe.
- No hover, focus, active, or error states were observed in the supplied CSS; all interaction
  states in this spec are proposed.
- Mobile/tablet menu behavior, drawer animation timing, and touch interactions were not observed;
  only CSS custom-property names (`--menu-drawer-animation-index`) hint at drawer-based navigation.
- Button, badge, and card component paddings/border-radii beyond the confirmed
  `border-radius:50%` badge rule are proposed estimates.
