---
version: alpha
name: "Burgon & Ball"
source_url: "https://www.burgonandball.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sheffield steel against an #abb837 chartreuse — the specific yellow-green of new growth on an overcast northern English morning — anchors every product photograph and primary CTA on burgonandball.com, a deliberate inversion of the beige-and-brown rusticity that garden brands typically reach for. The deep navy #204a80 arrives as structural counterweight: the navigation bar, section anchors, and trust-mark backgrounds hold the composition while the lime-tinged green does the emotional work. Near-black #121212 carries all body copy with genuine ink depth, and a single warm gray #dedede handles hairlines and card strokes, present but thin as folded muslin. Buttons inherit {rounded.sm} geometry — noticeably soft without becoming pill-shaped — consistent with a brand whose products have ash handles and forged Sheffield heads; there is nothing aggressive about the corner radius here. Navigation sits in a #204a80 deep-navy bar that grounds the page immediately, with #abb837 surfacing as hover indicators and active states, creating a chlorophyll-and-indigo rhythm that recurs in product badges and section underlines. The catalogue is organized around use-case — borders, digging, harvesting, planting — so the top-level nav reads like a potting-shed drawer index rather than a retail taxonomy, unhurried and confident. Product cards carry a {rounded.xs} border and a quiet #dedede stroke; photography is wide and tool-forward, letting spade geometry and patinated steel carry the texture. Typography could not be recovered from extraction — the brand loads typefaces through Shopify's JS asset pipeline — but on-screen proportions suggest a condensed display face for hero and category headers paired with a neutral grotesque for product descriptions and pricing. Spacing is generous at section level and tight at component level, echoing the pace of a manufacturer that has been making garden tools since 1730 and has never needed to shout.

colors:
  primary: "#abb837"
  primary-active: "#8a9a2a"
  primary-disabled: "#d4dc8e"
  accent: "#204a80"
  accent-active: "#163569"
  accent-muted: "#3a6aaa"
  ink: "#121212"
  body: "#2d2d2d"
  muted: "#5e5e5e"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f6f6f4"
  surface-card: "#ffffff"
  surface-dark: "#204a80"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-upper:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.1px
  price-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
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
    rounded: "{rounded.sm}"
    padding: 13px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.accent}"
    border: "2px solid {colors.accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 22px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.accent-active}"
    border: "2px solid {colors.accent-active}"
    rounded: "{rounded.sm}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 10px 14px
    height: 44px
    focus-borderColor: "{colors.accent}"
    placeholder-textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    logo-maxHeight: 40px
    active-indicator-color: "{colors.primary}"
  nav-bar-top:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "4/3"
    padding: "{spacing.md}"
    shadow: "0 1px 4px rgba(0,0,0,0.06)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-md}"
    textColor: "{colors.ink}"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 480px
    paddingX: "{spacing.xxl}"
    paddingY: "{spacing.section}"
    overlayColor: "rgba(18,18,18,0.38)"
  hero-eyebrow:
    typography: "{typography.caption-upper}"
    textColor: "{colors.primary}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.canvas}"
  category-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    height: 40px
    typography: "{typography.body-sm}"
    focus-borderColor: "{colors.accent}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    headingColor: "{colors.primary}"
    headingTypography: "{typography.caption-upper}"
    bodyTypography: "{typography.body-sm}"
    paddingY: "{spacing.section}"
    dividerColor: "{colors.muted}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    accentBorderColor: "{colors.primary}"
    accentBorderWidth: 3px
    paddingBottom: "{spacing.sm}"
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    paddingY: "{spacing.xl}"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.xxl}"
    accentColor: "{colors.primary}"

## Components

### Buttons

**`button-primary`** — The main CTA fills with #abb837 chartreuse green at 48px tall with {rounded.sm} corners; white text in a 600-weight, 15px grotesque. On hover the fill deepens to #8a9a2a without changing geometry, confirming the action without drama. The disabled state uses the pale #d4dc8e wash with white text, visually retiring the affordance rather than merely graying it. This button appears on PDPs as "Add to Basket," on category pages as "Shop Now," and on the homepage hero alongside a secondary option.

**`button-secondary`** — White fill with a 2px #204a80 navy border and matching navy text at the same 48px height and {rounded.sm} rounding. Active state shifts border and text to #163569. Paired with `button-primary` on hero and gift-guide layouts where two equal-weight choices need visual separation without hierarchy ambiguity.

**`button-accent`** — Solid #204a80 fill with white text, same sizing as `button-primary`. Used in hero banners, dark-background editorial sections, and the nav-bar call-to-action where the green primary would compete with photography or disappear against navy backgrounds.

### Navigation

**`nav-bar`** — A solid #204a80 deep-navy bar at 64px that creates an immediate, confident ground plane. The Burgon & Ball wordmark appears reversed in white on the left; primary navigation links in {typography.nav-link} weight 500 sit in the center or right rail, also white. The active-page underline or hover indicator surfaces #abb837 chartreuse, so the chlorophyll-and-indigo pairing recurs at the top of every page as a structural signature. Dropdown menus open against a white card with {rounded.xs} at the dropdown edge.

**`nav-bar-top`** — A slim 36px announcement rail in near-black #121212 that sits above the main nav bar. Single-line centered copy in {typography.caption} white carries delivery thresholds, seasonal offers, or store news. On mobile this bar either collapses or displays a condensed single icon with tooltip.

### Product Card

**`product-card`** — White surface with a {rounded.xs} 4px corner and a 1px #dedede border; a faint 6% black box-shadow lifts each card from the grid without drama. Photography occupies a 4:3 aspect ratio — tool-only studio shots or hand-in-glove lifestyle — and bleeds edge to edge within the card bounds. The product title renders directly below in {typography.title-sm} at weight 600; pricing in {typography.price-md} (Georgia serif, 20px/700) anchors the lower area. Badges — category green or sale navy — overlap the upper corner of the image at 8px inset. On hover a subtle shadow lift (4px → 8px Y offset) signals interactivity without animation over-engineering.

### Hero Banner

**`hero-banner`** — Full-width, minimum 480px tall, over field or studio photography dampened by a 38% black scrim so that display text remains legible across all images. The eyebrow sits first: {typography.caption-upper}, 11px, weight 700, letter-spacing 1.2px, uppercase, in #abb837, functioning as a collection label or heritage callout ("Sheffield since 1730", "RHS Partner Collection"). The headline follows in {typography.display-xl} — 42px Georgia serif, weight 700, white — then a single line of {typography.body-md} supporting copy in white at reduced opacity (80%). The primary CTA in `button-primary` sits below; a ghost button with white border sometimes accompanies it for browse-path navigation.

### Badges

**`category-badge`** — Filled #abb837 green, white text, {rounded.xs}, 11px uppercase with 0.6px tracking. Denotes product family or collection membership (e.g. "RHS Collection", "Stainless", "Soft Grip"). By reserving green for collection context and not for promotions, the brand keeps the primary color non-transactional. **`sale-badge`** — Identical geometry, filled #204a80 navy, used for "Sale" or "New" promotional states, maintaining the navy-as-structural reading rather than introducing a third red.

### Breadcrumb

**`breadcrumb`** — Lightweight trail in {typography.caption} at 12px, {colors.muted} text (#5e5e5e), separated by a thin #dedede chevron or slash. Sits between the nav bar and the page header on collection and product pages. The current page renders in {colors.ink} at weight 600 to orient the visitor without a second visual element.

### Search

**`search-bar`** — 40px, {rounded.sm}, 1px #dedede border at rest with focus shift to the #204a80 accent. Placeholder text in {colors.muted}. On mobile the search icon in the nav is a 44×44px tap target that expands to a full-width overlay input with a white background; on desktop a contained search field sits inline or in a flyout panel.

### Trust Strip

**`trust-strip`** — A {colors.surface-soft} (#f6f6f4) band that runs full-width beneath the hero, carrying three or four icon-plus-label pairs: manufacture heritage, RHS partnership, return policy, and delivery terms. Icon strokes render in #abb837 green at roughly 24×24px; labels in {typography.body-sm}. 32px top and bottom padding. On mobile the strip converts to a 2×2 tile grid; on wide desktop all four sit in a single flex row with equal spacing.

### Section Heading

**`section-heading`** — Used above product grids, editorial modules, and collection previews. The heading renders in {typography.display-md} — Georgia, 28px, weight 600, {colors.ink} — with a 3px bottom border in #abb837 green that underlines only the text block width rather than the full container, functioning as a small brand punctuation mark that ties section identity to the primary palette without a full color fill.

### Collection Header

**`collection-header`** — A {colors.surface-soft} band above the product grid on category pages. Contains a collection title in {typography.display-md}, a one-to-two sentence description in {typography.body-md}, optional breadcrumb, and active-filter chips. The {colors.primary} accent appears as a 3px left border on any active filter tag and as the checkmark inside filter checkboxes.

### Announcement Bar

**`announcement-bar`** — 36px full-width in #121212, a single centered line in {typography.caption} white. Used for shipping offers, seasonal promotions, or event notices. Optionally dismissible via a small × icon at the right edge; dismissed state is stored in session to avoid re-appearing on navigation.

### Footer

**`footer`** — Full-width #121212 near-black ground. On desktop: four-column link grid with section headings in {typography.caption-upper} at #abb837 green and links in {typography.body-sm} at #dedede. A thin hairline divides the grid from the legal/copyright row. Logo reversed in white repeats in the footer brand bar. On mobile, link columns collapse to tap-to-expand accordions with a chevron indicator.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav-bar collapses to hamburger + wordmark + cart icon; hero headline reduces to ~26px; trust strip becomes a 2×2 tile grid; footer link groups accordion; announcement bar single line or hidden if overflowing |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories only with overflow in hamburger; hero headline at ~34px; trust strip 2-column flex row; section headings step down one scale |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with hover dropdowns; hero at full 42px; trust strip four-item single row; `section-heading` at full {typography.display-md} |
| Wide | > 1440px | Content constrained to ≈1440px max-width centered; side gutters in {colors.canvas}; no column count increase beyond desktop; hero photography crops centrally |

### Touch Targets
- All primary interactive elements (buttons, nav items, badge chips, card tap areas) minimum 44×44px.
- Footer links padded to 44px touch height with {spacing.md} vertical gap between rows.
- Mobile search icon expands to full-width overlay — the icon itself is a 44px square tap target.
- Cart and account icons in collapsed nav each receive 44px square touch areas with no overlap.
- Filter tags on collection pages minimum 36px height with {spacing.sm} horizontal padding on each side.

### Collapsing Strategy
- Primary nav collapses to hamburger drawer at < 1128px; drawer slides from left over a {colors.surface-dark} overlay.
- Product grids: 4-col → 3-col → 2-col → 1-col at breakpoints 1440 → 1128 → 744 → 0.
- Section headings reduce one typographic step at < 744px: {typography.display-md} (28px) becomes {typography.title-md} (18px).
- Trust strip converts from horizontal flex row to 2×2 grid at < 744px, and scrolls horizontally at < 480px.
- Announcement bar collapses or hides at < 375px if copy cannot fit on a single line.
- Footer four-column grid collapses to two columns at tablet and single-column accordions at mobile.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No font families extracted** — Shopify's JS asset pipeline loads typefaces at runtime, blocking CSS-level extraction. All typography stacks in this file use Georgia serif + system grotesque as informed placeholders; actual brand fonts must be confirmed by inspecting loaded network resources in browser DevTools (look for woff2 requests on the Network tab).
- **Only four hex values captured** — Extraction yielded #dedede, #204a80, #abb837, and #121212. Hover-state derivatives, error and success indicator colors, form focus rings, and surface tints are all mathematically derived or inferred; they should be confirmed against the live site or a Shopify theme source file.
- **No spacing or grid tokens confirmed** — Column counts, gutter widths, max-width containers, and section padding values are inferred from the brand category and Shopify defaults, not measured from the live site.
- **Icon system unknown** — Whether Burgon & Ball uses a custom SVG icon set, Shopify's built-in icon library, or a licensed icon font could not be determined from the extraction.
- **Animation and transition values absent** — Hover transition durations, drawer slide timing, card lift animation curves, and any scroll-triggered effects are entirely unextracted.
- **Mobile breakpoint values unconfirmed** — Exact Shopify theme breakpoints may differ from the standard 744px / 1128px / 1440px values used here; inspect the theme CSS for `--breakpoint-*` custom properties.
- **Price formatting and currency variants** — Multi-currency display, sale price strikethrough styling, and "from £X" range formatting could not be confirmed from static extraction.
