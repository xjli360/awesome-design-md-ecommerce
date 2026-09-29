---
version: alpha
name: "Wolf & Shepherd"
source_url: "https://wolfandshepherd.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The dress code problem Wolf & Shepherd solved — running-shoe cushioning inside a brogued oxford — bleeds into the visual system: a near-black navy (#1b2330) stands in for conventional dress-shoe black, stopping just short of corporate severity while remaining authoritative enough for a boardroom entrance. SuisseIntl carries the entire typographic hierarchy; SuisseIntlBold commands display weight at measured scales rather than heroic sizes, while SuisseIntlBook handles body copy with the unhurried confidence of a brand that does not need typographic muscle to make its case. The palette runs deliberately lean — three dark navies (#1b2330, #1b1f27, #262934) anchor authority; a spread of near-whites (#f7f7f7, #f4f4f4) opens clean breathing room for product photography; #1f6fae, the only chromatic note in an otherwise achromatic deck, surfaces as the accent for interactive highlights and select calls-to-action. Mid-register neutrals (#a4a4a4, #c4ced6, #919eab, #b6c2cc) handle hairlines, disabled states, and the secondary-label detail that premium footwear retail demands. Corners behave like the footwear itself — tailored and precise. {rounded.xs} on inputs and cards; {rounded.none} on primary buttons. There is no pill shape anywhere, no soft-radius excess that would signal casual sportswear. Section spacing breathes wide — hero panels command full-bleed height — then contracts predictably through the product grid into the PDP detail zone. A persistent navy announcement bar and navy footer create a bracketing structure: dark header band, white body, dark foot — a framing device the brand applies consistently across templates. No neon gradients, no explosive visual hierarchy, no sportswear theatrics; a clean surface that trusts shoe photography and a single chromatic blue to carry the brand's entire emotional argument.

colors:
  primary: "#1b2330"
  primary-active: "#1b1f27"
  primary-disabled: "#919eab"
  accent-blue: "#1f6fae"
  accent-blue-muted: "#c4ced6"
  ink: "#121212"
  body: "#262934"
  muted: "#5b5b5b"
  muted-light: "#a4a4a4"
  hairline: "#dedede"
  hairline-soft: "#c7c7c7"
  hairline-strong: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f4f4f4"
  cool-gray: "#919eab"
  cool-gray-light: "#b6c2cc"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'SuisseIntlBold', 'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'SuisseIntlBold', 'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'SuisseIntlBold', 'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'SuisseIntlBook', 'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'SuisseIntlBook', 'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'SuisseIntlBook', 'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-uppercase:
    fontFamily: "'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  price:
    fontFamily: "'SuisseIntlBold', 'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'SuisseIntl', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px

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
    rounded: "{rounded.none}"
    padding: 14px 32px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "3/4"
    padding: "{spacing.md}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  product-card-price-sale:
    typography: "{typography.price}"
    textColor: "#c0392b"
  product-card-price-original:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    overlayColor: "rgba(27, 35, 48, 0.45)"
    minHeight: 600px
  hero-eyebrow:
    typography: "{typography.label-uppercase}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.sm}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.lg}"
  technology-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 6px 10px
  technology-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.primary}"
    backgroundSelected: "{colors.primary}"
    textColorSelected: "{colors.on-primary}"
    size: 48px
  size-selector-unavailable:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted-light}"
    textDecoration: line-through
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    border: "1.5px solid transparent"
    borderSelected: "1.5px solid {colors.primary}"
  review-stars:
    starColor: "{colors.primary}"
    emptyStarColor: "{colors.hairline}"
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  pdp-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 56px
    width: "100%"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 16px
    height: 48px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.cool-gray-light}"
    headingTypography: "{typography.label-uppercase}"

## Components

### Buttons

**`button-primary`** — Full navy (#1b2330) block with zero corner radius, uppercase SuisseIntl at 0.8px tracking, 48px height. The hard square termination signals tailored precision rather than casual approachability. Hover deepens to `{colors.primary-active}` (#1b1f27); disabled state desaturates to `{colors.primary-disabled}` (#919eab) with the white label remaining legible. Governs all primary commerce actions: Add to Cart, Shop Now, Checkout.

**`button-secondary`** — White canvas with a 1px navy border and the same uppercase SuisseIntl label. Mirrors primary geometry exactly — no radius, same height — so the pair reads as a matched set rather than a visual hierarchy afterthought. Used for secondary navigation actions, wishlist CTAs, and filter-apply buttons.

**`button-ghost`** — Transparent background with a 1px white border and white uppercase label, deployed over dark hero imagery and the navy footer. Preserves the same squared geometry as the two solid variants; the white stroke prevents any perceived softness.

### Navigation

**`nav-bar`** — White ground at 64px, a 1px soft-gray hairline at base, SuisseIntl 14px links with 0.5px tracking. Brand wordmark sits left; bag and account icons sit right. On scroll the bar holds static rather than collapsing. A slimmer `announcement-bar` at 40px in full navy runs above, hosting promotional copy in `{typography.label-uppercase}`. `nav-bar-dark` mirrors the layout on full-navy ground for hero-backed landing pages where a white bar would float disconnected.

### Product Card

**`product-card`** — Warm near-white (#f7f7f7) ground with 2px radius and a 3:4 portrait image ratio prioritizing the three-quarter shoe angle. Name in `{typography.title-md}`, price in `{typography.price}` (SuisseIntlBold 18px). Sale price renders in red (#c0392b) with the original struck through in `{colors.muted}` beneath. Hover state reveals a secondary quick-add button at the card foot using the primary button treatment.

### Hero

**`hero`** — Full-bleed imagery under a `rgba(27, 35, 48, 0.45)` navy scrim, minimum 600px height, viewport-height on landing pages. Eyebrow copy in `{typography.label-uppercase}` above the headline; headline in `{typography.display-xl}` (SuisseIntlBold 48px, -0.5px tracking). One ghost button and an optional text link sit beneath at `{spacing.lg}` gap. The scrim hue matches the primary navy exactly, creating seamless color continuity when the image is absent.

### Technology Strip

**`technology-strip`** — Full-width section sequencing the brand's proprietary comfort technologies (Crossover, Springflex, Arch Support, etc.) in a horizontal icon-and-label grid. Each node pairs a small icon with `{typography.label-uppercase}` for the technology name and `{typography.body-sm}` for a one-line descriptor. This strip appears on the homepage and PDP as the brand's primary performance-credentialing moment — the visual equivalent of the footnote that justifies the dress-shoe price point.

### Technology Badge

**`technology-badge`** — Compact tag (2px radius, not a full pill) in `{colors.surface-card}` with a `{colors.hairline}` border and uppercase SuisseIntl label. Applied within PDP detail panels to flag individual shoe technologies. Multiple badges stack horizontally with `{spacing.xs}` gap between them.

### Size Selector

**`size-selector`** — 48×48px square tiles with 1px hairline border and 2px radius. Selected state inverts to navy fill with white label. Unavailable sizes render at reduced opacity with label struck through (`size-selector-unavailable`). Tiles wrap in a flex row at `{spacing.xs}` gap; a "Size Guide" text link in `{typography.caption}` trails the grid.

### Color Swatch

**`color-swatch`** — 28px circles with a 1.5px border that is transparent (invisible) when unselected and navy when selected, avoiding the doubled-ring effect of offset outlines. Swatches sit in a row at the product card foot on hover and at PDP level beneath the colorway name label rendered in `{typography.caption}`.

### Review Stars

**`review-stars`** — Five-star row using `{colors.primary}` navy filled stars and `{colors.hairline}` empty stars, with review count in `{typography.caption}` `{colors.muted}` beside the row. On the PDP the aggregate score escalates to `{typography.display-sm}` weight above the star row, followed by the review count and a link to the reviews section below.

### PDP Add to Cart

**`pdp-add-to-cart`** — Full-width 56px navy block, zero radius, uppercase SuisseIntl, that pins to the bottom viewport edge on mobile. The extra 8px height over standard buttons signals its primacy on the page. Disabled (no size selected) state uses `{colors.primary-disabled}` with white label text that reads "Select a Size."

### Footer

**`footer`** — Full navy (#1b2330) ground completing the dark-top / white-body / dark-foot template bracket. Four-column link grid in `{typography.body-sm}` with `{colors.cool-gray-light}` (#b6c2cc) link color. Column headers in `{typography.label-uppercase}` white. Social icons row white at bottom. Copyright line in `{colors.cool-gray}` (#919eab). The navy continuity with the announcement bar above makes the site feel contained, finished.

### Search Bar

**`search-bar`** — Inline field in `{colors.surface-soft}` ground, 1px `{colors.hairline}` border, `{rounded.xs}` radius, 48px touch height. Placeholder in `{colors.muted-light}`. Focus applies a 1px `{colors.primary}` navy border. On desktop, search opens as a dropdown overlay panel; on mobile it claims full nav width.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer on navy ground; hero 480px height, text bottom-anchored center-aligned; technology strip becomes horizontal scroll; PDP add-to-cart bar pins to bottom viewport edge |
| Tablet | 744–1128px | Two-column product grid; nav retains logo and icons, hamburger for main links; hero 540px min-height; technology strip shows 3-across grid |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with dropdown panels; hero viewport-height; technology strip 4-across |
| Wide | > 1440px | Max content width 1400px centered; four-column product grid; hero capped at 840px height to prevent excessive image stretch |

### Touch Targets

- All buttons minimum 48px height meeting WCAG AA guidance; PDP add-to-cart 56px
- Size selector tiles exactly 48×48px for precise tap targeting
- Nav icons (bag, account, hamburger) minimum 44×44px tap zone extended by padding
- Color swatches at 28px visual size carry a 40px tap zone via invisible padding extension
- Footer links spaced minimum 44px vertically on mobile

### Collapsing Strategy

- Navigation: full horizontal nav → hamburger drawer (navy ground, white links) at < 1128px; account and bag icons always visible in compressed state
- Technology strip: 4-column grid → horizontal scroll carousel at < 744px
- Product grid: 4 → 3 → 2 → 1 column across breakpoints
- Hero: left-aligned overlay text shifts to bottom-anchored center-aligned at mobile; CTA buttons stack vertically
- Footer: 4-column grid stacks to single-column accordion on mobile; each column header becomes an expand-on-tap toggle
- PDP image gallery: side-by-side grid collapses to swipeable full-width carousel with dot indicators on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specified border-radius documentation extracted; {rounded.xs} and {rounded.none} assigned from visual analysis of the athletic-dress hybrid category aesthetic
- Precise usage context for `{colors.accent-blue}` (#1f6fae) — whether it appears as link text, interactive UI accent, or badge fill — could not be confirmed from extraction data alone
- Exact nav dropdown treatment (mega-menu vs. flyout, column count, featured image presence) not confirmed from extraction
- Animation and transition timing values absent — easing curves and hover-state duration are not derivable from the extracted tokens
- Sale price color (#c0392b) is inferred from retail convention, not extracted directly from the site palette
- Whether SuisseIntlBold and SuisseIntlBook are weight-named variants within a single variable font or separate font files is ambiguous in the extracted font stack; both loading patterns treated as equivalent
- Mobile hamburger drawer background (navy assumed from brand convention; not explicitly validated in extraction output)
- Exact announcement bar copy rotation and whether it uses a ticker or static single message not confirmed
