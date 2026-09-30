---
version: alpha
name: "Sphero"
source_url: "https://www.sphero.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Electric cyan (#18acf2) is the engine of Sphero's visual identity — not a background utility color but a live voltage that fires at every primary CTA, navigation hover, and icon stroke against near-black canvases (#121212), where the contrast reads like the glow ring of a Sphero BOLT mid-roll. Four secondary voltages partition the product ecosystem without losing coherence: lime green (#78d318) marks curriculum and app-integration tiers, coral red (#f54055) flags urgency and alert states, deep purple (#5f249f) anchors advanced CTE product lines, and hot pink (#e94194) appears in promotional and campaign contexts — all held in check by the dark base canvas so high-chroma neighbors coexist rather than collide. Montserrat Black locks display headers into all-caps, wide-tracked wordmarks engineered to read from the back of a classroom or across a gymnasium floor during a robot demo; Roboto takes the continuous prose of curriculum descriptions and educator guides at weights that prioritize scanning speed over personality. The corner language is deliberately stratified: category selector pills push toward {rounded.full} to signal interactivity, product cards use {rounded.md} for a contained grid treatment, and primary CTA buttons settle at {rounded.sm} to read as technical controls rather than soft consumer-app affordances. Material Symbols Outlined icons position Sphero inside the Google Workspace for Education ecosystem — a deliberate signal to district IT administrators evaluating classroom integrations. Amber (#ffb81c) surfaces in star ratings and promotional callouts, and the full palette — cyan, lime, red, purple, pink, amber against near-black — operates with the calibrated intensity of a robot demonstration: maximum legibility under projector light, maximum energy without visual chaos. The PK–12 grade-level system manifests not in cartoon illustration but in a tight badge vocabulary stamped directly onto product cards, letting educators identify curriculum fit in a single glance without opening a product page.

colors:
  primary: "#18acf2"
  primary-active: "#0a7db3"
  primary-disabled: "#aadddd"
  ink: "#121212"
  body: "#212121"
  muted: "#8a9297"
  muted-soft: "#abb1b4"
  hairline: "#d4d6d8"
  hairline-soft: "#e1e3e4"
  canvas: "#ffffff"
  canvas-dark: "#121212"
  surface-soft: "#e1e3e4"
  surface-card: "#252525"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#f54055"
  accent-lime: "#78d318"
  accent-purple: "#5f249f"
  accent-pink: "#e94194"
  accent-amber: "#ffb81c"

typography:
  display-xl:
    fontFamily: "'Montserrat Black', Montserrat, Roboto, sans-serif"
    fontSize: 56px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Montserrat Black', Montserrat, Roboto, sans-serif"
    fontSize: 40px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: -0.3px
    textTransform: uppercase
  display-md:
    fontFamily: "Montserrat, Roboto, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "Montserrat, Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "Montserrat, Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Montserrat, Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "Montserrat, Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Montserrat, Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "Montserrat, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  grade-label:
    fontFamily: "Montserrat, Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  eyebrow:
    fontFamily: "Montserrat, Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "Montserrat, Roboto, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    border: "2px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    typography: "{typography.body-md}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.surface-card}"
    activeAccent: "{colors.primary}"
  nav-bar-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    activeAccent: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    hoverBorder: "2px solid {colors.primary}"
  hero-banner:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: 80px
    paddingHorizontal: "{spacing.xl}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
  grade-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.grade-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  grade-badge-purple:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.grade-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  grade-badge-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.grade-label}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  category-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    border: none
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    height: 40px
  eyebrow-label:
    textColor: "{colors.primary}"
    typography: "{typography.eyebrow}"
    backgroundColor: transparent
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    iconColor: "{colors.primary}"
    typography: "{typography.body-md}"
    focusBorder: "2px solid {colors.primary}"
  robot-spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.md}"
    headerTypography: "{typography.title-sm}"
    headerColor: "{colors.muted-soft}"
    bodyTypography: "{typography.body-sm}"
    rowDivider: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  promo-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.grade-label}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  section-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  section-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.body}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary}"
    dividerColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — Filled electric cyan (#18acf2) at 48px height with white Montserrat 700 uppercase text at 15px/0.5px tracking and {rounded.sm} corners. Hover and active states deepen to {colors.primary-active} (#0a7db3); disabled softens the fill to {colors.primary-disabled} (#aadddd). This button handles all primary purchase CTAs — "Shop Now", "Add to Cart", "Start Learning" — and appears on both dark and light canvas sections since the cyan reads with sufficient contrast on both.

**`button-secondary`** / **`button-secondary-dark`** — Transparent fill, 2px border, matching 48px height and uppercase Montserrat 700 typography for visual pairing with the primary button. On white-canvas sections the border and label are {colors.primary}; on dark-canvas sections the `button-secondary-dark` variant switches to white border and white label. Ghost variant (`button-ghost`) uses underlined white text with no fill or border, reserved for inline contextual actions such as "Learn More" in dense content blocks.

### Navigation

**`nav-bar`** — 64px bar in {colors.canvas-dark} that sits above hero sections on the dark-primary page layout. Nav links are 14px Montserrat 600 in {colors.on-dark}; the active item receives a {colors.primary} underline accent. A light variant (`nav-bar-light`) serves white-canvas interior pages (educator resources, support) with dark ink links and a {colors.hairline} bottom border. The bar is sticky on scroll; it does not add a blur or transparency layer — it stays fully opaque to preserve readability against motion content beneath.

### Product Card

**`product-card`** — Dark-surface card ({colors.surface-card}, #252525) with {rounded.md} corners and {spacing.lg} internal padding. The image lockup occupies a 4:3 ratio slot at card top using `object-fit: cover`. Title renders in {typography.title-md} at {colors.on-dark}; pricing uses {typography.price-display} (20px Montserrat 700) below the title. Grade badges — {grade-badge} in cyan, {grade-badge-purple} in deep purple, {grade-badge-lime} in lime — overlay the image top-left to communicate grade-level curriculum fit immediately. On hover, a 2px {colors.primary} border traces the card perimeter without changing the fill, keeping hover feedback precise and contained.

### Hero Banner

**`hero-banner`** — Full-bleed dark section ({colors.canvas-dark}) opening every major product or curriculum landing page. The eyebrow label ({typography.eyebrow} in {colors.primary}) anchors the section to a category before the headline fires in {typography.display-xl} — Montserrat Black, uppercase, 56px, tight leading. Supporting body copy sits below in {typography.body-md} at 16px Roboto. A primary CTA button aligns left below the copy. When photography or a robot render occupies the right column on desktop, a 40% opacity dark gradient scrim ensures the white headline remains legible across all image brightness levels.

### Grade Badges

**`grade-badge`** / **`grade-badge-purple`** / **`grade-badge-lime`** — A three-badge vocabulary encoding Sphero's PK–12 grade-band system. Blue (#18acf2) covers elementary and primary grades; deep purple (#5f249f) marks middle-school and CTE advanced tracks; lime (#78d318) with dark ink text flags programming and app-integration curriculum. All three use {rounded.xs}, 11px Montserrat 700 uppercase at +0.8px tracking, and 4px × 8px padding. Badges stack or sit in a horizontal row on product cards and curriculum category pages; they never appear in isolation — they always accompany a product name or grade-range label.

### Category Chips

**`category-chip`** / **`category-chip-active`** — Pill-shaped selectors ({rounded.full}) arranged in a horizontal filter rail above product grids and curriculum tables. Default state: dark card fill ({colors.surface-card}), 1px {colors.hairline} border, white 13px Montserrat 700 uppercase label. Active state fills with {colors.primary}, drops the border, and sets label to {colors.on-primary}. Chip labels include "Coding", "STEM", "AI Literacy", "Robotics", "CTE", "K–2", "3–5" and so on. On mobile the rail scrolls horizontally rather than wrapping.

### Eyebrow Labels

**`eyebrow-label`** — 12px Montserrat 700 uppercase in {colors.primary} with 1.5px letter spacing and no background. Appears above every major section headline as a curriculum or product tier anchor (e.g., "PK–12 EDUCATION", "AI LITERACY", "CTE PATHWAYS"). The pattern is consistent enough across the site to function as a structural rhythm cue: wherever an eyebrow appears, a large display headline and a supporting body paragraph follow in a predictable three-tier stack.

### Search Bar

**`search-bar`** — Pill-form search input ({rounded.full}) on a dark surface (#252525) with 12px vertical and 20px horizontal padding. A {colors.primary} Material Symbols Outlined magnifier icon anchors the left end. Placeholder text sits in {colors.muted}; on focus, a 2px {colors.primary} ring traces the pill without changing the background fill. The search bar appears in the top navigation on smaller breakpoints and as an inline search field on curriculum browse pages.

### Robot Spec Table

**`robot-spec-table`** — Dark card ({colors.surface-card}) with {rounded.md} used in product detail pages to present battery life, connectivity standard, waterproofing rating, and recommended age range in a two-column labeled grid. Row headers render in {typography.title-sm} at {colors.muted-soft}; values render in {typography.body-sm} at {colors.on-dark}. Rows are separated by 1px {colors.hairline} dividers. On mobile this component collapses to a single-column stacked list with the label above the value.

### Promo Badge

**`promo-badge`** — Amber (#ffb81c) badge with dark ink text ({colors.ink}), {rounded.xs}, grade-label typography (11px/700/+0.8px tracking). Used for "SALE", "NEW", and star-rating callout chips on product cards and in promotional hero blocks. The amber makes it visually distinct from the grade badges (cyan/purple/lime) so educators can separate curriculum information from commercial promotions at a glance.

### Footer

**`footer`** — Dark charcoal (#212121) base with white body text and {colors.primary} link accents. Organized into four label-list columns: Shop, Educators, Support, Company. Column headings use {typography.title-sm}; link items use {typography.body-sm}. Social icons render in {colors.muted-soft} and brighten to {colors.on-dark} on hover. A bottom bar below a 1px {colors.surface-card} divider carries copyright and legal links in {typography.caption} at {colors.muted}.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline scales to display-md (32px); nav collapses to hamburger drawer; category chip rail scrolls horizontally; grade badges stack vertically above card title |
| Tablet | 744–1128px | Two-column product grid; hero headline at display-lg (40px); nav shows top-level items with overflow drawer for sub-categories; chip rail fully visible |
| Desktop | 1128–1440px | Three to four-column product grid; full nav with mega-menu dropdowns; hero at display-xl (56px) with side-by-side text and product image |
| Wide | > 1440px | Content container capped ~1400px and centered; hero background bleeds full viewport width; product grid may reach five columns |

### Touch Targets
- All buttons minimum 48×48px
- Category chip pills minimum 40px tall
- Nav links expand to 44px touch target height in the mobile drawer
- Product card tap target covers the full card surface via a single wrapping anchor

### Collapsing Strategy
- Mega-menu nav collapses to a full-height slide-in drawer at < 1128px
- Hero CTA pair (primary + secondary) stacks vertically at < 480px
- Robot spec table converts from a two-column grid to a single-column labeled list on mobile
- Grade badge rows wrap to two lines rather than truncating; badge text never clips
- Footer four-column layout reduces to two columns at tablet, one column at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Montserrat vs Montserrat Black usage breakpoints across heading hierarchy not extracted — weight assignments are inferred from brand conventions
- Nav-bar height (64px) is estimated; scroll-triggered transparency-to-opaque transition behavior and timing not confirmed
- Hero section gradient scrim opacity values not extracted — dark overlay assumed at 40–60%
- Social platform colors (#3b5998 Facebook, #1da1f2 Twitter/X, #bd081c Pinterest, #d83776 likely Instagram gradient) appear in the extracted palette and may be social-icon fills rather than brand design tokens
- Amber (#ffb81c) context not fully confirmed — may be restricted to star ratings or may extend to broader promotional badge usage
- No explicit elevation or box-shadow tokens extracted; card hover shadow values are inferred
- Dark-to-light section transition treatment (hard cut vs. gradient bleed) not determinable from color extraction
- Exact grid gutter width and max-content-width container value not confirmed
