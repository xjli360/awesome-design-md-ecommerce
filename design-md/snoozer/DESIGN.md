---
version: alpha
name: "Snoozer"
source_url: "https://snoozerpetproducts.com"
captured_at: "2026-09-28T10:11:56.068043+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Snoozer's site CSS shows a warm, craft-shop palette built around a dark umber
  ink (#3d2e2b) used for both body copy and the Bitter-serif H1, paired with a
  tan/gold CTA color (#c9985f) confirmed on the homepage ".btn" rule and a
  cool sky-blue accent (#5c9ad2) confirmed on price text, cart totals, and
  hover states for search results. Secondary dark surfaces come from WordPress
  default block classes (#32373c button background, #313131 "very dark gray"
  background) and are treated here as inferred footer/secondary-surface
  colors rather than confirmed brand system colors. Neutral grays (#eeeeee,
  #f7f7f7, #dddddd) and warm off-whites (#f4f0ea, #fdfcfa) supply card and
  section backgrounds. Typography pairs Bitter (serif, confirmed on H1 at
  42px/700/capitalize) for display headings with Open Sans (confirmed body
  font at 16px/1.5) for text and UI, both falling back to system sans/serif.
  Button geometry mixes two observed radii — a small 2px radius on the
  homepage CTA and a full 9999px pill on generic WP button blocks — so this
  spec treats pill buttons as the default interactive shape and reserves the
  sharper radius for hero/promo CTAs. Roles for hero background, sale badges,
  and footer treatment are inferred from generic theme/plugin CSS, not
  confirmed brand-specific styling; they should be validated against live
  rendering before production use.

colors:
  primary: "#c9985f"
  ink: "#3d2e2b"
  canvas: "#ffffff"
  body: "#3d2e2b"
  muted: "#666666"
  hairline: "#dddddd"
  surface-soft: "#f4f0ea"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent: "#5c9ad2"
  secondary-dark: "#32373c"
  footer-dark: "#313131"
  cream: "#fdfcfa"
  sale: "#dc3232"
  border-light: "#eeeeee"
typography:
  display-xl: {fontFamily: "'Bitter', Georgia, serif", fontSize: 42px, fontWeight: 700, lineHeight: 1.0, letterSpacing: 0px}
  display-md: {fontFamily: "'Bitter', Georgia, serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.15, letterSpacing: 0px}
  title-md: {fontFamily: "'Bitter', Georgia, serif", fontSize: 22px, fontWeight: 700, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Open Sans', Arial, Helvetica, sans-serif", fontSize: 15px, fontWeight: 600, lineHeight: 1.2, letterSpacing: 0px}
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
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "{colors.secondary-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    hoverColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.border-light}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceColor: "{colors.accent}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-dark}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    textColor: "{colors.ink}"
    resultHoverColor: "{colors.accent}"
    typography: "{typography.body-md}"
  size-selector:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xs} {spacing.md}"

## Components

**button-primary** — Derived from the confirmed `#snoozer-home .btn` rule (tan background `#c9985f`, white text, 2px radius, 15px/600 label). Proposed as the default add-to-cart/hero CTA; hover/active/disabled states are not observed and are proposed only.

**button-secondary** — Based on the generic `.wp-block-button__link` rule (`#32373c` background, white text, full pill radius). Proposed for secondary actions (e.g., "View Details") to visually distinguish from the primary tan CTA.

**text-input** — No dedicated input styling was present in the evidence; border, radius, and padding are proposed using the observed hairline gray (`#dddddd`) and body typography for consistency with surrounding text.

**nav-bar** — Background and text colors are inferred from the site's neutral canvas/ink pairing; the accent hover color (`#5c9ad2`) is confirmed from the `a.view-all-results:hover` rule and reused here for nav-link hover, a proposed extension.

**product-card** — Price color `#5c9ad2` is directly confirmed from `.products-small .product-item .price` and `.price` rules. Card background, border, and radius are proposed, matching the site's general white-card, gray-hairline convention seen in other neutral tokens.

**hero** — Background uses the warm off-white `#f4f0ea` (inferred; present in palette but role unconfirmed) to suit the "hand-sewn," craft-brand tone from the page copy. Heading typography matches the confirmed H1 rule exactly (Bitter, 42px, 700, capitalize).

**footer** — Uses the WordPress "very dark gray" background class (`#313131`) as an inferred footer surface, with white text and the confirmed accent blue for links. Actual footer layout/content was not observed.

**badge** — Sale/promo badge color (`#dc3232`) is present in the extracted palette (commonly a WooCommerce/plugin error or sale-highlight color) and is proposed here for "Sale," "New," or clearance labels referenced in the nav copy (25% Off Sale, Last Chance Sale). Role is inferred, not confirmed as intentional brand styling.

**search** — Styled around the confirmed hover-accent color for `view-all-results`; base input chrome (border, radius, background) is proposed to match the text-input pattern.

**size-selector** — A category-specific component proposed for dog-bed/size-guide selection (referenced in nav as "Snoozer Sizing Guide"), using the primary tan color for the selected state and hairline borders for unselected options. Entirely proposed; no selector markup or states were present in the evidence.

## Responsive Behavior

This is a proposed breakpoint scheme, not measured site behavior:

| Breakpoint | Width       | Notes                                      |
|-----------|-------------|---------------------------------------------|
| mobile    | 0–599px     | Single-column product grid, collapsed nav (hamburger), full-width CTAs |
| tablet    | 600–959px   | 2-column product grid, condensed nav labels |
| desktop   | 960–1279px  | 3–4 column product grid, full horizontal nav with mega-menu (nav depth suggests dropdowns) |
| wide      | 1280px+     | Max-width content container, extra gutter space |

Touch targets should be a minimum 44×44px for buttons and nav links, consistent with the pill-shaped button-secondary geometry. The multi-level navigation implied by the evidence (Dog Cave Beds > Cozy Cave® subcategories) suggests an accordion or mega-menu collapse pattern on mobile, but no such interaction was directly observed and is proposed only.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Evidence is static CSS/text extraction only; no live rendering, computed layout, or DOM structure was observed.
- Several palette colors (e.g., `#dc3232`, `#3b5998`, `#007cba` family) originate from generic WordPress/WooCommerce/social-plugin defaults and may not represent intentional brand decisions; their component roles (badge, footer) are inferred.
- Spacing scale, all radii other than `2px` and `9999px`, and most typography sizes besides the confirmed H1 (42px/700) and body (16px/1.5) are proposed, not measured.
- No hover/focus/active/disabled interaction states were observed for any component; all such states are proposed placeholders.
- Mobile/tablet layout, navigation collapse behavior, and product-grid column counts were not observed and are recommendations only.
- Font licensing and self-hosting/CDN availability for Bitter and Open Sans were not verified from the supplied evidence.
