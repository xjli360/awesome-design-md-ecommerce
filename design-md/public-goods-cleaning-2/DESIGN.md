---
version: alpha
name: "Public Goods"
source_url: "https://publicgoods.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A monochrome foundation of #080808 and #f5f5f5 defines Public Goods — a cleaning-supply brand that treats its own packaging as the primary visual asset, letting product labels in muted #7d7d7d and #c1c1c1 do the selling rather than hero photography or illustration. The palette is deliberately restrained: near-black ink (#1e1e1e) on a warm off-white canvas (#f5f5f5) with hairline borders in #ebebeb, creating a clinical-but-hygienic feel that mirrors the brand's "no-toxins" promise. A single accent — #4469af, a muted slate blue — appears sparingly on select CTAs and informational badges, never competing with the product's own label colors. Typography runs NeuzeitS-Book at modest weights (400–700), with BebasNeue reserved for display headlines that punch through the quiet grid at 36px. Buttons are softly rectangular at {rounded.sm} (8px), while product cards use {rounded.md} (12px) to echo the rounded-corner packaging the brand ships in. The overall effect is a store that feels more like a clean pantry than a website — every surface is wipeable, every edge intentional, every color decision subordinate to the product itself.

colors:
  primary: "#080808"
  primary-active: "#1e1e1e"
  primary-disabled: "#d9d9d9"
  ink: "#080808"
  body: "#1e1e1e"
  muted: "#595959"
  muted-soft: "#7d7d7d"
  hairline: "#ebebeb"
  hairline-soft: "#f4f4f4"
  canvas: "#f5f5f5"
  surface-soft: "#f7f7f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-blue: "#4469af"
  accent-red: "#c8232c"
  accent-gold: "#eca937"
  accent-terracotta: "#dc886d"
  border-light: "#c1c1c1"
  border-strong: "#8c8c8c"

typography:
  display-xl:
    fontFamily: "'BebasNeue', 'NeuzeitS-Book', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 1px
  display-lg:
    fontFamily: "'BebasNeue', 'NeuzeitS-Book', sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'NeuzeitS-Book', 'Nunito Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-accent:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  text-input-focus:
    borderColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.md}"
  product-card-badge:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    borderColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: 64px 24px
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    borderColor: "{colors.hairline}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in near-black (#080808) with white text and uppercase NeuzeitS-Book at 14px/700. On hover, the background deepens to #1e1e1e. Disabled state uses #d9d9d9 with muted text, signaling the action is unavailable without error color. All primary buttons use 8px corner radius (`{rounded.sm}`) and 44px height for comfortable tap targets.

**`button-secondary`** — An outlined variant on the off-white canvas (#f5f5f5) with near-black text. Used for "Add to Cart" alternatives, "Learn More" links, and secondary purchase flows. Shares the same dimensions and typography as primary but inverts the color relationship.

**`button-accent`** — Reserved for informational actions like "Subscribe & Save" or "Shop Bundles." Uses the muted slate blue (#4469af) as background, maintaining the brand's restrained palette while providing visual distinction from the primary black buttons.

### Cards
**`product-card`** — The core product display unit, a white card on the off-white canvas with 12px rounded corners (`{rounded.md}`). Product images sit within the card with matching corner radius. Text uses body-sm (14px) for descriptions and title-sm (18px) for product names. Cards include a subtle shadow or border via the hairline (#ebebeb) to lift them from the background.

**`product-card-badge`** — Small informational tags (e.g., "NEW", "BESTSELLER", "PLANT-BASED") in slate blue (#4469af) with white uppercase text. Uses 4px corner radius (`{rounded.xs}`) and tight padding to sit unobtrusively on product images or card corners.

### Navigation
**`nav-bar`** — A fixed top navigation at 64px height on the off-white canvas. Links use uppercase NeuzeitS-Book at 14px/600 with 0.3px letter spacing. The brand logo (typically in BebasNeue) sits left, with cart and account icons right. No background color change on scroll — the canvas remains consistent.

**`category-tag`** — Pill-shaped tags (9999px radius) for filtering products by category (e.g., "Kitchen", "Bath", "All-Purpose"). Inactive state uses the soft surface (#f7f7f8) with muted text (#595959). Active state fills with near-black (#080808) and white text. Tags are compact at 6px vertical padding for horizontal scrolling strips.

### Forms
**`text-input`** — Standard form input with off-white background, 48px height, and 8px corner radius. Border uses the hairline (#ebebeb) by default, switching to near-black on focus. Typography is body-md (16px) for readability. Used in search, newsletter signup, and checkout forms.

**`search-bar`** — A dedicated search input matching the text-input dimensions but with a search icon inset. On focus, the border transitions to near-black. The bar sits prominently in the nav on mobile and collapses to an icon on desktop.

### Footer
**`footer`** — A near-black (#080808) footer section with white text, spanning the full viewport width. Links use body-sm (14px) with generous spacing (48px padding top/bottom). The footer includes the brand's sustainability messaging, customer service links, and social icons in white. No accent colors — the footer is purely monochrome.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; search bar becomes icon-triggered overlay; category tags scroll horizontally; buttons full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; search bar inline; category tags wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; persistent search bar; category tags in single horizontal strip |
| Wide | > 1440px | Four-column product grid; max-width container (1440px) centered; increased whitespace around hero and product sections |

### Touch Targets
- All buttons and interactive elements minimum 44px height (buttons, inputs, selectors)
- Category tags minimum 32px height for comfortable tapping
- Nav links and icons minimum 40px tap area
- Quantity selector buttons minimum 40px x 40px

### Collapsing Strategy
- Primary nav links collapse to hamburger menu below 744px
- Search bar collapses to icon-only trigger below 744px, expands to full-width overlay on tap
- Product grid collapses from 4 columns to 1 column below 744px
- Footer link columns stack vertically below 744px
- Category tag strip switches from horizontal scroll to wrap layout between 744px and 1128px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be reliably extracted from static analysis; only primary button hover was inferred from the extracted palette
- Error states (input validation, form submission errors) are not represented in the extracted data
- Dark mode is not present on the live site; no dark palette tokens available
- The exact font stack for NeuzeitS-Book variants (Book, Heavy, Regular) could not be disambiguated; the stack shown uses the most common declaration
- BebasNeuse usage is inferred from font-family declarations but exact sizes and weights for display headlines are estimated based on typical brand implementation
- Spacing values for components are estimated from common e-commerce patterns; exact padding/margin values may vary on the live site
- The accent colors (#4469af, #c8232c, #eca937, #dc886d) were present in extracted hex data but their specific usage contexts (badges, links, sale tags) are inferred
- No animation or transition timing data was extractable
- Shopify-specific checkout widget colors (Klarna, Afterpay) may be present in the extracted palette but are not part of the brand design system
