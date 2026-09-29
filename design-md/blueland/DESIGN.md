---
version: alpha
name: "Blueland"
source_url: "https://www.blueland.com"
captured_at: "2026-09-28T04:10:46.349163+00:00"
evidence_status: "historical_partial_css_evidence"
description: |-
  Every product page at Blueland opens with a color-coded argument — lemon yellow (#fffcbb) for citrus, pale mint (#c8faa1) for eucalyptus, soft lavender (#fce5ff) for fresh linen — a candy-counter display that reframes cleaning as sensory selection rather than household obligation. The structural anchor is deep cobalt #133cd1, an almost inkwell blue that carries every primary CTA, nav active state, and brand wordmark, sitting against a cool sky canvas (#f0f7ff and #ffffff) that keeps the system feeling clean without reading clinical. Dark navy (#000175) provides typographic weight for headlines and key UI text, while the stepped blue family — #001589, #0033a7, #133cd1, #2d56d2, #587bda — creates monochromatic depth that allows the pastel product colors to read as signal rather than decoration. Type runs GT-Pressura at display scale, a geometric grotesque with slightly compressed tracking that gives headlines an assured, modern solidity; Sailec handles body and UI copy, offering neutral legibility that keeps product descriptions readable without visual noise. Corner radii skew friendly: primary buttons are full pills ({rounded.full}), scent-selector chips match that pill shape, while product cards sit at a gentler {rounded.md} that softens the grid without fully dissolving it. The eco-impact band — a full-bleed cobalt section counting plastic bottles saved and CO₂ offset — appears at page transitions, translating environmental credentials into motion-driven numerics rather than copy-heavy callouts. Subscription toggle placement directly beside the add-to-cart button reflects the refill business model's centrality; the UI never lets a one-time purchaser forget that a cadence option exists. Starter kit bundles carry a distinct card treatment with included-items iconography, reinforcing the onboarding path for new customers and the brand's argument that switching cleaning systems is a single, discrete decision.

colors:
  primary: "#133cd1"
  primary-active: "#000175"
  primary-disabled: "#b8caef"
  primary-dark: "#001589"
  primary-mid: "#2d56d2"
  primary-light: "#587bda"
  ink: "#000175"
  body: "#0033a7"
  muted: "#9ca3af"
  hairline: "#e5e7eb"
  hairline-soft: "#e3eafd"
  canvas: "#ffffff"
  surface-soft: "#f0f7ff"
  surface-card: "#f4f8fe"
  surface-blue-pale: "#deeaff"
  on-primary: "#ffffff"
  accent-yellow: "#fffcbb"
  accent-green: "#c8faa1"
  accent-lavender: "#fce5ff"
  accent-peach: "#fff2dd"
  accent-mint: "#f3fff8"
  accent-blush: "#fff6f1"
  accent-rose: "#f7ebeb"
  accent-sky: "#a0ddff"
  error: "#ce4947"

typography:
  display-xl:
    fontFamily: "'GT-Pressura', 'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT-Pressura', 'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT-Pressura', 'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'GT-Pressura', 'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.1px
  title-md:
    fontFamily: "'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  label-sm:
    fontFamily: "'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'GT-Pressura', 'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'GT-Pressura', 'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  price-display:
    fontFamily: "'GT-Pressura', 'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  impact-counter:
    fontFamily: "'GT-Pressura', 'Sailec', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px

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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    textColor: "{colors.ink}"
    subtextColor: "{colors.muted}"
    bodyTypography: "{typography.body-sm}"
  scent-chip:
    height: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderSelected: "2px solid {colors.primary}"
    padding: 4px 12px
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderSelected: "3px solid {colors.ink}"
    borderUnselected: "1px solid {colors.hairline}"
  eco-badge:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.primary-active}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  refill-badge:
    backgroundColor: "{colors.surface-blue-pale}"
    textColor: "{colors.primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  impact-stat-band:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    counterTypography: "{typography.impact-counter}"
    labelTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
    rounded: "{rounded.none}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.full}"
    minHeight: 560px
    rounded: "{rounded.none}"
  subscription-toggle:
    backgroundColor: "{colors.surface-soft}"
    activeColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    inactiveTextColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.lg}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} {spacing.base}"
  starter-kit-card:
    backgroundColor: "{colors.canvas}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
    titleTypography: "{typography.display-sm}"
    titleColor: "{colors.ink}"
    itemIconColor: "{colors.primary}"
    itemTypography: "{typography.body-sm}"
    savingsBadgeBackground: "{colors.accent-green}"
    savingsBadgeTextColor: "{colors.primary-active}"
  scent-variant-card:
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.surface-blue-pale}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons

**`button-primary`** — Full pill-shaped button (#133cd1 background, white text, `{rounded.full}`, 48px tall) used for primary CTAs: "Add to Cart," "Shop Now," "Start Your Kit." On hover the background deepens to `{colors.primary-active}` (#000175); the disabled state uses `{colors.primary-disabled}` (#b8caef) at reduced opacity. The pill form is held at all viewport widths and never collapses to a square or rectangle variant.

**`button-secondary`** — White canvas with a 2px cobalt (#133cd1) border and matching text, identical pill radius. Used for secondary actions such as "Learn More," "Compare Bundles," or "View All Products." Hover shifts border and text to `{colors.primary-active}`.

**`button-ghost`** — Transparent background with `{colors.ink}` text, pill shape, no border. Reserved for use inside colored banners and overlay surfaces where a filled button would create too much visual mass. Relies entirely on surrounding context for boundary definition.

### Inputs

**`text-input`** — White field with 1px `{colors.hairline}` border at rest and a 2px cobalt focus ring, `{rounded.md}` (12px) corners. Placeholder text renders in `{colors.muted}`. Used in email-capture modules, promo code fields, and newsletter sign-up bars at the footer top.

### Navigation

**`nav-bar`** — White bar, 72px tall, 1px hairline bottom border. The Blueland wordmark appears in `{colors.primary}` cobalt at the left. Center holds product-category links in `{typography.nav-link}` weight-500 Sailec. Right side carries a cart icon with a cobalt fill count badge (white numeral) and a hamburger menu button on mobile. On scroll, a subtle drop-shadow appears beneath the bar without changing the white background.

### Product Components

**`product-card`** — Pale blue card (`{colors.surface-card}`) at `{rounded.md}`, 12px radius. Product image sits on a `{colors.surface-soft}` image field. Product name renders in `{typography.title-sm}`, one-time price in `{typography.price-display}`, subscribe-and-save price below in `{typography.body-sm}` and `{colors.muted}`. A scent-category color chip pulled from the accent family (accent-yellow, accent-green, accent-lavender, etc.) appears in the card's upper corner as a visual differentiator across the grid.

**`scent-chip`** — Pill-shaped fragrance-selector with transparent fill and a 2px border (transparent when idle, cobalt when selected). Text label in `{typography.body-sm}`. Arranged in a horizontal row beneath the product title on PDPs; on mobile the row becomes a single-line horizontal scroll track.

**`color-swatch`** — 24px circular swatch button tinted to the product variant's accent color. Selected state shows a 3px `{colors.ink}` border; unselected shows a 1px `{colors.hairline}`. Tapping a swatch updates the card background color, image, and the scent-chip row simultaneously.

**`subscription-toggle`** — Two-segment control ("One-time" / "Subscribe & Save") rendered in a pale blue `{colors.surface-soft}` container at `{rounded.lg}`. The active segment slides a cobalt fill pill with white text beneath it. Placed directly above the primary CTA on every PDP; it is never hidden or moved below the fold. Subscription price appears at a discount relative to one-time, formatted in `{typography.price-display}`.

### Badges & Labels

**`eco-badge`** — Pale green pill (`{colors.accent-green}`) with dark navy text in `{typography.label-sm}` uppercase. Used for "Plastic-Free," "Refillable," and certification callouts (EPA Safer Choice, B-Corp, etc.) on product cards and PDPs.

**`refill-badge`** — Pale blue pill (`{colors.surface-blue-pale}`) with cobalt text, same label-sm uppercase treatment. Used for "Refill Available" and "Works with Starter Kit" callouts to reinforce system compatibility at a glance.

### Marketing Sections

**`hero-banner`** — Full-width section, minimum 560px tall, `{colors.surface-soft}` background. Headline in `{typography.display-xl}` at `{colors.ink}`, subhead in `{typography.body-md}` at `{colors.body}`. CTA uses cobalt fill, white text, pill radius. Photography shows products floating or resting on clean domestic surfaces against white or pale backgrounds. On desktop the layout splits 60/40 text-to-image; on mobile the image stacks above text.

**`impact-stat-band`** — Full-bleed cobalt section (`{colors.primary}`) with no corner radius. Displays three or four statistics: plastic bottles diverted, CO₂ offset, orders shipped, tablets sold. Each stat renders in `{typography.impact-counter}` (white, 48px, −1px tracking) with a short descriptor below in `{typography.body-sm}` white. Numbers animate via count-up on viewport entry; layout is four-column on desktop, two-by-two on tablet, stacked on mobile.

**`starter-kit-card`** — White card with a 2px cobalt border at `{rounded.md}`, generous internal padding from `{spacing.xl}`. Headline in `{typography.display-sm}`, a bulleted list of included tablet types with cobalt checkmark icons in `{typography.body-sm}`, a savings badge in `{colors.accent-green}`, and a full-width primary CTA at the base. This is the primary conversion surface for first-time customers and appears as a sticky recommendation module on the homepage.

**`scent-variant-card`** — Small card whose background is set to one of the accent colors (accent-yellow, accent-green, accent-lavender, accent-peach) corresponding to the product's scent profile. Title in `{typography.title-sm}`, `{colors.ink}`. Used in scent-collection grid sections and "choose your scent" flows within the PDP.

### Footer

**`footer`** — Deep navy background (`{colors.primary-active}`, #000175) with `{colors.on-primary}` body text and `{colors.surface-blue-pale}` links. Four-column layout at desktop: Shop, Company, Sustainability, Social. Column headings in `{typography.title-sm}`, links in `{typography.body-sm}`. Email sign-up bar embedded at footer top spans full content width with a white text input on navy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to wordmark + cart icon + hamburger; scent chips and color swatches scroll horizontally; hero headline drops to `{typography.display-md}`; impact-stat-band stacks stats in a single column; footer sections collapse to accordion |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level labels with sub-categories in a slide-in drawer; hero splits 50/50 image and text; starter-kit-card goes full-width; impact-stat-band shows 2×2 grid |
| Desktop | 1128–1440px | Three-column product grid; full nav with mega-menu dropdowns; hero 60/40 text-to-image split; impact-stat-band four-column horizontal; footer four-column |
| Wide | > 1440px | Content constrained to 1440px max-width with auto side margins; hero photography bleeds to viewport edge with content column inset; product grid can expand to four columns |

### Touch Targets

- All buttons minimum 48px tall
- Color swatches padded invisibly to 40px tap target despite 24px visual size
- Scent chips at 32px visual height padded to 44px minimum touch height
- Nav hamburger and cart icon padded to 44×44px touch area
- Subscription toggle segments each minimum 44px touch height
- Footer accordion toggle rows minimum 48px touch height

### Collapsing Strategy

- Nav: full horizontal mega-menu on desktop → icon strip + hamburger drawer on mobile
- Product grid: 4-col wide → 3-col desktop → 2-col tablet → 1-col mobile
- Footer: 4-column → 2-column on tablet → collapsible accordion on mobile
- Hero: side-by-side text + image → stacked image above text on mobile
- Impact stat band: 4-across horizontal → 2×2 grid on tablet → 1-column stacked on mobile
- Scent chip row: wrapping flex on desktop → single horizontal scroll track on mobile
- Starter-kit-card: sidebar placement on desktop PDP → full-width block below product details on mobile

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- GT-Pressura weight range and precise tracking values not confirmed from extraction; sizes and weights estimated from visual inspection of live site
- Sailec is a licensed typeface; exact weight and style availability (italic, light, black) not confirmed from font-stack extraction alone
- Self-Modern appears in the detected font stack but its usage context (display editorial vs. marketing headers) could not be determined — omitted from component definitions pending visual verification
- Exact button height and horizontal padding not extracted from CSS; 48px height and 28px horizontal padding are estimates consistent with Shopify theme conventions
- Motion/animation spec for impact-counter count-up entrance and subscription-toggle pill transition not available from static extraction
- Dark-mode palette not observed; unclear whether Blueland ships a dark surface variant
- Precise mapping of scent names to accent colors (#fffcbb → citrus, #c8faa1 → eucalyptus, etc.) inferred from brand knowledge, not directly extracted
- Meta theme-color not set, so OS-level browser chrome color is unspecified
- No confirmed icon system library (custom SVG set vs. third-party); cobalt color usage on icons assumed from brand palette
