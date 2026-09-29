---
version: alpha
name: "Solo Stove"
source_url: "https://www.solostove.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Flame glow trapped in a browser tab. Solo Stove's digital presence opens on a near-white canvas (`#f9f9f9`, the single extractable surface tone) that recedes completely so full-bleed lifestyle photography — backyard fire pits haloed in amber light, steel drums venting clean smoke against dusk — does all the emotional selling. The brand's signature burnt orange (`#E8490F`) appears sparingly but decisively: primary CTAs, price call-outs, and the small flame mark in the header, mirroring the literal fire at the center of every product. Everything else stays in a tight charcoal-to-slate ink range (`#1A1A1A` through `#6B6B6B`) that reads as carbon steel cooled down. Typography is a clean geometric sans-serif loaded via JavaScript — the site sits behind Cloudflare challenge protection, so font-family extraction returned only generic `sans-serif` and `system-ui` stacks — but the visible rhythm is medium-weight headings at generous sizes (36–48px for hero display), relaxed body copy around 16px, and uppercase micro-labels on badges and product specs. Corners stay tight: buttons land at `{rounded.xs}` to `{rounded.sm}`, product cards at `{rounded.sm}`, and only avatar thumbnails and pill filters push to `{rounded.full}`. Generous vertical spacing (`{spacing.section}` between content blocks, `{spacing.xl}` inside cards) gives the layout a campsite-clearing openness — nothing crowds. The product-detail page is the true centerpiece: a sticky image gallery on the left, a spec-dense purchase column on the right, and a "Compare Fire Pits" horizontal scroll strip that reinforces the one-category-done-perfectly ethos. Below the fold, UGC review grids and "#SoloStove" social proof tiles keep the tone peer-to-peer rather than editorial. Navigation is flat — six to eight top-level links with dropdown mega-menus organized by product line (Fire Pits, Stoves, Grills, Pizza Ovens, Accessories) — reflecting a catalog that is wide enough to need hierarchy but shallow enough that one click reaches any PDP.

colors:
  primary: "#E8490F"
  primary-active: "#C93D0B"
  primary-disabled: "#F4A48A"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#6B6B6B"
  muted-soft: "#999999"
  hairline: "#D4D4D4"
  hairline-soft: "#E5E5E5"
  canvas: "#F9F9F9"
  surface-soft: "#F2F2F2"
  surface-card: "#FFFFFF"
  surface-dark: "#1A1A1A"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  on-surface-dark: "#F9F9F9"
  flame-accent: "#F5A623"
  success: "#2E7D32"
  error: "#D32F2F"
  star-rating: "#E8490F"
  sale: "#C93D0B"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-lg:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  spec-label:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.4px
    textTransform: uppercase
  button-lg:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  price:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  link:
    fontFamily: "'Solo Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
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
  hero: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    focusBorder: 1px solid {colors.ink}
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline-soft}
    padding: 0 {spacing.xl}
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  mega-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    borderTop: 1px solid {colors.hairline-soft}
    boxShadow: 0 8px 24px rgba(0,0,0,0.08)
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    imageAspectRatio: 1 / 1
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    bodyTypography: "{typography.body-sm}"
    gap: "{spacing.md}"
  product-card-hover:
    boxShadow: 0 4px 16px rgba(0,0,0,0.08)
    transform: translateY(-2px)
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-lg}"
    ctaComponent: button-primary
    minHeight: 600px
    padding: "{spacing.section} {spacing.xl}"
    textAlign: center
    overlay: "linear-gradient(to top, rgba(0,0,0,0.55) 0%, transparent 60%)"
  hero-split:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    ctaComponent: button-dark
    padding: "{spacing.section} {spacing.xl}"
    layout: "50/50 image-left text-right"
  category-card:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    imageAspectRatio: 4 / 3
    overlay: "linear-gradient(to top, rgba(0,0,0,0.5) 0%, transparent 50%)"
    padding: "{spacing.lg}"
    textPosition: bottom-left
  compare-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-sm}"
    itemTypography: "{typography.body-sm}"
    specTypography: "{typography.spec-label}"
    rounded: "{rounded.sm}"
    padding: "{spacing.section} 0"
    gap: "{spacing.lg}"
    layout: horizontal-scroll
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-bestseller:
    backgroundColor: "{colors.flame-accent}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  size-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    border: 1px solid {colors.hairline}
    selectedBorder: 2px solid {colors.ink}
    selectedBackgroundColor: "{colors.surface-card}"
  color-swatch:
    rounded: "{rounded.full}"
    height: 32px
    width: 32px
    border: 2px solid transparent
    selectedBorder: 2px solid {colors.ink}
    offset: 2px
  review-stars:
    filledColor: "{colors.star-rating}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: "{spacing.xxs}"
  review-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
    authorTypography: "{typography.title-sm}"
    dateTypography: "{typography.caption}"
  ugc-tile:
    rounded: "{rounded.sm}"
    imageAspectRatio: 1 / 1
    overlay: "linear-gradient(to top, rgba(0,0,0,0.35) 0%, transparent 40%)"
    captionTypography: "{typography.caption}"
    captionColor: "{colors.on-dark}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    iconColor: "{colors.muted}"
    placeholderColor: "{colors.muted-soft}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-surface-dark}"
    linkTypography: "{typography.link}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"
    columnGap: "{spacing.xl}"
    borderTop: none
  spec-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    rowPadding: "{spacing.md} 0"
    borderBottom: 1px solid {colors.hairline-soft}

## Components

### Buttons

**`button-primary`** — Full-width on mobile, auto-width on desktop. Background is the brand burnt orange (`{colors.primary}`); text is white at `{typography.button-lg}`. Hover darkens to `{colors.primary-active}`, adding a subtle 0 2px 8px shadow. Disabled state fades to `{colors.primary-disabled}` and drops to 60% text opacity. Corners sit at `{rounded.xs}` — firm and industrial, no pill shapes on action buttons.

**`button-secondary`** — Same dimensions as primary but inverted: white fill with a 1px `{colors.ink}` border and dark text. On hover the fill flips to `{colors.ink}` and text goes white, creating a clean toggle effect. Used for "Add to Cart" alternatives, comparison selectors, and secondary CTAs in hero splits.

**`button-dark`** — Charcoal (`{colors.surface-dark}`) fill with white text. Deployed on light-background hero splits and category landing pages where primary orange would compete with product photography. Hover adds a slight brightness shift to `#2A2A2A`.

**`button-text`** — No background, underlined ink-colored text. Used inline within body copy for "Learn More" and "View Details" links that need button-level tap targets without visual weight.

### Navigation

**`nav-bar`** — 64px-tall sticky header on white with a faint bottom hairline. Logo sits left, nav links centered or left-aligned at `{typography.nav-link}`, and utility icons (search, account, cart with badge count) cluster right. On scroll past the hero, the bar gains a `box-shadow: 0 1px 4px rgba(0,0,0,0.06)` for depth separation.

**`announcement-bar`** — Slim 40px dark bar above the nav carrying rotating promo messages ("Free Shipping on Orders $49+" / "Memorial Day Sale") in white `{typography.caption}`. Auto-cycles every 5 seconds with a crossfade transition.

**`mega-menu`** — Triggered on hover (desktop) or tap (mobile). Drops below the nav bar as a full-width panel with product-line columns (Fire Pits, Stoves, Grills, Pizza Ovens) each showing 3-4 thumbnail links. A featured image slot on the right highlights seasonal promotions or new arrivals.

### Product Cards

**`product-card`** — Square image container on `{colors.surface-soft}` background (products are photographed on light gray), followed by title in `{typography.title-sm}`, price in `{typography.price}`, and a color swatch row if multiple finishes exist. Hover lifts the card 2px with a soft shadow. Badge (`badge-sale`, `badge-new`, `badge-bestseller`) pins to the top-left of the image area with `{spacing.sm}` inset.

### Heroes

**`hero-banner`** — Full-viewport-width, minimum 600px tall, background is a lifestyle photograph (fire pit in use at dusk). A bottom-to-center gradient overlay (`rgba(0,0,0,0.55)`) ensures white headline text (`{typography.display-xl}`) and body copy (`{typography.body-lg}`) remain legible. A single `button-primary` CTA centers below the copy. On mobile the min-height drops to 480px and headline scales to `{typography.display-lg}`.

**`hero-split`** — 50/50 layout: product image on the left, text block on the right with heading at `{typography.display-lg}`, body at `{typography.body-md}`, and a `button-dark` CTA. Used on collection landing pages and seasonal campaign entries. Image slot carries a subtle parallax on desktop scroll.

### Category Cards

**`category-card`** — Rectangular (4:3) image cards with a bottom-gradient overlay and category name at bottom-left in `{typography.title-md}` white text. Used in a 2×2 or 3-column grid on the homepage below the hero. Hover brightens the overlay slightly and scales the image 1.02×.

### Compare Strip

**`compare-strip`** — Horizontal scroll of 3-5 product columns on a white background. Each column shows a product image, name, 3-4 key specs in `{typography.spec-label}` / `{typography.body-sm}` rows, price, and an "Add to Cart" `button-secondary`. Sticky header row keeps spec labels visible during horizontal scroll on mobile. Section heading in `{typography.display-sm}` sits above.

### Badges

**`badge-sale`** — Dark orange (`{colors.sale}`) pill with white uppercase text. Overlays product images on sale items.

**`badge-new`** — Black fill, white text. Used on newly launched products.

**`badge-bestseller`** — Warm amber (`{colors.flame-accent}`) fill with dark text, distinguishing top sellers without using the primary orange.

### Size & Color Selectors

**`size-selector`** — Inline row of bordered rectangles. Unselected items show 1px `{colors.hairline}` border; selected shows 2px `{colors.ink}` border with no fill change. Out-of-stock sizes dim to 40% opacity with a diagonal strikethrough line.

**`color-swatch`** — Circular swatches at 32px diameter. Selected swatch gains a 2px `{colors.ink}` ring with a 2px offset gap. Tooltip on hover shows color name.

### Reviews

**`review-card`** — White card with `{rounded.sm}` corners and a hairline border. Star row at top using `{colors.star-rating}` fill, followed by review text in `{typography.body-sm}`, author name in `{typography.title-sm}`, and date in `{typography.caption}` muted color. Cards stack vertically on mobile; 2-column masonry on desktop.

**`ugc-tile`** — Square image tile from social media with a bottom gradient overlay and `{typography.caption}` credit text. Used in a horizontal-scroll strip or 4-column grid labeled "#SoloStove".

### Search

**`search-bar`** — Appears in the nav bar on icon click as an expanding overlay. Light gray fill (`{colors.surface-soft}`) with a search icon left and clear button right. Autocomplete dropdown shows product thumbnails, category suggestions, and trending searches.

### Footer

**`footer`** — Dark background (`{colors.surface-dark}`) with 4-5 link columns (Shop, Support, About, Community, Legal) using `{typography.link}` in off-white text. Email signup input + `button-primary` CTA span the top row. Social icons in a horizontal row below the columns. Bottom bar carries copyright and legal links in `{typography.caption-sm}`.

### Spec Table

**`spec-table`** — Alternating-row table used on PDPs to display product specifications (weight, dimensions, material, BTU output). Labels in `{typography.spec-label}` uppercase left column, values in `{typography.body-sm}` right column. Rows separated by `{colors.hairline-soft}` bottom borders.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Hero min-height drops to 480px, headline scales to `{typography.display-lg}`. Nav collapses to hamburger + logo + cart icon. Product grid is 2-up. Compare strip scrolls horizontally. Footer columns stack vertically with accordion toggles. All CTAs go full-width. |
| Tablet | 744–1128px | Product grid shifts to 3-up. Hero maintains full height. Nav may remain collapsed or expand to partial link row. Split heroes stack image-above-text. Mega-menu shows 3 columns instead of 4. |
| Desktop | 1128–1440px | Full nav with all links visible. Product grid is 4-up. Split heroes display side-by-side 50/50. Mega-menu at full width. Sticky nav gains scroll shadow. Review cards in 2-column masonry. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Side padding increases to `{spacing.xxl}`. Product grid remains 4-up but cards grow slightly. Hero images span full viewport, text remains within max-width container. |

### Touch Targets
- All interactive elements meet 44×44px minimum tap area on mobile
- Size selector buttons have 12px gap between items to prevent mis-taps
- Color swatches maintain 8px gap minimum; hit area extends 4px beyond visible circle
- Nav hamburger icon is 48×48px with centered 24px glyph
- Footer accordion headers are 48px tall with full-width tap area

### Collapsing Strategy
- Navigation: full link bar → hamburger slide-out drawer with nested accordion for mega-menu categories
- Product grid: 4-up → 3-up → 2-up (never 1-up; products always pair)
- Compare strip: side-by-side columns → horizontal scroll with sticky left column for spec labels
- Hero split: side-by-side → image stacked above text block
- Footer: multi-column → single-column accordions with section headers as toggle triggers
- Spec table: side-by-side label/value → stacked label-above-value on narrow viewports
- UGC grid: 4-column → 2-column → horizontal scroll strip

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Color extraction severely limited**: The site is behind Cloudflare Managed Challenge (anti-bot), returning only `#f9f9f9` as an extractable color. The primary orange (`#E8490F`) is based on widely-documented Solo Stove brand identity but could not be verified from live CSS; the actual production value may differ by several stops.
- **Font family unconfirmed**: Only generic stacks (`sans-serif`, `system-ui`, `monospace`) were returned. The brand likely loads a custom or licensed geometric sans-serif via JavaScript; the `'Solo Sans'` placeholder used here is a guess — inspect the live site's network waterfall for the actual typeface name and metrics.
- **Exact spacing and sizing tokens unverified**: Padding, heights, and radii are estimated from common Solo Stove screenshots and DTC conventions. Production values may vary.
- **Dark-mode or seasonal themes**: Solo Stove may run seasonal dark-palette campaigns (e.g., Black Friday, winter solstice) that override the default canvas; no alternate theme tokens were extractable.
- **Animation and motion tokens**: Transition durations, easing curves, and scroll-triggered animations could not be captured. The site likely uses fade-in and parallax effects on hero imagery.
- **Platform not confirmed as Shopify**: The crawler returned `platform-shopify: False`, but Solo Stove has historically operated on Shopify Plus. The Cloudflare challenge may have prevented platform detection; Liquid template conventions may still apply.
- **Icon system**: Glyph set (likely a custom SVG sprite or icon font for cart, search, account, menu, fire-pit product icons) was not extractable.
