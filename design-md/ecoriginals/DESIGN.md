---
version: alpha
name: "Ecoriginals"
source_url: "https://ecoriginals.com.au"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Where most plant-based baby care brands retreat to sage and pastel restraint, Ecoriginals plants a bold tomato-red (#d72c0d) on every primary CTA against a warm beeswax-cream canvas (#eeede5) — a deliberate refusal of the visual shorthand that equates "natural" with "soft-spoken." The palette earns its confidence from contrast rather than comfort: a deep forest night (#21301d) anchors eco authority in the navigation header and overline headings, while warm sand (#e2aa79) and terracotta (#d38571) surface through feature panels and product callouts, evoking pressed botanicals and clay rather than antiseptic white. Montserrat — the single typeface across every scale — runs at 700–800 weight for display headlines and relaxes to 400–500 for ingredient copy and subscription prose, achieving a voice that reads clearly for a parent scanning labels at midnight and a desktop shopper comparing bundle savings at noon. Corner radii stay generous throughout: {rounded.lg} on product cards, {rounded.full} on certification badges and pill-shaped promo tags, which soften the primary's voltage without losing the directness that separates the brand from softer-coded competitors. A recurring deep forest panel ({colors.forest}) set against on-dark white type and ochre-yellow accent marks (#f1e04d) provides a brief moment of authority — used for subscription upsell blocks and sustainability pledges — before the page returns to warm cream and earthy accents. Add-to-cart buttons run full-width in red at the base of every product card, removing purchase friction without apology. The overall register is a brand that has done the formulation work, holds the certifications, and trusts that bold color plus ingredient honesty will close the sale faster than a mood board full of eucalyptus sprigs.

colors:
  primary: "#d72c0d"
  primary-hover: "#f9423a"
  primary-active: "#b82209"
  primary-disabled: "#f0b3aa"
  ink: "#232323"
  body: "#3c3c3b"
  muted: "#888887"
  hairline: "#dedede"
  hairline-soft: "#e3e3e3"
  canvas: "#eeede5"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  forest: "#21301d"
  on-forest: "#ffffff"
  sand: "#e2aa79"
  terracotta: "#d38571"
  ochre: "#f1e04d"

typography:
  display-xl:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 52px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  overline:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "'Montserrat', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
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
    padding: "14px 28px"
    height: 48px
    hoverBackgroundColor: "{colors.primary-hover}"
    activeBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.ink}"
    padding: "12px 26px"
    height: 48px

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "12px 26px"
    height: 48px
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"

  button-pill:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-forest}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"

  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px

  nav-bar:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-forest}"
    typography: "{typography.nav-link}"
    height: 64px
    logoMaxHeight: 40px
    borderBottom: none

  nav-bar-announcement:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.lg}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    ctaFullWidth: true
    ctaComponent: "button-primary"

  hero-banner:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-forest}"
    overlineTypography: "{typography.overline}"
    overlineColor: "{colors.sand}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    ctaComponent: "button-primary"

  eco-badge:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-forest}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 12px"

  promo-tag:
    backgroundColor: "{colors.ochre}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "4px 10px"

  trust-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.forest}"
    borderTop: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.lg} 0"

  ingredient-callout:
    backgroundColor: "{colors.sand}"
    textColor: "{colors.forest}"
    overlineTypography: "{typography.overline}"
    headingTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xl}"

  subscription-panel:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-forest}"
    accentColor: "{colors.ochre}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.lg}"
    padding: "{spacing.xxl} {spacing.xl}"
    ctaComponent: "button-primary"

  certification-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"

  quantity-selector:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    buttonColor: "{colors.forest}"
    height: 44px

  rating-stars:
    activeColor: "{colors.primary}"
    inactiveColor: "{colors.hairline}"
    typography: "{typography.caption}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-forest}"
    linkColor: "{colors.sand}"
    headingTypography: "{typography.overline}"
    bodyTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — The full-weight tomato-red (#d72c0d) CTA is the brand's single conversion signal; it appears on product cards (full-width), hero sections, and subscription panels with no ghost or outline variant competing for attention at the same level. On hover the fill lifts to a slightly brighter coral (#f9423a); on press it deepens to #b82209; disabled state renders in pale blush (#f0b3aa) to preserve the red family without implying interactability. Text is Montserrat 700 at 14px uppercase with 0.5px tracking — abbreviated, confident labels like "SHOP NOW" or "ADD TO BUNDLE."

**`button-secondary`** — Warm cream canvas fill with a 2px ink (#232323) border, used alongside primary actions where two equal-weight choices exist (e.g., "ADD TO CART" vs. "LEARN MORE" on a feature row). Shares the same uppercase Montserrat weight as primary to avoid hierarchy ambiguity; differentiated by fill and border alone.

**`button-ghost`** — Transparent fill, 2px primary-red border, primary-red text. Deployed on deep forest panels ({colors.forest}) where a full red fill would collapse into the background. On hover, fills solid to primary for a satisfying snap.

**`button-pill`** — Forest-green pill ({rounded.full}) for navigation sub-labels, filter toggles, and promo chips on light surfaces. Montserrat 700 at 12px uppercase; terse and informational rather than transactional.

### Navigation
**`nav-bar`** — A deep forest-green (#21301d) header that immediately signals the brand's eco positioning before a single word loads. White Montserrat 600 nav links; cart and hamburger icons in white. Height is 64px on desktop. The forest color holds on scroll — no transparency or color shift — maintaining stable brand presence across all page depths.

**`nav-bar-announcement`** — A slim 36px band in primary red (#d72c0d) sitting above the forest nav, used for shipping thresholds ("Free AU shipping over $X"), promo codes, or launch announcements. White caption text centered; dismissible with a right-aligned ×. The stacked red-over-forest opening immediately establishes the brand's two dominant hues before product imagery appears.

### Product Card
**`product-card`** — White surface with a 1px #dedede hairline and 20px corner radius ({rounded.lg}), floating slightly off the warm cream canvas. Product image fills the top two-thirds with a 12px inner radius ({rounded.md}). Title in {typography.title-sm} (Montserrat 600, 16px); price in {typography.price-display} (Montserrat 700, 22px) with strikethrough original price in {colors.muted} when on sale. An `eco-badge` in forest green overlays the image top-left when the product carries a plant-based or compostable claim. The add-to-cart button runs full-width in primary red at card base — no ghost variant, every card resolves to a clear buy action.

### Hero
**`hero-banner`** — Deep forest (#21301d) background, optionally overlaid on a lifestyle photograph with a dark scrim. An overline in warm sand (#e2aa79) using {typography.overline} (11px/700/uppercase/1.5px tracking) introduces the product category above a {typography.display-xl} (52px/800) headline in white. Body copy at {typography.body-md} in white follows, then a primary-red button-primary CTA. On mobile the headline scales to {typography.display-md} (36px/700) and padding collapses from {spacing.xxl} to {spacing.xl}.

### Badges & Tags
**`eco-badge`** — Compact forest-green pill ({rounded.full}) with white {typography.badge-label} text (10px/700/uppercase/1px tracking). Applied to product images and feature lists to flag plant-based, compostable, or dermatologist-tested claims without interrupting the layout. The forest color draws a visual thread back to the nav header.

**`promo-tag`** — Ochre-yellow (#f1e04d) pill with ink (#232323) text; used for "SAVE 20%", "SUBSCRIBE & SAVE", or limited-run callouts. The yellow creates a brief attention pulse on both light and dark surfaces without competing with the red primary, and its warmth harmonizes with the sand and terracotta accent palette.

**`certification-badge`** — Neutral surface-soft (#eeeeee) tile with 1px hairline border and {typography.caption} text, displayed in a horizontal trust strip to surface certifications (GOTS, dermatologist-tested, cruelty-free, compostable). No color emphasis — the brand lets the credential carry its own weight.

### Forms & Inputs
**`text-input`** — Clean white field, 1px hairline border, 8px radius ({rounded.sm}). Focus state promotes border to 2px primary-red, grounding form interaction in the same red energy as CTA buttons. Placeholder text in {colors.muted} (#888887). Used in email capture, subscription sign-up, and checkout address fields.

**`quantity-selector`** — Surface-soft (#eeeeee) background flanked by forest-green ± buttons, centered count in {typography.title-sm}. 1px hairline border, {rounded.sm} radius, 44px height meeting minimum touch target. Sits inline on the PDP beneath the size/variant selector and mirrors the color split of the nav (forest action, neutral field).

### Content Panels
**`ingredient-callout`** — Warm sand (#e2aa79) background with forest-green heading and body text, creating an earthy inversion of the primary palette. An {typography.overline} label ("WHAT'S INSIDE") precedes a {typography.title-md} claim; body copy at {typography.body-sm} lists key plant-derived ingredients. Rounded at {rounded.lg}. Used on PDPs and homepage feature rows where ingredient transparency is the conversion argument.

**`subscription-panel`** — Full-width deep forest (#21301d) block with ochre-yellow accent marks, white {typography.display-md} heading, {typography.body-md} body copy, and a primary-red button-primary CTA. This is the brand's highest-authority conversion surface — a contained panel that snaps a scrolling parent into focus before the final subscription decision. The ochre accent color ({colors.ochre}) applies to savings callouts or star icons within the panel.

### Trust & Social Proof
**`trust-strip`** — Canvas-cream (#eeede5) band with hairline borders top and bottom. Forest-green icons (leaf, truck, shield, lab flask) flanked by short {typography.body-sm} phrases ("Free AU shipping over $X", "Plant-based & biodegradable", "Dermatologist tested"). Runs as a 4-item horizontal row on desktop; collapses to 2×2 grid on mobile.

**`rating-stars`** — Five stars in primary red (#d72c0d) for filled, {colors.hairline} for empty. An unusual choice for baby care but consistent with the brand's commitment to owning its primary color everywhere rather than switching to a conventional gold or amber for social proof.

### Footer
**`footer`** — Near-black (#232323) base with a 3px primary-red top border that closes the page with the same red energy as the announcement bar that opens it, creating a deliberate chromatic frame. Column headings in {typography.overline} (11px/700/uppercase) in sand (#e2aa79); body links in sand at {typography.body-sm}. {spacing.section} (64px) padding top and bottom. Social icons in sand, turning white on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero headline drops to {typography.display-md} (36px/700); product grid 1-column; nav collapses to hamburger on forest bar; trust strip stacks 2×2 grid; subscription-panel padding reduces to {spacing.xl}; announcement bar text truncated or scrolls |
| Tablet | 744–1128px | 2-column product grid; hero splits text left / image right at 50/50; nav shows primary links, secondary links collapse to overflow menu; ingredient-callout switches to side-by-side |
| Desktop | 1128–1440px | 3–4 column product grid; hero expands to full-bleed with text overlay on photograph; nav fully expanded with all primary and secondary links; subscription-panel shows heading+body left, CTA block right |
| Wide | > 1440px | Max content width 1440px centered on canvas; hero background image extends edge-to-edge; all content panels constrained to 1440px inner container with auto side margins |

### Touch Targets
- All interactive elements minimum 44×44px — quantity selector buttons, icon buttons, nav links, and close buttons
- Add-to-cart button full-width on mobile product cards, giving a ~100% card-width tap area
- Cart icon and hamburger padded to 44px tap zone in forest nav bar
- Pill buttons minimum 36px height with extended horizontal padding to avoid mis-taps on small screens
- Announcement bar dismiss × padded to 44px tap zone even though the bar is only 36px tall

### Collapsing Strategy
- Nav: forest bar persists at all widths; primary links (Shop, Bundles, Subscriptions, About) visible at ≥744px; secondary links (Blog, Sustainability, FAQ) move to hamburger drawer below 1128px
- Trust strip: horizontal scroll with visible overflow on mobile rather than wrapping unpredictably; snap-scroll to 2-item increments
- Ingredient callout: image stacks above text on mobile; side-by-side at ≥744px with image occupying 45% of width
- Subscription panel: single-column stacked on mobile (heading → body → CTA); splits to heading+body left / savings callout+CTA right at ≥1128px
- Hero: text-only layout on mobile (image suppressed or reduced to background); full image/text split on tablet; full-bleed photography with overlay on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Custom icon set style (outline vs. filled, stroke weight) not extractable from static hints — forest green color is confirmed but glyph style is unverified
- Exact Montserrat weight subsets loaded not confirmed — 400, 600, 700, 800 assumed from typical e-commerce usage; actual subset may be narrower (e.g. 400/700 only)
- Shadow and elevation tokens not available — product cards may use drop-shadow rather than hairline border; verify on live site at multiple zoom levels
- Hover transition timing and easing curves (button fills, card lifts) not capturable from static extraction
- Mega-menu structure, product category taxonomy, and nav link labels not confirmed
- Mobile header height unverified; 64px is a desktop assumption
- Subscription plan UI structure (toggle, radio tabs, or stepped selector) not captured
- Photography art direction (lifestyle vs. product-flat vs. ingredient-macro) visible on live site but not encodable in this spec
- #008060, #049cff, #35ee7a present in extracted palette — likely Shopify admin artifacts or third-party widget colors, not brand tokens; excluded from spec pending verification
