---
version: alpha
name: "Magnolia Pictures"
source_url: "https://www.magpictures.com"
captured_at: "2026-09-29T04:21:44.659242+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Magnolia Pictures presents itself through a high-contrast, cinematic surface: a
  near-black-on-white (and white-on-black) palette drawn from the site's own
  declarations (#ffffff, #222222, #181818, #000000) rather than the many
  third-party social-icon hexes (Facebook blue, YouTube red, Pinterest red, etc.)
  that appear in the raw evidence but are treated here as unrelated share-widget
  colors, not brand identity. Supporting neutrals (#f6f6f6, #ebebeb, #dddddd,
  #999999, #333333) are inferred as tonal steps for surfaces, hairlines, and
  secondary text based on their grayscale character.

  Typography is confidently bimodal: Oswald appears at an oversized 128px for the
  hero/logo treatment, condensed-uppercase and cinematic, while proxima-nova
  carries body copy, form labels, and buttons at small, letter-spaced sizes,
  with Helvetica Neue/Arial as the structural fallback and button font. This
  suggests a design language of one dramatic display face over a quiet
  functional sans, appropriate for a film distributor whose hero imagery (film
  stills, trailers) should dominate. Rounded corners and spacing scales below
  are proposed conventions, not measured, since only isolated declarations were
  supplied.

colors:
  primary: "#222222"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  overlay-dark: "#181818"
  border-soft: "#efefef"
  shadow-tint: "#ebebeb"
  disabled: "#cccccc"
typography:
  display-xl: {fontFamily: "Oswald, sans-serif", fontSize: 128px, fontWeight: 400, lineHeight: 1em, letterSpacing: 0.01em}
  display-md: {fontFamily: "proxima-nova, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.14em}
  title-md: {fontFamily: "'Helvetica Neue', Arial, sans-serif", fontSize: 30px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 2px}
  body-lg: {fontFamily: "'Helvetica Neue', Arial, sans-serif", fontSize: 26px, fontWeight: 400, lineHeight: 1.3em, letterSpacing: 0.5px}
  body-md: {fontFamily: "proxima-nova, sans-serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.4em, letterSpacing: 0.01em}
  body-sm: {fontFamily: "proxima-nova, sans-serif", fontSize: 13px, fontWeight: 400, lineHeight: 1.4em, letterSpacing: 0.01em}
  caption: {fontFamily: "proxima-nova, sans-serif", fontSize: 12px, fontWeight: 700, lineHeight: 1.3em, letterSpacing: 0em}
  button-md: {fontFamily: "'Helvetica Neue', Arial, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 2px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.on-primary}"
    border: "2px solid {colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
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
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  hero:
    backgroundColor: "{colors.overlay-dark}"
    textColor: "{colors.on-primary}"
    displayTypography: "{typography.display-xl}"
    eyebrowTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-lg}"
    padding: "{spacing.section}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-soft}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    hairline: "{colors.overlay-dark}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  channel-subscribe-card:
    backgroundColor: "{colors.overlay-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-secondary"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"

## Components
**button-primary** renders as a solid white pill/rectangle with dark (#222222) text, matching the observed `background:#fff;color:#222;border-style:none` rule used on the cover-page's solid-style call-to-action (e.g. "DISCOVER OUR FILMS"). Hover state is proposed as a subtle shadow lift, since only a raised-variant box-shadow (`0 .2em 0 0 #ebebeb`) was observed for a related button style.

**button-secondary** mirrors the observed outline-style button: transparent background, white 2px border, white text, transitioning to a dark (#181818) fill/text pairing on hover per the supplied `:hover{color:#181818}` and `background-color:#fff` rules. Used for secondary actions like "SUBSCRIBE TO MAGNOLIA SELECTS" when placed over hero imagery.

**text-input** is a proposed pattern for newsletter/subscribe forms implied by the `.form-wrapper input[type=submit]` selectors in evidence; exact input-field styling (borders, focus rings) was not directly observed and is inferred from the site's hairline and body-copy tokens.

**nav-bar** is proposed as a clean white bar with dark, letter-spaced caption-style labels, consistent with the brand's uppercase, tracked-out button and heading treatments seen throughout the evidence; actual nav markup/behavior was not present in the supplied CSS.

**hero** models the "cover-page" slide type directly evidenced: a full-bleed dark section with an oversized Oswald title (128px), a tracked-out proxima-nova eyebrow/subheading, and Helvetica Neue body copy at 26px — matching the `.sqs-slide-wrapper[data-slide-type="cover-page"]` rules supplied.

**product-card** (film/title card) is proposed for a films grid or catalog listing; it borrows title-md for film titles and body-sm for metadata (year, genre), since no explicit card markup was in the evidence — this is an inferred, category-appropriate extrapolation.

**footer** is proposed as a dark, ink-colored band with small body-copy, consistent with the site's dark-overlay hero treatment; footer-specific CSS was not present in the supplied rules.

**badge** is a small pill label (e.g. "NEW," "COMING SOON") using the caption typography's bold, uppercase, tightly-set 12px style observed in the form-submit declarations; this is a proposed reuse of an observed type style into a new component, not an observed badge.

**search** is a proposed lightweight input using surface-soft background and body-md typography; no search UI was present in the evidence.

**channel-subscribe-card** is the category-appropriate component for Magnolia Selects, the brand's curated streaming channel mentioned in the page text ("Enjoy our curated channel Magnolia Selects... SUBSCRIBE TO MAGNOLIA SELECTS"). It is proposed as a dark card pairing the display-md eyebrow style with a button-secondary CTA, since this is a named, distinct product offering on the page but no dedicated card CSS was supplied.

## Responsive Behavior
This is a recommendation, not measured site behavior, as no media queries were present in the supplied evidence.

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | < 600px     | Single-column stacking; hero display-xl scales down substantially (e.g. to ~48–64px) to remain legible; nav collapses to a hamburger/menu overlay. |
| tablet    | 600–1024px  | Two-column product-card grid; hero eyebrow and body remain but display-xl scales to ~80–96px. |
| desktop   | 1024–1440px | Full hero at or near observed 128px display size; multi-column film grids. |
| wide      | > 1440px    | Max-width content container with generous section padding ({spacing.section}). |

Touch targets should be at least 44×44px for buttons and nav items; primary/secondary buttons' padding ({spacing.md} {spacing.lg}) approximates this at larger font sizes but should be verified. Navigation is assumed to collapse into a mobile menu below the tablet breakpoint; no such interaction was observed in the supplied static CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from a limited, static snapshot of CSS declarations and a page-text excerpt for a single cover-page slide type; it does not reflect full-site crawling, JavaScript-driven states, or responsive breakpoints. The large supplied color list includes numerous well-known third-party brand/social-icon hexes (e.g. Facebook, Twitter, YouTube, Pinterest, Instagram colors) that were deliberately excluded from the design tokens as non-brand noise; only grayscale/neutral values with clear in-context CSS usage were promoted to tokens. Semantic role names (primary, muted, surface-soft, etc.) are inferred mappings onto observed hex values, not labels present in the source CSS. Several typography sizes (body-sm) and most spacing/rounded values are proposed conventions rather than measured from the evidence. No interaction states (focus rings, active states, mobile menu behavior, card hover) were observed beyond the two button hover rules supplied. Font availability, licensing, and self-hosting versus third-party CDN delivery for Oswald and proxima-nova were not verified. This is presented as the current Squarespace-hosted parent-site presentation of Magnolia Pictures, not a reconstruction of any prior or independent site design.
