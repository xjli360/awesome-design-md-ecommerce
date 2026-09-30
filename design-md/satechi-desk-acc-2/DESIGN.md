---
version: alpha
name: "Satechi"
source_url: "https://satechi.net"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Two simultaneous voltage colors run on Satechi's storefront — a charged orange (#f55a19) on every primary CTA, add-to-cart action, and sale badge, and a deep indigo (#4e34e0) that surfaces in promotional announcement bars and secondary accent moments — an assertive pairing that reads more product-launch than the serene aluminum-desk-accessory category it occupies. The near-black #222021 anchors both the nav header and the product photography backdrop; aluminum peripherals photograph cleanly against it, giving the storefront a studio-showroom quality that justifies premium pricing without requiring lengthy editorial copy. Below the fold the brand decompresses into warm neutrals: off-white (#f5f2ef), a barely-cool surface-card (#f4f4f6), and layered taupe bands (#cfc6bf, #ede6e0) that absorb the high-contrast hero and let the SKU-dense product grid breathe.

  A third accent — bright teal #00eab6 — appears in loyalty badges and callout highlights, isolated enough to carry its own signal without diluting the orange primary. Dark slate sections (#272d45) frame the footer and deep-link promotional blocks, giving the page a dark-light-dark bracketed rhythm that mirrors how premium hardware packaging presents itself. The color logic is unambiguous: orange moves inventory, indigo announces events, teal rewards customer behavior, and dark-section backgrounds hold navigational weight.

  No brand typeface was captured in extraction — only a third-party review-widget icon font surfaced — so the spec defaults to a clean system geometric sans-serif and flags the font family as a known gap. Radius language stays conservative: buttons at {rounded.sm}, cards at {rounded.xs}, category filter pills at {rounded.full}, but primary CTAs never pill — the brand keeps action shapes angular enough to signal precision over warmth. Spacing runs a clear section rhythm at {spacing.section} between major content blocks, tight {spacing.sm}–{spacing.base} grid gaps within the product shelf, and generous {spacing.xl}–{spacing.xxl} padding inside hero areas. The net effect is a DTC tech storefront that builds credibility through photographic density and color discipline rather than editorial illustration — every color token either moves a product, marks a state, or brackets a section.

colors:
  primary: "#f55a19"
  primary-active: "#d44c14"
  primary-disabled: "#f9bfa0"
  accent-indigo: "#4e34e0"
  accent-teal: "#00eab6"
  error: "#e22120"
  info: "#1878b9"
  ink: "#222021"
  ink-secondary: "#1b1c21"
  body: "#4c4c4c"
  muted: "#757679"
  muted-subtle: "#919090"
  hairline: "#dedede"
  hairline-soft: "#e5e5eb"
  canvas: "#fafafa"
  surface-soft: "#f5f2ef"
  surface-card: "#f4f4f6"
  surface-warm: "#ede6e0"
  surface-taupe: "#cfc6bf"
  dark-nav: "#222021"
  dark-section: "#272d45"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent-teal: "#222021"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
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
    rounded: "{rounded.sm}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.dark-nav}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    logoHeight: 28px
    borderBottom: none
  announcement-bar:
    backgroundColor: "{colors.accent-indigo}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageRounded: "{rounded.xs}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-new:
    backgroundColor: "{colors.accent-indigo}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-featured:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-accent-teal}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  hero-section:
    backgroundColor: "{colors.dark-nav}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.section}"
  category-pill:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  swatch-selector:
    size: 24px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    inactiveBorder: "1px solid {colors.hairline}"
    selectedOffset: 2px
  section-header:
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    accentBarColor: "{colors.primary}"
    accentBarHeight: 3px
    marginBottom: "{spacing.lg}"
  product-spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline-soft}"
    labelTypography: "{typography.caption-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  promo-banner:
    backgroundColor: "{colors.dark-section}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-sm}"
    accentColor: "{colors.accent-teal}"
    paddingY: "{spacing.xxl}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.dark-section}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-subtle}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    paddingY: "{spacing.xxl}"
    columnGap: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — The primary CTA carries the charged orange (#f55a19) fill with white type at {typography.button-md} (15px/600), sitting at 44px tall with {rounded.sm} corners. On hover it transitions to #d44c14 via `button-primary-active`; on disabled state it fades to the pale wash #f9bfa0. This button is reserved exclusively for add-to-cart, buy-now, and primary lead-generation actions — the orange is never diluted across secondary or decorative elements.

**`button-secondary`** — Transparent fill with a 1.5px {colors.ink} border at {rounded.sm}, matching the primary in height and radius. Used for "Learn More", collection navigation, and secondary CTAs where the orange primary would oversaturate the page. On hover, the border darkens toward full black; no fill is added, preserving the outline treatment.

**`button-ghost`** — Text-only in {colors.primary} orange with no border or background. Appears as "See all" links in section footers and low-hierarchy inline navigation. Does not carry the same interaction weight as button-primary and should not compete with it on the same viewport section.

### Navigation

**`nav-bar`** — A flat {colors.dark-nav} (#222021) bar at 60px tall with no border-bottom divider. The brand logo anchors left; category links at {typography.nav-link} (14px/500) in white run to the right. Search, account, and cart icons sit at the far right, each with minimum 44px tap zones. The dark bar creates a sharp contrast flip when the page transitions into the warm-neutral body below, reinforcing the dark-top bracket structure.

**`announcement-bar`** — A 36px full-width stripe in {colors.accent-indigo} (#4e34e0) pinned above the nav. Carries sitewide promotions, free-shipping thresholds, and launch countdowns at {typography.caption} in white, centered. The indigo bar is the first visual signal on every page load — it establishes the secondary accent color before the orange primary surfaces in the body.

### Product Grid

**`product-card`** — Cards sit on {colors.surface-card} (#f4f4f6) with {rounded.xs} radius — present enough to soften corners, subtle enough not to read as decorative rounding. Product photography fills the image zone; the title runs {typography.title-sm} in {colors.ink}; the price runs {typography.price-display} (18px/700). Badge overlays anchor to the top-left corner of the image area. On hover, a secondary product angle typically cross-fades or a subtle drop shadow lifts the card.

**`badge-sale`** — Orange (#f55a19) fill, white type at {typography.badge} (11px/700), {rounded.xs}. The sale badge is the primary vehicle by which the orange primary enters the product grid; it is never applied decoratively, only to mark a genuine price reduction.

**`badge-new`** — Indigo (#4e34e0) fill, identical sizing and radius to `badge-sale`. Reserved for recently launched SKUs, typically within the first 30–60 days of availability. The indigo-versus-orange badge system lets customers visually sort newness from value at a glance.

**`badge-featured`** — Bright teal (#00eab6) fill with {colors.on-accent-teal} ink text, used for editorial callouts such as "Editor's Pick" or loyalty-tier highlights. Constrained to one per visible shelf row to prevent teal from spreading into ambient noise.

### Product Detail

**`swatch-selector`** — 24px circular chips at {rounded.full} for color and finish variant selection. The active state draws a 2px {colors.ink} ring offset 2px from the chip edge, creating a halo without altering the chip itself. Inactive chips sit behind a 1px {colors.hairline} ring. Both PDP and product-card hover states share this component.

**`product-spec-table`** — A {colors.surface-soft} background specification block with hairline-bordered rows. Labels run {typography.caption-label} (11px/600/uppercase) in {colors.muted}; values run {typography.body-sm} in {colors.ink}. This is Satechi's primary trust surface: USB wattage, port count, compatibility matrix, and dimensions live here — the data that converts a browsing session into a purchase for the technical accessories buyer.

### Layout & Marketing

**`hero-section`** — Full-width dark canvas ({colors.dark-nav}) block with the headline at {typography.display-xl} (48px/700) and supporting copy at {typography.body-md}. Vertical padding at {spacing.section} (64px) on both sides. The hero typically stages a product in three-quarter view against the dark background, with `button-primary` as the sole CTA. On mobile the image stacks above the copy block and the CTA expands to full width.

**`section-header`** — Section titles at {typography.display-md} (28px/600) in {colors.ink}. Selected section headers — "New Arrivals", "Best Sellers", "Featured Collections" — carry a 3px {colors.primary} accent bar below or beside the heading text. This is the only context where orange appears as a purely decorative mark rather than an interactive affordance.

**`category-pill`** / **`category-pill-active`** — Horizontal scrolling filter chips at {rounded.full}. Inactive: {colors.surface-card} fill, {colors.hairline} border, {colors.body} text. Active: inverts to {colors.ink} fill with white text. The pill shape is reserved for filters and category navigation; primary CTAs use {rounded.sm} to maintain a distinct affordance language between filtering and purchasing actions.

**`promo-banner`** — Full-width {colors.dark-section} (#272d45) block with headline at {typography.display-sm} and key numerical callouts (e.g., discount percentages, product counts) rendered in {colors.accent-teal}. Used between grid sections to interrupt visual monotony and surface campaign messaging. The teal-on-dark combination is the highest-contrast accent state in the palette.

**`footer`** — {colors.dark-section} base with column headings at {typography.title-sm} in white and body links at {typography.body-sm} in {colors.muted-subtle}. Newsletter capture uses `text-input` against the dark background with a `button-primary` CTA alongside it. The dark footer closes the page's dark-light-dark bracket, returning visual weight to where the nav opened it.

**`search-bar`** — Compact 40px field in {colors.surface-card} with {rounded.xs} and a {colors.hairline-soft} border. Placeholder text at {colors.muted}; on focus a {colors.primary} border ring appears. On desktop the search bar typically collapses into an icon that expands inline; on mobile it opens as a full-width overlay panel with autocomplete suggestions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + icon row; hero stacks image above copy block with full-width CTA; category pills scroll horizontally; spec table converts to stacked label-value pairs; filters move to bottom-drawer panel |
| Tablet | 744–1128px | 2-column product grid; nav shows logo and icon row with slide-out drawer for categories; hero maintains side-by-side layout; announcement bar persists |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with all category links visible; announcement bar pinned to top; hero at full viewport width with product image right-aligned |
| Wide | > 1440px | Max-width container (~1440px) centered with auto lateral margins; hero photography bleeds edge-to-edge within container; product grid gains additional column at far-wide breakpoints |

### Touch Targets
- All interactive controls maintain a minimum 44×44px tap area
- Swatch selectors are 24px visually but sit within a 44px invisible tap zone via padding
- Mobile nav icons (search, cart, account) each occupy 44px tap zones with no overlap
- Category pills gain extra vertical padding on mobile to reach the 44px touch height minimum
- Add-to-cart button expands to full width on mobile for single-thumb reachability

### Collapsing Strategy
- Primary nav collapses to hamburger icon at < 744px; mega-menu becomes a full-screen slide-over drawer with category hierarchy intact
- Product filters shift from inline horizontal pill row to a bottom-sheet drawer panel on mobile
- Footer multi-column layout collapses to single-column accordion with tap-to-expand section headers
- Hero copy block stacks vertically below the product image on mobile; CTA button spans full container width
- Announcement bar persists across all breakpoints; text truncates with ellipsis below 360px viewport width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Brand typeface not extracted** — only third-party Okendo review-widget icon fonts (oke-widget-icons) were detected in font-family stacks; the actual brand typeface loads dynamically via JavaScript and could not be captured. All typography tokens use a system UI fallback.
- **primary-active and primary-disabled** hex values are arithmetically derived from #f55a19 (darkened / lightened), not directly extracted from site CSS.
- **No meta theme-color defined** — mobile browser chrome color is unspecified; no pinned theme color exists in page metadata.
- **Accent usage boundaries** — the contexts separating #4e34e0 (indigo) and #00eab6 (teal) are inferred from color prominence and DTC conventions, not confirmed via full sitemap extraction.
- **Dark-mode variant** — the dark nav and dark section colors (#222021, #272d45) may participate in a full dark-mode theme; no explicit dark-mode CSS custom property declarations were found to confirm or deny this.
- **Button and card radius** — actual computed border-radius on CTAs and product cards was not measured from the live site; {rounded.xs} (4px) for cards and {rounded.sm} (8px) for buttons are visual estimates.
- **Typography scale** — all fontSize, fontWeight, lineHeight, and letterSpacing values are estimated from category norms for a Shopify tech-accessories storefront; no computed CSS metrics were captured.
- **Grid column count and gutter widths** — product grid column counts and gap values are inferred from standard Shopify theme conventions, not measured from live DOM.
