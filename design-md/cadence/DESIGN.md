---
version: alpha
name: "Cadence"
source_url: "https://keepyourcadence.com"
captured_at: "2026-09-28T09:30:28.905590+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Cadence's storefront CSS shows a warm, neutral-first palette (whites and soft
  stone tones such as #f7f5f3, #f0ede9, #ebe5dd, #d0cac3) paired with a single
  saturated brand color, deep merlot/oxblood #682b1f, used as the sole observed
  button background in the theme's .btn rule. Body copy runs on a near-black ink
  (#2b2b2b), with #000000 appearing as a literal 1px header hairline. A large
  supplied palette also includes seasonal/collection accents — lavender "jelly"
  tones (#b5b5db, #8fb4f4), a mustard/yellow alert tone (#ffe302), and a second
  red (#a51313) — which are treated here as limited-drop/badge accents rather
  than core UI color, since their functional role is not confirmed by the
  evidence. Typography is built on a proprietary "Spezia" family (SpeziaMedium
  for body text per html,body; SpeziaBold for headings and buttons;
  SpeziaCustomMedium for a specific large centered header treatment at 34px/
  -0.88px tracking), with sans-serif as the only confirmed fallback. Availability
  and licensing of Spezia are not verified. The interpretation favors a calm,
  editorial retail feel — generous neutral surfaces, one confident brand-red
  action color, and restrained hairline borders — appropriate to a premium
  travel-organization goods brand. Component states beyond the base .btn and
  header rules are inferred, not observed.

colors:
  primary: "#682b1f"
  ink: "#2b2b2b"
  canvas: "#ffffff"
  body: "#2b2b2b"
  muted: "#606060"
  hairline: "#000000"
  border-light: "#d0cac3"
  surface-soft: "#f7f5f3"
  surface-card: "#f0ede9"
  surface-alt: "#ebe5dd"
  on-primary: "#ffffff"
  accent-merlot: "#a51313"
  accent-jelly: "#b5b5db"
  accent-alert: "#ffe302"
typography:
  display-xl: {fontFamily: "SpeziaBold, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "SpeziaCustomMedium, sans-serif", fontSize: 34px, fontWeight: 400, lineHeight: 1.2, letterSpacing: -0.88px}
  title-md: {fontFamily: "SpeziaBold, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "SpeziaMedium, SuisseInt, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "SpeziaMedium, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "SpeziaMedium, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "SpeziaBold, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.42, letterSpacing: 0.2px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-light}"
    textColor: "{colors.body}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    borderBottomColor: "{colors.hairline}"
    padding: "{spacing.lg}"
    itemTypography: "{typography.body-sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted}"
    padding: "{spacing.section} {spacing.lg}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
    typography: "{typography.caption}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    headerBorderColor: "{colors.hairline}"
    lineItemTypography: "{typography.body-sm}"
    progressTrackColor: "{colors.surface-alt}"
    progressFillColor: "{colors.primary}"
    ctaComponent: "button-primary"

## Components

**button-primary** reflects the theme's actual `.btn` rule: a solid `#682b1f` fill, white text, `SpeziaBold` at `.875rem`/600 weight, and a `2px` corner radius — this is the only observed interactive-color mapping in the evidence and is used here for primary checkout/CTA actions.

**button-secondary** is a proposed outline variant sharing the same brand color as border and text on a transparent fill, for lower-emphasis actions like "Shop Now" links; no outline button was directly observed.

**text-input** is inferred from the neutral border/canvas palette; no explicit input CSS was supplied, so border color, radius, and padding are proposed defaults consistent with the hairline and radius scale used elsewhere.

**nav-bar** is grounded in `.header-container` (flex, space-between, `#fff` background, `25px` padding, solid 1px black bottom border) — padding and hairline are observed; the compact drawer/back-button pattern (`.new-navigation .back-button`) confirms a slide-out mobile nav exists, though its full layout is not verified.

**product-card** is a proposed pattern for the observed capsule/parcel product grid (Small/Medium/Large, Skincare, Haircare, etc.); no card-specific CSS was supplied, so surface color and spacing are inferred from the general neutral surface palette.

**hero** maps to the `.cadfont-h2-header` rule (centered `SpeziaCustomMedium` headline at 34px, -0.88px tracking) seen for section headers like "Life, in cadence" — treated as a hero/section-intro pattern rather than a literal full-bleed hero, since no hero-specific background or image CSS was supplied.

**footer** color mapping is uncertain: `html,body` sets `background-color:#2b2b2b; color:#2b2b2b`, an ambiguous dark-on-dark rule likely overridden per-section. It is applied here to the footer only, as a plausible dark closing band, and is flagged as an inferred/uncertain mapping.

**badge** supports the repeated feature chips in the copy ("Leakproof," "Magnetic," "TSA-compliant," "Sustainable") as small pill labels; no badge CSS was supplied, so styling is proposed.

**cart-drawer** is a category-appropriate proposed component built from the observed cart copy ("You are $100 away from free shipping," gift note, quantity stepper) — a slide-in panel with a shipping-progress bar using the brand merlot as fill color; visual treatment of the progress bar itself is not observed.

**search** is inferred minimally; a `Search` nav item exists in the text content but no search-input CSS was supplied.

## Responsive Behavior
| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| mobile | 0–599px | Single-column product grid; nav collapses to the observed drawer/back-button pattern; sticky bottom CTA on PDP proposed. |
| tablet | 600–1023px | 2-column product grid; nav-bar padding reduces toward `{spacing.base}`. |
| desktop | 1024px+ | Full `.header-container` flex row as observed; multi-column mega-menu proposed for Capsules/Parcels/Accessories. |

Touch targets should be a minimum 44px hit area on all buttons and drawer controls. This table is a recommendation based on general commerce conventions, not measured site behavior; no media queries were included in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, computed styles, or DOM screenshots were available. Semantic color roles (primary, ink, muted, hairline, surface tiers) are inferred from selector names and usage context, not confirmed via a live design system or style guide. The `html,body` dark-on-dark background/color pair is contradictory in the raw CSS and its true rendered effect is unknown. Most typography sizes beyond the two directly observed rules (`.btn` and `.cadfont-h2-header`) are proposed, following the family names found in the CSS but not their exact sizes/weights per level. The custom "Spezia" font family's licensing, availability, and full weight range are not verified — sans-serif fallback is assumed throughout. No hover, focus, active, disabled, or error states were observed for any component; all are proposed. Mobile menu, cart drawer, and carousel interactions referenced in the page text were not visually confirmed. Rounded and spacing scales beyond the single observed `2px`/`.7rem` values are proposed conventions, not extracted measurements.
