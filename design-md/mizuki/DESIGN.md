---
version: alpha
name: "Mizuki"
source_url: "https://www.mizuki.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Pearl and gold meet in a grammar of restraint — every editorial decision on mizuki.com serves the luminosity of the stone rather than the brand identity itself. The founder's Japanese heritage inflects the aesthetic as negative space and proportion rather than motif: long vertical product silhouettes, sparse copy set at generous line-height, and a canvas that shifts from pure white to a faintly warm ivory (#F8F6F2) to keep the pearls from floating against a clinical background. Primary calls-to-action are rendered in near-black (#1C1A17) rather than a conventional jewel color, because the jewelry itself supplies all the color the page needs. Gold appears as a material signal rather than a brand accent — thin 1px hairlines, delicate icon strokes at 1.5px weight, and price figures rendered in a warm #B89660 that references the 14k and 18k alloys in the product catalog. The jade category introduces a muted sage (#5B7A6E) as a secondary orientation token, distinct from the pearl palette but equally desaturated so neither line dominates the other. Type runs in a high-contrast serif at display sizes — Cormorant Garamond or equivalent optical-size serif — shifting to a narrow geometric sans (Helvetica Neue or system fallback) for utility text at caption and badge scale. Rounded values stay minimal: cards use a near-square `{rounded.xs}` 4px corner, buttons sit at `{rounded.none}` to `{rounded.xs}` — softness is reserved for search pills and filter chips at `{rounded.full}`. Spacing is spacious by DTC standards: section gaps at 96–120px on desktop push each product cluster into its own breathing zone. The overall visual register is that of a museum vitrine — controlled illumination, nothing extraneous, every object presented as if behind glass.

colors:
  primary: "#1C1A17"
  primary-active: "#2E2A22"
  primary-disabled: "#A09D98"
  ink: "#1C1A17"
  body: "#3D3A35"
  muted: "#7A7773"
  hairline: "#E2DED9"
  hairline-soft: "#EDE9E4"
  canvas: "#FFFFFF"
  surface-soft: "#F8F6F2"
  surface-card: "#F4F1ED"
  surface-warm: "#EDE8E0"
  on-primary: "#FFFFFF"
  pearl: "#F0ECE5"
  gold-accent: "#B89660"
  gold-light: "#D4B97E"
  jade: "#5B7A6E"
  jade-light: "#8EA99F"
  jade-muted: "#CDD8D4"
  error: "#C0392B"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.1px
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  price-display:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.06em
  logo-display:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.18em
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
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
  section-lg: 96px
  section-xl: 120px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 44px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
  button-text-link:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "none"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderBottom: "1px solid {colors.primary}"
    padding: 10px 0px
    placeholderColor: "{colors.muted}"
  text-input-focus:
    borderBottom: "1px solid {colors.ink}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoTypography: "{typography.logo-display}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: none
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageBackground: "{colors.surface-soft}"
    imagePadding: "20px"
    gap: "{spacing.md}"
  product-card-name:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.gold-accent}"
  product-card-hover:
    imageTransform: scale(1.03)
    transition: transform 0.4s ease
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    sublineColor: "{colors.muted}"
    layout: split-50-50
    padding: "{spacing.section-xl} 0"
  hero-full-bleed:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    overlayColor: "rgba(28,26,23,0.18)"
    textPosition: bottom-left
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    descriptionColor: "{colors.muted}"
    paddingBottom: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  material-badge:
    backgroundColor: "{colors.pearl}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  material-badge-jade:
    backgroundColor: "{colors.jade-muted}"
    textColor: "{colors.jade}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  material-badge-gold:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.gold-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 10px"
  product-detail-title:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.sm}"
  product-detail-price:
    typography: "{typography.display-sm}"
    textColor: "{colors.gold-accent}"
    fontWeight: 300
  product-detail-description:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    lineHeight: 1.7
  product-detail-meta:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    letterSpacing: 0.04em
  swatch-selector:
    size: 20px
    borderRadius: "{rounded.full}"
    activeBorder: "2px solid {colors.primary}"
    inactiveBorder: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "8px 16px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    border: "none"
    placeholderColor: "{colors.muted}"
  editorial-callout:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    padding: "{spacing.xxl}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.hairline-soft}"
    padding: "{spacing.section} 0"
    logoTypography: "{typography.logo-display}"
  announcement-bar:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    padding: "10px {spacing.base}"
    textAlign: center

## Components

### Buttons
**`button-primary`** — A near-black (#1C1A17) rectangle with zero border radius, all-caps letter-spaced label at 12px. Hover darkens slightly to `{colors.primary-active}`; disabled state uses `{colors.primary-disabled}` ash. The square corner is intentional — no softening — keeping the CTA reading as a formal instruction rather than an invitation.

**`button-secondary`** — Identical geometry to primary, but inverted: white fill, 1px `{colors.primary}` border, same uppercase label. Used for "Add to Wishlist" and secondary drawer actions. On hover the border thickens optically via box-shadow rather than border-width to avoid layout shift.

**`button-ghost`** — Hairline-bordered, transparent background, used for filter menus and "View All" category links. Sits lower in hierarchy than secondary but higher than text-links.

**`filter-pill`** and **`filter-pill-active`** — The only `{rounded.full}` shape in the button system, appearing in collection filter bars. Inactive state is white with a hairline border; active flips to solid `{colors.primary}`. Groups of pills wrap on mobile.

### Inputs
**`text-input`** — Underline-only text field (bottom border only, no surrounding box), evoking a written inscription rather than a web form. Focus state transitions the bottom border from `{colors.hairline}` to `{colors.primary}`. No border-radius anywhere. Placeholder in `{colors.muted}`.

**`search-bar`** — A departure from the underline grammar: the search field uses `{rounded.full}` pill shape on a `{colors.surface-soft}` fill, floating above nav or within a search overlay. This is the one place warmth breaks the austere grid.

### Navigation
**`nav-bar`** — 64px tall, white canvas, 1px soft hairline bottom border. Logo centered in `{typography.logo-display}` — widely spaced uppercase serif. Left cluster: category links in `{typography.nav-link}` (12px, tracked). Right cluster: search icon, account, bag with item count dot in `{colors.gold-accent}`. On scroll the bar remains white; no transparency or blur effect.

**`announcement-bar`** — Sits above the nav in `{colors.surface-warm}`, 10px top/bottom padding. Used for free-shipping thresholds and new collection notices in `{typography.caption}` centered. Dismissible via a right-aligned × at 12px.

### Product Cards
**`product-card`** — No border, no shadow, no radius. Image sits on a `{colors.surface-soft}` block with 20px inner padding so the jewelry floats rather than bleeds to card edges. Name below in `{typography.body-sm}` body color; price in `{typography.price-display}` gold `{colors.gold-accent}`. Hover lifts the image with a subtle scale(1.03) transform over 0.4s ease — the only animation on the card.

**`material-badge`**, **`material-badge-jade`**, **`material-badge-gold`** — Small pill badges overlaid on product cards or used inline in PDPs to identify stone type: pearl (ivory `{colors.pearl}` fill), jade (muted sage `{colors.jade-muted}` fill with `{colors.jade}` text), or gold karat (`{colors.surface-warm}` fill with `{colors.gold-accent}` text). All use `{typography.badge}` at 10px tracked uppercase.

### Product Detail Page
**`product-detail-title`** — 22px serif at fontWeight 400 in `{typography.display-sm}`, creating a refined editorial register. Price immediately follows in the same size but `{colors.gold-accent}` and fontWeight 300 — lighter than the name, so metal reads as secondary information. Material meta (karat, origin, pearl type) in `{typography.product-detail-meta}` muted caption below price.

**`swatch-selector`** — 20px circular swatches at `{rounded.full}` with a 2px `{colors.primary}` ring on active state. Gap of `{spacing.sm}` between swatches. Used for metal color selection (yellow, white, rose gold).

**`size-selector`** — Flat rectangular selectors for chain length or ring size, square corners, hairline border inactive, solid `{colors.primary}` fill active. Mirrors the button grammar.

### Structural Sections
**`hero-editorial`** — 50/50 split layout: editorial image left, headline and CTA right, on a `{colors.surface-soft}` background. Headline in `{typography.display-xl}` at 300 weight — intentionally light. Section padding `{spacing.section-xl}` 120px top and bottom on desktop.

**`hero-full-bleed`** — Full-width campaign image with a 18% dark scrim and text anchored bottom-left. Headline in `{typography.display-lg}`. Used for seasonal campaigns.

**`collection-header`** — Collection title in `{typography.display-md}` above a 1px hairline separator, description text in `{colors.muted}` below. Minimal, functions as a chapter header.

**`editorial-callout`** — A content tile on `{colors.surface-card}` with generous `{spacing.xxl}` padding, used between product grid rows to break rhythm with brand storytelling. No border or shadow.

**`footer`** — Dark inverted footer on `{colors.primary}` near-black. Four-column link grid at desktop, stacked accordion at mobile. Logo in `{typography.logo-display}` ivory. Newsletter input inline with a ghost submit button. Social icons at 20px stroke weight.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + centered logo + icon row; hero becomes stacked (image top, text below); `{spacing.section-xl}` reduces to `{spacing.section}`; announcement bar stays visible |
| Tablet | 744–1128px | Two-column product grid; hero stays split but at 40/60 proportion; nav shows logo + 2 primary links + icon row; filter pills scroll horizontally |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav; 50/50 hero with generous vertical padding; editorial callouts appear between grid rows |
| Wide | > 1440px | Max-width container at 1440px centered; four-column grid; hero image bleeds to viewport edges while text column stays within grid |

### Touch Targets
- All tappable elements minimum 44×44px on mobile
- Swatch selectors expand hit area to 44px with transparent padding overlay
- Filter pills have minimum 36px height on mobile; scroll in a horizontal track
- Nav icons (search, account, bag) spaced minimum 44px apart

### Collapsing Strategy
- Navigation: hamburger drawer reveals full nav tree with category sections
- Footer link columns collapse to labeled accordions on mobile
- Swatch row wraps; size selector row wraps into a 3-column grid
- Product detail image gallery switches from side-scroll filmstrip to full-width swipeable carousel
- Editorial callout drops out of the product grid on mobile (full-width block, reduced padding)

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors were extracted from the live site — the palette above is inferred from Mizuki's brand positioning as a fine pearl and jade jewelry house; all color values should be verified against the live site or brand assets before production use
- No font families were extracted — typography recommendations (Cormorant Garamond for display, Helvetica Neue for utility) are inferred from fine jewelry brand conventions and should be confirmed against actual font loading on mizuki.com
- No theme-color meta tag was present, preventing detection of the true primary brand accent
- Platform is not confirmed as Shopify — component assumptions around cart drawer, collection filtering, and PDP structure may not match the actual storefront architecture
- Jade category color treatment is speculative; if Mizuki does not actively distinguish pearl vs. jade lines with separate palette tokens, the `{colors.jade}` family can be collapsed
- Animation timings (hover scale on product cards) are inferred convention, not extracted values
- Specific pearl types (Akoya, Freshwater, South Sea, Tahitian) may each have distinct badge or callout treatments not captured here
