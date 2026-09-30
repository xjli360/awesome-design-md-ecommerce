---
version: alpha
name: "King & McGaw"
source_url: "https://www.kingandmcgaw.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Portrait Light Web — a custom display serif licensed exclusively for this brand — sets King & McGaw apart from every mass-market poster retailer the moment the page loads. The typeface carries the weight of a gallery catalogue rather than a shop: letterforms are narrow and light, sized generously at display scale (~48px) but restrained in weight (Light/300), creating the impression of frame labels rather than headlines selling product. The canvas leans warm: off-white tones (#eae9e7, #f5f5f3) stop short of pure clinical white (#ffffff is reserved for card surfaces), so art photographs the way it looks on linen mounting board. Where a single accent color would suffice for most retailers, King & McGaw operates a seven-color category taxonomy — warm apricot (#fdc79e), sage green (#70a345), muted brick (#b64646), dusty slate (#708b9e), soft mint (#addbb3), pale gold (#e2bf24), and tan (#c7b097) — each mapped to an art genre or movement. Tags reading "Photography", "Abstract", "Mid-Century" each carry their own swatch, turning the navigation into a chromatic index of art history.

  The most singular brand color is the apricot (#fdc79e), used as the primary action accent — warm enough to signal curation without the urgency of a sale badge. Borders and dividers use a warm gray (#d8cdc3) rather than a neutral, preserving the linen-room warmth throughout. Buttons are flat-edged ({rounded.none}) in the tradition of print catalogues, which never needed to soften their corners. Search and input fields follow the same discipline: thin borders, warm background (#f5f5f3), no pill softening. The overall spatial grammar is generous — section spacing runs to 64px or more, echoing the white space a gallery uses to isolate a framed print on a wall. Typography hierarchy uses Portrait Light Web for emotional register (hero statements, artist names, feature titles) and system sans-serif for informational density (prices, sizes, edition counts, navigation links), a split that maps exactly onto how a gallery might separate editorial copy from wall labels.

colors:
  primary: "#fdc79e"
  primary-active: "#f0a870"
  primary-disabled: "#f8dfc9"
  accent-red: "#dc3300"
  ink: "#1a1a1a"
  body: "#222222"
  muted: "#474746"
  muted-soft: "#afafaf"
  hairline: "#d8cdc3"
  hairline-soft: "#eae9e7"
  canvas: "#ffffff"
  surface-warm: "#eae9e7"
  surface-soft: "#f5f5f3"
  surface-card: "#f0eee9"
  on-primary: "#1a1a1a"
  on-dark: "#ffffff"
  tag-apricot: "#fdc79e"
  tag-sage: "#70a345"
  tag-brick: "#b64646"
  tag-slate: "#708b9e"
  tag-mint: "#addbb3"
  tag-gold: "#e2bf24"
  tag-wheat: "#c7b097"

typography:
  display-xl:
    fontFamily: "'Portrait Light Web', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Portrait Light Web', Georgia, serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Portrait Light Web', Georgia, serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Portrait Light Web', Georgia, serif"
    fontSize: 20px
    fontWeight: 300
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  artist-credit:
    fontFamily: "'Portrait Light Web', Georgia, serif"
    fontSize: 12px
    fontWeight: 300
    lineHeight: 1.4
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  category-tag:
    fontFamily: "-apple-system, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase

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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted-soft}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "1px solid {colors.ink}"
    outline: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-logo:
    fontFamily: "'Portrait Light Web', Georgia, serif"
    fontSize: 18px
    fontWeight: 300
    letterSpacing: 2px
    textTransform: uppercase
    textColor: "{colors.ink}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/4"
    padding: 0
    gap: "{spacing.sm}"
    border: none
    boxShadow: none
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
    fontWeight: 500
  product-card-artist:
    typography: "{typography.artist-credit}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  hero:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.section}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    maxWidth: 680px
  hero-sub:
    typography: "{typography.display-sm}"
    textColor: "{colors.muted}"
  category-tag-apricot:
    typography: "{typography.category-tag}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    backgroundColor: "{colors.tag-apricot}"
    textColor: "{colors.ink}"
  category-tag-sage:
    typography: "{typography.category-tag}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    backgroundColor: "{colors.tag-sage}"
    textColor: "{colors.on-dark}"
  category-tag-brick:
    typography: "{typography.category-tag}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    backgroundColor: "{colors.tag-brick}"
    textColor: "{colors.on-dark}"
  category-tag-slate:
    typography: "{typography.category-tag}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    backgroundColor: "{colors.tag-slate}"
    textColor: "{colors.on-dark}"
  category-tag-mint:
    typography: "{typography.category-tag}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    backgroundColor: "{colors.tag-mint}"
    textColor: "{colors.ink}"
  category-tag-gold:
    typography: "{typography.category-tag}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    backgroundColor: "{colors.tag-gold}"
    textColor: "{colors.ink}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  search-bar-submit:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    width: 48px
    height: 48px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted-soft}"
    separator: "/"
    gap: "{spacing.xs}"
  artist-page-header:
    backgroundColor: "{colors.surface-warm}"
    padding: "{spacing.xxl} 0"
  artist-name-display:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
  edition-badge:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 10px
    border: "1px solid {colors.hairline}"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  price-was:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: line-through
  price-now:
    typography: "{typography.price-display}"
    textColor: "{colors.accent-red}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xl}"
  footer-link:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted-soft}"
    textDecoration: none
  footer-link-hover:
    textColor: "{colors.canvas}"
    textDecoration: underline
  footer-newsletter-input:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.muted}"
    padding: 12px 16px
    height: 44px

## Components

### Buttons

**`button-primary`** — Flat-edged (`{rounded.none}`) apricot (#fdc79e) blocks standing 48px tall with uppercase, letter-spaced sans-serif labels at 13px/500 weight. The zero-radius corners are an intentional editorial choice — they echo the rectilinear geometry of a framed print rather than a consumer app button. On hover the fill deepens to `{colors.primary-active}` (#f0a870); disabled state washes to `{colors.primary-disabled}` with muted-soft text.

**`button-secondary`** — Identical flat geometry, canvas background with a 1px solid ink border. Used for secondary CTAs such as "Add to wishlist" or "Browse full collection." On hover, background shifts to `{colors.surface-soft}` for a perceptible state change without abandoning the restrained palette.

**`button-ghost`** — Transparent, ink text, no border, underline decoration. Used inline for tertiary actions: "Learn more about framing", "See artist biography", "Read our story." Never competes with the apricot primary.

### Navigation

**`nav-bar`** — 64px white bar separated from the page by a single 1px warm-gray hairline (`{colors.hairline-soft}`). The wordmark uses Portrait Light Web at ~18px, uppercase, widely tracked (2px letter-spacing), functioning as a logotype rather than a marketing headline. Right-side cluster: search icon, wishlist, and cart — all at 44px tap zones. No pill or rounded element appears anywhere in the navigation system.

**`search-bar`** — Flat-edged, warm surface background, 1px hairline border that sharpens to full ink on focus (no glow, no color shift, purely weight). The submit element is a solid ink square (48×48px) with an icon in white, completing the rectangle of the input — the two elements read as one rectilinear form.

### Product Grid

**`product-card`** — No border, no shadow, no radius. Portrait-oriented image at 3:4 aspect ratio fills the card top. Below, in tight vertical sequence: print title in `{typography.body-sm}` at weight 500, artist name in `{typography.artist-credit}` (12px, uppercase, tracked, Portrait Light Web Light, muted), then price in `{typography.price-display}`. Edition format label may appear as a muted caption beneath the price. On hover, the image area may receive a very light overlay with a centered CTA.

**`edition-badge`** — Small flat rectangles with 1px warm hairline borders and caption-weight muted text. Reads "Limited Edition", "Open Edition", or "Artist Proof" in restrained small caps. Sits on the product card image corner or below the title line.

**`sale-badge`** — The single maximum-intensity element on any page: a flat red (#dc3300) rectangle pinned to the image corner. Uppercase 11px label. The contrast between this red and the warm-apricot palette is deliberate — it reads immediately as a pricing departure, not a brand color.

### Category Taxonomy

**`category-tag-*`** — Seven distinct flat swatches, each assigned to an art genre or movement. Apricot for one classification, sage green (`{colors.tag-sage}`) for another, muted brick, dusty slate, soft mint, pale gold, and tan distribute across the taxonomy. All share identical geometry: zero radius, 4px 8px padding, uppercase 10px/600 labels. The system turns the filter rail into a colour-coded legend — a reader can navigate by hue without reading a label.

### Hero

**`hero`** — Full-width warm canvas section (`{colors.surface-warm}`) with 64px vertical padding. Headline in `{typography.display-xl}` at Portrait Light Web Light, left-aligned, max-width 680px. Sub-headline in `{typography.display-sm}` in muted ink below. Primary CTA button sits 24px below the sub-headline. Alternatively rendered as a full-bleed photograph with overlaid text in `{colors.on-dark}` and an apricot CTA button.

### Artist Pages

**`artist-page-header`** — Warm surface band above the product grid. Artist name in `{typography.display-md}` (Portrait Light Web, 36px, Light). Optional short biography paragraph in `{typography.body-md}`. A hairline rule (`{colors.hairline}`) separates the header from the grid below — no decorative imagery, purely typographic.

### Footer

**`footer`** — Full ink-black (#1a1a1a) strip. Multi-column link grid in `{typography.body-sm}`; links render at `{colors.muted-soft}` and transition to white on hover. Newsletter sign-up uses `{components.footer-newsletter-input}`: transparent field with a muted-gray border, ink background, white text — the flat geometry is preserved even in the inverted context. No radius anywhere in the footer.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + cart icons; hero headline drops to `{typography.display-md}`; section padding halves to 32px |
| Tablet | 744–1128px | Two-column product grid; nav may retain top-level categories visible inline; hero may split to 50/50 image-text layout |
| Desktop | 1128–1440px | Three or four-column product grid; full nav with dropdown mega-menus; hero at full `{typography.display-xl}` with 680px max-width text column |
| Wide | > 1440px | Four to five-column grid; max-width container (~1400px) centred; hero photography extends edge-to-edge behind a constrained text column |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch target at mobile breakpoints
- Nav icon buttons (search, wishlist, cart) use 44×44px tap zones regardless of visual icon size
- Category tag swatches expand their vertical padding on mobile to meet the 44px minimum
- The `{components.nav-bar}` height increases to 56px on mobile to give the wordmark and icons breathing room

### Collapsing Strategy
- Desktop mega-menu collapses to a full-screen drawer on mobile with accordion-style category expansion per genre group
- Product filters (medium, price range, artist, edition type) move to a bottom sheet on mobile and an off-canvas slide-in panel on tablet
- The seven-color category tag rail wraps to two rows on tablet and becomes a horizontally scrollable strip on mobile
- Footer multi-column layout stacks vertically on mobile; each link group collapses into an accordion with a thin hairline divider
- Hero switches from text-left / image-right to stacked image-above / text-below on mobile, with image capped at 56vh

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Portrait Light Web weight variants beyond Light (300) could not be confirmed — the brand may use a Regular (400) weight for body-level serif instances such as pull quotes or editorial captions
- The exact token used for primary CTA buttons is inferred from #fdc79e as the most distinctive extracted color; the live site may route primary actions through a different color in certain flows (e.g. framing configurator)
- Hover states, focus rings, and transition durations are not extractable from static analysis — all are assumed from color proximity and convention
- The #474xxx hex cluster (e.g. #474746, #474718, #474654) appears to be a color-picker artifact or internal tool state rather than intentional brand tokens; excluded from the palette
- Navigation mega-menu column count and dropdown hover behavior not observable — inferred from genre taxonomy implied by the tag color set
- Whether #dc3300 functions purely as a sale/promotion accent or also appears in primary CTA contexts for certain campaign pages could not be determined
- Animation and micro-interaction specs (image zoom on hover, cart drawer slide, filter panel transitions) are entirely absent from static extraction
