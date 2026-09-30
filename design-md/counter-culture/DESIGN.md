---
version: alpha
name: "Counter Culture"
source_url: "https://counterculturecoffee.com"
captured_at: "2026-09-29T04:09:35.553450+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Counter Culture Coffee's evidence shows a Shopify-based storefront using one confirmed checkout
  accent, "#000f8f" (a deep cobalt blue applied to the checkout override button), against a
  black/white base and a very large secondary palette of pastel and saturated hues (peach, mint,
  lavender, coral, yellow) that most plausibly serve as flavor-note or category tag colors rather
  than core brand chrome — this mapping is inferred, not confirmed by component-level evidence.
  Neutral grays ("#373737", "#696969", "#9b9b9b", "#c1c1c1", "#dadada", "#e9e6de", "#f9f9f9") support
  body text, hairlines, and soft surfaces. Typography draws on a broad observed stack: "Founders
  Grotesk" (multiple weights) and "Inter" (multiple weights) for utilitarian UI/body text, plus
  "eiko" (light through black) and "acorn" families suggesting a serif/display pairing for
  editorial or hero headlines, with "caveat" as a script accent likely reserved for handwritten-style
  callouts. This interpretation treats Founders Grotesk/Inter as the working UI system and Eiko as
  the display/editorial voice, since single-origin coffee sites commonly pair a utilitarian sans
  with an editorial serif for storytelling. The design system below proposes a restrained,
  content-forward commerce layout — product cards, subscription modules, and educational content
  blocks — anchored by the confirmed cobalt CTA color and neutral surfaces, with the wider palette
  reserved for badges, tags, and flavor-note chips rather than structural UI.

colors:
  primary: "#000f8f"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#373737"
  muted: "#696969"
  hairline: "#dadada"
  surface-soft: "#f9f9f9"
  surface-card: "#fcfbf8"
  on-primary: "#ffffff"
  accent-orange: "#f58320"
  accent-mint: "#bbe590"
  accent-lavender: "#8d93d9"
  accent-coral: "#ff5c35"
  accent-yellow: "#f5d300"
  border-strong: "#c1c1c1"
typography:
  display-xl: {fontFamily: "eiko-bold, serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "eiko-medium, serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "founders-grotesk-semibold, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "inter-regular, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.45, letterSpacing: "0px"}
  body-sm: {fontFamily: "inter-regular, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "inter-medium, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.3, letterSpacing: "0.2px"}
  button-md: {fontFamily: "founders-grotesk-medium, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.2, letterSpacing: "0.3px"}
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
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    tagTypography: "{typography.caption}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: "{spacing.sm} {spacing.base}"
  flavor-note-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.md}"
    border: "1px solid {colors.hairline}"

## Components

**button-primary** uses the one confirmed brand accent, the cobalt "#000f8f" seen in the checkout
override, on a solid fill with white text — proposed for primary commerce actions like "Add to
Cart" and "Shop All Coffee."

**button-secondary** mirrors the observed `.recharge-button-secondary` pattern (transparent
background, solid black border) for subscription-management actions such as "Add to Cart" toggles
or "Manage Subscription," with a disabled state in gray per the observed `:disabled` rule.

**text-input** is a proposed pattern for search and account fields, using a light hairline border
and body typography; no live input styling was captured in evidence.

**nav-bar** proposes a white sticky header with black text and a bottom hairline, holding the
observed navigation groups (Shop, Subscribe, Learn, Wholesale) — layout is inferred from content
structure, not measured CSS.

**product-card** is the core commerce unit for the large product grid evident in the page text
(blends, single-origins, subscriptions), pairing a serif/display-adjacent title with flavor-note
tags rendered as small caption chips.

**hero** proposes the top-of-homepage banner ("Coffee you can trust from seed to cup") on a soft
neutral surface with a large display headline — visual proportions are proposed, not observed.

**footer** is inferred as a dark, ink-colored band for secondary navigation (Wholesale, Training
Centers, Store Locator) — no footer CSS was present in evidence.

**badge** covers B Corp/Organic/Sustainably-Sourced labels seen in the page text, using a soft
accent fill; color choice is proposed from the secondary palette, not confirmed per-badge.

**flavor-note-chip** is a category-appropriate component unique to specialty coffee retail,
rendering tasting notes ("floral | melon | citrus") as small pill-shaped labels beneath each
product name.

## Responsive Behavior
| Breakpoint | Width | Notes (proposed) |
|---|---|---|
| Mobile | <640px | Single-column product grid, hamburger nav, sticky cart icon |
| Tablet | 640–1024px | 2-column product grid, collapsed secondary nav |
| Desktop | >1024px | 3–4 column product grid, full horizontal nav |

Touch targets should be at least 44px for cart/add buttons; the mobile menu and cart drawer
(referenced in evidence as "Toggle Main Mobile Menu" and "Close Cart") are assumed to collapse
into slide-in panels. This table is a recommendation based on typical commerce patterns, not
measured site behavior.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered layout, hover state,
animation, or responsive breakpoint was directly observed. The mapping of "#000f8f" to a general
primary role beyond checkout is inferred, as is the assignment of Eiko to display type and
Founders Grotesk/Inter to UI/body type — the CSS evidence names these families but does not show
which selectors use them. The large secondary palette's role as flavor/badge accents is a
plausible but unconfirmed interpretation. Spacing, radius, and most typographic sizes are proposed
defaults, not measured values. Availability, licensing, and web-font loading behavior for Eiko,
Founders Grotesk, Acorn, Inter, and Caveat were not verified. Mobile menu, cart drawer, and search
overlay interactions were not observed in motion.
