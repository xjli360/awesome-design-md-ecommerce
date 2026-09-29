---
version: alpha
name: "Cuyana"
source_url: "https://cuyana.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Cuyana's add-to-cart button is the same color as its headline type — near-black #1a1a1a pressed into double duty — because the brand's founding thesis ("fewer, better things") refuses a separate urgency color. The palette extracted from the live site resolves to a single neutral ramp: #1a1a1a for ink and primary CTAs, #565656 for secondary text, #979797 for muted copy and disabled states, #dadada for hairlines, and #f9fafb for the canvas — five stops, no accent, no promotional red. Panama Proportional carries editorial headers at wide letter-spacing while StyreneA-Regular-Web anchors product names in a cooler, more institutional register; Montserrat handles navigation and UI labels in lightweight uppercase, and Nunito Sans absorbs body copy with enough warmth to offset the otherwise spare palette. Cards use `{rounded.none}` — no softening radius, no pill shapes — trusting photography to supply all the warmth the color system withholds. Navigation is architecturally sparse: category links as flat text at `{typography.nav-link}` weight, a search input that stays compressed until engaged, and a cart icon reduced to its minimum viable form. Even sale and "new arrival" badges inherit near-black rather than reaching for contrast color, keeping the visual temperature cool across both editorial and promotional moments. Spacing is generous: product names sit with more vertical breathing room than the category average, and the product grid runs tight column gutters to surface more SKUs per viewport without fragmenting the sense of curation. The overall impression is a system that earns its premium positioning through what it omits — no gradients, no drop shadows, no personality colors — only type, image, and exactly enough structure to guide the eye.

colors:
  primary: "#1a1a1a"
  primary-active: "#141619"
  primary-disabled: "#979797"
  ink: "#1a1a1a"
  ink-secondary: "#565656"
  body: "#545454"
  muted: "#979797"
  hairline: "#dadada"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#ffffff"
  surface-subtle: "#eeeeee"
  border: "#cbccce"
  border-strong: "#636464"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sale-bg: "#1c1b1b"
  sale-text: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Panama Proportional', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: 0.04em
  display-md:
    fontFamily: "'Panama Proportional', serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.03em
  display-sm:
    fontFamily: "'Panama Proportional', serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-md:
    fontFamily: "'StyreneA-Regular-Web', 'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  title-sm:
    fontFamily: "'StyreneA-Regular-Web', 'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  product-name:
    fontFamily: "'StyreneA-Regular-Web', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
  body-md:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.08em
    textTransform: uppercase
  badge:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  price:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "'Nunito Sans', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    color: "#565656"
    textDecoration: line-through

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 15px 31px
    height: 48px
    border: "1px solid {colors.ink}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: "{spacing.sm} {spacing.base}"
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price}"
    padding: "{spacing.sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    imagePosition: center
    minHeight: 560px
    overlayMaxWidth: 480px
  hero-editorial:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-md}"
    layout: split-50-50
  category-label:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    backgroundColor: transparent
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.sm}"
  swatch-selector:
    size: 20px
    borderSelected: "2px solid {colors.ink}"
    borderUnselected: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    tapTarget: 40px
  size-selector:
    typography: "{typography.caption}"
    textColor: "{colors.ink}"
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    minHeight: 40px
  quantity-stepper:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 40px
    width: 120px
  email-capture:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    inputTypography: "{typography.body-md}"
    buttonTypography: "{typography.button-md}"
    padding: "{spacing.xxl}"
    rounded: "{rounded.none}"
    textAlign: center
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
    columns: 4
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    separator: "/"

## Components

### Buttons
**`button-primary`** — Flat near-black #1a1a1a fill, white uppercase Montserrat at 13px/0.12em tracking, strict `{rounded.none}` corners, 48px height. Hover/active deepens to #141619; disabled collapses to #979797 fill, preserving the uppercase label in white. The button makes no ergonomic concessions — no radius, no shadow, no hover lift — because the visual language treats restraint as the signal of quality. On full-bleed dark heroes the same token renders in reversed form with a white border using the `{colors.on-dark}` value.

**`button-secondary`** — Identical geometry to `button-primary` with a transparent fill and 1px `{colors.ink}` border. Used for wishlist saves, "Continue Shopping," and modal dismissals where a second action exists alongside a primary. On promotional dark panels the border inverts to white so the button remains legible without a fill swap.

**`button-text`** — Inline underlined link in `{typography.button-md}` style, no background or border. Appears in editorial copy, within accordion bodies, and as tertiary actions in the cart drawer.

### Navigation
**`nav-bar`** — 64px white bar with `{typography.nav-link}` uppercase links spaced at 0.1em tracking and no bold weight. A `nav-bar-promo-strip` in #1a1a1a sits flush above it, carrying shipping and offer messages in centered reversed caption type. Sub-navigation appears as a flat borderless panel — no drop shadow, no background wash — just left-aligned category columns flush with the nav bottom edge.

### Product Card
**`product-card`** — 3:4 portrait image on #f9fafb surface with `{rounded.none}` at all four corners. Product name in `{typography.product-name}` (StyreneA, tracked, regular weight), price in `{typography.price}` stacked below with no intervening element. A `product-card-badge` for "New" or "Sale" uses the same near-black fill with white `{typography.badge}` — no red urgency color, preserving the cool temperature even during promotions. Hover triggers a cross-fade to a secondary colorway image with no card elevation or box shadow.

### Hero
**`hero`** — Full-bleed image with a centered or left-anchored text overlay. Headline in `{typography.display-xl}` Panama Proportional at light weight, subhead in `{typography.body-md}`, CTA as a `button-primary` directly on the image. `hero-editorial` renders a split 50/50 layout with the image on the right and a solid near-black left panel — used for lookbook and campaign pages to force reading order without relying on an overlay scrim.

### Form Inputs
**`text-input`** — Full 1px `{colors.hairline}` border in resting state; border transitions to `{colors.ink}` on focus with no color fill change. `{rounded.none}` throughout. Placeholder text in `{colors.muted}`. Used identically across search, email capture, and all checkout fields — no visual distinction between input contexts.

### Selectors
**`swatch-selector`** — 20px circle for color swatches with a 40px invisible tap target zone. Selected state renders a 2px `{colors.ink}` ring; unselected sits at 1px `{colors.hairline}`. `size-selector` is a rectangular chip with the same border logic in `{typography.caption}` uppercase, `{rounded.none}`, minimum 40px height on mobile.

### Email Capture
**`email-capture`** — Centered module on `{colors.surface-soft}` with a Panama `{typography.display-sm}` headline, single `text-input`, and full-width `button-primary`. `{spacing.xxl}` padding on all sides. Appears at the base of editorial pages and category landings; no decorative imagery, no supporting copy beyond the headline.

### Footer
**`footer`** — Near-black #1a1a1a background with reversed white type. Four-column link grid on desktop using `{typography.caption}` uppercase column headers. A bottom row carries legal copy in `{typography.body-sm}`. Newsletter input appears inline in the footer as an inverted `text-input` with a white 1px border on the dark field.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered wordmark; hero text overlay shifts to bottom third of image; promo strip scrolls with page; filter rail becomes slide-up drawer |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories only with overflow to hamburger; hero switches to stacked image-above / text-below layout; email capture stacks to single column |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with all primary categories visible; hero spans full viewport width with overlay panel; filter rail reappears as left sidebar |
| Wide | > 1440px | Four-column product grid; max content width capped at ~1440px centered on canvas; nav padded symmetrically; hero image crops to 1440px with left-anchored overlay |

### Touch Targets
- All button components meet 48px minimum height
- Swatch selectors have a 40px tap target despite a 20px visual size via invisible padding
- Cart, search, and account icons in the nav bar are minimum 44×44px tap zones
- Size selector chips enforce 40px minimum height on mobile regardless of label length
- Quantity stepper plus and minus hits are padded to 44px each

### Collapsing Strategy
- Primary nav collapses to hamburger icon below 744px; search, account, and cart utility icons remain visible in the bar
- Product filter sidebar converts to a slide-up modal drawer on mobile with apply/clear actions pinned to the bottom
- Email capture module stacks to single column with full-width input and button below 744px
- Footer four-column grid collapses to two columns at tablet and single-column accordion at mobile
- Hero editorial 50/50 split layout stacks vertically at mobile (image first, text panel second) with the text panel using full-width near-black fill

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.
- No brand accent or warm neutral tone (cream, stone, sand) was extractable from CSS custom properties; Cuyana's seasonal editorial palette may include these tones but they are applied via inline styles or JS-driven theming not captured in the extraction
- Bootstrap 5 utility colors (#0d6efd, #198754, #0dcaf0, #084298, #664d03, #842029 and their tint/shade variants) contaminate the extracted palette; all were excluded as framework defaults rather than brand tokens
- Panama font weight range and named optical sizes are undocumented in public sources; weight 300 (light) is inferred from visual inspection rather than confirmed font-face declarations
- Panama Monospace usage context is unknown — it appears in the font stack but no clear typographic role (pricing, code, editorial aside) could be isolated
- Exact hover and focus-visible state colors for form fields and nav items could not be reliably isolated from the extraction output
- Product card hover behavior (cross-fade to alternate colorway) is JavaScript-driven and not reflected in CSS extraction
- Sale and promotional badge color behavior during seasonal campaigns (whether a red or warm tone appears) cannot be confirmed from static extraction alone
- Whether Cuyana uses a sticky or scroll-away nav pattern on mobile was not determinable from the extraction
