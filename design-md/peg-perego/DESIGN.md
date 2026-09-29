---
version: alpha
name: "Peg Perego"
source_url: "https://pegperego.com"
captured_at: "2026-09-29T04:02:53.236955+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Peg Perego's storefront CSS shows a single dominant brand color: a deep navy
  (#1e284c) used as the base text color for both `body` and `h1` selectors,
  making it function as both ink and de facto brand primary rather than a
  separate accent. Typography is set in Lato with a Helvetica Neue/Arial/
  sans-serif fallback stack, a restrained weight range (400 for headings, 600
  for buttons), and a fully rounded (100px) pill button shape with a soft
  lavender-gray background (#eeeef1) and navy text — an inferred secondary/
  tertiary action style rather than a high-contrast primary CTA. The wider
  observed palette includes several reds (#e02b27, #d30910, #e80000), which
  this spec treats as inferred promotional/sale accents given the page's
  "Car Seat Safety Week" banner copy, and a blue (#006bb4) treated as an
  inferred informational/link accent. Numerous neutral grays (#cccccc through
  #f6f6f6) are folded into hairline and surface-soft/surface-card roles. No
  live layout, breakpoints, or interaction states were observed; all spacing,
  radii, and non-button typography sizes below are proposed conventions
  layered onto the confirmed color and font evidence for a car-seat category
  storefront emphasizing safety, trust, and clarity.

colors:
  primary: "#1e284c"
  ink: "#1e284c"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#817a95"
  hairline: "#dddddd"
  surface-soft: "#eeeef1"
  surface-card: "#f6f6f6"
  on-primary: "#ffffff"
  accent-cta: "#e02b27"
  accent-info: "#006bb4"
  border-strong: "#bbb9c7"
typography:
  display-xl: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 48px, fontWeight: 400, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 24px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.4286, letterSpacing: 0px}
  body-sm: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Lato','Helvetica Neue',Helvetica,Arial,sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.125, letterSpacing: 0.2px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    accentColor: "{colors.accent-cta}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-cta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  stage-fit-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    borderColor: "{colors.accent-info}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

**button-primary**: Modeled on the confirmed `button` rule — pill-shaped (100px radius, i.e. `rounded.full`), 600-weight Lato label, `10px 24px` padding — but with the background/text roles inverted to `surface-soft`/`on-primary` here since the observed background (#eeeef1) is light and low-contrast against white canvas; this inversion is a proposed refinement for a true primary CTA, not the literally observed style.

**button-secondary**: Proposed outline variant reusing the same pill shape and button typography, for lower-emphasis actions (e.g., "Discover more" links) that appear throughout the category navigation copy.

**text-input**: Proposed field style for search, account, and newsletter forms; no input-specific CSS was supplied, so border color, radius, and padding are inferred from the general hairline/spacing scale.

**nav-bar**: Represents the top utility/category navigation implied by the page text ("Strollers, Car Seats, High Chairs, Accessories, Shop Parts, Outlet, Account, Wishlist, My Cart"). Background and ink colors are drawn from observed base values; the horizontal structure itself is proposed, not measured.

**product-card**: Supports the "Most Requested Baby Products" grid (e.g., Vivace, City Loop + Urban Mobility, Primo Viaggio Lounge) seen in the page text, including a title, price, and sale badge slot using the accent-cta color for "As low as / Regular Price" strike-through treatments.

**hero**: Proposed full-width promotional banner pattern for entries like "City Loop," "YPSI," and the "Car Seat Safety Week sale" message, using the soft surface background and display-xl heading scale.

**footer**: Proposed dark-navy footer using `colors.primary` as background with white text, inferred from the brand's consistent use of navy as its identifying color; actual footer markup/colors were not present in the supplied evidence.

**badge**: Proposed small pill label for sale/promo flags such as "20% off," using one of the observed reds (#e02b27) as an inferred promotional accent — the CSS evidence does not confirm this color's actual UI usage.

**search**: Proposed pill-shaped search field to match the confirmed "Search" affordance mentioned in the page text and the button radius already observed in CSS.

**stage-fit-badge**: A car-seat-category-specific label (e.g., "0–12 years," "Infant," "Convertible," "All-in-One," "Booster") to help parents quickly identify product stage/fit, styled with the inferred info-blue border for a clinical, safety-oriented tone appropriate to car seat merchandising. Fully proposed; no equivalent markup was present in evidence.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | <768px | Single-column product grids, hamburger nav (an actual "Hamburger" control is referenced in the page text, confirming its presence though not its breakpoint or animation) |
| Tablet | 768–1024px | 2-column product grids, condensed nav labels |
| Desktop | >1024px | Full horizontal nav with mega-menu style category flyouts implied by the nested Strollers/Car Seats/High Chairs listings in the page text |

Touch targets should be at least 44×44px for buttons and nav items given the pill button's generous `10px 24px` padding. This table is a **recommendation based on common e-commerce patterns**, not measured site behavior; no media queries, container widths, or actual mobile screenshots were supplied.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, JavaScript-driven interactions, or mobile viewport screenshots were observed.
- The pixel sizes in `typography` assume a 10px root font-size to convert observed `rem` values (e.g., `1.6rem` body, `3rem` h1); this root size was not directly confirmed and is a proposed assumption.
- Color-to-role mapping (primary vs. accent vs. informational) is inferred from color quantity and contextual page copy (e.g., sale banner text), not from confirmed element-level CSS bindings for most non-button elements.
- `button-primary`'s background/text roles were inverted from the literally observed `button` rule (light bg/dark text) to produce a higher-contrast primary action; this is a designed proposal, not an observed pattern.
- Footer, hero, product-card, and search components have no corresponding CSS rules in the supplied evidence; their color and spacing values are proposed extrapolations from the confirmed base palette and button styling.
- Lato is a widely available open-source (Google Fonts) family, but its licensing/self-hosting configuration for this specific deployment was not verified from the supplied evidence.
- No hover, focus (beyond the generic `button:focus`/`:active` background repeat), disabled, or error states were observed for any component beyond the base button rule.
