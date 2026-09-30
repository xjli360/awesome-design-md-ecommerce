---
version: alpha
name: "Lamy"
source_url: "https://www.lamy.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  FuturaNow headlines and English111AdagioBT calligraphic accents hold a deliberate tension across the Lamy interface — the same tension alive in a pen designed jointly by precision-manufacturing engineers and ink-devoted craftspeople. The structural palette runs dark: #111827 and #1f2937 carry navigation, price labels, and product names at near-black depth, while the canvas lifts to a near-white #f9fafb rather than full white, softening the surface without breaking precision. The one voltage color is emerald green, #059669, surfacing at add-to-cart CTAs, in-stock badges, and promotional accent marks — its {rounded.xs}-cornered pill badges keeping the geometry strict even in celebratory moments. FuturaNow is the dominant headline typeface: its geometric, Bauhaus-derived forms echo the LAMY 2000's barrel geometry and the Safari's utilitarian clip — the brand holds weight at 400 to 600, rejecting the heavy-900 heroism common to consumer electronics. English111AdagioBT appears as a script counterpoint for pull-quote moments and collection headers, a typographic acknowledgment that the product is ultimately about the act of writing, while Genos fills body copy and specification tables where information density is high. Product cards carry {rounded.sm} radius borders and #e5e7eb hairlines over #f3f4f6 surface backgrounds — a catalog structure suited to the dozens of SKU variants per pen model. The brand-signature UI is the nib-width selector: a horizontal row of {rounded.full} pill buttons turning a technical specification into a concrete, clickable choice, with ink color swatches rendered as 24×24px {rounded.full} dots bordered in #d1d5db when unselected and 2px solid {colors.primary} when chosen. Spacing is generous at the section level — {spacing.section} vertical breaks between category rows — but compact at the component level, with card padding at {spacing.base} and form elements at 48px heights; the layout reads as a German industrial catalog come to screen: methodical, unhurried, every specification present without decoration.

colors:
  primary: "#059669"
  primary-active: "#047857"
  primary-disabled: "#f0fdf4"
  ink: "#111827"
  body: "#374151"
  muted: "#6b7280"
  hairline: "#e5e7eb"
  hairline-soft: "#d1d5db"
  canvas: "#ffffff"
  surface-soft: "#f9fafb"
  surface-card: "#f3f4f6"
  on-primary: "#ffffff"
  dark-text: "#1f2937"
  neutral-mid: "#9ca3af"
  charcoal: "#444444"
  error: "#dc2626"
  error-soft: "#fef2f2"
  link: "#2563eb"
  link-active: "#1d4ed8"

typography:
  display-xl:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Genos', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Genos', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Genos', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  script-accent:
    fontFamily: "'English111AdagioBT', Gabriela, Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  button-md:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.3px
  badge:
    fontFamily: "'FuturaNow', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.5px
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
    padding: 14px 24px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 23px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  nav-bar-item-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageAspectRatio: "1/1"
    priceTypography: "{typography.price-display}"
    nameTypography: "{typography.title-sm}"
  nib-selector:
    layout: row
    gap: "{spacing.xs}"
    buttonBackgroundColor: "{colors.canvas}"
    buttonTextColor: "{colors.body}"
    buttonTypography: "{typography.spec-label}"
    buttonRounded: "{rounded.full}"
    buttonBorder: "1px solid {colors.hairline}"
    buttonPadding: "6px 14px"
    buttonHeight: 32px
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.canvas}"
    activeBorder: "1px solid {colors.ink}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderUnselected: "1px solid {colors.hairline-soft}"
    borderSelected: "2px solid {colors.primary}"
    gap: "{spacing.xs}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-stock:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
    padding: "3px 8px"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    displayTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: right
    layout: split-50-50
  hero-script-callout:
    accentTypography: "{typography.script-accent}"
    accentColor: "{colors.primary}"
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.xxl} {spacing.xl}"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-sm}"
    valueColor: "{colors.ink}"
    rowBorder: "1px solid {colors.hairline}"
    padding: "{spacing.md} 0"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    rounded: "{rounded.xs}"
    height: 48px
    padding: "0 {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.neutral-mid}"
    typography: "{typography.body-sm}"
    linkTypography: "{typography.caption}"
    padding: "{spacing.section} {spacing.xl}"
  alert-error:
    backgroundColor: "{colors.error-soft}"
    textColor: "{colors.error}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.md} {spacing.base}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"

## Components

### Buttons

**`button-primary`** — The add-to-cart and primary CTA renders with #059669 emerald fill, uppercase FuturaNow at 14px/0.5px tracking, and zero border radius — hard-cornered geometry that mirrors Lamy's machined pen barrels. Hover deepens to #047857; the disabled state drains to the pale #f0fdf4 wash with #6b7280 muted text to signal unavailability without alarm.

**`button-secondary`** — A 1px #111827 border outline on white canvas at the same 48px height as the primary, with matching uppercase FuturaNow. Used for "Add to Wishlist," model comparison, and secondary navigation prompts; always visually paired alongside the primary so purchase hierarchy is readable at a glance.

**`button-ghost`** — Transparent background, #374151 body-colored text, used for "See all," "View more," and inline text-level CTAs where full button weight would crowd the layout. No border, no radius, no fill — strictly a labeled action.

### Text Input

**`text-input`** — 48px input with 1px #e5e7eb border sharpening to #111827 on focus, {rounded.xs} 4px radius, and Genos body-md text. Placeholder text sits in #9ca3af and clears on entry without a floating label. Used across search, checkout address fields, and newsletter sign-up rows.

### Nav Bar

**`nav-bar`** — 64px tall, white canvas, FuturaNow nav-link at 14px/0.3px tracking. The 1px #e5e7eb bottom hairline separates it from page content. Active category items gain a 2px solid #059669 bottom border and matching text color, producing a minimal emerald underline as the sole decorative nav marker. Logo anchors left; cart and account icons sit right; category links occupy the center.

### Product Card

**`product-card`** — 1:1 product image at top, 1px #e5e7eb border, {rounded.xs} corners, {spacing.base} internal padding. Price in `price-display` (FuturaNow 20px/600), pen name in `title-sm` (FuturaNow 15px/500). Color swatches render as a row of 24px {rounded.full} dots beneath the name. A "New" or "Sale" badge sits as an absolute overlay at the image's top-left corner. On hover, the card border sharpens to #374151 and a ghost "Add to Cart" button slides up from the card's bottom edge.

### Nib Selector

**`nib-selector`** — The signature product configuration UI: a horizontal row of {rounded.full} pill buttons at 32px height labeled with nib grades in spec-label typography — "EF," "F," "M," "B," "BB," and calligraphy variants. Unselected pills carry a 1px #e5e7eb border on white; selected state fills the pill with #111827 and reverses text to white canvas. Gap between pills is {spacing.xs}. On mobile the row scrolls horizontally without wrapping; no chevron or overflow indicator is needed.

### Color Swatch

**`color-swatch`** — 24×24px circles rendered as {rounded.full} inline blocks with a 1px #d1d5db border in the unselected state. On selection, border weight increases to 2px and color shifts to #059669 primary. Swatches arrange in a single row with {spacing.xs} gap; overflow wraps to a second row at narrow widths. A tooltip with the color name (e.g. "Charcoal," "Petrol") appears on hover.

### Badges

**`badge-new`** — #059669 fill, white uppercase FuturaNow at 11px/0.5px, {rounded.xs} corners, 3px 8px padding. Appears as a product-card overlay and inline in listing headers for recently introduced SKUs.

**`badge-sale`** — #dc2626 fill, identical typography and geometry to badge-new. Reserved strictly for price-reduced items; never appears alongside badge-new on the same card.

**`badge-stock`** — Outlined variant: #f3f4f6 fill, 1px #059669 border, #059669 text. Used for "In Stock," "Ships Today," and limited availability notices on product detail pages.

### Hero

**`hero`** — Full-width dark panel with #111827 background and white display-xl FuturaNow text, product photography filling the right 50% on desktop. Top and bottom padding at {spacing.section}; horizontal at {spacing.xl}. A script-accent line from English111AdagioBT sits above the headline in #059669, functioning as a collection label (e.g., "The Classic Returns"). CTA buttons sit inline-flex below the subhead copy.

**`hero-script-callout`** — A lighter mid-page variant on {colors.surface-soft} background, used to introduce sub-collections. The English111AdagioBT line anchors the block visually, separated from the FuturaNow display-md headline by {spacing.sm}.

### Collection Header

**`collection-header`** — Full-width #f9fafb strip at {spacing.xxl} vertical padding, display-md FuturaNow headline in #111827, 1px #e5e7eb bottom border. Serves as the section header for product grid pages and category intros; no subheading — the headline carries alone.

### Spec Table

**`spec-table`** — Two-column definition list: left in spec-label (FuturaNow 11px/uppercase, #6b7280), right in body-sm (Genos 14px, #111827). Rows divided by 1px #e5e7eb lines with {spacing.md} vertical padding. Displays nib material, body material, fill system, country of manufacture, and barrel weight on all product detail pages.

### Search Bar

**`search-bar`** — Full-width on mobile, max 480px on desktop. {rounded.xs} corners, 1px #e5e7eb border sharpening to #111827 on focus, 48px height. Magnifying glass icon at right in #9ca3af. Matches text-input in height and padding for layout consistency across all form contexts.

### Footer

**`footer`** — #111827 dark footer with Genos body-sm white text and caption-scale links in #9ca3af. Four columns: Company, Products, Support, Follow Us. Top separator is 1px #374151. Legal and privacy links appear in a sub-footer row at caption size. The Lamy wordmark in white anchors the bottom-left.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart; hero stacks (image above, text below); nib-selector scrolls horizontally; color swatches wrap at two rows max; spec-table becomes an accordion below the fold |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories without dropdowns; hero splits 50/50; nib-selector fits in one row without scroll |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with hover dropdowns; hero split with constrained text column; spec-table moves to sidebar alongside product images |
| Wide | > 1440px | Max-width container 1440px centered; grid holds at four columns; hero image scales to fill remaining space; side margins increase proportionally |

### Touch Targets

- All interactive elements (buttons, nib pills, swatches, nav links) maintain a minimum 44×44px touch target regardless of visual size
- Color swatches (24×24px visual) are wrapped in 44×44px hit areas using invisible padding
- Nib-selector pills expand to minimum 44px height on mobile breakpoint
- Cart and account nav icons padded to 44×44px tap zones

### Collapsing Strategy

- Navigation collapses to a full-screen slide-in drawer on mobile with a close icon (×) anchored top-right
- Spec-table moves from sidebar to a below-the-fold accordion on mobile, collapsed by default to reduce scroll depth
- Hero switches from side-by-side split to stacked; product image renders above fold, headline and CTA below
- Footer columns stack to single column with disclosure chevrons on mobile, expanded on tap
- Collection-header padding reduces from 48px to 24px on mobile; display-md font size drops to display-sm

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted color palette is dominated by Tailwind CSS scale values (#6b7280, #111827, #1f2937, #e5e7eb, #374151, #059669, etc.); which are explicit brand tokens versus inherited Shopify theme utilities is not determinable from static extraction alone
- No meta theme-color was set; intended browser chrome and PWA accent color are unknown
- FuturaNow is a commercial typeface — exact licensed weight variants and optical sizes available in the deployed build were not confirmed from extraction
- English111AdagioBT and Gabriela usage context (which page regions, which heading levels) is inferred from brand positioning, not directly observed in rendered output
- No explicit product-line accent palette was captured (LAMY Safari seasonal colorways, LAMY AL-star series, LAMY Dialog series)
- Dark-mode treatment is unknown — no prefers-color-scheme overrides were detected
- Animation and transition timing values (hover, drawer open, add-to-cart confirmation flash) were not extractable from static analysis
- Cart drawer vs. full cart page pattern could not be confirmed from the extracted data
- The #007aff value appears to be an iOS system blue injected by the browser; its presence as a brand token is not confirmed
