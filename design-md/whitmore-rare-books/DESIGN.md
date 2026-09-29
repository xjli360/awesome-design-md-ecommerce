---
version: alpha
name: "Whitmore Rare Books"
source_url: "https://www.whitmorerarebooks.com"
captured_at: "2026-09-28T04:43:51.813285+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The observed CSS is a customized Bootstrap 3 base layered with a bespoke
  typographic system. Headings (h1–h6) are explicitly set to
  cormorant-garamond with Palatino/Georgia serif fallbacks and a pure black
  (#000000) color, giving the site's titling a classical, antiquarian
  character appropriate to a rare-book dealer. Body copy uses AvenirRegular
  with Trebuchet/Lucida/Tahoma sans-serif fallbacks at 14px, rendered in
  near-black (#070707). The supplied palette contains a distinct ramp of
  burgundy/wine reds (#a5153e, #821438, #c91747, #d21b4f, #780f2d) that
  recur across multiple shades; because no selector in the supplied
  evidence ties a single hex to a named component, this ramp is treated as
  an *inferred* brand-accent family rather than a confirmed primary color,
  most plausibly used for links, active states, or price/CTA emphasis.
  Neutral grays (#d1d1d1, #dddddd, #f5f5f5, #b8b8b8) come from Bootstrap's
  default button and table utility classes and are repurposed here as
  hairlines and soft surfaces. Bootstrap's contextual table colors
  (success green, danger pink, warning tan) are preserved as available
  status tones but are not confirmed to appear in the live storefront UI.
  The overall interpretation favors a restrained, gallery-like layout: serif
  display type for book titles and section headers, quiet sans-serif body
  text, and burgundy used sparingly as an accent against white/near-white
  surfaces.

colors:
  primary: "#a5153e"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#070707"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f5f5f5"
  surface-card: "#f7f6f6"
  on-primary: "#ffffff"
  accent-deep: "#821438"
  accent-bright: "#c91747"
  neutral-btn-bg: "#d1d1d1"
  neutral-btn-border: "#b8b8b8"
  neutral-btn-text: "#222222"
  table-hover: "#d1d1d1"
  success-bg: "#e5f0d5"
  danger-bg: "#ffe7e1"
  warning-bg: "#ffefd6"
typography:
  display-xl: {fontFamily: "cormorant-garamond, Palatino, Georgia, serif", fontSize: "48px", fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "cormorant-garamond, Palatino, Georgia, serif", fontSize: "32px", fontWeight: 400, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "cormorant-garamond, Palatino, Georgia, serif", fontSize: "22px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "AvenirRegular, 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.4285714, letterSpacing: "0px"}
  body-sm: {fontFamily: "AvenirRegular, 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "AvenirRegular, 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif", fontSize: "11px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0.2px"}
  button-md: {fontFamily: "AvenirMedium, 'Trebuchet MS', 'Lucida Grande', 'Lucida Sans Unicode', 'Lucida Sans', Tahoma, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.5px"}
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
    backgroundColor: "{colors.neutral-btn-bg}"
    textColor: "{colors.neutral-btn-text}"
    borderColor: "{colors.neutral-btn-border}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-deep}"
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
  bibliographic-detail:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    authorTypography: "{typography.body-sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.button-md}"
    priceColor: "{colors.primary}"
    padding: "{spacing.base} {spacing.lg}"

## Components

**button-primary** — Proposed as the main call-to-action treatment (e.g. "Inquire about Selling," "Submit Search"), using the burgundy accent ramp as background with white text. Hover/active states are not observed in the supplied CSS and are proposed only.

**button-secondary** — Maps to Bootstrap's `.btn-default` rule, which is explicitly observed (`background-color:#d1d1d1; border-color:#b8b8b8; color:#222` on hover). Used here for lower-emphasis actions like "Browse All."

**text-input** — Inferred from general Bootstrap form resets (`font-family:inherit`); no bespoke input styling was present in the evidence, so border and radius values are proposed defaults consistent with the site's restrained aesthetic.

**nav-bar** — Represents the top navigation containing "Inventory," "Catalogues," "Services," "About Us," and search. Layout, sticky behavior, and active-link color are not confirmed by the supplied CSS and are proposed.

**product-card** — Represents a single New Arrivals entry (author, title, imprint line, price). Card surface, border, and spacing are proposed; only the underlying typography tokens are grounded in observed heading/body rules.

**hero** — Represents the homepage banner ("Offering literary first editions and other books of merit"). Background is assumed white/canvas rather than the literal `body{background:#000}` rule, since a black full-bleed hero is inconsistent with a book-image-driven storefront; this substitution is flagged as inferred, not confirmed.

**footer** — Proposed as a dark, ink-colored band for site-wide links (Contact, FAQ, Open Positions), inverting the light body theme. Not directly observed; based on common antiquarian-bookseller footer conventions.

**badge** — Proposed small pill for tags such as "Inscribed," "First Edition," or "Presentation Copy," which appear frequently in the item text. Color drawn from the accent-deep burgundy; shape and use are inferred.

**search** — Represents the "Advanced Search" / "Submit Search" input pairing referenced in the nav text. Field chrome uses hairline/surface-soft tokens; no unique search-bar CSS was present in evidence.

**bibliographic-detail** — Category-appropriate component modeling the repeated author/title/imprint/price block seen throughout "New Arrivals" (e.g. "Fleming, Ian — Casino Royale — London: Jonathan Cape, 1953 — Price: $170,000"). Price uses the primary burgundy accent to draw attention within an otherwise serif-led, text-dense listing.

## Responsive Behavior

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| xs        | <576px      | Single-column listings, nav collapses to toggle (evidence shows a "Toggle main navigation" control) |
| sm        | 576–768px   | Two-column New Arrivals grid proposed |
| md        | 768–992px   | Three-column grid, inline search proposed |
| lg        | ≥992px      | Full nav bar, multi-column New Arrivals/category browse |

Touch targets are recommended at a minimum of 44×44px for nav toggle and buttons. The presence of a "Toggle main navigation" string confirms a collapsible mobile nav pattern exists, but its breakpoint, animation, and collapsed styling were not present in the supplied CSS and are therefore recommendations only, not measured behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no rendered screenshots, computed styles, or DOM layout were observed.
- The `body{background-color:#000}` rule is present in the evidence but was not adopted as the site canvas color, since it conflicts with a light, book-imagery-driven storefront; this substitution is an interpretive judgment, not a confirmed override.
- The burgundy accent family (`primary`, `accent-deep`, `accent-bright`) is inferred from repeated presence in the palette; no selector in the supplied evidence explicitly assigns these hexes to links, buttons, or price text.
- Font availability and licensing for `cormorant-garamond`, `AvenirRegular`/`AvenirMedium`, and `linotype-sabon` were not verified; fallback stacks are used as declared in the CSS.
- All component paddings, radii, and card/hero layouts are proposed design defaults, not measured from rendered pages.
- Interaction states (hover, focus, active, disabled) beyond the two explicitly observed Bootstrap rules (`.btn-default`, `.btn:hover`) are unconfirmed.
- Mobile/tablet layout behavior is inferred from the presence of a nav-toggle string only; no responsive CSS breakpoints were included in the supplied evidence.
