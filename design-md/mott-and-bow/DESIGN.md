---
version: alpha
name: "Mott & Bow"
source_url: "https://mottandbow.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A burnt-sienna CTA (#e06039) is the brand's one color defection — everything else stays in a disciplined grayscale running from near-black ink (#121212) through three tiers of mid-gray (#3b3b3b, #585858, #777777) to a bone-white canvas. RetroSignature, a hand-lettered script, sits at the logo mark but nowhere else in the UI, leaving the bulk of type work to ProximaNova across four weights — Regular, SemiBold, Bold — and a secondary voice in AmericaMono for label codes and size callouts, the kind of monospaced specificity that signals precision sizing rather than lifestyle vagueness. Bookish, a serif loaded for editorial moments, handles display headlines on campaign pages; its slightly antiquarian character offsets the otherwise utilitarian stack and nudges the brand toward premium without luxury clichés. The interplay between ProximaNova's geometric neutrality and AmericaMono's typewriter cadence creates a dual register — clean commerce up front, workshop exactness in the details.

  The terracotta voltage appears at the single most important moment: the primary CTA. It doesn't migrate to badges, nav accents, or section borders. That restraint amplifies it — every "Shop Now" or "Add to Cart" reads as the unique signal in a room that otherwise speaks only in charcoals and concrete grays. A second accent, the deep orange-red flame (#ff4a00), surfaces for urgency markers like sale banners and stock alerts. Sage-gray (#a1a6a0) appears as an ambient accent for secondary labels and availability states, quieter than muted (#777777) but not as invisible as hairlines. Buttons run with essentially zero rounding ({rounded.xs}) — a flat, almost industrial edge that suits raw denim's no-frills associations.

  Product cards are equally spare: flush image, lean ProximaNova title at 16px, price weight in SemiBold. No shadows, no card borders by default — just the product against white. Navigation uses uppercase letterspaced ProximaNova labels in a thin horizontal strip below a minimal wordmark, keeping top-of-page chrome extremely spare. The deep charcoal-navy (#2d343b) pulls double duty as the darkest surface and footer background, giving page endings a grounded, finished weight. Overall, the system reads as workwear-influenced, denim-native: stripped down, color-restrained, with one hot orange signal to prove the brand knows exactly where to break its own rules.

colors:
  primary: "#e06039"
  primary-active: "#c04d28"
  primary-disabled: "#f0c0ae"
  accent-red: "#980404"
  accent-flame: "#ff4a00"
  dark-navy: "#2d343b"
  sage: "#a1a6a0"
  ink: "#121212"
  body: "#3b3b3b"
  muted: "#777777"
  muted-mid: "#585858"
  hairline: "#dedede"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'Bookish', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Bookish', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.14
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Bookish', Georgia, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'ProximaNova Bold', 'Proxima Nova', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'ProximaNova SemiBold', 'Proxima Nova', 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'ProximaNova Regular', 'Proxima Nova', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'ProximaNova Regular', 'Proxima Nova', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'ProximaNova Regular', 'Proxima Nova', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-mono:
    fontFamily: "'AmericaMono Regular', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.04em
  label-mono-bold:
    fontFamily: "'AmericaMono Bold', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'ProximaNova Bold', 'Proxima Nova', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'ProximaNova Bold', 'Proxima Nova', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'ProximaNova SemiBold', 'Proxima Nova', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'ProximaNova SemiBold', 'Proxima Nova', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  logo-script:
    fontFamily: "'RetroSignature', cursive"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0

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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    transition: background-color 150ms ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.logo-script}"
    logoColor: "{colors.ink}"
    paddingX: "{spacing.xl}"
    gap: "{spacing.xl}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "2px solid {colors.ink}"
    padding: "{spacing.xl}"
    columnGap: "{spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    priceStrikeColor: "{colors.muted}"
    gap: "{spacing.sm}"
    padding: 0px
    swatchSize: 16px
    swatchGap: "{spacing.xs}"
    hoverState: image-swap
  hero-full:
    layout: full-bleed
    minHeight: 80vh
    textPosition: center-left
    textColor: "{colors.on-dark}"
    overlayColor: "{colors.scrim}"
    overlayOpacity: 0.28
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-primary
    paddingX: "{spacing.xxl}"
  hero-split:
    layout: two-column-equal
    imageColumn: right
    textColumn: left
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-md}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    paddingText: "{spacing.xxl}"
  promo-banner:
    backgroundColor: "{colors.dark-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    height: 40px
    textAlign: center
    urgencyColor: "{colors.accent-flame}"
  sale-badge:
    backgroundColor: "{colors.accent-flame}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-mono-bold}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  fit-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-mid}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    border: "1px solid {colors.hairline}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.label-mono}"
    rounded: "{rounded.none}"
    size: 40px
    border: "1px solid {colors.hairline}"
    selectedBorder: "1.5px solid {colors.ink}"
    selectedBackground: "{colors.ink}"
    selectedColor: "{colors.on-dark}"
    unavailableOpacity: 0.3
    unavailableDecoration: line-through
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedRing: "2px solid {colors.ink}"
    selectedRingOffset: 2px
  pdp-sticky-bar:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    height: 72px
    paddingX: "{spacing.xl}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    ctaComponent: button-primary
    zIndex: 100
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 40px
    iconColor: "{colors.muted}"
    border: none
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.dark-navy}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.sage}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.nav-link}"
    linkTypography: "{typography.body-sm}"
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.xl}"
    borderTop: none
    copyrightTypography: "{typography.caption}"
    copyrightColor: "{colors.sage}"

## Components

### Buttons

**`button-primary`** — Uppercase ProximaNova Bold at 13px with 0.1em tracking, this flat-edged ({rounded.xs}) terracotta button (#e06039) is the singular brand accent in an otherwise achromatic interface. On hover it deepens to #c04d28 (`button-primary-active`) via a 150ms ease transition. The disabled state renders in a washed peachy tint (#f0c0ae) at reduced opacity, clearly inert without heavy visual noise.

**`button-secondary`** — Same flat geometry and uppercase type as primary, but inverted to an ink-bordered white fill. Hover flips it to a full ink (#121212) fill with white text — a clean swap that avoids a third color. Used for secondary CTAs like "Save to Wishlist" and size-guide triggers.

**`button-ghost`** — Bare underlined link with no background or border. ProximaNova SemiBold at 11px, uppercase. Used for tertiary actions such as "View full details" within drawers and for breadcrumb-adjacent navigation calls.

### Inputs

**`text-input`** — Square-edged (no rounding), 48px tall, 1px hairline (#dedede) border sharpening to ink on focus. No box shadow, no colored focus ring. ProximaNova Regular at 16px. Matches the flat aesthetic of the button system — no softening curves anywhere in the form layer.

### Navigation

**`nav-bar`** — 56px tall white strip with a 1px bottom hairline. The RetroSignature wordmark sits at center or left at approximately 28px. Nav links are uppercase ProximaNova SemiBold at 13px with 0.06em tracking, ink-colored, with hover state using an underline rather than color change. No background color shifts on scroll. The right cluster holds a search icon, account icon, and a cart counter in the same sparse typographic register.

**`nav-dropdown`** — Opens below the hairline with a 2px solid ink top border (visual anchor), white background, multi-column link grid. Links run in ProximaNova Regular at 14px, body-gray (#3b3b3b). Editorial imagery or a featured product tile may occupy one column on wider viewports.

### Product Cards

**`product-card`** — Flush, borderless, no-shadow cards on a white ground. 3:4 portrait image with a secondary-image swap on hover. Title in ProximaNova Regular 16px/ink, price in ProximaNova Bold 16px below. Sale prices pair the original struck through in muted (#777777) beside the new price in ink. Color swatches (16px circles, full rounding, hairline border, ink selection ring) stack horizontally beneath the price. No card container — the product floats directly on the page surface.

### Hero

**`hero-full`** — Full-bleed campaign image at 80vh minimum. Bookish display headline at 52px sits left-aligned over a 28% opacity dark scrim, paired with a ProximaNova body subhead and a terracotta `button-primary`. Feels editorial rather than promotional — sparse copy, strong photography.

**`hero-split`** — Two equal columns: product image right, editorial text left on a surface-soft (#f0f0f0) ground. Bookish 36px headline, ProximaNova body at 16px, primary CTA below. Used for new-collection or category-entry moments.

### Badges and Labels

**`sale-badge`** — Flat rectangle with no rounding. AmericaMono Bold at 11px with 0.04em tracking, white text on accent-flame (#ff4a00). Appears in the top-left corner of product image frames. The monospaced font signals a tag-like, almost stamped quality.

**`fit-badge`** — Hairline-bordered, surface-soft fill, AmericaMono Regular text in muted-mid (#585858). Used for fit descriptors: "Slim", "Straight", "Relaxed". Groups horizontally beneath the product name on PDPs.

### Size & Color Selectors

**`size-selector`** — 40px square tiles, no rounding. Hairline border at rest, 1.5px ink border selected. Selected tile inverts to ink fill/white text. Unavailable sizes use 0.3 opacity and struck-through label. The monospaced label ensures uniform character width across size codes.

**`color-swatch`** — 20px circles with a 1px hairline border. Selected state gets a 2px ink ring with a 2px offset gap — the ring does not change color by product, keeping selection feedback typographically consistent.

### PDP Sticky Bar

**`pdp-sticky-bar`** — 72px bar pinned to viewport bottom on scroll. White background, 1px top hairline. Left: truncated product title (ProximaNova SemiBold 15px) and price (ProximaNova Bold 16px). Right: `button-primary` at full height. Appears only after the native ATC button scrolls out of view. z-index 100.

### Promo Banner

**`promo-banner`** — 40px dark-navy (#2d343b) strip at page top. Copy in ProximaNova SemiBold button-sm (11px uppercase). Urgency text fragments — countdown timers, "ends tonight" — rendered in accent-flame (#ff4a00). Dismissible via an ink-on-transparent × icon.

### Footer

**`footer`** — Dark-navy (#2d343b) field, white primary text, sage (#a1a6a0) for links and copyright. Headed columns in uppercase ProximaNova SemiBold nav-link style; links in ProximaNova Regular body-sm. No dividers between columns — whitespace carries the separation. Bottom bar contains copyright in caption-size sage text and minimal legal links.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart icon; hero headline drops to display-sm (26px Bookish); pdp-sticky-bar always visible; size selector wraps to scroll row |
| Tablet | 744–1128px | Two-column product grid; nav reveals top-level links, dropdowns on tap; hero-split stacks vertically; promo-banner remains; footer shifts to two-column layout |
| Desktop | 1128–1440px | Three or four-column product grid; full horizontal nav with dropdown hover; hero-full at 80vh; pdp layout two-column (images left, form right) |
| Wide | > 1440px | Max content width ~1440px, page centered; grid may expand to five columns for category pages; hero headline scales toward display-xl ceiling |

### Touch Targets

- All interactive elements minimum 44×44px on mobile; size selector tiles scale to 44px square
- Color swatches expand to 28px on mobile with increased ring offset
- Nav hamburger target is full header height (56px) × 48px wide
- Promo banner dismiss × target is 44×44px regardless of visual size

### Collapsing Strategy

- Nav: full horizontal → hamburger drawer (full-height, slides from left, dark-navy background, white links)
- Footer: four columns → two columns (tablet) → single accordion (mobile, each heading toggles its link group)
- Product grid: 4-col → 3-col (tablet) → 2-col (mobile); no single-column fallback for products
- Hero-split: two columns → stacked (image above, text below) at tablet breakpoint
- PDP image gallery: thumbnail strip sidebar → swipe carousel on mobile
- Filter sidebar: persistent left rail (desktop) → bottom sheet drawer (mobile)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; status bar color on mobile Safari/Chrome is unconfirmed
- Exact button height and padding values inferred from typographic scale — not confirmed via computed styles
- ProximaNova weight names ("Semibold" vs "SemiBold" inconsistency in font stacks) suggest possible mixed asset loading; canonical weight values unconfirmed
- Bookish font metrics (x-height, specific weights available) not extractable; editorial usage inferred from font-family presence
- RetroSignature: usage beyond wordmark is unconfirmed; may be a decorative asset rather than a live web font
- Exact nav height, dropdown column count, and sticky-bar breakpoint threshold not extracted
- No confirmed border-radius value for any UI element; {rounded.xs} (2px) inferred from denim/utilitarian brand conventions
- Hover states for product cards (image swap vs zoom vs overlay) not confirmed — image-swap assumed
- No design token file or CSS custom property sheet accessible; all values derived from computed color sampling
