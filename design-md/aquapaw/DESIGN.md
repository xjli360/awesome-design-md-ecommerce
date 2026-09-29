---
version: alpha
name: "Aquapaw"
source_url: "https://aquapaw.com"
captured_at: "2026-09-29T04:11:27.568117+00:00"
evidence_status: "css_values_observed_roles_inferred"
description: |-
  Aquapaw's storefront CSS centers on a single saturated accent, #00c1ff, applied to the theme's primary `.spr-button` class and unusually also set as the global `html,body` text color — treated here as the brand's signature "aqua" accent used for CTAs and highlight text, not as a literal body-copy color choice for this spec. Supporting neutrals run from near-black (#111111, #222222) through mid grays (#444444, #717171, #cccccc) to light surfaces (#f4f4f4, #f6f6f6, #ffffff), giving a clean, product-photo-forward backdrop typical of a DTC pet-gear shop. Secondary accents appear only in commerce widgets: warm greens (#a1c65b, #4ed14e, #44c767) mark bundle/upsell "add" buttons, while deep red (#8c0000) flags sale pricing and strikethrough comparisons. Headings use Quicksand with Helvetica Neue/sans-serif fallback at weight 500 with slight positive letter-spacing — a rounded, friendly display face fitting a pet-product brand; body copy falls back to plain Arial/Helvetica at 15px with generous 1.6 line-height. No custom font files, breakpoints, or interaction states were present in the supplied evidence, so layout, hover/focus behavior, and responsive rules below are explicitly inferred or proposed, grounded only in the class names and declarations observed (bundle pricing, upsell popups, slideshow markup, satisfaction-guarantee copy).

colors:
  primary: "#00c1ff"
  ink: "#222222"
  canvas: "#ffffff"
  body: "#444444"
  muted: "#717171"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  border-strong: "#cccccc"
  accent-bundle: "#a1c65b"
  accent-success: "#4ed14e"
  accent-upsell: "#44c767"
  accent-sale: "#8c0000"
  accent-badge: "#f3c200"
  accent-alert: "#d02e2e"
typography:
  display-xl: {fontFamily: "Quicksand, Helvetica Neue, sans-serif", fontSize: "48px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.025em"}
  display-md: {fontFamily: "Quicksand, Helvetica Neue, sans-serif", fontSize: "32px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.025em"}
  title-md: {fontFamily: "Quicksand, Helvetica Neue, sans-serif", fontSize: "22px", fontWeight: 500, lineHeight: 1.4, letterSpacing: "0.025em"}
  body-md: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "15px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0.05em"}
  body-sm: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "13px", fontWeight: 400, lineHeight: 1.6, letterSpacing: "0.05em"}
  caption: {fontFamily: "Arial, Helvetica, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.05em"}
  button-md: {fontFamily: "Quicksand, Helvetica Neue, sans-serif", fontSize: "16px", fontWeight: 500, lineHeight: 1.42, letterSpacing: "0.025em"}
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.lg}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl} {spacing.lg}"
  badge:
    backgroundColor: "{colors.accent-badge}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.base}"
  bundle-offer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.accent-sale}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"

## Components

**button-primary** mirrors the theme's `.spr-button` rule: `#00c1ff` fill, white text, square corners (`border-radius:0` observed), Quicksand at weight 500. This is the site's actual primary CTA class and the strongest evidence point in the palette.

**button-secondary** is a proposed outline/ghost variant for lower-emphasis actions (e.g., "About Us", "How-To Install"), using canvas background and primary-colored text since no distinct secondary button class was present in the evidence.

**text-input** is proposed for the header search field and newsletter email capture ("Enter your email"); styling is inferred from generic reset rules only (`color:inherit; font:inherit`), with rounding and padding not measured.

**nav-bar** reflects the observed link set (Shop Now, About Us, Contact, How-To Install, Log in) as plain content order from the page text; visual treatment (canvas background, hairline-free top bar) is proposed, not measured.

**product-card** generalizes the three featured-product blocks (Bathing Tool, Slow Treater, Equine Grooming Tool) into a card pattern with a light surface fill and title-md heading; card chrome (shadow, border) was not present in the CSS and is proposed.

**hero** models the homepage slideshow ("Make Bath Time Happier with Aquapaw", "Shop Now") as a full-width canvas section with a large display headline and primary button; slide mechanics and timing are not observed.

**footer** covers the link list (Home, Blog, Accessibility Statement, Customer Service, Privacy Policy, Terms of Service, Patent Information) plus social icons; background tone (light surface) and text size are proposed defaults, as no footer-specific selector was supplied.

**badge** is a proposed treatment for the "As Seen On SHARK TANK" ribbon and "As Seen In" press strip, using the gold `#f3c200` from the palette as a plausible callout color; no badge component CSS was directly observed.

**bundle-offer** directly reflects observed classes (`.lb-product-bundle`, `.bundle-total`, `.lb-price.regular`, `.add-lion-bundle`): a strikethrough regular price in muted gray, a bold sale total in deep red/brown (`#8c0000`/`#8c1919`), and a green add-to-bundle button (`#a1c65b`) — this is the most concretely evidenced commerce pattern in the source CSS.

**search** proposes a pill-shaped toggle for the header "Search" affordance referenced in the nav text; no dedicated search-input CSS was in evidence.

## Responsive Behavior

Recommendation only — no breakpoints, media queries, or mobile layout were present in the supplied CSS/text evidence.

| Breakpoint | Width       | Nav behavior            | Grid              |
|-----------|-------------|--------------------------|-------------------|
| mobile    | < 480px     | Hamburger/off-canvas menu (site text references "Skip to content Close menu", suggesting a collapsible nav pattern) | 1 column |
| tablet    | 480–1024px  | Collapsed nav or condensed links | 2 columns |
| desktop   | > 1024px    | Full horizontal nav       | 3–4 column product grid |

Touch targets on buttons should be at least 44px tall using `{spacing.md}`–`{spacing.lg}` vertical padding; the existing `.spr-button` hover rule (padding-right increases to reveal an arrow icon) implies a min-width/padding buffer for interactive states even on touch, though tap-specific behavior was not observed.

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

This document is built from static CSS declarations, a page-text excerpt, and a color/font inventory only — no rendered screenshots, computed layout, or DOM structure were available. Several role assignments (ink vs. body, hairline, surface-card vs. surface-soft) are inferred from typical usage of similarly-valued grays and are not confirmed by selector context. The global `html,body { color:#00c1ff }` rule is unusual and was reinterpreted as an accent/primary role rather than literal body text, since surrounding legible-text rules use darker grays. Font availability for Quicksand is assumed via Google Fonts or a similar CDN but was not verified for licensing or self-hosting. All typography sizes except the 15px body value and the button font-size ratio are proposed, not measured. No hover, focus, active, or disabled states beyond the single documented `.spr-button:hover` rule were observed. Mobile menu behavior, slideshow interaction, and modal/upsell popup layout (`.dp-popup-lbModal`) exist in the CSS but their positioning, animation, and breakpoints were not supplied and are therefore undocumented here.
