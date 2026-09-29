---
version: alpha
name: "French Paper Co."
source_url: "https://www.frenchpaper.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Fourteen-color paper swatches are the product, so the digital experience inherits the same logic a press operator uses when pulling color: high-chroma primaries against near-neutral substrate. The deep mill teal (#108474) runs the entire CTA system — add-to-cart, navigation active states, form focus rings — while a printer's red (#ec3e3d) and marigold yellow (#fbcd0a) rotate through badge, promotional, and callout surfaces depending on paper line. Dark purple (#23022e) surfaces as a near-black alternative to standard ink, giving the darkest elements a faint coated-stock warmth that plain #000 wouldn't carry. Figtree handles all interface text at modest weights; Times emerges on display headings where heritage copy reads like a letterpress spec sheet rather than a storefront header. Corners stay deliberately flat — {rounded.xs} on inputs, {rounded.sm} on buttons, nothing approaching a pill — echoing the cut-square format of physical paper samples. The spacing system inflates at section level, letting paper photography breathe the way a layout artist opens leading on a specimen broadside. Periwinkle (#899df1) and forest green (#2c7e3f) tag specific paper lines as distinct identities within the larger catalog, functioning less as brand colors and more as paper-family codes the way a Pantone swatch book uses color families. Light surfaces layer across five near-white values (#f9fafb through #fafafa), differentiating page canvas from card surface from input background the way a printer distinguishes 80 lb text from 100 lb cover. The gray ladder runs from #d8d8d8 through #eeeeee in four distinct steps, giving dense product grids enough separation without reaching for hard contrast. The overall register is intentionally printer-forward: more swatches, less gradient; more weight variety, less shadow depth; typographic precision where a production designer would feel immediately at home.

colors:
  primary: "#108474"
  primary-active: "#0a6158"
  primary-disabled: "#7fc2bb"
  accent-red: "#ec3e3d"
  accent-red-deep: "#e14d54"
  accent-yellow: "#fbcd0a"
  accent-periwinkle: "#899df1"
  accent-green: "#2c7e3f"
  accent-blue-tint: "#e4edfa"
  ink: "#090302"
  body: "#121212"
  muted: "#7b7b7b"
  muted-soft: "#aaaaaa"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  hairline-strong: "#d5d5d5"
  hairline-mid: "#e4e4e4"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#fafafa"
  surface-light: "#f9fafb"
  surface-teal: "#edf5f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  purple-dark: "#23022e"

typography:
  display-xl:
    fontFamily: "Times, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Times, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-label:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  paper-family-label:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  swatch-label:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Figtree', 'Nunito Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px

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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
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
    typography: "{typography.button-md}"
    borderColor: "{colors.primary}"
    borderWidth: 1.5px
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    borderColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
  button-accent-red:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-sm-teal:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 32px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline-strong}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 40px
    focusBorderColor: "{colors.primary}"
  text-input-error:
    borderColor: "{colors.accent-red}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.xs}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: "{spacing.base}"
    imageRounded: "{rounded.none}"
  product-card-hover:
    borderColor: "{colors.primary}"
    boxShadow: "0 2px 8px rgba(16,132,116,0.12)"
  swatch-chip:
    width: 32px
    height: 32px
    rounded: "{rounded.none}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    hoverBorderColor: "{colors.ink}"
    hoverBorderWidth: 2px
  swatch-chip-selected:
    borderColor: "{colors.ink}"
    borderWidth: 2px
    outlineColor: "{colors.primary}"
    outlineWidth: 2px
    outlineOffset: 2px
  swatch-grid:
    columns: 8
    columnsMobile: 4
    gap: "{spacing.xs}"
    backgroundColor: "{colors.canvas}"
  swatch-label-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.swatch-label}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    padding: "{spacing.sm} {spacing.md}"
  paper-family-badge:
    backgroundColor: "{colors.surface-teal}"
    textColor: "{colors.primary}"
    typography: "{typography.paper-family-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  paper-family-badge-red:
    backgroundColor: "#fdeaea"
    textColor: "{colors.accent-red}"
    typography: "{typography.paper-family-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  paper-family-badge-yellow:
    backgroundColor: "#fff9e0"
    textColor: "#a07c00"
    typography: "{typography.paper-family-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    minHeight: 480px
    paddingV: "{spacing.section}"
    paddingH: "{spacing.xl}"
  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingV: "{spacing.section}"
    paddingH: "{spacing.xl}"
  collection-header:
    backgroundColor: "{colors.purple-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-lg}"
    labelTypography: "{typography.paper-family-label}"
    labelColor: "{colors.accent-yellow}"
    paddingV: "{spacing.xxl}"
    paddingH: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    height: 40px
    focusBorderColor: "{colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-label}"
    height: 36px
  promo-banner:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    fontWeight: 600
    height: 40px
  paper-spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption-label}"
    labelColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rowPadding: "{spacing.sm} {spacing.base}"
    stripedBackground: "{colors.surface-soft}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline-strong}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    height: 40px
    buttonColor: "{colors.muted}"
    buttonHoverColor: "{colors.ink}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    widthMobile: "100vw"
    borderLeft: "1px solid {colors.hairline}"
    headerTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.surface-soft}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    paddingV: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — The teal (#108474) fill button carries every commercial action: add-to-cart, proceed-to-checkout, submit-quote. Hover deepens to `{colors.primary-active}` (#0a6158); disabled washes out to `{colors.primary-disabled}`. Corners hold at `{rounded.sm}` (8px) — intentionally more squared than consumer soft-goods brands, closer to a registration corner than a pill, consistent with the print-production register of the brand.

**`button-secondary`** — White fill with a 1.5px teal border. Pairs alongside `button-primary` on product detail pages for secondary actions like "request sample" or "save to list." Hover tints the fill to `{colors.surface-soft}` and shifts border to `{colors.primary-active}` to maintain legibility.

**`button-ghost`** — Hairline-bordered, transparent fill, ink text. Used for filter chips, sort controls, and navigation overflow. Carries no color signal beyond text weight, keeping the teal voltage reserved for transactional CTAs.

**`button-accent-red`** — `{colors.accent-red}` (#ec3e3d) fill for flash-sale callouts, clearance CTAs, and urgency notices. Appears at most once per page context to preserve its alarm-register function and avoid competing with the primary teal system.

**`button-sm-teal`** — Compact 32px height for inline table actions: quick-add within ream-quantity grids, reorder from account history, bulk-add to cart from swatch comparison views.

### Navigation

**`nav-bar`** — White 64px bar with a 1px hairline bottom border. Nav links run in `{typography.nav-link}` (Figtree Semi-Bold 14px); active state marks with a 2px teal underline flush to the bar's bottom edge. Logo anchors left in near-black ink. A cart icon with item-count badge uses `{colors.accent-red}` for the dot indicator, consistent with the brand's use of red for urgency signals.

**`announcement-bar`** — 36px teal strip above the nav, uppercase `{typography.caption-label}` in white. Reserved for time-sensitive operational notices — paper production updates, shipping windows, or mill-closure periods — not promotional copy.

### Forms

**`text-input`** — 40px height, 1px `{colors.hairline-strong}` border, `{rounded.xs}` (4px) corners. Focus ring swaps border to `{colors.primary}` with no box-shadow overlay, keeping the interaction lean. Error state replaces border with `{colors.accent-red}`. Placeholder sits in `{colors.muted}`.

**`search-bar`** — Same 40px height as `text-input` but placed on a `{colors.surface-soft}` background panel, anchored in the nav or as a full-width module on collection landing pages. Focus border switches to teal, signaling the same interaction grammar as form inputs.

### Product Card

**`product-card`** — Square-cut images (`{rounded.none}`) inside a card body with `{rounded.xs}` container corners and a 1px `{colors.hairline}` border on `{colors.surface-card}`. Product name in `{typography.title-sm}`, price in `{typography.price}` (Figtree Bold 18px). Hover state adds a teal 1px border with a soft teal shadow, lifting the card without dramatic elevation. Paper-family badges anchor top-left of the image.

### Swatch System

**`swatch-chip`** — 32×32px square color chips that represent individual paper color names from a given paper line. Zero border-radius is load-bearing: the cut-square format directly references the physical die-cut sample. Unselected chips carry a 1px hairline border that thickens to 2px ink on hover. Selected state adds a 2px teal outline with 2px offset, creating a visible gap between chip edge and selection ring.

**`swatch-grid`** — Dense 8-column grid at desktop, collapsing to 6 at tablet and 4 at mobile. Chips gap at `{spacing.xs}` (4px), producing an array reading more like a color field than a product selector. The tightness is intentional — it mirrors how physical swatch books present full-line color ranges side by side.

**`swatch-label-card`** — Small label card beneath or beside each chip carrying the paper color name in `{typography.swatch-label}` (Figtree Medium 11px). White background with hairline border maintains legibility across light and saturated paper colors.

### Badges

**`paper-family-badge`** — Uppercase 10px Figtree Black, 1px letter spacing, square corners (`{rounded.none}`). Three variants: teal text on `{colors.surface-teal}` for standard lines; `{colors.accent-red}` on light red for limited or discontinued stock; yellow-toned text on `#fff9e0` for promotional or featured lines. The badge functions as a paper-family classification tag, not a generic e-commerce status label.

### Collection Headers

**`collection-header`** — Full-width deep purple (#23022e) header band. Times serif `{typography.display-lg}` (36px weight 400) for the paper-line name; family code label in `{typography.paper-family-label}` tinted `{colors.accent-yellow}`. The combination of near-black purple, off-white serif, and marigold label reads as print-archive — closer to a trade catalog masthead than a Shopify collection hero. High contrast ensures legibility over the dark field.

### Hero

**`hero`** — Dark `{colors.ink}` canvas with Times `{typography.display-xl}` headline (52px weight 400) and Figtree `{typography.body-md}` subtext. 480px minimum height with `{spacing.section}` vertical padding. The serif-on-dark pairing signals brand heritage without needing photography as a crutch. Primary CTA button left-aligned on desktop, centered on mobile.

**`hero-light`** — Inverted variant on `{colors.surface-soft}` for seasonal campaigns and secondary landing pages where photography is the primary visual and the text system needs to recede.

### Utility

**`promo-banner`** — 40px marigold (#fbcd0a) strip, Figtree Semi-Bold ink text. Used for free-shipping thresholds and active promotional codes. Yellow is assertive enough to demand attention without requiring uppercase treatment or a red alarm register.

**`paper-spec-table`** — Striped specification table for displaying paper properties: weight (lb / gsm), brightness, finish type, caliper. Column labels in `{typography.caption-label}` (uppercase, muted), values in `{typography.body-sm}`. Alternating rows use `{colors.surface-soft}` (#f7f7f7). This is a core UI pattern — paper purchasers read specs the way software buyers read changelog entries.

**`quantity-selector`** — Inline ream-count stepper for quantity ordering. Minus/plus icon buttons use `{colors.muted}` that darkens to `{colors.ink}` on hover. Border and radius match `text-input` for form-field consistency. The stepper is sized for order quantities in the hundreds, so the input accepts free-form numeric entry, not just tap increments.

**`cart-drawer`** — Right-side slide-over at 400px desktop width, full-width on mobile. White background with a 1px hairline left border. Header title in `{typography.title-md}`; line-item price in `{typography.price}`. Subtotal and checkout CTA anchor at the bottom with a `button-primary` at full width.

**`footer`** — Near-black `{colors.ink}` background, `{typography.body-sm}` white links, teal on hover. Column headings in `{typography.title-sm}` white. Four dense link columns: paper lines, tools and resources, account, and about — structured like a trade catalog back matter, not a marketing footer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; swatch-grid collapses to 4 columns; nav collapses to hamburger drawer; hero reduces to 320px min-height; cart drawer fills full viewport width |
| Tablet | 744–1128px | 2–3 column product grid; swatch-grid at 6 columns; nav shows primary links with overflow in a dropdown; collection-header padding reduces |
| Desktop | 1128–1440px | 4-column product grid; swatch-grid at 8 columns; full horizontal nav; hero at 480px min-height; cart drawer at 400px fixed width |
| Wide | > 1440px | Content container centers at 1440px max-width; hero image bleeds edge-to-edge with text block constrained to 1200px inner column |

### Touch Targets

- All buttons, swatch chips, and nav links maintain a 44px minimum touch target
- Swatch chips display at 32px visually but are wrapped in 44px hit-area padding on mobile
- Quantity selector plus/minus buttons expand to 44px tap zones at mobile even when rendered at 32px
- Cart icon and search icon in the nav bar meet 44px height threshold via padding

### Collapsing Strategy

- Primary nav collapses to hamburger at < 744px; drawer slides from the left with the full link hierarchy
- Swatch grids reflow 8 → 6 → 4 columns across breakpoints; never drop below 4 or chips lose their array-reading quality
- Paper spec tables convert to stacked label/value pairs on mobile, one property per row
- Footer four-column grid collapses to two columns at tablet, single accordion at mobile with each column heading as a toggle
- Hero drops the subhead on mobile; only the display-xl headline and primary CTA remain to preserve above-fold legibility

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No computed border-radius values extracted from the live site; `{rounded.xs}` and `{rounded.sm}` are inferred from DTC print-brand convention and visual inspection
- `JudgemeStar` in the font stack is a Judge.me review-widget artifact and is excluded from brand typography
- `Muli` is the legacy name for Mulish (Google Fonts renamed it); whether it appears as a fallback or a legacy heading stack is unconfirmed — `Figtree` is treated as the primary UI typeface based on stack order
- Individual paper-color hex values for named lines (Dur-O-Tone, Pop-Tone, Speckletone, Construction, etc.) were not captured; live swatch colors appear to be rendered dynamically from product metafields
- Meta theme-color is absent — browser chrome accent color for PWA or Safari is unspecified
- `#e4edfa` (light blue tint) and `#899df1` (periwinkle) appear on specific paper-line pages; their full usage context across the catalog is unconfirmed and may be line-specific rather than global brand tokens
- No motion or animation timing values were extracted; hover transition durations and easing are estimated at 150ms ease convention
- Dark mode support is unknown — no `prefers-color-scheme` tokens or alternate palettes were observed during extraction
