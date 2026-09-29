---
version: alpha
name: "BlueRidge"
source_url: "https://www.blueridgeair.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Spec numbers crowd the top of every BlueRidge product card — BTU ratings at 20px bold before a model name appears, a hierarchy that signals a brand sold to homeowners who already know what they need. The palette anchors on a medium mountain-sky blue (#1B5FAF) that reads consistently from nav links through primary CTAs to icon fills, with no secondary accent competing for that role. Backgrounds hold to white (#FFFFFF) with a faint cool wash ({colors.surface-soft} at #F0F5FC) beneath specification grids, giving data-dense layouts an airy container rather than a heavy technical register. The energy efficiency badge — forest green (#2E8B57) — stands deliberately apart from primary blue, marking a compliance fact rather than a brand moment, and it never appears in decorative contexts.

  Typography runs in a clean geometric sans — Inter or system equivalent — with weight doing most of the hierarchy work. Spec values run 700 at 20px with tight letter-spacing so a shopper scanning BTU, coverage area, and SEER rating can read a row in a single sweep; body copy drops to 400 at 16px with 1.6 leading for the longer product descriptions that follow. Buttons carry 600 weight at 15px, moderately rounded at {rounded.sm} — not the pill softness of a lifestyle brand, not the hard square of an industrial catalog, but a middle register that communicates reliable appliance.

  Product pages follow a two-panel rhythm: photography left, specifications and add-to-cart right, then a scrollable spec table below the fold set on {colors.surface-soft}. Category tiles on the homepage use an {colors.accent-sky} fill (#E1EEFA) to assemble a soft grid of product types before any product photography appears, letting navigation double as catalog preview. A thin trust bar above the nav — warranty terms, shipping, certification marks — treats reassurance as ambient infrastructure rather than marketing. The footer drops to a deep navy ({colors.surface-dark} at #0F2D5C), the darkest surface in the system and used nowhere else, providing a decisive terminus after long product-detail scrolls.

colors:
  primary: "#1B5FAF"
  primary-active: "#174F94"
  primary-disabled: "#A6C4E8"
  ink: "#1A1A1A"
  body: "#3D3D3D"
  muted: "#6B7280"
  hairline: "#DDE3EC"
  canvas: "#FFFFFF"
  surface-soft: "#F0F5FC"
  surface-card: "#FFFFFF"
  surface-dark: "#0F2D5C"
  on-primary: "#FFFFFF"
  accent-sky: "#E1EEFA"
  badge-energy: "#2E8B57"
  badge-energy-text: "#FFFFFF"
  warning: "#D97706"
  warning-bg: "#FEF3C7"

typography:
  display-xl:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-strong:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  spec-label:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  spec-value:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.2px
  badge:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  price-display:
    fontFamily: "Inter, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px

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
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1.5px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-sm-outline:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "2px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 32px
    activeTextColor: "{colors.primary}"
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-strong}"
    iconColor: "{colors.primary}"
    paddingY: "{spacing.sm}"
    paddingX: "{spacing.section}"
    borderBottom: "1px solid {colors.hairline}"
    iconSize: 16px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
    imageAspectRatio: "4/3"
    imageRounded: "{rounded.sm}"
    titleTypography: "{typography.title-md}"
    specTypography: "{typography.spec-value}"
    priceTypography: "{typography.price-display}"
    hoverBoxShadow: "0 4px 16px rgba(27,95,175,0.10)"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 520px
    paddingY: "{spacing.xxl}"
    paddingX: "{spacing.section}"
    overlayGradient: "linear-gradient(90deg, #0F2D5C 55%, transparent 100%)"
    imagePosition: right center
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.md}"
    labelTypography: "{typography.spec-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.spec-value}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.base} {spacing.lg}"
    dividerColor: "{colors.hairline}"
    border: "1px solid {colors.hairline}"
  btu-selector:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    typography: "{typography.title-sm}"
    textColor: "{colors.body}"
    gap: "{spacing.sm}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
    padding: 10px 20px
  energy-badge:
    backgroundColor: "{colors.badge-energy}"
    textColor: "{colors.badge-energy-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  category-tile:
    backgroundColor: "{colors.accent-sky}"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    typography: "{typography.title-sm}"
    padding: "{spacing.lg}"
    iconSize: 40px
    iconColor: "{colors.primary}"
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  warning-notice:
    backgroundColor: "{colors.warning-bg}"
    textColor: "{colors.ink}"
    borderLeft: "4px solid {colors.warning}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.accent-sky}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption-strong}"
    headingColor: "{colors.muted}"
    paddingY: "{spacing.section}"
    dividerColor: "#1E3E6E"

## Components

### Buttons

**`button-primary`** — The primary action in the system, used for Add to Cart, Get a Quote, and checkout progression. Renders in #1B5FAF blue at 48px height with `{rounded.sm}` (8px) corners, keeping the form factor near-rectangular but not harsh. Hover drops to `{colors.primary-active}` (#174F94); disabled state fades to `{colors.primary-disabled}` (#A6C4E8) with `cursor: not-allowed` — never hidden, since an out-of-stock item should still show the intent of the action.

**`button-secondary`** — A bordered outline button used for secondary CTAs like "View Full Specs", "Compare Models", or "Find a Dealer". Uses a 1.5px solid `{colors.primary}` border with matching text against a white fill, maintaining the blue language without the filled weight. Maintains identical 48px height to `button-primary` so they can sit side-by-side without visual misalignment.

**`button-ghost`** — Inline text-only action with no background or border. Used for collapse/expand toggles, "Read more", and breadcrumb-style back navigation. Inherits `{colors.primary}` text color and `{typography.button-md}` weight so it reads as intentional rather than plain body text.

**`button-sm-outline`** — A 36px compact variant for table row actions, accessory selectors, and "Add to Wishlist" controls that live inside product cards without competing with the main CTA.

### Inputs

**`text-input`** — Standard form field used for zip-code entry (for retailer lookup), email capture, and contact forms. A 1px `{colors.hairline}` border transitions to a 2px `{colors.primary}` ring on focus — the focus ring uses the full primary blue rather than a tint, giving keyboard navigation users a clear, high-contrast indicator. Placeholder text sits in `{colors.muted}` to prevent confusion with filled values.

### Navigation

**`nav-bar`** — 64px tall, white background with a 1px `{colors.hairline}` bottom border. Logo anchors left at 32px height; navigation links center or right-align in `{typography.nav-link}` (500 weight, 14px). Active category link shifts to `{colors.primary}` without underline — color alone carries the active state. No mega-menu shadow or elevation; the nav reads flat against the page.

**`trust-bar`** — A thin utility strip that lives above the nav, never below it. Carries shipping thresholds, warranty callouts, and certification logos in `{typography.caption-strong}` against `{colors.surface-soft}`. Icons render at 16px in `{colors.primary}`, making the bar feel brand-connected rather than generic. Collapses or hides at mobile breakpoints.

### Product Display

**`product-card`** — The main unit on category and search pages. A white card with a 1px `{colors.hairline}` border and `{rounded.md}` (12px) corners, padding at `{spacing.lg}` (24px). Product image takes a 4:3 aspect ratio with `{rounded.sm}` corners. Title runs `{typography.title-md}`, BTU or wattage renders in `{typography.spec-value}` (700/20px) beneath — this reversal of the standard name→spec order is the most brand-specific layout decision in the system. Price renders in `{typography.price-display}` (700/26px). Hover state lifts with a soft blue box-shadow.

**`hero-banner`** — Full-bleed section on the homepage and major category pages. Deep navy `{colors.surface-dark}` (#0F2D5C) background with a directional gradient that fades rightward to reveal product photography. Headline in `{typography.display-xl}` (700/40px) in white, supported by a body line in `{typography.body-md}`. Minimum height 520px, with `{spacing.xxl}` vertical padding. On mobile, the gradient covers full width and the image either clips or hides.

**`spec-table`** — Horizontal key–value grid that appears below the two-column product detail section. Rows carry `{typography.spec-label}` (uppercase, 11px, 700, 0.5px tracking) in `{colors.muted}` and `{typography.spec-value}` (20px, 700) in `{colors.ink}`. The whole table sits on `{colors.surface-soft}` with a 1px `{colors.hairline}` border, `{rounded.md}` corners, and row dividers at the same hairline color. This is the product page's primary persuasion surface.

**`btu-selector`** — A horizontal chip-group used to choose BTU tiers (e.g. 8,000 / 10,000 / 12,000 / 14,000) or heating wattage. Inactive chips show `{colors.hairline}` border and `{colors.body}` text; the selected chip fills to `{colors.primary}` with white text and a matching blue border. Chips are `{rounded.xs}` (4px) — distinctly more rectangular than button controls, signaling "selector" rather than "action".

**`category-tile`** — Homepage grid entries for Portable AC, Mini-Split, Window Units, Heaters, and Accessories. Soft `{colors.accent-sky}` (#E1EEFA) fill at rest with a 40px icon in `{colors.primary}` and `{typography.title-sm}` label. On hover, the tile fills to `{colors.primary}` and text and icon invert to white — a full-bleed color flip that reinforces the primary brand hue as an active surface, not just a text color.

**`energy-badge`** — A small pill attached to product cards and spec tables when a unit carries an Energy Star rating. Forest green (#2E8B57) fill with white `{typography.badge}` text (11px, 700, uppercase). Never uses primary blue — the color distinction signals a third-party certification status rather than a brand choice.

**`warning-notice`** — Used for BTU-recommendation callouts ("This unit is undersized for rooms over 500 sq ft") and installation requirement notices. Left-bordered with `{colors.warning}` (#D97706) amber, body in `{colors.warning-bg}` (#FEF3C7). Appears inline on PDPs below the add-to-cart section.

**`footer`** — Four-column link grid on deep navy `{colors.surface-dark}` (#0F2D5C). Column headings in `{typography.caption-strong}` at `{colors.muted}` gray; links in `{typography.body-sm}` at `{colors.accent-sky}` (#E1EEFA) for legibility on dark background. Internal column dividers use a slightly lighter navy (#1E3E6E) rather than the main hairline, keeping contrast subtle against the dark surface. Section padding of `{spacing.section}` (64px) top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout throughout; trust-bar collapses; hero-banner image hidden, gradient covers full width; product grid becomes 1-up; spec-table scrolls horizontally; btu-selector wraps to 2×2 grid; nav condenses to hamburger + logo |
| Tablet | 744–1128px | Product grid shifts to 2-up; PDP two-panel collapses to stacked (image top, specs below); hero-banner shows partial image; trust-bar shows 2 of 4 items; category-tile grid 2×3 |
| Desktop | 1128–1440px | Full two-panel PDP layout; product grid 3-up; hero-banner at full gradient treatment; trust-bar shows all 4 items inline; nav links fully expanded |
| Wide | > 1440px | Max content width capped at 1440px with auto side margins; hero-banner background extends edge-to-edge while content constrains; no layout changes beyond centering |

### Touch Targets

- All interactive controls minimum 44×44px on mobile (btu-selector chips expand padding to meet this)
- `button-primary` and `button-secondary` maintain 48px height across all breakpoints
- Product card tap area covers full card including image, not just text
- Nav items in mobile drawer minimum 48px row height with full-width tap zone

### Collapsing Strategy

- Spec-table rows below the fold on PDP collapse behind a "Show all specs" toggle on mobile to reduce scroll distance before the add-to-cart CTA
- Category-tile grid reduces from 3 columns (desktop) → 2 (tablet) → 2 (mobile, with horizontal scroll)
- Trust-bar items de-prioritize: shipping threshold shows always, others collapse into a "+2 more" expand on mobile
- Hero-banner copy truncates headline from 40px to 28px (`{typography.display-md}`) on mobile with line-clamp on body text at 3 lines

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **All colors are brand-knowledge estimates**, not extracted hex values — the live site returned zero color tokens. Palette was inferred from brand name ("BlueRidge"), product photography context, and typical HVAC brand conventions. Primary #1B5FAF and surface-dark #0F2D5C should be validated against the actual site before use.
- **No fonts were extracted** — zero font-family stacks detected. Inter is used as a high-probability match for a clean geometric sans used in this product category; the actual typeface must be confirmed by inspecting the live site's loaded font resources.
- **No theme-color meta tag found** — cannot confirm a canonical brand hex via the simplest available signal.
- **Site is not on Shopify** — product card and cart component conventions may differ significantly from typical DTC patterns; PDP layout assumptions should be verified against actual site structure.
- **Typography scale weights and sizes are inferred**, not measured — spec-value sizing, display headline sizing, and nav-link weight are estimates based on HVAC product page conventions, not live measurements.
- **No secondary palette data available** — the warning amber (#D97706) and energy-badge green (#2E8B57) are functional assumptions; actual brand-approved alert and certification colors unknown.
- **BTU selector interaction model unconfirmed** — the btu-selector component is inferred from product category conventions (size tiering is universal in HVAC); actual selector mechanism on the live site may differ.
