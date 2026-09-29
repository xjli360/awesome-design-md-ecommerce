---
version: alpha
name: "Manscaped"
source_url: "https://manscaped.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A dark, direct-to-consumer men's grooming brand built on a near-black ink (#313131) that reads as industrial confidence rather than corporate gray, paired with a stark white canvas that lets product photography and instructional illustration carry the selling story. The brand's single extracted hex — a deep charcoal — suggests a system that trusts contrast over color: white text on dark backgrounds for headlines, black text on white for body copy, and no secondary accent color visible in the extracted palette. Typography runs the Apple system stack at modest weights, with display sizes likely landing in the 20–28px range at weight 500–600, avoiding the gym-bro boldness one might expect from a grooming brand aimed at men. Navigation reads as utilitarian and transactional: a sticky top bar with logo left, utility icons right, and a search field that collapses on mobile. Product cards use generous whitespace, soft rounded corners ({rounded.md} ~12px), and a single CTA button that lives in the dark ink — no gradient, no glow, no gimmick. The checkout flow, while not fully extracted, likely mirrors the same high-contrast, low-color approach: dark buttons on white, thin hairlines for dividers, and a focus on trust signals (secure checkout badges, money-back guarantees) over decorative flourish. This is a brand that sells razors and trimmers with the visual language of a tool company, not a skincare line.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#2e7d32"
  warning: "#f57c00"
  error: "#d32f2f"
  badge-new: "#313131"
  badge-sale: "#d32f2f"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase

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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: 2px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 23px
    height: 48px
    border: 2px solid "{colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 24px
    height: 48px
  button-large:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 16px 32px
    height: 56px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 2px solid "{colors.primary}"
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 2px solid "{colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid "{colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    border: 1px solid "{colors.hairline-soft}"
  product-card-hover:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    border: 1px solid "{colors.hairline}"
    boxShadow: 0px 4px 12px rgba(0, 0, 0, 0.08)
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0px 0px"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base} 0px {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-section-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 40px
    border: 2px solid "{colors.primary}"
  footer-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  accordion-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base}"
    borderBottom: 1px solid "{colors.hairline-soft}"
  accordion-content:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base} {spacing.base} {spacing.base}"
  rating-stars:
    color: "{colors.primary}"
    size: 16px
  trust-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: 1px solid "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in the full-strength ink (#313131) on white. Used for "Add to Cart", "Subscribe & Save", and checkout actions. On hover, deepens to near-black (#1a1a1a) for a subtle press effect. Disabled state drops to a mid-gray (#a0a0a0) with a not-allowed cursor, signaling the action is unavailable without visual noise.

**`button-secondary`** — An outlined variant with the same ink color on a white background, bordered by a 2px solid stroke. Used for secondary actions like "Learn More" or "View Details" alongside primary buttons. Active state shifts the border and text to the deeper primary-active shade.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Cancel" or "Skip" in forms and modals. Relies entirely on the ink color and button-md typography for visibility.

**`button-large`** — An expanded primary button for hero sections and promotional banners, using 18px bold type and 56px height. Carries the same dark fill and white text, but with increased padding for visual weight in high-impact placements.

### Text Inputs
**`text-input`** — Standard single-line input with a 1px hairline border and 12px internal padding. Focus state swaps to a 2px primary-colored border for clear keyboard focus indication. Error state uses a red border (#d32f2f) without changing the background, keeping the error visible but not alarming.

**`select-input`** — Dropdown selector matching the text-input dimensions and border style. Uses the system-native dropdown arrow rather than a custom icon, consistent with the brand's utilitarian approach.

### Navigation
**`nav-bar`** — A 64px sticky header with white background and a thin bottom border. Logo sits left, navigation links (Shop, Learn, Help) use uppercase 14px medium-weight type in muted gray for inactive states and full ink for active. Utility icons (search, account, cart) cluster on the right.

**`nav-link-active` / `nav-link-inactive`** — Navigation link states that toggle between the brand's ink and muted gray. No underline or background shape — the color shift alone signals the current section.

### Product Cards
**`product-card`** — A white card with a 1px soft hairline border and 12px rounded corners. Contains a full-width product image (top corners rounded, bottom corners square), a title in 14px semibold, and a price in 16px regular. On hover, the border strengthens and a subtle drop shadow lifts the card off the page.

**`product-card-badge`** — A small uppercase label pinned to the top-left of the product image. Uses the brand's ink on white for "New" badges, and red (#d32f2f) for "Sale" badges. Tight 2px horizontal padding keeps the badge compact.

### Hero Section
**`hero-section`** — A full-width dark band using the primary ink as background with white text. Houses the brand's largest display type (28px) and a large CTA button. Used for campaign headers and category landing pages. A light variant (`hero-section-light`) swaps to a soft gray background with dark text for content-heavy sections.

### Search
**`search-bar`** — A pill-shaped input field with soft gray background and 1px hairline border, used in the navigation bar. On focus, the background turns white and the border becomes a 2px primary stroke. The pill shape (`rounded.full`) is the only rounded-full element in the system, giving the search field a distinct identity.

### Footer
**`footer-section`** — A full-width dark footer matching the primary ink, with white links in body-sm type. Links use the on-primary white by default and shift to muted-soft gray on hover. Organized in columns with accordion headers on mobile.

### Accordion
**`accordion-header`** — A full-width clickable row with a 1px soft bottom border, used for FAQ sections and mobile navigation menus. Content panels collapse beneath with reduced padding and body-sm type.

### Trust Elements
**`trust-badge`** — A small pill-shaped badge on a soft gray background, used for "Free Shipping", "30-Day Guarantee", and "Secure Checkout" messaging. Rendered in caption-sm type for secondary emphasis.

**`rating-stars`** — A 5-star rating display using the brand's ink color for filled stars and muted-soft for empty. Each star is 16px, placed inline with the product card price.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu; hero padding reduces to 32px; search bar moves to expandable overlay; footer accordions replace column layout; product cards stack full-width |
| Tablet | 744–1128px | Two-column product grid; nav links remain visible but condensed; hero uses 40px side padding; search bar visible but compact; footer shows 2-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at 64px padding; search bar at full width in nav; footer at 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to 4 columns; hero content centered with max-width; all elements scale proportionally |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch compliance
- Product card CTAs are 48px tall on mobile, matching desktop
- Accordion headers have 48px minimum tap area
- Nav bar icons (search, cart, account) are 40x40px tap targets
- Quantity selector buttons are 40x40px with 8px internal padding

### Collapsing Strategy
- Primary navigation collapses to hamburger menu below 744px
- Product filters collapse to a sticky bottom sheet on mobile
- Footer link columns collapse to accordion panels below 744px
- Search bar collapses to an icon that expands to full-screen overlay on mobile
- Product image galleries collapse from thumbnail strip to swipeable dots on mobile
- Multi-step checkout collapses to single-page scroll on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was reliably extracted from the live site; the full brand palette (secondary accents, gradients, hover states) could not be determined. The colors block above includes inferred values (success, warning, error, badge colors) based on common e-commerce patterns, not extracted data.
- No font-family declarations beyond the Apple system stack were found; the brand may use a custom typeface (e.g., a bespoke sans-serif) that is loaded via JavaScript or a CDN not captured in the extraction.
- Button hover and active states for secondary, ghost, and large variants are inferred from common patterns, not extracted from the live site.
- No data on form validation styling (success states, helper text, character counts) was available.
- Modal, tooltip, and toast notification styling is unknown.
- Dark mode support and corresponding color tokens could not be verified.
- The brand's use of illustration style, iconography, and photography treatment (lifestyle vs. product-only) is inferred from category norms, not extracted.
- Checkout flow components (payment forms, address fields, order summary) are based on standard e-commerce patterns, not Manscaped-specific extraction.
- The extracted page title "Just a moment..." suggests a Cloudflare challenge page was served instead of the actual homepage; all design data should be treated as partial and potentially incomplete.
