---
version: alpha
name: "Aperion Audio"
source_url: "https://aperionaudio.com"
captured_at: "2026-09-28T09:08:29.640966+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Aperion Audio's storefront runs on a Shopify theme whose CSS exposes a neutral
  operating palette (white #ffffff canvas, near-black #171717 foreground, and
  mid-grey #333333 body text) rather than a saturated brand color system. A
  muted brick-red (#9c1f2e / #9c1f21) recurs across the extracted rules and is
  treated here as the inferred accent/primary, since no other repeated
  chromatic value stands out as a call-to-action color. A gold tone (#edca00)
  is explicitly tied to the star-rating widget and is retained only for that
  badge/rating role. Light greys (#f2f2f2, #dedede, #e5e5e5) are read as
  surface and hairline tones for cards, dividers, and soft backgrounds.
  The only font-family evidence captured from the CSS is a system monospace
  stack (ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation
  Mono, Courier New, monospace), most likely originating from a code/textarea
  or debug element rather than the brand's display typeface. Per the
  observed-only-fonts constraint, this monospace stack is applied across all
  typography tokens below and flagged as a placeholder; it should not be
  read as Aperion's actual marketing typeface. Layout numerics (page padding,
  topbar height, product grid ratios, clamp-based title scaling) are present
  in the CSS but reference undefined spacing variables, so concrete pixel
  values in this spec are proposed, not measured.

colors:
  primary: "#9c1f2e"
  primary-alt: "#9c1f21"
  ink: "#171717"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#dedede"
  hairline: "#e5e5e5"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-gold: "#edca00"
  dark-surface: "#1c1c1c"
  charcoal: "#232323"
  black: "#000000"
typography:
  display-xl: {fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace", fontSize: 56px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace", fontSize: 36px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, 'Liberation Mono', 'Courier New', monospace", fontSize: 14px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.3px}
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    borderColor: "{colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    borderColor: "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.xl}"
    borderColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    borderColor: "{colors.hairline}"
  hero:
    backgroundColor: "{colors.dark-surface}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.charcoal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  spec-comparison-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    borderColor: "{colors.hairline}"

## Components

**button-primary** carries the inferred brick-red accent (#9c1f2e) as a call-to-action surface, e.g. "Add to Cart" or "Shop Now." White text is proposed for contrast; hover/active states are not observed and would need confirmation.

**button-secondary** uses a white/transparent surface with a hairline border, suited to lower-emphasis actions like "View Details" alongside a primary button. Its border and text colors reuse existing tokens rather than introducing new ones.

**text-input** is proposed for the search field and order-note/discount-code inputs referenced in the page text (e.g. cart discount entry). Padding and rounding follow the compact `sm` radius consistent with a utilitarian commerce UI.

**nav-bar** models the persistent header with logo, primary navigation (Speakers, Hi-Fi, Custom Install, Subwoofers, Amplifiers, Accessories), search, account, and cart icon. The white background and near-black foreground match the `--color-background`/`--color-foreground` pair explicitly set on the header section in the CSS.

**product-card** represents the repeated product grid items (e.g. "A5 Atmos," "Verus V8T") seen in the text excerpt, each with title, price, star rating, and variant swatches. A soft card background and hairline border are proposed since Shopify grid cards typically separate from a flat page background.

**hero** models the homepage banner sections (Grandis, Super Tweeters, Energy Power Amplifiers, Theatrus) which pair large display type with a dark or image-backed surface; `dark-surface` (#1c1c1c) is used as a proposed backdrop for overlaid white text, though actual hero background imagery is not captured in this evidence.

**footer** groups the About, Reviews, Dealers/Affiliates, and social links visible in the navigation text, set on a dark charcoal surface for visual separation from the white body, consistent with common Shopify footer patterns.

**badge** covers the star-rating indicator (explicitly styled via `--lxs-rating-icon-color: #edca00`) and stock/shipping callouts like "In stock, ready to ship" or "30-Day In Home Audition." The gold fill is the one color in the palette with a confirmed semantic tie in the CSS.

**search** is proposed as a pill-shaped input for the site's "Search Site navigation" feature, using the soft grey surface tone to sit unobtrusively in the header.

**spec-comparison-table** is a category-appropriate addition for home-theater/audio equipment, supporting technical specification tables (frequency response, power handling, dimensions) commonly needed for products like the DS15 Subwoofer or Energy E7 Amplifier; styling reuses existing card and hairline tokens rather than introducing new evidence-less colors.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| Mobile | < 480px | Single-column product grid, collapsed hamburger nav, sticky cart icon |
| Tablet | 480–1024px | 2-column product grid, condensed nav labels |
| Desktop | 1024–1280px | Full nav bar, 3–4 column product grid |
| Wide | > 1280px | Content capped near the CSS's `--page-width`/`max(...,1280px)` container logic |

Touch targets should be at least 44×44px for cart, search, and account icons. Primary navigation should collapse into a drawer or accordion below ~1024px given the number of top-level categories (Home, Speakers, Hi-Fi, Custom Install, Subwoofers, Amplifiers, Accessories, About). This table is a design recommendation only; no live responsive behavior was observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static extraction only: no rendered layout, hover/focus states, animations, or JavaScript-driven interactions (e.g. cart drawer, variant swatches) were observed.
- The only font-family evidence is a monospace system stack, almost certainly sourced from a code/textarea utility class rather than Aperion's actual display or body typeface; all typography tokens use this stack as a constrained placeholder, and real brand fonts should be re-verified against rendered pages.
- Color-to-role mapping is partly inferred: `primary` (#9c1f2e) is assumed from repetition in the CSS, not from an explicit `--color-primary`-style variable; only the gold rating color and header background/foreground pair have direct semantic evidence.
- Numeric spacing/type scale (`--sp-*`, `--text-h*`, `--title-lg/xl` clamp values) reference undefined custom properties in the supplied evidence, so all pixel values in `typography` and `spacing` are proposed approximations, not measured computed styles.
- Mobile/tablet layout, breakpoint pixel values, and grid column counts are proposed conventions, not extracted from responsive CSS or viewport testing.
- Custom font licensing/availability was not verified since no proprietary font file or `@font-face` declaration was present in the supplied evidence.
