---
version: alpha
name: "Instant Pot"
source_url: "https://www.instantpot.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  That deep cocoa-bean brown (#331612) is the first thing that registers — darker than espresso, warmer than black, it coats the navigation bar and primary CTAs like the fond at the bottom of a sauté pan. Instant Pot's digital presence borrows its confidence from the kitchen counter, not the electronics aisle, and the choice of Filson Soft as the primary typeface seals the deal: every letterform carries a soft, pillowed radius that mirrors the rounded silhouette of the pressure cooker itself. Headlines land at weight 700 in that font, but the generous x-height and rounded terminals keep even bold display text (`{typography.display-xl}`) from ever reading as aggressive. Body copy shifts to Geologica Variable, a geometric sans with optical-size intelligence — crisp at 14px captions, open and readable at 16px paragraphs — while Smoothy appears sparingly for promotional callouts and seasonal badge text, injecting a hand-lettered warmth that feels like a recipe note scribbled in the margin.

  The palette is deliberately restrained. A near-black ink (#121212) handles body text and icon strokes; a silver-warm gray (#dedede) draws hairlines, divider rules, and surface tints across the product grid. Between those two poles, the brown primary does all the heavy lifting for interactive affordance — buttons, active states, hover underlines, and the sticky add-to-cart bar all wear #331612. Cards sit on a white canvas with `{rounded.md}` corners and a single `{colors.hairline}` border, casting no box-shadow; the visual hierarchy relies on spacing (`{spacing.lg}` gutters, `{spacing.section}` vertical rhythm) rather than elevation. Product photography is large, always on white or light-gray backgrounds, and the grid favors two-up on mobile and four-up on desktop with consistent `{spacing.md}` gaps. A thin top announcement bar in the brown primary with `{colors.on-primary}` white text handles promotions, and the overall impression is a kitchen-tool brand that trusts the product's physical presence over decorative flourish — clean shelves, warm wood tones, nothing between you and the cooker.

colors:
  primary: "#331612"
  primary-active: "#1f0e0c"
  primary-disabled: "#99817d"
  ink: "#121212"
  body: "#333333"
  muted: "#6b6b6b"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f5f3f2"
  surface-card: "#ffffff"
  surface-warm: "#faf8f7"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-red: "#c0392b"
  star-rating: "#f5a623"
  success: "#27ae60"
  promo-bar: "#331612"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'filson-soft', 'Nunito', -apple-system, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'geologica-variable', 'Inter', -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  body-sm:
    fontFamily: "'geologica-variable', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'geologica-variable', 'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-lg:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-lg:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  price-compare:
    fontFamily: "'geologica-variable', 'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
    textDecoration: line-through
  badge:
    fontFamily: "'filson-soft', 'Nunito', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  promo-script:
    fontFamily: "'smoothy', 'Pacifico', cursive"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  micro-label:
    fontFamily: "'geologica-variable', 'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.4px
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
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary}
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: 2px solid {colors.primary-active}
  button-small:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.primary}
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.xl}
    logoHeight: 40px
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    boxShadow: 0 1px 3px rgba(0,0,0,0.08)
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.lg} {spacing.xl}"
    borderTop: 1px solid {colors.hairline}
    boxShadow: 0 8px 24px rgba(0,0,0,0.1)
    columnGap: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: 1px solid {colors.hairline}
    padding: 0
    imageAspectRatio: 1 / 1
    imageBackgroundColor: "{colors.surface-soft}"
    bodyPadding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    comparePriceTypography: "{typography.price-compare}"
    hoverTransform: translateY(-2px)
    hoverBoxShadow: 0 4px 12px rgba(0,0,0,0.08)
  product-card-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: button-primary
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    imageObjectFit: contain
    contentMaxWidth: 560px
  promo-announcement-bar:
    backgroundColor: "{colors.promo-bar}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    padding: 0 {spacing.base}
    textAlign: center
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    iconColor: "{colors.muted}"
    placeholderColor: "{colors.muted-soft}"
    borderFocus: 2px solid {colors.primary}
  star-rating-row:
    starColor: "{colors.star-rating}"
    starSize: 14px
    gap: "{spacing.xxs}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"
  add-to-cart-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderTop: 1px solid {colors.hairline}
    padding: "{spacing.md} {spacing.base}"
    height: 72px
    priceTypography: "{typography.price-lg}"
    buttonComponent: button-primary
    position: sticky
    bottom: 0
    zIndex: 50
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: 1px solid {colors.hairline}
    height: 44px
    buttonWidth: 44px
    buttonColor: "{colors.ink}"
  recipe-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: 1px solid {colors.hairline-soft}
    imageAspectRatio: 16 / 10
    bodyPadding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  comparison-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: 1px solid {colors.hairline-soft}
    padding: "{spacing.md} {spacing.base}"
    headerTypography: "{typography.title-sm}"
    headerBackgroundColor: "{colors.surface-soft}"
    checkColor: "{colors.success}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: none
    columnGap: "{spacing.xl}"
  footer-newsletter:
    backgroundColor: transparent
    inputBackgroundColor: rgba(255,255,255,0.1)
    inputTextColor: "{colors.on-dark}"
    inputRounded: "{rounded.sm}"
    inputHeight: 44px
    buttonComponent: button-primary
    typography: "{typography.body-sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    padding: "{spacing.md} 0"

---

## Components

### Buttons
**`button-primary`** — A solid brown (#331612) rectangle with `{rounded.sm}` corners and Filson Soft 600-weight text in white. Hover darkens to `{colors.primary-active}` with no scale transform; the transition is a 150ms background-color ease. Disabled state fades to `{colors.primary-disabled}`, a washed-out mauve-brown that reads as clearly inactive. The 48px height and 28px horizontal padding give the button a confident, tappable presence without feeling oversized next to product imagery.

**`button-secondary`** — White fill with a 2px `{colors.primary}` border and brown text. On hover, the background tints to `{colors.surface-soft}` and the border darkens. This variant appears for "View Details" and "Compare" actions where the primary CTA is already present on the page. Shares the same 48px height and `{rounded.sm}` radius as primary.

**`button-small`** — A compact 36px-tall variant used inside product cards for quick-add actions and filter pills. Uses `{typography.button-sm}` and `{rounded.xs}` to distinguish itself from full-sized CTAs in the visual hierarchy.

### Text Input
**`text-input`** — Standard 48px-tall input field with a `{colors.hairline}` border that transitions to `{colors.primary}` on focus. The rounded corners use `{rounded.sm}` to match button geometry. Placeholder text renders in `{colors.muted-soft}`. Used across newsletter signups, search overlays, and the checkout flow.

### Navigation
**`nav-bar`** — A 72px white bar with a thin `{colors.hairline}` bottom border. The logo sits left at 40px height, navigation links center in `{typography.nav-link}` (Filson Soft 500), and cart/account icons anchor right. On scroll, the bar compresses to 64px and gains a subtle drop-shadow via `nav-bar-scrolled`. The navigation accommodates product categories (Cookers, Blenders, Air Fryers, Coffee) as top-level links.

**`mega-menu`** — Drops below the nav-bar on hover with a clean white panel, organized into columns separated by `{spacing.xl}` gaps. Each column has a bold category header in `{typography.title-sm}` and links in `{typography.body-sm}`. A subtle 24px box-shadow provides depth without feeling heavy. Product thumbnails may appear in a featured column on the right.

### Product Card
**`product-card`** — A white card with `{rounded.md}` corners and a 1px `{colors.hairline}` border. The image sits in a square (1:1) container with a `{colors.surface-soft}` background, ensuring consistent alignment across the grid regardless of product photo dimensions. Below the image, `{spacing.base}` padding wraps the product title (`{typography.title-sm}`), price (`{typography.price-sm}`), and optional star rating. On hover, the card lifts 2px with a soft shadow. Sale badges use `product-card-badge` positioned top-left over the image.

### Hero Banner
**`hero-banner`** — A warm-toned section (`{colors.surface-warm}`) with a minimum height of 480px. Content is constrained to 560px max-width on one side, with a large product photograph (object-fit: contain) on the opposite side. The headline uses `{typography.display-xl}` — the largest type in the system — and a primary CTA button sits below a one-line subhead in `{typography.body-md}`. On mobile, the layout stacks image-first, content below.

### Promo Announcement Bar
**`promo-announcement-bar`** — A 40px-tall strip in the brand brown (#331612) with centered white text in `{typography.body-sm}`. Sits above the nav-bar and may include a dismiss button. Used for sitewide promotions, free-shipping thresholds, and seasonal sales. Content rotates if multiple messages are active.

### Search
**`search-bar`** — A pill-shaped (`{rounded.full}`) input with a `{colors.surface-soft}` background, 44px tall. A magnifying glass icon in `{colors.muted}` sits left-aligned. On focus, a 2px `{colors.primary}` border appears and the background shifts to white. Search suggestions drop into a panel matching `mega-menu` styling.

### Star Rating
**`star-rating-row`** — A horizontal row of 14px star icons in `{colors.star-rating}` (#f5a623) with `{spacing.xxs}` gaps. The review count follows in `{typography.caption}` and `{colors.muted}`. Empty stars render as outlines in `{colors.hairline}`. Used on product cards, product detail pages, and recipe cards.

### Add to Cart Bar
**`add-to-cart-bar`** — A sticky bottom bar on mobile product pages: white background, 72px tall, with a `{colors.hairline}` top border. The current price displays left in `{typography.price-lg}`, and a full-width `button-primary` sits right. The bar has z-index 50 to clear other page elements. On desktop, this bar does not appear — the add-to-cart button lives inline on the product page instead.

### Quantity Selector
**`quantity-selector`** — A 44px-tall inline control with minus/plus buttons flanking a centered number. The outer border matches `{colors.hairline}` with `{rounded.sm}` corners. Button tap targets are 44px square for accessibility.

### Recipe Card
**`recipe-card`** — Similar structure to `product-card` but with a 16:10 image aspect ratio suited to food photography. Metadata (cook time, servings) displays in `{typography.caption}` and `{colors.muted}` below the title. Border uses the softer `{colors.hairline-soft}` to differentiate content cards from commerce cards.

### Comparison Table
**`comparison-row`** — Alternating rows with `{colors.surface-soft}` header backgrounds and white data rows. Text is `{typography.body-sm}`, separated by `{colors.hairline-soft}` bottom borders. Check marks render in `{colors.success}`. Used on landing pages to compare Duo, Duo Plus, and Pro models.

### Footer
**`footer`** — A dark footer with `{colors.ink}` (#121212) background and white text. Section headings use `{typography.title-sm}`, links use `{typography.body-sm}` in `{colors.hairline}` that brighten to white on hover. Columns are separated by `{spacing.xl}` gaps. A newsletter signup block (`footer-newsletter`) sits in the final column with a semi-transparent input field and a brown primary button.

### Breadcrumb
**`breadcrumb`** — A horizontal trail in `{typography.caption}` with `{colors.muted}` text and chevron separators in `{colors.hairline}`. The final (active) crumb renders in `{colors.ink}`. Sits below the nav-bar with `{spacing.md}` vertical padding.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Nav collapses to hamburger + logo + cart icon. Hero stacks vertically (image above, content below). Sticky `add-to-cart-bar` appears at bottom. Mega-menu becomes full-screen slide-in. `{spacing.base}` horizontal page padding. |
| Tablet | 744–1128px | Two-column product grid. Nav shows top-level links but mega-menu triggers on tap. Hero can sit side-by-side at reduced image size. `add-to-cart-bar` still sticky. `{spacing.lg}` horizontal padding. |
| Desktop | 1128–1440px | Four-column product grid. Full nav with hover mega-menu. Hero at full 480px height, side-by-side layout. Add-to-cart lives inline. Comparison table shows all columns. `{spacing.xl}` horizontal padding. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Grid may expand to five columns for collection pages. Hero image scales proportionally. `{spacing.xxl}` outer margins. |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target on mobile and tablet.
- `quantity-selector` buttons are explicitly 44px square.
- Nav hamburger icon hit area extends to 48×48px.
- Product card tap target covers the entire card surface, not just the title link.
- Footer links have `{spacing.sm}` vertical padding for comfortable finger targeting.

### Collapsing Strategy
- Navigation collapses to a hamburger menu below 744px; category links move into a full-height slide-in panel with `{typography.title-md}` headings.
- Product grid shifts from four columns → two → one as viewport narrows, maintaining `{spacing.md}` gaps throughout.
- Hero banner stacks at the tablet breakpoint: image fills full width, then text content below with `{spacing.lg}` vertical separation.
- Comparison tables scroll horizontally on mobile with a sticky first column for model names.
- Footer columns stack vertically on mobile with accordion toggles for each section heading.
- Announcement bar text truncates with ellipsis on narrow viewports; a swipe gesture may reveal additional messages.

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only three hex colors were extracted (#dedede, #331612, #121212); the site likely loads additional palette tokens via JavaScript or Shopify theme settings. Colors like `accent-red`, `star-rating`, `success`, and surface tints are inferred from common Shopify kitchen-appliance patterns and should be verified against the live rendered DOM.
- Font weights and specific size ramps for `filson-soft`, `geologica-variable`, and `smoothy` could not be confirmed from static extraction; the values above are educated defaults based on typical usage of these typefaces. Smoothy's role (promotional badges vs. seasonal display) needs confirmation.
- No meta theme-color was present, suggesting the mobile browser chrome color is unset or defaults to white.
- Exact border-radius values, box-shadow definitions, and transition timings are approximated — the Shopify theme may use CSS custom properties loaded at runtime that were not captured in the static crawl.
- Comparison table structure and the number of model columns need verification against the actual product lineup pages.
- Recipe content section styling is inferred from the brand's known recipe community presence; the current site may have restructured or removed this content area.
- Icon system (stroke weight, size grid, source library) was not extractable and is not specified here.
