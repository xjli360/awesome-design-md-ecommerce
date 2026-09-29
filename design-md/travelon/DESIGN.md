---
version: alpha
name: "Travelon"
source_url: "https://travelonbags.com"
captured_at: "2026-09-28T09:30:35.467647+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Travelon's storefront evidence points to a utilitarian, security-focused retail system built on a Bootstrap-derived token set. The root `:root` variables expose a muted primary (#696969), a yellow-green secondary/success pairing (#c4d600, #97d700), and standard Bootstrap state colors (info #17a2b8, warning #ffc107, danger #cc0000/#dc3545) alongside a neutral gray scale (#f8f9fa through #343a40) used for surfaces, borders, and body text (#212529 on #ffffff). The `.btn-primary` rule confirms the muted gray #696969 as the primary action color with white text, a deliberately understated choice suited to a practical travel-goods brand rather than a fashion label.
  Typography is inferred with caution: the global stylesheet imports Dosis via Google Fonts but applies the system sans-serif stack (-apple-system, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans) to body text by rule. Montserrat and Roboto appear in the font list without confirmed selector usage, so headline typography here treats Dosis as a plausible display candidate (inferred role, unverified weight availability) while body/UI text follows the confirmed system stack. This interpretation favors clear hierarchy, generous touch targets, and security/trust badges (RFID, anti-theft) as first-class UI elements, reflecting the site's heavy emphasis on protective product features.

colors:
  primary: "#696969"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  secondary: "#c4d600"
  success: "#97d700"
  info: "#17a2b8"
  warning: "#ffc107"
  danger: "#cc0000"
  danger-alt: "#dc3545"
  accent-blue: "#0070d2"
  border-dark: "#343a40"
  overlay-ink: "#000000"
typography:
  display-xl: {fontFamily: "Dosis, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Dosis, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Montserrat, sans-serif", fontSize: 20px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0px}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
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
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.border-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.ink}"
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
  rfid-badge:
    backgroundColor: "{colors.info}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.md}"

## Components

**button-primary** maps to the confirmed `.btn-primary` rule: a muted gray (#696969) fill with white text and a subtle 0.1875rem radius (approximated here to the sm token). This is the strongest directly observed component in the evidence.

**button-secondary** is a proposed outline variant using the same primary gray for border and text on a transparent background, intended for secondary CTAs like "Learn More" or "View Details" — not directly observed but consistent with Bootstrap `.btn` conventions present in the CSS.

**text-input** is a proposed form-field pattern using the Bootstrap-standard hairline gray (#dee2e6) border and white canvas background seen throughout the neutral palette; used for search boxes, newsletter signup, and account forms.

**nav-bar** is inferred from the extensive mega-menu category list (Anti-Theft, RFID Bags, Passport Organizers, etc.) implying a multi-level dropdown navigation on white background with hairline dividers; exact layout is not measured from static CSS.

**product-card** is proposed for the "Discover real RFID travel wallets" and "Pull-Up Passport Holder" grid callouts referenced in page text; uses card surface white, hairline border, and title-md typography for product names.

**hero** is proposed for the homepage banner area ("FALL 2026 FASHION TRENDS", "5-Point Anti-Theft Explained") using the soft gray surface and display-xl heading type; exact hero styling was not present in supplied CSS rules.

**footer** is inferred from the dense footer link list (About, Process & Policy, Connect With Us) and uses the dark gray-900 tone (#343a40) as a plausible footer background for contrast, though this specific background-color assignment was not confirmed in the supplied selectors.

**badge** is proposed for merchandising flags (e.g., "Sale," "Best Sellers") using the secondary yellow-green (#c4d600) pulled from the `:root` variables, pill-shaped per the full-radius token.

**rfid-badge** is a category-appropriate proposed component for labeling RFID-blocking products (a core Travelon feature per "RFID Blocking" and "Will my RFID blocking product set off airport security" copy), using the info teal (#17a2b8) to visually distinguish security/tech callouts from general merchandising badges.

## Responsive Behavior
This is a recommendation, not measured site behavior; no responsive CSS rules or breakpoints beyond Bootstrap defaults were present in supplied evidence.

| Breakpoint | Width | Layout Notes (proposed) |
|---|---|---|
| xs | 0–543px | Single-column stack, hamburger nav, full-width cards |
| sm | 544–834px | Matches `--breakpoint-sm` token; 2-column product grid |
| md | 835–991px | Matches `--breakpoint-md` token; mega-menu collapses to accordion |
| lg | 992–1199px | Matches `--breakpoint-lg` token; horizontal nav bar visible |
| xl | 1200px+ | Matches `--breakpoint-xl` token; max-width contained layout |

Touch targets for buttons and nav items should be at least 44×44px (proposed, not observed). Mega-menu category lists should collapse into an accordion or drawer below `md` given the large number of listed subcategories.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS variables, a single global stylesheet excerpt, and page text — no rendered layout, computed styles, or interaction states were observed. Dosis is imported via `@import` but no selector confirms its applied usage; its role as display typography is inferred, not verified, and font weight/style availability from Google Fonts was not checked. Montserrat and Roboto appear only in the supplied font-family list without a matching selector, so their assigned roles (title-md, unused body fallback) are speculative. The `rounded.sm` (4px) token approximates but does not exactly match the observed `.btn` radius of 0.1875rem (3px). Hero, footer, product-card, nav-bar, search, and badge components are structurally proposed from page-text content and generic e-commerce/Bootstrap conventions, not from confirmed layout CSS. No hover, focus, active, or error states were present in the supplied rules beyond `.btn:hover` and table hover/striping, so most interactive states above are proposed. Mobile menu behavior, breakpoint-specific layout shifts, and actual grid structure were not observed and are recommendations only. No licensing or self-hosting confirmation exists for Dosis or Montserrat.
