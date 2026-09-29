---
version: alpha
name: "BySimran"
source_url: "https://bysimran.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Wine-dark burgundy (#791d34) occupies the meta theme-color slot rather than the aspirational gold that most ethnic jewelry brands lead with — a deliberate inversion that positions BySimran's identity in the deeper, more ceremonial register of South Asian color vocabulary: the color of sindoor, of dark silk borders, of the night-blooming rose. Against it, the antique gold family (#ab8c52, #9a7e4a, #d4af32) operates in three distinct temperatures — warm, richer, flash-bright — allowing the metallic vocabulary to carry visual hierarchy without redundancy. A fourth accent, Mughal teal (#108474), surfaces rarely but decisively, the hue of enameled meenakari inlay found in traditional Jaipur goldsmithing and Mughal tilework alike, landing as a genuine cultural signal rather than a borrowed global palette choice.

  The ground system is warm throughout: four cream registers (#fcfbf9, #f5f2ec, #f0ebe2, #e8d4ae) that deepen in saturation from canvas to surface-warm, evoking undyed cotton, ivory bangle material, and aged linen rather than clinical white. Hard edges — `{rounded.none}` on buttons and inputs, `{rounded.xs}` on filter chips — run counter to the soft-pill conventions saturating the DTC market; this is a brand whose goods have geometry, whose craft belongs to a metalworking tradition with defined forms and sharp bezels.

  Baskerville in the display register carries productive ambiguity: a British serif from the 1750s repurposed by a Modern Desi brand to signal both antiquity and the irreverence of reclaiming inherited aesthetics. DM Sans and Karla handle utility layers — navigation, body copy, captions — in modest weights, keeping the functional tier visually quiet so the editorial serif can breathe. Button labels run in tracked uppercase at 0.06em via `{typography.button-md}`, a deliberate pause before action that fits the considered nature of a jewelry purchase rather than the frictionless impulse flows of fast-fashion checkouts.

  The deep brown spectrum (#4e2c1d, #5f3725, #613624) substitutes for black in text-on-warm-surface contexts, softening contrast to match the palette's warmth without losing legibility. Burgundy variants (#b31e46, #9d1a3d) serve as hover and active states, keeping the primary hue family coherent through interaction while providing clear feedback. Trust signals, sale callouts, and filter states all share the zero-radius geometry — a mark of visual discipline across a brand that spans traditional bridal, everyday wear, and contemporary fusion.

colors:
  primary: "#791d34"
  primary-active: "#5f1528"
  primary-disabled: "#c4899a"
  gold: "#ab8c52"
  gold-bright: "#d4af32"
  gold-muted: "#9a7e4a"
  teal: "#108474"
  teal-active: "#0c6559"
  burgundy-alt: "#b31e46"
  ink: "#212121"
  body: "#555555"
  muted: "#a49c8b"
  hairline: "#d9d9d9"
  hairline-soft: "#ece7db"
  canvas: "#fcfbf9"
  surface-soft: "#f5f2ec"
  surface-card: "#f0ebe2"
  surface-warm: "#e8d4ae"
  on-primary: "#ffffff"
  brown-deep: "#4e2c1d"
  brown-mid: "#5f3725"
  scrim: "#282c2e"

typography:
  display-xl:
    fontFamily: "Baskerville, 'Baskerville Old Face', 'Goudy Old Style', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Baskerville, 'Baskerville Old Face', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'DM Sans', Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0.01em
  title-sm:
    fontFamily: "'DM Sans', Karla, 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0.09em
    textTransform: uppercase
  body-md:
    fontFamily: "Karla, 'DM Sans', 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Karla, 'DM Sans', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Karla, 'DM Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  price-display:
    fontFamily: "'DM Sans', Karla, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-compare:
    fontFamily: "'DM Sans', Karla, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'DM Sans', Karla, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  label-sm:
    fontFamily: "'DM Sans', Karla, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'DM Sans', Karla, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.03em

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
    hoverBackground: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
    cursor: not-allowed
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "1px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    hoverBackground: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
    hoverBorderColor: "{colors.brown-mid}"
  button-gold:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
    hoverBackground: "{colors.gold-muted}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    activeColor: "{colors.primary}"
    logoAccentColor: "{colors.gold}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    comparePriceTypography: "{typography.price-compare}"
    comparePriceColor: "{colors.muted}"
    comparePriceDecoration: line-through
    salePriceColor: "{colors.primary}"
    padding: "{spacing.md}"
    hoverElevation: "0 4px 20px rgba(40,44,46,0.09)"
    quickAddBackground: "{colors.scrim}"
    quickAddTextColor: "{colors.on-primary}"
    quickAddTypography: "{typography.label-sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.brown-deep}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaBackground: "{colors.primary}"
    ctaTextColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.none}"
    minHeight: 560px
    paddingDesktop: "80px {spacing.xxl}"
    imageOverlay: "linear-gradient(to right, rgba(252,251,249,0.88) 40%, transparent)"
  collection-header:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.brown-deep}"
    titleTypography: "{typography.display-md}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.brown-mid}"
    padding: "{spacing.section} {spacing.xl}"
    borderBottom: "2px solid {colors.gold}"
    accentGlyph: "{colors.gold}"
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.teal}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  gold-badge:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  category-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.brown-mid}"
    border: "1px solid {colors.hairline-soft}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
    activeBackground: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  price-tag:
    currentPriceTypography: "{typography.price-display}"
    currentPriceColor: "{colors.ink}"
    salePriceColor: "{colors.primary}"
    compareAtColor: "{colors.muted}"
    compareAtTypography: "{typography.price-compare}"
    compareAtDecoration: line-through
  trust-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.gold}"
    borderTop: "1px solid {colors.hairline-soft}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base} {spacing.xl}"
  filter-tag:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "6px 14px"
    activeBackground: "{colors.brown-deep}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.brown-deep}"
  footer:
    backgroundColor: "{colors.scrim}"
    textColor: "{colors.muted}"
    headingColor: "{colors.on-primary}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    accentColor: "{colors.gold}"
    dividerColor: "{colors.brown-mid}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Solid burgundy (#791d34) fill on a flat, zero-radius rectangle; typography runs in tracked uppercase DM Sans at 13px/700 weight. Hover darkens to `{colors.primary-active}` (#5f1528) with no animation delay, preserving immediacy. The disabled variant `button-primary-disabled` uses the lightened #c4899a fill; it does not reduce opacity, keeping the label readable for accessibility.

**`button-secondary`** — Transparent background with a 1px burgundy border and burgundy text; the interior gains a warm soft fill (`{colors.surface-soft}`) on hover, signaling interactivity without weight. Used for secondary CTAs like "Add to wishlist" or "View more" adjacent to a primary CTA.

**`button-ghost`** — Transparent with a hairline border (`{colors.hairline}`) and ink text; the border darkens to `{colors.brown-mid}` on hover. Employed for modal dismiss controls, filter reset, and tertiary actions where visual quietness is required.

**`button-gold`** — Antique gold (#ab8c52) fill, white text, zero radius. Reserved for promotional moments — bridal landing pages, sale announcements, or email CTA mirrors — where the metallic color carries celebratory weight beyond the default burgundy primary.

### Text Input

**`text-input`** — Warm canvas background (#fcfbf9) with a 1px hairline border, no radius, and Karla body-md typography. The border shifts to `{colors.primary}` on focus with no box-shadow, keeping the focus ring language minimal and flat. Placeholder text in `{colors.muted}` (#a49c8b) at the same size as entry text prevents the "empty state" from feeling too visually light.

### Nav Bar

**`nav-bar`** — 64px tall on a warm canvas ground, separated from the body by a single hairline-soft bottom border. Navigation links use DM Sans 14px/500 with 0.03em tracking; the active/current link switches to `{colors.primary}` burgundy with no underline. The logo lockup is expected to carry a gold accent element (`{colors.gold}`). On mobile the nav collapses to a hamburger trigger; on desktop categories expand into mega-dropdowns.

### Product Card

**`product-card`** — Zero-radius card sitting on a warm canvas ground; the image area uses `{colors.surface-soft}` as a background before the photograph loads, preventing jarring white flashes against the warm palette. Product name is set in `{typography.title-md}` (DM Sans 16px/600), current price in `{typography.price-display}` (DM Sans 18px/600). Sale pricing shows the current price in `{colors.primary}` burgundy alongside the compare-at in `{colors.muted}` with strikethrough. On hover, a subtle shadow lifts the card and a quick-add overlay slides from the bottom of the image in `{colors.scrim}` with `{colors.on-primary}` label text.

### Hero Banner

**`hero-banner`** — Minimum 560px tall section with the image occupying the right half while a gradient veil (warm canvas at 88% opacity fading right to transparent) ensures legibility of left-aligned copy on any photography. Headline in Baskerville display-xl at 48px/400 weight rendered in `{colors.brown-deep}`, subhead in Karla body-md in `{colors.body}`. The primary CTA sits below the subhead in `{colors.primary}` fill with zero radius. On mobile the image crops to a 4:5 aspect ratio above stacked text.

### Collection Header

**`collection-header`** — A full-bleed warm band (`{colors.surface-warm}`, #e8d4ae) marking category entry points. The title runs in Baskerville display-md at 32px in `{colors.brown-deep}`, with a descriptive subtitle in Karla body-md at `{colors.brown-mid}`. A 2px solid gold (`{colors.gold}`) rule along the bottom border anchors the section to the product grid below and echoes the metallic accent register without requiring imagery.

### Badges

**`sale-badge`** — Flat burgundy (#791d34) rectangle, 11px/700 uppercase label in white. Zero radius. Positioned absolute top-left over the product image. **`new-badge`** — Same geometry in Mughal teal (#108474), communicating newness through cultural color rather than a generic convention. **`gold-badge`** — Antique gold fill (#ab8c52), used for "Bestseller" or "Editor's Pick" callouts. All three badges share the same typography token (`{typography.label-sm}`) and 3px 8px padding, forming a coherent badge family differentiated only by fill color.

### Category Chips

**`category-chip`** — Rounded-xs (4px) chips on a warm card surface with a hairline-soft border and brown-mid text in tracked uppercase 13px. Used in collection filter rows and occasion/metal/style pickers. The active state inverts to a solid burgundy fill with white text, matching the primary button language. The chip strip scrolls horizontally on mobile with no wrap, maintaining a single horizontal scannable row of options.

### Price Tag

**`price-tag`** — A composable price display used both on cards and product detail pages. Current price in DM Sans 18px/600 (`{typography.price-display}`); compare-at price in DM Sans 14px/400 with strikethrough (`{typography.price-compare}`) immediately following in muted color. Sale mode colors the current price `{colors.primary}` to mark the discount without requiring a badge, giving the price block its own hierarchy signal.

### Trust Strip

**`trust-strip`** — A slim horizontal band in `{colors.surface-soft}` carrying 3–4 short trust signals ("Free shipping over ₹X", "Hallmark certified", "Easy returns", "Secure checkout") separated by gold icon dividers. Body-sm Karla text in `{colors.body}` keeps the copy visually subordinate; the gold icons (`{colors.gold}`) provide the only accent. The strip appears below the hero on the homepage and above the footer sitewide.

### Filter Tags

**`filter-tag`** — Flat, zero-radius pill with a 1px hairline border; selected state fills to `{colors.brown-deep}` with white text, using the dark sandalwood tone rather than the primary burgundy to distinguish filter active states from CTAs. Used in collection sidebars and mobile filter drawers. On desktop the tag list is static; on mobile it collapses behind a "Filter" trigger button using `{typography.button-md}`.

### Footer

**`footer`** — Deep scrim (#282c2e) ground, close to charcoal but warm-leaning. Column headings in tracked uppercase `{typography.title-sm}` at `{colors.on-primary}`. Link text in Karla body-sm at `{colors.muted}` (#a49c8b), warming on hover to `{colors.gold}`. A gold accent rule or glyph separates the brand column from the utility links. Newsletter input inherits `{text-input}` styling recolored to match the dark ground. Payment and certification icons render in `{colors.muted}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav; hero image stacked above text at 4:5 crop; category chips scroll horizontally; filter opens as a bottom-sheet drawer |
| Tablet | 744–1128px | 2-column product grid; horizontal nav with text labels retained; hero splits 55/45 image-to-text; trust strip shows 2 items |
| Desktop | 1128–1440px | 3–4 column product grid; full mega-nav with dropdown category panels; hero at full 560px min-height with gradient overlay; filter sidebar pinned left |
| Wide | > 1440px | Max-width container (~1440px) centered on the body; side margins fill with `{colors.canvas}`; product grid stays at 4 columns maximum |

### Touch Targets

- All buttons minimum 48px height to meet touch-target guidelines
- Category chips minimum 40px height on mobile with 16px horizontal padding
- Nav hamburger and close targets at 48×48px
- Filter tag rows on mobile use 40px chip height with 8px gap between items
- Quick-add on product card activates on tap of the full image area on mobile, not a small button target

### Collapsing Strategy

- Nav collapses to hamburger at <744px; mega-dropdowns become full-screen slide-in panels
- Collection filter sidebar becomes a bottom-sheet drawer triggered by a sticky "Filter & Sort" bar above the product grid on mobile
- Trust strip reduces from 4 items to 2 on tablet, hides on the smallest mobile breakpoints (<375px)
- Footer columns stack to single column on mobile; accordion expand/collapse controls sections
- Hero text content left-aligns on all breakpoints; image stacks above (not behind) on mobile to preserve the editorial serif headline against a plain warm background

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius value could not be confirmed from extraction — zero radius (`{rounded.none}`) assumed based on cultural jewelry brand conventions; verify against computed styles
- Specific custom font weights for Baskerville (regular vs italic display usage) were not extractable; the brand may use Baskerville italic for product-name accents
- Exact nav height and mega-dropdown structure were not confirmed — 64px assumed from common Shopify theme patterns
- Animation/transition timing values (hover durations, drawer slide speeds) not captured
- Mobile header behavior (sticky vs scroll-away, transparent-on-hero variant) unconfirmed
- Exact price formatting conventions (₹ prefix, comma grouping for Indian numbering system) not confirmed from extraction
- Wishlist and recently-viewed components exist on most Shopify jewelry themes but their styling specifics were not captured
- Whether the teal (#108474) appears as a standalone CTA color or purely as a badge/accent color is ambiguous — treat as accent-only until confirmed
