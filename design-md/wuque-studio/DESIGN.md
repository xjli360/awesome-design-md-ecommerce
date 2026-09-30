---
version: alpha
name: "Wuque Studio"
source_url: "https://wuquestudio.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Forty-five-degree chamfers on a backplate edge, anodized aluminum in colorways named for seasons — Wuque Studio maps keyboard-builder precision to a storefront that opens on near-black (#191919) canvas, the meta theme-color (#212121) confirming a dark-first commitment before a single pixel loads. The brand's primary voltage, teal #108474, carries the entire interactive burden: nav hover states, CTA fills, focus outlines, and link underlines all route through it, giving the UI a terminal-prompt clarity that engineers recognize immediately — purposeful rather than decorative. Against the near-black field, teal reads like a cursor: it marks exactly where action is possible and nowhere else.

  Type splits along a deliberate axis. Asap handles display and headline work in geometric, lightly condensed strokes at 500–600 weight; Nunito Sans carries all body and UI copy with its characteristically open apertures and rounded terminals. The pairing mirrors the product — aluminum precision wrapped in a hobby with feelings. Neither face pushes past 600 weight in the UI; the boldest moments are 600-weight at 48px in the hero, not the 800-weight slabs that streetwear brands favor.

  Product cards surface from #262626 panels with tight {rounded.sm} 8px corners and a single 1px #303030 hairline — no shadows, no glow, no texture fill. Keycap colorway photography appears at full saturation against the dark field: the lavender at #a89cc8, the dusty rose at #e0b5b2, the hot pink at #e8144b, and the brassy yellow at #fbcd0a all function strictly as colorway swatches rather than global brand signals. They live on badge pills and swatch dots, never on buttons or chrome.

  The group buy lifecycle — Interest Check, Group Buy, Production, Shipping, Delivered — demands a five-state badge vocabulary. Wuque resolves this with {rounded.full} pill shapes, routing the live Group Buy state through primary teal and leaving surrounding stages in neutral hairline-bordered fills so the purchasable window is immediately legible without scanning text. Spacing is disciplined: {spacing.base} 16px gutters inside cards, {spacing.section} 64px breaks between product family sections, and {spacing.xxl} 48px footer clearance that keeps legal copy from colliding with the last product row.

colors:
  primary: "#108474"
  primary-active: "#0a6358"
  primary-disabled: "#7ec4ba"
  primary-muted: "#e0faef"
  accent-pink: "#e8144b"
  accent-red: "#d72c0d"
  accent-lavender: "#a89cc8"
  accent-rose: "#e0b5b2"
  accent-blush: "#fff4fa"
  accent-yellow: "#fbcd0a"
  accent-green: "#13a165"
  accent-green-dark: "#028e48"
  status-error: "#c00000"
  ink: "#eeeeee"
  body: "#cbcbcb"
  muted: "#7b7b7b"
  hairline: "#303030"
  hairline-soft: "#262626"
  canvas: "#191919"
  surface-soft: "#212121"
  surface-card: "#262626"
  surface-elevated: "#303030"
  on-primary: "#ffffff"
  on-dark: "#eeeeee"
  scrim: "#0d0d0d"

typography:
  display-xl:
    fontFamily: "'Asap', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Asap', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Asap', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Nunito Sans', 'Assistant', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Assistant', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Assistant', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Assistant', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Assistant', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  label:
    fontFamily: "'Nunito Sans', 'Assistant', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.6px
    textTransform: uppercase
  price:
    fontFamily: "'Asap', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Asap', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', 'Assistant', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', 'Assistant', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Nunito Sans', 'Assistant', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
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
    rounded: "{rounded.sm}"
    padding: "12px 24px"
    height: 44px
    transition: "background-color 150ms ease"

  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"

  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: "not-allowed"

  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "11px 23px"
    height: 44px

  button-secondary-hover:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"

  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: "12px 0"

  button-sm-outline:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "7px 14px"
    height: 32px

  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    focusOutline: "none"
    rounded: "{rounded.sm}"
    padding: "10px 14px"
    height: 42px

  nav-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    linkHoverColor: "{colors.primary}"
    activeLinkColor: "{colors.ink}"
    logoHeight: 32px

  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspect: "4/3"
    border: "1px solid {colors.hairline-soft}"
    hoverBorderColor: "{colors.hairline}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
    gap: "{spacing.sm}"

  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    minHeight: 480px
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    ctaGap: "{spacing.sm}"

  badge-status:
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
    variants:
      interest-check:
        backgroundColor: "{colors.surface-card}"
        textColor: "{colors.muted}"
        border: "1px solid {colors.hairline}"
      group-buy:
        backgroundColor: "{colors.primary}"
        textColor: "{colors.on-primary}"
      production:
        backgroundColor: "{colors.accent-yellow}"
        textColor: "#191919"
      shipping:
        backgroundColor: "{colors.accent-green}"
        textColor: "{colors.on-primary}"
      delivered:
        backgroundColor: "{colors.surface-elevated}"
        textColor: "{colors.body}"
        border: "1px solid {colors.hairline}"
      sold-out:
        backgroundColor: "{colors.status-error}"
        textColor: "{colors.on-primary}"

  colorway-swatch:
    borderRadius: "{rounded.full}"
    size: 20px
    border: "1.5px solid transparent"
    selectedBorder: "1.5px solid {colors.primary}"
    selectedOffset: "2px solid {colors.canvas}"
    gap: "{spacing.xs}"

  collection-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    activeBackgroundColor: "{colors.surface-elevated}"
    activeTextColor: "{colors.ink}"
    activeBorder: "1px solid {colors.hairline}"
    hoverTextColor: "{colors.ink}"

  group-buy-progress:
    trackColor: "{colors.surface-elevated}"
    fillColor: "{colors.primary}"
    height: 4px
    rounded: "{rounded.full}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.caption}"
    valueColor: "{colors.body}"

  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
    focusBorder: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    height: 40px
    padding: "0 {spacing.base}"
    iconColor: "{colors.muted}"
    iconSize: 16px

  product-image-gallery:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    thumbnailSize: 72px
    thumbnailBorder: "1px solid {colors.hairline-soft}"
    thumbnailActiveBorder: "2px solid {colors.primary}"
    thumbnailRounded: "{rounded.xs}"

  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    linkColor: "{colors.body}"
    linkHoverColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.xxl}"
    copyrightColor: "{colors.muted}"
    copyrightTypography: "{typography.caption}"

  quantity-stepper:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 42px
    buttonWidth: 42px
    buttonHoverColor: "{colors.surface-elevated}"

## Components

### Buttons

**`button-primary`** — The standard purchase CTA: teal #108474 fill, white text, 8px radius, 44px tall. On hover the background shifts to `{colors.primary-active}` (#0a6358) with a 150ms ease transition; the treatment is subtle enough that the button reads as stable, not flashy. Disabled state uses `{colors.primary-disabled}`, a washed teal, with the same white text — there is no opacity trick, just the flat color swap. Because teal is the sole interactive signal on a dark canvas, the primary button appears with deliberate restraint; product pages typically show one per view.

**`button-secondary`** — Transparent background, `{colors.ink}` text, 1px `{colors.hairline}` border. Shares the same 44px height and {rounded.sm} radius as the primary so the two buttons pair naturally side-by-side (e.g., "Add to Cart" + "Buy It Now"). Hover shifts the background to `{colors.surface-elevated}` (#303030) to signal interactivity without pulling color from the primary CTA.

**`button-ghost`** — Text-only link-style button in `{colors.primary}` teal. Used for secondary navigation actions like "View All" on collection rows. No border, no background, no height constraint.

**`button-sm-outline`** — Compact 32px tall outline button in `{colors.body}` / `{colors.hairline}`, {rounded.xs} 4px. Appears on product cards for quick-action overlays (e.g., wishlist, quick-view) where a full-height button would crowd the card.

### Text Input & Search

**`text-input`** — Dark card surface (`{colors.surface-card}` #262626), 1px `{colors.hairline}` border, teal focus ring, Nunito Sans body-md. The input doesn't lighten on focus — only the border color changes — maintaining the dark-field aesthetic throughout form flows.

**`search-bar`** — Pill-shaped ({rounded.full}), 40px tall. One of the only round-cornered elements on the site. The icon is muted until the field receives focus, at which point the border transitions to `{colors.primary}`. Sits in the nav-bar on desktop, collapses to an icon tap on mobile.

### Navigation

**`nav-bar`** — 64px tall, `{colors.surface-soft}` (#212121) background with a 1px `{colors.hairline-soft}` bottom border. Nav links use Nunito Sans at 14px/600 weight in `{colors.body}`, shifting to `{colors.primary}` on hover. The logo sits left at 32px height. On desktop the primary navigation categories (Keyboards, Keycaps, Accessories, Group Buys, About) sit in the center bar; a cart icon and locale selector sit right.

**`announcement-bar`** — Full-width strip in `{colors.primary}` teal above the nav-bar. Used for active group buy countdowns, shipping notices, or discount codes. Body-sm Nunito Sans in white, centered. When a live group buy is running, the bar text acts as a persistent reminder.

### Product Cards

**`product-card`** — #262626 panel, 1px `{colors.hairline-soft}` border on rest, stepping to `{colors.hairline}` on hover. Image sits above at a 4:3 aspect ratio. Below: product title in `{typography.title-sm}`, price in `{typography.price}` (Asap 18px/500), and a status badge pinned top-left on the image. Colorway swatches render as 20px `{rounded.full}` dots below the price with a 4px gap. The card has no box shadow — elevation is communicated purely through the border color step.

### Group Buy Lifecycle Badges

**`badge-status`** — Pill-shaped ({rounded.full}), uppercase label typography at 11px/700. Five variants map the entire group buy lifecycle: Interest Check (neutral hairline border on dark fill), Group Buy (primary teal, the only moment a badge competes with the CTA), Production (amber `{colors.accent-yellow}` with dark text for legibility), Shipping (`{colors.accent-green}`), and Delivered (hairline neutral). Sold Out routes through `{colors.status-error}` red. The system ensures that at any point in a product's lifecycle, its state is scannable from the card grid without opening a PDP.

### Colorway Swatches

**`colorway-swatch`** — 20px diameter circles in {rounded.full}, rendered in the literal colorway color (lavender, rose, teal, etc.). Unselected swatches have no visible border; selected state adds a 1.5px `{colors.primary}` ring with a 2px canvas-colored gap between ring and dot, creating an outline effect without a composite component. Swatches appear on product cards (read-only preview row, max 5 visible) and on the PDP (interactive selector).

### Group Buy Progress

**`group-buy-progress`** — A 4px tall pill track in `{colors.surface-elevated}` filled with `{colors.primary}` teal. Sits below the price block on active group buy PDPs. Caption-weight labels show the unit count on the left and percentage or goal on the right in `{colors.muted}`. The bar is decorative on cards (compressed to a static snapshot) and interactive on the PDP where it may update live.

### Hero

**`hero`** — Full-width, `{colors.canvas}` background, minimum 480px tall. Title in `{typography.display-xl}` (Asap 48px/600), supporting copy in `{typography.body-md}` at `{colors.body}`. Two buttons sit side-by-side with an 8px gap: a `button-primary` CTA and a `button-secondary` secondary action. No gradient overlay; product photography is placed as a right-column or background image and masked with the canvas color on small viewports.

### Collection Filter

**`collection-filter`** — Horizontal chip row for filtering by category or status. Each chip: `{colors.surface-soft}` background, {rounded.xs}, body-sm text. Active chip steps to `{colors.surface-elevated}` with a `{colors.hairline}` border and `{colors.ink}` text. No teal used here — the filter active state is deliberately subdued so it doesn't compete with product card CTAs below.

### Footer

**`footer`** — `{colors.surface-soft}` background, 1px `{colors.hairline}` top border, {spacing.xxl} 48px vertical padding. Four-column grid on desktop: Products, Support, Community, Social. Section headings in Nunito Sans title-sm at `{colors.ink}`; links in body-sm at `{colors.body}`, shifting to `{colors.primary}` on hover. Copyright line in caption at `{colors.muted}`, centered below the columns.

### Product Image Gallery

**`product-image-gallery`** — Main image area in `{colors.surface-card}` (#262626) at {rounded.sm}. Thumbnail strip runs below the main image: 72×72px tiles, {rounded.xs} 4px, 1px `{colors.hairline-soft}` border at rest, stepping to a 2px `{colors.primary}` border when active. No lightbox by default; clicking the main image on mobile enters a swipe-enabled full-screen overlay over a `{colors.scrim}` backdrop.

### Quantity Stepper

**`quantity-stepper`** — 42px tall inline control: minus button | count | plus button, each zone 42px wide. `{colors.surface-card}` background, 1px `{colors.hairline}` border, {rounded.sm}. Button zones shift to `{colors.surface-elevated}` on hover. Count displayed in `{typography.body-md}` centered. Sits immediately left of the "Add to Cart" button on PDPs.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to logo + hamburger + cart icon; search moves behind tap-to-expand icon; hero stacks text above image; colorway swatches scroll horizontally; collection filter chips scroll horizontally without wrapping; announcement-bar text truncates to one line |
| Tablet | 744–1128px | Two-column product grid; nav-bar shows top-level categories, sub-menus behind tap; hero uses 60/40 text/image split; filter chips wrap to two rows; footer compresses to two columns |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with hover drop-downs; hero uses side-by-side layout; filter panel optionally moves to left sidebar; footer expands to four columns |
| Wide | > 1440px | Content constrained to ~1400px max-width centered in canvas; product grid stays at four columns; hero padding scales to {spacing.section} × 1.5; wide negative space on canvas sides reinforces dark-field premium feel |

### Touch Targets

- All interactive elements minimum 44×44px on mobile (buttons, swatches, stepper zones, nav icons)
- Colorway swatch dots expand hit area to 32×32px via padding even though the visible dot is 20px
- Thumbnail gallery tiles maintain 72px tap targets on mobile rather than scaling down
- Filter chips minimum 36px tall on mobile with adequate horizontal padding

### Collapsing Strategy

- Nav collapses to hamburger at < 744px; drawer slides in from left over a `{colors.scrim}` overlay
- Collection filter row hides the "active" label chip at < 744px and shows a "Filter" icon-button instead
- Footer grid collapses: 4-col → 2-col at tablet → 1-col accordion at mobile (sections tap-to-expand)
- Product card colorway swatch row caps at 5 dots on cards at all breakpoints; excess indicated by "+N" label in `{colors.muted}`
- Announcement bar hides on scroll-down on mobile (IntersectionObserver pattern), reappears on scroll-up

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Asap and Nunito Sans font weights actively used on live pages not confirmed — weight 500/600 inferred from visual hierarchy; 700 inferred for buttons
- No confirmed font-size scale from CSS extraction; all px values are reasonable estimates based on Shopify theme conventions and visual inspection
- Icon system not identified — JudgemeIcons and JudgemeStar in font stack are review-widget assets, not brand icons; actual nav and UI iconography source unknown
- Animation/transition timing functions not extracted (150ms ease assumed for buttons; no parallax or scroll-trigger data confirmed)
- Light-mode or high-contrast variant existence unconfirmed — all palette tokens assume dark-canvas-first rendering
- Exact grid column count and gutter widths for product collections not confirmed from CSS
- Mega-menu or drop-down nav structure on desktop not confirmed
- Mobile nav drawer animation direction and overlay opacity not extracted
- Currency/locale selector placement and behavior not confirmed
- Review widget styling (star colors, rating bar fills) sourced from JudgeMe third-party embed — not a Wuque-controlled design token
