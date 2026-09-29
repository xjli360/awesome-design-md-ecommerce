---
version: alpha
name: "Ferkos Fine Jewelry"
source_url: "https://www.ferkosfinejewelry.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The site's dominant color is the same clay-rose as the interior of a well-worn gold ring box — #a38473 warms every primary CTA and category hover state, occupying the exact register between champagne gold and bare skin. Antic Didone, a high-contrast editorial serif with dramatic thin-thick stroke transitions, handles all display text; at 48px those hairline strokes dissolve into geometry, creating the same visual tension as a delicate gold chain photographed against pale linen. Montserrat in weights 400–600 carries the entire UI shell — nav labels, button caps, captions, form fields — its clean geometry making a deliberate counterpoint to Antic Didone's theatrical vertical rhythm. The canvas stays near-white (#fbfbfb, #f7f7f7), keeping product photography primary, while warm cream (#e2d2ab) and deeper blush (#dcc8ba) resurface as surface tints for collection banners and callout modules — the palette reads like the inside of a luxury packaging suite rather than interface chrome.

  The brand-specific palette builds outward from the primary terracotta: #ac9181 lightens it for hover states while #574b44 — a dark warm brown without any gray cast — handles secondary text and links. Near-black (#121212) anchors headlines for legibility; #2c332f, a near-black with barely perceptible forest warmth, appears in overlays and footer grounds. The lone saturated accent is a deep wine-crimson (#82021f), surfacing only on sale badges and error states. Components carry essentially no border radius — {rounded.none} is the default posture, with inputs receiving at most {rounded.xs} — because softness here comes from color temperature rather than corner geometry. CTAs render at 44px tall with Montserrat uppercase letter-tracking, surrounded by generous horizontal padding, producing an unhurried editorial checkout atmosphere rather than high-urgency conversion pressure. The system's restraint extends to decoration: hairlines at #ebebeb keep sections separated without weight, and the announcement bar borrows the same terracotta as the primary button, reinforcing a single brand voltage across both promotional and transactional surfaces.

colors:
  primary: "#a38473"
  primary-active: "#574b44"
  primary-hover: "#ac9181"
  primary-disabled: "#dcc8ba"
  accent-crimson: "#82021f"
  ink: "#121212"
  body: "#1d1d1d"
  muted: "#574b44"
  muted-soft: "#ac9181"
  hairline: "#ebebeb"
  hairline-soft: "#eeeeee"
  border-mid: "#d6d6d6"
  canvas: "#fbfbfb"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  surface-warm: "#dcc8ba"
  surface-cream: "#e2d2ab"
  overlay: "#2c332f"
  on-primary: "#ffffff"
  on-dark: "#f7f7f7"
  on-cream: "#574b44"

typography:
  display-xl:
    fontFamily: "'Antic Didone', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.02em
  display-lg:
    fontFamily: "'Antic Didone', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  display-md:
    fontFamily: "'Antic Didone', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'Antic Didone', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  product-name:
    fontFamily: "'Antic Didone', serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.01em
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.09em
    textTransform: uppercase
  body-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.02em
  body-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.02em
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.14em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.03em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 28px
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
    padding: 14px 32px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    nameTypography: "{typography.product-name}"
    priceTypography: "{typography.price-display}"
    nameColor: "{colors.ink}"
    priceColor: "{colors.body}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  product-badge-sale:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.body}"
    ctaComponent: "button-primary"
    textAlign: center
  collection-banner:
    backgroundColor: "{colors.surface-cream}"
    headlineTypography: "{typography.display-md}"
    headlineColor: "{colors.on-cream}"
    captionTypography: "{typography.title-sm}"
    captionColor: "{colors.muted}"
    padding: "{spacing.xxl} {spacing.xl}"
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
    iconColor: "{colors.primary}"
  wishlist-button:
    backgroundColor: "transparent"
    iconColor: "{colors.muted-soft}"
    iconColorActive: "{colors.accent-crimson}"
    size: 32px
    rounded: "{rounded.full}"
  ring-sizer-callout:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.button-sm}"
    linkColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 48px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    headerTypography: "{typography.title-md}"
    headerColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
    subtotalTypography: "{typography.body-md}"
  footer:
    backgroundColor: "{colors.overlay}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.surface-soft}"
    borderTop: "none"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Filled in the brand's clay-rose terracotta (#a38473), 44px tall, zero border radius, Montserrat uppercase at 12px/0.14em tracking. On hover the background deepens to the darker warm brown (#574b44); on disabled the fill softens to blush (#dcc8ba) with muted brown text. The lettertracking and uppercase treatment give CTAs a stamp-like authority that reads as confidence without aggression.

**`button-secondary`** — Transparent fill with a 1px solid #121212 stroke, identical sizing to primary. Hover introduces a soft #f7f7f7 fill without changing the border, keeping the two-state transition subtle. Used for "Add to Wishlist," secondary CTAs on product pages, and filter controls.

**`button-ghost`** — No border, no fill, terracotta text in Montserrat uppercase. Appears inline in body copy and callout modules where a full-height button would crowd the layout.

### Inputs

**`text-input`** — Square-cornered ({rounded.none}), 44px tall, 1px hairline border (#ebebeb) that shifts to the primary terracotta on focus. Placeholder text uses the lighter muted-soft tone (#ac9181). Form labels sit above the field in `{typography.title-sm}` uppercase tracking.

**`search-overlay`** — A full-width search field that drops into a dedicated overlay panel rather than an inline bar. Square cornered, 48px tall, borderless except for a bottom-only 1px hairline. Autocomplete suggestions render on the same cream canvas.

### Navigation

**`nav-bar`** — 60px tall, near-white canvas (#fbfbfb), Montserrat 12px uppercase spaced at 0.09em. Desktop shows collection mega-menu dropdowns with Antic Didone category headings. A minimal 1px hairline bottom border separates it from page content without visual weight. Logo centered or left-aligned depending on viewport.

**`announcement-bar`** — 36px strip in the primary terracotta above the nav, white Montserrat caption text centered. The single color shared with the primary CTA creates an intentional top-to-bottom brand echo. Dismissible on mobile.

### Product Cards

**`product-card`** — No card border or drop shadow; product images sit on a soft #f7f7f7 ground that bleeds into the page canvas. Product name in Antic Didone 17px below the image, price in Montserrat 14px below. Sale and new badges overlay the image top-left in respective terracotta or crimson pill-less rectangles. A wishlist heart icon ({wishlist-button}) overlays top-right on hover. No border radius anywhere on the card.

### Hero and Collection Surfaces

**`hero`** — Full-bleed image with a centered Antic Didone headline at display-xl (48px) over a soft #f7f7f7 or image-darkened surface. Subhead in Montserrat body-md, a single primary CTA below. Text-only hero variants use the surface-soft background without photography.

**`collection-banner`** — Warm cream (#e2d2ab) background with Antic Didone display-md headline in on-cream brown (#574b44). Category label appears above in title-sm uppercase as an eyebrow. Used at section breaks between jewelry categories.

**`ring-sizer-callout`** — Inset module in warm blush (#dcc8ba) with a 2px corner radius, Montserrat body-sm prose and an underlined button-sm link in primary-active brown. Appears on ring product pages to surface the ring sizer tool without modal overhead.

**`trust-bar`** — Full-width band in surface-soft, thin hairlines top and bottom, three or four trust icons (shipping, returns, material purity) in terracotta with Montserrat caption labels. Sits just above or below the hero.

### Cart and Footer

**`cart-drawer`** — 400px side drawer on desktop, full-screen on mobile. White canvas, title-md uppercase header, Montserrat body-md line items. Subtotal and checkout CTA at the bottom use button-primary full-width.

**`footer`** — Dark forest-overlay background (#2c332f), off-white on-dark text. Column headings in title-sm uppercase Montserrat. Links in body-sm Montserrat at surface-soft (#f7f7f7) softened tone. Newsletter input inline with a ghost-on-dark variant CTA. No top border — the color change is the separator.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; announcement bar remains visible; hero headline drops to display-md (28px); cart drawer becomes full-screen bottom sheet |
| Tablet | 744–1128px | Two-column product grid; nav still hamburger or condensed horizontal; hero headline at display-lg (36px); collection banners full-bleed with reduced padding |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with mega-menu dropdowns; hero at display-xl (48px); trust bar switches to single horizontal row |
| Wide | > 1440px | Max content width capped ~1400px, centered with balanced side gutters; product grid stays at four columns; hero text constrained to ~640px centered column to avoid overly long lines |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Wishlist icon buttons padded to at least 44px hit area despite 32px visual size
- Nav hamburger icon 44px tap target
- Cart drawer close affordance full-width swipe-down in addition to icon tap
- Filter chips in collection pages minimum 36px tall with {spacing.md} gap between

### Collapsing Strategy

- Navigation mega-menu collapses to accordion-style drawer sections on mobile and tablet
- Product grid collapses 4 → 3 → 2 → 1 column across breakpoints; single-column only on the smallest mobile viewports
- Trust-bar icon+text pairs wrap to two rows on mobile with centered alignment
- Ring sizer callout collapses to full-width below product description on mobile
- Footer four-column layout collapses to two-column on tablet and single-column stacked on mobile with accordion disclosure for link groups

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No extracted button border-radius confirmed from live DOM — zero-radius inferred from fine jewelry brand conventions and lack of rounded value signals in extracted colors; verify against computed styles
- Font weights for Antic Didone cannot be confirmed beyond weight 400 (the font has a single-weight design); bold display hierarchy is achieved through size and spacing rather than weight variation
- Exact nav height (60px) and announcement bar height (36px) are estimates — not directly extractable from color/font hints
- Hover and focus transition durations not extractable from static color hints; assume 200ms ease for all interactive state changes
- Product image aspect ratios (likely 1:1 or 4:5) not confirmed from extraction
- #1aac7a (bright mint green) and #e8e9eb (cool gray) appear in extracted palette but are likely Shopify system UI colors (success states, system badges) rather than brand palette — not incorporated into brand tokens
- Dark mode or alternate theme variant unknown; no dark-canvas signals in extraction beyond footer overlay color
- Mega-menu layout and column count not determinable from color/font extraction alone
