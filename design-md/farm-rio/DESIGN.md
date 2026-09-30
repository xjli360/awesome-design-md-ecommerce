---
version: alpha
name: "Farm Rio"
source_url: "https://farmrio.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Coral-red (#f94f44) is the combustion point of the entire FARM Rio storefront — every Add to Cart button, every sale badge, every hover state ignites in this single saturated hue against a white canvas (#ffffff), creating a visual shorthand for the brand's Brazilian exuberance before a single print photograph loads. The warm family splits into two extracted tones: #f94f44 for primary actions and the softer #fe6f66 for hover fills and secondary accents, both saturated enough to read as one unified brand signature across any scroll position. A second accent, the deep ocean blue (#016aa3), surfaces in links and informational callouts — a cooler counterpoint that holds its own against the warm palette without competing for CTA dominance. The type system runs entirely on Montserrat, a geometric sans used with deliberate weight contrast: display headings at 700 anchor section titles with authority, while nav and body text holds at 400–500 so the photography — densely printed, maximally chromatic — remains the primary visual event. Buttons are flat rectangles ({rounded.xs}) rather than the pill shapes common in premium minimalist fashion; the flatness lets the coral fill carry the brand signal rather than the form. Product cards are square-cornered ({rounded.none}) frames with no elevation, relying on a hairline border (#dedede) on hover to communicate interactivity — the tropical print image is the decoration, not the container. A near-black (#121212) anchors product names and price labels; body and nav copy steps to #3a3a3a, fractionally warmer to avoid clashing against the chromatic palette. Light gray surfaces (#f5f5f5) isolate filter panels and collection headers, keeping the site architecture legible without adding visual noise to a brand built on pattern density. Vertical rhythm uses {spacing.section} between content zones, giving each print scene room to breathe before the next one fires.

colors:
  primary: "#f94f44"
  primary-active: "#d63b32"
  primary-disabled: "#fbbab7"
  coral-soft: "#fe6f66"
  accent-blue: "#016aa3"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#767676"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-original:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
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
    rounded: "{rounded.xs}"
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "12px {spacing.base}"
    height: 48px
    placeholderColor: "{colors.muted}"
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    iconColor: "{colors.ink}"
    iconSize: 24px
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.primary}"
    originalPriceTypography: "{typography.price-original}"
    originalPriceColor: "{colors.muted}"
    hoverBorder: "1px solid {colors.hairline}"
    padding: "{spacing.sm}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    position: "top-left"
  product-badge-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    position: "top-left"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.display-sm}"
    ctaComponent: "button-primary"
    layout: full-bleed
    minHeight: 600px
    textAlign: center
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
  promo-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    linkColor: "{colors.coral-soft}"
    height: 40px
    dismissible: true
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    disabledTextColor: "{colors.muted}"
    height: 40px
    minWidth: 48px
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    border: "1px solid {colors.hairline}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    unselectedBorder: "1px solid {colors.hairline}"
  wishlist-button:
    backgroundColor: transparent
    iconColor: "{colors.muted}"
    activeIconColor: "{colors.primary}"
    rounded: "{rounded.full}"
    tapTarget: 40px
  search-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputComponent: "text-input"
    rounded: "{rounded.none}"
    shadow: "0 4px 16px rgba(0,0,0,0.08)"
    overlayColor: "rgba(18,18,18,0.4)"
  newsletter-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headlineTypography: "{typography.micro-label}"
    linkColor: "{colors.on-dark}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Coral-red (#f94f44) fill with white text in uppercase Montserrat 700 at 14px with 1px letter-spacing; 48px tall with {rounded.xs} corners reads as decisive rather than soft, making the CTA register immediately against print-heavy photography. Active state compresses to #d63b32; disabled state washes to #fbbab7 while retaining white text. Used for Add to Cart, Checkout, and every primary collection CTA across all breakpoints.

**`button-secondary`** — White fill with #121212 text and a 1px ink border; same 48px height and uppercase Montserrat as button-primary. Pairs cleanly on colored or image hero backgrounds where a coral button would visually merge with the scene. Used for secondary actions such as "Shop Collection" or "Learn More" when a primary button is already in frame.

**`button-ghost`** — Transparent fill with a 1px {colors.hairline} border and ink text. Lowest-emphasis variant used for filter resets, "Back" navigation, and supplementary account or editorial CTAs. Never appears alongside button-primary on the same section without at least one hierarchy step separating them.

### Inputs

**`text-input`** — 48px tall, {rounded.xs} corners, 1px #dedede border at rest sharpening to 1px #121212 on focus. Montserrat 16px weight 400 for value text; #767676 for placeholder. Used in search, newsletter sign-up, and checkout address fields. No fill color change on focus — only the border weight and color shift to signal activation.

### Navigation

**`nav-bar`** — 72px bar on white canvas with a 1px #dedede bottom border. Logo sits left in near-black (#121212); category links in Montserrat 14px weight 500 span center or right cluster; utility icons (search, wishlist, bag) at 24px sit far right. On tablet and mobile the category links collapse into a slide-in drawer triggered by a hamburger icon, leaving logo and utility icons visible in the condensed bar.

### Product Cards

**`product-card`** — Square-cornered ({rounded.none}) container; 3:4 portrait image above title and price with no separator. On hover, a 1px #dedede hairline frames the card and a secondary image or quick-add overlay activates. Title in title-sm (Montserrat 16px 600), standard price in price-display (18px 700 #121212), sale price in coral (#f94f44), crossed-out original in price-original (14px 400 #767676). Padding {spacing.sm} on all sides outside the image.

**`product-badge`** — Coral-red (#f94f44) flat rectangle at 11px uppercase Montserrat 700 with 0.5px letter-spacing and no border-radius, pinned to the top-left corner of the product image. Used for NEW, SALE, and collection callouts. A blue variant (product-badge-blue, #016aa3) marks exclusive, limited, or internationally exclusive styles.

### Hero & Banners

**`hero-banner`** — Full-bleed image or video with overlaid text. Headline in display-xl (Montserrat 40px 700), subline in display-sm (22px 600), both in #ffffff; text-shadow or semi-opaque scrim ensures legibility over busy tropical prints. Primary CTA button sits {spacing.lg} below with center alignment. Minimum 600px tall on desktop; 480px on mobile. The image extends behind the nav bar on landing pages for maximum impact.

**`promo-banner`** — 40px sticky strip in #121212 with 12px Montserrat 500 white text announcing promotions, shipping thresholds, or limited-time events. Inline links render in coral-soft (#fe6f66). Dismissible on mobile via an × icon at the right edge; persists on desktop.

**`collection-header`** — Light gray (#f5f5f5) band below the nav on collection pages. Title in display-md (28px 700), optional subtitle in body-md (16px 400 #3a3a3a). Padding {spacing.xxl} vertical and {spacing.xl} horizontal gives editorial breathing room before the product grid begins.

### Selectors & Filters

**`size-selector`** — Compact 40px-tall square buttons, {rounded.xs}, 1px #dedede border at rest. Selected state inverts to #121212 fill with white text. Unavailable sizes show in #767676 with a diagonal strike. Minimum 48px touch target width enforced on mobile. Arranged in a horizontal wrap row below the color swatches on the PDP.

**`filter-pill`** — Full-radius pill ({rounded.full}) in #f5f5f5 with body text at 12px caption weight 500. Selected state flips to #121212 fill, white text. Arranged in a horizontal scrolling bar above the product grid on desktop; on mobile, the entire filter set moves into a slide-up bottom-sheet modal.

**`color-swatch`** — 24px circles ({rounded.full}) in the product's actual color fill; 1px #dedede border at rest, 2px #121212 border when selected. Arranged in a horizontal row below the size heading on the PDP. On product cards, a condensed row of up to five swatches appears on hover.

### Utility

**`wishlist-button`** — Transparent background, 40px tap target, heart outline icon in #767676 at rest flipping to solid coral (#f94f44) fill when favorited. Positioned top-right of the product image on cards; inline below the title on the full PDP.

**`search-drawer`** — Full-width panel dropping from the nav with white background, no radius, soft box-shadow (0 4px 16px rgba(0,0,0,0.08)), and a 40% ink scrim behind it over the page. Contains a text-input with an inline magnifier icon at left, and a row of trending-search filter-pills below it. Closes on overlay click or Escape.

**`newsletter-block`** — Full-width #f5f5f5 section with title in title-md (18px 600 #121212), supporting copy in body-sm (14px 400 #3a3a3a), then an email input and coral CTA side-by-side on desktop; stacked vertically on mobile. Padding {spacing.xxl} vertical and {spacing.section} horizontal on desktop.

**`footer`** — Dark (#121212) footer with white link text in body-sm (14px 400). Section column headings in micro-label (10px uppercase 600 1px letter-spacing #767676). Social icons at 20px in white. Payment method icons in muted white row at the bottom. {spacing.xxl} top padding; four columns on desktop collapsing to two at tablet and single-column accordion on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to logo + icons + hamburger drawer; hero min-height 480px with headline dropping to display-md (28px); promo-banner becomes dismissible; size selectors in horizontal scroll row; filter-pills move to slide-up bottom-sheet modal; newsletter block stacks input + CTA vertically |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + search + bag only with full category menu in drawer; hero stays full-bleed at 520px; collection-header padding reduces to {spacing.xl} vertical; footer collapses to two columns |
| Desktop | 1128–1440px | Four-column product grid; full horizontal nav with category dropdowns; hero at 600px+ with centered overlaid text; filter-pill bar visible above the grid; footer shows all four columns |
| Wide | > 1440px | Content area max-width 1440px centered on page; product grid remains four columns; hero image scales but text container holds to max-width; side gutters grow proportionally |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Size selector buttons expand to 48px min-width and 48px height on mobile
- Filter pills receive 44px minimum tap height via top/bottom padding adjustment
- Wishlist icon surrounded by a 40px invisible tap zone
- Nav icons minimum 44px tap target with transparent padding extension
- Swatches on mobile expand to 32px with 6px gap for reachability

### Collapsing Strategy
- Product grid: 4-col → 2-col → 1-col at tablet and mobile breakpoints
- Navigation: full horizontal category bar → hamburger + slide-in drawer at < 1024px
- Hero: wide cinematic crop with centered overlay → tighter crop, stacked text + CTA at mobile
- Footer: 4 columns → 2 columns at tablet → single-column accordion at mobile
- Filter controls: horizontal pill scroll bar → bottom-sheet modal at mobile
- Collection header padding: {spacing.xxl} → {spacing.xl} → {spacing.lg} across desktop → tablet → mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact active and disabled hex values for the primary button were not extracted; #d63b32 (active) and #fbbab7 (disabled) are derived approximations — verify against live hover and disabled button states
- Muted text color (#767676) not present in the extracted palette; estimated from Shopify Dawn theme conventions
- Exact font size and weight scale not confirmed from extraction; Montserrat is confirmed present but per-role sizing is inferred from visual norms for Shopify fashion storefronts
- Whether #016aa3 functions as a primary brand accent or solely as a link/informational system color could not be determined from extraction alone
- Hover transition timing (duration and easing curves) not extractable from static analysis
- Mega-menu or dropdown background color, shadow, and animation spec not captured
- Product-card secondary image swap vs. quick-shop overlay behavior not confirmed
- Mobile navigation drawer animation (slide vs. fade, duration) not observed
- Exact promo-banner dismissal persistence (session vs. cookie vs. permanent) not confirmed
- Loading skeleton and lazy-image placeholder patterns not observed in extraction
