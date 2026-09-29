---
version: alpha
name: "Artipoppe"
source_url: "https://artipoppe.com"
captured_at: "2026-09-28T09:22:12.982504+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Artipoppe's public CSS evidence shows a restrained neutral system layered under a generic Bootstrap utility framework. Brand-specific rules are sparse but consistent: a dark charcoal (#32373c) fills solid buttons and file-download links with white text, body copy runs in the Bootstrap default sans-serif stack at #212529 on a white (#ffffff) canvas, and a bordered white hero CTA uses "Avenir Heavy" in uppercase, letter-spaced, 12px type. Product-name labels in the homepage slider use "AvenirM" at 12px/18px with 1px tracking, suggesting Avenir variants are the brand's intended display/label family, with system sans-serif as the safe fallback for body text. Because most of the supplied hex palette originates from Bootstrap's default CSS variables (blue, red, green, yellow, etc.) rather than brand-authored rules, this interpretation treats those saturated colors as framework noise and instead builds the system from the neutral grays and near-blacks that actually appear in themed selectors, extending them into an inferred tonal scale (muted, hairline, surface-soft) appropriate to a minimal, editorial baby-carrier brand. Rounded-full (9999px) buttons are directly observed; other radii and all spacing/breakpoint values are proposed for consistency, not measured.

colors:
  primary: "#32373c"
  ink: "#212529"
  canvas: "#ffffff"
  body: "#212529"
  muted: "#6c757d"
  hairline: "#dee2e6"
  surface-soft: "#f8f9fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  ink-strong: "#000000"
  border-alt: "#ced4da"
  text-secondary: "#495057"
  surface-dark: "#343a40"
typography:
  display-xl: {fontFamily: "'Avenir Heavy', Helvetica, Arial, sans-serif", fontSize: "48px", fontWeight: 600, lineHeight: 1.1, letterSpacing: "-0.5px"}
  display-md: {fontFamily: "'Avenir Heavy', Helvetica, Arial, sans-serif", fontSize: "32px", fontWeight: 500, lineHeight: 1.2, letterSpacing: "0px"}
  title-md: {fontFamily: "'AvenirM', Helvetica, Arial, sans-serif", fontSize: "20px", fontWeight: 500, lineHeight: 1.3, letterSpacing: "0.5px"}
  body-md: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  body-sm: {fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0px"}
  caption: {fontFamily: "'AvenirM', Helvetica, Arial, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.5, letterSpacing: "1px"}
  button-md: {fontFamily: "'Avenir Heavy', Helvetica, Arial, sans-serif", fontSize: "12px", fontWeight: 500, lineHeight: 1.17, letterSpacing: "1px"}
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
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.border-alt}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl} {spacing.lg}"
    border: "1px solid {colors.hairline}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
  carousel-control:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink-strong}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs}"
    border: "none"

## Components

**button-primary** reflects the observed `.wp-block-button__link` rule directly: a solid charcoal (#32373c) pill with white text, fully rounded at 9999px. This is the closest thing to a confirmed brand button pattern in the evidence and is proposed as the primary add-to-cart/CTA style.

**button-secondary** is modeled on the observed `hero-cta` rule — white background, hairline-thin border, uppercase small-caps-style type — used for outline or on-image CTAs where a solid dark button would compete with hero photography. Its square corners (rounded.none) are inferred from the absence of any border-radius in that rule.

**text-input** is a proposed pattern for the search field referenced in the page text ("Search for:"). No input styling was present in the supplied CSS, so border, radius, and padding are inferred from the general neutral system.

**nav-bar** covers the persistent header implied by "Select country and currency," "Go to shopping bag," and the mega-menu category list. Background and text colors are drawn from the observed body defaults; the mega-menu itself (multi-column category submenus) is described only from page-text structure and its visual treatment is not observed.

**product-card** supports the many carrier/collection tiles (Zeitgeist Denim Classic, Argus Oat, etc.). Typography reuses the observed 12px/18px, 500-weight, letter-spaced product-name style from the homepage slider; card chrome (border, padding, radius) is proposed.

**hero** represents the large banner area ("SHOP THE COLLECTION," "FREE WORLDWIDE SHIPPING") pairing a full-bleed canvas background with a bold display headline; exact hero image treatment and overlay are not observed.

**footer** is inferred as a lighter neutral band (surface-soft) holding secondary-weight links such as Shipping & Returns and Contact Us; no footer-specific CSS was supplied.

**badge** proposes a small filled pill for "NEW" labels seen repeatedly in the page text (e.g., "Zeitgeist Arrow Ink NEW NEW"), reusing the primary button color for visual consistency.

**search** is a lightweight variant of text-input for the live-updating search experience described in the page text ("This search updates results as you type").

**carousel-control** models the directly-observed Slick carousel dot pattern (`.slick-dots li button`), used extensively across "FEATURED," "CATEGORIES," and "SHOP BY CATEGORY" carousels; active/inactive opacity (0.75/0.25) is observed, exact dot sizing (20px) is observed, color mapping to ink-strong is inferred since Slick's default is #000.

## Responsive Behavior

This is a proposed breakpoint recommendation, not measured site behavior:

| Breakpoint | Width | Layout guidance |
|---|---|---|
| xs | 0–575px | Single-column stacks; carousels swipe with visible dot controls; nav collapses to a hamburger/mega-menu drawer |
| sm | 576–767px | 2-column product grids; hero CTA remains full-width |
| md | 768–991px | 2–3 column product grids; nav-bar shows primary category labels inline |
| lg | 992–1199px | 3–4 column grids; full mega-menu on hover |
| xl | 1200px+ | Max-width container; 4+ column grids |

Touch targets for buttons and carousel dots should be at least 44×44px regardless of the smaller visual dot size (20px observed). Mega-menu submenus should collapse to accordions under `md`. None of this is confirmed from live rendering.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Extraction is static (CSS + page text only); no rendered layout, hover/focus states, or JS-driven interactions (e.g., live search results, carousel autoplay behavior) were observed.
- The supplied color list is dominated by Bootstrap's default `:root` utility variables (blue, red, green, yellow, teal, etc.); these are framework defaults, not confirmed brand colors, and were deliberately excluded from primary role assignments in favor of the neutral grays actually used in themed selectors.
- "Avenir Heavy" and "AvenirM" are referenced by name in CSS but their licensing, hosting method (self-hosted vs. system), and availability across browsers/devices were not verified.
- All font sizes above 16px (display-xl, display-md, title-md) are proposed for visual hierarchy; only 12px (button/caption) and 16px/1rem (body) sizes are directly evidenced.
- Rounded values beyond the observed `full` (9999px, wp-block-button) are proposed estimates, not measured.
- Spacing scale is a standard proposed system, not derived from measured pixel gaps on the live site.
- Mega-menu, product grid, and footer structures are inferred from page-text hierarchy (e.g., submenu labels) rather than observed DOM/CSS layout rules.
