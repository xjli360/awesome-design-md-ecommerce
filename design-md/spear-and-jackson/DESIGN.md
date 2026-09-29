---
version: alpha
name: "Spear & Jackson"
source_url: "https://www.spear-and-jackson.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Deep-soil green (#234600) anchors every header bar and primary action on a site that reads more like an indexed workshop manual than a lifestyle catalogue. Spear & Jackson — trading since 1760 — lets the product photography do the selling while the interface stays deliberately unadorned: a canvas of warm grays (#eeeeee, #f4f4f4) layered with card surfaces at #f6f6f6, separated by hairlines so pale they barely register. The typographic stack pairs Baskerville for display moments — a nod to the brand's Sheffield-steel heritage that feels engraved rather than designed — with Arial and Verdana for body text at utilitarian weights, prioritising scannability across dense product grids. Buttons and category navigation carry that hunter-green at full saturation; active and hover states shift to a brighter spring-lime (#bbee77) that evokes new growth on an established trunk. Corner radii stay tight — `{rounded.xs}` on inputs, `{rounded.sm}` on cards — reinforcing the squared-off, no-nonsense posture of a toolmaker's brand. An orange (#ed541d) appears exclusively for alerts, sale flags, and error states, calibrated to feel urgent against the otherwise muted palette. Spacing is generous vertically (`{spacing.section}` between product groups) but compressed horizontally inside grid cells, letting the eye scan columns of spades, secateurs, and saws without decorative interruption. Navigation sits in a dark-green band with white reversed type, product cards float on white with a single `{colors.hairline}` border, and the footer mirrors the nav in full #234600 density. The overall impression is institutional confidence — a brand that trusts its 260-year reputation over trend-chasing gradients.

colors:
  primary: "#234600"
  primary-light: "#bbee77"
  primary-active: "#1a3400"
  primary-disabled: "#8cab6e"
  accent-orange: "#ed541d"
  accent-orange-soft: "#fef5f1"
  accent-orange-dark: "#8c2e0b"
  ink: "#444444"
  body: "#3f3f3f"
  muted: "#aaaaaa"
  muted-soft: "#bbbbbb"
  hairline: "#dfdfdf"
  hairline-soft: "#ededed"
  border-strong: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-strong: "#f4f4f4"
  surface-warm: "#f8fff0"
  surface-alert: "#fffce5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  link: "#003399"
  link-hover: "#2a62bc"
  link-active: "#3948a4"
  focus-ring: "#5897fb"
  error: "#ff0000"
  warning-bg: "#ffffdd"
  star-rating: "#eedd55"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Times New Roman', Georgia, serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Times New Roman', Georgia, serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Baskerville, 'Times New Roman', Georgia, serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Verdana, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Verdana, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  breadcrumb:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Verdana, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  mono:
    fontFamily: "monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
  button-primary-hover:
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
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: 2px solid {colors.primary}
  button-secondary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-accent:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 42px
    border: 1px solid {colors.border-strong}
    focusBorder: 2px solid {colors.focus-ring}
  text-input-error:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 2px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: 0 {spacing.lg}
  nav-bar-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.12)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 360px
  hero-banner-light:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 360px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline}
    hoverBorder: 1px solid {colors.primary-light}
    boxShadow: none
    hoverBoxShadow: "0 2px 8px rgba(35,70,0,0.08)"
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.primary}"
  category-card:
    backgroundColor: "{colors.surface-strong}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    minHeight: 180px
  sale-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  breadcrumb-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.breadcrumb}"
    padding: "{spacing.sm} {spacing.lg}"
    linkColor: "{colors.link}"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 40px 10px 12px
    height: 42px
    border: 2px solid {colors.primary}
    iconColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    linkColor: "{colors.primary-light}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.md}"
  star-rating:
    filledColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: "{spacing.xxs}"
  alert-banner:
    backgroundColor: "{colors.surface-alert}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
    border: 1px solid {colors.star-rating}
  sidebar-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"
    border: 1px solid {colors.hairline-soft}
    headingTypography: "{typography.title-sm}"
  tooltip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"

---

## Components

### Buttons

**`button-primary`** — A squared-off, dark-green button with white uppercase text at 14px bold. Hover deepens the green to `{colors.primary-active}`; disabled state fades to a sage `{colors.primary-disabled}` while keeping white text legible. The 4px radius (`{rounded.xs}`) gives a utilitarian, mechanical feel — these are tool-buying buttons, not lifestyle-brand pills.

**`button-secondary`** — White fill with a 2px green border and green uppercase label. On hover, the fill inverts to solid green with white text, creating a decisive snap rather than a gradual transition. Used for secondary actions like "View Range" or "Compare Products."

**`button-accent`** — Reserved for sale CTAs and time-limited promotions. The orange (#ed541d) demands attention against the otherwise green-and-gray palette. Same squared geometry as primary.

### Navigation

**`nav-bar`** — A full-width dark-green (#234600) bar at 56px height. White navigation links in bold 14px Arial sit evenly spaced; dropdown menus appear on white cards with subtle shadow (`nav-bar-dropdown`). The green band is the single strongest brand signal on every page.

**`breadcrumb-bar`** — A soft-gray ribbon below the nav showing category hierarchy. Text in 12px muted gray; links in the brand navy (#003399) with hover underline. Provides orientation across deep product taxonomies (Garden > Digging > Spades > Stainless Steel).

### Product Display

**`product-card`** — White card with a 1px gray hairline border. Image sits in a 4:3 container with light-gray background for loading state. Title in bold 16px, price in bold 18px green. On hover, the border shifts to lime (#bbee77) and a faint green-tinted shadow appears — enough to signal interactivity without disrupting grid rhythm.

**`category-card`** — Larger card for range browsing (Digging, Cutting, Raking). Gray fill with bold title, often overlaid on a cropped product silhouette. 8px radius softens the otherwise angular system just enough for category-level warmth.

**`sale-badge`** — Small orange pill overlaid on product-card images. White uppercase text at 11px bold. Positioned top-right with 8px inset from card edges.

**`new-badge`** — Lime-green background with dark-green text. Same dimensions as sale-badge but lower visual urgency — signals newness without implying a discount.

### Search

**`search-input`** — A prominent input with 2px green border, distinguishing it from standard form fields. Search icon in brand green sits right-aligned. Placeholder text in `{colors.muted}`. Focus state adds the blue ring (#5897fb) familiar from browser defaults — no custom focus styling overrides accessibility.

### Hero

**`hero-banner`** — Full-width dark-green section used on landing pages. White display text in Baskerville at 36px creates a heritage-catalogue feel. Minimum 360px height with generous vertical padding (`{spacing.section}`). Product photography bleeds to edge or sits in a right-aligned composition.

**`hero-banner-light`** — Alternate hero using the faint-green surface (#f8fff0). Dark text on light background for seasonal promotions and softer campaigns. Same dimensions and typography as the standard hero.

### Footer

**`footer`** — Mirrors the nav in full dark-green density. Content organised in columns: product ranges, support links, company info. Headings in bold 16px white; links in lime-green (#bbee77) for contrast. Social icons in white at 20px. Generous 48px vertical padding gives the footer visual weight matching the nav bar.

### Supporting Elements

**`star-rating`** — Gold (#eedd55) filled stars with gray empties. Used on product cards and detail pages. 16px size with 2px gap keeps them legible at product-grid scale.

**`alert-banner`** — Pale-yellow background with gold border for stock warnings, delivery notices, and seasonal messages. Body-small text in ink keeps urgency proportional.

**`sidebar-filter`** — White panel with soft border, used on product listing pages. Filter group headings in bold 16px; individual options in 13px body text with checkboxes. Collapse/expand interaction on mobile.

**`tooltip`** — Dark-gray (#444444) background with white caption text. Appears on icon-only actions (wishlist, compare). 4px radius matches the overall tight-corner system.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger menu with slide-out panel; hero reduces to 240px height; sidebar filters move to a full-screen overlay triggered by "Filter" button; footer stacks to single column |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links with dropdown on tap; hero maintains 320px height; sidebar filters sit above product grid as collapsible accordions |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with dropdowns on hover; sidebar filters pinned left at 240px width; hero at full 360px+ height |
| Wide | > 1440px | Content max-width caps at 1440px and centers; product grid may extend to five columns; increased horizontal padding (`{spacing.xxl}`) keeps content from stretching uncomfortably |

### Touch Targets

- All interactive elements maintain minimum 44×44px touch area on mobile and tablet
- Product card entire surface is tappable, not just the title link
- Filter checkboxes use 44px row height with full-width tap target
- Nav hamburger icon sits in a 48×48px hit area with 16px margin from screen edge
- Close buttons on overlays use 48×48px targets positioned top-right

### Collapsing Strategy

- Navigation: full horizontal links → hamburger + slide-out drawer below 744px
- Product grid: 4-col → 3-col → 2-col → 1-col as viewport narrows
- Sidebar filters: pinned left panel → above-grid accordions → full-screen overlay
- Hero text: display-xl (36px) → display-md (28px) below 744px; image may shift to below-text stacking
- Footer columns: 4-across → 2×2 grid → single stack
- Breadcrumbs: full path shown on desktop; truncated to "… > Parent > Current" on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom web font detected — the site relies on system-available Baskerville and Arial/Verdana; actual font files may load via JS or a CMS theme layer not captured in static extraction
- Many extracted blues (#3875d7, #0072b9, #5897fb) appear to be Drupal CMS admin/form defaults rather than brand tokens — included as `{colors.focus-ring}` and `{colors.link}` but may not reflect intentional brand decisions
- No motion/animation tokens extracted — transition durations, easing curves, and hover animations are undetermined
- Icon system not captured — product category icons and UI glyphs may use an icon font or SVG sprite not visible in color/font extraction
- Exact grid gutter widths and container max-widths could not be confirmed from color/font data alone
- No dark-mode variant detected or documented
- The #ff0000 pure red likely serves as a form-validation error color from the CMS rather than a branded token
