---
version: alpha
name: "Koio"
source_url: "https://koio.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Handstitched welts and full-grain leathers sourced from artisan workshops in Italy arrive at Koio's digital storefront wearing a palette pulled from the vinous end of the spectrum — deep burgundy #580303 anchors every primary call-to-action and editorial accent, while its brighter relative #841719 appears on active states, both reading as controlled and precise against a near-white #fafafa canvas. The hide itself surfaces as a warm sand token (#c1b59a), a literal material reference that grounds the design system in the object being sold. Display headlines are set in Apercu Black Pro at wide letter-spacing — the type feels pressed rather than printed, suggesting a cobbler's stamp more than the rounded-friendly sans-serifs that dominate the contemporary sneaker category. Editorial body copy drops into Founders Grotesk Light, borrowing a lookbook cadence from Italian print fashion. GT America Condensed takes compression duty for tab labels, size selectors, and filter pills, keeping information dense without competing with Apercu's authority in the display register. The deep navy #272d45 stands in for ink, softer than flat black against warm card surfaces yet firm enough to read authoritative. A teal note #0e7a82 appears in narrow utility roles — the single vivid cool accent inside an otherwise earth-and-burgundy palette, likely a collection-period holdover. Corner radii hold at zero throughout — buttons, inputs, cards, and badges all carry squared profiles — a precision gesture applied to pixel geometry that echoes tailored stitching over consumer-friendly softness. Section breaks on desktop are generous, giving editorial photography the breathing room of a luxury print catalog where a single shoe owns the spread.

colors:
  primary: "#580303"
  primary-active: "#841719"
  primary-disabled: "#c1b59a"
  ink: "#272d45"
  body: "#676986"
  muted: "#ababab"
  hairline: "#d9d9d9"
  hairline-soft: "#ebebeb"
  canvas: "#fafafa"
  surface-soft: "#f4f4f6"
  surface-card: "#f7f7f8"
  surface-warm: "#e4e0dd"
  on-primary: "#fafafa"
  leather: "#c1b59a"
  accent-teal: "#0e7a82"
  scrim: "#272d45"

typography:
  display-xl:
    fontFamily: "'Apercu-Black-Pro', 'Apercu Pro', sans-serif"
    fontSize: 56px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: 0.05em
  display-md:
    fontFamily: "'Apercu-Bold-Pro', 'Apercu Pro', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.03em
  title-md:
    fontFamily: "'Apercu-Bold-Pro', 'Apercu Pro', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.02em
  editorial-light:
    fontFamily: "'FoundersGroteskWeb-Light', 'Founders Grotesk', sans-serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: 0
  body-md:
    fontFamily: "'FoundersGroteskWeb-Regular', 'Founders Grotesk', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'FoundersGroteskWeb-Regular', 'Founders Grotesk', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'FoundersGroteskWeb-Light', 'Founders Grotesk', sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.02em
  price:
    fontFamily: "'Apercu-Regular-Pro', 'Apercu Pro', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'GT-America', 'GT America', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  label-condensed:
    fontFamily: "'GT-America-Condensed', 'GT America Condensed', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'GT-America', 'GT America', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.05em
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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-condensed}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1:1"
    imageBg: "{colors.surface-warm}"
  hero-banner:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.editorial-light}"
    rounded: "{rounded.none}"
    padding: "{spacing.section}"
  size-selector:
    typography: "{typography.label-condensed}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    selectedBackgroundColor: "{colors.ink}"
    selectedTextColor: "{colors.on-primary}"
    disabledTextColor: "{colors.muted}"
    rounded: "{rounded.none}"
    height: 40px
    minWidth: 48px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  badge-sold-out:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  leather-detail-badge:
    backgroundColor: "{colors.leather}"
    textColor: "{colors.ink}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.none}"
    padding: 4px 12px
  filter-pill:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.label-condensed}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.ink}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    padding: 8px 16px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "none"
    padding: 12px 16px
    height: 48px
  product-image-carousel:
    backgroundColor: "{colors.surface-warm}"
    dotColor: "{colors.muted}"
    activeDotColor: "{colors.ink}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    bodyTypography: "{typography.body-sm}"
    linkTypography: "{typography.label-condensed}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — A squared burgundy block (#580303) carrying GT America uppercase text at 0.1em tracking, white on wine. The zero-radius profile is deliberate — it reads as precision craft rather than consumer warmth. Active state shifts to the brighter #841719; disabled pulls back to the leather tan primary-disabled, signaling unavailability without the utilitarian gray common to sportswear UI. Full-width on mobile; auto-width on desktop.

**`button-secondary`** — Transparent fill with a 1px ink border and matching GT America uppercase type, identical in height and padding to primary. Used for secondary CTAs such as "View Details," wishlist actions, and filter confirmations. On hover the border intensifies and a ghost surface-soft fill may appear.

**`button-primary-disabled`** — Same geometry as primary but warm leather-tan background with ink text, maintaining the brand's color system even in disabled states rather than reaching for generic grays.

### Navigation

**`nav-bar`** — 64px fixed-height bar on a white canvas with a hairline border below. All navigation links are set in GT America uppercase at 13px with 0.05em tracking. Logo sits centered on mobile and left-aligned on desktop, with category links expanding rightward. A 36px `announcement-bar` in primary burgundy floats above it on load, carrying promotional copy in white label-condensed.

**`search-bar`** — Inset on a surface-soft background with no border or radius, giving it an embedded editorial quality rather than a form-field appearance. Placeholder text uses the muted gray; input text resolves to ink navy.

### Product Card

**`product-card`** — Square-cropped product imagery set on surface-warm (#e4e0dd), a warm gray that approximates butcher paper and keeps the shoe the sole focus. No border radius anywhere on the card. Product name sits in title-md (Apercu Bold, 18px), price beneath it in Apercu Regular, and the leather-detail badge — warm tan on tan background with ink type — may overlay the top-left corner of the image on Italian collection pieces. Hover state typically reveals a secondary lifestyle image.

**`size-selector`** — A row of squared tiles, each holding GT America Condensed size labels. Default state carries a hairline border; selected state inverts fully to ink fill with white text; sold-out sizes receive muted text and a visual strikethrough or diagonal rule.

### Hero

**`hero-banner`** — Full-bleed editorial section using either a deep navy scrim over photography or a direct dark-field image. Headline in Apercu Black Pro display-xl (56px, 0.05em tracking) evokes a stamped mark on Italian goods. Subtext drops into Founders Grotesk Light editorial-light (20px, weight 300) for a looser print-magazine cadence. The primary button sits below, white text on burgundy.

### Badges & Labels

**`badge-new`** — Flat burgundy rectangle with white label-condensed text; zero radius; used on product card overlays to signal new arrivals. `badge-sold-out` uses the muted gray with white text in the same geometry. `leather-detail-badge` uses the leather tan (#c1b59a) with ink text, applied to handcrafted or limited-edition collection items.

**`filter-pill`** — Squared pill with hairline border and label-condensed uppercase. Activating a filter inverts the pill to ink fill with white text, maintaining the same border-to-fill pattern used in the size selector for visual consistency.

### Product Image Carousel

**`product-image-carousel`** — Sits on a surface-warm background (warm off-white matching Italian linen), with pagination dots in muted gray becoming ink navy when active. No border radius on the image container; images fill edge-to-edge. Swipe gesture on mobile; click or arrow-key navigation on desktop.

### Footer

**`footer`** — Full-width section in ink navy (#272d45), carrying white body-sm prose and GT America Condensed link labels in label-condensed uppercase. Arranged in three to four columns on desktop, collapsing to a stacked accordion on mobile. The contrast between the dark footer and the near-white body canvas creates a strong visual terminus to editorial page scrolls.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with slide-over drawer; full-width primary and secondary buttons; sticky add-to-cart bar anchored to bottom of viewport; hero text drops to display-md |
| Tablet | 744–1128px | Two-column product grid; horizontal nav links become visible; announcement bar remains; hero text at display-md; filter sidebar collapses to top filter row |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with category flyouts; hero at display-xl; product detail page splits 50/50 between image carousel and info panel |
| Wide | > 1440px | Max-width container ~1400px centered; side margins expand and fill with canvas color; hero imagery bleeds edge-to-edge behind a centered content well |

### Touch Targets

- All size selector tiles minimum 40×40px with spacing.sm gutter between
- Primary and secondary buttons minimum 48px height across all breakpoints
- Nav hamburger icon minimum 44×44px tap area on mobile
- Filter pills padded to minimum 36px height on mobile for thumb reach

### Collapsing Strategy

- Product grid: 3-col → 2-col → 1-col as viewport narrows
- Footer columns: 4-col → 2-col → stacked accordion with tap-to-expand
- Size selector: wraps to multiple rows rather than scrolling horizontally
- Nav links: collapse to hamburger drawer below 744px; drawer slides from right with ink overlay scrim
- Hero text: display-xl (56px) scales to display-md (32px) on tablet and mobile; line length capped at ~12 words per line at mobile
- Announcement bar: persists across all breakpoints; text may truncate with marquee scroll if copy exceeds single-line width on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact hover transition duration and easing curves not captured; border and fill transitions on buttons and filter pills assumed at 150–200ms ease
- Whether GT America Bold is used in any display context or remains solely a weight variant for emphasis labels is unclear from extraction
- Accent teal (#0e7a82) origin is ambiguous — may be a limited-run collection color or a legacy site element rather than a current core system token
- Logo clearance zone, exact dimensions, and SVG/wordmark specifics not extracted
- Focus ring and accessibility outline styling not confirmed from extraction
- Mobile nav drawer interior layout, background, and animation direction not verified
- Exact breakpoint pixel values for Koio's own grid may differ from the standard Shopify defaults assumed here
- Whether product detail page uses sticky image scrolling (fixed left panel) or standard scroll not confirmed
- Dark-mode variant (if any) not detected
- Custom collection-page hero or lookbook-style layout variants beyond the standard product grid are likely but not confirmed
