---
version: alpha
name: "Rockford Fosgate"
source_url: "https://rockfordfosgate.com"
captured_at: "2026-09-28T09:09:16.395813+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Evidence shows a dark, high-contrast automotive-audio aesthetic built on near-black
  neutrals (#272727, #1e1e1e, #1c1c1c) paired with a white canvas (#ffffff) used for
  lighter sections (body.light .main-content). Body copy runs Source Sans Pro Regular
  at 16px/26px line-height; headings (h1, h2, .h0) use Helvetica Neue Bold Condensed
  for a compact, aggressive tone fitting motorsport branding. A saturated red
  (#d60925, with #e8112d and #c40821 as close variants) recurs across the palette and
  is inferred here as the primary accent for CTAs and brand marks; no supplied CSS
  rule directly ties red to a button, so this role mapping is inferred, not observed.
  A warm cream (#ffe7b5) is confirmed on hero subheadings and bracketed CTA text over
  dark hero imagery. Buttons use a distinctive bracketed-corner treatment
  (.btn-bracketed, .btn-bracketed-new) with uppercase, letter-spaced Helvetica Neue
  labels and no visible border-radius, implying a squared, technical visual language
  rather than soft rounding. Font families Abolition-Round and Zuume appear in the
  evidence list without associated selectors, so their use for large display
  headlines is inferred, not confirmed. This interpretation favors a dark-capable,
  utilitarian layout emphasizing product categories (Mobile, Marine, Motorsports,
  Motorcycle) with sharp edges and high-contrast text.

colors:
  primary: "#d60925"
  primary-alt: "#e8112d"
  primary-dark: "#c40821"
  ink: "#272727"
  canvas: "#ffffff"
  body: "#272727"
  muted: "#585858"
  hairline: "#e7e7e7"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  surface-dark: "#1e1e1e"
  surface-dark-alt: "#1c1c1c"
  accent-warm: "#ffe7b5"
  border-dark: "#4a4a4a"
typography:
  display-xl: {fontFamily: "'Abolition-Round', 'Helvetica Neue Bold Condensed', sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Helvetica Neue Bold Condensed', 'Helvetica Neue', sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.125, letterSpacing: "0px"}
  title-md: {fontFamily: "'Helvetica Neue', sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0.4px"}
  body-md: {fontFamily: "'Source Sans Pro Regular', monospace, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.625, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Source Sans Pro Regular', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'Helvetica Neue', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.79, letterSpacing: "2.1px"}
  button-md: {fontFamily: "'Helvetica Neue', sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.2, letterSpacing: "0.8px"}
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
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    hairline: "{colors.border-dark}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-dark-alt}"
    overlayColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    eyebrowTypography: "{typography.caption}"
    eyebrowColor: "{colors.accent-warm}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-primary}"
    hairline: "{colors.border-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  category-tile:
    backgroundColor: "{colors.surface-dark-alt}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-md}"
    hoverOverlay: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"

## Components

**button-primary** — A solid red CTA (inferred primary color, since no rule maps
red directly to a button) intended for high-priority actions like "Shop Now." Uses
squared corners consistent with the site's sharp bracketed-button motif rather than
observed rounding.

**button-secondary** — Mirrors the observed `.btn-bracketed`/`.btn-bracketed-new`
pattern: transparent background, ink-colored uppercase label, letter-spaced Helvetica
Neue text, and a proposed hover state lightening the text color as seen in
`.btn-bracketed:hover` (color shifts to #4a4a4a).

**text-input** — Proposed field style for search/newsletter forms; no input CSS was
supplied, so background, border, and radius are inferred from the site's light
surface tones (#f8f8f8) and hairline grays (#e7e7e7).

**nav-bar** — Dark persistent navigation bar reflecting `body` and
`.page-dark-header` background tones (#272727), housing category links (Mobile,
Marine, Motorsports, Motorcycle) and cart/search icons; exact layout not observed.

**product-card** — Proposed card for product/category listings using a white surface,
subtle hairline border, and condensed title typography matching the brand's
heading style; card shadow/elevation was not present in supplied CSS.

**hero** — Full-bleed dark hero matching `.parallax-hero`, with white 32px headline
text, a cream (#ffe7b5) uppercase eyebrow line, and a bracketed CTA button
positioned below — directly grounded in the supplied hero CSS.

**footer** — Dark footer band using the same near-black surface as the header,
carrying support/dealer links and social icons in body-sm typography; content
hierarchy is proposed, not observed in detail.

**badge** — Small pill-shaped label (e.g., "NEW") in primary red, proposed for
flagging new products such as "New Punch Pro Speakers," referencing marketing
copy in the page-text excerpt.

**search** — Lightweight search field styled with the site's light neutral surface;
proposed since no dedicated search-input CSS was supplied, only the presence of a
"Search" control in navigation text.

**category-tile** — A category-appropriate component representing the site's core
navigation pattern (Mobile / Marine / Motorsports / Motorcycle / OEM Audio /
Accessories / Apparel), styled as a dark tile with a red hover overlay to reinforce
brand accent usage.

## Responsive Behavior

This is a proposed breakpoint scheme, not measured site behavior:

| Breakpoint | Width        | Notes                                   |
|------------|--------------|------------------------------------------|
| xs         | <480px       | Single-column, stacked hero text          |
| sm         | 480–767px    | Nav collapses to hamburger menu           |
| md         | 768–1023px   | 2-column product grids                    |
| lg         | 1024–1279px  | Full nav bar, 3-column product grids      |
| xl         | ≥1280px      | Max-width container, 4-column grids       |

Touch targets should be at least 44px for buttons and nav links. The uppercase
bracketed-button style should retain adequate horizontal padding on touch devices
to avoid accidental taps. Mobile nav collapse behavior is a recommendation only —
no hamburger menu markup or breakpoint values were present in supplied evidence.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS/text extraction, not a rendered or
interactive audit. The mapping of red tones (#d60925, #e8112d, #c40821) to a
"primary" action color is inferred from palette frequency, not from an observed
button rule. Font families Abolition-Round, Zuume, and Dementer appear in the
evidence's font list but no selector confirms where they are applied; their
proposed use for display headlines is speculative. Border-radius values are not
present in any supplied CSS rule — the `rounded` scale is a proposed convention,
and the bracketed-button style suggests the brand may favor sharp corners over
rounding in practice. Spacing tokens follow a generic scale, not measured layout
values. Mobile/responsive behavior, hover/focus states beyond the two documented
`:hover` rules, and interactive component states (input focus, cart drawer,
dealer-locator modal) were not observed and are proposed only. Licensing and
web-font availability for Abolition-Round, Dementer, and Zuume were not verified.
