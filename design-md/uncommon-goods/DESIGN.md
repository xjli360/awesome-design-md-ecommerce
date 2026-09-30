---
version: alpha
name: "Uncommon Goods"
source_url: "https://www.uncommongoods.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The shop declares its personality through an unlikely chromatic adjacency: a national-forest green (#006341) — the shade of a ranger station rather than a commerce CTA — set against warm apricot (#ffa549) that turns every sale badge and promo strip golden. That green, confirmed by the site's own meta theme-color, saturates every primary button, navigation bar, and trust marker, deepening to #003926 under hover. What distinguishes the visual system is its refusal to stop at two or three anchors: Uncommon Goods runs a full gift-taxonomy spectrum across catalog browse — dusty peach (#fee4ca) and vivid tangerine (#eb5721) tag outdoor and garden discoveries, rose (#f391a4) and deep mauve (#d94f6a) mark personal-care items, swimming-pool teal (#2ac4e3) signals kitchen and bar finds, warm honey (#f5bc22) flags art and home décor. Each hue functions as a wayfinding signal as much as a brand color; the palette is a product taxonomy wearing category colors.

  Typography pairs the custom "Escalator" display face with "Tiempos Text," an editorial serif that lends catalog gravity and reading warmth to product descriptions. The proprietary "UncommonGoods" font appears only in wordmark and logotype contexts. Display headings run large with moderate negative letter-spacing, asserting discovery over transactional efficiency. Rounded corners sit at {rounded.xs} for primary CTAs and {rounded.sm} for product cards — warm enough to signal friendliness, not so open they read playful. Only filter chips and category badge pills bloom to {rounded.full}. The canvas is white, with {colors.surface-soft} — the palest mint at #e1efea — providing section-level background differentiation without heavy color weight. Gray #aaaaaa handles secondary labels and metadata; near-black #212121 anchors all body type. Social share buttons adopt platform-native tones (#3b5998, #bd081c, #55acee) unchanged — Uncommon Goods treats sharing as infrastructure rather than a brand extension opportunity.

colors:
  primary: "#006341"
  primary-active: "#003926"
  primary-disabled: "#aad4c2"
  ink: "#212121"
  body: "#3d3d3d"
  muted: "#aaaaaa"
  hairline: "#e6e6e6"
  canvas: "#ffffff"
  surface-soft: "#e1efea"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#ffa549"
  accent-orange-dark: "#e27300"
  accent-orange-vivid: "#eb5721"
  accent-orange-deep: "#b23608"
  accent-peach: "#fee4ca"
  accent-peach-mid: "#eca154"
  accent-pink-soft: "#fccebe"
  accent-pink: "#f391a4"
  accent-rose: "#d94f6a"
  accent-rose-soft: "#f5dbe0"
  accent-teal: "#2ac4e3"
  accent-teal-dark: "#0097b5"
  accent-teal-mid: "#3eb1c8"
  accent-teal-soft: "#ccecf2"
  accent-gold: "#f5bc22"
  accent-gold-dark: "#d69f09"
  accent-gold-soft: "#fbefcc"
  social-facebook: "#3b5998"
  social-pinterest: "#bd081c"
  social-twitter: "#55acee"

typography:
  display-xl:
    fontFamily: "'Escalator', 'UncommonGoods', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Escalator', 'UncommonGoods', serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Escalator', 'UncommonGoods', serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Tiempos Text', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Tiempos Text', Georgia, serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Tiempos Text', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Tiempos Text', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Tiempos Text', Georgia, serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Escalator', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Escalator', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  badge:
    fontFamily: "'Escalator', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  label-sm:
    fontFamily: "'Escalator', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Escalator', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Tiempos Text', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  wordmark:
    fontFamily: "'UncommonGoods', serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.0
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 26px
    height: 48px
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.xs}"
    typography: "{typography.body-md}"
    padding: 12px 16px
    height: 48px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.primary}"
    borderWidth: 2px
    rounded: "{rounded.sm}"
    typography: "{typography.body-md}"
    padding: 12px 48px 12px 16px
    height: 48px
    iconColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.primary}"
  nav-bar-promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderRadius: "{rounded.sm}"
    imageBorderRadius: "{rounded.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.md}"
    shadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-badge-garden:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-badge-personal:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-badge-kitchen:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  category-badge-art:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    headlineColor: "{colors.ink}"
    ctaComponent: "button-primary"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  section-heading:
    typography: "{typography.display-sm}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  gift-finder-card:
    backgroundColor: "{colors.surface-soft}"
    borderRadius: "{rounded.md}"
    labelTypography: "{typography.label-sm}"
    labelColor: "{colors.primary}"
    titleTypography: "{typography.title-md}"
    padding: "{spacing.lg}"
  price-tag:
    typography: "{typography.price-display}"
    color: "{colors.ink}"
  price-tag-sale:
    typography: "{typography.price-display}"
    color: "{colors.accent-orange-vivid}"
  price-tag-original:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    textDecoration: line-through
  social-share-facebook:
    backgroundColor: "{colors.social-facebook}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 18px
  social-share-pinterest:
    backgroundColor: "{colors.social-pinterest}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 18px
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.accent-teal-soft}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Forest green (#006341) fill on a 4px-radius rectangle, 48px tall, with white label in Escalator 600 at 16px and 0.5px tracking. Hover deepens to `{colors.primary-active}` (#003926) without transition animation — a deliberate, no-fuss state change. Disabled state uses `{colors.primary-disabled}` (a pale mint) and keeps white text, rendering the button present but clearly inert. Used for primary checkout, add-to-cart, and gift-registry CTAs.

**`button-secondary`** — White canvas with a 2px green border and green label, matching the primary's geometry (48px, `{rounded.xs}`). Signals a peer-level choice — "save for later" alongside "add to cart" — without visual competition. Border color shifts to `{colors.primary-active}` on hover.

**`button-text`** — Transparent background, green label in `{typography.button-md}` with underline. Used for inline navigation cues, "see all" links, and editorial "learn more" hooks in editorial sections.

**`filter-chip` / `filter-chip-active`** — Pill-shaped (`{rounded.full}`) at 36px height. Resting state sits on `{colors.surface-soft}` (pale mint); activated state inverts to `{colors.primary}` fill with white text. A row of these chips handles category filtering, price-range selection, and "for whom" gift narrowing.

### Navigation

**`nav-bar`** — White background at 64px height, borderline `{colors.hairline}` below. Logo renders in the custom "UncommonGoods" face; nav links use Escalator 500 at 15px. A persistent `{nav-bar-promo-strip}` in forest green sits above the bar, 36px tall, carrying promotional copy in `{typography.label-sm}` white uppercase — free shipping thresholds, seasonal messaging, gift deadlines.

### Search

**`search-bar`** — White field with a 2px `{colors.primary}` border and a green magnifier icon. The heavier border signals primary utility without a filled background, distinguishing it from standard text inputs. Rounded at `{rounded.sm}`, 48px tall, icon-padded right for a clear affordance.

### Product Cards

**`product-card`** — White card, `{rounded.sm}` corners, subtle 8px-diffuse shadow. Product image fills the top portion with matching `{rounded.sm}` clipping. Below: title in Tiempos Text 600 at 16px, price in `{typography.price-display}`, optional maker credit in `{typography.caption}`. A `{product-card-badge}` pill overlaps the image corner for "New," "Bestseller," or sale flags in the category's accent color.

**`category-badge-*`** — Four badge variants keyed to gift taxonomy. Garden/outdoor items carry `{colors.accent-orange}` (#ffa549). Personal care and self-gift items use `{colors.accent-rose}` (#d94f6a). Kitchen finds run `{colors.accent-teal}` (#2ac4e3). Art and home décor badges sit in `{colors.accent-gold}` (#f5bc22) with dark ink text for legibility against the lighter fill. All share `{rounded.full}` geometry and `{typography.badge}` uppercase lettering.

### Hero

**`hero`** — Minted `{colors.surface-soft}` (#e1efea) background providing gentle differentiation from the white canvas. Headline in `{typography.display-xl}` (Escalator 700, 48px, −0.5px tracking), subhead in `{typography.body-md}` (Tiempos Text 400, 16px). Primary CTA button anchored below subhead. Minimum 480px height; on wide viewports the layout shifts to a two-column image/text split.

### Gift Finder

**`gift-finder-card`** — Soft mint background (`{colors.surface-soft}`), 12px radius, internal label in green uppercase `{typography.label-sm}` ("For Her," "Under $50"), title in `{typography.title-md}`. These grid tiles drive the "shop by occasion" and "shop by recipient" landing experiences, bridging editorial intent with category navigation.

### Pricing

**`price-tag`** and **`price-tag-sale`** — Regular price uses `{colors.ink}` in `{typography.price-display}`. Sale price switches to `{colors.accent-orange-vivid}` (#eb5721), while the original price sits in `{colors.muted}` with line-through via `{price-tag-original}`. The orange strike-through pairing draws the eye to savings without requiring a badge.

### Social Sharing

**`social-share-facebook`** and **`social-share-pinterest`** — Platform-native fills (#3b5998 and #bd081c respectively), white label, 4px radius. These components make no effort to match the brand green — the platform identity is the affordance. Gift registries and curated lists surface these share buttons prominently, since social proof is central to the gifting use case.

### Footer

**`footer`** — Deep forest (#003926) background with off-white body text and `{colors.accent-teal-soft}` (#ccecf2) links that maintain legibility against the dark field. Section headings in `{typography.label-sm}` white uppercase create scannable columns. The dark footer grounds the page after the colorful product browse above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces link row; promo strip collapses to single line; hero goes full-width single-column; filter chips scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; nav links visible if space permits, otherwise hamburger; hero splits to 60/40 image-text; gift-finder cards in 2×2 grid |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav with dropdowns; hero at two-column 50/50; gift-finder cards in 4-across row; search bar expands inline |
| Wide | > 1440px | Four-column product grid; content max-width ~1380px centered; hero image fills full bleed behind constrained text column |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Filter chips padded to 36px height with generous horizontal padding for tap accuracy
- Product card tap target covers full card face including image
- Nav hamburger target 48×48px

### Collapsing Strategy

- Primary nav collapses to hamburger at < 1024px; drawer slides from left over canvas
- Category badge row scrolls horizontally on mobile with gradient fade indicating overflow
- Footer columns stack vertically on mobile: newsletter signup first, then link columns, then legal row last
- Hero text/image stacks vertically on mobile with text above image

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Escalator font metrics (x-height, cap-height, optical size range) not confirmed; fontSize and weight values are estimated from visual pattern and category conventions
- UncommonGoods custom font is likely scoped to wordmark only — weight and full character set not extractable from CSS alone
- Tiempos Text licensing tier and whether a web-subset is in use could not be confirmed
- Exact button border-radius for production CTAs not pixel-confirmed; 4px estimated from visual inspection
- Card shadow values (blur, spread, opacity) are approximated; exact box-shadow string not extracted
- Navigation dropdown structure (mega-menu vs. simple dropdown, column count, featured imagery) not mapped
- Modal and overlay patterns (quick-view, cart drawer) not extracted
- Animation and transition timing values entirely absent from hints
- Exact spacing scale used in production grid (column width, gutter width) not confirmed beyond token approximations
- Whether Tiempos Text is used for all body copy or alternates with a sans-serif in UI chrome is ambiguous from font-family extraction
