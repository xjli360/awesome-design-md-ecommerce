---
version: alpha
name: "Formaspace"
source_url: "https://www.formaspace.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Steel-gauge authenticity is the opening move — Formaspace's navigation renders under a near-black charcoal (#313131) that reads less like a website header and more like the cross-section of a workbench edge, structural material before the surface begins. The brand sells configurable industrial furniture for aerospace assembly lines, university chemistry labs, warehouse operations, and electronics manufacturing, and the design logic mirrors the product: modular, specification-first, optimized for configuration flows rather than impulse browsing. Typography runs on a pure system-UI stack with no licensed typeface, which signals a B2B audience that expects clarity over brand personality and treats technical spec sheets as the actual content rather than aspirational photography. The presumed primary accent is an orange-amber near #e87722, the one warm voltage the brand uses to separate CTA buttons, quote-request forms, and configurator "Add to Quote" actions from the surrounding charcoal-and-white grid; in the workbench category, orange carries industrial warning-label authority rather than consumer warmth. Corners land at a modest `{rounded.sm}` — 8px on cards, 4px on buttons — avoiding both the harshness of zero-radius enterprise design and the friendliness of pill shapes, landing precisely where a tool catalog belongs: professional, dimensional, unhurried. Section spacing is generous on desktop, using `{spacing.section}` and `{spacing.xxl}` rhythm to let full-bleed product photography of large-format benches breathe without crowding specification details. The overall palette is intentionally restrained — charcoal plus orange on white, with mid-gray body text and light-gray hairlines separating configuration panels — because buyers reading load ratings and surface materials do not need visual interference between themselves and the specification.

colors:
  primary: "#e87722"
  primary-active: "#c55e10"
  primary-disabled: "#f4bb90"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#767676"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#313131"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#e87722"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.38
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
    padding: "{spacing.sm} 0"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    imageAspectRatio: "4/3"
    boxShadow: none
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaStyle: button-primary
    minHeight: 480px
    imageOverlay: "rgba(49,49,49,0.55)"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  quote-request-form:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.title-md}"
    inputStyle: text-input
    ctaStyle: button-primary
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    sectionDivider: "1px solid {colors.hairline-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-md}"
    addToQuoteButton: button-primary
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.spec-label}"
    rowPadding: "{spacing.sm} {spacing.base}"
    rounded: "{rounded.xs}"
  industry-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  category-tile:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    titleTypography: "{typography.display-sm}"
    overlayGradient: "linear-gradient(to top, rgba(49,49,49,0.85) 0%, transparent 60%)"
    imageAspectRatio: "16/9"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  alert-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Orange-amber (#e87722) fill at `{rounded.xs}` (4px radius), 44px tall, 15px/600 weight system-UI text with 0.3px letter-spacing that sharpens the label against an industrial palette. Hover shifts to `{colors.primary-active}` (#c55e10), a deeper burnt-orange; disabled state washes to `{colors.primary-disabled}` (light peach), removing CTA authority without hiding the element entirely. This button carries all quote-request submissions, configurator "Add to Quote" actions, and primary landing-page CTAs — orange is the sole action signal in the system.

**`button-secondary`** — White fill with a 1px solid `{colors.ink}` border at `{rounded.xs}`. Used for "Download Spec Sheet," "Contact Sales," and comparison-flow secondary actions. The charcoal outline on white reads as technical documentation UI — matching the product's precision character — rather than a generic ghost pattern.

**`button-ghost`** — Transparent background with `{colors.primary}` orange border and text. Appears in inline "Learn More" links within configurator panels and category pages where orange reinforcement is needed without the visual weight of a filled button.

**`button-dark`** — Charcoal (#313131) fill with white text at `{rounded.xs}`, used on hero sections and dark-background panels where the orange primary would lose contrast against surrounding photography.

### Navigation

**`nav-bar`** — 64px dark-charcoal (#313131) horizontal bar with white `{typography.nav-link}` links at weight 500. The dark top rail is the brand's most immediate visual signature: visitors understand immediately they are in a professional specification environment, not a consumer retail site. Dropdowns (`nav-dropdown`) open on white card backgrounds with `{rounded.xs}` and 1px hairline borders, creating strong contrast against the dark parent bar. No underline or active-state decoration on nav links beyond hover color shift to `{colors.primary}`.

### Product Cards

**`product-card`** — White card at `{rounded.sm}` with 1px `{colors.hairline}` border and `{spacing.base}` internal padding, no elevation shadow. Images occupy a 4:3 aspect ratio to consistently frame full workbench photography across catalog grids. Title at `{typography.title-sm}` (weight 600), body text at `{typography.body-sm}`. The hairline border — not a shadow — separates products without implying floating or depth, consistent with the flat, specification-forward aesthetic.

### Hero Banner

**`hero-banner`** — Full-width section with a 55% charcoal overlay (`rgba(49,49,49,0.55)`) over large-format product photography. White headline at `{typography.display-xl}` (40px/700), supporting copy at `{typography.body-md}`, and an orange `button-primary` CTA. Minimum height 480px on desktop to give workbench photography adequate room. The dark overlay and dark nav bar create a seamless charcoal band across the top of the page — a visual anchor that frames every hero entry point.

### Configurator Panel

**`configurator-panel`** — The core B2B interaction surface. White canvas with 1px `{colors.hairline}` border, `{rounded.sm}` corners, and `{spacing.xl}` internal padding so dense option sets do not crowd. Configuration options (surface material, leg type, load rating, width, depth) are organized under uppercase spec labels at `{typography.spec-label}` (13px/700/0.4px tracking). Section dividers are `{colors.hairline-soft}` 1px rules. The "Add to Quote" action uses a full-width `button-primary` at the panel base. On desktop, the configurator is a persistent right-rail panel beside a product viewer; it is the commercial engine of every product detail page.

### Quote Request Form

**`quote-request-form`** — Light-gray `{colors.surface-soft}` background distinguishes the form from surrounding white canvas. `{spacing.xl}` internal padding, `{rounded.sm}` corners. Text inputs follow the standard `text-input` token with `{rounded.xs}` and 1px `{colors.hairline}` borders. Title at `{typography.title-md}` (18px/600). Submission CTA is full-width `button-primary`. Used in sidebar panels, modal overlays, and dedicated "Request a Quote" landing pages.

### Spec Table

**`spec-table`** — Two-column table with a `{colors.surface-soft}` header row, 1px `{colors.hairline}` borders on all cells, and alternating white rows. Labels render in `{typography.spec-label}` (uppercase/700/0.4px tracking), values in `{typography.body-sm}`. Row padding is `{spacing.sm}` vertical by `{spacing.base}` horizontal. This component is the primary content surface of product detail pages — presenting load ratings, surface materials, dimensions, and certifications that buyers evaluate before initiating a quote.

### Category Tiles

**`category-tile`** — Wide-format image tiles at 16:9 aspect ratio with a bottom-anchored dark gradient overlay. White title at `{typography.display-sm}` (22px/600) anchors to the lower third. `{rounded.sm}` corners. Used on category browse pages to navigate between workbench families, lab furniture, storage systems, and accessory lines. Three tiles per row on desktop, descending to two and then one at smaller breakpoints.

### Industry Badges

**`industry-badge`** — Pill-shaped (`{rounded.full}`) chips at `{typography.label-sm}` (11px/600/uppercase/0.5px tracking), `{colors.surface-soft}` background, 1px `{colors.hairline}` border. Tags products by vertical — Aerospace, Pharmaceutical, Electronics Assembly, Food Service — and populates filter sidebars as well as product-detail "Designed For" sections. The pill shape is the only `{rounded.full}` element in the system, distinguishing taxonomy tags from all rectangular action and input elements.

### Alert Banner

**`alert-banner`** — Full-width orange (#e87722) strip at `{typography.body-sm}` weight, `{spacing.sm}` vertical padding. Used for site-wide promotions, lead-time notices, and trade-show announcements. Orange fill makes this the highest-attention non-modal element on the page; use sparingly so it retains signal value.

### Footer

**`footer`** — Dark charcoal (`{colors.surface-dark}`) full-width band with a 3px `{colors.primary}` orange top border — the brand's single decorative flourish, tying the footer visually back to the CTA color and closing the page composition symmetrically with the dark nav rail. Column headings at `{typography.label-sm}` (uppercase/600); link text at `{typography.body-sm}` in `{colors.hairline}` for legibility on dark. `{spacing.xxl}` top and bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger menu replaces nav rail; hero headline drops to `display-md` (28px); configurator panel stacks full-width below product image; spec table horizontally scrollable within clipped container |
| Tablet | 744–1128px | Two-column product grid; nav retains logo plus condensed links or hamburger depending on link count; hero min-height 360px; configurator panel occupies right 42% beside product image |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with dropdown megamenus; hero 480px min-height; configurator is persistent 360px right rail beside full-width product viewer |
| Wide | > 1440px | Content max-width ~1360px centered on white canvas; hero image extends full bleed; product grid remains 3-column with wider gutters using `{spacing.xl}` between cards |

### Touch Targets
- All primary and secondary buttons: minimum 44px height
- Nav links and dropdown rows: minimum 44px tap height via vertical padding
- Product cards: full-card tap surface on mobile, not just the title link
- Industry badge filter chips: minimum 36px height on mobile via increased vertical padding
- Configurator option rows: minimum 48px tap height on mobile
- Text inputs: minimum 44px height (already defined at 44px)

### Collapsing Strategy
- Desktop 3-column product grid → 2-column at tablet → 1-column at mobile
- Horizontal nav → hamburger icon at ≤ 1024px; drawer slides from left with charcoal overlay behind
- Configurator panel stacks below product image on mobile; "Add to Quote" button becomes sticky bottom bar at < 744px with white shadow separator
- Spec table scrolls horizontally within overflow container; columns do not drop or reorder
- Category tiles: 3-across desktop → 2-across tablet → 1-across mobile with reduced 56vw height
- Hero copy: `display-xl` 40px → `display-md` 28px at mobile; CTA button full-width at < 744px
- Footer columns: 4-column grid on desktop → 2-column at tablet → single stacked column at mobile; orange top border persists at all widths

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Critical color gap**: Only one hex value (#313131) was extracted from the live site. Cloudflare anti-bot middleware returned a "Just a moment…" challenge page, blocking all CSS token extraction. Every color except `{colors.ink}` (#313131) is inferred from Formaspace's observable brand identity and must be verified against live DevTools.
- **Primary accent unverified**: `{colors.primary}` (#e87722) is inferred from Formaspace's product imagery and marketing usage of orange-amber; the exact hex should be sampled from the live logo or CTA button via browser color picker.
- **No custom typeface detected**: The extracted font stack is the OS system-UI cascade with no proprietary typeface. If Formaspace uses a licensed font (e.g., via Adobe Fonts or self-hosted WOFF2), it did not surface in extraction — recommend auditing `@font-face` declarations on the live site.
- **Logo mark colors**: The exact logo orange and any secondary wordmark colors were not extractable from the blocked page.
- **Configurator specifics**: The product configurator is a complex interactive component; option layouts, pricing display format, validation states, and multi-step flow structure are unverified.
- **Interaction tokens**: Hover transition durations, focus ring styles, skeleton loader patterns, and configurator loading states could not be observed.
- **Meta theme-color**: No `<meta name="theme-color">` present; mobile browser chrome color is undefined.
- **Secondary palette**: Whether Formaspace uses any additional accent beyond orange (e.g., a blue for links or a green for availability indicators) could not be confirmed from extraction alone.
