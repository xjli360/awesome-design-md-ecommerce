---
version: alpha
name: "Earthway"
source_url: "https://earthway.com"
captured_at: "2026-09-28T09:37:06.847858+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Earthway's storefront CSS shows a utilitarian, trade-durable palette built around a single saturated brand red (#a6192e, with a near-identical #ac1a2e used in an inline sticky-header background variable — treated here as a hover/pressed variant since both values are functionally interchangeable). Neutral structure comes from near-black text tones (#121212, #1c1c1c, #232323), a light gray surface (#f6f6f6), a soft hairline gray (#dedede), and a mid gray (#9ca3af) for muted/secondary text. Several bright hues (#eb001b, #f79e1b, #ff5f00, #0071ce, #142fbd, #1532cb, #1990c6, #136f99, #5b6881) match common third-party payment-network mark colors rather than brand tokens; they are excluded from the core palette and noted in Known Gaps. Typography is set in "Host Grotesk" with system sans/mono fallbacks, using a defined heading scale (h0–h6) and body sizes (xs–lg) that scales up at wider breakpoints per the supplied root variables.
  The interpretation leans into a rugged, equipment-catalog aesthetic: bold uppercase red accents for sale/badge text (as seen in a collection-tab rule), high-contrast red CTAs on white/near-black surfaces, and a dense, grid-forward product layout implied by the product-list column variables. Spacing, radius and exact font weights are proposed and labeled inferred where not directly measured.

colors:
  primary: "#a6192e"
  primary-strong: "#ac1a2e"
  ink: "#121212"
  body: "#232323"
  muted: "#9ca3af"
  hairline: "#dedede"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  canvas: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  overlay-scrim: "#00000066"
  border-subtle: "#0000001a"
  shadow-soft: "#0000000d"
typography:
  display-xl: {fontFamily: "Host Grotesk, Arial, sans-serif", fontSize: 80px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Host Grotesk, Arial, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Host Grotesk, Arial, sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Host Grotesk, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Host Grotesk, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Host Grotesk, Helvetica, sans-serif", fontSize: 12px, fontWeight: 500, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Host Grotesk, Arial, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
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
    backgroundColor: "{colors.ink}"
    overlayColor: "{colors.overlay-scrim}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  quiz-callout:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg} {spacing.xl}"

## Components
**button-primary** is the red, filled call-to-action used for actions like "Add to Cart" or "Take the Spreader Quiz." A hover state with reduced background opacity is observed in the CSS (`--button-background-opacity: 0.85`); other states (focus, disabled) are proposed.

**button-secondary** is an outlined variant on white/light surfaces for lower-emphasis actions such as "Shop All Spreaders." Its border and text use the primary red; fill and hover treatments are inferred from common outline-button conventions, not directly observed.

**text-input** covers search and account form fields. Border color, padding and radius are proposed defaults consistent with the neutral hairline gray observed in the palette; no explicit input CSS was supplied.

**nav-bar** reflects the sticky header, which CSS confirms uses a red background (`166 25 46` = #a6192e) with white text (`255 255 255`) at least in a transparent/overlay header state. The mega-menu structure (Spreaders, Lawn & Garden, Snow & Ice, Parts & Accessories, Support) is evidenced in page text; exact dropdown styling is proposed.

**product-card** models the grid-based product listings implied by `--product-list-items-per-row` (2 on smaller layouts, 4 at wider ones). Card background, border and radius are inferred defaults since no card-specific CSS rules were supplied.

**hero** represents the homepage banner ("Transform Your Lawn This Season") using a dark overlay gradient confirmed in CSS (`linear-gradient(to top, rgb(0 0 0 / 0.5)...)`) over imagery, with white text. Exact hero copy placement is proposed.

**footer** is a dark, informational footer area for brand story and support links ("Made In Indiana," "About EarthWay"); colors are inferred from the site's dark-neutral values since no footer-specific selector was supplied.

**badge** models the uppercase red sale/label text explicitly observed in one collection-tab rule (`color: #a6192e; text-transform: uppercase; font-weight: bold;`), reused here as a small tag component for sale pricing or category flags.

**search** is a rounded search field triggered from the header search icon referenced in page text; visual treatment is proposed, following the neutral surface/hairline pattern.

**quiz-callout** is a category-specific component for the recurring "Find Your Perfect Spreader — Take the Quiz" prompt that appears repeatedly in the page content, styled as a soft-surface panel with a red accent to match the brand's guided-selection tooling.

## Responsive Behavior
This is a proposed breakpoint recommendation, not measured site behavior:
| Breakpoint | Width | Layout notes |
|---|---|---|
| Mobile | <640px | Single-column stacking, collapsed hamburger nav, product grid at 2 columns per `--product-list-items-per-row: 2` |
| Tablet | 640–1024px | 2–3 column product grid, condensed header padding |
| Desktop | 1024–1440px | Full horizontal nav (`main-nav logo secondary-nav` grid), 4-column product grid per observed variable increase |
| Wide | >1440px | Larger heading scale activates (`--text-h0: 5rem`), increased section spacing (`--section-outer-spacing-block: var(--spacing-24)`) |

Touch targets should be a minimum 44px tall for buttons and nav items; the mega-menu should collapse into an accordion on mobile. These recommendations are not derived from measured interaction testing.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction only; no live rendering, computed layout, or interaction states (hover, focus, active, disabled) were observed.
- Several palette values (#eb001b, #f79e1b, #ff5f00, #0071ce, #142fbd, #1532cb, #1990c6, #136f99, #5b6881) closely resemble third-party payment-network brand marks (e.g., card logos) rather than site-authored brand colors; they were excluded from the semantic token set.
- The near-duplicate reds (#a6192e vs #ac1a2e) are assumed to represent base/hover or base/legacy variants; their exact distinct usage was not confirmed.
- Spacing scale, radius scale, and most font sizes beyond the documented `--text-*` variables are proposed conventions, not extracted values.
- Font weights, letter-spacing, and line-height figures are inferred typographic defaults; only font-family names and base rem sizes were directly observed.
- "Host Grotesk" availability, licensing, and exact loaded weights were not verified from the supplied evidence.
- Mobile menu behavior, quiz modal design, and product-card visual details are proposed based on page-text structure, not observed DOM/CSS for those specific components.
