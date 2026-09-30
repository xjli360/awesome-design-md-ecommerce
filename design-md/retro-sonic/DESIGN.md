---
version: alpha
name: "Retro-Sonic"
source_url: "https://www.retro-sonic.com"
captured_at: "2026-09-29T04:10:33.090324+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Retro-Sonic sells hand-built recreations of classic guitar effect pedals, and its site CSS reflects a Wix-built storefront with a neutral gray/black/white base accented by red. The only font-family directly bound to a live selector (`body`) is Arial/Helvetica/sans-serif at a 10px root size, which is typical of Wix's rem-scaling pattern rather than a true reading size. The wider font list (Raleway, Open Sans, Libre Baskerville, Futura, Din Next, Lulo Clean, Courier variants, and several Wix hashed webfont names) are bundle-level resources whose exact element assignments were not resolvable from static evidence; Raleway is proposed here as a plausible display face because it is a common Wix heading choice and appears cleanly in the family list, but this mapping is inferred, not confirmed.
  The palette is dominated by near-black grays (#151414, #2f2e2e, #212121) against white, with a cluster of saturated reds (#ce2026, #e60211, #df3131, #ff4040) that plausibly serve as the brand accent given the pedal-electronics context, and a soft warm-gray scale (#e0dfdf, #f1f0ef) for card and section backgrounds. A blue (#116dff) and multi-stop blue/orange/green ramps also appear in the evidence; these read as Wix editor UI/state colors (links, focus rings, palette swatches) rather than brand marks, and are included only as optional accents. All roles below are semantic inferences layered onto measured hex values — no live layout, spacing, or hover behavior was observed.

colors:
  primary: "#ce2026"
  ink: "#151414"
  canvas: "#ffffff"
  body: "#2f2e2e"
  muted: "#757575"
  hairline: "#e0dfdf"
  surface-soft: "#f1f0ef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-red-bright: "#e60211"
  accent-red-soft: "#f9d6d7"
  link-blue: "#116dff"
  border-strong: "#a8a6a5"
typography:
  display-xl: {fontFamily: "Raleway, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Raleway, Arial, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.5px}
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-red-soft}"
    textColor: "{colors.primary}"
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
  pedal-spec-panel:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components
- **button-primary**: A solid red call-to-action (e.g. "Shop" or "Subscribe") using `{colors.primary}` fill and white text, matching the saturated red cluster found in the palette. Hover/active states were not observed and would need to be confirmed against live markup.
- **button-secondary**: An outlined variant for lower-priority actions (e.g. "Learn More," "Dealers"), sharing the primary red as both text and border color on a transparent background, proposed for visual consistency without adding new hues.
- **text-input**: A simple bordered field for the mailing-list subscribe form referenced in the page text ("SUBSCRIBE TO OUR MAILING LIST"), using the hairline gray border and card-white background; focus-ring styling is proposed, not observed.
- **nav-bar**: A white top bar holding the HOME / PRESS / PEDALS (with sub-categories Chorus, Flanger, Phaser, Delay, Overdrive, Compressor, Distortion) / LEGACY PEDALS / SHOP / DEALERS / CONTACT / ABOUT US / FAQ menu implied by the page-text excerpt, plus a currency selector (USD $). Dropdown/mega-menu behavior for the pedal category list is inferred from the flat text list, not confirmed structurally.
- **product-card**: A white card with soft hairline border for each pedal model, using rounded-md corners and generous padding to present product imagery, name, and short spec copy in title/body typography pairs.
- **hero**: A dark, full-bleed introductory band ("Get the Vintage Vibes!", "Quality Classic Effects Recreations") using the darkest ink tone as background and white display type, echoing the brand's vintage/analog tone; exact background image or gradient was not present in the supplied evidence.
- **footer**: A dark closing band carrying the Canada Post shipping note and copyright line ("© 2017-2020 by Retro-Sonic Inc."), styled with the same ink background as the hero for visual bookending.
- **badge**: A small pill using the soft red tint background with red text, proposed for labels like "AS FEATURED IN" or press mentions (Premier Guitar quote is called out prominently in the copy).
- **search**: A lightweight search field using the neutral soft-surface background, proposed for locating pedal models by name; no search UI was directly observed in the evidence.
- **pedal-spec-panel**: A category-specific component for presenting per-pedal technical detail (voltage/headroom notes like the "18V mode" mentioned in the Premier Guitar quote), styled as a bordered panel distinct from the general product-card to separate marketing copy from spec data.

## Responsive Behavior
This is a proposed recommendation, not measured site behavior:
| Breakpoint | Width | Layout notes |
|---|---|---|
| Mobile | <480px | Single-column stack; nav collapses to a hamburger/menu icon; product cards full-width. |
| Tablet | 480–1024px | 2-column product grid; nav-bar items may wrap or condense into a horizontal scroll. |
| Desktop | >1024px | 3–4 column product grid; full horizontal nav with category sub-items visible or on hover. |

Touch targets should be at least 44×44px for nav links and buttons; the mobile menu should collapse the full category list (Chorus, Flanger, Phaser, Delay, Overdrive, Compressor, Distortion) under a single "Pedals" toggle. None of this was captured in the supplied static CSS/text evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static extraction returned selectors mostly for a generic Wix `StylableButton` component and root-level CSS variables; no selectors for actual nav, hero, product-card, or footer markup were present, so those components are structurally proposed, not observed.
- The 10px root `font-size` on `body` is a Wix rem-scaling anchor, not a literal reading size; all typography sizes above are proposed conventional values, not measured.
- Font-role mapping is uncertain: only `Arial, Helvetica, sans-serif` is bound to a live selector; Raleway and other listed families are inferred as possible heading fonts but unconfirmed, and custom/webfont licensing was not verified.
- Color roles (primary red, ink, muted, hairline, etc.) are inferred from the observed hex palette by frequency and plausibility; no computed styles confirming actual usage on buttons, links, or backgrounds were available.
- No hover, focus, active, or disabled states, no breakpoint values, and no mobile menu behavior were observed; all interaction and responsive guidance above is a proposed convention only.
- Blue and multi-stop ramp colors (e.g. `#116dff`, `#7fccf7`, orange/green ramps) may be Wix editor/theme utility colors unrelated to the public brand and were excluded from primary role assignment for that reason.
