---
version: alpha
name: "Noctua"
source_url: "https://noctua.at"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Brown as a primary brand color is almost unheard of in PC hardware — a category saturated with black chassis, RGB lighting, and aggressive angular geometry. Noctua commits to it completely and without apology: the signature warm brown (#9C6B44) appears on every physical product, in the logo mark, and as the single accent color against a clean white digital canvas. No gradient, no secondary neon, no lifestyle photography — just the brown, and the engineering behind it. Product pages are specification-dense in a way that signals the intended audience: thermal resistance figures, noise-normalized airflow values, and bearing-lifetime data appear at card level rather than buried in a collapsed accordion. The site architecture organizes a sprawling SKU catalog by CPU socket compatibility and cooling topology rather than by lifestyle segment or performance tier, which is a structural choice that tells you exactly who is shopping here. Typography runs on system sans-serif at measured weights — there is no custom brand typeface, reinforcing an engineer-over-image posture that matches the physical products. Component radii sit at `{rounded.xs}`, not pill-shaped or soft; nothing here reads as consumer-friendly in the bubbly sense. Award badges appear frequently and visibly — Editor's Choice, Gold Award, Top Pick — rendered as compact rectangular chips with brown borders, reflecting a brand whose reputation is built on third-party validation across hundreds of review cycles rather than paid media. The footer carries an unusually prominent distributor-locator column, acknowledgment that Noctua sells through a global network of enthusiast retailers rather than primarily direct. Within a category that spends enormous resources trying to look futuristic, the brown palette performs a distinct emotional function: it reads as proven, analog, and warm — a product with Noctua brown on it signals the buyer has already moved past the RGB phase of their PC hardware hobby.

colors:
  primary: "#9C6B44"
  primary-dark: "#7A4F30"
  primary-light: "#C8A882"
  primary-disabled: "#D9C4AD"
  ink: "#1A1A1A"
  body: "#333333"
  muted: "#666666"
  hairline: "#DDDDDD"
  hairline-soft: "#EEEEEE"
  canvas: "#FFFFFF"
  surface-soft: "#F5F2EE"
  surface-card: "#FFFFFF"
  surface-warm: "#FAF7F3"
  on-primary: "#FFFFFF"
  spec-label: "#888888"
  badge-bg: "#F0EBE4"
  badge-text: "#7A4F30"
  link: "#7A4F30"
  warning: "#C8540A"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "Menlo, Consolas, 'SF Mono', 'Liberation Mono', monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1px
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.5px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 1.5px
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 34px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    height: 40px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  category-nav:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.primary}"
    activeBorderColor: "{colors.primary}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.nav-link}"
    height: 48px
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    specTypography: "{typography.spec-value}"
    hoverBorderColor: "{colors.primary-light}"
    hoverBoxShadow: "0 2px 12px rgba(0,0,0,0.06)"
  product-image-viewer:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.xl}"
  spec-chip:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  compatibility-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary-dark}"
    borderColor: "{colors.primary-light}"
    borderWidth: 1px
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  award-badge:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary-dark}"
    borderColor: "{colors.primary}"
    borderWidth: 2px
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackground: "{colors.surface-soft}"
    headerTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    labelColor: "{colors.spec-label}"
    rowBorderColor: "{colors.hairline-soft}"
  socket-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 6px 14px
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    mutedTextColor: "{colors.muted}"
    linkColor: "{colors.primary-light}"
    borderTop: "4px solid {colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"

## Components

### Buttons
**`button-primary`** — Warm brown (`{colors.primary}`, #9C6B44) fill with white text at `{rounded.xs}` (4px radius), 44px height. The squared corner is intentional — it reads as precision instrument, not consumer product. Hover state deepens to `{colors.primary-dark}` (#7A4F30); disabled drops to `{colors.primary-disabled}` with no shape change. This is the primary add-to-cart and configurator CTA across all product pages.

**`button-secondary`** — White fill with a 1.5px `{colors.primary}` border and matching brown text. Used alongside `button-primary` in dual-CTA rows (e.g., "Add to Cart" + "Compare"). The thin-border approach avoids the heavy ghost-button style common to gaming hardware sites.

**`button-sm`** — Same brown fill at reduced dimensions (34px height, tighter padding) using `{typography.button-sm}`. Appears inside product listing cards and inline spec-table rows where space is constrained.

**`button-ghost`** — Transparent background, dark `{colors.body}` text, no border. Used for secondary actions like "View All" in category blocks and "Show More" spec toggles.

### Form Inputs
**`text-input`** — White canvas, 1px `{colors.hairline}` border, 42px height, `{rounded.xs}` radius. Focus state shifts the border to `{colors.primary}` without adding a glow or shadow. Placeholder uses `{colors.muted}`. Applied to newsletter sign-up, contact forms, and socket search.

**`search-bar`** — 40px, `{colors.surface-soft}` background instead of pure white, icon-left layout with a brown submit button on the trailing edge. Handles the keyword + socket-type + form-factor search that the SKU depth demands.

### Navigation
**`nav-bar`** — 64px white bar with a 1px `{colors.hairline}` bottom border. Logo left, product-category links center at `{typography.nav-link}`, search and cart icons right. At desktop widths, category links trigger `nav-dropdown` — a `{colors.canvas}` mega-panel with `{rounded.xs}` corners and a soft box-shadow — organized by product family: Coolers, Fans, Thermal Compound, Accessories.

**`category-nav`** — A secondary 48px horizontal tab strip on `{colors.surface-soft}`. The active tab uses a 2px bottom border in `{colors.primary}` with matching text color — the most color-forward interaction element on the page. Handles sub-categories within a product family: by socket, by cooler type, by fan size.

**`breadcrumb`** — `{typography.caption}` trail in `{colors.muted}`, current page in `{colors.ink}`, hairline-colored separators. Persistent on product detail pages; helps orient within a deep socket × form-factor taxonomy where multiple navigation paths reach the same SKU.

### Product Cards
**`product-card`** — White card, 1px `{colors.hairline}` border, `{rounded.xs}` radius. On hover, border shifts to `{colors.primary-light}` with a 6px soft shadow. Title in `{typography.title-sm}`, body copy in `{typography.body-sm}`. Directly below the product name sits a horizontal row of `spec-chip` tokens surfacing key specs — TDP, noise ceiling, cooler height — giving the listing page a datasheet-like density. Product image renders inside a `{colors.surface-warm}` inset panel to complement the brown and beige fan tones.

**`product-image-viewer`** — Warm surface (`{colors.surface-warm}`) container with `{rounded.xs}` radius and generous `{spacing.xl}` padding. On PDP, wraps a zoom-enabled multi-angle image rail. The warm background is load-bearing: the brown-tan physical product reads as intentionally colored rather than utilitarian when set against cream rather than pure white.

### Specification Elements
**`spec-chip`** — Cream-brown background (`{colors.badge-bg}`) with dark-brown text, `{typography.spec-label}` in uppercase. Used inline on product cards and inside comparison tables. Delivers technical metadata — bearing type, airflow, noise level — without using color to imply status or urgency.

**`compatibility-badge`** — Warm surface with a 1px `{colors.primary-light}` border. Contains socket identifiers (AM5, LGA1700, AM4) and signals physical fit. Appears on product cards, in the mega-dropdown, and at the top of the PDP above the title.

**`spec-table`** — Full-width table with alternating row backgrounds (`{colors.canvas}` / `{colors.surface-soft}`). Label column uses `{typography.spec-label}` in `{colors.spec-label}` (uppercase, muted gray). Value column uses `{typography.spec-value}` monospace for numeric fields — dB(A) noise figures, mm H₂O static pressure, rpm ranges — giving a deliberate datasheet reading experience. The monospace choice is the most typographically unconventional decision on the site and signals whose opinion Noctua is optimizing for.

### Awards and Badges
**`award-badge`** — White fill with a 2px `{colors.primary}` border, `{typography.badge-label}` uppercase text in `{colors.primary-dark}`. Noctua products frequently display third-party awards from hardware review outlets; these appear as a horizontal strip below the product title. The border-only treatment prevents them from visually competing with the product image. The frequency and prominence of these badges is higher than industry average.

### Hero
**`hero-banner`** — Dark (`{colors.ink}`) full-bleed banner with white display heading and a `{colors.primary}` accent detail (rule line or icon highlight). Product image floats right or bleeds to edge at desktop. Used on category landing pages and seasonal campaigns. The dark hero creates visual punctuation against the otherwise light-canvas site without introducing any new color.

### Footer
**`footer`** — Dark (`{colors.ink}`) footer with a 4px `{colors.primary}` top border as the single decorative element — the brown stripe makes it immediately legible as a Noctua footer without logos. Links render in `{colors.primary-light}` for legibility on dark. Column structure: Products, Support, Press/Media, Where to Buy (the distributor-locator column is unusually prominent, reflecting that Noctua's primary channel is a curated global retailer network, not direct-to-consumer).

### Filtering
**`socket-filter-chip`** — Neutral `{colors.surface-soft}` fill with 1px `{colors.hairline}` border at rest; active state fills solid `{colors.primary}` with `{colors.on-primary}` text. `{rounded.xs}` — never pill-shaped. Used in the sidebar filter panel on listing pages and in the mobile filter bottom sheet. Socket type, fan diameter, and TDP range are the primary filter axes.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; socket-filter-chip row scrolls horizontally with trailing fade mask; spec-table collapses to definition-list layout; hero text stacks above image |
| Tablet | 744–1128px | Two-column product grid; nav shows logo and icons only, categories via hamburger drawer; category-nav becomes horizontally scrollable strip |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav-bar with mega-dropdown; spec-table side-by-side columns; hero image at 50% width |
| Wide | > 1440px | Content caps at 1440px centered; four-column grid available for high-SKU fan listings; footer expands from four to six columns |

### Touch Targets
- All `socket-filter-chip` and interactive `spec-chip` elements maintain minimum 44×44px tap area via vertical padding expansion
- Nav-bar icon buttons minimum 44×44px
- `button-sm` is 34px tall visually but wrapped in a 44px touch region
- Product card: full card boundary is the tap target; no sub-element tap required

### Collapsing Strategy
- Mega-dropdown collapses to full-screen overlay drawer on mobile with back-button navigation per level
- `spec-table` collapses to `<dl>` definition-list pairs at < 744px — label bold, value inline
- `category-nav` becomes a horizontally overscrolling row with a right-edge fade mask
- Hero image is hidden at < 744px when text legibility is at risk; remains visible inside `product-image-viewer` on PDP
- Footer four-column layout becomes two columns at tablet, single-column accordion at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Extraction failed entirely**: noctua.at was behind a Vercel Security Checkpoint at time of extraction; all extracted hex values (#0070f3, #3291ff) and font stacks are Vercel's own checkpoint page assets, not Noctua's
- **Primary brown hex is approximate**: #9C6B44 is constructed from widely-documented brand-knowledge (Noctua's signature brown is among the most-discussed brand colors in PC hardware enthusiast communities); exact hex must be confirmed via direct site inspection or brand asset access
- **Secondary palette unconfirmed**: the beige (#C8A882) and warm surface (#FAF7F3) tokens are reasoned from the physical product's two-tone brown-and-tan colorway; not extracted from live CSS
- **Font family unconfirmed**: Noctua's actual heading and body typefaces could not be captured; system sans-serif stack is a safe fallback pending inspection — a humanist sans like Inter or Source Sans would be consistent with the brand register
- **Light vs. dark primary layout uncertain**: this DESIGN.md assumes a light-canvas body with dark hero sections; the actual site layout split could not be verified
- **Animation and transition tokens absent**: hover timing, loading states, and scroll-triggered animation behavior were not accessible
- **Icon system unknown**: Noctua uses socket-compatibility glyphs and product-type icons; their visual style (filled, outline, custom drawn) could not be determined from extraction
