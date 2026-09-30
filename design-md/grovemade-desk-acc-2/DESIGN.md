---
version: alpha
name: "Grovemade"
slug: grovemade-desk-acc-2
source_url: "https://grovemade.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The primary action color at Grovemade earns its authority through material honesty — the warm amber cluster (#c16508, #ee730a, #904b06) traces directly to the oiled walnut and finished hardwood surfaces the brand machines and sells. Where most workspace-goods stores reach for a cool neutral to signal precision, Grovemade inverts this by making wood-tone amber the sole CTA voltage, so every "Add to Cart" button carries the thermal register of the grain inside the box. This single decision functions simultaneously as brand mark and product promise. The interface rests on a near-white canvas with #ebebeb and #dedede as the only surface treatments, letting photography do the work that a busier design language would assign to illustration or type decoration. Text runs exclusively on the system UI stack — no custom typeface was detected — in weights spanning 300 (display headers) to 600 (material-label uppercase callouts). The light display weight at large sizes (`{typography.display-xl}`, 48px/300) creates an open, airy header register that pairs with full-bleed imagery rather than competing with it. A deep navy (#163959) surfaces in low-frequency zones — footer background, trust-badge iconography, shipping-timeline rails — functioning as the cool-material counterweight to the warm amber action layer without ever rising to a competing primary. The middle blues (#2f7bbf, #62a1d8) belong to link states and secondary informational UI. Product cards at `{rounded.sm}` carry a material-swatch strip of 20px `{rounded.full}` circles at card base — three to four finish options (walnut, maple, felt) displayed as color chips with an amber ring-selection indicator. This swatch mechanic, reproduced consistently across listing and product-detail pages, is the brand's most recognizable UI pattern: it translates the physical customization model (pick your wood, pick your finish) into a repeatable interaction primitive. Gutters between cards run at `{spacing.xl}`, pacing the grid in a way that signals deliberate curation rather than catalog density.

colors:
  primary: "#c16508"
  primary-active: "#904b06"
  primary-disabled: "#f9b169"
  brand-amber: "#ee730a"
  brand-amber-mid: "#f68b1f"
  brand-amber-pale: "#f9b169"
  ink: "#272727"
  body: "#404040"
  muted: "#737373"
  muted-soft: "#bfbfbf"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#ebebeb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-navy: "#163959"
  accent-blue: "#2f7bbf"
  accent-blue-light: "#62a1d8"
  brand-forest: "#516b1d"
  alert-error: "#bd2426"
  alert-error-soft: "#de5052"
  scrim: "#272727"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  material-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.02em
  footer-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
  full: 9999px

spacing:
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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    border: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "4/3"
    imageRounded: "{rounded.xs}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    materialLabelTypography: "{typography.material-label}"
    materialLabelColor: "{colors.muted}"
    hoverShadow: "0 4px 16px rgba(39,39,39,0.08)"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    rounded: "{rounded.none}"
    minHeight: 560px
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
  material-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    gap: "{spacing.xs}"
    tooltipTypography: "{typography.caption}"
    tooltipColor: "{colors.ink}"
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-navy}"
    typography: "{typography.caption}"
    iconColor: "{colors.accent-navy}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.base}"
    border: "none"
  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    buttonColor: "{colors.muted}"
    buttonHoverColor: "{colors.primary}"
    height: 40px
    minWidth: 120px
  product-material-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.material-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.muted}"
    paddingBottom: "{spacing.xxl}"
  swatch-ring-selected:
    outlineColor: "{colors.primary}"
    outlineWidth: 2px
    outlineOffset: 2px
    rounded: "{rounded.full}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerTypography: "{typography.title-md}"
    headerBorder: "1px solid {colors.hairline}"
    itemTypography: "{typography.body-sm}"
    itemPriceTypography: "{typography.price-display}"
    subtotalTypography: "{typography.title-sm}"
    subtotalColor: "{colors.ink}"
    checkoutBackgroundColor: "{colors.primary}"
    checkoutTextColor: "{colors.on-primary}"
    checkoutTypography: "{typography.button-md}"
    checkoutRounded: "{rounded.xs}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.footer-label}"
    headingColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.accent-blue-light}"
    borderTop: "none"
    padding: "{spacing.xxl} 0"
  sale-badge:
    backgroundColor: "{colors.alert-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.material-label}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xxs} {spacing.sm}"

## Components

### Buttons

**`button-primary`** — Flat amber (#c16508) fill with near-square corners (`{rounded.xs}`), uppercase tracked letterforms at 14px/500 weight, and 48px fixed height. Hover and active states darken to #904b06 with no transition delay — the shift is immediate and physical, like pressing a key. Disabled state renders in the pale straw #f9b169 at reduced opacity, keeping the amber family consistent rather than defaulting to a generic gray.

**`button-secondary`** — White canvas with a one-pixel hairline border (`{colors.hairline}`), matching uppercase typography to primary. Used for secondary page-level actions such as "Save for Later" or "Add to Wishlist." Hover fills the interior with `{colors.surface-soft}` without changing the border, signaling interactivity without competing visually with the amber primary.

**`button-ghost`** — Transparent body with amber border and amber text at the smaller `{typography.button-sm}` scale. Appears as a tertiary action on collection grid cards ("View Details") and within product-detail supplementary CTAs. Hover floods with a light amber tint derived from `{colors.brand-amber-pale}`.

### Product Card

The product card is the brand's primary commercial surface — a flat `{rounded.sm}` container on a white ground with a subtle hairline border. Product images run at 4:3 aspect ratio with minimal rounding (`{rounded.xs}`). Below the image, the product title sits in `{typography.title-sm}`, followed by a material descriptor line in `{typography.material-label}` all-caps (e.g. "AMERICAN WALNUT / MAPLE"). Price runs at `{typography.price-display}` in `{colors.ink}`. A horizontal strip of `material-swatch` circles sits at card base, each 20px in diameter, showing available finish options with an amber ring on the selected state. On hover, the card lifts with a gentle shadow (`0 4px 16px rgba(39,39,39,0.08)`) — no background color change, no border intensification, just depth.

### Hero Banner

Full-bleed product photography at minimum 560px height with zero rounding (`{rounded.none}`). Headline runs at `{typography.display-xl}` (48px, weight 300) in `{colors.ink}` over a light `{colors.surface-soft}` panel when a text-on-image layout isn't viable. The single CTA button uses the primary amber style at full 48px height. Subhead copy at `{typography.body-md}` in `{colors.body}` stays under two lines to preserve the open register. No gradient overlays — the photography is presented flat and unfiltered.

### Navigation Bar

64px-tall bar on a white canvas with a bottom hairline. Brand wordmark/logo in `{colors.ink}` anchors left. Nav links at `{typography.nav-link}` (14px, tracked 0.02em) span the center in `{colors.body}`. Utility icons (search, account, cart) sit right-aligned. The active nav category receives no underline or fill — just a subtle weight bump to 500. Cart icon carries a count badge in `{colors.primary}` amber.

### Material Swatch

The swatch is 20px diameter, `{rounded.full}`, presented in a horizontal strip of 3–5 chips. The unselected state has a 2px transparent border; selected state renders a 2px amber ring (`{colors.primary}`) with a 2px offset gap. On mobile, strips of 6+ options scroll horizontally rather than wrapping. A tooltip on hover/long-press shows the material name in `{typography.caption}`.

### Trust Badge

A small informational chip in `{colors.surface-soft}` with `{colors.accent-navy}` icon and text at `{typography.caption}`. Used in a horizontal strip below the product-detail Add-to-Cart block for messages like "Handcrafted in Portland", "Ships in 3–5 Days", and "Free Returns." Navy anchors the informational register, keeping it visually distinct from the amber action layer above.

### Cart Drawer

Slides in from the right at 400px width on desktop with a single left-border hairline. Header row ("Your Cart", X close) at `{typography.title-md}` with a bottom hairline separator. Each line item shows thumbnail, product name at `{typography.body-sm}`, material descriptor at `{typography.material-label}`, and price at `{typography.price-display}`. Quantity selector sits inline per item. Subtotal row in `{typography.title-sm}` above the full-width amber checkout button.

### Footer

Full-width `{colors.accent-navy}` background. Column headers in `{typography.footer-label}` (uppercase, tracked) in `{colors.on-dark}`. Navigation links at `{typography.body-sm}` in `{colors.accent-blue-light}` (#62a1d8) for legibility against navy. Four-column link grid on desktop. Brand mark and tagline centered below the grid rule on the sub-footer row.

### Sale / Promo Badge

A small `{rounded.xs}` chip in `{colors.alert-error}` (#bd2426) rendered over product card images at top-left. Typography at `{typography.material-label}` in white. Used sparingly — the amber CTA layer should remain the dominant color signal on any given page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav drawer, hero stacks text below image, cart becomes full-screen bottom sheet |
| Tablet | 744–1128px | Two-column product grid, condensed nav with dropdowns, hero image at full width with text panel below |
| Desktop | 1128–1440px | Four-column product grid, full horizontal nav bar, hero at 560px min-height with side-by-side text layout |
| Wide | > 1440px | Grid and content max-width capped at 1440px with auto side margins; hero expands to full viewport width |

### Touch Targets

- All primary and secondary buttons fixed at 48px height
- Material swatches 20px with 8px gap; touch area padded to 32×32px minimum per chip
- Quantity selector +/– controls minimum 40×40px tap area
- Nav links in hamburger drawer minimum 48px row height
- Cart drawer close button minimum 44×44px

### Collapsing Strategy

- Product grid: 4 → 2 → 1 columns at Desktop → Tablet → Mobile breakpoints; gutter held at `{spacing.xl}` across all breakpoints
- Navigation: full horizontal bar with dropdowns → icon-row with hamburger on Mobile; search expands to full-width input on Mobile
- Hero: fixed 560px height on Desktop/Wide; auto height with image full-bleed and text block stacked below on Mobile
- Cart drawer: 400px right-panel on Desktop; full-screen bottom sheet with drag-to-dismiss on Mobile
- Material swatch strip: horizontal scroll preferred over wrapping for 6+ options on all breakpoints; two-row wrap as fallback when scroll isn't feasible
- Footer: 4-column link grid → 2-column → single-column accordion with expand/collapse per section on Mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; only system font stacks were present in static extraction. Grovemade may load a custom or licensed typeface via JS or a font delivery service not captured by the crawler. All typography tokens fall back to the system UI stack.
- Site was behind Cloudflare anti-bot protection at extraction time; the full color palette may be incomplete or partially drawn from third-party widget layers (reviews, chat, cookie banners) rather than Grovemade's own design tokens.
- Red entries (#bd2426, #de5052, #521010) and green entries (#9bca3e, #bada7a, #516b1d) in the extracted palette may belong to sale-badge overlays, review-star widgets, or environmental photography rather than the core brand token set — they have been assigned to alert/accent roles accordingly but should be verified against live DOM inspection.
- Exact button border-radius, card shadow values, and nav height are estimated from brand aesthetic knowledge and general DTC conventions, not from live DOM measurement.
- No motion or animation tokens were extractable; hover transition duration and easing for product cards and swatch selection are unspecified.
- Dark mode support is unknown; no dark-mode color variants were detected.
- Mega-menu structure and category taxonomy are unverified due to Cloudflare block.
