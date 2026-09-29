---
version: alpha
name: "Doc Sweeney Drums"
source_url: "https://www.docsweeneydrums.com"
captured_at: "2026-09-29T03:53:12.900443+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Doc Sweeney Drums is a Carlsbad, CA custom-shell drum builder running on a Squarespace
  template; the supplied CSS is largely platform boilerplate (cookie banner, tooltip,
  confirmation-button rules) rather than bespoke brand styling, so this interpretation is
  conservative. The only clearly product-specific colors are near-black/off-black neutrals
  (#111111, #1d1d1d, #222222, #272727, #0e0e0e, #131313, #2a2a2a) paired with white and
  light-gray surfaces (#ffffff, #f6f6f6, #ebebeb, #eeeeee, #dddddd), fitting a workshop/
  luthier aesthetic built around dark wood tones and clean product photography. A single
  observed interactive accent, #f0523d, appears on hover states in the cookie/tooltip UI and
  is inferred here as the site's primary accent for calls-to-action, since no other
  non-social-icon accent exists in evidence. Many palette entries (#3b5998, #1877f2-style
  blues, #e4405f, #55acee, #cc2127, #1ab7ea) are third-party social-icon brand colors and are
  excluded from role assignment. Typography draws on the observed `din-condensed-web`
  (condensed, suited to bold headlines) and `proxima-nova` (body/UI), both real Typekit-style
  font-family declarations in the CSS, with Helvetica Neue/Arial/sans-serif as documented
  fallbacks. Button typography (11px, uppercase, 500 weight, 0.5px tracking) is directly
  observed from tooltip/confirmation-button rules.

colors:
  primary: "#f0523d"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#ebebeb"
  on-primary: "#ffffff"
  surface-dark: "#000000"
  text-secondary: "#3e3e3e"
  border-dark: "#2a2a2a"
  surface-alt: "#eeeeee"
typography:
  display-xl: {fontFamily: "din-condensed-web, Helvetica Neue, Arial, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "din-condensed-web, Helvetica Neue, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "proxima-nova, Helvetica Neue, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "proxima-nova, Helvetica Neue, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "Helvetica Neue, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.02em}
  caption: {fontFamily: "Helvetica Neue, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5em, letterSpacing: 0.05em}
  button-md: {fontFamily: "proxima-nova, Helvetica Neue, Arial, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 22px, letterSpacing: 0.5px, textTransform: uppercase}
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
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
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
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
    hairline: "{colors.border-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    hairline: "{colors.border-dark}"
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
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  shell-config-swatch:
    backgroundColor: "{colors.surface-alt}"
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs}"
    typography: "{typography.caption}"

## Components

**button-primary** — Uses the one directly observed non-social accent (#f0523d hover background paired with #ffffff text) from tooltip/reject-button CSS, repurposed as the primary call-to-action (e.g., "Request a Quote," "Contact"). Uppercase button typography and 0.5px tracking are taken verbatim from the CSS.

**button-secondary** — A proposed outline treatment for lower-priority actions (e.g., "View Gallery"), using the hairline gray border and dark ink text; no hover/active state was present in evidence, so states are proposed.

**text-input** — Proposed form field styling for the contact form, using canvas background, hairline border, and body typography; no input-specific CSS was supplied.

**nav-bar** — Proposed dark header bar (Home / Drums / Contact / Artists / Media) using the near-black surface tones observed in the palette, since Squarespace dark navigation is consistent with the site's neutral-heavy color set; exact nav styling was not present in evidence.

**product-card** — Proposed card pattern for the Focus Series, HolloCore, Impact, and Classic snare listings, using the light gray surface-card against hairline borders to separate product photography from the white canvas.

**hero** — Proposed dark full-bleed hero for the homepage "Welcome to Doc Sweeney Drums / ONE OF A KIND" statement, using the dark surface and display-xl condensed headline typography to suit a craftsman/workshop tone.

**footer** — Proposed dark footer matching the nav-bar treatment, carrying contact details (address, phone, email) in muted gray text against the dark surface.

**badge** — Proposed small pill label (e.g., "New," "Custom Build") using the primary accent color; not observed in supplied CSS, purely a category-appropriate proposal.

**search** — Proposed lightweight search field using surface-soft background, included for completeness though no search UI was evidenced on this brochure-style site.

**shell-config-swatch** — A category-appropriate proposed component for displaying wood-species or finish options referenced in the site copy ("solid wood, single ply or stave shell... extensive list of species"), styled as small selectable swatches with a primary-colored selected-state border.

## Responsive Behavior
Proposed breakpoints (not measured from live rendering):

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | single-column stack, nav collapses to menu icon |
| tablet | 600–1024px | 2-column product grids |
| desktop | 1024px+ | multi-column grids, expanded nav |

Touch targets should be at least 44×44px; the primary nav is expected to collapse into a hamburger/off-canvas menu below tablet width. This table is a recommendation based on common Squarespace responsive conventions, not observed site behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Supplied CSS is dominated by Squarespace platform boilerplate (cookie banner, tooltip, confirmation-button rules); minimal brand-specific selectors were available, so most component styling above is proposed rather than observed.
- Several palette entries (#3b5998, #55acee, #e4405f, #1ab7ea, #cc2127, and similar) are recognizable third-party social-icon colors, not brand colors, and were deliberately excluded from role assignment.
- The #f0523d accent is real CSS evidence but only appears in a cookie-banner/tooltip hover state; its use as a site-wide primary/CTA color is inferred, not confirmed on live product pages.
- Font usage mapping (din-condensed-web for display, proxima-nova for body) is inferred from font-family names present in the stylesheet reference list; no selector-level evidence ties specific families to headings versus body copy, and "Clarkson" appears in the family list with no confirmed usage context.
- Layout, spacing scale, rounded-corner values, and responsive breakpoints are proposed defaults, not measured from rendered pages.
- No interaction states (hover/focus/active) beyond the cookie-banner/tooltip rules were observed; mobile navigation behavior was not observed.
- Custom font licensing/availability (Typekit-hosted proxima-nova, din-condensed-web) was not verified.
