---
version: alpha
name: "Soho Home"
source_url: "https://www.sohohome.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Dark charcoal (#313131) does the work that most brands assign to a signature hue — at Soho Home it functions simultaneously as ink, primary action color, and environmental mood, collapsing the distinction between text and brand into a single authoritative tone. The canvas stays warm-white rather than clinical, creating a gallery-wall contrast where oversized lifestyle photography dominates the viewport and UI elements recede to near-invisible rules and restrained type. Navigation runs in a slim uppercase sans-serif at modest tracking, lending the header the feel of a printed magazine masthead rather than a software toolbar. Product cards carry no visible border — they float on `{colors.canvas}` with generous `{spacing.xl}` gutters, relying on image aspect ratio and typographic hierarchy alone to define their boundaries. Buttons are squared-off rectangles (`{rounded.none}` to `{rounded.xs}`) filled solid in `{colors.primary}`, telegraphing the no-nonsense attitude of a members-club retail arm that assumes you already know what you want. Category landing pages lean on full-bleed hero images at near-cinematic aspect ratios, overlaid with display type in light weight against dark scrims — a layout grammar borrowed from editorial print that treats the browser window as a broadsheet spread. The spacing system breathes wide: section gaps reach 80–120px on desktop, and even mobile preserves 48px between content blocks, refusing to crowd furniture imagery into tight grids. Colour accents are almost absent; where other home brands reach for terracotta or sage to signal warmth, Soho Home trusts the photography to carry warmth and keeps the interface monochromatic — `{colors.muted}` for secondary text, `{colors.hairline}` for dividers, and nothing else competing with the product.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#9e9e9e"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  muted-soft: "#a0a0a0"
  hairline: "#e0e0e0"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f7f7f5"
  surface-card: "#ffffff"
  surface-warm: "#f5f3f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "rgba(0, 0, 0, 0.55)"
  accent-gold: "#b8965a"
  error: "#c0392b"
  success: "#2d7d46"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 1.2px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 1.0px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 1.5px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  eyebrow:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
  section: 80px
  section-lg: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 31px
    border: "1px solid {colors.primary}"
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 8px 0
    borderBottom: "1px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 14px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-transparent:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0
    imageAspectRatio: "3:4"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 85vh
    contentPadding: "{spacing.xxl}"
    contentMaxWidth: 640px
  category-tile:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1:1"
    padding: "{spacing.lg}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-lg}"
    descriptionTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
    textAlign: center
  membership-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
    linkColor: "{colors.hairline}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.title-lg}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
  product-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    thumbnailSize: 64px
    thumbnailBorder: "1px solid {colors.hairline}"
    thumbnailActiveBorder: "1px solid {colors.primary}"
    gap: "{spacing.sm}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
    buttonWidth: 44px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    letterSpacing: 0.5px

---

## Components

### Buttons

**`button-primary`** — A solid charcoal rectangle with no border-radius, carrying uppercase tracked-out text in `{typography.button-md}`. The zero-radius silhouette reads as decisive and architectural, consistent with the brand's members-club heritage. On hover the fill deepens to `{colors.primary-active}` (#1a1a1a) with no transition delay; disabled state drops to `{colors.primary-disabled}` with pointer-events removed.

**`button-secondary`** — Identical dimensions to primary but inverted: white fill, 1px solid `{colors.primary}` border, charcoal text. On hover the background warms to `{colors.surface-soft}` and the border darkens to `{colors.primary-active}`. Used for secondary actions like "View Details" on collection pages and "Add to Wishlist" in product views.

**`button-tertiary`** — A text-only link-style button with a 1px bottom border. No background, no height constraint. Used inline within editorial content and for "Shop Now" links below category descriptions.

### Navigation

**`nav-bar`** — A 64px-high white strip anchored to the viewport top, separated from content by a single `{colors.hairline}` border. Logo sits center-left; navigation links in `{typography.nav-link}` (12px uppercase, 1.5px tracking) spread evenly. On hero-led pages the nav starts transparent (`nav-bar-transparent`) with white text, transitioning to solid white on scroll past the hero fold. Hamburger icon collapses all links on mobile. Cart and account icons sit flush-right at 24px size.

**`announcement-bar`** — A 36px-tall solid `{colors.primary}` banner above the nav carrying promotional copy in `{typography.caption}` with 0.5px extra tracking. Dismissible via a small ✕ icon flush-right; once dismissed it stays hidden for the session.

### Product Display

**`product-card`** — No border, no shadow, no radius — the card is simply an image followed by stacked text. Images render at 3:4 aspect ratio on a `{colors.surface-soft}` placeholder during load. Below the image: product title in `{typography.title-md}`, then price in `{typography.price}`, separated by `{spacing.sm}`. On hover the image scales to 1.03× with a 400ms ease; no other visual change. "Members Price" appears in `{colors.accent-gold}` when applicable, using `{typography.caption}`.

**`product-gallery`** — A full-width `{colors.surface-soft}` container holding the main product image at native aspect ratio. Thumbnails sit below on mobile (horizontal scroll) or to the left on desktop (vertical stack), 64px squares with 1px `{colors.hairline}` border; the active thumbnail swaps to `{colors.primary}` border. Gallery supports pinch-zoom on touch and lightbox on click.

**`quantity-selector`** — A compact inline control: − and + buttons flanking a numeric input, all within a 1px `{colors.hairline}` bordered box at 44px height. Button regions are 44px wide for touch compliance. Typography is `{typography.body-md}` centered.

### Content Sections

**`hero-banner`** — Full-viewport-height (85vh minimum) photographic hero with a dark gradient scrim (`{colors.scrim}`) concentrated at the bottom third. Display title in `{typography.display-xl}` (light weight, 48px) over the scrim, followed by a one-line subtitle in `{typography.body-md}` and a `button-primary` CTA. Content block max-width 640px, left-aligned on desktop, centered on mobile. On mobile the min-height drops to 70vh to preserve scroll-hint.

**`collection-header`** — A centered text block with `{typography.display-lg}` title and `{typography.body-md}` description beneath, padded `{spacing.xxl}` vertically. No background image, no decoration — pure typographic hierarchy against `{colors.canvas}`.

**`category-tile`** — Square tiles (1:1 ratio) showing a lifestyle image with an `{typography.eyebrow}` label overlay at the bottom. Background `{colors.surface-warm}` visible during image load. No radius, no shadow. Used in grid layouts of 2 columns on mobile, 4 on desktop.

### Utility

**`membership-badge`** — A small inline label in `{colors.accent-gold}` background with white uppercase text (`{typography.eyebrow}`), `{rounded.xs}` corners, padded 4px 8px. Appears on product cards and detail pages to flag members-only pricing.

**`breadcrumb`** — Horizontal chain of `{typography.caption}`-sized links in `{colors.muted}`, separated by "/" in `{colors.muted-soft}`. Sits flush below the nav bar with `{spacing.base}` vertical padding.

**`search-overlay`** — A full-screen white overlay triggered by the nav search icon. Input field spans the top in `{typography.title-lg}` (20px, weight 400) with no visible border — just a bottom `{colors.hairline}` rule. Results populate below in real-time as a product grid.

### Footer

**`footer`** — Solid `{colors.primary}` background spanning full width. Internal layout: four columns of links in `{typography.body-sm}` colored `{colors.hairline}` (light gray on dark), with column headers in `{typography.eyebrow}`. Bottom row carries legal text, locale selector, and payment icons. Generous `{spacing.section}` vertical padding separates the footer from content above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart; hero min-height 70vh; category tiles 2-column; footer stacks to single column accordion; section spacing drops to `{spacing.xxl}` |
| Tablet | 744–1128px | Two-column product grid; nav remains collapsed; hero retains 85vh; category tiles 3-column; footer remains stacked but shows two columns |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav visible; hero 85vh with left-aligned text; footer four-column layout; product gallery switches to side-thumbnail configuration |
| Wide | > 1440px | Content max-width caps at 1440px centered; product grid holds four columns with wider gutters (`{spacing.xl}`); hero image allowed to bleed full viewport width while text block stays within max-width container |

### Touch Targets

- All interactive elements maintain minimum 44×44px tap area on mobile
- Product card tap area covers the entire image + text block (not just text)
- Nav hamburger icon padded to 48×48px; close icon in overlay matches
- Quantity selector buttons explicitly 44px wide for thumb reach
- Footer accordion headers: full-width tap rows at 48px height

### Collapsing Strategy

- Navigation links collapse into a full-screen slide-out drawer below 1128px, anchored left with a dark scrim backdrop
- Footer columns collapse into expandable accordions on mobile, each header toggling its link list with a ± icon
- Product filters move from a persistent left sidebar (desktop) to a bottom-sheet modal (mobile) triggered by a sticky "Filter" button
- Breadcrumbs truncate to "… / Parent / Current" on viewports below 744px
- Search overlay remains full-screen at all breakpoints; result grid adapts column count

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned a Cloudflare "Just a moment..." challenge page — no real page content, CSS custom properties, or JS-loaded tokens could be extracted
- Only a single hex color (#313131) was captured; the full brand palette (warm neutrals, gold accent tones) is inferred from widely-known Soho House group design language and may not match current production values exactly
- No custom web fonts were detected — Soho Home likely loads proprietary or licensed serif/sans-serif typefaces via JS that the scraper could not access; the system-font fallback stack used here should be replaced once actual font files are identified
- Exact border-radius values, transition timings, and shadow definitions could not be confirmed
- Members-only pricing logic, sale-state color treatments, and loyalty-tier UI variants are undocumented
- Mobile navigation animation (slide direction, duration, easing) is assumed, not observed
- Product grid column counts at each breakpoint are estimated from common luxury-home patterns, not measured
