---
version: alpha
name: "Chase Bliss"
source_url: "https://www.chasebliss.com/"
captured_at: "2026-09-29T04:11:59.244291+00:00"
evidence_status: "css_values_observed_roles_inferred"
quality_tier: "css_reference"
usage_scope: "style_reference_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Chase Bliss is a Squarespace-built storefront for a boutique guitar-pedal
  maker (PEDALS, CHOMPI, UTILITY, MERCH), and the supplied CSS evidence comes
  primarily from the site's newsletter popup-overlay module. That module shows
  a clear pattern: Squarespace's default Helvetica Neue/Arial stack is
  declared first and then overridden by Poppins for the rendered heading,
  body, and button styles, so Poppins is treated here as the working type
  family with Helvetica Neue/Arial as historical fallback. Baskerville and
  Clarkson appear in the site's font-family list but never inside a captured
  rule, so their role is unconfirmed and excluded from typography tokens.
  The observed color set mixes true site neutrals (near-black #1f1f1f used
  for solid-button fill and outline strokes, white button text, warm
  off-whites like #fefbf6/#fffdfa, and mid grays for hairlines/muted text)
  with a long run of recognizable third-party social-icon colors (YouTube
  red, Instagram pink, Facebook/Twitter blue, Discord purple, TikTok,
  Bandcamp, Soundcloud). Those social colors are excluded from brand tokens.
  #f0523d is the one saturated, non-social hue in the palette and is
  interpreted (inferred) as an accent for badges, links, or highlight
  moments, fitting a "deep and playful effects" brand voice. All layout,
  spacing, and radius values below are proposed conventions, not measured.

colors:
  primary: "#1f1f1f"
  accent: "#f0523d"
  ink: "#000000"
  canvas: "#ffffff"
  body: "#1f1f1f"
  muted: "#a9a9a9"
  hairline: "#dddddd"
  surface-soft: "#f6f6f6"
  surface-card: "#fefbf6"
  surface-cream: "#fffdfa"
  surface-dark: "#0e0e0e"
  line: "#e7e7e7"
  on-primary: "#ffffff"
  hover-dark: "#262626"
  shadow-line: "#454545"
typography:
  display-xl: {fontFamily: "Poppins, 'Helvetica Neue', Arial, sans-serif", fontSize: "36px", fontWeight: 600, lineHeight: 1.0, letterSpacing: "0em"}
  display-md: {fontFamily: "Poppins, 'Helvetica Neue', Arial, sans-serif", fontSize: "28px", fontWeight: 600, lineHeight: 1.15, letterSpacing: "-0.25px"}
  title-md: {fontFamily: "Poppins, 'Helvetica Neue', Arial, sans-serif", fontSize: "20px", fontWeight: 600, lineHeight: 1.2, letterSpacing: "0em"}
  body-md: {fontFamily: "Poppins, 'Helvetica Neue', Arial, sans-serif", fontSize: "16px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.015em"}
  body-sm: {fontFamily: "Poppins, 'Helvetica Neue', Arial, sans-serif", fontSize: "14px", fontWeight: 400, lineHeight: 1.5, letterSpacing: "0.01em"}
  caption: {fontFamily: "Poppins, 'Helvetica Neue', Arial, sans-serif", fontSize: "12px", fontWeight: 400, lineHeight: 1.4, letterSpacing: "0.02em"}
  button-md: {fontFamily: "Poppins, 'Helvetica Neue', Arial, sans-serif", fontSize: "15px", fontWeight: 500, lineHeight: 1.0, letterSpacing: "0.05em"}
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
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    hairline: "{colors.line}"
    padding: "{spacing.base} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.body-md}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    hairline: "{colors.shadow-line}"
    padding: "{spacing.xxl} {spacing.xl}"
  badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xxs} {spacing.sm}"
  search:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "{spacing.sm} {spacing.base}"
  artist-demo-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    accentColor: "{colors.accent}"

## Components

**button-primary** mirrors the popup's solid-style CTA, which is the only fully confirmed interactive style in the evidence: `#1f1f1f` fill with white text, no border, uppercase-free Poppins label at 15px/500. Proposed for "Add to Cart" and primary checkout actions.

**button-secondary** follows the popup's outline-style button — transparent fill, `#1f1f1f` text and 2px border, with the observed hover state inverting to a dark fill. Proposed for "Learn More" or secondary product actions; the exact non-popup hover colors are not confirmed.

**text-input** is proposed from the newsletter form's input context (visible submit styling implies an adjacent field). Card-warm background, thin hairline border, and body typography are inferred conventions for email/search fields, not directly measured.

**nav-bar** is a proposed pattern for the top navigation (PEDALS, CHOMPI, UTILITY, MERCH, SUPPORT, ABOUT) inferred from the page-text structure; no nav CSS was captured, so background, spacing, and sizing are conventional Squarespace-header defaults, not observed.

**product-card** is proposed for pedal listing/grid pages. It borrows the warm card surface (`#fefbf6`) and hairline border from the general palette, with title/price typography drawn from confirmed heading and body styles; the grid itself was not observed.

**hero** is proposed as a full-bleed dark section (using observed near-black `#0e0e0e`) to host large Poppins display type, appropriate for a "We make deep and playful effects" brand statement; exact hero markup was not captured.

**footer** reuses the dark neutral surface and muted gray text implied by the palette, sized to hold the observed footer content groups (Support, Company, Social) with a subtle divider line; footer CSS itself was not in the evidence.

**badge** applies the one saturated accent color (`#f0523d`) as a small pill label — proposed for "New," "Limited Edition," or "Small Batch" tags referenced in the page text, since Small Batch Bliss is a named section.

**search** is a proposed pill-shaped input using the soft neutral surface, included for completeness though no search UI was present in the captured CSS.

**artist-demo-card** is the category-appropriate component, modeled on the page's recurring "Artist + Video" pattern (Onward Workshop w/ Omari Jazz, Big Time – Preset Play w/ John Snyder, Meeting Big Time w/ David Torn). It pairs a card surface, title typography, caption typography for the artist name, and the accent color for a small "watch" indicator — proposed, not observed as literal markup.

## Responsive Behavior

Recommended, not measured from live site:

| Breakpoint | Width       | Nav                         | Grid                  |
|-----------|-------------|------------------------------|------------------------|
| Mobile    | < 600px     | Collapsed/hamburger (proposed) | 1-column product cards |
| Tablet    | 600–1024px  | Condensed inline nav (proposed) | 2-column product cards |
| Desktop   | > 1024px    | Full inline nav (proposed)   | 3–4 column product cards |

Touch targets should be at least 44×44px for buttons and nav links. Popup/lightbox close controls and outline buttons should retain the observed hover/transition timing (170ms ease-in-out) as a general interaction convention across breakpoints. None of this responsive behavior was directly observed; it is a standard proposal for a Squarespace-based commerce layout.

## Known Gaps

- **Agent usage policy:** Only evidenced CSS values are reusable facts. Token roles, spacing, dimensions and responsive rules are proposals unless an attached measurement explicitly establishes them.






- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- The captured CSS is almost entirely scoped to the `.sqs-slide-wrapper[data-slide-type="popup-overlay"]` newsletter/lightbox module, not the primary storefront layout, nav, or product pages — most component definitions here are extrapolated from that single module and are inferred, not directly measured elsewhere on the site.
- Baskerville and Clarkson appear in the site's loaded font-family list but were never tied to a specific selector in the evidence, so their actual usage (if any) on headings, logo, or body copy is unconfirmed and was excluded from typography tokens.
- The palette supplied includes numerous well-known third-party social-icon colors (YouTube, Instagram, Facebook, Twitter, Discord, TikTok, Bandcamp, Soundcloud, etc.); these were deliberately excluded from brand color tokens as they represent icon-set colors, not Chase Bliss brand color.
- `#f0523d` is the only saturated non-neutral, non-social color in the evidence; its actual on-site usage (accent, sale tag, link, etc.) is inferred, not confirmed by any captured rule.
- No grid, spacing, breakpoint, or hover/focus states were observed outside the popup buttons; all spacing, radius, and responsive values are proposed conventions.
- Mobile navigation collapse behavior, product grid layout, and cart/checkout UI were not present in the evidence and are not described as observed.
- Font licensing/hosting (e.g., whether Poppins is self-hosted or Google Fonts, and Helvetica Neue's proprietary licensing) was not verified from this evidence.
