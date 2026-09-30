---
version: alpha
name: "Crescent Garden"
source_url: "https://www.crescentgarden.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Four distinct greens sit alongside a deep-water teal (#0e252c) that does the heavy lifting no plant-brand would normally trust to near-black — Crescent Garden leans into the darkness rather than retreating to beige or sage-wash. The primary button blue (#2ea3f2) is the one sharp break from the botanical register, a utility signal that reads as open sky against all that foliage below it. Backgrounds stack in near-whites (#f9f9f9, #f4f4f4) with gray hairlines (#e0e0e0, #bbbbbb) giving product photography clean air, while the dark teal anchors the nav and footer to something with soil-weight. The green family moves from a muted sage (#7cc68d) through forest (#31856c) and deep forest (#276a56) down to a jewel-toned teal-mint (#18b394) — a range that covers fresh-growth to aged-copper, letting planter product photos sit on-palette regardless of what is planted in them. Type is Open Sans throughout, a workmanlike geometric sans that yields the stage to product imagery; display headings run large and weight-600 while product labels lean 400 at 14px. An unexpected lavender (#c37cc6) and amber (#edb059) surface in the swatch data — SKU colorways rather than brand decisions, but present enough to need deliberate swatch UI handling. The site is built on Divi (WordPress), confirmed by the ETmodules icon font and slick.js carousel signatures, which constrains some layout geometry to that builder's grid conventions. Rounded language is modest: cards and buttons use small `{rounded.xs}`–`{rounded.sm}` radii, keeping the catalog grid serious rather than lifestyle-pop.

colors:
  primary: "#2ea3f2"
  primary-active: "#1a87d4"
  primary-disabled: "#a8d8f8"
  ink: "#0e252c"
  body: "#3e3e3e"
  muted: "#8d9096"
  muted-soft: "#adb1b8"
  hairline: "#e0e0e0"
  hairline-soft: "#e8e8e8"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-muted: "#f4f4f4"
  surface-card: "#f4f4f4"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  brand-dark: "#0e252c"
  brand-dark-mid: "#203741"
  brand-slate: "#4d5d64"
  blue-pale: "#d8e2e7"
  green-forest: "#31856c"
  green-deep: "#276a56"
  green-sage: "#7cc68d"
  green-teal: "#18b394"
  alert-red: "#ce2b37"
  swatch-terra: "#cd5c5c"
  swatch-amber: "#edb059"
  swatch-lavender: "#c37cc6"
  dark-blue: "#003388"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  price-display:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  swatch-label:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  filter-label:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  promo-text:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px

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
    padding: 14px 28px
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
    border: "2px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: "2px solid {colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.brand-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    paddingX: "{spacing.xl}"
  nav-bar-utility-strip:
    backgroundColor: "{colors.brand-dark-mid}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    paddingX: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageAspect: "4/3"
    padding: "{spacing.base}"
    shadow: "0 2px 8px rgba(14,37,44,0.08)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-badge-area:
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
    display: flex
    gap: "{spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.alert-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.green-forest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "2px solid transparent"
    outlineOffset: 2px
    tapTarget: 40px
    gap: "{spacing.xs}"
  swatch-tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.swatch-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  size-selector-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 14px
    height: 36px
  size-selector-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
  hero-section:
    backgroundColor: "{colors.brand-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 480px
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.section}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subline:
    typography: "{typography.body-md}"
    textColor: "{colors.blue-pale}"
  hero-cta-row:
    display: flex
    gap: "{spacing.base}"
    marginTop: "{spacing.lg}"
  collection-filter-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    borderBottom: "2px solid {colors.hairline}"
    typography: "{typography.filter-label}"
    rounded: "{rounded.none}"
    paddingY: "{spacing.sm}"
    paddingX: "{spacing.base}"
  promo-banner:
    backgroundColor: "{colors.green-forest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.promo-text}"
    paddingY: "{spacing.sm}"
    textAlign: center
  newsletter-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    paddingY: "{spacing.section}"
    paddingX: "{spacing.xxl}"
  newsletter-headline:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.brand-dark}"
    textColor: "{colors.blue-pale}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
    paddingY: "{spacing.xxl}"
    columns: 4
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    separator: "/"
    marginBottom: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary CTA renders in Crescent Garden's sky blue (#2ea3f2) with white uppercase Open Sans at 15px weight-700 and 0.6px tracking. The 4px `{rounded.xs}` radius keeps the shape square-leaning — authoritative, not friendly. Hover shifts to `{colors.primary-active}` (#1a87d4); disabled drains to `{colors.primary-disabled}` (#a8d8f8) with no cursor change.

**`button-secondary`** — Outlined in a 2px `{colors.ink}` border with white fill. Used for secondary actions like "View Details" or "Compare" where the primary would crowd the layout. Active state inverts to ink fill with white text. Height and padding match primary for easy side-by-side pairing.

**`button-ghost`** — Transparent with `{colors.primary}` text, no border. Typically used inline on content cards or within product description blocks.

### Text Input
**`text-input`** — A 44px-tall input with 1px `{colors.hairline}` border, shifting to `{colors.primary}` on focus. Open Sans `{typography.body-md}` at 400 weight. Applied to newsletter capture, site search overlay, and any account/checkout form fields.

### Navigation
**`nav-bar`** — The full-width header sits on `{colors.brand-dark}` (#0e252c), a near-black deep teal that immediately differentiates the site from generic white-header garden retail. Links render in white Open Sans 14px weight-600 with slight letter-spacing. A utility strip (`nav-bar-utility-strip`) at 36px above the main nav in `{colors.brand-dark-mid}` (#203741) carries shipping thresholds, phone, and account links at `{typography.caption}` size. The ETmodules icon font handles cart, account, and search glyphs in white. On scroll, the nav remains fixed and opaque with no transparency treatment.

### Product Card
**`product-card`** — Cards sit on `{colors.surface-card}` (#f4f4f4) with a soft `rgba(14,37,44,0.08)` shadow and `{rounded.sm}` corners. Product image occupies a 4:3 aspect ratio crop. Title in `{typography.title-sm}` weight-600 sits above price in `{typography.price-display}` weight-700. A row of `color-swatch` circles appears below the price, allowing quick colorway preview without leaving the grid. Badge chips (`badge-sale`, `badge-new`) overlay the top-left corner of the image absolutely.

### Color Swatches
**`color-swatch`** — 28px circles at `{rounded.full}`, spanning the planter colorway catalog: greens (`{colors.green-sage}`, `{colors.green-forest}`), earthy tones (`{colors.swatch-terra}`, `{colors.swatch-amber}`), the unexpected `{colors.swatch-lavender}`, and standard grays/whites. The selected swatch carries a 2px `{colors.ink}` ring with 2px offset gap. A `swatch-tooltip` (dark ink pill at `{rounded.xs}`) appears on hover naming the colorway in `{typography.swatch-label}`. On mobile, swatches wrap to a second row with a "+N" overflow label if more than six are present.

### Badges
**`badge-sale`** — `{colors.alert-red}` (#ce2b37) background, white uppercase text at 11px, `{rounded.xs}`. Applied absolute top-left over product card imagery. **`badge-new`** — Same geometry in `{colors.green-forest}` (#31856c) for newly launched SKUs. Both are small enough (3px 8px padding) to avoid obscuring the product image significantly.

### Hero Section
**`hero-section`** — Full-width dark banner on `{colors.brand-dark}` with the headline in `{typography.display-xl}` white and a supporting subline in `{colors.blue-pale}` (#d8e2e7) for warmth and contrast without full brightness. Min-height 480px. A `hero-cta-row` below the subline pairs a `button-primary` with a `button-secondary` (which uses `{colors.on-dark}` border treatment on dark backgrounds). Used on the homepage and seasonal campaign landing pages.

### Collection Filter Bar
**`collection-filter-bar`** — A `{rounded.none}` horizontal strip in `{colors.surface-soft}` carrying sort dropdowns and filter controls in `{typography.filter-label}`. A 2px `{colors.hairline}` bottom border separates it from the product grid. Size chips (`size-selector-chip`) sit to the right, toggling to the ink-filled `size-selector-chip-active` state. On mobile, this bar becomes a bottom sheet triggered by a filter icon button.

### Promo Banner
**`promo-banner`** — Full-width `{colors.green-forest}` strip for sitewide promotions. Centered `{typography.promo-text}` in white. Pinned just above the `nav-bar-utility-strip`. Dismissed via an X icon; reappears on next session if promo is still active.

### Newsletter Section
**`newsletter-section`** — On `{colors.surface-soft}` with generous `{spacing.section}` vertical padding. `newsletter-headline` in `{typography.display-sm}` weight-600, followed by a line of `{typography.body-md}` copy. An inline `text-input` + `button-primary` pair captures email. Renders centered at 640px max-width.

### Footer
**`footer`** — Deep `{colors.brand-dark}` background, body text in `{colors.blue-pale}` for legibility without full-white glare. Four columns at desktop: Shop, About, Support, Connect. Link hover shifts to `{colors.primary}` (#2ea3f2) for a warm sky-blue pop against the dark. Collapses to a single-column accordion on mobile.

### Breadcrumb
**`breadcrumb`** — Minimal `{colors.muted}` text in `{typography.caption}` with "/" separators in `{colors.muted-soft}`. Sits below the nav bar on PDP and collection pages, margin-bottom `{spacing.base}` before the page headline.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; utility strip hides entirely; hero drops to 320px min-height with stacked CTA row; color swatches cap at 6 with "+N" label; filter bar becomes bottom sheet; promo banner wraps to two lines |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links, sub-categories behind "More" overflow; hero at 400px; filter bar displays as horizontal scroll strip with visible overflow fade |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with Divi mega-menu dropdowns; hero at 480px; filter bar as sticky horizontal strip above grid |
| Wide | > 1440px | Four-column product grid; 1440px max-content-width with `{colors.canvas}` lateral fills; hero image bleeds full-width behind a constrained 800px text column |

### Touch Targets
- All buttons minimum 44px height
- Color swatches have 40px tap target (swatch itself is 28px; transparent padding expands the hit area)
- Nav items minimum 44px height on mobile drawer
- Filter chips minimum 40px height on mobile
- Size selector chips minimum 40px height on mobile

### Collapsing Strategy
- Utility strip (shipping/phone notices) disappears entirely below 744px to recover vertical space for primary nav
- Mega-menu navigation drops to full-screen slide-in panel on mobile and tablet
- Footer collapses to stacked accordion sections on mobile
- Product card swatch row caps at 6 swatches on mobile with an overflow indicator
- Hero CTA row stacks vertically on mobile if both buttons are present

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact primary button corner radius not confirmed from live extraction; `{rounded.xs}` (4px) is inferred from Divi builder patterns — could range from fully square (0px) to 6px
- `ETmodules` is the Elegant Themes Divi icon font; no custom SVG icon system or separate icon library detected
- Open Sans weight range not confirmed — site may use only 400/600 or include 300/700 variants
- Mega-menu category structure and depth not extracted; assumed from planter-brand category conventions (Shape, Size, Material, Color, Style)
- No cart drawer, quickview modal, or lightbox design data recovered
- `#2ea3f2` as primary CTA is plausibly a Divi builder default retained as brand blue; if the brand refreshes, `{colors.green-forest}` (#31856c) or `{colors.green-deep}` (#276a56) are botanically aligned candidates for primary promotion
- `#003388` / `#003399` (dark blues) likely belong to Amazon/external marketplace link styling rather than core brand palette
- No dark-mode support detected
- Slick.js carousel is present but carousel card design (hero banners, product feature sliders) not extracted
- Exact Divi grid column gutter width not confirmed; values follow 30px Divi default convention
