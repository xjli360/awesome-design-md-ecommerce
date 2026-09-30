---
version: alpha
name: "Jenny Bird"
source_url: "https://jenny-bird.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The #ffcf2a marigold-gold that saturates Jenny Bird's primary CTA buttons and category labels is not an accent — it is a temperature match for the brand's actual vermeil and brass castings, so browsing the site carries the ambient warmth of looking into a lit jewelry case. Against deep near-black (#1c1d1d) headers and a rich dark navy (#272d45) used in editorial modules, the yellow reads as actual metal rather than UI color. The contrast it achieves with {colors.on-primary} (#1c1d1d) text is high enough for accessibility without sacrificing warmth — a rare quality in a saturated yellow. Typography divides into two entirely distinct voices: Sabon LT Pro and EB Garamond carry the editorial register — product campaigns, collection introductions, brand storytelling — at 400 weight so the serif sits open and press-cut rather than heavy; Avenir and Avenir Light manage the transactional layer across navigation, filters, price strings, and form inputs, with letter-spacing at 0.05–0.1em to preserve legibility at small sizes. The pairing is disciplined and asymmetric — the serif vocabulary signals artisanal provenance without antiquarian styling, while the humanist sans keeps conversion flows modern and uncluttered. A secondary teal (#0e7a82) appears exclusively on sale indicators and promotional badges, cool-toned against the warm primary so that commercial urgency reads at a different chromatic frequency than brand warmth — they coexist without competing. The periwinkle-slate (#676986) functions as a structural neutral: filter chips, metadata labels, secondary navigation states — quieter than {colors.muted} (#707070) but more distinctive than generic gray. Rounded corners are deliberately minimal: {rounded.xs} on badges and chips, {rounded.sm} on input fields and buttons, {rounded.none} on full-bleed images — the system stays close to architectural and jewelry-cabinet-precise, never soft or bubble-like. Product cards rest on pale gray ({colors.surface-soft}, #f4f4f6), image-led in a 3:4 portrait ratio with product name below in Sabon LT Pro and price in Avenir — the font-family switch within a single card encodes the brand's dual register even at the micro level. The footer reverses the entire palette to {colors.surface-dark} (#1c1d1d) with pale hairlines and {colors.on-dark} type, a deliberate tonal shift that closes the editorial loop and signals the brand's fluency in its own visual language.

colors:
  primary: "#ffcf2a"
  primary-active: "#e6b600"
  primary-disabled: "#f5e3a0"
  teal-accent: "#0e7a82"
  slate-secondary: "#676986"
  dark-navy: "#272d45"
  ink: "#1c1d1d"
  body: "#535565"
  muted: "#707070"
  muted-soft: "#a4a5a5"
  hairline: "#e5e5e5"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f4f4f6"
  surface-card: "#e5e5eb"
  surface-dark: "#1c1d1d"
  on-primary: "#1c1d1d"
  on-dark: "#f4f4f6"

typography:
  display-xl:
    fontFamily: "'Sabon LT Pro', 'EB Garamond', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Sabon LT Pro', 'EB Garamond', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Sabon LT Pro', 'EB Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Avenir', 'Avenir Light', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Avenir', 'Avenir Light', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.03em
  body-md:
    fontFamily: "'Avenir Light', 'Avenir', -apple-system, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir Light', 'Avenir', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  button-md:
    fontFamily: "'Avenir', 'Figtree', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Avenir', 'Figtree', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-label:
    fontFamily: "'Avenir', -apple-system, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.05em
  product-name:
    fontFamily: "'Sabon LT Pro', 'EB Garamond', Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Avenir', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge-label:
    fontFamily: "'Avenir', -apple-system, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
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
    padding: 14px 28px
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
    padding: 13px 27px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 44px
    border: "1px solid {colors.on-dark}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
    border-focus: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoFont: "{typography.display-sm}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    productNameFont: "{typography.product-name}"
    priceFont: "{typography.price-display}"
    priceColor: "{colors.muted}"
    padding: "{spacing.sm}"
    gap: "{spacing.xs}"
  hero-editorial:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineFont: "{typography.display-xl}"
    subheadFont: "{typography.body-md}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaFont: "{typography.button-md}"
    overlayOpacity: 0.35
    padding: "{spacing.section} {spacing.xl}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineFont: "{typography.display-md}"
    subheadFont: "{typography.body-sm}"
    subheadColor: "{colors.muted}"
    textAlign: center
    padding: "{spacing.xxl} 0 {spacing.xl}"
  sale-badge:
    backgroundColor: "{colors.teal-accent}"
    textColor: "#ffffff"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.slate-secondary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    border: "1px solid {colors.hairline}"
    border-active: "1px solid {colors.ink}"
    textColor-active: "{colors.ink}"
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-label}"
    borderBottom: "2px solid transparent"
    borderBottom-active: "2px solid {colors.primary}"
    textColor-active: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    border: none
    placeholderColor: "{colors.muted}"
  jewelry-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "2px solid {colors.hairline}"
    border-active: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingFont: "{typography.title-sm}"
    linkFont: "{typography.body-sm}"
    linkColor: "{colors.on-dark}"
    hairlineColor: "#333333"
    padding: "{spacing.section} 0"

---

## Components

### Buttons
**`button-primary`** — Jenny Bird's primary action button fills with the signature #ffcf2a marigold-gold and sets near-black {colors.on-primary} text in 13px uppercase Avenir at 0.1em tracking. Height is 44px with {rounded.sm} corners — angular enough to feel precision-cut without harshness. On active/pressed states the fill deepens to `{colors.primary-active}` (#e6b600); disabled drains to `{colors.primary-disabled}` with {colors.muted} text. Used on PDPs for "Add to Bag" and on hero modules as the primary editorial CTA.

**`button-secondary`** — A 1px {colors.ink} border on a white {colors.canvas} fill with matching uppercase Avenir label, same height as primary. Used where the page already carries enough warmth and the gold fill would create visual competition. On dark editorial backgrounds `button-secondary-dark` substitutes transparent fill and {colors.on-dark} border and text, preserving the outlined structure.

**`button-ghost`** — Text-only link button in {typography.button-md} with an underline decoration and no background or border. Reserved for tertiary editorial actions — "Shop the story," "See all" — where adding weight would disrupt content flow.

### Text Input
**`text-input`** — 44px tall with {rounded.xs} corners (nearly flat) and a 1px {colors.hairline} border that sharpens to 1px {colors.ink} on focus. Body text is Avenir Light 16px with {colors.muted} placeholder copy. No floating labels or animated validation states — the field is minimal and undemonstrative.

### Navigation
**`nav-bar`** — 64px tall on {colors.canvas} with a 1px {colors.hairline} bottom border. The JENNY BIRD wordmark sits left in {typography.display-sm} Sabon LT Pro — the only serif element in the nav frame. Navigation links use {typography.nav-label} (Avenir, 13px, 0.05em tracking); cart, search, and account icons anchor the right cluster. Mobile collapses to a hamburger triggering a full-screen {colors.surface-dark} drawer with stacked links in {colors.on-dark}.

**`category-tab`** — A horizontal tab row on PLP pages beneath the main nav. Inactive tabs carry {colors.muted} text and no indicator; the active tab gains a 2px {colors.primary} bottom border and {colors.ink} text — the gold stripe is the only navigation affordance that uses the primary color, anchoring context without pressure.

### Product Card
**`product-card`** — Sits on a pale {colors.surface-soft} (#f4f4f6) tile, no border, no shadow. Image is full-width at a 3:4 portrait ratio. Below the image: product name in {typography.product-name} (Sabon LT Pro, 15px) and price in {typography.price-display} (Avenir, 14px, {colors.muted}) — the font-family shift between name and price encodes the editorial/transactional divide even at the smallest card scale. On hover, a secondary model image swaps in via Shopify variant-image behavior. `sale-badge` and `new-badge` pin to the top-left corner of the image.

### Badges
**`sale-badge`** — Teal (#0e7a82) fill with white text in {typography.badge-label} (10px uppercase Avenir, 0.08em tracking). The cool teal is deliberately chromatic-opposite to the warm gold, so price-reduction signals don't bleed into brand warmth. `new-badge` uses {colors.primary} (#ffcf2a) fill with {colors.on-primary} text at the same label scale — arrival emphasis in the brand's own temperature.

### Filter Chip
**`filter-chip`** — Pill-shaped ({rounded.full}) with a 1px {colors.hairline} border and {colors.slate-secondary} (#676986) text in 11px uppercase Avenir. Active state upgrades the border to 1px {colors.ink} and snaps text to {colors.ink}. Used on PLP pages for material (gold-tone, silver-tone), style, and size. The chip row scrolls horizontally on mobile with a gradient trailing fade to signal overflow.

### Hero Editorial
**`hero-editorial`** — Full-bleed dark section ({colors.surface-dark}) with a photography layer at 0.35 overlay opacity. Headline in {typography.display-xl} (Sabon LT Pro, 48px) in {colors.on-dark}; subhead in {typography.body-md} (Avenir Light) with 1.6 line height. The CTA button fills {colors.primary} with {colors.on-primary} text — the gold-on-dark pairing is the system's highest-contrast moment and the brand's strongest voltage. Padding is {spacing.section} vertically, {spacing.xl} horizontally.

### Collection Header
**`collection-header`** — Centered, white-background section atop every PLP. Headline in {typography.display-md} (Sabon LT Pro, 32px, {colors.ink}); editorial subhead in {typography.body-sm} ({colors.muted}). The typographic deceleration signals an editorial pause before the product grid resumes below, a deliberate rhythm the brand maintains across all collection landings.

### Search Bar
**`search-bar`** — Borderless, {colors.surface-soft} fill, {rounded.xs} corners. Activates as an overlay on icon tap. Placeholder copy in {colors.muted} Avenir Light. The absence of a border distinguishes it visually from `text-input` transactional fields while keeping the same quiet, undecorated language.

### Jewelry Swatch
**`jewelry-swatch`** — 20px circular metal-finish selectors ({rounded.full}) for variant selection on PDP and quick-add panels. Inactive swatches carry a 2px {colors.hairline} ring; the selected swatch upgrades to a 2px {colors.ink} ring with no fill change, keeping focus on the metal color itself. Common variants render as gold-tone (warm fill), silver-tone (cool fill), and two-tone (split fill). Gap between swatches is {spacing.xs}.

### Footer
**`footer`** — Full-width dark reversal to {colors.surface-dark} (#1c1d1d). Column headings in {typography.title-sm} (Avenir medium, 14px) in {colors.on-dark}; link lists in {typography.body-sm} (Avenir Light) at the same color. Newsletter row embeds a text input and a {colors.primary} gold CTA button — the gold reappears here as the single warm accent against dark, closing the editorial loop that opened in the hero. Internal hairlines use #333333 to separate column groups without reading as borders.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + full-screen dark drawer; filter chips scroll horizontally with trailing fade; hero headline drops to {typography.display-md}; collection-header subhead removed to save vertical space |
| Tablet | 744–1128px | Two-column product grid; nav shows wordmark + icon cluster only, text links hidden; category tabs scroll horizontally if overflow; hero retains full-bleed with centered text overlay |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav text links visible; filter chips wrap rather than scroll; hero uses side-anchored text over full-bleed image |
| Wide | > 1440px | Max-width container (~1440px) centered on canvas; product grid holds at four columns; hero image extends edge-to-edge behind the constrained content column |

### Touch Targets
- All buttons minimum 44px height on mobile regardless of visual padding
- Filter chips padded to ≥ 44px tap target height with transparent vertical extension
- Jewelry swatches expand from 20px visual to 32px tap target via transparent padding on touch devices
- Nav icon buttons (cart, search, account) minimum 44×44px hit area

### Collapsing Strategy
- Mega-menu nav folds to a full-screen {colors.surface-dark} drawer with stacked category links in {colors.on-dark} and a visible close trigger
- Category tabs on PLP convert to a horizontally scrolling chip row on mobile, hidden behind a {colors.canvas} gradient fade on the trailing edge
- Collection header collapses to a single headline line above the filter row; editorial subhead is suppressed on screens below 744px
- Hero editorial stacks vertically on mobile: text block and CTA above, image below, or image full-bleed with reduced overlay opacity
- Footer columns collapse to a single-column accordion on mobile; each section heading becomes a tap-to-expand toggle

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact nav behavior on scroll (sticky vs. hide-on-scroll vs. static) could not be confirmed from static extraction
- Font weights for Sabon LT Pro beyond regular (400) not observed — italic and bold variants assumed available but not confirmed in production use
- Wordmark logo exact size and any custom letterspacing not extractable; {typography.display-sm} is an approximation
- Figtree appears in the font stack but its specific component assignments versus Avenir could not be distinguished from extraction data alone
- Product card hover animation timing and easing curve not available from static analysis
- Exact Shopify theme breakpoints are estimates; the theme may use non-standard values
- No motion or animation tokens observable from static extraction
- Cart drawer and mini-cart styling not captured
- The #2c3e50 and #121212 values in the extracted list may be Shopify framework defaults or dead theme code — no confirmed production UI assignment identified
- Mega-menu structure, column count, and featured-image treatment not confirmed
