---
version: alpha
name: "Tommee Tippee"
source_url: "https://tommeetippee.com"
captured_at: "2026-09-28T09:07:45.702412+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Tommee Tippee's UK storefront runs on a Shopify theme exposing explicit CSS
  custom properties for color and type, giving high confidence in the core
  palette. The system pairs a warm off-white canvas (#FFFFFF) and a muted
  greige surface (#E5E3DF) with a near-black ink (#282828) used for both text
  and, inverted, as the primary button fill. A small set of named pastel
  accents — green, blue, peach, purple, yellow — appear as CSS variables and
  likely support category tagging, illustration backdrops, or swatch UI,
  though their exact application is inferred rather than observed in layout.
  Typography splits cleanly: "Victor Serif" (weight 500) for headings signals
  a softer, editorial parenting-brand voice, while "Aktiv Grotesk" (weight
  300, generous letter-spacing) carries body copy and UI text. Buttons are
  fully pill-shaped (3rem radius) with three confirmed variants — solid,
  secondary (greige), and outline — each with defined hover states. Numerous
  neutrals (#f0f0f0–#3c3c3c range) and card-network brand colors were present
  in the raw palette but are excluded here as non-brand payment iconography.
  This spec proposes a restrained, editorial-meets-functional system fit for
  a feeding/product-heavy catalog.

colors:
  primary: "#282828"
  ink: "#282828"
  canvas: "#ffffff"
  body: "#282828"
  muted: "#606060"
  hairline: "#dedede"
  surface-soft: "#e5e3df"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  accent-green: "#d1d1b7"
  accent-blue: "#a0b3ad"
  accent-peach: "#e09f87"
  accent-purple: "#9b8692"
  accent-yellow: "#edd98a"
  sale: "#dc3544"
  highlight: "#00bbff"
typography:
  display-xl: {fontFamily: "'Victor Serif', serif", fontSize: 48px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  display-md: {fontFamily: "'Victor Serif', serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.25, letterSpacing: 0px}
  title-md: {fontFamily: "'Victor Serif', serif", fontSize: 24px, fontWeight: 500, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Aktiv Grotesk', sans-serif", fontSize: 16px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0.056rem}
  body-sm: {fontFamily: "'Aktiv Grotesk', sans-serif", fontSize: 14px, fontWeight: 300, lineHeight: 1.5, letterSpacing: 0.056rem}
  caption: {fontFamily: "'Aktiv Grotesk', sans-serif", fontSize: 12px, fontWeight: 300, lineHeight: 1.4, letterSpacing: 0.056rem}
  button-md: {fontFamily: "'Aktiv Grotesk', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.056rem}
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
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.surface-soft}"
  button-outline:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    height: "56px"
    padding: "{spacing.none} {spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.display-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  promo-banner:
    backgroundColor: "{colors.accent-peach}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.title-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.lg} {spacing.xl}"
    rounded: "{rounded.md}"

## Components

**button-primary** is the confirmed solid CTA: black fill, white text, fully pill-shaped via the observed `border-radius: 3rem`, used for primary actions like "Shop Now."

**button-secondary** maps directly to `.button--secondary`, using the greige surface as both fill and border with dark text — a lower-emphasis CTA for secondary actions such as "Continue shopping."

**button-outline** reflects `.button--outline`: transparent background with a dark border and text, inverting to a solid black fill with greige text on hover per the observed `:hover` rule.

**text-input** is proposed for search and newsletter fields; the newsletter form's absolute-positioned icon button (`.newsletter-form__button`) confirms an inline-icon input pattern, though full input styling (border, fill) is inferred from neutral palette values.

**nav-bar** reflects the observed `.header` rule: dark (#282828) background with greige (#e5e3df) text and links, transitioning on scroll state per `.transparent-header.scrolled`. Height and padding are proposed to match the drawer header's 5.6rem/1.6rem values.

**product-card** is proposed for the catalog grid (Baby Bottles, Perfect Prep, Dummies, etc.); no direct card CSS was supplied, so surface, border, and spacing are inferred from the general neutral/hairline palette.

**hero** is proposed for the homepage banner ("First feeds made simple") using the greige surface-soft background and serif display type; exact hero layout and imagery were not present in the CSS evidence.

**footer** is proposed as a dark-mode band mirroring the nav-bar treatment, appropriate for a newsletter-signup section referenced in the page text ("join our parenting community").

**badge** is proposed for sale/discount flags ("up to 35% off"), using the one clearly non-neutral, non-payment brand color (#dc3544) found in the palette, labeled here as a sale/alert role.

**search** is proposed as a pill-shaped overlay input consistent with the rounded button language and surface-card neutral, though no dedicated search-bar CSS was supplied.

**promo-banner** is a category-appropriate component for feeding-kit callouts (e.g., "One kit. Two teats. Zero guesswork"), using the peach accent as an inferred illustrative/promotional background distinct from the neutral hero.

## Responsive Behavior
This is a recommendation, not measured site behavior — no breakpoint or viewport CSS was present in the supplied evidence.

| Breakpoint | Width      | Notes (proposed) |
|------------|-----------|-------------------|
| mobile     | <480px    | Single-column nav collapses to drawer (evidenced by `.drawer--navigation`); stacked product grid. |
| tablet     | 480–960px | 2-column product grid; nav-bar remains persistent. |
| desktop    | >960px    | Full mega-menu navigation (categories: Feeding, Dummies, Sleeping, etc.); 3–4 column product grid. |

Touch targets should be a minimum 44px in the proposed system; the observed `.drawer__header` height (5.6rem ≈ 56px) supports this for mobile nav. Collapse the mega-menu into the drawer pattern already evidenced in CSS below the tablet breakpoint.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Static CSS extraction provides only variable declarations and isolated component rules; full layout, grid structure, and imagery treatment were not observed.
- The `--color-greige` variable value was truncated in the source evidence; it is inferred here as equal to `--color-background-secondary` (#E5E3DF) based on contextual usage in `.header` and `.drawer__header`.
- Numerous palette entries (e.g., #eb001b, #f79e1b, #ff5f00, #0071ce, #142fbd) correspond to third-party payment-network brand colors (Mastercard, PayPal, Visa) and were deliberately excluded from the design token set as non-brand.
- Font sizes referenced via `var(--font-size-14)` etc. had no resolved pixel values in the supplied CSS; all typographic sizes in this spec are proposed estimates, not confirmed measurements.
- No hover/focus/active states beyond `.button--outline:hover` and `.button--secondary-outline:hover` were observed; all other interaction states are proposed.
- Mobile/responsive layout behavior was not directly observed; the breakpoint table above is a design recommendation only.
- Availability and licensing of "Aktiv Grotesk" and "Victor Serif" as web fonts were not verified; generic fallbacks (sans-serif, serif) are included per the observed `font-family` declarations.
