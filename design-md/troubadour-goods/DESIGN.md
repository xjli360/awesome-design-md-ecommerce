---
version: alpha
name: "Troubadour Goods"
source_url: "https://troubadourgoods.com"
captured_at: "2026-09-29T04:10:34.440086+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Troubadour presents itself as a restrained, design-forward carry brand: matte
  neutrals, one warm gold accent, and a mix of a humanist sans (Inter) for
  reading copy with IBM Plex Mono reserved for uppercase labels and buttons
  (observed directly on `.button.tertiary`, which sets
  `font-family:var(--font-ibm-plex-mono)`, `text-transform:uppercase`, and
  `font-size:.8125rem`). The supplied palette is dominated by near-black and
  near-white values (`#000000`, `#ffffff`, `#2c2c2c`, `#1a1a1a`, `#111827`)
  alongside warm off-whites (`#f0efeb`, `#f7f6f3`, `#f4f1f0`) that read as
  paper/canvas surfaces rather than pure white cards. `.button.primary` and
  `.button.secondary` both resolve to the same dark charcoal
  (`rgb(44 44 44)`), so this system treats charcoal as the primary action
  color rather than pure black, with pure black (`.button.black`) as a
  secondary emphatic variant. `#e1b22c` (`.button.primary-alt`) is the only
  saturated brand accent observed and is mapped here to award/CTA highlight
  use. Grays (`#9ca3af`, `#6b7280`, `#d1d5db`, `#e5e7eb`) are inferred as a
  Tailwind-style utility scale for muted text, hairlines, and disabled
  states — their exact semantic roles are not confirmed by the evidence and
  are treated as inferred. Heading rhythm for long-form content is grounded
  in the `.prose h1` rule (`font-size:2.25em; font-weight:800;
  line-height:1.11111`), which informs, but does not fix, the proposed
  display scale below.

colors:
  primary: "#2c2c2c"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#1a1a1a"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  surface-soft: "#f0efeb"
  surface-card: "#f7f6f3"
  on-primary: "#ffffff"
  accent-gold: "#e1b22c"
  accent-hover: "#c44800"
  border-strong: "#d1d5db"
  eco-green: "#69815b"
  eco-green-deep: "#516657"
  alert: "#c30102"
  link: "#2563eb"
  overlay: "#00000066"
  paper-warm: "#f4f1f0"
typography:
  display-xl: {fontFamily: "Inter, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.11, letterSpacing: -0.5px}
  display-md: {fontFamily: "Inter, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "IBM Plex Mono, monospace", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
  button-md: {fontFamily: "IBM Plex Mono, monospace", fontSize: 13px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.5px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-tertiary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid transparent"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    height: "72px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.paper-warm}"
    overlay: "{colors.overlay}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  laptop-fit-indicator:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary** maps to the observed `.button.primary`/`.button.secondary` rule, both resolving to a `#2c2c2c` background with white text — used here as the main add-to-bag and shop CTA. **button-secondary** is a proposed outline treatment for lower-emphasis actions (e.g. "View Details"), since no distinct secondary style was distinguishable in the evidence beyond `.button.outlined`. **button-tertiary** is directly grounded in `.button.tertiary`: warm off-white background, mono uppercase label, no visible border — suited to filter chips or "Continue Shopping" links. **text-input** is proposed (no form-field CSS supplied) but follows the site's hairline/rounded-xs vocabulary. **nav-bar** is inferred from the text navigation list (Featured, Bags, Accessories, iPhone Cases, About Us) with a plain white background and black text; exact height/behavior is proposed, not measured. **product-card** is proposed for grid listings (visible "New in" / "Loading..." placeholders suggest a card grid) using the warm card surface and hairline border. **hero** models the homepage banner copy ("New styles for our minimalist carry") against a warm paper background with a primary CTA; overlay is proposed for any image-backed hero variants. **footer** is inferred from the footer link groups (About, Help, Shop, Collections, Social) rendered in a dark, high-contrast band. **badge** is proposed for award/press callouts (Red Dot, Esquire) using the single gold accent. **search** is proposed styling for the "Search" nav item, reusing the tertiary surface tone. **laptop-fit-indicator** is a category-specific proposed component — a small spec chip (e.g. "Fits 16\" Laptop") appropriate to a daily/laptop backpack catalog, styled with the same caption typography and card border as other metadata tags; it is not evidenced in the supplied CSS and is purely a category-fit proposal.

## Responsive Behavior

Recommended, not measured — no breakpoint or viewport CSS was present in the supplied evidence.

| Breakpoint | Width      | Layout notes (proposed) |
|-----------|------------|--------------------------|
| mobile    | < 640px    | Single-column product grid, collapsed hamburger nav, stacked hero text |
| tablet    | 640–1024px | 2-column product grid, nav links may collapse into a menu |
| desktop   | > 1024px   | 3–4 column product grid, full horizontal nav visible |

Touch targets should be at least 44×44px for buttons and nav items; the mono uppercase button label style should retain adequate horizontal padding (`{spacing.lg}`) at small sizes to preserve tap area. Mobile nav is expected to collapse into a drawer or overlay using `{colors.overlay}`, though this interaction was not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.




- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is built from static CSS/text extraction only; no rendered page, computed layout, or interaction states (hover/focus/active beyond the listed `:hover` rules) were observed. Several color roles (muted grays, green tones, red/blue values) are inferred from typical Tailwind-style utility usage and are not confirmed against actual rendered UI. Font sizes and weights outside the `.prose h1` and `.button.tertiary` rules are proposed estimates, not measured values. Responsive breakpoints, mobile menu behavior, product-card grid structure, and form-field styling were not present in the supplied evidence and are marked proposed throughout. Availability and licensing of Inter, IBM Plex Mono, and Roboto for production use were not verified here and should be confirmed independently before implementation.
