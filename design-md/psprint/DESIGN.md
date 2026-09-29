---
version: alpha
name: "PsPrint"
source_url: "https://www.psprint.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Offset-press cyan owns PsPrint's interface the way it owns a four-color print run: #005875, the brand's primary, is unmistakably process-cyan shifted toward deep sea — it reads less like a tech-blue and more like a Pantone swatch mounted under warehouse fluorescents, the color of ink drums and proofing tables. Beside it, an amber-to-burnt-orange arc handles every conversion moment — #fabf01 ignites the sunniest highlight badges, #ee911a fills the main CTA buttons, and #b14f1e marks the hover-press, the gradient tracing the same warm arc a print job takes from proof to final pull. A surprise magenta accent (#cb2a88) surfaces in category chips and promotional callouts — a nod to CMYK's M channel, completing an implicit four-color brand palette. Type runs entirely on system stacks: Trebuchet MS at weight 700 for display headings, Arial for body copy and labels. This is a zero-flash, production-tool decision — the site serves working print buyers who want upload confirmations and quantity price breaks, not editorial delight. Surface hierarchy is handled through six shades of near-white: #ffffff canvas, #f5f5f5 and #ecf2f6 for sectional wells, #eeeeee for card backgrounds, #e1e2e3 and #e5e5e5 as structural hairlines. The only editorial color not derived from print process is the near-black ink (#2c2a29), a warm charcoal that avoids pure black's harshness on screen. Error states reach for #db2404 with a deeper #ad0000 for active. Corner radii stay deliberately small — {rounded.xs} on form fields, {rounded.sm} on cards — confirming a B2B-adjacent tool built for repeat buyers who return knowing exactly what they need.

colors:
  primary: "#005875"
  primary-dark: "#00626b"
  primary-disabled: "#7ab3c5"
  accent-yellow: "#fabf01"
  cta: "#ee911a"
  cta-hover: "#e5851e"
  cta-active: "#b14f1e"
  cta-light: "#f3aa10"
  magenta: "#cb2a88"
  ink: "#2c2a29"
  body: "#3c3c3c"
  muted: "#63666a"
  muted-soft: "#6f6f6f"
  hairline: "#e1e2e3"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#eeeeee"
  surface-tinted: "#ecf2f6"
  surface-light-blue: "#edf6fc"
  on-primary: "#ffffff"
  on-cta: "#ffffff"
  on-accent: "#2c2a29"
  error: "#db2404"
  error-dark: "#ad0000"
  highlight-cream: "#fefde7"
  highlight-yellow: "#ded877"
  dark-ui: "#575757"

typography:
  display-xl:
    fontFamily: "'Trebuchet MS', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Trebuchet MS', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Trebuchet MS', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Trebuchet MS', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Trebuchet MS', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.2px
  label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Trebuchet MS', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Trebuchet MS', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  price-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hover:
      backgroundColor: "{colors.primary-dark}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 44px
  button-cta:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
    hover:
      backgroundColor: "{colors.cta-hover}"
    active:
      backgroundColor: "{colors.cta-active}"
  button-cta-lg:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 16px 40px
    height: 52px
    hover:
      backgroundColor: "{colors.cta-hover}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
    hover:
      backgroundColor: "{colors.surface-tinted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 42px
    focus:
      borderColor: "{colors.primary}"
      outlineColor: "{colors.surface-tinted}"
    error:
      borderColor: "{colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
    hoverColor: "{colors.cta}"
    logoColor: "{colors.primary}"
  subnav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    shadow: "0 4px 12px rgba(0,0,0,0.12)"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
  product-card:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.muted}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.primary}"
    hover:
      borderColor: "{colors.primary}"
      shadow: "0 2px 8px rgba(0,88,117,0.15)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.accent-yellow}"
    ctaComponent: button-cta-lg
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 400px
  promo-strip:
    backgroundColor: "{colors.cta}"
    textColor: "{colors.on-cta}"
    typography: "{typography.button-sm}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
    accentColor: "{colors.accent-yellow}"
  promo-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  promo-badge-magenta:
    backgroundColor: "{colors.magenta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-chip:
    backgroundColor: "{colors.surface-tinted}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 1px
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    active:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  price-display:
    textColor: "{colors.primary}"
    typography: "{typography.price-display}"
    unitColor: "{colors.muted}"
    unitTypography: "{typography.body-sm}"
  price-break-table:
    backgroundColor: "{colors.surface-soft}"
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.label}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.ink}"
    highlightRowColor: "{colors.highlight-cream}"
    rounded: "{rounded.xs}"
    borderColor: "{colors.hairline}"
  upload-zone:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.muted-soft}"
    borderStyle: dashed
    borderWidth: 2px
    rounded: "{rounded.sm}"
    padding: "{spacing.xxl}"
    textColor: "{colors.muted}"
    typography: "{typography.body-md}"
    labelTypography: "{typography.caption}"
    activeColor: "{colors.primary}"
    activeBorderColor: "{colors.primary}"
    activeBackgroundColor: "{colors.surface-tinted}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 42px
    buttonColor: "{colors.surface-card}"
    buttonHoverColor: "{colors.surface-tinted}"
  guarantee-badge:
    backgroundColor: "{colors.surface-light-blue}"
    borderColor: "{colors.primary}"
    borderWidth: 1px
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.primary}"
    padding: "{spacing.sm} {spacing.md}"
  alert-error:
    backgroundColor: "#fff0ee"
    borderColor: "{colors.error}"
    borderWidth: 1px
    textColor: "{colors.error-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline-soft}"
    linkHoverColor: "{colors.accent-yellow}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label}"
    headingColor: "{colors.accent-yellow}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — Teal (#005875) fill with white text and 4px radius, 44px tall. The primary action button appears in configurators and account flows where the orange CTA would create visual competition. On hover, deepens to #00626b; disabled state fades to #7ab3c5 and removes pointer events.

**`button-cta`** — The amber-orange (#ee911a) button is PsPrint's loudest conversion lever, reserved for "Order Now," "Get a Quote," and checkout progression. Hover shifts to #e5851e, active press reaches #b14f1e — all values extracted from the site's gradient arc. The large variant (`button-cta-lg`) at 52px tall appears in hero sections.

**`button-secondary`** — White canvas with a 2px teal border and teal text, giving parity weight to secondary actions like "Learn More" or "Save for Later" without competing with the orange CTA. On hover, fills with `{colors.surface-tinted}`.

**`button-ghost`** — Transparent background with `{colors.ink}` text for tertiary actions in dense UI zones like product configurators or breadcrumb flows.

### Form Inputs

**`text-input`** — White field, 1px `{colors.hairline}` border, 42px tall with `{rounded.xs}`. Focus ring shifts border to `{colors.primary}` with a `{colors.surface-tinted}` outer glow. Error state swaps border to `{colors.error}`. Labels sit above the field in `{typography.label}` style.

### Navigation

**`nav-bar`** — White bar, 64px tall, with a 1px `{colors.hairline}` bottom rule. Logo renders in `{colors.primary}` teal. Navigation links in `{typography.nav-link}` (Trebuchet MS 14px bold) color to `{colors.cta}` on hover, signaling the brand's orange-as-engagement system. A `{colors.cta}` promotional strip (`promo-strip`) runs above the nav for site-wide offers.

**`subnav-dropdown`** — White panel anchored below the nav with a 3px `{colors.primary}` top accent, no radius, and a soft shadow. Product category columns use `{typography.body-sm}` with `{colors.muted}` section headings.

### Product Cards

**`product-card`** — White background, 1px `{colors.hairline}` border, `{rounded.sm}`, with `{typography.title-sm}` product name in `{colors.ink}` and `{typography.price-sm}` starting price in `{colors.primary}`. Hover state lifts border to teal and adds a gentle teal-tinted shadow, making the card feel selectable without aggressive lift effects. Promo badges (`promo-badge`) pin to the card corner in amber or magenta depending on offer type.

### Hero

**`hero-banner`** — Deep teal (#005875) fill, 400px minimum height, `{typography.display-xl}` headline in white, `{typography.body-md}` subhead in white at reduced opacity. `{colors.accent-yellow}` decorative elements or highlights thread through the copy. The CTA always uses `button-cta-lg`. Background may accept a product image with a teal color overlay.

**`promo-strip`** — 36px orange (#ee911a) strip above the nav, `{typography.button-sm}` in white. `{colors.accent-yellow}` inline highlights (bold text spans) pick out discount figures or expiry countdowns.

### Badges and Tags

**`promo-badge`** — Amber (#fabf01) pill with `{colors.on-accent}` (dark) label text, `{typography.label}` uppercase at 11px. Used for "SALE," "POPULAR," "BESTSELLER" overlays on product cards.

**`promo-badge-magenta`** — Magenta (#cb2a88) version of the same geometry, reserved for "NEW" or limited-offer labels. The magenta reads as a print-CMYK M-channel nod, distinct enough to signal novelty without red-alert urgency.

**`category-chip`** — `{colors.surface-tinted}` background with `{colors.primary}` border and text, `{rounded.full}` pill shape, `{typography.caption}` size. Active state inverts to solid teal fill with white text. Used in product category filter bars and faceted navigation.

### Pricing

**`price-display`** — `{typography.price-display}` (Trebuchet MS 24px 700) in `{colors.primary}`, with a `{typography.body-sm}` unit label in `{colors.muted}`. Starting-price copy ("from $X.XX") sits beneath the product title on listing pages.

**`price-break-table`** — Quantity/price matrix with a solid teal header row (`{colors.primary}` bg, `{colors.on-primary}` text, `{typography.label}`), alternating white and `{colors.surface-soft}` rows. The "best value" row highlights in `{colors.highlight-cream}`. Rounded at `{rounded.xs}` with hairline column rules.

### Upload and Order Tools

**`upload-zone`** — `{colors.surface-soft}` fill with a 2px dashed `{colors.muted-soft}` border and `{rounded.sm}`. On drag-enter, border and fill shift to `{colors.primary}` and `{colors.surface-tinted}` respectively. Label copy uses `{typography.body-md}` in `{colors.muted}` with a cloud-upload icon.

**`quantity-selector`** — Stepper input at 42px tall, white fill with hairline border. Decrement/increment buttons use `{colors.surface-card}` fill that lifts to `{colors.surface-tinted}` on hover. Value display in `{typography.body-md}`.

### Trust Elements

**`guarantee-badge`** — `{colors.surface-light-blue}` fill, 1px `{colors.primary}` border, teal icon (checkmark or shield), `{typography.caption}` copy in `{colors.primary}`. Used inline in cart and product pages for "100% Satisfaction Guarantee" and "Free Proofs" claims.

**`alert-error`** — Soft pink-red well (#fff0ee background) with 1px `{colors.error}` border and `{colors.error-dark}` text. Appears on form validation and file-upload failure states.

### Footer

**`footer`** — Dark charcoal (#2c2a29) fill, 4px `{colors.primary}` top accent rule. Link columns use `{typography.label}` section heads in `{colors.accent-yellow}`, body links in `{colors.hairline-soft}` that brighten to `{colors.accent-yellow}` on hover. Social icons render in white, inverting to teal on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Hamburger nav replaces full menu; promo-strip collapses to single scrolling line; product grid goes single-column; hero stacks to text-over-image; price-break-table scrolls horizontally; upload-zone reduces to 120px tall; quantity-selector goes full-width |
| Tablet | 744–1128px | Nav shows top-level categories, dropdowns on tap; product grid switches to 2-column; hero splits 60/40 text-image; price-break-table fits 4 quantity tiers before scroll |
| Desktop | 1128–1440px | Full dropdown nav with mega-menu panels; product grid 3–4 columns; hero full-bleed with contained max-width text block; price-break-table shows all tiers inline |
| Wide | > 1440px | Max-width container (~1400px) centered on white canvas; hero background tiles or extends with gradient; nav and footer remain full-bleed |

### Touch Targets

- All buttons minimum 44×44px per WCAG 2.1 AA
- Category chips minimum 36px tall with 8px horizontal gap between chips
- Quantity stepper buttons minimum 44px wide
- Nav hamburger icon 44×44px tap region
- Upload-zone tap area full card, not icon-only

### Collapsing Strategy

- Mega-menu dropdown collapses to accordion drawer on mobile, triggered by hamburger
- Promo-strip text truncates with ellipsis below 400px viewport, showing only the primary offer
- Price-break-table gains horizontal scroll at tablet and below; pinned first column (quantity) for reference
- Product configurator steps stack vertically on mobile, collapsing the sidebar summary into a sticky bottom drawer
- Footer column grid collapses from 4-col to 2-col at tablet, single-col at mobile with expandable accordion sections
- Hero CTA button goes full-width on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font detected; Trebuchet MS and Arial are system-font fallbacks — PsPrint may load a web font via JavaScript that was not captured in static extraction; verify at runtime
- `primary-disabled` color (#7ab3c5) is an extrapolation from the primary teal, not a directly extracted value
- Hover/focus states for nav links inferred from the orange CTA spectrum — exact hover hex not confirmed via interaction
- Shadow values (box-shadow depth, blur radius) not extractable from static analysis; estimates used in product-card and subnav-dropdown
- Icon system (SVG set, icon library name) not identifiable from extracted data
- Form field label positioning (above vs. floating) not confirmed; above-field assumed from industry norm
- Animation/transition timing curves not captured
- Dark mode or high-contrast theme presence not confirmed
- Exact max-width breakpoint for the desktop content container not extracted (1400px estimated)
- The `highlight-yellow` (#ded877) and `highlight-cream` (#fefde7) tokens appear in the extraction but their precise UI role (text highlight, row emphasis, tooltip background) could not be confirmed from static data
