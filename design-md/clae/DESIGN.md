---
version: alpha
name: "Clae"
source_url: "https://clae.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every sole on a CLAE sneaker carries a material origin story — recycled plastic bottles, natural rubber, chrome-free leather — and the brand's visual system is built to make that traceability feel effortless rather than preachy. The defining voltage is #ff6600, a traffic-cone orange that hits CTAs, sale badges, and hover states with the same blunt confidence you'd find on the tongue of a construction worker's boot. It reads as industrial rather than fashionable, which is exactly the point: CLAE (an acronym for Clean, Life, Art, Earth) wants sustainability to feel like craft, not virtue-signaling. That orange sits against a near-black ink of #0f172a — a Tailwind slate-950 derivative, not a pure black — giving the palette a slightly blue-shifted shadow that keeps everything from reading as flat CMYK dark. The secondary tone, #006699, a mid-depth teal-blue, handles informational links and complementary accent work without competing with the orange. Canvas is #f8fafc rather than pure white, a barely-there off-white that softens the high-contrast pairing. Montserrat carries all display and body text — geometric, dependable, legible at small sizes on product description copy, and punchy enough at weight 700 to sell a product title without custom letterforms. Spacing is generous for an e-commerce context: large product imagery is given room to breathe, filter rails collapse cleanly, and the checkout flow avoids the cramped multi-column layouts common to footwear brands. Rounded corners sit at a restrained {rounded.sm} for buttons and cards — just enough to soften without going pill-shaped, keeping the industrial design language intact. The sustainability credential block — a row of material badges (recycled, vegan, natural) — appears on every PDP and uses {colors.surface-soft} chip backgrounds with {colors.primary} icon accents to communicate eco-sourcing without interrupting the purchase flow.

colors:
  primary: "#ff6600"
  primary-active: "#e55a00"
  primary-disabled: "#ffb380"
  secondary: "#006699"
  secondary-active: "#005580"
  ink: "#0f172a"
  body: "#1e293b"
  muted: "#64748b"
  hairline: "#dedede"
  hairline-soft: "#cececd"
  canvas: "#f8fafc"
  surface-soft: "#f1f5f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  eco-badge-bg: "#e8f4f0"
  eco-badge-text: "#1a5c45"
  sale-badge-bg: "#ff6600"
  sale-badge-text: "#ffffff"
  scrim: "#0f172a"

typography:
  display-xl:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  eco-label:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
    textTransform: uppercase
  price-display:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Montserrat', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    hoverBackground: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
    hoverBackground: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
    activeIndicatorColor: "{colors.primary}"
  mega-menu:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    columnGap: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "4/3"
    padding: "{spacing.md}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    hoverShadow: "0 4px 16px rgba(15,23,42,0.10)"
  product-card-badge:
    backgroundColor: "{colors.sale-badge-bg}"
    textColor: "{colors.sale-badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.sm}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    overlayScrim: "rgba(15,23,42,0.45)"
  eco-badge:
    backgroundColor: "{colors.eco-badge-bg}"
    textColor: "{colors.eco-badge-text}"
    typography: "{typography.eco-label}"
    rounded: "{rounded.full}"
    padding: 5px 12px
    iconSize: 14px
  material-tag-row:
    display: flex
    gap: "{spacing.sm}"
    padding: "{spacing.md} 0"
    itemBackground: "{colors.surface-soft}"
    itemTypography: "{typography.caption}"
    itemRounded: "{rounded.xs}"
    itemPadding: 4px 10px
  size-selector:
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    inactiveBackground: "{colors.canvas}"
    inactiveTextColor: "{colors.body}"
    unavailableBackground: "{colors.surface-soft}"
    unavailableTextColor: "{colors.hairline}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.hairline}"
    activeBorder: "1.5px solid {colors.ink}"
    size: 44px
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    unselectedBorder: "1.5px solid {colors.hairline}"
    gap: "{spacing.sm}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    gap: "{spacing.xs}"
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    activeBorder: "1px solid {colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    padding: 10px 16px
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    borderTop: "none"
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 52px
    width: "100%"
    hoverBackground: "{colors.primary-active}"

## Components

### Buttons
**`button-primary`** — A 48px-tall block filled with CLAE's #ff6600 orange, uppercase Montserrat 700 at 14px with 0.5px letter-spacing. Hover darkens to #e55a00; disabled washes out to #ffb380 while maintaining white text. Used for Add to Cart, Shop Now, and newsletter subscription.

**`button-secondary`** — Same geometry as primary but inverted: white fill with a 1.5px #0f172a ink border. Hover softens background to {colors.surface-soft}. Appears alongside the primary CTA for secondary actions like "View Details" or "Save to Wishlist."

**`button-ghost`** — Transparent background, #ff6600 text, no border, no radius. Used for inline text actions — "See all styles," "Load more," filter resets — where a full button frame would crowd the layout.

### Text Input
**`text-input`** — 48px height, {rounded.sm}, 1.5px border in {colors.hairline} resting, upgrading to {colors.ink} on focus. Placeholder text in {colors.muted}. Used across search, email capture, and checkout form fields. No box-shadow on focus — border color shift is the sole focus signal, keeping the form aesthetic flat and industrial.

### Navigation
**`nav-bar`** — 64px tall on {colors.canvas} with a 1px {colors.hairline} bottom border. Logo anchored left at 28px height. Nav links in all-caps Montserrat 600 13px with 0.3px tracking. Active category underlined with a 2px {colors.primary} bar. Cart icon shows item count badge in {colors.primary}. Collapses to hamburger on mobile with a full-screen slide-over drawer.

**`mega-menu`** — Full-width dropdown on {colors.surface-card} with {colors.hairline} border top, {spacing.xl} padding, and product category columns with supporting editorial imagery. Typography drops to {typography.body-sm} for sub-links.

### Product Card
**`product-card`** — White card with {rounded.sm}, 4:3 image ratio, hover lift of `0 4px 16px rgba(15,23,42,0.10)`. Product name in {typography.title-sm}, price in {typography.price-sm}. Quick-add swatch dots appear on hover below the image. The `product-card-badge` (SALE / NEW) clips to the top-left corner in {colors.primary} orange with all-caps badge type.

### Hero
**`hero`** — Full-bleed image with a 45% slate-navy scrim (`rgba(15,23,42,0.45)`) that darkens product imagery enough for the white headline to pass WCAG AA without washing the photograph. Headline in {typography.display-xl}, a 48px/800-weight Montserrat statement. Min-height 560px. CTA button sits below the subhead in the {button-primary} treatment.

### Eco Credentials
**`eco-badge`** — Pill-shaped chip in {colors.eco-badge-bg} (a soft sage-green tint) with {colors.eco-badge-text} text in all-caps {typography.eco-label}. Each badge pairs a 14px icon (leaf, droplet, recycled-arrow) with a label like "RECYCLED" or "VEGAN." Appears as a horizontal scroll row at the top of every PDP.

**`material-tag-row`** — A flex row of small rectangular chips in {colors.surface-soft}, each naming a specific material origin ("EcoFreeze Rubber," "rPET Lining"). Typography is {typography.caption}. Gap is {spacing.sm}. Positioned directly below the eco-badge row.

### Size & Color Selectors
**`size-selector`** — 44×44px square tiles with {rounded.xs}. Unselected: white fill, {colors.hairline} border. Selected: {colors.ink} fill, white text. Unavailable: {colors.surface-soft} fill, strikethrough text in {colors.hairline}. Grid wraps at 5 tiles per row on desktop, 6 on mobile.

**`color-swatch`** — 28px circular swatches with a 2px {colors.ink} ring on selected state, 1.5px {colors.hairline} ring at rest. Gap between swatches is {spacing.sm}. Tooltip shows colorway name on hover.

### Search
**`search-bar`** — Inline bar in {colors.surface-soft}, 44px height, {rounded.sm}. Magnifier icon in {colors.muted}. On activation expands to full-width overlay with predictive results below. Category suggestions appear as {filter-pill} chips in a row beneath the input.

### Filters
**`filter-pill`** — Pill-shaped filter chip at {rounded.full} for category, size, color, and material filters. Resting state is white with a light border; active inverts to {colors.ink} fill with white text. No dropdown — CLAE uses inline filter pills in a horizontal scroll on mobile rather than a sidebar.

### Footer
**`footer`** — Full-width {colors.ink} block. Column headings in {typography.title-sm} white. Links in {typography.body-sm} at {colors.hairline} tone, turning {colors.primary} orange on hover. Social icons row above the legal strip. Newsletter input uses an inline button-primary configuration.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-screen slide-over; hero drops to 420px min-height; eco-badge row horizontally scrollable; size grid 6-across; filter pills in horizontal scroll strip |
| Tablet | 744–1128px | 2-column product grid; nav collapses to icon row with label; hero 480px; mega-menu replaced with accordion drawer; PDP layout stacks image above details |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-menu nav; hero 560px; PDP splits 60/40 image/detail; sidebar filters appear |
| Wide | > 1440px | Max content width 1440px, side padding grows to {spacing.section}; 4-column product grid maintained; hero stays 560px with wider image bleed |

### Touch Targets
- All size selector tiles minimum 44×44px
- Color swatches padded to 44px tap zone despite 28px visual size
- Nav hamburger icon minimum 44×44px touch area
- Filter pills minimum 36px height on mobile with 8px vertical padding
- Add-to-cart button full-width at 52px height on mobile

### Collapsing Strategy
- Mega-menu collapses to full-screen slide-over drawer with accordion sub-menus at < 1128px
- Two-column PDP (image + details) stacks vertically below 1128px
- Desktop sidebar filters become a horizontal pill-strip at top of grid below 1128px
- Material tag row clips to 2 rows with "show more" toggle below 744px
- Footer columns (4-up desktop) collapse to 2-up tablet, 1-up mobile accordion

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No design tokens or CSS custom properties were extractable — palette sourced entirely from top hex extraction; mid-range grays (body text, muted states) derived from Tailwind slate-600 analogs consistent with the #0f172a/#1e293b family
- Font weights for Montserrat beyond 400/700 not confirmed from extraction; 600 and 800 weights assumed from common Montserrat usage patterns
- Exact button border-radius not confirmed; {rounded.sm} (8px) inferred from screenshot norms for footwear e-commerce
- Hover/active state colors for #006699 secondary are derived (–15% lightness), not extracted
- Animation/transition specs (carousel timing, menu slide speed, hover fade duration) not available from static extraction
- Wishlist, loyalty program, and account dashboard UI patterns not observed in extraction
- Mobile navigation drawer visual treatment (overlay opacity, slide direction) not confirmed
