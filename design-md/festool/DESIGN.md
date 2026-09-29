---
version: alpha
name: "Festool"
source_url: "https://festoolusa.com"
captured_at: "2026-09-28T04:48:36.730104+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Festool USA's evidence set shows a utilitarian, high-contrast industrial palette
  built around a saturated safety green (#46b82e, hover #3d9f28) used for primary
  buttons, paired with a slate blue-gray (#536877/#43545f) for secondary actions.
  Status colors follow a conventional pattern: green success (#43ac6a), red alert
  (#ce272d), and orange warning (#f08a24), consistent with a large e-commerce
  catalog of tools, batteries, and accessories. Body copy renders in DINWebPro
  with Verdana/sans-serif fallback, a condensed, technical German-engineered feel
  appropriate to the brand. A deep navy (#191e2b/#111622) appears in the palette
  and is inferred here as a header/footer ground rather than a proven role, since
  no header selector was captured. Neutral grays (#efefef, #dddddd, #f9f9f9,
  #e9edf1) are treated as card, hairline, and soft-surface tones for a dense
  navigation of tool categories. Button radius is ambiguous in the evidence — one
  inline CTA uses 6px, while the core `.button` class is square (0px) — so this
  spec proposes a small 4px default radius as a restrained middle ground, noting
  the conflict. All semantic role assignments beyond literal button/background
  declarations are inferred and flagged accordingly.

colors:
  primary: "#46b82e"
  primary-hover: "#3d9f28"
  secondary: "#536877"
  secondary-hover: "#43545f"
  success: "#43ac6a"
  alert: "#ce272d"
  warning: "#f08a24"
  ink: "#191e2b"
  canvas: "#ffffff"
  body: "#3f3c39"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f9f9f9"
  surface-card: "#efefef"
  on-primary: "#ffffff"
  border-soft: "#e9edf1"
  navy-deep: "#111622"
typography:
  display-xl: {fontFamily: "DINWebPro, Verdana, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "DINWebPro, Verdana, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "DINWebPro, Verdana, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
  body-md: {fontFamily: "DINWebPro, Verdana, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "DINWebPro, Verdana, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "DINWebPro, Verdana, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "DINWebPro, Verdana, sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
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
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"
    borderColor: "{colors.secondary-hover}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.xxl} {spacing.section}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  voltage-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.xs}"

## Components

**button-primary** renders the safety-green fill (`#46b82e`) observed directly on the live CTA/livechat button, with white text and a proposed 4px radius reconciling the two conflicting observed radii (0px in `.button`, 6px inline). Hover darkens to `#3d9f28`, matching the CSS `:hover`/`:focus` rule exactly.

**button-secondary** uses the observed slate `.button.secondary` colors (`#536877` fill, `#43545f` border/hover) for lower-priority actions like "compare" or "add to list," proposed to sit beside primary CTAs on product pages.

**text-input** is proposed and unobserved in the evidence; it borrows the neutral hairline (`#dddddd`) and body ink for a plain, industrial form field consistent with the site's utilitarian tone.

**nav-bar** infers the deep navy (`#191e2b`) as the header/mega-menu ground given the large nested category taxonomy (Tools, Accessories, Fan Shop) implied by the page text; this color-to-role mapping is not confirmed by a captured header selector.

**product-card** proposes the light gray `#efefef` surface with a hairline border to separate dense tool listings (saws, sanders, dust extractors) — a common catalog pattern, not directly observed.

**hero** is proposed for a top-of-page campaign banner (e.g., "Win the Ultimate Festool Setup") using the large display type scale; no hero-specific CSS was captured.

**footer** infers the darkest navy (`#111622`) as a footer ground with muted gray link text, typical for dealer/company/blog link clusters mentioned in the page text.

**badge** reuses the observed `.button.warning` orange (`#f08a24`) as a promotional/sale indicator pill; pairing and exact usage are proposed.

**search** is a proposed lightweight search bar treatment using the soft off-white surface (`#f9f9f9`), since no search-input selector was present in evidence.

**voltage-badge** is a category-specific proposed component for labeling cordless tool voltage (e.g., "18V") seen throughout the taxonomy text, styled as a small dark navy pill to sit on product thumbnails.

## Responsive Behavior

Breakpoints below are drawn directly from observed media-query fragments (em-based, Foundation-style); pixel conversions assume 16px root and are approximate. This table is a **recommendation**, not measured live layout behavior:

| Range | ~Px | Proposed behavior |
|---|---|---|
| ≤45em | ≤720px | Single-column stack, collapsed hamburger nav, full-width cards |
| 45.0625–75em | 721–1200px | Two-column product grids, condensed nav labels |
| 75.0625–90em | 1201–1440px | Three-column grids, expanded mega-menu |
| 90.0625–120em | 1441–1920px | Four-column grids, wider hero |
| ≥120.0625em | ≥1921px | Max-width container, extra gutter |

Touch targets are proposed at a minimum 44px height for buttons and nav items; the deeply nested category menu (Tools > Cordless products > ... ) should collapse to an accordion on mobile — this interaction is not observed and is a UX recommendation only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This spec is derived from static CSS/text extraction only; no rendered page, JavaScript-driven state, or actual mobile viewport was observed. The header, hero, and footer background colors are inferred from the general palette, not from captured selectors for those regions — treat `ink`/`navy-deep` role assignments as best-guess. Button border-radius is contradictory in the source (0px vs. 6px), so the 4px default is a proposed compromise, not a measured value. Type sizes for display/title/caption levels are proposed conventions layered onto the one confirmed font stack (DINWebPro, Verdana, sans-serif) and the one confirmed weight/size pairing (16px/600 on the CTA button); DINWebPro's licensing and availability as a web font were not independently verified beyond the linked `dinwebpro-font.css`. Hover/focus states beyond the primary/secondary/success/alert/warning buttons are unconfirmed. No dealer-locator, cart, or checkout component markup was present in evidence, so those flows are omitted rather than fabricated.
