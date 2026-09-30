---
version: alpha
name: "Pearl Paradise"
source_url: "https://www.pearlparadise.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pearl Paradise's in-house grading nomenclature — AAA, AA+, AA — surfaces in product titles and filter panels before the price does, signaling a gemological retailer operating at category-expert depth rather than lifestyle aspiration. The confirmed palette anchor is near-charcoal #313131, deployed on headings and body copy against a white-to-ivory canvas that functions as a photography neutral, not a styled surface; the pearls themselves, lit to reveal overtone and nacre depth, carry all the visual weight. Navigation organizes by pearl species first — Akoya, South Sea, Tahitian, Freshwater — with an Education hub given equal billing alongside shopping, reflecting an audience that arrives knowing what it wants and needs sorting tools over discovery imagery. Typography at display scale leans classical serif, fitting for a brand that publishes harvest reports and grading methodology alongside product listings; system sans-serif handles UI chrome at body sizes to keep page weight manageable across a catalog running to thousands of SKUs. Cards are information-dense by design: pearl type, grade badge, strand length, and price stack vertically inside a {rounded.sm}-cornered container with no decorative furniture, and photography is lit on white to show luster without interference. On the PDP, the Education tab with side-by-side overtone photography and harvest provenance establishes an editorial authority layer absent from volume jewelry competitors. The {rounded.xs}-to-{rounded.sm} range throughout — no pill shapes, no heavy radii — reads as precise and gemologically honest, a restraint that extends to the pearl photography itself. Palette tokens beyond the confirmed charcoal are extrapolated from pearl-category conventions and should be verified against a live site capture.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#9e9e9e"
  ink: "#313131"
  body: "#4d4d4d"
  muted: "#767676"
  hairline: "#e2ddd7"
  canvas: "#ffffff"
  surface-soft: "#f9f6f2"
  surface-card: "#ffffff"
  surface-warm: "#f2ede6"
  on-primary: "#ffffff"
  gold-accent: "#b8985c"
  pearl-cream: "#f7f4ee"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.02em
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  title-lg:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.07em
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  grade-badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.01em

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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.ink}"
    padding: 11px 27px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 42px
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    padding: "{spacing.sm}"
    imageAspectRatio: "1:1"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    gradeBadgePresent: true
  grade-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.grade-badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    layout: "split-left-text-right-image"
    imageSide: right
  pearl-type-filter:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.base}"
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.on-primary}"
  sortby-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 36px
  pdp-spec-table:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    rowBorder: "1px solid {colors.hairline}"
    rowPadding: "{spacing.sm} 0"
  education-tab:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-lg}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
  certification-badge:
    backgroundColor: "{colors.pearl-cream}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 40px
    padding: "0 {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    headlineTypography: "{typography.caption}"
    padding: "{spacing.xxl} 0"
    columns: 4

## Components

### Buttons
**`button-primary`** — Dark charcoal (#313131) fill with white text, all-caps tracked lettering via `{typography.button-md}`, and a tight `{rounded.xs}` corner that reads as precise rather than friendly — fitting for a gemological context. Height 44px with 28px horizontal padding. On hover/press it deepens to `{colors.primary-active}` (#1a1a1a); disabled state uses `{colors.primary-disabled}` neutral gray while retaining white text.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border and matching charcoal text. Geometry is identical to the primary so the two sit side-by-side cleanly (e.g., "Add to Cart" / "Save to Wishlist") without visual competition.

### Text Input
**`text-input`** — White background with a 1px `{colors.hairline}` border at rest, upgrading to 1px `{colors.ink}` on focus. No glow or shadow — the state shift is communicated by border color alone, keeping the aesthetic quiet. Used in search, custom-length request forms, and the contact/inquiry flow.

### Navigation
**`nav-bar`** — 64px-tall white bar with a bottom `{colors.hairline}` separator. Primary navigation items are pearl species (Akoya, South Sea, Tahitian, Freshwater) followed by Education and Sale — species-first ordering signals expert positioning. No mega-menu imagery; dropdowns are text lists only. Logo anchors top-left; cart/account icons top-right.

### Product Cards
**`product-card`** — White `{rounded.sm}` card. A square 1:1 pearl strand photograph occupies the full card width — white-lit to show luster and overtone. Below the image: grade badge, pearl type and strand length in `{typography.title-md}`, and price in `{typography.price-display}` (22px Georgia). No hover-state animation; the card is static to keep the UI transparent in favor of product photography.

**`grade-badge`** — Small warm-surface (`{colors.surface-warm}`) label with all-caps grade text — AAA, AA+, AA — in `{typography.grade-badge}`. Positioned above the product title rather than overlaid on the image, preserving photograph clarity. The badge is the most brand-specific UI element on the listing page; its presence signals quality sorting is built into the catalog structure.

### Hero
**`hero-banner`** — Split layout: headline in `{typography.display-xl}` serif left-anchored with a single `button-primary` CTA below; pearl strand photography fills the right half on white. No gradient overlay, no image darkening — the white background of the photography merges with the page canvas. On mobile, image moves below the text block with a full-width button.

### Filters
**`pearl-type-filter`** — Horizontal pill-button filter row at the top of collection pages. Inactive state: `{colors.surface-soft}` background with `{colors.ink}` text. Active state inverts to charcoal fill with white text, the same visual language as the primary button. Filter dimensions: pearl type, price, strand length, grade, size in millimeters, shape. No sidebar — horizontal bar keeps the grid wide on desktop.

**`sortby-dropdown`** — Compact 36px dropdown right-aligned to the filter bar. White fill, `{colors.hairline}` border. Options: Featured, Price: Low to High, Price: High to Low, Newest.

### PDP
**`pdp-spec-table`** — Two-column spec table (label / value) with `{colors.hairline}` row separators and no outer border. Labels in `{typography.caption}` muted gray; values in `{typography.body-sm}` charcoal. Rows typically include: Pearl Type, Origin, Size (mm), Grade, Luster, Surface, Nacre Thickness, Shape, Body Color, Overtone, Clasp, Strand Length, Metal Type.

**`education-tab`** — Warm-surface (`{colors.surface-warm}`) section on the PDP, below the spec table. Headline in `{typography.title-lg}` Georgia serif; body prose in `{typography.body-md}`. Contains side-by-side overtone comparison photographs and grading methodology prose — the primary trust-signal element for high-AOV purchases.

**`certification-badge`** — Pearl-cream (`{colors.pearl-cream}`) bordered box with a 1px `{colors.hairline}` edge. Body-sm type with gemologist curation or quality-guarantee language. Appears in the PDP sidebar and in the cart review step before checkout.

### Search
**`search-bar`** — 40px height, `{colors.hairline}` border, `{colors.surface-soft}` fill. Magnifier icon left-anchored; inline clear button appears on text entry. Sits in the nav bar on desktop; expands to full-width on mobile.

### Footer
**`footer`** — Full-width charcoal (#313131) background with white links and text. Four columns on desktop: Company, Learn, Shop, Customer Service. Link text in `{typography.body-sm}`; section labels in `{typography.caption}` all-caps with letter-spacing. Collapses to stacked accordions on mobile with charcoal chevron indicators.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter bar scrolls horizontally; hero image moves below headline; nav collapses to hamburger; footer becomes stacked accordions; sticky Add to Cart bar at bottom of PDP viewport |
| Tablet | 744–1128px | Two-column product grid; filter bar remains horizontal but wraps to two rows if needed; split hero layout maintained at reduced proportions |
| Desktop | 1128–1440px | Three-column product grid; full horizontal filter bar in a single row; 64px nav with all species links visible; split hero at full proportions |
| Wide | > 1440px | Four-column product grid; layout constrained to 1440px max-width and centered; whitespace margins grow proportionally |

### Touch Targets
- All filter pill buttons minimum 44px tall on touch viewports
- Grade badge is display-only — not an interactive target
- Sortby dropdown minimum 44px height on mobile
- Add to Cart button renders full-width (100%) on mobile PDP
- Nav hamburger icon minimum 44×44px touch area

### Collapsing Strategy
- Nav: hamburger icon at < 744px; full horizontal species link row at ≥ 744px
- Filters: horizontal scrollable pill row persists on all breakpoints; no sidebar drawer at any breakpoint
- PDP: spec table, education tab, and certification badge stack vertically below the main product image on mobile; sticky bottom bar ("Add to Cart — $X") appears fixed to the viewport bottom
- Footer: four columns collapse to single-column accordions on mobile; each section header is a full-width tap target

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site — the Cloudflare challenge page ("Just a moment...") blocked full extraction; all palette tokens except `colors.primary` and `colors.ink` are inferred from pearl-category conventions and must be verified against a live capture
- No custom font families detected; the system font stack was the only font data returned — display typography may use a licensed serif (Playfair Display, Georgia Pro, or similar) loaded via JS after the bot check; `{typography.display-xl}` and `{typography.title-lg}` using Georgia above are inferred from category conventions
- Meta theme-color absent; actual CTA button color unconfirmed — charcoal (#313131) is used as primary but a warm gold or deep navy accent may be the real button color
- `{colors.gold-accent}` (#b8985c) is a category-convention infer, not an extracted value
- Hover/focus transition durations, box-shadow tokens, and animation curves are entirely unconfirmed
- Mobile navigation pattern (hamburger vs. species-tab bottom bar) is unconfirmed
- Cart, checkout, account, and wishlist page UI not captured
- Whether a custom typeface is licensed and served from a CDN cannot be determined from extraction results
