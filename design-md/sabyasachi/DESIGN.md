---
version: alpha
name: "Sabyasachi"
source_url: "https://www.sabyasachi.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Futura PT — the geometric modernist face designed in 1927 for a Berlin stripped of ornament — anchors the typographic system for a house whose entire product proposition rests on hand-stitched zardozi, raw silk, and centuries-old Bengali craft traditions. That structural tension is the brand's sharpest design statement: a rigidly contemporary letterform holds the negative space while the imagery it captions — embroidery so dense it reads as textile painting — operates in an entirely different century. The official site carries a white (#ffffff) meta theme-color and runs on Shopify, but the atmosphere is anything but minimal: full-bleed editorial photography locks every viewport into a composed frame, with models set against crumbling Mughal architecture, unspun fibre backdrops, or monsoon-light interiors. Navigation is centered and unhurried, with the wordmark commanding its own axis at 0.3em tracking — this is not a multi-brand platform, it is a singular signature. The color palette, unextractable from automated tooling (tokens load via JS; anti-bot protection suppresses scrapers), is documented extensively in fashion press: a deep lacquer burgundy anchors the brand's chromatic identity, appearing in packaging, brand marks, and campaign props at a consistent near-oxblood value; warm matte gold distinguishes the jewelry line without resorting to chrome shimmer; ivory and warm bone supply the recessive canvas that allows textiles to dominate. Rounded values skew toward absolute zero — this is a house of straight edges and architectural frames, with {rounded.none} applied to product cards, buttons, and input fields alike. Where other luxury platforms add soft border-radius as a hospitality signal, Sabyasachi uses angularity as authority. Spacing is generous and asymmetric in editorial sections, compressing only in catalog grids where the density of product demands restraint. The result is a digital presence that functions as an art direction studio first and a commerce platform second — every scroll position is a composed frame, every typographic choice a curatorial act.

colors:
  primary: "#6b1c1c"
  primary-active: "#4d1212"
  primary-disabled: "#c4a0a0"
  gold: "#b5862e"
  gold-light: "#d4a84b"
  gold-muted: "#8a6420"
  ink: "#1c1008"
  body: "#3a2c1e"
  muted: "#7a6858"
  hairline: "#d6cec4"
  hairline-soft: "#ece8e2"
  canvas: "#ffffff"
  surface-soft: "#faf6f0"
  surface-card: "#f5f0e8"
  surface-dark: "#130c05"
  on-primary: "#ffffff"
  on-dark: "#faf6f0"
  on-gold: "#ffffff"

typography:
  display-xl:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: 0.15em
    textTransform: uppercase
  display-lg:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  display-md:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  title-md:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  title-sm:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.14em
    textTransform: uppercase
  body-md:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0.03em
  body-sm:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.03em
  caption:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.08em
  nav-link:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.18em
    textTransform: uppercase
  wordmark:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.3em
    textTransform: uppercase
  button-md:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2em
    textTransform: uppercase
  price:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
  badge:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 9px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2em
    textTransform: uppercase
  announcement:
    fontFamily: "'futura-pt', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.14em
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    position: sticky
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  announcement-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.announcement}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    gap: "{spacing.sm}"
    padding: 0
  product-card-hover:
    imageOverlay: "rgba(28,16,8,0.05)"
    transition: "opacity 0.4s ease"
  hero-editorial:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: "100vh"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.title-md}"
    objectFit: cover
    overlay: "linear-gradient(to bottom, transparent 40%, rgba(19,12,5,0.65) 100%)"
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    minHeight: 640px
    titleTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    layout: "50/50 image-text split"
    textPadding: "{spacing.xxl}"
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xxl}"
    textAlign: center
  lookbook-grid:
    backgroundColor: "{colors.canvas}"
    columns: 2
    gap: "{spacing.xs}"
    imageAspectRatio: "2/3"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
  category-badge:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  gold-accent-badge:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  search-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    suggestionTypography: "{typography.title-sm}"
    border: none
    boxShadow: "0 4px 24px rgba(28,16,8,0.12)"
    inputBorder: "1px solid {colors.hairline}"
    inputRounded: "{rounded.none}"
  jewelry-detail:
    backgroundColor: "{colors.canvas}"
    imageLayout: "2-column stacked grid left"
    titleTypography: "{typography.display-md}"
    priceTypography: "{typography.title-md}"
    descriptionTypography: "{typography.body-md}"
    accentColor: "{colors.gold}"
    ctaButton: "{components.button-primary}"
    materialNoteTypography: "{typography.caption}"
    materialNoteColor: "{colors.muted}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.title-sm}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    borderTop: "1px solid rgba(250,246,240,0.1)"
    columns: 4

## Components

### Buttons

**`button-primary`** — Hard-edged rectangular CTA in deep lacquer burgundy ({colors.primary}), with uppercase Futura PT at 0.2em letter-spacing that reads as command rather than invitation. Height is fixed at 44px with 32px horizontal padding; the proportion is deliberate — neither the slim pill of fast fashion nor the oversized slab of direct-response. Hover state deepens to {colors.primary-active}; disabled state mutes to a parchment-toned {colors.primary-disabled} with no cursor change.

**`button-secondary`** — Transparent fill with a 1px {colors.ink} border and identical uppercase typography, for placement over light editorial surfaces. Hover inverts to a full {colors.ink} fill with {colors.on-dark} text — an ink-wash effect that maintains the hard geometry throughout the state change. No radius at any state.

**`button-ghost`** — Mechanically identical to secondary but keyed to {colors.on-dark}, used exclusively over dark editorial photography, the {announcement-bar}, and the {footer}. Preserves legibility against the {colors.surface-dark} ground without requiring a separate visual language.

### Navigation

**`nav-bar`** — Sticky, 60px tall, bone-white ({colors.canvas}) with the Sabyasachi wordmark centered at {typography.wordmark} (Futura PT, 0.3em tracking, uppercase). Category links in {typography.nav-link} (11px, 0.18em tracked caps) spread symmetrically left and right of the wordmark. A 1px {colors.hairline} bottom border materializes on scroll. The {announcement-bar} sits above in {colors.surface-dark}: a single rotating message in {typography.announcement} — typically a shipping note or new-collection signal — reinforces the house's direct address to the customer before any commerce begins.

### Product Cards

**`product-card`** — Portrait-ratio (3:4) imagery set on {colors.surface-card} at zero radius with no shadow or elevation. Title renders in {typography.title-sm} (12px, 0.14em tracked caps) and price in {typography.price} (13px, sentence case), both left-aligned below the image with {spacing.sm} gap. On hover, a subtle rgba veil ({colors.ink} at 5% opacity) fades in across the image over 0.4s — signaling interactivity without disturbing the photographic composition. No inline "Add to cart" mechanism; the entire card surface routes to the detail page.

### Hero

**`hero-editorial`** — Full-viewport editorial hero with object-fit cover imagery, a linear gradient overlay darkening from transparent at 40% to {colors.surface-dark} at 65% opacity at the base. Headline text in {typography.display-xl} (Futura PT 300, 0.15em tracking, uppercase) sits centered or lower-left depending on campaign composition. When a CTA is present it renders as {button-ghost} over the dark field. On mobile, the image crop anchors to the upper frame where the subject typically sits.

**`hero-split`** — 50/50 split with editorial photography left and text right on {colors.canvas}, used for sub-collection and feature pages. Title in {typography.display-lg}, body in {typography.body-md} at 1.7 line-height. A {spacing.xxl} text padding on the right panel maintains the breathing room that differentiates this from a product shelf — it reads as essay, not category listing.

### Lookbook Grid

**`lookbook-grid`** — Two-column grid of 2:3 portrait photographs with {spacing.xs} gutters, producing the impression of a continuous film strip. Captions appear below each image in {typography.caption} at {colors.muted} — location names, textile references, or stylist credits. At desktop widths above 1128px the grid expands to three columns; below 744px it collapses to a single full-width column.

### Collection Banner

**`collection-banner`** — Full-width centered editorial header for collection landing pages set on {colors.surface-soft}, with {typography.display-md} headline and {typography.body-md} subhead. {spacing.section} vertical padding on desktop creates a breath between the nav and the product grid below, signaling editorial intention before the commerce begins.

### Jewelry Detail

**`jewelry-detail`** — Two-column layout: left stacks 2–4 high-resolution images in a tight portrait grid; right presents title in {typography.display-md}, a fine rule in {colors.gold}, price in {typography.title-md}, and description in {typography.body-md}. A single full-width {button-primary} anchors the CTA with no quantity selector or variant noise on the initial render. Material and provenance notes appear below the button in {typography.caption} at {colors.muted}, carrying information like "22-karat gold, hand-set in Kolkata."

### Search Panel

**`search-panel`** — Overlay panel dropping from the nav with {colors.canvas} ground and a diffuse box-shadow rather than a hard border. The text input uses {typography.body-md} at {rounded.none} with a 1px {colors.hairline} border. Suggestions render in {typography.title-sm} (uppercase, tracked) as a clean vertical list. No autocomplete chips or filter tags at this level — those appear only on the full search results page.

### Footer

**`footer`** — Four-column, {colors.surface-dark} ground with {colors.on-dark} text organized into brand, shop, services, and legal columns. Link text in {typography.caption}; column headings in {typography.title-sm}. A 1px border at 10% {colors.on-dark} opacity separates the footer body from the lower legal strip. The brand mark or a stylized seal typically centers above copyright at reduced opacity — not a button, purely an identity close.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + centered wordmark; hero crops to upper frame; product grid drops to 2-col; lookbook grid to 1-col; hero-split stacks image-over-text; jewelry detail goes single-column with sticky CTA bar pinned to viewport bottom |
| Tablet | 744–1128px | Nav retains top bar at reduced tracking; product grid stays 2-col; hero-split holds at 55/45 image-text; footer compresses to 2-col; collection banner reduces vertical padding to {spacing.xxl} |
| Desktop | 1128–1440px | Full symmetric nav with all links visible; product grid expands to 3-col; lookbook-grid to 3-col; hero-split at strict 50/50; jewelry detail at full two-column layout |
| Wide | > 1440px | Content max-width caps at 1440px centered on canvas; hero imagery bleeds edge-to-edge; product grid optionally adds a fourth column in catalog views |

### Touch Targets

- All buttons are 44px height minimum per design system spec
- Nav links padded to minimum 44×44px tap area via vertical padding expansion on mobile
- Product cards are tappable across the entire card surface, not just the text label area
- Hamburger and close icon targets expanded to 44×44px via padding
- Footer links padded to 36px minimum height on mobile to prevent mis-taps

### Collapsing Strategy

- Primary nav collapses at < 744px to a full-screen overlay drawer with links centered in {typography.display-md} scale — the scale shift signals a mode change, not just a layout change
- Announcement bar collapses to a single scrolling marquee line on mobile, preserving the message without requiring layout height
- Jewelry detail stacks on mobile: full-width image scroll column first, all product info below, with a sticky 56px CTA bar at {colors.primary} pinned to the viewport bottom so the purchase action is never below the fold
- Footer columns collapse to a single centered accordion on mobile with {spacing.xl} between expanded sections
- Collection banners reduce vertical padding to {spacing.lg} on mobile; headline drops to {typography.display-md} scale

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site suppresses color extraction via JS token injection and anti-bot protection. All palette values in this file are derived from fashion press documentation, runway coverage, and brand packaging photography; they are informed approximations, not pixel-sampled values. An authenticated browser session or rendered DOM inspection would be required for accurate extraction.
- **No serif font confirmed** — only `futura-pt` and `sans-serif` were found in the extracted font stack. Some editorial sub-pages or the e-magazine section may employ a serif face (possibly a custom or licensed one) for long-form copy; this was not verifiable from the extracted data.
- **Exact gold value uncertain** — {colors.gold} (#b5862e) is estimated from jewelry campaign photography and editorial imagery; the actual brand gold may be warmer (more amber) or cooler (more champagne).
- **Primary burgundy value uncertain** — {colors.primary} (#6b1c1c) is the widely-documented oxblood associated with Sabyasachi packaging and brand marks; exact digital hex has not been pixel-verified from the live site.
- **No border-radius data extracted** — the zero-radius assumption is based on brand aesthetic documentation and category norms for Indian luxury couture, not extracted CSS values.
- **No spacing scale extracted** — the spacing system above follows Shopify-base conventions adjusted for luxury brand pacing; it is not pixel-verified from the live site.
- **Dark mode or alternate editorial themes** — unknown whether collection-specific dark themes toggle programmatically or whether {colors.canvas} is the universal base.
- **Icon system style** — nav icon line weight and visual style were not extractable; custom SVGs are likely given the brand's design investment and the absence of any standard icon library fingerprint.
- **Mobile nav drawer design** — the exact visual treatment of the collapsed mobile nav (full-screen overlay vs. slide-in drawer vs. push layout) could not be verified without a live mobile session.
