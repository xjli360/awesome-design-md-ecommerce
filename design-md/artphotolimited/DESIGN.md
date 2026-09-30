---
version: alpha
name: "ArtPhotoLimited"
source_url: "https://www.artphotolimited.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Edition numbers float beneath photographs the way tombstone text appears beneath auction house listings — sparse, authoritative, and final. ArtPhotoLimited operates as a gallery-grade limited edition photography marketplace where the UI's primary job is to disappear: near-white canvases (#f8f7f5, #ffffff), near-black ink (#111111), and a single warm brass accent (#c4a35a) constitute nearly the entire chromatic vocabulary. That restraint is a deliberate claim about the work's primacy — the photograph must be the only thing that carries visual weight. Edition quantities (typically "5 of 25" or "Artist's Proof 2/5") are rendered in spaced uppercase caption type that mimics the pencil notation photographers make on traditional gelatin silver prints. Print sizes are merchandised like bespoke tailoring options — 20×16, 30×24, 40×30 — each with a corresponding price tier displayed in a quiet monospace or tabular-numerals variant so columns align cleanly. The add-to-cart surface uses a near-full-width dark CTA that anchors the product page without competing with the image above it. Navigation favors editorial categories ("Landscape", "Portrait", "Abstract", "Documentary") over conventional faceted filtering, which signals curation over catalog breadth. Artist profile pages read as condensed solo exhibition pamphlets: a brief biography paragraph, a looping grid of their available works, and a link to their CV or statement. Certificates of authenticity — a significant purchase-decision trigger at this price point — are previewed inline with a small facsimile document thumbnail. Typography across the system likely pairs a geometric or humanist sans-serif at large display sizes with a more neutral system serif for body reading. Spacing is generous to the point of austerity: wide margins, tall image containers, and section gaps that read like the silence between gallery rooms. All token refs below — {colors.accent-limited}, {rounded.none}, {spacing.section} — are design-system approximations derived from fine-art print retail conventions; see Known Gaps for extraction status.

colors:
  primary: "#111111"
  primary-active: "#000000"
  primary-disabled: "#999999"
  accent-limited: "#c4a35a"
  accent-limited-muted: "#e8d9b5"
  ink: "#111111"
  body: "#333333"
  muted: "#767676"
  muted-soft: "#a0a0a0"
  hairline: "#e5e5e5"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f8f7f5"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  edition-ink: "#555555"
  price-primary: "#111111"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.02em
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  edition-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  artist-name:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 12px
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
  section: 80px
  section-xl: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 52px
    width: "100% (full-width on product page)"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 15px 31px
    height: 52px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoType: "wordmark, left-aligned"
    paddingX: "{spacing.xl}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3 or 3/4 depending on orientation"
    imageFit: cover
    gap: "{spacing.md}"
    titleTypography: "{typography.title-sm}"
    artistTypography: "{typography.artist-name}"
    editionTypography: "{typography.edition-label}"
    editionColor: "{colors.edition-ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.price-primary}"
    hoverEffect: "image scale(1.02) over 300ms ease"
  edition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.edition-ink}"
    typography: "{typography.edition-label}"
    accentColor: "{colors.accent-limited}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    display: "inline-flex, shows remaining editions e.g. '3 of 25 remaining'"
  print-size-selector:
    backgroundColor: "{colors.canvas}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    padding: "{spacing.md} {spacing.lg}"
    layout: "horizontal pill-list or vertical stack on mobile"
  hero-fullbleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    layout: "full-viewport-height image with centered text overlay"
    overlayOpacity: 0.35
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.caption}"
    ctaComponent: button-primary
  artwork-detail-panel:
    backgroundColor: "{colors.canvas}"
    layout: "two-column: image left ~60%, metadata right ~40%"
    titleTypography: "{typography.display-md}"
    artistTypography: "{typography.artist-name}"
    bodyTypography: "{typography.body-md}"
    priceTypography: "{typography.price-display}"
    editionComponent: edition-badge
    sizeSelectorComponent: print-size-selector
    paddingY: "{spacing.section}"
  artist-profile-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    avatarSize: 80px
    avatarRounded: "{rounded.full}"
    nameTypography: "{typography.display-sm}"
    bioTypography: "{typography.body-md}"
    padding: "{spacing.xxl}"
    linkTypography: "{typography.button-sm}"
    linkColor: "{colors.accent-limited}"
  certificate-preview:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.lg}"
    thumbnailWidth: 64px
    labelTypography: "{typography.caption}"
    descriptionTypography: "{typography.body-sm}"
    accentColor: "{colors.accent-limited}"
  lightbox:
    backgroundColor: "rgba(0,0,0,0.92)"
    textColor: "{colors.on-dark}"
    imageMaxWidth: "90vw"
    imageMaxHeight: "90vh"
    closeButtonRounded: "{rounded.full}"
    captionTypography: "{typography.caption}"
    navigationArrowSize: 48px
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    borderRight: "1px solid {colors.hairline}"
    labelTypography: "{typography.caption}"
    optionTypography: "{typography.body-sm}"
    activeColor: "{colors.ink}"
    inactiveColor: "{colors.muted}"
    width: 240px
    paddingY: "{spacing.xl}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.md} {spacing.base}"
    height: 48px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "none"
  price-tier-label:
    backgroundColor: transparent
    textColor: "{colors.price-primary}"
    mutedColor: "{colors.muted}"
    typography: "{typography.price-display}"
    strikethroughTypography: "{typography.body-sm}"
    layout: "price prominent, size label in caption below"

## Components

### Buttons
**`button-primary`** — A flat, square-cornered ({rounded.none}) black rectangle at 52px tall, spanning full width on product pages. Uppercase tracked lettering in {typography.button-md} reads as a label rather than a shout. Disabled state drops to {colors.primary-disabled} gray with no radius change, preserving the geometric discipline. No hover shadow — instead, a subtle opacity shift from 1.0 to 0.85 on hover signals interactivity without decorative flourish.

**`button-secondary`** — Identical geometry to `button-primary` but inverted: white fill with a 1px {colors.ink} border. Used for secondary actions like "Request More Information" or "Save to Wishlist" alongside the primary add-to-cart. On hover, background fills to a very light {colors.surface-soft} to signal state.

**`button-text-link`** — Inline underlined text at {typography.body-sm}, {colors.ink}. Appears in artist attribution lines ("View all works by [Artist Name]") and within editorial copy. No padding, no background — behaves as a document hyperlink consistent with the gallery-text aesthetic.

### Navigation
**`nav-bar`** — A 64px-tall header on {colors.canvas} with a 1px bottom hairline. The wordmark sits left-aligned; category navigation (Landscape, Portrait, Abstract, Documentary, Artists, About) runs center or right in {typography.nav-link} — small, spaced uppercase with no active underline treatment beyond a subtle weight shift. A cart icon and search icon sit at far right. On editorial/hero pages, a `nav-bar-dark` variant places the same elements over {colors.surface-dark} in {colors.on-dark}.

### Product Card
**`product-card`** — Zero-radius image container with a 4:3 or 3:4 aspect ratio depending on photograph orientation. Below the image: artist name in {typography.artist-name} (a lighter-weight serif, evoking handwritten exhibition labels), work title in {typography.title-sm}, edition status via `edition-badge`, and price in {typography.price-display}. Card hover applies a gentle scale(1.02) on the image over 300ms — the only motion on the page — which reads as the photograph being lifted off a surface rather than a software animation.

### Edition Badge
**`edition-badge`** — A rectangular chip in {colors.surface-soft} containing text like "3 OF 25 REMAINING" in {typography.edition-label} with {colors.accent-limited} brass accent applied to the fraction or count portion. The warm gold against the near-white surface signals scarcity without alarm-red urgency. When an edition is sold out, the badge reads "EDITION SOLD OUT" in {colors.muted} and the CTA button becomes disabled.

### Print Size Selector
**`print-size-selector`** — A horizontal row of rectangular option tiles (or vertical stack on mobile) each showing a print dimension and its corresponding price delta ("20×16 — £195", "30×24 — £295"). Selected tile fills {colors.ink} with {colors.on-primary} text; unselected tiles show a 1px {colors.hairline} border. The component sits between the edition badge and the add-to-cart button in the product detail panel, functioning like a garment size selector but for archival paper dimensions.

### Artwork Detail Panel
**`artwork-detail-panel`** — Two-column layout: the photograph occupies ~60% of viewport width at left in a tall container with no border or drop shadow (the white canvas is the mat); the right column carries the work title in {typography.display-md}, artist name as a linked {typography.artist-name}, a three-sentence description in {typography.body-md}, the edition badge, size selector, price, and add-to-cart button stacked with {spacing.lg} between each element. {spacing.section} padding top and bottom ensures the panel breathes like an uncluttered exhibition wall.

### Hero
**`hero-fullbleed`** — Full-viewport-height image with a 35% dark overlay. A single centered headline in {typography.display-xl} (white, lightweight serif) names a featured artist or collection. A {typography.caption} subline in the same white gives the edition context ("Limited to 25 Prints — From £195"). A `button-primary` CTA — inverted here to white-fill-on-dark, or a `button-secondary` in white border variant — anchors the bottom of the overlay text.

### Certificate Preview
**`certificate-preview`** — A small horizontal strip in {colors.surface-soft} with a 64px thumbnail of the certificate document facsimile at left, and two lines of text at right: "Certificate of Authenticity Included" in {typography.caption} and a supporting sentence in {typography.body-sm}. A subtle {colors.accent-limited} left border (3px) adds the gold-standard visual cue without requiring an icon. Appears just below the edition badge in the product detail panel.

### Lightbox
**`lightbox`** — Opens on image click with a near-black (92% opacity) overlay. The full-resolution image centers in viewport with max constraints of 90vw × 90vh. Left/right navigation arrows are 48px icon buttons in white. A close button sits top-right as a {rounded.full} circle. Caption below the image shows artist name, title, and year in {typography.caption} white.

### Filter Sidebar
**`filter-sidebar`** — A 240px left sidebar on collection pages with filter groups (Category, Artist, Price Range, Format, Size) labeled in {typography.caption} uppercase. Individual filter options use {typography.body-sm} with a checkbox or toggle. Active filters render {colors.ink}; inactive {colors.muted}. On mobile, the sidebar collapses into a bottom sheet triggered by a "Filter" button.

### Artist Profile Block
**`artist-profile-block`** — A {colors.surface-soft} section on product pages and standalone artist pages. An 80px circular avatar floats left; to its right, the artist name in {typography.display-sm} and a 2–3 sentence biography in {typography.body-md}. A "View All Works" link in {typography.button-sm} with {colors.accent-limited} text anchors the block's bottom. The brass link color is the only instance of the accent in a clickable affordance, reinforcing its "premium provenance" role.

### Footer
**`footer`** — Full-width {colors.surface-dark} band with four columns: About / Artists / Categories / Customer Service. Column heads in {typography.caption}, links in {typography.body-sm} {colors.muted-soft}. Bottom row carries copyright, payment mark icons (monochrome), and a newsletter subscribe input + submit button pair in a lighter bordered variant. No decorative border-top — the dark background is a sufficient visual terminus.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; artwork-detail-panel stacks image above metadata; print-size-selector becomes vertical stack; filter-sidebar collapses to bottom sheet; nav-bar hides category links behind hamburger; hero headline drops to {typography.display-md} |
| Tablet | 744–1128px | Two-column grid for collection pages (2-up product cards); artwork-detail-panel maintains two columns at 50/50 split; filter-sidebar may render as a top horizontal filter bar instead of side panel; nav shows 3–4 top categories, rest in overflow |
| Desktop | 1128–1440px | Three-column product grid; artwork-detail-panel at 60/40 split; full nav visible; filter-sidebar at 240px fixed left |
| Wide | > 1440px | Constrained max-width container (~1400px) centered; four-column product grid; generous {spacing.section-xl} vertical rhythm; hero image gains more vertical height |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Print size selector tiles minimum 48px height on touch viewports
- Lightbox navigation arrows expand to 56px hit area on mobile
- Filter toggles and checkboxes minimum 44px tap height

### Collapsing Strategy
- Category navigation collapses to hamburger at < 900px
- Filter sidebar converts to a bottom sheet drawer at < 744px
- Two-column artwork detail panel stacks vertically at < 744px
- Certificate preview thumbnail hides on mobile to reduce height; text remains
- Artist profile block portrait and bio stack vertically at < 500px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — extraction returned zero results, suggesting tokens are loaded via JavaScript at runtime or the site employs anti-bot protections. All color values above are design-system approximations based on fine-art photography print retail conventions, not verified brand assets.
- No font families were detected in extraction. Typography stacks above (Cormorant Garamond / Helvetica Neue) represent plausible genre conventions for premium gallery-adjacent retail; the actual brand may use licensed or custom typefaces not detectable via static extraction.
- No meta theme-color was present, so mobile chrome tint is unspecified.
- The platform is confirmed non-Shopify; the actual e-commerce platform is unknown, which may affect component naming conventions and checkout flow patterns.
- Exact border-radius values could not be confirmed — the {rounded.none} default throughout is a conservative assumption consistent with gallery minimalism, but the brand may use subtle rounding (2–4px) on certain elements.
- Limited edition numbering UI patterns (how sold/remaining counts are displayed, real-time vs. static) are unconfirmed.
- Certificate of authenticity treatment is assumed from category conventions, not extracted markup.
- Hover and transition animation durations are estimated; no motion design documentation was available.
