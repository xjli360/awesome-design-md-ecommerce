---
version: alpha
name: "Columbia University Press"
source_url: "https://cup.columbia.edu"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep navy #0c4da2 anchors the Columbia University Press website like the spine of a clothbound academic volume — it appears in the primary nav bar, hover states on linked text, and the bold header band that introduces each section. The site runs on a two-typeface system: Adobe Caslon W01 for display and body text, lending a serifed gravity that signals peer-reviewed authority, and Museo Sans W01 for UI labels, buttons, and metadata, introducing a clean sans-serif counterpoint that prevents the reading experience from feeling antiquarian. The canvas is a warm off-white #eeeeee rather than pure white, softening the reading surface for long-form catalog copy and author interviews. Accent colors arrive sparingly but with purpose: #dc3232 appears on sale badges and error states, #00d084 on in-stock indicators, and #fdf497 on highlighted callout boxes — each a small jolt against the predominantly blue-gray palette. The search bar uses a pill shape ({rounded.full}) with a subtle border, while buttons are softly rectangular ({rounded.sm}), never aggressive. The overall mood is that of a serious but accessible library reading room: hushed, orderly, and confident in its typographic hierarchy.

colors:
  primary: "#0c4da2"
  primary-active: "#003388"
  primary-disabled: "#8ba8d1"
  ink: "#313131"
  body: "#444444"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#dddddd"
  canvas: "#eeeeee"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sale: "#dc3232"
  accent-stock: "#00d084"
  accent-highlight: "#fdf497"
  accent-link: "#0693e3"
  accent-cta: "#003399"

typography:
  display-xl:
    fontFamily: "'Adobe Caslon W01', 'Adobe Caslon W01_B6', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Adobe Caslon W01', 'Adobe Caslon W01_B6', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Adobe Caslon W01', 'Adobe Caslon W01_B6', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  display-sm:
    fontFamily: "'Adobe Caslon W01', 'Adobe Caslon W01_B6', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Museo Sans W01', 'Museo Sans W01_R5', 'Museo Sans W01_n4', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Museo Sans W01', 'Museo Sans W01_R5', 'Museo Sans W01_n4', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Adobe Caslon W01', 'Adobe Caslon W01_B6', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Adobe Caslon W01', 'Adobe Caslon W01_B6', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Museo Sans W01', 'Museo Sans W01_R5', 'Museo Sans W01_n4', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Museo Sans W01', 'Museo Sans W01_R5', 'Museo Sans W01_n4', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Museo Sans W01', 'Museo Sans W01_R5', 'Museo Sans W01_n4', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Museo Sans W01', 'Museo Sans W01_R5', 'Museo Sans W01_n4', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Museo Sans W01', 'Museo Sans W01_R5', 'Museo Sans W01_n4', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Adobe Caslon W01', 'Adobe Caslon W01_B6', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  nav-link:
    fontFamily: "'Museo Sans W01', 'Museo Sans W01_R5', 'Museo Sans W01_n4', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
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
    padding: 10px 24px
    height: 40px
  button-primary-active:
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
    padding: 9px 23px
    height: 40px
    border: "1px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.primary-active}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 10px 0
  button-tertiary-active:
    textColor: "{colors.primary-active}"
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: "none"
  text-input-error:
    border: "1px solid {colors.accent-sale}"
  select-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 40px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
  nav-bar-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 0 16px
  nav-bar-link-active:
    textColor: "{colors.on-primary}"
    borderBottom: "2px solid {colors.on-primary}"
  nav-bar-link-hover:
    textColor: "{colors.on-primary}"
    opacity: 0.85
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.md}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    marginTop: "{spacing.xs}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.accent-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-stock:
    backgroundColor: "{colors.accent-stock}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-cta}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-subtitle:
    typography: "{typography.title-md}"
    textColor: "{colors.on-primary}"
    marginTop: "{spacing.md}"
  section-header:
    typography: "{typography.display-lg}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.xl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  accordion-trigger:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.sm}"
  accordion-panel:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.base} {spacing.lg}"
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"
  tab-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm} {spacing.md}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action button, used for "Add to Cart", "Subscribe", and "Search" actions. It uses a solid navy fill ({colors.primary}) with white text and a subtle 4px radius ({rounded.sm}). On hover, it deepens to {colors.primary-active} (#003388). The disabled state uses a lighter blue {colors.primary-disabled} (#8ba8d1) to indicate non-interactivity while maintaining brand continuity.

**`button-secondary`** — An outlined variant for secondary actions like "View Details" or "Learn More". It uses a white background with a 1px {colors.primary} border and navy text. The active state shifts the border and text to {colors.primary-active}. This button sits alongside primary buttons in product listings and catalog pages.

**`button-tertiary`** — A text-only link styled as a button, used for "Cancel" or "Back to Results" actions. It carries no background or border, only {colors.primary} text that darkens to {colors.primary-active} on hover. This is the quietest button in the system, reserved for low-priority navigation.

**`button-pill`** — A fully rounded variant ({rounded.full}) used sparingly for promotional CTAs or "Shop Now" badges on featured items. It uses the same navy fill and white text as the primary button but with a pill shape that reads as more promotional and less transactional.

### Cards
**`product-card`** — The standard book listing card, used across search results, category pages, and author collections. It is a white card ({colors.surface-card}) with 8px rounded corners ({rounded.md}) and 16px padding. The card contains a book cover image (also 8px rounded), a title in {typography.title-sm}, an author line in {typography.caption} at {colors.muted}, and a price in {typography.body-md} at {colors.ink}. Cards stack in a responsive grid that goes from 1 column on mobile to 4 columns on desktop.

### Navigation
**`nav-bar`** — The primary site navigation bar, fixed at 56px height with a solid {colors.primary} background. Navigation links use {typography.nav-link} — 14px Museo Sans with 0.5px letter spacing and uppercase transformation — in white. The active link is underlined with a 2px white border. On hover, links reduce opacity to 0.85. The nav bar collapses into a hamburger menu on mobile.

**`search-bar`** — A pill-shaped search input ({rounded.full}) with a white background and 1px {colors.hairline} border. On focus, the border thickens to 2px and shifts to {colors.primary}. The search bar sits prominently in the nav bar on desktop and expands to full width on mobile.

### Forms
**`text-input`** — Standard text input for forms (search, newsletter signup, contact). It uses a white background, 1px {colors.hairline} border, and 4px radius ({rounded.sm}). On focus, the border becomes a 2px {colors.primary} stroke. Error states use a 1px {colors.accent-sale} border.

**`select-input`** — Dropdown select menus styled to match text inputs: white background, 1px {colors.hairline} border, 4px radius. Used for filtering products by category, sorting by date or price, and selecting quantities.

### Badges
**`badge-sale`** — A small uppercase badge with {colors.accent-sale} (#dc3232) background and white text. Used on product cards to indicate discounted prices. The badge has a 2px radius ({rounded.xs}) and tight padding (2px 8px).

**`badge-stock`** — A green badge ({colors.accent-stock} #00d084) indicating in-stock status. Same shape and typography as the sale badge but communicates availability rather than promotion.

**`badge-new`** — A blue badge ({colors.accent-cta} #003399) used for new releases or featured titles. It sits in the top-left corner of product card images.

### Footer
**`footer`** — The site footer uses a dark {colors.ink} (#313131) background with white text. It contains copyright information, policy links, and social media icons. Links use {typography.caption} at 80% opacity, increasing to full opacity on hover. The footer is padded with {spacing.xl} vertically and {spacing.lg} horizontally.

### Accordion
**`accordion-trigger`** — Used for FAQ sections and collapsible content panels. The trigger has a soft background ({colors.surface-soft}) with 4px radius and 12px padding. On click, it expands to reveal the `accordion-panel` below, which uses a white background and standard body typography.

### Tabs
**`tab-active`** — The active tab in a tabbed interface (used on product detail pages for "Description", "Reviews", "Details"). It uses a solid {colors.primary} fill with white text and 4px radius. Inactive tabs use a soft background ({colors.surface-soft}) with muted text, signaling they are clickable but not selected.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack in single column; search bar expands to full width; hero banner text reduces to {typography.display-md}; footer links stack vertically |
| Tablet | 744–1128px | Nav bar shows full links but with reduced padding; product cards display in 2-column grid; hero banner maintains display-lg; search bar remains in nav bar but narrows |
| Desktop | 1128–1440px | Full nav bar with all links visible; product cards in 3-column grid; hero banner at full display-xl; search bar at standard width in nav bar |
| Wide | > 1440px | Max-width container (1440px) centers content; product cards in 4-column grid; additional whitespace around hero banner and section headers |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height for touch accessibility
- Nav bar links have 16px horizontal padding, ensuring adequate tap targets
- Search bar height is 40px on desktop, 48px on mobile for easier tapping
- Accordion triggers have 12px vertical padding, making them easy to tap on touch devices

### Collapsing Strategy
- Nav bar links collapse into a hamburger menu below 744px
- Product card grid reduces columns from 4 to 1 as viewport narrows
- Hero banner text reduces by one typography tier at each breakpoint
- Footer links stack vertically on mobile, with each link on its own line
- Tab interfaces on product pages collapse into a select dropdown on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is heavily weighted toward blues and grays, with a few bright accents (#dc3232, #00d084, #fdf497, #0693e3) that appear to be functional (sale, stock, highlight, link) rather than brand-defining. The true brand primary (#0c4da2) was selected as the most distinctive blue in the list, but without access to the actual design tokens, the exact hierarchy of accent colors is inferred.
- Font-family declarations were extracted from CSS but exact weights and sizes for each typography tier are estimated based on common academic press patterns. The actual site may use different sizes for display, body, and UI text.
- Hover, focus, and active states for all components are inferred from common patterns; the actual site may use different transitions, opacities, or color shifts.
- Error styling for forms (error messages, validation icons) was not extracted and is estimated.
- Dark mode is not present on the live site; no dark mode tokens are defined.
- Sub-brand palettes (e.g., for specific book series or imprints) were not extracted and may exist.
- The exact border radius values for cards, buttons, and inputs are estimated; the actual site may use different values.
- Spacing values (padding, margins) are estimated based on common grid systems; the actual site may use a different spacing scale.
- The extracted font list includes multiple variants of Museo Sans (W01_R5, W01_i1, W01_i2, W01_n1, W01_n3, W01_n4) and Adobe Caslon (W01, W01_B6), but the exact mapping of variant to typography tier is inferred.
