---
version: alpha
name: "Pilgrim Surf + Supply"
source_url: "https://pilgrimsurfsupply.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Three extracted hex values — #010101, #121212, and #dedede — constitute the entire visible palette, and that compression is intentional: Pilgrim Surf + Supply operates on near-total contrast, an editorial gambit that hands all visual weight to the goods themselves. The canvas is white (#ffffff, confirmed by meta theme-color), type runs close-to-black, dividers sit at a single soft gray, and nothing else is added — no accent hue, no brand voltage, no signature color. The refusal of ornament is the identity. Founded in Brooklyn and rooted in the overlapping cultures of surf, skate, and outdoor craft, the shop curates objects that speak through material quality rather than marketing palette. Primary CTAs almost certainly execute as a simple inversion: #010101 fill with #ffffff text, resting flush on {rounded.none} — hard-edged, confident, consistent with a shop that treats decorative radius as noise. Typography could not be extracted from this build (likely JS-loaded tokens or bot-protection), but the brand's documented editorial sensibility points toward a clean grotesque set at restrained tracking, quiet enough to let product names lead without competition from letterform personality. Small-scale labels — buttons, category chips, nav links — likely carry slight open tracking in the {typography.button-md} and {typography.category-tag} ranges, giving uppercase text clarity without added weight. Spacing is generous throughout; whitespace is the primary selling tool. Product cards surface without decorative chrome: full-bleed portrait image, name in {typography.title-md}, price in {typography.price}, nothing else cluttering the object's presence. Navigation is deliberately spare — a wordmark, a shallow set of category links, a cart count — with no mega-menu expansion and no promotional bar competing with the header zone. The footer grounds the page against {colors.dark-ground}, reversing to {colors.on-dark} for link columns, closing the page exactly as it opened: high contrast, minimal structure, nothing extra.

colors:
  primary: "#010101"
  primary-active: "#333333"
  primary-disabled: "#999999"
  ink: "#121212"
  body: "#2c2c2c"
  muted: "#6b6b6b"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  dark-ground: "#010101"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 42px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -0.02em
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.01em
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
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
    letterSpacing: 0.05em
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-label:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.02em
  category-tag:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
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
    height: 44px
    border: none
  button-primary-active:
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
    padding: 13px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: none
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    paddingX: "{spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    gap: "{spacing.sm}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    titleColor: "{colors.ink}"
    priceColor: "{colors.muted}"
    border: none
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 85vh
    layout: full-bleed-image-with-text-overlay
    overlayColor: "rgba(1,1,1,0.25)"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    paddingY: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  category-tag-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.category-tag}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 6px 12px
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    selectedBorder: "1px solid {colors.primary}"
  badge-sold-out:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    inputBorder: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    backdropColor: "rgba(0,0,0,0.5)"
    inputHeight: 48px
  footer:
    backgroundColor: "{colors.dark-ground}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    linkColor: "{colors.on-dark}"
    paddingY: "{spacing.xxl}"
    columnGap: "{spacing.xl}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-lg}"
    itemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    paddingX: "{spacing.xl}"
    checkoutButton: button-primary

## Components

### Buttons

**`button-primary`** — A full #010101 block with uppercase white text at 0.1em letter-spacing, sitting on zero border-radius. The flat edge is the statement: no rounding softens the purchase action, matching the shop's hard-edge editorial confidence throughout. Hover transitions to `{colors.primary-active}` (#333333); disabled washes to `{colors.primary-disabled}` (#999999) with white text retained. Width is contextual — full-width on mobile product pages, auto-width in desktop cart drawers and checkout flows.

**`button-secondary`** — White fill outlined by a 1px `{colors.ink}` border, dimensionally identical to `button-primary`. Acts as a peer action — "Add to Wishlist" or "View Size Guide" alongside the primary CTA — without competing through color contrast. The `button-ghost` variant strips the border entirely for inline text-level actions such as "Continue Shopping" or navigation breadcrumbs.

### Text Input

**`text-input`** — Clean rectangle with 1px `{colors.hairline}` perimeter border and zero radius; on focus, the border sharpens to 1px `{colors.ink}` providing a clear state change without color animation or glow. Placeholder text renders in `{colors.muted}`. Used in search fields, email capture, and checkout forms; the visual language is consistent across all contexts — no field variation by type.

### Navigation

**`nav-bar`** — White ground at 56px, separated from page content by a single 1px `{colors.hairline}` bottom border and no shadow. Wordmark or compact logotype anchors the left; category links in `{typography.nav-label}` run center or right; search and cart icons close the far right. No sticky behavior or blur treatment is indicated — the bar scrolls away on mobile, consistent with a shop that trusts the content over persistent chrome.

**`announcement-bar`** — A 36px strip in `{colors.ink}` pinned above the nav, centered `{typography.caption}` text in `{colors.on-primary}`. The only place editorial content asserts precedence before the browse experience begins; used for shipping thresholds, seasonal messages, or new-arrival callouts.

### Product Card

**`product-card`** — Image dominates at 3:4 portrait ratio, edge-to-edge within the column with no frame, rounding, or hover zoom overlay. Below the image: product name in `{typography.title-md}` at `{colors.ink}`, price in `{typography.price}` at `{colors.muted}`, nothing else. No quick-add button appearing on hover, no rating stars, no badge stack — the object is presented, not promoted.

### Hero

**`hero`** — Full-bleed photography at 85vh minimum with a 25% black scrim softening contrast between image and type. Display copy in `{typography.display-xl}` runs `{colors.on-primary}` against the image; any sub-headline or CTA button sits directly below with minimal spacing. The layout trusts the photograph; type is sparse and positioned to frame rather than compete with the subject.

### Collection Header

**`collection-header`** — A white canvas text zone: collection title in `{typography.display-md}` and an optional one-sentence descriptor in `{typography.body-md}`, separated from the product grid below by a 1px `{colors.hairline}` rule. Padding runs `{spacing.xl}` top and bottom. No hero image, no banner — the name and the grid are the full collection experience.

### Filters and Tags

**`category-tag-chip`** — Zero-radius rectangular chip with a 1px `{colors.hairline}` border and uppercase `{typography.category-tag}` text in `{colors.ink}`. Selected state inverts to `{colors.primary}` fill with `{colors.on-primary}` text, maintaining the monochromatic flip pattern used throughout the button system. Used for category filtering, size selectors, and color swatches where a text label is appropriate.

**`badge-sold-out`** — Subdued `{colors.surface-soft}` ground with `{colors.muted}` text in `{typography.caption}`, placed inline below the price or as a small corner overlay on the product image. Zero radius, no color alarm — sold-out is treated as a neutral fact rather than an urgent warning.

### Search

**`search-overlay`** — A full-width `{colors.canvas}` panel descending from the nav bar on icon trigger, carrying a single `{typography.body-md}` input field bordered by 1px `{colors.ink}` with a 50% dark backdrop behind the panel. The experience is intentionally minimal — a text field and a submit trigger — with no autocomplete bubbles or decorated result rows indicated. Zero radius throughout.

### Footer

**`footer`** — `{colors.dark-ground}` (#010101) ground with `{colors.on-dark}` link columns in `{typography.caption}`, spaced at `{spacing.xl}` column gap and `{spacing.xxl}` vertical padding. Column groups (Shop, About, Help, Social) present as short functional lists; the wordmark appears above the column block. The footer executes the same high-contrast inversion as the primary button, bookending the white canvas experience with an assertive black close.

### Cart Drawer

**`cart-drawer`** — A 400px panel sliding in from the right edge, `{colors.canvas}` ground bordered by a single 1px `{colors.hairline}` left rule. "Your Cart" title renders in `{typography.title-lg}`; line items in `{typography.body-sm}` with individual prices in `{typography.price}`. The checkout button at the drawer base inherits `button-primary` styles — black, full-width, zero radius — ensuring the highest-stakes CTA in the flow carries the same weight as every other primary action on the site.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger icon + wordmark + cart; hero text scales down to `display-md`; cart drawer expands to full viewport width; announcement bar text wraps or truncates |
| Tablet | 744–1128px | Two-column product grid; nav may retain visible category links or remain hamburger-collapsed depending on link count; hero maintains full-bleed at reduced text size |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav bar with all category links visible; cart drawer fixed at 400px; collection header adds horizontal padding |
| Wide | > 1440px | All content constrained to a max-width container (~1280–1320px) centered on canvas; side gutters widen proportionally; grid column count stays at four; no additional layout changes |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch target on mobile
- `button-primary` and `button-secondary` render full-width at mobile, always meeting the height requirement
- Nav bar icons (search, cart, hamburger) are padded to 44×44px regardless of visible icon size
- `category-tag-chip` elements on mobile maintain at least 36px height with horizontal padding ensuring comfortable thumb reach
- Cart line-item remove buttons are padded to 44×44px even when the visual element is smaller

### Collapsing Strategy

- Navigation: hamburger overlay at mobile, revealing a full-screen or slide-in panel with category links stacked vertically in `{typography.title-md}`
- Product grid: 1 column (mobile) → 2 columns (tablet) → 3–4 columns (desktop)
- Hero: text block shifts from right- or center-overlay to a stacked bottom-anchored layout on mobile, with the CTA button going full-width
- Footer: link columns stack vertically at mobile, collapsing into a disclosure accordion if column count exceeds three
- Announcement bar: text truncates with ellipsis or runs a slow marquee if content exceeds a single line at narrow widths
- Filters: horizontal scrolling chip row on mobile rather than a collapsible sidebar; sidebar appears at desktop widths only

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Font families not extracted** — zero font stacks were detected on the live site; all typography tokens use a Helvetica Neue fallback stack inferred from the brand's editorial aesthetic. Actual brand fonts (potentially Founders Grotesk, Acumin, or a licensed grotesque) must be confirmed and substituted before production use.
- **Sparse color palette** — only three hex values (#010101, #dedede, #121212) were extractable; the site appears fully monochromatic with no secondary or accent colors confirmed. Seasonal accent colors, sale-price color, and error-state color remain unknown.
- **Sale and promotional color** — no price-reduction or urgency color was visible in extraction; sale pricing, low-stock indicators, and cart badge background are assumed to follow the monochromatic system but may deviate in practice.
- **Exact button and input radius** — confirmed as zero or near-zero based on brand aesthetic and extraction data; not validated against live computed styles.
- **Navigation depth and structure** — mega-menu presence, exact top-level category count, and mobile nav animation pattern are inferred from brand-class conventions rather than live DOM inspection.
- **Spacing system base unit** — 8px assumed; actual grid gutter, section padding, and card gap values were not captured from computed styles.
- **Typography scale values** — font-size, weight, and line-height tokens are estimated from typical editorial-minimal conventions for this brand tier; exact values require font-inspector validation against the live site.
