---
version: alpha
name: "Dekor Lighting"
source_url: "https://www.dekorlighting.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Purple appears where you'd expect amber — DEKOR Lighting's brand voltage runs through a layered violet sequence (pale #d6c6df at rest, saturated #82559f at depth, near-midnight #554163 for shadow states) that repositions deck and landscape fixtures as an interior design decision rather than a contractor supply run. The near-black ink (#1c1c1c) anchors the visual field while a warm light-gray canvas (#eeeeee) keeps the palette from reading dark-room oppressive; together they create a gallery tension that lets product photography lead without the page competing for attention. Baskerville serif carries all display headlines — an editorial choice unusual for a Shopify outdoor-products store — lending old-world authority to what could easily dissolve into category commodity. Nunito Sans takes over at body scale, offering rounded letterforms that welcome first-time installers alongside seasoned landscapers. The typographic hierarchy is generous: display headlines push to 52px while body copy rests at 16px with 1.6 line-height, and vertical rhythm is controlled by 48–64px section breathing. Buttons hold a moderate {rounded.sm} rather than pill-shaped, suggesting precision engineering over consumer softness. The primary purple (#9d79b3) appears on primary CTAs, active nav indicators, badge fills, and left-accent bars on guide cards — always as signal, never as wash. Neutrals carry the structural load: #cfcfcf handles hairlines and card borders, #555555 carries secondary text, and #303030 grounds body copy, forming a three-tier gray hierarchy that prevents flatness without adding color noise. Product badges (BEST SELLER, NEW, SALE) live in the purple family, visually linking commerce signals back to brand identity. The overall impression is a lighting manufacturer whose own site demonstrates the quality of light it sells — organized, luminous, and unhurried.

colors:
  primary: "#9d79b3"
  primary-active: "#82559f"
  primary-deep: "#554163"
  primary-hover: "#a381b8"
  primary-disabled: "#d6c6df"
  primary-soft: "#b89ec9"
  ink: "#1c1c1c"
  body: "#303030"
  muted: "#555555"
  muted-soft: "#727272"
  hairline: "#cfcfcf"
  hairline-soft: "#eeeeee"
  canvas: "#eeeeee"
  canvas-white: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  neutral-mid: "#9d9d9d"
  success: "#4a7c59"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Times New Roman', Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Times New Roman', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Baskerville, 'Times New Roman', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-uppercase:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  badge:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'Nunito Sans', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0.3px
    textTransform: uppercase

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
    padding: "14px 28px"
    height: 48px
    hover:
      backgroundColor: "{colors.primary-active}"
    active:
      backgroundColor: "{colors.primary-deep}"
    disabled:
      backgroundColor: "{colors.primary-disabled}"
      textColor: "{colors.on-primary}"

  button-secondary:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: "12px 26px"
    height: 48px
    hover:
      backgroundColor: "{colors.primary-disabled}"

  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "10px 20px"

  text-input:
    backgroundColor: "{colors.canvas-white}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 44px
    padding: "0 {spacing.base}"

  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas-white}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "none"
    logo:
      maxHeight: 36px
    activeIndicator:
      color: "{colors.primary}"
      height: 2px

  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: "0 {spacing.base}"
    iconColor: "{colors.muted}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    shadow: "0 2px 8px rgba(28,28,28,0.08)"
    image:
      aspectRatio: "4/3"
      rounded: "{rounded.sm}"
      backgroundColor: "{colors.canvas}"
    productName:
      typography: "{typography.title-sm}"
      textColor: "{colors.ink}"
    price:
      typography: "{typography.price-display}"
      textColor: "{colors.ink}"
    comparePrice:
      typography: "{typography.body-sm}"
      textColor: "{colors.muted}"
      textDecoration: line-through
    badge:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
      typography: "{typography.badge}"
      rounded: "{rounded.xs}"
      padding: "3px 8px"

  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas-white}"
    minHeight: 520px
    padding: "{spacing.section} 0"
    overlay: "linear-gradient(to right, rgba(28,28,28,0.72) 0%, rgba(28,28,28,0.2) 100%)"
    headline:
      typography: "{typography.display-xl}"
      textColor: "{colors.canvas-white}"
    subheadline:
      typography: "{typography.body-md}"
      textColor: "{colors.hairline}"
    cta:
      component: button-primary

  collection-badge:
    typography: "{typography.badge}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    variants:
      new:
        backgroundColor: "{colors.primary}"
      bestseller:
        backgroundColor: "{colors.primary-active}"
      sale:
        backgroundColor: "{colors.primary-deep}"
      instock:
        backgroundColor: "{colors.success}"

  spec-row:
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
    label:
      typography: "{typography.spec-label}"
      textColor: "{colors.muted}"
    value:
      typography: "{typography.body-sm}"
      textColor: "{colors.ink}"
    row:
      backgroundColor: "{colors.surface-soft}"
    alternateRow:
      backgroundColor: "{colors.canvas-white}"

  install-guide-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.primary-disabled}"
    padding: "{spacing.xl}"
    accentBar:
      width: 4px
      backgroundColor: "{colors.primary}"
      rounded: "{rounded.xs}"
    title:
      typography: "{typography.title-md}"
      textColor: "{colors.ink}"
    body:
      typography: "{typography.body-md}"
      textColor: "{colors.body}"
    stepNumber:
      typography: "{typography.display-sm}"
      textColor: "{colors.primary-disabled}"

  finish-swatch:
    size: 32px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    activeBorder: "2px solid {colors.primary}"
    tooltip:
      typography: "{typography.caption}"
      backgroundColor: "{colors.ink}"
      textColor: "{colors.canvas-white}"
      rounded: "{rounded.xs}"

  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    fontWeight: 700
    height: 40px
    padding: "0 {spacing.base}"
    closeButton:
      textColor: "{colors.on-primary}"
      size: 20px

  category-tile:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    overflow: hidden
    image:
      aspectRatio: "1/1"
    label:
      typography: "{typography.title-sm}"
      textColor: "{colors.ink}"
      backgroundColor: "{colors.canvas-white}"
      padding: "{spacing.sm} {spacing.base}"
    hover:
      shadow: "0 4px 20px rgba(157,121,179,0.25)"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.hairline}"
    padding: "{spacing.section} 0 {spacing.xl}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.primary-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas-white}"
    dividerColor: "{colors.muted}"
    copyrightTypography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — Purple fill (#9d79b3) at 48px tall with 8px radius corners. Hover darkens to the active-purple (#82559f); active press goes deeper to #554163; disabled washes to pale lavender (#d6c6df) while holding white text. The Nunito Sans label at 15px bold with 0.5px letter spacing reads precise without going uppercase.

**`button-secondary`** — White fill with a 2px solid purple border and matching purple label text. Hover floods the interior with the pale-lavender disabled tint to signal proximity before click. Used for secondary CTAs on product detail pages (e.g. "Download Spec Sheet," "Compare Products").

**`button-ghost`** — Transparent with a 1px #cfcfcf border and ink text. Appears on light surfaces for non-urgent actions like "View All" or pagination, keeping visual weight low within content-dense listing pages.

### Navigation

**`nav-bar`** — Full-width #1c1c1c bar, 64px tall. White nav links in Nunito Sans semibold 14px. The active category is underlined with a 2px #9d79b3 stripe. Logo caps at 36px height. The high-contrast dark bar creates a clear visual frame without competing with hero imagery below.

**`search-bar`** — Full-pill shape (`{rounded.full}`) on a #f5f5f5 field, 40px tall, with a muted gray (#555555) search icon. Sits inline in the nav row on desktop; collapses to an icon-tap that expands a full-width overlay on mobile.

### Product Cards

**`product-card`** — White card with 12px radius and a 1px #cfcfcf border, shadow at 2px blur/8px spread at 8% opacity. Image area holds a 4:3 ratio over a warm #eeeeee canvas background. Product name in Nunito Sans bold 15px; price in the price-display style at 22px bold. Collection badges attach to the top-left corner in purple with 4px radius and uppercase Nunito 10px at 0.8px tracking.

### Hero Banner

**`hero-banner`** — #1c1c1c base with a left-anchored directional gradient overlay; minimum 520px height. Headline in Baskerville at 52px creates immediate editorial contrast against the dark field. Subheadline drops to Nunito Sans 16px in #cfcfcf. Primary CTA sits below at standard purple fill. On mobile, text stacks above a full-width cropped image rather than overlaying it.

### Badges

**`collection-badge`** — Uppercase Nunito Sans 10px, 0.8px letter spacing, 4px radius, white text. Four color variants: primary purple (#9d79b3) for NEW, active-purple (#82559f) for BEST SELLER, deep purple (#554163) for SALE, and tonal green for IN STOCK. All share the same padding and cap-height rhythm.

### Spec Table

**`spec-row`** — Alternating rows of #f5f5f5 and white, 1px #cfcfcf bottom border. Label column in uppercase Nunito Sans 12px, 0.3px tracking, muted gray; value column in regular 14px ink. Used on product detail pages for wattage, lumen output, IP rating, color temperature, and wire gauge.

### Install Guide Cards

**`install-guide-card`** — White card with 12px radius, a 1px pale-lavender (#d6c6df) border, and a 4px left accent bar in #9d79b3. Step numbers render in Baskerville display-sm at #d6c6df — the faint oversized serif numeral creates depth without distracting from instructional content. Body in Nunito Sans 16px at body color (#303030).

### Finish Swatches

**`finish-swatch`** — 32px circular swatches with a 2px transparent border at rest; 2px purple (#9d79b3) border when active. A dark #1c1c1c tooltip with white 12px caption appears on hover to name the finish. Used for housing-color selection on fixtures offered in matte black, brushed nickel, or bronze.

### Promo Banner

**`promo-banner`** — Full-width 40px bar in primary purple (#9d79b3) above the nav. White Nunito Sans bold body-sm text centered. Close button right-aligned in white. Used for free-shipping thresholds, seasonal sales, and new collection launches.

### Category Tiles

**`category-tile`** — Square 1:1 tiles with 12px radius. Label bar at bottom in white fill, Nunito Sans bold 15px, ink text, 8px×16px padding. Hover elevates a soft purple-tinted shadow (rgba 157,121,179 at 0.25) to signal interactivity without color shift. Used in the homepage shop-by-category grid.

### Footer

**`footer`** — Mirrors the nav in #1c1c1c. White section headings in Nunito Sans bold 15px; #cfcfcf body links at 14px; hover transitions to soft purple (#b89ec9). A 1px #555555 rule separates columns from the copyright row. Copyright and legal in caption 12px.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero text stacks above cropped image with no overlay; nav collapses to hamburger drawer; search becomes icon-tap overlay; footer columns stack vertically; promo banner text wraps |
| Tablet | 744–1128px | Two-column product grid; hero overlay layout restored; nav shows primary links with overflow dropdown for sub-categories; spec table scrolls horizontally |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with mega-dropdown; hero at full 520px min-height; install guide cards in two-column grid |
| Wide | > 1440px | Content max-width ~1340px centered; hero image scales but text column holds fixed width; product grid holds at four columns |

### Touch Targets

- All buttons minimum 44×44px tap zone
- Finish swatches padded to 44px touch area even though visible circle is 32px
- Nav hamburger icon 44×44px tap zone
- Footer links padded to minimum 44px row height on mobile
- Badge-area on product cards not independently tappable — parent card is the tap target

### Collapsing Strategy

- Primary navigation: full horizontal links with hover dropdowns (desktop) → hamburger drawer with accordion category groups (mobile)
- Search: inline pill bar in nav row (desktop/tablet) → icon that expands full-width input overlay (mobile)
- Spec table: two-column label/value pairs (desktop) → horizontal scroll container on narrow viewports
- Hero: image-overlay layout (≥744px) → stacked image-below-text (mobile)
- Install guide cards: two-column grid (desktop) → single-column stack (mobile)
- Category tile grid: 4-up (desktop) → 2-up (tablet and mobile)

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- "Baskerville" appears as a system/web font stack entry — DEKOR may use a licensed variant (e.g. Libre Baskerville via Google Fonts) that extraction did not capture; weight and optical size may differ from system Baskerville
- No explicit white (#ffffff) appeared in the top extracted colors — primary canvas assumed to be #eeeeee; product-card and modal backgrounds assumed white from e-commerce convention but not confirmed from computed styles
- Meta theme-color was absent; mobile browser chrome color and PWA manifest color are unknown
- No motion or transition timing tokens extracted — hover fade durations, carousel easing, and drawer animation curves are unspecified
- Exact nav height, logo dimensions, and mega-dropdown structure could not be measured from extraction
- Purple color stop assignments (which specific shade maps to which UI component) are inferred from extraction frequency and order, not from computed DOM styles
- No brand icon set was identified beyond JudgemeIcons (third-party review widget) — SVG style (outline vs. filled, stroke weight) for product-type icons could not be confirmed
