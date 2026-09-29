---
version: alpha
name: "Barlow Tyrie"
source_url: "https://www.teak.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Forest green on white linen — that is the first impression teak.com delivers, the palette of an English garden lunch translated into a digital system anchored on #2c5234, a deep verdant primary that colours every CTA, navigation accent, and collection heading. The gold (#f1d600) that appears alongside it is not decorative excess; it serves as the heritage mark, the "Since 1920" badge, and the occasional promotional flash against an otherwise restrained canvas. Typography runs a deliberate dual track — Goudy Old Style, a serif designed in 1915 (five years before the company was founded), handles display headlines and collection titles, lending the gravitas of letterpress catalogues to a screen medium. Source Sans Pro takes over for body copy, navigation, and interface text, its open apertures and generous x-height keeping long product descriptions legible at `{typography.body-md}` 16px. The overall weight distribution is lighter than most luxury-goods sites: display tops out at 600 rather than 800, body sits at 400, and Helvetica Neue Light appears in select caption and breadcrumb contexts where a near-whisper weight reinforces the hierarchy without competing with the product imagery. Corners stay tight — `{rounded.xs}` on buttons and inputs, `{rounded.sm}` on cards — because the furniture itself is the source of curvature, all sweeping arm rests and curved bench lines, and the UI should not mimic what the photography already shows. Spacing follows a disciplined vertical rhythm with `{spacing.section}` (64px) between major content blocks and `{spacing.lg}` (24px) between card-grid rows, giving each piece of furniture the visual breathing room it gets on an actual terrace. The colour palette is overwhelmingly neutral: five extracted grays between #626263 and #9a9a9a handle everything from body text to disabled states to metadata, while the single hairline value #e4e4e4 draws subtle borders across tables and cards. Product cards float on a warm-white surface (`{colors.surface-soft}` at #f7f6f3) that avoids the clinical sterility of pure white, hinting at the natural teak grain that dominates every product photograph. The overall system reads as an architect's specification sheet given just enough warmth to feel residential.

colors:
  primary: "#2c5234"
  primary-active: "#1e3a24"
  primary-disabled: "#8fa896"
  accent-gold: "#f1d600"
  accent-gold-active: "#d4b800"
  ink: "#222222"
  body: "#626263"
  muted: "#7a7a7c"
  muted-soft: "#9a9a9a"
  muted-light: "#929292"
  hairline: "#e4e4e4"
  hairline-soft: "#efefef"
  border-mid: "#6e6f70"
  canvas: "#ffffff"
  surface-soft: "#f7f6f3"
  surface-card: "#ffffff"
  surface-warm: "#f3f1ec"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent: "#222222"
  success: "#2c5234"
  warning: "#c45500"
  error: "#b5332a"
  star-rating: "#f1d600"
  scrim: "rgba(0, 0, 0, 0.50)"
  footer-bg: "#222222"
  footer-text: "#9a9a9a"
  heritage-badge-bg: "#f1d600"
  heritage-badge-text: "#222222"

typography:
  display-xl:
    fontFamily: "'goudy-old-style', 'Georgia', 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'goudy-old-style', 'Georgia', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'goudy-old-style', 'Georgia', 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'goudy-old-style', 'Georgia', 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.28
    letterSpacing: 0
  title-lg:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-lg:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-md:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'HelveticaNeue-Light', 'Helvetica Neue Light', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-md:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  button-lg:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-md:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  nav-category:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  price:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  collection-title:
    fontFamily: "'goudy-old-style', 'Georgia', 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  spec-label:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'source-sans-pro', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  heritage-mark:
    fontFamily: "'goudy-old-style', 'Georgia', 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px

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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.xs}"
    border: "1.5px solid {colors.primary-active}"
  button-accent:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-gold-active}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.xs}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 76px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  mega-menu:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    borderTop: "1px solid {colors.hairline}"
    boxShadow: "0 8px 24px rgba(0,0,0,0.10)"
  mega-menu-category:
    textColor: "{colors.ink}"
    typography: "{typography.nav-category}"
    marginBottom: "{spacing.md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
    hoverBoxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card-image:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.xs}"
    aspectRatio: "4/3"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-collection:
    typography: "{typography.caption-md}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.ink}"
  hero-lifestyle:
    minHeight: 560px
    overlayGradient: "linear-gradient(to right, rgba(44,82,52,0.75) 0%, rgba(44,82,52,0.25) 50%, transparent 70%)"
    padding: "{spacing.section} {spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subhead:
    typography: "{typography.body-lg}"
    textColor: "{colors.on-primary}"
    opacity: 0.9
  hero-solid:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 420px
    padding: "{spacing.section} {spacing.xl}"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.xxl} {spacing.xl}"
  collection-header-title:
    typography: "{typography.collection-title}"
    textColor: "{colors.ink}"
  collection-header-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    maxWidth: 640px
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  heritage-badge:
    backgroundColor: "{colors.heritage-badge-bg}"
    textColor: "{colors.heritage-badge-text}"
    typography: "{typography.heritage-mark}"
    rounded: "{rounded.xs}"
    padding: "6px 14px"
  fabric-swatch:
    rounded: "{rounded.xs}"
    height: 48px
    width: 48px
    border: "1px solid {colors.hairline}"
  fabric-swatch-active:
    border: "2px solid {colors.primary}"
    boxShadow: "0 0 0 2px {colors.primary}"
  dimension-table:
    backgroundColor: "{colors.canvas}"
    borderCollapse: separate
    rowOddBg: "{colors.surface-soft}"
    rowEvenBg: "{colors.canvas}"
    cellPadding: "{spacing.md} {spacing.base}"
  dimension-table-label:
    typography: "{typography.spec-label}"
    textColor: "{colors.muted}"
  dimension-table-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 48px
    border: "1px solid {colors.hairline}"
    padding: 12px 16px 12px 44px
  search-icon:
    textColor: "{colors.muted}"
    size: 20px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    separator: "/"
    activeColor: "{colors.ink}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.footer-text}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-heading:
    textColor: "{colors.on-dark}"
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.base}"
  footer-heritage-line:
    typography: "{typography.heritage-mark}"
    textColor: "{colors.muted-soft}"
  image-gallery:
    backgroundColor: "{colors.surface-warm}"
    rounded: "{rounded.sm}"
    gap: "{spacing.sm}"
  image-gallery-thumb:
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    height: 72px
    width: 72px
  image-gallery-thumb-active:
    border: "2px solid {colors.primary}"

---

## Components

### Buttons

**`button-primary`** — A solid forest-green rectangle with tight `{rounded.xs}` corners and white text in `{typography.button-lg}` weight 600. Hover darkens to `{colors.primary-active}` (#1e3a24); disabled state fades to `{colors.primary-disabled}` at reduced opacity. Used for principal CTAs: "Add to basket," "Request a quote," "Find a dealer."

**`button-secondary`** — White fill with a 1.5px green border and green text. On hover, the background shifts to `{colors.surface-soft}` and the border deepens. Maintains the same 48px height and `{rounded.xs}` radius as primary. Appears for secondary actions: "View collection," "Download specifications," "Compare."

**`button-accent`** — Gold fill (#f1d600) with dark text, reserved for promotional moments and heritage callouts. Slightly smaller at 44px height. The bright warmth of the gold against the otherwise muted palette makes it impossible to miss without being garish. Hover shifts to `{colors.accent-gold-active}`.

**`button-ghost`** — Text-only in forest green with no background or border. Used for inline navigation: "View all dining tables," "Read more," "See the full range."

### Navigation

**`nav-bar`** — A 76px white bar with a 1px `{colors.hairline}` bottom border. Logo left (likely a wordmark in forest green), primary navigation links center, utility icons (search, account, dealer locator) right. On scroll, the border drops and a very subtle shadow (`nav-bar-scrolled`) takes over. The height is slightly taller than average, giving the logo breathing room appropriate for a century-old brand.

**`mega-menu`** — Full-width dropdown panel on category hover. White background with `{spacing.xl}` padding. Category headings in `{typography.nav-category}` (uppercase, 13px, weight 700, 0.8px tracking) with sub-links in `{typography.body-sm}`. Includes lifestyle thumbnails for collections (Equinox, Aura, Linear) and a subtle top border plus soft shadow. Closes on mouse-leave.

### Product Cards

**`product-card`** — A white card with `{rounded.sm}` corners and a faint `{colors.hairline-soft}` border. The image container uses `{colors.surface-warm}` (#f3f1ec) as its background — a warm off-white that flatters teak tones and prevents the product from floating in clinical white space. Below sits the collection name in `{typography.caption-md}` muted grey, the product title in `{typography.title-sm}`, and the price in `{typography.price-sm}`. On hover, the card gains a light shadow. No image-zoom effect — the furniture's silhouette and wood grain do the work.

**`product-card-image`** — 4:3 aspect ratio on `{colors.surface-warm}` with `{rounded.xs}` inner radius. Products are typically shown from a three-quarter angle to convey scale and material finish. The warm background is the single most recognisable visual choice on the site.

### Hero

**`hero-lifestyle`** — Full-width garden or terrace photograph with a left-to-right green gradient overlay (rgba(44,82,52,0.75) fading to transparent). Headline in `{typography.display-xl}` serif white, subhead in `{typography.body-lg}` at 0.9 opacity. A primary or accent button sits below. Minimum height 560px. The gradient ensures legibility while keeping the right half — usually showing furniture arranged on a terrace — fully visible.

**`hero-solid`** — Simpler variant with a flat `{colors.primary}` green background and white text. Used for interior landing pages (About, Heritage, Dealer Network) where lifestyle photography isn't the focus. Lower minimum height at 420px.

### Collection Header

**`collection-header`** — A `{colors.surface-soft}` band spanning full width with `{spacing.xxl}` vertical padding. Collection title in `{typography.collection-title}` (32px Goudy Old Style), description in `{typography.body-md}` capped at 640px width. Sits between the breadcrumb and the product grid, orienting users within Barlow Tyrie's deep collection taxonomy (Equinox, Aura, Linear, Titan, Monaco, etc.).

### Material & Heritage Badges

**`material-badge`** — Small `{colors.surface-soft}` pill with uppercase text in `{typography.badge}`. Indicates material composition: "TEAK," "ALUMINIUM," "STAINLESS STEEL," "CERAMIC." Positioned on product cards or detail pages near the title.

**`heritage-badge`** — Gold background (#f1d600) with dark text in `{typography.heritage-mark}` (14px Goudy Old Style, weight 600). Reads "EST. 1920" or "SINCE 1920." Appears in the nav-bar, hero blocks, and footer. The serif face on the gold ground is one of the few moments where decoration is permitted.

### Fabric & Finish Swatches

**`fabric-swatch`** — 48×48px tiles with `{rounded.xs}` corners and a 1px `{colors.hairline}` border, used on product detail pages for selecting cushion fabrics and parasol canopy colours. Swatches display the actual fabric texture or solid colour.

**`fabric-swatch-active`** — Selected state adds a 2px green border with a matching 2px ring via box-shadow. The double ring clearly marks the active choice without covering the swatch fill.

### Dimension & Specification Table

**`dimension-table`** — Alternating row backgrounds (`{colors.surface-soft}` / `{colors.canvas}`) with labels in `{typography.spec-label}` muted grey and values in `{typography.spec-value}` ink. Outdoor furniture demands detailed dimensions (seat height, table diameter, umbrella clearance, weight), and this table handles dense specification data without outer borders — the alternating rows provide sufficient grouping.

### Search

**`search-bar`** — A 48px white input with `{rounded.xs}` corners, left-padded 44px to accommodate a `{colors.muted}` search icon. Focus state switches the border to `{colors.primary}`. Likely opens an overlay or dropdown with type-ahead results showing product thumbnails, collection names, and material filters.

### Badges

**`badge-sale`** — Red (#b5332a) pill with white uppercase text for markdowns and seasonal promotions. Positioned over the product-card image corner.

**`badge-new`** — Forest-green pill with white uppercase text for newly launched collections or restocked items.

### Image Gallery

**`image-gallery`** — The product detail page gallery uses a primary image area on `{colors.surface-warm}` with `{rounded.sm}` corners. Below or alongside sits a row of 72×72px thumbnails (`image-gallery-thumb`) with `{rounded.xs}` corners. Active thumbnail gets a 2px green border. The warm background unifies all product shots regardless of the specific piece's wood tone.

### Breadcrumb

**`breadcrumb`** — Lightweight trail in `{typography.caption}` (12px, Helvetica Neue Light, weight 300) with forward-slash separators. Parent links in `{colors.muted-soft}`, current page in `{colors.ink}`. Navigates the hierarchy: Home / Dining / Teak Dining Tables / Titan Table 300.

### Footer

**`footer`** — Dark background (#222222) with grey text (`{colors.footer-text}`). Organised in 4–5 columns: Collections, Materials, About, Dealer Network, Customer Service. Headings in `{typography.title-sm}` white, links in `{typography.body-sm}` grey. A heritage line in `{typography.heritage-mark}` reads "Award-winning outdoor furniture since 1920," centred below the columns. Social icons and legal links sit in a final row separated by a hairline border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid. Mega-menu becomes full-screen slide-over with accordion categories. Hero height reduces to 380px with bottom-aligned text. Image gallery switches to horizontal swipe carousel. Nav collapses to hamburger + logo + search icon. Fabric swatches scroll horizontally. |
| Tablet | 744–1128px | Two-column product grid. Mega-menu remains dropdown but narrows to single-row thumbnails. Hero maintains 480px height. Side-by-side layout for specification tables. Collection header description wraps to full width. |
| Desktop | 1128–1440px | Three-column product grid. Full mega-menu with collection thumbnails and lifestyle images. Hero at full 560px+. Image gallery shows primary + thumbnail strip side by side. Dimension table displays at full width. |
| Wide | > 1440px | Content maxes at 1320px centred. Margins grow symmetrically. Four-column grid available for collection landing pages. Hero imagery fills viewport width while text area remains constrained. |

### Touch Targets

- All interactive elements maintain minimum 44×44px tap target on mobile
- Fabric swatches scale to 56×56px on touch with 8px gap between them
- Nav hamburger icon padded to 48px square
- Footer links spaced with `{spacing.md}` vertical gap on mobile
- Add-to-basket button stretches to full width on mobile at 52px height

### Collapsing Strategy

- Desktop mega-menu → mobile full-screen slide-over accordion with collection thumbnails retained
- Product specification tables → stacked label/value pairs on mobile, no horizontal scroll
- Image gallery grid → horizontal swipe carousel with dot indicators on mobile
- Hero side-by-side gradient/image → full-bleed image with bottom gradient and stacked text below on mobile
- Footer multi-column → single accordion column with expandable sections
- Breadcrumb truncates middle segments on mobile, showing first and last two levels with ellipsis
- Collection header centres text and removes max-width constraint on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted colour palette is heavily weighted toward grays (#6e6f70, #6f6e6e, #7a7a7c, #929292, #626263) which are difficult to differentiate in function; the assigned roles (body, muted, muted-soft, muted-light) are best-guess mappings
- Goudy Old Style and Source Sans Pro were detected in font-family stacks but exact weights and size scales are estimated from brand positioning rather than measured from computed styles
- Helvetica Neue Light appears in the font stack but its specific usage contexts (caption, breadcrumb, or broader body role) could not be confirmed
- The site is not on Shopify, and its platform could not be determined — CMS-specific component patterns (cart drawer, quick-view modal) may differ from what is modelled here
- Exact border-radius values are inferred from the brand's architectural aesthetic; the site may use `{rounded.none}` more aggressively than modelled
- Animation and transition timing (hover states, menu transitions, image gallery interactions) could not be observed
- Dark-mode tokens are not defined — the site almost certainly does not offer a dark theme
- Specific icon set (line weight, style, library) is unknown
- The precise collection taxonomy and depth of the mega-menu structure could not be confirmed from extraction alone
- No meta theme-color was detected, so mobile browser chrome colour is unknown
