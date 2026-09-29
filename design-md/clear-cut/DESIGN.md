---
version: alpha
name: "The Clear Cut"
source_url: "https://www.theclearcut.co"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  NoeDisplay paired with Raisonne is the tell — The Clear Cut is a media property that happens to sell diamonds, not a jeweler that added a blog. NoeDisplayMedium renders headlines with the authority of a fashion magazine masthead; its wedge serifs carry editorial confidence that Garamond fallbacks echo at lower fidelity. Raisonne's geometric letterforms handle navigation, specification tables, and carat weights with the crispness the 4Cs demand. The warm cream canvas (#f5f4f2) is the brand's most consequential decision: it refuses the cold white-and-steel grammar of traditional diamond retail, reading instead as though a printed lookbook has been digitised. The palette extends from this cream into a cluster of soft pastels — powder blue (#c4d6e0), blush peach (#f7d0bb), dusty lavender (#e6d1ea), and muted mauve (#947481) — used as surface tints for editorial cards, education modules, and category pages rather than as CTA colors. Primary actions run on near-black (#202223), setting a sober, authoritative tone against the warm ground. Button shapes stay mildly rounded (`{rounded.sm}`) rather than fully pill-shaped, signalling precision over approachability. The overall register is closer to a magazine like Porter or Vogue Living than to a traditional jewellery counter — prices are treated as data, diamonds as subjects worth studying, and the site architecture foregrounds education (What Is the Best Diamond Shape? The 4Cs Explained) as prominently as commerce. The extraction surfaced a notably broad palette for a single brand; the pastels are almost certainly thematic background swatches for content categories rather than a single accent, making the powder blue #c4d6e0 the best candidate for the "primary" brand color anchoring the cool editorial identity, even while dark ink handles the action layer.

colors:
  primary: "#c4d6e0"
  primary-active: "#a8bfcc"
  primary-disabled: "#dfe9ed"
  on-primary: "#202223"
  action: "#202223"
  action-hover: "#3a3a3a"
  on-action: "#f5f4f2"
  ink: "#202223"
  body: "#3a3a3a"
  muted: "#6d7175"
  muted-soft: "#606060"
  hairline: "#dadada"
  hairline-soft: "#e0e0e0"
  canvas: "#f5f4f2"
  canvas-pure: "#fafafa"
  surface-soft: "#faf0ec"
  surface-card: "#ffffff"
  accent-blush: "#f7d0bb"
  accent-blush-deep: "#ffcdb7"
  accent-lavender: "#e6d1ea"
  accent-mauve: "#947481"
  on-accent-mauve: "#fafafa"
  accent-blue-muted: "#c9d6db"
  accent-gold: "#ffc500"
  error: "#ff5757"

typography:
  display-xl:
    fontFamily: "NoeDisplayMedium, Garamond, Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "NoeDisplayMedium, Garamond, Georgia, serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "NoeDisplayRegular, Garamond, Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "NoeDisplayRegular, Garamond, Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "RaisonneANSemiBold, Raisonne, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.05em
    textTransform: uppercase
  title-sm:
    fontFamily: "RaisonneANSemiBold, Raisonne, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "Raisonne, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Raisonne, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Raisonne, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  label:
    fontFamily: "RaisonneANSemiBold, Raisonne, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.09em
    textTransform: uppercase
  price:
    fontFamily: "Raisonne, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  spec-value:
    fontFamily: "Raisonne, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "RaisonneANSemiBold, Raisonne, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "RaisonneANSemiBold, Raisonne, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "Raisonne, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.03em

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
    backgroundColor: "{colors.action}"
    textColor: "{colors.on-action}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.action-hover}"
    textColor: "{colors.on-action}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.action}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px
    border: "1px solid {colors.action}"
  button-secondary-hover:
    backgroundColor: "{colors.action}"
    textColor: "{colors.on-action}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas-pure}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.ink}"
    outline: none
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas-pure}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    padding: "{spacing.base}"
  product-card-label:
    typography: "{typography.label}"
    textColor: "{colors.muted}"
  product-card-title:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  hero:
    backgroundColor: "{colors.canvas}"
    layout: split-50-50
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  hero-mobile:
    layout: stack-image-first
    headlineTypography: "{typography.display-lg}"
  education-card:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    headlineTypography: "{typography.display-md}"
    labelTypography: "{typography.title-sm}"
  education-card-blush:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    headlineTypography: "{typography.display-md}"
    labelTypography: "{typography.title-sm}"
  education-card-lavender:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    headlineTypography: "{typography.display-md}"
    labelTypography: "{typography.title-sm}"
  education-card-mauve:
    backgroundColor: "{colors.accent-mauve}"
    textColor: "{colors.on-accent-mauve}"
    rounded: "{rounded.none}"
    padding: "{spacing.xl}"
    headlineTypography: "{typography.display-md}"
    labelTypography: "{typography.title-sm}"
  diamond-spec-chip:
    backgroundColor: "{colors.canvas-pure}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    height: 32px
  diamond-spec-chip-active:
    backgroundColor: "{colors.action}"
    textColor: "{colors.on-action}"
    border: "1px solid {colors.action}"
    rounded: "{rounded.full}"
  filter-panel:
    backgroundColor: "{colors.canvas}"
    borderRight: "1px solid {colors.hairline}"
    padding: "{spacing.xl}"
  filter-panel-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  spec-table-row:
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"
  spec-table-key:
    typography: "{typography.label}"
    textColor: "{colors.muted}"
  spec-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  consultation-banner:
    backgroundColor: "{colors.accent-blush}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
    rounded: "{rounded.none}"
  category-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "#ffffff"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-new:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  section-divider:
    borderTop: "1px solid {colors.hairline}"
    margin: "{spacing.section} 0"
  footer:
    backgroundColor: "{colors.action}"
    textColor: "{colors.on-action}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-action}"

## Components

### Buttons

**`button-primary`** — Near-black (#202223) fill with warm cream text, set in RaisonneANSemiBold uppercase at 14px with 0.08em tracking. Minimal rounding (`{rounded.sm}`, 4px) keeps the shape precise rather than friendly. Hover darkens to `{colors.action-hover}` (#3a3a3a); disabled state uses `{colors.hairline}` background with `{colors.muted}` text. Used for all primary commerce CTAs: "Shop Now," "Book a Consultation," "Add to Cart."

**`button-secondary`** — Transparent background with a 1px `{colors.action}` border; typography identical to `button-primary`. On hover, fills with `{colors.action}` and flips text to `{colors.on-action}` in a clean inversion. Used for secondary navigation CTAs like "Learn More" and "View All Styles."

**`button-text`** — Underlined inline link, no border or background. Used within editorial body copy and education articles for contextual cross-links.

### Text Input

**`text-input`** — Pure white (`{colors.canvas-pure}`) on the warm cream canvas creates a subtle lift without a heavy shadow. 1px `{colors.hairline}` border, 48px tall, body-md Raisonne. Focus replaces the hairline with a full ink border — no glow, no colour shift. Error state swaps border to `{colors.error}`. Placeholder text in `{colors.muted}`.

### Navigation Bar

**`nav-bar`** — 72px tall on the warm canvas ground, hairline bottom border. Category links in Raisonne 14px with light tracking; active category underlined with a 2px ink rule. The wordmark renders in NoeDisplayMedium left-docked. The bar is sticky on scroll with no background colour change or elevation shadow — the hairline alone marks the separation.

### Product Card

**`product-card`** — Sharp-cornered (`{rounded.none}`) portrait grid tile. Ring image in a 4:5 crop; below it a `{typography.label}` stone-shape/metal descriptor in `{colors.muted}`, the ring name in NoeDisplay `{typography.display-sm}`, and price in `{typography.price}` Raisonne. Hover interaction: image scales subtly (transform: scale(1.02)) with no shadow or border — precision over flourish.

### Hero

**`hero`** — 50/50 editorial split: left column NoeDisplayMedium headline in `{typography.display-xl}`, Raisonne subhead in `{typography.body-md}`, and a `button-primary`; right column full-bleed ring or lifestyle photography. The warm canvas surround (`{colors.canvas}`) avoids pure-white brightness. On mobile, layout stacks image above headline per `hero-mobile`.

### Education Cards

**`education-card`** / **`education-card-blush`** / **`education-card-lavender`** / **`education-card-mauve`** — Solid-colour editorial tiles used for content category navigation (The 4Cs, Diamond Shapes, Buying Guides, Metal Types). Each variant maps to one of the extracted pastels: powder blue (`{colors.primary}`), blush peach (`{colors.accent-blush}`), dusty lavender (`{colors.accent-lavender}`), or mauve (`{colors.accent-mauve}`). No imagery — headline in NoeDisplay `{typography.display-md}`, category label in Raisonne `{typography.title-sm}`. Zero border-radius, consistent with the sharp editorial grid.

### Diamond Spec Chips / Filter Panel

**`diamond-spec-chip`** — Pill-shaped (`{rounded.full}`) filter token for ring-builder and search pages; selects carat weight, cut grade, colour, and clarity grades. Inactive: white background, ink text, hairline border. Active (`diamond-spec-chip-active`): inverts to full ink background with cream text — no animation, a hard swap. **`filter-panel`** anchors the left rail with a hairline right border; each group headed by `{typography.title-sm}` with chip rows below.

### Specification Table

**`spec-table-row`** — Used on individual diamond PDPs to display GIA certificate data (cut, colour, clarity, carat, fluorescence, depth %, table %). Key column in `{typography.label}` at `{colors.muted}`; value column in `{typography.spec-value}` at `{colors.ink}`. Rows separated by soft hairlines; no outer border, no background alternation.

### Consultation Banner

**`consultation-banner`** — Full-width blush-peach band (`{colors.accent-blush}`) used as an interstitial CTA between content sections for "Work With a Diamond Expert." Headline in NoeDisplay `{typography.display-md}`, body in Raisonne `{typography.body-md}`, anchored by a `button-primary`. No rounding, no imagery — the solid colour block functions as an editorial section break.

### Footer

**`footer`** — Ink-dark background (`{colors.action}`) with cream-white text inverts the page canvas cleanly. Four-column link grid on desktop (Shop, Learn, Company, Social), column headings in `{typography.title-sm}` all-caps Raisonne, links in `{typography.body-sm}`. The high-contrast inversion closes the editorial scroll with authority.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; hero stacks image above headline; nav collapses to logo + hamburger; filter panel becomes full-screen bottom-sheet drawer; product grid 1-column; spec chips scroll horizontally in a pill row |
| Tablet | 744–1128px | 2-column product grid; hero maintains split with tighter padding; filter panel shown as collapsible left sidebar; education cards in a 2-column grid |
| Desktop | 1128–1440px | 3–4 column product grid; filter panel fixed left rail; hero 50/50 split at full scale; education cards 4-column row |
| Wide | > 1440px | Max-width container (~1440px) centred; grid gutters expand; hero image bleeds further right; display-xl headline may scale to 64px |

### Touch Targets

- All filter chips minimum 40px tall; pill form allows natural touch width
- CTA buttons minimum 48px height across all breakpoints
- Hamburger icon minimum 44×44px hit area
- Spec table rows minimum 48px tall on mobile for tap accuracy
- "Book a Consultation" CTA on mobile PDPs: full-width sticky button at 52px tall

### Collapsing Strategy

- Filter panel collapses to a "Filter & Sort" bottom-sheet drawer on mobile with apply/clear actions at the base
- Multi-column education card grids reduce to a horizontal scroll carousel on mobile, preserving the colour-block aesthetic rather than stacking tall
- Sticky nav reduces to wordmark + hamburger; search icon persists at right
- Spec table on mobile: key-value pairs stack vertically (label above value) rather than side by side
- Hero headline scale drops from `{typography.display-xl}` to `{typography.display-lg}` on mobile; subhead to `{typography.body-sm}`

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No confirmed primary CTA button color from extraction — `{colors.action}` (#202223) is inferred as the button fill from the dark-dominant palette; if the brand uses a pastel accent for CTAs this would need revision
- Exact NoeDisplay and Raisonne numeric font weights not confirmed — 500/600 values are editorial-norm inferences, not extracted CSS
- Ring-builder step-flow UI (gem selection → setting → metal → size → engraving) not extractable from static hints; component structure inferred from category conventions
- Exact nav height and sticky-scroll behavior not confirmed from extraction
- Dark mode or seasonal theme variants not surfaced; palette assumed single warm-light mode
- Shopify theme name not identified; markup likely follows Dawn or a custom theme; component semantics may differ
- Animation and transition timing not extractable; standard 200–300ms ease assumed throughout
- The breadth of the pastel palette (#c4d6e0, #f7d0bb, #e6d1ea, #c9d6db, #947481, #faf0ec) suggests per-category thematic backgrounds; exact color-to-category mapping could not be confirmed from static extraction
