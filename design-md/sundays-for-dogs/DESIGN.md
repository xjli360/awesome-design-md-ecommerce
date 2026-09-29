---
version: alpha
name: "Sundays for Dogs"
source_url: "https://sundaysfordogs.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The marigold-yellow primary (#f2d001) set against warm parchment (#fff4e6) is an unusual design bet for pet food — most competitors reach for clean white or clinical blue, but Sundays bets on something that reads like a Saturday farmer's market stall, grain sacks in sunlight. Monument, a wide geometric display sans, carries the brand's top-of-funnel declarations at scale while Garamond Book and Garamond Light handle the ingredient narrative below, producing a bifurcated typographic register: geometry for the shout, old-press serif for the story. Deep forest greens (#003005, #116600) anchor everything — appearing in text, borders, and dense illustrative foliage — so the warmth of the yellow reads as earned rather than cheery. The warm canvas (#fff4e6) is not a lazy off-white but a baked, slightly orange-tinted parchment that makes the brand feel edible-adjacent even before a product image loads. Secondary yellows (#ffdf5d, #ffda00, #ffed80) modulate the primary across hover, badge, and disabled states without ever abandoning the hue family — the palette has the internal consistency of a recipe, not a mood board. Sage (#abb39c) plays supporting role as a desaturated mid-tone, appearing in ingredient chips, secondary borders, and muted labels where the green family would be too loud. Pill-shaped badges (`{rounded.full}`) label protein source, production method, and certifications directly on product cards, making regulatory-speak feel like a menu callout. Alert and status colors (#ff0000, #008000) are strictly utilitarian — form validation, stock status — and carry zero brand weight. The subscription model surfaces through a persistent warm-tinted callout component, using golden yellows and the deep forest ink to frame recurring-delivery offers as a household staple rather than a cost-saving transaction.

colors:
  primary: "#f2d001"
  primary-active: "#d5b901"
  primary-disabled: "#ffed80"
  primary-warm: "#ffdf5d"
  primary-gold: "#ffda00"
  ink: "#003005"
  body: "#024108"
  muted: "#abb39c"
  hairline: "#e6e6e6"
  hairline-soft: "#f2e9dd"
  canvas: "#fff4e6"
  surface-soft: "#f2e9dd"
  surface-card: "#fcfcfc"
  surface-neutral: "#f7f7f7"
  on-primary: "#003005"
  on-dark: "#fff4e6"
  forest: "#003005"
  meadow: "#116600"
  sage: "#abb39c"
  parchment: "#fff8f0"
  error: "#ff0000"
  success: "#008000"
  warning: "#ff6900"
  info-blue: "#8bd3e6"
  info-purple: "#c98bdb"

typography:
  display-xl:
    fontFamily: "'Monument', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Monument', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Monument', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Monument', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Garamond Book', Garamond, Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'Garamond Book', Garamond, Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Garamond Book', Garamond, Georgia, serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Garamond Light', Garamond, Georgia, serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Garamond Light', Garamond, Georgia, serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Monument', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Monument', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.04em
    textTransform: uppercase
  label-caps:
    fontFamily: "'Monument', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  price:
    fontFamily: "'Monument', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.1
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
    rounded: "{rounded.full}"
    padding: "14px 32px"
    height: 48px
    border: "none"
    hover:
      backgroundColor: "{colors.primary-active}"
    disabled:
      backgroundColor: "{colors.primary-disabled}"
      textColor: "{colors.sage}"

  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: "13px 31px"
    height: 48px
    border: "2px solid {colors.ink}"
    hover:
      backgroundColor: "{colors.ink}"
      textColor: "{colors.on-dark}"

  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "0 0 2px"
    border: "none"
    borderBottom: "1px solid {colors.ink}"

  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.sage}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.meadow}"
    padding: "12px 16px"
    height: 48px

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    ctaButton:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.full}"
      typography: "{typography.button-sm}"
      padding: "10px 20px"

  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    badgeStack: "top-left"
    padding: "{spacing.base}"
    hover:
      boxShadow: "0 4px 20px rgba(0, 48, 5, 0.10)"

  hero:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.title-md}"
    subheadColor: "{colors.body}"
    minHeight: "560px"
    layout: "split-image-right"
    ctaPrimary:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.full}"
      typography: "{typography.button-md}"

  ingredient-badge:
    backgroundColor: "{colors.primary-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "5px 12px"
    variants:
      sage:
        backgroundColor: "{colors.sage}"
        textColor: "{colors.canvas}"
      forest:
        backgroundColor: "{colors.forest}"
        textColor: "{colors.on-dark}"
      outline:
        backgroundColor: "transparent"
        textColor: "{colors.ink}"
        border: "1px solid {colors.ink}"

  subscription-callout:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    ctaButton:
      backgroundColor: "{colors.ink}"
      textColor: "{colors.on-dark}"
      rounded: "{rounded.full}"
      typography: "{typography.button-md}"
    savingsBadge:
      backgroundColor: "{colors.canvas}"
      textColor: "{colors.ink}"
      rounded: "{rounded.full}"
      typography: "{typography.label-caps}"

  recipe-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.lg}"
    imageBorderRadius: "{rounded.md}"
    nameTypography: "{typography.display-sm}"
    nameColor: "{colors.ink}"
    descTypography: "{typography.body-sm}"
    descColor: "{colors.body}"
    proteinBadge:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      rounded: "{rounded.full}"
      typography: "{typography.badge}"
    ingredientList:
      typography: "{typography.body-sm}"
      color: "{colors.body}"
      bulletColor: "{colors.meadow}"

  nutrition-facts-panel:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "2px solid {colors.ink}"
    headingTypography: "{typography.display-sm}"
    headingColor: "{colors.ink}"
    labelTypography: "{typography.label-caps}"
    labelColor: "{colors.body}"
    valueTypography: "{typography.title-sm}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.lg}"

  why-sundays-strip:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    iconAccentColor: "{colors.primary}"
    layout: "3-column-grid"
    padding: "{spacing.section} {spacing.xl}"

  trust-badge-row:
    backgroundColor: "transparent"
    iconColor: "{colors.meadow}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.body}"
    layout: "horizontal-scroll-mobile"
    gap: "{spacing.xl}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.sage}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.label-caps}"
    headingColor: "{colors.primary}"
    dividerColor: "#116600"
    copyrightTypography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — Pill-shaped (#9999px radius) marigold (#f2d001) button with deep forest ink (#003005) text in all-caps Monument at 14px. The fully-rounded pill is the brand's dominant CTA shape, appearing on hero sections, product pages, and subscription upsells. On hover the background darkens to #d5b901; disabled states drop to #ffed80 with sage text to signal unavailability without hard grey.

**`button-secondary`** — Transparent background with a 2px solid #003005 border and ink text, same pill shape and Monument uppercase type as the primary. Hover inverts to forest fill with cream text, making the toggle feel decisive rather than soft.

**`button-ghost`** — Zero background, no border radius, underline-only decoration. Used inline in editorial copy and footer navigation where a button-styled element would be visually intrusive. Keeps Monument uppercase at 12px.

### Inputs

**`text-input`** — Light card surface (#fcfcfc) with a 1px #e6e6e6 hairline border, softly rounded at 8px. Focus state shifts the border to meadow green (#116600) — the only moment a non-yellow accent appears in a transactional element. Garamond Book 17px for entered text; sage (#abb39c) placeholder.

### Navigation

**`nav-bar`** — 64px warm parchment (#fff4e6) bar with a 1px hairline bottom border. Logo sits left; links center in Helvetica Neue 14px medium. A pill-shaped primary CTA ("Try Sundays") anchors the right end, ensuring the subscription offer is visible at every scroll position. On mobile the nav collapses to hamburger with a full-height drawer on the forest green (#003005).

### Product Cards

**`product-card`** — Rounded-12px card on #fcfcfc with subtle 1px hairline border. Product imagery fills the top portion with matching 12px corner clip. Ingredient badges stack in the top-left corner. Name in Garamond Book 18px ink; price in Monument 20px bold; a short descriptor line in Garamond Light 14px sage. Hover lifts a soft green-tinted shadow. Subscribe-and-save pricing appears as a secondary price line in meadow green below the full-price display.

### Hero

**`hero`** — Split-layout: copy left, lifestyle photography right, full-bleed on warm parchment (#fff4e6). Headline uses Monument display-xl at up to 64px in forest ink. Subheadline drops to Garamond Book 22px for ingredient and origin narrative. CTA is the full pill primary button. A trust-badge row runs beneath the CTA stack — human-grade, vet-developed, USDA-approved — in caption-size Garamond Light with meadow-green check icons.

### Ingredient Badges

**`ingredient-badge`** — Small all-caps pill chips in three variants: golden-yellow (#ffdf5d background, forest ink text) for protein sources and hero ingredients; sage (#abb39c background, cream text) for secondary attributes; and forest (#003005 background, cream text) for certification marks. Applied liberally on product cards and recipe detail pages, acting as scannable visual shorthand for ingredient quality claims.

### Subscription Callout

**`subscription-callout`** — Full-width section in primary marigold (#f2d001), with a forest ink CTA button and a small pill badge showing savings percentage in warm parchment. Headline in Monument display-sm; body copy in Garamond Book. The contrast between the yellow field and the dark button creates strong visual separation without introducing a third color.

### Recipe Card

**`recipe-card`** — Used on PDP and recipe index pages. Surface-soft (#f2e9dd) card with 20px radius. Product name at Monument display-sm scale; ingredient list in Garamond Light with meadow-green bullet dots. A protein-source badge in golden pill sits beneath the name. The warm parchment surface distinguishes recipe cards from the white product cards in mixed-content grids.

### Nutrition Facts Panel

**`nutrition-facts-panel`** — Mimics a physical nutrition label: 2px solid forest ink border, all-caps Monument label text, Garamond Book values, and hairline dividers between nutrient groups. Intentional reference to FDA label design gives the panel immediate legibility credibility without lengthy explanatory copy.

### Why Sundays Strip

**`why-sundays-strip`** — Full-bleed forest green (#003005) section with three-column icon-plus-copy layout. Headline in Monument display-md in parchment white; body in Garamond Book; icon accent dots in primary marigold. This is the brand's trust-building register, answering skepticism about air-dried versus kibble in warm, credible tones.

### Footer

**`footer`** — Deep forest ink (#003005) background. Section headings in label-caps Monument, primary yellow; body links in Garamond Light sage (#abb39c), hovering to primary yellow. A divider hairline in meadow green (#116600) separates the link grid from the legal strip. Copyright in Garamond Light 12px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hero becomes single-column, image stacks below copy; nav collapses to hamburger + forest green full-height drawer; product cards go 1-column; ingredient badge row wraps to 2 lines; subscription callout becomes stacked block |
| Tablet | 744–1128px | Hero split holds but image shrinks to 45%; product cards shift to 2-column grid; nav links visible but compressed; why-strip collapses to 2-column + 1 below |
| Desktop | 1128–1440px | Full split hero; 3–4 column product grid; nav at full width with visible link set and pill CTA; why-strip at 3-column |
| Wide | > 1440px | Content max-widths cap around 1280px; hero padding expands; section gutters increase to {spacing.xxl}; product grid may surface a 4th column |

### Touch Targets

- All pill buttons maintain minimum 48px height on mobile
- Nav hamburger and close icon target is 44×44px minimum
- Ingredient badge chips are 32px minimum height on mobile, with 8px vertical padding
- Add-to-cart and subscribe CTAs on mobile are full-width (100%) to maximize tap area

### Collapsing Strategy

- Navigation: links collapse immediately to hamburger at < 744px; drawer slides from right over forest green overlay
- Hero: image drops below copy block on mobile; headline scales from 64px → 36px (display-lg → display-md)
- Why-strip: 3-col → 2-col at tablet, 1-col on mobile; items stack with left-aligned icon+text pairs
- Recipe cards: grid goes 2-col → 1-col at mobile; image aspect ratio crops to 16:9 from square
- Nutrition panel: full width on mobile, max 480px on desktop, centered

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Monument font files were not directly observed in extraction; weight variants beyond 700 are inferred from visual patterns and common Monument usage conventions
- Garamond Light vs Garamond Book weight assignments to specific components are approximated — the site likely uses a single Garamond family instance with weight values 300/400 rather than separate named files
- Exact button padding and height values were not extracted from computed styles; 48px height and 14px/32px padding are inferred from brand-appropriate DTC conventions
- Hover and focus state colors were not confirmed via interaction recording; active-state values (#d5b901) are derived from the extracted palette's next-darkest yellow
- Animation/transition durations for card hovers, drawer open, and badge entry are unknown
- Mobile nav drawer design (color, animation direction, link size) is inferred — not extracted
- Dark-mode support is unknown; no dark canvas colors were present in the extraction
- Exact grid column counts and gutter sizes for the product listing page were not confirmed
