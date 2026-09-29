---
version: alpha
name: "Whirlpool"
source_url: "https://www.whirlpool.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every primary CTA, logo lockup, and navigation anchor in Whirlpool's digital presence runs from the same deep navy well — a saturated #003087 blue that functions as a single load-bearing color, carrying trust signals across product filters, service CTAs, and promotional banners without any secondary hue needing to shoulder the weight. The canvas beneath is pure white, making high-resolution appliance photography the actual texture of the UI: front-load washers, top-mount dryers, and refrigerators shot on seamless white become indistinguishable from the surface they sit on, collapsing the boundary between editorial and product. Navigation is category-first — Washers, Dryers, Refrigerators, Dishwashers each claim a top-level node — and the comparison architecture is unusually prominent for a consumer brand, with sticky side-by-side rails that treat spec sheets as primary content rather than PDF downloads. Type runs in a clean geometric sans-serif at restrained weights; display sits around 32–36px at weight 700 for heroes, then drops sharply to 14–16px body copy, creating a two-tier rhythm with almost nothing in between. Button radii are modest (`{rounded.sm}`) — not pill-shaped, not square — landing at the pragmatic middle of a brand that prizes utility over charm. Promotional badges use a #e31837 alert red that appears only in sale contexts, functioning as a pure attention signal rather than a brand expression. The overall system reads as a confident, mid-century American manufacturer that has translated its physical reliability into a UI language: no gradient, no illustration, no dark-mode toggle — just navy, white, appliance chrome, and a grid that trusts the product to do the work.

colors:
  primary: "#003087"
  primary-active: "#001f5b"
  primary-disabled: "#a8c0e0"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#003087"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  promo-red: "#e31837"
  promo-red-surface: "#fdf0f2"
  star-rating: "#f5a623"
  success: "#2e7d32"
  error: "#c62828"
  link: "#003087"

typography:
  display-xl:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  label-uppercase:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  spec-value:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Gotham SSm', 'Gotham', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 10px 22px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  button-cta-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  text-input-error:
    border: "2px solid {colors.error}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-bar-secondary:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageBackground: "{colors.canvas}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-sm}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 2px 8px rgba(0,48,135,0.12)"
    rounded: "{rounded.sm}"
  hero-full-bleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    subheadTypography: "{typography.body-md}"
    imageRatio: "1/1"
    padding: "{spacing.section} 0"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    iconColor: "{colors.primary}"
  promo-badge:
    backgroundColor: "{colors.promo-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  sale-banner:
    backgroundColor: "{colors.promo-red-surface}"
    textColor: "{colors.promo-red}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.promo-red}"
    padding: "{spacing.sm} {spacing.base}"
  spec-comparison-row:
    backgroundColor: "{colors.canvas}"
    alternateBackground: "{colors.surface-soft}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-value}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  spec-table-header:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
  feature-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    iconColor: "{colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  star-rating-row:
    starColor: "{colors.star-rating}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 14px"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.primary}"
    padding: "6px 14px"
  model-search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    placeholder: "Enter model number"
    padding: "12px 16px"
    height: 52px
  service-cta-card:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    typography: "{typography.body-sm}"
    headlineTypography: "{typography.caption-bold}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — The primary action button runs in `{colors.primary}` (#003087 navy) with white text, 4px radius, and 48px height. It covers "Add to Cart," "Shop Now," and all hard-conversion actions. Hover state deepens to `{colors.primary-active}`; disabled fades to `{colors.primary-disabled}` with no opacity change on the label.

**`button-secondary`** — A white fill with a 2px navy border creates the outlined secondary button, used for "Compare," "View Details," and navigation escalations. On hover it takes a light `{colors.surface-soft}` fill. Same 48px height as primary to maintain visual parity in side-by-side CTA pairs.

**`button-cta-dark`** — Used specifically inside `hero-full-bleed` dark sections where the primary navy button would disappear against the navy surface. Same geometry as `button-primary` but anchored to `{colors.surface-dark}`, it reads as a local variant rather than a separate system tier.

**`button-text-link`** — Transparent background, navy text, underlined. Appears in spec rows, breadcrumb areas, and "Learn More" escalations in feature callouts. No height constraint — inline text flow.

### Inputs

**`text-input`** — Standard form field at 48px tall, 1px `{colors.hairline}` border, 4px radius. Focus ring promotes to 2px `{colors.primary}` navy — the only blue on white that signals interactivity. Error state replaces the border with `{colors.error}` red. Used for model-number lookup, zip-code-based dealer search, and checkout forms.

**`model-search-bar`** — A slightly taller (52px) variant of `text-input` with prominent placeholder copy "Enter model number." Common in support and registration flows; often paired with a navy `button-primary` CTA flush to the right edge to form a compound search unit.

### Navigation

**`nav-bar`** — 64px tall, white background, separated from content by a 1px `{colors.hairline}` bottom border. The Whirlpool wordmark in `{colors.primary}` navy anchors left. Category links (Washers, Dryers, etc.) sit center in `{typography.nav-link}` weight 500; utility links (Cart, Account, Search) dock right as icon-plus-label pairs.

**`nav-bar-secondary`** — A 44px secondary rail in `{colors.surface-soft}` gray sits below the primary nav on category and PDP pages, carrying breadcrumb navigation and "currently browsing" context. It collapses to hidden on mobile where breadcrumbs shift inline.

**`breadcrumb`** — Muted gray links with a `/` separator; the final node is `{colors.ink}` non-linked. Uses `{typography.caption}` to stay visually subordinate below the product headline.

### Product Cards

**`product-card`** — White card with 1px `{colors.hairline}` border and 4px radius. Product image sits on a pure white sub-surface (no gray box), creating the seamless appliance-on-white effect. Below the image: model name in `{typography.title-md}`, star rating row, and price in `{typography.price-sm}`. Hover promotes the border to `{colors.primary}` with a soft navy shadow.

**`promo-badge`** — A small `{colors.promo-red}` chip in `{typography.label-uppercase}` (11px, 700w, 1px tracking, all-caps). Values: "SALE," "REBATE," "LIMITED TIME." Appears as an absolute overlay on the product card image corner or inline beside the price. Red is strictly reserved for this badge — it never appears in navigation or non-promotional UI.

**`filter-chip`** / **`filter-chip-active`** — Pill-shaped filter tokens rendered in a horizontal scroll row above product grids. Inactive chips are white with `{colors.hairline}` borders; selected chips fill with `{colors.primary}` navy. Filters include finish (Stainless, White, Black), capacity, and feature set (smart appliance, steam, etc.).

### Hero Sections

**`hero-full-bleed`** — Full-width, navy `{colors.surface-dark}` background, minimum 480px tall. White headline at `{typography.display-xl}`, white body copy, then a white or `button-cta-dark` button. Lifestyle photography of appliances in use bleeds to the right edge on desktop; on mobile the image drops below the text block.

**`hero-split`** — White background, image left, text right (or reversed). Used for feature campaigns ("Steam Clean," "Smart Appliance"). Headline in `{typography.display-lg}` navy, body in `{typography.body-md}`. Avoids the dark surface, letting the appliance photography itself provide visual weight.

### Comparison & Specs

**`spec-comparison-row`** — Alternating white / `{colors.surface-soft}` rows carry spec-label / spec-value pairs for side-by-side model comparison. Labels in `{typography.spec-value}`, values in `{typography.body-sm}`. Sticky header row uses `{colors.primary}` fill with white model names in `{typography.title-sm}`.

**`feature-callout`** — A `{colors.surface-soft}` card with a `{colors.primary}` icon, bold headline in `{typography.title-md}`, and supporting copy in `{typography.body-sm}`. Appears in a 3- or 4-up grid on category and PDP pages, translating spec language ("1.4 cu. ft. capacity") into benefit language ("fits a king comforter").

### Promotions & Service

**`sale-banner`** — A light `{colors.promo-red-surface}` strip with a 3px top border in `{colors.promo-red}`. Used for site-wide promotions ("Save up to $500 this weekend"), seasonal rebate windows, and utility shutdowns. Full viewport width, text centered, `{typography.body-sm}` in red. Appears above the nav bar — the only element allowed to sit above the primary nav.

**`service-cta-card`** — A navy `{colors.primary}` card, white text, used in footer pre-rail and on-page service escalation zones. Carries repair scheduling, warranty registration, and parts lookup CTAs. The only card-shaped element that uses the primary navy fill rather than reserving it for buttons.

### Footer

**`footer`** — Dark `{colors.ink}` (#1a1a1a) background, off-white links in `{colors.hairline}`, section heads in `{typography.caption-bold}`. Four-column layout on desktop (Products, Support, Company, Social). Legal copy drops to `{typography.caption}` at bottom. The footer's dark surface provides the only page-level color contrast other than the hero; the body grid between them is entirely white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces category links; hero image stacks below text; spec comparison becomes single-model accordion; filter chips horizontally scrollable |
| Tablet | 744–1128px | Two-column product grid; nav collapses category links behind "Products" dropdown; hero runs split layout at reduced height (360px); comparison table supports 2 columns max |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all categories exposed; hero at full 480px; comparison supports 3–4 columns with sticky left label column |
| Wide | > 1440px | Max content width 1440px, centered with increased side padding; product grid moves to 4 columns; hero photography scales to fill without cropping |

### Touch Targets
- All primary and secondary buttons maintain 48px minimum height across all breakpoints
- Filter chips at `{spacing.sm}` vertical padding ensure 36px minimum touch height on mobile
- Nav icons (cart, account) are 44×44px touch target minimum on mobile nav bar
- Star rating rows include 8px vertical padding to prevent mis-taps on adjacent spec text
- Comparison "Add to Compare" checkbox zones are padded to 44px minimum height

### Collapsing Strategy
- Category mega-menu collapses to a hamburger-triggered drawer on mobile; categories become vertically stacked full-width taps
- Spec comparison table collapses to a single-model accordion on mobile; users switch between models via a dropdown rather than horizontal scroll
- Footer four-column layout stacks to a single accordion on mobile; each section head is a tap target that reveals links
- Secondary nav bar (breadcrumbs) hides on mobile; current location shown only as page `<h1>`
- Feature callout grid reduces from 4-up → 2-up → 1-up as viewport narrows
- Sale banner remains full-width at all breakpoints but reduces to 2 lines max with ellipsis truncation

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the live site returned "Access Denied" to the extractor. All colors above are based on Whirlpool's publicly visible brand materials and widely documented brand identity (navy primary, red promotional accent). The exact hex values (#003087, #e31837) should be verified against brand guidelines or the live site's CSS when accessible.
- **No font data extracted** — font-family stacks are based on brand knowledge; Whirlpool has historically used Gotham or Gotham SSm in marketing materials but the digital property may use a licensed variant or different geometric sans-serif. Verify via DevTools `/fonts` panel.
- **Exact button radius unconfirmed** — `{rounded.sm}` (4px) is an inference from the brand's utilitarian aesthetic. Could be `{rounded.none}` (0px) on some button variants; inspect rendered CSS to confirm.
- **Dark mode** — no evidence of a dark mode toggle; assumed absent but not confirmed.
- **Promotional color variants** — the `{colors.promo-red}` (#e31837) is an approximation of Whirlpool's sale-context red; confirm against actual CSS or brand swatch documentation.
- **Icon system** — Whirlpool uses product-category icons throughout navigation; their style (line vs. filled, stroke weight, sizing) could not be confirmed without site access.
- **Animation / transition tokens** — no motion data could be extracted; easing curves and durations are absent from this spec.
