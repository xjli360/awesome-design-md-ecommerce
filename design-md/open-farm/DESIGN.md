---
version: alpha
name: "Open Farm"
source_url: "https://openfarmpet.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Two greens share the brand voltage at Open Farm — the deep forest #128230 that carries primary CTAs, nav highlights, and active states, and a brighter #1ab243 that surfaces in badge fills and hover transitions, a layering that reads less like a calculated palette split and more like a field caught in two different kinds of afternoon light. The harvest-warm #d05018 cuts against this cool axis as the urgency accent: sale callouts, limited-batch ingredient chips, and seasonal campaign banners reach for this burnt orange whenever the UI needs a conversion signal that contrasts the green-dominant system. The near-black #121212 handles all ink duties without tipping to full monochrome, keeping contrast high while staying a degree warmer than a pure black would. Moderat — Colophon Foundry's geometric sans with round apertures and even stroke weight — is the sole typeface. Its natural legibility at caption scale suits ingredient-dense product pages, while its geometric authority at display weight carries homepage claims about ethical sourcing without reading promotional. Display headlines run at weight 700; section titles step to 500; body prose sits at 400 with a 1.6 line-height that is unusually generous for ecommerce, signaling the brand expects customers to actually read the ingredient copy. Button labels use weight 600 with slight uppercase tracking, carving a distinct register from editorial text. Corner radii stay soft throughout: subscription CTAs reach for {rounded.full} pill shapes, product cards sit at {rounded.md}, and form inputs use {rounded.sm}. The same {rounded.full} shape returns on provenance chips — "Humanely Raised," "Ocean-Caught," "Non-GMO Project Verified" — functioning as trust architecture near the product title rather than decorative footnotes buried below the fold. Navigation stays white with the green wordmark and a single filled {colors.primary} CTA button in the top-right. Product tiles render on {colors.surface-soft} so the photography reads bright and farm-referencing rather than moody or editorial. A full-width subscription upsell bar pinned to the viewport bottom on PDPs uses {colors.accent-orange} as background — the one moment the orange earns its full brand weight, creating a conversion signal without requiring visual novelty.

colors:
  primary: "#128230"
  primary-active: "#0e6b25"
  primary-disabled: "#a8cfb0"
  ink: "#121212"
  body: "#3d3d3d"
  muted: "#717171"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#d05018"
  accent-orange-soft: "#f7e9e1"
  accent-green-bright: "#1ab243"

typography:
  display-xl:
    fontFamily: "Moderat, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Moderat, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Moderat, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Moderat, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Moderat, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "Moderat, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Moderat, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Moderat, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Moderat, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "Moderat, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "Moderat, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  label-caps:
    fontFamily: "Moderat, sans-serif"
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 44px
  button-pill-outline:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1.5px
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 72px
    ctaSlot: "button-primary"
    cartBadgeColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    subtitleColor: "{colors.muted}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    imageFill: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    badgeSlot: "sourcing-badge"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    ctaVariant: "button-pill"
  sourcing-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  sourcing-badge-outline:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  subscription-upsell-bar:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    position: "sticky"
    bottom: 0
    height: 56px
    padding: 0 {spacing.lg}
  ingredient-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 8px 14px
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    height: 48px
    orbColor: "{colors.primary}"
    orbTextColor: "{colors.on-primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    borderTop: "none"

## Components

### Buttons

**`button-primary`** — The filled forest-green CTA (#128230) is the primary action throughout: "Add to Cart," "Subscribe & Save," and checkout progression all use this button at 48px height with uppercase-tracked Moderat at weight 600. On active/hover, the background deepens to `{colors.primary-active}` (#0e6b25) without any opacity trick; disabled state uses the muted `{colors.primary-disabled}` (#a8cfb0) at full opacity.

**`button-secondary`** — White fill with a 1.5px forest-green border and matching green label text. Appears as the secondary action when paired with a primary CTA — "Learn More" beside "Add to Cart," or "Compare Plans" beside "Subscribe." On hover, border and label shift to `{colors.primary-active}` for visual consistency with the primary button's active state.

**`button-pill`** — The `{rounded.full}` variant of the primary button, used for subscription prompts, loyalty enrollment, and homepage hero CTAs where the pill shape reads friendlier and more inviting than the standard `{rounded.sm}` form. Slightly lower height (44px) keeps the pill proportionally comfortable at wider widths.

**`button-pill-outline`** — Transparent fill with a 1.5px green border at `{rounded.full}`. Appears as the secondary action in two-button hero layouts where `button-pill` already occupies the primary slot. Also used for "View Details" ghost actions on editorial content cards.

### Form Inputs

**`text-input`** — White canvas with a 1.5px `{colors.hairline}` border at rest, shifting to `{colors.primary}` green on focus. Moderat `{typography.body-md}` at 16px, 48px height. Error states swap the border to `{colors.accent-orange}` rather than introducing a separate red token, keeping error feedback within the existing warm-accent palette. Placeholder text uses `{colors.muted}` at the default opacity.

### Navigation

**`nav-bar`** — White bar at 72px height with a 1px `{colors.hairline}` bottom border. The wordmark sits on the left in `{colors.primary}` green; center holds flat-weight nav links in `{typography.nav-link}` (no underline at rest, underline on hover). A single `button-primary` in the top-right slot carries the dominant conversion action — typically "Shop" or "Start Subscription." Cart icon in `{colors.ink}` with a numeric badge fill in `{colors.primary}`. On scroll past 60px the nav gains a subtle drop shadow rather than a background color change.

### Search

**`search-bar`** — Pill-shaped at `{rounded.full}` with a white input body and a circular green search orb on the right end. The orb uses `{colors.primary}` fill with `{colors.on-primary}` icon, echoing the primary button language in a compact form. Appears in the mobile nav overlay and as an inline element in collection page headers.

### Product Cards

**`product-card`** — White card at `{rounded.md}` with an image tile that fills to `{colors.surface-soft}` on load. Product name in `{typography.title-md}`, price in `{typography.title-sm}`, and a one-line descriptor in `{typography.caption}` at `{colors.muted}`. One to three `sourcing-badge` chips sit below the product name, functioning as inline trust signals before the customer clicks through. Hover state elevates with a 4px shadow rather than a border color change, keeping the interaction subtle. A quick-add "+" button appears on hover in the card's lower-right corner using the `button-primary` token at reduced (40px) height.

### Hero Banner

**`hero-banner`** — Full-bleed `{colors.primary}` green container with headline reversed to `{colors.on-primary}` using `{typography.display-xl}`. A supporting one-sentence claim in `{typography.body-md}` sits at 85% opacity white beneath the headline. The CTA uses `button-pill` in an inverted color treatment (white background, green text) so it reads against the dark green ground without a second accent color. No border radius on the container — the green runs edge-to-edge. Variant banners for seasonal campaigns substitute `{colors.accent-orange}` as the background, keeping the layout identical and swapping the pill CTA to a standard `button-pill`.

### Sourcing Badges

**`sourcing-badge`** — Filled forest-green pill at `{rounded.full}` using `{typography.badge}` (11px/weight 600 reversed white). The filled variant is the primary trust signal on product cards and PDP headers. **`sourcing-badge-outline`** is the secondary variant used inside expanded ingredient panels and the brand values section, where the filled green would overpower body copy. Both variants hold consistent pill height (24px) regardless of label length so a row of three badges remains visually even.

### Subscription Upsell Bar

**`subscription-upsell-bar`** — A full-width sticky bar pinned to the viewport bottom on product detail pages. Background is `{colors.accent-orange}` — the single moment in the UI where the orange operates at full saturation and full width. Text and inline CTA label use `{colors.canvas}` for legibility against the warm ground. The bar fades in after 30% page scroll depth on PDP, carries a brief value proposition ("Subscribe & Save 20% — Free Shipping Included"), and includes a dismissal `×` in `{colors.canvas}` at the far right that sets a session cookie.

### Ingredient Callout

**`ingredient-callout`** — A `{colors.surface-soft}` block at `{rounded.md}` used within product accordion sections to spotlight individual hero ingredients. Headline in `{typography.title-sm}`, body in `{typography.body-sm}`, with an optional small provenance thumbnail or iconographic mark floating left. This block recurs on recipe pages and the brand story sections, keeping ingredient education visually consistent across content types.

### Category Pills

**`category-pill`** — `{colors.surface-soft}` background, `{colors.ink}` text, `{rounded.full}`, uppercase Moderat at 11px/weight 700 with 1px letter-spacing. Used in filter bars on collection pages and as quick-nav anchors in the footer product section. Active state flips to `{colors.primary}` background with `{colors.on-primary}` text; no border is used in either state.

### Footer

**`footer`** — Dark `{colors.ink}` background with `{colors.canvas}` column headers and nav links; secondary legal links use `{colors.muted}` to visually de-prioritize. No decorative top border — the dark footer arrives abruptly from the preceding section, functioning as a tonal break. The wordmark appears in `{colors.canvas}` at the left of the baseline row alongside certification marks (ASPCA, Certified B Corp, Non-GMO Project Verified) rendered at 60% opacity white so they read as credentials rather than competing with link navigation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen overlay in `{colors.primary}`; hero headline drops to `{typography.display-md}`; subscription-upsell-bar goes full-width fixed at viewport bottom; sourcing badges stack vertically below product name |
| Tablet | 744–1128px | Two-column product grid; nav shows primary links inline with hamburger for overflow; hero uses 50/50 text-image split with the `{colors.primary}` block on the left and product photography bleeding to the right edge |
| Desktop | 1128–1440px | Three or four-column product grid; full horizontal nav with all links visible and no hamburger; hero banner full-bleed with centered text overlay on photography |
| Wide | > 1440px | Content max-width constrains at 1440px with symmetrical side padding increasing; hero text block stays centered at a fixed width column; footer columns spread to a six-column layout |

### Touch Targets
- All primary buttons maintain 48px minimum height across all breakpoints
- Nav icons (cart, hamburger) are 44×44px hit area on mobile
- Sourcing badge chips are display-only on mobile; interactive filter variants in collection pages enforce a minimum 36px height with 8px horizontal padding
- Quick-add card buttons suppress on mobile tap targets in favor of a dedicated "Add to Cart" button on the expanded PDP

### Collapsing Strategy
- Collection page filters collapse into a bottom-sheet modal overlay on mobile, triggered by a fixed filter-count pill in `{colors.primary}`
- Ingredient accordions remain expandable at all breakpoints but default to collapsed on mobile to reduce scroll depth on PDP
- Footer four-column layout folds to two columns at tablet breakpoint and single-column stacked at mobile
- The subscription upsell bar reduces to an icon + single-line CTA on viewports below 375px and hides if the customer has already added a subscription item to cart

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; mobile browser chrome tint is unconfirmed — likely `{colors.primary}` (#128230) based on the nav and brand primary
- Exact Moderat weight range confirmed (400, 500, 600, 700); condensed or extended optical variants not confirmed from extraction
- Drop-shadow elevation values for product card hover and sticky nav scroll states not extracted — values are inferred from category convention
- Animation easing curves for subscription bar entrance, badge hover, and accordion open/close transitions not confirmed
- No icon system source identified — custom SVG set versus a third-party library (Phosphor, Heroicons) not determinable from extraction
- Exact corner radius values at the pixel level not confirmed from live extraction; all `rounded` values are inferred from visual pattern and ecommerce category convention
- `accent-orange-soft` (#f7e9e1) is a derived tint not directly extracted; used speculatively for light-background callout contexts
- Typography scale below 12px (legal fine print, nutritional footnotes) not confirmed
