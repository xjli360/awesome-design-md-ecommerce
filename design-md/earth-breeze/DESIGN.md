---
version: alpha
name: "Earth Breeze"
source_url: "https://earthbreeze.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The first signal that Earth Breeze isn't a conventional detergent brand is its canvas: #fffef9, not clinical white but a warm, faintly creamy ground that suggests afternoon light through unbleached linen. Against that surface, two pastel tones share equal billing as co-accent hues — powder blue (#aec9e3) and rose blush (#e0a6bc) — a pairing more likely on a botanical-print candle than a cleaning-product shelf, and the central design argument that household essentials can feel like a wellness purchase. Deep navy (#113988) anchors every primary CTA and trust-building surface, the one hard-contrast element in an otherwise unhurried palette; a brighter sky tone (#74d1f6) flickers through illustrations and lifestyle imagery, while dusty mauve (#d6c1c8) wraps certification badges and secondary labels. BRSonoma, a contemporary geometric-humanist sans-serif, carries all type at weights that read as confident without urgency — display heads sit at 500–600, not the heavy 700+ common in discount-driven e-commerce, and body copy runs at 400 in generous 1.55–1.6 line-heights that make eco-certification copy feel readable rather than obligatory. Earth Breeze's core product — flat laundry sheets shipped in a slim paperboard sleeve — shapes the UI rhythm: layouts are unhurried, cards use soft rounding ({rounded.md}), and whitespace is treated as breathing room rather than waste. Certification claims — plastic-free, B Corp, carbon-neutral — appear throughout the page in cloud-blue or petal-toned chips ({colors.cloud}, {colors.petal}), with all-caps 11px labels at wide tracking, signaling credentials without overwhelming the purchase moment. Scent and variant selectors use a pill format ({rounded.full}) in surface-soft, shifting to navy fill on selection. Subscription-first positioning surfaces toggle components near the add-to-cart module, reflecting a revenue model that prizes repeat commitment over one-time volume.

colors:
  primary: "#113988"
  primary-active: "#0c2a6b"
  primary-disabled: "#8aaad4"
  ink: "#121212"
  body: "#2b2b2b"
  muted: "#6b6b6b"
  hairline: "#dedede"
  canvas: "#fffef9"
  surface-soft: "#eef3f8"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  cloud: "#aec9e3"
  sky: "#74d1f6"
  mid-blue: "#94c6e8"
  bloom: "#e0a6bc"
  petal: "#d6c1c8"

typography:
  display-xl:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 52px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  badge-label:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.35px
    textTransform: uppercase
  button-md:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  stat-display:
    fontFamily: "'BRSonoma', system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px

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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
    ctaComponent: button-primary
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageBorderRadius: "{rounded.md}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.title-sm}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    subheadColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xl}"
    maxWidth: 640px
    ctaComponent: button-primary
  eco-badge:
    backgroundColor: "{colors.cloud}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "5px 12px"
  trust-badge:
    backgroundColor: "{colors.petal}"
    textColor: "{colors.primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "5px 12px"
  certification-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.md} {spacing.lg}"
    rounded: "{rounded.sm}"
    iconSize: 20px
    gap: "{spacing.lg}"
    display: flex
    alignItems: center
  impact-counter:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.stat-display}"
    labelTypography: "{typography.caption}"
    padding: "{spacing.xxl} {spacing.section}"
    rounded: "{rounded.none}"
    gap: "{spacing.xl}"
  variant-selector:
    backgroundColor: "{colors.surface-soft}"
    selectedBackgroundColor: "{colors.cloud}"
    textColor: "{colors.ink}"
    selectedTextColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1.5px solid {colors.primary}"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    activeBackgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.sm} {spacing.base}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1.5px solid {colors.primary}"
  quantity-stepper:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    buttonSize: 36px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.cloud}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"
    linkHoverColor: "{colors.sky}"

## Components

### Buttons

**`button-primary`** — A fully pill-shaped (`{rounded.full}`) navy button (#113988) at 48px height, carrying the brand's only high-contrast CTA moment. On hover it deepens to #0c2a6b; the disabled state fades to #8aaad4 at 60% opacity, keeping the blue family consistent rather than switching to gray. Text runs in BRSonoma 600 at 15px with slight 0.1px letter-spacing to counter the optical compression of all-caps pill shapes.

**`button-secondary`** — Same pill geometry, but inverted: warm-white canvas fill with a 1.5px navy border and navy label. Used for secondary actions adjacent to the primary CTA — "Learn More" or "View Ingredients" alongside "Add to Cart". On hover, the border intensifies and a subtle cloud-blue (#aec9e3) wash replaces the canvas fill.

**`button-ghost`** — Transparent background, ink-colored label, pill rounding, no border. Used for low-priority navigation links — "See All Reviews", "Read Our Story" — where adding a border would crowd the layout.

### Text Input

**`text-input`** — 48px tall, 8px rounding (`{rounded.sm}`), hairline (#dedede) border at rest. On focus, border weight steps up to 1.5px and shifts to primary navy, giving feedback without a color surprise. Placeholder text runs in muted (#6b6b6b). Used for email capture in subscription flows and site search, never with a visible label above — placeholder text carries the label role.

### Navigation

**`nav-bar`** — Sits on the warm canvas (#fffef9) with a single hairline separator at the bottom. Wordmark anchors the left; a cart icon and the primary pill CTA anchor the right. Links use BRSonoma 500 at 15px — below the threshold that reads as bold — so the CTA button remains the dominant call to action. A persistent announcement bar above the nav carries promotional copy in white on navy at 12px/center-aligned.

### Product Card

**`product-card`** — White card on the warm canvas, 12px rounding (`{rounded.md}`), 1px hairline border, and 16px internal padding. The product image uses the same 12px radius and fills the full card width. Title runs in BRSonoma 600 at 18px; price in 500 at 15px; a short descriptor below in body-sm muted. Eco and trust badges stack below the descriptor using the `eco-badge` or `trust-badge` component at 5px vertical gap.

### Hero

**`hero-section`** — Full-width canvas background, copy-left / image-right split at desktop, stacking to copy-top at mobile. Headline sits at 52px/600 weight, sub-head at 16px/400 in body (#2b2b2b) with 1.6 line-height — enough room for a two-line sustainability claim. The primary pill CTA follows directly below. No decorative border, no pattern overlay; whitespace and the off-white ground carry the premium cue.

### Badges and Certifications

**`eco-badge`** — Cloud-blue (#aec9e3) fill, navy text, full-pill rounding, 11px all-caps at 0.35px tracking. Used inline with product copy for "Plastic-Free", "Hypoallergenic", and similar short claims. **`trust-badge`** — Same geometry in dusty petal (#d6c1c8) fill, for third-party credentials like "B Corp" or "1% for the Planet". The two badge types never appear in the same color on the same line, creating a visual hierarchy between product claims and external certifications.

**`certification-strip`** — A soft surface-soft (#eef3f8) band spanning the full content width, housing a horizontal row of 20px icons with caption-weight labels. Typically placed between hero and product section to front-load trust before the purchase decision. Rounded at 8px (`{rounded.sm}`), padded generously, never more than five icons wide on desktop.

### Impact Counter

**`impact-counter`** — Full-width navy band (#113988), white text. Large stat numbers use `stat-display` typography (44px/700) with labels in caption below. Designed to interrupt the warm-canvas scroll with a moment of social proof — "X plastic bottles saved", "Y loads cleaned". No rounding; the hard edge reinforces the factual, not decorative, intent of the data.

### Variant and Subscription Selectors

**`variant-selector`** — Pill-shaped chips in surface-soft (#eef3f8) for unselected, shifting to cloud-blue (#aec9e3) fill and 1.5px navy border on selection. Used for scent variants ("Fresh Scent", "Fragrance-Free") and sheet count options. **`subscription-toggle`** — Two-state toggle between "One-time" and "Subscribe & Save", same pill/card geometry. The active state fills navy with white text; the inactive state remains surface-soft with a hairline border. The save-percentage callout sits as a caption tag to the right of the active label.

### Quantity Stepper

**`quantity-stepper`** — Minus / number / plus arranged in a pill-contained row. The outer wrapper uses `{rounded.full}` with a hairline border; minus and plus icons are 36×36px touch targets on either side of the numeric display in title-sm weight. Increment steps by 1; no animated transitions — the count updates in place.

### Footer

**`footer`** — Near-black (#121212) background for a clean terminus to the warm-canvas page. Section headings in BRSonoma 500/white; links in body-sm weight, cloud blue (#aec9e3) at rest, brightening to sky (#74d1f6) on hover. Social icons align left in a dedicated row. The color shift from warm off-white to near-black is the brand's version of a hard rule — it signals "page is done" rather than fading to a soft gray.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout. Hero stacks copy above image. Nav collapses to hamburger menu on left, cart icon on right. Product cards span full width. Certification strip scrolls horizontally. Impact counter stacks stats vertically. Announcement bar wraps to two lines if needed. |
| Tablet | 744–1128px | Two-column grid for product cards. Hero shifts to 60/40 copy-left / image-right split. Nav links remain visible; hamburger suppressed. Certification strip fits 4 icons without scroll. |
| Desktop | 1128–1440px | Three-column product grid. Hero max-width 640px for copy column; image fills remainder. Full nav with all links visible and primary CTA button in top-right. Impact counter shows stats in a single horizontal row. |
| Wide | > 1440px | Content max-width caps at 1440px with symmetric horizontal padding; canvas background bleeds to edges. No layout changes beyond the cap. |

### Touch Targets

- All interactive chips (variant-selector, subscription-toggle) minimum 44px tall on mobile via increased vertical padding
- Quantity stepper buttons expand to 44×44px on mobile
- Nav hamburger icon target 44×44px
- Primary and secondary buttons remain at 48px height across all breakpoints

### Collapsing Strategy

- Announcement bar is the first element to shrink font to 11px on small mobile (< 375px) before wrapping
- Certification strip collapses from 5-icon horizontal row → 4-icon → horizontal scroll on mobile rather than vertical stack, to avoid height penalty in the trust section
- Hero copy stacks above product image on mobile; image aspect ratio clips to 4:3 rather than showing full portrait
- Footer four-column link grid collapses to two columns at tablet and single accordion-expandable sections at mobile
- Impact counter stats reflow from four-across to two-by-two grid at tablet and single column at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was extracted; the mobile browser chrome color is unknown — likely defaults to the nav-bar canvas (#fffef9) but unconfirmed
- Surface-soft (#eef3f8) is a derived light tint of the extracted blue palette, not a directly extracted value; the exact brand token may differ
- Font weights for BRSonoma in use on the live site were not confirmed — the scale (400/500/600/700) is inferred from BRSonoma's known variable-font range and common DTC conventions
- Exact button border-radius values were not measured from computed styles; `{rounded.full}` (pill) is inferred from the brand's visual softness rather than pixel extraction
- Hover and focus state colors were not extracted; active-state darkenings (#0c2a6b from #113988) are derived by standard 10% HSL darkening
- Animation/transition timings (button hover, selector state change) were not captured — no motion tokens defined
- Dark-mode or alternate-theme behavior unknown; no `prefers-color-scheme` variants documented
- Exact nav-bar height (64px) is an estimate; computed height from live DOM was not measured
