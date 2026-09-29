---
version: alpha
name: "HelloFresh"
source_url: "https://hellofresh.com"
captured_at: "2026-09-28T09:47:17.846893+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from a single captured stylesheet and page-text excerpt for hellofresh.com's US marketing homepage, not from a full design audit. The only concretely observed rule sets html/body typography to agrandir-tight-bold with Verdana, Geneva, sans-serif fallbacks, 16px size, 400 weight, and a near-black #242424 body color on a white canvas. The supplied palette otherwise reads as a warm, food-forward neutral system (cream #faf8f3, warm taupe #e0d9cb/#d3cab7/#efe9de) paired with a saturated brand green (#009645) and a darker forest green (#02451d), plus incidental accent tones (#ffcf70, #96dc16, #732429, #7d7561) that likely mark diet-plan badges or illustrative UI rather than primary chrome. Because no heading-specific CSS rule was captured, the use of agrandir-tight-black for display type is inferred from the font-family list alone, not confirmed from a matched selector. Roboto appears in the family list but its application is unobserved, so it is assigned here only to smaller supporting text as a reasonable, clearly-labeled inference. The resulting system favors a warm, editorial food-brand feel: cream and taupe surfaces, high-contrast near-black ink, and brand green as the primary call-to-action color, consistent with the subscription meal-kit content described in the page text.

colors:
  primary: "#009645"
  ink: "#242424"
  canvas: "#ffffff"
  body: "#4b4b4b"
  muted: "#656565"
  hairline: "#e0e0e0"
  surface-soft: "#faf8f3"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  accent-forest: "#02451d"
  accent-gold: "#ffcf70"
  accent-lime: "#96dc16"
  accent-maroon: "#732429"
  accent-olive: "#7d7561"
  surface-warm: "#e0d9cb"
  surface-warm-alt: "#efe9de"
  border-warm: "#d3cab7"
  overlay-scrim: "#00000026"
typography:
  display-xl: {fontFamily: "agrandir-tight-black, Verdana, Geneva, sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "agrandir-tight-black, Verdana, Geneva, sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "agrandir-tight-bold, Verdana, Geneva, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "agrandir-tight-bold, Verdana, Geneva, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "roboto, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "roboto, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "agrandir-tight-bold, Verdana, Geneva, sans-serif", fontSize: 16px, fontWeight: 700, lineHeight: 1.2, letterSpacing: 0.3px}
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
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
  plan-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-warm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-sm}"

## Components

**button-primary** is proposed as the brand-green, pill-shaped call-to-action used for phrases like "See Pricing & Plans" seen repeatedly in the page text; rounding and pill shape are inferred conventions for a subscription-signup flow, not measured from CSS.

**button-secondary** provides an outlined alternative for lower-emphasis actions (e.g. "Log in," "View Menu"); its hairline border and transparent fill are proposed to sit quietly beside the primary green button.

**text-input** covers signup/zip-code entry fields implied by a subscription checkout flow; background, border, and padding are proposed defaults using the observed hairline and canvas colors, with no input styling actually captured.

**nav-bar** represents the persistent top navigation implied by the large menu list ("Our Plans," "Our Menus," "Sustainability," etc.); a white background with hairline underline is proposed since no header-specific rule was supplied.

**plan-card** is a category-appropriate component for the diet/plan tiles referenced in the text (Meat & Veggies, Veggie & Plant-Based, Calorie Smart, High Protein, etc.), using the warm surface and border tones from the palette to differentiate each plan option; this pattern is proposed, not observed in markup.

**hero** models the large landing banner ("Take Back Dinnertime!") using the cream surface-soft background and display-xl type; exact hero layout, image treatment, and spacing are inferred.

**footer** is proposed as a dark, ink-colored band for legal/help links, contrasting with the light body of the page; this inverts the primary ink/canvas relationship and is not confirmed by captured CSS.

**badge** covers small labels such as calorie counts ("650KCal OR LESS") or plan tags ("MOST POPULAR"); the gold accent is chosen from the observed palette to draw attention without introducing a new hue, but its actual application is unverified.

**search** is included as a category-appropriate utility (e.g., searching recipes) using the same rounded, muted styling family as inputs; no evidence confirms a search UI exists on this page.

## Responsive Behavior

Recommended, not measured, breakpoints: mobile up to 599px (single-column stacked hero and plan cards, nav collapsed to a hamburger menu), tablet 600–1023px (two-column plan grid, condensed nav), desktop 1024px+ (full multi-item nav, three-to-four column plan grid). Touch targets should be at least 44px tall for buttons and nav items; collapse secondary nav links ("Sustainability," "Partnerships") into an overflow or hamburger menu below tablet width. These are proposed conventions for a meal-kit marketing site and were not derived from observed responsive CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from one static HTML/CSS snapshot and a text excerpt, not a rendered or interactive audit: only a single CSS rule (html/body) was actually supplied, so all component styling beyond that rule is proposed/inferred rather than observed. The mapping of agrandir-tight-black to headings is inferred purely from its presence in the font-family list, not from a matched selector, and roboto's supporting-text role is similarly assumed. Hover, focus, active, error, and loading states for buttons, inputs, and cards are not observed and are marked proposed by omission of any state-specific values. Mobile/tablet layout, breakpoint values, and collapse behavior are recommendations only, not measured from responsive CSS or viewport testing. Licensing and availability of the agrandir-tight-black/agrandir-tight-bold custom fonts were not verified; system fallbacks (Verdana, Geneva, Arial, Helvetica, sans-serif) should be assumed until confirmed.
