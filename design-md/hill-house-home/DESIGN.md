---
version: alpha
name: "Hill House Home"
source_url: "https://hillhousehome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Hill House Home's central gesture is the Nap Dress — a garment that straddles garden-party and sleepwear without fully belonging to either — and that productive ambiguity runs through the entire visual system down to its smallest token. The primary is a steel teal (#276680), a color that reads as neither cold corporate blue nor warm coastal aqua but something precisely between: adult, editorial, quietly unexpected on a brand selling ruffled smocked dresses. It anchors navigation, primary CTAs, and the meta theme-color (#43647c), while a soft rose blush (#e48a91) surfaces as the emotional counterpoint — appearing on sale badges, wishlist fills, and seasonal callouts, its warmth drawing the eye without shouting. The canvas pulls back to near-white (#f7f7f8 / #f4f4f6) rather than stark white, giving product photography the diffused quality of afternoon light through sheer curtains. Neutrals span a thoughtful range from deep navy-ink (#272d45) through purple-washed midtones (#676986, #9a9db1) to pale lavender-gray borders (#d3d4dd, #dbdde4), a palette that sits unmistakably closer to editorial fashion than to mass retail's hard black-and-white grid. A bright mint (#b2f9e9) and a saturated teal-green (#00caaa) appear as highlight accents — seasonal promo strips, progress indicators, gift-note callouts — adding a fresh counterpoint against the otherwise restrained ground. Typography was not captured in extraction; the brand's aesthetic suggests an elegant serif face for display headings and a refined geometric sans-serif for body and UI copy, scales set at light-to-regular weights to preserve the softness the product photography depends on. Buttons favor full-pill shapes ({rounded.full}) for primary actions, maintaining the brand's approachable, feminine line quality throughout the purchase funnel. Spacing is generous: product cards breathe on a matte near-white surface, collection grids favor two-up on mobile rather than cramped three-up, and editorial sections command full-bleed photography with copy laid over soft teal scrim overlays.

colors:
  primary: "#276680"
  primary-active: "#1e5469"
  primary-disabled: "#b8ccea"
  primary-light: "#e8f4fe"
  accent-rose: "#e48a91"
  accent-rose-soft: "#faeded"
  accent-mint: "#b2f9e9"
  accent-teal: "#00caaa"
  accent-teal-dark: "#0e7a82"
  brand-steel: "#43647c"
  ink: "#121212"
  body: "#272d45"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#d3d4dd"
  hairline-soft: "#dbdde4"
  canvas: "#ffffff"
  surface-soft: "#f7f7f8"
  surface-card: "#f4f4f6"
  surface-neutral: "#e5e5eb"
  navy-deep: "#2c3e50"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
    fontStyle: italic
  display-lg:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.04em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  overline:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.04em
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  price-sale:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-megamenu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    categoryHeaderTypography: "{typography.overline}"
    categoryHeaderColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xl} 0"
  announcement-bar:
    backgroundColor: "{colors.brand-steel}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    imageRatio: "3/4"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
  product-card-badge-sale:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  product-card-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.full}"
    padding: "3px 10px"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderUnselected: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
    soldOutOverlay: "diagonal-slash"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.primary}"
    padding: "8px 12px"
    unavailableTextDecoration: "line-through"
    unavailableColor: "{colors.muted-soft}"
  price-regular:
    textColor: "{colors.body}"
    typography: "{typography.price}"
  price-sale:
    textColor: "{colors.accent-rose}"
    typography: "{typography.price-sale}"
  price-compare:
    textColor: "{colors.muted}"
    typography: "{typography.price}"
    textDecoration: line-through
  wishlist-icon:
    activeColor: "{colors.accent-rose}"
    inactiveColor: "{colors.muted-soft}"
    size: 20px
    touchTarget: 44px
  hero-full-bleed:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.on-primary}"
    overlayColor: "rgba(39, 102, 128, 0.30)"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    ctaVariant: button-primary
  collection-banner:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.display-md}"
    padding: "{spacing.xxl} 0"
    textAlign: center
  collection-grid:
    columns: 4
    gap: "{spacing.base}"
    pageBackground: "{colors.surface-soft}"
  promo-banner:
    backgroundColor: "{colors.accent-mint}"
    textColor: "{colors.navy-deep}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  promo-banner-sale:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
  email-capture:
    backgroundColor: "{colors.primary-light}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.display-sm}"
    inputBackground: "{colors.canvas}"
    inputRounded: "{rounded.full}"
    inputBorder: "1px solid {colors.hairline}"
    buttonRounded: "{rounded.full}"
    buttonBackground: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.xl}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-md}"
    borderLeft: "1px solid {colors.hairline-soft}"
    width: 400px
    footerBackground: "{colors.surface-card}"
  footer:
    backgroundColor: "{colors.navy-deep}"
    textColor: "{colors.surface-neutral}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.surface-neutral}"
    headingTypography: "{typography.overline}"
    headingColor: "{colors.on-primary}"
    padding: "{spacing.section} 0"
    columns: 4

## Components

### Buttons
**`button-primary`** — Full pill (`{rounded.full}`) in brand steel teal (#276680), uppercase-spaced 13px lettering, 48px height with generous 32px side padding. Hover and press deepen to `{colors.primary-active}` (#1e5469); the disabled state uses washed sky blue (`{colors.primary-disabled}`) rather than gray, a gentler signal that keeps the palette coherent.

**`button-secondary`** — White fill with a 1px teal border and teal text at matching pill radius. Reads cleanly against both white and `{colors.surface-soft}` backgrounds. On hover the border strengthens slightly and the fill picks up a faint teal wash (`{colors.primary-light}`).

**`button-ghost`** — Transparent with a 1px `{colors.hairline}` border at 40px height. Used for secondary card-level actions — wishlist toggles, quick-add overlays — where the primary CTA already dominates the surface.

### Navigation
**`nav-bar`** — White 64px header with a bottom hairline in `{colors.hairline-soft}`. Logo sits centered or left-aligned; search, account, and cart icons cluster right. The mobile variant replaces category links with a hamburger that triggers a full-height drawer.

**`nav-megamenu`** — Drops on hover with white surface and substantial internal padding (`{spacing.xl}`). Category labels use `{typography.overline}` in `{colors.muted}`; product and editorial links use `{typography.body-sm}`. A featured image panel occupies the rightmost column, typically showing the season's hero product.

**`announcement-bar`** — A sticky 36px strip directly above the nav in `{colors.brand-steel}` (#43647c), white caption text carrying shipping thresholds or promo codes. Swaps to `{colors.accent-mint}` background with `{colors.navy-deep}` text for site-wide sale moments.

### Product Cards
**`product-card`** — White surface, 3:4 portrait image ratio, minimal `{rounded.xs}` corner treatment. Color swatches render below the image as 20px circles (`{rounded.full}`), product name in `{typography.body-sm}`, price in `{typography.price}`. On hover a secondary image cross-fades and a quick-add button rises from the card's lower edge.

**`product-card-badge-sale`** / **`product-card-badge-new`** — Full-pill badges (`{rounded.full}`) pinned top-left over the product image. Sale uses rose blush (#e48a91); New Arrival uses primary teal (#276680). Both render in `{typography.overline}` — 11px all-caps at 0.12em letter-spacing — keeping the label unobtrusive against the photography.

**`color-swatch`** — 20px circles in a horizontal strip. The selected swatch gets a 2px primary-teal ring with a 2px gap between ring and fill; unselected sits behind a 1px `{colors.hairline}` border. Sold-out swatches carry a diagonal slash overlay rather than hiding them entirely.

**`size-selector`** — Inline pill-shaped tiles in white with `{colors.hairline}` border, switching to `{colors.primary}` border when selected. Unavailable sizes remain visible with strikethrough text in `{colors.muted-soft}`.

### Hero & Editorial
**`hero-full-bleed`** — Full-viewport photography with a soft teal-wash scrim (`rgba(39, 102, 128, 0.30)`) over darker imagery. Headline runs `{typography.display-xl}` (serif italic) centered or left-offset; the CTA sits directly below in the primary pill style. On mobile the image crops to square or 4:5, with headline and button stacking below the image rather than overlaying it.

**`collection-banner`** — A quieter editorial header at the top of collection pages: white or `{colors.surface-card}` ground, `{typography.display-md}` serif headline centered, no photography overlay. Keeps the transition from nav to grid clean.

**`collection-grid`** — Four-column grid on desktop with `{spacing.base}` gaps on a `{colors.surface-soft}` page field. Collapses to two columns at tablet and two columns on mobile — never one, as the portrait-format cards need width to read.

### Promotions
**`promo-banner`** — A 40px site-wide strip in `{colors.accent-mint}` (#b2f9e9) with `{colors.navy-deep}` text for standard promotions; swaps body to `{colors.accent-rose}` fill with white text during clearance or flash events. Both use centered `{typography.caption}`.

**`email-capture`** — A `{colors.primary-light}` (#e8f4fe) full-width module deployed at section breaks and on the Nap Dress waitlist page. Houses a pill-shaped input and a pill primary button in a single row on desktop; stacks vertically on mobile.

### Pricing
**`price-regular`** uses `{typography.price}` in `{colors.body}` with no decoration. **`price-sale`** switches to `{colors.accent-rose}` to signal the discount in brand palette rather than generic red. **`price-compare`** renders original price with strikethrough in `{colors.muted}`, displayed inline next to the sale price.

### Cart & Wishlist
**`cart-drawer`** — A 400px right-anchored drawer on white, separated from content by a 1px `{colors.hairline-soft}` left border. Product thumbnails at 64×64px; name, color, and size in `{typography.body-sm}`; order subtotal in `{typography.title-md}`. A sticky footer zone inside the drawer holds the full-width pill Checkout button.

**`wishlist-icon`** — 20px heart icon with a 44px touch target. Unfilled in `{colors.muted-soft}` at rest; fills to `{colors.accent-rose}` (#e48a91) on save, rhyming with the brand's rose accent across sale and promotional surfaces.

### Footer
**`footer`** — Deep navy ground (`{colors.navy-deep}` #2c3e50), four columns on desktop. Column headers in `{typography.overline}` white; body links in `{typography.body-sm}` at `{colors.surface-neutral}` opacity. A full-width `email-capture` strip sits immediately above the columns. On mobile the columns collapse into a stacked accordion.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 2-col product grid; hamburger nav with full-height slide-in drawer; hero image stacks above text; cart drawer fills full width; announcement bar truncates to single line with scroll |
| Tablet | 744–1128px | 2-col product grid; megamenu replaced by tap-to-expand accordion nav; hero text overlaid at `{typography.display-md}` scale; editorial modules shift to side-by-side |
| Desktop | 1128–1440px | 4-col product grid; megamenu hover panels with featured image column; full-bleed hero at `{typography.display-xl}`; 400px fixed cart drawer |
| Wide | > 1440px | Grid and content columns max at ~1400px with auto side margins; hero photography fills edge-to-edge; inner content bound stays at 1280px |

### Touch Targets
- Primary and secondary pill buttons minimum 48px height, full-width on mobile
- Color swatches padded to minimum 28px tap target regardless of 20px visual size
- Wishlist and quick-add icons padded to 44×44px tap area
- Nav drawer rows minimum 48px height
- Cart quantity stepper buttons minimum 40×40px
- Size-selector tiles minimum 44px height on mobile

### Collapsing Strategy
- Product grid: 4-col → 2-col → 2-col (portrait cards need horizontal room; single-col is never used)
- Hero: text-overlaid full-bleed → stacked image-above-text with full-width CTA
- Editorial split modules (image + text): side-by-side 50/50 → image-above, text-below
- Footer columns: 4-col → 2×2 → single-column stacked accordion with expand/collapse
- Megamenu: hover panel with image column → full-screen overlay drawer
- Announcement bar: static centered text → marquee scroll when content overflows viewport

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Custom typefaces not extracted**: Extraction returned only `oke-widget-icons` (OKendo reviews widget) and `inherit` — no brand typeface names were captured. Display and body font stacks above are inferred from the brand's editorial aesthetic. Verify actual font families, weights, and sizes from a DevTools network waterfall on hillhousehome.com.
- **Exact button border-radius**: Pill vs. rounded-rect preference inferred from brand softness; confirm computed `border-radius` values via DevTools inspector.
- **Typography scale values**: All `fontSize`, `fontWeight`, and `lineHeight` values are editorial estimates — no CSS typography tokens were extracted.
- **Animation and transition tokens**: No duration, easing, or motion preference data was captured.
- **Dark mode**: No dark-mode color alternates detected in extraction.
- **Icon system**: No brand icon font or SVG sprite identified beyond OKendo widget glyphs.
- **`#0078d7` exclusion**: This standard Microsoft/Edge focus-ring blue was excluded from the palette as a likely browser default rather than a brand token — confirm whether it appears in brand UI.
- **Mobile nav pattern**: Hamburger drawer vs. bottom tab bar not confirmed; hamburger inferred from Shopify defaults and brand site scale.
- **Exact grid gap and padding values**: Column counts and spacing tokens above are inferred; verify against the live computed grid layout.
