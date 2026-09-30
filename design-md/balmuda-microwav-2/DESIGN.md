---
version: alpha
name: "Balmuda"
source_url: "https://us.balmuda.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Steam rises from a single-slice toaster rendered in matte white — that product-as-sculpture philosophy governs every pixel of the Balmuda digital storefront. The canvas is an unrelenting near-white (#f9fafb to #fafafa), allowing full-bleed product photography to breathe inside generous vertical rhythm set by `{spacing.section}` gutters. The sole voltage color is a deep institutional teal (#108474) — not the expected appliance-brand red or blue — reserved exclusively for primary CTAs, active navigation underlines, and the occasional hover state, lending every interaction a clinical calm. A secondary warm brass (#b19356) surfaces in promotional badges and limited-edition callouts, evoking the copper heating elements inside Balmuda's physical products. Typography is deliberately understated: Open Sans at weights 300–600 handles everything from 42px hero headlines to 13px legal captions, trusting the photography and whitespace to do the emotional labor rather than display type. Corners are barely softened — product cards sit at `{rounded.sm}` (8px), buttons at `{rounded.xs}` (4px) — communicating precision engineering over lifestyle playfulness. The navigation bar floats on a white surface with ink-dark (#1c1d1d) wordmarks and teal accent underlines, collapsing to a hamburger icon at mobile with a full-screen slide-over panel. Product cards are borderless white rectangles with a single `{colors.hairline}` bottom rule, relying on `{spacing.lg}` internal padding and a centered product image rather than decorative chrome. The overall system reads as a Japanese engineering manual translated into e-commerce: nothing is decorative, every element earns its space, and the teal accent arrives with the authority of a single stamp on parchment.

colors:
  primary: "#108474"
  primary-active: "#0c6b5e"
  primary-disabled: "#a3d4cc"
  accent-gold: "#b19356"
  accent-gold-active: "#96793e"
  accent-yellow: "#fbcd0a"
  ink: "#1c1d1d"
  body: "#7b7b7b"
  muted: "#7b7b7b"
  hairline: "#dadada"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  canvas-warm: "#f9fafb"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-tint: "#edf5f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link-blue: "#114499"
  scrim: "#1c1d1d"

typography:
  display-xl:
    fontFamily: "'Open Sans', -apple-system, system-ui, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.19
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.1px
  caption-bold:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.1px
  button-md:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.27
    letterSpacing: 0
  badge-label:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Open Sans', -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
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
  hero: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 44px
    border: 1px solid {colors.hairline}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.ink}
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
    width: 100%
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid #c13515
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-active-indicator:
    backgroundColor: "{colors.primary}"
    height: 2px
    position: bottom
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: none
    boxShadow: none
    imageAspectRatio: 1:1
    imageObjectFit: contain
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    boxShadow: 0 4px 16px rgba(28, 29, 29, 0.08)
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 80vh
    padding: "{spacing.hero} {spacing.xl}"
    imagePosition: center
    contentAlignment: center
  hero-section-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
  badge-limited:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  spec-table-row:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.spec-value}"
    padding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    opacity: 0.7
    opacityHover: 1.0
  product-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    thumbnailSize: 64px
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorderActive: 2px solid {colors.primary}
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  search-overlay:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    boxShadow: 0 8px 32px rgba(28, 29, 29, 0.12)
    padding: "{spacing.lg}"
  mobile-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    width: 100vw
    padding: "{spacing.xl} {spacing.lg}"

---

## Components

### Buttons

**`button-primary`** — A compact, sharp-cornered rectangle in deep teal (#108474) with white uppercase-leaning text at 14px/600. Hover darkens to `{colors.primary-active}`, transitions at 200ms ease. Disabled state fades to a washed teal (#a3d4cc) with no cursor interaction. Used for "Shop Now," "Learn More," and collection CTAs.

**`button-secondary`** — White fill with a 1px `{colors.hairline}` border and ink-dark text. On hover the border sharpens to `{colors.ink}` and background tints to `{colors.surface-soft}`. Pairs alongside primary buttons for "View Details" or filter toggles.

**`button-add-to-cart`** — Full-width variant of primary at 52px height, used exclusively on product detail pages. Slightly larger `{typography.button-lg}` text gives the action more visual weight on the page's single conversion point.

### Navigation

**`nav-bar`** — A 64px white bar with a subtle `{colors.hairline-soft}` bottom rule. Logo sits left as a wordmark in `{colors.ink}`. Navigation links render in uppercase 14px/600 with generous 24px horizontal gaps. The active route receives a 2px teal underline aligned to the bar's bottom edge. Cart icon sits right with a teal dot counter when items are present.

**`announcement-bar`** — A 40px teal (#108474) strip pinned above the nav, carrying promotions or shipping thresholds in white `{typography.caption-bold}` text, centered. Dismissible via a small × icon at right.

### Product Cards

**`product-card`** — Borderless white card with `{rounded.sm}` corners containing a 1:1 product image (object-fit: contain on a `{colors.surface-soft}` background), product name in `{typography.title-sm}`, and price in `{typography.price-display}`. No decorative borders or shadows at rest; on hover a soft 4px/16px shadow lifts the card. Limited-edition products receive a `{colors.accent-gold}` badge in the top-left corner.

### Hero Section

**`hero-section`** — Full-viewport-height block with a single centered product image against `{colors.canvas}`. Headline in `{typography.display-xl}` (42px, weight 300) sits below the image with a single-line subtitle in `{typography.body-md}`. A primary CTA button anchors the bottom third. The dark variant inverts to `{colors.ink}` background with white text for dramatic product launches.

### Product Gallery

**`product-gallery`** — Left-column layout on desktop showing the active image in a `{colors.surface-soft}` container at `{rounded.sm}`. Thumbnail strip sits below (mobile) or left (desktop) as 64px squares with `{rounded.xs}` corners; active thumbnail receives a 2px teal border. Supports swipe gestures on touch devices.

### Spec Table

**`spec-table-row`** — Two-column row with label in `{typography.body-sm}` muted gray and value in `{typography.spec-value}` ink-dark. Rows separated by `{colors.hairline-soft}` 1px rules. Used on PDP for wattage, dimensions, weight, and material callouts.

### Footer

**`footer`** — Full-width dark block (`{colors.ink}`) with white text organized into 4-column link groups on desktop. Links render at 70% opacity, rising to full on hover. Bottom row carries copyright, legal links, and locale selector. Generous `{spacing.section}` vertical padding maintains the brand's breathing-room philosophy even in utility zones.

### Search

**`search-overlay`** — A centered modal panel with `{rounded.sm}` corners and a prominent shadow, triggered from the nav bar magnifying-glass icon. Input field auto-focuses with a teal bottom-border on focus. Results appear below as minimal product rows (thumbnail + title + price) with keyboard navigation support.

### Mobile Menu

**`mobile-menu`** — Full-screen white slide-over from the right, triggered by hamburger icon below 744px. Navigation items stack vertically in `{typography.title-md}` with `{spacing.lg}` vertical gaps. Close button sits top-right. Secondary links (support, account) appear below a `{colors.hairline-soft}` divider in smaller body text.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero image stacks above text; product gallery becomes horizontal swipe carousel; footer collapses to accordion sections |
| Tablet | 744–1128px | Two-column product grid; nav remains visible but link count may reduce to key categories; hero maintains full-height with scaled image; spec table remains two-column |
| Desktop | 1128–1440px | Three-to-four column product grid; full nav with all links visible; product detail uses 50/50 split (gallery left, info right); footer in 4-column layout |
| Wide | > 1440px | Content max-width caps at 1440px, centered on canvas; product grid may go to 4 columns; hero image scales proportionally within container; generous side margins |

### Touch Targets

- All interactive elements maintain 44px minimum touch target on mobile
- Product card tap area covers the entire card surface, not just the text
- Navigation links in mobile menu padded to 48px row height
- Gallery thumbnails spaced with `{spacing.sm}` gaps to prevent mis-taps
- Announcement bar dismiss icon expanded to 40×40px hit area

### Collapsing Strategy

- Navigation links collapse to hamburger at 744px breakpoint
- Product grid shifts from 4 → 3 → 2 → 1 columns as viewport narrows
- Footer link columns collapse into expandable accordion sections on mobile
- Hero section switches from side-by-side to stacked (image above, text below)
- Spec table remains two-column but switches to full-width rows on very narrow viewports
- Product gallery thumbnails move from vertical left strip to horizontal bottom strip below 1128px

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only Open Sans detected as a text font; Balmuda may load a custom display face via JavaScript or a third-party type service that wasn't captured in static extraction
- FontAwesome and JudgemeStar are utility/icon fonts — actual icon library specifics (custom SVG set vs. Font Awesome subset) unclear
- Exact animation/transition timing values (easing curves, durations) not extractable from color/font scrape
- Shopify theme variant (Dawn, custom, or third-party) not identified — component structure inferred from typical Balmuda patterns
- No extracted box-shadow values; shadow specs in components are estimates based on the brand's minimal visual language
- The blue (#114499) and yellow (#fbcd0a) may be contextual (sale badges, alerts) — their exact usage trigger is undetermined
- Mobile breakpoint value (744px) inferred from common Shopify themes; actual value may differ
- Spacing and padding values are systematized estimates — actual Shopify theme spacing variables not captured in extraction
