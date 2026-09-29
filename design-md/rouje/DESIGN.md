---
version: alpha
name: "Rouje"
source_url: "https://rouje.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Jeanne Damas built Rouje's digital canvas around a tension most French fashion brands sidestep: a warm cream ground (#fbf7f3) interrupted by a deep botanical teal (#108474) that carries every primary CTA, active indicator, and hover fill — a color that sits somewhere between verdigris metalwork and sea glass, entirely at odds with the blush-and-ivory palette the category expects. The site's declared mission — "une allure féminine et sensuelle" — finds its visual proof not in ornament but in restraint: soft gray neutrals (#eeeeee, #dedede, #dadada) layer over the cream like natural linen at different distances, while a reserved burgundy (#a91c2a) surfaces on sale states and discount callouts with old-world precision. The near-black (#0f0f0f, #121212) carries all editorial text at full weight, with #7b7b7b absorbing secondary labels and metadata without competing for attention. Surface depth is built through color temperature — cool near-white (#f9fafb) card backgrounds read as recessed against the warm canvas, eliminating the need for drop shadows. A pale teal wash (#edf5f5) appears behind trust signals and filter drawers, extending the primary hue into ambient territory. Rounded values are deliberately conservative — inputs and buttons carry gentle {rounded.sm} curves rather than the pill geometry dominant in wellness or beauty DTC, keeping the reference close to tailored clothing rather than cosmetic packaging. Because the live build delivers fonts through a JS bundle that defeats static extraction (only the Judge.me review widget glyph 'JudgemeStar' surfaced), precise type metrics are reconstructed from visual observation: display headings suggest a fine-weight serif set at generous sizes with open tracking, body copy resolves to a neutral grotesque. Product photography dominates every viewport from the first scroll — imagery is wide, unhurried, and lit like editorial rather than e-commerce. The teal stays the single unexpected signature: one botanical note pressed between pages of cream and shadow.

colors:
  primary: "#108474"
  primary-active: "#0a6860"
  primary-disabled: "#82bdb5"
  accent-red: "#a91c2a"
  accent-red-soft: "#f5e0e2"
  teal-wash: "#edf5f5"
  ink: "#0f0f0f"
  body: "#121212"
  muted: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  hairline-faint: "#dadada"
  canvas: "#fbf7f3"
  surface-soft: "#f9fafb"
  surface-card: "#fafafa"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: 0.02em
  display-lg:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.01em
  display-md:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'Cormorant Garamond', 'Playfair Display', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.01em
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.03em
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  label-upper:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.04em
  price-display:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: "none"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "none"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  product-card-hover:
    imageOverlay: "second-look swap"
    borderBottom: "1px solid {colors.hairline-soft}"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    ctaVariant: "button-primary"
    layout: "full-bleed image with text overlay or split 50/50"
    padding: "{spacing.section} {spacing.xl}"
  collection-grid:
    backgroundColor: "{colors.canvas}"
    columns:
      mobile: 2
      tablet: 3
      desktop: 4
    gap:
      mobile: "{spacing.sm}"
      desktop: "{spacing.base}"
    paddingHorizontal:
      mobile: "{spacing.base}"
      desktop: "{spacing.xxl}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 2px 6px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    disabledTextColor: "{colors.muted}"
    disabledDecoration: line-through
    height: 36px
    minWidth: 36px
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline-soft}"
    headlineTypography: "{typography.title-md}"
    width:
      mobile: "100vw"
      desktop: 420px
    ctaVariant: "button-primary"
  filter-sidebar:
    backgroundColor: "{colors.teal-wash}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.label-upper}"
    valueTypography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
  section-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    layout: "image left / text right, alternating"
    imageFill: "full-bleed within column"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline-soft}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    borderTop: "none"
    padding: "{spacing.xxl} {spacing.xxl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    height: 36px

## Components

### Buttons
**`button-primary`** — Full-width teal (#108474) block with zero border-radius, uppercase tracking at `{typography.button-md}`, white text, and 48px height. The sharp corners are the brand's intentional anti-move against the rounded DTC default; it reads as a graphic element rather than a rounded blob. Active state deepens to #0a6860; disabled washes to #82bdb5 at the same geometry.

**`button-secondary`** — Transparent field with a 1px solid black border and identical uppercase type. On hover the field inverts: background floods to #0f0f0f and text switches to white, making the hover feel like a print block rather than a glow.

**`button-ghost`** — Text-only link styled in `{colors.primary}` teal with underline, no border or background. Used for "View all," pagination links, and secondary editorial CTAs where a full button would over-weight the layout.

### Inputs & Forms
**`text-input`** — Sits on the warm cream canvas with a 1px #dedede border that sharpens to the primary teal on focus. No radius; the square geometry matches button and card edges. Placeholder text rests at `{colors.muted}` (#7b7b7b). Newsletter fields in the footer invert: dark background, near-white border.

### Navigation
**`nav-bar`** — 60px tall, cream (#fbf7f3) background, 1px `{colors.hairline-soft}` underline. Links render in `{typography.nav-link}` — small, slightly tracked, lowercase-friendly. Subnav mega-menus open as full-width panels with collection imagery and category columns. The cart icon carries a small teal count bubble. On scroll the bar remains un-sticky by default on desktop; mobile collapses to a hamburger with an off-canvas panel.

### Product Cards
**`product-card`** — Frameless, zero radius, 3:4 portrait image on a near-white (#fafafa) surface. Title in `{typography.body-sm}`, price in `{typography.price-display}` below. On hover, the image swaps to a second editorial shot (back view or styled detail). Sale price renders in `{colors.accent-red}` (#a91c2a) alongside a struck-through original in `{colors.muted}`. Badges (SALE, NEW) anchor to the top-left corner as small uppercase blocks.

### Badges
**`badge-sale`** — Solid #a91c2a rectangle, white uppercase label at 10px / 0.12em tracking. No radius. Sits inset over the product image corner at 8px offset. The burgundy creates a distinct urgency signal without disrupting the teal primary system.

**`badge-new`** — Same geometry in #0f0f0f with white text. Used for new-arrival callouts and freshly restocked items.

### Size Selector
**`size-selector`** — Square 36×36px tiles, 1px #dedede border, no radius. Active state inverts to solid black with white text. Sold-out sizes appear in `{colors.muted}` with a diagonal line-through rather than hidden, preserving grid geometry and communicating demand.

### Cart Drawer
**`cart-drawer`** — Slides in from the right at 420px on desktop, full-width on mobile. Canvas background (#fbf7f3), 1px soft hairline left border. Line items render with thumbnail, title in `{typography.title-md}`, quantity steppers as bare minus/plus buttons. The CTA is the full-width `button-primary` teal block pinned to the drawer bottom. Subtotal label uses `{typography.label-upper}`.

### Hero Banner
**`hero-banner`** — Full-viewport editorial image with either a centered text overlay at `{typography.display-xl}` (light-weight serif, 300) or a 50/50 split layout on desktop. On full-bleed layouts, the headline sits over the image with no scrim — photography is chosen for dark enough zones at the type position. Mobile collapses to stacked image-above / text-below.

### Filter Sidebar
**`filter-sidebar`** — On collection pages, filters sit in a left rail with a pale teal wash (#edf5f5) background. Category headers in `{typography.label-upper}`; option values in `{typography.body-sm}`. Active filters are marked with a teal check or colored underline. Mobile filters open as a full-screen drawer.

### Footer
**`footer`** — Near-black (#0f0f0f) ground, white body copy, hairline-soft (#eeeeee) links. Four columns on desktop: brand story blurb, shop links, help/policy links, newsletter capture. Newsletter input inverts the standard field — dark field, white text, white 1px border, with the same zero-radius geometry as all other inputs. The submit arrow or button uses the teal primary CTA style.

### Announcement Bar
**`announcement-bar`** — 36px teal (#108474) strip at the very top of the page, white uppercase label text, typically carrying shipping thresholds or sale messaging. Rotates through multiple messages via a slow fade carousel.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column nav hidden behind hamburger; product grid 2-column; hero stacks image above text; cart drawer is full viewport width; filter opens as bottom sheet; announcement bar text truncates to one message |
| Tablet | 744–1128px | Product grid shifts to 3 columns; nav bar exposes top-level categories inline; hero may remain stacked or go 50/50; filter rail collapses to an expandable top bar |
| Desktop | 1128–1440px | 4-column product grid; full mega-menu nav with image panels; hero at full 50/50 or full-bleed; left-rail filters visible by default; cart drawer 420px fixed width |
| Wide | > 1440px | Max-width container centers at ~1440px; editorial image sections expand edge-to-edge while text columns remain padded; extra whitespace absorbed in outer margins rather than content stretch |

### Touch Targets
- All interactive controls (size tiles, color swatches, quantity steppers, nav links) maintain a minimum 44×44px tap area even when visually smaller
- Cart and wishlist icon buttons in the nav bar include invisible padding to meet 44px minimum
- Filter chip labels on mobile render at minimum 44px height with extended horizontal padding

### Collapsing Strategy
- Product grid reduces columns before reducing image size: 4 → 3 → 2; never 1-column on devices wider than 375px
- Hero image maintains aspect ratio by cropping rather than letterboxing; focal-point CSS used to preserve subject
- Mega-nav collapses fully at tablet breakpoint — no intermediate "partial" state; hamburger takes over cleanly
- Footer columns stack 2×2 at tablet, fully single-column at mobile; newsletter capture always appears last

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Brand typeface unconfirmed**: The only font identifier extracted from the live site is `JudgemeStar`, a glyph font belonging to the Judge.me review widget — not a brand type asset. Display serif and body grotesque families in this file are reconstructed from visual inspection; actual font names and weights should be verified by inspecting the site's CSS `@font-face` declarations or Shopify theme files directly.
- **Exact button radii**: The rounded values used here (all `{rounded.none}` / 0px for buttons and inputs) reflect the sharp-edge pattern visible in screenshots, but Shopify theme CSS was not directly inspected to confirm `border-radius: 0` is explicitly set vs. inherited.
- **Motion / animation tokens**: Page transition speed, hover crossfade duration for product image swap, and announcement bar rotation interval could not be extracted from static analysis.
- **Dark mode or seasonal palette variants**: Rouje runs occasional limited-edition drops with altered color treatments; no variant palette data was captured.
- **Mega-nav imagery dimensions**: Image dimensions and crop ratios inside the desktop mega-menu panels could not be confirmed from extraction.
- **Icon set**: Navigation and UI icons (cart, search, hamburger, wishlist) are not characterized — whether SVG inline, icon font, or sprite sheet is unknown.
