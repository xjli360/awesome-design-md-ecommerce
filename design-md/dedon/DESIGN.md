---
version: alpha
name: "Dedon"
source_url: "https://www.dedon.de"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Golden amber (#f1ad09) strikes against deep charcoal (#323232) like afternoon sunlight falling across a weave of hularo fiber — that single warm accent carries every call-to-action, hover state, and wayfinding cue on an otherwise deliberately restrained canvas. Dedon's digital presence mirrors the physicality of its furniture: generous negative space acts like the air flowing through an outdoor pavilion, and product imagery dominates the viewport at near-full-bleed scale, letting material texture speak before any headline does. Typography is set in a geometric sans-serif at moderate weights — display copy rarely exceeds weight 500, trusting the photography and spatial rhythm to create hierarchy. Navigation is architecturally minimal: a slim top bar with the wordmark left-aligned and a hamburger or sparse text links right-aligned, collapsing to a single icon on mobile. Cards and containers carry barely-there radii (`{rounded.xs}` to `{rounded.sm}`), reinforcing the precision-engineered quality of the physical product line. Buttons are compact rectangles with `{rounded.xs}` corners, filled with `{colors.primary}` amber on primary actions and outlined in `{colors.ink}` for secondary paths — never pill-shaped, never playful. The overall color story is near-monochrome with that single golden voltage: white canvas, charcoal ink, warm mid-grays for muted text and hairlines, and amber reserved exclusively for interactive affordances and brand moments. Scroll-triggered reveals and subtle parallax on hero images give the page a slow, deliberate cadence that echoes the handcraft narrative central to the brand. Footer and legal areas recede into `{colors.surface-soft}` warm gray, keeping the eye anchored on product above. The system communicates permanence, material honesty, and a European restraint that lets one accent color do all the emotional lifting.

colors:
  primary: "#f1ad09"
  primary-active: "#d99a08"
  primary-disabled: "#f8d680"
  ink: "#323232"
  body: "#4a4a4a"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#e0e0e0"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f4f2"
  surface-card: "#ffffff"
  surface-dark: "#323232"
  on-primary: "#323232"
  on-dark: "#ffffff"
  accent-warm: "#f1ad09"
  footer-bg: "#2a2a2a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.375
    letterSpacing: 0
  body-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-upper:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0.3px
  nav-link-active:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.3px
  footer-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
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
  section-xl: 128px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: 8px 0
    border: none
    textDecoration: underline
  button-on-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 1px 4px rgba(0,0,0,0.06)
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
  hero-fullbleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 90vh
    padding: "{spacing.section-lg} {spacing.xl}"
    ctaTypography: "{typography.button-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    minHeight: 70vh
    padding: "{spacing.section} {spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: 0
    imageAspectRatio: 4/3
    titleTypography: "{typography.title-sm}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    hoverTransform: translateY(-2px)
    hoverShadow: 0 8px 24px rgba(0,0,0,0.08)
  product-card-collection:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
  collection-grid:
    gap: "{spacing.lg}"
    columns: 3
    columnsMobile: 1
    columnsTablet: 2
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  designer-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    imageRounded: "{rounded.full}"
    imageSize: 80px
    nameTypography: "{typography.title-md}"
    bioTypography: "{typography.body-sm}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-md}"
    inputBorder: none
    inputBorderBottom: 2px solid {colors.ink}
    resultsTypography: "{typography.body-md}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.footer-link}"
    padding: "{spacing.section} {spacing.xl}"
    headingTypography: "{typography.caption-upper}"
    headingColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary}"
  newsletter-signup:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-md}"
    inputBackgroundColor: transparent
    inputBorder: 1px solid {colors.muted-soft}
    inputTextColor: "{colors.on-dark}"
    inputRounded: "{rounded.xs}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonRounded: "{rounded.xs}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    thumbnailSize: 64px
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorderActive: 2px solid {colors.ink}
    gap: "{spacing.sm}"

---

## Components

### Buttons

**`button-primary`** — A compact rectangle filled with the brand's signature amber (#f1ad09), paired with dark charcoal text for maximum contrast against the warm ground. Corners are clipped at `{rounded.xs}` (4px), reinforcing the architectural precision of the brand. On hover, the fill darkens to `{colors.primary-active}`; disabled state washes out to `{colors.primary-disabled}` with muted text. Text is set in uppercase `{typography.button-md}` with generous letter-spacing.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border, holding uppercase charcoal text. On hover, the button inverts entirely: solid `{colors.ink}` background with white text, creating a confident flip-state. This treatment appears on product detail pages and configuration panels where the primary amber would compete with product photography.

**`button-tertiary`** — A text-only link-style button with underline decoration, used for inline actions like "View all collections" or "Read more." No background, no border — typography and underline do the work.

**`button-on-dark`** — Identical to primary but deployed on dark hero sections and the footer. The amber reads even more intensely against charcoal or black backdrops.

### Navigation

**`nav-bar`** — A 72px-tall strip of white canvas with the Dedon wordmark left-aligned in charcoal and sparse navigation links to the right. A barely-visible `{colors.hairline-soft}` bottom border separates nav from content. On scroll, the border disappears in favor of a subtle box-shadow. Navigation links use `{typography.nav-link}` at 14px weight 400 — deliberately quiet so imagery below commands attention.

**`nav-bar-dark`** — A variant used on landing pages where the hero extends to the top edge. The bar becomes transparent over the hero image with white text and wordmark, then transitions to solid white on scroll.

### Hero Sections

**`hero-fullbleed`** — A viewport-dominating image container (90vh minimum) with text overlay in `{typography.display-xl}` white type. A single amber CTA button sits below the headline. The image darkens slightly via a gradient scrim to ensure text legibility. Used on the homepage and collection landing pages.

**`hero-split`** — A two-column layout at desktop widths: left column holds display text and a secondary CTA, right column fills with a cropped product image. Background is clean white canvas. Used on story pages and designer profiles.

### Product Cards

**`product-card`** — A borderless card with a 4:3 aspect-ratio image container and minimal text below. Title in `{typography.title-sm}`, subtitle (collection name or material) in `{typography.body-sm}` muted gray. On hover, the card lifts 2px with a soft shadow bloom. No explicit border or background color — the card lives on the page canvas and relies on spacing and shadow for separation.

**`product-card-collection`** — A larger card variant with a warm gray `{colors.surface-soft}` background fill and `{rounded.sm}` corners, used when grouping products by collection. Includes a bolder `{typography.title-md}` title and optional amber accent line.

### Supporting Components

**`material-badge`** — A small pill displaying material names ("Hularo Fiber," "Teak," "Aluminum") in uppercase caption type on a soft gray background. Used on product detail pages to quickly communicate construction.

**`designer-card`** — Presents a circular portrait (80px, `{rounded.full}`), designer name in `{typography.title-md}`, and a brief bio in `{typography.body-sm}`. Grouped in grid layouts on the "Designers" landing page.

**`search-overlay`** — A full-screen white overlay triggered from the nav magnifying-glass icon. The search input is styled as borderless display-sized text with only a bottom rule in `{colors.ink}`, creating an editorial feel. Results appear below in `{typography.body-md}`.

**`newsletter-signup`** — A dark-background module embedded in or above the footer. Input field is transparent with a muted border; the submit button is amber. Headline in white, supporting text in muted-soft gray.

**`footer`** — Deep charcoal `{colors.footer-bg}` background with column headings in uppercase `{typography.caption-upper}` muted-soft, and link lists in `{typography.footer-link}` white. Links highlight to `{colors.primary}` amber on hover — the only color accent in the footer region.

**`breadcrumb`** — Minimal path indicator in `{typography.caption}` with muted text, a hairline separator, and the current page in `{colors.ink}`. Sits below the nav-bar on interior pages.

**`image-gallery`** — Product detail gallery with a large hero image on a `{colors.surface-soft}` background and a row of 64px thumbnails below. Active thumbnail gets a 2px `{colors.ink}` border. Transitions between images are crossfade, not slide.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger + wordmark. Hero images drop to 60vh. Product grid becomes vertical scroll. Display type scales down to 32px. Section padding reduces to `{spacing.xl}`. |
| Tablet | 744–1128px | Two-column product grid. Nav remains collapsed or shows max 3 links. Hero split stacks vertically. Footer columns reduce from 4 to 2. |
| Desktop | 1128–1440px | Full three-column product grid. Nav expands to full link set. Hero sections reach 90vh. All spacing tokens at defined values. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Side gutters grow symmetrically. Image galleries may expand to 4-across thumbnails. |

### Touch Targets

- All interactive elements maintain a minimum 48px touch target on mobile, even when visually smaller
- Product cards receive full-card tap area — not just the text link
- Nav hamburger icon padded to 48×48px hit zone
- Gallery thumbnails spaced with `{spacing.sm}` gap to prevent mis-taps
- Footer links stacked with `{spacing.base}` vertical gap on mobile for comfortable thumb reach

### Collapsing Strategy

- Navigation collapses to a slide-in drawer (from left) below 1128px, with full-height dark overlay scrim
- Product grids shift from 3-col → 2-col → 1-col at each breakpoint
- Hero split sections stack image-above-text on mobile, maintaining the image's visual primacy
- Footer columns stack vertically with accordion toggles on mobile to prevent excessive scroll
- Material badges wrap naturally; designer cards shift from 3-across to a horizontal scroll strip on mobile
- Search overlay remains full-screen at all breakpoints — input text scales from `{typography.display-md}` to `{typography.title-lg}` on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stacks were extracted from the live site; typography tokens use a Helvetica Neue fallback stack as a best approximation — the actual brand typeface may be a custom or licensed web font loaded via JavaScript
- Only two hex colors (#323232, #f1ad09) were reliably extracted; all derivative palette tokens (muted, hairline, surface, footer-bg) are inferred from those anchors and general brand positioning rather than measured from CSS
- Exact border-radius values could not be confirmed — the `{rounded.xs}` assumption is based on the brand's architectural visual language but may differ from implemented values
- Animation timing functions and durations (hero parallax, card hover transitions) are not captured
- Icon set (material symbols, custom SVGs, or proprietary glyph font) is unknown
- Exact nav-bar height and breakpoint values may differ from the 72px / 1128px estimates used here
- The site may use a dark-mode or region-specific color variant not represented in this extraction
