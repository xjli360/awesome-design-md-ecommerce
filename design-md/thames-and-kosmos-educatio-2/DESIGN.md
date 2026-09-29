---
version: alpha
name: "Thames & Kosmos"
source_url: "https://www.thamesandkosmos.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Four accent colors — orange (#f89406), red (#bd362f), grass-green (#51a351), and teal (#2f96b4) — organize the Thames & Kosmos catalog the way a periodic table indexes elements: each hue maps to a subject family or age band, working as a functional taxonomy rather than emotional decoration. The sky-blue primary (#2bbaf4) that runs headers and CTAs sits conspicuously lighter than the deep institutional navy most STEM education brands default to, reading closer to a lit indicator lamp than a corporate identity color — energetic without tipping into toy-store primary. Deep navy (#0044cc, #002a80) is not the hero here; it anchors the navigation bar and footer as a dark frame that makes the bright accent spectrum read cleanly against the near-white canvas (#fbfbfb).

  Thames & Kosmos makes no investment in custom typefaces — the entire interface runs on Arial, Helvetica, sans-serif, an unusually utilitarian commitment for a brand whose kit packaging overflows with illustrated characters and colorful diagrams. The restraint is purposeful: box photography and illustrated catalog art carry visual personality, while the type layer stays flat and scannable for a parent comparing reading-level suitability across a dozen products. Display headlines step through 700-weight Arial at 28–36px; titles hold at 600-weight at 16–20px; body copy reads at 16px weight 400. Nothing in the type system asks for attention — it organizes.

  Geometry stays soft without crossing into toy-store territory: {rounded.sm} (8px) on buttons and inputs, {rounded.md} (12px) on product cards, and {rounded.full} pills reserved for age-range badges and category filter chips — the one place the brand leans fully playful. A kit-specs strip below each product title (piece count, age range, skill level, subject tag) is a brand-signature information layer that converts the product card promise into structured spec detail before the customer reaches the full description. The overall logic is an instrument panel — organized grids, color-coded taxonomy, utilitarian type — designed for the comparison-shopping parent, not the browsing child.

colors:
  primary: "#2bbaf4"
  primary-active: "#0088cc"
  primary-disabled: "#d1e3fb"
  accent-orange: "#f89406"
  accent-orange-active: "#ad6704"
  accent-orange-soft: "#fbb450"
  accent-red: "#bd362f"
  accent-red-soft: "#ee5f5b"
  accent-green: "#51a351"
  accent-green-soft: "#62c462"
  accent-teal: "#2f96b4"
  accent-teal-soft: "#5bc0de"
  navy: "#0044cc"
  navy-mid: "#003399"
  navy-deep: "#002a80"
  ink: "#222222"
  body: "#444444"
  muted: "#a2a2a2"
  hairline: "#e6e6e6"
  hairline-soft: "#edebeb"
  canvas: "#fbfbfb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.25px
    textTransform: uppercase
  age-label:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 10px
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.navy}"
    border: "2px solid {colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocused: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocused: "2px solid {colors.primary}"
    iconColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: 12px
    imageAspectRatio: "1/1"
  age-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-badge-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-badge-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-badge-teal:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.navy}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    padding: 24px 16px
  hero-banner:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: 64px 48px
  kit-specs-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    padding: 12px 16px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: 48px 0

## Components

### Buttons

**`button-primary`** — Sky-blue (#2bbaf4) fill with white uppercase Arial at 14px/700, 8px radius, 44px tall. On hover the background transitions to #0088cc; the disabled state washes to #d1e3fb while keeping white text. Used for "Add to Cart," "Shop Now," and all category-entry CTAs throughout the catalog.

**`button-secondary`** — White canvas background with a 2px #0044cc navy border and matching navy text, designed to pair with button-primary where two actions share equal weight on a product page (for example, "Add to Cart" alongside "View Kit Contents"). Hover deepens the border to #002a80 and matches the text.

**`button-ghost`** — Transparent fill with a 2px #2bbaf4 border and primary-blue text label, reserved for less prominent actions such as secondary filter triggers or "Learn More" links in content-heavy layouts where a solid fill would add visual noise.

### Forms

**`text-input`** — White background with a 1px #e6e6e6 hairline border and 8px radius. On focus the border upgrades to a 2px #2bbaf4 ring. Runs body-md Arial at 16px for comfortable adult readability; at 44px tall it aligns with button height for clean inline form rows. Placeholder text in muted #a2a2a2.

**`search-bar`** — Matches text-input geometry but carries a right-aligned magnifier icon rendered in #a2a2a2. On desktop it sits inline within the nav-bar at a compact 40px height; on mobile it expands to a full-width overlay with the same hairline border and focus ring.

### Navigation

**`nav-bar`** — Deep navy (#002a80) masthead at 60px tall, with the Thames & Kosmos logo at left, white 600-weight 15px nav-links spanning subject categories, and a search icon plus cart badge at right. The navy background provides the horizontal band without requiring a border. Category hover states surface a dropdown on a white background with a navy-deep top accent line.

### Cards & Tiles

**`product-card`** — White surface-card with a subtle #e6e6e6 hairline border and 12px radius. A square product image (1:1 aspect ratio) fills the top zone, followed by a category badge, product title in title-sm, price in body-sm, and an age-badge pill positioned at the image corner. Desktop grids run four columns; mobile reduces to two.

**`age-badge`** — Orange (#f89406) pill with white uppercase badge-style Arial at 11px/700. This is the primary age-range marker; it appears on product cards, PDPs, and search-result chips. Orange functions as the default badge hue when a product spans multiple age ranges and serves as the most immediately scannable color in the full badge family.

**`category-badge-red`**, **`category-badge-green`**, **`category-badge-teal`** — Sister variants to age-badge using #bd362f, #51a351, and #2f96b4 respectively, each coding a distinct product family (physics/chemistry, biology/ecology, and engineering/electronics by convention). All share the same {rounded.full} geometry and badge typography with white text throughout.

**`category-tile`** — A soft-gray (#f5f5f5) card with #e6e6e6 border and 12px radius, title-md in #0044cc navy. Used on the category browse grid to let shoppers navigate by subject. Tiles typically carry an illustrated product-family icon or a cropped kit image above the text label.

**`hero-banner`** — Full-width deep-navy (#002a80) strip with a display-xl white headline, body-md subtitle, and a button-primary CTA. Top and bottom padding is 64px to give the content room to breathe. The banner background may accept a low-opacity overlay of kit components or lab equipment photography as a secondary visual layer.

### Product Detail

**`kit-specs-strip`** — A lightly ruled horizontal band in surface-soft (#f5f5f5) that runs immediately below the product title on PDPs. Columns surface piece count, recommended age, skill level, and subject tag — each as a caption label above a body-sm value. This brand-signature strip converts the product card promise into structured spec data before the buyer reaches the full long-form description, reducing scroll and cognitive load for comparison shoppers.

### Utility

**`breadcrumb`** — Muted #a2a2a2 body-sm text for ancestor nodes, ink #222222 for the active page, forward-slash separator. Sits above the product title on PDP and category landing pages to help parent shoppers maintain catalog context.

**`footer`** — Navy-deep (#002a80) background with white body-sm copy organized in four columns: shop categories, learning resources, company information, and newsletter signup. Column headings use title-sm in white. Link color is white at rest and shifts to primary #2bbaf4 on hover, reinforcing the primary hue as the single interactive signal color throughout the site.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; search expands to full-width overlay; hero-banner headline drops to display-md and padding reduces to 24px; age-badge moves below product image |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links only with sub-categories behind a tap; hero uses display-md rather than display-xl |
| Desktop | 1128–1440px | Four-column product grid; full nav-bar with hover dropdowns; hero at display-xl; kit-specs-strip shows all spec columns inline |
| Wide | > 1440px | Content columns cap at 1440px max-width and center; hero image bleeds to viewport edge while headline and CTA stay within the content bounds |

### Touch Targets

- button-primary and button-secondary are 44px tall, meeting WCAG 2.5.5 minimum on touch
- Category tiles padded to a minimum 48px tap height on mobile
- Nav hamburger icon and cart icon both at 44×44px minimum hit area
- Age and category badges are informational on cards; the full card surface acts as the tap target via an anchor overlay

### Collapsing Strategy

- Nav mega-menu collapses to a full-height side drawer on mobile with accordion sub-categories
- Kit-specs-strip reduces to two visible columns on mobile with a "Show all specs" expand trigger revealing the remainder
- Product grid steps 4→2→1 columns at desktop→tablet→mobile breakpoints
- Hero headline, subtitle, and CTA remain single-column at all widths; only font size and padding reduce
- Footer four-column grid stacks to single column on mobile; newsletter form anchors at the bottom of the stacked layout

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom typeface detected — the full site runs on Arial, Helvetica, sans-serif; brand kit packaging likely uses a licensed or proprietary display face not surfaced via stylesheet
- Meta theme-color is absent; mobile status-bar color cannot be confirmed (navy-deep #002a80 is inferred from nav background observation)
- Category-to-color mapping is inferred from the extracted accent spectrum — actual product-family assignments require navigation audit of the live catalog
- Button and card border-radius values are approximations from the extracted palette context; pixel-exact values require live DevTools inspection
- Shadow and elevation tokens (card drop-shadow, nav-bar scroll shadow) were not detectable from color/font extraction and are omitted
- Dark-mode support is unknown — no evidence of prefers-color-scheme media queries in extraction
- Icon set style (outlined vs. filled, stroke weight) and category-tile illustration system not characterizable from color and font data alone
