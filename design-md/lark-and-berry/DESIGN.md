---
version: alpha
name: "Lark & Berry"
source_url: "https://www.larkandberry.com"
captured_at: "2026-09-29T03:59:53.084252+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Lark & Berry presents itself as a London-founded demi-fine/fine jewellery
  house built around lab-grown diamonds, private appointments and modular
  "Studios" for bespoke pieces. The observed CSS exposes a restrained
  editorial palette: near-black ink (#0b0b0b) on a warm off-white paper
  (#f8f8f7), with a cool pale sage (#eceeef) used for section backgrounds
  and a family of mid-greys (#666666, #777777, #999999, #d0d0d0, #dddddd)
  for supporting text, hairlines and disabled/secondary states. A single
  observed deep red (#7a2020) stands out against the neutral field and is
  treated here as an inferred accent for limited-edition or "Icons"
  badging, since its exact role was not confirmed. Typography pairs a
  Cormorant Garamond/Georgia serif — used per the CSS for h1/h2 and
  intro/body-large copy with tight negative tracking — with Poppins/Arial
  as the workhorse sans for body copy, buttons, labels and navigation,
  matching the site's small-caps, letter-spaced micro-labels (7–9px)
  seen on buttons and product captions. The resulting interpretation
  favors generous whitespace, thin 1px hairlines, uppercase tracked
  labels and large serif display type, consistent with a private, made-
  to-order jewellery presentation rather than a high-density retail grid.

colors:
  primary: "#0b0b0b"
  ink: "#0b0b0b"
  canvas: "#f8f8f7"
  body: "#3f4243"
  muted: "#666666"
  muted-2: "#777777"
  hairline: "#dddddd"
  border-strong: "#d0d0d0"
  surface-soft: "#eceeef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-heritage: "#7a2020"
typography:
  display-xl: {fontFamily: "'Cormorant Garamond', Georgia, serif", fontSize: 56px, fontWeight: 400, lineHeight: 1.1, letterSpacing: "-0.055em"}
  display-md: {fontFamily: "'Cormorant Garamond', Georgia, serif", fontSize: 36px, fontWeight: 400, lineHeight: 1.2, letterSpacing: "-0.03em"}
  title-md: {fontFamily: "'Cormorant Garamond', Georgia, serif", fontSize: 28px, fontWeight: 400, lineHeight: 1.25, letterSpacing: "0"}
  body-md: {fontFamily: "'Poppins', Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0"}
  body-sm: {fontFamily: "'Poppins', Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: "0"}
  caption: {fontFamily: "'Poppins', Arial, sans-serif", fontSize: 10px, fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.14em"}
  button-md: {fontFamily: "'Poppins', Arial, sans-serif", fontSize: 9px, fontWeight: 500, lineHeight: 1, letterSpacing: "0.13em"}
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
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted-2}"
    hairline: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-heritage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  studio-card:
    backgroundColor: "{colors.surface-card}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.border-strong}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.base} {spacing.lg}"

## Components

**button-primary** — A solid ink-on-white call-to-action (e.g. "BOOK AN APPOINTMENT", "VIEW ALL JEWELLERY"), matching the observed dark, sharp-edged buttons in the chat and studio CSS. Hover/pressed states are proposed, not observed.

**button-secondary** — An outlined variant for lower-emphasis actions such as "ESSENTIAL ONLY" in the cookie banner, using the same ink color as a border on a transparent field. State transitions are proposed.

**text-input** — A minimal bordered field for the newsletter "Email address" capture and account/search forms, using the hairline border color and body typography; focus and error states are proposed.

**nav-bar** — A slim, light utility bar carrying "UK · GBP £ / SEARCH / ACCOUNT / BAG" style micro-labels in tracked caption type on the paper canvas; sticky/scroll behavior is proposed, not confirmed from static CSS.

**product-card** — A quiet card for jewellery listings (e.g. "Veto Lux Emerald Necklace"), pairing a plain image field with small-caps metadata (collection, price) beneath, consistent with the `.product-info small` and `.product-image>span` rules observed.

**hero** — A full-width introductory panel on the sage/soft surface, combining large serif display copy ("Wear the life you chose.") with a shorter serif subhead, used for landing moments like the homepage and collection intros.

**footer** — A dense, multi-column informational footer (Client Services, Discover, Care & Delivery) on the paper canvas with muted grey link text and hairline dividers, matching the site's long footer link list.

**badge** — A small pill label for scarcity/edition messaging such as "ONLY 5 MADE" or "17 PIECES," using the heritage red as an inferred accent since its production role wasn't directly observed.

**search** — A bordered overlay/field triggered from the nav "SEARCH" label; visual treatment mirrors text-input but is proposed as a distinct component for modal/overlay presentation.

**studio-card** — A category-specific component for the four "Studios" (Ear Styling, Tennis, Statement Earring, Imagination), toggling between a light default state and an ink-filled active state, mirroring the observed `.atelier-steps button.active` pattern.

## Responsive Behavior

| Breakpoint | Approx. width | Layout intent (proposed) |
|---|---|---|
| Mobile | <640px | Single-column stack; hero copy reduces toward display-md scale; nav collapses to icon row. |
| Tablet | 640–1024px | Two-column product grids; studio-card list may wrap to 2×2. |
| Desktop | 1024–1440px | Multi-column footer and product grids as implied by footer link density. |
| Wide | >1440px | Max-width content container with increased side padding (`{spacing.xxl}`+). |

Touch targets should be at least 44px in height for primary buttons despite the compact 8–9px button label type observed, achieved via generous vertical padding. Navigation and filters likely collapse into a drawer or accordion on mobile; this is a recommendation only and was not measured from live responsive behavior.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived from static CSS fragments, a text excerpt and a flat color list, not a rendered or interactive audit of the live site. Component states (hover, focus, active, error, loading) are proposed, not observed, except where a CSS rule explicitly showed a state (e.g. `.atelier-steps button.active`). Exact spacing, breakpoints and rounded-corner values are conventional proposals, since no spacing scale or media-query breakpoints were present in the supplied evidence. The "gold" and "tennis" configurator tokens referenced in the raw CSS (e.g. tennis-specific rose/ice/sapphire hues) were excluded here because their hex values did not appear in the supplied top-level color palette, so they are not represented as design tokens. Font availability, licensing and self-hosting status for Cormorant Garamond and Poppins were not verified. Mobile navigation, cart/bag drawer, checkout flow and search-overlay behavior were not observed and are not described as confirmed patterns.
