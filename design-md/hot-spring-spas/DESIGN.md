---
version: alpha
name: "Hot Spring Spas"
source_url: "https://www.hotspring.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The thermal teal at `#007681` — not aqua, not navy, but the specific blue-green of mineral-rich spring water — anchors every primary action surface on hotspring.com, from CTA buttons to section dividers, functioning as a single brand voltage that names the product category without words. MuseoSans-300, a genuinely thin humanist face, carries all body copy at weights that feel lighter than most wellness brands dare; the 300 in the font name is not incidental — the brand trusts generous white space and a restrained typographic hand over heavy slab muscle. Roboto Slab steps in for display headings, adding serif warmth that grounds the teal and signals durability for hardware built to last a decade outdoors. The neutral backbone runs from near-black `#434343` ink through midtone grays `#707070` and `#555555` to the light hairline `#eeeeee`, a complete tonal range without a single pure black or pure white in the extracted set. A warm stone tone `#b8a88c` surfaces as an earthy counterpoint to the teal — it appears in lifestyle sections evoking wood cabinetry and cedar deck surroundings rather than clinical pool environments. The accent vocabulary extends to `#63c6bd` (a lighter teal for hover states and badges), `#7aba7b` (sage for eco and FreshWater Salt System indicators), and `#a4d866` (bright lime for energy-efficiency callouts). Corner radii are modest at 4–8px — cards and inputs stay grounded and product-forward rather than playfully pill-shaped, appropriate for an audience making a $5,000–$20,000 purchase decision. Navigation lives in a dark charcoal `#32373c` band capped by a 4px teal stripe at the very top of the viewport, a signature structural accent that reads before any content begins. The navy `#003388` and alert red `#b94a48` are reserved for dealer-network maps and error states respectively, keeping the teal uncontested as the primary brand signal.

colors:
  primary: "#007681"
  primary-hover: "#009ca6"
  primary-active: "#035457"
  primary-disabled: "#63c6bd"
  primary-light: "#63c6bd"
  ink: "#434343"
  body: "#424242"
  muted: "#707070"
  muted-soft: "#555555"
  hairline: "#eeeeee"
  hairline-dark: "#bbbbbb"
  canvas: "#ffffff"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  surface-dark: "#32373c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-teal-bright: "#009ca6"
  accent-teal-light: "#63c6bd"
  accent-sage: "#7aba7b"
  accent-lime: "#a4d866"
  accent-stone: "#b8a88c"
  accent-navy: "#003388"
  error: "#b94a48"
  error-dark: "#cf2e2e"
  warning: "#e1523d"
  nav-bg: "#32373c"

typography:
  display-xl:
    fontFamily: "'Roboto Slab', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Roboto Slab', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Roboto Slab', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'MuseoSans-300', Roboto, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'MuseoSans-300', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'MuseoSans-300', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 300
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'MuseoSans-300', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 300
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'MuseoSans-300', Roboto, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.33
    letterSpacing: 0.25px
  label-sm:
    fontFamily: "'MuseoSans-300', Roboto, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'MuseoSans-300', Roboto, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'MuseoSans-300', Roboto, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'MuseoSans-300', Roboto, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  price-display:
    fontFamily: "'Roboto Slab', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.1
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
    padding: 14px 28px
    height: 50px
    hover:
      backgroundColor: "{colors.primary-hover}"
    active:
      backgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 50px
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 50px
    border: "2px solid {colors.primary}"
    hover:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 50px
    border: "2px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline-dark}"
    focus:
      border: "2px solid {colors.primary}"
    placeholder:
      textColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.nav-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 68px
    topStripe:
      backgroundColor: "{colors.primary}"
      height: 4px
    logo:
      height: 40px
    dropdown:
      backgroundColor: "{colors.canvas}"
      textColor: "{colors.ink}"
      shadow: "0 8px 24px rgba(0,0,0,0.12)"
      rounded: "{rounded.xs}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    shadow: "0 2px 12px rgba(0,0,0,0.08)"
    imageAspect: "4/3"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    badge:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.label-sm}"
      rounded: "{rounded.xs}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    minHeight: 600px
    overlayColor: "rgba(3,84,87,0.45)"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaSpacing: "{spacing.lg}"
    layout: "full-bleed image background, text left-aligned in constrained column, dual-button CTA row (primary + ghost)"
  series-band:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0"
    gridColumns: 3
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    cardRounded: "{rounded.sm}"
    cardShadow: "0 4px 16px rgba(0,0,0,0.1)"
    cardBorder: "1px solid {colors.hairline}"
  feature-icon-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.xxl} 0"
    iconColor: "{colors.primary}"
    iconSize: 48px
    labelTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    columns: 4
    layout: "icon top, label, short description — equal-width columns"
  wellness-callout:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.section}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    accentBar:
      height: 4px
      backgroundColor: "{colors.accent-teal-light}"
    layout: "two-column — headline + body left, lifestyle image or stat right"
  dealer-locator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.body-md}"
    inputBorder: "1px solid {colors.hairline-dark}"
    inputRounded: "{rounded.xs}"
    mapPinColor: "{colors.primary}"
    dealerCardRounded: "{rounded.sm}"
    dealerCardBorder: "1px solid {colors.hairline}"
    dealerCardBackground: "{colors.canvas}"
    dealerTitleTypography: "{typography.title-md}"
    dealerBodyTypography: "{typography.body-sm}"
  comparison-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.title-md}"
    rowTypography: "{typography.body-sm}"
    rowAlternate: "{colors.surface-soft}"
    checkColor: "{colors.primary}"
    dividerColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
  spec-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    highlight:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  eco-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  promo-banner:
    backgroundColor: "{colors.accent-stone}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    dividerColor: "rgba(255,255,255,0.15)"
    logoHeight: 36px
    padding: "{spacing.xxl} 0 {spacing.xl} 0"
    columns: 4
    bottomBar:
      backgroundColor: "{colors.primary-active}"
      textColor: "{colors.on-dark}"
      typography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — The primary CTA renders in thermal teal `#007681` with uppercase MuseoSans-300 lettering at 600 weight, tracking out at 0.5px. On hover the background lifts to the brighter `#009ca6`; on active press it drops to the deep forest teal `#035457`. Disabled state uses the pale `#63c6bd`. The 4px radius (`{rounded.xs}`) keeps the button grounded and architectural rather than pill-soft, appropriate for a considered hardware purchase.

**`button-secondary`** — A transparent body with a 2px teal `#007681` border and matching teal text, inverting fully to filled teal on hover. Used alongside primary CTAs in hero sections and product detail pages where two actions carry near-equal weight without visual competition.

**`button-ghost`** — Reserved for dark or image-overlaid backgrounds — hero banners, full-bleed lifestyle sections. White text on a 2px white border over transparent ground; does not invert on hover to preserve legibility against variable photography. Pairs with `button-primary` as the secondary action in the hero CTA row.

**`button-sm`** — Same construction at reduced scale (13px, 0.5px tracking) for inline filter chips, mobile nav actions, and card-level CTAs where a 50px-tall button would overwhelm the surrounding content.

### Text Input

**`text-input`** — White background with a 1px `#bbbbbb` border at rest, 48px height, and 12px vertical padding. Focus ring upgrades to a 2px solid teal `#007681` outline. Placeholder text renders in `#707070` at MuseoSans weight 300. Used throughout the dealer locator ZIP input, build-your-spa configurator, and lead-capture contact forms.

### Navigation

**`nav-bar`** — A dark charcoal `#32373c` horizontal bar at 68px height, capped at the viewport top by a 4px teal `#007681` stripe that functions as a brand signature before any logo or link appears. Nav links use MuseoSans-300 at 600 weight and 0.25px tracking in white (`{colors.on-dark}`). Dropdown panels emerge on a white canvas with `#434343` ink, an 8px radius, and `0 8px 24px rgba(0,0,0,0.12)` shadow — a clean reversal from the dark bar above.

### Product Card

**`product-card`** — White card with 1px `#eeeeee` border and a `0 2px 12px rgba(0,0,0,0.08)` shadow lift. A 4:3 product image occupies the card top. Below: series/model name in `title-md` (MuseoSans 600/18px), starting price in Roboto Slab `price-display` (28px/700), followed by a 2–3 line spec summary in `body-sm`. A teal badge overlay (`{typography.label-sm}`, uppercase) appears for series tier labels ("Highlife", "Limelight") or "New" callouts.

### Hero

**`hero`** — Full-bleed lifestyle photography behind a `rgba(3,84,87,0.45)` teal scrim that ensures the `display-xl` Roboto Slab headline reads cleanly in white. Text aligns left inside a constrained inner column (~600px). Two CTAs in a horizontal row — one `button-primary` (filled teal), one `button-ghost` (white outline) — separated by `{spacing.lg}`. Minimum 600px tall on desktop, compressing to 380px on mobile. The scrim's teal cast reinforces the primary brand color even when photography varies by season.

### Series Band

**`series-band`** — A light `#eeeeee` section band displaying 3–4 spa series in an equal-width image card grid. Section headline in Roboto Slab `display-sm`. Cards carry a 4:3 product render, series name in `title-md`, and a 1–2 sentence descriptor in `body-sm`. Subtle `0 4px 16px rgba(0,0,0,0.1)` shadow and 8px radius. Functions as the primary product-family navigation immediately below the hero.

### Feature Icon Row

**`feature-icon-row`** — Four-column icon grid on white canvas. Teal `#007681` Font Awesome Pro line icons at 48px sit above a label in `title-sm` and a 2–3 line description in `body-sm`. Feature claims include jet count, filtration cycles, energy certification, and hydrotherapy benefits. On tablet collapses to a 2×2 grid; on mobile stacks to a single-column scroll list.

### Wellness Callout

**`wellness-callout`** — A full-width teal `#007681` band with a 4px `#63c6bd` accent bar leading the section. Headline in Roboto Slab `display-md` in white, body in MuseoSans `body-md`. Right column holds a lifestyle image or a large stat (e.g., "9 out of 10 owners report better sleep"). Used for hydrotherapy benefit messaging and FreshWater system claims. The solid teal fill makes this the highest-contrast non-hero section on the page.

### Dealer Locator

**`dealer-locator`** — A soft `#eeeeee` background section housing a ZIP-code `text-input`, radius selector, and an interactive map. Teal `#007681` pins mark authorized dealers with an expanded 44px touch target on mobile. A scrollable left panel holds dealer result cards: white background, `{rounded.sm}`, `{colors.hairline}` border; dealer name in `title-md`, address and phone in `body-sm`. The navy `#003388` may appear in map cluster markers.

### Comparison Table

**`comparison-table`** — Header row fills with teal `#007681`; feature labels and model names render in white `title-md`. Feature rows alternate between white and `#eeeeee`. Check marks appear in teal; dashes in `#bbbbbb`. Container has `{rounded.sm}` rounding and a `{colors.hairline}` outer border. Used for side-by-side spa model comparisons on collection and category pages.

### Spec Badge / Eco Badge

**`spec-badge`** — A muted `#eeeeee` pill in `caption` text (12px/300 weight) for jet count, gallon capacity, or dimension specs. A highlighted variant swaps to teal fill with white text for a featured or differentiating spec value.

**`eco-badge`** — A sage green `#7aba7b` pill with uppercase white `label-sm` text. Applied to products certified for energy efficiency or equipped with the FreshWater Salt System, pairing the color with an environmental claim rather than a promotional one.

### Promo Banner

**`promo-banner`** — A warm stone `#b8a88c` strip pinned above the nav-bar during seasonal sale windows. Centered `body-sm` promotional copy with an inline teal `#007681` CTA link at 600 weight. On mobile the strip truncates to a single line with a right-chevron "Details" link.

### Footer

**`footer`** — Dark `#32373c` background with a 4-column link grid. Section headings in `title-sm` white/600. Links in `body-sm` white/300 at 15% opacity dividers between columns. Logo at 36px height. Bottom bar uses deep teal `#035457` for legal, copyright, and privacy links in `caption`. The teal-on-dark bottom stripe echoes the teal stripe at the top of the nav-bar, bookending the page in brand color.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero min-height 380px, headline drops to display-md; nav collapses to hamburger over charcoal bar; series-band stacks vertically; feature-icon-row goes 1-column; comparison table scrolls horizontally with sticky first column |
| Tablet | 744–1128px | Two-column product grid; feature-icon-row 2×2; hero text block widens to 60%; nav shows primary product links, hides utility links in overflow menu |
| Desktop | 1128–1440px | Three-column product grid; four-column feature-icon-row; full nav with dropdown mega-menus; wellness-callout two-column layout active |
| Wide | > 1440px | Max-width container ~1360px centered; hero and wellness-callout bleed full viewport width; comparison table shows all model columns without horizontal scroll |

### Touch Targets

- All buttons minimum 50px height on mobile; 44px minimum width
- Hamburger nav icon tap target 44×44px
- Dealer locator map pins expanded to 44px touch area with invisible padding
- Product card full-surface tap area (no separate "View" button required)
- Comparison table horizontal scroll triggered by swipe, not a visible scrollbar

### Collapsing Strategy

- Mega-nav product dropdowns collapse to accordion panels inside a full-height charcoal drawer on mobile
- Comparison table reflows to one swipeable card per model below 744px; feature rows become labeled rows within each card
- Feature icon row reflows 4→2→1 columns at the 1128px and 744px breakpoints respectively
- Promo banner truncates to one line on mobile with a "Learn more ›" text link
- Footer 4-column grid collapses to 2-column at tablet, single-column accordion at mobile (headings become expand/collapse triggers)
- Wellness callout shifts from two-column to stacked image-below-text at tablet width

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- MuseoSans-300 appears in the extracted font stack but specific weights used per typographic role (300 vs 600 vs 700) are inferred from the stack declaration, not from computed rendered styles; exact weight assignments per scale may differ
- Exact button corner-radius not extracted from computed styles — 4px (`{rounded.xs}`) is inferred from the brand's architectural aesthetic rather than measured from a live element
- No dark-mode palette detected or confirmed; all surfaces assumed to operate in light mode only
- Logo dimensions, clearspace rules, and lockup variants (full wordmark vs. icon-only) not available from extraction
- Hover and focus animation timings (transition duration, easing curve) not extracted
- Font Awesome 6 Pro is confirmed via font stack; icon style (outline vs. solid fill, stroke weight) within the product UI not specified
- The navy `#003388`, bright lime `#a4d866`, and orange-red `#e1523d` appear in the extracted palette but specific usage contexts (map cluster UI, energy-label callouts, alert/error states) could not be confirmed from extraction alone
- Mobile navigation pattern (drawer slide-in vs. full overlay vs. push) is inferred from category norms, not observed directly
- No confirmed grid gutter or max-content-width value extracted; 1360px max-width is a reasonable inference for the site category
