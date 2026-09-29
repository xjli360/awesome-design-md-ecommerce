---
version: alpha
name: "Heartwood"
source_url: "https://www.heartwood.ca"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  "Heartwood Manufacturing Ltd." keeps the full corporate suffix in its page title — a deliberate signal that this is a maker, not a merchant. The name itself borrows from dendrology: heartwood is the load-bearing core of a mature tree, denser and darker than the sapwood that surrounds it, and that material logic runs through the brand's implied design language. Deep walnut tones anchor the primary palette, graduating toward a warm charcoal ink (#1C1410) rather than the cold near-black that most B2B filing brands default to. The canvas is an off-warm white (#FAF7F4) that reads like uncoated paper stock rather than a clinical screen-white — a quiet nod to the physical world of filing and document storage. Buttons sit in a rounded-corner system ({rounded.sm} at 8px) that stops short of pill-softness: purposeful, not precious. Product cards lean on a warm surface ({colors.surface-card}) with a subtle hairline border ({colors.hairline}), letting form photography — storage units in natural wood veneer and powder-coated steel — carry most of the visual weight. Typography defaults to a sturdy humanist serif stack for display headings, communicating longevity and craft, with a clean sans-serif for body copy where scan-ability is paramount. An accent forest green ({colors.accent-forest}, #3B5E45) appears on secondary actions and callout badges, recalling the Canadian Pacific Northwest context implicit in the .ca domain. Spacing is generous — the brand is not optimizing for conversion density but for the kind of institutional credibility that sells to office managers and procurement teams over a multi-touch evaluation cycle. **Important caveat:** no hex colors or font stacks were extractable from the live site; all specific values below are inferred from brand name, category, and Canadian office-manufacturing context. Treat as provisional pending a live-site audit.

colors:
  primary: "#6B3D1E"
  primary-active: "#4F2D13"
  primary-disabled: "#C4A882"
  accent-forest: "#3B5E45"
  accent-forest-active: "#2A4432"
  ink: "#1C1410"
  body: "#3D2B1F"
  muted: "#7A6255"
  hairline: "#D8CBBF"
  hairline-soft: "#EDE6DE"
  canvas: "#FAF7F4"
  surface-soft: "#F2EDE7"
  surface-card: "#FFFFFF"
  surface-warm: "#EDE0D0"
  on-primary: "#FFFFFF"
  on-dark: "#FFFFFF"
  success: "#3B5E45"
  error: "#B33A1A"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.1px
  caption-bold:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  price-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
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
    padding: 13px 28px
    height: 48px
    border: none
    states:
      hover: { backgroundColor: "{colors.primary-active}" }
      disabled: { backgroundColor: "{colors.primary-disabled}", cursor: not-allowed }

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
    states:
      hover: { backgroundColor: "{colors.surface-soft}" }

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 20px
    border: "1px solid {colors.hairline}"
    states:
      hover: { borderColor: "{colors.muted}" }

  button-forest:
    backgroundColor: "{colors.accent-forest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 28px
    height: 48px
    states:
      hover: { backgroundColor: "{colors.accent-forest-active}" }

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
    height: 48px
    states:
      focus: { borderColor: "{colors.primary}", outline: "2px solid {colors.primary-disabled}" }
      error: { borderColor: "{colors.error}" }
      placeholder: { color: "{colors.muted}" }

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
    logoMaxHeight: 40px

  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    boxShadow: "0 4px 16px rgba(28,20,16,0.10)"

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    imagePadding: 0
    bodyPadding: "{spacing.base}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.body-sm}"
    states:
      hover: { boxShadow: "0 4px 20px rgba(28,20,16,0.10)", borderColor: "{colors.hairline-soft}" }

  product-card-badge:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"

  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    contentMaxWidth: 640px
    ctaSpacing: "{spacing.lg}"

  section-divider:
    borderTop: "1px solid {colors.hairline}"
    margin: "0 auto"
    maxWidth: 1200px

  category-tile:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline}"
    overlayLabelAlign: bottom-left
    states:
      hover: { borderColor: "{colors.primary}" }

  spec-table:
    backgroundColor: "{colors.canvas}"
    headerBackgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headerTypography: "{typography.caption-bold}"
    bodyTypography: "{typography.body-sm}"
    borderColor: "{colors.hairline}"
    cellPadding: "10px 16px"
    rowStripe: "{colors.surface-soft}"

  inquiry-form-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"

  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
    spacing: "{spacing.xs}"

  tag-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
    border: "1px solid {colors.hairline}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.label-upper}"
    headingColor: "{colors.surface-warm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: "4px solid {colors.primary}"


## Components

### Buttons

**`button-primary`** — Walnut brown (#6B3D1E) fill with white label at 15px/600, 8px radius, 48px height, 13px 28px padding. Darkens to #4F2D13 on hover; fades to the sand-toned #C4A882 when disabled. This is the primary call-to-action used on quote requests, product inquiry submissions, and catalogue downloads.

**`button-secondary`** — White canvas fill with a 1.5px walnut border and primary-colored label. Mirrors the primary in sizing and radius, transitions to {colors.surface-soft} on hover. Used beside primary CTAs as the "Learn More" or "Download Spec Sheet" counterpart.

**`button-ghost`** — Transparent with a 1px {colors.hairline} border. Lower-emphasis navigation action (e.g., "Back to category", "Clear filters"). Border strengthens to {colors.muted} on hover to confirm interactivity without competing with primary actions.

**`button-forest`** — Forest green (#3B5E45) fill with white label, same geometry as `button-primary`. Reserved for secondary conversion moments: "Request a Quote," "Contact a Dealer." Provides chromatic contrast against the warm brown primary without reading as a warning or error signal.

### Text Input

**`text-input`** — 48px tall, 8px radius, 1px {colors.hairline} border on a white canvas. Body-md type, {colors.muted} placeholder. On focus, the border upgrades to {colors.primary} with a 2px soft ring in {colors.primary-disabled} to maintain a warm, on-brand focus indicator rather than a default browser blue. Error state replaces the border with {colors.error} (#B33A1A).

### Navigation

**`nav-bar`** — 72px tall white bar with a bottom hairline border. Logotype sits left at max 40px height. Center or right nav links use {typography.nav-link} (15px/500). On scroll the bar gains a subtle box-shadow to communicate elevation without a color shift. A "Request a Quote" ghost or forest button sits flush right as the persistent conversion anchor.

**`nav-dropdown`** — Appears on category hover. White panel, 8px radius, 1px hairline border, 16px padding. Soft drop-shadow (10% opacity walnut). Links use {typography.body-sm}; subheadings use {typography.label-upper} in {colors.muted} to separate product families.

### Product Card

**`product-card`** — White card, 8px radius, 1px hairline border. Product image occupies the full card width at top; body area has 16px padding. Title in {typography.title-md}, price in {typography.price} (Georgia serif, 20px), secondary detail in {typography.body-sm}/{colors.muted}. On hover the card lifts with a 4px/20px warm shadow and the border softens. An optional **`product-card-badge`** chip (uppercase, 11px, warm sand background) communicates "New," "Bestseller," or "Made in Canada."

### Hero Banner

**`hero-banner`** — Warm off-white ({colors.surface-soft}) section, 64px vertical padding. Heading in {typography.display-xl} (Georgia, 48px/700), body copy in {typography.body-md}, max-width 640px for reading comfort. CTA row holds one `button-primary` and one `button-ghost` spaced 24px apart. On mobile the heading drops to `display-md` scale and padding halves.

### Category Tile

**`category-tile`** — Used in product-family grid. Warm sand ({colors.surface-warm}) background, 8px radius, 1px hairline. Category name in {typography.title-sm}, aligned bottom-left over a light-opacity background on hover-revealed scrim. Border transitions to {colors.primary} on hover. Tiles are always square or 4:3 aspect with background-image fill.

### Spec Table

**`spec-table`** — Key fixture on product detail pages. Header row in {colors.surface-soft} with {typography.caption-bold} labels; body rows alternate between white and {colors.surface-soft} for scan-ability. All cell borders use {colors.hairline}. Used to display dimensions, weight capacities, material grades, and finish options.

### Inquiry Form Panel

**`inquiry-form-panel`** — Warm off-white panel ({colors.surface-soft}), 12px radius, 32px padding. Contains a {typography.display-sm} heading, {typography.body-md} brief, stacked `text-input` fields, and a full-width `button-primary`. Positioned as a sidebar on product detail pages or as a full-width modal on mobile.

### Footer

**`footer`** — Deep walnut ink (#1C1410) background with a 4px {colors.primary} top border accent — the most saturated moment of warm brown anywhere in the layout. Column headings in {typography.label-upper}/{colors.surface-warm}. Body links in {typography.body-sm}/{colors.hairline} with hover upgrade to {colors.canvas}. A "Made in Canada" line and the full corporate name ("Heartwood Manufacturing Ltd.") appear in {typography.caption}/{colors.muted}.


## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout. Nav collapses to hamburger. Hero text drops to `display-md` (32px). Product grid 1-up. Inquiry form expands full-width. Spec table scrolls horizontally. Footer stacks columns. |
| Tablet | 744–1128px | 2-column product grid. Nav links visible but abbreviated. Hero text at `display-md`–`display-xl` scaling. Inquiry panel moves below product detail. Category tiles 2×2 grid. |
| Desktop | 1128–1440px | 3-column product grid. Full nav with dropdowns. Hero at `display-xl`. Inquiry panel as sidebar. Spec table full-width. |
| Wide | > 1440px | Content max-width 1200–1320px centered. Whitespace increases; no new layout regions added. Product grid stays 3-up or moves to 4-up depending on category volume. |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- `button-primary` and `button-secondary` height 48px (meets target natively)
- Nav hamburger icon: 48×48px tap area with 12px visible icon
- `product-card` entire card surface is tappable on mobile
- `text-input` height 48px; form elements stacked, never side-by-side on mobile

### Collapsing Strategy
- Primary nav: links → hamburger drawer at <744px; drawer slides from left with {colors.ink} background and {colors.on-dark} links
- Product filters: sidebar panel collapses to a bottom-sheet modal triggered by a "Filter" ghost button
- Spec table: horizontal scroll with sticky first column (property label) on <744px
- Inquiry form: full-width stacked below main product content; button becomes full-width
- Category tile grid: 4-up → 2-up → 1-up at breakpoints
- Footer: 4-column → 2-column → 1-column


## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the live site at heartwood.ca returned no parseable color tokens. All palette values in this file are inferred from brand name ("heartwood" = dense dark inner wood), category (office storage, institutional buyer), and Canadian manufacturing context. A live-site audit or design-file handoff is required before any token is treated as canonical.
- **No font stacks extracted** — zero font-family declarations were parsed. The Georgia serif / Helvetica Neue sans pairing here is a reasoned default for the brand archetype; the actual site may use a licensed web font (common for Canadian manufacturing sites: Freight Text, Acumin, or a custom wordmark face).
- **No meta theme-color** — no mobile browser chrome color is specified, suggesting either a non-Shopify custom build or a static site that omits the tag. Cannot confirm primary brand color from this signal.
- **Platform unknown** — confirmed not Shopify; the underlying CMS/framework is unidentified. Component architecture assumptions (card, nav-bar) are framework-agnostic.
- **Product photography art direction** — unable to confirm whether the brand uses lifestyle photography, technical white-background shots, or rendered 3D imagery. This significantly affects hero and card layout decisions.
- **Secondary and tertiary page templates** — only the root domain was analyzed. Category pages, product detail pages, and the quote/inquiry flow may have distinct layout patterns not captured here.
- **Accent and alert colors** — success, error, and informational states are inferred from brand palette logic; actual site values unknown.
