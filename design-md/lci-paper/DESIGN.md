---
version: alpha
name: "LCI Paper"
source_url: "https://www.lcipaper.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The weight of paper stock — the gap between 80 lb text and 130 lb cover — is the invisible axis around which LCI Paper organizes its entire catalog. Every product page reads as a material study: metallics with a mirror-bright surface, cotton rags with a felt-side texture, linen covers with a woven-grid embossing. The single confirmed extracted color, #313131, operates exactly as heavy ink pressed onto uncoated stock — flat, dense, and paper-forward — so no vivid accent competes with the substrates on display. Sharp square corners (`{rounded.none}`) on product cards and form fields reinforce the rectilinear logic of a printed grid; there are no soft pill radii that would read as consumer-casual. Typography runs on system fonts, a utilitarian architecture that steps back so substrate names, paper weights, and sheet counts carry the communicative load. Primary buttons inherit #313131 on white `{colors.on-primary}`, a press-run monochrome with no gradient or color flourish. The canvas reads as clean white or a faint warm cream `{colors.surface-soft}` (#f8f5f1) that suggests a quality paper sample card rather than a clinical tech surface. Navigation likely exposes material categories — Cotton, Metallic, Textured, Translucent, Recycled — at the top level, mirroring the sample-book taxonomy a print studio would use. Product cards are spec-forward: material name, sheet size, weight (gsm/lb), finish, and price form the visual hierarchy, not aspirational lifestyle photography. The brand operates in the professional-prosumer corridor — letterpress studios, wedding invitation designers, packaging shops — where the interface must communicate material expertise and catalog efficiency above any other ambition. With only one reliably extracted hex value and no confirmed custom typeface, portions of this palette are inferred from category norms and declared in Known Gaps.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#9e9e9e"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#7a7a7a"
  hairline: "#e0dbd5"
  canvas: "#ffffff"
  surface-soft: "#f8f5f1"
  surface-card: "#ffffff"
  surface-cream: "#f2ede7"
  on-primary: "#ffffff"
  warm-neutral: "#c4bdb4"
  link: "#313131"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  label-uppercase:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  material-spec:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 42px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    columnGap: "{spacing.xl}"
    padding: "{spacing.lg} {spacing.xxl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.title-sm}"
    specTypography: "{typography.material-spec}"
    priceTypography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    imageAspect: "1/1"
    padding: "{spacing.md}"
    hoverBorderColor: "{colors.ink}"
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  weight-tag:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.body}"
    typography: "{typography.material-spec}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  paper-swatch:
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    size: 48px
    shadow: "0 1px 3px rgba(49,49,49,0.12)"
  hero:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
  category-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separator: "/"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 42px
    iconColor: "{colors.muted}"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
    activeBgColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 40px
  spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-uppercase}"
    labelColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    rowPadding: "{spacing.sm} {spacing.md}"
  section-header:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    borderBottom: "2px solid {colors.primary}"
    paddingBottom: "{spacing.sm}"
    marginBottom: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.warm-neutral}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    padding: "{spacing.xxl} {spacing.xxl}"

## Components

### Buttons

**`button-primary`** — A solid #313131 charcoal block, white text, zero corner radius — the visual equivalent of a clean ink impression on white stock. On hover the fill deepens to `{colors.primary-active}` (#1a1a1a); the disabled state uses `{colors.primary-disabled}` at reduced opacity without introducing a secondary hue. Height is fixed at 44px for consistent catalog-page call-to-action rows.

**`button-secondary`** — White fill with a 1px `{colors.primary}` border and charcoal text. The outline echoes a die-cut or deboss border rather than a color accent, maintaining strict monochromatic discipline. On hover, the border weight can thicken to 2px without color change to signal interactivity.

**`button-ghost`** — Transparent background, `{colors.ink}` text in `{typography.button-sm}` with 0.5px letter-spacing. Used for inline actions like "View all sizes", "See more colors", or secondary nav links. No border, no fill — disappears into the page until activated.

### Inputs

**`text-input`** — Square-cornered (`{rounded.none}`), `{colors.hairline}` border at rest, `{colors.primary}` border on focus. The field reads as a data-entry form aligned to a printed order slip. Placeholder text in `{colors.muted}`. No border-radius softening at any state.

**`search-bar`** — Identical geometry to `text-input` with a `{colors.muted}` magnifying-glass icon inset left. On focus the border upgrades to `{colors.primary}`. Typically paired with a `filter-pill` row immediately below for faceted paper filtering by weight, finish, color, and sheet size.

### Navigation

**`nav-bar`** — 64px tall, `{colors.canvas}` background, bottom 1px `{colors.hairline}` border. Left: wordmark or logo lockup. Center: flat category triggers typeset in `{typography.nav-link}` — Cotton, Metallic, Textured, Envelopes, Accessories. Right: search icon, account icon, cart with item badge. The hairline border maintains scroll-position legibility without a sticky shadow.

**`mega-menu`** — Full-width panel below the nav bar, white fill, top hairline. Four to five columns of category links in `{typography.body-sm}` with `{typography.label-uppercase}` column headers in `{colors.muted}`. The rightmost column may feature a paper stock image or curated product tile.

**`breadcrumb`** — Ancestor nodes in `{colors.muted}`, active node in `{colors.ink}`, "/" as separator. Typeset in `{typography.body-sm}`. Appears on all product detail and subcategory pages to surface catalog depth at a glance.

### Product Display

**`product-card`** — Square image tile, 1px `{colors.hairline}` border on all sides, `{rounded.none}`. Below the image: material name in `{typography.title-sm}`, weight and finish in `{typography.material-spec}` / `{colors.muted}`, price in `{typography.title-sm}`. On hover the border upgrades to 1px `{colors.ink}` for emphasis without fill change or elevation.

**`paper-swatch`** — 48×48px flat square tiles showing the actual paper color or texture; `{rounded.none}`, 1px `{colors.hairline}` border, and a subtle `0 1px 3px rgba(49,49,49,0.12)` shadow that lifts the swatch off the white canvas to suggest physical depth. Used in PDP color-selector rows; at least 6–12 swatches may appear per product.

**`material-badge`** — Small zero-radius tag, `{colors.surface-soft}` fill, `{typography.label-uppercase}` text in `{colors.muted}`. Labels substrate category: "COTTON", "METALLIC", "RECYCLED", "TRANSLUCENT". Appears on product cards and in filter controls.

**`weight-tag`** — `{colors.surface-cream}` background, `{colors.body}` text in `{typography.material-spec}`. Used inline beside material badges to display print-trade shorthand: "80 lb Text", "120 lb Cover", "300 gsm". Pairs with `material-badge` in a single-row chip cluster.

**`spec-table`** — Two-column table on product detail pages. Left column: attribute label in `{typography.label-uppercase}` / `{colors.muted}`. Right column: value in `{typography.body-sm}` / `{colors.body}`. Rows separated by 1px `{colors.hairline}`. Covers Size, Weight, Brightness, Finish, Opacity, Acid-Free status, and compatibility notes.

### Layout

**`hero`** — `{colors.surface-cream}` (#f2ede7) background section, headline in `{typography.display-xl}`, supporting copy in `{typography.body-md}`. Paired with a product photography float or a fanned paper-stack image. Full-bleed width on desktop, vertically stacked on mobile.

**`category-card`** — Used on homepage or landing pages to present paper families. `{colors.surface-soft}` background, full-bleed image on top, category name in `{typography.title-md}` below. Hover state adds 1px `{colors.primary}` border. Grid of 3–4 cards on desktop.

**`section-header`** — Catalog section dividers: heading in `{typography.display-md}`, underlined by a 2px `{colors.primary}` bottom border. Creates visual rhythm in dense grid layouts and mirrors the ruled-line convention of a printed order form or sample catalog.

**`filter-pill`** — Rounded `{rounded.full}` toggle chips for faceted browsing. Inactive: `{colors.surface-soft}` fill, `{colors.body}` text. Active: `{colors.primary}` fill, `{colors.on-primary}` text. The only `{rounded.full}` element in an otherwise square-cornered system — a deliberate soft counterpoint reserved exclusively for interactive filter state.

### Checkout & Cart

**`quantity-selector`** — Square stepper (−/+) flanking a numeric input, sharing a 1px `{colors.hairline}` border with `{rounded.none}` geometry throughout. Height 40px. Text in `{typography.body-md}`. Stepper buttons must meet 44×44px touch targets on mobile.

### Footer

**`footer`** — Full-width `{colors.ink}` (#313131) background, `{colors.on-primary}` body text, `{colors.warm-neutral}` links. Column headers in `{typography.label-uppercase}`, body links in `{typography.body-sm}`. The charcoal footer grounds the page the same way a heavy impression anchors a printed sheet — a deliberate visual terminus.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger nav replaces mega-menu; product grid collapses to 2 columns; hero stacks vertically (image above copy); filter pills scroll horizontally in a single row; spec-table goes full width; breadcrumb truncates to last 2 ancestors |
| Tablet | 744–1128px | 3-column product grid; mega-menu appears as full-width dropdown with 2 columns; hero switches to side-by-side layout; filter pill row wraps up to 2 lines |
| Desktop | 1128–1440px | 4-column product grid; full mega-menu with 4–5 columns; hero full-bleed with text beside or overlaid on image; breadcrumb and filter row fully visible |
| Wide | > 1440px | Content constrained to ~1380px max-width, centered; product grid extends to 5 columns; hero image can bleed full viewport width behind a contained text column |

### Touch Targets
- All buttons minimum 44px height and 44px tap width
- Quantity stepper −/+ buttons minimum 44×44px even if visually smaller
- Nav menu triggers minimum 44px height on mobile
- Paper swatches scale to at least 44×44px in mobile PDP context (up from 48px desktop default, which already meets threshold)
- Filter pills minimum 36px height with generous horizontal padding for comfortable one-thumb filtering
- Breadcrumb links minimum 32px height; acceptable below 44px given supplementary-navigation role

### Collapsing Strategy
- Primary navigation collapses to hamburger at < 744px; mega-menu becomes a slide-in drawer with accordion category sections
- Hero stacks vertically (image above copy) on mobile; side-by-side or overlay layout at tablet+
- Spec-table remains full-width at all breakpoints; font size may step down by 1px on mobile
- Filter row becomes a single horizontally scrollable row of pills on mobile rather than a multi-row grid
- Product grid: 2 columns (mobile) → 3 columns (tablet) → 4 columns (desktop) → 5 columns (wide)
- Footer collapses from 4-column grid to single-column accordion on mobile; background color and typography unchanged

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Severely limited extraction**: The site returned a Cloudflare "Just a moment..." anti-bot challenge page; only one hex value (#313131) was captured and no custom typeface was detectable
- **No confirmed accent or CTA color**: Whether LCI Paper uses any secondary brand color (a warm ochre, sage, or rust accent on CTAs or promotional banners) is unknown; primary and ink tokens are both set to #313131 as the sole extracted value
- **No confirmed custom typeface**: Only OS system fonts appeared in the font-stack scan; LCI Paper may use a licensed or hosted font (serif or geometric sans-serif) not visible via CSS meta-scan under anti-bot conditions
- **No confirmed border-radius values**: The `{rounded.none}` default is inferred from the specialty-paper catalog aesthetic; the live site may use light rounding on some interactive elements
- **No dark mode or seasonal palette confirmed**: Whether alternate surface themes, promotional color overlays, or holiday color variants exist is unknown
- **No motion or animation tokens captured**: Transition durations, easing curves, and hover animation behavior are assumed from e-commerce category norms
- **No logo or wordmark geometry confirmed**: Letterform style, horizontal versus stacked lockup availability, and minimum-size rules are unverified
- **Price and sale-badge colors unknown**: Whether LCI Paper uses a red or contrasting accent for sale pricing, clearance badges, or promotional callouts could not be determined
