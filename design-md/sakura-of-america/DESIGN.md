---
version: alpha
name: "Sakura of America"
source_url: "https://www.sakuraofamerica.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pigma Micron pens leave a very particular mark — a deep, slightly maritime teal sitting somewhere between inkwell and tide pool, and that same hue, #226d7a, anchors every primary action on Sakura of America's site, from add-to-cart buttons to nav hover states. The palette barely strays from this teal family: a near-identical sibling (#1e6d7a) handles pressed states, a charged cyan volt (#22b8d1) fires only on hover highlights and accent stripes, and at the far end a powder wash (#e4f5fa) lifts section backgrounds off white — giving the catalog a watercolor-paper lightness appropriate for a brand whose product line spans Cray-Pas oil pastels, Gelly Roll gel pens, and archival Micron inks in sixty-plus colors.

  Typography leans on Open Sans at a catalog-appropriate scale: display headings run at 32px/700 while button labels and nav links stay at 14–15px/600, letting broad product grids speak louder than typographic drama. Corner rounding is spare and intentional — product cards at {rounded.sm}, buttons at {rounded.xs}, category filters at {rounded.full} — echoing the rectilinear geometry of pen barrels, ink bottles, and pastel sticks. The {colors.surface-soft} wash (#e4f5fa) recurs throughout the layout as chip backgrounds, spec-table alternating rows, and promo banner fills, tying every secondary surface back to the single teal brand voltage without introducing an unrelated neutral. Grid density is high: six product columns on desktop with tight {spacing.sm} gutters, designed for buyers who already know whether they need a 0.1mm or 0.5mm Micron nib and expect the catalog to let them find it fast.

colors:
  primary: "#226d7a"
  primary-active: "#1e6d7a"
  primary-disabled: "#8ab8c0"
  primary-light: "#b0e0e9"
  primary-wash: "#e4f5fa"
  accent-cyan: "#22b8d1"
  ink: "#1f2324"
  body: "#3c3c3c"
  muted: "#717171"
  hairline: "#d0e8ed"
  hairline-soft: "#eaf3f6"
  canvas: "#ffffff"
  surface-soft: "#e4f5fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  error: "#c0392b"
  success: "#1e8a4c"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.41
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  price-display:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: 0
  pill-label:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.3px

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
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 1.5px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    hoverBackgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 10px 14px
    height: 42px
    focusBorderColor: "{colors.primary}"
    focusRingColor: "{colors.primary-light}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottomColor: "{colors.hairline}"
    borderBottomWidth: 1px
    height: 64px
    activeTextColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline-soft}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.md}"
    hoverBorderColor: "{colors.primary-light}"
    hoverShadow: "0 2px 12px rgba(34,109,122,0.10)"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 420px
    accentColor: "{colors.accent-cyan}"
    padding: "{spacing.xxl} {spacing.section}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.pill-label}"
    rounded: "{rounded.full}"
    borderColor: "{colors.primary-light}"
    borderWidth: 1px
    padding: 6px 14px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  product-badge:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.primary-light}"
    borderWidth: 1px
    rounded: "{rounded.full}"
    typography: "{typography.body-md}"
    padding: 10px 20px
    iconColor: "{colors.primary}"
    focusBorderColor: "{colors.primary}"
    height: 42px
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    headerTextColor: "{colors.primary}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.body}"
    borderColor: "{colors.hairline}"
    rowAlternateBackground: "{colors.primary-wash}"
  swatch-chip:
    borderRadius: "{rounded.full}"
    borderColor: "{colors.hairline}"
    borderWidth: 1.5px
    size: 24px
    activeBorderColor: "{colors.primary}"
    activeBorderWidth: 2.5px
  promo-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    borderTopColor: "{colors.primary-light}"
    borderTopWidth: 3px
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTextColor: "{colors.primary-light}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    borderTopColor: "{colors.accent-cyan}"
    borderTopWidth: 3px
    padding: "{spacing.xl} 0"

## Components

### Buttons
**`button-primary`** — Deep teal ({colors.primary}, #226d7a) fill with white label at {typography.button-md} (15px/600 weight) and {rounded.xs} (4px) corner radius, fixed at 44px height. Hover shifts to the near-identical sibling {colors.primary-active} (#1e6d7a) — the delta is subtle but sufficient at this saturation level. Disabled state uses the desaturated {colors.primary-disabled} (#8ab8c0) at unchanged geometry.

**`button-secondary`** — White fill with a 1.5px {colors.primary} border and teal-colored text at {typography.button-md}. Hover floods the surface with {colors.surface-soft} (#e4f5fa) to confirm interactivity without losing the outline. Shares height (44px) and {rounded.xs} with the primary for visual alignment on dual-CTA rows (e.g., "Add to Cart" + "Add to Wishlist").

**`button-ghost`** — Transparent background with {colors.primary} text at {typography.button-sm}. Used for "View All" links, pagination controls, and secondary navigation actions where a bordered button would carry too much visual weight.

### Navigation
**`nav-bar`** — 64px white bar with a 1px {colors.hairline} bottom border. Links use {typography.nav-link} (14px/600) and shift to {colors.primary} on hover or active state. The compact height prioritizes product-grid real estate; mega-dropdown panels should use {colors.surface-soft} backgrounds to stay within the teal color family.

### Product Card
**`product-card`** — White card with a 1px {colors.hairline-soft} border, {rounded.sm} (8px) corners, and {spacing.md} internal padding. Title uses {typography.title-sm}, price uses {typography.price-display}, and secondary metadata such as SKU or tip size uses {typography.caption}. On hover, the border transitions to {colors.primary-light} (#b0e0e9) with a faint teal box-shadow (0 2px 12px rgba(34,109,122,0.10)), surfacing the card without an aggressive lift. Badges sit top-left using `product-badge` or `product-badge-new` geometry.

### Hero Banner
**`hero-banner`** — Full-bleed {colors.primary} section with white ({colors.on-primary}) display text at {typography.display-xl} (32px/700), minimum height 420px. The charged cyan {colors.accent-cyan} (#22b8d1) appears as a decorative stripe or inline CTA button within the hero zone, providing a single voltage pop against the deep teal ground. Sub-headline copy runs {typography.body-md} at {colors.on-primary}.

### Search
**`search-bar`** — Pill-shaped ({rounded.full}) input on {colors.surface-soft} with a {colors.primary-light} border and a {colors.primary} search icon. Gains a solid {colors.primary} border ring on focus. Designed for the header row on desktop and a full-width position below the nav bar on mobile.

### Spec Table
**`spec-table`** — Used for nib-size, ink-type, and archival-rating comparison grids on product detail pages. Header row uses {colors.surface-soft} fill with {typography.spec-label} (11px/uppercase/600) in {colors.primary}. Alternating data rows fill with {colors.primary-wash} (#e4f5fa) to reinforce brand color without impeding readability. Cells use {typography.body-sm} at {colors.body}.

### Color Swatches
**`swatch-chip`** — 24px circular chips ({rounded.full}) for displaying ink or gel-pen color variants. Default state shows a 1.5px {colors.hairline} ring; selected state upgrades to a 2.5px {colors.primary} ring so the active swatch reads clearly against any fill value, including near-white swatches. On mobile, tappable area expands to a 40px minimum via transparent padding.

### Category Pills
**`category-pill`** — {rounded.full} pill with {colors.surface-soft} fill and {colors.primary} text for inactive state; active pills invert to solid {colors.primary} fill with {colors.on-primary} text. Used for product-line filter rows (Pigma Micron, Gelly Roll, Cray-Pas, Koi Watercolor) sitting above the product grid, communicating state change without a heavy selected indicator.

### Promotional Banner
**`promo-banner`** — Slim {colors.surface-soft} strip at the top of the viewport for shipping thresholds and seasonal sale announcements. A 3px {colors.primary-light} top border, {typography.body-sm} text in {colors.primary}, and tight {spacing.sm} vertical padding. Dismissible with a small X icon.

### Footer
**`footer`** — {colors.primary} fill matching the hero, with {colors.on-primary} headings at {typography.title-sm} and {colors.primary-light} (#b0e0e9) for all navigation and policy links. A 3px {colors.accent-cyan} top border creates a bright teal seam separating body canvas from footer. Column layout uses {typography.body-sm} with {spacing.xl} top and bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero shrinks to 280px min-height; search bar goes full-width below nav; spec tables scroll horizontally |
| Tablet | 744–1128px | Two–three column product grid; filter pills scroll horizontally above the grid; nav shows logo + search + cart only |
| Desktop | 1128–1440px | Six-column product grid; persistent left filter sidebar; full nav-bar with mega-dropdown categories |
| Wide | > 1440px | Content centered in ~1400px max-width container; grid stays at six columns with wider gutters |

### Touch Targets
- All interactive buttons minimum 44 × 44px touch target
- Swatch chips expand from 24px display size to a 40px tap target via transparent padding on mobile
- Category pills gain {spacing.sm} extra vertical padding on touch devices for comfortable thumb navigation
- Mobile drawer nav links use full-width rows at minimum 48px height

### Collapsing Strategy
- Desktop mega-menu collapses to a full-screen slide-in drawer with accordion sections on mobile
- Six-column product grid steps to three columns at tablet and two at mobile; card image aspect ratio holds at 4:3 throughout
- Spec tables become horizontally scrollable at < 600px with the product-name column pinned left
- Hero banner drops the decorative cyan accent stripe on mobile to preserve headline breathing room
- Promo banner wraps to two lines on mobile rather than truncating copy

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Dark neutral palette (ink, body, muted) was not present in extracted colors — values (#1f2324, #3c3c3c, #717171) are contrast-safe defaults that should be verified against the live site once accessible
- Font extraction returned only generic stacks (Arial, Open Sans, Roboto); no brand-specific or licensed display typeface was identified — DESIGN.md assumes Open Sans as primary; confirm whether a custom web font loads via JavaScript on the live site
- Site returned a 403 Forbidden response, so no layout screenshots, navigation structure, or component-level HTML were available for inspection
- Mega-menu structure and product taxonomy depth are unknown — the nav-bar component will likely need extension once live site access is restored
- No form validation, error, or success state colors were extracted; error (#c0392b) and success (#1e8a4c) are WCAG-compliant defaults, not confirmed brand values
- Imagery art direction (lifestyle photography vs. flat-lay product vs. color-swatch grids) could not be confirmed from the blocked page response
- Exact grid column counts and gutter widths are inferred from catalog-site conventions rather than extracted measurements
