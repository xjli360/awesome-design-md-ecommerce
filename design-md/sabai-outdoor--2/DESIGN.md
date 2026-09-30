---
version: alpha
name: "Sabai"
source_url: "https://sabai.design"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Sunbleached linen draped over a modular sofa frame — that's the first impression Sabai's digital storefront delivers. The palette draws almost entirely from the warm taupe-to-sand continuum (#9c8d85 through #c9bcac to the canvas at #f8f4ef), punctuated only by a deep indigo (#1d1b3e) on primary CTAs and a golden amber (#ffb600) that flashes across sale badges and urgency callouts. Typography pairs PPEditorialNew for editorial display moments — collection headers, lifestyle captions — with Mabry Pro carrying the everyday UI at 400-weight body and 500-weight buttons, creating a tone that reads as a design magazine married to a furniture showroom. Corners stay soft throughout: product cards at `{rounded.md}`, buttons at `{rounded.sm}`, and pill-shaped tags at `{rounded.full}` reinforce the brand's commitment to comfort as a visual language. Spacing is generous — `{spacing.section}` between lifestyle blocks, `{spacing.xl}` gutters on desktop grids — letting photography breathe rather than packing catalog density. The modular furniture concept extends into the UI: swappable fabric-swatch selectors, configuration builders with step indicators, and sustainability credential badges (#806e28 olive-gold on cream backgrounds) that appear on every product card without overwhelming the warm neutral foundation. Navigation is minimal — a sticky top bar in warm off-white with the wordmark left-aligned and a compact icon cluster (cart, account, search) right-aligned, collapsing to a hamburger on mobile with a full-screen takeover drawer tinted in the brand's lightest sand (#f1eeea).

colors:
  primary: "#1d1b3e"
  primary-active: "#12102e"
  primary-disabled: "#8a899a"
  accent: "#ffb600"
  accent-active: "#e6a400"
  accent-warm: "#feb62b"
  earth: "#9c8d85"
  earth-light: "#c9bcac"
  earth-medium: "#8e7e76"
  earth-muted: "#a99d96"
  olive-gold: "#806e28"
  gold-muted: "#ccb560"
  ink: "#373737"
  body: "#373737"
  muted: "#8f817a"
  muted-soft: "#a2a2a2"
  hairline: "#e6e2e0"
  hairline-soft: "#cdc6c2"
  canvas: "#f8f4ef"
  surface-soft: "#f1eeea"
  surface-warm: "#f0eede"
  surface-card: "#ffffff"
  surface-cream: "#f1eedc"
  on-primary: "#ffffff"
  on-accent: "#373737"
  error: "#cd3824"
  error-soft: "#ffeaeb"
  sale: "#ee575a"
  highlight-orange: "#ff8327"
  highlight-burnt: "#e16a13"
  neutral-bg: "#f2f2f2"
  neutral-light: "#f6f7f8"
  border-soft: "#bfbfbf"

typography:
  display-xl:
    fontFamily: "'PPEditorialNew', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'PPEditorialNew', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'PPEditorialNew', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'PPEditorialNew', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-lg:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-bold:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Mabry Pro', 'Maison Neue', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  editorial-body:
    fontFamily: "'PPEditorialNew', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 1.5px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-active:
    backgroundColor: "{colors.accent-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
  text-input-error:
    border: 1px solid {colors.error}
    backgroundColor: "{colors.surface-card}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.lg}
    borderBottom: 1px solid {colors.hairline}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 1px 4px rgba(0,0,0,0.06)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    overflow: hidden
    boxShadow: none
    border: none
  product-card-image:
    aspectRatio: 4/3
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section-lg} {spacing.xl}"
    minHeight: 560px
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.muted}"
  sustainability-badge:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.olive-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  fabric-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    border: 2px solid {colors.hairline}
  fabric-swatch-active:
    border: 2px solid {colors.primary}
    boxShadow: 0 0 0 2px {colors.canvas}, 0 0 0 4px {colors.primary}
  configuration-step:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
  configuration-step-active:
    border: 1px solid {colors.primary}
    boxShadow: 0 0 0 1px {colors.primary}
  collection-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl} 0"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.on-primary}"
    opacity: 0.8
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
  announcement-bar:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.caption-bold}"
    height: 40px
    padding: 0 {spacing.base}
  mobile-drawer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    width: 100vw
    padding: "{spacing.lg}"
  search-overlay:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: 0 8px 32px rgba(0,0,0,0.12)
  tooltip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 10px

## Components

### Buttons

**`button-primary`** — Deep indigo (#1d1b3e) fill with white text, 8px radius, 48px height. On hover, darkens to #12102e with a subtle 100ms ease transition. Disabled state reduces opacity to 0.6 with the muted indigo fill. Used for all primary conversions: Add to Cart, checkout steps, and email signup.

**`button-secondary`** — White fill outlined with a 1.5px indigo border. On hover, fills entirely with the primary indigo and text flips to white, creating a satisfying inversion. Used for secondary actions like "Learn More", "View Details", and configurator options.

**`button-accent`** — Golden amber (#ffb600) fill with dark text, reserved for urgency moments: limited-time offers, quiz CTAs, and promotional banners. Active state deepens to #e6a400.

### Text Input

**`text-input`** — Clean white field with 1px hairline border (#e6e2e0), 48px height, 8px radius. Focus state swaps the border to indigo with no box-shadow — keeps the warm, uncluttered aesthetic. Error state uses #cd3824 border paired with the soft pink background (#ffeaeb) for inline validation messages.

### Navigation

**`nav-bar`** — 64px sticky header on warm off-white canvas. Logo/wordmark left-aligned, utility icons (search, account, cart with item count badge) right-aligned. On scroll, gains a subtle bottom shadow rather than a hard border change. Desktop shows up to five text links centered; tablet collapses to hamburger with full-screen drawer.

**`announcement-bar`** — Full-width amber (#ffb600) strip above the nav, 40px tall, displaying rotating promotional messages in uppercase caption-bold type. Dark text on gold reads clearly without competing with the indigo primary.

### Product Card

**`product-card`** — No border, no shadow — relies on the 4:3 image container with 12px radius and warm soft background (#f1eeea) as placeholder during load. Title in Mabry Pro 500-weight below, price in muted taupe. Sustainability badge floats top-left of the image when applicable. Hover lifts card 2px with a 200ms transition shadow.

### Hero Banner

**`hero-banner`** — Full-width lifestyle photography background with a warm-tinted overlay or split-layout (image right, copy left). Headline in PPEditorialNew at display-xl scale, subhead in body-lg muted. CTA button sits below with generous spacing. Minimum height 560px on desktop, stacks vertically on mobile with reduced image crop.

### Sustainability Badge

**`sustainability-badge`** — Pill-shaped (`{rounded.full}`) with the soft cream background (#f1eedc) and olive-gold text (#806e28). Used on product cards, PDP features, and collection pages to surface eco-credentials. Uppercase badge typography at 11px with generous letter-spacing.

### Fabric Swatch Selector

**`fabric-swatch`** — 32px circles with 2px hairline border showing fabric color or thumbnail. Active state gains a double-ring treatment: 2px gap in canvas color, then 2px indigo outer ring. Arranged in a horizontal scrollable row on mobile, wrapping grid on desktop.

### Configuration Builder

**`configuration-step`** — Card-style container (12px radius, 1px hairline border) for each modular step: choose frame, choose fabric, choose legs. Active step gains the indigo border with 1px outer glow. Contains illustration/photo, title, and option grid within.

### Footer

**`footer`** — Deep indigo (#1d1b3e) background spanning full width. White text at reduced opacity (0.8) for links, full opacity for headings. Four-column grid on desktop: brand story, shop links, support links, newsletter signup with email input and accent-colored submit button.

### Mobile Drawer

**`mobile-drawer`** — Full-viewport slide-in from left on warm cream (#f1eeea). Navigation links stack vertically with generous 48px touch targets. Accordion sections for Shop categories. Close button top-right as a 32px circle icon button.

### Search Overlay

**`search-overlay`** — Centered modal with 12px radius, generous padding, and deep shadow. Input auto-focuses on open. Results display as minimal product rows (thumbnail, title, price) with instant filtering.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, stacked hero, hamburger nav, full-screen drawer, bottom-sticky Add to Cart bar |
| Tablet | 744–1128px | Two-column product grid, split hero layout, condensed nav with hamburger, fabric swatches scroll horizontally |
| Desktop | 1128–1440px | Three-to-four column product grid, full nav links visible, side-by-side PDP layout (gallery left, details right), footer four-column |
| Wide | > 1440px | Content max-width 1440px centered, increased section padding to `{spacing.section-lg}`, hero image scales proportionally |

### Touch Targets

- Minimum 44px hit area on all interactive elements (mobile)
- Fabric swatches get 44px invisible tap zone despite 32px visual size
- Nav links on mobile maintain 48px row height with full-width tap area
- Cart and account icons in header use 44px circular touch targets

### Collapsing Strategy

- Desktop four-column product grid → two columns on tablet → single column with horizontal scroll peek on mobile
- Footer columns collapse to accordion sections on mobile
- PDP side-by-side becomes stacked: full-width image carousel on top, details below with sticky bottom CTA bar
- Configuration builder steps go from horizontal stepper to vertical accordion on mobile
- Announcement bar text truncates to single line with carousel arrows on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact font weights for Topol and Min Sans typefaces could not be determined from extraction — they may be used in limited editorial contexts or marketing landing pages
- Hover/focus transition durations and easing curves not captured in static extraction
- Dark mode palette not detected — brand likely does not ship one
- Exact box-shadow values for card hover states and dropdown menus inferred from common Shopify patterns rather than measured
- Icon system (line weight, size grid, stroke vs fill) not extractable from color/font scan
- Motion/animation tokens (page transitions, scroll-triggered reveals) not captured
- PPEditorialNew italic variant usage could not be confirmed but is likely present for editorial emphasis
