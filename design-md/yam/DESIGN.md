---
version: alpha
name: "Yam"
source_url: "https://www.yamnyc.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The name carries deliberate earthiness — a root vegetable dropped into New York's demi-fine jewelry landscape, declaring that ornamentation needn't perform preciousness to earn its place on a body. Yam's visual system earns its sustainability claim through a deep forest green (#0d4f3d) deployed as the primary action color, then softened through a four-step ramp — #4b916d, #97c693, #bde2a7, through to petal-pale #effae5 — that reads like a cross-section of living material rather than a brand-color kit. The neutral axis runs notably warm: parchment (#f1f0ef) and ash (#a8a6a5) ground the canvas rather than cool white-marble beige, giving product photography the feeling of stone-counter and linen rather than clinical gallery light. A muted coral-red (#df3131) enters selectively as an accent counterweight — enough warmth to keep the palette from reading as a produce co-op, not so much that it eclipses the green identity. Typography pairs a serif display voice for editorial moments — collection headers, hero statements — against clean Helvetica Neue for body and label copy, a combination positioning the brand just below the luxury threshold while remaining accessible. Product cards sit on warm off-white ({colors.surface-soft}) rather than pure white, reinforcing the organic material story without heavy-handed messaging. Navigation stays deliberately understated: no oversized logotype, no marquee banner, the product photography doing the commercial work. Pill-shaped badges ({rounded.full}) carry sustainability callouts and material labels — 14k gold-fill, recycled silver — surfacing brand values at the SKU level rather than the homepage level. Spacing is generous without the cold emptiness of luxury minimalism: {spacing.section} section breaks, {spacing.lg} card gutters, and touch targets that presume a mobile-first customer browsing between subway stops in Queens or the Lower East Side.

colors:
  primary: "#0d4f3d"
  primary-mid: "#4b916d"
  primary-light: "#97c693"
  primary-tint: "#bde2a7"
  primary-pale: "#effae5"
  primary-active: "#0a3d2f"
  primary-disabled: "#bde2a7"
  accent: "#df3131"
  accent-mid: "#e55c5e"
  accent-light: "#f4b8b9"
  accent-pale: "#fcebeb"
  ink: "#151414"
  body: "#383838"
  muted: "#767574"
  muted-soft: "#a8a6a5"
  hairline: "#e0dfdf"
  hairline-soft: "#f1f0ef"
  canvas: "#ffffff"
  surface-soft: "#f1f0ef"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.04em
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
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  label-upper:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.05em

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
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.primary-pale}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "none"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    borderBottom: "1px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    padding: "{spacing.sm}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
  product-card-hover:
    backgroundColor: "{colors.surface-soft}"
    transition: background-color 0.2s ease
  sustainability-badge:
    backgroundColor: "{colors.primary-pale}"
    textColor: "{colors.primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: 4px 12px
    border: "1px solid {colors.primary-tint}"
  material-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 3px 10px
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    displayTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    textAlign: center
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    paddingTop: "{spacing.xxl}"
    paddingBottom: "{spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
  category-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 16px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: 6px 16px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    height: 36px
    textAlign: center
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    subtotalTypography: "{typography.title-md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.hairline}"
    linkColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    padding: "{spacing.section} {spacing.xl}"
  pdp-image-rail:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    thumbnailBorder: "2px solid transparent"
    thumbnailBorderActive: "2px solid {colors.primary}"
  pdp-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 52px
    width: "100%"
  size-swatch:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    padding: 8px 12px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.xs}"

## Components

### Buttons

**`button-primary`** — A flat rectangular CTA using deep forest green (#0d4f3d) fill with white uppercase letter-spaced label. No border radius; the sharp geometry reads as artisanal precision rather than tech friendliness. Hover darkens to `{colors.primary-active}` (#0a3d2f); disabled state uses the pale mint fill (#bde2a7) with muted text to remain visible without drawing attention.

**`button-secondary`** — White fill with a 1px forest-green border and green label, same sharp corners and uppercase treatment as primary. Hover introduces a pale green background (`{colors.primary-pale}`) as a soft fill-in rather than a solid flip. Used for secondary CTAs like "View Collection" or "Learn More" alongside a primary add-to-cart.

**`button-ghost`** — Transparent background with underlined ink-colored text, no border. Used for low-hierarchy actions: "Continue Shopping," "View All," editorial navigation links. Keeps pages visually clean by reserving color for actionable commerce moments.

### Sustainability Badge & Material Tag

**`sustainability-badge`** — Full-radius pill in pale sage (#effae5) with forest-green text and a mint border (#bde2a7), displaying uppercase labels like "RECYCLED SILVER" or "SUSTAINABLE GOLD-FILL." Surfaces brand values directly on the product card without requiring the customer to navigate to a separate about page.

**`material-tag`** — Smaller pill in warm surface-soft (#f1f0ef) with muted text. Used for secondary descriptors: "14k Gold Fill," "Freshwater Pearl," "Sterling Silver." Stacks horizontally beneath the product title on PDP.

### Navigation

**`nav-bar`** — Clean white bar, 60px height, with a 1px warm hairline separator below. Links use 13px Helvetica Neue at 500 weight with generous letter-spacing (0.05em), uppercased optically by the small size rather than CSS transform. Active state gets a 1px forest-green underline and green text. Logo sits left; cart icon and account icon right; a persistent announcement bar above in deep forest green carries promotions.

### Product Card

**`product-card`** — Sharp-cornered, no shadow, 4:5 portrait image ratio. Title in 14px regular weight, price in a slightly heavier 15px. On hover the card background shifts to the warm parchment (#f1f0ef) to signal interactivity without an aggressive lift or border treatment. Sustainability badges float over the image corner when present.

### Hero

**`hero`** — Parchment-background (#f1f0ef) full-width band with centered serif display type (`{typography.display-xl}`) and a short body paragraph. CTAs sit below the body copy as a primary + ghost button pair, spaced with `{spacing.md}` between them. Deliberately low-key for a jewelry brand — no lifestyle photography bleed, letting the editorial text lead and product grid deliver the visual weight beneath.

### PDP

**`pdp-image-rail`** — Warm soft-surface background, square image ratio, square thumbnail strip below. Active thumbnail highlighted by a 2px forest-green border. Add-to-cart button spans full container width, 52px height, flat green with white uppercase label. Size swatches use 1px hairline border, thickening to ink-color on selection.

### Footer

**`footer`** — Near-black (#151414) background with warm hairline links and uppercase section headings in `{typography.label-upper}`. A sustainability mission statement appears as a short paragraph in `{typography.body-sm}` muted text before the link columns, reinforcing brand positioning at page exit.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo; hero text scales to `{typography.display-md}`; PDP image goes full-width; cart drawer overlays full screen |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + icons, categories in a scrollable horizontal pill strip below; hero padding reduces to `{spacing.xl}` |
| Desktop | 1128–1440px | Three or four-column product grid; full horizontal nav with category links visible; announcement bar + nav + categories in three stacked bands |
| Wide | > 1440px | Grid max-width constrained to 1440px, centered; hero typography steps up to full `{typography.display-xl}`; product card images gain more vertical breathing room |

### Touch Targets

- All nav icons minimum 44×44px tap area, regardless of visual size
- Size swatches minimum 44px height on mobile
- `button-primary` and `pdp-add-to-cart` full-width on mobile, minimum 52px height
- Category pills scroll horizontally without wrapping on mobile

### Collapsing Strategy

- Three-column grid collapses to two at tablet, one at mobile — no masonry, no mixed sizes
- Footer columns stack vertically on mobile with accordion disclosure for link groups
- PDP two-column (image | details) stacks to image-then-details at mobile
- Sustainability badges on product cards truncate to icon-only at single-column width

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The blue color ramp (#116dff, #3899ec, #0f2ccf, #2f5dff, #597dff, #acbeff, #d5dfff, #eaefff, #f5f7ff) closely matches the Wix editor UI palette and was excluded from brand color mapping as likely platform-builder artifacts; if the site uses blue for any brand surface, this needs verification
- Platform is confirmed non-Shopify but builder identity not confirmed; if Wix, "Madefor" in the font stack is WixMadefor, which could be the actual brand display font rather than Georgia serif — PDP and nav typographic treatment would differ
- No custom icon set identified; product and nav icons likely use a generic SVG library
- Actual product photography art direction (lifestyle vs. flat-lay vs. model-worn) not extractable from color/font hints — card image treatment above assumes flat/still-life
- Logo lockup, wordmark weight, and logotype font unknown — nav-bar assumes text-only lockup
- Exact grid column counts and gutter widths not confirmed; four-column desktop assumption is an educated default for demi-fine jewelry at this price tier
- Animation/transition durations beyond the card hover not specified
