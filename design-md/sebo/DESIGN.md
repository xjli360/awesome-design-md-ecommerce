---
version: alpha
name: "Sebo"
source_url: "https://www.sebo.us"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Sage green (#c7dfc2) runs through a predominantly white site at a moment when most appliance brands default to anthracite or corporate blue — it is the first and most telling choice, a garden-soft hue pressed against stainless-steel engineering language. The palette has almost no warmth after the sage: a series of barely-differentiated near-whites (#f7f7f7, #f3f3f3, #f0f0f0, #ececf3) flatten into a single luminous background field, then deep navy (#102745) anchors all heavy type and primary action elements, with a link-toned medium blue (#116699) as the only secondary accent. This is a cool, northern-European palette applied deliberately to a product sold on longevity rather than novelty. Baskerville appears at the display scale — a serif that reads as old-world and trustworthy rather than modern and disposable — while Arial handles every interface label, button, and body paragraph. The typographic split is architecturally honest: Baskerville argues for the brand's permanence, Arial executes the catalog. Corner radii are conservative; the interface uses {rounded.xs} and {rounded.sm} at most, and product imagery sits in flat or barely-cornered containers that reinforce the industrial precision of the machines themselves. Navigation is restrained — horizontal links in plain Arial with no mega-menu theatrics, letting the product hierarchy stay quiet. Section spacing is generous, giving each vacuum enough page volume to read as an engineered object rather than a catalog entry. The sage-on-navy pairing in primary actions ({colors.primary} background, {colors.on-primary} text) subverts the conventional white-on-dark CTA expectation and signals that Sebo is not designing to appliance-industry default.

colors:
  primary: "#c7dfc2"
  primary-active: "#aaddaa"
  primary-disabled: "#e4f0e2"
  navy: "#102745"
  link: "#116699"
  ink: "#3f3f3f"
  body: "#444444"
  muted: "#7a7a7a"
  muted-soft: "#bdbdbd"
  hairline: "#eeeeee"
  hairline-strong: "#bdbdbd"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f3f3f3"
  surface-subtle: "#ececf3"
  on-primary: "#102745"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  label-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-key:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 16px
  xl: 24px
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
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-navy:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.navy}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.navy}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-strong}"
    padding: 10px 14px
    height: 44px
    placeholderColor: "{colors.muted}"
    focusBorder: "1px solid {colors.navy}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.navy}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    imageBg: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-subtle}"
    textColor: "{colors.navy}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingY: "{spacing.xxl}"
  feature-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    paddingY: "{spacing.sm}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.primary}"
    padding: "{spacing.sm} {spacing.base}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-strong}"
    iconColor: "{colors.muted}"
    height: 40px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
  spec-table:
    backgroundColor: "{colors.canvas}"
    alternateRowBg: "{colors.surface-soft}"
    keyTypography: "{typography.spec-key}"
    valueTypography: "{typography.spec-value}"
    borderColor: "{colors.hairline}"
    paddingY: "{spacing.sm}"
    paddingX: "{spacing.base}"
  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Sage green (#c7dfc2) background with navy (#102745) text, 44px tall with minimal {rounded.xs} corners and uppercase Arial at 0.8px letter-spacing. The sage/navy pairing inverts the conventional white-on-dark CTA; hover deepens to `button-primary-active` (#aaddaa). Disabled state fades to near-white sage (#e4f0e2) with {colors.muted} text.

**`button-navy`** — Deep navy (#102745) fill with white text is Sebo's highest-contrast action variant, used for primary e-commerce actions like "Add to Cart" and "Buy Now" where sage reads as too ambient. Shares the same 44px height, padding, and uppercase {typography.button-md} as `button-primary`.

**`button-secondary`** — White canvas background, 1px navy border, navy text. Matches the primary button footprint exactly (44px, {rounded.xs}) for visual alignment in side-by-side action pairs like "Add to Cart / Learn More" or "Buy Now / Compare."

**`button-ghost`** — Transparent background with {colors.link} (#116699) blue text and no border. Applies to inline text-link actions, download links, and navigation sub-items where a filled button would overweight the layout.

### Navigation

**`nav-bar`** — 64px tall white bar with a 1px {colors.hairline} bottom border separating it from page content. Logo sits left in navy; nav links run in 14px Arial at normal weight — no bold, no uppercase — keeping the bar visually quiet relative to the product content below.

**`category-tab`** — Horizontal filter tabs on product listing pages. Inactive tabs in {colors.muted} gray; active tab in {colors.ink} with a 2px {colors.primary} sage underline. The sage underline is the one place the brand color appears as a UI accent rather than a fill, a restraint that prevents the palette from becoming decorative.

### Forms & Search

**`text-input`** — White background, {colors.hairline-strong} border, 44px tall with {rounded.xs} corners. Focus state upgrades the border to navy ({colors.navy}). Placeholder text in {colors.muted}. Standard Arial 16px body text inside.

**`search-bar`** — 40px tall, same construction as `text-input` with a search icon in {colors.muted} at the trailing edge. Appears in the nav utility row and above product listing grids as a standalone filter entry.

### Product Display

**`product-card`** — Light {colors.surface-card} (#f3f3f3) container with {rounded.xs} corners. Product image area uses {colors.surface-soft} background so the machine reads against a clean field. Title in bold {typography.title-sm}; price in {typography.price} at 20px. The card avoids star-rating clusters at catalog level, letting the engineering silhouette carry the visual argument.

**`product-badge`** — Small sage-green chip with navy text in uppercase {typography.label-sm}, applied to "New", "Award Winner", and promotional flags. {rounded.xs} corners keep it rectangular rather than capsule-shaped, consistent with the site's hard-edge geometry.

**`spec-table`** — Alternating white and {colors.surface-soft} rows with no outer border. Key column in bold {typography.spec-key}; value column in regular {typography.spec-value}. Used extensively in product detail pages where motor wattage, filtration class, suction power, and cable length are primary purchase arguments rather than marketing copy.

### Content Sections

**`hero-banner`** — {colors.surface-subtle} (#ececf3) background — the faint lavender-gray that distinguishes the hero zone from the product grid below — with navy Baskerville headlines in {typography.display-xl} and a `button-navy` CTA. The hero does not rely on full-bleed photography; the vacuum itself is the visual center.

**`feature-strip`** — Full-width sage green bar ({colors.primary}) carrying short uppercase feature claims in {typography.label-sm} navy text. Functions as a zone separator and the clearest single-element expression of the brand's accent color, independent of button state.

**`breadcrumb`** — Muted gray path labels in {typography.body-sm} with {colors.muted-soft} slash separators. Active page node renders in {colors.ink}. No background container — the breadcrumb sits directly on whatever surface is behind it, keeping the chrome minimal.

**`footer`** — Deep navy (#102745) background, white body text, sage green link color ({colors.primary}) — the palette inversion of the hero. Navigation link columns in {typography.body-sm}; section headings in bold {typography.title-sm}. Sage links on navy in the footer create visual continuity with the primary button color and close the palette loop across the page.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero headline drops to {typography.display-md}; spec tables gain horizontal scroll |
| Tablet | 744–1128px | Two-column product grid; nav may partially collapse; hero maintains text-plus-image split |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav bar; hero at full {typography.display-xl} scale |
| Wide | > 1440px | Content container max-width (~1280px) centered on canvas; four columns possible for accessories grid |

### Touch Targets
- All buttons minimum 44px tall to meet iOS and Android touch target guidelines
- Nav links carry at least 44px vertical tap area regardless of visible text size
- Product cards are fully tappable across their entire surface, not only the title or image

### Collapsing Strategy
- Primary navigation collapses to a hamburger icon on mobile; drawer slides in from the left over a navy scrim
- Category filter tabs become a horizontally scrollable strip on mobile rather than wrapping to multiple lines
- Spec tables scroll horizontally at mobile widths; rows do not stack into definition-list format
- Footer link columns stack vertically on mobile, each section headed by a disclosure toggle

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom brand font detected beyond system stacks; it is unclear whether Sebo loads a proprietary typeface via JavaScript or relies entirely on Baskerville and Arial — all typography tokens use system fallbacks
- Exact primary color role unconfirmed: #c7dfc2 is the most distinctive extracted color but its specific usage as button fill, hero tint, or background accent could not be verified without live DOM inspection
- Button corner radius not confirmed — {rounded.xs} (2px) is estimated from the utilitarian aesthetic; site may use fully square corners ({rounded.none})
- No hover or visited state colors for the link tone (#116699) were extractable
- primary-disabled (#e4f0e2) is a derived value, not directly extracted from the site
- Dark mode support unknown — no prefers-color-scheme tokens detected in the extraction
- Promotional alert or sale colors (red, amber) may exist in the live palette but did not appear in the top extracted colors
- Font Awesome 5 icon usage patterns and sizing conventions for cart, search, and account icons in the nav utility row are not mapped
