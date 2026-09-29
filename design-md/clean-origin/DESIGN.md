---
version: alpha
name: "Clean Origin"
source_url: "https://www.cleanorigin.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  When the chemical composition of a stone is identical whether it grew in the earth over a billion years or in a controlled thermal reactor over a few weeks, the design challenge is not authenticity — it is clarity. Clean Origin builds its visual system on that premise: a white canvas against #313131, a warm charcoal (the single confirmed extraction from a Cloudflare-protected site) that carries navigation, body copy, and primary CTAs without flinching toward the silver-cold blacks that commodity retailers use. The name is literal instruction — no decorative borders, no script-font romanticism, no textured parchment backgrounds reaching for antique significance. Product photography runs large and unframed, letting stone brilliance supply the luxury signal that other brands achieve with heavy gold UI chrome. Type almost certainly splits between a light-weight display serif for headline moments — ring hero pages, editorial features on diamond origin — and a neutral sans-serif for filter panels, cart flows, and comparison tables where precision outweighs atmosphere. The ring customizer is the brand's defining commitment: a multi-step configuration panel where shoppers choose stone shape, carat, cut grade, and metal, all within a layout that must stay calm and informative against the emotional weight of the purchase. Filter chips cycle between `{rounded.full}` pill states when active and hairline-bordered resting states, giving immediate visual confirmation without color noise. A champagne-gold accent — widely used across the fine jewelry category and consistent with Clean Origin's aesthetic positioning — is assumed for price displays, ring metal callouts, and trust-badge icons, though not confirmed by extraction. Section rhythm runs at `{spacing.section}` between major content blocks, and `{colors.surface-soft}` warm-cream panels break the all-white scroll without introducing color. The overall register is confident restraint: every visual decision is an argument that a lab-grown diamond and a mined diamond are not merely equivalent, but that choosing the former is the cleaner, more deliberate act.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#ababab"
  ink: "#313131"
  body: "#4d4d4d"
  muted: "#787878"
  stone-gray: "#a0a0a0"
  hairline: "#e4e4e4"
  hairline-soft: "#f2f2f2"
  canvas: "#ffffff"
  surface-soft: "#f8f6f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  champagne: "#b8973f"
  champagne-light: "#f2e9d8"
  champagne-on-dark: "#d4b86a"
  success: "#3a7d44"
  error: "#c0392b"

typography:
  display-xl:
    fontFamily: "Georgia, 'Playfair Display', 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: 0.02em
  display-lg:
    fontFamily: "Georgia, 'Playfair Display', serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0.015em
  display-md:
    fontFamily: "Georgia, 'Playfair Display', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "Georgia, 'Playfair Display', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.005em
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.625
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  label-uppercase:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Playfair Display', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.04em

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
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
    padding: "0"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.stone-gray}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    padding: "{spacing.base}"
  product-card-badge:
    backgroundColor: "{colors.champagne}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 560px
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
  ring-customizer:
    backgroundColor: "{colors.canvas}"
    borderLeft: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
  stone-shape-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    borderActive: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    labelTypography: "{typography.caption}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-tag-champagne:
    textColor: "{colors.champagne}"
    typography: "{typography.price-display}"
  education-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    borderLeft: "3px solid {colors.champagne-light}"
  trust-badge:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    iconColor: "{colors.champagne}"
  quiz-start:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
  comparison-table:
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.title-sm}"
    rowTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline-soft}"
    rowAltBackground: "{colors.surface-soft}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
    linkColor: "{colors.champagne-on-dark}"

## Components

### Buttons
**`button-primary`** — Charcoal #313131 fill with white type, letter-spaced uppercase at 13px/600 weight. The `{rounded.xs}` 4px corner reads architectural rather than soft — appropriate for a purchase decision that carries significant weight. Active state descends to `{colors.primary-active}` near-black; disabled bleaches to `{colors.primary-disabled}` mid-gray. This dark-on-white pairing signals premium confidence without urgency.

**`button-secondary`** — White fill with a 1px charcoal border, matching uppercase type and 4px corner radius. Used for secondary actions on product pages — "Add to Wishlist" or "Compare Stones" sitting beside a "Start Building" primary. Maintains hierarchy without introducing a third color into the palette.

**`button-ghost`** — Transparent background with charcoal underlined type at `{typography.button-sm}`. Reserved for low-priority inline text actions within educational copy blocks, such as "Learn more about IGI certification." No padding, flows within prose.

### Text Input
**`text-input`** — White fill at rest with a 1px `{colors.hairline}` border, sharpening to a 1px `{colors.primary}` charcoal border on focus. Height matches primary button at 48px so form rows align cleanly. Placeholder text in `{colors.stone-gray}`. Corner radius matches buttons at `{rounded.xs}` for a cohesive form language.

### Navigation
**`nav-bar`** — White background, 64px tall, separated from page content by a hairline bottom border. Logo left-anchored; category links (`{typography.nav-link}`, 13px/500 with 0.04em spacing) span the center; search, wishlist, and cart icons cluster right. The promo strip above it (`{colors.primary}` fill, 40px, `{typography.caption}` white type) carries offers and free-shipping thresholds — the only use of charcoal fill outside of CTAs at the top of the page.

### Product Cards
**`product-card`** — Zero-radius square cards; ring and stone photography fills a 1:1 image zone with no frame. Below: ring name in `{typography.title-md}`, metal and stone variant in `{typography.body-sm}` muted, price in `{typography.price-display}`. Lab-grown quality callouts (e.g., "IGI Certified", "Conflict-Free") appear as `{colors.champagne}` `{typography.label-uppercase}` badges pinned to the image corner. Cards sit flush in a grid with `{spacing.base}` gutters.

### Hero Banner
**`hero-banner`** — `{colors.surface-soft}` warm-cream background on homepage and category entry heroes — warm enough to register as distinct from pure white without introducing color. Headline at `{typography.display-xl}` (52px/300 weight serif) commands the viewport; subline at `{typography.body-md}` delivers the single value proposition in 1–2 sentences. CTA floats below at `{spacing.lg}` gap. Photography or ring renders are right-aligned on desktop, stacked below text on mobile.

### Ring Customizer
**`ring-customizer`** — The brand's core feature: a sticky right panel (desktop) or bottom drawer (mobile) holding all configuration choices — stone shape, carat, cut, color, clarity, and metal type. White background divided from the product view by a hairline left border. Section group headers in `{typography.title-sm}` uppercase; option labels in `{typography.body-sm}`. Running price in `{typography.price-display}` updates inline; a `{colors.champagne}` accent marks the active price figure.

**`stone-shape-selector`** — A grid of icon + label tiles within the customizer. Each tile carries a 1px `{colors.hairline}` border at rest, upgrading to a 2px `{colors.primary}` border when selected. `{rounded.sm}` (8px) corner keeps the tiles readable at compact mobile sizing. Shape label in `{typography.caption}` below the icon glyph.

### Filter System
**`filter-chip`** — Pill-shaped tags (`{rounded.full}`) for browsing ring shape, metal, price range, and carat. At rest: `{colors.canvas}` fill, 1px `{colors.hairline}` border, `{colors.body}` text. Active: flips to `{colors.primary}` fill with white type. The sharp visual switch makes selection state unambiguous across dense filter rows. Chips scroll horizontally on mobile.

### Price Display
**`price-tag`** — Default price in `{typography.price-display}` (24px light serif) at `{colors.ink}`. The serif face gives the price a deliberate weight, slowing the eye appropriately for a high-consideration purchase.

**`price-tag-champagne`** — Sale or "compare at" pricing uses the same serif scale in `{colors.champagne}`, creating a warm-gold signal distinct from error reds.

### Education & Trust
**`education-callout`** — Inline within PDP pages and blog content: a `{colors.surface-soft}` block with a 3px `{colors.champagne-light}` left border, `{rounded.sm}` radius, and `{spacing.lg}` padding. Used to explain grading criteria, lab-grown vs. mined comparisons, and certification details. Body type at `{typography.body-sm}`.

**`trust-badge`** — Icon + short label ("Lifetime Warranty", "Free Returns", "Conflict-Free Stones"). Icon rendered in `{colors.champagne}`; label in `{typography.caption}` at `{colors.muted}`. Typically rendered as a horizontal bar just above the footer or below the hero CTA.

### Comparison Table
**`comparison-table`** — Side-by-side lab-grown vs. mined diamond comparison table with a `{colors.primary}` header row carrying `{colors.on-primary}` white `{typography.title-sm}` uppercase labels. Alternating rows use `{colors.surface-soft}` for scan-ability. Column borders in `{colors.hairline-soft}`. Row text at `{typography.body-sm}`.

### Quiz / Ring Finder
**`quiz-start`** — Entry card for the style-preference or ring-finder guided flow. `{colors.surface-soft}` background with `{rounded.md}` radius and generous `{spacing.xxl}` padding on all sides. Headline in display serif (`{typography.display-md}`), body copy in `{typography.body-md}`. CTA button uses standard `button-primary` below.

### Footer
**`footer`** — Full-width `{colors.primary}` charcoal reverses the canvas-and-ink relationship: white type on dark, with `{colors.champagne-on-dark}` warm-gold links for category and resource navigation. Column layout (Shop, About, Education, Support) in `{typography.body-sm}`. Newsletter input row sits at the footer top before the columns. The single footer color keeps the visual frame closed without introducing a new brand hue.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column ring grid; customizer becomes bottom drawer with summary price visible; nav collapses to hamburger with full-screen overlay; hero image stacks below headline; filter chips scroll horizontally; comparison table scrolls horizontally |
| Tablet | 744–1128px | 2-column ring grid; customizer narrows to ~40% right panel; nav links visible with possible overflow menu; hero image right-aligned at reduced height |
| Desktop | 1128–1440px | 3-column ring grid; full sticky customizer panel; hero at 560px min-height; trust-badge bar visible below hero |
| Wide | > 1440px | Max content width ~1360px centered; ring grid may expand to 4 columns; hero imagery may bleed edge-to-edge behind a max-width text container |

### Touch Targets
- All buttons minimum 48px height
- Stone shape selector tiles minimum 44×44px tap area
- Filter chips minimum 36px height with horizontal padding providing adequate touch area
- Nav icon buttons (search, wishlist, cart) minimum 44px hit area via padding expansion
- Footer links minimum 44px vertical spacing in collapsed mobile column

### Collapsing Strategy
- Ring customizer: desktop sticky right panel → tablet narrowed right panel (~40% width) → mobile bottom drawer that expands on tap
- Navigation: full link bar with all categories → condensed bar with primary links only → hamburger with full-screen overlay at mobile
- Product grid: 3-col → 2-col → 1-col (with optional 2-across compact option at narrowest mobile)
- Comparison table: full multi-column layout → horizontal scroll at tablet and mobile rather than stacked rows
- Hero: side-by-side text and image → image below text with reduced padding at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extraction severely limited: site returned a Cloudflare "Just a moment..." challenge page — only #313131 confirmed; this color may originate from the challenge page itself rather than the brand UI
- Full brand palette unconfirmed: all surface colors, the champagne/gold accent (#b8973f assumed), and error/success states are category-inferred from fine jewelry conventions
- Brand typeface unknown: extraction found only OS-level system font stacks; the display serif (Georgia used as primary fallback) is inferred from brand category — Clean Origin may load a licensed or custom typeface (Cormorant Garamond, Canela, or similar) via JS after bot-check
- Button corner radius unconfirmed; `{rounded.xs}` (4px) chosen for a formal fine-jewelry register — the brand may use fully square (`{rounded.none}`) or a slightly larger radius
- Exact promo strip color, nav height, and footer background treatment not verifiable from extraction
- Ring customizer step count, animation behavior, and price-update interaction details not observed
- Champagne gold hex (#b8973f) is estimated; the actual brand accent may differ in hue or saturation
- Whether the brand uses a serif display font at all is inferred — some modern jewelry brands run all-sans-serif type systems
