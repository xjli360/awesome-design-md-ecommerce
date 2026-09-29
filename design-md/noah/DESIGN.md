---
version: alpha
name: "Noah"
source_url: "https://noahny.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The deep-sea navy of #1d1e45 sits at Noah's foundation like the hull of the wooden sailboats that appear on its hangtags and seasonal graphics — an indigo so dark it reads black at arm's length yet opens up to something distinctly maritime under direct light. From that anchor color the brand pivots hard: #ed1c24 punches through on campaign headers and sale callouts with the bluntness of a protest banner, while #a45cec surfaces as an unexpected seasonal accent that refuses the usual streetwear chromatic vocabulary. Brendan Babenzien built Noah as a deliberate counterweight to the hype machine — small batches, above-cost pricing transparency, and terse copy that says what it means. That restraint lives in the typography: Archivo, a grotesque with sturdy humanist counters, runs at tight tracking and full uppercase for display, natural case for body, choosing legibility over showmanship. Primary CTAs sit on the navy field with white reverse type rather than reaching for the red, reserving #ed1c24 for moments of genuine urgency — clearance, limited availability, editorial callouts. Cards are borderless on a near-white (#fefefe) canvas with hairlines at #dedede; the product grid breathes without theatrical padding. Corner radii stay minimal — product cards carry 4px — the brand's workwear and military references demand nothing rounder. Buttons hold at {rounded.xs} rather than the pill shapes dominant in consumer DTC. The footer is dense with text links, newsletter capture, and a short mission statement that other brands bury in an "About" modal; Noah puts it in plain sight because the position is the product. Muted gray (#888888) handles secondary metadata — fabrication notes, country of origin, restocking caveats — while the dark-canvas (#121212) powers login and cart drawer surfaces, shifting the experience into near-black without a full dark-mode toggle. Purple (#a45cec) appears selectively on seasonal drop badges, never as structural chrome. The result reads more like a journal with a commerce layer than a commerce site with a journal layer.

colors:
  primary: "#1d1e45"
  primary-active: "#14152e"
  primary-disabled: "#6b6c8a"
  accent-red: "#ed1c24"
  accent-red-active: "#c21019"
  accent-purple: "#a45cec"
  ink: "#1b1c1e"
  body: "#3a3a3a"
  muted: "#888888"
  hairline: "#dedede"
  canvas: "#fefefe"
  surface-soft: "#f5f5f5"
  surface-card: "#fefefe"
  surface-dark: "#121212"
  on-primary: "#fefefe"
  on-dark: "#fefefe"

typography:
  display-xl:
    fontFamily: "'Archivo', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Archivo', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
    textTransform: uppercase
  display-sm:
    fontFamily: "'Archivo', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.2px
    textTransform: uppercase
  title-md:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
  price-display:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  product-name:
    fontFamily: "'Archivo', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 13px 23px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 24px
    height: 44px
  button-accent-red-active:
    backgroundColor: "{colors.accent-red-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    borderBottom: "1px solid {colors.hairline}"
    height: 56px
    logoHeight: 28px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    productNameTypography: "{typography.product-name}"
    priceTypography: "{typography.price-display}"
    salePriceColor: "{colors.accent-red}"
    strikethroughColor: "{colors.muted}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  badge-seasonal:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    height: 36px
    textAlign: center
  hero-editorial:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 80vh
    padding: "{spacing.section} {spacing.xl}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"
  filter-tag:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    textColorActive: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
  cart-drawer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headerTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    width: 400px
    rounded: "{rounded.none}"
  newsletter-block:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    inputBorder: "1px solid {colors.on-primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — Navy (#1d1e45) fill with white uppercase Archivo text at 13px/1px tracking, 44px height, {rounded.xs} corners. Pressed state deepens to #14152e; disabled washes out to #6b6c8a. This is the principal add-to-cart and checkout CTA — it appears on PDPs, the cart drawer, and account forms without variation.

**`button-secondary`** — Transparent fill, 1px ink (#1b1c1e) border, same uppercase Archivo treatment and 44px height. Hover fills the ink field and reverses type to white. Used for secondary CTAs: "View All", "See Details", wishlist toggles, editorial "Shop Now" where a softer register is warranted.

**`button-accent-red`** — Red (#ed1c24) fill reserved exclusively for sale pages, clearance callouts, and limited-availability urgency situations. Never substituted for a generic primary action. Its presence signals scarcity rather than decoration.

### Text Inputs
**`text-input`** — 44px height, 1px hairline (#dedede) border that sharpens to 1px ink (#1b1c1e) on focus, {rounded.xs} corners. Labels sit above the field in `{typography.button-sm}` uppercase rather than inside as floating placeholders. Applied consistently across search, account forms, and newsletter capture.

### Navigation
**`nav-bar`** — 56px sticky header on white canvas with a 1px hairline bottom border. Logo left-aligned on desktop, center-aligned on mobile. Navigation links in `{typography.nav-label}` — 13px Archivo, 0.5px tracking — with no underline; active state signals by color shift to primary navy. Cart and account icons align right. No complex hamburger animation on mobile.

### Product Card
**`product-card`** — Zero-radius, borderless card on the white canvas. Product image fills a 3:4 aspect ratio with no shadow or border. Product name in `{typography.product-name}` (13px, weight 400) sits immediately below; price in `{typography.price-display}` (14px, weight 500). Sale pricing shows original struck through in muted gray (#888888) with the active price in accent-red (#ed1c24). Hover swaps to a secondary lifestyle image via crossfade — no zoom, no overlay.

### Badges
**`badge-sale`** — Red (#ed1c24) tight rectangle at {rounded.xs}, 3×6px padding, 11px uppercase Archivo. Positioned top-left on product imagery. **`badge-new`** — Same geometry in primary navy (#1d1e45). **`badge-seasonal`** — Purple (#a45cec) used for seasonal drops or collaboration labels; appears sparingly and never alongside the other two simultaneously.

### Announcement Bar
**`announcement-bar`** — 36px navy strip pinned above the nav. White 11px uppercase Archivo centered. Carries a single rotating message: free shipping threshold, ethical sourcing note, or limited-release countdown. No dismiss control — it is editorial positioning, not promotional filler.

### Hero
**`hero-editorial`** — Full-bleed dark canvas (#121212) with left-aligned or centered copy in `{typography.display-xl}` (48px uppercase Archivo). Body copy in `{typography.body-md}` in white. Minimum 80vh height. CTA pair uses `button-primary` (navy) alongside `button-secondary` (white-bordered) depending on the seasonal story. No gradient overlays — image and type share the frame without softening.

### Collection Header
**`collection-header`** — White canvas section with collection name in `{typography.display-md}` (32px uppercase), padded 48px vertically, separated from the product grid by a 1px hairline. Optional one-line editorial descriptor in `{typography.body-md}` directly beneath the heading.

### Filter Tags
**`filter-tag`** — Minimal chips with 1px hairline border and muted (#888888) label text at rest; active state brings the border and text to ink (#1b1c1e). No fill, no shadow. Labels uppercase 11px Archivo. Filter strip runs horizontally below the collection header without drawer or modal.

### Cart Drawer
**`cart-drawer`** — Slides from the right at 400px width. Dark canvas (#121212) background with white type. Product names in `{typography.title-sm}` (uppercase 14px), pricing in `{typography.price-display}`. Checkout CTA renders as `button-primary` reversed to navy inside the dark container. Zero corner radius — the drawer edge meets the viewport edge as a clean cut.

### Newsletter Block
**`newsletter-block`** — Full-width navy (#1d1e45) section above the footer. Heading in `{typography.display-sm}` (24px uppercase). Input has transparent fill with white 1px border and white placeholder; submit uses `button-primary` styled white-on-navy within the navy field. Copy leans editorial — "Updates & Opinions" over "Sign Up for Deals."

### Footer
**`footer`** — Ink (#1b1c1e) background with multi-column link grid in `{typography.body-sm}` white. Section headings in `{typography.title-sm}` (uppercase, 14px). Includes a condensed mission/ethics statement column alongside shop, account, and legal columns — brand values sit at the same visual tier as customer service links, not tucked into an "About" dropdown.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + cart icon; hero copy drops to display-md (32px); cart drawer goes full-width |
| Tablet | 744–1128px | Two-column product grid; top nav shows primary links; hero copy at display-xl; filter strip visible |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with dropdown category panels; announcement bar always visible |
| Wide | > 1440px | Grid centers in max-width 1440px container with increased side gutter; hero image gains lateral breathing room |

### Touch Targets
- All interactive controls minimum 44×44px on mobile (buttons, filter tags, nav icons, quantity steppers)
- Product card tap area covers full image and metadata block as a single hit zone
- Announcement bar carries no tap target — no dismiss, no link
- Cart drawer close icon padded to 44×44px regardless of visible icon size

### Collapsing Strategy
- Desktop multi-column nav collapses to icon-only hamburger on mobile; no mega-menu on touch viewports
- Filter strip converts to horizontal scroll row on mobile; no modal or slide-over
- Newsletter block stacks input above CTA button (column layout) below 744px
- Footer link columns collapse to accordion-style expandable sections on mobile
- Hero CTA pair shifts from horizontal row (desktop) to vertical stack (mobile)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius value not extracted from CSS; {rounded.xs} (4px) inferred from visual brand aesthetic and workwear design references
- Archivo font weight distribution across display scales inferred from editorial style; specific CSS font-weight values not confirmed via extraction
- #a45cec (purple) confirmed in extracted palette but precise usage context — seasonal badge, collaboration accent, or other — not verified in live CSS
- No confirmed dark-mode toggle; dark surfaces (#121212) observed in hero and cart drawer only; full dark-mode treatment unknown
- Nav height (56px) estimated from visual inspection; scroll-triggered shrink or transparency behavior not confirmed
- Hover transition timing (product card image crossfade, drawer slide duration) not extracted
- Exact product grid gutter widths at each breakpoint not confirmed via CSS inspection
- Logo asset format (SVG vs raster), exact dimensions, and any responsive swap not confirmed
- Announcement bar message rotation mechanism (JS carousel vs. server-rendered) not observed
