---
version: alpha
name: "NECA"
source_url: "https://necaonline.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The blood-red #e83630 is not decoration — it is the urgency voltage that marks every add-to-cart button, sale callout, and new-release badge on a site where 7-inch scale demons, time-traveling robots, and alien hunters share catalog space with vintage horror villains. The palette runs from this alert-red through deep burgundy (#600040) and near-black charcoal (#313131) to a cool light neutral (#eeeeee), assembling a cinematic contrast register that echoes the poster art of the franchises NECA licenses rather than any contemporary ecommerce playbook. Text lives entirely in system-web stacks centered on Open Sans — no custom typeface — which keeps the brand honest: the products carry the personality, not the letterforms. Navigation is dense and category-driven; collectors need to reach "Aliens Series 14" or "Ultimate Dutch" without wading through editorial layers, so the nav runs taxonomic depth over aspirational lifestyle copy, with franchise-organized mega-menu columns. Product cards surface high-fidelity photography against light neutral backgrounds, letting the sculpt and paintwork speak; the red primary reserves itself for badges, CTAs, and sale callouts. Deep navy (#003050) and cobalt (#4054b2) anchor secondary banner modules, pulling from the science-fiction and military visual vocabulary that defines many licensed properties. The burgundy (#600040) emerges as a premium collector tone, used sparingly for featured-series and special-edition callouts. Border radii stay modest at {rounded.xs} to {rounded.sm} — NECA's aesthetic has edges, mirroring the sharp detail lines of a freshly unboxed figure rather than the soft friendliness of a lifestyle brand. Spacing is utility-first: desktop grids run tight to surface maximum product thumbnails per row, and section padding compresses on mobile to keep imagery above the fold. The footer carries licensing attributions, trademark notices, and franchise partner links in structured columns — functionally heavy, legally necessary. The overall register is specialist retailer for an enthusiast audience: dense, image-forward, red-highlighted, and organized around deep-catalog navigation logic.

colors:
  primary: "#e83630"
  primary-active: "#c42820"
  primary-disabled: "#f5a9a7"
  ink: "#111111"
  body: "#32373c"
  muted: "#555555"
  muted-soft: "#808080"
  hairline: "#bbbbbb"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-dark: "#313131"
  surface-darkest: "#111111"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  brand-burgundy: "#600040"
  brand-navy: "#003050"
  brand-cobalt: "#4054b2"
  brand-red-alt: "#de4528"
  sale-badge: "#e83630"
  exclusive-badge: "#600040"
  new-badge: "#003050"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-primary:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-secondary:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  franchise-label:
    fontFamily: "'Open Sans', Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
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
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 42px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 9px 19px
    height: 42px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.muted}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 42px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 8px 12px
    height: 40px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-primary}"
    height: 52px
    borderBottom: "3px solid {colors.primary}"
  nav-bar-top-strip:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    height: 32px
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-secondary}"
    border: "1px solid {colors.hairline}"
    headerTypography: "{typography.franchise-label}"
    headerColor: "{colors.primary}"
    padding: "{spacing.lg}"
    columnGap: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    imageBg: "{colors.surface-soft}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.primary}"
    padding: "{spacing.sm}"
    hoverBorder: "1px solid {colors.hairline}"
    hoverShadow: "0 2px 8px rgba(0,0,0,0.12)"
  product-badge-new:
    backgroundColor: "{colors.new-badge}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
  product-badge-exclusive:
    backgroundColor: "{colors.exclusive-badge}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
  product-badge-sale:
    backgroundColor: "{colors.sale-badge}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 6px"
  hero-banner:
    backgroundColor: "{colors.surface-darkest}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    minHeight: 420px
    overlayGradient: "linear-gradient(to right, rgba(0,0,0,0.75) 40%, transparent)"
    ctaButton: "{components.button-primary}"
  franchise-banner:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-sm}"
    labelTypography: "{typography.franchise-label}"
    labelColor: "{colors.primary}"
    padding: "{spacing.xl} {spacing.xxl}"
    rounded: "{rounded.none}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 38px
    submitButtonBg: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
    submitButtonWidth: 42px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.xs}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    activeBg: "{colors.primary}"
    activeColor: "{colors.on-primary}"
  pagination:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    activeBg: "{colors.primary}"
    activeColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    height: 34px
    width: 34px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.muted-soft}"
    headingTypography: "{typography.franchise-label}"
    headingColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.primary}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"
  price-strikethrough:
    originalColor: "{colors.muted}"
    saleColor: "{colors.primary}"
    typography: "{typography.price-display}"

## Components

### Buttons

**`button-primary`** — Flat red (#e83630) block with 4px corners, uppercase Open Sans 700 at 14px with 0.5px tracking. The tight radius and uppercase treatment signals collector-retailer utility over lifestyle softness. Hover darkens to #c42820; disabled washes to a light pink (#f5a9a7) with cursor blocked. Used exclusively for add-to-cart, checkout, and primary CTAs.

**`button-secondary`** — White fill with a hairline border and matching uppercase type in body charcoal. Pairs with `button-primary` in two-button rows (e.g., "Add to Cart" + "Add to Wish List") where red must stay singular and dominant.

**`button-dark`** — Charcoal (#313131) fill on dark-surface contexts such as hero banners and franchise spotlight modules. Keeps CTAs legible without competing with the red voltage reserved for commerce actions.

### Navigation

**`nav-bar`** — Dark charcoal (#313131) bar, 52px tall, with a 3px red bottom border that functions as the brand's sole horizontal accent line. Primary link text is Open Sans 600 at 14px. A thinner secondary strip above carries account links and announcements in near-black (#111111) at caption scale. Franchise-organized mega menus drop on hover with a white panel, red uppercase column headers, and secondary-weight link lists — taxonomy depth prioritized over visual drama.

**`mega-menu`** — White canvas drop panel with 1px hairline border. Column headers use `franchise-label` style (11px, 700, 1px letter-spacing, uppercase) in red, organizing links by property (Aliens, Predator, Teenage Mutant Ninja Turtles, etc.). Gap between columns is `{spacing.xl}`.

### Product Card

**`product-card`** — Minimal white card with 1px soft hairline border and 4px radius. Product image sits on a light neutral (#eeeeee) swatch area to isolate the figure photography from the white card background. Title renders in `title-sm` (600 weight), franchise attribution in `franchise-label` style above the title in red. Price uses `price-sm` in primary red. On hover, shadow lifts (0 2px 8px rgba black 12%) to indicate interactivity. Badge chips (NEW / EXCLUSIVE / SALE) stack in the top-left corner of the image — flat, no-radius rectangles in navy, burgundy, or red respectively.

### Badges

**`product-badge-new`**, **`product-badge-exclusive`**, **`product-badge-sale`** — Three-color badge system: navy (#003050) for new releases, deep burgundy (#600040) for exclusives, and alert-red (#e83630) for sale pricing. All share the same flat rectangle treatment (0px radius, 11px 700 uppercase Open Sans, 3px 6px padding) so they read as a system rather than ad-hoc labels. Stacked vertically in the image corner when multiple apply.

### Hero Banner

**`hero-banner`** — Full-bleed dark panel (minimum 420px tall) with a left-anchored gradient overlay (75% black → transparent) over franchise photography. Heading uses `display-xl` (36px 700), subtext uses `body-md` in white. The CTA button is `button-primary`. No decorative shapes or patterns — photography and red carry all visual energy.

**`franchise-banner`** — Narrower spotlight module in brand navy (#003050) for mid-page franchise collections. Franchise label runs in `franchise-label` style in red above a `display-sm` heading in white, with a right-side product grouping.

### Search

**`search-bar`** — Inline text input (38px tall, 4px radius, hairline border) with a flush-right red submit button containing a white magnifier glyph. The red button extends the add-to-cart color signal into site-wide utility, making search feel like an active commerce gesture rather than a passive filter.

### Footer

**`footer`** — Charcoal (#313131) multi-column footer with a 3px red top border mirroring the nav bar. Column headers in `franchise-label` style (white, uppercase, 1px tracking), link lists in `body-sm` at muted-soft (#808080) with red hover state. Bottom legal strip carries trademark/licensing text at caption scale in near-black.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces mega-menu; hero banner crops to square with centered copy overlay; search bar expands full-width below nav strip |
| Tablet | 744–1128px | Two-column product grid; nav condenses to icon+label row with drawer-style franchise menu; hero banner restores landscape crop |
| Desktop | 1128–1440px | Three- to four-column product grid; full mega-menu on hover; hero banner at full height with left-anchored gradient overlay |
| Wide | > 1440px | Grid caps at 1440px max-width centered; five-column product grid available; franchise-banner modules stack side-by-side |

### Touch Targets

- All navigation links minimum 44×44px tap target on mobile and tablet
- Product cards link the entire card surface, not just the title text
- Pagination buttons minimum 34×34px, with 8px gap between items
- Badge chips are display-only and not individually interactive

### Collapsing Strategy

- Mega-menu collapses to a slide-in drawer organized by franchise at ≤ 1128px
- Breadcrumb truncates middle segments with an ellipsis on widths < 480px
- Product title truncates at two lines with ellipsis overflow; price always remains visible
- Hero banner subtext hides on mobile < 480px to preserve CTA above the fold
- Footer columns stack to two-column at tablet, single-column at mobile; legal strip moves below column stack

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface detected; system stacks (Open Sans, Arial, Helvetica) dominate — a custom NECA display face may exist but was not observed in extraction
- Several extracted colors (#f78da7, #7bdcb5, #00d084, #8ed1fc, #9b51e0, #fcb900, #ff6900) match WordPress Gutenberg editor default palette — these are almost certainly editor artifacts, not brand tokens; they have been excluded
- Meta theme-color is absent, so mobile browser chrome color is unspecified
- Exact nav bar height, mega-menu column count, and sticky behavior could not be confirmed from extraction alone
- Hover/focus animation timing (transition duration, easing) is not recoverable from color/font extraction
- Icon system glyph set (cart, wish-list, account, compare) unconfirmed; assumed standard ecommerce glyphs
