---
version: alpha
name: "Printful"
source_url: "https://www.printful.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The most revealing thing about Printful's palette is that its cobalt — `#003399`, a blue with almost no green contamination that reads closer to a university crest or heraldic seal than any typical SaaS product blue — shares the same design system with a cluster of fabric-sample warm neutrals: blush `#f4e3d9`, sand `#e6bda1`, muted khaki `#d0cdac`. That thermal opposition is the core brand signal. Printful is an industrial fulfillment platform that presents in the visual register of a design studio, and the palette is where the two identities negotiate. The single extracted font stack — ProximaNova-Extrabld — tells the same story from the typographic side: display headings run at extra-bold weight not as a gesture toward editorial refinement but as a frank declaration of production capability. Print fulfillment companies sell confidence in execution, and 800-weight type does the same work a bold guarantee seal does on a shipping label. The near-black navy `#03253d` serves as the ink anchor, keeping the entire system in the blue family even at its darkest end rather than slipping into neutral black. A deep teal `#003d3d` appears as a secondary surface and CTA color — pulling green into the cool temperature range for the first time, giving the system a second axis of authority distinct from the cobalt. Rounded corners are applied with restraint: buttons sit at a small 6px radius, cards at 12–16px, full-pill reserved only for search inputs and filter chips. Hero architecture is conversion-direct — high-contrast headline, single primary CTA in cobalt, a secondary outline button for alternative paths — because the product is invisible until it is printed. The design system must carry photography trust signals (lifestyle mockups of apparel, mugs, posters in use) and deliver a frictionless store-connection flow in the same breath. Surface colors do structural work: blush `#f4e3d9` containers provide warm contrast for transparent product PNG mockups; blue-mist `#c3d7e0` frames social proof stats; sand `#e6bda1` gives full-width editorial banners a material warmth that plain white cannot.

colors:
  primary: "#003399"
  primary-active: "#002580"
  primary-disabled: "#99aed6"
  primary-teal: "#003d3d"
  primary-teal-active: "#002929"
  ink: "#03253d"
  body: "#323841"
  muted: "#6b7280"
  muted-soft: "#9ca3af"
  hairline: "#e7e6e7"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f4e3d9"
  surface-warm: "#e6bda1"
  surface-khaki: "#d0cdac"
  surface-blue-mist: "#c3d7e0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  success: "#16a34a"
  error: "#dc2626"
  warning: "#d97706"

typography:
  display-xl:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 52px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 40px
    fontWeight: 800
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 32px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Proxima Nova', ProximaNova, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Proxima Nova', ProximaNova, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Proxima Nova', ProximaNova, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  label-sm:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'ProximaNova-Extrabld', 'Proxima Nova', sans-serif"
    fontSize: 22px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: -0.3px

rounded:
  none: 0px
  xs: 4px
  sm: 6px
  md: 12px
  lg: 16px
  xl: 24px
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    transition: background-color 150ms ease
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 48px
  button-secondary-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.on-dark}"
    padding: 12px 26px
    height: 48px
  button-teal:
    backgroundColor: "{colors.primary-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "1/1"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    textColor: "{colors.ink}"
    captionColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    ctaGap: "{spacing.sm}"
  hero-warm:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    subheadTypography: "{typography.body-md}"
    paddingVertical: "{spacing.xxl}"
  feature-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    border: "1px solid {colors.hairline}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    textColor: "{colors.ink}"
    captionColor: "{colors.muted}"
  feature-card-teal:
    backgroundColor: "{colors.primary-teal}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
  stat-card:
    backgroundColor: "{colors.surface-blue-mist}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    valueTypography: "{typography.display-md}"
    labelTypography: "{typography.caption}"
    textColor: "{colors.ink}"
  pricing-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    priceTypography: "{typography.display-sm}"
    labelTypography: "{typography.label-sm}"
    bodyTypography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  pricing-card-featured:
    backgroundColor: "{colors.primary}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"
    priceTypography: "{typography.display-sm}"
    labelTypography: "{typography.label-sm}"
    bodyTypography: "{typography.body-sm}"
    textColor: "{colors.on-primary}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-free:
    backgroundColor: "{colors.success}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  category-chip:
    backgroundColor: "{colors.surface-blue-mist}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  section-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.xxl}"
    rounded: "{rounded.none}"
  cta-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    paddingVertical: "{spacing.xl}"
  mockup-preview:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.lg}"
    border: "none"
    padding: "{spacing.lg}"
    imageAspectRatio: "4/3"
  progress-step:
    activeColor: "{colors.primary}"
    completedColor: "{colors.primary-teal}"
    inactiveColor: "{colors.hairline}"
    labelTypography: "{typography.caption-bold}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    paddingVertical: "{spacing.section}"
    dividerColor: "rgba(255,255,255,0.12)"

## Components

### Buttons

**`button-primary`** — The main conversion driver on every Printful page. Filled with cobalt `#003399`, white text in ProximaNova-Extrabld at 16px, 6px corner radius, 48px tall. Hover state deepens to `#002580`; disabled washes to `#99aed6`. Used for "Start for free", "Get started", and checkout confirmation actions — appears in both the top nav and every hero section.

**`button-secondary`** — White background with a 2px cobalt border and cobalt text, identical sizing to `button-primary`. Conveys equal visual weight without dominating the CTA hierarchy. Commonly paired alongside `button-primary` as "Compare plans", "See all products", or "Learn more".

**`button-secondary-dark`** — Transparent fill with 2px white border and white text. Used exclusively on dark hero sections over `#03253d` or full-bleed photography backgrounds where a cobalt fill would compete with the background. Maintains contrast without a colored surface.

**`button-teal`** — Fills with deep teal `#003d3d`. Marks Printful's secondary brand territory — appears on sustainability modules, partner story sections, and brand mission callouts where the cobalt reads too transactional. Used sparingly: one per page section maximum.

**`button-ghost`** — Transparent with ink text at 14px/700. Used inline in product configurator panels, filter drawers, and modal footers for low-priority actions like "Reset filters" or "Cancel".

### Navigation

**`nav-bar`** — 64px tall, white background, 1px `#e7e6e7` bottom border. Logo in cobalt `#003399`. Nav links in ProximaNova-Extrabld at 15px in ink. Product-category dropdowns open on hover with blush `#f4e3d9` panel surfaces behind the subcategory grids. A `button-primary` "Get started" CTA lives at the far right. Collapses to a hamburger icon below 744px.

**`nav-bar-dark`** — Full `#03253d` fill, white links, same proportions. Used on marketing landing pages that open with photography heroes, where the standard white nav would create a harsh light edge against a dark image.

### Forms

**`text-input`** — 44px height, 6px radius, 1px `#e7e6e7` border at rest, 1px cobalt on focus. ProximaNova regular at 16px. Applied across contact forms, store-name fields, product customization inputs, and Shopify integration setup flows.

**`search-bar`** — Full-pill variant (`{rounded.full}`) of the input field, 44px tall. Used specifically for the product catalog search bar above category grids. The pill radius signals search intent, softening the otherwise structured column grid and providing visual contrast to the card grid below.

### Cards

**`product-card`** — White card with 1px `#e7e6e7` border, 12px radius, 16px padding, 1:1 image at top. Product name in `title-sm`, price in the `price` scale (22px/800), subcategory in `caption` at muted gray. On hover, a shallow box-shadow lifts the card 2px. Forms the primary grid unit across all product category pages.

**`feature-card`** — 16px radius, 32px padding, white on a `#f0f0f0` section background. Headline at `title-md` (18px/700), body at `body-sm`. 40px icon slot in cobalt at top-left. Appears in three-column grids for "Why Printful" and platform capability sections.

**`feature-card-teal`** — Deep teal `#003d3d` fill version of the feature card. White text throughout. Used at a maximum of one tile per grid to create a visual anchor — its position in the grid is always deliberate (typically the second card in a three-card row to maintain scanning rhythm).

**`stat-card`** — Blue-mist `#c3d7e0` surface, 12px radius, 24px padding. Large metric in `display-md` (32px/800), descriptive label in `caption`. Used in social-proof rows: "1M+ active stores", "140+ products in catalog", "shipping to 190+ countries".

**`pricing-card`** and **`pricing-card-featured`** — Standard card is white with hairline border. Featured card fills with cobalt `#003399` and white text to mark the recommended plan. Both use `display-sm` for the price amount, `label-sm` (all-caps 12px) for plan names, and `body-sm` for the feature checklist rows. A checkmark icon in green `#16a34a` precedes each included feature.

**`mockup-preview`** — Blush `#f4e3d9` container with 16px radius and 24px padding, no border. Renders lifestyle and product mockup photography. The warm background color provides contrast for transparent product PNGs regardless of what color apparel or accessory is displayed — it reads as a studio lightbox surface.

### Hero Sections

**`hero`** — Full-bleed `#03253d` background, white headline at `display-xl` (52px/800), white subhead at `body-md`, horizontal CTA pair (`button-primary` + `button-secondary-dark`), 64px vertical padding. Used on the main homepage. On desktop, a product mockup image occupies the right half of the grid; on mobile, it stacks below the CTA.

**`hero-warm`** — Blush `#f4e3d9` background, ink text, `display-lg` headline (40px/800), 48px vertical padding. Appears on niche landing pages — "Print-on-demand for beginners", "Sell custom merch" — where the tone should feel accessible rather than enterprise-scale.

### Utility Components

**`badge-new`**, **`badge-sale`**, **`badge-free`** — Compact chips with 2×8px padding and 4px radius. All-caps 11px ProximaNova-Extrabld. Cobalt for new product additions, error red for discounts, success green for free shipping or trial callouts. Overlay at top-left of `product-card` image containers.

**`category-chip`** / **`category-chip-active`** — Blue-mist pill chips at rest, switching to cobalt fill and white text when active. `{rounded.full}`, `caption-bold` text at 13px. Used in the horizontal-scroll filter strip above category grids. The strip momentum-scrolls on mobile with visible overflow to signal scrollability.

**`section-banner`** — Full-width warm sand `#e6bda1` strip, no radius — bleeds edge to edge. `display-md` headline with `body-md` supporting text. Used for editorial callouts between feature sections: "Designed for creators", "No upfront costs". A single `button-secondary` CTA sits below the text, left-aligned on desktop, centered on mobile.

**`cta-strip`** — Full-width cobalt `#003399` band. `display-sm` white headline, `body-sm` supporting copy, single `button-secondary-dark` CTA. The standard page-bottom conversion zone directly above the footer.

**`progress-step`** — Step indicator for onboarding flows: store connection, product selection, mockup customization, shipping configuration. Active step is cobalt, completed step turns teal `#003d3d`, inactive steps are `#e7e6e7`. `caption-bold` labels sit below each node. Progress is horizontal on desktop, condensed to a numbered count ("Step 2 of 4") on mobile.

**`footer`** — `#03253d` background, white text, 64px vertical padding. Four-column grid with `label-sm` uppercase column headings and `body-sm` link rows. Logo renders white at far left of the top row. Social icon row and legal link row at the bottom separated by a semi-transparent white divider at 12% opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks headline → subhead → CTA pair vertically, mockup image drops below; nav collapses to hamburger full-screen drawer; product grid goes 2-up; category-chip strip scrolls horizontally with momentum; pricing cards stack 1-up with featured card rendered first; section padding reduces to `{spacing.xl}`; footer links collapse to accordion sections |
| Tablet | 744–1128px | 2-column feature-card grid; 3-up product card grid; nav shows primary links but condenses secondary dropdowns behind a "More" overflow; hero shrinks `display-xl` to 36px/800; pricing cards go 2-up; stat-cards in a 2×2 grid |
| Desktop | 1128–1440px | 4-up product grid; 3-column feature-card row; full nav with hover mega-menu dropdowns; hero at full `display-xl` in a two-column text-left/mockup-right layout; pricing cards 3-up in a centered 960px container |
| Wide | > 1440px | Content container caps at 1360px and centers; hero text column constrained to 640px while background bleeds full-width; product grid holds at 4-up with larger gutters; stat-card row switches to a single horizontal band with auto-spacing |

### Touch Targets

- All buttons minimum 44px tall on mobile
- Nav hamburger: 44×44px tap area
- Category-chip filter strip: chips minimum 36px tall, 12px horizontal gap
- Product card: entire card surface is a tap target including image area
- Footer accordion toggles: full row width, minimum 44px tap height
- Progress step nodes: 32px diameter minimum with extended invisible tap ring

### Collapsing Strategy

- Nav: Logo + hamburger at mobile; logo + condensed primary links + "Get started" at tablet; full mega-menu at desktop
- Hero: Two-column text/mockup layout at desktop → single-column centered at tablet → single-column with mockup image collapsed below CTA at mobile
- Feature grid: 3-col → 2-col → 1-col; `feature-card-teal` renders as full-width row at 1-col to preserve its visual anchor function
- Stat cards: 4-col horizontal band → 2×2 grid at tablet → 1-col stack at mobile
- Pricing: 3-col → 2-col → 1-col; featured card always renders first in DOM order for mobile scroll priority
- Footer: 4-col grid → 2-col at tablet → accordion at mobile; legal row always visible without expansion

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only the extra-bold weight variant of Proxima Nova was extracted; regular, semibold, and light weights are inferred from standard Proxima Nova family conventions but not confirmed from live extraction
- No meta theme-color extracted; mobile browser chrome color is unknown
- Exact button border-radius not confirmed via extraction — 6px is an estimate based on the overall soft-but-structured aesthetic signal
- Nav height (64px) is estimated; actual computed height was not captured
- The khaki surface color `#d0cdac` was extracted but no specific component assignment could be confirmed; it is included in the color tokens but not assigned to a named component
- Dark mode support is unknown — no dark-mode color tokens or media-query overrides found in extraction
- Icon library, glyph style (filled vs. outline), and icon sizing system not confirmed
- Animation easing curves and transition durations not extracted
- Exact responsive typography scaling breakpoints not confirmed; sizes in this spec are estimated from standard ProximaNova usage patterns at each breakpoint
