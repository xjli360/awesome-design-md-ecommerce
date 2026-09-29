---
version: alpha
name: "Martian Toys"
source_url: "https://martiantoys.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Muted teal (#94d5d4) against a near-black field (#121212) is the visual proposition — not the luminescent cyber-neon of streetwear, but a cooler, almost spectral accent that suggests display cases lit from inside collector shelving. The earthy olive (#716a56) and two registers of forest green (#3f5147, #2c332f) ground the palette in something physical: Pelican foam, cabinet stain, the faded label on a well-travelled auction lot. Together they build a chromatic atmosphere that flatters the subject matter — art toys, designer vinyl, and limited-edition figures sit naturally in a space this color-restrained rather than amid the primary-color noise of mass-market retail.

  Jost, a geometric sans-serif, handles all type throughout the storefront. Headlines run at weight 600–700 with negative tracking at larger sizes; body copy sits at 400 with a 1.6 line-height long enough for product descriptions to read as curatorial notes rather than retailer copy. Buttons use uppercase {typography.button-md} at tight letter-spacing, echoing the stamped-edition vocabulary of limited-run print culture. {rounded.sm} on cards, badges, and inputs reads as precise rather than playful — sharp enough to signal collector seriousness, just soft enough to stay approachable. Primary CTAs surface {colors.primary} teal with {colors.ink} text: unusual in an era where white-on-accent is assumed, but legible and consistent with the brand's tendency to sidestep brightness conventions.

  The dark-canvas nav ({colors.canvas-dark}) frames the browsing experience as gallery navigation rather than retail shelf browsing. Product cards maintain strict visual hierarchy — image floated on {colors.surface-soft}, title in {typography.title-md}, edition callout in {typography.label-tag} uppercase, price in {typography.price-display}. Status badges in {colors.forest} and {colors.midnight} communicate availability as a plain fact rather than a marketing alarm; scarcity here does not shout.

colors:
  primary: "#94d5d4"
  primary-active: "#6bb8b7"
  primary-disabled: "#c9e8e7"
  ink: "#121212"
  body: "#2c332f"
  muted: "#716a56"
  hairline: "#dedede"
  canvas: "#ffffff"
  canvas-dark: "#121212"
  surface-soft: "#f2f1ee"
  surface-card: "#ffffff"
  surface-dark: "#1e2421"
  on-primary: "#121212"
  on-dark: "#ffffff"
  on-dark-muted: "#dedede"
  earth: "#716a56"
  forest: "#3f5147"
  midnight: "#2c332f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Jost', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.6px
  display-lg:
    fontFamily: "'Jost', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.4px
  display-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.09em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  label-tag:
    fontFamily: "'Jost', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  price-display:
    fontFamily: "'Jost', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "'Jost', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Jost', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.05em
  announcement:
    fontFamily: "'Jost', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.07em
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
    rounded: "{rounded.sm}"
    padding: 13px 28px
    height: 44px
    transition: background-color 150ms ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.earth}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 44px
  button-secondary-on-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.on-dark-muted}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    borderColorFocusWidth: 2px
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.muted}"
    height: 40px
    padding: 0 14px
  announcement-bar:
    backgroundColor: "{colors.midnight}"
    textColor: "{colors.on-dark-muted}"
    typography: "{typography.announcement}"
    height: 36px
    linkColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "none"
    logoColor: "{colors.on-dark}"
    cartIconColor: "{colors.on-dark}"
    hoverColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageFit: contain
    imageBackground: "{colors.surface-soft}"
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    editionTypography: "{typography.label-tag}"
    editionColor: "{colors.muted}"
    gap: "{spacing.sm}"
    padding: "{spacing.sm}"
    border: "1px solid {colors.hairline}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero-banner:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    subColor: "{colors.on-dark-muted}"
    ctaComponent: "button-primary"
    minHeight: 540px
    padding: "{spacing.section} {spacing.xl}"
    overlayScrim: "linear-gradient(to right, {colors.scrim} 30%, transparent)"
  collection-header:
    backgroundColor: "{colors.midnight}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.on-dark-muted}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderBottom: "1px solid {colors.forest}"
  edition-badge:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sold-out-badge:
    backgroundColor: "{colors.midnight}"
    textColor: "{colors.on-dark-muted}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  limited-badge:
    backgroundColor: "{colors.earth}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-tag}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  filter-chip:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.label-tag}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 7px 16px
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-tag}"
    border: "none"
    rounded: "{rounded.full}"
    padding: 7px 16px
    height: 32px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerBackgroundColor: "{colors.canvas-dark}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.display-sm}"
    lineItemTitleTypography: "{typography.title-sm}"
    lineItemPriceTypography: "{typography.price-display}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
  product-image-gallery:
    backgroundColor: "{colors.surface-soft}"
    thumbnailBorder: "2px solid transparent"
    thumbnailBorderActive: "2px solid {colors.primary}"
    thumbnailRounded: "{rounded.xs}"
    mainImageRounded: "{rounded.sm}"
    imageFit: contain
  footer:
    backgroundColor: "{colors.midnight}"
    textColor: "{colors.on-dark-muted}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
    headlineTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "2px solid {colors.forest}"

## Components

### Buttons

**`button-primary`** — The primary action surface runs {colors.primary} teal with {colors.ink} near-black text, a pairing that reads as confident rather than conventional; most Shopify stores default to white-on-color but the brand inverts expectation here. Uppercase {typography.button-md} at 0.09em tracking gives the label a stamped, edition-number quality. Active state deepens to {colors.primary-active}; disabled state washes to {colors.primary-disabled} with {colors.earth} text. Height locks at 44px with {rounded.sm} corners — specific enough to feel designed, not a framework default.

**`button-secondary`** — A 1px {colors.ink} border outline on a transparent field, matching button-primary in height and typography so the two can sit side-by-side in hero sections without visual mismatch. On dark-background surfaces, `button-secondary-on-dark` substitutes a {colors.on-dark-muted} border against the transparent dark field. Neither variant uses fill, keeping attention on the primary CTA.

**`button-ghost`** — A text-only affordance in {colors.muted} olive with an underline, used for soft nudges like "view all" or "learn more." No border, no radius, no height constraint — sits inline with copy without adding visual weight.

### Text Input & Search

**`text-input`** — Standard height 44px, {rounded.sm}, 1px {colors.hairline} border that brightens to a 2px {colors.primary} stroke on focus. {typography.body-md} inside with {colors.muted} placeholder; the focus ring doubles in weight rather than changing color, so keyboard navigation stays distinct even at small sizes.

**`search-bar`** — A compact 40px variant on {colors.surface-soft} rather than white, sitting inside the nav or as a standalone filter header component. The muted background integrates the bar visually into dark nav contexts. Icon tint uses {colors.muted}; the field rounds to {rounded.sm}.

### Navigation Bar

**`nav-bar`** — Floats on {colors.canvas-dark} at 64px height, establishing the gallery-black register before a product image loads. Nav links in {typography.nav-link} uppercase-tracked text sit in {colors.on-dark} with {colors.primary} hover, creating a teal wayfinding system against the dark field. Logo and cart icon in {colors.on-dark} with no fill treatment; the absence of fills keeps the bar minimal. An optional `announcement-bar` stacks above in {colors.midnight} with {typography.announcement} uppercase copy for shipping notices and drop dates.

### Product Card

**`product-card`** — Image renders on {colors.surface-soft} at 1:1 aspect ratio with `object-fit: contain`, preventing crops on unusually shaped figures. Below the image, title in {typography.title-md} is followed by an edition callout in {typography.label-tag} {colors.muted} — the edition line is the card's most collectibles-specific element, communicating run size or series at a glance. Price in {typography.price-display} weight 700 anchors the bottom. A 1px {colors.hairline} border and {rounded.sm} give the card a low-profile frame; hover promotes a 0 4px 16px soft shadow without displacement, suggesting the card can be picked up.

### Hero Banner

**`hero-banner`** — Full-width against {colors.canvas-dark} with a left-to-right scrim overlay to hold headline legibility over photographic backgrounds. Headline in {typography.display-xl} at weight 700; subtitle in {typography.body-md} {colors.on-dark-muted}. The single CTA is `button-primary` — the teal swatch against the near-black field is the sharpest moment of brand color on the page and should not compete with a second button at this level. Minimum height 540px on desktop, collapsing to natural image height on mobile.

### Badges

**`edition-badge`** — {colors.forest} green background with {colors.on-dark} text in {typography.label-tag}; used for "Limited Edition", series names, and artist collaboration labels. {rounded.xs} keeps the badge rectilinear. **`new-badge`** uses {colors.primary} teal — the one context where teal serves as a fill rather than a CTA, because "New" is an attentional signal, not an action. **`sold-out-badge`** uses {colors.midnight} with {colors.on-dark-muted} text, communicating finality without drama. **`limited-badge`** uses {colors.earth} olive, connecting visual scarcity to the earthy, archival palette register. All four sit at {rounded.xs} so badge families read as a cohesive system regardless of fill.

### Filter Chips

**`filter-chip`** — Pill-shaped ({rounded.full}), 32px height, transparent with 1px {colors.hairline} border and {colors.body} text in {typography.label-tag}. When active, flips to {colors.primary} fill with {colors.on-primary} dark text — the teal accent functions as selection state across the catalog filter UI. Chips handle category, brand, price range, and availability filters; the uniform size and radius make multi-select filter rows easy to scan.

### Collection Header

**`collection-header`** — A dark band in {colors.midnight} that separates the nav from the product grid on collection pages. Headline in {typography.display-md}, descriptor in {typography.body-md} {colors.on-dark-muted} with generous line-height. A 1px {colors.forest} bottom border marks the transition to the light product grid, creating a frame-within-frame reading across dark header → light grid.

### Cart Drawer

**`cart-drawer`** — 400px slide-in from the right on {colors.canvas} with a {colors.canvas-dark} header strip repeating the nav's dark register. Line item titles in {typography.title-sm}, prices in {typography.price-display}. The drawer's narrow width and clean hierarchy keep it from feeling like an upsell surface; the brand's restraint in color carries through — no accent fills on line items, just ink text and hairline separators.

### Product Image Gallery

**`product-image-gallery`** — Main image on {colors.surface-soft} at {rounded.sm} with `object-fit: contain` to accommodate figures of every proportion without cropping limbs or bases. Thumbnails below use a 2px transparent border that switches to 2px {colors.primary} on selection — the only border that uses teal as a selection indicator rather than fill. Thumbnail corners at {rounded.xs}, main image at {rounded.sm}.

### Footer

**`footer`** — Deep {colors.midnight} ground with a 2px {colors.forest} top border as a parting line against the page body. All type in {typography.body-sm} {colors.on-dark-muted}; section headers use {typography.title-sm} {colors.on-dark}. Links rest in {colors.on-dark} and warm to {colors.primary} on hover. The color floor of the footer — three shades of the earthy-dark palette — feels like a return to the brand's material register after the browsing session.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon + cart; hero min-height drops to auto with stacked text; filter chips scroll horizontally; cart drawer becomes bottom sheet at full width; collection header padding reduces to `{spacing.base}` |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + icons only, secondary links collapse; hero switches to stacked layout; filter chips wrap to two rows; cart drawer stays at 400px |
| Desktop | 1128–1440px | Three or four-column product grid; full nav bar with all links visible; hero uses side-by-side image + text layout with scrim overlay; filter rail optionally pins to left column |
| Wide | > 1440px | Grid remains at 4 columns max with `max-width: 1440px` centered; hero image fills remaining bleed; footer columns expand to 5; typography scales do not increase beyond desktop values |

### Touch Targets

- All interactive elements (buttons, filter chips, nav links, thumbnail switchers) maintain a minimum 44×44px tap target
- Filter chips at 32px visual height gain transparent padding to meet 44px tap target on mobile
- Badge overlays on product cards are non-interactive; tapping the card navigates to PDP

### Collapsing Strategy

- Navigation: hamburger at < 744px, full horizontal link row at ≥ 1128px; tablet shows icon-only strip
- Product grid: 1 → 2 → 3/4 columns across Mobile → Tablet → Desktop
- Hero text: stacked (image above, text below) at < 744px; side-by-side with scrim at ≥ 1128px
- Collection filter: horizontal scroll chips at < 744px; wrapping chips at tablet; optional pinned left-rail at desktop
- Cart drawer: full-width bottom sheet on mobile; 400px right-panel at ≥ 744px
- Announcement bar hides at < 375px if nav is already compressed

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was set; dark nav chrome on mobile (`#121212`) is inferred from palette, not extracted
- Font weight range for Jost not confirmed from live extraction — weights 400/500/600/700 assumed from Google Fonts variable axis availability
- No extracted motion / animation timing values; transitions defaulted to 150ms ease
- Hover and focus states for nav links inferred from palette; no computed style data extracted
- Exact product-card padding and grid gutter widths not available from extraction; values are estimated to match Shopify Dawn/Craft conventions
- No confirmed type scale from live headings; all font sizes derived from category conventions and Jost proportions
- Dark-mode or alternate theme variants not detected; single light/dark hybrid theme assumed
- Actual image aspect ratios for figure photography not confirmed; 1:1 assumed based on art-toy category norms
