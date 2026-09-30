---
version: alpha
name: "Morrison Hotel Gallery"
source_url: "https://www.morrisonhotelgallery.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  At Morrison Hotel Gallery, the orange-red flash of #ff3300 — the exact hue of a stage light caught in a long-exposure concert shot — is the only warm voltage in an otherwise near-monochrome system. Every other color defers to the photographs: ink-black (#222222) anchors display text, a descending grayscale of #3d4246, #595959, and #737373 carries hierarchy without competing with silver-gelatin tones, and the warm cream surface (#faf1e9) evokes archival photographic paper rather than generic off-white. Rounded corners are held at {rounded.xs} on inputs and {rounded.none} on product cards — a deliberate museum-frame discipline that keeps the UI from softening the impact of a Jimi Hendrix close-up or a backstage Nixon handshake. A teal counterpoint (#00a47c) handles secondary actions and availability states, preventing the palette from collapsing into monochrome; amber (#f29100) marks promotional moments with warmth rather than urgency; a quiet lavender-gray register (#50506d, #80808d, #bbbbdd, #ddddee) surfaces in filter chips, pagination, and hover states — visually distinct from pure gray hairlines (#c7c7c7, #ebebeb) without borrowing the brand red. The Shopify commerce layer operates subordinately: product cards place the print image at full bleed, set the title in a modest title-md weight, and push dimensions, edition number, and price to caption scale in {colors.body} and {colors.muted}. Navigation is deliberately spare — wordmark left, minimal links, cart icon — trusting that collectors arrive with intent. No custom font families were captured in the extraction, as the stack appears to load via JS or a third-party service; a condensed grotesque at display scale and a clean geometric sans for body would match the gallery's editorial register, and the type specs below use a neutral system-sans fallback until confirmed.

colors:
  primary: "#ff3300"
  primary-active: "#dd3300"
  primary-disabled: "#c7c7c7"
  accent-teal: "#00a47c"
  accent-amber: "#f29100"
  ink: "#222222"
  ink-dark: "#262626"
  ink-medium: "#3d4246"
  body: "#595959"
  muted: "#737373"
  muted-soft: "#80808d"
  hairline: "#c7c7c7"
  hairline-soft: "#ebebeb"
  hairline-medium: "#e8e9eb"
  hairline-light: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#f8f8f8"
  surface-warm: "#faf1e9"
  surface-muted: "#eeeef4"
  on-primary: "#ffffff"
  accent-lavender: "#bbbbdd"
  accent-lavender-soft: "#ddddee"
  accent-purple: "#50506d"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-strong:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  edition-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px

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
    padding: 14px 28px
    height: 46px
    hoverBackground: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 46px
    hoverBackground: "{colors.ink}"
    hoverTextColor: "{colors.on-primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 10px 20px
    hoverBackground: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    focusBorder: "1px solid {colors.hairline}"
    padding: 10px 40px 10px 14px
    iconColor: "{colors.muted}"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    linkHoverColor: "{colors.primary}"
    cartIconColor: "{colors.ink}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    shadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    artistTypography: "{typography.caption}"
    artistColor: "{colors.muted}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    editionTypography: "{typography.edition-label}"
    editionColor: "{colors.muted-soft}"
    padding: "{spacing.sm} 0"
    hoverImageScale: 1.03
    transitionDuration: 300ms
  hero-fullbleed:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    overlayBackground: "rgba(0,0,0,0.35)"
    ctaButton: "{colors.primary}"
    minHeight: 80vh
  artist-profile-header:
    backgroundColor: "{colors.surface-warm}"
    nameTypography: "{typography.display-md}"
    nameColor: "{colors.ink}"
    bioTypography: "{typography.body-md}"
    bioColor: "{colors.body}"
    padding: "{spacing.xxl} {spacing.section}"
  edition-badge:
    backgroundColor: "{colors.ink-dark}"
    textColor: "{colors.on-primary}"
    typography: "{typography.edition-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  availability-tag:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  sale-tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  filter-chip:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.accent-purple}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.accent-lavender-soft}"
    padding: 6px 12px
    activeBackground: "{colors.accent-purple}"
    activeTextColor: "{colors.on-primary}"
  filter-chip-active:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  lightbox-overlay:
    backgroundColor: "rgba(0,0,0,0.92)"
    closeButtonColor: "{colors.on-primary}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.surface-soft}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.nav-label}"
    labelColor: "{colors.hairline-soft}"
    borderTop: "none"
    padding: "{spacing.section} 0"
  pagination:
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.muted}"
    inactiveBorder: "1px solid {colors.hairline}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.none}"
    size: 36px

## Components

### Buttons

**`button-primary`** — Flat, uppercase, zero-radius CTA rendered in #ff3300 against white text. The hover state deepens to #dd3300 with no transition other than a color swap, maintaining the gallery's abrupt editorial register. Disabled state uses #c7c7c7, making it visually inert. Used for "Add to Cart" and checkout progression.

**`button-secondary`** — White background with a 1px solid #222222 border and uppercase letter-spaced label. On hover, the entire button inverts: black fill, white text. Appears alongside the primary on product detail pages for "Inquire" or "View More" actions.

**`button-ghost`** — Outlined in #ff3300 with matching red text; inverts to solid red on hover. Reserved for secondary promotional CTAs where the red must appear without the visual weight of a filled button — typically on warm-cream (#faf1e9) editorial sections.

### Search

**`search-bar`** — Low-contrast field on #f9f9f9 with a 1px #ebebeb border, subtly separated from the canvas. A loupe icon in #737373 sits right-anchored. Focus sharpens the border to #c7c7c7. The zero-radius treatment reinforces the gallery aesthetic across all input surfaces.

### Navigation

**`nav-bar`** — 64px-tall bar on white with a 1px #ebebeb bottom border. Links are 13px uppercase with 0.5px letter-spacing; active and hover states shift to #ff3300. The wordmark sits left-aligned; navigation links and a cart icon anchor the right. On scroll, no sticky behavior change is expected — the bar remains white and static.

**`nav-dropdown`** — Flush-edged panel (no border-radius) with a soft shadow (0 4px 16px rgba(0,0,0,0.08)) dropping below the nav link. Typography shifts to 14px body-sm, left-aligned, with each link on its own row. Background is pure white, border is 1px #ebebeb.

### Product Cards

**`product-card`** — Image at full-width, zero-radius, with a 1.03× scale on hover over 300ms. Below the image: artist name in 12px #737373 caption, print title in 15px 600-weight title-sm in #222222, edition info in 11px #80808d, and price in 16px 600-weight. No card surface background — the card sits directly on the canvas or grid background. Tags (edition-badge, availability-tag, sale-tag) overlay the image corner at 0-radius.

### Badges and Tags

**`edition-badge`** — Near-black (#262626) fill, white text, 11px, zero-radius. Applied as an image-overlay to indicate "Limited Edition" or print run numbers.

**`availability-tag`** — Teal (#00a47c) fill, white text, zero-radius. Used to signal in-stock or available-for-order status without the urgency of the brand red.

**`sale-tag`** — Primary (#ff3300) fill, white text, zero-radius. Applied to sale items or new arrivals where the brand voltage is appropriate.

### Filters

**`filter-chip`** — Pale lavender-gray (#eeeef4) background with a 1px #ddddee border and #50506d text. Active state inverts to #50506d fill with white text. The lavender-shifted tone distinguishes filter UI from the gray hairline system without borrowing from the brand red.

### Artist Profile Header

**`artist-profile-header`** — Warm cream (#faf1e9) section spanning the page width, with the artist name in 32px 600-weight and bio in 16px body-md at #595959. The warm surface provides the only break from the white-canvas baseline, evoking archival photographic paper.

### Lightbox

**`lightbox-overlay`** — 92% black scrim behind an enlarged print image. Caption and edition info appear below in 12px #f8f8f8. Close control is a white × icon top-right. No animation specification was extractable; a simple opacity transition is assumed.

### Footer

**`footer`** — Full-width #222222 block. Section labels are 11px all-caps with 1px letter-spacing in #ebebeb; links are 14px #c7c7c7 with #ffffff on hover. The dark footer anchors the page and ties to the editorial-photography brand register without introducing any new color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces top links; hero drops to 60vh; filter chips scroll horizontally; footer columns stack |
| Tablet | 744–1128px | 2-column product grid; nav links visible; hero at 70vh; filter bar wraps to 2 rows |
| Desktop | 1128–1440px | 3–4 column product grid; full nav with dropdowns; hero at 80vh; sidebar filter panel possible |
| Wide | > 1440px | Max-width container (~1400px) centered; 4-column grid; generous section padding |

### Touch Targets

- All buttons minimum 44px height
- Filter chips minimum 36px height with 12px horizontal padding
- Nav links 44px touch area even if visually smaller
- Cart and close icons wrapped in 44×44px tap zones

### Collapsing Strategy

- Nav collapses to hamburger below 744px; logo remains visible
- Product grid: 4-col → 3-col → 2-col → 1-col across breakpoints
- Artist profile header padding scales from {spacing.section} (desktop) to {spacing.xl} (mobile)
- Filter row collapses from inline chips to horizontally-scrolling pill strip at mobile
- Footer: 4-column link grid collapses to 2-column at tablet, single-column at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families were detected — the typeface stack is likely loaded via JavaScript or a third-party font CDN (e.g., Adobe Fonts or a custom CDN). All `fontFamily` values in this file use a system-sans fallback and should be updated once the actual face is confirmed.
- No font-weight variants or display-specific font sizes could be confirmed without font extraction; sizes and weights above are inferred from gallery-editorial conventions.
- Disabled state colors for primary buttons (#c7c7c7 placeholder) were not present in the extracted palette; actual disabled token may differ.
- Hover, focus, and transition timing values were not extractable from static color analysis.
- Lightbox/modal animation curves and durations are unconfirmed.
- Mobile navigation structure (hamburger vs. persistent) could not be verified without live interaction.
- Custom icon set (cart, search, close, social) typeface or SVG system was not captured.
- Meta theme-color was absent, suggesting no PWA manifest or pinned-tab color is defined.
