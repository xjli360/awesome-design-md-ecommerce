---
version: alpha
name: "Egg Press"
source_url: "https://eggpress.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every Egg Press product page starts on #f7f5ec — the exact shade of warm cream that comes off a cotton-rag stock after it's run through a letterpress — and that single material choice sets the entire system's logic. Against that ground, #ff7e05 arrives without softening toward peach or warming toward amber: a raw construction-site orange that drives every primary CTA, hover state, and sale marker, the one color in the palette that refuses to recede. It reads as deliberate disruption, which is precisely the move a greeting card brand needs when the product itself is doing the whimsy. The dark warm brown (#513f37) serves as secondary text and dark-surface fill — the color of dried ink on a compositing table — keeping the brand from reading clinical when it needs contrast. Two blues complete the extraction: #5183a3, a faded steel that plausibly handles link text or accent bars, and #8dc6d3, a softer powder present in illustration or spot-color detail. Typography extraction returned empty — the site almost certainly pulls its typeface via Shopify asset injection past the extraction layer — so this spec proxies with a classical serif, Georgia-first, consistent with the hand-set letterpress character the brand presents in all print photography. Buttons run in small uppercase with generous letter-spacing ({typography.button-md}), a nod to traditional type-setting where spacing between cast letters reads as intentional craft rather than carelessness. Card corners hold at {rounded.xs}, treating the interface the way a freshly cut card stock demands: clean, un-softened edges with no pill-shape softness. Navigation stays compact and understated, letting the grid of illustrated cards carry the visual weight. At {spacing.section} intervals, section breaks open the page so photography can breathe against the cream ground without competing with the orange signal color.

colors:
  primary: "#ff7e05"
  primary-active: "#d96800"
  primary-disabled: "#ffd4a8"
  ink: "#121212"
  body: "#404040"
  muted: "#513f37"
  muted-soft: "#8a7a75"
  hairline: "#dedede"
  canvas: "#f7f5ec"
  surface-soft: "#f0ede2"
  surface-card: "#ffffff"
  surface-dark: "#513f37"
  on-primary: "#ffffff"
  on-dark: "#f7f5ec"
  accent-steel: "#5183a3"
  accent-sky: "#8dc6d3"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.14
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  title-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.68
    letterSpacing: 0
  body-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.3px
  button-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 2px
    textTransform: uppercase
  button-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 2px
    textTransform: uppercase
  nav-link:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
  price:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  category-label:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 2.5px
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
    hoverEffect: image-scale-subtle
    boxShadow: none
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaButton: button-primary
    paddingY: "{spacing.xxl}"
    layout: split-image-right
  collection-hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    paddingY: "{spacing.xl}"
    textAlign: center
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.category-label}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
  category-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.category-label}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    positionAbsolute: top-left
  breadcrumb:
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.accent-sky}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.category-label}"
    paddingY: "{spacing.xxl}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    height: 40px
    iconColor: "{colors.muted}"
    placeholderColor: "{colors.muted-soft}"
  tag-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 10px
    border: "1px solid {colors.hairline}"

## Components

### Buttons

**`button-primary`** — The main conversion action fills with #ff7e05 and carries white text in small 13px uppercase at 2px letter-spacing, landing closer to a letterpress label than a standard web CTA. Hover darkens the fill to #d96800 with no transition easing change; disabled fades to #ffd4a8 and blocks pointer interaction. Corners sit at {rounded.xs} (4px) — the brand treats rounding the way a print shop treats die cuts: minimal, structural, never decorative.

**`button-secondary`** — Hollow counterpart to primary: transparent fill with a 1px solid ink (#121212) border and identical uppercase treatment. Used where the orange would be too insistent — "View All Cards," "Learn More," pagination. On hover the border can thicken to 2px or the fill can shift to surface-soft for a subtle press effect.

**`button-text-link`** — Inline text action in warm brown (#513f37) with underline, no border, no background. Appears inside product descriptions, navigation submenus, and "See all" links at section footers. The warm brown distinguishes it from body copy (#404040) without introducing a third typeface.

### Navigation

**`nav-bar`** — 64px tall, canvas cream background, bottom hairline at #dedede separating it from page content. Links render in Georgia 14px with 0.5px letter-spacing — quiet but legible against the cream. Logo likely renders as a wordmark or simple icon in ink (#121212). Cart count badge uses primary orange as the indicator dot. An announcement bar above the nav occupies 36px in dark warm brown (#513f37) with reversed cream text centered, used for promotions and shipping thresholds.

### Product Card

**`product-card`** — White card surface against the cream page canvas so the card edge reads as a subtle lift without a drop shadow. Image fills a 3:4 portrait ratio, natural for greeting card proportions. Product name in body-sm (#121212) and price in price-scale type directly below, no star ratings or review counts cluttering the grid. On hover the image scales to approximately 1.03× over 200ms — subtle enough to signal interactivity without animation theatrics. Corners at {rounded.xs}.

### Hero

**`hero`** — Split layout: editorial copy on the left, photography or product flat-lay on the right, both sitting on the #f7f5ec canvas. Headline in display-xl (42px serif), followed by one to two lines of body-md copy, then a primary button. Vertical padding at {spacing.xxl}. No dark overlay, no full-bleed image — the brand keeps heroes airy and lets the orange CTA do the converting.

**`collection-hero`** — Single-column text header for category and collection pages. Display-md headline (28px) centered over surface-soft (#f0ede2), paddingY at {spacing.xl}. No imagery in the header; the product grid immediately below carries the visual weight. Optional category-label subtitle in uppercase above the headline to orient the shopper.

### Filters and Badges

**`category-pill`** — Rounded-full filter pills for the product grid. Inactive: surface-soft fill, hairline border, category-label uppercase in #404040. Active inverts to ink fill with canvas cream text. No animation on state change — swap is instantaneous, consistent with the print-shop directness of the brand.

**`sale-badge`** — Sharp-cornered orange tag ({rounded.none}) positioned absolute top-left on product card images. Orange fill (#ff7e05), white text in button-sm uppercase. Communicates SALE, NEW, or LIMITED without softening into a pill. Sits flush against the image corner with 4px padding.

**`tag-chip`** — Non-interactive product attribute label ("Blank Inside," "Set of 8," "Letterpress"). No rounding, surface-soft fill, hairline border, caption typography. Appears in a horizontal row below the product title on detail pages.

### Footer

**`footer`** — Dark warm brown background (#513f37) closes the page like a colophon closes a hand-printed book. Column headings in category-label (10px, 2.5px tracking, uppercase); body links in body-sm. Link color shifts to accent-sky (#8dc6d3) for legibility against the brown, providing a visual surprise that connects back to the extracted blue accent. Generous vertical padding at {spacing.xxl}.

### Search

**`search-bar`** — White fill, hairline border, {rounded.xs} corners, 40px height for compact nav placement. Icon in muted brown (#513f37); placeholder text in muted-soft (#8a7a75). Expands from a collapsed icon state on mobile; sits inline in the nav on desktop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart icon; hero stacks vertically with image above copy; announcement bar wraps to two lines if needed; filters move to a slide-up bottom sheet |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories horizontally with hamburger overflow for sub-categories; hero maintains split layout at display-md scale instead of display-xl |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with dropdown or mega-menu; hero at full display-xl scale; filter sidebar appears inline left of grid |
| Wide | > 1440px | Max content width ~1280px centered with increasing side padding; product grid holds at four columns; hero imagery caps at 640px wide to avoid over-scaling illustrated photography |

### Touch Targets
- All buttons minimum 48px tall, 48px wide
- Category pill filters minimum 44px tall on mobile
- Nav items in mobile drawer minimum 52px tall for thumb clearance
- Add-to-cart button runs full-width on mobile product detail pages
- Cart icon, hamburger, and search icon minimum 44×44px hit areas

### Collapsing Strategy
- Nav dropdown collapses to a flat accordion inside the mobile side drawer
- Product filter row on desktop becomes a bottom-sheet on mobile triggered by a "Filter" button above the grid
- Footer four-column layout stacks to single-column at mobile breakpoint; column headings become accordion toggles
- Hero split layout stacks vertically at tablet breakpoint; image moves above the copy block
- Breadcrumb truncates to show only the immediate parent category on mobile widths

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font-family stack was extracted; the site almost certainly loads its typeface via Shopify asset injection. This spec uses Georgia as a serif proxy consistent with the brand's letterpress aesthetic. Actual typefaces should be confirmed by inspecting network requests in DevTools under the Fonts filter.
- `primary-disabled` (#ffd4a8), `muted-soft` (#8a7a75), and `surface-soft` (#f0ede2) are derived by lightening or adjusting extracted palette values — they were not directly observed in the extraction and must be validated against the live site.
- `surface-dark` (#513f37) is confirmed in the extraction but its precise UI roles (footer fill, announcement bar, or other dark surfaces) are inferred from brand convention rather than confirmed markup inspection.
- Accent colors #5183a3 and #8dc6d3 were present in the extraction but their specific component roles — links, illustration spot color, section backgrounds — could not be determined from the extraction alone; treat as provisional.
- Icon system (SVG sprite, inline SVG, or icon font) was not captured; nav, cart, and search icons follow standard Shopify theme conventions here but are not formally specified.
- Hover transitions, focus ring styles, and animation timing functions are inferred rather than extracted; no CSS custom property values for easing or duration were available.
- Breakpoint values use standard Shopify Dawn theme defaults (744px, 1128px); actual breakpoints should be confirmed against the deployed theme's CSS.
- No type-scale evidence for mobile-specific font sizes; display-xl at 42px may need to step down to 28–32px at mobile widths — this should be confirmed against the live responsive behavior.
