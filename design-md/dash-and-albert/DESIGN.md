---
version: alpha
name: "Dash & Albert"
source_url: "https://annieselke.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Braided wool and hand-loomed cotton have always defined Dash & Albert's physical identity, and the digital palette reflects that same earthy-then-surprising logic — an anchoring range of warm grays and near-blacks (#5a5957, #414141, #272d45) grounds every page before the deep teal primary (#0e7a82) surfaces like a found stone in still water. The serif editorial voice (Lora) carries collection headings and brand story passages while Avenir Next Demi handles commerce mechanics — a deliberate split that reads as artisan-made-available-at-scale rather than mass market. Buttons sit at {rounded.none} with widely-spaced uppercase tracking on their labels, an old-world signage move that prevents the commerce layer from feeling transactional. The terra cotta accent (#c64836) appears only in sale and promotional contexts, never in primary navigation — a warm signal that reads "markdown" without cheapening the page's default register. Forest greens (#1f3b34, #284039) appear in editorial callouts and outdoor-collection category tiles, reinforcing the brand's claim on landscaped interiors. A bright aqua (#00caaa) and a pale mint surface (#b2f9e9) show up in hover states and seasonal tint bands — present enough to carry freshness, sparse enough that they never override the warm neutrality that woven textures already bring. The muted purple-gray (#676986) provides a mid-tone for secondary labels and breadcrumbs, adding perceptual depth to what might otherwise read as a flat two-tone palette. Product cards lean on close-crop photography rather than lifestyle staging, trusting that a good rug surface shot carries its own argument. The overall spacing grammar is generous — section breaks run at {spacing.section} — matching the unhurried pace of someone choosing a rug for a room they care about.

colors:
  primary: "#0e7a82"
  primary-active: "#0a616a"
  primary-disabled: "#9dcdd1"
  accent: "#c64836"
  accent-active: "#783124"
  accent-disabled: "#e8b0a8"
  aqua-bright: "#00caaa"
  surface-mint: "#b2f9e9"
  forest: "#1f3b34"
  forest-mid: "#284039"
  ink: "#272d45"
  body: "#414141"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#d3d4dd"
  hairline-soft: "#e5e5eb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f8"
  surface-card: "#f4f4f6"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Lora', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Avenir Next Demi', 'Avenir Next', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Avenir Next Demi', 'Avenir Next', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Avenir Next', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir Next', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir Next', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  label-uppercase:
    fontFamily: "'Avenir Next Demi', 'Avenir Next', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Avenir Next Demi', 'Avenir Next', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Avenir Next Demi', 'Avenir Next', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Avenir Next', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Avenir Next', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.3px
  badge-text:
    fontFamily: "'Avenir Next Demi', 'Avenir Next', Inter, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1px
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
    padding: 14px 32px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.ink}"
    iconColor: "{colors.ink}"
  promo-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-uppercase}"
    height: 36px
    textAlign: center
  product-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "5/4"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.body}"
    salePriceColor: "{colors.accent}"
    strikethroughColor: "{colors.muted}"
    hoverImageScale: 1.03
    hoverShadow: "0 4px 16px rgba(0,0,0,0.08)"
    gap: "{spacing.sm}"
  color-swatch:
    size: 20px
    borderRadius: "{rounded.full}"
    borderUnselected: "1px solid {colors.hairline}"
    borderSelected: "2px solid {colors.ink}"
    gap: "{spacing.xs}"
    tapTarget: 32px
  sale-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge-text}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    position: top-left of card image
  new-badge:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-text}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    position: top-left of card image
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    overlayColor: "rgba(39,45,69,0.25)"
    titleTypography: "{typography.display-xl}"
    titleColor: "{colors.on-dark}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.on-dark}"
    ctaBackgroundColor: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    minHeight: 560px
    contentPadding: "{spacing.xxl}"
    textAlignment: left
  collection-tile:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    labelTypography: "{typography.label-uppercase}"
    labelColor: "{colors.ink}"
    labelHoverColor: "{colors.primary}"
    gap: "{spacing.sm}"
  editorial-band:
    backgroundColor: "{colors.forest}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    accentRuleColor: "{colors.aqua-bright}"
    padding: "{spacing.xxl} {spacing.section}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
    activeTextColor: "{colors.primary}"
    activeUnderline: "2px solid {colors.primary}"
    height: 48px
    position: sticky
  breadcrumb:
    typography: "{typography.caption}"
    parentColor: "{colors.muted}"
    currentColor: "{colors.body}"
    separatorColor: "{colors.hairline}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1.5px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "{spacing.sm} {spacing.md}"
    height: 40px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    height: 44px
    padding: "0 {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.label-uppercase}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
    columns: 4

## Components

### Buttons
**`button-primary`** — Deep teal (#0e7a82) fill with white text, zero border radius, and uppercase Avenir Next Demi at 13px with 1.5px letter-spacing. The sharp corner echoes the cut edge of a rug sample. Active state darkens to #0a616a; disabled washes to the soft teal-gray #9dcdd1. Padding is generous at 14px vertical and 32px horizontal, giving the uppercase label room to read without crowding.

**`button-secondary`** — White canvas fill with a 1px ink (#272d45) border and matching uppercase label. Used for "Add to Wishlist," secondary nav CTAs, and "View All" links within collection bands. Shares the same 0px radius as primary to maintain surface consistency.

**`button-accent`** — Terra cotta (#c64836) fill, reserved for promotional contexts only — sale events, clearance pages, and limited-time offer callouts. Never appears as a primary action on a standard product or collection page.

**`button-ghost`** — Transparent fill, hairline (#d3d4dd) border. Used in modal dismiss actions, filter overlays, and any context where a full-fill button would compete with surrounding content.

### Navigation
**`nav-bar`** — White canvas, 64px tall, separated from page by a soft hairline bottom border. Logo in ink at left; centered category links in Avenir Next nav-link style with light tracking; right cluster holds search, account, and cart bag icons. A `promo-banner` strip (36px, ink background, white uppercase text) sits above and collapses on scroll past 40px.

**`promo-banner`** — Ink (#272d45) background strip, white label-uppercase text, centered. Used for shipping thresholds, seasonal promotions, and site-wide sale announcements. Never used for persistent brand messaging.

### Product Card
**`product-card`** — Zero-radius cards with a 5:4 crop and a soft surface-soft (#f7f7f8) image stage. Product title in body-sm Avenir Next; price in price-display at 18px weight 400. Sale price swaps to terra cotta (#c64836) alongside a strikethrough original price in muted gray. A color-swatch row sits between title and price showing available colorways as 20px round chips. On hover the image scales to 1.03 and a subtle shadow lifts the card off the grid.

**`color-swatch`** — 20px round swatches, 1px hairline ring at rest, 2px ink ring on selected state. Tap target expands to 32px invisibly. Used on both product cards and the full PDP colorway picker.

### Badges
**`sale-badge`** — Terra cotta (#c64836) fill, zero radius, badge-text Avenir Next Demi, pinned to the top-left corner of the product card image. Appears only on discounted items.

**`new-badge`** — Forest green (#1f3b34) fill, same geometry. Signals new arrivals. The two badges should not appear simultaneously on a single card.

### Hero
**`hero-banner`** — Full-bleed editorial photography with a 25% dark overlay (rgba(39,45,69,0.25)) for legibility. Title in Lora display-xl at 48px, left-aligned, white. Subtitle in Avenir Next body-md, white, below. Primary teal CTA button follows immediately. Minimum 560px height; on mobile the title downgrades to display-md (32px) and contentPadding collapses to {spacing.xl}.

### Collection & Editorial
**`collection-tile`** — 4:3 image tiles, no card background, no shadow. A label-uppercase caption sits below each tile; hover shifts the caption from ink to teal primary (#0e7a82). Used on the homepage and category landing pages to surface sub-collections.

**`editorial-band`** — Full-width forest green (#1f3b34) band with white Lora display-sm heading, Avenir Next body copy, and an aqua-bright (#00caaa) rule beneath the heading as an accent underline. Used for brand story, sustainability callouts, and designer-feature modules.

### Filters & Breadcrumbs
**`filter-bar`** — Sticky bar below sub-nav on collection pages, 48px tall, hairline bottom border. Avenir Next body-sm labels; active filter gets a 2px teal primary underline and the text shifts to primary color. On mobile converts to a slide-up drawer with a teal primary "Done" button.

**`breadcrumb`** — Caption-size Avenir Next, muted (#676986) for parent nodes, body (#414141) for the current page. Hairline-colored slash separator.

### Inputs & Search
**`text-input`** — Zero radius, 1px hairline border at rest, 1px teal primary border on focus. 44px tall, used in checkout, newsletter signup, and account forms.

**`search-bar`** — Surface-soft (#f7f7f8) fill, no radius, hairline border, muted icon at right. Expands to full-width overlay on mobile. Icon hides when the field receives input.

### Size & Variant Selectors
**`size-selector`** — Flat rectangular chips, zero radius. 1px hairline at rest; selected state switches to 1.5px ink border with no fill change. Used on the rug PDP for size variants (2×3, 5×8, 8×10, 9×12, etc.).

### Footer
**`footer`** — Dark ink (#272d45) background, white text, muted-soft (#9a9db1) links that lighten to white on hover. Four-column grid at desktop; accordion at mobile with +/− toggles on each section heading. Column headings in label-uppercase Avenir Next Demi; link lists in body-sm Avenir Next.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hero title at display-md (32px), hero contentPadding collapses to {spacing.xl}, nav collapses to hamburger + logo + cart icon trio, filter-bar converts to a slide-up bottom-sheet drawer |
| Tablet | 744–1128px | Two-column product grid, hero at display-md, nav shows top-level categories (no mega-menu), filter-bar stays sticky horizontal, editorial-band stacks image above text |
| Desktop | 1128–1440px | Three-column product grid, full nav with hover mega-menu dropdown, hero at display-xl (48px), editorial-band shows side-by-side image+text layout |
| Wide | > 1440px | Container max-width 1440px centered, four-column product grid on search and sale pages, hero crops to wider aspect ratio without increasing font size further |

### Touch Targets
- All buttons minimum 44×44px
- Color swatches render at 20px visually but carry a 32px invisible tap target
- Filter chips minimum 40px tall on mobile
- Nav hamburger and icon buttons minimum 44×44px tap area
- Size selector chips minimum 40px tall on mobile

### Collapsing Strategy
- Mega-nav collapses to a full-screen slide-in drawer on tablet and below; top-level categories shown as flat accordion list with disclosure toggles
- Filter sidebar (desktop) becomes a bottom-sheet drawer on mobile, with a teal primary "Done" CTA pinned at the bottom of the sheet
- Footer four-column layout collapses to accordion sections at tablet and below; section headers show +/− toggle in muted color
- Promo-banner single-line on desktop; wraps gracefully on mobile, never truncates with ellipsis — full message always visible

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No design token file or CSS custom properties were accessible; all hex values extracted from rendered page styles and may include third-party widget colors (OKE review widget, chat badge) not belonging to the Dash & Albert brand system
- Button border-radius inferred as 0px from the overall visual register of the extracted palette and brand context; actual computed value should be confirmed in browser DevTools on a live button element
- Exact nav height (64px) and promo-banner height (36px) are estimates from typical Shopify theme patterns; live measurement not confirmed
- Lora's role as the editorial/display serif is inferred from its presence alongside Avenir Next and its classification; no published type specimen or style guide was found to confirm heading-level assignments
- Animation durations (hover transitions, drawer open, image fade, swatch swap) could not be extracted from static analysis
- Colors #df9200 (amber), #00a13a (green), #1d80df (blue), #40b45c (mid-green) appear in the extracted palette but their usage context is unconfirmed — likely third-party UI elements (payment provider badges, trust seals, review stars) rather than Dash & Albert brand tokens
- Dark mode: not observed in extraction; assumed absent
- Icon system: no first-party icon font identified; `oke-widget-icons` belongs to the OKE review platform, not the brand
