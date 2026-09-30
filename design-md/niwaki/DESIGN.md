---
version: alpha
name: "Niwaki"
source_url: "https://www.niwaki.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every product in the Niwaki catalogue is photographed against bare white — no lifestyle props, no styled surfaces — just the tool suspended in clean emptiness, its silhouette carrying the full argument for ownership. This editorial restraint runs through the entire digital surface: a near-black (#313131) on canvas white, with almost no midtone decoration between them. The brand sells Japanese garden tools to a British audience with the visual language of a specialist instrument maker rather than a lifestyle retailer, and the absence of colour is itself a design position — what would be chromatically expressive on a fashion or food brand reads here as confidence in craft. Navigation is flat and architectural, with a category structure that mirrors the seriousness of the product taxonomy (pruning, ladders, maintenance, clothing). Typography leans toward the clean and editorial — generous line heights, modest weights, no display font theatrics — because the tools themselves are the visual event. Buttons operate in the same dark charcoal as the text, so the primary CTA feels less like a push-point and more like a natural conclusion to reading. Product cards show generous whitespace margins, tools at eye-level in a square crop, with price and title set close together in a tight typographic unit. The brand's Japanese heritage surfaces not through ornament but through studied negative space: what is absent is the design. Corners are square or barely softened — {rounded.none} on primary buttons, {rounded.xs} at most on inputs — and the overall geometry is orthogonal, precise, and unapologetic. The palette recovered from a live crawl reduced to a single tone (#313131), which speaks to a brand that achieves distinction through structural precision rather than colour volume. Any green accent implied by the brand's lacquered tool handles was not confirmed in extraction and is noted as a gap.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#999999"
  ink: "#313131"
  body: "#4c4c4c"
  muted: "#787878"
  hairline: "#dcdcdc"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f9f9f7"
  surface-card: "#ffffff"
  surface-offwhite: "#f4f4f2"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.02em
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  label-upper:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.3
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoAlign: left
  nav-bar-link-active:
    textColor: "{colors.ink}"
    textDecoration: underline
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "1 / 1"
    imageBackground: "{colors.canvas}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    gap: "{spacing.sm}"
    padding: "{spacing.base}"
    rounded: "{rounded.none}"
  product-card-hover:
    outline: "1px solid {colors.hairline}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    layout: "image-left text-right"
    imageWidth: "55%"
    padding: "{spacing.section} {spacing.xxl}"
  collection-header:
    backgroundColor: "{colors.surface-offwhite}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    rounded: "{rounded.none}"
  category-nav-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
    typography: "{typography.label-upper}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-limited:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.label-upper}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  specification-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.sm} 0"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    buttonWidth: 40px
    inputWidth: 48px
    height: 48px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 400px
    borderLeft: "1px solid {colors.hairline}"
    headerTypography: "{typography.title-md}"
    itemTypography: "{typography.body-sm}"
  newsletter-strip:
    backgroundColor: "{colors.surface-offwhite}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    padding: "{spacing.xxl} {spacing.xl}"
    columnGap: "{spacing.xxl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center

## Components

### Buttons
**`button-primary`** — A full charcoal (#313131) rectangle with no border-radius, white text in a small all-caps sans-serif with wide tracking (0.06em). The zero-curve geometry is deliberate — no softening, no friendliness affectation, just a precise action point consistent with the tool aesthetic. Active state deepens to `{colors.primary-active}`; disabled state washes to `{colors.primary-disabled}`. The uppercase label echoes a precision stamp on a tool shank rather than a typical ecommerce "Add to Basket" push button.

**`button-secondary`** — Identical geometry to primary (no radius, 48px height, same uppercase tracking), but inverted: white fill with a 1px charcoal border. Used for secondary actions such as "Continue Shopping" or "View All." Hover may deepen the border toward `{colors.primary-active}` without fill change.

**`button-text-link`** — Transparent background, ink text, underline decoration. Used inline in editorial copy and navigation footnotes. No hover animation beyond cursor change.

### Text Input
**`text-input`** — Square-cornered field ({rounded.none}), 1px `{colors.hairline}` border at rest sharpening to a full `{colors.ink}` border on focus. The 48px height ensures comfortable mobile tap targets. No floating label, no pill shape — the orthogonal geometry of the buttons carries straight through to form elements.

### Navigation
**`nav-bar`** — White bar at 64px with a bottom hairline separator. Logo left-aligned; category links (Tools, Clothing, Accessories, About, Stockists) span right in `{typography.nav-link}`. Subcategories open as flat panels, not animated mega-menus. Active link underlined with no background highlight.

**`category-nav-pill`** — Square chips used to filter within a collection page. Muted text on a hairline-bordered transparent background at rest; solid ink fill with white text when active. Uppercase 11px tracking matches the button convention and signals filtering intent without colour theatrics.

### Product Card
**`product-card`** — Square-crop tool image on white background, name in `{typography.title-sm}`, price in `{typography.price-display}` directly below. No drop shadow, no card elevation. Hover renders a 1px `{colors.hairline}` outline. No quick-add overlay, no swatch row — the card presents one tool, one price, and nothing else.

### Product Detail
**`specification-row`** — A ruled list beneath the product description, muted label left and value right, each row separated by a `{colors.hairline-soft}` bottom rule. Used to surface material, weight, blade length, and country of origin in a tabular reading pattern. No alternating row backgrounds.

**`quantity-stepper`** — Minus and plus buttons flanking a numeric input, all 48px tall and square, bordered in `{colors.hairline}`. Width-efficient and strictly functional; placed directly above the primary CTA in the add-to-basket row.

### Hero
**`hero-editorial`** — Two-column layout: large-format tool photograph at ~55% viewport width left, headline and body copy right. Headline at `{typography.display-xl}` in the serif stack — the single moment of typographic scale on the page. White canvas background, no scrim, no gradient.

### Collection Header
**`collection-header`** — Full-width offwhite (`{colors.surface-offwhite}`) band above the product grid, carrying the collection name at `{typography.display-md}` and an optional editorial sentence at `{typography.body-md}`. Minimal vertical padding, no image, no decorative border.

### Badges
**`badge-new`** and **`badge-limited`** — Two-state tagging for product status. "New" uses a filled charcoal chip with white label-upper type. "Limited" inverts to a transparent chip with a 1px charcoal border. Both fully square-cornered at 11px with 0.1em tracking — legible without being loud.

### Cart Drawer
**`cart-drawer`** — Slides from the right at 400px width, 1px left-border hairline, white fill. Header in `{typography.title-md}`, line items in `{typography.body-sm}`. Full-width `button-primary` anchors the base as the checkout CTA. No full-page dimming overlay — the drawer sits on top of the live page.

### Newsletter Strip
**`newsletter-strip`** — Full-width offwhite band before the footer. Headline at `{typography.display-sm}` in the serif stack, email input and submit side by side on desktop, stacked on mobile. Understated contrast; no decorative background pattern.

### Footer
**`footer`** — Dark charcoal fill (#313131), white type throughout. Column headings in `{typography.label-upper}`; links in `{typography.body-sm}`. Four-column grid on desktop, accordion on mobile. No visual border at the top — the colour shift from white page to dark footer is its own separator.

### Announcement Bar
**`announcement-bar`** — Slim 36px bar above the nav in the same charcoal as the body primary, white centered caption text. Carries shipping thresholds or limited-run notices. Dismissible on some implementations.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replacing horizontal links; hero stacks image above copy; cart drawer expands to full viewport width; newsletter input and button stack vertically |
| Tablet | 744–1128px | Two-column product grid; condensed horizontal nav or partial hamburger; hero retains two-column layout at compressed proportions |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav bar; standard two-column hero; specification rows display inline |
| Wide | > 1440px | Content max-width ~1400px centred; wider side gutters only; hero photography may bleed to edge with text column constrained |

### Touch Targets
- All buttons, inputs, and quantity steppers hold a minimum 48px height on touch viewports
- Category nav pills expand tap area to 44px height with additional vertical padding
- Footer accordion rows are full-width touch targets at 48px minimum
- Cart drawer close button minimum 44×44px hit area

### Collapsing Strategy
- Horizontal nav collapses to full-screen overlay drawer on mobile
- Specification rows remain single-column at all widths — no reflow required
- Product grid: 4-col → 3-col → 2-col → 1-col across breakpoints
- Cart drawer: 400px fixed → full viewport width below 744px
- Footer columns: 4-col → 2-col → single accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Palette almost entirely unextractable** — anti-bot protection ("Just a moment…") blocked the live crawl; only a single hex value (#313131) was recovered. All colours beyond primary/ink are inferred from the brand's documented minimalism, not extracted pixels. If Niwaki uses a secondary accent colour (a deep bottle-green is plausible given their lacquered tool handles), it was not confirmed and is absent from this spec.
- **Custom fonts unknown** — only system font stacks were present in the crawl. The site may use a licensed serif (Garamond, Freight Text, or similar) for editorial headers and/or a geometric sans for body. The serif/sans split used here is an informed estimate; verify against the live font-face declarations.
- **Button radius** — zero-radius (square) treatment is inferred from the brand's orthogonal aesthetic; should be verified against the live stylesheet.
- **Green brand accent** — Niwaki's physical tools frequently feature a deep bottle-green lacquered handle. Whether this colour appears as a digital accent on the site (badges, hover states, highlight strip) is unconfirmed.
- **Exact navigation structure** — first-level items, submenu pattern (flat panel vs. dropdown vs. mega-menu), and mobile navigation drawer behaviour were not observable from the blocked crawl.
- **Announcement bar presence** — included as a plausible e-commerce pattern; not confirmed as a live element.
