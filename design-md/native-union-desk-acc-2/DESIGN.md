---
version: alpha
name: "Native Union"
source_url: "https://www.nativeunion.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Signal orange (#ef521b) declares itself exactly once per page — on the primary CTA button, nowhere else — while near-black (#111111) absorbs everything around it: nav labels, product titles, icon strokes, footer columns. That single-voltage restraint is the Native Union grammar. Neue Haas Grotesk (drawn across its display and text cuts) delivers Swiss-grid precision to a product category — braided charging cables, magnetic desktop hubs, bamboo desk mats, cord organizers — that most brands render with catalog indifference. museo-sans enters the body layer with enough humanist curvature to offset the rationalist headline stack without undermining its authority; museo-sans-condensed compresses into material labels and filter chips where horizontal space is borrowed; museo-sans-rounded handles badge pills with the same warmth. A gold-bronze tone (#cb8a3d) is not a declared brand color — it surfaces through product photography of woven fabric finishes and natural wood desk companions, then bleeds into the palette as the system's material witness, appearing in callout blocks and material-specification chips. White canvas (#ffffff) hosts the product grid; #dedede hairlines mark card edges; muted mid-gray (#9a9a9a) renders compatibility annotations and secondary SKU metadata without competing for the eye. Primary buttons are squared to near-nothing — {rounded.xs} reads as engineered hardware, deliberately set beside the filter pills that reach {rounded.full}. Spacing opens generously at section breaks but compresses inside product cards, creating a browse rhythm that feels spacious and inventory-confident simultaneously. The extracted near-black pair (#111111 ink, #121212 dark surface) enables a tonal frame: a dark navigation bar and dark footer bracket the white product zone, directing the eye to photography the instant it enters the page. Cable braids, matte aluminum, and stone-grain textures carry the persuasion — the typographic system steps aside and lets materials do the brand storytelling.

colors:
  primary: "#ef521b"
  primary-active: "#cc3e0e"
  primary-disabled: "#f7b499"
  ink: "#111111"
  body: "#111111"
  muted: "#9a9a9a"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-bronze: "#cb8a3d"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'museo-sans-display', 'museo-sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.04
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'Neue Haas Grotesk Display Pro', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: -0.8px
  display-sm:
    fontFamily: "'Neue Haas Grotesk Display Pro', 'HelveticaNeue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: -0.4px
  title-md:
    fontFamily: "'Neue Haas Grotesk Text Pro', 'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-sm:
    fontFamily: "'Neue Haas Grotesk Text Pro', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'museo-sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'museo-sans', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'museo-sans', sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Neue Haas Grotesk Text Pro', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Neue Haas Grotesk Text Pro', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Neue Haas Grotesk Text Pro', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0
  label-upper:
    fontFamily: "'museo-sans-condensed', 'museo-sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  price-lg:
    fontFamily: "'Neue Haas Grotesk Display Pro', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Neue Haas Grotesk Text Pro', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'museo-sans-rounded', 'museo-sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
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
    padding: "14px 28px"
    height: 48px
    border: none

  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"

  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.65

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "13px 27px"
    height: 48px
    border: "1px solid {colors.ink}"

  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: "13px 0"
    border: none
    textDecoration: underline

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"

  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
    position: fixed

  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1 / 1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    padding: "16px"
    gap: "12px"

  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  product-badge-bestseller:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 560px
    padding: "96px 0"
    imagePosition: right

  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    height: 40px
    textAlign: center
    padding: "0 24px"

  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.full}"
    padding: "5px 12px"
    border: "1px solid {colors.hairline}"

  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    border: "1px solid {colors.hairline}"

  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    border: none

  pdp-swatch:
    size: 28px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"

  pdp-swatch-active:
    size: 28px
    rounded: "{rounded.full}"
    border: "2px solid {colors.ink}"
    outlineOffset: "2px"
    outline: "2px solid {colors.canvas}"

  compatibility-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"

  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    headerTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-sm}"
    width: 400px
    overlay: "{colors.scrim}"
    overlayOpacity: 0.4
    position: right

  collection-header:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-md}"
    captionTypography: "{typography.label-upper}"
    captionColor: "{colors.muted}"
    padding: "64px 0 40px"

  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.muted}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    headingColor: "{colors.on-dark}"
    padding: "64px 0 32px"
    columns: 4

## Components

### Buttons

**`button-primary`** — Signal orange (#ef521b) on a near-flush {rounded.xs} corner, uppercase Neue Haas Grotesk at 13px with 0.8px tracking. The uppercase setting is intentional: it reads as a hardware label, not a marketing verb. Hover transitions to `button-primary-hover` (#cc3e0e) with no border change. Disabled state uses the washed coral `{colors.primary-disabled}` at 65% opacity, making inactivity immediately legible without layout shift.

**`button-secondary`** — White field with a full 1px ink border, matching the primary height (48px) and corner radius. The border ensures the two button types read as peers on product pages. Hover lightens the fill to `{colors.surface-soft}` while retaining the ink border.

**`button-ghost`** — Text-only with underline, no border, no background. Used for secondary text actions inside PDPs (e.g., "View Full Specs", "See Compatibility"), confirmation flows, and cart line-item removal. Never competes with button-primary on the same row.

### Nav Bar

Dark-surfaced masthead (`{colors.surface-dark}`) fixed at 64px, with white (`{colors.on-dark}`) Neue Haas nav links at 14px/500 weight. The dark band creates immediate contrast against the white product grid below — the eye enters the content zone the moment it drops below the bar. Logo sits left-aligned; search, account, and cart icons cluster right. On hover, individual nav links shift to `{colors.primary}` (signal orange). A mega-menu or dropdown inherits the dark surface for visual continuity.

### Product Card

White surface (`{colors.surface-card}`) with a thin `{colors.hairline}` border and `{rounded.sm}` corners. The square image zone fills a 1:1 aspect ratio crop — no letterboxing, no padding inside the image frame. Title renders in `{typography.title-sm}`, price in `{typography.price-sm}`, variant caption (colorway or material name) in `{typography.caption}` at `{colors.muted}`. The badge component (`product-badge-new` or `product-badge-bestseller`) overlays the top-left corner as an absolute-positioned chip. No drop shadow on default state; a subtle elevation may appear on hover.

### Hero Section

Full-width dark panel (`{colors.surface-dark}`) with headline in `{typography.display-xl}` (museo-sans-display at 56px/700) rendered in `{colors.on-dark}`. Body copy uses `{typography.body-md}` in the same on-dark tone. The primary CTA button (button-primary) anchors the bottom of the text column. On desktop, product photography occupies the right half of the panel; on mobile, the image drops to background with a dark overlay for text legibility.

### Announcement Bar

Full-width ink-black strip at 40px height, `{typography.body-sm}` text centered in `{colors.on-dark}`. Used for shipping thresholds, new product drops, and limited-time promotions. No dismiss button on desktop; may cycle between two messages with a crossfade transition at 4-second intervals.

### Material Badge

Uppercase `{typography.label-upper}` pill on `{colors.surface-soft}` with a `{colors.hairline}` border at `{rounded.full}`. Labels such as "BRAIDED NYLON", "NATURAL WOOD", "GENUINE LEATHER" appear beneath product images on PDP and in collection header callout rows. The pill format and uppercase tracking give material callouts the weight of a certification without introducing color noise.

### Filter Pills

Collection-page taxonomy controls. Default: soft surface with hairline border, `{rounded.full}`. Active: full ink fill with on-dark text, border removed. The pill geometry deliberately contrasts the squared product cards — soft filter UI against engineered product geometry. On mobile, the pill row scrolls horizontally in a single no-wrap track with 8px snap padding.

### PDP Swatches

Color and finish swatches render as 28px circles (`{rounded.full}`). Unselected ring is 2px `{colors.hairline}`; selected ring is 2px `{colors.ink}` with a 2px white outline gap creating a double-ring focus indicator. Material swatches (woven fabric, stone, leather) use an inset photographic crop of the actual surface rather than a flat color fill.

### Compatibility Chip

Small pill at `{rounded.full}` with `{typography.caption}` in `{colors.muted}` on `{colors.surface-soft}`. Displays interface or device compatibility strings: "USB-C", "MagSafe 15W", "Lightning". Groups appear horizontally beneath the product title on PDP, establishing technical credibility without requiring the customer to read fine print.

### Cart Drawer

400px right-side panel on desktop, full-width bottom sheet on mobile. White background with ink text, hairline-bordered line items. Header uses `{typography.title-md}`. Line items include product thumbnail, name in title-sm, variant label in caption/muted, quantity controls, and remove link as button-ghost. Subtotal and checkout CTA (button-primary, full-width) anchor the bottom. Scrim overlay at 40% opacity on the page beneath.

### Collection Header

Dark panel (`{colors.surface-dark}`) above the product grid, similar to hero but shallower. Collection name renders in `{typography.display-md}` in `{colors.on-dark}`; a category label in `{typography.label-upper}` sits above in `{colors.muted}` as a breadcrumb-style descriptor. Padding 64px top, 40px bottom, creating a generous entry into the grid below.

### Footer

Four-column link grid on `{colors.surface-dark}` mirroring the nav. Column headings use `{typography.label-upper}` in `{colors.on-dark}`. Link rows use `{typography.body-sm}` in `{colors.muted}`, lightening on hover to `{colors.on-dark}`. Bottom row: copyright in `{typography.caption}` left, social icons and payment method marks right. No divider lines between columns — whitespace handles separation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav over dark bar, hero text scales to display-sm (28px), cart drawer becomes full-width bottom sheet, filter pills scroll horizontally in a no-wrap track |
| Tablet | 744–1128px | Two-column product grid, nav retains logo + top-level links but secondary items collapse to hamburger, hero supports text left / image right at reduced image width |
| Desktop | 1128–1440px | Three- or four-column product grid, full horizontal nav visible with hover mega-menu, cart drawer 400px fixed right, announcement bar shows two lines before cycling |
| Wide | > 1440px | Content max-width ~1440px centered with increased horizontal padding, hero allows two-column split with larger image zone, footer switches to five columns if brand adds regional nav |

### Touch Targets

- All interactive tap zones minimum 44×44px on mobile, regardless of visual size
- Swatches expand from 28px desktop to 36px on touch screens
- Filter pills gain 10px vertical padding on mobile
- Nav icon buttons (search, account, cart) padded to 44×44px tap target
- Quantity steppers on cart line items minimum 44px width

### Collapsing Strategy

- Navigation: logo + hamburger on mobile; all primary links visible on desktop; secondary links (language/region) collapse first on tablet
- Product grid: 1 column (mobile) → 2 columns (tablet) → 3–4 columns (desktop)
- Hero: full-bleed image as background layer with dark overlay on mobile; side-by-side layout on desktop
- Collection filters: horizontal scroll row on mobile; left-rail sidebar on desktop wide
- Footer: four columns collapse to two on tablet, single stacked column on mobile
- Announcement bar: present at all breakpoints; text truncates with ellipsis below 375px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Light neutral surface (`{colors.surface-soft}`, set to #f5f5f5) not directly in extraction — derived from common Shopify theme defaults; actual value may differ
- No animation or transition timing values captured — hover duration, easing curves, and drawer open animations unknown
- Exact nav height (set to 64px) is an estimate; could range 56–72px depending on logo lockup
- Whether #121212 is the nav/footer surface or a full-page dark-mode canvas is not confirmed from extraction alone
- Dark-mode variant palette (if any) not captured; single dark-surface tone extracted
- Icon set style — line weight, fill vs. outline, stroke width — not captured from extraction
- Responsive typography scaling not confirmed; display-xl assumed to reduce approximately 50% on mobile
- museo-sans weight variants (100, 300, 500, 700) available in the brand's Typekit license not confirmed
- Button height (48px) is an estimate based on Shopify theme default sizing; site-specific override possible
- #cb8a3d bronze may be purely photographic (product finish color, not a UI token) — usage restricted to material callout context until confirmed as a declared brand color
- Price typography for strikethrough/sale states (compare-at price styling) not captured
- Search input placement (inline nav bar vs. expanded overlay) not confirmed
