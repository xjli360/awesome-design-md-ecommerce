---
version: alpha
name: "Polywood"
source_url: "https://www.polywood.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Milk-jug plastic pressed into lumber planks, then photographed against white backdrops as if each Adirondack were a piece of Danish mid-century — that visual contradiction is the engine of the whole digital system. The palette runs exclusively through a cool blue-gray corridor: a steel-slate `{colors.primary}` (#607089) surfaces on secondary accents, review-star fills, and icon tints, while a deeper navy `{colors.navy}` (#2a3b5c) commands every primary CTA, the top announcement bar, and the full-width footer. Two nearly identical grays — #e2e2e2 and #dedede — split duty between `{colors.hairline-soft}` and `{colors.hairline}`, giving borders and dividers a subtle two-tone depth that most brands skip. Near-black `{colors.ink}` (#121212) anchors all body copy with enough contrast to read comfortably in direct sunlight on a tablet propped against a patio table. There is no warm accent, no sustainability-green badge, no lifestyle coral — the restraint is deliberate, letting the lumber-finish color swatches in the product configurator be the only saturated elements on any given page. Typography pairs two faces that shouldn't work together but do: Gotham, a geometric sans-serif carrying all interface text with tight uppercase tracking on buttons (`{typography.button-md}`, 0.5px letter-spacing, textTransform uppercase), and quincy-cf, a soft-shouldered serif that only appears at the hero and collection-header level (`{typography.display-xl}` at 48px/700). The serif never touches navigation or product cards, enforcing a clean editorial/functional split. Corners stay architectural to echo the right-angle joinery of the furniture: product cards use `{rounded.none}`, buttons and inputs take only `{rounded.xs}` (4px), and the lone curved element is the `{rounded.full}` color-swatch circle on the PDP. Spacing is wide open — `{spacing.section}` (64px) between content blocks, `{spacing.xxl}` (48px) inside hero panels — because the product itself is big, and the layout needs room to breathe around a six-seat dining set rendered at 1:1.

colors:
  primary: "#607089"
  primary-active: "#4e5d74"
  primary-disabled: "#b0bac8"
  navy: "#2a3b5c"
  navy-active: "#1e2d49"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#6e6e6e"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-warm: "#f0eeeb"
  on-primary: "#ffffff"
  on-navy: "#ffffff"
  star-rating: "#607089"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'quincy-cf', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'quincy-cf', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'quincy-cf', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'quincy-cf', Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  label-uppercase:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  promo-bar:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
  link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  badge:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.3px
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
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.navy-active}"
    textColor: "{colors.on-navy}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    borderWidth: 2px
    borderColor: "{colors.navy}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.navy-active}"
    rounded: "{rounded.xs}"
    borderWidth: 2px
    borderColor: "{colors.navy-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.navy}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.navy}"
  nav-link-inactive:
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  promo-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.promo-bar}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 0
    imageAspectRatio: "1:1"
    gap: "{spacing.sm}"
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "1:1"
    backgroundColor: "{colors.surface-soft}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 500
  product-card-swatch-row:
    gap: "{spacing.xs}"
    swatchSize: 20px
    rounded: "{rounded.full}"
  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
  hero-banner-dark:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: "button-secondary"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    borderWidth: 2px
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
  color-swatch-sm:
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    selectedBorderColor: "{colors.ink}"
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  sustainability-icon-row:
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    iconSize: 24px
    gap: "{spacing.base}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.md} 0"
    borderBottom: "1px solid {colors.hairline}"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  filter-pill-active:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "{spacing.xs} {spacing.md}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    boxShadow: "0 4px 24px rgba(0,0,0,0.12)"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    textColor: "{colors.on-navy}"
    typography: "{typography.link}"
    opacity: 0.8
  footer-link-hover:
    textColor: "{colors.on-navy}"
    opacity: 1
  review-stars:
    filledColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: "{spacing.xxs}"
  badge-sale:
    backgroundColor: "#c13515"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
  divider-soft:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The main CTA across the site, rendered in deep navy (#2a3b5c) with white uppercase Gotham text at 14px/500 and 0.5px letter-spacing. Height is 48px with 4px rounded corners — barely softened, matching the right-angle geometry of the lumber furniture. On hover, the background darkens to #1e2d49. The disabled state shifts to a desaturated blue-gray (#b0bac8) with white text, visually receding without disappearing. Used for "Add to Cart," "Shop Now," and primary form submissions.

**`button-secondary`** — An outlined variant: white background, navy text, and a 2px solid navy border. Shares the same 48px height and 4px radius as primary for alignment consistency. On hover, the fill shifts to the soft surface tone (#f5f5f5) and the border darkens. Used for "Learn More," "Compare," and secondary actions that should be visible but not compete with the primary CTA.

**`button-tertiary-text`** — A text-only button with no background or border, rendered in navy at 12px/500 uppercase. Appears in tight spaces: "View All" links within collection grids, "Cancel" in modal dialogs, or inline secondary actions within product detail accordions.

### Cards
**`product-card`** — A zero-radius card that lets the product image bleed edge-to-edge. The image sits in a 1:1 square container with a #f5f5f5 fallback background. Below, the title uses 16px/500 Gotham in near-black, and the price appears at the same size but with a heavier 500 weight. A row of tiny 20px color swatches at the bottom indicates available finish options, each circle separated by 4px. No visible border or shadow — cards rely on whitespace and the grid gutter alone for separation.

**`product-card-swatch-row`** — A horizontal strip of miniature color swatches beneath the product title and price. Each swatch is 20px diameter, fully rounded, with a 1px hairline border. Selected state swaps to ink-colored border. This row is critical for Polywood because a single chair model may ship in 15+ lumber finishes, and the swatch row communicates breadth without requiring a click-through.

### Navigation
**`nav-bar`** — A 72px-tall white bar with a subtle 1px bottom border in #e2e2e2. The logo sits left, category links center in 14px/500 Gotham with 0.3px tracking. Active links carry a 2px navy underline; inactive links use muted gray (#6e6e6e). Utility icons (search, account, cart) are right-aligned. The bar stays fixed on scroll.

**`promo-bar`** — A 40px announcement strip pinned above the nav bar in navy (#2a3b5c) with white text at 13px/500 Gotham. Carries sale messaging, free-shipping thresholds, or seasonal promotions. This is one of only two places in the system where white text meets a dark background (the other is the footer).

### Hero
**`hero-banner`** — A full-width panel with a warm off-white background (#f0eeeb) that keeps the hero from feeling cold despite the blue-gray palette. The heading uses quincy-cf at 48px/700 — the largest serif moment on any page. Body copy sits in 16px/400 Gotham. A primary navy button anchors the bottom-left. Minimum height is 560px, with 64px vertical and 32px horizontal padding. Lifestyle photography typically fills a 50–60% right column.

**`hero-banner-dark`** — An inverted variant using the navy background (#2a3b5c) with white text. The heading remains quincy-cf display-xl. The CTA switches to button-secondary (white outline on dark) for contrast. Used for seasonal campaigns and collection launches where a more dramatic entrance is needed.

### Collection
**`collection-header`** — A white-background block that opens every collection page with a quincy-cf heading at 28px/600, a body-md description paragraph, and 48px vertical padding. No image — the heading and copy carry the entire context, relying on the serif's warmth to do the work that a lifestyle banner would do elsewhere.

**`filter-bar`** — A horizontal bar below the collection header that houses sort controls and filter pills. Background is white, with a 1px hairline bottom border. Filter pills are fully rounded capsules: inactive in #f5f5f5 with gray text, active in navy with white text. The transition between states is immediate (no fade), reinforcing the industrial clarity of the brand.

### Product Detail
**`color-swatch`** — A 32px circle with a 2px hairline border. On selection, the border snaps to ink (#121212). No checkmark overlay, no inner ring — just the border change. This is the primary configuration interface for choosing among Polywood's extensive lumber-finish palette (sometimes 20+ options per product).

**`material-badge`** — A small rectangular tag (4px radius) with a #f5f5f5 background and uppercase 11px/700 Gotham text in body gray. Used to label material types ("HDPE LUMBER," "MARINE-GRADE HARDWARE") and sustainability certifications on the product detail page. Padding is tight: 4px top/bottom, 8px left/right.

**`sustainability-icon-row`** — A horizontal row of 24px icons (recycled content, UV resistance, warranty) in the slate primary (#607089), each followed by a caption-sized label. Spaced at 16px intervals. Appears below the main product description and above the reviews section, quietly reinforcing the brand promise without a heavy visual treatment.

### Reviews
**`review-stars`** — Star icons filled in the slate primary (#607089) with unfilled stars using the hairline gray (#dedede). Each star is 16px, separated by 2px. The muted fill color keeps the rating from visually competing with the navy CTAs — a deliberate hierarchy choice.

### Footer
**`footer`** — A full-width block in navy (#2a3b5c) with white text. Contains four columns: product categories, customer service, company info, and a newsletter sign-up input. Links appear at 80% opacity, rising to full on hover. Section padding is 64px top/bottom and 32px left/right. The footer is the visual bookend to the promo-bar — same background, same white text, framing the entire page in navy.

### Breadcrumb
**`breadcrumb`** — A horizontal trail using caption-sized (12px) Gotham text in muted gray, with hairline-colored separators. The final (current) item renders in ink for a subtle active indicator. Appears at the top of product detail and collection pages, providing orientation within the catalog hierarchy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger navigation replaces inline links, hero reduces to 360px min-height with stacked text/image, promo-bar text truncates to single line, display-xl drops to 32px, color swatches shrink to 24px |
| Tablet | 744-1128px | Two-column product grid, navigation expands to dropdown mega-menu, hero image moves to 50/50 split, filter bar scrolls horizontally, display-xl at 40px, footer columns collapse to 2x2 grid |
| Desktop | 1128-1440px | Three-column product grid, full top-nav with all category links visible, hero at full 560px height with 60/40 text-image split, filter pills wrap naturally, all typography at defined sizes, four-column footer |
| Wide | > 1440px | Max-width container at 1440px centered, four-column product grid, hero imagery extends to bleed edges while content stays contained, increased horizontal padding on section blocks |

### Touch Targets
- All buttons maintain 48px minimum height on mobile; tertiary text buttons get a 44x44px invisible hit area
- Product card tap target extends to the full card surface, not just the title text
- Color swatches on mobile enlarge to 40px diameter with 8px spacing for accurate finger selection
- Hamburger icon is 48x48px; cart and search icons are 44x44px minimum
- Filter pills maintain 36px height on mobile for comfortable thumb tapping
- Footer links receive 44px vertical spacing on mobile for reliable tap accuracy

### Collapsing Strategy
- Top navigation collapses to a left-aligned hamburger at < 744px, opening a full-height drawer with stacked category links and utility icons at the top
- Product grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile), with consistent 16px gutters throughout
- Hero stacks vertically on mobile: image on top at 16:9, text block below with centered alignment and reduced padding (32px)
- Filter bar becomes a horizontally scrollable strip on mobile, with a "Filter" button that opens a bottom-sheet overlay for advanced options
- Footer columns collapse from 4 (desktop) to 2x2 (tablet) to fully stacked (mobile), with accordion-style section toggles on mobile
- Color-swatch rows on the PDP wrap to a second line on mobile rather than scrolling horizontally, ensuring all finishes remain visible
- Search bar collapses to an icon on mobile, expanding to a full-width overlay with recent searches on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only five hex colors were extracted (#e2e2e2, #607089, #dedede, #2a3b5c, #121212); the site likely loads additional palette tokens via JavaScript or CSS custom properties at runtime
- No warm accent or green sustainability color was detected despite the brand's heavy recycled-material messaging — this may be delivered through imagery or JS-injected elements rather than static CSS
- Gotham and quincy-cf font weights beyond what is inferred (400, 500, 600, 700) could not be confirmed; the site may use additional intermediate weights
- Hover and focus states for interactive elements (product cards, swatches, links) are inferred from convention, not extracted
- Dark mode palette does not appear to exist on the live site
- Modal and drawer components (quick-view, mobile nav drawer, filter sheet) could not be reliably styled from extraction
- Product configurator interactions (selecting a lumber finish and seeing the product image update) involve JS-driven state that is not captured in static CSS
- Loading and skeleton-screen patterns are undocumented
- Toast, notification, and success-state component styling is absent from extracted data
- Mega-menu dropdown styling (shadow, animation, column layout) for desktop navigation sub-menus was not captured
- Form validation error states (border color, message typography, icon usage) are inferred from common patterns
- The site's Shopify platform may inject additional theme-level variables not visible in the initial CSS extraction
