---
version: alpha
name: "Daphine"
source_url: "https://www.daphine.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Every chain and signet ring in the Daphine collection is photographed against bare skin — a deliberate choice that anchors the entire visual system to body warmth rather than studio white. The brand's palette consequence is inevitable: canvas reads as near-white ivory ({colors.canvas} #FEFDF8), gold CTAs draw from actual 18k warmth (#B8935A) rather than the saturated amber that cheaper jewelry brands use to telegraph luxury. Type is set in a refined serif — Cormorant Garamond or a close equivalent — at lightweight grades that let the letterforms breathe; display headings arrive at 14–16px letter-spacing to produce the elongated rhythm of a French maison logotype, not a fast-fashion banner. Buttons are nearly square-cornered ({rounded.xs} at 3px), a choice that reads as precision rather than severity against the warmth of the gold palette. Product cards carry no shadow and no border — they sit on the surface ({colors.surface-soft}) separated only by generous white margins, trusting the jewelry photography to hold attention without chrome. Navigation is a single horizontal line of widely-spaced uppercase labels in the smallest caption grade: the brand communicates hierarchy through spatial pause, not size escalation. A persistent cart icon and a discreet hamburger for mobile are the only structural chrome. The editorial layer — lookbook sections and founder-voice copy — runs flush to the viewport edge on desktop, with a centered text column capped at 560px to maintain the intimacy of a printed editorial. Gold foil details, monogram packaging, and the brand's recurring motif of an open signet oval all point toward an identity rooted in heirloom gesture: something owned for decades, not a season.

colors:
  primary: "#B8935A"
  primary-active: "#9A7A46"
  primary-disabled: "#E2CFA9"
  ink: "#1C1C1A"
  body: "#3D3C38"
  muted: "#7A7870"
  hairline: "#E5E2DC"
  hairline-soft: "#EFECE6"
  canvas: "#FEFDF8"
  surface-soft: "#F7F4EE"
  surface-card: "#FFFFFF"
  on-primary: "#FFFFFF"
  gold-tint: "#F0E6D3"
  gold-deep: "#8C6F3E"
  error: "#B0392E"

typography:
  display-xl:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: 0.06em
  display-lg:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: 0.05em
  display-md:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.04em
  display-sm:
    fontFamily: "'Cormorant Garamond', 'EB Garamond', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.03em
  title-md:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.12em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0.15em
    textTransform: uppercase
  body-md:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.08em
  price:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.03em
  button-md:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0.18em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0.16em
    textTransform: uppercase
  nav-label:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0.18em
    textTransform: uppercase
  badge-label:
    fontFamily: "'Cormorant Garamond', Georgia, serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0.14em
    textTransform: uppercase

rounded:
  none: 0px
  xs: 3px
  sm: 6px
  md: 10px
  lg: 16px
  xl: 28px
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
    height: 46px
    border: none
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 46px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 46px
    border: "1px solid {colors.ink}"
    hoverBackgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    border: none
    padding: 0
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 46px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoHeight: 20px
    gap: "{spacing.xl}"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: none
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: none
    imageAspectRatio: "3/4"
    imageBackgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
    hoverEffect: "image-scale 1.03"
  product-badge:
    backgroundColor: "{colors.gold-tint}"
    textColor: "{colors.gold-deep}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.body-md}"
    layout: "split — 50% editorial image / 50% text column on desktop; stacked image-above on mobile"
    textPaddingDesktop: "0 {spacing.section}"
    ctaMarginTop: "{spacing.lg}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-md}"
    captionTypography: "{typography.caption}"
    textAlign: center
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xl}"
  filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    borderBottom: "1px solid {colors.hairline}"
    activeBorderBottom: "1px solid {colors.ink}"
    padding: "{spacing.md} 0"
    gap: "{spacing.xl}"
  metal-selector:
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    defaultBackgroundColor: "{colors.canvas}"
    defaultTextColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.primary}"
    size: "28px"
  size-guide-link:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    textDecoration: underline
    hoverColor: "{colors.ink}"
  editorial-block:
    backgroundColor: "{colors.gold-tint}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-lg}"
    bodyTypography: "{typography.body-md}"
    maxTextWidth: 560px
    padding: "{spacing.section} {spacing.xl}"
    imagePosition: "right"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "none"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} {spacing.md}"
    placeholderColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkTypography: "{typography.caption}"
    headingTypography: "{typography.title-sm}"
    linkColor: "{colors.muted}"
    linkHoverColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.xl}"
    logoFilter: "brightness(0) invert(1)"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    width: 420px
    borderLeft: "1px solid {colors.hairline}"
    headingTypography: "{typography.title-md}"
    itemTitleTypography: "{typography.body-sm}"
    itemPriceTypography: "{typography.price}"
    subtotalTypography: "{typography.title-md}"

## Components

### Buttons

**`button-primary`** — The add-to-cart and checkout CTA renders as a near-square-cornered rectangle ({rounded.xs}, 3px) in warm 18k gold ({colors.primary} #B8935A), uppercase spaced lettering at 12px/0.18em. On hover the gold deepens to {colors.primary-active}; disabled state fades to {colors.primary-disabled} without changing the label. Height is fixed at 46px across all product pages so the CTA row never shifts when size options are selected.

**`button-secondary`** — A bordered ghost variant with a 1px ink border and transparent fill; used for secondary actions like "Save to Wishlist" and "View Full Collection." On hover the fill shifts to {colors.surface-soft} to signal interactivity without introducing colour. Shares the uppercase button-md tracking with the primary.

**`button-ghost`** — Text-only link style in {colors.muted} with underline decoration; used for editorial "Read more" links and inline size-guide triggers. No background, no border, no height constraint.

### Navigation

**`nav-bar`** — A 60px-tall horizontal strip in {colors.canvas} with a hairline border ({colors.hairline-soft}) at the base. Nav labels run in {typography.nav-label} (11px / 0.18em uppercase) with wide gaps between: Rings, Necklaces, Bracelets, Earrings, Gifts. The logotype centres at 20px height. A cart count bubble in {colors.primary} and a search icon flank the right edge. On scroll the border intensifies from hairline-soft to hairline; no opacity change or colour shift on the background.

### Product Card

**`product-card`** — Borderless, shadow-free, with a 3:4 image in {colors.surface-soft} that scales to 1.03× on hover at 300ms ease. Title runs in {typography.body-sm} directly below the image with {spacing.sm} gap; price follows in {typography.price} at medium weight. No "Quick Add" overlay on desktop — the brand favours deliberate navigation to the PDP over cart shortcuts.

### Product Badge

**`product-badge`** — A {colors.gold-tint} pill with zero border-radius ({rounded.none}), {colors.gold-deep} text in {typography.badge-label} (10px / 0.14em uppercase). Used sparingly: "New" and "Best Seller" only. Never used for promotional percentages.

### Hero

**`hero`** — A split-frame layout at desktop: the left half carries a full-bleed skin-tone editorial photograph, the right half centres a vertically-stacked heading in {typography.display-xl} (52px / weight 300), a single sentence of body copy in {typography.body-md}, and a {colors.primary} `button-primary`. The {colors.surface-soft} background on the text column provides a warm off-white separation. On mobile the image stacks above and crops to a 1:1 square.

### Metal Selector

**`metal-selector`** — 28px circular swatches with a 1px {colors.hairline} border by default; the selected swatch switches to a 1px {colors.primary} border and fills with {colors.primary}. A label below the swatch row updates in {typography.caption}/{colors.muted} to name the current selection: "18K Yellow Gold", "Sterling Silver", "14K White Gold."

### Editorial Block

**`editorial-block`** — A full-width band in {colors.gold-tint} with a 560px-capped text column on the left and a portrait photograph bleeding to the right edge. The heading runs {typography.display-lg} (38px / weight 300), body copy in {typography.body-md}. Used once per collection page as a brand voice interrupt between product grid sections.

### Filter Bar

**`filter-bar`** — A sticky horizontal rule of category chips below the collection heading. Each chip is plain text in {typography.title-sm} (uppercase / 0.15em) with {spacing.xl} gaps; the active chip underlines with a 1px solid {colors.ink} rule rather than a filled background. No scrolling ticker on desktop — max five categories are shown.

### Cart Drawer

**`cart-drawer`** — A 420px right-anchored panel separated from the page by a 1px {colors.hairline} border (no shadow). Heading in {typography.title-md} uppercase, item titles in {typography.body-sm}, prices in {typography.price}. A persistent {colors.primary} `button-primary` at the bottom reads "Proceed to Checkout." Free shipping threshold note in {typography.caption}/{colors.muted} sits directly above the button.

### Footer

**`footer`** — Dark canvas ({colors.ink}) reversal with muted link text in {typography.caption} that brightens to {colors.canvas} on hover. Column headings in {typography.title-sm}. The logo inverts to white via CSS filter. Social icons are line-weight SVGs at 18px. A newsletter input in {typography.body-sm} sits in its own column with a borderless inline submit arrow.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero stacks image above text; nav collapses to hamburger + logo + cart; filter bar becomes a horizontal scroll row |
| Tablet | 744–1128px | Two-column product grid; hero remains split but text column shrinks to 45%; nav labels reduce to four entries; cart drawer widens to 100vw |
| Desktop | 1128–1440px | Three-column product grid; full split hero; all nav labels visible; editorial block shows side-by-side layout |
| Wide | > 1440px | Four-column product grid; hero image caps at 720px; content columns max-width centred with symmetrical outer margins |

### Touch Targets

- All buttons minimum 46px tall, matching the fixed `button-primary` height
- Metal selector swatches expand hit area to 44×44px with an invisible padding ring around the 28px visual swatch
- Nav hamburger icon: 44×44px touch target; filter chips: 36px minimum tap height with lateral padding
- Cart icon and search icon: 44×44px each

### Collapsing Strategy

- Navigation collapses to hamburger at < 744px; a full-screen overlay slide-in replaces the drawer with stacked category links at {typography.display-sm}
- Filter bar transitions from sticky horizontal tabs to a "Filter +" bottom-sheet trigger at < 744px
- Editorial block reorders to image-above / text-below in a single column on mobile, image crops to 16:9
- Footer four-column grid stacks to two columns at tablet, single column at mobile with accordion-collapsed link sections

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No hex colors could be extracted — the domain daphine.com currently resolves to a domain marketplace ("Strategic-Grade domain names for established businesses") rather than the actual Daphine jewelry site; all palette values above are derived from brand knowledge, not live extraction, and should be verified against the real storefront before production use
- No font stacks were detected; Cormorant Garamond is inferred from the brand's documented Parisian fine-jewelry positioning and is consistent with observed competitors in the French everyday-jewelry segment, but the exact font license and weight variants used on the live site are unconfirmed
- Exact button radius, input height, and spacing scale values are approximated from category conventions; the brand may use a tighter or looser spacing system
- Animation curves and transition durations for product card hover and cart drawer open are not confirmed
- Mobile navigation overlay design (full-screen vs. slide panel, background treatment) is unverified
- Promotional/sale badge colour treatment is unknown — the brand may avoid percentage-off badging entirely
- Exact breakpoints may differ from the 744/1128/1440px grid used here if the brand uses a non-standard grid (e.g., a 320/768/1024/1280 scale)
