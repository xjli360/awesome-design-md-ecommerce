---
version: alpha
name: "iRobot"
source_url: "https://www.irobot.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Harmonia Sans Pro — a Monotype humanist with gently broadened letterforms — distinguishes iRobot from the sterile geometric sans-serifs dominating consumer electronics; the font lends legible warmth to a palette that would otherwise read as purely clinical. The base dark slate (#3c4453) anchors every headline and navigation element as near-navy authority, while the vivid cyan (#00a1e0) fires on every CTA, interactive link, and icon accent — a color borrowed from precision-instrument display panels rather than lifestyle consumer retail. Unexpectedly, an amber-golden tone (#ebc172) surfaces in promotional ribbons and product highlights, creating a productive tension between a cool-signal tech register and the domestic approachability needed to sell autonomous devices to households rather than research labs. Sage greens (#447355, #008827) appear as status-indicator and eco-messaging tones — visible on robot lifecycle and "clean" filters — while a hard error-red (#cc0000) handles both alert states and urgency messaging when cyan alone is insufficient. The layout relies on full-bleed hero photography, robot products centered against near-white surfaces (#f9f9f9, #f7f7f7) to let hardware geometry carry visual weight. Cards use a modest {rounded.md} radius — functional rather than playful — and product taxonomy is organized by lifestyle segmentation ("For Pet Owners," "For Large Homes") sitting above specification-dense secondary text, bridging engineering credibility and consumer decision-making in a single component. Button labels run in uppercase with measured letter-spacing, reinforcing the precision-instrument register without tipping into aggression. The overall system is a controlled dual-register brand: cool-cyan engineering authority that warms at contact points through amber and sage, engineered for a consumer who wants proof of smart hardware, not just a clean floor.

colors:
  primary: "#00a1e0"
  primary-dark: "#005474"
  primary-active: "#0082b8"
  primary-disabled: "#b8e5f6"
  primary-light: "#94e1ff"
  primary-pale: "#a1ddf3"
  ink: "#3c4453"
  ink-soft: "#596273"
  body: "#444444"
  muted: "#818182"
  hairline: "#d6d8db"
  hairline-soft: "#c8cbcf"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-card: "#f7f7f7"
  on-primary: "#ffffff"
  accent-amber: "#ebc172"
  accent-amber-dark: "#7a643b"
  accent-sage: "#447355"
  accent-sage-pale: "#b8dec3"
  accent-sage-light: "#a7d6b4"
  accent-success: "#008827"
  accent-success-dark: "#004714"
  accent-error: "#cc0000"
  accent-error-dark: "#6a0000"
  accent-mauve: "#ae72a3"
  deep-teal: "#0c5460"
  charcoal: "#383d41"
  dark-slate: "#1b1e21"
  cyan-sky: "#61d2ff"
  cyan-pale: "#bee5eb"

typography:
  display-xl:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.21
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.375
    letterSpacing: 0
  body-md:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  caption-strong:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.5px
  button-md:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0
  eyebrow:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.5px
    textTransform: uppercase
  badge:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Harmonia Sans Pro', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.22
    letterSpacing: 0
  mono:
    fontFamily: "Consolas, 'Courier New', 'Liberation Mono', monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
    height: 48px
    hoverBackgroundColor: "{colors.primary-active}"

  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"

  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 10px 26px
    height: 48px
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    hoverTextColor: "{colors.primary}"

  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 28px
    height: 48px
    hoverBackgroundColor: "{colors.charcoal}"

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 44px

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    activeItemColor: "{colors.primary}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    megaMenuBackground: "{colors.canvas}"
    megaMenuBorder: "{colors.hairline}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    badgeBackgroundColor: "{colors.primary}"
    badgeTextColor: "{colors.on-primary}"
    badgeTypography: "{typography.badge}"
    hoverShadow: "0 4px 16px rgba(60,68,83,0.12)"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"

  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary-light}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaSecondaryBackgroundColor: "{colors.canvas}"
    ctaSecondaryTextColor: "{colors.ink}"
    padding: "{spacing.section} 0"

  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.primary}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    padding: "{spacing.section} 0"

  feature-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  sale-badge:
    backgroundColor: "{colors.accent-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"

  promo-ribbon:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
    padding: "6px {spacing.base}"
    rounded: "{rounded.none}"

  robot-status-chip:
    backgroundColorActive: "{colors.accent-success}"
    backgroundColorIdle: "{colors.muted}"
    backgroundColorError: "{colors.accent-error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.full}"
    padding: "4px 10px"

  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    height: 44px
    padding: "10px 20px"

  comparison-table:
    backgroundColor: "{colors.surface-soft}"
    headerBackgroundColor: "{colors.ink}"
    headerTextColor: "{colors.on-primary}"
    cellBorderColor: "{colors.hairline}"
    checkmarkColor: "{colors.accent-success}"
    xColor: "{colors.accent-error}"
    highlightColumnBackground: "{colors.primary-pale}"
    typography: "{typography.body-sm}"
    headerTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"

  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorderColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    height: 38px

  alert-banner-info:
    backgroundColor: "{colors.primary-pale}"
    textColor: "{colors.primary-dark}"
    iconColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"

  alert-banner-success:
    backgroundColor: "{colors.accent-sage-pale}"
    textColor: "{colors.accent-success-dark}"
    iconColor: "{colors.accent-success}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"

  alert-banner-error:
    backgroundColor: "{colors.accent-error}"
    textColor: "{colors.on-primary}"
    iconColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"

  footer:
    backgroundColor: "{colors.dark-slate}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.primary-light}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.caption-strong}"
    bodyTypography: "{typography.body-sm}"
    borderTopColor: "{colors.charcoal}"
    padding: "{spacing.section} 0"

  rating-stars:
    filledColor: "{colors.accent-amber}"
    emptyColor: "{colors.hairline}"
    countTypography: "{typography.caption}"
    countColor: "{colors.muted}"

## Components

### Buttons

**`button-primary`** — Solid cyan (#00a1e0) fill with white uppercase text in Harmonia Sans Pro, 1px letter-spacing giving it an engineered rather than casual feel. Height is 48px with 28px horizontal padding; corner radius is {rounded.xs} (4px) — square enough to signal hardware precision, slightly softened so it reads as modern. Hover darkens to `primary-active` (#0082b8); disabled washes out to pale cyan (#b8e5f6) with muted text.

**`button-secondary`** — White fill with a 2px solid cyan border and cyan text, mirroring the primary label style. On hover the fill inverts to solid cyan, matching button-primary — so both variants converge on the same hover state. Used for secondary CTAs like "Learn More" or "Compare."

**`button-dark`** — Dark slate (#3c4453) fill with white text, deployed in hero modules where cyan would compete with background photography. Hover shifts to charcoal (#383d41). Shares the same uppercase tracking as button-primary.

**`button-ghost`** — Transparent background, ink-colored label, no border. Used for tertiary actions like "See All" links within sections, text-link style. Hover shifts text to primary cyan to signal interactivity.

### Text Input

**`text-input`** — Standard 44px height, 1px hairline border (#d6d8db), {rounded.xs} radius. Focus ring swaps border to primary cyan — consistent with the single-voltage accent system. Placeholder runs in muted (#818182).

### Navigation

**`nav-bar`** — White canvas, 72px tall, with a 1px bottom hairline separating it from page content. Nav links in Harmonia Sans Pro 14px semibold; the active category link underlines or colors in primary cyan. Right side carries a primary cyan CTA button ("Shop Now" or "Find My Robot"). On scroll, the bar gains a soft drop shadow. Mega-menu panels expand below on hover, white background with hairline border, product category grid with small product imagery.

### Product Card

**`product-card`** — Lightly tinted surface (#f7f7f7) with a 1px hairline border that shifts to cyan on hover, providing selection affordance without heavy shadow. Image area uses an even lighter background (#f9f9f9) to isolate the robot device. Title in title-md (18px semibold), price in price-display (24px bold). Feature badges (wifi, mapping tier, suction class) stack in the upper-left corner as small cyan rectangles with white uppercase badge text. Sale pricing uses accent-error (#cc0000) badge. Card corner radius is {rounded.md}.

### Hero Banner

**`hero-banner`** — Full-bleed dark slate (#3c4453) background or deep photographic overlay. Eyebrow text runs in cyan (#94e1ff) uppercase at 11px with 1.5px letter-spacing, providing context before the headline. Headline in display-xl (48px bold). Primary CTA is `button-primary`; a secondary ghost-white CTA often sits alongside it. `hero-light` variant uses near-white (#f9f9f9) canvas for lifestyle photography modules where the device is photographed on white.

### Feature Badge & Sale Badge

**`feature-badge`** — Cyan fill, white uppercase text, {rounded.xs}. Stacked in the top corner of product cards to denote tier differentiators (e.g., "AI NAVIGATION," "SELF-EMPTY"). **`sale-badge`** — Same geometry in error-red (#cc0000), used for promotional pricing events.

### Promo Ribbon

**`promo-ribbon`** — Full-width amber (#ebc172) strip, ink text, caption-strong typography. Appears at the very top of the page for sitewide promotions or limited-time offers. The warm amber against the white nav below creates strong contrast without the alarm-register of red, signaling opportunity rather than urgency.

### Robot Status Chip

**`robot-status-chip`** — Pill-shaped ({rounded.full}), used within robot detail pages and app-integration UI to indicate operating state: green (#008827) for active cleaning, gray (#818182) for idle/docked, red (#cc0000) for error. White caption-strong text over all states.

### Search Bar

**`search-bar`** — Full pill shape ({rounded.full}), 44px tall, cyan search icon on the right. Border highlights to primary cyan on focus. Sits prominently in the nav or within category filtering zones. Lighter than the default input to signal "exploration" rather than form-completion.

### Comparison Table

**`comparison-table`** — Dark slate (#3c4453) header row with white text, title-sm typography. Subsequent rows alternate between surface-soft and white. The highlighted "best value" column uses a pale cyan tint (#a1ddf3 background). Feature checkmarks in accent-success green, X marks in accent-error red. {rounded.sm} corner radius on the outer container.

### Category Chip

**`category-chip`** — Pill filter chips used in product listing pages for "Pet," "Large Homes," "Budget" etc. Inactive state is surface-soft with hairline border; active state fills with primary cyan, white text. Compact 38px height so a row of chips reads as a filter control rather than a button row.

### Alert Banners

Three semantic variants — info (pale cyan background, dark teal text), success (pale sage background, dark green text), error (solid error-red, white text). All share {rounded.sm} and body-sm typography. Used for warranty messages, out-of-stock notices, and order confirmations.

### Footer

**`footer`** — Near-black (#1b1e21) background, surface-soft (#f9f9f9) body text, light-cyan (#94e1ff) links that shift to white on hover. Column headings in caption-strong (uppercase, 0.5px tracking). Legal and social links in the bottom strip. The stark dark base provides a visual bookend to the predominantly light-surfaced product pages.

### Rating Stars

**`rating-stars`** — Amber (#ebc172) filled stars, hairline-colored empty stars, muted gray count text in caption scale. The amber star color ties back to the promo-ribbon amber, creating a warm-accent sub-system within the cool-cyan primary system.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen drawer; hero text reduces to display-md (28px); hero CTA stacks vertically; comparison table scrolls horizontally; promo ribbon text truncates to one line |
| Tablet | 744–1128px | Two-column product grid; nav shows logo + hamburger or condensed top-level links; hero uses display-lg (36px); category chips scroll horizontally in single row |
| Desktop | 1128–1440px | Three-column product grid; full nav with mega-menu hover; hero at full display-xl (48px); comparison table fully visible |
| Wide | > 1440px | Max content width ~1400px, centered with symmetric gutter; hero background extends full-bleed; product grid may expand to four columns for accessory/parts pages |

### Touch Targets

- All buttons minimum 48px height, 44px minimum width
- Category chips minimum 38px height with adequate horizontal padding for thumb tap
- Nav hamburger icon minimum 44×44px tap target
- Product card CTA button maintains 48px height on mobile
- Robot status chips expand to 36px minimum on touch viewports

### Collapsing Strategy

- Mega-menu becomes full-screen slide-in drawer on mobile, with nested accordion for subcategories
- Comparison table collapses to a swipeable card stack on mobile — one model per "slide"
- Footer collapses link columns to accordion sections below 744px
- Promo ribbon remains sticky at top on mobile; can be dismissed with an X icon
- Product filter chips overflow into a horizontal scroll row with fade-out right edge on mobile
- Hero with dual CTAs stacks them vertically (primary on top) below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed exact heading font sizes or weights extracted from live CSS — Harmonia Sans Pro scale derived from visual conventions for the brand; actual values may differ
- Button border-radius not directly confirmed; {rounded.xs} (4px) inferred from screenshot analysis
- Exact nav bar height not extracted; 72px is a reasonable inference for a product-category-heavy nav
- Dark-mode or alternate theme tokens not identified — site appears to use a single light-dominant theme
- Icon system (likely a custom glyph font or SVG sprite) not extractable; FontAwesome stack detected but may be a legacy fragment
- Spacing scale is conventional — no CSS custom properties or design-token JSON was extractable from the page
- Harmonia Sans Pro licensing means it may be subset or served as a proprietary WOFF2; fallback to Arial/sans-serif may be more visible on non-licensed environments than expected
- #ae72a3 (mauve) and #ebc172 (amber) appear in the palette but their precise usage contexts (specific product lines, seasonal promotions, or persistent brand elements) could not be confirmed from extraction alone
- Meta theme-color was absent, suggesting no PWA manifest color override; nav bar color on mobile address bar is unspecified
