---
version: alpha
name: "Outer"
source_url: "https://liveouter.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep teal (#223843) anchors every primary surface and call-to-action — a color that reads neither coastal nor forest but somewhere between the two, placing this outdoor furniture system in a temperate middle ground where shade fabric meets eucalyptus wood. The palette stays deliberately restrained; near-black ink (#121212) carries all body copy, a single soft gray (#dedede) handles dividers and subtle borders, and the rest is white canvas breathing around oversized lifestyle photography. Barlow, a neo-grotesque with generous x-height and open apertures, runs at comfortable weights — semi-bold 600 for headlines, regular 400 for long-form product descriptions that read more like magazine editorial than furniture spec sheets. Corners soften consistently at `{rounded.sm}` for interactive elements and `{rounded.md}` for cards, never reaching full pill shapes except on tags and small badges; the overall geometry suggests precision joinery rather than playful softness. Spacing is generous — section gaps of 64–80px let hero images command attention, and product cards sit in neat grids with `{spacing.lg}` gutters that prevent the dense material swatches and configuration options from feeling cluttered. The nav bar is minimal, transparent over hero imagery, with teal text links that darken on hover. Product pages lean heavily on a configurator pattern — inline swatches for fabric, frame finish, and sectional arrangement — all rendered in compact touch targets with `{rounded.xs}` chip borders. A persistent sticky add-to-cart bar appears on scroll, using the full-width teal `{colors.primary}` button at `{rounded.sm}` to close the sale. The system trusts its photography and generous whitespace to carry emotional weight while keeping UI chrome functionally invisible.

colors:
  primary: "#223843"
  primary-active: "#1a2c35"
  primary-disabled: "#8fa3ab"
  accent-blue: "#007aff"
  ink: "#121212"
  body: "#333333"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-warm: "#f9f7f4"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#2e7d32"
  star-rating: "#f5a623"
  scrim: "rgba(0,0,0,0.45)"

typography:
  display-xl:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  label:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  uppercase-tag:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "'Barlow', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 20px
  xl: 32px
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
  section-lg: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: 2px solid {colors.primary-active}
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.primary}
    backgroundColor: "{colors.canvas}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  hero-section:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    padding: "{spacing.section-lg} {spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 640px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: 0
    border: none
    imageAspectRatio: 4/3
    imageRounded: "{rounded.md} {rounded.md} 0 0"
    bodyPadding: "{spacing.base} {spacing.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-hover:
    boxShadow: 0 4px 16px rgba(0,0,0,0.08)
    transform: translateY(-2px)
  swatch-chip:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    border: 2px solid {colors.hairline}
  swatch-chip-active:
    border: 2px solid {colors.primary}
    boxShadow: 0 0 0 2px {colors.canvas}, 0 0 0 4px {colors.primary}
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
  sticky-add-to-cart:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.md} {spacing.base}"
    borderTop: 1px solid {colors.hairline}
    boxShadow: 0 -2px 8px rgba(0,0,0,0.06)
    position: sticky
    bottom: 0
  badge-promo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-material:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  testimonial-card:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    textTypography: "{typography.body-lg}"
    textColor: "{colors.body}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px
    gap: "{spacing.xxs}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.on-primary}"
    opacity: 0.8
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center

## Components

### Buttons

**`button-primary`** — Full teal (#223843) fill with white text at `{typography.button-lg}`. Corners at `{rounded.sm}` (8px). On hover, background darkens to `{colors.primary-active}` with a subtle 150ms ease transition. Disabled state washes out to `{colors.primary-disabled}` with reduced opacity. Used for all primary conversion actions: "Add to Cart," "Shop Now," "Configure Your Set."

**`button-secondary`** — White fill with a 2px teal border and teal text. Same dimensions as primary. On hover, background shifts to `{colors.surface-soft}` and border deepens. Used for secondary actions like "Learn More," "View Details," and paired alongside primary buttons in two-action layouts.

**`button-tertiary`** — Text-only with underline decoration in `{colors.primary}`. No background or border. Used for inline navigation links within content blocks and "See all" type actions.

### Navigation

**`nav-bar`** — 64px height, white background with a 1px `{colors.hairline}` bottom border. Logo left-aligned, main navigation links centered using `{typography.nav-link}` at weight 500. Cart icon and hamburger menu (mobile) right-aligned. On hero sections, switches to `nav-bar-transparent` with white text overlaying lifestyle imagery.

**`announcement-bar`** — Sits above the nav, 36px tall with `{colors.ink}` background and white centered text in `{typography.caption}`. Used for shipping thresholds, promotions, and seasonal messaging. Dismissible with an × icon.

### Product Cards

**`product-card`** — No outer border, `{rounded.md}` corners, with a 4:3 aspect-ratio hero image that has top-rounded corners only. Body content sits below with `{spacing.base}` padding. Product title in `{typography.title-sm}`, price in `{typography.price}`. On hover, card elevates with a soft box-shadow and -2px Y translation. Swatch dots appear below the title when multiple fabric options exist.

### Swatches & Configurator

**`swatch-chip`** — 32px circles with `{rounded.full}`, showing fabric/material colors. Inactive chips have a 2px `{colors.hairline}` border. Active selection gets a double-ring treatment: inner white gap, outer teal ring via box-shadow. The configurator panel groups swatches by category (fabric, frame, arrangement) inside a `{rounded.md}` bordered container with `{spacing.lg}` internal padding.

### Hero Section

**`hero-section`** — Warm off-white background (`{colors.surface-warm}`) with display typography at `{typography.display-xl}`. Minimum height of 560px. Content is left-aligned with a max-width of 640px, leaving the right side open for a product lifestyle image that bleeds to the edge. A single primary CTA button sits below the headline with `{spacing.lg}` top margin.

### Sticky Add-to-Cart

**`sticky-add-to-cart`** — Appears on product pages after scrolling past the main CTA. White background, top border and subtle upward shadow for depth separation. Contains a condensed price summary and a full-width `button-primary`. Fixed to viewport bottom on mobile, constrained to content width on desktop.

### Testimonials

**`testimonial-card`** — Warm surface background (`{colors.surface-warm}`) with `{rounded.md}` corners. Contains star rating, quote text in `{typography.body-lg}`, and customer attribution in `{typography.caption}`. Cards stack in a horizontal scroll on mobile, 3-column grid on desktop.

### Footer

**`footer`** — Full-width teal (`{colors.primary}`) background with white text. Organized in a 4-column grid on desktop: brand story, product categories, support links, and newsletter signup. Column headings use `{typography.title-sm}` in white, links at 80% opacity that brighten to 100% on hover. Newsletter input is a white-background text field with rounded corners.

### Badges

**`badge-promo`** — Small teal pill with uppercase white text for promotional callouts ("NEW," "BEST SELLER"). **`badge-material`** — Soft gray chip for material descriptors ("OuterShell® Fabric," "Eucalyptus Frame"), using `{typography.label}` with `{rounded.xs}` corners.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger + logo + cart icon. Hero stacks vertically (text above image). Product grid becomes 1-col with horizontal scroll for "related" rows. Sticky add-to-cart bar spans full width. Configurator panel takes full screen as a bottom sheet. |
| Tablet | 744–1128px | 2-column product grid. Hero maintains side-by-side at reduced image width. Nav shows top-level links, secondary items collapse. Configurator stays inline but narrows. Footer shifts to 2×2 grid. |
| Desktop | 1128–1440px | Full layout. 3-column product grid. Configurator alongside product imagery. Nav fully expanded. Hero at full bleed with 50/50 text-image split. |
| Wide | > 1440px | Content max-width caps at 1440px, centered on canvas. Additional whitespace on sides. Image galleries may expand to 4-column. Section padding increases to `{spacing.section-lg}`. |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch area on mobile
- Swatch chips are 32px visually but have 44px tap targets via padding
- Nav hamburger icon has 48px tap zone
- Sticky CTA button spans full viewport width minus `{spacing.base}` margins on each side

### Collapsing Strategy

- Desktop multi-column grids collapse to 2-col at tablet, 1-col at mobile
- Horizontal filter bars become a scrollable row or bottom-sheet modal on mobile
- Product configurator transitions from inline sidebar to full-screen overlay below 744px
- Footer columns stack vertically with accordion-style expandable sections on mobile
- Announcement bar text truncates with ellipsis on narrow viewports, full text on hover/tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only four hex colors extracted; the site likely loads additional palette tokens (warm neutrals, success/error states) via JavaScript or CSS custom properties at runtime
- Barlow is the only confirmed typeface; a secondary serif or display face may be used for editorial content but was not detected in static extraction
- Exact border-radius values on product cards and buttons inferred from visual convention — live computed values may differ by 1–2px
- Icon system (material icons, custom SVGs) not captured in extraction
- Animation/transition timing curves not available from static analysis
- The #007aff value appears to be iOS system blue rather than a brand token — likely used only in mobile webview link defaults, not intentional brand usage
- Exact spacing scale steps may vary; values here are derived from common Shopify theme patterns paired with visual estimation
