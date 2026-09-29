---
version: alpha
name: "Rowenta"
source_url: "https://www.rowentausa.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Oxanium in the hero masthead — a geometric display face more at home on esports scoreboards and aerospace instrument panels than small-appliance retail — signals Rowenta's design intent before the first product photograph loads: precision expressed as a visual register, not a marketing claim. That typeface choice anchors a palette built on a specific saturated azure (#2768b1) that reads neither corporate-generic nor tech-startup; it sits in the middle register of confidence, recalling the blue of German precision-engineering brands without the heaviness of navy. The primary azure carries CTAs, category tabs, active states, and link-hover cues; a darker cousin (#34679f) deepens on press; a mid-tone sibling (#4480c2) handles disabled states without disappearing into the canvas.

  Red (#eb322f) enters as a narrowly deployed interrupt. Sale badges, urgency labels, and promotional announcement strips use it — never a primary navigation or CTA color. The pairing creates a legible two-channel signal: blue means confirm and navigate, red means act now on value. Soft pink (#f48e8c) surfaces only in tinted promotional backgrounds where the accent needs to breathe rather than alarm.

  The most unexpected register on the site is a warm amber-to-cream zone built from #fdf0d5, #c07600, and #f5f0e8. These honey-warm tones appear selectively in lifestyle editorial modules and premium product callouts, pulling against the cool engineering palette and implying a secondary brand voice: the appliances live inside warm domestic interiors — wood counters, natural light — not sterile white studios. The contrast is architecturally considered. Product cards sit on a near-white surface (#f6f6f6) framed by hairline borders (#e8e8e8), with `{rounded.sm}` corners that soften without rounding away the precision feel. Open Sans covers body copy, form labels, and UI text — neutral and legible — keeping Oxanium reserved for headline moments so its technical register accumulates force from scarcity. Navigation runs a two-tier system: a white top bar for account, search, and cart, with a secondary category strip in `{colors.surface-soft}` that scrolls horizontally at narrower breakpoints.

colors:
  primary: "#2768b1"
  primary-dark: "#34679f"
  primary-active: "#1979c3"
  primary-disabled: "#4480c2"
  accent: "#eb322f"
  accent-soft: "#f48e8c"
  ink: "#111111"
  body: "#333f48"
  muted: "#7d7d7d"
  muted-soft: "#adadad"
  steel: "#5b6770"
  hairline: "#e8e8e8"
  hairline-soft: "#e3e3e3"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#f5f5f5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  nav-dark: "#242f3a"
  body-dark: "#222222"
  warm-surface: "#f5f0e8"
  warm-cream: "#fdf0d5"
  warm-amber: "#c07600"
  warm-brown: "#6f4400"
  teal: "#00699d"

typography:
  display-xl:
    fontFamily: "'Oxanium', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Oxanium', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Oxanium', 'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  eyebrow:
    fontFamily: "'Oxanium', 'Open Sans', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.8px
    textTransform: uppercase
  price:
    fontFamily: "'Open Sans', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
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
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.primary}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-dark}"
    border: "1px solid {colors.primary-dark}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.on-dark}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    height: 44px
    padding: 10px 14px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    height: 44px
    padding: 10px 16px
    iconColor: "{colors.steel}"
    iconRight: true
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-utility-strip:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
  nav-category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.nav-link}"
    height: 44px
    borderBottom: "1px solid {colors.hairline}"
    activeColor: "{colors.primary}"
    activeBorder: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.10)"
    hoverBorderColor: "{colors.primary-disabled}"
  product-card-badge:
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  product-card-feature-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.steel}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline-soft}"
  star-rating:
    filledColor: "{colors.warm-amber}"
    emptyColor: "{colors.hairline}"
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.accent}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 520px
    contentMaxWidth: 560px
    contentPadding: "{spacing.section}"
  hero-banner-warm:
    backgroundColor: "{colors.warm-cream}"
    textColor: "{colors.warm-brown}"
    eyebrowColor: "{colors.warm-amber}"
    eyebrowTypography: "{typography.eyebrow}"
    headlineTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    accentColor: "{colors.warm-amber}"
    minHeight: 400px
    contentPadding: "{spacing.xl}"
  promo-announcement-bar:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    textAlign: center
  promo-announcement-bar-blue:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    textAlign: center
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    hoverBorder: "1px solid {colors.primary}"
    hoverTextColor: "{colors.primary}"
    padding: "{spacing.base}"
    imageSize: 80px
  tech-feature-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    labelTypography: "{typography.title-sm}"
    captionTypography: "{typography.caption}"
    iconColor: "{colors.primary}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} 0"
    columns: 4
  accordion-faq:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    triggerTypography: "{typography.title-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    activeBorderColor: "{colors.primary}"
    iconColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.nav-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    headlineTypography: "{typography.eyebrow}"
    linkTypography: "{typography.body-sm}"
    borderTop: "3px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The main conversion button: Rowenta's brand azure (#2768b1) fill with white uppercase Open Sans label at 14px/700 weight and 0.6px letter-spacing. `{rounded.xs}` (4px) keeps corners present but minimal, reinforcing the precision-engineering register. Hover darkens to #34679f; active shifts to #1979c3; disabled drops to #4480c2 at 60% opacity.

**`button-secondary`** — White canvas fill with a 1px #2768b1 border and matching azure text. Paired with `button-primary` in hero and product-detail layouts as the "learn more / compare" path. Hover fills surface-soft (#f6f6f6) and darkens both border and label to `{colors.primary-dark}`.

**`button-ghost`** — Transparent fill, white border and label, used exclusively on dark hero panels and the `nav-utility-strip`. Signals secondary action on dark grounds without introducing a new fill color.

**`button-accent`** — Solid #eb322f fill for high-urgency promotional moments: flash-sale CTAs, limited-stock alerts. Kept out of standard navigation flows so the red channel retains its urgency signal.

### Navigation

**`nav-utility-strip`** — A 36px-tall dark bar (#242f3a) at page top carrying shipping thresholds, store-locator links, and account utilities in 12px caption type on white. Sets a premium framing layer above the main nav.

**`nav-bar`** — White, 60px tall, with a hairline bottom border (#e8e8e8). Logo anchors left in `{colors.primary}` blue. Search input and cart/account icons anchor right. Sticky on scroll.

**`nav-category-strip`** — 44px surface-soft bar below the main nav with horizontally scrolling category tabs. Active tab gets a 2px bottom border in `{colors.primary}` and blue text; inactive tabs render in `{colors.body}`.

### Product Card

**`product-card`** — White rectangle, 1px hairline border, `{rounded.sm}`, with a surface-soft image well occupying the upper ~60% of the card. Product name in `{typography.title-sm}`, price in `{typography.price}` (20px/700), star rating row using `{colors.warm-amber}` filled stars and `{colors.muted}` review-count caption. A subtle box-shadow on hover and optional `{colors.primary-disabled}` border tint signal interactivity without animation weight.

**`product-card-badge`** — Absolute-positioned top-left, `{colors.accent}` fill, white badge typography at 11px uppercase. Used for SALE, NEW, and REFURB labels. One badge per card maximum.

**`product-card-feature-badge`** — Inline chip below the product name: surface-soft fill, hairline border, steel text at 11px uppercase. Labels technology tiers like "Steam Technology" or "EcoFlow System" without competing with the price or rating.

### Hero

**`hero-banner`** — Full-width dark panel (#242f3a) with left-aligned content column. Eyebrow line in Oxanium uppercase at 11px with 1.8px tracking in `{colors.accent}` red sets category context. Headline in `{typography.display-xl}` (Oxanium 48px/700) in white. Subhead in `{typography.body-md}` Open Sans. CTA row pairs `button-primary` and `button-ghost`. Right half of the panel holds product photography bleeding to the edge.

**`hero-banner-warm`** — An alternate editorial hero for lifestyle/gifting modules: warm-cream (#fdf0d5) background, warm-brown (#6f4400) text, amber (#c07600) accent. Uses `{typography.display-md}` (Oxanium 32px) at reduced scale. Signals the domestic warmth register distinct from the engineering-blue system hero.

### Promotional & Utility

**`promo-announcement-bar`** — Full-width 40px strip pinned above the utility nav. Accent red (#eb322f) variant for urgency messaging; primary blue variant for standard promotions (free shipping, new arrivals). Center-aligned 14px Open Sans body-sm.

**`tech-feature-strip`** — A four-column icon-and-label band spanning the full content width below hero or product detail sections. Each column: a 32px icon in `{colors.primary}` blue, a bold title in `{typography.title-sm}`, and a descriptor in `{typography.caption}`. Top border in `{colors.hairline}` separates it from the preceding section without a full background band.

**`star-rating`** — Five stars using SVG fills: `{colors.warm-amber}` (#c07600) for filled, `{colors.hairline}` for empty. Review count and average score rendered in 12px `{typography.caption}` in `{colors.muted}`.

**`accordion-faq`** — Single-border cards with `{rounded.xs}` corners. Trigger row in `{typography.title-sm}` with a `{colors.primary}` chevron icon. Expanded body in `{typography.body-md}`. Active accordion item gains a `{colors.primary}` left border accent.

### Footer

**`footer`** — Dark ground (#242f3a) with a 3px `{colors.primary}` top border as the sole accent. Column headlines in Oxanium eyebrow caps (11px/600, 1.8px tracking) in white. Link lists in 14px Open Sans body-sm at `{colors.muted-soft}`, hovering to white. Bottom row carries copyright, legal links in muted-soft, and social icon row.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart; category strip hides behind "Shop" dropdown; hero headline drops to `display-sm` (Oxanium 22px); tech-feature-strip collapses to 2 columns |
| Tablet | 744–1128px | Two-column product grid; nav-category-strip horizontal-scrolls; hero content column occupies 55% width; tech-feature-strip runs 2×2 |
| Desktop | 1128–1440px | Three-column product grid; full horizontal category strip visible; hero at full 520px height with edge-bleed product photography; tech-feature-strip 4 columns |
| Wide | > 1440px | Content max-width 1440px centered; hero background extends full-bleed; four-column product grid in catalog views |

### Touch Targets

- All interactive buttons maintain minimum 44px height on mobile
- Category tab strip items: minimum 44px height with 16px horizontal padding
- Product card touch area spans the full card including image well
- Accordion triggers: full-row touch target, minimum 48px height on mobile
- Nav icons (search, cart, account): minimum 44×44px tap zones

### Collapsing Strategy

- Top nav collapses to hamburger menu at < 744px; utility strip hides entirely
- Category strip at tablet degrades to horizontal scroll with visible overflow indicator
- Hero banner at mobile stacks to text-above, image-below at full bleed; warm editorial hero hides lifestyle imagery on mobile to preserve text legibility
- Tech-feature-strip reflows 4→2→1 columns at tablet→mobile breakpoints
- Footer column grid collapses from 4 columns to 2 (tablet) to 1 (mobile) with accordion disclosure for link lists on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` tag detected; PWA/install accent color unconfirmed
- Oxanium usage scope uncertain — may be limited to logo/wordmark or select headline instances rather than a full display type system; verify by inspecting hero heading computed styles
- Exact border-radius values not confirmed via computed CSS; `{rounded.xs}` (4px) is an inference from the precision-engineering aesthetic — could be `{rounded.none}` (0px) for a harder industrial look
- Custom icon fonts (`magento-icons`, `meigee-icons`) detected in font stacks; individual glyph-to-semantic mapping not available
- Hover and transition timing values (duration, easing) not extracted
- Mobile-specific type scale reductions not confirmed; display-xl may drop more aggressively than estimated
- Premium/Steam Pro product line color differentiation (if any) not confirmed from extracted palette
- Grid column gutters and max content widths not extracted from computed layout
- Warm amber/cream palette zone (#fdf0d5, #c07600) usage frequency and placement rules inferred from palette extraction; exact editorial module inventory unknown
- Dark navy (#242f3a vs #333f48) usage boundary between nav-dark and body-dark contexts not confirmed
