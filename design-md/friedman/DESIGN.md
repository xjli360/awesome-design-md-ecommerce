---
version: alpha
name: "Friedman"
source_url: "https://www.friedmanamplification.com"
captured_at: "2026-09-28T10:32:51.038732+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from Friedman Amplification's WooCommerce/Divi-powered
  storefront selling USA hand-built tube amps, cabinets, and pedals. The only clearly
  brand-specific token in the evidence is the warm gold "#bea668", which repeats across
  the sticky header background, footer widget headings, and primary form/submit buttons
  with an explicit uppercase, tight letter-spacing (-1px) treatment. Body copy and
  headings resolve to pure black ("#000000") on white ("#ffffff") per the h1-h6 rule and
  the mini-cart (xoo-wsc) text color. A dark charcoal ("#32373c") appears as the default
  WordPress block-button background, suggested here as a secondary/dark surface. Neutral
  grays ("#eeeeee", "#c6c6c6", "#949494", "#767676", "#dee2e6") are treated as inferred
  hairlines, muted text, and card surfaces since no distinct roles were labeled in source.
  The remaining palette entries are standard Gutenberg default swatches (reds, blues,
  purples, oranges) unlikely to be intentional brand colors and are excluded from primary
  roles. Fonts observed are Josefin Sans, Raleway, Roboto, and system sans-serif stacks;
  heading/body assignment below is inferred from typical Divi/WooCommerce usage, not
  confirmed per-element. Layout, spacing, and breakpoints are proposed, not measured.

colors:
  primary: "#bea668"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#222222"
  muted: "#767676"
  hairline: "#eeeeee"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary-dark: "#32373c"
  accent-hover: "#9999ff"
  border: "#dee2e6"
  muted-2: "#c6c6c6"
typography:
  display-xl: {fontFamily: "'Josefin Sans', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Josefin Sans', sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Raleway', sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "'Raleway', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Raleway', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Raleway', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Raleway', sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1, letterSpacing: -1px, textTransform: uppercase}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.secondary-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    headingColor: "{colors.primary}"
    textColor: "{colors.muted-2}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  cart-drawer:
    headerBackground: "{colors.canvas}"
    headerBorder: "{colors.hairline}"
    bodyBackground: "{colors.canvas}"
    itemTypography: "{typography.body-md}"
    itemPadding: "{spacing.lg} {spacing.base}"
    emptyStateColor: "{colors.muted}"

## Components

**button-primary** reflects the observed gold (`#bea668`) submit/CTA background with white text, uppercase transform, and the explicit `-1px` letter-spacing found in the WooCommerce submit-button rule; hover swaps to a transparent gold-bordered state per source (`background-color:rgba(190,166,104,0)`), proposed here as the interactive state.

**button-secondary** is inferred from the default WordPress/Gutenberg block-button rule (`#32373c` background, white text), offered as a darker alternative action for secondary flows like "Learn More" links; no distinct secondary hover was observed.

**text-input** is a proposed pattern with no direct field styling in the evidence; white background and a light neutral border are assumed to match the site's WooCommerce/Divi form conventions.

**nav-bar** models the observed `#top-header` and fixed-header rules, which set a solid gold background (`#bea668`) rather than a typical white/dark bar — a distinctive brand choice worth preserving. Text color is proposed as black for contrast; no scroll-state details were captured.

**product-card** draws from the `.xoo-wsc-product` mini-cart item rule (white background, `20px 15px` padding, `border-radius:0`) and generalizes it to full product listings (Heads, Cabs, Pedals) — title and price typography are proposed, not confirmed for grid cards specifically.

**hero** is proposed to anchor the homepage's featured-product callouts (e.g., "JOSE 20", "PLEX", "Jake E Lee Signature") seen in the text excerpt; no hero CSS was supplied, so background/typography choices are inferred from global heading and color rules.

**footer** uses the confirmed `#bea668` heading color for footer widget titles (`.footer-widget h4`, `#main-footer h1-h4`) against a dark ink background, which is proposed since footer background color itself was not directly captured.

**cart-drawer** is the most concretely evidenced component: the `.xoo-wsc-header`, `.xoo-wsc-body`, and `.xoo-wsc-products` rules confirm a white-background slide-out cart with black text, 16px product typography, and zero border-radius on line items — directly usable as-is.

**badge** and **search** are proposed patterns for stock/availability tags ("Available Now") and the header search icon referenced in page text (`account_circle`, `search search`); no dedicated styling was supplied for either.

## Responsive Behavior

| Breakpoint | Range | Notes (proposed) |
|---|---|---|
| Mobile | ≤ 599px | Single-column product grid, collapsed hamburger nav, cart drawer full-width |
| Tablet | 600–1023px | 2-column product grid, nav collapses at lower end of range |
| Desktop | 1024–1079px | 3-column product grid, full horizontal nav |
| Wide | ≥ 1080px | Content capped near the observed `--wp--style--global--wide-size: 1080px` token |

Touch targets should be at least 44×44px for buttons and nav items; the gold nav bar and gold CTAs should maintain WCAG-contrast black text at small sizes. This table is a recommendation based on common WooCommerce/Divi conventions, not measured breakpoints or verified responsive CSS from the source.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no rendered layout, real breakpoints, hover/focus states, or animation were observed beyond the two hover rules captured (`#9999ff` load-more hover, gold-button hover-to-transparent).
- Font-to-element mapping (Josefin Sans vs. Raleway vs. Roboto for headings vs. body) is inferred from common Divi/WooCommerce theme conventions, not confirmed per-selector.
- Most spacing, radius (beyond the confirmed `0px` on buttons/products), and component sizes are proposed defaults, not measured.
- Many palette entries (e.g., `#cf2e2e`, `#0693e3`, `#9b51e0`, `#fcb900`) are standard Gutenberg editor default swatches and were excluded from brand roles as unverified brand intent.
- Mobile navigation, cart-drawer open/close interaction, and product-grid responsive column counts were not observed and are marked proposed.
- Custom font licensing/self-hosting for Josefin Sans/Raleway was not verified; assume web-font availability needs confirmation before implementation.
