---
version: alpha
name: "Elliott Bay Book Company"
source_url: "https://www.elliottbaybook.com"
captured_at: "2026-09-28T10:11:07.664940+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  This interpretation is drawn from a production React/Ant Design bundle rather than
  from custom brand styling — the site is built on the Ant Design component library
  (evident from .ant-picker, .ant-radio-button-wrapper rules and Ant's default palette
  tokens such as #1890ff, #52c41a, #faad14). Because Ant Design ships its own defaults,
  those saturated utility colors are treated here as framework artifacts, not brand
  signals, and are excluded from the semantic palette below. Instead the interpretation
  favors the neutral grayscale (#ffffff, #f5f5f5, #d9d9d9, #333333, #0d0d0d) that forms
  the actual body chrome, plus a small set of deeper, book-trade-appropriate hues —
  forest green (#154532), deep teal (#1b4b59) and a warm cream (#f2eddd) — pulled from
  the observed palette to stand in for an inferred shop identity (unverified against a
  live screenshot).
  Typography is limited strictly to font-family names present in the evidence. Body
  copy uses the system-font stack found on the `body` and `.internal,body` selectors
  (-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen, Ubuntu, Cantarell, Fira
  Sans, Droid Sans, Helvetica Neue, sans-serif). "Brown" and "Poppins" also appear
  repeatedly in the font-family evidence (including weighted variants), so they are
  proposed — as inferred, unverified-license choices — for display and title roles
  respectively, each falling back to the same observed system stack.

colors:
  primary: "#154532"
  secondary: "#1b4b59"
  accent: "#c20232"
  ink: "#0d0d0d"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#d9d9d9"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  surface-warm: "#f2eddd"
  on-primary: "#ffffff"
typography:
  display-xl: {fontFamily: "Brown, -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Brown, -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 32px, fontWeight: 500, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5715, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Poppins, -apple-system, BlinkMacSystemFont, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.5715, letterSpacing: 0.2px}
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
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hairline: "{colors.hairline}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
    accentColor: "{colors.accent}"
  hero:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
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
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  event-listing:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    dateAccent: "{colors.secondary}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"

## Components
**button-primary** — the primary call-to-action (e.g. "Add to cart," "RSVP for event") uses the deep forest-green fill inferred as the shop's brand tone, with white text and a modest 4px radius consistent with Ant Design's default control rounding. Hover/pressed states are proposed, not observed.

**button-secondary** — an outlined variant for lower-priority actions (e.g. "View details"), sharing the primary's radius and type scale but with a transparent fill and green border/text, proposed for visual hierarchy.

**text-input** — modeled on Ant Design's default form field styling (light border, 4px-ish radius, inherited font), used for search boxes and newsletter/account forms; focus-ring treatment is proposed, not observed.

**nav-bar** — a white top bar carrying the store wordmark and primary navigation (Books, Events, Cafe, Gift Cards). Divider from page content is proposed via the observed hairline gray; sticky/scroll behavior is not observed.

**product-card** — a book-listing card on an off-white surface with a thin hairline border and 8px radius, pairing a Poppins-based title with a smaller body-sm price line; the accent red is reserved for sale/badge callouts, proposed rather than confirmed from a live grid.

**hero** — a large introductory band using the cream/warm surface tone as a proposed departure from pure white, intended to evoke a print/paper feel appropriate to an independent bookstore; large display type anchors the "since 1973" framing from the page copy.

**footer** — a dark ink-colored band closing the page, carrying store hours, address and social links in small body-sm type on white text; column layout is proposed, not observed.

**badge** — a compact pill for labels such as "Signed," "New," or "Staff Pick," using the accent red fill with a fully rounded shape; this is a proposed pattern inferred from the presence of a saturated red in the palette, not a confirmed UI element.

**search** — a search field styled with the light gray surface tone and hairline border, intended for the catalog search bar referenced by the "150,000 titles" copy; icon placement and autocomplete behavior are not observed.

**event-listing** — a bookstore-specific component for the frequent author events mentioned in the page text: a card with a teal date accent, event title in title-md, and description in body-md; this pattern is proposed to match the site's stated emphasis on events, not confirmed from markup.

## Responsive Behavior
Recommended (not measured) breakpoints:

| Breakpoint | Width | Notes |
|---|---|---|
| mobile | <600px | single-column nav collapses to a hamburger/drawer; product-card grid becomes 1–2 columns |
| tablet | 600–1024px | 2–3 column product grid; nav-bar remains horizontal with condensed spacing |
| desktop | 1024–1440px | full nav-bar, 3–4 column grids, hero at full padding |
| wide | >1440px | max-width content container, generous section spacing |

Touch targets should be at least 44×44px for primary/secondary buttons and search controls. Navigation and filter panels are recommended to collapse into an off-canvas drawer below the tablet breakpoint. None of this is derived from observed responsive CSS; it is a standard proposal for a bookstore catalog layout.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.



- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is generated from static CSS/text evidence only — no rendered screenshots, computed styles, or interaction states were captured. The bulk of the supplied CSS originates from Ant Design's default component library and Leaflet (a map plugin), not brand-authored styling, so the semantic color/typography mapping above (primary, accent, hero, event-listing, etc.) is an inferred interpretation layered onto neutral/system values, not a confirmed brand system. "Brown" and "Poppins," used for display and title typography, appear in the font-family evidence but their licensing, actual weight availability, and rendering on the live site are unverified. All spacing, radius, breakpoint, and component-state values (hover, focus, active, disabled) are proposed conventions, not measured from the site. The presence of react-rendered content behind a "You need to enable JavaScript" notice further limits how much of the live storefront's actual visual structure could be captured statically.
