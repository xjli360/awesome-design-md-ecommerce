---
version: alpha
name: "Kwikset"
source_url: "https://kwikset.com"
captured_at: "2026-09-28T09:37:48.704258+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Kwikset's site evidence shows a utilitarian, security-hardware register: a near-black text color paired with a saturated red (#d90114, hovering to #f00016 and darkening to #d01b32) used consistently across primary call-to-action buttons ("BUY DIRECT," "SHOP NOW," "LEARN MORE"). Typography is set almost entirely in the Gotham SSm A/B family with Tahoma and generic sans-serif fallbacks, at a tight -0.04em tracking on body copy and headings, while buttons and jump-links use wider, uppercase 0.1em tracking — a pattern kept intact here as button-md and a separate heading letter-spacing rule. Font Awesome and slick-carousel classes confirm icon-driven navigation and homepage sliders (product drops, smart-lock features) rather than a single static hero.
  Color roles below are inferred from usage context, not confirmed live-site screenshots: ink and body text are drawn from the darkest observed grays (#000000, #333333), muted text from mid-grays (#626262/#888888), hairlines and card backgrounds from the extensive light-gray set (#e6e6e6, #f6f6f6, #f4f4f4). A cross-brand utility bar (.weiserheader/.weiserfooter, #242424) suggests Kwikset shares infrastructure with sister brands, informing the footer's dark surface here. Blue accents (#007aff, #3b99fc) are treated as smart-home/App-compatibility badge colors given "Works With App," Matter, and Apple references in the copy.

colors:
  primary: "#d90114"
  primary-hover: "#f00016"
  primary-darker: "#d01b32"
  ink: "#000000"
  ink-soft: "#242424"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#626262"
  hairline: "#e6e6e6"
  surface-soft: "#f6f6f6"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  accent-blue: "#007aff"
  success: "#1ca563"
  danger: "#be1e1e"
typography:
  display-xl: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', Tahoma, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.04em}
  display-md: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', Tahoma, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.04em}
  title-md: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', Tahoma, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: -0.04em}
  body-md: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', Tahoma, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: -0.04em}
  body-sm: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', Tahoma, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: -0.04em}
  caption: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', Tahoma, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0em}
  button-md: {fontFamily: "'Gotham SSm A', 'Gotham SSm B', Tahoma, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1.2, letterSpacing: 0.1em}
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
    padding: "14px 32px"
    hover: "{colors.primary-hover}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.ink}"
    overlayColor: "{colors.ink-soft}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink-soft}"
    textColor: "{colors.surface-soft}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  compatibility-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    accentColor: "{colors.accent-blue}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xs} {spacing.sm}"

## Components
**button-primary** is the site's dominant call-to-action, directly evidenced by `.btn--solid` (background `#d90114`, white text, 14px/32px padding) with a lighter-red hover (`#f00016`); used for "SHOP NOW," "BUY DIRECT," and "LEARN MORE" prompts throughout the homepage copy.

**button-secondary** is proposed for lower-emphasis actions (e.g., "Compare Smart Locks," "Browse all smart locks") using an outlined ink border on transparent background, inferred from the presence of `.btn--black` and `.btn--transparent` variants in the CSS without full state definitions.

**text-input** is proposed for the sitewide search field ("Search Toggle Site Navigation," "Search Search Close Search"); no explicit input styling was supplied, so border, radius, and padding are inferred defaults consistent with the hairline/canvas palette.

**nav-bar** represents the primary site header with Products/Support/About mega-menu items; layout and stickiness are not confirmed by the evidence and are treated as a conventional proposed pattern.

**product-card** supports the category grid (Deadbolts, Knobs, Handlesets, Levers, Padlocks) referenced in the "Ready to browse?" section; card surface and hairline border are inferred from the extensive light-gray token set since no card-specific selector was supplied.

**hero** covers rotating homepage promotions (Tripoli/Arroyo direct-sale banners, Halo Select Plus, Aura Reach) implied by slick-carousel classes; dark overlay and white text are proposed, not confirmed as the live rendering.

**footer** reuses the dark `.weiserheader`/`.weiserfooter` background (`#242424`) as the closest observed evidence of a persistent dark chrome band, extended here to a full site footer housing Support/About/Trade-Professional links.

**badge** is proposed for small status labels such as "NEW," "AVAILABLE NOW," or "Limited Time Offer" callouts seen in the copy, using the observed green (`#1ca563`) as a neutral success/highlight tone since no badge-specific CSS was supplied.

**search** models the full-page search overlay implied by repeated "Search" tokens in the extracted text; treated as a distinct component from text-input because Kwikset's copy suggests a dedicated overlay/close pattern rather than an inline field.

**compatibility-badge** is a hardware/smart-lock-specific component for "Works With App," Matter, and Apple Home/Watch integration marks referenced in the smart-lock copy; it uses the Apple-blue-adjacent accent (`#007aff`) observed in the palette, on a soft neutral background, and is explicitly proposed since no compatibility-icon markup was supplied.

## Responsive Behavior
This is a recommendation, not measured site behavior; no breakpoints, media queries, or mobile layouts were present in the supplied evidence.

| Breakpoint | Width | Layout guidance (proposed) |
|---|---|---|
| mobile | <768px | Single-column stacks; nav collapses to hamburger/off-canvas menu; hero CTA stacks under headline |
| tablet | 768–1023px | 2-column product-card grid; nav condenses top-level items |
| desktop | 1024–1439px | 3–4 column product-card grid; full mega-menu nav |
| wide | ≥1440px | Max-width container (~1280–1440px) with increased section padding |

Touch targets should be a minimum 44×44px for buttons and nav items (proposed, WCAG-aligned, not measured). Mobile nav is assumed to collapse into a toggled off-canvas panel given the "Search Toggle Site Navigation" text pattern, but the actual collapse mechanism, animation, and breakpoints were not observed.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This specification is derived from static CSS/text extraction only; no rendered screenshots, computed styles, or DOM layout were available. Semantic color roles (ink, body, muted, hairline, surface-soft/card) are inferred from hex frequency and plausible usage context, not confirmed against live element inspection. Typography sizes beyond what a few utility classes hinted at (button 16px/0.1em tracking, heading -0.04em tracking) are proposed conventions, not measured font-size declarations. Interaction states (focus, active, disabled, form validation), mobile navigation behavior, and carousel/slider timing are not observed — only the presence of slick-carousel and Font Awesome classes is confirmed. Gotham SSm A/B is a licensed commercial font family; availability and licensing for reuse were not verified, and Tahoma/sans-serif are supplied as safe fallbacks only. The `proxima-nova` and `Baskerville` entries in the font list were not tied to any specific selector in the evidence and were therefore omitted from the typography tokens.
