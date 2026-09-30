---
version: alpha
name: "Vanessa Fernandez"
source_url: "https://www.vanessafernandez.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  When a jeweler defaults to compressed-indigo (#016087) instead of champagne or rose gold for their primary brand signal, every product photograph must carry the warmth the palette withholds — and that trade-off is the organizing logic this color range implies. The darker flanking tone (#043959, near-navy) and mid-range sibling (#135e96) bracket the primary into a monochromatic cool spectrum unusual in the engagement ring category, where competitors conventionally echo the warm metal tones of their products. Light neutrals — the near-white field (#f3f5f6), card surface (#f1f1f1), and hairline gray (#dadada) — deliver the negative space that high-resolution stone photography requires: a near-colorless field where prong geometry and facet lines carry all visual weight. A note on extraction confidence: the site returned a WordPress error page rather than the live brand at time of scraping, so the entire palette may reflect WordPress admin defaults rather than brand intent; all color attributions should be verified against the live site, and the Known Gaps section details what could not be reliably extracted. Typography detection yielded only operating-system system stacks — no custom web fonts were registered in the DOM — suggesting the brand typeface loads via a JavaScript font kit that bypassed static extraction. For a fine jewelry engagement brand, display type conventionally runs in an old-style serif or geometric sans at low weight (300–400) and generous letter-spacing, kept at modest scale to read as editorial rather than declarative. Body copy at #444444 rather than full black softens overall read without sacrificing contrast. Component structure follows the precision model expected of a high-consideration purchase: slim hairline-bordered inputs, sparse centered-wordmark navigation, product cards dominated by a single ring image, and a detail page organized around a stone-and-metal configurator that terminates in a consultation booking rather than a cart. Corner radii hold at `{rounded.xs}` to `{rounded.sm}` throughout — no pill shapes, no orbs.

colors:
  primary: "#016087"
  primary-active: "#043959"
  primary-disabled: "#7e8993"
  primary-light: "#135e96"
  ink: "#444444"
  body: "#444444"
  muted: "#7e8993"
  muted-soft: "#ccd0d4"
  hairline: "#dadada"
  hairline-strong: "#ccd0d4"
  canvas: "#ffffff"
  surface-soft: "#f3f5f6"
  surface-card: "#f1f1f1"
  on-primary: "#ffffff"
  accent-navy: "#043959"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.02em
  display-lg:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.015em
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
    textTransform: uppercase
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
    textTransform: uppercase
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.05em
  label-field:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  price:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em

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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
    border: none
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
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    labelTypography: "{typography.label-field}"
    labelColor: "{colors.muted}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoAlign: center
    linkAlign: left
  product-card:
    backgroundColor: "{colors.surface-soft}"
    imageAspect: "1:1"
    rounded: "{rounded.none}"
    padding: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    hover: "imageScale: 1.03, transition: 200ms ease"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.muted}"
    ctaButton: button-primary
    layout: "image-right, text-left"
    padding: "{spacing.section} {spacing.xl}"
  ring-configurator:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    selectorLabelTypography: "{typography.title-sm}"
    selectorLabelColor: "{colors.ink}"
    activeSwatchBorder: "2px solid {colors.primary}"
    inactiveSwatchBorder: "1px solid {colors.hairline}"
    swatchSize: 32px
    swatchShape: "{rounded.full}"
    padding: "{spacing.xl} 0"
  stone-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    activeBackgroundColor: "{colors.surface-soft}"
    activeBorderColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  consultation-cta:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    ctaButton: button-primary
    padding: "{spacing.section} {spacing.xl}"
    rounded: "{rounded.none}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  image-gallery:
    backgroundColor: "{colors.surface-soft}"
    thumbnailBorder: "1px solid {colors.hairline}"
    activeThumbnailBorder: "2px solid {colors.primary}"
    thumbnailSize: 80px
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The primary CTA runs 44px tall with squared corners (`{rounded.none}`), uppercase tracking via `{typography.button-md}` (13px, 0.1em spacing), and the brand's ocean blue (`{colors.primary}`) as fill. Active state drops to `{colors.primary-active}` (#043959), the extracted near-navy, adding authority without animation. Disabled state shifts to `{colors.primary-disabled}` (#7e8993), a muted blue-gray that reads clearly inactive. The uppercase + wide-tracked label is the primary signal distinguishing this as a fine jewelry CTA rather than a mass-market buy button.

**`button-secondary`** — Outlined variant: 1px `{colors.primary}` border, white canvas fill, primary-blue text. Shares `{typography.button-md}` uppercase treatment with the primary. Used for secondary actions on the detail page — "Save to Wishlist," "Compare Stones" — while the primary button holds the consultation path.

**`button-ghost`** — Borderline or faint-hairline text button in `{colors.ink}` for tertiary actions, filter resets, and navigation micro-interactions. Uses `{typography.button-sm}` scale. No fill change on hover; underline or subtle color shift only.

### Navigation

**`nav-bar`** — 64px tall, white canvas background, 1px `{colors.hairline}` bottom border. Brand wordmark centers in the bar; category links (Collections, Engagement, About, Contact) float left in `{typography.nav-link}` (13px, 0.05em spacing); account and wishlist icons anchor right. Navigation depth is intentionally shallow — for fine jewelry, the configurator IS the category.

### Product Cards

**`product-card`** — Square image block on a `{colors.surface-soft}` background with no rounding. Title in `{typography.title-sm}` (uppercase, 13px, tracked) in `{colors.ink}`. Price renders in `{typography.price}` (Georgia serif, 18px, weight 400), introducing a formal, document-like register at the moment of valuation — a deliberate departure from the sans-serif convention used for everything else. On hover the image scales to 1.03× over 200ms.

### Hero

**`hero-banner`** — Left-aligned editorial text on a `{colors.surface-soft}` near-white field, with a full-bleed ring photograph filling the right half on desktop. Headline at `{typography.display-xl}` (36px serif, weight 300) reads as a caption for the image rather than a command. Sub-line in `{typography.body-md}` handles descriptive copy in `{colors.muted}`. The primary CTA sits 24px below the sub-line. On mobile the layout stacks, image above text.

### Ring Configurator

**`ring-configurator`** — The core interactive block on the product detail page, sitting directly below the hero image. Metal swatches (Yellow Gold, White Gold, Platinum, Rose Gold) render as 32px circular color chips — inactive: 1px `{colors.hairline}` border; active: 2px `{colors.primary}` border. Stone shape options (Round, Oval, Cushion, Emerald, Pear) appear below as labeled icon tiles via the `stone-selector` component. Each selection should update the hero image client-side without full-page reload.

### Stone Selector

**`stone-selector`** — Rectangular tiles in `{rounded.xs}` used within the ring configurator for stone shape choice. Inactive: 1px `{colors.hairline}` border, `{colors.canvas}` background, `{typography.caption}` label. Active: 1px `{colors.primary}` border, `{colors.surface-soft}` background. These are more information-dense than the metal swatches — closer to filter chips than visual swatches — and tile in a wrapping row rather than a fixed grid.

### Consultation CTA

**`consultation-cta`** — A full-width band in `{colors.accent-navy}` (#043959), the darkest extracted tone. White headline in `{typography.display-md}` (22px serif), white body in `{typography.body-md}`, and a white-label `button-primary` (same fill logic, inverted context). This section converts the configurator's exploratory session into a booked private appointment. Copy would read "Begin Your Ring Journey" or "Book a Private Consultation" — not e-commerce phrasing.

### Image Gallery

**`image-gallery`** — Main ring image at full container width (or ~58% of the detail layout on desktop), with 80px square thumbnails beneath showing alternate angles: profile views, prong details, lifestyle wrist shots. Inactive thumbnail: 1px `{colors.hairline}` border. Active thumbnail: 2px `{colors.primary}` border. No rounded corners anywhere in the gallery block. On mobile, thumbnails convert to a swipe carousel with dot indicators.

### Footer

**`footer`** — Dark canvas in `{colors.ink}` (#444444), white body text, links in `{colors.muted-soft}` (#ccd0d4). Section headings in `{typography.title-sm}` (uppercase, tracked). Body links and copyright in `{typography.body-sm}`. Four-column grid on desktop (Collections, About, Contact, Legal) collapses to two on tablet and single-column stacked on mobile with `{spacing.xl}` section gaps.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; ring configurator swatches scroll horizontally in a single row; hero stacks image above text; product grid 2-up; consultation CTA single-column with reduced padding |
| Tablet | 744–1128px | 2-column product grid; hero retains side-by-side at reduced scale; nav shows full text links; configurator swatches wrap to two rows |
| Desktop | 1128–1440px | 3-column product grid; hero at full bleed; detail page uses sticky right-column layout with configurator and consultation CTA remaining in viewport while user scrolls image gallery |
| Wide | > 1440px | Max-width container at 1280px centered on a `{colors.surface-soft}` bleed; hero image extends edge-to-edge while text column remains fixed-width; product grid holds at 3-up to preserve card scale |

### Touch Targets

- All buttons minimum 44px tall and 44px wide
- Metal swatch chips upscaled to 40px diameter on mobile (from 32px desktop)
- Stone selector tiles minimum 44px tall on mobile
- Image gallery thumbnails replaced by full-width swipe gesture; tap area per dot indicator minimum 44×44px
- Nav hamburger icon minimum 44×44px tap area with generous invisible padding

### Collapsing Strategy

- Ring configurator moves below the hero photograph on mobile; a sticky "Request Consultation" bar pins to bottom of screen once user scrolls past the fold
- Product card title and price always visible; no text truncation on card grid
- Footer 4-column grid collapses to single-column stacked on mobile with `{spacing.xl}` between sections
- Image gallery thumbnails convert to swipe carousel with dot-position indicators on mobile; no thumbnail strip

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Extracted colors are likely WordPress admin defaults** — the site returned a "WordPress › Error" page at extraction time, not the live brand. Colors #007cba, #2271b1, #135e96, #043959, and #ccd0d4 are documented WordPress admin palette values. The #016087 treated here as brand primary also falls within the WordPress admin blue range. True brand palette is unverified and should be extracted from the live site directly.
- **No custom web fonts detected** — DOM extraction found only OS/browser system stacks. The brand's actual display typeface (likely a purchased serif or geometric sans) loads via a font CDN or JavaScript kit that bypassed static extraction. The Georgia-based display stack used here is a fine jewelry convention, not an observed brand choice.
- **No Shopify metadata** — platform detection returned false for Shopify. Underlying e-commerce platform, checkout architecture, and cart behavior are unknown.
- **No meta theme-color** — browser chrome tint color not set or not extractable from the error page.
- **No live product content** — ring photography style, product taxonomy (collections, stone types, price range), and CMS structure are inferred from category positioning (engagement rings, fine jewelry), not observed from the live site.
- **Component interaction states** — hover transitions, configurator update behavior, and modal animations are designed per fine jewelry UI conventions, not extracted from live behavior.
- **No brand iconography or logo format** — wordmark style, logo lock-up, and any brand marks are unknown without access to the live site.
