---
version: alpha
name: "NuGlas"
source_url: "https://www.nuglas.com.au"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every product NuGlas sells begins with optical clarity — 9H hardness tempered glass engineered to vanish onto a phone display — and the brand's digital identity follows that same zero-distraction logic: white canvas, soft neutral surfaces, and a single tech-blue primary that fires on CTAs without competing with device photography. The harder design challenge in screen protectors is SKU specificity: shoppers arrive knowing their exact phone model and need rapid confirmation of compatibility before committing. The layout architecture centers on this need — device filter strips appear persistently across category pages as make-model-generation lookups, a first-class interaction rather than a buried sidebar facet. Product cards carry dense functional metadata beneath clean hero shots: hardness rating badges, anti-fingerprint claims, edge-coverage indicators, and package counts rendered as small `{rounded.xs}` chips in `{colors.surface-badge}` sitting on a `{colors.surface-card}` background. Rounding is consistent but professional, landing at `{rounded.sm}` for cards and `{rounded.md}` for form inputs — approachable without softness that would undermine the technical positioning. Button language is direct and transactional: "Add to Cart", "Find My Device", "Shop iPhone 16 Cases". Trust signals — installation kit inclusion, lifetime replacement guarantees, and retail packaging callouts — cluster in the add-to-cart zone beneath price, reinforcing purchase confidence at the moment of highest intent. Type weights are modest; this brand does not rely on heavy display headlines, because the product name and device-model confirmation carry more conversion weight than editorial ambition. The footer likely carries compatibility tables and a model lookup tool, serving the shopper who arrives from a deep-linked device page. The palette, typeface stack, and exact spacing tokens could not be reliably extracted from the live site (JS-loaded tokens, possible headless build); all values below are category-informed estimates. Treat this file as a calibration-required scaffold pending access to live brand assets.

colors:
  primary: "#0063cc"
  primary-active: "#004fa3"
  primary-disabled: "#99c2e8"
  ink: "#111111"
  body: "#333333"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  canvas: "#ffffff"
  surface-soft: "#f5f7fa"
  surface-card: "#ffffff"
  surface-badge: "#eef2f7"
  on-primary: "#ffffff"
  success: "#16a34a"
  success-soft: "#dcfce7"
  warning: "#d97706"
  warning-soft: "#fef3c7"
  error: "#dc2626"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  badge-label:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  price-md:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  filter-tab:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  model-lookup:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-find-device:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.model-lookup}"
    border: "1px solid {colors.hairline}"
    border-focus: "1.5px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: 10px 14px
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.model-lookup}"
    border: "1px solid {colors.hairline}"
    border-focus: "1.5px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: 10px 16px
    height: 44px
    iconColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 60px
    logoHeight: 28px
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
  device-filter-strip:
    backgroundColor: "{colors.surface-soft}"
    borderBottom: "1px solid {colors.hairline}"
    tabTextColor: "{colors.muted}"
    tabTextColor-active: "{colors.primary}"
    tabTypography: "{typography.filter-tab}"
    tabPadding: 8px 16px
    tabBorderBottom-active: "2px solid {colors.primary}"
    height: 48px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-md}"
    priceColor: "{colors.ink}"
    badgeGap: "{spacing.xs}"
    padding: "{spacing.md}"
    shadow: "0 1px 4px rgba(0,0,0,0.06)"
  feature-badge:
    backgroundColor: "{colors.surface-badge}"
    textColor: "{colors.body}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  compatibility-chip:
    backgroundColor: "{colors.success-soft}"
    textColor: "{colors.success}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.sm}"
    minHeight: 440px
    contentMaxWidth: 560px
  add-to-cart-row:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    priceTypography: "{typography.price-lg}"
    priceColor: "{colors.ink}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-md}"
    buttonRounded: "{rounded.sm}"
    buttonHeight: 48px
    padding: "{spacing.base} 0"
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    itemGap: "{spacing.xl}"
    padding: "{spacing.md} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    textColor-active: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    mutedTextColor: "{colors.muted-soft}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} 0 {spacing.xl}"
  model-lookup-widget:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    inputTypography: "{typography.model-lookup}"
    inputBorderFocus: "1.5px solid {colors.primary}"
    dropdownBg: "{colors.canvas}"
    dropdownBorder: "1px solid {colors.hairline}"
    dropdownItemHoverBg: "{colors.surface-soft}"
    dropdownItemTypography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

### Buttons

**`button-primary`** — The main conversion driver used for "Add to Cart" and "Shop Now" actions. Solid `{colors.primary}` fill on a `{rounded.sm}` corner, 44px tall with 24px horizontal padding. Active state deepens to `{colors.primary-active}`; disabled washes to `{colors.primary-disabled}`. The weight-600 `{typography.button-md}` label reads as confident without aggression.

**`button-secondary`** — Outlined variant with a 1.5px `{colors.primary}` border and matching text on a `{colors.canvas}` background, equal height and rounding to primary. Used for secondary CTAs — "View Full Compatibility List", "Compare Models" — where a ghost treatment would be too low-contrast against light section backgrounds.

**`button-ghost`** — Transparent background with `{colors.body}` text in `{typography.button-sm}`. Reserved for lowest-hierarchy actions: "Clear Filters", "Show Less", inline table dismiss. No border.

**`button-find-device`** — Dark `{colors.ink}` fill paired with `{colors.canvas}` text, used specifically in the homepage hero alongside the model-lookup widget as a high-contrast CTA that reads clearly on `{colors.surface-soft}` hero backgrounds. Same rounding and height as primary.

### Inputs

**`text-input`** — Standard form field with a 1px `{colors.hairline}` border tightening to `{colors.primary}` on focus. `{rounded.md}` corners, 44px tall. Placeholder text renders in `{colors.muted}`.

**`search-bar`** — Full-radius `{rounded.full}` variant for site-wide search in the nav header. Set on `{colors.surface-soft}` with a leading icon in `{colors.muted}`; activates with a `{colors.primary}` ring on focus. The pill shape provides visual contrast against the boxy nav chrome.

**`model-lookup-widget`** — Multi-step cascading select for Brand → Device Family → Model, the most brand-critical interactive component in the system. Appears embedded in the hero on the homepage and as a persistent sticky element on category pages. Dropdown rows hover on `{colors.surface-soft}`; the confirm action uses `button-primary` styling. `{rounded.md}` outer container on a `{colors.canvas}` background with a `{colors.hairline}` border.

### Navigation

**`nav-bar`** — 60px tall, `{colors.canvas}` background with a single `{colors.hairline}` bottom border. Logo sits left at 28px height; category links run center in `{typography.nav-link}` weight 500; a cart icon and primary CTA ("Find My Device" or "Shop Now") anchor the right in `{colors.primary}` at `{rounded.sm}`. On scroll, the bar acquires a soft box-shadow to maintain visual separation from page content.

**`device-filter-strip`** — A 48px sticky strip directly below the nav on category pages, carrying horizontal tab selectors for Apple, Samsung, Google, and other device brands in `{typography.filter-tab}`. The active tab shows a 2px `{colors.primary}` underline with colored text; inactive tabs render in `{colors.muted}`. The strip scrolls horizontally on mobile rather than wrapping.

**`breadcrumb`** — Small `{typography.caption}` trail in `{colors.muted}` with chevron separators in `{colors.muted-soft}`. The current page label shifts to `{colors.ink}` weight 500 to confirm location without using a full heading.

### Product Display

**`product-card`** — White `{colors.surface-card}` card with a 1px `{colors.hairline}` border, `{rounded.sm}` corners, and a subtle 1px drop shadow. Product imagery sits on a `{colors.surface-soft}` background to normalize transparent-background product photography. Title in `{typography.title-sm}`, price in `{typography.price-md}`, feature badges stacked horizontally below the title with `{spacing.xs}` gap.

**`feature-badge`** — Uppercase `{typography.badge-label}` chips in `{colors.surface-badge}` background with `{colors.body}` text, carrying product attribute claims: "9H HARDNESS", "ANTI-FINGERPRINT", "EDGE-TO-EDGE". `{rounded.xs}` corners, 3px vertical padding. These are the primary mechanism for conveying technical differentiation on card surfaces.

**`compatibility-chip`** — Same geometry as `feature-badge` but rendered in `{colors.success-soft}` with `{colors.success}` text. Carries the confirmed device model label ("Fits iPhone 16 Pro") directly on product cards in category listings and in the add-to-cart zone on PDP. Green color language signals a positive match, removing doubt at the point of purchase.

**`sale-badge`** — `{colors.primary}` background with `{colors.on-primary}` text in `{typography.badge-label}` and `{rounded.xs}` corners. Floats as an absolute overlay on the top-left corner of product card images for discounted SKUs.

### Product Detail

**`add-to-cart-row`** — Full-width strip in the PDP buy-box, sticky at the bottom of the viewport on mobile scroll. Price in `{typography.price-lg}` on the left; the 48px "Add to Cart" `button-primary` on the right; a `{colors.hairline}` top border separates it from the content above. The `compatibility-chip` sits immediately above the price to keep device confirmation visible at the moment of commitment.

**`hero`** — `{colors.surface-soft}` background with the headline in `{typography.display-xl}` and supporting copy in `{typography.body-md}`. On the homepage the model-lookup-widget is embedded inline in the hero body; on category pages the hero is abbreviated and flows directly into the device-filter-strip. Minimum 440px height desktop.

### Trust & Footer

**`trust-bar`** — A horizontal strip carrying three to four trust signals — free shipping threshold, 30-day returns, lifetime replacement guarantee, Australian-owned callout — each with a small icon in `{colors.primary}` and label in `{typography.caption}`. Rendered on `{colors.surface-soft}` with thin `{colors.hairline}` borders top and bottom. Appears once below the hero and once above the footer.

**`footer`** — Dark `{colors.ink}` background with `{colors.canvas}` text organized into link columns. Column headings in `{typography.title-sm}` weight 600; link lists in `{typography.body-sm}`. Legal and sitemap links render in `{colors.muted-soft}`. A "Find My Device" lookup input is likely embedded in the footer head section, serving the shopper who lands on the footer while researching compatibility.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + cart icon; device-filter-strip scrolls horizontally; add-to-cart-row sticks to bottom viewport; hero stacks headline above model-lookup-widget |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline; device-filter-strip remains sticky below nav; hero places text left and model-lookup-widget right |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with all category links visible; trust-bar expands to single horizontal row; PDP uses side-by-side layout with image gallery left and buy-box right |
| Wide | > 1440px | Max-width container (~1280px) centers all content; grid holds at four columns; hero gains generous vertical padding but caps image scale |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Filter strip tabs use 48px height to meet touch target requirements while appearing visually slimmer via padding
- Cart icon and hamburger menu in the nav are padded to 44px tap area
- Product cards are fully tappable (not just image or title) and route to PDP
- Model-lookup dropdown rows are minimum 44px tall for comfortable selection

### Collapsing Strategy

- Nav collapses to hamburger at < 744px; drawer slides from left with the full category tree and a search bar at top
- Device filter strip switches from scrolling text tabs to a compact dropdown `<select>` at < 480px
- Trust bar stacks into a 2×2 grid at < 744px; single column at < 480px
- Footer link columns collapse to accordions at < 744px
- Product card badge row truncates beyond three badges with a "+N more" overflow chip at mobile widths

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted**: the live site returned zero hex values — likely JS-rendered tokens, anti-bot protection, or a headless build. All palette values above are category-informed estimates; do not ship without sampling from live brand assets
- **Primary color unconfirmed**: `#0063cc` is a plausible tech-blue for the phone accessories category but is inferred — NuGlas's actual primary was not reliably documented in public sources at time of writing
- **No fonts extracted**: typeface stack defaulted to Inter with system fallbacks; actual brand font may be a licensed geometric or humanist sans-serif
- **No page title or meta theme-color**: the HTML head returned no canonical brand signals; theme-color meta tag was absent or blocked
- **Exact rounding values unknown**: `{rounded.sm}` (8px) and `{rounded.md}` (12px) are category norms; actual product measurements may differ
- **Icon system unknown**: NuGlas may use a licensed set (Phosphor, Heroicons, custom SVG library); no data available
- **Motion and animation tokens absent**: hover transitions, drawer animation timing, and add-to-cart micro-interactions could not be derived
- **Dark mode stance unknown**: no evidence of dark mode support found; assume light-only until confirmed
- **AUD pricing and locale conventions**: Australian-market formatting ($ symbol positioning, GST display, free shipping threshold) should be validated against live store behavior before implementing price display components
