---
version: alpha
name: "Cohen Media Group"
source_url: "https://cohenmedia.net/"
captured_at: "2026-09-29T04:11:34.935999+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Cohen Media Group's public site presents theatrical and streaming film titles
  ("Winter of the Crow," the Cohen Media Channel) through a dark, cinema-poster-driven
  layout. The supplied palette is dominated by neutral grays and near-blacks
  (#000000, #1e1e1e, #292e31, #333333, #777777, #999999) consistent with a
  poster-forward, low-chroma presentation, punctuated by a single warm
  red-orange accent (#ef4023) inferred here as the primary call-to-action
  color (trailer buttons, "SIGN UP," subscribe links). White (#ffffff) and
  soft off-white/warm neutrals (#f0efea, #d0cec3, #f5f5f5) are treated as
  canvas and card surfaces against poster art. Hairline dividers are inferred
  from light grays (#dddddd, #e5e5e5, #e1e1e1).

  Typography draws from the observed font stack: display headings are
  interpreted using "Playfair Display" for an editorial, classic-cinema tone
  suited to a distributor of restored and independent film, while body copy
  and UI chrome use "Roboto"/"Open Sans" for legibility, and condensed
  "Oswald" is proposed for navigation/button labels and eyebrow metadata
  (e.g., "2026 | DIR: KASIA ADAMIK"). Font-role assignments are inferred from
  the stack, not confirmed via rendered elements. All colors below are reused
  directly from the supplied palette; no new hues were introduced.

colors:
  primary: "#ef4023"
  ink: "#1e1e1e"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#777777"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  ink-deep: "#000000"
  footer-bg: "#292e31"
  warm-neutral: "#d0cec3"
  border-soft: "#e5e5e5"
  muted-strong: "#999999"
typography:
  display-xl: {fontFamily: "'Playfair Display', serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Playfair Display', serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "'Oswald', sans-serif", fontSize: 20px, fontWeight: 500, lineHeight: 1.3, letterSpacing: "0.5px"}
  body-md: {fontFamily: "'Roboto', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Roboto', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Open Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.25px"}
  button-md: {fontFamily: "'Oswald', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1, letterSpacing: "1px"}
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
    textColor: "{colors.canvas}"
    border: "1px solid {colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.ink-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.xl}"
    hairline: "{colors.footer-bg}"
  film-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    titleTypography: "{typography.title-md}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.ink-deep}"
    overlayColor: "#00000080"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    ctaSlot: "{components.button-primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.muted-strong}"
    linkColor: "{colors.on-primary}"
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
    iconColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** is the site's single warm accent, mapped to `#ef4023`, proposed for trailer/watch/subscribe actions ("WATCH TRAILER," "SIGN UP," "START YOUR FREE TRIAL"). Its high contrast against the dark hero background is inferred to carry primary conversion intent.

**button-secondary** proposes an outlined white-on-dark treatment for lower-priority actions ("MORE INFO," "VIEW MORE") that sit adjacent to primary CTAs in carousel/hero regions, avoiding accent-color competition.

**text-input** covers the newsletter signup field, styled with a light card surface and hairline border for legibility against dark hero/footer sections; focus and validation states are not observed and remain proposed.

**nav-bar** represents the top-level "FILMS / NEWS / ABOUT" navigation, assumed dark to match the poster-forward hero; condensed uppercase type is proposed for a marquee-like feel, though exact spacing/height is not measured.

**film-card** is a category-specific component for listing titles (e.g., "Coming Soon," "In Theaters," "Watch at Home" rails implied by the page text). It pairs a poster image slot with title and director/year caption typography, using restrained rounding and neutral card surfaces.

**hero** models the homepage's featured-title slide ("WINTER OF THE CROW"), using a dark overlay over presumed poster/still imagery, large serif display type, and primary/secondary CTA pairing — structure is inferred from the text sequence, not a captured screenshot.

**footer** groups the sitemap links, legal text, and credit line ("Website design by Cyber-NY. Built on Logic CMX"), using the darker footer-bg tone and muted link color for secondary information density.

**badge** is proposed for status labels such as "COMING SOON," using the accent color at small caption scale and full rounding for a pill-shaped tag.

**search**, though not explicitly evidenced in the excerpt, is included as a category-appropriate utility for filtering the film catalog, styled with soft surface and full rounding consistent with other pill-shaped UI proposals.

## Responsive Behavior

This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Width | Nav behavior | Grid |
|---|---|---|---|
| Mobile | <640px | Hamburger/collapsed nav | 1-column film cards |
| Tablet | 640–1024px | Condensed inline nav | 2-column film cards |
| Desktop | >1024px | Full horizontal nav | 3–4 column film cards / full-bleed hero |

Touch targets for buttons and nav items are proposed at a minimum 44px height. Hero CTAs should stack vertically below tablet width. None of this reflects captured DOM/CSS at specific viewports; it is a design recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived solely from static homepage text, a supplied color palette, and a font-family list — no rendered layout, computed styles, or DOM structure were observed. Semantic role assignments (which hex is "primary" vs. incidental icon/utility color, which font applies to which text tier) are inferred from typical distributor-site conventions, not confirmed via inspected elements. All pixel sizes, weights, line-heights, spacing, and rounding values are proposed defaults, not measured from the live site. Interactive states (hover, focus, active, disabled) and mobile/collapsed navigation behavior were not observed. Availability, licensing, and self-hosting terms for the listed font families (e.g., Playfair Display, Oswald, Roboto) were not verified against the site's actual asset delivery. The Font Awesome icon rules present in the evidence are utility/icon-library CSS and were not used to infer brand color or type roles.
