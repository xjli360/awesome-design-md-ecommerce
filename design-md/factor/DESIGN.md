---
version: alpha
name: "Factor"
source_url: "https://factor75.com"
captured_at: "2026-09-28T10:22:16.306491+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Factor's captured CSS confirms a white canvas (#ffffff) with near-black
  body text (#000000) set in plus-jakarta-sans, falling back to Arial
  Black and generic sans-serif. This interpretation treats plus-jakarta-sans
  as the primary UI/display face, since it is the only family explicitly
  declared on the html/body rule; source-sans-pro appears in the supplied
  font list and is proposed as a secondary body/alt-weight face, though its
  exact application (headings vs. copy) is not confirmed by the extracted
  rule and is labeled inferred.

  The observed palette includes a mid-tone green (#206b19) alongside pale
  green tints (#a3d69e, #d1ebce), which are interpreted as Factor's primary
  brand/CTA color and supporting soft-accent tints respectively, consistent
  with a fresh-food, clean-eating positioning implied by the page copy.
  Warm cream neutrals (#f1f1ea, #f9f9f3, #efe9de, #f5efd2) are proposed as
  alternating section/card surfaces against the white canvas. Muted grays
  (#525252, #656565, #adadad, #e0e0e0, #d2d2d2) are assigned to secondary
  text and hairlines. Gold tones (#8c6e00, #6b5400) are inferred as a
  reserved accent for badges or nutrition callouts; no CSS rule confirms
  this specific usage. All color-to-role assignments beyond the literal
  background/color declaration are inferred from palette proportion and
  common e-commerce convention, not from measured component styles.

colors:
  primary: "#206b19"
  ink: "#141414"
  canvas: "#ffffff"
  body: "#000000"
  muted: "#656565"
  hairline: "#e0e0e0"
  surface-soft: "#f9f9f3"
  surface-card: "#efe9de"
  on-primary: "#ffffff"
  accent-green-soft: "#a3d69e"
  accent-green-pale: "#d1ebce"
  accent-gold: "#8c6e00"
  accent-gold-deep: "#6b5400"
  border-strong: "#d2d2d2"
  text-secondary: "#525252"
  overlay-dark: "#00000026"
typography:
  display-xl: {fontFamily: "plus-jakarta-sans, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "plus-jakarta-sans, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "plus-jakarta-sans, sans-serif", fontSize: "24px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0px"}
  body-md: {fontFamily: "plus-jakarta-sans, \"Arial Black\", sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "plus-jakarta-sans, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "source-sans-pro, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "plus-jakarta-sans, sans-serif", fontSize: "16px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0.2px"}
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
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairlineColor: "{colors.hairline}"
    height: "proposed 72px"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base}"
  plan-selector:
    backgroundColor: "{colors.canvas}"
    selectedBorderColor: "{colors.primary}"
    selectedBackground: "{colors.accent-green-pale}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.base} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-green-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components
The **button-primary** uses the observed green (#206b19) as a solid fill with white text, matching the site's repeated "GET STARTED" call-to-action pattern in the page copy; hover/active states are proposed, not observed. **button-secondary** is an outlined variant for lower-emphasis actions (e.g., "Skip or cancel anytime" links), using the same green for border and text on a white ground.

The **nav-bar** is proposed as a white, sticky header holding the extensive menu list seen in the text excerpt (Weekly Menu, Plans, How It Works, etc.); a hairline bottom border separates it from content, though no explicit nav CSS was captured.

The **hero** component pairs the cream surface-soft tone with large display typography for statements like "Let's Eat Real," reflecting the lifestyle-forward copy; exact hero padding and video/background treatment are inferred from layout convention, not measured.

**product-card** represents individual meal tiles (e.g., "Grilled Filet Mignon & Creamy Parmesan Shrimp") on a warm cream card surface with rounded corners, suited to the rotating weekly-menu grid described in the text.

**plan-selector** is a category-specific component for choosing subscription plans or dietary tracks (GLP-1, High Protein, Mediterranean), using a pale-green selected state to visually confirm the active plan; selection interaction is proposed, not observed.

**badge** covers small pills such as "50% Off" or nutrition callouts, using the soft green tint for a light, food-safe accent rather than the deeper primary green.

**search/text-input** are conventional form patterns assumed necessary for account/login and gift-card flows referenced in the nav copy; no form CSS was present in the supplied evidence, so styling is proposed from the neutral palette.

**footer** is inferred as a dark-ink band (using #141414) with white text, a common contrast pattern for closing global navigation (Sustainability, FAQs, Gift Cards) — this treatment is not confirmed by any footer-specific rule in the evidence.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width      | Layout notes (proposed)                    |
|-----------|------------|---------------------------------------------|
| mobile    | <600px     | Single-column stack; nav collapses to menu icon |
| tablet    | 600–1024px | 2-column meal grid; nav remains condensed   |
| desktop   | >1024px    | 3–4 column meal grid; full horizontal nav   |

Touch targets should be at least 44px in height for buttons and plan-selector cards. Navigation collapse (hamburger/menu drawer) at the tablet breakpoint is a common pattern assumption, not confirmed from the extracted CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is built from a single static CSS/text snapshot and cannot confirm true rendered layout, responsive breakpoints, hover/focus/active states, or JavaScript-driven interactions (e.g., plan selection, video hero behavior). Color-to-role mapping (which hex serves as primary CTA vs. badge vs. section background) is inferred from palette proportion and typical meal-delivery site conventions, not from directly observed component-level rules — only the html/body background (#ffffff) and text color (#000000) declarations are directly confirmed. The relative roles of plus-jakarta-sans versus source-sans-pro are inferred, since only plus-jakarta-sans appears in the captured body font-family declaration. All spacing, rounding, and breakpoint values are proposed design-system defaults, not measured pixel values from the live site. Custom font licensing and self-hosted availability for plus-jakarta-sans/source-sans-pro were not verified in this evidence set.
