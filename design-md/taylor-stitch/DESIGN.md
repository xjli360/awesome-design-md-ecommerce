---
version: alpha
name: "Taylor Stitch"
source_url: "https://taylorstitch.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Taylor Stitch runs its entire visual logic from a single deep chamber — #0f2130, a midnight navy so dark it reads almost as black at small sizes, pressed into every primary CTA, the site header, and the footer band. Against that near-black ground, a flash of seafoam (#aadddd) and a muted forest green (#3d8144) operate as the only relief — not as playful accents but as gear-check markers, the kind of color that might appear on a topographic map overlay or a waxed canvas label tab. The canvas is clean white (theme-color: #fff), and surface softs land on a neutral #eeeeee; the site trusts photography of worn-in denim and Chromexcel leather to carry warmth, not the UI shell. Typography arrived at extraction as Arial/Helvetica — almost certainly a fallback scaffold beneath JS-loaded custom fonts. At scale, display headlines feel heavy and compressed (estimated 700 weight), product titles live at a confident 18–20px at weight 600, and body copy runs at 15–16px with relaxed line-height to suit long editorial paragraphs about fabric provenance and workshop pre-orders. The Workshop model — Taylor Stitch's crowdfunding-before-production mechanic — introduces a badge vocabulary that sets it apart from standard apparel e-commerce: WORKSHOP tags, funding-progress bars, and funded-state badges must all resolve against the same dark primary palette rather than borrowing the coral (#ff9966) or soft yellow (#ffffae) seasonal tones. Olive (#8b8e77) reads as a muted earth finish; warm coral and lemon yellow appear as campaign-specific tokens rather than permanent brand fixtures. Rounded corners lean minimal — nearly square buttons and cards, with only a small `{rounded.xs}` radius on form inputs and `{rounded.full}` applied strictly to progress-bar fills and color swatches. The overall geometry feels engineered and purposeful, echoing the functional workwear heritage of the label: nothing decorative, every radius earned. Spacing is generous in editorial sections — large photo-first hero layouts, full-bleed collection imagery — but tightens in the product grid, where density and clear pricing hierarchy dominate.

colors:
  primary: "#0f2130"
  primary-active: "#1a3346"
  primary-disabled: "#8b9ba8"
  ink: "#0f2130"
  body: "#2f3e4b"
  muted: "#aaaaaa"
  hairline: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-seafoam: "#aadddd"
  accent-green: "#3d8144"
  accent-olive: "#8b8e77"
  accent-coral: "#ff9966"
  accent-yellow: "#ffffae"
  workshop-progress: "#3d8144"
  funded-badge: "#3d8144"
  scrim: "#0f2130"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-upper:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.5px
  workshop-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 2px
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
    padding: "14px 24px"
    height: 48px
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
    padding: "13px 23px"
    height: 48px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "13px 23px"
    height: 48px
    border: "1px solid {colors.on-primary}"
  button-workshop:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "14px 24px"
    height: 48px
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    padding: "12px 16px"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: none
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    height: 40px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBorderRadius: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.sm}"
    border: none
  workshop-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.workshop-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    position: absolute-top-left
  workshop-progress-bar:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.workshop-progress}"
    height: 4px
    rounded: "{rounded.full}"
  funded-badge:
    backgroundColor: "{colors.funded-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.workshop-label}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    position: absolute-top-left
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 600px
    layout: full-bleed
    overlayScrim: "rgba(15,33,48,0.4)"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    activeTextColor: "{colors.primary}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.primary}"
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    height: 44px
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.primary}"
    selectedRingOffset: 2px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: none
    height: 44px
    padding: "0 {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.caption-upper}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Solid midnight navy (#0f2130) rectangle with zero border-radius, white uppercase-tracked text at 700 weight and 1px letter-spacing. Height is 48px. Active state shifts to `#1a3346`; disabled state mutes the fill to `#8b9ba8` while keeping white label text. Used for every primary commerce action: Add to Cart, Checkout, Shop Now.

**`button-secondary`** — White fill with a 1px navy border, matching `button-primary` dimensions exactly. Used for secondary actions — Learn More on editorial modules, Wishlist toggles on PDPs — where the navy fill would visually outcompete surrounding content.

**`button-ghost`** — Transparent background with 1px white border and white text. Appears over dark hero imagery and full-bleed campaign banners where neither the navy fill nor the white fill would be legible. Same height and typography as `button-primary`.

**`button-workshop`** — Forest green (#3d8144) fill, white text, zero radius, same 48px height. Exclusive to Workshop product pages and funding-stage CTAs. Its green signals "this product is in active pre-order" and must not be reused outside that context.

### Navigation

**`nav-bar`** — Full-width midnight navy bar at 56px height. White nav-link text (14px, 600 weight, 0.5px tracking). Desktop exposes primary category links (Shop, Workshop, Journal, About); mobile collapses to a hamburger that opens a full-screen drawer. No bottom border — the dark background provides sufficient separation from the page below.

**`announcement-bar`** — Sits above `nav-bar`, sharing the #0f2130 background. Caption-upper typography (11px, 700 weight, 1.5px letter-spacing, uppercase) in white, centered. Carries shipping thresholds, Workshop funding milestones, and campaign callouts.

### Product Card

**`product-card`** — No border, no border-radius; the grid gutter provides visual separation. Photography is always full-bleed square (1:1 ratio). Title uses `{typography.title-sm}` in `{colors.ink}`. Price uses `{typography.price-display}` (700 weight, 16px). Workshop products show a `workshop-badge` overlay at top-left of the image. Color swatches render as 24px circles beneath the title with a 2px navy ring on selection. On hover, a secondary image (model lifestyle shot) replaces the product flat.

### Workshop Components

**`workshop-badge`** — A flat navy rectangle (zero radius) positioned absolute top-left over product card imagery. All-caps "WORKSHOP" text at 10px, 700 weight, 2px tracking in white. Indicates the product is in the pre-order funding phase.

**`workshop-progress-bar`** — A full-width 4px pill bar rendered below the workshop product title on collection pages and PDPs. Track is `{colors.hairline}` (#eeeeee); fill is forest green `{colors.workshop-progress}`. Accompanied by a `{typography.caption}` label reading "74% Funded" or similar milestone text.

**`funded-badge`** — Identical geometry to `workshop-badge` but uses `{colors.funded-badge}` green fill. Signals a successfully funded workshop product still available for late-backer pre-order.

### Hero

**`hero`** — Full-bleed imagery with a navy scrim overlay (`rgba(15,33,48,0.4)`) to guarantee white headline and ghost-button contrast. Minimum 600px tall on desktop. Headline in `{typography.display-xl}` (48px, 700 weight). Body copy in `{typography.body-md}`. CTA pattern: `button-primary` + `button-ghost` side by side; on mobile, buttons stack vertically to full width.

### Forms and Inputs

**`text-input`** — White fill, 1px `{colors.hairline}` border, 4px radius. On focus, border upgrades to 1px `{colors.primary}` navy. Height 48px with 16px horizontal padding. Error state uses a 1px red border (no dedicated error-color token extracted — flag as gap).

**`size-selector`** — Square tiles (zero radius) for apparel size selection, 44px height. Default: white background, 1px hairline border. Selected: navy fill, white text. Out-of-stock: diagonal strikethrough over `{colors.muted}` text.

**`color-swatch`** — 24px circles per color option. A 2px navy ring with 2px offset indicates the selected swatch; ring renders correctly on both white and dark surfaces.

**`search-bar`** — Surface-soft (#eeeeee) background, 4px radius, no border. 44px height. Sits in a dropdown panel triggered from the nav, not inline in the nav bar itself.

### Footer

**`footer`** — Full-width navy block matching `nav-bar` background. Column headings use `{typography.caption-upper}` (11px, 2px tracking, uppercase) in white. Link text uses `{typography.body-sm}` at 14px, white. Section padding at `{spacing.section}` (64px) top and bottom. Newsletter signup embed uses `text-input` with an inverted border color for visibility on dark ground.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline scales to `display-sm` (24px); announcement bar condenses to single scrolling line; buttons stack full-width |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories with secondary links in drawer; hero retains full-bleed with side-by-side CTA buttons |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav visible; workshop progress bars and funded badges surface inline in product cards |
| Wide | > 1440px | Max-width container (~1440px) centered with symmetric side margin; hero imagery scales without upsampling artifacts |

### Touch Targets

- All buttons, nav links, size tiles, and swatches meet 44×44px minimum touch target
- Size selector tiles expand to 44px minimum height on mobile regardless of label length
- Color swatches maintain 24px visual size with transparent 44px tap area via padding

### Collapsing Strategy

- Desktop mega-menu nav collapses to a full-screen slide-in drawer on mobile; category list is vertically scrollable
- Workshop funding progress bar hides on mobile product-card thumbnails — visible only on the Workshop collection page and individual PDPs
- Filter panel transitions from a sidebar (desktop) to a bottom sheet (mobile)
- Footer four-column grid collapses to a single-column accordion with expandable sections on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Custom webfonts not captured**: Only Arial/Helvetica (system fallbacks) were extracted. Taylor Stitch almost certainly loads a custom geometric sans-serif (possibly Aktiv Grotesk, Founders Grotesk, or a similar neutral-humanist face); all font-family tokens should be updated once confirmed via DevTools network inspection
- **Hover-state intermediates**: No hover colors between default and active were captured; `primary-active` (#1a3346) is an approximation from darkening primary — verify against computed styles
- **Error and validation states**: No error-red color was surfaced in extraction; form error borders and inline messages are unspecified
- **Exact button radius**: Zero radius (`{rounded.none}`) is the conservative spec based on brand workwear aesthetic; confirm against live computed border-radius values before finalizing
- **iOS system blue (#007aff)**: Appears in extracted palette — almost certainly a browser or Shopify framework default for hyperlinks, not a Taylor Stitch brand token; excluded from palette
- **Seasonal accent palette usage contexts**: Coral (#ff9966) and soft yellow (#ffffae) appear in extraction but their precise placement (campaign banners, seasonal collection headers, sale states) is unconfirmed; treat as optional tokens until verified
- **Dark mode**: No dark-mode token variants detected; the site may implement none
- **Workshop funding percentage thresholds**: Color behavior of the progress bar at 0%, 100%, and over-funded states is unspecified
