---
version: alpha
name: "Analogman"
source_url: "https://www.analogman.com"
captured_at: "2026-09-29T04:21:06.555630+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Analogman's own site (analogman.com) is a legacy, text-first reference page that the
  company itself describes as its "original website," kept live for its archive of
  product history while commerce has moved to buyanalogman.com. The only evidence
  recovered is a near-default browser stylesheet: black body copy on a white canvas,
  Times serif typography, and the standard unvisited-hyperlink blue (#0000ee) used
  throughout for the dense "quick and dirty links" index. There is no evidence of a
  custom color system, spacing scale, or component styling in the supplied CSS —
  headings share the same black color and transparent background as body text, and
  borders resolve to the same black as the ink.
  This interpretation treats that plainness as the brand voice: utilitarian, dense,
  hand-written, workshop-like, in contrast to glossy "boutique pedal" marketing. The
  blue link color is promoted to a primary accent for buttons and interactive states
  since it is the only non-neutral hue observed. Muted text, hairlines, and card
  surfaces are inferred and mapped onto the same three observed hex values (reused
  per instructions) rather than invented tones. All spacing, radii, and type sizes
  below are proposed defaults for a modern re-skin, not measurements taken from the
  live page.

colors:
  primary: "#0000ee"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#000000"
  hairline: "#000000"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "Times, serif", fontSize: 40px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  display-md: {fontFamily: "Times, serif", fontSize: 28px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "Times, serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Times, serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Times, serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Times, serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Times, serif", fontSize: 15px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.lg}"
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
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  pedal-index-row:
    backgroundColor: "{colors.surface-card}"
    linkColor: "{colors.primary}"
    dividerColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.sm}"

## Components

**button-primary** renders the site's single accent hue (#0000ee, the observed default link blue) as a solid fill with white text, proposed for primary calls to action such as "Shop at buyanalogman.com." No hover/active state was observed; states beyond default are proposed.

**button-secondary** is an outlined variant using the same blue for border and label on a white field, intended for lower-emphasis actions like "View Manuals" or "Check Order Status." Interaction states are proposed, not measured.

**text-input** is a plain bordered field using the black hairline and body typography, appropriate for a proposed contact or waitlist form; no form styling was present in the supplied evidence.

**nav-bar** proposes a simple top bar listing the site's many "quick and dirty links" (Amps, Fuzzface, King of Tone, Repairs, etc.) as blue text links on white, echoing the flat, list-dense structure of the original page rather than a modern mega-menu.

**product-card** is a proposed container for individual pedal listings (name, short description, availability note), using a hairline border and white surface since no card styling exists in the source; this is a structural proposal for organizing the long link index into discrete units.

**hero** proposes a plain, text-forward top section stating the brand's "USA Made, hand-built" positioning, matching the page's actual emphasis on craftsmanship copy rather than any imagery, since no hero imagery or layout was observed.

**footer** carries the contact/hours/legal text seen in the excerpt (address, hours, email routing by department) in small body copy with blue links, mirroring the page's dense administrative footer content.

**badge** is proposed for short status labels such as "In Stock," "No Delays," or "KOT List," using the accent blue as a fill; no such visual badge was observed, only inline text like "No Delays on almost all pedals!"

**pedal-index-row** is a category-specific proposed component for the long alphabetical list of pedal/brand names (Tube Screamers, Sun Face, ARDX20, etc.), rendered as simple divided rows of blue links, staying faithful to the source's list-based navigation pattern rather than introducing a grid the evidence doesn't support.

## Responsive Behavior

Proposed breakpoints (not measured from the live site): mobile ≤480px, tablet 481–768px, desktop ≥769px. Below tablet, nav-bar and pedal-index-row are recommended to collapse into a single-column stacked list, since the source text explicitly notes a separate mobile-friendly commerce site (buyanalogman.com) rather than describing responsive behavior on analogman.com itself. Touch targets for button-primary/secondary and pedal-index-row links should be at least 44×44px per standard accessibility guidance. This section is a recommendation for a re-skin, not an observation of analogman.com's actual responsive markup or breakpoints.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This DESIGN.md is derived from a static computed-style snapshot limited to three colors (#0000ee, #000000, #ffffff) and one font family (Times), plus page text. No layout, spacing, grid, imagery, or interaction states were present in the supplied evidence; all spacing scale, radii, typographic sizes/weights, and component states above are proposed defaults, not measurements. Semantic role assignments (muted, hairline, surface-soft, surface-card, on-primary) are inferred by reusing the three observed hex values because no additional neutral or surface colors were supplied. Mobile/responsive behavior, hover/focus states, and any JavaScript-driven interactions were not observed and are marked proposed. Font availability and licensing for "Times" as rendered (likely a system/browser default rather than a webfont) were not verified. The source page itself states it is a legacy/original site kept for reference, with active commerce directed to buyanalogman.com; this document describes the archival analogman.com presentation only, not the current transactional storefront's design.
