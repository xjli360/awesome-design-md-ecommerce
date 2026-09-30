---
version: alpha
name: "HyperShop"
source_url: "https://www.hypershop.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  At rest, HyperShop's interface is nearly indistinguishable from the dark glass face of the devices it powers — the canvas sits at #121212, barely eighteen lux above true black, while product surfaces layer upward through #171717 and #1f1f1f in increments that read as material depth rather than color contrast. The lone departure from this monochrome compression is #dedede, a cool silver-gray that carries all readable text and every primary interactive signal; it is not white — its slight desaturation avoids the clinical glare of #ffffff and recalls the brushed aluminum chassis of the HyperDrive docks and HyperJuice battery packs the store sells. This single non-black value does the work of a full accent palette: it fills primary buttons, anchors product names on dark cards, and marks active category tabs, because contrast alone is strong enough against the near-black stack below. Typography runs through a proprietary font family — myFontLight, myFontRegular, myFontMedium, myFontBold — with Inter as the system fallback, a stack that signals custom brand investment while keeping OS rendering crisp at small sizes. The four named weights let a single typeface handle the range from 11px all-caps specification labels set in myFontMedium with 1.2px tracking, to 48px hero headlines in myFontBold, without importing a display face or a contrasting serif. Rounded corners hold at {rounded.xs} and {rounded.sm} throughout — 4px and 8px respectively — a range that reads as precisely machined rather than friendly or organic; there are no pill shapes or full radii in the core UI. The overall effect is a storefront that behaves like a settings screen from the device's own operating system: monochromatic, deliberate, and confident that the hardware will provide the color.

colors:
  primary: "#dedede"
  primary-active: "#ffffff"
  primary-disabled: "#404040"
  ink: "#dedede"
  body: "#c4c4c4"
  muted: "#888888"
  hairline: "#2c2c2c"
  canvas: "#121212"
  surface-soft: "#171717"
  surface-card: "#1f1f1f"
  on-primary: "#121212"
  on-dark: "#dedede"
  theme-chrome: "#171717"
  sale-red: "#c0392b"

typography:
  display-xl:
    fontFamily: "myFontBold, Inter, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "myFontBold, Inter, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "myFontMedium, Inter, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "myFontMedium, Inter, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "myFontMedium, Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "myFontRegular, Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "myFontRegular, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "myFontLight, Inter, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "myFontMedium, Inter, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  price:
    fontFamily: "myFontBold, Inter, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "myFontBold, Inter, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "myFontMedium, Inter, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "myFontMedium, Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  logo-display:
    fontFamily: "myFontBold, Inter, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px

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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary-active}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.ink}"
    backgroundColor: "{colors.surface-card}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
  nav-bar-logo:
    typography: "{typography.logo-display}"
    textColor: "{colors.primary-active}"
  category-tab-active:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
  category-tab-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid transparent"
    paddingBottom: "{spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 44px
    iconColor: "{colors.muted}"
    iconColorActive: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid transparent"
    imageAspectRatio: "1/1"
    imageFit: contain
  product-card-hover:
    border: "1px solid {colors.hairline}"
    backgroundColor: "{colors.surface-card}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xxl}"
    textAlign: left
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.primary-active}"
  hero-subheadline:
    typography: "{typography.display-sm}"
    textColor: "{colors.body}"
    marginTop: "{spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
    marginTop: "{spacing.xl}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rowPadding: "12px 0"
    divider: "1px solid {colors.hairline}"
  product-image-viewer:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    thumbnailBorder: "2px solid {colors.hairline}"
    thumbnailBorderActive: "2px solid {colors.primary}"
    thumbnailSize: 64px
    thumbnailGap: "{spacing.sm}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.sale-red}"
    textColor: "#ffffff"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  tooltip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "8px 12px"
    maxWidth: 240px
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.xxl}"
    linkColor: "{colors.ink}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.primary}"

## Components

### Buttons

**`button-primary`** — Light-on-dark filled button using #dedede as the fill and #121212 as the label color, creating an inverted-display effect that reads as active rather than washed out against the dark canvas. Active state steps up to full #ffffff fill; disabled state drops to the #404040 background with muted text at {colors.muted}, keeping the element spatially present without affording interaction. Corners hold at {rounded.xs} (4px) — matching the machined-edge aesthetic of the hardware product category.

**`button-secondary`** — Transparent background with a 1px {colors.hairline} border and {colors.ink} text at rest. Hover state fills with {colors.surface-card} and sharpens the border to 1px {colors.primary}, creating subtle depth. Used for secondary actions like "Compare," "Learn More," or modal dismissal alongside primary add-to-cart flows.

**`button-ghost`** — Borderless, transparent, {colors.ink} text at {typography.button-sm}. Appears for in-context navigation-style actions within spec tables, accordion bodies, and inline "See all" links.

### Search

**`search-bar`** — A 44px-tall input variant on {colors.surface-card} with a 1px {colors.hairline} border and {rounded.xs} corners. Search icon sits at {colors.muted} at rest, sharpening to {colors.ink} on first keystroke. Results surface as a {colors.surface-card} dropdown below the bar with per-result product thumbnails and names in {typography.title-sm}.

### Navigation

**`nav-bar`** — 64px bar in {colors.surface-soft} (#171717) separated from the page by a 1px {colors.hairline} bottom border. Category links render in {typography.nav-link}; the logo in {typography.logo-display} colored {colors.primary-active} (white). Active category receives a 2px {colors.primary} underline via the `category-tab-active` spec; inactive categories use {colors.muted} text and a transparent underline, making the tab selection read as a state rather than a selection widget.

### Product Card

**`product-card`** — Sits on {colors.surface-card} (#1f1f1f) with {rounded.sm} corners and a transparent border at rest that upgrades to 1px {colors.hairline} on hover. Product images display at 1:1 aspect ratio with `contain` fit — required for the varied form factors of docks, cable adapters, and battery packs, which cannot be safely cropped. Name in {typography.title-sm}, price in {typography.price} at {colors.primary}.

### Hero

**`hero`** — Full-width section on raw {colors.canvas} (#121212) with left-aligned text layout. The headline renders in {typography.display-xl} at {colors.primary-active} (white) for maximum contrast; the subheadline in {typography.display-sm} at {colors.body} for tonal separation. The primary CTA uses the `hero-cta` spec with 32px horizontal padding. On mobile, type scale steps down one level and the layout becomes center-aligned with the product image repositioned below the text block.

### Spec Table

**`spec-table`** — A two-column key-value layout used extensively on product detail pages for port counts, wattage ratings, and compatibility lists. Labels set in {typography.spec-label} (11px, uppercase, 1.2px tracking) at {colors.muted}; values in {typography.body-sm} at {colors.body}. Rows are separated by 1px {colors.hairline} dividers with 12px vertical padding each. The table renders directly on {colors.canvas} without any surface elevation — it reads as editorial content rather than a UI component.

### Product Image Viewer

**`product-image-viewer`** — Main image in a {colors.surface-card} panel with {rounded.sm} corners. A thumbnail strip (64px tiles, {spacing.sm} gaps) sits below; the active thumbnail receives a 2px {colors.primary} border while inactive ones hold a 2px {colors.hairline} border. The {colors.surface-card} background is load-bearing: product images often have transparency and need a non-black backing to avoid merging with the canvas.

### Badges

**`badge-new`** — A 4px-rounded label on {colors.primary} fill with {colors.on-primary} text in {typography.caption}. Appears in the top-left corner of product card images for recently released SKUs. **`badge-sale`** — Identical geometry on {colors.sale-red} fill (#c0392b) for discounted items.

### Tooltip

**`tooltip`** — Appears on hover over spec icons and "?" labels in product configurator rows. Rendered on {colors.surface-card} with a 1px {colors.hairline} border, {rounded.xs} corners, {typography.caption} text at {colors.body}, and a 240px max-width to keep spec copy readable.

### Footer

**`footer`** — Full-width on {colors.canvas} with a 1px {colors.hairline} top border and {spacing.xxl} vertical padding. Section headings in {typography.title-sm} at {colors.primary}; link text in {typography.body-sm} at {colors.ink}; legal and copyright copy in {colors.muted}. Renders as a four-column grid on desktop, collapses to stacked accordions on mobile with tappable heading toggles.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with drawer; hero text centers and product image moves below copy; spec table scrolls horizontally; footer collapses to accordions |
| Tablet | 744–1128px | Two-column product grid; nav shows logo and search bar with hamburger for categories; hero retains left alignment; footer shifts to two-column grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with all category links and search visible; hero gains side-by-side image layout; spec table full-width two-column |
| Wide | > 1440px | Content constrained to 1440px max-width and centered; four-column product grid; hero background extends edge-to-edge behind the content container |

### Touch Targets

- All interactive elements minimum 44×44px tap region regardless of visual size
- Nav hamburger icon: 44×44px tap zone with {spacing.sm} internal padding
- Product card: entire card surface is tappable, not just the name or image region
- Image viewer thumbnails: minimum 44px tap zone even when rendered at 64px visual size
- Add to Cart / Buy Now: full-width on mobile (100% minus {spacing.lg} side margins)
- Category tab strip: individual tabs min 44px height; strip scrolls horizontally on mobile

### Collapsing Strategy

- Footer links collapse to tap-to-expand accordions at < 744px; section headings remain visible as toggles
- Category nav folds to a horizontal scroll strip on tablet and into a hamburger drawer on mobile
- Spec tables reflow to stacked card rows (label above value) on mobile to avoid horizontal overflow
- Hero two-column layout (text + image) collapses to stacked single-column on mobile, image second
- Image viewer thumbnail strip switches from a vertical left-rail (desktop optional) to a horizontal scroll row on mobile and tablet
- Search bar moves from inline in the nav to a full-width bar below the logo row on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand accent color detected — HyperShop likely uses a highlight color (possibly cyan, electric blue, or orange) loaded via JavaScript or injected through a theme asset; all interactive accent and badge colors in this spec are approximated from the extracted near-black and silver-gray palette
- Only four hex values extracted (#171717, #1f1f1f, #dedede, #121212); muted, hairline, body, and all derived intermediate tones are reasoned interpolations between the extracted endpoints, not confirmed computed values
- Badge sale color (#c0392b) is a conventional alert red derived from general UI practice, not extracted from the site
- Custom font family "myFont" (myFontBold, myFontLight, myFontMedium, myFontRegular) is present in the CSS font-family stack but the foundry name, actual weight integers, and license terms are unconfirmed; Inter is the specified fallback
- Exact font sizes, line heights, and letter-spacing values for the proprietary myFont family are not extractable from static hints and are inferred from category conventions
- Logo treatment (wordmark, monogram, or icon lockup) not determinable from extraction
- Dark/light mode toggle presence unknown — the #171717 theme-color meta tag signals dark-mode-first, but a light theme may exist
- Hover animation durations and easing curves not extractable from static page hints
- Cart drawer, checkout flow, and account page component patterns not captured
