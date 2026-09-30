---
version: alpha
name: "Satechi (Stands)"
source_url: "https://satechi.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Blaze-orange at `#f55a19` does all the commercial lifting on a page that otherwise insists on restraint — every primary CTA, sale callout, and active-state indicator borrows this same high-Kelvin flame while the broad canvas stays in warm bone tones (`#f5f2ef`, `#ede6e0`, `#cfc6bf`) that echo the brushed aluminum and woven fabric of the physical stands themselves. That pairing — industrial warmth offset by a single hot accent — is the defining visual move. Satechi then layers two auxiliary voltages that never compete for the same real estate: a deep indigo-purple at `#4e34e0` appears in promo banners and price-comparison highlights, and a mint-teal at `#00eab6` surfaces on trust indicators and secondary badges. The three-accent system is unusually legible because each hue maps to a distinct message register — purchase urgency, promotional frame, credibility signal — preventing palette fatigue across long, spec-heavy product pages.

  Typography couldn't be directly extracted: the font stack resolves to `inherit` and a review-widget icon font (`oke-widget-icons`). Satechi's visual density suggests a geometric or neutral grotesque at modest size (15–16px body) with tightly tracked uppercase for category labels and spec headers. The near-black `#222021` carries primary text, softening to `#4c4c4c` for body copy and `#6d6d6d` for secondary descriptors — a three-level ink hierarchy that reads against warm grounds without pure-black harshness.

  Product cards in the stands category carry high information density: thumbnail, model name, rating strip, current price with strikethrough MSRP, and an Add to Cart orange pill — all within a `{rounded.sm}`-cornered white surface (`{colors.surface-card}`) floating against the warm-off-white canvas. Spec comparison tables reach for the navy `#272d45` on row headers, establishing a data-register tone that sits cleanly apart from the product-marketing voice. The error red `#e22120` and info blue `#1878b9` stay strictly functional — form states and notification banners only, never decorative.

  The overall architecture is a Shopify storefront reading as more considered than the platform default: horizontal filter rails, sticky nav with cart count badge, and hero modules that bleed edge-to-edge with overlay text on a dark gradient scrim, all consistent with a mid-market tech accessories brand that wants adjacency to the Apple ecosystem without imitating its monochrome severity.

colors:
  primary: "#f55a19"
  primary-active: "#d44a0f"
  primary-disabled: "#f9c4a6"
  ink: "#222021"
  body: "#4c4c4c"
  muted: "#6d6d6d"
  muted-soft: "#919090"
  hairline: "#dedede"
  hairline-soft: "#e5e5eb"
  canvas: "#fafafa"
  surface-soft: "#f5f2ef"
  surface-warm: "#ede6e0"
  surface-card: "#ffffff"
  surface-cool: "#f4f4f6"
  on-primary: "#ffffff"
  accent-purple: "#4e34e0"
  accent-teal: "#00eab6"
  navy: "#272d45"
  warm-sand: "#cfc6bf"
  error: "#e22120"
  link: "#1878b9"
  scrim: "#222021"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
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
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-uppercase:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
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

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 24px
    height: 44px
  button-primary-active:
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 42px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
  nav-bar-announcement:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageBackground: "{colors.surface-cool}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    msrpColor: "{colors.muted}"
    msrpDecoration: line-through
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    scrimColor: "{colors.scrim}"
    scrimOpacity: 0.55
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaRounded: "{rounded.xs}"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-promo:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  filter-pill:
    backgroundColor: "{colors.surface-cool}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 14px"
    height: 36px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "none"
    padding: "6px 14px"
    height: 36px
  spec-table:
    backgroundColor: "{colors.surface-card}"
    headerBackgroundColor: "{colors.navy}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.label-uppercase}"
    rowTextColor: "{colors.body}"
    rowTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    alternateRowColor: "{colors.surface-soft}"
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    iconColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  promo-banner:
    backgroundColor: "{colors.accent-purple}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    ctaTextColor: "{colors.accent-teal}"
    padding: "{spacing.md} {spacing.base}"
    height: 36px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.warm-sand}"
    mutedColor: "{colors.muted-soft}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Fire-orange `#f55a19` fill with white text at `{typography.button-md}`, `{rounded.xs}` corners keep the shape crisp and tech-adjacent. On hover the fill darkens to `#d44a0f`; disabled state washes to `#f9c4a6` while preserving the geometry. Height locks at 44px so the target stays touch-safe without reading as inflated. This is the only button style that carries full commercial urgency — every add-to-cart and checkout trigger uses it.

**`button-secondary`** — White canvas fill with a 1px `{colors.hairline}` border and ink text; mirrors the primary shape and 44px height exactly. Used for comparison, wishlist, and secondary download CTAs that sit alongside an orange primary. On hover the border steps up to `{colors.ink}` for legibility. Because it shares geometry with the primary, the two never fight for dominance — hierarchy is purely chromatic.

**`button-ghost`** — Transparent fill with a 1px orange border and matching `{colors.primary}` text at `{typography.button-sm}`. Appropriate for white-canvas zones where a filled button would read as error state. Used for "Learn More," "View Specs," and "Compare" roles on PDP pages.

### Product Card

**`product-card`** — A white `{colors.surface-card}` surface with `{rounded.sm}` corners and a `{colors.hairline-soft}` border, floating against the warm-bone canvas. The image zone renders against `{colors.surface-cool}` as a neutral stage for product photography; no drop shadow is added, letting the border do the separation work. Model name in `{typography.title-sm}`, current price in `{typography.price-display}`, and the MSRP strikethrough in `{colors.muted}` create a clear price hierarchy. Rating appears as a star row in `{colors.primary}` orange with review count in `{colors.muted}`. The Add to Cart CTA sits flush at the card bottom with `{colors.primary}` fill and `{rounded.xs}`.

### Hero Banner

**`hero-banner`** — Full-bleed imagery with `{colors.scrim}` overlay at 55% opacity to anchor white headline text at `{typography.display-xl}`. The primary CTA sits at `{rounded.xs}` with `{colors.primary}` fill. On desktop the text block left-aligns within the max-width container; on mobile it centers and the CTA stacks below the headline. Secondary CTAs in the hero use `{typography.button-sm}` with underline rather than a contained shape, keeping the visual field uncluttered.

### Badges

**`badge-sale`** — Orange `{colors.primary}` fill in `{typography.label-uppercase}` at `{rounded.xs}`, positioned top-left of product card images. **`badge-new`** — Mint-teal `{colors.accent-teal}` fill with `{colors.ink}` text, same geometry. **`badge-promo`** — Indigo-purple `{colors.accent-purple}` fill with white text, reserved for bundle deals and limited-time offers. The three badge hues map exactly to Satechi's three-accent system, so the accent color alone communicates message type without additional icons.

### Filter Pills

**`filter-pill`** — Rounded-full pills for category, compatibility, and finish filters in the product list rail. Inactive state: `{colors.surface-cool}` fill with a hairline border in `{typography.button-sm}`. Active state inverts to `{colors.ink}` fill with white text and no border. The sharp contrast between inactive and active avoids any ambiguity about selection state. All pills sit in a horizontally scrollable strip on mobile.

### Spec Table

**`spec-table`** — Dimension, weight, compatibility, and port specs presented in a striped table. Row headers use `{colors.navy}` fill with `{typography.label-uppercase}` in white; data rows alternate between `{colors.surface-card}` and `{colors.surface-soft}`; all cell borders in `{colors.hairline}`. The navy header register reads as distinct from the product-marketing sections above it, signaling a shift from editorial to technical.

### Trust Strip

**`trust-strip`** — A horizontal band in `{colors.surface-soft}` carrying 3–4 icon-plus-label pairs (Free Shipping, Warranty, Returns, Apple Compatibility). Icons render in `{colors.primary}` orange; labels in `{typography.caption}` at `{colors.body}`. Top and bottom `{colors.hairline}` borders frame the strip against adjacent sections. Typically placed below the hero or above the footer.

### Promo Banner

**`promo-banner`** — A full-width bar in `{colors.accent-purple}` carrying announcements or countdown timers in `{typography.label-uppercase}`. CTA link text uses `{colors.accent-teal}` to complete the three-accent system in a single horizontal band. Stacks above the main nav bar so it is the first thing seen on page load.

### Nav Bar

**`nav-bar`** — White `{colors.canvas}` fill, 60px height, bottom `{colors.hairline}` border. Logo sits left, category links center at `{typography.nav-link}`, cart icon and search sit right with orange cart-count badge in `{colors.primary}`. The `{nav-bar-announcement}` strip above uses `{colors.ink}` fill with white `{typography.label-uppercase}` text. On mobile the center links collapse to a hamburger; tapping opens a full-height slide-over drawer on `{colors.surface-card}`.

### Footer

**`footer`** — Near-black `{colors.ink}` fill, four-column link grid on desktop. Column headings in `{typography.title-sm}` white; link lists in `{typography.body-sm}` at `{colors.warm-sand}`. Warm sand on near-black reads as composed and premium rather than the flat white-on-black common to lower-tier tech brands. A hairline separator in `{colors.muted-soft}` divides the link columns from the legal row below.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column PLP grid, hero text centers, filter rail becomes horizontal scroll strip, nav collapses to hamburger drawer, spec table scrolls horizontally with a fade-shadow affordance |
| Tablet | 744–1128px | Two-column PLP grid, hero text left-aligns, filter sidebar appears as collapsible panel at ≥900px, promo banner line wraps to two rows |
| Desktop | 1128–1440px | Three-column PLP grid, sticky nav activates on scroll, hero bleeds full-width with max-width text container, spec table fully visible |
| Wide | > 1440px | Content container caps at ~1360px with lateral canvas whitespace; PLP may shift to four-column grid; hero image scales from center |

### Touch Targets
- All buttons minimum 44px height and 44px minimum width
- Filter pills minimum 36px height with 8px horizontal padding floor
- Nav icon buttons (cart, search, hamburger) padded to 44px × 44px tap area
- Product card CTA row stretches full card width on mobile for easier targeting

### Collapsing Strategy
- Filter sidebar collapses to a modal bottom-sheet on mobile, triggered by a "Filter" ghost button pinned above the product grid
- Spec table scrolls horizontally on narrow viewports; a right-edge shadow indicates overflow
- Footer four-column layout collapses to single-column with expandable accordion sections, each with a `{colors.primary}` orange chevron toggle
- Hero CTA stacks below body text on mobile; secondary text-link CTA is hidden below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Brand typeface not extracted — font stacks resolved only to `inherit` on the live site; `oke-widget-icons` is a third-party review widget font, not a brand asset. All typography tokens above use system-ui fallback. Actual brand font (likely a geometric grotesque such as Inter, DM Sans, or a licensed equivalent) must be substituted once confirmed from Satechi's brand assets or a deeper CSS audit bypassing CDN font-loading.
- Custom icon set not identified — product-category glyphs, port-diagram icons, and compatibility indicators are absent from the extraction and should be audited separately.
- Interaction animations and micro-transitions not captured — hover timing curves, drawer slide duration, image-swap easing, and add-to-cart feedback animations are unknown.
- Dark mode: no `prefers-color-scheme` surface tokens detected; dark-mode behavior and alternate palette are undocumented.
- `primary-disabled` color (`#f9c4a6`) is an interpolated estimate within the orange family — it was not directly extracted from the live site.
- Exact border-radius values for CTAs and cards are inferred from the extracted color palette context; a live DOM audit may reveal tighter or looser values than the `{rounded.xs}` / `{rounded.sm}` assignments above.
