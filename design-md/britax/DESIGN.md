---
version: alpha
name: "Britax"
source_url: "https://www.britax-roemer.com/"
captured_at: "2026-09-29T03:59:14.823111+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from the Britax Römer parent storefront (britax-roemer.com), which
  presents the Britax Römer car seat and pushchair (stroller) range as its current live catalog under
  the Britax corporate identity. The supplied CSS evidence is dominated by a third-party OneTrust cookie
  consent widget rather than first-party page components, so component styling below is proposed and
  evidence-qualified rather than measured from the storefront's own stylesheet. The observed color
  palette is broad and mixed-provenance (brand, editorial, and consent-widget hues); a small, restrained
  subset has been selected here as plausible brand roles: a strong red as primary accent, near-black ink
  for text, white canvas, and light grey neutrals for hairlines and soft surfaces. A sustainability-leaning
  green is retained as a secondary accent given the site's visible "Sustainability" and award messaging.
  Typography is limited to the observed system/web-safe stack (Lato, Roboto, Helvetica, Arial, sans-serif)
  for body and UI text; "Crete Round" appears in the font list and is treated as an inferred display
  candidate for headings, not a confirmed brand typeface. Layout, spacing, radii, and interaction states
  are proposed conventions suited to a safety-focused juvenile-products retailer, not observations of the
  live DOM or responsive behavior.

colors:
  primary: "#d50c2d"
  ink: "#1b1b1b"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#6a7171"
  hairline: "#d4d7da"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#84bd00"
  info: "#3860be"
  warning: "#f37321"
  border-strong: "#b6bcc1"
typography:
  display-xl: {fontFamily: "'Crete Round', serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Crete Round', serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Lato, Roboto, Helvetica, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Lato, Roboto, Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Lato, Roboto, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Lato, Roboto, Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.1px}
  button-md: {fontFamily: "Lato, Roboto, Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  fit-finder-widget:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
- **button-primary**: A solid red call-to-action (e.g. "DISCOVER", "EXPLORE") intended for primary product and category actions. Hover/active/disabled states are proposed, not observed.
- **button-secondary**: An outlined variant using the same red on a white ground, for secondary actions like "Where to Buy" or "Support" links styled as buttons. State transitions are proposed.
- **text-input**: A bordered field for search or contact forms, using a light hairline border and standard body typography; focus-ring styling is proposed.
- **nav-bar**: A white top navigation bar hosting "Car Seats / Pushchairs / Accessories" plus utility links ("Safety notices", "Where to Buy", "Support") and a language selector; sticky/scroll behavior is proposed, not confirmed.
- **product-card**: A white card with a soft hairline border for listing items such as "BABY-SAFE PRO" or "SAFEFIX," pairing a title style with a lighter price/body style; "NEW" labeling would use the badge component. Grid arrangement is proposed.
- **hero**: A large full-width introductory band (e.g. the "COMFORT THAT GROWS. PROTECTION THAT LASTS." messaging) using display typography on a soft neutral background; imagery treatment is not verifiable from the supplied CSS.
- **footer**: A dark, high-contrast footer housing sitemap links (Support, About Us, Sustainability, Careers), legal links, and social icons, mirroring the site's visible footer text content.
- **badge**: A small rounded pill for status flags like "NEW," using the sustainability-leaning green; alternate semantic colors (e.g. warning/info) are proposed for other flag types.
- **search**: A compact input affordance for the utility bar, using neutral bordering consistent with the text-input pattern; icon placement is proposed.
- **fit-finder-widget**: A category-specific promotional module reflecting the site's visible "FIT FINDER®" tool, styled as a soft-background panel with a primary-red accent to guide users toward compatible car seats/pushchairs; actual interactive behavior was not observed.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width      | Layout guidance                                  |
|-----------|------------|---------------------------------------------------|
| mobile    | <600px     | Single-column stacking; nav collapses to a menu drawer |
| tablet    | 600–1024px | Two-column product grids; nav remains condensed   |
| desktop   | >1024px    | Multi-column grids; full horizontal nav exposed   |

Touch targets should be at least 44px in height for primary/secondary buttons and nav items. The navigation bar is expected to collapse into a hamburger/menu pattern below tablet width; this is a proposed convention for juvenile-safety retail sites and has not been observed in the supplied markup.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- The supplied CSS evidence is almost entirely from a third-party OneTrust cookie-consent widget; no first-party component-level stylesheet rules (nav, product grid, hero, footer) were available, so all component styling above is proposed rather than extracted.
- Color role assignments (primary, ink, muted, etc.) are inferred selections from a large, mixed-provenance palette; no selector-to-role mapping was confirmed for brand-specific elements.
- "Crete Round" is present in the observed font-family list but its actual usage context (headings vs. elsewhere) is unverified; treat as an inferred display font, not a confirmed brand typeface.
- No custom/proprietary web font files, licensing, or @font-face declarations were observed; only system font-stack names are confirmed.
- All spacing, radius, and breakpoint values are proposed conventions, not measured from live layout or DOM inspection.
- No interaction states (hover, focus, active, disabled), animations, or mobile menu behavior were observed; all are proposed.
- This document describes the current Britax Römer parent-site presentation of car seats and pushchairs; it does not reconstruct any former independent site and should not be read as such.
