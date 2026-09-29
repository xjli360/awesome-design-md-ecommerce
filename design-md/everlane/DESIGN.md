---
version: alpha
name: "Everlane"
source_url: "https://everlane.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every garment on Everlane's site carries a cost breakdown — materials, labor, transport, duty, markup — and that accounting ethos maps directly onto its visual system: the fewest colors needed, the plainest type, no ornament that cannot be justified by function. The primary action color, #334fb4, is a medium institutional blue that appears at CTAs and active states and nowhere else; the rest of the palette collapses into a near-black (#121212) ink scale with light-gray surfaces (#f3f3f3, #dedede, #e0dfdf). Maison Neue carries all type across three weights — Book for editorial body, Medium for navigation and labels, Demi for headings that need weight without decorative intent. Selva Script Pro appears in campaign contexts only, never in transactional UI, arriving at large display sizes as a seasonal counterweight to the system's otherwise strict grotesque voice. Buttons and cards hold {rounded.none} — no soft radius anywhere in functional UI — a deliberate refusal of approachability in favor of precision. A warm taupe, #c8c0b8, anchors swatch states and contextual imagery; brick #ca3214 is reserved strictly for sale callouts so its urgency reads as a genuine system signal rather than decorative noise. The top navigation resolves at a compact fixed height with Maison Neue Medium labels and a 1px hairline underline at {colors.primary} to mark the active category — no background fill, no hover box, no animated transition. Product photography is white-backed for catalog grids and atmospheric for editorial modules; because the surrounding UI is near-monochrome, photography carries all warmth without fighting chrome. The footer unfolds into a structured transparency grid — ethics pages, supply chain maps, impact reports — doubling as brand content and functional wayfinding, set in white type on an #121212 ground.

colors:
  primary: "#334fb4"
  primary-active: "#2a3f90"
  primary-disabled: "#9aaed9"
  ink: "#121212"
  body: "#242833"
  muted: "#737373"
  hairline: "#dedede"
  hairline-soft: "#e0dfdf"
  canvas: "#ffffff"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  warm-taupe: "#c8c0b8"
  sale: "#ca3214"

typography:
  display-xl:
    fontFamily: "'Maison Neue Book', 'AvenirLTStd', sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Maison Neue Demi', 'AvenirLTStd', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Maison Neue Medium', 'AvenirLTStd', sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.2px
  logo-display:
    fontFamily: "'Selva Script Pro', serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0
  title-md:
    fontFamily: "'Maison Neue Demi', 'AvenirLTStd', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'Maison Neue Medium', 'AvenirLTStd', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Maison Neue Book', 'AvenirLTStd', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Neue Book', 'AvenirLTStd', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue Book', 'AvenirLTStd', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  price-display:
    fontFamily: "'Maison Neue Medium', 'AvenirLTStd', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Maison Neue Medium', 'AvenirLTStd', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Maison Neue Medium', 'AvenirLTStd', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.05px
  button-md:
    fontFamily: "'Maison Neue Medium', 'AvenirLTStd', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Maison Neue Medium', 'AvenirLTStd', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.5px
    textTransform: uppercase
  label-uppercase:
    fontFamily: "'Maison Neue Demi', 'AvenirLTStd', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.0px
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
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 24px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
    activeIndicatorColor: "{colors.primary}"
    activeIndicatorHeight: 1px
  collection-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "8px 0"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    nameTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    salePriceColor: "{colors.sale}"
    originalPriceDecoration: line-through
    originalPriceColor: "{colors.muted}"
    gap: "{spacing.sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    padding: "{spacing.section}"
    minHeight: 600px
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-tag-sale:
    textColor: "{colors.sale}"
    typography: "{typography.price-sale}"
    originalPriceDecoration: line-through
    originalPriceColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  badge-sale:
    backgroundColor: "{colors.sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: "2px 6px"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    soldOutDecoration: line-through
    soldOutColor: "{colors.muted}"
    size: 40px
  color-swatch:
    rounded: "{rounded.full}"
    size: 20px
    border: "1px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
    selectedGap: 2px
  transparency-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    border: none
    rowSeparator: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-uppercase}"
    padding: "{spacing.section}"
    columns: 5
    linkHoverDecoration: underline

## Components

### Buttons

**`button-primary`** — 48px-tall flat rectangle with zero border radius, #334fb4 fill, and white Maison Neue Medium uppercase text at 0.5px tracking. Hover darkens to `{colors.primary-active}` (#2a3f90) with no transition delay; the uppercase treatment is the primary typographic signal of interactivity across the site. Disabled state softens to `{colors.primary-disabled}` (#9aaed9) with `cursor: not-allowed`.

**`button-secondary`** — Identical dimensions to primary with a 1px solid `{colors.ink}` border and transparent fill. Used for secondary actions on product pages such as "Save to Wishlist." Hover convention inverts fill to ink and text to canvas.

**`button-ghost`** — Text-only with no border or background, button-sm uppercase type with persistent underline. Reserved for inline contextual links like "View size guide" or "Learn about our factories."

### Inputs

**`text-input`** — 48px tall, no radius, 1px `{colors.hairline}` border at rest that snaps to 1px `{colors.ink}` on focus with no animation. Maison Neue Book 16px. Covers search, email capture, and checkout fields. Placeholder disappears on focus; no floating label pattern.

### Navigation

**`nav-bar`** — 56px fixed header on white canvas with a 1px `{colors.hairline}` bottom border. Maison Neue Medium 14px labels. Active category marked by a 1px solid `{colors.primary}` underline flush with the tab bottom — no background fill, no pill. Logo centered on mobile, left-aligned on desktop.

**`collection-tab`** — Flat horizontal strip below the primary nav for category browsing. Inactive labels render in `{colors.muted}`; active label shifts to `{colors.ink}` with a 1px ink underline. No background fill anywhere in the tab system.

### Product

**`product-card`** — Flush 3:4 aspect-ratio image with no radius and a white backdrop. Name renders in body-sm Maison Neue Book immediately below; price in price-display Maison Neue Medium. When on sale, the sale price in `{colors.sale}` (#ca3214) precedes a line-through original in `{colors.muted}`. On hover, a secondary color swatch row fades in below the image without layout shift.

**`size-selector`** — 40px square tiles, no radius, 1px `{colors.hairline}` border at rest. Selected tile upgrades to 1px `{colors.ink}` border. Sold-out sizes apply `text-decoration: line-through` in `{colors.muted}` and remain visible but non-interactive.

**`color-swatch`** — 20px circular chips (`{rounded.full}`) with a 1px `{colors.hairline}` ring. Selected chip gains a 2px `{colors.ink}` outer ring with a 2px transparent gap between chip and ring. The warm taupe `{colors.warm-taupe}` (#c8c0b8) is the most common color in the natural materials range.

**`transparency-callout`** — Everlane's brand-defining cost-breakdown module: `{colors.surface-soft}` background, Maison Neue Demi title ("What We Pay"), and body-sm rows showing individual cost line items separated by 1px `{colors.hairline}` rules. Renders inline on product pages beneath the add-to-cart block; no border, no shadow, no radius.

**`price-tag` / `price-tag-sale`** — Regular price in `{colors.ink}` Maison Neue Medium 16px. On sale, the sale price in `{colors.sale}` renders first, followed by the struck-through original in `{colors.muted}`, both on the same line.

**`badge-new` / `badge-sale`** — Zero-radius label chips at 2px 6px padding, label-uppercase type. New badges are ink-on-white; sale badges are white-on-`{colors.sale}`. Positioned as absolute overlays in the upper-left corner of product card images.

### Layout

**`hero-banner`** — Full-bleed editorial unit with `{colors.surface-soft}` or a full-bleed photograph as background. display-xl Maison Neue Book headline, body-md copy block, and a primary button. Minimum 600px tall on desktop. Text alignment switches between centered and left-aligned by editorial template.

**`footer`** — `{colors.ink}` background, five columns on desktop (Shop, Company, Help, Impact, Social) in Maison Neue Book 14px white. Column headings in label-uppercase with 1px letter-spacing. Prominent links to ethics pages, factory maps, and impact reports function as first-class brand content, not auxiliary legal copy.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered wordmark; hero headline drops to display-md scale and centers; footer stacks to 2 columns then single |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level labels only; hero text left-aligned; footer 3 columns |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with collection tabs; transparency callout renders as sidebar on product pages |
| Wide | > 1440px | Layout centers within 1440px max-width container; side margins grow proportionally; editorial modules maintain fixed photographic proportions |

### Touch Targets
- All buttons hold 48px minimum height on all breakpoints
- Size selector tiles are 40px — should expand to 44px tap area on mobile while retaining visual size
- Color swatches at 20px are below WCAG 2.5.5; expand hit area to 32px on mobile with CSS padding, visual size unchanged
- Nav row height (56px) doubles as the tap target; no separate expansion needed

### Collapsing Strategy
- Primary nav collapses behind a hamburger at < 744px; category browsing opens in a full-screen slide-in drawer with accordion sub-categories
- Transparency callout moves from product-page sidebar to a below-fold inline section on mobile
- Size selector grid wraps to preserve 40px tile sizes rather than compressing tile dimensions
- Collection tab strip becomes a horizontally scrollable row on mobile with no visible scroll indicator
- Footer condenses from 5 columns to 2 at tablet and single column at mobile, headings collapsing as accordion triggers

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Border-radius behavior is inferred from visual inspection; `{rounded.none}` for buttons and cards is not confirmed from extracted CSS tokens
- `{colors.primary-active}` (#2a3f90) and `{colors.primary-disabled}` (#9aaed9) are derived by darkening and lightening the extracted #334fb4; neither appears in the extracted color list
- Maison Neue exact CSS fontWeight mappings (Book = 300 vs 400; Demi = 600 vs 700) not confirmed from extracted font stacks
- Selva Script Pro usage scope (logo lockup vs editorial headlines) inferred; not confirmed from extracted CSS
- `{colors.body}` (#242833) usage context is unclear — may be a dark overlay, a nav background in a specific state, or a legacy token; mapped to `body` as secondary dark text
- Assistant font role not confirmed — may be a utility/form fallback rather than a primary editorial face
- AvenirLTStd relationship to Maison Neue not confirmed; likely a licensed-font fallback in the CSS stack
- No animation or transition timing values extracted
- No box-shadow or elevation tokens extracted; product cards appear shadowless based on visual inspection
- Nav height (56px) is estimated; exact value not confirmed from extracted layout metrics
- Dark/light mode support, if any, is unconfirmed from extracted data
