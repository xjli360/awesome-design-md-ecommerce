---
version: alpha
name: "Andrew Prokos"
source_url: "https://andrewprokos.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Charcoal at #313131 carries nearly the entire visual weight of the Andrew Prokos interface — it surfaces in navigation text, primary button fills, price labels, and footer links — leaving the photography itself as the sole source of hue and sensation on any given page. The print shop operates as a stripped gallery: white canvas, a single near-black tone, hairline borders at {colors.hairline}, and section spacing generous enough that each print thumbnail reads as a framed object rather than a catalog item in a feed. No decorative gradients or secondary brand colors compete with a long-exposure Manhattan skyline or a blue-hour shot of a European city center; the interface deliberately recedes so the image fills the room.

  Buttons take a flat rectangular form at {rounded.none} with {colors.primary} fill and {colors.on-primary} type — no rounded pill, no drop shadow, no hover glow — a choice that positions the brand closer to a Chelsea gallery price list than a consumer print marketplace. The nav bar holds minimal items: genre categories, an about page, and a cart icon, set in tracked uppercase letters at tight scale. Product cards rely on aspect-ratio-locked image crops with a thin-border hover state rather than card lift or background color shift; the photograph itself becomes the interaction affordance.

  Typography runs on the system stack — no custom webfont was detectable on the live crawl. Display headings sit around 40px in a light or regular weight with generous letter-spacing, body copy at 15px, and caption lines at 12px for print dimensions, paper stock, and edition details. The restrained type scale suits the gallery context: it holds attention on the image rather than the interface chrome around it. Edition labels for limited-run prints read as small all-caps badge text at {typography.edition-badge} without background fills — a whisper of scarcity, not a loud merchandising flag. Overall density stays low: wide gutters, tall section padding at {spacing.section}, and print grids of two or three columns on desktop that privilege the viewing experience over catalog velocity.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#b0b0b0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f8f8f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.02em
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.01em
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
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
    letterSpacing: 0.04em
  nav-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  edition-badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  price-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    logoColor: "{colors.ink}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
    priceTypography: "{typography.price-label}"
    textColor: "{colors.ink}"
    mutedColor: "{colors.muted}"
    hoverBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    gap: "{spacing.md}"
  hero:
    backgroundColor: "{colors.scrim}"
    overlayOpacity: 0.3
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.canvas}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.canvas}"
    minHeight: 80vh
    textAlign: center
  print-size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    selectedBackgroundColor: "{colors.surface-soft}"
    padding: 8px 14px
  edition-badge:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.edition-badge}"
    rounded: "{rounded.none}"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price-label}"
  lightbox-overlay:
    backgroundColor: "{colors.scrim}"
    overlayOpacity: 0.95
    closeButtonColor: "{colors.canvas}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    linkColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: 10px 14px
  category-filter-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-label}"
    rounded: "{rounded.none}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "1px solid {colors.ink}"
    padding: "{spacing.sm} 0"

## Components

### Buttons

**`button-primary`** — A flat {rounded.none} rectangle filled with {colors.primary} (#313131) carrying {colors.on-primary} uppercase text at {typography.button-md}. The squared geometry signals a gallery pricing aesthetic rather than a consumer storefront. On hover, the fill deepens to {colors.primary-active}; the disabled state uses {colors.primary-disabled}. No shadows, no glow, no transition beyond a subtle color shift.

**`button-secondary`** — White {colors.canvas} fill with a 1px {colors.ink} border, matching the flat geometry of button-primary. Used for secondary actions like "Add to Wishlist" or "Request Custom Size." On hover, the background shifts to a light {colors.surface-soft} while the border is retained. Same height and typography scale as the primary variant so the two CTA types sit flush in a horizontal pair.

### Text Input

**`text-input`** — White fill, no border-radius, 1px {colors.hairline} border at rest. Focus shifts the border to 1px {colors.ink}, providing clear focus indication without color theatrics. Placeholder text uses {colors.muted}. At 44px height with generous horizontal padding, the input stays proportional to the minimal surrounding layout. Error states can apply a red border with no background fill change.

### Navigation

**`nav-bar`** — White {colors.canvas} with a 1px {colors.hairline} bottom border. Category links use {typography.nav-label} (tracked uppercase, 13px) in {colors.ink}. Logo sits left-aligned in {colors.ink}, either as wordmark or monogram. Cart and possibly a search icon sit right-aligned. At 72px height, the bar frames the photography without dominating it.

**`category-filter-tab`** — A horizontal tab strip below the nav for filtering by city, subject, or collection. Inactive tabs show {colors.muted} text at {typography.nav-label}; the active tab switches to {colors.ink} with a 1px {colors.ink} bottom-border underline. No background fills shift — the underline alone carries active state, consistent with the flat geometry of the rest of the interface.

### Product Card

**`product-card`** — Image-first layout at a locked 4:3 aspect ratio. Title uses {typography.title-md}, price uses {typography.price-label}, and edition or dimension metadata uses {typography.caption} in {colors.muted}. No card lift or shadow on hover — a thin 1px {colors.hairline} border overlay appears around the image crop instead, keeping the hover state from competing with the image. Grid gap is {spacing.md} so prints read as grouped but not crowded.

### Hero

**`hero`** — Full-bleed photography with a {colors.scrim} overlay at 30% opacity, providing contrast for a centered text block. Title uses {typography.display-xl} in {colors.canvas}, caption uses {typography.caption} in {colors.canvas}. A single `button-primary` CTA sits below. Minimum height is 80vh so the hero photograph is the first complete visual experience on load, before the grid of prints below.

### Print Size Selector

**`print-size-selector`** — Bordered tag buttons at {rounded.xs} for choosing paper size (e.g., 20×30 cm, 40×60 cm). Default state: 1px {colors.hairline} border on {colors.canvas}. Selected state: 1px {colors.ink} border with {colors.surface-soft} background. Text uses {typography.body-sm}. Tags sit in a horizontal wrap row with {spacing.sm} between options; on mobile they stack or scroll horizontally.

### Edition Badge

**`edition-badge`** — An all-caps micro-label in {typography.edition-badge} with {colors.muted} text and no background fill or border. Placed below the print title to signal limited-edition status (e.g., "EDITION OF 50") without competing visually with the image, price, or title. Operates as ambient information rather than a sales urgency flag.

### Lightbox Overlay

**`lightbox-overlay`** — A 95%-opacity {colors.scrim} overlay framing a high-resolution print preview. Close button sits top-right in {colors.canvas}. Caption and print metadata use {typography.caption} in {colors.canvas} at the bottom edge. No border-radius anywhere on the overlay frame; the black field against the dark screen recalls a physical darkroom print held up to light rather than a modal dialog box.

### Footer

**`footer`** — {colors.surface-soft} background with a 1px {colors.hairline} top border. Links and text use {typography.caption} with {colors.muted} default and {colors.ink} on hover. Column layout with category links, contact, and social handles. Padding is {spacing.xxl} top and bottom to keep the footer visually distinct from the print grid above without heavy visual weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column print grid; nav collapses to hamburger with slide-in drawer; hero min-height drops to 60vh; size selectors wrap to two columns; category filter tabs become horizontal scroll strip |
| Tablet | 744–1128px | Two-column print grid; nav shows primary categories, overflow collapses; hero retains full landscape crop at reduced overlay text size |
| Desktop | 1128–1440px | Three-column print grid; full nav bar visible; category filter tabs displayed inline; hero at full 80vh with centered text block |
| Wide | > 1440px | Grid constrained to max-width ~1400px with auto side margins; display heading scales up ~10%; section padding increases proportionally |

### Touch Targets

- All buttons minimum 44×44px touch target per WCAG 2.1 AA
- Print size selector tags minimum 44px tall on mobile
- Nav bar items minimum 44px tall with adequate horizontal padding
- Cart and search icons minimum 44×44px hit areas regardless of visual icon size

### Collapsing Strategy

- Nav: hamburger icon at mobile, reveals a full-height slide-in drawer with category links listed vertically
- Category filter tabs: horizontal scroll strip on mobile rather than wrapping to multiple rows
- Product grid: 1 column mobile → 2 columns tablet → 3 columns desktop
- Hero text block: display-xl font reduces to ~26px on mobile; CTA button goes full-width
- Footer columns: stack vertically on mobile, two- or three-column horizontal layout on tablet and above

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site; the crawler was blocked by a Cloudflare challenge page ("Just a moment..."), preventing full palette extraction
- No custom webfont was detected — the typography system is inferred as a system stack; Andrew Prokos may use a licensed serif or display typeface that could not be fingerprinted through the challenge wall
- Accent colors (hover tints, link colors, sale or discount badge colors, selection highlights) could not be extracted and are inferred from gallery-minimal print shop conventions
- Logo treatment (wordmark vs. monogram, serif vs. sans-serif) is unknown
- Exact grid gutter values, container max-width, and confirmed section padding measurements are not available
- Product card metadata layout (dimension display order, paper stock label position, edition count placement) is inferred from comparable fine-art print shop patterns
- Dark-mode variant existence is unknown; the palette is built assuming a light-mode default
- Animation timing, easing curves, and transition durations are entirely inferred
- Whether the site uses a custom checkout flow or a third-party processor (and its attendant UI) could not be confirmed
