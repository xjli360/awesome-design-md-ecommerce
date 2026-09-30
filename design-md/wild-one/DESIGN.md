---
version: alpha
name: "Wild One"
source_url: "https://wildone.com"
captured_at: "2026-09-28T04:18:13.464549+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Wild One's storefront CSS exposes a neutral operating palette — pure black
  (#000000) and white (#ffffff) drive foreground, background, link, and badge
  variables — layered with a single directly observed accent, magenta-purple
  #9d0696, used as the checkout button's hover state. This interpretation
  treats black as the default interactive/ink color and #9d0696 as the
  brand's primary accent for hover and emphasis states, since that is the
  only accent color tied to a concrete interaction in the evidence. A
  secondary lavender (#e7e5ff) appears as a `--color-button` variable and is
  kept as a soft accent/surface option. Additional palette entries (lime,
  coral, pink, yellow, blue) are broad and likely represent product/category
  tagging or seasonal campaign colors rather than core UI; they are included
  as optional accents only, with role inferred.
  Typography pairs "Modern Era" — confirmed in multiple rules for titles,
  buttons, and cart UI, set bold and uppercase for CTAs — with "Fraunces
  Variable," which appears in the site's font stack but has no directly
  observed selector; its use here as a serif display headline face is
  therefore inferred, following common DTC pairing of a geometric sans body
  face with a warm serif display face. All fallbacks (Arial, Helvetica,
  Georgia, sans-serif, serif) are drawn from the supplied evidence.

colors:
  primary: "#9d0696"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#676986"
  hairline: "#e5e5e5"
  surface-soft: "#f3f3f3"
  surface-card: "#f7f7f8"
  on-primary: "#ffffff"
  accent-lavender: "#e7e5ff"
  accent-lime: "#dff464"
  accent-coral: "#ff774d"
  accent-pink: "#d92b90"
  accent-yellow: "#ffc72c"
  accent-blue: "#6994cd"
typography:
  display-xl: {fontFamily: "Fraunces Variable, Georgia, serif", fontSize: 56px, fontWeight: 600, lineHeight: 1.08, letterSpacing: -0.5px}
  display-md: {fontFamily: "Fraunces Variable, Georgia, serif", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Modern Era, Arial, Helvetica, sans-serif", fontSize: 20px, fontWeight: 700, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Modern Era, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Modern Era, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.45, letterSpacing: 0px}
  caption: {fontFamily: "Modern Era, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Modern Era, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.05em, textTransform: "uppercase"}
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    hoverBackgroundColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** follows the checkout button rule directly: black background, white text, bold uppercase "Modern Era" label, and a hover state that swaps to `{colors.primary}` (#9d0696) — this hover behavior is observed CSS, not inferred. `rounded.full` approximates the pill-style 30px radius seen on a related Rebuy button widget.

**button-secondary** mirrors the `--color-secondary-button` / `--color-secondary-button-text` variable pair (white background, black text/border) observed in the root theme variables. Hover/active states are proposed, not observed.

**text-input** is a compact, low-chrome field derived from the observed `.rebuy-select` padding and 14px font-size, styled with a hairline border rather than the raw "background: none" custom-arrow treatment seen in evidence.

**nav-bar** is a proposed top-level navigation using the observed `--color-link: 0,0,0` (black links on white) since no header markup or breakpoint behavior was present in the supplied CSS.

**product-card** uses `title-md` for product names (matching the bold "Modern Era" rule applied to `.rebuy-product-title`) and `body-sm` for price/meta text. Card chrome (surface color, radius, padding) is inferred from general e-commerce card conventions, not measured.

**hero** is an entirely proposed marketing band: a large serif `display-xl` headline paired with a plain-sans `body-md` subhead, since no hero markup appeared in evidence.

**footer** proposes a muted, low-contrast band using `{colors.surface-soft}` and `{colors.muted}` for secondary link/legal text; layout and content are unobserved.

**badge** reflects the `--color-badge-foreground/background/border` variables directly (black-on-white with black border), styled as a small square-cornered tag suitable for "Bestseller" or material labels.

**search** is a proposed pill-shaped input reusing the input treatment above with a fuller radius, appropriate for a product-catalog site; no search markup was present in evidence.

**size-selector** is a category-appropriate proposed component for harness/collar sizing (e.g., S/M/L), styled as a segmented pill group with `{colors.primary}` marking the active choice — consistent with the one confirmed accent-hover interaction in the evidence, extended here to a plausible size-picker pattern.

## Responsive Behavior

No breakpoints, media queries, or mobile layout were present in the supplied evidence. The following is a **recommendation only**, not a measured site behavior:

| Breakpoint | Range         | Notes                                            |
|-----------|---------------|---------------------------------------------------|
| mobile    | 0–599px       | Single-column stacking; nav collapses to a menu icon (proposed). |
| tablet    | 600–959px     | 2-column product grid; header condenses (proposed). |
| desktop   | 960–1279px    | 3–4 column product grid; full nav visible (proposed). |
| wide      | 1280px+       | Max content width with generous side margins (proposed). |

Touch targets should be a minimum of 44×44px for buttons and the proposed `size-selector` pills. Navigation is expected to collapse into a hamburger/drawer pattern below the tablet breakpoint; this has not been observed and should be validated against live markup before implementation.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence was extracted from static CSS/DOM fragments (mostly cart-flyout, Rebuy widget, and Okendo review-widget selectors), not full page templates — header, hero, footer, and product-grid markup were not present, so several components above are proposed conventions rather than observed structure.
- The role of `#9d0696` as "primary" and `#676986` as "muted" is a semantic inference based on limited hover-state and stray-color evidence; no direct `--color-primary` or `--color-muted` variable was supplied.
- "Fraunces Variable" appears only in the font-family list, with no selector confirming where or whether it is actually applied; its assignment to display/headline typography is inferred, not observed.
- All font sizes, line-heights, letter-spacing, radii, and spacing values not directly quoted in the CSS (e.g., `display-xl`, `display-md`, most padding/rounded tokens) are proposed defaults for a clean, editorial pet-goods brand, not measurements.
- No responsive/mobile behavior, interaction states (focus, disabled, error), or real breakpoints were present in the evidence; all such guidance above is a recommendation.
- Custom font availability, licensing, and self-hosting terms for "Modern Era" and "Fraunces Variable" were not verified and must be confirmed with Wild One/Shopify theme licensing before production use.
