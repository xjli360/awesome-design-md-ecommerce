---
version: alpha
name: "Yamaha Pianos"
source_url: "https://usa.yamaha.com/products/musical_instruments/pianos/"
captured_at: "2026-09-29T04:05:00.791879+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from the Yamaha USA piano catalog page, which
  presents acoustic, hybrid, and digital piano families (Grands, Uprights,
  Disklavier, Silent, TransAcoustic, AvantGrand, Clavinova, ARIUS, Portables)
  under a dark hero banner reading "Craftsmanship and innovation in perfect
  harmony." The observed CSS shows a large 100px bold GTAmerica headline
  rendered in white, implying a dark hero background (inferred, not directly
  observed here). Body copy runs in Helvetica Neue/Arial at 14px with a
  precise 1.414213562 line-height, colored #333333 on a white canvas — a
  utilitarian, legible baseline typical of a large industrial catalog site.
  The only fully observed interactive color pair is the lavender CTA button
  (#d6a4e9 background, #000000 text, #dc87f6 hover), reused here as the
  primary action color despite reading as pastel rather than "brand purple."
  A deeper purple (#4b1e78) appears only on small consent/utility links and
  is treated as a secondary accent, not a hero color. Grays (#cccccc,
  #eeeeee, #777777) supply hairlines, muted text, and soft surfaces. Category
  tiles (Grand/Upright/Hybrid/Digital, each with an "Explore" link) and a
  persistent mega-nav are proposed structural components inferred from the
  page's link inventory, not from measured layout.

colors:
  primary: "#d6a4e9"
  primary-hover: "#dc87f6"
  accent-deep: "#4b1e78"
  ink: "#000000"
  body: "#333333"
  canvas: "#ffffff"
  muted: "#777777"
  hairline: "#cccccc"
  hairline-soft: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#fcfcfc"
  surface-alt: "#eeeeee"
  on-primary: "#000000"
  danger: "#cc0000"
typography:
  display-xl: {fontFamily: "GTAmerica, sans-serif", fontSize: 100px, fontWeight: 700, lineHeight: 1.05, letterSpacing: 1px}
  display-md: {fontFamily: "GTAmerica, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.3px}
  title-md: {fontFamily: "GTAmerica, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.414213562, letterSpacing: 0px}
  body-sm: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.3px}
  button-md: {fontFamily: "GTAmerica, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: 4px}
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
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
    hover:
      backgroundColor: "{colors.primary-hover}"
    proposed: false
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.ink}"
    hover:
      backgroundColor: "{colors.surface-soft}"
    proposed: true
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    focus:
      border: "1px solid {colors.accent-deep}"
    proposed: true
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.lg}"
    itemGap: "{spacing.lg}"
    proposed: true
  hero:
    backgroundColor: "{colors.accent-deep}"
    textColor: "#ffffff"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    proposed: true
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    ctaComponent: "button-primary"
    proposed: true
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
    shadow: "0 1px 2px rgba(0,0,0,0.08)"
    proposed: true
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "#ffffff"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    proposed: true
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
    proposed: true
  footer:
    backgroundColor: "{colors.surface-alt}"
    textColor: "{colors.muted}"
    linkTypography: "{typography.body-sm}"
    legalTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.xl}"
    columnGap: "{spacing.xl}"
    proposed: true

## Components
**button-primary** reproduces the page's only fully observed CTA pattern — the `.learn-more-button` / `.cta-text button` rules — with a lavender fill, black text, uppercase 4px-tracked GTAmerica label, square corners, and a lighter lavender hover state (#dc87f6), all directly observed.

**button-secondary** is a proposed outline variant for lower-emphasis actions (e.g., "Find a Dealer" links), using ink-colored text and border with a soft hover fill; no such variant was directly observed.

**text-input** is a proposed generic form control (e.g., site search, dealer-locator ZIP entry) styled with body typography and a hairline border, since no input-specific CSS was supplied.

**nav-bar** models the observed top-level menu structure (Products, Dealer Locator, Support, Shop, My Account, Search) as a light horizontal bar; exact spacing and collapse behavior are proposed, not measured.

**hero** reflects the page's large white GTAmerica headline; because a white h1 implies a dark backdrop, the hero background is inferred using the brand's deep purple accent rather than an explicitly captured hero background color.

**category-tile** represents the Grand/Upright/Hybrid/Digital "Explore" groupings seen in the page text, proposed as bordered cards with a title, short description, and primary-button CTA.

**product-card** is a proposed pattern for individual model listings (e.g., CX Series, Clavinova) not directly present in the supplied evidence but necessary for a usable catalog grid.

**badge** proposes a small pill label (e.g., "New" or "Hybrid") in the site's red accent (#cc0000), unobserved but consistent with the palette.

**search** and **footer** are proposed from the page's text inventory (a "Search" nav item; a dense multi-column footer with legal/copyright text) rather than from captured selectors.

## Responsive Behavior
Recommended breakpoints (not measured): mobile ≤480px, tablet 481–1024px, desktop ≥1025px. Nav collapses to a hamburger/off-canvas menu below tablet width; category tiles reflow from a multi-column grid to a single column on mobile. Touch targets should be at least 44×44px for buttons and nav items. This is a proposed responsive strategy only; no live breakpoint or mobile layout was observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from static CSS/text extraction only; no rendered layout, interaction states (focus, active, disabled), or JavaScript-driven behavior were observed. The hero background color, nav-bar layout, footer structure, product-card, category-tile, badge, and search components are proposed inferences, not captured selectors. Several fonts in the raw evidence (Adelle, Playfair Display, Oswald, Crimson Text, Suranna, Roboto Condensed) appear likely tied to unrelated shared vendor CSS and were excluded from the core type scale as unconfirmed for this page. Licensing/availability of GTAmerica as a web font was not verified. All pixel values in the typography scale beyond the two explicitly observed sizes (100px headline, 16px button, 14px body) are proposed defaults for a coherent scale, not measurements.
