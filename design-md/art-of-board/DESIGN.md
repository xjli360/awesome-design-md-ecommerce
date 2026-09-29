---
version: alpha
name: "Art of Board"
source_url: "https://artofboard.com"
captured_at: "2026-09-29T03:54:16.075618+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Art of Board presents itself through a minimal, editorial Squarespace foundation: a near-black ink (#111111) on white canvas (#ffffff), with body copy carried in a softer charcoal (#3e3e3e) and secondary/meta text in mid-grey (#999999–#a9a9a9). The observed palette is dominated by neutrals and greys (#f6f6f6, #f7f7f7, #e7e7e7, #dddddd), consistent with a photography- and texture-led site where recycled skateboard imagery and material tiles are expected to supply the color, not the chrome. A single warm red-orange (#f0523d) appears in interactive/hover states (cookie-consent controls) and is treated here, by inference, as the brand accent for primary actions and focus states, since no other consistent accent recurs across the supplied evidence. Typography draws on roc-grotesk and Clarkson as the site's distinctive display faces, paired with Helvetica Neue/Arial as the system body fallback stack — fitting a design-and-licensing agency voice that is confident, condensed, and unfussy. Layout, spacing, and rounding values below are proposed conventions for a content-forward agency/catalog hybrid (statement hero, material/texture tiles, licensing contact), not measurements taken from a live DOM.

colors:
  primary: "#f0523d"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#3e3e3e"
  muted: "#999999"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  ink-soft: "#272727"
  border-light: "#e7e7e7"
  accent-deep: "#ce2c30"
  overlay-dark: "#0e0e0e"
typography:
  display-xl: {fontFamily: "roc-grotesk, sans-serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.05, letterSpacing: -0.5px}
  display-md: {fontFamily: "roc-grotesk, sans-serif", fontSize: 34px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Clarkson, roc-grotesk, sans-serif", fontSize: 22px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.55, letterSpacing: 0px}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, Sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.05em}
  button-md: {fontFamily: "'Helvetica Neue', Helvetica, Sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    borderColor: "{colors.border-light}"
    padding: "{spacing.base} {spacing.xl}"
  hero:
    backgroundColor: "{colors.overlay-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  material-swatch:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink-soft}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-light}"
    textColor: "{colors.body}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
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
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** — The warm red-orange accent (#f0523d), the only recurring interactive color in the evidence, is proposed as the fill for primary calls to action such as "Reach Out" or licensing inquiry submissions. Hover/active/disabled states are proposed, not observed.

**button-secondary** — An outlined, ink-on-transparent variant for lower-emphasis actions (e.g., "Learn More" links inside the material/licensing sections). Border uses the neutral hairline grey; no hover treatment was captured in the CSS evidence.

**text-input** — A plain-bordered field styled from the neutral hairline and canvas colors, suited to a contact/licensing inquiry form. Focus-ring color is proposed to reuse the primary accent, consistent with the single colored interactive state observed in the cookie-tooltip CSS.

**nav-bar** — A white, top-anchored bar carrying the "ART OF BOARD / TILE MATERIALS / AOB CONTRACT / RIDE / RECYCLE / AOB LICENSING" wayfinding seen in the page text, set in the small-caps caption style. Sticky/collapse behavior is proposed, not confirmed from static CSS.

**hero** — A full-bleed, dark statement section pairing the mission quote ("To inspire self-expression…") with the large display type. Background is proposed as the darkest observed neutral (#0e0e0e) to let photographic skateboard/texture imagery carry color; this is an inferred pattern given the agency's image-led positioning.

**material-swatch** — A category-appropriate tile component representing the "TILE MATERIALS" offering: a soft-grey card surface holding a texture thumbnail and short label, echoing the site's stated focus on recycled skateboard imagery and pattern licensing.

**product-card / license-card** — Reused for licensing/portfolio entries (e.g., Sashiko-inspired, football-centric, lemon-slice designs mentioned in copy), with a light card surface and mid-weight title type. Interaction states (hover elevation, click-through) are proposed conventions.

**footer** — A dark, ink-colored closing band carrying contact details (Managing Director, phone, email) and secondary navigation, mirroring the dark hero for visual bookending. Column layout is proposed.

**badge** — A small pill using the primary accent for short labels (e.g., "New," "Licensed"), sized from the caption typography scale.

**search** — A pill-shaped, soft-grey field for filtering the material/texture library; not confirmed present on the live site but proposed as fitting for an image-licensing catalog.

## Responsive Behavior
This is a recommended breakpoint structure, not measured site behavior:

| Breakpoint | Range | Layout guidance |
|---|---|---|
| mobile | <640px | Single column; nav collapses to hamburger ("Open Menu/Close Menu" text confirms a toggle pattern exists); hero type steps down to `display-md`. |
| tablet | 640–1024px | Two-column material/license grids; nav remains collapsed or condenses to icon+label. |
| desktop | 1024–1440px | Multi-column grids (3–4 up) for material swatches and license cards; full horizontal nav. |
| wide | >1440px | Max content width constrained (~1280–1440px) with increased section padding (`{spacing.section}`). |

Touch targets should meet a 44px minimum height for buttons and nav items. The confirmed "Open Menu / Close Menu" text pair indicates an off-canvas or full-screen mobile menu pattern; its visual treatment (overlay color, animation) was not present in the supplied CSS and is therefore not specified here.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- This interpretation is built entirely from static CSS/text extraction; no live DOM, computed styles, or rendered layout were observed.
- The accent color (#f0523d) is inferred from a single cookie-consent hover rule; its use as the site-wide primary brand color is a reasonable but unverified extrapolation.
- roc-grotesk and Clarkson are named in the font evidence but their exact weights, availability, and licensing (self-hosted vs. Typekit/Adobe Fonts) were not verified.
- Component states (hover, focus, disabled, active) beyond the cookie-tooltip rules are proposed conventions, not observed interactions.
- Mobile menu visuals, breakpoint pixel values, and grid column counts are proposed defaults, not measured from the site.
- Spacing and rounding scales follow a generic proposed system, as no layout metrics (margins, radii) were present in the supplied CSS evidence.
