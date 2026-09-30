---
version: alpha
name: "Fossil Farms"
source_url: "https://fossilfarms.com"
captured_at: "2026-09-28T10:06:19.646664+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fossil Farms sells premium and exotic game meats to home cooks and chefs, and the
  observed CSS reflects a lean, utilitarian Shopify theme rather than a fully custom
  brand system. The color evidence is dominated by neutrals: near-black ink (#171717,
  #1f1f1f) paired with white and light-gray surfaces (#ffffff, #f2f2f2, #dddddd), which
  we read as the working UI palette. A muted brick red (#aa1f23) appears repeatedly on
  loyalty-balance and referral-share text and is the strongest recurring non-neutral
  color, so it is proposed as the primary brand accent. A small teal (#108474) and a
  muted gold (#b08c37) also appear once each in third-party widget styling; these are
  treated as rare, inferred secondary accents suitable for badges or tags rather than
  core brand color.
  Typography evidence includes Work Sans, explicitly set on the add-to-cart button, and
  Baskerville, Nunito Sans, and Inter among the declared font-family list. We assign
  Baskerville — the only observed serif — to display/heading roles to suit a
  provisions/butcher-shop tone, and Work Sans (confirmed on interactive UI) to buttons
  and body copy, with Nunito Sans/Inter as sans-serif fallbacks. All sizing, spacing,
  and radius values are proposed conventions, not measured layout, and are labeled as
  such throughout.

colors:
  primary: "#aa1f23"
  ink: "#171717"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#dddddd"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  border-strong: "#d1d1d1"
  accent-teal: "#108474"
  accent-gold: "#b08c37"
  overlay-scrim: "#00000080"
typography:
  display-xl: {fontFamily: "Baskerville, serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Baskerville, serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Work Sans, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Work Sans, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Nunito Sans, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Nunito Sans, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Work Sans, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    overlay: "{colors.overlay-scrim}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  freshness-tag:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** is proposed as a solid near-black fill (`{colors.ink}`), matching the observed `background-color: #1F1F1F` on the theme's add-to-cart control, with a darker `#000000` hover state also present in evidence; used for "Add to Cart," "Check Out," and primary CTAs.

**button-secondary** is an outlined, white-fill variant for lower-priority actions (e.g., "Continue Shopping"), using the observed border-gray (`#d1d1d1`) rather than the primary accent, keeping emphasis on button-primary. States (hover, disabled) are proposed, not observed.

**text-input** covers search and account/newsletter fields; the light hairline border and white background follow the neutral palette dominance in evidence. Focus-ring styling is not observed and is proposed as a thin ink-colored outline.

**nav-bar** reflects the site's header/utility-bar pattern implied by the text excerpt (announcement bar, main nav, search/cart icons). Background and foreground map to the theme's declared `--color-background: 255 255 255` and `--color-foreground: 23 23 23` custom properties.

**product-card** is inferred for the Shop grid (game meats, poultry, beef, exotics categories listed in evidence). Card radius and padding are proposed conventions; no card-specific CSS was supplied.

**hero** models the homepage banner ("REWILD THE WAY YOU COOK") as a dark, full-bleed panel with large serif display type, consistent with the ink-heavy palette; exact hero styling was not present in the supplied CSS and is proposed.

**footer** uses the same ink/white pairing as the nav for visual continuity, sized for the multi-column link structure evident in the page text (Quick Links, Information, Market & Kitchen, newsletter signup).

**badge** and **freshness-tag** are proposed small-format labels for merchandising (e.g., "Grass Fed," "Free Range," sale flags). Badge uses the observed brick-red accent; freshness-tag borrows the rarer teal accent to visually differentiate provenance/quality claims from promotional badges — both roles are inferred, not confirmed by evidence.

## Responsive Behavior

Proposed breakpoints (not measured from live layout):

| Breakpoint | Width | Behavior |
|---|---|---|
| Mobile | <640px | Single-column product grid; nav collapses to hamburger + icon bar; hero type steps down to `{typography.display-md}` |
| Tablet | 640–1024px | 2–3 column product grid; sticky condensed nav |
| Desktop | 1024–1280px | Full multi-column nav with mega-menu categories (Game Meats, Poultry, Beef, Exotics, etc.) |
| Wide | >1280px | Content capped near the theme's `--page-width` custom property; additional space becomes margin |

Touch targets should be a minimum 44×44px for cart/menu icons and buttons. Mega-menu category lists (extensive per evidence: Bison, Elk, Wagyu tiers, Exotics, etc.) should collapse into accordions on mobile. This section is a recommendation only; no responsive behavior was directly observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived from static CSS/text extraction only; no rendered page, computed layout, or interaction states were observed. Component states (hover, focus, active, disabled) beyond the two documented add-to-cart rules are proposed conventions. Font pairing (Baskerville for display, Work Sans for UI/body) is an inference from the observed font-family list — actual heading font usage on the live site was not confirmed, and licensing/availability of Baskerville and Work Sans for production use was not verified. Numeric type scale, spacing scale, and border-radius values are proposed design conventions, not measured from the site. Color role assignments (e.g., ink vs. body, teal/gold as rare accents) are best-effort semantic guesses based on frequency and context of use in the supplied CSS, not confirmed brand guidelines. Mobile navigation and cart-drawer behavior were described only in flattened page text, not in layout CSS, so their structure here is inferred.
