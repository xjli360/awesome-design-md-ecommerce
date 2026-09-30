---
version: alpha
name: "Leen Heyne"
source_url: "https://www.leenheyne.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every photograph on leenheyne.com dissolves into a warm ivory field — the background is not white but the particular off-white of aged paper and polished bone, a deliberate contrast against the cool platinum and rose gold of the rings themselves. Leen Heyne is a Dutch atelier producing bespoke engagement rings and fine jewelry; the visual identity leans hard into the editorial quietness of Scandinavian luxury rather than the baroque density typical of traditional jewelers. Display type is set in a high-contrast hairline serif — the kind that narrows to near-invisibility on thin strokes — at large point sizes and generous tracking, producing headlines that feel more like captions in a contemporary art catalogue than product names. The primary accent is a warm antique gold, used almost nowhere except CTA buttons, hover underlines, and the faint ruled hairlines that separate content zones; the site depends on restraint, trusting the photography to carry visual weight. Rounded corners are virtually absent — rings, product cards, and input fields are rendered with minimal or zero radius, echoing the precision geometry of the jewelry itself. Navigation is minimal: a wordmark left, three or four links right, and nothing else — no mega-menus, no promotional banners. Product detail pages expand into full-bleed imagery stacked vertically, with specification type in a small-caps sans-serif beneath. The customization flow, which is the brand's commercial core, opens as an inline configurator rather than a separate page, keeping the editorial calm intact. The overall chromatic register is warm neutrals — ivory, champagne, warm gray, near-black — with the single gold `{colors.primary}` note providing all necessary contrast against the `{colors.canvas}` field. Spacing is generous to the point of ceremony: section gaps of 80–96px, product grids with wide gutters, and text blocks that never run wider than roughly 60 characters. This is a site that moves slowly and expects visitors to stay.

colors:
  primary: "#B8975A"
  primary-active: "#9A7C43"
  primary-disabled: "#DDD0B3"
  ink: "#1A1714"
  body: "#3B3530"
  muted: "#7A7068"
  hairline: "#DDD8D0"
  hairline-soft: "#EDEAE4"
  canvas: "#FDFAF5"
  surface-soft: "#F5F0E8"
  surface-card: "#FAF7F2"
  surface-warm: "#EDE8DE"
  on-primary: "#FDFAF5"
  on-dark: "#FDFAF5"
  champagne: "#E8DFC8"
  deep-brown: "#0F0C0A"
  error: "#9C3A2E"
  success: "#4A7A5A"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: 0.04em
  display-lg:
    fontFamily: "'Cormorant Garamond', 'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: 0.03em
  display-md:
    fontFamily: "'Cormorant Garamond', 'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: 0.025em
  display-sm:
    fontFamily: "'Cormorant Garamond', 'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-md:
    fontFamily: "'Jost', 'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.12em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Jost', 'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0.14em
    textTransform: uppercase
  body-md:
    fontFamily: "'Jost', 'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 300
    lineHeight: 1.7
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'Jost', 'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 300
    lineHeight: 1.65
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Jost', 'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.06em
  button-md:
    fontFamily: "'Jost', 'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.16em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.14em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Jost', 'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  price:
    fontFamily: "'Cormorant Garamond', 'Cormorant', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.02em
  small-caps-label:
    fontFamily: "'Jost', 'Raleway', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.18em
    textTransform: uppercase
  editorial-quote:
    fontFamily: "'Cormorant Garamond', 'Cormorant', Georgia, serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.45
    letterSpacing: 0.015em
    fontStyle: italic

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
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
  section: 80px
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 46px
    border: none
    hoverBackgroundColor: "{colors.primary-active}"
    transition: background-color 0.25s ease
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 46px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 46px
    border: "1px solid {colors.ink}"
    hoverBorderColor: "{colors.primary}"
    hoverTextColor: "{colors.primary}"
    transition: border-color 0.25s ease, color 0.25s ease
  button-ghost-underline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderBottom: "1px solid {colors.ink}"
    hoverBorderColor: "{colors.primary}"
    hoverTextColor: "{colors.primary}"
    paddingBottom: 3px
  button-text-gold:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderBottom: "1px solid {colors.primary}"
    paddingBottom: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xxl}"
    logoTypography: "{typography.display-sm}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 0"
    border: none
    borderBottom: "1px solid {colors.hairline}"
    focusBorderBottomColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    transition: border-color 0.2s ease
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    gap: "{spacing.md}"
    nameFontStyle: "{typography.title-md}"
    priceTypography: "{typography.price}"
    textColor: "{colors.body}"
    hoverImageScale: 1.03
    transition: transform 0.4s ease
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: "90vh"
    padding: "{spacing.section} {spacing.xxl}"
    imagePosition: right
    imageWidth: "55%"
  category-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-lg}"
    labelTypography: "{typography.small-caps-label}"
    labelColor: "{colors.primary}"
    padding: "{spacing.section} {spacing.xxl}"
    minHeight: "60vh"
  editorial-quote-block:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    quoteTypography: "{typography.editorial-quote}"
    attributionTypography: "{typography.small-caps-label}"
    attributionColor: "{colors.muted}"
    padding: "{spacing.section} {spacing.xxl}"
    maxWidth: 720px
    borderLeft: "2px solid {colors.primary}"
    paddingLeft: "{spacing.xl}"
  product-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.small-caps-label}"
    subtitleColor: "{colors.primary}"
    priceTypography: "{typography.price}"
    bodyTypography: "{typography.body-md}"
    dividerColor: "{colors.hairline}"
    padding: "{spacing.xl} {spacing.xxl}"
  ring-configurator:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    labelTypography: "{typography.small-caps-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    selectedSwatchBorder: "2px solid {colors.ink}"
    swatchSize: 28px
    swatchGap: "{spacing.sm}"
  material-swatch:
    size: 28px
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    activeBorder: "2px solid {colors.ink}"
    hoverBorder: "1.5px solid {colors.muted}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    size: 40px
    border: "1px solid {colors.hairline}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.small-caps-label}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: "3px 8px"
  badge-bespoke:
    backgroundColor: "{colors.champagne}"
    textColor: "{colors.body}"
    typography: "{typography.small-caps-label}"
    rounded: "{rounded.none}"
    padding: "3px 10px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.champagne}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.small-caps-label}"
    headingColor: "{colors.muted}"
    borderTop: "none"
    padding: "{spacing.section} {spacing.xxl}"
  section-divider:
    height: 1px
    backgroundColor: "{colors.hairline}"
    margin: "{spacing.section} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  atelier-callout:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.body}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.section} {spacing.xxl}"
    layout: "2-column"

## Components

### Buttons

**`button-primary`** — A flat rectangle with zero border radius, `{colors.primary}` antique-gold fill, and `{typography.button-md}` uppercase tracked sans-serif. Height sits at 46px with 32px horizontal padding; the hover state darkens the fill to `{colors.primary-active}` over 250ms. The disabled state uses `{colors.primary-disabled}`, a pale champagne that signals unavailability without visual noise.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border; on hover the border and text transition to `{colors.primary}` gold over 250ms, reinforcing the gold-as-action-signal system. Same height and padding as the primary.

**`button-ghost-underline`** — Inline text-only CTA with a single bottom border replacing the box frame. Used for editorial "Explore" or "Learn More" links within content columns; the underline shifts to `{colors.primary}` on hover.

**`button-text-gold`** — Pre-styled gold inline link used for configurator steps and filter labels. No box, just `{colors.primary}` text with a matching bottom border.

### Navigation

**`nav-bar`** — 72px tall, `{colors.canvas}` background separated from content by a 1px `{colors.hairline}` border. The wordmark is set in `{typography.display-sm}` at reduced weight, sitting left; links in `{typography.nav-link}` uppercase tracking sit right. No hamburger on desktop; on mobile the links collapse into a full-screen overlay. The nav does not compress or change appearance on scroll — no sticky color flip.

### Product Card

**`product-card`** — Image at 4:5 aspect ratio with a 1.03× scale on hover over 400ms — slow enough to feel considered rather than snappy. Name in `{typography.title-md}` uppercase tracking below, price in `{typography.price}` serif on the next line. No card border, no shadow — the card is a frameless image-and-text stack on the `{colors.canvas}` page.

### Hero

**`hero-section`** — Two-column layout at desktop: editorial copy occupying 45% width at left, full-bleed photography at right bleeding to the viewport edge. Headline in `{typography.display-xl}` weight 300 with generous tracking. Minimum height 90vh. At mobile this collapses to stacked image-above, text-below with reduced headline to `{typography.display-lg}`.

### Configurator

**`ring-configurator`** — The core commerce component. A `{colors.surface-card}` panel with 1px `{colors.hairline}` border and zero radius. Step labels in `{typography.small-caps-label}` muted; values in `{typography.body-md}`. Material swatches are 28px circles with a 2px `{colors.ink}` selection ring. Size tiles are 40×40px flat squares. A persistent summary bar anchors to the panel bottom showing current selection and the primary CTA.

### Editorial & Supporting

**`editorial-quote-block`** — A `{colors.surface-warm}` band spanning full width, with a 2px `{colors.primary}` left border and the quote set in `{typography.editorial-quote}` italic. Attribution below in `{typography.small-caps-label}` muted. Max content width 720px, centered.

**`category-banner`** — Full-bleed section header at 60vh min-height. Label in `{typography.small-caps-label}` gold above a headline in `{typography.display-lg}` weight 300. Background `{colors.surface-soft}` or photography.

**`atelier-callout`** — Two-column band reserved for the bespoke/custom-order pitch. Left column carries `{typography.display-sm}` headline and `{typography.body-md}` prose; right column carries a CTA button. Background `{colors.surface-soft}`.

**`footer`** — Dark `{colors.ink}` background. Column headings in `{typography.small-caps-label}` `{colors.muted}`; links in `{typography.caption}` `{colors.champagne}`. No logo repeat; wordmark in small white type at bottom-left beside a copyright line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; hero stacks image above text; nav collapses to full-screen overlay; product grid drops to 1 column; configurator goes full-width modal; section padding reduces to `{spacing.xl}` |
| Tablet | 744–1128px | Hero shifts to 40/60 split; product grid moves to 2 columns; configurator runs in a side-by-side two-column layout; nav retains 3–4 visible links with overflow hidden |
| Desktop | 1128–1440px | Full two-column hero; 3-column product grid; configurator panel inline at 50% viewport width; full footer column layout |
| Wide | > 1440px | Content max-width caps at 1440px; page margins expand to maintain centered column; hero photography scales up within viewport; no new layout regions introduced |

### Touch Targets

- All interactive buttons minimum 44px tall on mobile; icon-only controls padded to 44×44px hit area
- Swatch selectors expand from 28px visual to 44px tap zone via padding
- Nav overlay links minimum 52px tall with full-width tap zone
- Breadcrumb links padded to minimum 32px vertical

### Collapsing Strategy

- Navigation menu collapses to hamburger icon at < 744px; overlay takes full viewport with links in `{typography.display-sm}` serif for legibility
- Two-column editorial blocks reflow to single column; image moves above text
- Ring configurator transitions from inline panel to bottom-sheet modal on mobile, preserving scroll context on the PDP above
- Footer 4-column grid compresses to 2 columns at tablet, single column at mobile with accordioned link groups
- Hero display headline scales from `{typography.display-xl}` (56px) to `{typography.display-md}` (32px) at mobile breakpoint

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — the palette above is inferred from the brand's documented aesthetic (Dutch fine jewelry, editorial minimalism) and is a best-effort approximation. Actual brand primaries may differ.
- No font families were extracted — the typography stack (Cormorant Garamond + Jost) represents a plausible match for the brand's visual register but is not confirmed from site inspection.
- No meta theme-color was present, removing one signal for the primary brand color.
- Site does not run on Shopify, meaning standard Shopify token extraction methods returned nothing; the platform and any framework-level design tokens are unknown.
- Specific corner radius values, exact spacing rhythm, and shadow/blur values on overlay panels could not be confirmed.
- Animation curves and durations (beyond the hover transitions modeled here) are unverified.
- Whether the brand uses a custom typeface (commissioned or licensed) versus the open-source stacks above is unknown.
- Configurator step logic (number of steps, pricing display, 3D viewer presence) is unconfirmed and the component spec above reflects a plausible pattern only.
