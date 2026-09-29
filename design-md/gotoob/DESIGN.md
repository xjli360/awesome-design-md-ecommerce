---
version: alpha
name: "GoToob"
source_url: "https://humangear.com"
captured_at: "2026-09-28T10:08:24.680125+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from humangear.com's Squarespace-hosted stylesheet, which underlies the GoToob travel-bottle line. The observed palette is neutral-forward: near-white canvas (#ffffff), a near-black ink (#111111/#0e0e0e), and a wide grayscale ramp (#f6f6f6 through #333333) used for structure, borders, and secondary text. The one clearly branded accent is a coral-red (#f0523d), observed driving hover/interaction states on tooltip and cookie-banner controls; it is inferred here as the primary call-to-action color since no other saturated hue recurs as consistently. A bright cyan (#00b2ff) and a flat yellow (#ffff00) also appear in the palette and are treated as secondary/utility accents (e.g., informational or highlight badges) rather than primary brand color, since their functional role in the live UI is not evidenced.

  Typography is system-first: Helvetica Neue/Helvetica/Arial with sans-serif fallback is explicitly used for cookie-banner and tooltip copy, and is extended here as the working body/UI font family. "aktiv-grotesk" and "Clarkson" appear in the site's font-family list and are inferred as the template's heading/display faces (Clarkson likely serif-leaning per Squarespace convention); their availability and licensing are not verified from static CSS alone.

  The overall design language proposed is minimal, high-contrast, and utilitarian — consistent with humangear's "civilized gear" positioning — using restrained color, clear hairlines, and generous whitespace.

colors:
  primary: "#f0523d"
  ink: "#111111"
  canvas: "#ffffff"
  body: "#272727"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  deep-ink: "#000000"
  accent-blue: "#00b2ff"
  alert: "#cc0000"
  highlight: "#ffff00"
typography:
  display-xl: {fontFamily: "Clarkson, serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Clarkson, serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "aktiv-grotesk, 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "aktiv-grotesk, 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.6, letterSpacing: 0px}
  body-sm: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0.05em}
  caption: {fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.5em, letterSpacing: 0.05em}
  button-md: {fontFamily: "aktiv-grotesk, 'Helvetica Neue', Helvetica, Arial, sans-serif", fontSize: 11px, fontWeight: 500, lineHeight: 22px, letterSpacing: 0.5px}
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
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.deep-ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.highlight}"
    textColor: "{colors.deep-ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xs} {spacing.md}"

## Components
**button-primary** is the coral (#f0523d) call-to-action, extrapolated from the one observed hover/interactive accent in the stylesheet; used for "Shop," "Add to Cart," and similar high-intent actions.

**button-secondary** is a low-contrast neutral button (light-gray fill, hairline border) proposed for tertiary actions like "Learn More" or filter toggles, keeping the coral reserved for primary intent.

**text-input** follows the minimal-border convention seen in the cookie-banner/tooltip markup — thin hairline border, white fill, no heavy shadow — proposed for newsletter/search fields.

**nav-bar** is a white, top-anchored bar with dark-ink text and a bottom hairline, inferred from the site's "Skip to Content / Shop / Wholesale / Company" menu structure in the page text; exact spacing/collapse behavior is not observed.

**product-card** uses the off-white surface-card tone against a hairline border to lightly separate product tiles (e.g., GoToob+ bottles by size) from the white canvas; title and body typography scale down from display to title-md/body-sm.

**hero** is a full-width, white-background introductory band using display-xl typography for headline statements like "Obsessively designed outdoor & travel products," proposed to match the brand's stated design-forward tone.

**footer** inverts to near-black (#000000/#0e0e0e) with white text, holding secondary navigation (About, Sustainability, Warranty, Patents, Social) per the page-text menu list; this is a proposed dark-footer convention, not a confirmed layout.

**badge** is a small yellow pill (#ffff00 fill, near-black text) proposed for "New," "Limited," or sustainability callouts, since yellow appears in the palette without a confirmed functional role.

**search** is a compact, rounded field styled like text-input but with tighter padding, proposed for a header-level product search affordance.

**size-selector** is the category-specific component: since GoToob bottles ship in multiple sizes, a pill-style toggle group (coral fill on selection, neutral outline otherwise) is proposed for size/variant pickers on product detail pages.

## Responsive Behavior
This is a recommended breakpoint scheme, not measured site behavior:

| Breakpoint | Range | Notes |
|---|---|---|
| mobile | <480px | Single-column stack, nav collapses to hamburger menu, touch targets ≥44px |
| tablet | 480–959px | Two-column product grid, condensed nav |
| desktop | ≥960px | Multi-column grid (3–4 up), full horizontal nav |

Buttons and size-selector pills should maintain a minimum 44×44px touch target on mobile. Nav-bar is proposed to collapse into a slide-out or overlay menu below 960px, consistent with the "Open Menu / Close Menu" labels present in the page text, though the actual mobile interaction pattern was not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
- Evidence is static CSS/text extraction only; no rendered layout, breakpoints, or interaction states (hover, focus, active, disabled) beyond the cookie-banner/tooltip rules were directly observed.
- Semantic color mapping (primary, alert, highlight) is inferred from the limited set of rules where color pairs with function (e.g., hover states); most of the 51-color palette has no confirmed role and may belong to imagery, illustrations, or unrelated template states.
- "Clarkson" and "aktiv-grotesk" are listed in the site's font-family declarations but their weight availability, actual usage location, and licensing/self-hosting status were not verified.
- All typography sizes except button-md (11px, sourced directly from tooltip CSS) and caption/body-sm (12–14px, sourced from cookie-banner CSS) are proposed scale values, not measured from headings or body copy.
- Component definitions (product-card, hero, size-selector, footer, nav-bar) are proposed UI patterns appropriate to a travel-accessories storefront, not confirmed from rendered HTML/DOM.
- Mobile menu, cart drawer, and search interaction behavior are not evidenced and are marked proposed throughout.
