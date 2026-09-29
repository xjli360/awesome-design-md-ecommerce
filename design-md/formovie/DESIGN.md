---
version: alpha
name: "Formovie"
source_url: "https://formovie.com"
captured_at: "2026-09-28T09:22:40.434171+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is built from Formovie's Shopify theme CSS variables and a
  Judge.me review-widget palette, not from live rendered screenshots. The
  dominant brand blue (#2741d6) anchors primary actions and links, matching the
  Judge.me primary/write-review accent, and is paired with a neutral gray scale
  (#3c3c3c through #fafafa) that forms the theme's --se-gray-* system for text,
  hairlines, and surfaces. A darker slate (#324062) and indigo (#2a3094) appear
  as --se-accent and --se-secondary tokens; their exact UI usage is inferred
  since the source CSS only exposes them as variables without confirmed
  selectors. Status colors (#009a00 success, #feaf07 warning, #e22839 danger)
  and the review-star yellow (#fbcd0a) are explicitly named in the theme and
  widget CSS. Typography relies on observed font-family names in the stylesheet
  cascade — Inter and Nunito Sans, with Arial/Helvetica/sans-serif as system
  fallbacks — but which family renders for headings versus body copy is not
  confirmed from static extraction, so that mapping is marked inferred. Given
  Formovie's projector/Laser-TV catalog, the interpretation favors a clean,
  spec-forward, dark-on-white commerce layout with restrained blue accents for
  CTAs, ratings, and interactive states.

colors:
  primary: "#2741d6"
  ink: "#3c3c3c"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#818181"
  hairline: "#dedede"
  surface-soft: "#f5f5f5"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  accent-slate: "#324062"
  secondary-indigo: "#2a3094"
  success: "#009a00"
  warning: "#feaf07"
  danger: "#e22839"
  star: "#fbcd0a"
  border-strong: "#c2c2c2"
typography:
  display-xl: {fontFamily: "Nunito Sans, Arial, sans-serif", fontSize: "48px", fontWeight: 700, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "Nunito Sans, Arial, sans-serif", fontSize: "32px", fontWeight: 700, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Inter, Arial, sans-serif", fontSize: "22px", fontWeight: 600, lineHeight: 1.25, letterSpacing: "0px"}
  body-md: {fontFamily: "Inter, Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "Inter, Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "Inter, Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.2px"}
  button-md: {fontFamily: "Inter, Arial, sans-serif", fontSize: "15px", fontWeight: 500, lineHeight: 1, letterSpacing: "0.2px"}
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.accent-slate}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
  spec-comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"

## Components

**button-primary** carries Formovie's core blue (#2741d6, matching the Judge.me write-review button color) for cart, checkout, and "Buy now" actions across product tiles. Hover/active/disabled states are proposed, not observed in static CSS.

**button-secondary** is an outline variant for lower-emphasis actions like "Learn more," reusing the primary blue as border/text on a transparent field so it reads as secondary against imagery-heavy hero sections.

**text-input** covers newsletter subscribe fields and account/login forms, using the neutral hairline border and white canvas seen in the theme's gray-scale tokens; focus-ring styling is proposed.

**nav-bar** models the persistent header (cart count, category menu) in white with dark-gray text and a thin hairline underline, consistent with the --se-gray-400 border token; sticky/scroll behavior is not confirmed from the CSS supplied.

**product-card** applies the lightest gray surface (--se-gray-100) as a card background to separate projector/screen tiles from the white page canvas, with an 8px radius as a proposed soft-tech aesthetic fitting hardware photography.

**hero** proposes the light gray (#f5f5f5) banner treatment for promotional sections like "Theater Premium" and Black Friday callouts, using the large display type scale; actual hero background imagery/gradient was not observed.

**footer** uses the darker slate accent (#324062) as an inferred footer/utility background with white text, since this color exists only as a CSS variable without a confirmed selector in the supplied evidence.

**badge** repurposes the review-star/warning yellow (#feaf07/#fbcd0a family) for promotional or rating badges (e.g., discount tags, star ratings), rounded as a pill; exact badge copy and placement are proposed.

**search** is a proposed header search affordance styled with the muted gray surface and mid-gray border, since no dedicated search-input CSS was present in the supplied rules.

**spec-comparison-table** is a category-specific proposed component for projector spec sheets (lumens, resolution, throw ratio), using plain white background and hairline row dividers consistent with the neutral palette; no table-specific brand styling was observed beyond generic Bootstrap-like table resets.

## Responsive Behavior

This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Width | Layout notes (proposed) |
|---|---|---|
| Mobile | <480px | Single-column product cards, stacked nav collapsing to a hamburger/menu icon, full-width buttons |
| Tablet | 480–1024px | 2-column product grid, condensed nav with horizontal category row |
| Desktop | 1024–1440px | 3–4 column product grid, full horizontal nav with dropdowns |
| Wide | >1440px | Max-width content container (proposed ~1280–1440px) with increased hero/section padding |

Touch targets should be at minimum 44×44px for buttons and nav items (proposed, per common accessibility guidance, not site-verified). Navigation is assumed to collapse into a mobile menu below the tablet breakpoint; no actual collapse behavior, animation, or breakpoint values were present in the supplied CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is derived entirely from static CSS variable dumps, a Shopify base stylesheet, and a Judge.me review-widget stylesheet — no rendered page, computed layout, or interaction states were observed. Several colors (accent-slate #324062, secondary-indigo #2a3094) exist only as root-level CSS custom properties without a confirmed selector/usage context, so their component role (footer, accents) is inferred rather than verified. Font-family-to-role mapping (which text uses Inter vs. Nunito Sans vs. Arial fallback) could not be confirmed since `var(--se-body-font-family)` and `var(--se-font-sans-serif)` values were not resolved in the supplied evidence. All spacing, radius, and breakpoint values are proposed conventions, not measured from the live site. Hover, focus, active, and disabled states for buttons/inputs are proposed UI conventions, not observed CSS. Mobile navigation collapse behavior, sticky header behavior, and cart-drawer interactions were not present in the supplied CSS and are therefore not described as verified. Custom font licensing and self-hosting status for Inter/Nunito Sans were not verified from the supplied evidence.
