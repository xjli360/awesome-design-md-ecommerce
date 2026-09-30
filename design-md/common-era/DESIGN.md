---
version: alpha
name: "Common Era"
source_url: "https://www.commonera.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Molten wine (#64242f) sits in the meta theme-color slot — a choice that announces Common Era as a brand fluent in the visual language of oxidized bronze, ochre pigment, and the deep-red ink of ancient manuscripts. Most demi-fine brands reach for black or neutral cream as their primary voltage; here the primary CTA and brand anchor is the color of a dried pomegranate, of blood-red carnelian, of the rarest Roman murex dye. Cormorant handles the entire display register at weight 300–400, its hairline serifs mimicking the incised strokes of stone inscription; EB Garamond runs body copy with the unhurried clarity of a printed codex. Neither font has ever been selected for modernity.

  The palette's most surprising element is the periwinkle band — #c0c6e5 deepening to #828fd6 — which appears as category chips and accent surfaces rather than a principal tone. It reads as lapis lazuli ground into powder, the color ancient Egyptians reserved for sky-gods and sacred water. Against the deep wine and antique gold (#ab8c52), this periwinkle creates a three-note chord that signals Mediterranean rather than contemporary Scandinavian or Parisian demi-fine. Gold itself renders as #ab8c52 rather than a bright yellow, closer to hammered electrum than machine-polished 18k, deepening to #806430 in active and shadow states.

  The canvas is never pure white: #f9f6f2 is the ground, with surface layers stepping through #f5f2ec and #f4efe8 toward #f1eae1 — a progression from cool parchment to warm vellum that makes photography of metal and stone read older and heavier. Border radius is near-zero throughout; the brand's reference objects — coins, wax seals, carved stelae — all have sharp minted edges, not pill shapes. Spacing is generous, treating each product image as an artifact on a clear display field. The dark registers (#282c2e, #2f0d13, #140004) form a near-black palette layered beneath overlaid display text and footer backgrounds, suggesting dim gallery light rather than e-commerce daylight.

colors:
  primary: "#64242f"
  primary-active: "#501011"
  primary-disabled: "#d1bdc1"
  ink: "#212121"
  body: "#2e2e2e"
  muted: "#626160"
  muted-soft: "#a49c8b"
  hairline: "#d9d9d9"
  hairline-warm: "#e6d2b9"
  canvas: "#f9f6f2"
  surface-soft: "#f5f2ec"
  surface-card: "#f4efe8"
  surface-warm: "#f1eae1"
  on-primary: "#f9f6f2"
  on-dark: "#f9f6f2"
  scrim: "#140004"
  ink-alt: "#282c2e"
  wine-deep: "#2f0d13"
  gold: "#ab8c52"
  gold-dark: "#806430"
  gold-light: "#e6d2b9"
  myth: "#c0c6e5"
  myth-deep: "#828fd6"

typography:
  display-xl:
    fontFamily: "'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 58px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 38px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  body-md:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.03em
  button-md:
    fontFamily: "'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.15em
    textTransform: uppercase
  price-display:
    fontFamily: "'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.02em
  eyebrow:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Cormorant', 'EB Garamond', Georgia, serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 44px
    borderColor: "{colors.primary}"
    borderWidth: 1px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    focusBorderColor: "{colors.primary}"
    padding: 12px 16px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottomColor: "{colors.hairline}"
    borderBottomWidth: 1px
    logoColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.body}"
  hero-banner:
    backgroundColor: "{colors.wine-deep}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    overlayColor: "{colors.scrim}"
    overlayOpacity: 0.45
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    eyebrowTypography: "{typography.eyebrow}"
    eyebrowColor: "{colors.gold}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section}"
  myth-tag:
    backgroundColor: "{colors.myth}"
    textColor: "{colors.ink-alt}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  gold-badge:
    backgroundColor: "{colors.gold}"
    textColor: "{colors.canvas}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  price-display:
    typography: "{typography.price-display}"
    regularColor: "{colors.body}"
    saleColor: "{colors.primary}"
    compareAtColor: "{colors.muted}"
  search-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    borderBottomColor: "{colors.hairline}"
    borderBottomWidth: 1px
  footer:
    backgroundColor: "{colors.ink-alt}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.gold-light}"
    headingTypography: "{typography.eyebrow}"
    headingColor: "{colors.gold}"
    borderTopColor: "{colors.primary}"
    borderTopWidth: 2px
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — Deep wine (#64242f) fill with warm off-white label, zero corner radius so the edge reads like the face of a minted coin. Button label runs in Cormorant at 12px with 0.15em letter-spacing and uppercase transform — the wide tracking mimics the cadence of a stone-cut Latin inscription. Active state descends to #501011 (near-black red); disabled washes the fill to blush #d1bdc1 with muted-gray text. These are never pill-shaped or rounded; the sharp edge is the point.

**`button-secondary`** — Transparent body with a 1px wine border, same uppercase-tracked Cormorant label as primary. Sits comfortably against the warm parchment canvas backgrounds without flattening hierarchy when placed alongside editorial imagery. Reduces visual noise where a solid fill would overpower product photography.

**`button-ghost`** — Hairline-bordered, transparent fill, ink label. Reserved for tertiary actions such as material selector swatches, wishlist toggles, and filter dismissal where the interaction is low-stakes and the primary action already dominates.

### Text Input

**`text-input`** — Flat rectangle, no border radius, single hairline-gray border (#d9d9d9) that sharpens to a wine outline (#64242f) on focus. EB Garamond body-md type keeps form fields tonally consistent with surrounding editorial copy; the checkout flow does not break the period atmosphere. Placeholder text in muted gray (#626160) is light but readable on the warm canvas background.

### Navigation

**`nav-bar`** — 64px tall on warm canvas, main links in Cormorant uppercase at 13px with 0.12em letter-spacing. Wordmark likely rendered in primary wine (#64242f). A single hairline rule at the bottom separates the bar from page content. On mobile, the bar collapses to a hamburger icon; the resulting drawer likely inverts to a dark background to signal the overlay mode.

### Product Card

**`product-card`** — Portrait 3:4 image sits on a warm surface-card (#f4efe8) field with no border radius. Product name renders in title-sm EB Garamond below the image; price sits beneath that in Cormorant price-display scale. Grid columns are spaced generously — the brand's artifact-on-display-field photography style demands breathing room, not a tight pack.

### Hero Banner

**`hero-banner`** — Either a full-bleed photograph with a near-opaque dark scrim (#140004 at 45%) or a flat wine-deep (#2f0d13) panel. Headline in display-xl Cormorant at weight 300, typically one or two lines, reading as a classical heading rather than a commerce callout. Editorial subtext in EB Garamond body-md below; a primary button sits at left or center alignment beneath.

### Collection Header

**`collection-header`** — Warm surface-soft (#f5f2ec) panel that opens each collection page above the product grid. An eyebrow line in antique-gold uppercase type names the cultural source ("Ancient Greece", "Mesopotamia", "Celtic Myth"). A display-md Cormorant headline follows, then two to four sentences of editorial body copy in EB Garamond before the grid begins. Section-level padding on all sides creates a reading experience rather than a banner.

### Myth Tag

**`myth-tag`** — Periwinkle (#c0c6e5) chip with zero border radius, uppercase eyebrow type in ink-alt (#282c2e). The most distinctive UI element in the system: used to label products by mythological origin, filter panels by cultural category, and occasionally as a story accent on editorial pages. The periwinkle reads as lapis lazuli and sky-deity iconography against the wine-and-gold primary palette — no other demi-fine brand has this chip color.

### Gold Badge

**`gold-badge`** — Antique gold (#ab8c52) fill, warm canvas text, uppercase eyebrow type. Applied to "New Arrival", "Bestseller", and material callouts such as "18k Vermeil" or "Sterling Silver". The hammered quality of #ab8c52 keeps the badge from reading as generic e-commerce gold; it sits closer to an old coin than a retailer's highlight sticker.

### Price Display

**`price-display`** — Cormorant price-display scale (16px, weight 400, 0.02em tracking). Regular price in body color (#2e2e2e); sale price renders in wine primary (#64242f); compare-at price struck through in muted gray (#626160). No bright red sale states — the wine primary is already the most dramatic tone in the palette, and overloading it would dilute its authority as the primary CTA color.

### Search Drawer

**`search-drawer`** — Drops from the top or slides in from the right on a warm canvas background. Houses a full-width text-input at the top; results appear below in body-md EB Garamond. A single hairline border separates the input row from the results list. No border radius anywhere in the drawer — consistent with the zero-radius system.

### Footer

**`footer`** — Near-black ink-alt (#282c2e) background. Column headings in antique-gold eyebrow uppercase; links in gold-light (#e6d2b9) — warm enough to avoid the clinical look of pure white on dark. A 2px primary wine border tops the footer, marking the transition from page body. Body copy in on-dark (#f9f6f2) rather than pure white preserves the aged-manuscript atmosphere even at the darkest tier.

### Breadcrumb

**`breadcrumb`** — Caption-scale EB Garamond at 12px, muted gray (#626160) for inactive path segments, ink (#212121) for the current page. Hairline-gray separators. Sits directly below the nav-bar on collection and product detail pages; understated and functional, never prominent.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline scales from display-xl to display-sm; collection-header padding reduces to spacing.lg; myth-tags wrap horizontally across filter rows |
| Tablet | 744–1128px | Two-column product grid; nav shows main categories inline; hero image runs full-bleed with left-aligned text block; collection-header editorial copy fully visible |
| Desktop | 1128–1440px | Three to four-column product grid; collection-header side-text panel active; breadcrumb visible; search drawer slides from right edge |
| Wide | > 1440px | Grid max-width ~1280px centered on canvas; hero imagery bleeds to viewport edge with tighter scrim; footer spreads to five columns |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Nav links expand to full-width tap targets inside the mobile drawer overlay
- Entire product card face is tappable, not just the image or name element
- Myth-tag and gold-badge chips maintain at least 40px tap height on mobile filter panels

### Collapsing Strategy
- Navigation collapses to hamburger at < 744px, opening a full-screen overlay in ink-alt (#282c2e) with large Cormorant nav links in on-dark type
- Collection filter sidebar collapses to a bottom sheet or modal on mobile; myth-tags and gold-badge filters are the primary filter affordances
- Hero headline scales from display-xl on desktop to display-sm on mobile, maintaining Cormorant weight 300 throughout — never goes bold
- Footer columns stack vertically at < 744px; the 2px wine top border remains visible as an anchor

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Button border radius not confirmed from extraction; zero-radius assumed from the brand's reference aesthetic (coins, seals, carved stone)
- Exact nav-bar height not extracted; 64px estimated from visual conventions for editorial jewelry brands
- No animation or transition data captured (hover state timing, cart drawer entrance, product image swap behavior on hover)
- Product image hover behavior (second-image swap vs. zoom vs. none) not confirmed
- Exact Cormorant weight variants available on the live Shopify build not confirmed; 300/400/500 assumed from typical Cormorant variable font range
- Mobile navigation drawer background color not confirmed from extraction; ink-alt (#282c2e) assumed from palette
- Cart drawer, wishlist drawer, and quick-add sheet UI not extracted
- Whether the wordmark is set in Cormorant or is a custom SVG logotype not confirmed
- Periwinkle (#c0c6e5, #828fd6) exact usage contexts inferred from palette position; category-chip and filter role assumed, not observed directly
- Gold-dark (#806430) exact usage context not confirmed; assumed for hover/active state on gold elements
