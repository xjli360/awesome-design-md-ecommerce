---
version: alpha
name: "Gozney"
source_url: "https://www.gozney.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Where most kitchen-equipment brands default to white-canvas minimalism, Gozney opens on charcoal (#272c32) — a background color that exists to make fire look more fire-like and molten cheese look more luminous against a screen. The primary CTA red (#c8102e) is not a sale-rack accent but a thermal signal: it appears on every "Shop Now" and "Add to Cart" button with the logic of an oven dial pushed to maximum, and it doubles as the data color for temperature statistics — 950°F printed large enough to register as a boast. Maison Neue Mono handles the numbers that matter most: cook-time readouts, stone temperature claims, weight specs — set in fixed-width columns that read like instrument panels rather than marketing copy, a detail that separates the brand's product pages from every other outdoor-cooking competitor who sets these figures in the same serif or sans as their prose.

  The wider Maison Neue family carries everything else: Demi for structural headings, navigation labels, and uppercase button text held at 0.5px tracking; Book for body descriptions and product features at comfortable 1.6 line-height. The letter-spacing is tight throughout — no airy editorial looseness — giving the typographic system the weight and authority of precision-engineered hardware documentation. Maison Neue Mono is the telling third member: most brands license a display and a text weight and stop there; commissioning the mono variant signals that fixed-width numeric comparison is a designed experience, not a fallback.

  Three extracted colors do heavy structural work: the charcoal (#272c32) anchors the nav and all hero sections, the near-black (#121212) carries body text on light surfaces, and the light gray (#dedede) provides the only visual rest in an otherwise saturated palette. A deep navy (#012169) appears in trust and provenance contexts — "Made in the UK" badges, warranty callouts — adding heritage register without softening the fire-forward primary. Component geometry stays deliberately angular: buttons carry {rounded.xs} at most, product cards are flat-cornered, and the search field is a bare rectangle. Nothing rounds off that would undercut the impression of hardware built to withstand thermal extremes.

  Spacing is generous at section level ({spacing.section}) but compressed inside components, letting product photography dominate the viewport. The nav stays #272c32 regardless of scroll position or page type — it never lightens for interior pages — which holds a single consistent visual register across the entire site: high-heat, technically credible, built for people who take 60-second Neapolitan pizza seriously.

colors:
  primary: "#c8102e"
  primary-active: "#a30d24"
  primary-disabled: "#e8a0ab"
  ink: "#121212"
  body: "#3a3f45"
  muted: "#6b7074"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#ffffff"
  surface-dark: "#272c32"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  navy: "#012169"

typography:
  display-xl:
    fontFamily: "'Maison Neue Demi', sans-serif"
    fontSize: 72px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: -1.5px
  display-md:
    fontFamily: "'Maison Neue Demi', sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'Maison Neue Demi', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  title-md:
    fontFamily: "'Maison Neue Demi', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Maison Neue Demi', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Maison Neue Book', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Neue Book', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue Book', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  mono-spec:
    fontFamily: "'Maison Neue Mono', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  mono-stat:
    fontFamily: "'Maison Neue Mono', monospace"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -1px
  button-md:
    fontFamily: "'Maison Neue Demi', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Maison Neue Demi', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Maison Neue Demi', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  tag:
    fontFamily: "'Maison Neue Demi', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 20px
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
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-secondary-on-dark:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: none
  nav-dropdown:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.tag}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-sm}"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    layout: full-bleed
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 100vh
    paddingX: "{spacing.lg}"
  temperature-stat:
    valueTypography: "{typography.mono-stat}"
    valueColor: "{colors.primary}"
    labelTypography: "{typography.mono-spec}"
    labelColor: "{colors.on-dark}"
  spec-badge:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.mono-spec}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.base}"
  feature-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    iconColor: "{colors.primary}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xl} 0"
    dividerColor: "{colors.hairline}"
  review-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    starColor: "{colors.primary}"
    bodyTypography: "{typography.body-sm}"
    authorTypography: "{typography.caption}"
    authorColor: "{colors.muted}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  trust-badge:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.tag}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xs} {spacing.sm}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headerBackgroundColor: "{colors.surface-dark}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.tag}"
    width: 400px
    titleTypography: "{typography.title-md}"
    itemTypography: "{typography.body-sm}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.tag}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — A flat, nearly cornerless ({rounded.xs}) red block that reads as a control console rather than an invitation. The uppercase Maison Neue Demi label with 0.5px tracking stays legible against #c8102e at 48px height; hover deepens to #a30d24 without a perceptible animation delay, signaling instant response. Disabled state fades fill to #e8a0ab while keeping uppercase label structure intact. This button appears on product hero sections, add-to-cart flows, and any primary conversion moment.

**`button-secondary`** — Transparent fill with a 1px solid border matching the foreground color, used for comparative CTAs ("Learn More", "Compare Models") placed alongside a primary button. On dark surfaces ({colors.surface-dark}), border and label invert to white via `button-secondary-on-dark`; geometry and padding are identical to the primary variant to preserve visual rhythm in button pairs. Never uses a filled background so it never competes with the red primary.

**`button-ghost`** — Text only, no border, on-dark color. Reserved for navigation sub-actions like "View All" in dropdown menus and carousel arrow labels where a bordered button would crowd the dark panel. Uses {typography.button-sm} uppercase.

### Text Input

**`text-input`** — Zero border radius, matching the brand's angular hardware posture. The focus state upgrades the border from {colors.hairline} to {colors.ink} rather than adding a color ring, keeping the form palette monochromatic. Used in newsletter signup footer strips, search fields on light-canvas pages, and address forms at checkout. Placeholder text renders in {colors.muted}.

### Navigation

**`nav-bar`** — Holds #272c32 at all times regardless of scroll position or underlying page color — it never lightens to white for interior pages. Navigation links use {typography.nav-link}: Maison Neue Demi at 14px, 0.3px tracking, white. Cart and account icons sit right-aligned with {spacing.sm} gap between them. An `announcement-bar` in {colors.primary} sits above the nav bar during promotions, adding 40px to the total header height.

**`nav-dropdown`** — Mega-menu panel in the same #272c32, full viewport width, dropping flush below the nav bar with no shadow or gap. Product categories appear in a 3-column grid: category headers in {typography.tag} white, sub-links in {typography.body-sm} at 70% white opacity with full-opacity hover. No image thumbnails in the dropdown — links only, keeping the panel fast and text-forward.

### Product Card

**`product-card`** — No border radius, no drop shadow; the card boundary is implied by white canvas between a dark or soft-gray page section. Product image fills a 4:3 aspect ratio container with object-fit cover. Name uses {typography.title-sm} and price uses {typography.title-sm} in a tight two-line stack below the image. Hover overlays a semi-transparent #272c32 scrim on the image with a "Quick Shop" trigger centered in {typography.button-sm}. Bestseller or "New" labels use {typography.tag} in a {colors.primary} block placed flush top-left on the image.

### Hero

**`hero`** — Full-bleed, viewport-height section on {colors.surface-dark}, with fire or food photography as a background layer composited at 50–70% opacity so the charcoal reads through. The headline runs {typography.display-xl} in white with no text shadow; a subhead sits below in {typography.body-md} at 70% white opacity. Two buttons — `button-primary` and `button-secondary-on-dark` — sit in a horizontal pair with {spacing.md} gap between them. Content vertically anchors around 45% from the top rather than strict center to leave room for fire imagery at the bottom of the frame.

### Temperature Stat

**`temperature-stat`** — The brand's most distinctive display component. The numerical value ("950") renders in {typography.mono-stat} colored {colors.primary}; the unit ("°F" / "°C") and a one-line descriptor label appear below in {typography.mono-spec} white. Monospace fixed-width means multiple stats placed side by side — temperature, preheat time, cook time, weight — column-align without manual spacing intervention. Used in product hero sections and the technical specification band.

### Spec Badge

**`spec-badge`** — A small, corner-free rectangle using {typography.mono-spec} on {colors.surface-dark} background. Groups a label and value inline: "STONE TEMP · 950°F". Rows of these badges build the technical spec strip that appears below the product hero image, functioning as a scannable data sheet rather than a prose feature list. No border, no shadow — the dark fill differentiates them from the surrounding canvas.

### Feature Strip

**`feature-strip`** — A {colors.surface-soft} horizontal band providing a typographic rest between rich imagery sections. Four to six icon-plus-label pairs distribute across the full width, separated by 1px {colors.hairline} vertical rules. Icons render at 24px in {colors.primary}. The title uses {typography.title-sm} and the descriptor uses {typography.body-sm} in {colors.ink}. No photography; this band exists to state credibility claims ("Ships Free", "2-Year Warranty", "5-Star Rated") without visual noise.

### Review Card

**`review-card`** — Flat-bordered (1px {colors.hairline}), no elevation. Stars render in {colors.primary} as SVG fills; a numeric rating in {typography.title-sm} precedes the star row. Review body uses {typography.body-sm} in {colors.ink}. Author name and "Verified Purchase" tag render in {typography.caption} in {colors.muted}. Cards appear in a horizontal scroll carousel on mobile and a 3-column grid on desktop; no carousel controls on desktop.

### Trust Badge

**`trust-badge`** — Navy ({colors.navy}) rectangle with {typography.tag} uppercase white label. Used for "FREE SHIPPING", "LIFETIME WARRANTY", and "MADE IN THE UK" claims arranged in a horizontal badge strip above the footer or below the product hero. The navy creates a third register distinct from both the primary red and dark charcoal — it reads as institutional credibility rather than promotional heat.

### Cart Drawer

**`cart-drawer`** — Right-edge slide-in panel, 400px wide. The header uses {colors.surface-dark} with "YOUR CART" in {typography.tag} white, preserving the dark brand register inside the transactional layer. The body switches to {colors.canvas} for line items in {typography.body-sm} {colors.ink}. Subtotal row uses {typography.title-md}. The checkout CTA is a full-width `button-primary` pinned to the drawer bottom, no margin from the edges.

### Footer

**`footer`** — Full-width {colors.surface-dark} block with four link columns. Column headers use {typography.tag} in white; links use {typography.body-sm} in white at 70% opacity with full-opacity hover. Social icons sit bottom-left as 20px SVGs in white. Legal copy and cookie preferences align bottom-right in {typography.caption} at 50% white opacity. The footer carries the same charcoal as the nav, closing the page with a consistent dark frame.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger + centered logo + cart icon; hero headline drops to `display-sm`; product cards full-width stacked; spec badges horizontal-scroll strip (no wrapping); temperature stats stack vertically; footer sections collapse to accordion; cart drawer goes full-width (100vw) |
| Tablet | 744–1128px | 2-column product grid; nav shows logo + hamburger with mega-menu as full-screen overlay; hero text-block left-aligned at 60% width; temperature stats in 2×2 grid; feature strip becomes 2-column icon grid |
| Desktop | 1128–1440px | Full 3-column product grid; mega-menu fully expanded inline; hero content at 50% viewport width left-aligned; spec badge row horizontal; review cards 3-column grid; cart drawer 400px fixed width |
| Wide | > 1440px | Content max-width capped at 1440px with symmetric auto margins; hero background scales to cover without upscaling; product grid expands to 4 columns; temperature stat section gains additional breathing room via increased column gap |

### Touch Targets

- All nav links minimum 44×44px tap target via padding; visible hit area may appear smaller
- Cart, account, and hamburger icon buttons: 48×48px minimum
- Product card tap area covers full image + title + price block — no separate "Add to Cart" required on the listing page itself
- Announcement bar CTA link: full 40px row height is tappable, no separate button needed
- Spec badges in horizontal-scroll strip: 44px minimum height to allow thumb scrubbing

### Collapsing Strategy

- Navigation: hamburger at < 1128px; mega-menu becomes full-viewport slide-down overlay at tablet and mobile
- Product grid: 4-col → 3-col → 2-col → 1-col descending through breakpoints
- Spec badge strip: horizontal scroll with overflow-x auto on mobile — never wraps, preserves the "instrument panel" read
- Temperature stat display: horizontal row on tablet and desktop, vertical stack on mobile
- Feature strip: 2-column grid (icon above, text below each) on mobile; horizontal row on desktop
- Footer: 4-column → 2-column (tablet) → single-column accordion (mobile) with expand/collapse per section; social icons move to above the legal row on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only five hex values extracted; hover states, focus rings, error colors, and success confirmation colors are inferred from brand conventions and not observed directly on-site
- Exact numeric font weights for Maison Neue variants not captured in extraction — "Book" mapped to 400 and "Demi" to 600 per standard Maison Neue naming; verify against loaded font assets
- Maison Neue Mono usage context (which specific components and which data values use it) inferred from brand positioning; exact CSS applications were not captured
- No border-radius values were extractable — the angular geometry is inferred from product photography and hardware brand conventions; actual px values may differ from {rounded.xs}/{rounded.sm} choices here
- Navy (#012169) role in the live UI was not directly observed; its assignment to trust badges and provenance claims is inferred rather than confirmed
- Animation and transition durations for hover states, cart drawer slide, and dropdown open/close not extracted
- Mobile breakpoint pixel values are inferred from Shopify theme defaults rather than observed in site CSS
- Price display formatting (currency symbol weight, sale vs. original price treatment) not captured
