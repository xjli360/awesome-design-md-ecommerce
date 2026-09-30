---
version: alpha
name: "BlueStar"
source_url: "https://www.bluestarcooking.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep royal blue (#003388) saturates the header bar, CTAs, and navigation anchors the way enamel coats cast iron — thick, opaque, unapologetic. BlueStar's digital presence borrows confidence from its product line: professional-grade burners that ship in 750+ custom colors, so the site itself runs a restrained two-hue system of that signature cobalt against a warm antique-gold accent (#e2af38) reserved for promotional callouts, hover states, and "Build Your Own" configuration highlights. Trade Gothic — a mid-century grotesque with squared terminals and narrow proportions — sets every headline and navigation label in weights that read like stamped steel nameplates, while Open Sans softens body copy into comfortable reading at 16px/1.6. The layout grid is wide and confident: hero photography bleeds edge-to-edge at 1440px+, product cards stack on a rigid 3-up desktop grid with `{rounded.xs}` corners that stay nearly flush, and generous `{spacing.section}` vertical rhythm keeps each product family (Platinum, Residential, RNB series) visually quarantined. Buttons are squared-off rectangles (`{rounded.xs}`) with uppercase Trade Gothic labels — no pills, no softness, just machined edges that echo brushed-stainless control knobs. The dark navy tone (#172a54) appears in footers and overlay panels, creating depth without resorting to pure black, while a constellation of utility grays (#949494 for muted labels, #f0f0f0 and #f5f5f5 for alternating section bands) keeps the chrome-and-steel metaphor intact. Gold (#e2af38) punctuates sparingly: award badges, "?"  icons on the range configurator, and the occasional promotional banner — it functions as a maker's mark rather than a call to action.

colors:
  primary: "#003388"
  primary-active: "#002266"
  primary-disabled: "#6688bb"
  accent-gold: "#e2af38"
  accent-gold-active: "#c89a2e"
  navy-deep: "#172a54"
  ink: "#1e1f26"
  body: "#32373c"
  muted: "#949494"
  muted-soft: "#444444"
  hairline: "#eeeeee"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-alt: "#f0f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-gold: "#1e1f26"
  success: "#00d084"
  info: "#0693e3"
  warning: "#ff9900"
  error: "#ea4434"

typography:
  display-xl:
    fontFamily: "'Trade Gothic', 'Trade-Gothic', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Trade Gothic', 'Trade-Gothic', Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.25px
    textTransform: uppercase
  display-md:
    fontFamily: "'Trade Gothic', 'Trade-Gothic', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Trade Gothic', 'Trade-Gothic', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Trade Gothic', 'Trade-Gothic', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Trade Gothic Light', 'Trade-Gothic-Light', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.2px
  body-lg:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Trade Gothic', 'Trade-Gothic', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Trade Gothic', 'Trade-Gothic', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Trade Gothic', 'Trade-Gothic', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Trade Gothic', 'Trade-Gothic', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Trade Gothic Light', 'Trade-Gothic-Light', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-value:
    fontFamily: "'Trade Gothic', 'Trade-Gothic', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 16px 32px
    height: 52px
    border: none
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
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 30px
    height: 52px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.primary-active}
  button-gold:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 12px 16px
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 14px 16px
    height: 52px
    border: 1px solid {colors.hairline}
    borderFocus: 2px solid {colors.primary}
  text-input-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.xl}
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: 0 2px 8px rgba(0,0,0,0.08)
  nav-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg}"
    borderTop: 3px solid {colors.primary}
    boxShadow: 0 8px 24px rgba(0,0,0,0.12)
  hero-banner:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    overlay: linear-gradient(to right, rgba(23,42,84,0.85), transparent)
  hero-cta:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 18px 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline}
    hoverBorder: 1px solid {colors.primary}
    hoverShadow: 0 4px 16px rgba(0,51,136,0.1)
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: 4/3
    objectFit: contain
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-subtitle:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  configurator-panel:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline}
    boxShadow: 0 2px 12px rgba(0,0,0,0.06)
  color-swatch:
    rounded: "{rounded.full}"
    height: 36px
    width: 36px
    border: 2px solid {colors.hairline}
    borderSelected: 3px solid {colors.primary}
  color-swatch-label:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
  spec-table-row:
    padding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  award-badge:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-gold}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    padding: 0 {spacing.base}
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.on-dark}"
    opacity: 0.75
    hoverOpacity: 1
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 48px
    padding: 0 {spacing.base}
    border: 1px solid {colors.hairline}
    borderFocus: 2px solid {colors.primary}

---

## Components

### Buttons

**`button-primary`** — Full-bleed royal blue (#003388) background with white uppercase Trade Gothic labels tracked at 1px. The squared `{rounded.xs}` radius matches the industrial precision of the product line. On hover, the background deepens to `{colors.primary-active}` (#002266) with no transition on border-radius. Disabled state desaturates to `{colors.primary-disabled}`, a muted steel-blue that reads as inactive without disappearing.

**`button-secondary`** — White fill with a 2px `{colors.primary}` border and blue uppercase text. Hover fills `{colors.surface-soft}` to create subtle depth without competing with primary CTAs. Used for "Compare Models", "View Specs", and secondary navigation actions.

**`button-gold`** — Reserved exclusively for promotional and configurator actions ("Build Your Own", "Request a Quote"). The `{colors.accent-gold}` background with dark text creates urgency without the blue-brand saturation, signaling a distinct action category.

**`button-ghost`** — Transparent background with underlined blue text. Used inline within body copy and specification panels for "Learn More" and "See Details" links that need button-level hit targets without visual weight.

### Navigation

**`nav-bar`** — 72px fixed header on white canvas with a single-pixel `{colors.hairline}` bottom border. Logo sits left; product category links run center in `{typography.nav-link}` (14px uppercase Trade Gothic, 700 weight, 0.5px tracking). On scroll, the bottom border drops away and a soft box-shadow fades in to lift the bar off content. Mega-menu dropdowns slide down with a 3px blue top border accent.

**`nav-mega-menu`** — Full-width dropdown panels organized in columns by product family (Ranges, Cooktops, Wall Ovens, Ventilation). Each column headed by a `{typography.title-md}` family name with thumbnail images at 80×60px. The 3px `{colors.primary}` top border anchors the panel to the active nav item.

### Hero

**`hero-banner`** — Edge-to-edge photography (typically a kitchen vignette or product beauty shot) overlaid with a left-anchored gradient from `{colors.navy-deep}` at 85% opacity to transparent. Display text in `{typography.display-xl}` (48px uppercase, white) sits within the gradient zone. The `{colors.accent-gold}` CTA button provides the sole warm-tone punctuation against the cool navy overlay.

### Product Cards

**`product-card`** — Contained within a 1px `{colors.hairline}` border box with `{rounded.xs}` corners. Product image renders on a `{colors.surface-soft}` background at 4:3 aspect ratio with `object-fit: contain` to preserve appliance proportions. On hover, the border shifts to `{colors.primary}` and a 16px blue-tinted shadow emerges. Title in `{typography.title-md}`, model number/subtitle in `{typography.body-sm}` muted gray.

### Configurator

**`configurator-panel`** — The range/oven builder tool uses a white panel with light shadow and `{rounded.sm}` corners. Color swatches render as `{rounded.full}` circles (36px diameter) in a wrapping grid, with the selected swatch receiving a 3px `{colors.primary}` border. Swatch labels appear below in `{typography.caption}`. Configuration steps are separated by `{colors.hairline-soft}` dividers.

### Specifications

**`spec-table-row`** — Two-column layout with label in `{typography.spec-label}` (Trade Gothic Light, 13px, gray) on the left and value in `{typography.spec-value}` (Trade Gothic bold, 13px, ink) on the right. Rows separated by 1px `{colors.hairline-soft}` borders. Used extensively on PDP pages for BTU ratings, dimensions, and feature lists.

### Awards & Badges

**`award-badge`** — Small gold pill with dark text in `{typography.button-sm}` uppercase. Appears on product cards and hero sections to surface editorial awards and certifications. The gold color ties it to the premium accent system rather than the primary action blue.

### Promotional Banner

**`promo-banner`** — 40px-tall strip in solid `{colors.primary}` blue pinned above the nav bar. White `{typography.body-sm}` text announces sales, events, or lead-time notices. Dismissible via an × icon that collapses the bar with no layout shift below.

### Footer

**`footer`** — Deep navy (`{colors.navy-deep}`) background spanning full width. Content organized in 4–5 columns: product families, support, company info, social links. Column headings in `{typography.title-sm}` at full white opacity; links at 75% opacity lifting to 100% on hover. A secondary row below carries legal text, copyright, and certification logos on `{colors.hairline-soft}` top border.

### Search

**`search-bar`** — Recessed input field with `{colors.surface-soft}` background and subtle hairline border. On focus, border strengthens to 2px `{colors.primary}`. Placeholder text in `{colors.muted}`. Results dropdown mirrors the mega-menu shadow treatment with product thumbnails and model numbers.

### Breadcrumb

**`breadcrumb`** — Compact wayfinding in `{typography.caption}` with `{colors.muted}` text and "/" separators in `{colors.hairline}`. Final crumb renders in `{colors.ink}` at the same weight to indicate current position without additional emphasis.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + slide-out drawer; hero image stacks above text (no gradient overlay); product grid drops to single column; configurator swatches reflow to 6-per-row; footer stacks vertically |
| Tablet | 744–1128px | Product grid moves to 2-up; mega-menu becomes accordion within the slide-out; hero text overlays at reduced font (36px); spec tables remain two-column |
| Desktop | 1128–1440px | Full nav with mega-menu dropdowns; 3-up product grid; hero at full 560px min-height; configurator panel sits beside product image in 60/40 split |
| Wide | > 1440px | Content max-width caps at 1440px with centered canvas; hero photography extends to viewport edge while text column stays within max-width; increased `{spacing.section-lg}` between page sections |

### Touch Targets

- All interactive elements maintain 48px minimum touch target on mobile/tablet
- Color swatches in configurator expand to 44px on touch devices with 8px gutters
- Nav drawer links receive 52px row height with full-width tap area
- Close/dismiss icons padded to 44×44px hit zone

### Collapsing Strategy

- Desktop mega-menu categories become accordion sections in mobile drawer, preserving hierarchy
- Product comparison table scrolls horizontally on mobile with sticky first column (model name)
- Specification tables remain two-column on all breakpoints; label column truncates with ellipsis below 360px
- Hero CTA moves below fold on mobile but gains a sticky bottom bar CTA on PDP scroll
- Promo banner text truncates with "..." on mobile; full message available on tap/expand

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Trade Gothic font weights and exact loading strategy (WOFF2 vs hosted CDN) could not be confirmed from extraction alone; the site likely loads via @font-face in a dynamically injected stylesheet
- Exact animation/transition durations (hover states, mega-menu open/close) not captured in static extraction
- The range configurator's interactive 3D/360° viewer component uses a custom canvas element whose internal styling is not extractable
- Several extracted blues (#0757fe, #0a7aff, #4280ff, #0866ff) appear to be WordPress editor/Gutenberg defaults rather than brand tokens — excluded from the palette
- Social media colors (#5865f2 Discord, #e94c89, #f00075) extracted but not included as brand tokens
- Mobile-specific nav drawer styling (slide direction, overlay opacity, close gesture) not determinable from color/font extraction
- Form validation states and inline error message styling not observed in extraction data
