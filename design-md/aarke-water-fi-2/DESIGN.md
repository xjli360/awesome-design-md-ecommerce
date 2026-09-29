---
version: alpha
name: "Aarke"
source_url: "https://www.aarke.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Stainless-steel cylinders, precision-milled nozzles, and a website that feels like holding cold metal — Aarke's digital presence strips away everything that isn't the object itself. The palette is near-monochromatic: a deep charcoal ink (`#1a1a1a`) dominates headlines and navigation, while the canvas stays a pure white (`#ffffff`) so product photography — always shot on seamless white or soft gray — floats without distraction. The single accent, a warm brass-gold (`#b8964e`), appears only at inflection points: the "Add to Cart" button, limited-edition badges, and hover states on hero CTAs. Typography leans on a tight geometric sans-serif stack at moderate weights — display headings land around 44–56px in weight 500, never bold enough to compete with the product silhouettes. Body copy sits at a comfortable 16px/1.6, generous line-height reflecting the same air the industrial design demands. Corner radii are almost nonexistent: buttons carry a bare `{rounded.xs}` 4px, cards hold `{rounded.sm}` 8px, and nothing on the page reaches pill territory. Spacing is architectural — `{spacing.section}` (80px) separates content blocks, giving each product hero room to breathe like a gallery pedestal. Navigation is a single horizontal bar, text-only, no icons, collapsing to a minimal hamburger on mobile. Product cards are borderless rectangles relying on shadow and whitespace for separation. The entire system communicates through absence: no gradients, no patterns, no illustrated flourishes — just steel, glass, and the negative space between them.

colors:
  primary: "#b8964e"
  primary-active: "#9a7b3d"
  primary-disabled: "#d9c9a7"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#7a7a7a"
  muted-soft: "#a0a0a0"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-surface-dark: "#f5f5f5"
  brass-highlight: "#c9a96e"
  steel-dark: "#2c2c2c"
  steel-mid: "#4a4a4a"
  overlay-scrim: "rgba(0,0,0,0.4)"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, -apple-system, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.07
    letterSpacing: -1.2px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.09
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.12
    letterSpacing: -0.4px
  display-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.17
    letterSpacing: -0.2px
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
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
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
    lineHeight: 1.14
    letterSpacing: 0.4px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.6px
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.14
    letterSpacing: 0.2px
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: -0.2px

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
  section: 80px
  section-lg: 120px

components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 48px
    textTransform: uppercase
    letterSpacing: 0.8px
  button-primary-active:
    backgroundColor: "{colors.steel-mid}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-accent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 48px
    textTransform: uppercase
  button-accent-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 15px 31px
    height: 48px
    border: 1px solid {colors.ink}
    textTransform: uppercase
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: 8px 0
    borderBottom: 1px solid {colors.ink}
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 14px 0
    borderBottom: 1px solid {colors.hairline}
    focusBorderColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    height: 48px
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
    padding: 0 48px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: 1px solid {colors.hairline-soft}
    boxShadow: none
  nav-bar-inverted:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    imageAspectRatio: 1/1
    imageFit: contain
    imageBackground: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.md}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.xs}"
  product-card-hover:
    transform: none
    opacity: 0.85
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 100vh
    padding: "{spacing.section-lg} {spacing.xxl}"
    display: flex
    alignItems: center
    justifyContent: center
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 720px
    textAlign: center
  hero-subline:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 480px
    textAlign: center
    marginTop: "{spacing.lg}"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 24px
    width: 24px
    border: 2px solid {colors.hairline}
  color-swatch-active:
    border: 2px solid {colors.ink}
  badge-limited:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-gallery:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    aspectRatio: 4/5
    imageFit: contain
  product-detail-price:
    typography: "{typography.price-lg}"
    textColor: "{colors.ink}"
  product-detail-title:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.hairline}
    height: 48px
    padding: 0 16px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-heading:
    typography: "{typography.caption-upper}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.lg}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    hoverColor: "{colors.on-dark}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 420px
    padding: "{spacing.xl}"
    boxShadow: -4px 0 24px rgba(0,0,0,0.08)
  cart-item:
    padding: "{spacing.lg} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  modal-overlay:
    backgroundColor: "{colors.overlay-scrim}"
  modal-content:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    maxWidth: 560px

---

## Components

### Buttons

**`button-primary`** — A solid charcoal-black rectangle with minimal 4px radius and uppercase tracking. The default CTA for add-to-cart, checkout, and form submissions. On hover the background lightens to `{colors.steel-mid}`; disabled state drops to the hairline gray. The button holds 48px height consistently across all viewports.

**`button-accent`** — The brass-gold variant reserved for high-priority conversion moments: limited-edition launches, hero CTAs on dark backgrounds, and promotional banners. Same geometry as primary but uses `{colors.primary}` to break the monochrome field. Hover darkens to `{colors.primary-active}`.

**`button-secondary`** — A transparent button with a 1px ink border. Used for secondary actions like "Learn more" or "Compare models." On hover, the fill inverts to solid ink with white text, creating a satisfying snap between states.

**`button-tertiary`** — A text-only link-style button with an underline border-bottom. Used inline within editorial content or as "View all" triggers in collection grids.

### Inputs

**`text-input`** — Borderless on three sides with only a bottom hairline, reflecting the brand's reductive aesthetic. On focus the bottom border transitions to full ink black. Labels float above in `{typography.caption}` muted gray. No rounded corners — the field is pure horizontal line.

### Navigation

**`nav-bar`** — A 64px-tall horizontal bar with the Aarke wordmark left-aligned and navigation links centered. No bottom border by default; on scroll, a subtle `{colors.hairline-soft}` divider appears. The inverted variant renders transparent with white text for use over dark hero images. The hamburger icon on mobile is a minimal two-line glyph, not three.

**`announcement-bar`** — A slim 36px black strip above the nav carrying shipping thresholds or launch announcements in centered caption text. Dismissible with an × icon that uses the same on-dark color.

### Product Cards

**`product-card`** — A borderless container with a soft-gray image well (`{colors.surface-soft}`) holding the product on a 1:1 aspect ratio with `contain` fit so negative space frames the object. Title and price sit below in tight spacing. No hover scale — only a subtle opacity shift to 0.85 signals interactivity. The restraint keeps the grid feeling like a catalog rather than a marketplace.

### Product Detail

**`product-gallery`** — A 4:5 ratio container with soft-gray background. Product images use `contain` fit to preserve the precise silhouette. Thumbnail navigation below or side-scrolling dots on mobile.

**`product-detail-title`** — Uses `{typography.display-md}` at 32px weight 500, centered or left-aligned depending on layout variant.

**`product-detail-price`** — `{typography.price-lg}` at 22px, placed directly below the title with minimal spacing.

**`color-swatch`** — 24px circles with 2px hairline border. Active selection gets a full ink border. Used for finish selection (matte black, steel, brass, copper).

**`quantity-selector`** — A compact bordered box with minus/plus icons flanking the count. 48px tall to match button height for visual alignment in the add-to-cart row.

### Hero Sections

**`hero-section`** — Full-viewport-height containers with centered content. The default light variant uses `{colors.surface-soft}` background; the dark variant (`hero-dark`) inverts to `{colors.surface-dark}` with white text for dramatic product reveals. Product photography is always the focal point, with text held to a tight max-width column.

**`hero-headline`** — Display-xl type (56px, weight 500) with negative letter-spacing. Max-width 720px prevents overly long lines on wide screens.

### Badges

**`badge-limited`** — Brass-gold background with white uppercase caption text. Appears on product cards and detail pages for limited-edition finishes. Tight 4px radius keeps it angular.

**`badge-new`** — Ink-black variant of the same badge shape. Used for new product launches.

### Cart & Modals

**`cart-drawer`** — A 420px-wide panel sliding from the right with a soft shadow. White background, generous 32px internal padding. Cart items stack vertically separated by hairline-soft borders.

**`modal-overlay`** — 40% black scrim with centered white content panel at `{rounded.sm}`.

### Footer

**`footer`** — Dark background (`{colors.surface-dark}`) with a multi-column link grid. Section headings use uppercase caption tracking. Links render in muted-soft gray, brightening to white on hover. Generous section-level padding (80px top/bottom) maintains the spatial rhythm.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, hero text scales to display-md (32px), cart drawer becomes full-width bottom sheet, section spacing reduces to 48px |
| Tablet | 744–1128px | Two-column product grid, nav links still visible, hero maintains display-lg (44px), cart drawer stays side panel at 380px |
| Desktop | 1128–1440px | Three-column product grid, full horizontal nav, display-xl headlines, 420px cart drawer, 80px section spacing |
| Wide | > 1440px | Content max-width caps at 1440px centered, four-column grid on collection pages, hero images scale to fill with max-height constraint |

### Touch Targets
- All interactive elements maintain minimum 44×44px tap area on mobile
- Quantity selector buttons expand hit area with padding despite 24px visible icon
- Color swatches space at minimum 12px gap to prevent mis-taps
- Nav hamburger icon has 48×48px tap zone

### Collapsing Strategy
- Desktop multi-column nav collapses to single hamburger icon below 744px
- Product detail layout shifts from side-by-side (image left, info right) to stacked (image top, info below) at tablet breakpoint
- Footer columns collapse from 4-across to 2×2 grid on tablet, single accordion stack on mobile
- Announcement bar text truncates with ellipsis on narrow screens, never wraps to two lines

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extractable from the live site — palette above is based on widely-documented Aarke brand materials and public photography; actual CSS custom properties may differ
- No font-family stacks were extractable — the site likely loads fonts via JavaScript or uses a custom typeface behind anti-bot protection; Helvetica Neue is used as a documented fallback consistent with Scandinavian design brands
- Exact border-radius values could not be confirmed from computed styles
- Animation/transition timing curves (likely subtle ease-out on cart drawer, hover states) are undocumented
- Specific breakpoint values may differ from the 744/1128/1440 assumed here
- Dark-mode variant may exist but was not detectable
- The brass/gold accent (`#b8964e`) is inferred from Aarke's well-known brass finish product line; the exact digital equivalent used on-site may vary
