---
version: alpha
name: "Sofia Zakia"
source_url: "https://www.sofiazakia.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Where most bridal jewelers reach for pale blush or polished platinum, Sofia Zakia anchors its identity in a sumac-dark brown (#4d300f) — a pigment closer to aged amber or dried rosewater than the cool metallics its category defaults to. The canvas is a warm off-white (#fcfcf9), barely distinguishable from cream parchment, and secondary surfaces drift further into golden ivory (#f7f7e8, #f5f5eb) — a thermal palette that suggests handwritten invitations and wax seals rather than digital storefronts. Against this warmth, primary text sits in #22292d, a near-black with just enough green undertone to feel alive rather than stark.

  Typography makes an unusual pairing: Cardo, a humanist oldstyle serif with generous proportions, carries the editorial weight — product names, section headlines, the brand's quieter narrative moments. Inconsolata, a monospace, appears as a deliberate counterpoint for price callouts, SKU references, and fine-print annotations — introducing a faint mechanical precision into an otherwise romantic register, the way a jeweler's loupe or hallmark stamp intrudes on ceremony. Work Sans handles UI infrastructure: navigation, buttons, filter labels, the functional skeleton beneath the sentiment.

  The palette holds an unexpected triad of accents — a burgundy-wine (#592a38), a forest green (#435830), and a golden amber (#e69b1d) — suggesting gemstone references: the deep garnet of a pavé setting, a tsavorite, a canary sapphire. These never dominate; they surface as category markers, selection states, or hover cues, the way a jeweler's case catches light at different angles. Corners throughout lean toward sharp or minimally rounded — {rounded.xs} and {rounded.sm} rather than soft pills — reinforcing the precision that hand-set rings demand. The overall effect is an archive rather than a shop: browsable, lit with warm ambient light, built for a customer who reads the hallmark before the price tag.

colors:
  primary: "#4d300f"
  primary-active: "#3a2209"
  primary-disabled: "#b8b8b8"
  ink: "#22292d"
  body: "#4f4f4f"
  muted: "#74727b"
  hairline: "#dedede"
  canvas: "#fcfcf9"
  surface-soft: "#f7f7e8"
  surface-card: "#f5f5eb"
  surface-warm: "#ededda"
  on-primary: "#fcfcf9"
  on-dark: "#fcfcf9"
  accent-wine: "#592a38"
  accent-amber: "#e69b1d"
  accent-forest: "#435830"
  accent-green: "#478947"
  alert-red: "#d21404"

typography:
  display-xl:
    fontFamily: "'Cardo', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cardo', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.22
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Cardo', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Work Sans', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.03em
  title-sm:
    fontFamily: "'Work Sans', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.05em
  body-md:
    fontFamily: "'Work Sans', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  price-display:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  price-sm:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.02em
  sku-label:
    fontFamily: "'Inconsolata', 'Courier New', monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.06em
  editorial-quote:
    fontFamily: "'Cardo', Georgia, serif"
    fontSize: 21px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
    fontStyle: italic
  button-md:
    fontFamily: "'Work Sans', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Work Sans', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Work Sans', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em

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
    padding: 14px 32px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    placeholderColor: "{colors.muted}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
    logoColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    imageBg: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.display-sm}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    padding: "{spacing.sm}"
    hoverEffect: image-zoom-subtle
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaVariant: button-primary
    minHeight: 80vh
    layout: split-50-50
    imagePosition: right
  collection-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.xxl} {spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  price-tag:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
    saleColor: "{colors.alert-red}"
    compareAtColor: "{colors.muted}"
    compareAtDecoration: line-through
  sku-annotation:
    typography: "{typography.sku-label}"
    textColor: "{colors.muted}"
    backgroundColor: transparent
  gemstone-filter-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    selectedBorder: "none"
  ring-swatch:
    size: 22px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderDefault: "1px solid {colors.hairline}"
    gap: "{spacing.xs}"
    tooltipTypography: "{typography.caption}"
  product-detail-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.xl}"
    maxWidth: 480px
    gap: "{spacing.lg}"
  editorial-pullquote:
    textColor: "{colors.ink}"
    typography: "{typography.editorial-quote}"
    borderLeft: "2px solid {colors.primary}"
    paddingLeft: "{spacing.lg}"
    marginY: "{spacing.xxl}"
  metal-tag:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "4px 10px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.surface-card}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.surface-warm}"
    borderTop: "none"
    padding: "{spacing.xxl} {spacing.xl}"
    columns: 4
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    letterSpacing: 0.06em

## Components

### Buttons

**`button-primary`** — A dark sumac-brown (#4d300f) block with cream text, tracking-wide uppercase Work Sans at 12px. Padding of 14px vertical, 32px horizontal against a height of 44px gives a proportional CTA without excess mass. On hover, shifts to the deeper #3a2209; disabled state goes hairline gray (#b8b8b8) with cream text. Corners are minimal — {rounded.xs} at 2px — more a softened edge than a true radius.

**`button-secondary`** — Transparent background with a 1px ink (#22292d) border, matching height and typography to the primary. On hover, inverts: ink fill with cream text, preserving the button geometry. Used for secondary CTAs such as "Learn More" on editorial sections and "Add to Wishlist" on product pages.

**`button-ghost`** — No border, no background. Muted gray (#74727b) uppercase text with an underline. Used for low-priority actions: "See Size Guide," "Back to Collection," inline prose links within product descriptions.

### Text Input

**`text-input`** — Warm off-white (#fcfcf9) field with a 1px hairline border (#dedede) at rest, hardening to 1px ink on focus. 44px height with 10px/14px padding. Work Sans body-md at 15px. Placeholder text in muted gray (#74727b). No rounded corners beyond {rounded.xs}. Used in email capture, checkout fields, and the search overlay.

### Navigation

**`nav-bar`** — 64px tall, warm white (#fcfcf9) background with a 1px hairline bottom border. Logo in Cardo at {typography.display-sm} — 22px, weight 400 — giving the wordmark an editorial serif identity. Navigation links in Work Sans 13px with 0.04em tracking, unbolded. On mobile, collapses to a hamburger; search icon and cart icon persist in the top-right cluster.

### Product Card

**`product-card`** — Portrait 3:4 image on a warm ivory (#f7f7e8) background, no border, no radius. Product name in Cardo {typography.display-sm}; material or subtitle in Work Sans body-sm in muted gray (#74727b). Price rendered in Inconsolata {typography.price-display} — the monospace treatment gives pricing a deliberate, stamp-like precision distinct from the editorial headline above it. Hover applies a subtle image zoom without overlaying a UI element.

### Hero

**`hero-editorial`** — A 50/50 split layout on the warm ivory (#f7f7e8) surface: copy left, photography right. Headline in Cardo display-xl at 52px. Subhead in Work Sans body-md, body-color (#4f4f4f). Minimum height 80vh. CTA uses button-primary. On mobile, stack vertically: image first, copy below.

### Price Display

**`price-tag`** — Inconsolata monospace at 18px (price-display). Sale price in alert-red (#d21404); original price struck through in muted gray. The monospace choice sets pricing apart from the serif/sans-serif system elsewhere — it reads as a discrete stamp, not editorial prose.

### Gemstone Filter Chips

**`gemstone-filter-chip`** — Pill-shaped ({rounded.full}) chips in warm card surface (#f5f5eb) with a 1px hairline border. Caption-scale Work Sans at 12px. Selected state fills the chip with primary brown (#4d300f) and cream text, dropping the border. Used in PLP filter rails for metal type, stone, and ring style.

### Ring Color Swatches

**`ring-swatch`** — 22px circles ({rounded.full}) representing metal colors (yellow gold, white gold, rose gold, etc.). Default state has a 1px hairline border; selected state upgrades to a 2px ink border with a small offset ring. Gap between swatches is {spacing.xs}. On hover, a tooltip in caption typography names the metal.

### Editorial Pull Quote

**`editorial-pullquote`** — Cardo italic at 21px (editorial-quote), ink color, with a 2px left border in primary brown (#4d300f) and {spacing.lg} left padding. Generous vertical margin ({spacing.xxl}) above and below. Used in "About Sofia Zakia" sections and lookbook editorial pages.

### Metal Tag

**`metal-tag`** — Small pill in warm card surface (#f5f5eb) with a 1px hairline border and {rounded.sm} corners. Caption typography, body text color (#4f4f4f). Labels metal type (14k, 18k, Platinum) inline on product pages above the title or adjacent to the size selector.

### Announcement Bar

**`announcement-bar`** — Full-width strip in primary brown (#4d300f) with cream text. Caption typography at 12px with 0.06em tracking and implicit uppercase. 36px height. Used for shipping promotions, seasonal sale notices, or ethical sourcing callouts.

### Footer

**`footer`** — Dark ink (#22292d) background with warm ivory text (#f5f5eb) and warm-tinted headings (#ededda). Four-column layout on desktop: Shop, About, Customer Care, Newsletter. Body links in {typography.body-sm}, section heads in {typography.title-sm}. No top border; the color shift serves as the visual break. Social icons in row at bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column PLP grid; hamburger nav with slide-in drawer; hero stacks image above copy; filter chips scroll horizontally in a rail; product detail panel full-width below image |
| Tablet | 744–1128px | Two-column PLP grid; nav bar retains horizontal links if space permits, otherwise hamburger; hero split at 40/60 image-heavy; footer collapses to 2 columns |
| Desktop | 1128–1440px | Three-column PLP grid; full nav bar with four-link primary navigation; hero at 50/50 split; footer four columns; product detail panel fixed at 480px with sticky position on scroll |
| Wide | > 1440px | Content max-width capped (typically 1440px centered); hero image allowed to bleed beyond center column; PLP can accommodate four columns with generous gutter |

### Touch Targets

- All interactive elements (buttons, swatches, filter chips, nav links) maintain a minimum 44px touch target height
- Ring swatches displayed at 22px visual size are backed by a 44×44px invisible tap area
- Footer links have minimum 40px vertical tap spacing
- Announcement bar dismiss icon (if present) padded to 44px tap target

### Collapsing Strategy

- Primary navigation collapses to hamburger drawer below 1024px; drawer slides in from left over a warm-white scrim
- Filter rail on PLP becomes a bottom sheet modal on mobile, triggered by a sticky "Filter" button
- Product detail panel moves below the product image stack on mobile; sticky Add to Cart bar pins to viewport bottom
- Hero split layout converts to stacked on mobile: full-width image (aspect 4:3) above, copy block with reduced headline size below (display-md instead of display-xl)
- Footer collapses from four columns to two on tablet, single column accordion on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact animation timing and easing curves for image transitions, hover states, and drawer open/close could not be extracted
- Whether Inconsolata is a deliberate brand choice or a Shopify theme default for price/code elements is not confirmed from extraction alone
- Mobile menu design specifics (animation direction, overlay opacity, icon style) were not available in the extracted data
- Loading skeleton or placeholder patterns for product images not confirmed
- Exact letter-spacing on Cardo headings at the largest display sizes could differ from the 0 / −0.5px estimated values
- Loyalty, wishlist, or account UI patterns not visible from top-level extraction
- Dark mode or alternate theme variants not detected; the warm-cream palette appears to be the only registered theme
- Grid gutter widths and exact column counts for PLP at each breakpoint were not directly extractable
