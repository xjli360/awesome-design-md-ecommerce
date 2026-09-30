---
version: alpha
name: "Smythson"
source_url: "https://www.smythson.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every Smythson notebook arrives lined in Nile Blue — a proprietary dusty-periwinkle that has remained unchanged since Frank Smythson registered it on Bond Street in 1887. This interior reveal structures the entire visual grammar: maximum restraint on the exterior, a single chromatic signature within. The outer surfaces run in a near-black charcoal (#313131) that functions as ink rather than shadow — warm enough to sit beside vegetable-tanned calfskin, precise enough to carry embossed gilding. The palette radiates outward from that anchoring darkness through paper creams and hairline grays before Nile Blue appears as hover state or focus ring, always a disclosure rather than a headline.

  Type scales are deliberately compressed: display headings sit below 40px because the brand's luxury register lives in material weight — the press of a Featherweight page, the resistance of an Italian calf cover — rather than screen-scale drama. Positive letter-spacing on uppercase labels echoes the deliberate spacing between ruled lines in Smythson's own writing paper. Button labels are tracked uppercase, signalling precision rather than urgency; no aggressive color appears on any CTA because the customer arrives with intention.

  Grid discipline is absolute. Product bleeds are uniform, margins do not collapse below 24px at any breakpoint, and product cards carry no radius ({rounded.none}) — the photography itself provides human warmth. Inputs are hairline-bordered on white, never filled-background, pulling from the same sensibility as a letter written on cream laid paper. The Nile Blue surfaces sparingly: focus rings, selected swatches, the interior of editorial bands — a color that signals you have opened the cover.

  Navigation is a single horizontal tier of tracked uppercase labels with no cascade menus, structured for a brand whose catalogue depth is curated rather than vast. The overall register is that of a printed catalogue made interactive: material specificity, white space as breath, and an extreme restraint that trusts the object over the interface.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a8a8a8"
  nile-blue: "#7eb5c4"
  nile-blue-deep: "#5a98aa"
  nile-blue-pale: "#daedf3"
  ink: "#313131"
  body: "#4d4d4d"
  muted: "#888888"
  muted-soft: "#b4b4b4"
  hairline: "#d8d8d8"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f9f8f6"
  surface-card: "#ffffff"
  paper-cream: "#f5f1eb"
  on-primary: "#ffffff"
  on-nile: "#ffffff"
  gold-foil: "#b89a5e"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  editorial-pull:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
    fontStyle: italic
  title-md:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 1.5px
    textTransform: uppercase
  body-md:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  price:
    fontFamily: "Georgia, 'Times New Roman', Times, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.6px
  caption-upper:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 2px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 1px
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
    padding: 14px 32px
    height: 48px
    border: none
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        cursor: not-allowed

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
    states:
      hover:
        backgroundColor: "{colors.surface-soft}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "8px 0"
    border: none
    borderBottom: "1px solid {colors.primary}"
    states:
      hover:
        borderBottom: "1px solid {colors.primary-active}"
        textColor: "{colors.primary-active}"

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
    states:
      focus:
        border: "1px solid {colors.nile-blue}"
        outline: "2px solid {colors.nile-blue-pale}"
        outlineOffset: 0

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 28px
    padding: "0 {spacing.xxl}"
    states:
      scrolled:
        boxShadow: "0 1px 0 {colors.hairline}"

  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    imageFit: cover
    titleTypography: "{typography.body-sm}"
    categoryTypography: "{typography.caption-upper}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    categoryColor: "{colors.muted}"
    priceColor: "{colors.ink}"
    gap: "{spacing.sm}"
    states:
      hover:
        imageTransform: scale(1.04)
        imageTransition: transform 400ms ease

  hero:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.editorial-pull}"
    titleColor: "{colors.ink}"
    subtitleColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xxl}"
    minHeight: 560px
    ctaMarginTop: "{spacing.xl}"

  editorial-section:
    backgroundColor: "{colors.paper-cream}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    titleColor: "{colors.ink}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xxl}"
    maxWidth: 760px
    margin: "0 auto"

  nile-blue-band:
    backgroundColor: "{colors.nile-blue}"
    textColor: "{colors.on-nile}"
    titleTypography: "{typography.display-sm}"
    captionTypography: "{typography.caption-upper}"
    padding: "{spacing.xl} {spacing.xxl}"
    accentColor: "{colors.on-nile}"

  material-swatch:
    size: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    cursor: pointer
    states:
      selected:
        border: "2px solid {colors.primary}"
        outline: "2px solid {colors.hairline}"
        outlineOffset: 2px
      hover:
        border: "2px solid {colors.muted-soft}"

  personalisation-panel:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.title-sm}"
    labelColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    inputBorder: "1px solid {colors.hairline}"
    charCountTypography: "{typography.caption}"
    charCountColor: "{colors.muted}"

  monogram-badge:
    backgroundColor: "{colors.nile-blue}"
    textColor: "{colors.on-nile}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: "4px 10px"

  search-overlay:
    backgroundColor: "{colors.canvas}"
    inputTypography: "{typography.body-md}"
    inputColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: none
    borderBottom: "1px solid {colors.nile-blue}"
    padding: "{spacing.lg} {spacing.xxl}"
    backdropColor: "rgba(49,49,49,0.45)"
    backdropBlur: 0
    resultTypography: "{typography.body-sm}"
    resultColor: "{colors.ink}"

  category-filter-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    border: none
    padding: "10px 0"
    marginRight: "{spacing.xl}"
    states:
      active:
        textColor: "{colors.ink}"
        borderBottom: "1px solid {colors.primary}"
      hover:
        textColor: "{colors.body}"

  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    separatorContent: "/"
    padding: "{spacing.base} 0"

  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.caption}"
    headingColor: "{colors.on-primary}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.xxl}"
    dividerColor: "rgba(255,255,255,0.12)"
    logoTint: "{colors.on-primary}"

## Components

### Buttons

**`button-primary`** — A full-width or fixed-width charcoal (#313131) block with no border radius, uppercase tracked type at 13px/1.5px spacing. The background transitions to #1a1a1a on hover with no bounce or animation — the shift is immediate and dry, consistent with the brand's refusal of decoration. Disabled state uses a mid-gray (#a8a8a8) to signal unavailability without visual noise. No drop shadow at any state.

**`button-secondary`** — White fill with a 1px charcoal border, using the same uppercase tracked type as the primary. On hover the fill shifts to the off-white surface (#f9f8f6), preserving the border unchanged. Used for secondary CTAs such as "View all", "Save to wishlist", and personalisation confirmations. Sits flush beside `button-primary` at equal height (48px) in side-by-side CTA pairs.

**`button-ghost`** — Transparent background with a bottom-border underline rather than a full border box. Used for inline text actions (size guides, returns policy links, "Continue reading" in editorial pages). The underline color matches the text, transitioning to `primary-active` on hover. Padding is zero-horizontal to align with surrounding body text.

### Inputs

**`text-input`** — White background, 1px hairline border (#d8d8d8), no radius. On focus the border color transitions to Nile Blue (#7eb5c4) with a soft pale-blue outline at 2px offset — the only moment the brand color appears in functional UI. Placeholder text is muted gray (#888888) in Georgia italic at body-md scale. Error state uses a bottom-border treatment in a warm red, keeping the overall field quiet.

### Navigation

**`nav-bar`** — Fixed at 60px, white background with a 1px hairline bottom border. The wordmark (Smythson logotype) centers vertically at max-height 28px. Navigation labels are uppercase tracked sans-serif at 13px (nav-label). A utility row above (account, wishlist, bag, currency) runs at caption-upper scale in muted gray. On scroll the bar does not shrink — it holds its 60px height and adds a subtle hairline shadow. No hamburger on desktop; the full category tier is always visible.

### Product Card

**`product-card`** — Portrait aspect ratio (3:4) image with no radius and a subtle scale-up (1.04×) on hover over 400ms ease. Below the image: the category label in caption-upper muted gray, the product title in body-sm, and the price in the dedicated price style (Georgia, 15px, regular weight). No "Add to bag" button appears on the card itself — purchase intent is captured on the PDP. The card carries no border, shadow, or background fill; it sits directly on the canvas.

### Hero

**`hero`** — Full-width editorial block on a warm off-white (#f9f8f6) or photography fill. The display-xl title (Georgia, 40px, weight 300) anchors left-aligned at desktop and centers on mobile. A single editorial-pull subtitle in italic Georgia at 20px runs below, providing breath before the CTA. The CTA uses `button-primary` with `margin-top: 32px`. Image-led heroes place the typography in a left-side text column against a right-side bleed photograph, never overlaid on top of the image.

### Editorial Section

**`editorial-section`** — Paper-cream (#f5f1eb) band with a display-md heading, body copy in body-md Georgia at 1.65 line-height, and constrained max-width (760px) to preserve readable measure. Used for brand story content, craft narratives, and gift-guide copy. No imagery required — the warm background and generous line-height carry the section. CTAs at the bottom use `button-ghost` rather than a full button block.

### Nile Blue Band

**`nile-blue-band`** — A full-bleed band in the brand's signature Nile Blue (#7eb5c4), used sparingly for promotional messaging, personalisation callouts, and new-collection reveals. Headline in display-sm white, supporting label in caption-upper white at reduced opacity (80%). This is the only surface where the brand color is dominant rather than accentual. Used at most once per page.

### Personalisation Panel

**`personalisation-panel`** — Off-white (#f9f8f6) inset panel within the PDP, bordered by a 1px hairline. The section heading ("Add a personal touch", "Monogram") runs in title-sm uppercase. Each field — initials, thread colour — is a standard `text-input` component. A character counter in caption gray tracks remaining monogram characters. The CTA within the panel is `button-secondary` at reduced width rather than full-bleed.

### Material Swatch Selector

**`material-swatch`** — 32px circular swatches with a 2px transparent border at rest. On selection the border becomes 2px charcoal with a 2px hairline outline at 2px offset, creating a visible ring-within-ring selection indicator. On hover a muted-soft border (#b4b4b4) previews selectability. Swatches are used for both color (leather hue) and material (calf, nappa, canvas) selection on the PDP, labelled beneath in caption-upper.

### Search Overlay

**`search-overlay`** — A full-width panel dropping from the nav bar with a white background and a single Nile Blue bottom border on the input field — the focus treatment made permanent as a design choice. The backdrop dims to rgba(49,49,49,0.45) without blur. Results appear as a simple list in body-sm below the input with no card chrome. Closing the overlay via Escape or click-outside removes the backdrop with a 200ms fade.

### Footer

**`footer`** — Full-bleed charcoal (#313131) background, reversing the canvas/ink relationship. Column headings in title-sm white, links in caption muted-soft (#b4b4b4) transitioning to white on hover. The Smythson wordmark appears in white at the bottom-left at reduced scale. A thin rgba-white divider separates the link columns from the legal and social row. No newsletter signup form appears in the footer — it is handled as an inline editorial module above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to wordmark + bag icon + hamburger drawer; hero text centers; editorial-section padding reduces to `{spacing.lg}`; button-primary goes full-width |
| Tablet | 744–1128px | Two-column product grid; nav bar shows top-level categories, utility row collapses to icons; hero splits to stacked image-over-text layout; nile-blue-band padding scales to `{spacing.xl}` |
| Desktop | 1128–1440px | Three-column product grid standard; full horizontal nav with both category and utility tiers; hero splits left-text / right-image at 50/50; editorial-section constrained to 760px centered |
| Wide | > 1440px | Max content width capped at 1440px with symmetric canvas margins; four-column product grid on collection pages; hero image column allowed to bleed edge-to-edge while text column holds 1440px grid |

### Touch Targets

- All interactive elements minimum 44×44px on mobile, including swatch selectors (expanded tap area beyond visual 32px diameter)
- Nav drawer links padded to 48px row height
- Breadcrumb links padded vertically to meet 44px minimum without altering visual spacing
- Monogram badge and material swatch tap areas extended via invisible padding overlay

### Collapsing Strategy

- Nav: horizontal category tier → full-height drawer with accordion category groups; utility icons remain in the fixed header bar
- Personalisation panel: inline on desktop PDP → bottom sheet on mobile, triggered by a sticky "Personalise" button
- Editorial section: two-column image+text → stacked image-above-text with text padding reduced
- Footer: four-column link grid → single-column accordion with section headings acting as expand toggles
- Nile blue band: horizontal headline+CTA layout → stacked centered layout with full-width CTA button

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Only one hex extracted** (#313131): the live site was behind Cloudflare anti-bot protection ("Just a moment…"), returning no meaningful DOM. The full Smythson color system — including confirmed hex values for Nile Blue, cream surfaces, and any promotional accent colors — could not be extracted and must be verified against the live stylesheet or design files.
- **Nile Blue hex is approximate**: #7eb5c4 is derived from brand-knowledge of Smythson's widely documented signature lining color, not from site extraction. The actual brand value may differ; treat as a placeholder pending extraction.
- **No brand fonts extracted**: the font stack returned is entirely system-UI fallbacks. Smythson likely uses a licensed serif and/or optical-size sans that loads via self-hosted or third-party CDN. Georgia has been used as a serif stand-in throughout; replace with the actual brand typeface once confirmed.
- **Gold-foil token unverified**: #b89a5e is an approximation of the embossed gilt detailing visible on Smythson packaging; no on-screen hex was recovered for this value.
- **No meta theme-color**: the absence of a theme-color meta tag means the mobile browser chrome color is unspecified by the brand; this should be confirmed against the actual site on iOS/Android.
- **Iconography system unknown**: the icon library (if custom vs. a standard set such as Feather or Material) and stroke weight could not be determined from extraction.
- **Animation tokens absent**: transition curves, durations, and easing functions used across page transitions and hover states are unverified; values in this file are informed estimates consistent with luxury e-commerce conventions.
