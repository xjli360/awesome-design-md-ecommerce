---
version: alpha
name: "The Paper Mill Store"
source_url: "https://www.thepapermillstore.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Forty-three paper weights listed on a single category page — The Paper Mill Store's real design challenge is taxonomy, not aesthetics. The store sells paper as a commodity with craft-grade specificity: 60 lb text, 80 lb cover, linen finish, laid finish, bright white vs. natural white, by the sheet or by the ream. The visual system has to carry a catalog with hundreds of SKUs that differ by properties invisible in a thumbnail, so every product tile leans heavily on typographic metadata — weight, finish, size — rather than lifestyle photography. The palette skews toward print-industry neutrals: a warm ivory canvas (#faf8f0) evokes the stock itself, while a deep burgundy primary (#9b1f3a) reads as an ink-press red, credible to paper buyers who deal in PMS swatches. Supporting surfaces stay close to white so product paper-color samples read accurately; any tint on the background would corrupt color perception for a customer comparing Natural White to Bright White. Typography leans on a workhorse sans-serif at modest weights for body copy, then switches to a slightly condensed weight for category labels and spec lines — mirroring the structured information hierarchy of a paper mill spec sheet. Buttons are modestly rounded ({rounded.sm}) rather than fully pill-shaped, matching the no-nonsense posture of an industrial supplier that also serves wedding stationers. The nav organizes by paper type, occasion, and format — three taxonomies that overlap — so breadcrumbs and filter chips are load-bearing UI, not decorative. Footer sections list brand names, paper lines, and certifications (FSC, recycled content), positioning the store as a verifiable supply-chain partner rather than a lifestyle retailer. The entire system is calibrated for a customer who arrives knowing what they want and needs the UI to get out of the way of the spec.

colors:
  primary: "#9b1f3a"
  primary-active: "#7a1630"
  primary-disabled: "#d9a0ab"
  primary-light: "#f5e8eb"
  ink: "#1c1c1c"
  body: "#3a3a3a"
  muted: "#6b6b6b"
  muted-soft: "#9a9a9a"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#faf8f0"
  surface-soft: "#f5f3ec"
  surface-card: "#ffffff"
  surface-strong: "#edeae0"
  on-primary: "#ffffff"
  accent-navy: "#1e3456"
  accent-gold: "#c8a84b"
  spec-tag-bg: "#f0ede4"
  spec-tag-text: "#4a4232"
  success: "#2d6a4f"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Georgia', 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  spec-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-category:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  breadcrumb:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    border: none
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1.5px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  button-add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
    width: 100%
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.lg}"
  nav-top-utility:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 32px
    padding: "0 {spacing.lg}"
  nav-mega-dropdown:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    borderTop: "2px solid {colors.primary}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.10)"
    padding: "{spacing.xl}"
  nav-category-header:
    textColor: "{colors.primary}"
    typography: "{typography.nav-category}"
    marginBottom: "{spacing.sm}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md}"
    boxShadow: none
  product-card-image:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    aspectRatio: "1 / 1"
    objectFit: contain
  product-card-title:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-spec-line:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
  product-card-price:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    marginTop: "{spacing.xs}"
  spec-chip:
    backgroundColor: "{colors.spec-tag-bg}"
    textColor: "{colors.spec-tag-text}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  spec-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: "10px 14px"
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: "10px 14px 10px 40px"
    height: 40px
    iconColor: "{colors.muted}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    borderRight: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    width: 240px
  filter-group-label:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    paddingBottom: "{spacing.sm}"
    borderBottom: "1px solid {colors.hairline-soft}"
    marginBottom: "{spacing.sm}"
  filter-checkbox-label:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  breadcrumb-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.breadcrumb}"
    padding: "8px {spacing.lg}"
    separatorColor: "{colors.hairline}"
  breadcrumb-current:
    textColor: "{colors.ink}"
    typography: "{typography.breadcrumb}"
  hero-banner:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.section}"
    minHeight: 280px
  hero-eyebrow:
    textColor: "{colors.accent-gold}"
    typography: "{typography.spec-label}"
    marginBottom: "{spacing.sm}"
  hero-headline:
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    marginBottom: "{spacing.base}"
  hero-sub:
    textColor: "#c8d4e8"
    typography: "{typography.body-md}"
    maxWidth: 480px
  category-tile:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    overflow: hidden
    textAlign: center
  category-tile-label:
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.md} {spacing.sm}"
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  new-badge:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  quantity-selector:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    height: 40px
    buttonWidth: 36px
  swatch-selector:
    size: 28px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.primary}"
    borderUnselected: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
  pagination:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "6px 10px"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "#c8d4e8"
    padding: "{spacing.xxl} {spacing.section} {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-category}"
    marginBottom: "{spacing.base}"
  footer-link:
    textColor: "#c8d4e8"
    typography: "{typography.body-sm}"
    hoverColor: "{colors.on-primary}"
  footer-bottom:
    backgroundColor: "#121e33"
    textColor: "#7a8fa8"
    typography: "{typography.caption}"
    padding: "{spacing.base} {spacing.section}"

## Components

### Buttons

**`button-primary`** — A 44px-tall burgundy button with 4px radius and uppercase tracked sans-serif label; used exclusively for add-to-cart, proceed-to-checkout, and primary form submissions. Active state darkens to `#7a1630` without scale animation — the brand avoids playful micro-interactions that would feel out of place in a supply-grade context. Disabled state uses a desaturated rose (`#d9a0ab`) and sets `cursor: not-allowed`. On mobile the button expands to full width and gains 4px additional height.

**`button-secondary`** — Hollow variant with a 1.5px burgundy border on the warm canvas background; used for secondary actions like "View Details", "Download Spec Sheet", and "Save to List". The border makes it legible against both the `{colors.canvas}` and `{colors.surface-soft}` backgrounds common in the sidebar.

**`button-ghost`** — Neutral border, no brand color; used for tertiary actions in filter panels, quantity adjustments, and "Clear All" controls. Keeps the interface from looking too red-heavy when multiple action levels appear together.

**`button-add-to-cart`** — Full-width variant of `button-primary` (48px tall) used in product detail pages. The extra height creates a stable touch target when the customer is toggling weight, size, and quantity options above it.

### Navigation

**`nav-top-utility`** — A 32px navy bar above the main nav carries shipping thresholds, sale announcements, and account/cart links in 12px caption text. The navy (`#1e3456`) creates a clear tier separation from the warm canvas below without requiring a drop shadow.

**`nav-bar`** — 56px canvas bar with a single bottom hairline. Category links use `{typography.nav-link}` at 13px/500 weight — deliberately understated so the mega-dropdown column headers can punch louder. No logo animation; the store name stays static, communicating stable authority rather than expressiveness.

**`nav-mega-dropdown`** — Full-width panel anchored with a 2px burgundy top border that visually connects the dropdown to the triggering nav item. Interior uses `{typography.nav-category}` uppercase labels in burgundy as section headers, with regular `{typography.body-sm}` links beneath. Max four columns on desktop; collapses to accordion on mobile.

### Product Cards

**`product-card`** — 1px soft hairline border, 2px radius, no drop shadow. The flat border reads as a physical sheet edge — appropriate given the catalog. The image area uses `contain` (not `cover`) so paper color swatches and sheet samples aren't cropped. Spec lines below the title carry weight, finish, and size in `{typography.body-sm}` muted text; this metadata is often more decision-relevant than the product name.

**`spec-chip`** and **`spec-chip-active`** — Small uppercase tags (11px, 0.6px tracking) used both as filterable attributes on category pages and as active-state selectors on product detail pages. Active fills with `{colors.primary}`; inactive uses the warm spec-tag-bg (`#f0ede4`) to stay visible without competing with the product image. Up to six chips may appear in a row before wrapping.

### Filters & Search

**`filter-sidebar`** — 240px fixed-width sidebar on desktop. Filter groups (Paper Type, Weight, Finish, Size, Color, Brand) each open with a labeled divider using `{typography.title-sm}`. Checkboxes use brand burgundy for the checked state. The sidebar background matches the page canvas so it reads as inset rather than overlaid.

**`search-bar`** — 40px input with a left-aligned magnifier icon in `{colors.muted}`. Focus ring upgrades the border to 1.5px burgundy. On mobile this expands full-width and the filter toggle button sits to its right.

### Hero & Promotions

**`hero-banner`** — Deep navy background (`{colors.accent-navy}`) keeps paper product photography readable at any color temperature. An optional gold eyebrow label (`{colors.accent-gold}`) in `{typography.spec-label}` signals sale events or seasonal promotions. The headline uses the serif `display-xl` — the only place the site uses a serif, anchoring the brand in print-trade heritage. CTA buttons on the hero are white-outlined secondary style against the navy, avoiding a red-on-navy contrast problem.

### Spec & Detail Components

**`quantity-selector`** — Inline stepper with minus/plus buttons flanking a centered count; 40px tall, hairline border, `{rounded.sm}`. The count uses `{typography.title-md}` at 600 weight so the number reads clearly when customers are configuring large bulk orders.

**`swatch-selector`** — 28px circular swatches for paper color selection, with a 2px burgundy ring on the selected state. Tooltip on hover shows the paper color name (e.g., "Natural White", "Ivory", "Bright White") since the swatch itself cannot fully represent finish variation.

**`sale-badge`** and **`new-badge`** — Rectangular chips, 2px radius, overlaid on the top-left of product card images. Sale uses `{colors.primary}` burgundy; New uses `{colors.accent-navy}`. Both use `{typography.spec-label}` uppercase — consistent with the spec chip system so badges feel native to the information hierarchy.

### Footer

**`footer`** — Full-width navy (`#1e3456`) with five link columns (Paper Types, Occasions, Brands, Customer Service, About) and a certification strip (FSC, SFI, recycled content logos). The dark footer anchors the warm-canvas body and signals supply-chain credibility. `{footer-heading}` in gold-adjacent uppercase creates column hierarchy; body links in muted blue-white stay legible without high contrast noise.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar collapses to a bottom-sheet drawer triggered by a sticky "Filter & Sort" bar; nav collapses to hamburger with accordion mega-menu; hero headline drops to `display-md` (26px serif); add-to-cart button full-width sticky at bottom of PDP |
| Tablet | 744–1128px | Two-column product grid; filter sidebar hidden by default, revealed by toggle button above grid; nav shows top-level categories only (mega-dropdown on tap); hero splits image/text 50/50 |
| Desktop | 1128–1440px | Three-column product grid; 240px filter sidebar always visible; full mega-dropdown nav; hero full-bleed with max-width text column constrained to 520px |
| Wide | > 1440px | Four-column product grid; content max-width 1440px centered; hero padding expands to `{spacing.section}` both axes; footer columns spread to six |

### Touch Targets

- All buttons minimum 44px tall; icon-only buttons (search, cart, hamburger) minimum 44×44px
- Spec chips minimum 32px tall on touch to allow rapid filter toggling
- Quantity stepper plus/minus buttons minimum 40×40px tap area
- Filter checkboxes padded to 40px row height for thumb accessibility
- Swatch selectors minimum 36px tap area with invisible padding around the 28px visual target

### Collapsing Strategy

- Filter sidebar → bottom-sheet drawer (full-width, 80vh max) with scrim overlay; filter count badge on the trigger button
- Mega-dropdown nav → hamburger + full-height side drawer with accordion; category section headers remain uppercase and burgundy
- Spec chip rows → horizontally scrollable single row on mobile, no wrapping; "+" overflow chip shows count of hidden options
- Breadcrumb bar → collapses to show only parent category and current page (ellipsis middle items)
- Footer five-column grid → two-column at tablet, single-column accordion at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site returned no color tokens from the live extraction pass (likely JS-rendered CSS custom properties). All palette values above are inferred from paper-trade industry conventions and general brand aesthetics; they should be verified against the live site before production use.
- **No font families extracted** — typography stack (Georgia serif for display, Helvetica Neue for UI) is inferred; the actual brand may use a licensed web font (e.g., a Garamond variant or a geometric sans). Inspect `@font-face` declarations on the live site.
- **No theme-color meta tag** — cannot confirm primary brand color from standard browser signals.
- **Actual button radius unknown** — using `{rounded.sm}` (4px) as a conservative default appropriate for a supply/trade context; could range from sharp (0px) to slightly rounder (8px).
- **Logo treatment unknown** — whether the wordmark is serif, sans-serif, or includes a paper-themed mark (watermark, ream icon) cannot be confirmed without visual inspection.
- **Promotion cadence and banner structure** — not confirmed; hero banner design above is a plausible inference for an e-commerce paper retailer.
- **Price display format** — bulk pricing (per-sheet vs. per-ream vs. per-pack) is a significant UX concern for this category; specific price-line layout cannot be confirmed from extraction alone.
