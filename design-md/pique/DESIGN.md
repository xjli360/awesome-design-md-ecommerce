---
version: alpha
name: "Pique"
source_url: "https://piquelife.com"
captured_at: "2026-09-28T09:26:57.559845+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Pique Life presents as a wellness-and-beauty-forward supplement and tea storefront, and the extracted evidence supports a clinical-clean, editorial aesthetic rather than a rustic tea-shop look. The dominant neutral is a deep navy (#021832), confirmed as the design system's primary text, border, and button color via the site's review-widget CSS custom properties (--oke-text-primaryColor, --oke-border-color, --oke-button-backgroundColor). This pairs against light, near-white canvases (#fafafa, #ffffff) for a airy, apothecary-like field. A single high-saturation lime-chartreuse (#d4e85c) appears explicitly paired with navy text in a promotional rule, and is interpreted here as the brand's signature accent for callouts and highlight bands — consistent with Pique's "radiant"/wellness positioning. A muted blue-gray (#676986) is confirmed for secondary/meta text (review dates, helpful-vote labels) and is mapped to the muted role. Soft mint (#b2f9e9, #e8f4f4) and cream (#f6f1e5) tones are inferred as supporting surface colors for section backgrounds and badges, drawn from the observed palette but not confirmed in layout context. Typography is Proxima Nova (regular/semibold/bold, observed as the primary family, inferred as licensed/self-hosted) with Noto Serif available as an editorial accent face; both fall back to system sans-serif/serif stacks. Sizes below are proposed unless a CSS value (14px button text, 700 button weight) was directly observed.

colors:
  primary: "#021832"
  ink: "#021832"
  body: "#272d45"
  muted: "#676986"
  hairline: "#e5e5e5"
  surface-soft: "#f6f1e5"
  surface-card: "#ffffff"
  on-primary: "#fafafa"
  canvas: "#fafafa"
  accent: "#d4e85c"
  accent-mint: "#b2f9e9"
  accent-info: "#4469af"
  accent-alert: "#c8232c"
  accent-success: "#479a56"
  border-strong: "#d5d8dc"
typography:
  display-xl: {fontFamily: "Proxima Nova, Arial, Helvetica, sans-serif", fontSize: 48px, fontWeight: 600, lineHeight: 1.1, letterSpacing: -0.5px}
  display-md: {fontFamily: "Proxima Nova, Arial, Helvetica, sans-serif", fontSize: 32px, fontWeight: 600, lineHeight: 1.15, letterSpacing: -0.25px}
  title-md: {fontFamily: "Proxima Nova Semibold, Proxima Nova, Arial, sans-serif", fontSize: 22px, fontWeight: 600, lineHeight: 1.25, letterSpacing: 0px}
  body-md: {fontFamily: "Proxima Nova, Arial, Helvetica, sans-serif", fontSize: 16px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  body-sm: {fontFamily: "Proxima Nova, Arial, Helvetica, sans-serif", fontSize: 14px, fontWeight: 400, lineHeight: 1.5, letterSpacing: 0px}
  caption: {fontFamily: "Proxima Nova, Arial, Helvetica, sans-serif", fontSize: 12px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0.2px}
  button-md: {fontFamily: "Proxima Nova Bold, Proxima Nova, Arial, sans-serif", fontSize: 14px, fontWeight: 700, lineHeight: 1, letterSpacing: 0.5px}
  editorial-serif: {fontFamily: "Noto Serif, serif", fontSize: 20px, fontWeight: 400, lineHeight: 1.4, letterSpacing: 0px}
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
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.border-strong}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

**button-primary** uses the confirmed navy background and near-white text pairing pulled directly from the site's review-widget button variables, applied here as the storefront's primary "Add to cart" / "Shop Now" action. Hover/active states are proposed as a slight opacity or shadow shift since no hover CSS was captured beyond the review widget's own box-shadow pattern.

**button-secondary** is an inferred outline variant for lower-emphasis actions ("View All Reviews," "Shop All"), reusing primary navy as an outline and text color on a transparent field to keep the palette restrained.

**text-input** is proposed for quiz/search/newsletter fields, using the near-white card surface with a light hairline border; no live input styling was observed, so padding and radius are conventional defaults.

**nav-bar** reflects the sticky-header behavior implied by the `--use-sticky-header` custom property, styled on the light canvas with navy wordmark/text; exact height and logo sizing are inferred from the `--header-logo-width` values (110–120px) observed in the CSS.

**product-card** models the "Best Sellers" grid items (e.g., Carrara, Sun Goddess Matcha), using a white surface with a hairline border, a semibold title, a muted-color meta line (servings/benefit tags), and price typography — meta color is grounded in the confirmed `#676986` secondary-text token.

**hero** represents the top banner ("A New Breakthrough… No caffeine. No sugar.") on the cream/soft surface, using the largest display type; exact hero imagery and layout were not observed.

**footer** is proposed as a full-navy band with light text, echoing the button system's navy/near-white contrast rather than any directly captured footer CSS.

**badge** covers "Best Seller," "New," and promotional pill labels, using the confirmed lime accent (`#d4e85c`) with navy text, matching the one explicit color pairing found in the evidence.

**search** is a proposed pill-shaped input for site search, styled consistently with the rounded, light-surface language used elsewhere; no search-specific CSS was supplied.

**subscription-toggle** is a category-appropriate component for the "Delivery every 30 days" subscribe-and-save selector seen repeatedly in the product data, toggling between a soft cream default state and a solid-navy active state to signal selection.

## Responsive Behavior

Proposed breakpoints (not measured from live site behavior): mobile ≤599px (single-column product grid, collapsed hamburger nav, sticky "Add to cart" bar), tablet 600–1023px (2-column product grid, condensed nav), desktop ≥1024px (3–4 column grid, full horizontal nav with mega-menu for "Health Benefits"/"Products"). Touch targets should be at least 44px tall for buttons and the subscription-toggle control. Navigation is expected to collapse into a drawer or accordion below tablet width, given the multi-level "Shop Health Benefits / Products / About Us" menu structure implied by the page text. This section is a recommendation based on conventional e-commerce patterns, not observed responsive CSS.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This interpretation is derived entirely from static CSS/text extraction and a third-party review-widget's custom properties, not a rendered or interactive audit of piquelife.com. Several roles are inferred rather than confirmed: `body`, `hairline`, `surface-soft`, `accent-mint`, and `border-strong` are drawn from the observed palette but their in-context usage (backgrounds vs. borders vs. illustration colors) was not directly evidenced. Typographic sizes, weights (aside from the confirmed 700 button weight and 14px default button size), letter-spacing, and line-heights are proposed conventions, not measured values. No hover, focus, error, or loading states were observed beyond the review widget's own hover/active button rules, which were used only as a general interaction reference. Mobile/tablet layout, breakpoint values, grid column counts, and navigation collapse behavior were not observed and are stated as recommendations. Availability and licensing of Proxima Nova and Noto Serif for production use have not been verified. Component structures (hero, footer, search, subscription-toggle) are reconstructed from product/page text content, not from captured layout or component CSS.
