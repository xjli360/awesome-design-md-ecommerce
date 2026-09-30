---
version: alpha
name: "All-Clad"
source_url: "https://www.all-clad.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Stainless steel under studio lighting — that first visual impression of All-Clad's digital presence is a surface of muted charcoal (#19212c) and near-white (#f6f6f6) panels that mimic the reflective layers of bonded cookware. The primary action blue (#006bb4) reads as a Pantone-precise industrial marker rather than a playful accent; it anchors every "Add to Cart" button, filter link, and navigation active state with the understated confidence of a bolt torque spec printed on a factory wall. Body copy sets in Open Sans at 400 weight — light enough to disappear behind product photography yet sturdy at 14–16px on dense comparison grids where seven SKUs line up like pans on a pot rack. Headlines rarely exceed weight 600; the brand lets product imagery carry authority rather than typographic volume. A vivid orange (#ff5501) fires only on promotional callouts and sale badges — the single spike of warmth in an otherwise cool-neutral system, reminiscent of a burner ring glowing beneath brushed aluminum. Card components use tight `{rounded.xs}` corners (4px) or none at all, reinforcing the machined precision of tri-ply construction. Spacing is generous at section boundaries (`{spacing.section}` = 64px) but compressed within product cards (`{spacing.sm}` = 8px between price and rating), creating a rhythm of breathing room punctuated by information density. A warm cream surface (#fdf0d5) paired with amber type (#6f4400) appears in trust badges and warranty callouts — a brief nod to heritage craft before the interface returns to its steel-and-carbon palette. Navigation runs a single-row mega-menu against a white bar, all uppercase category labels in `{typography.nav-label}`, underline-on-hover rather than background highlight.

colors:
  primary: "#006bb4"
  primary-active: "#00699d"
  primary-disabled: "#a6d4e8"
  accent: "#ff5501"
  accent-hover: "#ff9635"
  ink: "#111111"
  dark: "#19212c"
  body: "#424242"
  muted: "#7d7d7d"
  muted-soft: "#8f8f8f"
  hairline: "#dbdbdb"
  hairline-soft: "#e4e4e4"
  border-medium: "#cfcfcf"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-alt: "#eeeeee"
  surface-warm: "#fdf0d5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-warm: "#6f4400"
  amber: "#c07600"
  error: "#e02b27"
  sale: "#c72935"
  success: "#4db6ac"

typography:
  display-xl:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-md:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-lg:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.3px
  nav-label:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-strike:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
    textDecoration: line-through
  badge:
    fontFamily: "'Open Sans', Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
  hero: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    borderWidth: 0
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    borderWidth: 1px
    borderColor: "{colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 12px
    height: 40px
    borderWidth: 1px
    borderColor: "{colors.border-medium}"
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.error}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    paddingHorizontal: "{spacing.xl}"
  nav-bar-mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg}"
    borderTop: 1px solid {colors.hairline-soft}
    boxShadow: 0 4px 12px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    imageAspectRatio: 1:1
    imageBackgroundColor: "{colors.surface-soft}"
  product-card-hover:
    boxShadow: 0 2px 8px rgba(0,0,0,0.1)
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price}"
    textColor: "{colors.sale}"
  product-card-original-price:
    typography: "{typography.price-strike}"
    textColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 480px
    padding: "{spacing.section}"
    ctaButton: button-accent
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    minHeight: 480px
    padding: "{spacing.section}"
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.none}"
    imageAspectRatio: 4:3
    padding: "{spacing.lg}"
  sale-badge:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  promo-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  trust-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.on-warm}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    borderWidth: 1px
    borderColor: "{colors.amber}"
  rating-stars:
    filledColor: "{colors.accent}"
    emptyColor: "{colors.hairline}"
    size: 14px
    gap: "{spacing.xxs}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    borderWidth: 1px
    borderColor: "{colors.border-medium}"
    iconColor: "{colors.muted}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 12px
    borderWidth: 1px
    borderColor: "{colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    borderWidth: 0
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.accent-hover}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-dark}"
    marginBottom: "{spacing.md}"
  warranty-callout:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.on-warm}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    borderLeft: 4px solid {colors.amber}
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 40px
    borderWidth: 1px
    borderColor: "{colors.border-medium}"
    buttonColor: "{colors.muted}"

---

## Components

### Buttons

**`button-primary`** — Solid blue (#006bb4) fill with white text, 4px radius, 44px height. On hover darkens to #00699d. Disabled state drops to 70% opacity with a washed-out blue. Used for primary commerce actions: "Add to Cart," "Apply," "Submit." Never stacked — only one primary button per viewport section.

**`button-secondary`** — White fill with a 1px black border, black text. On hover inverts to solid black with white text, creating a confident toggle effect. Used for secondary actions like "Compare," "View Details," or filter resets.

**`button-accent`** — Vivid orange (#ff5501) fill at a larger 48px height, reserved exclusively for promotional CTAs in hero banners and campaign modules. Hover warms to #ff9635. This button never appears in product grids or form flows.

### Navigation

**`nav-bar`** — 64px white bar with uppercase category labels in 13px/700 weight Open Sans, 0.5px letter-spacing. Active category shows a 2px bottom border in primary blue. Logo sits left, utility icons (search, account, cart with item count badge) right. Mega-menu drops below with a hairline divider and subtle shadow.

**`nav-bar-mega-menu`** — Full-width dropdown with three-column layout: category links left, featured product center, promotional image right. Background remains white; links in body gray hover to primary blue.

### Product Cards

**`product-card`** — Zero-radius container with 1:1 square product image on a light gray (#f6f6f6) background. Title in 16px/600 weight below, price in 18px bold. On hover gains a soft shadow (0 2px 8px). Sale items show original price struck through in muted gray alongside the new price in sale red (#c72935).

### Hero & Banners

**`hero-banner`** — Full-bleed dark (#19212c) background with white headline text in display-xl (36px/700), generous section padding. CTA uses the accent orange button. Lifestyle photography sits as a background image with a subtle dark gradient overlay ensuring text legibility.

**`hero-banner-light`** — Alternate light variant on #f6f6f6 with dark text, used for category landing pages and editorial content sections.

### Badges & Trust

**`sale-badge`** — Small red (#c72935) pill with uppercase white text at 11px. Positioned top-left on product card images with 4px radius.

**`promo-badge`** — Orange variant of the sale badge for non-discount promotions ("NEW", "BEST SELLER").

**`trust-badge`** — Warm cream (#fdf0d5) background with amber border and dark amber text. Used for warranty information, "Made in USA" callouts, and lifetime guarantee messaging.

**`warranty-callout`** — Larger block-level trust element with a 4px left amber border, cream background, and body-sized text. Appears on product detail pages near the add-to-cart section.

### Search & Filtering

**`search-bar`** — 44px input with 4px radius, medium gray border, and a magnifying glass icon in muted gray. On focus, border transitions to primary blue at 2px width.

**`filter-chip`** — Small bordered pills for active product filters. Default state has a hairline border; active state fills with primary blue and switches text to white.

### Rating & Reviews

**`rating-stars`** — 14px star icons filled in accent orange (#ff5501), empty stars in hairline gray. Displayed inline next to review count in caption text.

### Footer

**`footer`** — Dark (#19212c) full-width section with four-column link layout. Headings in 16px/600 white, links in 13px/400 white that warm to orange on hover. Contains newsletter signup input, social icons, and legal links at bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger menu replaces top nav categories, hero text drops to display-md (28px), sticky add-to-cart bar at bottom of PDP, mega-menu becomes full-screen slide-over |
| Tablet | 744–1128px | Two-column product grid, nav categories collapse to horizontal scroll, hero height reduces to 360px, filter panel becomes slide-out drawer |
| Desktop | 1128–1440px | Three- to four-column product grid, full mega-menu on hover, hero at full 480px height, sidebar filters visible on PLP |
| Wide | > 1440px | Content max-width caps at 1440px and centers, product grid holds four columns with increased card padding, hero imagery extends full bleed while text container remains centered |

### Touch Targets

- Minimum touch target 44×44px on all interactive elements
- Product card entire surface is tappable on mobile, not just the title link
- Filter chips maintain 8px gap to prevent mis-taps
- Quantity selector buttons are 40×40px with visible active states
- Mobile nav hamburger icon occupies 48×48px hit area

### Collapsing Strategy

- Desktop mega-menu categories collapse into an accordion within the mobile slide-over menu
- PLP sidebar filters move to a modal drawer triggered by a sticky "Filter" button
- Product detail tabs (Description, Specs, Reviews) collapse to stacked accordions on mobile
- Footer four-column grid stacks to single-column accordions with section headings as triggers
- Breadcrumbs truncate middle segments with "..." on mobile, showing only parent and current

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom icon font `allclad-icons` glyph mapping not extractable — icon names and codepoints unknown
- Exact hero image overlay gradient values not captured from static extraction
- Mega-menu column widths and featured product slot dimensions require live measurement
- Several extracted blues (#006bb4, #1979c3) may be Magento platform defaults rather than brand-specified tokens — the site runs on Magento and these colors appear in its default theme
- No custom brand typeface detected; Open Sans appears to be the sole web font, but a display face may load conditionally via JS
- Transition/animation durations and easing curves not available from static color/font extraction
- Product image zoom behavior and lightbox overlay styling not captured
- Mobile-specific promotional banner rotation timing unknown
