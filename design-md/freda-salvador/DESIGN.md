---
version: alpha
name: "Freda Salvador"
source_url: "https://fredasalvador.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The macron over the Ē in FRĒDA — a diacritic most browsers can't render in plain ASCII — sets the brand's governing logic: California directness delivered through European craft precision. Brick-red #ae3838 carries every primary CTA, sale badge, and hover flash against a canvas of warm cream (#f3f1ed, #f9f8f6) that reads more like sun-bleached linen than clinical white. HelveticaNeueCyr grounds the system in a grotesque tradition associated with mid-century European modernism, while Montserrat and proxima-nova extend the family toward legible digital utility — the result is a type stack that never romanticizes or over-softens, reading matter-of-fact in display and body alike. Secondary accents arrive from an unusually wide arc: deep navy (#0e4066), warm amber (#ffe6b5), and muted slate-blue (#84b5cf), all restrained to supporting roles — seasonal campaign banners, promotional ribbons, or editorial callouts — while the primary brick holds sole authority over interactive elements. Buttons are flat rectangles with zero rounding (`{rounded.none}` on primary CTAs), contrasting sharply with the clean imagery-first product cards that carry no shadow and no border decoration. The nav sits in near-black (#212121) on mobile and lifts to the cream canvas on wider breakpoints, creating a strong dark header shelf on small screens that anchors the site's visual weight at the top. Spacing is generous: section gutters at `{spacing.section}` push each product row into its own breathing zone, a pacing choice that positions the brand near footwear peers like Common Projects and Veja rather than the dense grid layouts of fast-fashion Shopify themes. Error surfaces (#f8d7da, #f5c6cb) appear only in form validation, never as brand expression — the reds of the brand are warm brick, not alarm.

colors:
  primary: "#ae3838"
  primary-active: "#d92d20"
  primary-disabled: "#855656"
  primary-dark: "#721c24"
  ink: "#212121"
  ink-deep: "#121212"
  body: "#1a1a1a"
  muted: "#646464"
  hairline: "#dedede"
  hairline-soft: "#f2f2f2"
  canvas: "#f9f8f6"
  surface-cream: "#f3f1ed"
  surface-soft: "#f8f8f5"
  surface-card: "#fafafa"
  surface-warm: "#ffe6b5"
  surface-light: "#f7f9fa"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-navy: "#0e4066"
  accent-slate: "#84b5cf"
  accent-green: "#1a8a51"
  error: "#d92d20"
  error-surface: "#f8d7da"
  error-border: "#f5c6cb"

typography:
  display-xl:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  title-sm:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  label-upper:
    fontFamily: "'Montserrat', 'HelveticaNeueCyr', 'proxima-nova', sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'HelveticaNeueCyr', 'Montserrat', 'proxima-nova', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1.2px
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-text:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 56px
  nav-bar-mobile:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 52px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
  product-card-name:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  product-card-original-price:
    typography: "{typography.price-display}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    minHeight: 600px
    imageOverlay: "rgba(0,0,0,0.15)"
  hero-banner-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    height: 36px
  announcement-bar-promo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    height: 36px
  promo-ribbon:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    height: 36px
  filter-chip:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  size-chip:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    width: 48px
    height: 48px
  size-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  size-chip-unavailable:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    textDecoration: line-through
  color-swatch:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
  color-swatch-active:
    outline: "2px solid {colors.ink}"
    outlineOffset: 2px
    rounded: "{rounded.full}"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.xs}"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxs} {spacing.xs}"
  editorial-callout:
    backgroundColor: "{colors.surface-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    padding: "{spacing.section}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline-soft}"
  footer-heading:
    typography: "{typography.label-upper}"
    textColor: "{colors.on-dark}"

## Components

### Buttons

**`button-primary`** — Flat rectangle with zero rounding, brick-red `{colors.primary}` fill, white text in small uppercase Helvetica at 1.5px tracking. Hover transitions immediately to `{colors.primary-active}` (#d92d20); disabled state softens to `{colors.primary-disabled}` (#855656). The uppercase letter-spacing on `{typography.button-md}` makes each button read like a stamped label — deliberate, unhurried, craft-adjacent.

**`button-secondary`** — Transparent background with a 1px `{colors.ink}` border and ink-colored uppercase text. On hover the button fills solid ink and flips text to white — a hard inversion that signals authority without softening to a pill or ghost treatment. Zero rounding keeps it fully consistent with the primary.

**`button-text`** — Used for secondary inline actions ("Add to Wishlist," "Size Guide"). Transparent, underlined, no padding boxing. Set in `{typography.button-sm}` at 11px uppercase, it recedes visually while remaining scannable.

### Navigation

**`nav-bar`** — On desktop, a 56px bar on the warm cream `{colors.canvas}` ground, separated from content by a 1px `{colors.hairline}` border. Logo centered or left-aligned in near-black; category links in 12px uppercase Helvetica at 1.2px tracking. **`nav-bar-mobile`** — Inverts to solid `{colors.ink}` (#212121) with white text, creating a dark header shelf that anchors small-screen layouts and echoes the footer's dark band.

### Product Cards

**`product-card`** — No rounding, no shadow, no card border. Image fills a 3:4 portrait container; below it the product name in `{typography.body-sm}` and price in `{typography.price-display}` sit on the near-white `{colors.surface-card}` ground with `{spacing.sm}` separation. On sale, price splits into red `product-card-sale-price` beside muted strikethrough `product-card-original-price` — both using the same `{typography.price-display}` spec, differentiated by color alone.

### Badges

**`badge-new`** and **`badge-sale`** — Tight rectangular labels, zero rounding, overlaid at the top-left of product imagery. "NEW" uses `{colors.ink}` fill; "SALE" and percentage discounts use `{colors.primary}`. Both set in 10px `{typography.label-upper}` at 600 weight and 1.5px tracking — small enough to not overrun the image, legible enough to register in a fast scroll.

### Form Elements

**`text-input`** — Flat, no rounding, 48px height, 1px `{colors.hairline}` border at rest. Focus promotes the border to solid `{colors.ink}` — a minimal but unambiguous state change. No inner shadow, no background shift. Placeholder text in `{colors.muted}`.

### Size & Color Selectors

**`size-chip`** — Square 48×48px touch targets with zero rounding and a 1px `{colors.hairline}` border. Active state inverts to ink fill on white text with a solid ink border. Unavailable sizes receive strikethrough text and a softened `{colors.hairline-soft}` border — no diagonal line overlay, keeping the tile uncluttered. **`color-swatch`** — 24px circular chips at `{rounded.full}` with a 1px `{colors.hairline}` ring. Active state adds a 2px ink outline at 2px offset — the only `{rounded.full}` element in a system otherwise composed of hard rectangles.

### Hero & Editorial

**`hero-banner`** — Full-width imagery over a `{colors.ink}` field with a 15% black overlay scrim for text legibility. Display text in `{typography.display-xl}` (48px, weight 300) reads light and editorial — the low weight contrasts the dark background without the aggression of a heavy-weight headline. CTA uses `hero-banner-cta` styling. **`editorial-callout`** — A `{colors.surface-cream}` (#f3f1ed) interstitial band between product sections with `{spacing.section}` padding on all sides. Used for "Designed in California. Handmade in Spain." messaging and seasonal stories — the cream separates it from the grid without adding visual noise.

### Announcement & Promo Bars

**`announcement-bar`** — Ink-black 36px top bar with white `{typography.label-upper}` text for shipping thresholds and sitewide notices. **`announcement-bar-promo`** — Swaps fill to `{colors.primary}` brick-red for flash sales. **`promo-ribbon`** — Warm amber `{colors.surface-warm}` (#ffe6b5) background for seasonal promotions and gift-with-purchase offers that need warmth without triggering the urgency read of the red primary.

### Footer

**`footer`** — Ink-black background mirroring the mobile nav, bookending the page with dark zones at top and bottom. Column headings in `{typography.label-upper}`; links in `{typography.body-sm}` at `{colors.hairline-soft}` — slightly dimmed against the dark ground, legible without glowing. Social icons and brand copyright at the base in the same type scale.

### Filters

**`filter-chip`** — Hairline-bordered flat chips for collection-page filtering (size, color, material, heel height). Active state inverts to ink fill. The zero-rounding language keeps filters visually continuous with the button system rather than introducing a separate pill vocabulary.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; `nav-bar-mobile` dark ink header; hamburger drawer; announcement bar wraps to 2 lines if needed; hero at full viewport height; size chips scroll horizontally in a single row |
| Tablet | 744–1128px | 2-column product grid; nav expands to horizontal links, secondary categories may collapse; hero scales to 480px min-height; filter chips visible inline |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with dropdown flyouts; PDP in side-by-side layout (images left, details right); editorial callout bands at intended width |
| Wide | > 1440px | Content max-width ~1440px centered; hero imagery expands edge-to-edge but text container capped at 1200px; grid holds at 4 columns |

### Touch Targets

- Size chips are minimum 48×48px
- Color swatches are 24px diameter wrapped in a 44px hit area
- Mobile nav links minimum 44px height inside the ink drawer
- Add-to-cart button spans full width on mobile at 48px height
- Filter chips minimum 36px height on mobile

### Collapsing Strategy

- Mobile nav collapses to hamburger icon + centered wordmark + bag icon
- Collection filters move behind a "Filter" modal/drawer on mobile; active filter count shown on the trigger button
- PDP image gallery collapses to a swipeable single image on mobile; thumbnail strip appears on tablet and above
- Footer columns collapse to stacked accordions on mobile with `{colors.hairline}` dividers
- Announcement bar text marquee-scrolls if the message exceeds viewport width at small breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom icon set identified; icon style (line vs filled, stroke weight, corner rounding) not extractable from color/font analysis alone
- Exact font weights for HelveticaNeueCyr variants not confirmed — weight 300 for display and 400/500 for UI are inferred from grotesque display conventions
- Desktop nav height of 56px is inferred from Shopify premium theme norms, not measured directly
- Hover transition timing and easing curves not extractable from static extraction
- Elevation / drop-shadow tokens not observed; assumed flat no-shadow system throughout
- Accent colors (#ffe6b5 amber, #84b5cf slate-blue, #1a8a51 green) may be seasonal or campaign-only rather than evergreen system tokens
- Font loading strategy for proxima-nova (Adobe Fonts vs. self-hosted) not confirmed — may require Adobe Fonts CDN in production
- PDP layout breakpoint (when gallery switches from swipe-single to multi-image grid) not confirmed from static analysis
