---
version: alpha
name: "iRocker"
source_url: "https://irockersup.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Electric lime (#e7fd39) against a deep-ocean dark (#003343) is the voltage signature of iRocker's entire visual language — an unlikely pairing that holds its nerve across hero sections, CTA buttons, and promo banners without sliding into hazmat-vest territory, because the brand resolves it by placing dark ink (#24292e) on the lime rather than white, preserving contrast with more seriousness. The surrounding palette reads like a cross-section of open water: midnight #003343 anchors the persistent nav and hero backdrops, #125b6f and #246f85 step toward mid-depth in gradients and card accents, #00a2bf and #1cc6e3 break at the surface in category chips and interactive highlights, and #e0f5fb appears as the faintest cyan wash behind specification comparison blocks. Coral (#e15748) runs point on urgency — low-stock alerts, countdown strips, clearance badges — without ever competing for the primary CTA register. Typography runs Inter Variable throughout the full UI, leaning on weight 600–700 at display scale rather than anything heavier; board names and hero headlines push into the 48–60px range on desktop but the system never escalates past that into condensed-gothic aggression. IBMPlexSerif enters only in editorial zones — ambassador stories, gear-guide pull quotes — where the serif signals narrative mode rather than product conversion. Card corners hold at {rounded.sm} (8px), modest enough to read structural rather than decorative, and buttons flatten further to {rounded.xs} (4px), maintaining the matter-of-fact outdoor-equipment register that the lime alone might undermine. The navigation bar stays in ocean-deep dark (#003343) regardless of underlying page tone, acting as a fixed horizon line that grounds every scroll position. Promo strips at the page crown run lime-on-dark — the primary CTA palette inverted — priming the eye before the hero image finishes loading, so the first conscious color association is action rather than scenery.

colors:
  primary: "#e7fd39"
  primary-active: "#cae320"
  primary-disabled: "#f0faa0"
  ink: "#24292e"
  body: "#596066"
  muted: "#9ca3af"
  muted-dark: "#6b7280"
  hairline: "#e5e7eb"
  hairline-soft: "#f3f4f6"
  canvas: "#fafafa"
  surface-soft: "#f6f7f9"
  surface-card: "#ffffff"
  on-primary: "#24292e"
  on-dark: "#fafafa"
  ocean-deep: "#003343"
  ocean-mid: "#125b6f"
  ocean-teal: "#246f85"
  ocean-bright: "#00a2bf"
  ocean-cyan: "#1cc6e3"
  ocean-tint: "#e0f5fb"
  graphite: "#454c52"
  coral: "#e15748"
  green-action: "#2f9461"

typography:
  display-xl:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.21
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: -0.2px
  editorial-display:
    fontFamily: "'IBMPlexSerif', Palatino, 'Playfair Display', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.31
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.88px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  price-display:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  spec-value:
    fontFamily: "'Inter Variable', Inter, -apple-system, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px

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
    height: 52px
    hoverBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"
    disabledTextColor: "{colors.muted}"

  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 52px
    border: "2px solid {colors.ink}"
    hoverBackgroundColor: "{colors.surface-soft}"

  button-ghost-light:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 52px
    border: "2px solid {colors.on-dark}"
    hoverBackgroundColor: "rgba(250,250,250,0.1)"

  button-sm-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 20px
    height: 40px

  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.ocean-bright}"
    padding: 12px 16px
    height: 48px

  nav-bar:
    backgroundColor: "{colors.ocean-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 68px
    borderBottom: none
    logoHeight: 36px
    activeUnderlineColor: "{colors.primary}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-sm}"
    ctaRounded: "{rounded.xs}"
    ctaPadding: 9px 18px

  promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    height: 40px
    padding: 0 16px

  hero-dark:
    backgroundColor: "{colors.ocean-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    minHeight: 600px
    imageOverlayOpacity: 0.45
    textMaxWidth: 560px
    textPadding: 80px 64px

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 16px
    imageAspectRatio: "4/3"
    imageRounded: "{rounded.xs}"
    productNameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    subPriceTypography: "{typography.body-sm}"
    subPriceColor: "{colors.muted}"
    badgeRounded: "{rounded.xs}"
    hoverShadow: "0 4px 20px rgba(0,51,67,0.12)"
    hoverBorderColor: "{colors.ocean-bright}"

  badge-sale:
    backgroundColor: "{colors.coral}"
    textColor: "{colors.surface-card}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  badge-bestseller:
    backgroundColor: "{colors.ocean-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 3px 8px

  spec-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 24px
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.ink}"
    accentBar: "3px solid {colors.primary}"
    accentBarPosition: top

  category-chip:
    backgroundColor: "{colors.ocean-tint}"
    textColor: "{colors.ocean-mid}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
    activeBackgroundColor: "{colors.ocean-bright}"
    activeTextColor: "{colors.on-dark}"
    border: "1px solid {colors.ocean-cyan}"

  comparison-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.ocean-deep}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.title-sm}"
    cellTypography: "{typography.body-sm}"
    highlightColumnBackground: "{colors.ocean-tint}"
    accentCheckColor: "{colors.primary}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    overflow: hidden

  editorial-block:
    backgroundColor: "{colors.ocean-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.editorial-display}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.muted}"
    accentColor: "{colors.primary}"
    accentBarWidth: 4px
    padding: 64px 48px

  search-overlay:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ocean-bright}"
    backdropColor: "rgba(0,51,67,0.6)"
    resultHoverBackground: "{colors.ocean-tint}"

  rating-row:
    starColor: "{colors.primary}"
    emptyStarColor: "{colors.hairline}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"

  stock-alert:
    backgroundColor: "{colors.coral}"
    textColor: "{colors.surface-card}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 8px 16px

  financing-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    accentColor: "{colors.green-action}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    borderTop: "3px solid {colors.primary}"
    padding: 48px 0 32px

## Components

### Buttons

**`button-primary`** — The electric lime (#e7fd39) fill with dark ink (#24292e) text at {rounded.xs} (4px) is the sharpest-cornered, most legible CTA in the system. It runs at 52px height with 28px horizontal padding, giving it enough mass to anchor dark hero sections without requiring a border. Hover darkens the fill to {colors.primary-active} (#cae320); disabled states fade the fill to {colors.primary-disabled} (#f0faa0) and the label to {colors.muted}, never removing the button from the layout flow.

**`button-secondary`** — White fill with a 2px solid {colors.ink} border; sits beside the primary at identical dimensions so pairings feel intentional rather than weighted. Hover shifts the fill to {colors.surface-soft}, keeping the border stable. Used for "Learn More," filter toggles, and secondary PDP actions like "Add to Wishlist."

**`button-ghost-light`** — Transparent fill with a 2px {colors.on-dark} border, for placement over dark or photographic surfaces where the primary lime would compete with background imagery. Hover adds a 10% white fill so state change is visible without full color commitment.

**`button-sm-primary`** — Compact 40px variant of the primary, used in nav CTA slots, promo modals, and bundle upsell rows where the full 52px height would overwhelm surrounding text.

### Navigation

**`nav-bar`** — Persistently dark (#003343 background) across all page types, including those with white body backgrounds, so the top of every page reads as a horizon rather than blending into content. Nav links at {typography.nav-link} (15px/500) sit left of a right-aligned CTA button using {colors.primary} fill. The active link state adds a 2px bottom underline in {colors.primary} rather than changing text weight, keeping the dark surface visually quiet. The logo locks at 36px height.

**`promo-strip`** — A 40px strip that lives above the nav-bar at the very top of the page crown. Background runs {colors.primary} (lime), text in {colors.on-primary} (dark ink) at {typography.label-upper} — the inverse of the main CTA palette, used here as a preview gesture. Content is typically a single centered promotional line with a linked code or anchor.

### Hero

**`hero-dark`** — Full-width photographic hero with a 45% dark overlay over action imagery, minimum 600px tall. Headline uses {typography.display-xl} in {colors.on-dark}; subheadline uses {typography.body-md} in {colors.muted} to differentiate hierarchy without adding a third color. The primary CTA button sits below with 48px of breathing room between subhead and button top. Text content is left-aligned and capped at 560px wide so long board names and taglines never span the full viewport.

### Product Cards

**`product-card`** — White surface with 1px {colors.hairline} border and {rounded.sm} corner. On hover, the border color lifts to {colors.ocean-bright} and a directional shadow (0 4px 20px rgba(0,51,67,0.12)) creates elevation without animation lag. Badge pills (sale, bestseller, new) stack top-left over the product image at {rounded.xs}, using three distinct background colors to signal different urgencies: coral for markdown, ocean-deep for bestseller, lime for new arrival. Pricing renders at {typography.price-display} (26px/700) with struck-through original price at {typography.body-sm}/{colors.muted} beside it when on sale.

### Specification Tiles

**`spec-tile`** — Used on PDPs in a 3–4 column grid to surface board dimensions, weight capacity, and inflation specs. Each tile carries a 3px top accent bar in {colors.primary}, a small all-caps label at {typography.caption}/{colors.muted}, and the value at {typography.spec-value} (20px/700). The lime accent bar ties this utilitarian block back to the brand CTA register.

### Category Chips

**`category-chip`** — Pill-shaped filters rendered in {colors.ocean-tint} background with {colors.ocean-mid} text. Active state shifts to {colors.ocean-bright} background with {colors.on-dark} text, creating a clear selection signal within the teal family without using the lime primary. Border at 1px {colors.ocean-cyan} on all states provides definition on light backgrounds.

### Comparison Table

**`comparison-table`** — A full-width table used to compare board models side-by-side. Header row uses {colors.ocean-deep} with {colors.on-dark} text at {typography.title-sm}. The highlighted "recommended" column sits in {colors.ocean-tint} with checkmark icons in {colors.primary} (lime) for boolean features. All corners are clipped to {rounded.sm} via `overflow: hidden` on the table wrapper.

### Editorial Block

**`editorial-block`** — Dark ocean ({colors.ocean-deep}) full-width section used for ambassador features, "Why SUP?" content, and gear guides. Headline runs {typography.editorial-display} (IBMPlexSerif, 32px) with a 4px left-border accent in {colors.primary} on the leading pull quote. Body text in {colors.muted} against the dark background intentionally reduces contrast slightly, signaling lower urgency than product modules. Used sparingly, no more than once per page template.

### Footer

**`footer`** — Dark ink (#24292e) background with a 3px top border in {colors.primary} that visually caps the page with the brand's CTA color rather than a neutral rule. Link columns use {typography.body-sm} at {colors.muted} with hover state shifting to {colors.primary}. Column headings use {typography.title-sm} at {colors.on-dark}. Social icons and payment logos sit in the bottom strip at reduced opacity.

### Supporting Components

**`financing-banner`** — A soft-gray ({colors.surface-soft}) inline row on PDPs that surfaces installment pricing ("As low as $X/mo with…"). The monthly figure renders in {colors.green-action} (#2f9461) to signal financial positivity without lime overload. Border and rounded at {rounded.sm} keep it contained as a supplemental element.

**`search-overlay`** — Triggered by a search icon in the nav; opens a centered panel with a 2px {colors.ocean-bright} border input at full focus immediately. The backdrop is a dark ocean scrim (rgba(0,51,67,0.6)) rather than generic black, keeping the brand's palette consistent in modal contexts. Result rows use {colors.ocean-tint} hover backgrounds.

**`stock-alert`** — A tight coral (#e15748) pill that appears inline near the add-to-cart button when a board color/size is low on inventory. Uses {typography.caption} in {colors.surface-card} (white), keeping it readable without adding visual weight beyond the urgency color itself.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero drops to 480px min-height with text padding reduced to 24px; nav collapses to hamburger menu with full-screen drawer in {colors.ocean-deep}; spec tiles go 2-column; comparison table scrolls horizontally |
| Tablet | 744–1128px | 2-column product grid; hero text area widens to 480px; nav shows top-level links, hides sub-links behind "More" overflow; spec tiles stay 3-column; category chips scroll horizontally in a snapping row |
| Desktop | 1128–1440px | 3-column product grid; full nav with all product categories visible; hero reaches full 600px min-height with 64px side padding; editorial block shows image + text side-by-side at 50/50 |
| Wide | > 1440px | Grid locks to max-width 1440px centered; hero text column caps at 560px; product grid allows 4-column layout; side padding increases to keep content from spreading uncomfortably |

### Touch Targets

- All interactive elements (chips, buttons, nav icons) hold minimum 44px height on mobile
- Category chip rows use `-webkit-overflow-scrolling: touch` with 16px start/end padding to signal scrollability without clipping the first/last chip
- Promo strip text links use full strip height (40px) as the touch target
- Rating stars are rendered at 24px per star minimum on touch viewports

### Collapsing Strategy

- Navigation collapses to a hamburger icon at < 744px; the drawer slides in from the left over the {colors.ocean-deep} nav and covers the full viewport height
- Footer link columns stack vertically on mobile with accordion expand/collapse per column heading
- Comparison table converts to a horizontal-scroll container on mobile; the first (feature name) column freezes at left
- Hero CTA button stacks below the subheadline at full width on mobile rather than inline
- Spec tiles reflow from 4-column to 2-column grid at tablet, then maintain 2-column on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius values from live rendered components could not be confirmed; {rounded.xs} (4px) and {rounded.sm} (8px) assignments are estimated from visual conventions for action sports Shopify stores
- Active/disabled state colors for {colors.primary-active} (#cae320) and {colors.primary-disabled} (#f0faa0) are derived by lightness-adjustment from the extracted lime; not confirmed from live CSS
- Custom icon library and glyph set not extractable; icon style (outline vs. filled, stroke weight) is unknown
- Animation easing curves and transition durations for hover states, drawer opens, and hero crossfades were not captured
- The exact weight axis range used for Inter Variable is unconfirmed; the site may restrict to discrete weights (400, 600, 700) rather than the full variable range
- Mobile navigation drawer layout and sub-category depth could not be verified from static extraction
- Exact shadow values for modals, overlays, and floating cart drawers are unknown
- Whether IBMPlexSerif is loaded as a full web font or only used in images/static assets is unconfirmed; Playfair Display is listed as a fallback alternative
