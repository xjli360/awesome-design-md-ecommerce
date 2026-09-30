---
version: alpha
name: "Recess"
source_url: "https://takearecess.com/"
captured_at: "2026-09-29T03:58:24.427849+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Recess's storefront evidence centers on a single dominant hue family: a deep
  navy (#25385b) that recurs across dozens of alpha-blended variants (from
  #25385b0d through #25385bf2), indicating it drives both text and translucent
  overlay/scrim treatments across the page. Internal CSS variable names
  (--color-cloud-burst, --color-melrose) point to a navy-on-lavender scheme;
  since exact hex-to-name mapping wasn't directly exposed, the nearest observed
  navies (#25385b, #1d2a58) and lavenders (#c2caff, #a8b2ff) are used here and
  labeled inferred. White (#ffffff) and light grays (#f0f0f0, #dedede) supply
  neutral canvas and card surfaces. A cluster of soft, semi-transparent pastel
  tones (pink, peach, yellow, sky, mint, all at ~90% alpha) appears tied to
  flavor/product swatches rather than UI chrome, so they are mapped to
  flavor-swatch roles only. Typography runs on Sharp Grotesk Web as the
  workhorse sans, with Antidote Display Web referenced for display-scale
  headings; both fall back to system sans-serif stacks. Buttons show a
  consistent 2px solid border, bold 700 weight, and generous clamp-based
  padding, suggesting an outlined, editorial button style rather than filled
  pills. Corner radii were not observed in the supplied CSS, so the rounded
  scale below is a conservative proposed default for a calm, low-chrome
  wellness-beverage aesthetic.

colors:
  primary: "#25385b"
  ink: "#1d2a58"
  canvas: "#ffffff"
  body: "#25385b"
  muted: "#565c70"
  hairline: "#25385b1a"
  surface-soft: "#c2caff"
  surface-card: "#f0f0f0"
  on-primary: "#ffffff"
  overlay-strong: "#25385bf2"
  overlay-soft: "#25385b33"
  accent-blue: "#163bf3"
  accent-purple: "#482e96"
  accent-green: "#47722a"
  accent-mauve: "#993e56"
  accent-peach: "#ffc8a0"
  danger: "#c51d1d"
  border-neutral: "#b1b1b1"
  flavor-pink: "#ffafb4e6"
  flavor-peach: "#ffcfa5e6"
  flavor-yellow: "#fff9b2e6"
  flavor-sky: "#9ddeffe6"
  flavor-mint: "#a6efb8e6"
typography:
  display-xl: {fontFamily: "Antidote Display Web, Sharp Grotesk Web, sans-serif", fontSize: 96px, fontWeight: 700, lineHeight: 1.05, letterSpacing: -1px}
  display-md: {fontFamily: "Antidote Display Web, Sharp Grotesk Web, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.3px}
  title-md: {fontFamily: "Sharp Grotesk Web, system-ui, sans-serif", fontSize: 36px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  body-md: {fontFamily: "Sharp Grotesk Web, system-ui, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Sharp Grotesk Web, system-ui, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Sharp Grotesk Web, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Sharp Grotesk Web, system-ui, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.125, letterSpacing: 0.2px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-neutral}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    borderColor: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-peach}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.border-neutral}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  flavor-swatch:
    backgroundColor: "{colors.flavor-sky}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.sm}"

## Components
- **button-primary**: A solid navy, square-cornered call-to-action button ("SHOP NOW," "SHOP ALL PRODUCTS") using the 700-weight button typography observed in the `.button` rule and a 2px border implied by the CSS `--_size-button-border` variable. Rounded is set to none since no radius was observed on `.button`; hover/active states are proposed, not confirmed.
- **button-secondary**: An outline variant on white/canvas background with navy border and text, intended for secondary actions (e.g., "login," sampler links). State transitions (hover fill, focus ring) are proposed only.
- **text-input**: Used for the newsletter/email capture ("email*" fields). Styling (light border, subtle rounding) is inferred from general form conventions; no explicit input CSS was supplied.
- **nav-bar**: A top-level horizontal navigation with logo, shop menu, subscribe & save, login, and cart count. Sticky/scroll behavior and the announcement-bar rotation ("free shipping," "10% off") are described from page text but their exact CSS timing/easing is not observed.
- **product-card**: Represents individual SKUs and sampler packs (Mood, Zero Proof, Mood Powder, original Recess lines). Card background uses the light-gray surface token; layout, image aspect ratio, and hover elevation are proposed, category-typical patterns.
- **hero**: The homepage hero introducing "Zero Proof Apple + Espresso 'Tinis" and the "calm cool collected" tagline, using the largest display typography scale (mapped from the 6rem heading-size token) against the soft lavender surface. Exact hero height/animation ("poof" motif) is referenced in page text but not measured.
- **footer**: Full-width navy footer containing sitemap links (shop, information, community), trademark/legal disclaimers, and newsletter signup, using white-on-navy contrast for legibility.
- **badge**: Small pill labels for promotional callouts (e.g., discount code "TAKE10") or flavor tags, using a warm peach accent for visual warmth against the cool navy system; exact usage context is inferred from the announcement-bar text.
- **search**: A rounded search affordance proposed for product/flavor lookup; not directly evidenced in the supplied CSS but included as a category-typical component.
- **flavor-swatch**: A category-specific component representing the many flavor variants (peach ginger, blood orange, orange vanilla Mood, etc.), using the observed pastel alpha-blended colors (pink, peach, yellow, sky, mint) as small rounded tags or dots beside product names.

## Responsive Behavior
Recommended (not measured) breakpoint table:
| Breakpoint | Width | Notes |
|---|---|---|
| sm | ≤640px | Single-column stacks; nav collapses to menu icon (proposed); container gutter narrows per `--container-gutter` clamp behavior implied at 6–8vw. |
| md | 641–1024px | Two-column product grids; hero heading steps down from the 6rem to ~3.75–5rem tier observed in `--heading-size` variables. |
| lg | 1025px+ | Full multi-column layouts; container inline size caps at `min(90rem, 88dvw)` per observed `--size-container-inline-lg`. |

Touch targets should be a minimum 44×44px for buttons and nav items; the announcement bar and sticky nav collapse behavior on mobile is not observed and should be validated against the live site before implementation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Colors are extracted from static CSS custom properties and computed styles; exact usage context (which element uses which alpha variant) is partially inferred from naming and repetition, not visual inspection.
- CSS variable names `--color-melrose` and `--color-cloud-burst` suggest a lavender/navy background-text scheme, but their literal hex values were not directly exposed in the supplied evidence; `#c2caff`/`#a8b2ff` and `#25385b`/`#1d2a58` are the closest observed candidates and are labeled inferred.
- No `border-radius` values were present in the supplied CSS; the rounded scale is a proposed default, not evidence-based.
- Spacing scale beyond the observed gutter variables (`--container-gutter`, `--y-gutter`) is proposed using conventional 4/8px multiples.
- Interaction states (hover, focus, active, disabled beyond the one `.button:disabled` rule) and mobile/responsive layout behavior were not observed and are marked proposed throughout.
- "Antidote Display Web" and "Sharp Grotesk Web" appear as font-family references in the supplied evidence; their licensing, hosting, and actual render fidelity were not verified.
- This document describes the current takearecess.com parent-site presentation of the Recess brand; no independent legacy site was reconstructed.
