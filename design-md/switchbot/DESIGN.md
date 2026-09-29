---
version: alpha
name: "SwitchBot"
source_url: "https://switch-bot.com"
captured_at: "2026-09-28T09:23:51.694522+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  This interpretation is drawn from CSS variables and inline rules captured on the SwitchBot International storefront, a Shopify-based smart-home ecommerce site. The clearest brand signal is the red accent (#e0393a), which appears as the Judge.me review primary color, search-button hover state, and hot-badge system, making it a strong candidate for the primary action color. Body copy uses dark neutral grays (#434343, #3c3c3c, #333844) against a white canvas (#ffffff), with a sticky header that switches menu-item color to pure black (#000000) on scroll — an inferred elevated-state treatment. Supporting neutrals (#e5e5e5, #f5f5f5, #f7f8f8) suggest hairline dividers and soft surface fills typical of a dense multi-category product catalog. An amber tone (#feae17) is explicitly used for a "hot" product-showcase badge, so it is retained here as a status/badge color rather than a brand primary. Typography is set in 'Noto Sans' for header/menu contexts per observed declarations; Nunito Sans, Open Sans, and Raleway are present in the font stack but their specific usage context was not captured, so they are treated as secondary/body candidates. All sizing, spacing, and radius values beyond the observed 0px Judge.me radius are proposed defaults suited to a dense smart-home product grid, not measured layout.

colors:
  primary: "#e0393a"
  ink: "#121212"
  canvas: "#ffffff"
  body: "#434343"
  muted: "#919da9"
  hairline: "#e5e5e5"
  surface-soft: "#f5f5f5"
  surface-card: "#f7f8f8"
  on-primary: "#ffffff"
  badge-hot: "#feae17"
  success: "#69ce82"
  info: "#005bd3"
  footer-bg: "#1c1d1f"
  footer-text: "#b9bfca"
  border-strong: "#444444"
typography:
  display-xl: {fontFamily: "'Noto Sans', sans-serif", fontSize: 48px, fontWeight: 700, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "'Noto Sans', sans-serif", fontSize: 32px, fontWeight: 700, lineHeight: 1.2, letterSpacing: -0.25px}
  title-md: {fontFamily: "'Noto Sans', sans-serif", fontSize: 16px, fontWeight: 600, lineHeight: 1.5, letterSpacing: 0px}
  body-md: {fontFamily: "'Open Sans', 'Noto Sans', sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "'Open Sans', 'Noto Sans', sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "'Noto Sans', sans-serif", fontSize: 11px, fontWeight: 400, lineHeight: 1.3, letterSpacing: 0.2px}
  button-md: {fontFamily: "'Noto Sans', sans-serif", fontSize: 14px, fontWeight: 600, lineHeight: 1.3, letterSpacing: 0.2px}
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
    textColor: "{colors.body}"
    borderColor: "{colors.border-strong}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    hairline: "{colors.hairline}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.badge-hot}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.xs}"
  search:
    backgroundColor: "{colors.border-strong}"
    inputBackground: "{colors.canvas}"
    borderColor: "{colors.border-strong}"
    iconColor: "{colors.ink}"
    iconHoverColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    hairline: "{colors.hairline}"
    surfaceSecondary: "{colors.surface-soft}"
    ctaBackground: "{colors.primary}"
    ctaText: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"

## Components
button-primary is proposed as the main add-to-cart / checkout action, using the red observed in the Judge.me review widget and search-hover state as a plausible brand accent, with white text for contrast.

button-secondary is a proposed outline treatment for lower-emphasis actions (e.g., "View All" links seen throughout the category text excerpt), using the dark neutral border and canvas background; hover/active states are not observed and would need site confirmation.

text-input reflects the captured `.header-search__input` rule, which sets a dark border and dark text color; padding and radius are proposed since no box-model values were present in the evidence.

nav-bar is modeled on the sticky-header rules, which explicitly toggle to a white background with black (#000000) link text on scroll — an inferred "elevated" state distinct from the default `#3c3c3c` menu-item color.

product-card is a proposed pattern for the dense catalog structure implied by the page text (many named products per category with "NEW"/"BEST SELLER"/"LAST CHANCE" labels); surface and hairline colors are drawn from the neutral palette, but card geometry is not measured.

hero is proposed to house the "Flash Sale" / "Shop new arrivals" banner text seen in the excerpt, using a soft surface background and the largest display type scale; no hero-specific CSS was captured.

footer uses the darkest palette value (#1c1d1f) against a light gray text tone (#b9bfca) as a plausible dark-footer convention; this pairing is inferred, not confirmed by a captured footer selector.

badge directly reflects the `.menu-tt__product-showcase::before` rule, which renders a lowercase "hot" label in amber (#feae17) on white text — the only unambiguous status-color evidence in the dataset.

search combines the `.header-search` container (dark background) with the `.header-search__button` hover-to-red rule, proposing icon and input treatments consistent with those two captured declarations.

cart-drawer is a proposed, category-appropriate component for a multi-SKU smart-home retailer, using canvas/hairline/surface tokens already evidenced elsewhere on the site; its existence and specific layout are not confirmed in the supplied CSS.

## Responsive Behavior
This is a recommended, non-measured breakpoint scheme suited to a Shopify catalog site: mobile <768px (single-column product grid, collapsed hamburger nav using `.switchbot-header-menu-mb`-style patterns already present in class names), tablet 768–1023px (two-column grid, condensed nav-bar), desktop ≥1024px (full horizontal nav, multi-column grid). Touch targets should be at least 44×44px for cart, search, and nav icons per standard accessibility guidance. The mobile menu should collapse into a full-height scrollable panel, mirroring the `overflow-y: scroll` behavior already declared on `.switchbot-header-menu-mb`. No responsive breakpoints or collapse animations were directly observed in the supplied evidence.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.
This document is derived from static CSS declarations and a page-text excerpt only; no rendered layout, spacing, or interaction states were observed. Semantic color roles (primary, muted, surface-soft/card, footer-bg) are inferred from partial selector context and may not match the site's actual design intent. Several palette entries (e.g., #334fb4, #2332d5, #8051ff, #7967c0, #fa541c, #005bd3, #69ce82) had no clear selector context in the evidence and were either omitted or assigned cautious, clearly-labeled roles. All typography sizes except the observed 16px/600/150% mobile-menu rule are proposed, not measured. Hover, focus, disabled, and error states for buttons/inputs are proposed conventions, not confirmed interactions. Mobile and tablet layouts are not observed and are offered only as standard responsive recommendations. Font availability, licensing, and exact fallback rendering for Noto Sans, Open Sans, Nunito Sans, and Raleway were not verified beyond their presence in the font-family list.
