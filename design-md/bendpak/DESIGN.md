---
version: alpha
name: "BendPak"
source_url: "https://bendpak.com"
captured_at: "2026-09-28T09:44:44.079457+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The observed palette centers on a dark navy, "#152d45", which recurs across
  multiple opacity variants ("#152d4599", "#152d454d", "#152d4533", "#152d4566",
  "#152d45cc"), suggesting it functions as a primary brand surface and overlay
  color for header, footer, and hero treatments. A bright yellow, "#ffde17"
  (paired with a near-identical "#ffd600"), appears alongside promotional copy
  ("SHOP NOW", rebate banners) and is interpreted here as the high-visibility
  accent for primary calls to action, consistent with industrial/safety
  signage conventions. Body text relies on a neutral gray scale ("#333333",
  "#666666") on white and light-gray surfaces ("#f0f2f4", "#f9f9f9",
  "#e5e5e5"), with red ("#c5221f") and green ("#188038") reserved for
  alert/success states inferred from adjacent light tint pairs in the palette
  (e.g. "#f8d7da", "#edf7f0").

  Typography is rooted in a system-font stack (system-ui, -apple-system,
  Segoe UI, Roboto, etc.) confirmed on body/reset rules, while "Host Grotesk",
  "Inter", "Outfit", and "Space Grotesk" appear in the site's font list and are
  inferred, not confirmed by direct selector evidence, to serve heading and UI
  roles via CSS custom properties (--font-body, --font-ui). The interpretation
  favors a confident, engineering-grade tone: squared surfaces, wide-tracked
  semibold button labels (observed on .hs-button), and navy/yellow contrast
  echoing workshop equipment branding.

colors:
  primary: "#152d45"
  accent: "#ffde17"
  ink: "#121c26"
  canvas: "#ffffff"
  body: "#333333"
  muted: "#666666"
  hairline: "#e5e5e5"
  surface-soft: "#f0f2f4"
  surface-card: "#f9f9f9"
  on-primary: "#ffffff"
  on-accent: "#121c26"
  danger: "#c5221f"
  success: "#188038"
  border: "#cccccc"
typography:
  display-xl: {fontFamily: "Space Grotesk, system-ui, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Space Grotesk, system-ui, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Outfit, system-ui, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Host Grotesk, Inter, system-ui, -apple-system, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Host Grotesk, Inter, system-ui, -apple-system, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Host Grotesk, Inter, system-ui, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Inter, system-ui, sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.1, letterSpacing: 1.2px}
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
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
    hairline: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    hairline: "{colors.primary}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
    typography: "{typography.body-md}"
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    accentColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"

## Components

**button-primary** uses the yellow accent as a high-visibility call-to-action fill, consistent with promotional banner copy ("SHOP NOW", rebate messaging). Wide letter-spacing and semibold weight on button labels are proposed from the observed `.hs-button` tracking-widest/font-semibold rules. Hover/active states are not observed and are marked proposed.

**button-secondary** inverts to the navy primary fill for lower-emphasis actions (e.g. "SEE MORE" category links), keeping the same button typography for consistency; border and hover states are proposed, not measured.

**text-input** assumes a plain white field with a light gray border, reflecting the reset rule that removes default border-radius on form elements; focus-ring styling is not observed and is proposed.

**nav-bar** is modeled on the dark navy header implied by the brand's primary color and the deep mega-menu of shop/brand/solutions links in the page text; sticky behavior and dropdown mechanics are not observed.

**product-card** is a proposed pattern for lift/equipment listings (e.g. 2-Post Lifts, Wheel Service), using the light card surface and hairline border for grouping; actual card markup was not present in the supplied CSS.

**hero** reflects the large banner text ("ENGINEERED FOR PERFORMANCE. DESIGNED FOR SAFETY.") sitting on a dark navy field, inferred from the primary color's prevalence and typical automotive-hero conventions; exact hero dimensions are not measured.

**footer** is proposed as a darker-than-primary ink block for legal/utility links (Support, Company, Offers), separated by a thin navy hairline; this structure is inferred from the long footer link list in the page text, not from footer-specific CSS.

**badge** supports short labels like "ALI CERTIFIED" using the accent yellow in a pill shape; this is a proposed treatment for certification/safety marks referenced in the copy, not an observed badge component.

**search** models the header "SEARCH ×" overlay control with a simple bordered field; overlay animation and result styling are not observed.

**spec-callout** is a category-appropriate proposed component for highlighting engineering/safety claims (ALI Certified, ASARS™ Automatic Swing Arm Restraint System) on a soft navy-tinted surface, distinct from marketing product cards, to visually separate technical trust signals.

## Responsive Behavior

The following breakpoints are a recommendation, not measured site behavior:

| Breakpoint | Width | Notes |
|---|---|---|
| sm | 0–639px | Single-column stacks; nav collapses to a hamburger/menu icon; hero text reduces toward `{typography.display-md}`. |
| md | 640–1023px | Two-column product grids; mega-menu categories condense into accordions. |
| lg | 1024–1279px | Full multi-column category grids; nav-bar shows top-level items with hover dropdowns. |
| xl | 1280px+ | Max-width content container; hero uses `{typography.display-xl}`. |

Touch targets should be at minimum 44×44px for nav links, search trigger, and cart/account icons given the icon-heavy header (CART, SEARCH, Sign in). Mega-menu categories (Shop, Brands, Solutions, Discover, Resources, Company, Support) should collapse into an accordion or drawer below the `md` breakpoint. None of this is confirmed by observed layout CSS.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.







- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- This document is derived from static CSS/text extraction only; no rendered layout, computed styles, or JavaScript-driven interactions were observed.
- The mapping of `--font-body` and `--font-ui` custom properties to specific families ("Host Grotesk", "Inter", "Outfit", "Space Grotesk") is inferred from the site's font list, not from a direct declaration pairing variable to value.
- All font sizes, line-heights, and letter-spacing values except the button tracking/weight are proposed defaults, not measured from the source CSS.
- Rounded and spacing scales are proposed conventions; no border-radius or spacing custom properties were present in the supplied evidence beyond the reset's `border-radius:0` on form controls.
- Component states (hover, focus, active, disabled, error) are proposed and unverified.
- Mobile/responsive layout behavior, breakpoint values, and menu collapse mechanics were not present in the supplied CSS and are marked as recommendations only.
- Custom font licensing/self-hosting for "Host Grotesk", "Space Grotesk", or "Outfit" was not verified; availability depends on the site's actual font-loading configuration, which was not confirmed in this evidence set.
- Color role assignments (e.g. yellow as CTA, navy as primary) are semantic inferences based on usage context in the page copy, not confirmed via computed background/foreground CSS on live elements.
