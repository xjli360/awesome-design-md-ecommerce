---
version: alpha
name: "Karas Pen Co."
source_url: "https://karaskustoms.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every Karas pen begins as bar stock — aluminum, brass, or titanium — cut on CNC machines a few blocks from their Phoenix storefront, and that manufacturing origin is fully legible in the digital shop. A near-black #171717 anchors the site header, signaling workshop over boutique; the primary action color is a machined-deep teal (#108474), saturated enough to own the screen without reading as corporate blue. A jolt of marigold (#fbcd0a) surfaces on sale pricing, material callouts, and select badges — the visual equivalent of a single brass detail on an otherwise matte-anodized barrel. Light neutral backgrounds cascade through #f9fafb, #f2f2f2, and #edf5f5, keeping anodized-barrel photography visible without chromatic competition, while a faint mint wash (#c5f7f0) backs configurator panels and informational callouts, echoing the primary palette without pulling full saturation. Inter's geometric letterforms handle all type: body copy runs 16px at weight 400, pen names display at 28–40px in weight 700, and every SKU label sits at 13px weight 600 — a hierarchy built for catalog density rather than editorial breathing room. Radii stay at {rounded.xs} to {rounded.sm} throughout; the machined aesthetic rejects pill shapes, so only the search field concedes to {rounded.md}. Checkout and product-detail flows surface material selectors and finish options as inline tag rows rather than dropdown menus, letting customers spec their order like configuring a part — which, effectively, is what they are doing.

colors:
  primary: "#108474"
  primary-active: "#0a6159"
  primary-disabled: "#7bbdb7"
  primary-light: "#edf5f5"
  accent-gold: "#fbcd0a"
  accent-gold-muted: "#fde99b"
  accent-mint: "#c5f7f0"
  ink: "#171717"
  body: "#1f1f1f"
  muted: "#7b7b7b"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#f9fafb"
  canvas-white: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  surface-teal-wash: "#edf5f5"
  surface-dark: "#121212"
  surface-dark-elevated: "#1f1f1f"
  on-primary: "#ffffff"
  on-dark: "#f9fafb"
  on-gold: "#171717"

typography:
  display-xl:
    fontFamily: "'Inter', 'Open Sans', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.4px
  display-sm:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  sku-label:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  price-lg:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  price-sale:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  material-tag:
    fontFamily: "'Inter', 'Open Sans', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1px

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
    padding: 12px 24px
    height: 46px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 46px
  button-ghost-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    border: "1px solid rgba(255,255,255,0.3)"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 46px
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 52px
    width: "100%"
  text-input:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  search-field:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: 9px 40px 9px 14px
    height: 40px
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    imageRatio: "1:1"
    padding: "{spacing.base}"
    nameTypography: "{typography.title-md}"
    priceTypography: "{typography.price-lg}"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.muted}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.10)"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 540px
    paddingX: "{spacing.xxl}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"
  material-badge:
    backgroundColor: "{colors.surface-teal-wash}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.accent-mint}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  option-tag-default:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.material-tag}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
  option-tag-selected:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary}"
    typography: "{typography.material-tag}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 6px 12px
  option-tag-unavailable:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.material-tag}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    padding: 6px 12px
    opacity: 0.45
    textDecoration: line-through
  price-display:
    regularPriceTypography: "{typography.price-lg}"
    regularPriceColor: "{colors.ink}"
    salePriceTypography: "{typography.price-sale}"
    salePriceColor: "{colors.primary}"
    compareAtTypography: "{typography.body-sm}"
    compareAtColor: "{colors.muted}"
    compareAtTextDecoration: line-through
    saleLabelBackgroundColor: "{colors.accent-gold}"
    saleLabelTextColor: "{colors.on-gold}"
    saleLabelTypography: "{typography.badge}"
    saleLabelRounded: "{rounded.xs}"
    saleLabelPadding: 3px 6px
  configurator-panel:
    backgroundColor: "{colors.surface-teal-wash}"
    border: "1px solid {colors.accent-mint}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.sku-label}"
    labelColor: "{colors.muted}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption-sm}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted-soft}"
    bodyTypography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.accent-mint}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — Solid #108474 fill on a 4px-radius (`{rounded.xs}`) rectangle, 46px tall, with 12–24px padding and 15px weight-600 Inter (`{typography.button-md}`). Hover steps the background to `{colors.primary-active}` (#0a6159); disabled pulls to `{colors.primary-disabled}` — a washed teal that communicates unavailability through color shift rather than opacity.

**`button-secondary`** — White fill, 1.5px #dedede border, identical dimensions to `button-primary`. Surfaces on product pages for secondary actions (wishlist, compare) where the full-width add-to-cart already holds primary hierarchy.

**`button-ghost-dark`** — Transparent with a 30%-opacity white border, used over `{colors.surface-dark}` hero sections. The letterforms ghost against near-black without the visual weight of a filled teal block.

**`button-add-to-cart`** — Full-width variant of `button-primary` at 52px tall, 32px horizontal padding. The larger footprint at the base of the product sidebar signals purchase intent without a separate visual treatment.

### Navigation
**`nav-bar`** — Opaque #171717 background, 64px tall, housing the wordmark left, category links center, and cart/account icons right. Link labels use `{typography.nav-link}` in `{colors.on-dark}`; a teal underline on hover signals the active state. The bar does not shift color or apply blur at any scroll depth — it is the same dark band from page top to checkout.

### Product Cards
**`product-card`** — White card with a 1px `{colors.hairline-soft}` border and `{rounded.sm}` corners, 16px inner padding. The upper section is a 1:1 product image; below it, pen name in `{typography.title-md}`, material/finish line in `{typography.caption}` / `{colors.muted}`, and price in `{typography.price-lg}`. Badge slots (`{components.sale-badge}`, `{components.new-badge}`, `{components.material-badge}`) anchor to the image's top-left corner. Hover tightens the border to `{colors.hairline}` and raises a 4–16px drop shadow.

### Hero
**`hero`** — Full-bleed dark section in `{colors.surface-dark}` (#121212), minimum 540px tall. Headline in `{typography.display-xl}` and sub-head in `{typography.display-sm}`, both in `{colors.on-dark}`. The teal CTA button sits below the subhead with `{rounded.xs}` geometry. At desktop, product photography (pen on raw metal surface, machined detail close-up) fills the right 50%; on mobile the image stacks above the text block. A faint 1px teal bottom edge transitions the dark band into the lighter catalog below.

### Configurator Panel
**`configurator-panel`** — Light teal-wash (#edf5f5) panel with a #c5f7f0 border and `{rounded.sm}` corners, used to group material, finish, and grip selectors in the product detail view. Each option renders as an `option-tag-default`, `option-tag-selected`, or `option-tag-unavailable` tag row. Section labels use `{typography.sku-label}` in `{colors.muted}` — tracking the parts-manifest aesthetic, not a shopping-form idiom. Unavailable options stay visible at 45% opacity with strikethrough rather than being hidden, preserving the full spec chart.

### Badges
**`material-badge`** — Teal-wash fill with #108474 text and a #c5f7f0 border, 11px all-caps Inter. Applied to material callouts ("CNC ALUMINUM", "BRASS", "TITANIUM"). **`sale-badge`** uses `{colors.accent-gold}` fill with `{colors.on-gold}` (#171717) text — marigold in a neutral grid is unmissable. **`new-badge`** uses full `{colors.primary}` fill with white text, sharing geometry with the other badge types at 4px radius and 4–8px padding.

### Price Display
**`price-display`** — Regular price in `{typography.price-lg}` / `{colors.ink}`. On sale: sale price shifts to `{typography.price-sale}` / `{colors.primary}` (teal), compare-at price strikes through in `{colors.muted}`, and a gold `sale-badge` appears inline to the right of the sale price. This three-element teal/struck-muted/gold-pill pattern is consistent across product cards and the PDP sidebar.

### Footer
**`footer`** — Matches the nav bar's `{colors.surface-dark}` background. Section headings in `{typography.title-sm}` / `{colors.on-dark}`; link lists in `{typography.body-sm}` / `{colors.muted-soft}`. Link hover transitions to `{colors.accent-mint}`, echoing the primary accent without pulling full-saturated teal onto a dark surface. The footer's mint hover is the only place this pale tint appears outside the configurator panel.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; configurator panel collapses to accordion below imagery; add-to-cart sticky to bottom viewport bar; nav collapses to hamburger drawer |
| Tablet | 744–1128px | 2-column product grid; configurator panel moves inline below image; hero stacks image above text block |
| Desktop | 1128–1440px | 3-column product grid; PDP splits 60/40 image/sidebar; hero runs side-by-side |
| Wide | > 1440px | 3–4 column grid within 1440px max-width centered container; hero image fills right half at full bleed |

### Touch Targets
- All buttons minimum 44px height; add-to-cart 52px full-width on mobile
- Option tags minimum 36px height on mobile, wrapping to multi-line before truncating
- Nav icons minimum 44×44px tap area
- Quantity steppers and pagination controls minimum 44px

### Collapsing Strategy
- Primary nav collapses into a slide-in drawer at < 744px; category hierarchy preserved as nested accordion
- Hero headline reduces from 40px to 28px on mobile; sub-head from 22px to 18px
- Configurator option rows wrap to multi-line before collapsing to accordion below ~400px
- Footer columns stack to 2-up at tablet, single column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed custom display typeface — Inter is inferred from the extracted font stack but a secondary headline or monospace face used in machining-spec callouts may not have been captured
- Hover and focus transition durations not extracted (animation timing curves unknown)
- Mega-menu or dropdown structure for main nav categories not confirmed
- Checkout and cart page palette may surface additional surface tokens absent from homepage extraction
- Mobile sticky add-to-cart behavior (fixed bar vs. scroll-triggered overlay) not confirmed
- PDP image aspect ratios for grip detail and barrel close-up shots not confirmed (may use portrait 3:4 or panoramic crops rather than the standard 1:1)
- No icon library confirmed — custom SVG set vs. a system library (e.g., Heroicons, Phosphor) is unknown
