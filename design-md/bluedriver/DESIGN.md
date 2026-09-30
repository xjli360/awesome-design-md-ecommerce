---
version: alpha
name: "BlueDriver"
source_url: "https://www.bluedriver.com"
captured_at: "2026-09-29T04:18:42.693023+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  BlueDriver's storefront (served on the us.bluedriver.com Shopify theme) evidences a dark, technical
  brand register built on a near-black navy (#08101b) body background with white (#ffffff) text and
  card surfaces, punctuated by a signature blue gradient (#0070ff to #0086fe) used on primary and
  secondary buttons alike. A secondary teal (#108474) appears in the Judge.me review-widget tokens
  (star color, write-review button, reviewer name) and is treated here as an accent for trust/social-proof
  moments such as star ratings and verified-review badges. Body copy in cookie-consent and utility UI
  uses #212121 and #787978/#858585 grays, which this spec generalizes into ink and muted roles for the
  wider site. Headings use a secondary font family (var(--font-family-secondary)) at weight 700 with
  capitalized casing; the concrete family is not resolved in the supplied CSS, so Inter/Instrument Sans
  from the observed font stack is assumed as a close analog — flagged as inferred. Buttons are pill-shaped
  (40px radius) with the blue gradient fill. Layout structure (grid, breakpoints, spacing rhythm) is not
  present in the supplied CSS and is proposed here to fit a diagnostic-tool DTC/e-commerce product context.

colors:
  primary: "#0070ff"
  gradient-end: "#0086fe"
  ink: "#08101b"
  canvas: "#ffffff"
  body: "#212121"
  muted: "#787978"
  hairline: "#dedede"
  surface-soft: "#f4f4f4"
  surface-card: "#eeeeee"
  on-primary: "#ffffff"
  accent-teal: "#108474"
  link: "#1863dc"
typography:
  display-xl: {fontFamily: "'Instrument Sans', Inter, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Instrument Sans', Inter, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Instrument Sans', Inter, sans-serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, Roboto, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, Roboto, sans-serif", fontSize: 14px, fontWeight: 500, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, Roboto, sans-serif", fontSize: 12px, fontWeight: 600, lineHeight: 1.4, letterSpacing: 0.25px}
  button-md: {fontFamily: "Inter, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0.25px}
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
    background: "linear-gradient({colors.primary}, {colors.gradient-end})"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    borderColor: "{colors.primary}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    eyebrowTypography: "{typography.caption}"
    headingTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted}"
    linkColor: "{colors.link}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  compatibility-checker:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    accentColor: "{colors.accent-teal}"
    labelTypography: "{typography.caption}"
    resultTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"

## Components

**button-primary** carries the site's signature blue gradient (#0070ff → #0086fe), directly observed in `.btn--primary`'s background declaration, with a fully rounded 40px radius mapped here to `rounded.full`. It is the default call-to-action treatment ("Shop BlueDriver," "Add to Cart").

**button-secondary** is proposed as an outline variant using the same primary blue for border/text on a transparent field, since the supplied CSS shows `.btn--secondary` sharing the identical gradient fill as primary — an outline alternative is inferred for lower-emphasis actions rather than observed directly.

**text-input** is a proposed pattern (not present in supplied CSS) styled to match the light canvas sections implied by white-bg button variants, using a hairline border and standard body typography for forms such as newsletter signup ("Get Updates & Learn About Specials").

**nav-bar** is inferred from the dark `body` background (#08101b) carried through the theme; the header/utility bar (cart, compatibility, support, about links from the text excerpt) is assumed to sit on the same ink background with white text and a subtle hairline divider.

**product-card** proposes a card surface for shop-grid items (Pro Scan Tool, Next Gen, MAX) using the lighter `#eeeeee` surface-card token against the dark page background for contrast, with title and price typography scales — not confirmed by supplied grid CSS.

**hero** models the homepage banner ("Built For Weekend Wrenching") on the dark ink background with large display typography and a primary-button CTA; copy hierarchy is grounded in the text excerpt but exact type sizes are proposed.

**footer** reflects the multi-column link structure in the text excerpt (Shop/Support/About) on the ink background, muted gray body text, and blue link color (#1863dc, observed in the cookie-consent policy link) reused for footer link states.

**badge** uses the teal accent (#108474) sourced from the Judge.me review widget tokens (`--jdgm-primary-color`), proposed for small status labels like "60,000+ Reviews" or in-stock indicators; this is a semantic extension beyond its observed review-widget-only usage.

**search** is a proposed pill-shaped input for site search, unobserved in supplied evidence but stylistically consistent with the button radius pattern.

**compatibility-checker** is a category-specific component addressing BlueDriver's "Compatibility" nav item and Pro/Next-Gen compatibility pages referenced in the text excerpt; it pairs the soft surface background with the teal accent to visually distinguish a VIN/vehicle-lookup tool from standard content blocks — entirely proposed, as no compatibility-tool markup or styles were supplied.

## Responsive Behavior

Recommended (not measured) breakpoints: mobile ≤480px, small tablet 481–768px, tablet 769–1024px, desktop ≥1025px. Touch targets for buttons and nav items should maintain a minimum 44×44px hit area, consistent with the pill-button padding proposed above. Navigation is expected to collapse into a hamburger/off-canvas menu below the tablet breakpoint, and the cart drawer (referenced as "Your Cart" in the text excerpt) should remain a slide-in panel at all sizes. Product-card grids are recommended to reflow from a multi-column desktop layout to single-column on mobile. This section is a design recommendation only; no responsive CSS, media queries, or rendered mobile layout were present in the supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.





- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This specification is derived from a partial, static CSS/text extraction and does not reflect a rendered or interactive audit of bluedriver.com. Specific gaps: (1) The custom property values for `--color-background`, `--color-foreground`, `--color-button`, etc. were present as empty/unresolved declarations in the supplied `:root` rule, so component color mappings above are inferred from literal hex values found elsewhere in the CSS, not from these theme variables. (2) The heading font family (`var(--font-family-secondary)`) and button font family (`var(--font-family-button)`) are CSS variable references whose resolved font names were not supplied; Instrument Sans and Inter are assumed from the broader observed font list. (3) All typography sizes beyond what could not be directly read from CSS (most sizes) are proposed, not measured. (4) No hover/focus/active/disabled interaction states, no mobile/responsive layout, and no grid or spacing system were observed in the supplied CSS — spacing and rounded scales are proposed conventions, not extracted values. (5) Licensing and availability of any inferred custom fonts have not been verified. (6) The teal accent's promotion from a Judge.me review-widget-only token to a general badge/accent role is a design inference, not a confirmed brand-wide usage.
