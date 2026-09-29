---
version: alpha
name: "Clek"
source_url: "https://clekinc.com"
captured_at: "2026-09-28T10:15:21.226448+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from a Shopify-hosted storefront (theme "main.css")
  selling infant, convertible, and booster car seats under the Clek brand. The
  observed palette is large and mixed: true brand-authored colors sit alongside
  what appear to be third-party widget colors (a yellow/amber pairing consistent
  with a review-star widget, and payment-brand colors such as PayPal/Amex hues)
  that are excluded here as non-brand noise. Core UI evidence is sparse: buttons
  render with plain black/white/transparent treatments and CSS custom-property
  placeholders (--btn-bg-color) whose resolved values were not captured, so a
  single confident "brand primary" cannot be measured directly. Font evidence is
  concrete for buttons (Futura, sans-serif, 16px) and the broader family list
  (Arial, Futura, Helvetica, Inter, Jost) suggests a geometric display face
  (Futura/Jost) paired with a neutral text face (Inter/Arial) — this pairing is
  inferred, not confirmed for headings/body specifically. The proposed system
  treats a deep, muted blue (#005293) — present in the observed palette and
  consistent with automotive/safety-tech positioning — as the inferred primary
  accent, with near-black and mid-gray neutrals doing most typographic work,
  and warm off-white/soft-gray surfaces for cards and section backgrounds.

colors:
  primary: "#005293"
  ink: "#232323"
  canvas: "#ffffff"
  body: "#4c4c4b"
  muted: "#797874"
  hairline: "#dedede"
  surface-soft: "#f4f6f8"
  surface-card: "#fdfdfa"
  on-primary: "#ffffff"
  accent: "#bf570a"
  success: "#00800a"
  danger: "#d90000"
  border-strong: "#000000"
typography:
  display-xl: {fontFamily: "Futura, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Futura, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Inter, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "Inter, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Inter, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Inter, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Futura, sans-serif", fontSize: 16px, fontWeight: 500, lineHeight: 1em, letterSpacing: 0.5px}
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
    borderColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  compare-table:
    backgroundColor: "{colors.canvas}"
    hairline: "{colors.hairline}"
    headerTypography: "{typography.title-md}"
    cellTypography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

**button-primary**: Primary calls to action ("Shop Now," "Find Your Seat") proposed to use the inferred navy primary with white text, since the captured markup shows only unresolved CSS variables for actual button color. Rounded uses the small radius, echoing the one directly observed `border-radius: 6px` on a `#button` selector.

**button-secondary**: An outline treatment mirrors the observed `.klaviyo-bis-trigger.button` pattern (white background, dark border/text, inverting on hover/focus/active). This is the one button style with concretely observed hover behavior in the evidence.

**text-input**: Proposed field style for search, account, and checkout forms. No input CSS was directly observed; border and padding values are inferred from the surrounding hairline/spacing tokens used elsewhere in the theme.

**nav-bar**: Represents the persistent header implied by page text (Search, Account, Cart, category mega-menu for Infant/Convertible/Booster seats, Compare, Accessories, Support). Layout and sticky behavior are proposed; a `--theme-sticky-header-height` variable was observed, confirming a sticky-header mechanism exists, though its exact styling was not captured.

**product-card**: Used for grid listings (e.g., Foonf, Fllo, Oobr) and the "Quick buy" module referencing sale/regular pricing and color swatches (marshmallow, shadow, snowberry). Card surface uses the warm off-white token; borders use the hairline gray.

**hero**: The homepage hero ("Built to Protect What Matters Most") is proposed as a full-width soft-surface band with large display type, consistent with the promotional carousel implied by "Previous/Next" navigation text.

**footer**: Dark-ink footer with inverted text, holding trust/legal content (warranty, shipping, support links). Structure is inferred; no footer-specific selectors were present in evidence.

**badge**: Proposed for sale/clearance flags and trust callouts ("Lifetime Extended Warranty," "Free Shipping Over $99"), using the accent orange found in the palette to draw attention without competing with the primary blue.

**search**: A lightweight, soft-background search affordance inferred from the header's "Search" text entry; no dedicated search-input CSS was observed.

**compare-table**: A category-appropriate component supporting the site's explicit "Compare Foonf vs Fllo," "Liing vs Liingo," and "Oobr vs Olli vs Ozzi" content — a tabular layout for spec-by-spec car-seat comparison, styled with plain hairline dividers to keep dense safety data legible.

## Responsive Behavior

| Breakpoint | Approx width | Container padding | Notes (proposed) |
|---|---|---|---|
| Mobile | ≤480px | 16px (`--container-pad-x` mobile, observed) | Single-column nav collapses to a menu icon; touch targets ≥44px. |
| Tablet | 481–1023px | 30px (observed) | Two-column product grids; sticky header height variable applies. |
| Desktop | 1024–1439px | 50px (observed) | Full mega-nav; three/four-column product grids. |
| Large | ≥1440px | 60px (observed) | Widened gutters via `--gutter-large`; hero/carousel max-width constrained. |

The `--container-pad-x` and `--gutter` custom properties were directly observed at four step values (16/30/50/60px), confirming a responsive container system exists; the pixel breakpoints mapped to each step above are proposed, not measured. Interactive/touch behavior (menu collapse, swipe carousels, filter drawers) is not observed and should be validated against the live site before implementation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built entirely from static CSS/text extraction; no rendered layout, computed styles, or DOM screenshots were available. Several button styles rely on unresolved CSS custom properties (`--btn-bg-color`, `--btn-border-color`, etc.), so the true primary button color is **inferred**, not confirmed — `#005293` was chosen from the observed palette as the most plausible brand accent. Heading typography (Futura for display, Inter for body) is inferred from the overall font-family list and the one concrete button-font observation; it has not been confirmed on actual `<h1>`–`<h3>` elements. Several palette entries (e.g., `#fcf1cd`/`#dd9a1a`, payment-brand hues like `#ff5f00`/`#1532cb`) appear to belong to third-party widgets (reviews, payment icons) and were deliberately excluded from brand tokens. Spacing/radius scales beyond the observed `--space-unit: 4px` and the single `border-radius: 6px` value are proposed conventions, not measured. Mobile menu behavior, carousel interaction, hover/focus states beyond the one Klaviyo button example, and responsive breakpoint pixel values are not observed. Font licensing/availability for Futura and Jost as web fonts was not verified and should be confirmed before production use.
