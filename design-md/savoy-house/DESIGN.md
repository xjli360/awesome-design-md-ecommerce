---
version: alpha
name: "Savoy House"
source_url: "https://savoyhouse.com"
captured_at: "2026-09-29T04:11:23.334907+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Savoy House's supplied stylesheet is a customized Magento Luma theme serving a lighting-fixture
  manufacturer catalog (chandeliers, pendants, ceiling fans, outdoor and wall lights). The observed
  palette is utilitarian: near-black body copy (#333333) on white canvas, light gray surfaces
  (#eeeeee, #f8f8f8, #f5f5f5) for buttons and panels, and a mid-gray hairline (#cccccc) for borders.
  No selector in evidence is explicitly labeled "brand" or "primary," so the interactive accent color
  is inferred from the Magento-default link blue (#1979c3) present in the palette, reused here for
  primary actions and focus states. A small set of saturated colors (#e02b27 red, #1a624f green)
  appear in the raw swatch list without role context; they are mapped as inferred danger/success
  utility colors typical of storefront validation messaging, not confirmed brand accents. Typography
  is anchored to the observed body/button font stack, Open Sans with Helvetica Neue, Helvetica, and
  Arial fallbacks, weight 600 for buttons and headings-in-small-text. Montserrat, present in the raw
  font list but not tied to a body/button selector, is treated as an inferred display-heading
  candidate only. Button radius, padding, and hover/active grays are drawn directly from the
  `.abs-action-link-button` and `button` rules.

colors:
  primary: "#1979c3"
  ink: "#333333"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#757575"
  hairline: "#cccccc"
  surface-soft: "#eeeeee"
  surface-card: "#f8f8f8"
  on-primary: "#ffffff"
  accent-hover: "#e1e1e1"
  accent-active: "#e2e2e2"
  border-soft: "#e4e4e4"
  danger: "#e02b27"
  success: "#1a624f"
  icon-default: "#757575"
  icon-hover: "#494949"
typography:
  display-xl: {fontFamily: "'Montserrat', 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Montserrat', 'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "32px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.3, letterSpacing: "0px"}
  body-md: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.43, letterSpacing: "0px"}
  body-sm: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0px"}
  caption: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "11px", fontWeight: 400, lineHeight: 1.3, letterSpacing: "0.2px"}
  button-md: {fontFamily: "'Open Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: "14px", fontWeight: 600, lineHeight: "16px", letterSpacing: "0px"}
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
    padding: "{spacing.sm} {spacing.lg}"
    hover: "proposed 10% darken of {colors.primary}"
  button-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.lg}"
    hover: "{colors.accent-hover}"
    active: "{colors.accent-active}"
  text-input:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    focusBorder: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.border-soft}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.border-soft}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    linkColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    hairline: "{colors.hairline}"
  badge:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.icon-default}"
    iconHoverColor: "{colors.icon-hover}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  finish-swatch:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "{colors.primary}"
    rounded: "{rounded.full}"
    size: "32px"
    labelTypography: "{typography.caption}"

## Components

**button-primary** anchors primary catalog actions (e.g. "Where To Buy," "Find A Sales Rep"). It reuses the inferred interactive blue as background with white text; no live hover/active state was observed for a filled button, so the darken-on-hover behavior is proposed.

**button-secondary** mirrors the literal `button` and `.abs-action-link-button` rules in evidence: light gray fill (#eee), 1px #ccc border, 3px-observed radius approximated to the `sm` token, with directly observed hover (#e1e1e1) and active (#e2e2e2) backgrounds.

**text-input** is proposed for search and dealer-login forms; only the general body font and hairline border color are observed, so padding, radius, and focus ring are inferred conventions.

**nav-bar** represents the top-level category/utility navigation implied by the page text (Where To Buy, Dealer Portal Login, Catalogs, Designers). Layout and collapse behavior are not observed and are proposed.

**product-card** supports catalog grids of fixtures. Title link color (#333, underline on hover/active) is taken directly from `.product-item-name>a` rules; card padding and border are proposed since no card-container CSS was supplied.

**hero** is a proposed introductory band for homepage/category imagery, using the light gray surface tone and the inferred display typography; no hero-specific selector was present in evidence.

**footer** reflects the sitemap structure in the text excerpt (Information, Resources, Contacts) with muted link coloring and hairline dividers consistent with the observed grayscale palette.

**badge** is proposed for "New," "Sale," or catalog-year callouts (e.g., "2026 New Products"); the red (#e02b27) found in the raw palette is repurposed here as an inferred alert/badge color, not a confirmed brand signal.

**search** is proposed for the site search field, styled with the observed icon colors (#757575 default, #494949 hover) drawn from the luma-icon selectors.

**finish-swatch** is a category-appropriate addition for lighting products, where fixtures are commonly offered in multiple metal finishes; it borrows the hairline border and inferred primary color for the selected state, as no literal swatch selector was present in evidence.

## Responsive Behavior

Recommended, not measured, breakpoints:

| Breakpoint | Width       | Notes                                  |
|-----------|-------------|-----------------------------------------|
| mobile    | 0–599px     | single-column nav, collapsed hamburger  |
| tablet    | 600–1023px  | 2-column product grid, condensed nav    |
| desktop   | 1024–1439px | full nav bar, 3–4 column product grid   |
| wide      | 1440px+     | max-width container, 4+ column grid     |

Touch targets should be at least 40–44px in the mobile range, consistent with the observed button padding scaling up on small screens. Navigation is expected to collapse into a hamburger/drawer pattern below the tablet breakpoint. None of this table reflects measured site behavior; it is a general storefront recommendation.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived solely from static CSS text and a page-text excerpt; no rendered layout, computed styles, JavaScript-driven interactions, or real breakpoints were observed. The primary/accent color is inferred from an unlabeled Magento-default blue in the raw palette and may not reflect Savoy House's actual brand color. Danger/success color roles for #e02b27 and #1a624f are inferred from typical storefront conventions, not confirmed usage. Montserrat's role as a display-heading font is inferred from its presence in the font-family list without a corresponding selector, and its licensing/availability on this domain is unverified. All spacing values, card/hero/nav layouts, hover/focus states beyond the literal button rules, and mobile navigation behavior are proposed patterns, not observed site behavior. The 3px button radius in evidence has been approximated to the nearest token in the fixed rounding scale.
