---
version: alpha
name: "Cariuma"
source_url: "https://cariuma.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Forest teal (#108474) does the heavy lifting in Cariuma's visual system — not a generic eco-marketing green but a deep, almost oceanic hue that anchors every primary CTA, sustainability callout, and active hover state. The supporting palette tells the rest of the brand's ecological story: a bright chartreuse green (#77c043) for certified-material badges and growth signals, a warm golden yellow (#fbcd0a) for promotional moments and sale strips, and a quieter soft lavender (#a89cc8) that surfaces in seasonal colorways without overpowering the core teal. Type splits across two registers: Baskerville carries the editorial weight — section headers where conviction matters, long-form sustainability copy that reads like a printed manifesto — while HCo Gotham handles product UI, navigation labels, and button copy in clean geometric mid-weight. Neither font reaches for decorative effect; together they read as a brand that wants to be taken seriously without performing luxury. The canvas stays near-white (#fafafa, #f9fafb) held up by a hierarchy of cool light grays (#f5f5f5, #f2f2f2, #eeeeee) that let natural-material product photography do its work — cork soles, bamboo canvas, and sugarcane-based midsoles all photograph cleaner against these neutral grounds. Corners land at `{rounded.none}` to `{rounded.sm}`; there are no pill shapes here, no rounded-corner friendliness borrowed from athleisure — Cariuma's geometry is straight-shouldered, closer to craft heritage than lifestyle sport. Sustainability panels shift to a light teal wash (#edf5f5) as a tonal signal that the brand is explaining rather than selling, separating its values language from its conversion language. Spacing is generous at the `{spacing.section}` level, letting photography breathe between story beats so each shoe feels curated rather than catalogued. Checkout and size-selector flows strip color to near-black (#121212) and white, keeping the conversion path clear while every upstream page deploys the full palette to communicate environmental ambitions.

colors:
  primary: "#108474"
  primary-active: "#0a6358"
  primary-disabled: "#7bbdb5"
  eco-green: "#77c043"
  eco-green-mid: "#66a443"
  eco-green-deep: "#508131"
  accent-yellow: "#fbcd0a"
  lavender: "#a89cc8"
  teal-soft: "#c1e6e6"
  teal-wash: "#edf5f5"
  ink: "#121212"
  body: "#4a4a4a"
  muted: "#7b7b7b"
  muted-light: "#888888"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#f9fafb"
  surface-card: "#f5f5f5"
  surface-gray: "#f2f2f2"
  on-primary: "#ffffff"
  error: "#ff0000"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Book Antiqua', Palatino, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Book Antiqua', Palatino, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Baskerville, 'Book Antiqua', Palatino, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'HCo Gotham', 'Nunito Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'HCo Gotham', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  body-md:
    fontFamily: "'Nunito Sans', 'HCo Gotham', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'HCo Gotham', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'HCo Gotham', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-caps:
    fontFamily: "'HCo Gotham', 'Nunito Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'HCo Gotham', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'HCo Gotham', 'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'HCo Gotham', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  price:
    fontFamily: "'HCo Gotham', 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.2
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
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
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 1.5px
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-eco:
    backgroundColor: "{colors.eco-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-light}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoMaxHeight: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBg: "{colors.surface-gray}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    hoverImageScale: 1.03
    hoverBorder: "2px solid {colors.primary}"
    padding: "{spacing.base}"
  eco-badge:
    backgroundColor: "{colors.teal-wash}"
    textColor: "{colors.primary}"
    borderColor: "{colors.teal-soft}"
    borderWidth: 1px
    typography: "{typography.label-caps}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  material-tag:
    backgroundColor: "{colors.eco-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    selectedBg: "{colors.ink}"
    selectedText: "{colors.canvas}"
    unavailableDecoration: line-through
    unavailableColor: "{colors.muted-light}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    size: 44px
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    selectedOutline: "2px solid {colors.ink}"
    selectedOutlineOffset: 2px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 600px
    imagePosition: right center
    overlayOpacity: 0
  sustainability-panel:
    backgroundColor: "{colors.teal-wash}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    iconColor: "{colors.primary}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.section}"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderBottom: "2px solid transparent"
    activeBorderBottom: "2px solid {colors.primary}"
  review-star:
    fillColor: "{colors.eco-green}"
    emptyColor: "{colors.hairline}"
    size: 16px
  promo-banner:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: 10px 16px
    fontWeight: 600
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.muted-light}"
    typography: "{typography.caption}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} 0"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    headerBg: "{colors.surface-soft}"
    width: 420px

## Components

### Buttons
**`button-primary`** — Square-cornered (`{rounded.none}`) forest-teal block at 48px tall, set in uppercase Gotham at 14px/0.8px tracking. On hover the background deepens from #108474 to `{colors.primary-active}` without animation delay, asserting rather than inviting. Disabled state uses mid-teal `{colors.primary-disabled}` to preserve brand presence rather than collapsing to gray. This button carries all product add-to-cart and checkout actions.

**`button-secondary`** — White fill with a 1.5px teal border and matching teal label, same 48px height and uppercase Gotham treatment as the primary. Used for secondary CTAs like "Learn More" on sustainability panels, wishlist actions, and size-guide triggers. Communicates the same brand register without the visual dominance of a filled teal block.

**`button-ghost`** — Hairline border, ink text, transparent fill. Appears in checkout flows and filter sidebars where teal would compete with active selection states. Maintains the same uppercase tracking, so button-family consistency holds across all three variants.

**`button-eco`** — A chartreuse-green (#77c043) filled block reserved exclusively for sustainability-context CTAs: "Offset Your Carbon," "See Our Materials," and B-Corp certification panels. Never appears on product or checkout flows — the color distinction signals a register shift from commerce to purpose.

### Navigation
**`nav-bar`** — 64px tall, near-white (#fafafa) background with a subtle hairline bottom border. Logo left; category links (Men, Women, Sale, Sustainability) centered in 14px Gotham medium; a right cluster carries search, wishlist, and cart. On scroll, a box-shadow replaces the border to signal page separation without a background color change. The Sustainability link often carries a teal dot marker, nudging attention toward the brand's differentiating story.

### Product Card
**`product-card`** — Square-cornered card on a light gray (#f5f5f5) image field with no decorative radius. On hover, the image scales 1.03× and a 2px teal border wraps the card edge, signaling interactive intent without a separate overlay or color wash. Title uses `{typography.title-md}` in ink; price uses `{typography.price}` directly below in the same weight family. Color swatches appear as 28px `{rounded.full}` dots with a 2px ink outline on the active swatch. Chartreuse `material-tag` labels pin to the image corner for bamboo, sugarcane, or cork material callouts.

### Size Selector
**`size-selector`** — 44×44px square buttons arranged in a tight grid with no gap rounding. Default: white fill, hairline border, ink text in `{typography.body-sm}`. Selected state inverts to full ink fill with white text. Unavailable sizes carry struck-through text in `{colors.muted-light}` with a diagonal SVG slash across the button face. The hard-square geometry here reinforces the same no-radius language used across the product experience.

### Eco Badge & Material Tag
**`eco-badge`** — Small chip with #edf5f5 fill and a #c1e6e6 border bearing uppercase `{typography.label-caps}` labels: "B Corp," "Carbon Neutral," "1% for the Planet." Appears on product cards, PDPs, and the sustainability panel header. The certification-document register comes from the tight tracking and 11px cap height rather than from iconography.

**`material-tag`** — Flush chartreuse (#77c043) block pinned to the product image corner with zero border radius. Used for "Bamboo Canvas," "Sugarcane EVA," and "Cork Insole" callouts — physical-tag energy rather than digital chip friendliness. Never appears outside of image contexts.

### Sustainability Panel
**`sustainability-panel`** — Full-width section on a #edf5f5 teal-wash ground. Headline in `{typography.display-md}` Baskerville, body in `{typography.body-md}` Nunito Sans. A three- or four-column icon grid below the headline uses teal SVG icons (leaf, water droplet, recycle loop) with `{typography.caption}` labels beneath each. This panel appears on every PDP below the fold, deliberately interrupting the add-to-cart momentum to re-anchor on brand purpose before the customer decides.

### Hero Banner
**`hero-banner`** — Split layout: editorial copy on the left (~45% width) over a near-white canvas, full-bleed studio product photography on the right. Headline in `{typography.display-xl}` Baskerville; subtitle in `{typography.body-md}` Nunito Sans at normal weight; primary CTA below. No gradient overlay — photography is shot against clean studio grounds that match the canvas color so the seam between image and copy field dissolves naturally. On mobile the image stacks above copy and minimum height collapses to fit the viewport.

### Promo Banner
**`promo-banner`** — Full-width golden-yellow (#fbcd0a) strip sitting above the nav bar. Short semi-bold ink copy in `{typography.body-sm}` for shipping thresholds, seasonal promotions, and certification announcements. Dismissible via an ink-colored × button on the right edge. The yellow is used nowhere else in the page, making this the highest-contrast attention signal in the entire layout.

### Footer
**`footer`** — Near-black (#121212) ground with white body links and uppercase `{typography.title-sm}` Gotham column headers. Link hover shifts to `{colors.primary}` teal — the only instance of the brand primary appearing on a dark surface. Four columns: Shop, Sustainability, About, Support. The B-Corp logo and social icons sit in the bottom strip above legal copy, giving the certification mark a permanent position in the most persistent template element.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks image above copy; nav collapses to hamburger with full-screen drawer; size selector scrolls horizontally; sustainability panel switches to single column with stacked icons |
| Tablet | 744–1128px | Two-column product grid; hero maintains split but copy column widens to 55%; nav shows logo and icon cluster only, category links hidden behind hamburger |
| Desktop | 1128–1440px | Three-column product grid; full nav visible; hero at natural split ratio; sustainability panel three-column icon grid |
| Wide | > 1440px | Four-column product grid; content max-width 1440px centered; hero gains additional left-side padding; footer spreads to five columns |

### Touch Targets
- Size selector buttons: 44×44px minimum, meeting WCAG AA
- Nav icon buttons (search, cart, wishlist): 44×44px tap area with 24×24px visual icon
- Color swatches: 28px visual, padded to 44px tap target
- Promo banner dismiss button: 44×44px tap area with 16px visual ×

### Collapsing Strategy
- Navigation: desktop horizontal links → hamburger drawer at < 1128px; search expands inline on desktop, full-screen overlay on mobile
- Sustainability panel: 4-column icon grid → 2-column at tablet → single column at mobile
- Product card color swatches: show up to 4, overflow truncated with "+N" count badge
- Hero: side-by-side split → stacked (image above, copy below) below 744px; minimum hero height collapses from 600px to natural content height

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No design token file or CSS custom properties directly accessible; all colors derived from extracted page render values — exact brand-specified hex codes may differ slightly
- Specific Gotham weight variants (Light, Book, Medium, Bold) used per context not confirmed; numeric weights 400/500/600/700 used as approximations
- Baskerville variant (regular vs. italic) used for display headings not confirmed from extraction
- Animation durations and easing curves for hover transitions (card border reveal, nav shadow) not captured
- Exact product grid gutter widths and column gap values not extracted
- Icon library for sustainability icons and nav icons not identified (custom SVG vs. third-party set)
- Cart drawer animation behavior (slide-in vs. modal overlay) not confirmed
- Dark-mode or high-contrast mode configuration not observed
- Review widget star color (#77c043 eco-green approximation) inferred from brand palette, not pixel-extracted from JudgeMe render
- Loyalty or rewards program UI components not observed on extracted pages
