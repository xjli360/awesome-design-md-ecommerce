---
version: alpha
name: "Oxford University Press"
source_url: "https://global.oup.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep navy blue (#002147) — the color of academic gowns and the Oxford sky at dusk — anchors every header, footer, and primary action across the site, while body text runs in a clean #333333 on a white (#ffffff) canvas that never wavers. The typography is unapologetically utilitarian: Arial at 16px for body copy, with display headings rarely exceeding 24px, reflecting a brand that trusts its content over its container. Navigation is a dense, text-heavy affair — a two-tier masthead with a global utility bar (Login, Cart, Help) above a subject-matter mega-menu that lists 30+ disciplines in a single column, each link set in 12px Arial with no iconography to soften the cognitive load. Search is a simple rectangular input with a magnifying-glass icon, not a pill or orb, and buttons are flat rectangles with 2px borders and no gradient or shadow — the form follows the function of a reference work. Product cards for books show the cover thumbnail, title, author, and price in a rigid three-column grid, with no hover animations or star ratings; the design language is that of a library catalog, not a retail storefront. The only decorative flourish is the OUP logo — a heraldic shield with an open book and the university motto — which appears in the top-left corner at a modest 40px height, never competing with the text. This is a system built for clarity, hierarchy, and the efficient retrieval of information, where every pixel serves the reader's task.

colors:
  primary: "#002147"
  primary-active: "#001a36"
  primary-disabled: "#b3c4d4"
  ink: "#000000"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#cccccc"
  hairline-soft: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#002147"
  link-hover: "#001a36"
  link-visited: "#551a8b"
  accent-red: "#c8102e"
  accent-gold: "#b3995d"
  error: "#c8102e"
  success: "#2e7d32"
  warning: "#f9a825"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.25px
  display-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.36
    letterSpacing: 0
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.44
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  body-lg:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.67
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.63
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.5px
  link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0.25px
  nav-link-subject:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.67
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  micro:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
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
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 9px 23px
    height: 40px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 10px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    outline: none
  text-input-error:
    border: "2px solid {colors.error}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 32px 10px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  textarea:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px
    border: "1px solid {colors.hairline}"
  checkbox:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 18px
  checkbox-checked:
    backgroundColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
  radio:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.hairline}"
    rounded: "{rounded.full}"
    height: 18px
  radio-checked:
    border: "6px solid {colors.primary}"
  top-nav-utility:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 32px
  top-nav-main:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 48px
    border-bottom: "1px solid {colors.hairline}"
  nav-link-utility:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  nav-link-main:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
  nav-link-main-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    border-bottom: "3px solid {colors.primary}"
  nav-link-subject:
    textColor: "{colors.body}"
    typography: "{typography.nav-link-subject}"
  nav-link-subject-hover:
    textColor: "{colors.primary}"
  mega-menu-column:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.lg}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: 8px 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-image:
    rounded: "{rounded.none}"
    height: 240px
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-author:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  breadcrumb-link:
    textColor: "{colors.link}"
    typography: "{typography.caption}"
  breadcrumb-current:
    textColor: "{colors.body}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
  footer-divider:
    backgroundColor: "{colors.on-primary}"
    opacity: 0.2
    height: 1px
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-subtitle:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-primary}"
    opacity: 0.9
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.lg} 0 {spacing.base} 0"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  table-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  table-cell:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    border-bottom: "1px solid {colors.hairline-soft}"
  pagination:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  pagination-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    padding: "4px 10px"
  pagination-link:
    textColor: "{colors.link}"
    padding: "4px 10px"
  alert-info:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    border-left: "4px solid {colors.primary}"
  alert-error:
    backgroundColor: "#fef2f2"
    textColor: "{colors.error}"
    border-left: "4px solid {colors.error}"
  alert-success:
    backgroundColor: "#f0fdf4"
    textColor: "{colors.success}"
    border-left: "4px solid {colors.success}"
  alert-warning:
    backgroundColor: "#fffde7"
    textColor: "{colors.warning}"
    border-left: "4px solid {colors.warning}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "4px 8px"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in Oxford blue (#002147) with white text and a subtle 4px radius. On hover, it darkens to #001a36; when disabled, it fades to a muted blue-gray (#b3c4d4) with gray text. The 40px height and 14px bold uppercase lettering give it a no-nonsense academic weight.
**`button-secondary`** — An outlined variant with a 2px Oxford blue border on a white background. The active state fills the background with a soft gray (#f5f5f5) and darkens the border. Used for "View All" links, secondary actions in forms, and cancel buttons.
**`button-tertiary-text`** — A text-only link styled as a button, used for "Learn More" and "Read Sample" actions. No background, no border — just the Oxford blue text with a hover color shift to #001a36.

### Navigation
**`top-nav-utility`** — A 32px-high dark blue strip at the very top of the page, containing Login, Cart, Help, and language selector links in white 12px bold text. This bar is fixed-width centered and sits above the main navigation.
**`top-nav-main`** — A 48px-high white bar with the OUP logo on the left and subject-matter navigation links on the right. A single 1px hairline border separates it from the utility bar above. The active link is indicated by a 3px bottom border in Oxford blue.
**`mega-menu-column`** — A dropdown panel triggered by hovering over a subject link in the main nav. It appears as a single column of 12px links with no icons, no images, and no sub-columns — just a dense list of disciplines from "Anthropology" to "Zoology". The panel has a 1px soft hairline border and 24px padding.

### Search
**`search-bar`** — A rectangular text input with a 1px hairline border and 4px radius, sitting at 40px height. On focus, the border thickens to 2px Oxford blue. The search icon is a simple magnifying glass placed inside the input on the left, and a blue submit button sits to the right.
**`search-submit`** — A 40px-tall Oxford blue button with white text and 4px radius, placed immediately to the right of the search input. No icon — just the word "Search" in 14px bold.

### Cards
**`product-card`** — A book listing card with no rounded corners, a 1px soft hairline border, and 16px padding. The layout is a vertical stack: cover image (240px tall, no radius), title in 14px bold, author in 12px gray, and price in 14px bold. No hover animation, no shadow, no rating.
**`product-card-badge`** — A small red (#c8102e) label with white uppercase text, used for "New", "Sale", or "Coming Soon" flags. It sits in the top-left corner of the card image with 2px padding and a 2px radius.

### Forms
**`text-input`** — A standard 40px-tall input with 1px hairline border and 4px radius. On focus, the border becomes 2px Oxford blue. Error state uses a 2px red border. Disabled inputs use a soft gray background and gray text.
**`select-input`** — A dropdown with the same dimensions as text-input, with a custom arrow icon on the right. The arrow is a simple downward chevron in Oxford blue.
**`checkbox`** and **`radio`** — Small 18px controls with a 2px hairline border. The checked state fills the background with Oxford blue (checkbox) or shows a 6px Oxford blue dot (radio). Both use a 2px radius for checkboxes and full round for radios.

### Footer
**`footer`** — A full-width Oxford blue band at the bottom of every page, with white text in 14px. It contains four columns of links (About, Products, Resources, Help) with 14px bold headings and 14px regular links. A semi-transparent white divider separates the columns from the copyright line. The footer has 64px top and bottom padding.

### Alerts
**`alert-info`** — A light gray background with a 4px Oxford blue left border, used for informational messages like "Free shipping on orders over $50". The text is in body-sm (14px) with 12px padding.
**`alert-error`** — A pale red background with a 4px red left border, used for error messages.
**`alert-success`** — A pale green background with a 4px green left border, used for success confirmations.
**`alert-warning`** — A pale yellow background with a 4px yellow left border, used for warnings.

### Tables
**`table-header`** — A light gray (#f5f5f5) row with 14px bold text and 8px/16px padding. Used for column headers in product listings, pricing tables, and comparison charts.
**`table-cell`** — A standard cell with 14px regular text and a 1px soft hairline bottom border. No alternating row colors — the design relies on the bottom border alone for row separation.

### Pagination
**`pagination`** — A horizontal row of page numbers in 14px text. The active page is rendered as an Oxford blue rectangle with 4px radius and white text. Inactive pages are blue links with no background. Previous/Next arrows are simple left/right chevrons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; top-nav-utility collapses to hamburger menu; mega-menu becomes accordion; product cards stack vertically; search bar full-width; footer columns stack |
| Tablet | 744–1024px | Two-column product grid; top-nav-utility shows key links only; mega-menu becomes two-column; search bar 60% width |
| Desktop | 1024–1440px | Three-column product grid; full top-nav-utility visible; mega-menu as single column; search bar 40% width; footer four-column |
| Wide | > 1440px | Max-width container at 1280px; all layouts centered; product grid can expand to four columns; additional whitespace on sides |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height on mobile to meet WCAG touch-target guidelines.
- Navigation links in the utility bar are 32px tall on desktop but expand to 44px on mobile.
- Checkbox and radio controls are 18px on desktop, 24px on mobile.
- Search submit button is 40px tall on all breakpoints.

### Collapsing Strategy
- The top-nav-utility collapses to a single hamburger icon on mobile, revealing a full-screen overlay menu with all links in a vertical list.
- The subject-matter mega-menu collapses to an accordion on mobile, with each subject heading expanding to reveal its list of disciplines.
- The footer collapses from four columns to a single vertical stack on mobile, with each section heading acting as an accordion toggle.
- The product grid collapses from three columns to two on tablet and one on mobile.
- The search bar expands to full width on mobile and shrinks to 40% on desktop.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted hex colors were available from the live site (the extraction returned empty). The color palette above is based on the Oxford University Press brand guidelines (Oxford blue #002147 is the official university color) and common web conventions for an academic publisher. The actual live site may use different shades.
- No font-family declarations beyond Arial were found. The site may use a custom typeface (e.g., Oxford fonts) that was not detected by the extraction tool.
- Hover states for most components are inferred from common patterns rather than extracted from the live site.
- Error, success, and warning colors are based on standard web conventions, not extracted from the brand.
- Dark mode is not supported and no dark-mode color tokens were extracted.
- Sub-brand palettes (e.g., for Oxford Academic, Oxford Scholarship Online, etc.) were not extracted.
- The mega-menu structure and its responsive behavior are inferred from common patterns for large academic publishers.
- No animation or transition timings were extracted.
- No box-shadow values were extracted; the design appears to use flat shadows or none at all.
- The product card image height (240px) is an assumption based on common book-cover aspect ratios.
- The breadcrumb component structure is inferred from typical e-commerce patterns.
- The pagination component is inferred from common listing-page patterns.
- The alert components are based on standard web conventions, not extracted from the brand.
