---
version: alpha
name: "Fabletics"
source_url: "https://fabletics.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every Fabletics landing page opens at impact — a full-bleed athlete in motion against deep charcoal, making the brand's GT Pressura display text land at 80px weight-800 like a physical object rather than a type choice. GT Pressura is the single typeface across all surfaces, a geometric grotesque athletic enough to hold at extreme display scale yet clean enough for 14px body copy, with no secondary font brought in to signal luxury or softness. The extracted palette is sparse — just #9d9d9c reaching through the JavaScript-loaded token system — but that confirmed neutral reads clearly as disabled state and secondary text in a system that otherwise operates at the poles: deep charcoal surface, white canvas in content zones, and a warm CTA red in the #e03 family that fires every primary action. The VIP membership mechanic shapes the component inventory in ways that distinguish Fabletics from standard DTC athleticwear: countdown timers live below hero sections, quiz-entry CTAs surface within two scrolls on every landing page, and member price renders in the accent red beside a struck-through retail price on every product tile. Buttons carry zero border-radius and uppercase lettering — 52px tall, weight 700, tracking opened slightly — a sharp geometry that reads confident rather than approachable, matching the brand's performance-first posture over the softly rounded competitors that lean on boutique minimalism. Product cards tile at 3:4 portrait aspect ratio in dense 4-column desktop grids, hover behavior swapping to a second lifestyle shot, with a badge system running BESTSELLER and sale-percentage overlays in label-uppercase at 11px letter-spaced 1.5px. Navigation megamenus embed editorial imagery panels beside category links, hinting at catalog depth that spans leggings, sports bras, outerwear, and menswear. Footer and primary hero sections share the same deep dark canvas, giving the brand's high-contrast identity a consistent frame at entry and exit.

colors:
  primary: "#1c1c1c"
  primary-active: "#000000"
  primary-disabled: "#c8c8c8"
  cta-accent: "#e0393e"
  cta-accent-active: "#c52d31"
  ink: "#1c1c1c"
  body: "#3d3d3d"
  muted: "#9d9d9c"
  hairline: "#d9d9d9"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#111111"
  surface-dark-raised: "#1c1c1c"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  member-badge: "#e0393e"

typography:
  display-xl:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 80px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -1px
  display-lg:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  title-sm:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  label-uppercase:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.8px
    textTransform: uppercase
  price-md:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-item:
    fontFamily: "'GT Pressura', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px

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
    height: 52px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-accent:
    backgroundColor: "{colors.cta-accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 52px
  button-accent-active:
    backgroundColor: "{colors.cta-accent-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.ink}"
    padding: 12px 30px
    height: 52px
  button-secondary-inverse:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "2px solid {colors.on-dark}"
    padding: 12px 30px
    height: 52px
  button-pill:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-item}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-item}"
    height: 72px
    borderBottom: none
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    nameTypography: "{typography.body-sm}"
    gap: "{spacing.sm}"
  product-card-price:
    memberPriceTypography: "{typography.price-md}"
    memberPriceColor: "{colors.member-badge}"
    retailPriceTypography: "{typography.price-sm}"
    retailPriceColor: "{colors.muted}"
    retailTextDecoration: line-through
  product-card-badge:
    backgroundColor: "{colors.member-badge}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    position: absolute
    top: "{spacing.sm}"
    left: "{spacing.sm}"
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    minHeight: 640px
    paddingH: "{spacing.section}"
  membership-cta-banner:
    backgroundColor: "{colors.surface-dark-raised}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    paddingV: "{spacing.xxl}"
    paddingH: "{spacing.xl}"
    rounded: "{rounded.none}"
  countdown-timer:
    backgroundColor: "{colors.cta-accent}"
    textColor: "{colors.on-primary}"
    labelTypography: "{typography.label-uppercase}"
    digitTypography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    activeBorder: "2px solid {colors.ink}"
    activeBackgroundColor: "{colors.canvas}"
  size-swatch:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
    disabledTextColor: "{colors.muted}"
    width: 40px
    height: 40px
  color-swatch:
    rounded: "{rounded.full}"
    width: 24px
    height: 24px
    selectedRingColor: "{colors.ink}"
    selectedRingOffset: 2px
    selectedRingWidth: 2px
  quiz-cta-card:
    backgroundColor: "{colors.surface-dark-raised}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.title-md}"
    ctaTypography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.on-dark}"
    paddingV: "{spacing.section}"

## Components

### Buttons

**`button-primary`** — Sharp-cornered ({rounded.none}), 52px tall, uppercase GT Pressura at weight 700 with 0.8px letter-spacing. The zero-radius treatment is consistent across the entire button family — this brand makes no concession to softness on primary actions. Active state darkens to pure black (#000000); disabled state uses #c8c8c8, keeping the uppercase form but draining color.

**`button-accent`** — The CTA-red variant ({colors.cta-accent}, approximate #e0393e) fires on high-urgency surfaces: hero CTAs, membership prompts, flash-sale sections, and quiz entry points. Shares all geometry with button-primary but signals the higher commercial pressure of the membership funnel. Active state drops to {colors.cta-accent-active}.

**`button-secondary`** — Outlined with a 2px solid {colors.ink} border, transparent fill, identical uppercase typography and height as button-primary. Used for secondary checkout actions and "Shop All" links adjacent to accent CTAs. An inverse variant (`button-secondary-inverse`) swaps border and text to {colors.on-dark} for use on dark canvas sections.

**`button-pill`** — Dark-filled ({colors.surface-dark}) pill shape ({rounded.full}) at reduced size, used for tag-style filter chips in a non-active state on collection header rows. Active filter pills switch to transparent fill with a 2px {colors.ink} border via `filter-pill`.

### Text Input

**`text-input`** — Zero border-radius, 1px {colors.hairline} border, 48px height. Focus state upgrades border to 1px solid {colors.ink}, no glow or shadow — consistent with the brand's hard-edge aesthetic. Placeholder text in {colors.muted} (#9d9d9c). Used in email capture, login, and search field contexts.

### Navigation

**`nav-bar`** — 72px tall on a white canvas with a 1px {colors.hairline} underline. Category links set in {typography.nav-item} (GT Pressura 600, 15px, 0.3px tracking). A dark variant (`nav-bar-dark`) drops the underline and renders on {colors.surface-dark} for hero-adjacent sections where the nav floats above photography. Megamenu drawers include editorial imagery panels at 240–280px width beside category-link columns, reflecting the catalog's breadth.

### Product Card

**`product-card`** — No border-radius, portrait 3:4 image aspect ratio, 4-column desktop grid with 16px gaps. Hover behavior swaps image to a second lifestyle shot. Below the image: product name in {typography.body-sm}, color-swatch row, then a two-line price block via `product-card-price` — member price in {colors.member-badge} red at {typography.price-md}, retail price struck-through in {colors.muted} at {typography.price-sm}. Absolute-positioned `product-card-badge` (BESTSELLER, sale percent) lives at top-left in label-uppercase — 11px, 1.5px letter-spacing, hard corners, red fill.

### Hero

**`hero-dark`** — Full-bleed dark section ({colors.surface-dark}) with left-aligned text stack: headline at {typography.display-xl} (80px, weight 800), sub-head at {typography.display-sm} (28px, weight 700), body copy at {typography.body-md}, then a button pair. Minimum height 640px. Photography bleeds behind a dark overlay or is isolated to the right half of the frame on wide viewports. The horizontal padding expands to {spacing.section} (64px) on desktop to create a column feel within the full-bleed surface.

### Membership & Countdown

**`membership-cta-banner`** — A standalone dark-canvas block ({colors.surface-dark-raised}) that interrupts the scroll between category sections. Headline in {typography.display-md} (40px, weight 700), body in {typography.body-md}, followed by a button-accent CTA. No border-radius. Padding is {spacing.xxl} vertical, {spacing.xl} horizontal.

**`countdown-timer`** — Renders in {colors.cta-accent} red with digit readout in {typography.display-sm} (28px, weight 700) and DAYS / HRS / MIN / SEC labels in {typography.label-uppercase}. Hard corners, no radius. Sits directly below or within the membership-cta-banner to reinforce sale urgency for VIP flash events.

### Collection Filtering

**`filter-pill`** — Rounded-full chips ({rounded.full}) in {colors.surface-soft} fill with {typography.button-sm} text. Active state switches to transparent background with a 2px {colors.ink} border. Used in a horizontal scroll row above collection grids on mobile, and as a static wrapping row on desktop.

### Product Swatches

**`size-swatch`** — 40×40px hard-cornered ({rounded.none}) tiles with 1px {colors.hairline} border. Selected state: 2px solid {colors.ink}. Out-of-stock: {typography.caption} in {colors.muted} with a diagonal strike rendered via CSS. Aligns with the brand's no-radius design language throughout.

**`color-swatch`** — 24px circular swatches ({rounded.full}) with a 2px {colors.ink} ring at 2px offset for selected state — standard DTC swatch interaction, clean and unornamented.

### Quiz CTA

**`quiz-cta-card`** — A dark ({colors.surface-dark-raised}) card-style block with headline in {typography.title-md} and a hard-cornered CTA in {typography.button-md}. The "Take the Style Quiz" entry point appears persistently across landing pages as the brand's primary personalization hook, often rendered as a 2-column card alongside a membership benefit list.

### Footer

**`footer`** — Full-bleed {colors.surface-dark} with {spacing.section} vertical padding. Column headings in {typography.label-uppercase} (11px, 1.5px letter-spacing, uppercase) provide strong scannable anchors. Links in {typography.body-sm} at {colors.muted} hover to {colors.on-dark}. Social icons and legal copy sit in a separated bottom row. No decorative border-top — the dark background establishes the footer boundary naturally.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart icon; hero headline scales to display-md (40px); filter-pills shift to horizontal scroll row; countdown timer stacks digits vertically |
| Tablet | 744–1128px | 2–3 column product grid; nav shows primary categories only, megamenu replaced by slide-in drawer; hero headline at display-lg (56px); membership banner reduces horizontal padding to {spacing.lg} |
| Desktop | 1128–1440px | 4-column product grid; full megamenu with editorial image panels; hero at display-xl (80px); filter row wraps in place; nav-bar shows full category list with VIP badge |
| Wide | > 1440px | Max-width container (~1440px) centered on wider viewports; hero image zones expand proportionally; product grid stays at 4-column but card images scale up; horizontal padding increases to {spacing.section} or beyond |

### Touch Targets

- All buttons minimum 52px tall, widths scale to content with generous horizontal padding (32px each side minimum)
- Size swatches are 40×40px — meets 44px iOS guideline in the tap-area sense with grid spacing as buffer
- Color swatches at 24px diameter should include at least 8px invisible tap-area expansion via padding
- Nav hamburger icon: 48×48px touch target
- Filter pills: minimum 36px tall; horizontal scroll on mobile allows smaller widths without crowding

### Collapsing Strategy

- Navigation: hamburger drawer on mobile — primary categories as large list items with sub-category expansion; megamenu editorial images are suppressed
- Product grid: 4-col → 3-col (tablet) → 2-col (mobile portrait) → 1-col only on very small screens (< 375px)
- Hero: text stack reflows left-center-aligned; image shifts from side-split to full-bleed underlay with overlay scrim at mobile
- Countdown timer: horizontal digit row on desktop/tablet; vertical stack with larger digits on mobile for legibility
- Filter row: horizontal scroll with fading edge gradient on mobile to signal overflow
- Footer: 4-column link grid collapses to accordion-style expandable sections on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#9d9d9c) was reliably extracted — the site loads its full design token system via JavaScript, preventing static extraction of the complete palette
- CTA accent red (used as cta-accent: #e0393e) is an approximation based on brand visual identity and is not extracted; exact brand hex is unconfirmed
- Primary dark background value (#1c1c1c / #111111) is approximate; actual dark canvas hex could not be confirmed from extraction
- No meta theme-color was present on the page, removing a common fallback for primary brand color
- Complete typography scale (exact font sizes per breakpoint, specific weight ladder) is inferred from GT Pressura's published usage patterns and brand positioning — not extracted from computed styles
- Secondary/accent color palette (if any seasonal or campaign colors exist beyond the core system) is entirely undocumented from this extraction
- Animation and transition values (hover crossfade timing on product cards, drawer slide duration) could not be extracted
