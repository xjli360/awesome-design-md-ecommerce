---
version: alpha
name: "Roxanne Assoulin"
source_url: "https://www.roxanneassoulin.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every page on roxanneassoulin.com opens with the same hard commitment: near-black (#121212) on white, interrupted exactly once by a single charge of lacquer-red (#cf2027) — the color of the brand's most iconic enamel bangles, stacked six-deep in campaign imagery — appearing on the primary CTA, the cart trigger, and occasional promo headlines. The palette extracted from the live site is deliberately sparse: the red, a neutral gray (#dedede) that carries hairlines and disabled states, and the near-black ink. That economy is structural rather than timid. The jewelry itself, photographed in dense color-blocked configurations against bare white, supplies all the chromatic richness the page needs; the site withdraws and holds the frame. No background fills, no decorative gradients — just the product against white, let at full size.

  Navigation is stripped to its minimum: a wordmark in spaced uppercase above a thin rule, with category links (SHOP, ABOUT, STOCKISTS) set in compact uppercase at roughly 12px. Product cards are unbordered and unrounded — hard square crops, product name and price set flush-left below the image in a lightweight sans, no hover overlays beyond a quick-add bar that slides up on pointer contact. The add-to-cart flow collapses into a side drawer, keeping the catalog scroll intact.

  The red (#cf2027) holds its voltage because it appears at a single semantic register: confirming intent. It is not ambient. Secondary interactions — ghost buttons, text links, quantity steppers — draw from #121212 with underlines or reduced-opacity states as affordance signals, never from a second hue. The gray #dedede appears exclusively at the threshold layer: input borders, column separators, rule lines, and the thin horizontal that anchors the navigation bar to the page below it.

  Corner radii across the entire system converge on {rounded.none}. Buttons are rectangles; product cards are rectangles; the search field and quantity inputs are rectangles. This hard-edged posture is not austerity by default — it is deliberate alignment with the jewelry itself, where hard enamel forms and geometric bead arrangements sit at right angles to each other, and softness is found in the colors, not the silhouettes.

colors:
  primary: "#cf2027"
  primary-active: "#a81820"
  primary-disabled: "#e8a0a2"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#767676"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.14em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  wordmark:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.22em
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
    padding: 13px 28px
    height: 44px
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
    border: "1px solid {colors.ink}"
    padding: 12px 27px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    wordmarkTypography: "{typography.wordmark}"
    layout: "wordmark centered, icons right (search, bag, account)"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.body}"
    gap: "{spacing.sm}"
    padding: 0
  product-card-quick-add:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 36px
    position: "overlay-bottom"
    showOn: hover
    transition: "slide-up 150ms ease"
  product-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  product-badge-sold-out:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    layout: "full-bleed image with flush-left headline overlay, or split 50/50 image + text"
    padding: "{spacing.section}"
    ctaStyle: button-primary
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.xl} 0"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    activeIndicator: "2px solid {colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    gap: "{spacing.xl}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
    overlayColor: "rgba(0,0,0,0.3)"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    imageSize: 80px
    rounded: "{rounded.none}"
    borderBottom: "1px solid {colors.hairline-soft}"
    gap: "{spacing.base}"
  footer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    linkTypography: "{typography.nav-link}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"
    columnGap: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — Full-bleed red (#cf2027) rectangle, zero radius, uppercase 12px tracking-wide label in white. On hover transitions to `#a81820`; the shift is perceptible but not theatrical — the button does not grow, lift, or shadow. Disabled state uses `#e8a0a2`, maintaining the red channel while clearly signaling inactivity.

**`button-secondary`** — White fill with a 1px black border, same rectangular silhouette and uppercase typesetting as the primary. Hover inverts to `{colors.ink}` fill with white text, maintaining the same hard-edged authority. Used for secondary purchase actions, newsletter forms, and editorial CTAs where the red would compete with imagery.

**`button-ghost`** — Transparent background, `{colors.ink}` text, underline as the sole affordance signal. Appropriate for "View all," "Learn more," and navigational text links within editorial content blocks where a bordered or filled button would add too much visual weight.

### Navigation
**`nav-bar`** — 56px tall, white background separated from page content by a 1px `#dedede` rule. Wordmark centered in spaced uppercase (`{typography.wordmark}`); category links in compact uppercase (`{typography.nav-link}`) flush-left or as a horizontal cluster; search, account, and bag icons right-aligned. No mega-menu dropdowns suggested by the brand's minimalism — a simple flat list or single-level flyout per category.

**`announcement-bar`** — Collapses to a 36px strip above the nav, black fill with white caption text centered. Used for shipping thresholds, limited-edition drops, or campaign notices. The dark bar provides a strong visual anchor that lifts the wordmark below it.

### Product Grid
**`product-card`** — Square-cropped image at 1:1 ratio, no rounding, no border, no shadow. Product name in `{typography.body-sm}` and price in `{typography.price-display}` sit flush-left beneath the image with `{spacing.sm}` gap. No color swatches are shown at grid level — a deliberate choice for a brand where colorways are the primary differentiator, relying instead on multiple hero images per product.

**`product-card-quick-add`** — A full-width red bar slides up from the bottom of the card image on hover, labeled ADD TO BAG in `{typography.button-sm}`. It does not obstruct the product image at rest. Sold-out cards replace the bar with `product-badge-sold-out` and suppress the quick-add interaction.

**`product-badge`** — Hard black rectangle in `{typography.title-sm}` uppercase, positioned top-left over the image. Used for NEW and LIMITED labels. `product-badge-sold-out` switches to `{colors.hairline}` fill with `{colors.muted}` text, visually retiring the card from active consideration without hiding it.

### Collection Controls
**`collection-filter`** — A horizontal strip of category/filter labels in compact uppercase below the collection header. Active item carries a 2px black underline with full-opacity text; inactive items are `{colors.muted}`. No dropdown panels — filters are inline pill-free text links, consistent with the editorial posture.

**`collection-header`** — Title in `{typography.display-sm}` serif, 1px `{colors.hairline}` rule below, `{spacing.xl}` vertical padding. Optional short editorial description in `{typography.body-md}` for seasonal collections.

### Cart & Purchase Flow
**`cart-drawer`** — Slides in from the right at 400px wide, separated from the page by a 1px border and a 30% black scrim behind. Header reads BAG in `{typography.title-md}` uppercase. Items listed as `cart-item` rows with a thumbnail, name, variant, price, and a quantity stepper. A sticky footer holds the subtotal and the primary CTA button (full-width red, `button-primary`).

### Hero & Editorial
**`hero-banner`** — Either full-bleed photography with a flush-left headline overlaid at `{typography.display-xl}` in serif, or a 50/50 split with image left and headline + CTA right. Background is always white or transparent — no colored panel fills. The serif display type at 42px provides the only editorial weight; the supporting body copy in `{typography.body-md}` is brief and declarative.

### Footer
**`footer`** — White background, 1px top rule, `{spacing.xxl}` vertical padding. Column layout: newsletter signup form (text-input + button-secondary), navigation links in `{typography.nav-link}` uppercase, and legal copy in `{typography.body-sm}`. No brand-color fills, no background tinting — the footer is a quiet administrative zone that matches the page canvas.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered wordmark; hero becomes stacked image above text; cart drawer goes full-width (100vw) |
| Tablet | 744–1128px | Two-column product grid; nav links may abbreviate or collapse to hamburger; hero remains 50/50 or full-bleed |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all category links visible; hero at maximum typographic scale |
| Wide | > 1440px | Grid max-width constrained (~1280px) and centered; no further column addition; typography and spacing unchanged |

### Touch Targets
- All interactive controls (buttons, nav links, quantity steppers, filter labels) maintain a minimum 44px hit area on mobile, even when the visible label is smaller
- Quick-add bar is replaced on mobile with a persistent ADD TO BAG strip that activates on tap rather than hover
- Cart drawer close button is minimum 44×44px in the top-right corner

### Collapsing Strategy
- Navigation collapses to hamburger at mobile breakpoint; the drawer slides in from the left with the full category list in `{typography.nav-link}` uppercase at increased line-height for touch
- Collection filters stack vertically or become a scrollable horizontal strip on mobile, with the active indicator shifting to left-border (3px) rather than bottom-border
- Hero headlines scale down from 42px (`display-xl`) to approximately 28px (`display-md`) on mobile; the serif weight is preserved at all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font families not extracted** — the live site loads type via JavaScript or a third-party font CDN; no `font-family` values were captured. Typography tokens above use system serif/sans fallbacks. Verify the actual typefaces (likely a geometric or humanist sans for UI, and possibly a custom or licensed serif for display) by inspecting the live site's network requests for `.woff2` or `fonts.googleapis.com` calls.
- **Extended color palette unconfirmed** — only three colors were extracted (#cf2027, #dedede, #121212). Surface, muted, and hover tokens are derived by convention. Inspect CSS custom properties or Shopify theme settings for the authoritative secondary palette.
- **Exact button and input border-radius** — confirmed as none/zero by brand posture inference, but not pixel-verified from computed styles.
- **Icon set and style** — nav icons (search, bag, account) style (stroke weight, fill vs outline) not captured; likely thin-line 1.5px stroke in `{colors.ink}`.
- **Product page layout** — media carousel behavior, variant selector style, and size-guide modal styling are not covered; would require deeper page scraping.
- **Animation and transition curves** — no motion tokens extracted; values above (150ms ease) are conventional defaults for this category of brand.
