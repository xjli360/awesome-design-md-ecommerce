---
version: alpha
name: "Linjer"
source_url: "https://www.linjer.co"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The product image carries the entire persuasion load on a Linjer page — a solid-gold ring photographed flat against near-white, no props, no model hand, no soft-focus lifestyle blur. Everything else in the UI steps deliberately back: body copy at 15px in the system sans stack, a near-black #313131 deployed simultaneously as link text, input borders, and the fill of the single primary CTA, and a warm-cream ground (#f9f7f4) that signals luxury through restraint rather than ornamentation. There is no brand voltage color competing for the eye; the metals on sale are the palette. Navigation holds a wordmark-first layout with links at weight 400 rather than 600 — no fills, no pills on hover, just an underline — and the top bar sits short enough to feel editorial rather than retail-storefront. Product cards are containerless: no box-shadow, no border stroke, just image-above-text in a tight grid where negative space does the separating. Material selectors — Yellow Gold, White Gold, Sterling Silver — use text chips with {rounded.full} geometry, the only soft curve that appears regularly in the brand's chrome; every button and input field uses {rounded.none}, keeping softness in the product rather than the interface chrome. Spacing is the primary luxury signal — sections breathe at 80px vertical, product detail pages give each specification its own line rather than cramming metadata into a dense paragraph, and the checkout flow strips sidebars entirely on mobile for an unhurried single-column experience. Badge overlays on product images are absent; urgency mechanics like countdown timers and low-stock banners do not appear. Button labels run in small uppercase with 0.08em tracking — deliberate and calm. A dark footer in the same #313131 that anchors body text closes each page with the same ink that opened it, a quiet full-circle close.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#aaaaaa"
  ink: "#313131"
  body: "#555555"
  muted: "#888888"
  hairline: "#e5e1da"
  hairline-soft: "#eeebe5"
  canvas: "#ffffff"
  surface-soft: "#f9f7f4"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  gold-warm: "#c4a46a"
  silver-neutral: "#b8b6b2"
  error: "#b84040"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.03em
  label-uppercase:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 28px
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
  section: 80px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
    width: 100%
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
    textDecorationHover: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
  nav-link-active:
    textColor: "{colors.ink}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 14px
    height: 48px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "4/5"
    rounded: "{rounded.none}"
    textColor: "{colors.ink}"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
    gap: "{spacing.sm}"
    padding: 0
  collection-grid:
    columns: 3
    gap: "{spacing.xl}"
    backgroundColor: "{colors.canvas}"
    padding: "0 {spacing.xl}"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.label-uppercase}"
    eyebrowColor: "{colors.muted}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    textAlign: left
    imagePosition: right
  material-selector:
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    inactiveBorder: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  size-selector:
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.ink}"
    inactiveBorder: "1px solid {colors.hairline}"
    unavailableTextColor: "{colors.primary-disabled}"
    unavailableDecoration: line-through
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    size: 40px
  sticky-add-to-cart:
    backgroundColor: "{colors.canvas}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.xl}"
    buttonComponent: button-primary
    displayBelowScroll: 300px
  product-details-accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    labelTypography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"
    iconStyle: plus-minus
  category-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    eyebrowTypography: "{typography.label-uppercase}"
    eyebrowColor: "{colors.muted}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.xl}"
  newsletter-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    inputComponent: text-input
    buttonComponent: button-primary
    paddingVertical: "{spacing.xxl}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
    padding: "{spacing.base} 0"
  tag-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    padding: "5px 12px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "#aaaaaa"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.label-uppercase}"
    bodyTypography: "{typography.body-sm}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    columns: 4
  progress-bar:
    activeColor: "{colors.ink}"
    inactiveColor: "{colors.hairline}"
    height: 2px
    rounded: "{rounded.none}"

---

## Components

### Buttons

**`button-primary`** — Full-width solid black ({colors.primary}) block, 48px tall, sharp corners ({rounded.none}), uppercase tracking label at 13px with 0.08em letterSpacing. Width expands to fill its container on product pages and checkout; stands at natural width inside narrower layout slots. Active state darkens to {colors.primary-active}; disabled washes to {colors.primary-disabled} with `not-allowed` cursor. There is no border-radius softening — this button is intentionally architectural.

**`button-secondary`** — White fill with a 1px {colors.ink} border; same height, typography, and corner treatment as `button-primary`. Used for secondary actions like "Save to Wishlist" or "Find My Ring Size." On hover the border does not shift weight — only a subtle background tint ({colors.surface-soft}) may appear.

**`button-text-link`** — Transparent background, underlined body-sm text in {colors.ink}. Used for inline navigational nudges ("View size guide", "Learn about our metals") where a full button would over-emphasize. Underline removes on hover rather than being added, reversing the usual convention for a quieter feel.

### Navigation

**`nav-bar`** — 60px white bar with a bottom hairline ({colors.hairline}), 13px nav links in weight 400 with 0.04em tracking. Wordmark sits left; primary navigation categories center or right; bag + account icons far right. No mega-dropdown fill color — flyout menus open on a plain white card with no heavy shadow. The brevity of the bar (no promotional banner by default) keeps the editorial quality intact.

**`breadcrumb`** — Muted caption text separated by "/" with no decorative chevrons. Active segment renders in {colors.ink} at the same 12px size; parent segments in {colors.muted}. Sits above the product title with {spacing.base} vertical padding.

### Forms & Inputs

**`text-input`** — Flat, 48px, no-radius field with a 1px {colors.hairline} border that sharpens to {colors.ink} on focus. No floating label animation — static label sits above the field in {typography.label-uppercase}. Error state swaps border to {colors.error} with a small inline message in {typography.caption}. Used across search, checkout, and newsletter fields with consistent geometry.

### Product Cards

**`product-card`** — No container chrome: image fills a 4:5 ratio frame borderless on a white grid, followed by product name in {typography.body-sm}, material line in {typography.caption} at {colors.muted}, then price in {typography.price} weight 400. Quick-shop or swatch selectors may appear on hover (desktop) as an absolute overlay at the image base, but are never shown as visible chrome in resting state. No badge overlays permitted over product imagery.

**`collection-grid`** — 3-column desktop grid with {spacing.xl} gaps and no visible separators between cards. The whitespace is the grid.

### Hero & Editorial

**`hero-editorial`** — Warm-cream ({colors.surface-soft}) section, title in {typography.display-xl} weight 400 (never bold), left-aligned text block alongside a right-positioned product image. An optional eyebrow label in {typography.label-uppercase} at {colors.muted} runs above the headline. Padding breathes at {spacing.section} vertical. The image carries weight; the text provides orientation only.

**`category-header`** — Softer version of the hero: {typography.display-md} weight 400 title, uppercase eyebrow, cream background, no full-bleed image. Used atop collection pages (Rings, Necklaces, Earrings) to orient without overwhelming.

### Product Detail Page

**`material-selector`** — Pill-shaped chips ({rounded.full}) for metal options (Yellow Gold, White Gold, Rose Gold, Sterling Silver). Active chip fills {colors.ink} with white text; inactive chips are white with a {colors.hairline} border that sharpens to {colors.ink} on hover. The pill geometry is the deliberate exception to the brand's otherwise sharp-corner rule — softness marks the physical material choice.

**`size-selector`** — 40×40px square tiles, {rounded.none}, same active/inactive fill logic as material-selector. Unavailable sizes render their label in {colors.primary-disabled} with strikethrough rather than hiding entirely, preserving size-range legibility.

**`product-details-accordion`** — Each PDP section (Details, Materials & Care, Shipping & Returns, Size Guide) lives in a borderless accordion separated by a single {colors.hairline} bottom rule. Label in {typography.title-sm}; body in {typography.body-sm} with generous 1.6 line-height for easy reading. Plus/minus icon right-aligned. No background fill change on open — the section simply expands in place.

**`sticky-add-to-cart`** — A white bar with a top hairline that appears fixed at the viewport bottom once the main add-to-cart button scrolls out of view (~300px). Holds product name (caption), selected variant chip(s), price, and the full-width `button-primary`. Disappears if the user scrolls back up to the primary button.

### Supporting Patterns

**`newsletter-strip`** — Cream ({colors.surface-soft}) band, left-aligned title in {typography.title-md}, optional one-line description in {typography.body-sm}, inline input + submit button side-by-side on desktop. Padding {spacing.xxl} top/bottom. No decorative borders or background illustration.

**`tag-chip`** — Cream pill used for filter tags in collection pages (Metal Type, Price Range, Stone). Typography {typography.label-uppercase} for consistent scanning at small size. Active filter state fills {colors.ink} matching the material-selector active pattern.

**`footer`** — Full-width {colors.ink} inversion: four-column layout on desktop with {typography.label-uppercase} column headers and {typography.body-sm} links at #aaaaaa lightening to white on hover. Social icons appear in the final column. Padding {spacing.section} vertical. No promotional content or secondary CTA in the footer — purely navigational.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column collection grid; nav collapses to hamburger + wordmark; hero becomes stacked (image above text); `material-selector` and `size-selector` wrap in a scrollable row; sticky add-to-cart active at all times; footer collapses to 2 columns then accordion. |
| Tablet | 744–1128px | 2-column collection grid; nav may keep top-level labels visible with hamburger for sub-nav; hero maintains side-by-side with equal column split; sticky add-to-cart maintained. |
| Desktop | 1128–1440px | 3-column collection grid; full horizontal nav; hero image takes ~55% width; accordion PDP sections; sticky add-to-cart triggers on scroll. |
| Wide | > 1440px | Max-width container (~1280–1360px) centered; collection grid holds at 3 columns with increased gap; hero section pads out horizontally rather than stretching image. |

### Touch Targets

- All buttons minimum 48px height, full-width on mobile
- `size-selector` tiles scale to 44×44px minimum on mobile
- `material-selector` chips receive 44px minimum tap height via vertical padding increase
- Accordion labels padded to 48px touch height on mobile
- Nav hamburger icon area minimum 44×44px

### Collapsing Strategy

- Collection grid: 3-col → 2-col → 1-col at tablet and mobile breakpoints
- Hero: side-by-side → stacked (image first, then text) on mobile
- Footer: 4-col → 2-col → 1-col accordion on mobile
- `product-details-accordion` remains accordion at all breakpoints (no expansion to always-visible on desktop)
- Nav: full labels → hamburger with full-screen drawer; drawer background is {colors.canvas} with standard link list
- `newsletter-strip`: horizontal input+button → stacked on mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Full color palette unextracted**: site returned an anti-bot challenge page ("Just a moment...") — only one hex value (#313131) was captured. Warm cream surface (#f9f7f4), gold accent (#c4a46a), and hairline tones are inferred from fine-jewelry brand conventions, not confirmed extraction.
- **Custom typeface unknown**: no custom font-family detected; extraction returned only OS/system font stacks. Linjer may load a proprietary or licensed typeface (possibly a geometric sans or editorial serif) via JS or a font host not captured. All typography tokens use the system stack as fallback — replace with confirmed family when available.
- **Exact button radius**: {rounded.none} is inferred from the minimal aesthetic; actual computed border-radius on CTAs was not confirmed.
- **Gold accent usage scope**: {colors.gold-warm} is a plausible brand accent for metal-callout labels or price badges, but its exact hex and usage pattern were not confirmed from live extraction.
- **Silver tone**: {colors.silver-neutral} approximated from standard fine-jewelry silver swatch conventions; not extracted.
- **Navigation mega-menu structure**: dropdown/flyout layout and content zones could not be inspected due to anti-bot block.
- **Animation and transition specs**: hover timing, accordion open/close easing, and image-swap transitions on PDP are unconfirmed.
- **Product image lazy-load skeleton**: background color for image placeholders not captured.
