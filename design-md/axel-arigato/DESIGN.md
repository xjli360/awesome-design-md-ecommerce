---
version: alpha
name: "Axel Arigato"
source_url: "https://axelarigato.com"
captured_at: "2026-09-28T04:16:13.962478+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Axel Arigato's storefront exposes a near-monochrome palette anchored by a soft
  black (#090909) rather than true #000000, paired with white canvases and a
  cluster of low-opacity black overlays (#0909091a, #0000001a, #090909b3) used
  for hairlines, scrims, and hover states. A small set of pastel tints
  (#e8effa, #fffae8, #fde1e1, #faedbc) sit alongside a saturated blue
  (#2563eb) and an Apple-system blue (#007aff) tied to Swiper's default theme
  variable; these are treated as inferred accent/badge colors rather than
  primary brand colors, since sneaker retail sites commonly reserve pastels
  for "New," "Sale," or size-guide highlights. Grays (#6b7280, #9ca3af,
  #999999, #aaaaaa) support muted text, disabled states, and dividers.
  Typography is exclusively HelveticaNowVar with standard system/sans-serif
  fallbacks and emoji stacks; the only concretely observed size is 0.8125rem
  (13px) shared by body and h1 selectors, suggesting a compact base scale
  where visual hierarchy is likely achieved through weight and spacing rather
  than large size jumps — the fuller display scale below is proposed for
  editorial hero and product-title moments consistent with a minimal
  Scandinavian sneaker brand.

colors:
  primary: "#090909"
  ink: "#090909"
  canvas: "#ffffff"
  body: "#090909"
  muted: "#6b7280"
  hairline: "#0909091a"
  surface-soft: "#f9f9f9"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"
  accent-blue: "#2563eb"
  accent-blue-soft: "#e8effa"
  accent-yellow-soft: "#fffae8"
  accent-yellow-deep: "#faedbc"
  accent-red-soft: "#fde1e1"
  muted-2: "#9ca3af"
  disabled: "#999999"
  border-subtle: "#aaaaaa"
  overlay-strong: "#00000080"
  overlay-soft: "#0000001a"
  scrim: "#090909b3"
  divider-soft: "#e9e9e933"
  icon-accent: "#007aff"
typography:
  display-xl: {fontFamily: "HelveticaNowVar, ui-sans-serif, system-ui, sans-serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "HelveticaNowVar, ui-sans-serif, system-ui, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "HelveticaNowVar, ui-sans-serif, system-ui, sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "HelveticaNowVar, ui-sans-serif, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "HelveticaNowVar, ui-sans-serif, system-ui, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "HelveticaNowVar, ui-sans-serif, system-ui, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "HelveticaNowVar, ui-sans-serif, system-ui, sans-serif", fontSize: 13px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.2px}
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
    border: "1px solid {colors.border-subtle}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    height: "64px"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    hoverOverlay: "{colors.overlay-soft}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    dividerColor: "{colors.divider-soft}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-red-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  size-finder:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hoverTextColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    accentColor: "{colors.icon-accent}"
    padding: "{spacing.sm} {spacing.base}"

## Components
**button-primary** renders as a solid near-black pill/rectangle with white
text, matching the site's `background-color:#0000` reset paired with the
dark ink used across interactive hover states; proposed for primary CTAs
like "Add to Bag."

**button-secondary** is an outlined variant on white, using the observed
mid-gray border tone (#aaaaaa) for a lighter-weight action such as
"Notify Me" or filter toggles; states beyond default are proposed.

**text-input** uses a hairline black border at very low opacity
(#0909091a), consistent with the subtle divider treatment seen in the CSS,
for newsletter or search fields; focus/error states are proposed and not
observed.

**nav-bar** is inferred as a white, fixed-height bar with a faint bottom
hairline, holding logo, category links, and icon actions; sticky behavior
is proposed, not confirmed from static CSS.

**product-card** groups a soft-gray surface (#f9f9f9) with an internal
title/price stack; the low-opacity black hover overlay observed in the
palette (#0909091a) is proposed as an image-hover treatment for sneaker
grid listings.

**hero** is a full-bleed dark section using the ink tone as background with
white display type, intended for campaign/editorial imagery; copy scale and
exact crop are proposed, not measured.

**footer** mirrors the hero's dark ink background, using the low-opacity
divider color (#e9e9e933) to separate link columns; this palette choice is
inferred from the overlay/divider tones present in the source, not from a
confirmed footer screenshot.

**badge** leverages one of the pastel tints (red-soft) as a small pill for
promotional flags like "Sale" or "New"; the other pastels (blue-soft,
yellow-soft, yellow-deep) are proposed alternates for different badge
categories, all unconfirmed in live context.

**search** and **size-finder** are functional components directly evidenced
by class names in the CSS (`SizeFinder-module`), styled with the shared
HelveticaNowVar body font and an underline-on-open interaction; the
`#007aff` icon-accent token maps to the Swiper theme variable and is
proposed for small interactive icon accents rather than confirmed brand use.

## Responsive Behavior
Recommended, not measured, breakpoint table:

| Breakpoint | Width      | Notes                                   |
|-----------|------------|------------------------------------------|
| mobile    | 0–639px    | single-column product grid, collapsed nav |
| tablet    | 640–1023px | 2-column grid, condensed nav              |
| desktop   | 1024–1439px| 3–4 column grid, full nav                 |
| wide      | 1440px+    | max-width container, generous gutters     |

Touch targets should be at least 44px per the Swiper navigation-size
variable observed in CSS (`--swiper-navigation-size:44px`), reused here as a
minimum tap-target guideline. Navigation should collapse into a hamburger
or drawer pattern below tablet width; none of this collapse behavior was
directly observed and is offered as a conventional recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS extraction and a title string, not
from rendered screenshots or interaction testing. Semantic role mapping
(e.g., which pastel tint belongs to which badge type, whether #090909 is
truly the primary action color versus pure text ink) is inferred and
unverified. Most typography sizes beyond the single observed 0.8125rem
value are proposed estimates for a plausible sneaker-retail hierarchy, not
measured from rendered pages. Mobile layout, hover/focus/active states,
motion, and hamburger-menu behavior were not observed. Availability and
licensing of "HelveticaNowVar" as a custom/commercial font were not
verified; production use should confirm license terms before deployment.
