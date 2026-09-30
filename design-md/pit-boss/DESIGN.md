---
version: alpha
name: "Pit Boss"
source_url: "https://pitboss-grills.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pit Boss renders its primary CTA in steel-blue (#2d77be) rather than the fire-orange every literal-minded grill competitor reaches for — the choice signals precision hardware and control panels over open-flame aesthetics, and it holds across every add-to-cart button and header link on a canvas of near-total black. The foundation color is pitch (#121212), deepening to ash (#202223) for the navigation bar and navy-deep (#272e66) for product callout sections, with five levels of machined gray (#555555, #414142, #6d7175, #dedede, #d8d8d8) building a step-ladder from smoke to hairline that maps to grate texture, hopper metal, and cast-iron finish. BerninoSansCondensed-ExtraBold carries every display headline in compressed uppercase columns — letterforms so narrow at large sizes that a 56px display stack occupies the horizontal footprint of a normal-weight 36px headline. Science Gothic pushes into even more extreme compression for brand wordmark moments, functioning as a second voice that amplifies the industrial register without departing the type family's logic. Product cards and UI elements use {rounded.xs} (2px) corners, keeping the geometry rectilinear and mechanical — no generous radius softens the edge of a pellet grill product tile. Promo and sale badges stack uppercase BerninoSansCondensed-ExtraBold at 11px with tight letter-spacing over {colors.primary} or {colors.navy-deep} fills, reading as warning labels on commercial equipment rather than consumer discount ribbons. Hero zones run edge-to-edge at full bleed with CTA buttons rendered in full uppercase and 0.5px letter-spacing — a combination that reads as embossed plate rather than a soft ecommerce tap target. Navigation collapses on mobile to a {colors.pitch} drawer with white knock-out text and a preserved blue CTA strip, the brand's single warm signal inside an otherwise monochromatic column. Footer blocks print at {colors.pitch} with {colors.muted} secondary links, a cast-iron density that ends the page rather than softening its exit.

colors:
  primary: "#2d77be"
  primary-active: "#23609b"
  primary-disabled: "#555555"
  ink: "#222222"
  body: "#414142"
  muted: "#6d7175"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#f8f8f8"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  pitch: "#121212"
  ash: "#202223"
  smoke: "#555555"
  navy-deep: "#272e66"
  silver: "#d8d8d8"

typography:
  display-xl:
    fontFamily: "BerninoSansCondensed-ExtraBold, BerninoSansCondensed, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "BerninoSansCondensed-ExtraBold, BerninoSansCondensed, sans-serif"
    fontSize: 36px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -0.25px
    textTransform: uppercase
  display-sm:
    fontFamily: "BerninoSansCondensed-ExtraBold, BerninoSansCondensed, sans-serif"
    fontSize: 24px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: 0
    textTransform: uppercase
  title-md:
    fontFamily: "BerninoSansCondensed, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-sm:
    fontFamily: "BerninoSansCondensed, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "BerninoSansCondensed, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "BerninoSansCondensed, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "BerninoSansCondensed, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  eyebrow:
    fontFamily: "BerninoSansCondensed, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "BerninoSansCondensed-ExtraBold, BerninoSansCondensed, sans-serif"
    fontSize: 16px
    fontWeight: 800
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "BerninoSansCondensed-ExtraBold, BerninoSansCondensed, sans-serif"
    fontSize: 14px
    fontWeight: 800
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  badge-label:
    fontFamily: "BerninoSansCondensed-ExtraBold, BerninoSansCondensed, sans-serif"
    fontSize: 11px
    fontWeight: 800
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  logo-display:
    fontFamily: "Science Gothic, BerninoSansCondensed-ExtraBold, sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: -1px

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
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.pitch}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "2px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    border: "1px solid {colors.smoke}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.pitch}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    height: 64px
    borderBottom: "1px solid {colors.ash}"
    activeLinkColor: "{colors.primary}"
    logoFont: "{typography.logo-display}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    priceTypography: "{typography.display-sm}"
    metaTypography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    borderColor: "{colors.hairline}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.12)"
  hero-banner:
    backgroundColor: "{colors.pitch}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
    ctaTypography: "{typography.button-lg}"
    layout: full-bleed
    minHeight: 560px
    contentPaddingX: "{spacing.xl}"
    contentMaxWidth: 720px
  promo-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.ash}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  category-tile:
    backgroundColor: "{colors.ash}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-sm}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
    rounded: "{rounded.none}"
    imageOverlayOpacity: 0.45
    aspectRatio: "3/2"
  breadcrumb:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    padding: "{spacing.sm} 0"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    iconColor: "{colors.smoke}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: 0 {spacing.base}
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    selectedBorderColor: "{colors.primary}"
    selectedTextColor: "{colors.primary}"
    height: 44px
  feature-icon-block:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    labelTypography: "{typography.title-md}"
    descTypography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    gap: "{spacing.md}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.pitch}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.muted}"
    linkColor: "{colors.silver}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.ash}"
    padding: "{spacing.xxl} {spacing.xl}"
  promo-bar:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.eyebrow}"
    height: 36px
    textAlign: center
  spec-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.ash}"
    headerTextColor: "{colors.on-dark}"
    rowTextColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.badge-label}"
    rounded: "{rounded.xs}"

## Components

### Buttons

**`button-primary`** — Full-bleed steel-blue (#2d77be) fill at 48px tall with BerninoSansCondensed-ExtraBold uppercase text and 0.5px letter-spacing; 2px radius keeps the corner nearly square, consistent with the brand's mechanical geometry. Hover darkens to `primary-active` (#23609b). Disabled state collapses to `smoke` (#555555) at 0.6 opacity with no pointer events.

**`button-secondary`** — Pitch-black fill (#121212) with a 2px solid white border and white uppercase text; reads as an outlined industrial toggle rather than a ghost. Used alongside `button-primary` in hero zones and product detail header rows.

**`button-ghost`** — Transparent fill with a 1px `smoke` (#555555) border, lowercase-permitted body, sits inside dark surface panels where a full fill would read as double-CTA. Used for secondary navigation actions like "Learn More" inside feature blocks.

### Navigation

**`nav-bar`** — 64px black (#121212) bar with 1px `ash` (#202223) bottom rule. Logo renders in Science Gothic at extreme compressed weight, white knock-out. Desktop links in BerninoSansCondensed title-sm; active link color punches to `primary` (#2d77be). Cart and account icons use Font Awesome 6 at 18px white. Mobile collapses to a full-height black drawer overlay.

### Cards

**`product-card`** — White surface-card background, 2px `xs` radius, hairline border, 4/3 aspect image crop with a 4px top bleed for badge overlap. Title in `title-md`, price in `display-sm` uppercase, body copy (cook area specs) in `body-sm` muted. Hover lifts with `0 4px 16px rgba(0,0,0,0.12)`.

**`category-tile`** — Full-bleed image tile at 3/2 aspect, `ash` (#202223) overlay at 45% opacity, eyebrow label in `primary` blue uppercase, category name in `display-sm` white. No radius — edge-to-edge grid at desktop, single-column stack on mobile.

### Badges

**`promo-badge`** — 0px radius rectangle, `primary` blue fill, white uppercase badge-label at 11px/0.5px tracking. Stacks at top-left of product image; reads as a hardware spec label, not a soft ecommerce chip. `sale-badge` uses `navy-deep` (#272e66) fill for markdown events. `new-badge` uses `ash` (#202223) fill for product launches.

### Hero

**`hero-banner`** — Full-bleed `pitch` (#121212) panel, min 560px tall, no side-padding reveal. Eyebrow label in `primary` blue uppercase eyebrow style precedes the `display-xl` headline in white. CTA button is `button-primary` at full size. Photographic product asset positioned right or center-bleed with no background isolation (product-on-black composition).

### Promo Bar

**`promo-bar`** — 36px single-line strip in `navy-deep` (#272e66) above the nav bar; uppercase eyebrow typography, centered white text for shipping or seasonal offer copy.

### Spec Table

**`spec-table`** — Used on PDP pages for cook area, hopper capacity, total BTU. Header row in `ash` (#202223) with white `badge-label` text, alternating rows on white, hairline borders between cells, `xs` radius on container. Label column in `body-sm` muted, value column in `body-sm` ink.

### Search

**`search-bar`** — `surface-soft` (#f0f0f0) fill, hairline border, Font Awesome magnifier icon in `smoke` left-padded. 44px height, `xs` radius. Focus ring shifts border to `primary` blue.

### Feature Icon Block

**`feature-icon-block`** — Surface-soft background, Font Awesome icon in `primary` blue at 32px, label in `title-md`, description in `body-sm` muted. Three- or four-column grid on desktop, single-column on mobile. No radius. Used in mid-page proof sections ("WiFi Control", "Dual-Sensor Lid", "All-in-One Design").

### Footer

**`footer`** — Full-bleed `pitch` (#121212), 1px `ash` top rule, four-column link grid on desktop. Column headings in `title-sm` white, links in `body-sm` `silver` (#d8d8d8). Muted legal text and copyright in `caption` `muted` (#6d7175). Social icons via Font Awesome 6 Brands at 18px white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to pitch-black drawer with hamburger icon; hero headline drops to `display-md`; product grid goes 1-column; category tiles stack vertically; feature icon blocks go 1-column; footer columns collapse to single accordion-style stack |
| Tablet | 744–1128px | Nav shows condensed horizontal links; hero headline at `display-md`; product grid 2-column; category tiles 2-column; feature icon blocks 2-column |
| Desktop | 1128–1440px | Full nav with all link groups; hero headline at `display-xl`; product grid 3- or 4-column; category tiles 3-column; feature icon blocks 4-column |
| Wide | > 1440px | Content max-width caps at 1440px with pitch-black side bleed on hero; grid gutters expand proportionally |

### Touch Targets

- All buttons minimum 44px height and 44px width
- Nav drawer links minimum 48px row height
- Size selector tiles minimum 44px height
- Product card CTAs full-width on mobile at 48px height
- Footer accordion toggles 48px touch row

### Collapsing Strategy

- Nav: horizontal links → hamburger drawer at < 744px; sub-menus become full-height drawer sections
- Hero: two-column image/copy split → stacked copy-over-image at < 744px; image crops to 16/9 at mobile
- Product grid: 4-col → 2-col at tablet → 1-col at mobile
- Category tiles: 3-col grid → 2-col at tablet → vertical scroll strip at mobile
- Spec table: full-column at tablet+ → horizontally scrollable at mobile with sticky label column
- Feature blocks: 4-col → 2-col → 1-col
- Footer: 4-col grid → accordion with toggle arrows at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No orange or red extracted — if Pit Boss uses a warm accent for sale urgency or flame iconography, it was not present in the crawled color sample; verify against live PDP and cart pages
- `surface-card` uses assumed #ffffff (pure white for product card backgrounds); this value was not in the extracted set and should be confirmed from Shopify theme JSON
- Science Gothic variable-font axis ranges (width, weight) are not documented in the extracted hints; extreme-condensed settings are inferred from typical usage of the font and brand category
- BerninoSansCondensed font-weight numeric mapping (ExtraBold = 800 assumed) should be verified against the actual webfont weight axis loaded by the Shopify theme
- No extracted motion tokens (transition duration, easing curves) — animation behavior on hover states and drawer open/close is unconfirmed
- Icon set sizing conventions (Font Awesome variant usage — Free vs Pro, Brands) not delineated in the extraction; icon weights across contexts are inferred
- No loyalty, rewards, or account-panel component data was extractable; those surfaces may carry distinct color treatment not visible in the top-level extraction
