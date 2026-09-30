---
version: alpha
name: "Quill & Fox"
source_url: "https://quillandfox.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Paper weight is Quill & Fox's first design argument — the brand photographs its goods pressed flat against raw linen or pale oak, where grain and texture do the persuading before any headline arrives. The visual system builds outward from a parchment-tinted canvas (#FDFAF5) that refuses the sterile white of commodity e-commerce, warming every page with the low glow of a well-lit writing desk. Fox-copper (#C4622D) lands as the single voltage point — on envelope seals, on primary CTA buttons, on the ampersand in the wordmark — making one heat tone do sustained structural work rather than decorative spotting. Display type runs in an editorial serif (Freight Display or a close stand-in) at regular weight 400, large enough that a 52px headline at {spacing.section} margin creates the breathing room of a quality print catalogue rather than a storefront. Body copy switches to a clean humanist sans at 16px/1.65 line-height, a ratio suited to extended paper-spec descriptions and ruling-style essays, not just product blurbs. A near-black ink (#1A1714) carries warmth, as if walnut oil were mixed into the carbon; the mid muted (#7A6F67) handles secondary text without going generic gray. A deep forest tone (#2E4A3A) appears on seasonal folio collections and gift-wrapping detail pages, holding the nature-adjacent positioning that both quill and fox imply. Corner radii are almost architectural — {rounded.none} on buttons and inputs, {rounded.xs} on cards — echoing the shear-cut precision of good paper stock; only category pills and search chips float on {rounded.full} to signal browsability. Spacing is generous throughout: product grids breathe at {spacing.xl} gutters, section breaks hold at {spacing.section}, and single-product editorial layouts stretch to full viewport width before the content column retreats to a readable 720px line length. The nav sits narrow and lean at 64px with one hairline below, deferring entirely to the flatlay photography and ink-prose voice that carry the actual brand.

colors:
  primary: "#C4622D"
  primary-active: "#A84E20"
  primary-disabled: "#E5BBA4"
  ink: "#1A1714"
  body: "#3B3530"
  muted: "#7A6F67"
  muted-soft: "#A89E96"
  hairline: "#DDD5CA"
  hairline-soft: "#EDE8E1"
  canvas: "#FDFAF5"
  surface-soft: "#F5EFE5"
  surface-card: "#FFFFFF"
  surface-warm: "#F0E8D8"
  on-primary: "#FFFFFF"
  forest: "#2E4A3A"
  forest-muted: "#4A6B58"
  fog: "#E8E2DA"

typography:
  display-xl:
    fontFamily: "'Freight Display Pro', 'Playfair Display', 'IM Fell English', Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Freight Display Pro', 'Playfair Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Freight Display Pro', 'Playfair Display', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Apercu', 'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "'Apercu', 'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.01em
  body-md:
    fontFamily: "'Apercu', 'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Apercu', 'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Apercu', 'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  label-uppercase:
    fontFamily: "'Apercu', 'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  button-md:
    fontFamily: "'Apercu', 'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Apercu', 'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Apercu', 'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  price:
    fontFamily: "'Freight Display Pro', 'Playfair Display', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  price-sm:
    fontFamily: "'Freight Display Pro', 'Playfair Display', Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  paper-spec:
    fontFamily: "'Apercu', 'DM Sans', 'Inter', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.04em

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
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
        cursor: not-allowed

  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1.5px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
    states:
      hover:
        backgroundColor: "{colors.surface-soft}"

  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    padding: 0
    textDecoration: underline-on-hover

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 14px
    height: 48px
    placeholderColor: "{colors.muted-soft}"

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoTypography: "{typography.display-sm}"
    logoColor: "{colors.ink}"
    activeLinkColor: "{colors.primary}"

  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "4/5"
    imageRounded: "{rounded.xs}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-sm}"
    priceColor: "{colors.body}"
    categoryTypography: "{typography.label-uppercase}"
    categoryColor: "{colors.muted}"
    gap: "{spacing.sm}"
    hoverEffect: image-scale-1.02

  hero-editorial:
    layout: full-bleed-split
    backgroundColor: "{colors.surface-soft}"
    imagePosition: right
    imageWidthPercent: 55
    contentPadding: "{spacing.xxl} {spacing.section}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaComponent: button-primary
    ctaMarginTop: "{spacing.lg}"
    minHeight: 580px

  hero-flatlay:
    layout: full-bleed-centered
    backgroundColor: "{colors.surface-warm}"
    imageObjectFit: cover
    overlayColor: "rgba(26,23,20,0.35)"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.canvas}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.fog}"
    ctaComponent: button-primary
    minHeight: 520px

  category-pill:
    backgroundColor: "{colors.fog}"
    textColor: "{colors.ink}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    states:
      active:
        backgroundColor: "{colors.ink}"
        textColor: "{colors.canvas}"

  product-badge:
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    position: absolute-top-left
    variants:
      new:
        backgroundColor: "{colors.primary}"
        textColor: "{colors.on-primary}"
      bestseller:
        backgroundColor: "{colors.forest}"
        textColor: "{colors.canvas}"
      limited:
        backgroundColor: "{colors.ink}"
        textColor: "{colors.canvas}"

  paper-spec-block:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    labelTypography: "{typography.label-uppercase}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.paper-spec}"
    valueColor: "{colors.body}"
    rowGap: "{spacing.sm}"

  monogram-stamp:
    shape: circle
    size: 48px
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.full}"

  collection-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-sm}"
    headlineColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xxl}"
    linkTypography: "{typography.label-uppercase}"
    linkColor: "{colors.fog}"
    linkHoverColor: "{colors.canvas}"
    accentColor: "{colors.primary}"

  newsletter-strip:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    inputComponent: text-input
    ctaComponent: button-primary
    padding: "{spacing.section} {spacing.xxl}"
    rounded: "{rounded.none}"

  search-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    closeIconColor: "{colors.muted}"

  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.fog}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.label-uppercase}"
    headingColor: "{colors.fog}"
    dividerColor: "{colors.body}"
    padding: "{spacing.section} {spacing.xxl} {spacing.xxl}"
    logoColor: "{colors.canvas}"

## Components

### Buttons

**`button-primary`** — A sharp-cornered ({rounded.none}) copper-filled rectangle at 48px tall, using uppercase tracked lettering ({typography.button-md}) so the label reads precise rather than casual. On hover the fill deepens from #C4622D to #A84E20; the disabled state bleaches to #E5BBA4 while holding the white label, preserving the shape's authority. Used exclusively for "Add to Cart," checkout confirmation, and hero CTAs where one dominant action needs to be unmistakable.

**`button-secondary`** — Identical in dimension and uppercase tracking to `button-primary` but hollow: parchment fill with a 1.5px ink border. A {colors.surface-soft} wash appears on hover. Used for supporting actions — "View the Collection," "Save to Wishlist," "See All Notebooks" — that sit alongside a primary CTA without competing.

**`button-text`** — Zero padding, transparent field, copper label in {typography.button-sm}. Underline appears on hover. Reserved for inline prose links ("learn about our paper sourcing") and low-stakes actions like "Remove from bag."

### Inputs

**`text-input`** — Flat-edged ({rounded.none}) at 48px tall, parchment canvas background, hairline border that thickens to 1.5px ink on focus. Placeholder runs in {colors.muted-soft} and retreats on first keystroke; no floating labels. Appears in search, newsletter capture, personalization name fields, and checkout address rows.

### Navigation

**`nav-bar`** — 64px tall, full-width, parchment canvas with a single 1px {colors.hairline-soft} below. Left-anchored wordmark in {typography.display-sm} at {colors.ink}. Category links in {typography.nav-link} at 0.03em tracking; the active link shifts to {colors.primary} copper. Cart, search, and account icons sit right-aligned. At mobile widths, links collapse into a hamburger that draws a full-screen right-side drawer; the wordmark remains centered.

### Product Cards

**`product-card`** — 4:5 portrait image with {rounded.xs} corner, then {spacing.sm} gap below before a category label in {typography.label-uppercase}/{colors.muted}, product name in {typography.title-sm}/{colors.ink}, and price in the brand serif via {typography.price-sm}/{colors.body}. On hover the image scales to 102% inside `overflow: hidden`. A single `product-badge` may float absolute at top-left of the image; never two badges stacked.

### Hero Blocks

**`hero-editorial`** — A split-panel layout: 55% right-side product flatlay on {colors.surface-soft}, 45% left content column with {spacing.xxl} horizontal padding. Headline in {typography.display-xl}, subhead in {typography.body-md}/{colors.body}, then `button-primary` below {spacing.lg} gap. Minimum 580px tall. The image bleeds flush to the viewport edge while the content side sits on parchment.

**`hero-flatlay`** — Full-bleed overhead photograph at 520px minimum height. A 35% dark scrim (#1A1714 at 0.35 opacity) sits over the image; headline in {typography.display-xl}/{colors.canvas}, subhead in {typography.body-md}/{colors.fog}. Used on seasonal and gift-guide landing pages where a single mood composition needs to carry the full entry before scroll.

### Taxonomy & Badges

**`category-pill`** — {rounded.full} chips at {colors.fog} fill, {typography.label-uppercase}. Active state inverts to {colors.ink} fill with {colors.canvas} text, making the selected filter clearly distinct from the rest. On mobile these sit in a horizontal scroll row above the product grid.

**`product-badge`** — Rectangular, {rounded.none}, 11px uppercase in three color variants: copper (NEW), forest (BESTSELLER), ink (LIMITED). One badge per card maximum, pinned absolute to the top-left corner of the image container. Never placed below the image.

### Paper Specification Block

**`paper-spec-block`** — The most stationery-specific component in the system. A {colors.surface-soft} panel on product detail pages listing paper weight (gsm), ruling style, sheet count, cover material, and binding type in a two-column label/value grid. Labels in {typography.label-uppercase}/{colors.muted}; values in {typography.paper-spec}/{colors.body}. Hairline border all sides, {rounded.none}. This block does the work a textile brand would do with a fabric swatch — it is the trust mechanism, not decoration.

### Stamps & Identity Marks

**`monogram-stamp`** — A 48px copper circle ({rounded.full}) showing a customer's initials in {typography.display-sm}/{colors.canvas} on {colors.primary} fill. Appears on personalization preview screens, gift packaging mockups, and order confirmation. Not used in navigation, product grids, or general UI patterns.

### Collection Strip

**`collection-strip`** — Full-width {colors.ink} band at {spacing.section} vertical padding, typically placed between distinct product-grid sections on collection and landing pages. Headline in {typography.display-sm}/{colors.canvas}; secondary links in {typography.label-uppercase}/{colors.fog} that shift to {colors.canvas} on hover. The copper accent ({colors.primary}) touches only decorative rule lines or illustrative details, not link text.

### Newsletter Strip

**`newsletter-strip`** — {colors.surface-warm} full-width band, centered two-column on desktop: headline + subhead left, inline input + CTA right. Headline in {typography.display-sm}/{colors.ink}, body in {typography.body-sm}/{colors.body}. The `text-input` and `button-primary` share a single row on desktop; at mobile they stack full-width with {spacing.sm} gap between.

### Search Chip

**`search-chip`** — {rounded.full} pills in {colors.surface-soft} with a 1px {colors.hairline} border, {typography.body-sm}, and a {colors.muted} close icon. Used in the search overlay to display recent searches and active filter terms. On focus-within the chip border thickens to {colors.ink}.

### Footer

**`footer`** — {colors.ink} background with four link columns in {typography.body-sm}/{colors.muted-soft}, column headings in {typography.label-uppercase}/{colors.fog}. Wordmark appears top-left in {colors.canvas}. A 1px {colors.body} horizontal rule separates the link grid from the legal row. Link hover shifts to {colors.canvas}.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to wordmark + hamburger (right-side drawer); hero-editorial stacks image above content at 100vw; category-pills scroll horizontally; newsletter input and CTA stack vertically; paper-spec-block reorganizes to single-column definition list |
| Tablet | 744–1128px | Two-column product grid; nav shows wordmark + icon trio only (search, cart, account); hero-editorial enters split layout at 50/50; collection-strip headline shrinks to {typography.display-md} |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav with all category links exposed; hero-editorial at full 55/45 split; all spacing values at specification |
| Wide | > 1440px | Content column max-width 1440px centered; product grid capped at four columns; hero photography scales while content column holds width |

### Touch Targets

- All buttons minimum 48px tall; icon-only controls minimum 44×44px with invisible padding
- Category pills padded to minimum 40px tall on mobile
- Product cards carry a full-area tap target including the image — no separate CTA needed on grid view
- Nav hamburger hit area 44×44px

### Collapsing Strategy

- Nav category links collapse to icon row at tablet, then to single hamburger at mobile
- Hero copy renders above image on mobile so the hook reads before the product
- Paper-spec-block converts from 2-column table to single-column definition list at mobile
- Footer link grid: four columns on desktop, two at tablet, single-column accordion at mobile
- Monogram-stamp hides on screens narrower than 375px; personalization preview becomes its own full-screen step in the flow

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No colors extracted**: The live site returned zero hex values. Every palette entry in this file is inferred from brand name, stationery category conventions, and editorial brand aesthetics. Treat all hex values as hypotheses requiring verification against the actual rendered site.
- **No font stacks extracted**: Typography families (Freight Display Pro, Apercu) reflect premium stationery conventions. The site may use licensed display fonts (custom or through Adobe Fonts/Fontspring) not detectable without full JS rendering.
- **No meta theme-color**: Could not confirm a machine-readable primary brand color from any reliable extracted signal.
- **Platform not confirmed**: Shopify flag was False; the actual platform (Webflow, custom, Squarespace) is unknown and affects component class-name conventions and available section types.
- **No page title captured**: Could not verify official wordmark casing, tagline, or subtitle from the document title.
- **Component inventory entirely inferred**: Whether a live monogram/personalization tool, subscription model, or gift-wrapping configurator exists could not be confirmed without screenshot access or HTML inspection.
- **Forest green (#2E4A3A) is speculative**: Added on category-convention grounds; may not appear in the actual brand palette.
- **Serif identity unconfirmed**: Freight Display is a common choice in this aesthetic tier but the brand may use a proprietary or different editorial face entirely.
