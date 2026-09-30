---
version: alpha
name: "Nordfrim"
source_url: "https://www.nordfrim.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The lime-to-forest green arc — #b0eb77 brightening into #63af1a at primary weight and deepening to #528f02 on hover — echoes the saturated ink fields of vintage perforated stock, the kind of artificial green that Nordic postal agencies printed on ordinary-rate stamps for decades. Nordfrim wears this palette deliberately: a philatelic retailer whose chromatic identity borrows from the catalog paper it sells rather than from generic e-commerce green-equals-go conventions. Garamond and its italic variant (GaramondPremierProItalic) anchor display headings, a choice that signals the antiquarian register of stamp dealing — condition grades, perforation gauges, and catalog numbers belong to a typographic tradition that sans-serif retail type would undermine. Myriad Pro and Arial handle the functional layer: prices, form labels, navigation items, facet text. The canvas is a pale near-white (#f3f3f3) lightened to pure white in card surfaces, with hairlines drawn from the mid-gray range (#dbdbdb, #cacaca) that feel like the ruled lines of a stock ledger. A secondary blue family (#217dbd, #258bd3, #007ac3) operates in informational contexts — links, selected states, promotional banners — referencing the airmail blue that philatelists associate with international postage. Red (#d71921) appears only for urgency signals: sale badges, out-of-stock warnings, price-reduction indicators, never as a primary brand action. Orange (#f58d3d) surfaces rarely as a tertiary accent on special-lot callouts. Corner radii are conservative throughout — {rounded.xs} on badges and inputs, {rounded.sm} on modal panels — reflecting the rectilinear world of stamp albums and stock books. Whitespace is generous within category grids but the overall layout runs dense at desktop widths, accommodating long facet lists (country, era, topic, condition, catalog number range) that serious collectors use to drill into inventory. The site reads as a working reference tool as much as a storefront, and the visual system supports that double register: Garamond display type for editorial gravitas, a tightly spaced sans-serif grid for data density, and the unmistakable green of a Scandinavian postal service as the single brand voltage that unifies every primary action.

colors:
  primary: "#63af1a"
  primary-active: "#528f02"
  primary-disabled: "#b5ec80"
  primary-light: "#b0eb77"
  ink: "#353535"
  body: "#5e5e5e"
  muted: "#797979"
  muted-soft: "#888888"
  hairline: "#dbdbdb"
  hairline-soft: "#e2e2e2"
  border-mid: "#cacaca"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  surface-mid: "#e2e2e2"
  on-primary: "#ffffff"
  accent-blue: "#217dbd"
  accent-blue-hover: "#005f9d"
  accent-blue-light: "#8cc4eb"
  accent-blue-sky: "#258bd3"
  accent-teal: "#008677"
  accent-red: "#d71921"
  accent-red-deep: "#b00000"
  accent-orange: "#f58d3d"
  dark-tone: "#312727"

typography:
  display-xl:
    fontFamily: "'Garamond', 'Georgia', 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  display-md:
    fontFamily: "'Garamond', 'Georgia', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  display-italic:
    fontFamily: "'GaramondPremierProItalic', 'Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.36
    letterSpacing: 0
  title-md:
    fontFamily: "'Myriad Pro', 'Arial', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  title-sm:
    fontFamily: "'Myriad Pro', 'Arial', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  body-md:
    fontFamily: "'Arial', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  body-sm:
    fontFamily: "'Arial', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.46
    letterSpacing: 0
  caption:
    fontFamily: "'Arial', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  button-md:
    fontFamily: "'Myriad Pro', 'Arial', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  button-sm:
    fontFamily: "'Myriad Pro', 'Arial', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Arial', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Myriad Pro', 'Arial', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  breadcrumb:
    fontFamily: "'Arial', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  price-lg:
    fontFamily: "'Myriad Pro', 'Arial', Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: 0
  price-sm:
    fontFamily: "'Arial', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0
  catalog-ref:
    fontFamily: "'Verdana', 'Arial', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.36
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
    padding: 10px 20px
    height: 40px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border-mid}"
    padding: 9px 19px
    height: 40px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.accent-blue}"
    rounded: "{rounded.xs}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.accent-blue}"
    typography: "{typography.body-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border-mid}"
    borderFocus: "1px solid {colors.accent-blue}"
    padding: 8px 12px
    height: 36px
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border-mid}"
    padding: 6px 10px
    height: 32px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    linkTypography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 56px
  nav-bar-top-stripe:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 28px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.border-mid}"
    height: 36px
  search-button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 36px
    width: 80px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    imageAspect: "1/1"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-sm}"
    padding: "{spacing.sm}"
  product-card-hover:
    border: "1px solid {colors.accent-blue-light}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.10)"
  stamp-condition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "2px 6px"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  catalog-ref-tag:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.catalog-ref}"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price-lg}"
  price-sale:
    textColor: "{colors.accent-red}"
    typography: "{typography.price-lg}"
  price-original-strikethrough:
    textColor: "{colors.muted}"
    typography: "{typography.price-sm}"
    textDecoration: line-through
  facet-sidebar:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    width: 220px
  facet-section-heading:
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "8px 0"
  facet-checkbox-label:
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
  facet-checkbox-active:
    accentColor: "{colors.primary}"
  breadcrumb-nav:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.muted-soft}"
    typography: "{typography.breadcrumb}"
    padding: "{spacing.sm} 0"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-md}"
    captionTypography: "{typography.caption}"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 280px
    padding: "{spacing.xxl} {spacing.xl}"
  info-stripe:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-mid}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xl} 0"
  pagination:
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.accent-blue}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
  cart-summary:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    totalTypography: "{typography.price-lg}"
    labelTypography: "{typography.body-md}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.border-mid}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    buttonWidth: 28px
    height: 32px

## Components

### Buttons
**`button-primary`** — The add-to-cart and checkout action is a forest green (#63af1a) rectangle with {rounded.xs} corners, 40px tall and padded 10px/20px, set in {typography.button-md} (Myriad Pro 14px, weight 600). The pressed state deepens to #528f02; the disabled state washes to {colors.primary-disabled} with {colors.muted} text. Green-on-white contrast clears WCAG AA at all body text sizes. Primary buttons appear on add-to-cart, basket confirmation, and search submission — never on destructive or navigational actions.

**`button-secondary`** — A white button with a 1px {colors.border-mid} border, matching height and typography to primary. On hover or focus the border shifts to {colors.accent-blue}, echoing the link color convention. Used for save-to-wishlist, back-to-results, and modal cancel. The two buttons typically sit side-by-side in a right-aligned row on desktop, stacking full-width on mobile.

**`button-link`** — Inline text in {colors.accent-blue} with underline decoration, following classical hyperlink convention. In a catalog-oriented layout where listing pages carry dense paragraph text, unambiguous link styling matters more than decorative restraint.

### Navigation
**`nav-bar`** — A white 56px bar with a bottom hairline. Above it the `nav-bar-top-stripe` — a 28px green band in {colors.primary} — carries service messaging (free-shipping threshold, newsletter prompts). Logo sits left; search bar occupies the center-right zone; cart and account icons anchor the far right. Links use {typography.nav-link} (Myriad Pro 14px, weight 600). Sub-categories are expected to appear in a simple dropdown on hover.

**`search-bar`** — A rectangle input field with a flush-attached green submit button (`search-button`, {colors.primary}, {rounded.none}) forming a single visual unit. The field carries {typography.body-md} and {colors.muted} placeholder text, height 36px. The attached-button pattern is common in mail-order and auction catalog UIs and reads as transactional rather than conversational.

### Product Cards
**`product-card`** — A lightly bordered ({colors.hairline}, 1px) white card with {rounded.xs} corners. The stamp image occupies a square 1:1 aspect ratio at top; below it appear the item title in {typography.body-md}, a catalog reference tag in {typography.catalog-ref}, and the price in {typography.price-sm}. On hover, the border brightens to {colors.accent-blue-light} and a 2px shadow lifts the card. Condition and sale badges layer over the image's top-left corner. Cards are fully linked as a single tap target on mobile.

**`stamp-condition-badge`** — A no-radius label in {typography.badge} (uppercase, 11px, weight 700) filled with {colors.surface-soft} and outlined by {colors.hairline}. Values like VF, XF, F-VF, and NH are standard philatelic shorthand and appear on virtually every listing. The neutral palette keeps condition badges visually subordinate to the sale badge's red urgency signal.

**`sale-badge`** — Solid {colors.accent-red} with white text, {rounded.none}, applied as an image overlay when a discount is active. Red is reserved for this badge and out-of-stock labels exclusively — it never appears on green or blue primary surfaces, preserving signal isolation.

### Facet Sidebar
**`facet-sidebar`** — A 220px fixed-width left column on desktop in {colors.surface-soft} with a {colors.hairline} border and square corners. Section headings use {typography.title-sm} with a bottom rule; checkbox labels use {typography.body-sm} in {colors.body}. Checkboxes use {colors.primary} as their accent color so ticked states reinforce the green identity. Typical facets for a stamp shop: Country, Year/Period, Topic/Theme, Condition, Catalog Number Range, Stamp Type (definitive, commemorative, airmail), Watermark, Perforation. On tablet the sidebar collapses to an accordion above the grid; on mobile it opens as a modal drawer from a filter button.

### Badges and Reference Tags
**`catalog-ref-tag`** — A transparent micro-label in {typography.catalog-ref} (Verdana, 11px) displaying catalog cross-references (Scott, Michel, Yvert numbers). Verdana's large x-height at small sizes aids legibility for the dense alphanumeric codes that serious collectors scan first.

**`new-badge`** — Solid {colors.primary} green with white text in {typography.badge}, used for recently listed lots or newly added sets. Placed in the same image-overlay zone as `sale-badge` but never simultaneously — condition badge at top-left, sale or new badge at top-right.

### Hero and Banners
**`hero-banner`** — A full-width green (#63af1a) panel with heading in {typography.display-xl} (Garamond 32px, weight 700) and supporting copy in {typography.body-md}. The serif display type on a saturated green ground establishes an editorial, catalog-house register distinct from typical lifestyle e-commerce imagery. Minimum height 280px; padding {spacing.xxl}/{spacing.xl}. Secondary landing pages may substitute {colors.surface-soft} background with {colors.ink} text for lower visual weight.

**`info-stripe`** — A narrow {colors.accent-blue} band in {typography.body-sm} with white text for system-level notices: shipping promotions, event announcements, or service interruptions. Sits between the top-stripe and the main nav, or pinned to the top of the viewport on scroll.

### Pricing
**`price-display`** — Standard price uses {typography.price-lg} (Myriad Pro 18px, weight 700) in {colors.ink}. When an item is on sale, the current price shifts to {colors.accent-red} and the original renders in {typography.price-sm} with strikethrough in {colors.muted}. These three tokens always appear together in a single price cell; never reorder them.

### Footer
**`footer`** — Dark near-black ({colors.ink}, #353535) ground with {colors.surface-mid} body text, a 3px {colors.primary} top border, and {typography.title-sm} column headings. Links use {typography.body-sm}. The green top border grounds the footer in brand identity without requiring green coverage across the entire dark field. Column topics typically include Help, Payment Methods, Shipping, About Nordfrim, and country/language selectors for Nordic markets.

### Cart and Quantity
**`cart-summary`** — A {colors.surface-soft} sidebar panel or bottom checkout strip with a 1px hairline border and {rounded.xs} corners. Line items, subtotal label, and VAT note use {typography.body-md}; the running total uses {typography.price-lg}. A full-width green `button-primary` anchors the bottom of the panel.

**`quantity-stepper`** — A three-cell minus/count/plus row at 32px height with square corners ({rounded.none}) and {colors.border-mid} outline. The rectilinear, no-radius treatment matches the grid-like visual language of stamp album pages and catalog grids.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Facet sidebar collapses into a modal drawer triggered by a filter button; product grid shifts to 2 columns; nav-bar condenses to logo + hamburger + cart icon; hero-banner min-height reduces to 180px; search bar moves below logo row; top stripe hidden, its message shifts to a sticky footer bar |
| Tablet | 744–1128px | Facet sidebar renders as a collapsible accordion above the grid rather than a fixed left column; 3-column product grid; top nav shows two category levels, sub-categories appear in dropdown on tap |
| Desktop | 1128–1440px | Full 4-column grid with 220px facet sidebar fixed left; complete top-nav with all category labels; hero-banner at full 280px+ height; search bar in header |
| Wide | > 1440px | Content container max-width ~1400px centered with widened gutters; hero typography remains at display-xl scale; sidebar and grid proportions held fixed; background bleeds to viewport edges in hero and footer only |

### Touch Targets
- All buttons and form controls maintain a minimum 44×44px touch target on mobile
- Facet checkboxes expand their hit area to the full row width via padding compensation
- Product cards are fully tappable as a single link surface on mobile — no sub-targets within the card
- Quantity stepper buttons widen to 44px on mobile, increasing from the 28px desktop default
- Badge overlays on product images do not intercept tap events; the card link takes precedence

### Collapsing Strategy
- Facets collapse first (mobile modal drawer), then sub-navigation merges into the hamburger menu
- Top service stripe hides on mobile to recover vertical space; equivalent messaging appears in a sticky bottom bar
- Two-button rows (primary + secondary side-by-side) stack vertically on mobile with full viewport width
- Catalog reference tags truncate to one line with ellipsis on narrow viewports; full value exposed on tap via tooltip or expand
- Category tile grids shift from 4-wide desktop to 2-wide mobile; tile labels always remain visible (no icon-only collapse)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand typeface confirmed; Garamond, GaramondPremierProItalic, Myriad Pro, and Arial are system/standard fonts identified from CSS stacks — webfont hosting or licensing details not confirmed
- Exact top-nav structure (mega-menu vs. simple multi-level dropdown, total number of top-level category links) could not be extracted
- Hover and active state colors for nav links not captured; {colors.accent-blue} applied as a reasonable inference from the site's link color convention
- Modal and overlay scrim opacity and color not extracted
- Cookie consent banner presence and styling unknown
- Orange accent ({colors.accent-orange}, #f58d3d) and teal ({colors.accent-teal}, #008677) usage contexts not confirmed from extraction; flagged as available tokens but specific component assignment uncertain
- Exact product grid gutter widths and column pixel dimensions at each breakpoint not measured
- Dark-mode support status unknown; extraction showed no dark-mode media query tokens
- Pagination exact active-state border color and spacing not measured directly from live site
- Whether the site uses a sticky header on scroll, and what visual changes accompany it, not confirmed
