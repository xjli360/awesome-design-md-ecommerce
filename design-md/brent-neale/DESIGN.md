---
version: alpha
name: "Brent Neale"
source_url: "https://www.brentneale.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Warm parchment (#f8f4eb) is the first cue: Brent Neale operates more like a private jeweler's reference book than a standard e-commerce grid. The palette layers three registers of gold — a mid-tone honey (#9d8858) as the signature brand accent, an amber vein (#a77a06) for active states, and a deep burnished sienna (#625332) for depth — all read against that cream canvas that makes each piece appear as if resting on archival paper rather than floating in a digital void. Garamond Premier Pro arrives in four optical-size variants (caption, text, subhead, display), carrying all editorial weight: long-form product descriptions, collection intros, and story prose run in the display cut at generous leading with open tracking, while Basis Grotesque Regular Pro handles every piece of UI chrome — navigation labels, price strings, checkout inputs — in deliberate counterpoint to the serif's warmth. The unexpected presence of a violet (#574cd5) appears in hover treatments and select interactive states, a flash of color recalling Brent Neale's signature rainbow gemstone work: bold, unlikely, and somehow exactly right. Hairlines hold at pale #ededed and barely announce themselves; product cards sit on the cream canvas without visible borders; corner radii stay at none or xs across all containers — the visual grammar of a space that trusts its objects to do the work and keeps its architecture invisible. Functional states complete the jewel-box range: a terracotta red (#c31818) for sale pricing, a muted forest green (#3c9342) for availability confirmation, and a near-black (#171717) that anchors primary CTAs as the one hard edge in an otherwise warm, yielding surface.

colors:
  primary: "#9d8858"
  primary-active: "#a77a06"
  primary-disabled: "#c9b899"
  ink: "#171717"
  body: "#4a4a4a"
  muted: "#aaaaaa"
  hairline: "#ededed"
  hairline-soft: "#e8e8e8"
  hairline-strong: "#dedede"
  canvas: "#f8f4eb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#f8f4eb"
  on-dark: "#f8f4eb"
  accent-violet: "#574cd5"
  gold-warm: "#7e6b45"
  gold-deep: "#625332"
  sale: "#c31818"
  sale-dark: "#a70100"
  availability: "#3c9342"
  availability-alt: "#478947"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "'garamond-premier-pro-display', 'Garamond Premier Pro', Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: 0.01em
  display-lg:
    fontFamily: "'garamond-premier-pro-display', 'Garamond Premier Pro', Georgia, serif"
    fontSize: 38px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: 0.01em
  display-md:
    fontFamily: "'garamond-premier-pro-subhead', 'Garamond Premier Pro', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "'garamond-premier-pro-subhead', 'Garamond Premier Pro', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.01em
  product-title:
    fontFamily: "'garamond-premier-pro', 'Garamond Premier Pro', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'garamond-premier-pro', 'Garamond Premier Pro', Georgia, serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'garamond-premier-pro', 'Garamond Premier Pro', Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'garamond-premier-pro-caption', 'Garamond Premier Pro', Georgia, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  body-ui:
    fontFamily: "'basis-grotesque-regular-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  title-md:
    fontFamily: "'basis-grotesque-regular-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  title-sm:
    fontFamily: "'basis-grotesque-regular-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  price:
    fontFamily: "'basis-grotesque-regular-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'basis-grotesque-regular-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'basis-grotesque-regular-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-label:
    fontFamily: "'basis-grotesque-regular-pro', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.05em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    opacity: 0.5
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-ui}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoType: wordmark
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.nav-label}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    gap: "{spacing.sm}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    height: 36px
    textAlign: center
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    layout: fullBleed
    ctaStyle: button-primary
    padding: "{spacing.section} 0"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    descriptionTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.product-title}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.none}"
    imageFit: cover
    imageAspect: 1 / 1
    gap: "{spacing.sm}"
    border: none
  quick-add-button:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    hoverBackgroundColor: "{colors.ink}"
    hoverTextColor: "{colors.canvas}"
    height: 36px
  product-badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  product-badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  price-display:
    textColor: "{colors.body}"
    typography: "{typography.price}"
    saleColor: "{colors.sale}"
    compareAtDecoration: line-through
    compareAtColor: "{colors.muted}"
  swatch-selector:
    size: 20px
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    borderSelected: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    padding: 8px 16px
  accordion:
    borderTop: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    padding: "{spacing.base} 0"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    bodyTypography: "{typography.body-ui}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.canvas}"
    typography: "{typography.nav-label}"
    bodyTypography: "{typography.body-ui}"
    padding: "{spacing.xxl} 0"
    linkHoverColor: "{colors.primary}"

## Components

### Buttons
**`button-primary`** — A sharp-cornered rectangular block with ink fill (#171717) and canvas text (#f8f4eb) in uppercase Basis Grotesque at 13px / 0.1em tracking. On hover the background transitions to brand gold (#9d8858) with cream text maintained — a warm payoff that rewards attention. The disabled state lightens to a derived pale gold (#c9b899) at reduced opacity rather than introducing a neutral gray. Focus carries a visible offset ring against the cream canvas for accessibility.

**`button-secondary`** — Matching geometry to primary, transparent fill with a 1px ink border and ink text. Hover inverts to solid ink, matching the primary rest state. Used for secondary CTAs like wishlist, gift notes, and filter confirmations where the page needs a second action without competing with the main CTA.

**`button-ghost`** — Text-only with an underline, body-gray (#4a4a4a), no border and no radius. Used for inline prose expansions, "Read More" in collection descriptions, and navigation cross-links within editorial copy.

### Navigation
**`nav-bar`** — A 64px canvas bar (#f8f4eb) with a single hairline bottom border (#ededed), wordmark centered or left-justified, and uppercase Basis Grotesque nav labels at 13px / 0.05em tracking. Dropdown panels inherit the canvas background and a hairline border, with category links tightly spaced in the same label style. A slim announcement bar in brand gold (#9d8858) with cream uppercase text sits above the nav on all pages.

### Product Cards
**`product-card`** — Square 1:1 images on the open canvas — no card container, no visible border, no drop shadow. The product title runs in Garamond Premier Pro at 20px below the image, followed by the price in Basis Grotesque. On hover, a `quick-add-button` slides up from the image base: hairline-bordered at rest, ink-filled on tap. The absence of any containing box means the grid reads as a sequence of floating objects, consistent with the archival-catalog aesthetic.

### Product Detail
**`accordion`** — Product details, materials, and care instructions live in hairline-bordered accordion rows. Headers use uppercase Basis Grotesque in `title-sm`; expanded bodies use Garamond's caption variant at 15px. Open and closed states share the same canvas background — no fill change differentiates them, keeping the page surface continuous.

**`swatch-selector`** — 20px circular gem-tone chips with a 1px hairline ring, upgrading to a 2px ink ring on selection. Gap is minimal (4px) to keep the selector compact for pieces offering multiple metal tones or stone colors. Touch area expands beyond the visual size for mobile usability.

**`size-selector`** — Rectangular, borderless-radius chips in hairline borders at rest, ink border on selection. Used primarily for ring sizes and bracelet lengths. No pill shape — the flat geometry matches the broader no-radius visual language.

### Utility
**`cart-drawer`** — A 400px right-panel drawer on the warm canvas, separated from the page by a single hairline left border. Item titles in Garamond; quantity controls and price in Basis Grotesque. No drop shadow — the hairline carries the visual separation cleanly.

**`price-display`** — Sale prices appear in terracotta red (#c31818) with the compare-at original in muted gray with strikethrough. Regular pricing uses body (#4a4a4a) rather than the deepest ink, softening the commercial moment against the editorial page tone.

**`footer`** — An ink (#171717) field inverting the warm canvas, with canvas-colored nav-label links that warm to brand gold on hover. Column headers in uppercase `title-sm`, body copy in `body-ui`. The inversion creates a definitive visual end to the page without introducing a new surface color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen slide-in drawer; announcement bar reduces to 30px; hero headline scales to display-md; product title truncates to 2 lines with ellipsis |
| Tablet | 744–1128px | Two-column product grid; nav retains wordmark but collapses links to hamburger; collection header padding compresses to spacing.xl; cart drawer narrows to 360px |
| Desktop | 1128–1440px | Three or four-column product grid; full horizontal nav with dropdown flyouts; hero at display-xl with section-level vertical padding; quick-add surfaces on hover |
| Wide | > 1440px | Grid caps at four columns within a ~1400px max-width container; canvas margins on either side reinforce the reference-book stillness |

### Touch Targets
- All buttons minimum 44px tall
- Swatch selectors expand touch target to 32×32px regardless of visual swatch size
- Accordion rows minimum 48px tap height
- Nav links minimum 44px height in mobile drawer

### Collapsing Strategy
- Nav: full horizontal with dropdowns → hamburger with slide-in full-screen drawer
- Product grid: 4-col → 3-col → 2-col → 1-col as breakpoints descend
- Hero: full-bleed with text overlay or side-by-side → stacked image-above / text-below on mobile
- Filters: sidebar panel (desktop) → bottom sheet drawer (mobile)
- Announcement bar: always present, height reduces from 36px to 30px on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Logo wordmark weight, size, and exact lockup geometry not confirmed; treatment inferred from fine-jewelry category conventions
- Whether the violet accent (#574cd5) is a theme-level CTA color or a component-scoped hover treatment is ambiguous — verify in live Shopify theme settings
- Primary-disabled color (#c9b899) is a derived lighter gold not present in the extracted palette; replace with the actual disabled token if available in theme CSS variables
- Hover transition timing and easing curves not extractable from static color analysis
- Exact nav height, announcement bar height, and whether both are present simultaneously require live inspection
- Collection filter panel layout (sidebar vs. horizontal top bar) not confirmed
- Whether a wishlist, back-in-stock alert, or email capture modal exists and its visual treatment not observed
- Dark-mode or high-contrast variant not detected; assumed light-only
