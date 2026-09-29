---
version: alpha
name: "Taylor Guitars"
source_url: "https://www.taylorguitars.com"
captured_at: "2026-09-28T04:06:12.457595+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  The observed evidence shows a high-contrast, editorial system built on a pure white canvas (#ffffff), a near-black header (#000000), and a warm off-white section tone (#f6f5f1) that echoes tonewood and studio-photography backdrops common to acoustic-instrument brands. The single clearly observed brand accent is a deep red (#aa1f23) used on the primary "add to cart" button, paired with white text — a strong signal for a CTA/primary color role. Supporting neutrals (#333333, #767676, #dddddd) are inferred as body text, muted text, and hairline roles from generic UI/jQuery-widget rules rather than confirmed brand components. Typography pairs a serif display face, Sentinel SSm A/B, for h1/h2 (36px/700/1.15 observed) with a system UI sans-serif stack for body copy and controls; Gotham SSm A/B appears in the font stack evidence and is used here, as inferred, for mid-weight subheads. This interpretation extends that pairing into a fuller scale — serif for craftsmanship-forward headlines, system sans for utilitarian UI — while reusing the deep red sparingly as the sole call-to-action color, consistent with the one high-confidence brand signal in the evidence.

colors:
  primary: "#aa1f23"
  ink: "#1a1a1a"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#767676"
  hairline: "#dddddd"
  surface-soft: "#f6f5f1"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  header-bg: "#000000"
  accent-gold: "#b9883b"
  success: "#77b259"
  warning: "#e09600"
  error: "#a51b00"
  link-legacy: "#1155cc"
typography:
  display-xl: {fontFamily: "\"Sentinel SSm A\", \"Sentinel SSm B\", serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "\"Sentinel SSm A\", \"Sentinel SSm B\", serif", fontSize: "36px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "0px"}
  title-md: {fontFamily: "\"Gotham SSm A\", \"Gotham SSm B\", sans-serif", fontSize: "20px", fontWeight: 700, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, \"Segoe UI\", sans-serif", fontSize: "14px", fontWeight: 700, lineHeight: 1.4, letterSpacing: "0px"}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.header-bg}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.header-bg}"
    textColor: "{colors.canvas}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"
  audio-sample-player:
    backgroundColor: "{colors.surface-soft}"
    accentColor: "{colors.primary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"

## Components

**button-primary** reflects the one concretely observed component in the evidence: a red (#aa1f23) "add to cart" style action with white text, bold 14px type, and a 2px radius. It should remain the single dominant call-to-action color across the site, used sparingly for purchase and primary conversion actions.

**button-secondary** is proposed as an outlined inverse of the primary button, using the same red as a border/text color on a white fill, for lower-emphasis actions like "compare" or "find a dealer." Hover/pressed states are not observed and should be treated as proposed.

**text-input** is inferred from generic jQuery-UI form styling in the evidence (Arial/Helvetica stack, hairline borders). For the brand's own forms (search, newsletter, dealer locator) a body-md typography and hairline border on white is proposed to match the site's clean, editorial tone.

**nav-bar** is grounded in the observed `header.site-header` rule (`background:#000; color:#fff`). It is proposed as a fixed or sticky bar holding logo, primary navigation, search, and cart icons, all rendered in white-on-black per the observed header treatment.

**product-card** is a proposed pattern for guitar model listings, pairing a white surface with a hairline border, a serif-adjacent Gotham subhead for the model name, and body-md for price/spec text — no card-specific CSS was present in evidence, so structure and spacing are inferred from general layout conventions.

**hero** is proposed as a full-bleed dark section (using the observed near-black ink tone) carrying large serif display type, intended for flagship guitar-series storytelling on the homepage; exact homepage hero markup was not present in the supplied CSS.

**footer** reuses the observed black header background for visual bookending, with body-sm links and a hairline divider; specific footer column structure is not observed and is proposed.

**badge** is a proposed small label (e.g., "New," "Limited Edition") using the gold-toned accent color pulled from the palette, appropriate for premium/limited-run acoustic models; no badge component was present in the evidence.

**search** is proposed using a warm off-white field consistent with the surface-soft tone observed elsewhere in the palette, intended for the header search affordance implied by the "icon-search" reference in the page title metadata.

**audio-sample-player** is a category-specific, fully proposed component responding to the "Audio/No-Audio/Pause" icon references in the evidence, suitable for in-page sound-clip playback on acoustic-guitar product pages; no player markup or states were present in the supplied CSS.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior, since no media queries or responsive markup were present in the supplied evidence.

| Breakpoint | Width       | Notes (proposed) |
|-----------|-------------|-------------------|
| mobile    | 0–599px     | Single-column product cards; nav collapses to hamburger + icon row |
| tablet    | 600–1023px  | 2-column product grids; search expands inline |
| desktop   | 1024–1439px | 3–4 column product grids; full horizontal nav |
| wide      | 1440px+     | Increased gutters/section padding; hero imagery scales up |

Touch targets should be at least 44×44px for nav, cart, and audio-player controls. The primary navigation is expected to collapse into a slide-out or dropdown menu below tablet width; this collapse behavior is proposed, not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS/text extraction only; no rendered page, JavaScript-driven state, or DOM screenshots were available. Several color-to-role mappings (ink, body, muted, hairline, surface-soft/card) are inferred from generic or jQuery-UI-widget selectors rather than confirmed brand-specific components, and may not match actual production usage. Typography sizes beyond the observed h1/h2 (36px/700/1.15) and button (14px/700) rules are proposed extrapolations, not measured values. Gotham SSm A/B is included based on its presence in the font-family evidence list, but no selector tying it to a specific role was supplied, so its usage here is inferred. Interaction states (hover, focus, active, disabled), mobile navigation behavior, and hero/footer layout structure were not observed and are marked proposed throughout. Availability and licensing of Sentinel SSm and Gotham SSm as web fonts were not verified and should be confirmed before implementation.
