---
version: alpha
name: "Erin Condren"
source_url: "https://www.erincondren.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The add-to-cart button, the coil binding printed in every product shot, and the "New" launch badge all run the same charged pink — a fuchsia anchored near #F04E88 that functions as the brand's single organizing voltage across every surface. Erin Condren sells the proposition that color is a productivity technology: planners ship in more than a dozen colorway families, and the site's cover customizer — a horizontally scrolling swatch strip — is often the first interactive moment a new visitor has with the brand, before they've finished reading the product description. This means the UI carries an unusually literal relationship to the physical product; the digital swatches are the same inks that will arrive in the customer's mailbox. Rounded corners appear everywhere — {rounded.md} on cards, {rounded.full} on badge pills and swatch selectors — echoing the coil apertures and tabbed page-edges that make the planners recognizable at arm's length. Background surfaces stay bright white (#FFFFFF) or a barely-there blush ({colors.surface-soft}), so product photography — always shot open at a 45-degree angle, weekly spread visible, stickers in mid-application — reads as editorial rather than catalogue. The type system is a clean geometric sans-serif at modest weights, deferring to color rather than scale for hierarchy: a planner-grid section label and an e-commerce category chip use the same family, differentiated by hue and size rather than typeface changes. A multi-color horizontal stripe — running through the logo mark and repeated as section dividers — makes the visual handoff between digital and physical feel inevitable rather than designed. The footer and PDP sidebar carry the same color-coded chip taxonomy used inside the planners themselves: color is not a cosmetic layer here, it is the information architecture.

colors:
  primary: "#F04E88"
  primary-active: "#D93878"
  primary-disabled: "#F9B8D5"
  accent-teal: "#34C1CE"
  accent-purple: "#9B6FD6"
  accent-coral: "#FF7B54"
  accent-yellow: "#FFD166"
  accent-green: "#6EC6A0"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#767676"
  hairline: "#E5E5E5"
  hairline-soft: "#F0F0F0"
  canvas: "#FFFFFF"
  surface-soft: "#FEF5F8"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  badge-new: "#F04E88"
  badge-sale: "#FF7B54"

typography:
  display-xl:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  button-md:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  badge-label:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "'Nunito Sans', 'Proxima Nova', -apple-system, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
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
    rounded: "{rounded.full}"
    padding: "12px 28px"
    height: 48px
    hoverBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: "10px 28px"
    height: 48px
    hoverBackgroundColor: "{colors.surface-soft}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 16px"
    hoverTextColor: "{colors.primary}"

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 40px
    subNavBackgroundColor: "{colors.canvas}"
    subNavShadow: "0 4px 12px rgba(0,0,0,0.08)"

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageBorderRadius: "{rounded.md}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.base}"
    shadow: "0 2px 8px rgba(0,0,0,0.06)"
    hoverShadow: "0 6px 20px rgba(0,0,0,0.10)"
    badgePosition: top-left

  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    minHeight: 520px
    accentBarHeight: 4px
    accentBarGradient: "linear-gradient(90deg, {colors.primary}, {colors.accent-coral}, {colors.accent-yellow}, {colors.accent-green}, {colors.accent-teal}, {colors.accent-purple})"

  rainbow-stripe:
    height: 4px
    gradient: "linear-gradient(90deg, {colors.primary}, {colors.accent-coral}, {colors.accent-yellow}, {colors.accent-green}, {colors.accent-teal}, {colors.accent-purple})"
    display: block
    width: 100%

  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "3px 10px"

  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.full}"
    padding: "3px 10px"

  customizer-swatch:
    width: 32px
    height: 32px
    rounded: "{rounded.full}"
    borderSelected: "3px solid {colors.ink}"
    borderUnselected: "2px solid transparent"
    hoverScale: 1.1

  swatch-strip:
    display: horizontal-scroll
    gap: "{spacing.sm}"
    paddingHorizontal: "{spacing.base}"
    scrollbarDisplay: none

  collection-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"

  planner-tab:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.sm}"
    padding: "8px 20px"
    borderBottom: "2px solid transparent"
    activeBorderBottom: "2px solid {colors.primary}"

  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    height: 44px
    padding: "0 16px"
    iconColor: "{colors.muted}"

  newsletter-signup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    inputBackgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.md}"
    paddingVertical: "{spacing.xxl}"
    paddingHorizontal: "{spacing.xl}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    captionTypography: "{typography.caption}"
    dividerColor: "rgba(255,255,255,0.12)"
    paddingVertical: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Full pill shape (`{rounded.full}`) in signature fuchsia (`{colors.primary}`), 48px tall with 28px horizontal padding. Darkens to `{colors.primary-active}` on hover/press; fades to `{colors.primary-disabled}` when disabled. White label text in bold 16px with 0.5px letter-spacing gives a slight print-adjacent feel. Appears on every primary CTA: "Shop Now," "Add to Cart," "Customize Your Cover."

**`button-secondary`** — White fill with a 2px fuchsia border and the same pill radius. Hover adds the lightest blush (`{colors.surface-soft}`) as a fill. Sits alongside `button-primary` in hero sections and PDP sidebars for secondary actions like "Save to Wishlist" or "View Size Guide."

**`button-ghost`** — Transparent background with ink-colored label; used for tertiary actions and navigation-embedded text links. Hover shifts the label to `{colors.primary}` without adding a border or fill, keeping the interaction signal minimal.

### Text Input

**`text-input`** — Hairline border (`{colors.hairline}`) on a white field; border transitions to `{colors.primary}` on focus with no outer glow, keeping form controls visually quiet against the colorful surrounding UI. Rounded at `{rounded.sm}` (8px) rather than the pill radii used on buttons — this shape distinction separates form controls from action elements at a glance. Placeholder in `{colors.muted}`.

### Navigation

**`nav-bar`** — White canvas, 64px tall, with a 1px bottom border and no resting shadow. Logo sits left-aligned at 40px height; right zone carries account, wishlist, and cart icon-buttons. Mega-menu panels on hover span the full viewport width with category imagery and product subcategories. The `rainbow-stripe` appears immediately below the nav bar on marketing pages, functioning as a brand fingerprint rather than a structural separator. Collapses to a hamburger drawer below 744px.

### Product Card

**`product-card`** — 12px radius white card with 16px internal padding and a whisper shadow (8px blur, 6% black) that lifts on hover. Title in `{typography.title-sm}`, price in `{typography.price-sm}`. Cover image fills the upper zone flush to the card edge; badge pills (`badge-new`, `badge-sale`) overlay the top-left corner. A `swatch-strip` optionally renders below the image for inline colorway browsing — making the cover customizer present on the listing page before the customer reaches the PDP.

### Hero Banner

**`hero-banner`** — Blush-tinted (`{colors.surface-soft}`) zone, minimum 520px tall, with generous vertical padding (`{spacing.section}`). Display headline in `{typography.display-xl}`; supporting copy in `{typography.body-md}`. A 4px rainbow gradient bar runs at the section's top or bottom edge, anchoring the seasonal color story. CTA pair — `button-primary` + `button-secondary` — sits below the body copy with 24px gap between them.

### Rainbow Stripe

**`rainbow-stripe`** — A 4px full-width gradient bar progressing from `{colors.primary}` through `{colors.accent-coral}`, `{colors.accent-yellow}`, `{colors.accent-green}`, `{colors.accent-teal}`, to `{colors.accent-purple}`. Applied as the top accent on hero sections, between major content zones, and as the footer's opening cap. This is the most immediate brand signal in the digital system — it maps directly to the rainbow coil motif on the physical planner and requires no text to communicate brand identity.

### Badges

**`badge-new`** — Pill chip in `{colors.badge-new}` (primary fuchsia) with white uppercase label in `{typography.badge-label}` (11px/700, tracked at 0.5px). **`badge-sale`** — Identical pill shape in `{colors.badge-sale}` (coral). Both overlay product card images at the top-left with 3px vertical / 10px horizontal padding. Used only for genuine launches and price reductions — sparing use preserves signal strength across a catalog with many colorways.

### Customizer Swatch

**`customizer-swatch`** — 32px circle at `{rounded.full}`, showing a cover colorway fill. Selected state gains a 3px `{colors.ink}` ring offset by a 2px transparent gap from the circle edge. Unselected swatches carry a 2px transparent border to maintain consistent spacing. Hover scales to 1.1×. Rendered inside `swatch-strip`: a horizontally scrollable row at all breakpoints, 8px gap, no visible scrollbar. This interaction is Erin Condren's most brand-specific UX moment — it mirrors the physical act of choosing a planner cover before committing to purchase.

### Collection Chip

**`collection-chip`** — Pill-shaped filter tag in `{colors.surface-soft}` with body-colored label in `{typography.button-sm}`. Active state flips to `{colors.primary}` background with white text. Used on collection landing pages to filter by format (Daily, Weekly, Monthly), cover style, and size. These chips replicate the color-coded section tab logic from inside the planners themselves, making the e-commerce taxonomy feel native to the product.

### Planner Tab

**`planner-tab`** — Used within PDP and collection pages to switch between planner layout views (Horizontal Weekly, Vertical Weekly, Monthly). Inactive tabs show muted text on white; active tab uses `{colors.primary}` fill with white text and an underline accent. Rounded at `{rounded.sm}` to maintain the softer geometry consistent with the rest of the system.

### Newsletter Signup

**`newsletter-signup`** — Blush-tinted module (`{colors.surface-soft}`) with 12px radius container and 48px vertical padding. Display headline in `{typography.display-md}`; body copy in `{typography.body-md}`. Single email input with `button-primary` inline on desktop, stacked on mobile. Typically appears between collection rows on the homepage as a soft interrupt without a modal or overlay.

### Footer

**`footer`** — Dark (`{colors.ink}`) background providing the only high-contrast zone on an otherwise light site, making it a strong visual anchor. Topped by the `rainbow-stripe` cap. Navigation columns in `{typography.body-sm}`, link hover in white. Dividers at 12% white opacity. Social icon row and legal text at base in `{typography.caption}`. The dark-on-light reversal here is abrupt by design — it signals a full stop after the colorful product experience above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hamburger nav drawer; swatch-strip stays horizontal-scroll; hero stacks text above image; product grid 2-up |
| Tablet | 744–1128px | 2–3 column product grid; nav retains horizontal links but drops mega-menu to simplified dropdowns; hero goes side-by-side |
| Desktop | 1128–1440px | 4-column product grid; full mega-menu panels; hero gains 80px horizontal padding; rainbow-stripe and badge overlays fully visible |
| Wide | > 1440px | Content capped at ~1440px max-width; hero and section padding increase to maintain reading measure; grid stays 4-up |

### Touch Targets

- All buttons minimum 48px tall; pill radius adds perceived tap width without explicit padding increase
- Swatch circles are 32px × 32px with 8px gap — dense but tappable; selected-state ring aids identification without requiring label text
- Nav links minimum 44px tap height inside the mobile drawer
- Collection chips 36px tall on mobile, collapsing to a horizontal scroll row when they overflow the viewport

### Collapsing Strategy

- Top nav collapses to hamburger drawer at 744px; category mega-menus become nested accordion sections inside the drawer
- Swatch strip remains horizontal-scroll at all breakpoints; never wraps to a grid (preserving the tactile customizer feel)
- Hero content stacks vertically below 744px; image moves above copy to lead with product imagery
- Product card grid: 4-up → 3-up → 2-up as viewport narrows; single-up only in narrow modal or drawer contexts
- Footer columns collapse from 4-column → 2-column at tablet, single column with accordion sections on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted** — erincondren.com appears to load design tokens via JavaScript or is behind anti-bot protection at time of extraction; zero hex values were captured. All colors in this file are inferred from widely-available brand imagery and marketing materials, not live site data. Treat as best-guess approximations; validate against live computed styles before production use.
- **Primary hex unconfirmed** — The fuchsia (#F04E88) is derived from brand imagery and packaging; the true production hex may differ by several lightness or saturation points.
- **No fonts extracted** — The Nunito Sans / Proxima Nova fallback stack is inferred from visual inspection of brand assets. The site almost certainly loads a licensed or custom typeface; confirm exact font name, weights, and loading strategy by inspecting network requests on the live site.
- **Accent palette hex values unconfirmed** — The brand uses 5–6 recurring accent hues; the precise production hex for each (teal, purple, coral, yellow, green) is unverified. Gradient stop order in `rainbow-stripe` matches commonly published brand assets but should be confirmed.
- **Custom illustration and icon set not captured** — Erin Condren uses illustrated icons, sticker-motif graphics, and seasonal spot illustrations throughout. No icon sizing or stroke-weight tokens are defined here.
- **Animation and transition tokens absent** — Cover-flip animations, swatch hover transitions, and the customizer scroll behavior are brand-signature micro-interactions; no duration, easing, or spring tokens were extractable.
- **Dark mode** — No dark-mode variant observed in brand materials; assumed light-only unless confirmed otherwise.
