---
version: alpha
name: "Bellroy"
source_url: "https://bellroy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  GTUltraFine — Grilli Type's geometric serif-adjacent face with calligraphic stress points — runs at weight 400 across bellroy.com, an unusual decision that makes even headline copy feel like a label stamped on a handmade object rather than a brand declaration. The signature burnt-orange (#cd4c20) is the only hot color in the system, appearing precisely at points of decision pressure: the primary CTA, new-item badges, the active-swatch ring, and section eyebrows. Everywhere else the palette retreats to near-black (#1d1d1b), cool mid-grays (#9b9b9b), and the off-white surface (#f7f7f7) that product photography rests on without competition. A secondary blue (#2279a9) appears exclusively in informational and link contexts, keeping thermal contrast purposeful. Hard corners ({rounded.none}) govern every button and input — flush ninety degrees, no radius softening — which reads as material confidence rather than approachability engineering. Product swatches are pill-shaped ({rounded.full}) at 20px while the surrounding card stays completely square, so the organic swatch form signals material sampling rather than UI embellishment. The navigation mega-menu exposes an unusually granular carry taxonomy — slim wallets, bifolds, travel wallets, cardholders, bags by size — segmented by carry function rather than gender or seasonal collection. This mirrors the brand's founding logic: engineer the minimum object for a specific carry need, then show it in every colorway. Typography rarely departs from two weights (400 and 700) and always pairs GTUltra for display contexts with Lato for utility text, keeping everything from campaign hero to checkout confirmation visually of a piece. Frank Ruhl Libre appears in the stack as a serif fallback for multilingual support, signaling global reach without introducing a third display voice. The word 'considered' in the page title is a system constraint, not marketing copy — the UI enforces it through sparse type scale, a single accent hue, and geometry that never competes with the product.

colors:
  primary: "#cd4c20"
  primary-active: "#b85021"
  primary-disabled: "#e8a080"
  accent-blue: "#2279a9"
  accent-blue-dark: "#1e6a93"
  error: "#eb340a"
  ink: "#1d1d1b"
  body: "#222222"
  muted: "#9b9b9b"
  hairline: "#eeeeee"
  hairline-soft: "#f7f7f7"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  swatch-border: "#d0d1d0"
  dark-footer: "#1d1d1b"

typography:
  display-xl:
    fontFamily: "'GTUltra', 'GTUltraFine', 'Frank Ruhl Libre', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GTUltra', 'GTUltraFine', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GTUltra', 'GTUltraFine', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'GTUltra', 'GTUltraFine', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  nav-link-active:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  eyebrow:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  link:
    fontFamily: "'Lato', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
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
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 15px 31px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 28px
  nav-mega-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    categoryHeadTypography: "{typography.title-sm}"
    padding: "{spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
    shadow: "0 8px 24px rgba(0,0,0,0.08)"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageRounded: "{rounded.none}"
    padding: "{spacing.sm}"
    gap: "{spacing.sm}"
    priceTypography: "{typography.price}"
    nameTypography: "{typography.title-md}"
    categoryTypography: "{typography.caption}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    selectedOffset: 2px
    unselectedBorder: "1px solid {colors.swatch-border}"
    gap: "{spacing.xs}"
  swatch-count-overflow:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
    paddingDesktop: "{spacing.section}"
    paddingMobile: "{spacing.xl}"
    imageObjectFit: cover
  section-eyebrow:
    textColor: "{colors.primary}"
    typography: "{typography.eyebrow}"
    marginBottom: "{spacing.sm}"
  collection-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.title-sm}"
    gap: "{spacing.base}"
    borderBottom: "1px solid {colors.hairline}"
    itemPadding: "12px 0"
    activeIndicator: "2px solid {colors.ink}"
  material-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 12px
    border: "1px solid {colors.hairline}"
  accordion-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "16px 0"
    iconSize: 20px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    iconColor: "{colors.muted}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
  size-guide-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    width: 480px
    padding: "{spacing.xl}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separator: "/"
    separatorColor: "{colors.muted}"
    gap: "{spacing.xs}"
  product-image-gallery:
    thumbnailSize: 72px
    thumbnailBorder: "2px solid transparent"
    thumbnailActiveBorder: "2px solid {colors.ink}"
    thumbnailRounded: "{rounded.none}"
    mainImageRounded: "{rounded.none}"
    gap: "{spacing.sm}"
  footer:
    backgroundColor: "{colors.dark-footer}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    legalTypography: "{typography.caption}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xl}"
    borderTop: "none"
    columnGap: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — Flat rectangular CTA in burnt-orange (#cd4c20) at 48px tall, no border-radius. Text is uppercase Lato 700 at 14px with 0.6px letter-spacing and wide 32px horizontal padding. On hover the background steps to #b85021 (`primary-active`); the disabled state washes to a desaturated `primary-disabled` peach. There is no border-radius softening anywhere — the hard edge is a deliberate design signal that the brand's authority comes from material and engineering, not interface friendliness.

**`button-secondary`** — Transparent background with 1px ink-colored border, same dimensions as `button-primary`. On hover fills to full ink (#1d1d1b) with white text. Used for secondary actions on product pages (add to wishlist, compare, find in store).

**`button-ghost`** — Zero-padding, transparent, primary-orange text, uppercase Lato 700. Used for inline navigation prompts ("See all wallets →") within editorial sections. Underline on hover.

### Navigation

**`nav-bar`** — White canvas, 64px tall, 1px hairline bottom border. Logo sits left at max 28px height. Primary nav links are Lato 400 at 14px; they gain weight 600 (`nav-link-active`) on hover/focus. A utility row (search, account, cart) lives right. On scroll the bar remains fixed with a subtle shadow. The cart icon carries a numeric badge.

**`nav-mega-dropdown`** — Opens on hover over any primary nav item. White panel, full viewport width, appears below the nav bar with a 1px hairline top border and a soft 8px drop shadow. Interior columns group product subcategories under `title-sm` headings with `body-sm` item links. A featured image column (rightmost) links to the current season's campaign. Closes on mouse-leave with a 150ms fade.

### Product Card

**`product-card`** — Square image fills the card width with no radius. Below the image: product name in `title-md`, colorway label in `caption` gray, price in `price` style (same as body-md, weight 400). The card has no visible border at rest — it relies on the grid gutter for separation. On hover the image shifts by a subtle 4px translate-Y suggesting depth without a box-shadow.

**`product-card-badge`** — Positioned absolute at top-left. Flat orange rectangle (`primary`), uppercase Lato 700 at 11px, no radius. Used for "New", "Sale", "Low Stock" states. Only one badge may appear at a time.

**`color-swatch`** — 20px pill ({rounded.full}) that renders the material color. Selected state adds a 2px ink-colored ring with a 2px offset gap between swatch and ring, a technique borrowed from jewelry display. Unselected has 1px `swatch-border` ring. Overflow when more than 5 colors are available is handled by `swatch-count-overflow` — a gray "+N more" caption link.

### Hero Banner

**`hero-banner`** — Full-width, typically 60–70vh on desktop. Background is either a full-bleed product photograph or a solid `surface-soft` panel. Above the headline: a section eyebrow in `eyebrow` style at `colors.primary` orange. Headline in `display-xl` (GTUltra 400, 56px) — the low weight at large size is central to the brand's quiet confidence. A supporting subhead or body line follows in `body-md`. One `button-primary` CTA sits below. Mobile collapses the headline to `display-md`.

### Accordion

**`accordion-row`** — Full-width rows separated by 1px hairline borders. Label in `title-md`, expand/collapse chevron at 20px right-aligned. Body appears in `body-sm` with 16px top padding. Used for shipping information, fit guides, and FAQ on PDP. No background change on open — the hairline and spacing alone carry the state change.

### Collection Strip

**`collection-strip`** — A horizontal scroll of category links (Wallets, Bags, Accessories, etc.) just below the nav on category landing pages. Each item is `title-sm` with a 2px ink-colored bottom underline for the active state and no underline at rest. The strip sits on a white canvas above the product grid, separated by a 1px hairline.

### Search

**`search-bar`** — Flat, no-radius input on a soft gray background, 48px tall, 1px hairline border that steps to 1px ink on focus. Placeholder in `muted` gray. A magnifier icon sits left at 20px in muted gray. Live results appear in a dropdown overlay below.

### Footer

**`footer`** — Full-width dark panel using `dark-footer` (#1d1d1b) background with white text. Columns carry `title-sm` headings in white and `body-sm` links in on-dark white at reduced opacity (70%). A newsletter signup row sits at top of footer using the `text-input` on a dark field. The very bottom row carries legal copy in `caption` style and social icon links.

### Material Chip

**`material-chip`** — Pill-shaped tags used in product detail to call out material attributes (Full-grain leather, RFID blocking, Recycled nylon). Soft gray background, 1px hairline border, `caption` typography. Rendered in a horizontal wrap below the color swatch row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to `display-md` (28px); nav-bar collapses to hamburger + logo + cart; collection-strip horizontally scrollable; mega-dropdown replaced by slide-in panel; product-card-badge repositioned to maintain legibility |
| Tablet | 744–1128px | Two-column product grid; hero headline at `display-lg` (40px); nav shows top-level items, mega-dropdown retained; collection-strip fits in one viewport row without scroll |
| Desktop | 1128–1440px | Three- or four-column product grid depending on category density; hero at full `display-xl` (56px); nav-bar shows full utility row; cart-drawer and size-guide-drawer slide in from right at fixed widths |
| Wide | > 1440px | Layout max-width caps at ~1440px with centered grid; hero image extends edge-to-edge behind a width-constrained text column; footer columns expand spacing to prevent orphaned short lines |

### Touch Targets

- All swatches rendered at minimum 20px with 8px padding zone between adjacent swatches
- Nav items in mobile slide-in panel minimum 48px tall per row
- Accordion trigger rows minimum 48px tall
- Cart quantity stepper buttons minimum 44×44px
- Breadcrumb taps minimum 32px tall to accommodate small link text

### Collapsing Strategy

- Mega-dropdown navigation transforms to full-screen slide-in drawer with back-button depth navigation on mobile
- Product detail accordion rows replace tabbed panels below 744px
- Color swatch row wraps to two rows before collapsing to "+N more" overflow label
- Hero banner stacks text above image on mobile rather than overlaying on photograph
- Footer columns collapse to a single-column accordion on mobile, defaulting to closed state

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact GTUltra/GTUltraFine weight ladder and licensed size table not publicly documented; weight 400 as display default inferred from visual inspection
- `primary-disabled` (#e8a080) approximated — no explicit disabled-state hex found in extraction
- Hover transition durations and easing curves not extractable from static extraction
- Frank Ruhl Libre usage context unclear — likely a Hebrew-locale or multilingual fallback rather than a primary display face
- Exact nav-bar height not confirmed; 64px is a reasonable inference from proportions
- Cart-drawer and size-guide-drawer widths (400px / 480px) are approximated — no extracted CSS values available
- Animation specs for image gallery, accordion, and dropdown overlays are unconfirmed
- Dark-mode or alternate theme variant, if any, has no extracted evidence — assumed light-only
