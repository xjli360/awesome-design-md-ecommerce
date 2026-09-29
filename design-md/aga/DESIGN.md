---
version: alpha
name: "AGA"
source_url: "https://www.aga-ranges.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Cast iron rendered as code — the first thing that registers on AGA's digital presence is the weight of the product itself, translated through dense hero imagery of enamelled cookers in jewel tones against warm domestic interiors. The primary brand navy (#1a2a4a) anchors headers, CTAs, and the persistent navigation bar, a colour drawn directly from the darkest swatch in AGA's classic cooker palette. Supporting it is a heritage cream (#f5f0e8) that replaces the sterile white canvas most appliance brands default to, lending warmth that evokes the perpetual heat of an AGA's cast-iron core. Typography leans on a clean geometric sans-serif stack — likely Proxima Nova or similar — set at moderate weights (400 body, 600 titles, 700 display) with generous line-height to let the photography breathe. Product cards use `{rounded.sm}` corners and subtle `{colors.hairline}` borders, never competing with the curves of the cookers themselves. Buttons are squared-off at `{rounded.xs}`, reinforcing the industrial solidity of the brand; a `{colors.accent-red}` (#c41e3a) appears sparingly for promotional badges and sale callouts, recalling AGA's iconic claret enamel finish. The layout grid is conservative — a maxed 1280px content width with generous `{spacing.section}` vertical rhythm between feature blocks. Navigation carries a mega-menu pattern housing AGA's deep product taxonomy (range cookers, modules, refrigeration, outdoor) with category thumbnails. The overall impression is one of engineered permanence: nothing trendy, nothing transient, a digital showroom designed to feel as enduring as the hundred-year-old product it sells.

colors:
  primary: "#1a2a4a"
  primary-active: "#0f1d36"
  primary-disabled: "#8a95a8"
  accent-red: "#c41e3a"
  accent-red-active: "#a3182f"
  heritage-cream: "#f5f0e8"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#6b6b6b"
  muted-soft: "#999999"
  hairline: "#d9d4cc"
  hairline-soft: "#e8e4dc"
  canvas: "#ffffff"
  surface-soft: "#f9f7f4"
  surface-card: "#ffffff"
  surface-warm: "#f5f0e8"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent: "#ffffff"
  success: "#2e7d32"
  warning: "#e65100"
  star-rating: "#d4a017"
  scrim: "rgba(0, 0, 0, 0.55)"
  footer-bg: "#1a2a4a"
  footer-text: "#d9d4cc"

typography:
  display-xl:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  nav-category:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Proxima Nova', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase

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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary-active}"
  button-accent:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.12)"
  mega-menu-category-heading:
    textColor: "{colors.ink}"
    typography: "{typography.nav-category}"
    marginBottom: "{spacing.md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    hoverBoxShadow: "0 4px 16px rgba(0,0,0,0.1)"
  product-card-image:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 520px
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-banner-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-primary}"
    opacity: 0.9
  hero-lifestyle:
    minHeight: 600px
    overlayGradient: "linear-gradient(to right, rgba(26,42,74,0.7) 0%, transparent 60%)"
  colour-swatch:
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
    border: "2px solid {colors.hairline}"
  colour-swatch-active:
    border: "2px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    borderCollapse: separate
    rowOddBg: "{colors.surface-soft}"
    rowEvenBg: "{colors.canvas}"
    cellPadding: "{spacing.md} {spacing.base}"
  spec-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  badge-promo:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  range-configurator:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
  configurator-option:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    border: "1px solid {colors.hairline}"
  configurator-option-selected:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  dealer-locator-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separator: "/"
    activeColor: "{colors.ink}"

---

## Components

### Buttons

**`button-primary`** — A solid navy rectangle with sharp `{rounded.xs}` corners that communicates industrial confidence. Text is set in `{typography.button-lg}` weight 600 white. Hover darkens to `{colors.primary-active}`; disabled state fades to `{colors.primary-disabled}` with reduced opacity. Used for primary CTAs: "Find a dealer," "Configure your AGA," "Add to basket."

**`button-secondary`** — White fill with a 1.5px navy border and navy text. On hover, the background shifts to `{colors.surface-soft}` and the border deepens to `{colors.primary-active}`. Maintains the same 48px height and `{rounded.xs}` radius as primary. Used for secondary actions like "View specifications," "Download brochure."

**`button-accent`** — Reserved for promotional and urgency-driven CTAs (seasonal offers, limited editions). Uses `{colors.accent-red}` fill with white text at the slightly smaller 44px height. Hover shifts to `{colors.accent-red-active}`.

**`button-ghost`** — Text-only button in navy with no background or border. Padding is minimal. Used for inline actions within content blocks: "Read more," "See all colours."

### Navigation

**`nav-bar`** — A 72px-tall white bar with a 1px `{colors.hairline}` bottom border. Logo sits left, navigation links center or slightly right, utility icons (search, account, dealer locator) at far right. On scroll, the border disappears and a subtle box-shadow appears via `nav-bar-scrolled`.

**`mega-menu`** — Drops below the nav on hover/click of top-level category links. Full-width white panel with category headings in `{typography.nav-category}` (uppercase, 14px, weight 700) and sub-links in `{typography.body-sm}`. Includes thumbnail images for key product categories. Closes on mouse-leave or escape.

### Product Cards

**`product-card`** — A white card with `{rounded.sm}` corners and a subtle `{colors.hairline-soft}` border. Image area uses `{colors.surface-warm}` (heritage cream) as background behind product photography. Below sits the product title in `{typography.title-sm}`, a brief descriptor in `{typography.body-sm}`, and price in `{typography.price}`. On hover, the card lifts with a deeper shadow. No image zoom — the card relies on the enamel colour and product silhouette to draw the eye.

**`product-card-image`** — Uses a 4:3 aspect ratio container with the warm cream background. Products are photographed at a slight angle to show depth. The `{rounded.xs}` on the image container prevents hard corners from conflicting with the card's own radius.

### Hero

**`hero-banner`** — Used for category landing pages and seasonal campaigns. Full-width block with a minimum height of 520px, either a solid `{colors.primary}` navy background with white text or a lifestyle photograph with `hero-lifestyle` overlay gradient. Headline in `{typography.display-xl}`, subhead in `{typography.body-lg}` at 0.9 opacity. A primary or accent button sits below with `{spacing.lg}` top margin.

**`hero-lifestyle`** — Variant with a full-bleed kitchen photograph. A left-to-right gradient overlay (navy at 70% opacity fading to transparent) ensures headline legibility over the image while letting the right side of the photograph — usually showing the cooker in-situ — remain visible.

### Colour Swatches

**`colour-swatch`** — 40×40px circles (`{rounded.full}`) filled with the actual enamel colour, bordered by `{colors.hairline}`. Used on product detail pages for selecting cooker finish (cream, black, dark blue, claret, salvia green, etc.).

**`colour-swatch-active`** — Selected state adds a 2px `{colors.primary}` border with an additional 2px navy ring via box-shadow, clearly indicating the active choice without obscuring the colour fill.

### Range Configurator

**`range-configurator`** — A contained panel with `{colors.surface-soft}` background, `{rounded.sm}` corners, and `{spacing.xl}` internal padding. Houses the multi-step configuration flow where users select fuel type, oven count, colour, and accessories.

**`configurator-option`** / **`configurator-option-selected`** — Individual option tiles within the configurator. Default state has a 1px `{colors.hairline}` border; selected state thickens to 2px `{colors.primary}`. Keeps users oriented in a multi-option layout without relying on colour fills that would conflict with the swatch colours being displayed.

### Specifications Table

**`spec-table`** — Alternating row backgrounds (`{colors.surface-soft}` / `{colors.canvas}`) with labels in `{typography.spec-label}` muted grey and values in `{typography.spec-value}` ink. Used extensively on product detail pages to display dimensions, BTU ratings, energy classes, and capacities. No outer border — the alternating rows provide sufficient visual separation.

### Badges

**`badge-promo`** — Small accent-red pill with white uppercase text for promotional messaging ("SAVE £500," "LIMITED EDITION"). Positioned absolutely over product card images or inline next to prices.

**`badge-new`** — Navy variant for new product launches or recently added items.

### Footer

**`footer`** — Deep navy background matching `{colors.footer-bg}` with cream-tinted text (`{colors.footer-text}`). Organized in 4-5 columns: Products, Support, About AGA, Find a Dealer, Social. Headings in `{typography.title-sm}` white, links in `{typography.body-sm}` muted cream. A heritage mark or tagline may appear centered below the columns.

### Dealer Locator Card

**`dealer-locator-card`** — White card with `{rounded.sm}` corners used in search results for finding local AGA showrooms. Contains dealer name, address, phone, and distance. Subtle shadow keeps it lifted from the map interface behind it.

### Breadcrumb

**`breadcrumb`** — Simple text trail in `{typography.caption}` with forward-slash separators. Muted grey for parent links, `{colors.ink}` for the current page. Helps users navigate AGA's deep product hierarchy (Home / Range Cookers / AGA R7 / 100cm).

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Mega-menu becomes full-screen slide-over with accordion categories. Hero height reduces to 360px. Configurator stacks vertically. Nav collapses to hamburger + logo + search icon. |
| Tablet | 744–1128px | Two-column product grid. Mega-menu remains dropdown but narrows. Hero maintains 480px height. Side-by-side layout for configurator options. |
| Desktop | 1128–1440px | Three-column product grid. Full mega-menu with thumbnails. Hero at full 520px+. Configurator displays all steps horizontally. |
| Wide | > 1440px | Content maxes at 1280px centered. Margins grow symmetrically. Four-column grid available for category pages. Hero imagery scales to fill viewport width. |

### Touch Targets

- All interactive elements maintain minimum 44×44px tap target on mobile
- Colour swatches increase to 48×48px on touch devices with 8px gap between them
- Nav hamburger icon padded to 48px square
- Footer links spaced with `{spacing.md}` vertical gap on mobile for easy thumb reach

### Collapsing Strategy

- Desktop mega-menu → mobile full-screen accordion with category thumbnails retained
- Product specification tables → stacked label/value pairs on mobile (no horizontal scroll)
- Range configurator multi-column layout → vertical step-by-step flow on mobile
- Hero side-by-side text/image → stacked with image above, text below on mobile
- Footer multi-column → single accordion column with expandable sections
- Breadcrumb truncates middle segments on mobile, showing first and last two levels with "..." ellipsis

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colours could be extracted from the live site (likely loaded via JavaScript bundles or behind anti-bot protections); the palette above is inferred from widely-documented AGA brand materials and may not match the exact digital implementation
- No font-family stacks were detected; Proxima Nova is used as a reasonable assumption based on the brand's premium-appliance positioning but the actual typeface could not be confirmed
- Exact border-radius values, spacing scale, and component dimensions are estimated from brand-category conventions rather than measured from the live site
- Animation/transition timing (hover states, menu open/close, configurator step transitions) could not be observed
- Dark-mode tokens are not defined — the site likely does not offer a dark theme
- Specific icon set (line weight, style, library) is unknown
- Form validation patterns, toast/notification styling, and modal overlays were not observable
- The exact mega-menu structure and depth of product taxonomy could not be confirmed from extraction
