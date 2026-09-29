---
version: alpha
name: "A Pup Above"
source_url: "https://apupabove.com"
captured_at: "2026-09-28T04:45:49.675989+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  A Pup Above's storefront evidence points to a deep forest-teal (#0C3D37) as the
  dominant brand color, applied to the header, nav headings, and drawer accents,
  paired with white text for contrast. A lighter mint-green (#76D4B2) appears on
  active navigation states, suggesting a secondary "fresh/organic" accent family
  alongside softer mint surfaces (#D8F1EA, #C0DED2) likely used for section
  backgrounds. Warm accent hues (#FDBA12 yellow, #FF6600 orange, #D20000 red)
  exist in the palette and are inferred as promotional, badge, or alert colors
  rather than confirmed primary actions, since no button component CSS was
  supplied. Body copy defaults to the theme's --color-foreground (#121212) at
  75% opacity, implying a softened near-black for running text versus pure ink
  for headings.

  Typography mixes a condensed uppercase sans ('Marquee') for header/nav labels
  with a warm serif ('Crete Round') for descriptive copy in mega-menus and
  banners — an inferred pairing of a bold utilitarian brand voice against a
  friendlier, editorial secondary voice. Additional families in evidence
  (Knockout weights, DD Paytone One, Raw Selvage) suggest a heavier condensed
  display face is reserved for hero/marketing headlines, though no headline CSS
  rule was directly observed, so that mapping is proposed rather than confirmed.
  The resulting system leans natural, appetite-appealing, and vet-credible:
  deep greens for trust, mint accents for freshness, and warm badge colors for
  urgency or promotions.

colors:
  primary: "#0c3d37"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#0c3d3799"
  muted: "#849e9b"
  hairline: "#ebebeb"
  surface-soft: "#d8f1ea"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  accent: "#76d4b2"
  accent-strong: "#178468"
  cta-warm: "#fdba12"
  alert: "#d20000"
  overlay-scrim: "#0000001a"
typography:
  display-xl: {fontFamily: "'Knockout 48', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'DD Paytone One', sans-serif", fontSize: 32px, fontWeight: 400, lineHeight: 1.2, letterSpacing: 0px}
  title-md: {fontFamily: "'Marquee', sans-serif", fontSize: 18px, fontWeight: 300, lineHeight: 1.3, letterSpacing: 0.5px}
  body-md: {fontFamily: "'Assistant', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.06rem}
  body-sm: {fontFamily: "'Crete Round', serif", fontSize: 15px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
  caption: {fontFamily: "'Assistant', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.4px}
  button-md: {fontFamily: "'Marquee', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1, letterSpacing: 0.5px}
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
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    activeStateBackground: "{colors.accent}"
    activeStateTextColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    descriptionTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  recipe-selector:
    backgroundColor: "{colors.surface-soft}"
    activeBorderColor: "{colors.accent-strong}"
    labelTypography: "{typography.caption}"
    priceTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-sm}"
    ctaComponent: "button-primary"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-md}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.cta-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** carries the dark teal brand color with white text, matching the header's high-contrast treatment observed on `.apa-header__icon-btn` and nav links; proposed as the default checkout/add-to-cart action.

**button-secondary** is a proposed outline variant using the same teal as border and text on a white fill, for lower-emphasis actions like "Learn More" — not directly observed but consistent with the two-tone header palette.

**text-input** is a proposed minimal field using the light hairline gray for borders, since no form-field CSS was supplied; ink text and a small radius keep it consistent with the header's rounded (6px-class) elements.

**nav-bar** reflects the observed `.apa-header` styling: solid dark teal background, uppercase white nav links, and a mint-green (#76D4B2) active/mega-menu state with dark teal text — directly grounded in the supplied `.apa-header__mega-active` rule.

**product-card** is inferred from the best-seller grid content (recipe name, price, short description) rather than measured CSS; it uses a light neutral card surface and the body-sm serif style seen in mega-menu product descriptions for its blurb text.

**recipe-selector** is a category-specific proposed component for the "rotate your pup's proteins" recipe-picker UI implied by the page text, using the soft mint surface and a stronger teal accent border to indicate a selected protein/recipe.

**hero** proposes a soft mint background with a large display headline, appropriate for the "sous-vide & bone broth infused" messaging, though hero-section CSS itself was not in the supplied evidence.

**footer** mirrors the header's dark teal/white combination, an inferred continuation of the brand's single strong-contrast color pairing rather than a separately observed footer style.

**badge** uses the warm yellow (#FDBA12) from the palette as a pill-shaped label, proposed for callouts like "Best Seller" or "4.9★ Reviews," since no badge-specific rule was supplied but the color is present in the observed palette.

**search** is a proposed lightweight input styled like text-input, since the site includes a "Close search" control in page text but no corresponding CSS was captured.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| Mobile | <749px | Single-column product grid, nav collapses to a drawer (implied by "Close search" / cart-drawer text) |
| Tablet | 749–989px | 2-column product/recipe grid |
| Desktop | ≥990px | Multi-column grid; mega-menu with 3-column link grid as seen in `.apa-header__mega-links--grid` |

Touch targets should be at minimum 44×44px for icon buttons and nav toggles. The mega-menu's 3-column grid layout is expected to collapse to a stacked list under the drawer navigation on mobile — this collapse behavior is proposed, not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Static CSS extraction provides no confirmation of actual live layout, breakpoints, or responsive collapse behavior; all responsive guidance above is proposed.
- The exact value of `--font-body-family` was not included in the supplied evidence; "Assistant" is used as the body font based on its presence in the observed font list, but this mapping is inferred, not confirmed.
- Button, form-input, hero, footer, and card component CSS were not present in the supplied evidence; all such components are proposed patterns based on general e-commerce conventions and the brand's header styling.
- Color-role assignments (e.g., cta-warm, alert, accent) are inferred from palette presence, not from confirmed usage in button/state CSS.
- Custom font availability, licensing, and actual rendering (e.g., 'Marquee', 'Knockout', 'Raw Selvage') were not verified; fallback to sans-serif/serif is assumed.
- Interaction states (hover, focus, disabled, error) were not observed in the supplied CSS and are not defined here.
- Font sizes for typography roles beyond the body base (1.5rem) are proposed conventional values, since root font-size and most heading rules were not supplied.
