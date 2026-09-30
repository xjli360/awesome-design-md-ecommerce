---
version: alpha
name: "Lisson Gallery"
source_url: "https://www.lissongallery.com"
captured_at: "2026-09-28T04:12:57.059183+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Lisson Gallery's public site exposes a deliberately restrained palette anchored in
  near-absolute black (#000000) and white (#ffffff), consistent with a contemporary
  art gallery letting artwork imagery carry visual weight. Supporting neutrals —
  #1c1c1c, #4d4d4d, #8c8c8c, #cccccc, #dedede — form a tonal ramp mapped here
  (inferred) to ink, body copy, muted labels, hairlines, and soft surfaces
  respectively; the underlying CSS gives no explicit semantic names for these
  values. Several alpha-blended blacks and whites (#0000001a, #00000040, #ffffff4d,
  #8c8c8c1a) appear only as translucency utilities in the extracted rules; they are
  treated (inferred) as hover tints and scrim overlays, not literal brand accents.
  A single red-alpha token (#ff00001a) has no confirmed usage context and is
  reserved (inferred) as an alert/validation tint. Typography draws on two declared
  families: "Lisson Serif" for editorial display headings paired with "Untitled
  Sans" as the workhorse UI/body sans, plus "lissonSerifSC" — inferred as a
  small-caps serif variant — reserved for captions and eyebrow labels. The evidence
  confirms explicit border-radius:0 resets on native form controls, extended here
  into a squared corner language across interactive elements. All font sizes,
  weights, and component paddings below are proposed defaults, not measured page
  values.

colors:
  primary: "#000000"
  ink: "#1c1c1c"
  canvas: "#ffffff"
  body: "#4d4d4d"
  muted: "#8c8c8c"
  hairline: "#cccccc"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  overlay-scrim: "#00000040"
  hover-tint: "#0000001a"
  alert-tint: "#ff00001a"
  transparent: "#00000000"
typography:
  display-xl: {fontFamily: "'Lisson Serif', serif", fontSize: "56px", fontWeight: 400, lineHeight: 1.05, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Lisson Serif', serif", fontSize: "36px", fontWeight: 400, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "'Untitled Sans', sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Untitled Sans', sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Untitled Sans', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'lissonSerifSC', serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.8px"}
  button-md: {fontFamily: "'Untitled Sans', sans-serif", fontSize: "13px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0.5px"}
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
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    height: "5.6rem"
    padding: "{spacing.none} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    captionColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    overlay: "{colors.overlay-scrim}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.alert-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  exhibition-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    metaColor: "{colors.muted}"
    typography: "{typography.title-md}"
    hoverOverlay: "{colors.hover-tint}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"

## Components

**button-primary** — A solid black fill (`{colors.primary}`) with white text, squared corners consistent with the observed `border-radius:0` reset on native buttons/inputs. Used (proposed) for primary calls to action such as "Enquire" or "Subscribe." Hover/focus states are not observed and should use `{colors.overlay-scrim}` as a proposed darkening treatment.

**button-secondary** — A transparent-background, hairline-bordered variant using `{colors.ink}` for the border and `{colors.primary}` for text, appropriate for secondary actions like "View exhibition" links. States (hover, disabled) are proposed, not measured.

**text-input** — A flat, unrounded field on `{colors.canvas}` with a `{colors.hairline}` border, matching the CSS evidence that resets input `border-radius` to `0` and inherits font/letter-spacing. Focus-ring styling is not observed and is proposed only.

**nav-bar** — A fixed-height header using the observed `--nav-mobile-height` custom properties (4.8rem–5.6rem across breakpoints) as the basis for the proposed `height` token. Background and text follow the canvas/ink pairing; a hairline bottom border is proposed for separation from content.

**product-card** — Reinterpreted for gallery inventory as an artwork tile: a white surface card with ink-colored primary text and muted caption text for artist/medium metadata. No card shadow or radius is evidenced, so `rounded.none` and a flat surface are used.

**hero** — A full-bleed introductory section pairing the serif `display-xl` treatment with a proposed dark scrim (`{colors.overlay-scrim}`) for text legibility over imagery. Padding draws loosely from the large observed `--padding-l`/`--padding-xl` spacing variables (14.8rem–18.6rem), scaled down to the standard spacing scale.

**footer** — An inverted block using `{colors.ink}` as background and `{colors.on-primary}` (white) text, consistent with a gallery site's tendency to bookend content in high-contrast bands. Link and legal-text hierarchy is proposed, not observed.

**badge** — A small pill using the reserved `{colors.alert-tint}` (a very light red) for status or "new" indicators such as sold/available flags on artworks. This is a proposed usage; no live badge markup was present in the evidence.

**search** — A soft-gray (`{colors.surface-soft}`) input field distinct from standard text inputs, intended for site-wide artist/exhibition search. Placeholder text uses `{colors.muted}`; interaction states are proposed.

**exhibition-card** — The category-appropriate component: a listing tile for current/upcoming exhibitions, pairing a mid-weight sans title (`typography.title-md`) with muted date/location metadata and a proposed hover tint (`{colors.hover-tint}`) to signal interactivity.

## Responsive Behavior

This is a recommendation only; no live responsive layout was observed. The evidence includes shifting `--grid-count` values (8 and 12) and `--nav-mobile-height` values (4.8rem, 5.6rem), suggesting the site adapts column count and header height across at least two viewport tiers — treated here as inferred confirmation that a mobile/desktop split exists, without confirmed pixel breakpoints.

| Breakpoint | Range (proposed) | Grid | Notes |
|---|---|---|---|
| Mobile | up to 767px | 8 columns (inferred) | Nav height ~4.8rem; stack cards single-column |
| Tablet | 768–1199px | 8–12 columns (inferred) | Nav height ~5.6rem; 2-column card grids |
| Desktop | 1200px+ | 12 columns | Full multi-column exhibition/artwork grids |

Touch targets should be a minimum 44×44px hit area for `button-primary`/`button-secondary`. Nav items should collapse into a hamburger/drawer pattern below the tablet breakpoint (proposed, not observed). Search should expand to a full-width overlay on mobile (proposed).

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static (CSS + a title string only); no rendered page, computed styles, or component markup was observed, so all layout composition is inferred or proposed.
- Color role assignments (e.g., which gray is "muted" vs "body") are inferred from typical usage patterns, not confirmed by class-name-to-role mapping in the supplied rules.
- All typography `fontSize`/`fontWeight`/`lineHeight` values are proposed defaults; the source CSS did not expose font-size declarations for any role.
- The spacing and rounded scales follow a standardized proposed system rather than the site's raw `rem` custom properties (e.g., `--spacing-m:1.2rem`, `--padding-l:14.8rem`); numeric correspondence is approximate.
- No hover, focus, active, or disabled states were observed for any interactive component; all are labeled proposed.
- Mobile/tablet layout, navigation collapse behavior, and touch interactions were not observed and are recommendations only.
- Availability and licensing of "Lisson Serif," "Untitled Sans," and "lissonSerifSC" as web fonts were not verified; fallbacks are generic (`serif`/`sans-serif`).
- The single red-alpha token's real-world usage (alert, error, or decorative) is unconfirmed and treated as inferred.
