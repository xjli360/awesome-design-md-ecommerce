---
version: alpha
name: "Rock Archive"
source_url: "https://www.rockarchive.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Two high-voltage brand colors — coral-red #ea4b46 and forest green #116633 — collide against the silver-gelatin grain of decades-old concert photography, giving Rock Archive the electric charge of a vintage gig poster rather than the hushed reverence of a fine-art gallery. The meta theme-color is unambiguously #ea4b46: it fires on every primary CTA, edition badge, and hover accent, while #116633 anchors secondary interactions and category markers. Without a custom font stack detected on the live site, the system leans on a serif-first editorial hierarchy — Georgia or a comparable old-style serif for display headings evokes press-pass credentials and vinyl liner notes, while a neutral geometric sans carries body copy and UI labels. The product experience centers on limited-edition print listings: each card surfaces photographer credit, artist name, edition size, and a certificate-of-authenticity signal, treating every frame as a collectible artifact rather than décor. Print sizes and framing options live in a structured selector rather than a dropdown, reinforcing the tactile gravity of choosing a physical object. The canvas is white with a warm off-white surface tint, keeping photography central and preventing brand chrome from competing with the image. Rounded values stay restrained — cards and inputs use small radii ({rounded.sm}) while badges and edition pills push to {rounded.xs}, echoing the straight-edged geometry of a framed print. The footer doubles as a curatorial statement, listing represented photographers alongside newsletter sign-up, treating archives as editorial content rather than sitemap boilerplate.

colors:
  primary: "#ea4b46"
  primary-active: "#c93832"
  primary-disabled: "#f4a9a7"
  accent-green: "#116633"
  accent-green-active: "#0d4f27"
  accent-green-muted: "#d6e9de"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#dedede"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f7f5f2"
  surface-card: "#ffffff"
  surface-dark: "#111111"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent-green: "#ffffff"
  edition-gold: "#b8952a"
  star-rating: "#ea4b46"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.1px
  title-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  body-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-bold:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.3px
  photographer-credit:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
    fontStyle: italic
  edition-label:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
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
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.sm}"
  button-green:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-accent-green}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.ink}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    activeLinkColor: "{colors.primary}"
    hoverLinkColor: "{colors.primary}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    activeLinkColor: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    padding: 10px 14px
    height: 44px
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageRatio: "3 / 4"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    sublineTypography: "{typography.photographer-credit}"
    sublineColor: "{colors.muted}"
    priceTypography: "{typography.body-md}"
    priceColor: "{colors.ink}"
    editionTypography: "{typography.edition-label}"
    editionColor: "{colors.muted}"
    hoverImageScale: 1.03
    hoverTitleColor: "{colors.primary}"
  edition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.edition-label}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 4px 8px
  sold-out-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.edition-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.edition-label}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-fullbleed:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    minHeight: 90vh
    overlayColor: "rgba(0,0,0,0.35)"
    ctaComponent: "button-primary"
    textAlignment: center
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    sublineTypography: "{typography.photographer-credit}"
    layout: "two-column image-left"
    imageRatio: "4 / 5"
  print-size-selector:
    backgroundColor: "{colors.canvas}"
    selectedBorder: "2px solid {colors.ink}"
    unselectedBorder: "1px solid {colors.hairline}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    hoverBorder: "1.5px solid {colors.muted}"
  certificate-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    iconColor: "{colors.accent-green}"
    borderTop: "1px solid {colors.hairline}"
    padding: 12px 0
  photographer-bio:
    backgroundColor: "{colors.canvas}"
    nameTypography: "{typography.display-sm}"
    nameColor: "{colors.ink}"
    creditTypography: "{typography.photographer-credit}"
    creditColor: "{colors.muted}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.section} 0"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-bold}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    activeBackgroundColor: "{colors.ink}"
    activeTextColor: "{colors.on-dark}"
  price-block:
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.primary}"
    originalPriceColor: "{colors.muted}"
    vatNoteTypography: "{typography.caption}"
    vatNoteColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-soft}"
    linkHoverColor: "{colors.on-dark}"
    headingTypography: "{typography.edition-label}"
    linkTypography: "{typography.body-sm}"
    borderTop: "4px solid {colors.primary}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Coral-red (#ea4b46) fill with all-caps tracked label at `{typography.button-md}`; height 48px, `{rounded.sm}` radius. Active state deepens to `{colors.primary-active}` (#c93832); disabled fades to `{colors.primary-disabled}`. Used for "Add to Basket", "Buy Now", and any checkout progression.

**`button-secondary`** — White fill with a 1px ink border and the same uppercase label. Communicates equal visual weight to primary but for secondary flows: saving to wishlist, viewing more editions, sharing. Active state shifts background to `{colors.surface-soft}`.

**`button-green`** — Forest green (#116633) fill, white label — reserved for curatorial or collection-level actions ("View Collection", "See All Prints by Artist") where the coral-red would compete with the imagery. Shares geometry with `button-primary`.

**`button-ghost`** — Transparent, underlined ink text at `{typography.button-sm}`. Used inline in product descriptions, footnotes, and photographer bio links. No border or radius — reads as inline editorial rather than UI chrome.

### Text Input & Search

**`text-input`** — White canvas, 1px `{colors.hairline}` border, `{rounded.xs}` corners. Focus ring tightens to 1.5px ink border with no glow — clean and press-pass direct. `{typography.body-md}` at 15px for readability against photograph thumbnails.

**`search-bar`** — Slightly warm surface-soft fill (`{colors.surface-soft}`) differentiates it from page canvas. Search icon in `{colors.muted}` sits left of placeholder text. On keystroke, border transitions to ink; on submit, fires against photographer, artist, and print-title index.

### Navigation

**`nav-bar`** — 64px white bar with 1px hairline bottom border. Logo in ink (or reversed white on dark pages). Category links in `{typography.nav-link}` with active/hover color flip to `{colors.primary}`. On photo-heavy hero pages, the bar may render as `nav-bar-dark` — surface-dark background, all-white labels — so brand chrome doesn't interrupt the image bleed.

### Product Card

**`product-card`** — No border radius — straight-edged like a mounted print. Image displays at 3:4 portrait ratio; on hover, scales 1.03× with a 300ms ease. Below the image: artist/subject name in `{typography.title-md}`, photographer credit in italic `{typography.photographer-credit}` (muted), and price in `{typography.body-md}`. Edition status renders as `edition-badge` (e.g., "Edition of 50") or `sold-out-badge` overlaid bottom-left of the image. Hover triggers title color shift to `{colors.primary}`.

### Edition & Status Badges

**`edition-badge`** — Warm surface-soft fill, ink text, all-caps tracked label at `{typography.edition-label}`, 1px hairline border, `{rounded.xs}`. Communicates collectible scarcity without drama.

**`sold-out-badge`** — Ink fill, white label — the visual weight signals finality. Placed as an image overlay to preserve card layout.

**`new-badge`** — Coral-red fill, white label — same geometry as edition badge. Reserved for recently added prints or new-release artist editions.

### Hero

**`hero-fullbleed`** — Full-viewport photograph with a 35% black overlay scrim. Headline in `{typography.display-xl}` Georgia serif, white, centered. Subline in `{typography.body-md}`, white, at reduced opacity. A single `button-primary` CTA sits below. This is the brand's loudest statement — concert photography at scale, not a lifestyle composite.

**`hero-editorial`** — Two-column white canvas: 4:5 portrait image left, editorial text right. Headline in `{typography.display-lg}`, attribution in `{typography.photographer-credit}` italic muted. Used for featured photographer spotlights and curated collections.

### Print Detail Panel

**`print-size-selector`** — A set of outlined tiles (xs radius) for each available size (e.g., A3, A2, 24×16"). Selected tile gets a 2px ink border; hover gets 1.5px muted border. Typography at `{typography.body-sm}`. Mirrors the considered physicality of choosing a frame.

**`certificate-strip`** — Soft surface strip with a green checkmark icon (`{colors.accent-green}`) and caption text confirming limited-edition certificate of authenticity. Sits immediately below the add-to-basket button. The green here is functional — it reads as a trust signal rather than decoration.

**`price-block`** — Price in `{typography.price-display}` Georgia serif at 24px. Sale price in `{colors.primary}` coral; original struck-through in `{colors.muted}`. VAT note in `{typography.caption}` muted below.

### Photographer Bio

**`photographer-bio`** — Full-width canvas section with generous `{spacing.section}` padding. Photographer name in `{typography.display-sm}`, italic credit line in `{typography.photographer-credit}`, body copy in `{typography.body-md}`. Treated as editorial longform, not a product sidebar.

### Category Pills

**`category-pill`** — Soft surface fill, hairline border, `{rounded.full}` pill shape — used to filter by genre (Rock, Jazz, Blues, Punk), era, or photographer. Active state flips to ink fill, white text, no border. Sits in a horizontally scrollable row on mobile.

### Footer

**`footer`** — Dark surface (`{colors.surface-dark}`) with a 4px coral-red top border — the brand's single decorative flourish. Section headings in `{typography.edition-label}` all-caps white. Links in `{typography.body-sm}` muted-soft, hovering to white. Photographer roster, newsletter sign-up, and social links all coexist as curatorial content.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero headline drops to `display-md` (28px); category pills scroll horizontally; nav collapses to hamburger + search icon; print-size-selector wraps to two columns |
| Tablet | 744–1128px | Two-column product grid; hero scales to `display-lg` (36px); nav shows primary links, hides secondary; photographer bio switches to stacked layout |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav bar with all category links; hero at `display-xl` (48px); editorial hero goes two-column |
| Wide | > 1440px | Max content width clamped to 1440px, canvas bleeds on sides; hero photography fills viewport width; four-column grid with generous gutter |

### Touch Targets

- All buttons minimum 48px height, full-width on mobile
- Print size selector tiles minimum 44×44px touch area
- Category pills minimum 36px height; horizontal scroll row with momentum
- Nav hamburger icon 48×48px tap target
- Product card tap area covers full image + text block

### Collapsing Strategy

- Primary navigation hides to hamburger below 1128px; search stays visible as icon
- Hero shifts from full-bleed + overlay text to stacked image-above / text-below on mobile
- Photographer bio switches from two-column to single-column stack at tablet
- Edition badges remain image-overlaid at all breakpoints; font size does not change
- Footer collapses from four-column to two-column at tablet, single-column at mobile; photographer roster truncated with "See All" link

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font stack was detected on the live site — the system may load typefaces via JS injection, a CDN with anti-bot protection, or a font manager not visible to static extraction. Georgia serif and Helvetica Neue are used here as plausible brand-aligned defaults; actual fonts should be confirmed by inspecting network requests in a real browser session.
- Only two hex values were extracted (#ea4b46, #116633). The full palette — neutral grays, surface tints, hover states, overlay scrim values — is inferred from category conventions and cannot be verified without deeper CSS inspection.
- No spacing scale, border-radius values, or component-level measurements were extractable. All token values are system defaults informed by photography-print-shop conventions.
- The exact treatment of the logo (wordmark vs. logotype, weight, color) was not extractable; ink color is assumed as default but a white reverse version likely exists for dark hero contexts.
- Edition numbering display format (inline badge vs. sidebar callout vs. product-title suffix) could not be verified without live product page inspection.
- Whether Rock Archive uses a custom e-commerce platform or Shopify was flagged as false, meaning checkout flow and cart components may differ significantly from standard Shopify patterns — these components should be validated directly.
