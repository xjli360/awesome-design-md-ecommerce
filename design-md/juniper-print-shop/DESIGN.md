---
version: alpha
name: "Juniper Print Shop"
source_url: "https://juniperprintshop.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Ratio Modern SC's small-caps letterforms on a parchment ground (#ede8db) announce the intention before a single product image loads — Juniper Print Shop is designing for the wall before it designs for the screen. That cream canvas does not try to disappear into a neutral void the way a white e-commerce template does; it already reads like uncoated stock, the same warm field a rolled poster ships inside. Near-black (#121212) headline ink lands at maximum contrast against it while still sitting warmer than a pure digital zero, so the hierarchy feels printed rather than coded. An indigo blue (#334fb4) — not generic corporate cobalt but something specific and slightly dusty, closer to a mid-century university press cover — carries every primary action: add-to-cart CTAs, active filter states, and link states. Next to parchment it reads as a printing ink choice rather than a UI affordance, and that compression of physical and digital vocabulary is the whole effect. Sage (#596a62) holds secondary labels, hover states, and muted utility copy, grounding the system in something botanical — an apt counterweight given the brand name.

  Work Sans handles all navigational chrome and product metadata at weights 400–600, keeping the interface legible and contemporary. Ratio Modern SC (small-caps, tracking open) is reserved for editorial display: hero headlines, section overlines, and collection names. The small-caps register performs the visual authority that a heavy-weight sans would otherwise supply; display-xl sits at 56px in weight 400 and the letterform transformation does the lifting. Corners are squared or barely there — {rounded.xs} on buttons and inputs, {rounded.none} on every image frame and product card — a deliberate echo of the physical print world where prints have square corners. {rounded.full} appears only on filter pills and the search field, one friendly concession to browseable e-commerce convention. Spacing is generous: collection rows breathe at {spacing.section} between them, grids carry {spacing.lg} gutters, and the parchment shows between cards rather than tiles pressing edge to edge. The result is a gallery wall browsed in good afternoon light, not a catalog scanned at speed.

colors:
  primary: "#334fb4"
  primary-active: "#2a3f96"
  primary-disabled: "#a8b9e4"
  ink: "#121212"
  body: "#2a2a2a"
  muted: "#596a62"
  sage: "#596a62"
  hairline: "#dedede"
  canvas: "#ede8db"
  surface-soft: "#ece8db"
  surface-mid: "#ece7db"
  surface-card: "#f3f3f3"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'ratio-modern-sc', 'ratiomodern', serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: 0.02em
    fontVariant: small-caps
  display-md:
    fontFamily: "'ratio-modern-sc', 'ratiomodern', serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.02em
    fontVariant: small-caps
  display-sm:
    fontFamily: "'ratio-modern-sc', 'ratiomodern', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.02em
    fontVariant: small-caps
  title-md:
    fontFamily: "'Work Sans', 'Assistant', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Work Sans', 'Assistant', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Work Sans', 'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Work Sans', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Work Sans', 'Assistant', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Work Sans', 'Assistant', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Work Sans', 'Assistant', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  label-uppercase:
    fontFamily: "'Work Sans', 'Assistant', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Work Sans', 'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
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
    padding: 12px 28px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageRounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    textColor: "{colors.ink}"
    mutedTextColor: "{colors.muted}"
    gap: "{spacing.sm}"
    padding: "0"
    aspectRatio: "1 / 1"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    paddingY: "{spacing.section}"
    ctaTypography: "{typography.button-md}"
  collection-header:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    paddingY: "{spacing.xxl}"
  filter-pill:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  artwork-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  artwork-badge-sage:
    backgroundColor: "{colors.sage}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    borderSelected: "2px solid {colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 12px"
    minWidth: 72px
  search-field:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "none"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    width: 420px
    titleTypography: "{typography.title-md}"
    lineItemTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
  email-signup:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    inputBackgroundColor: "{colors.canvas}"
    inputBorder: "1px solid {colors.hairline}"
    inputTypography: "{typography.body-md}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-md}"
    rounded: "{rounded.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    linkColor: "{colors.surface-card}"
    headingTypography: "{typography.label-uppercase}"
    bodyTypography: "{typography.body-sm}"
    paddingY: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Indigo (#334fb4) fill on 4px-rounded corners with uppercase Work Sans at 1px tracking. This is the primary purchase action: Add to Cart, Checkout, and prominent editorial CTAs. Hover darkens to primary-active (#2a3f96); disabled washes to a pale indigo (#a8b9e4). The uppercase tracking at this compact 13px size gives the label the register of a printed stamp rather than a typical digital button label.

**`button-secondary`** — Transparent background with a 1.5px solid ink (#121212) border; same uppercase typography as primary. Used for secondary browse actions (View Collection, See More) and paired alongside button-primary in product pages. On hover, background fills to a very light surface-card tint to acknowledge the interaction without committing to full ink fill.

**`button-ghost`** — No border, no fill; primary-blue text with underline. Used for in-body links and low-hierarchy actions like "Read More" in editorial text blocks. Keeps prose areas clean and avoids button proliferation.

### Form Inputs

**`text-input`** — Parchment canvas (#ede8db) background with a 1px hairline (#dedede) border and 4px rounding to match button geometry. On focus, border steps up to 1px solid ink (#121212) — a deliberate, quiet focus signal consistent with the squared-corner aesthetic. Placeholder text renders in sage (#596a62) rather than neutral gray, keeping even empty states on-palette.

### Navigation

**`nav-bar`** — 60px tall, parchment (#ede8db) background with a 1px hairline bottom border. Logo rendered in display-sm small-caps Ratio Modern SC. Nav links use Work Sans 14px/500. On mobile the nav collapses to a hamburger; the parchment ground extends full-bleed so the navigation always reads as part of the same printed surface as the page beneath it.

### Product Grid & Cards

**`product-card`** — Zero rounding on the image frame and card container; square aspect ratio for poster artwork. Title below in body-sm Work Sans, price in the price token (15px/500). A thin gap-sm space separates image from metadata. Hover state on the image may render a sage (#596a62) overlay or secondary title reveal; the card itself does not animate — prints do not move. Artwork badges (Limited Edition, New, Best Seller) sit as absolute-positioned overlays in the top-left corner.

### Hero

**`hero`** — Surface-soft parchment (#ece8db) background, full-width. Headline in display-xl Ratio Modern SC small-caps (56px), subhead in body-md Work Sans. CTA button uses button-primary inline below subhead copy. Section padding at spacing.section top and bottom gives the hero breathing room proportional to a broadsheet page. On mobile, headline drops to display-md (36px).

### Collection Browsing

**`collection-header`** — Surface-soft fill, headline in display-md Ratio Modern SC small-caps, optional descriptor in body-md. Sits above the filter-pill row. The parchment continuity between nav, hero, and collection-header creates an uninterrupted "page" feel before the product grid breaks into surface-card tiles.

**`filter-pill`** / **`filter-pill-active`** — Rounded-full tags using label-uppercase Work Sans (11px, 1.2px tracking, all caps). Inactive: transparent fill, 1px hairline border, ink text. Active: ink fill, canvas text — the only place the near-black becomes a background fill outside the footer. Filter pills appear as a scrollable horizontal row on mobile.

### Size Selector

**`size-selector`** — Print size options (e.g., 5×7, 8×10, 11×14, 16×20) rendered as discrete selection tiles: 1px hairline border at rest, 2px ink border when selected, body-sm text, 4px rounding. The border-weight shift is the sole selection signal — no fill change — keeping the grid of sizes feeling like a typeset table rather than a button group.

### Artwork Badges

**`artwork-badge`** — Indigo (#334fb4) fill, white text, label-uppercase typography, 4px rounding. **`artwork-badge-sage`** — Sage (#596a62) fill, white text; used for "New Arrival" or seasonal editorial labels where the blue would compete with the primary CTA. Both sit as small absolute overlays on product card images.

### Cart & Email

**`cart-drawer`** — 420px right-side drawer on canvas parchment, 1px hairline left border. Line item titles in body-sm, prices in price token, section title in title-md. Aligns visually with the page surface — no elevation shadow, no modal overlay darkness; the drawer is a panel of the same page, not a popup.

**`email-signup`** — Surface-soft parchment band, display-sm headline in Ratio Modern SC, body-md descriptor, canvas-background input field, and a button-primary CTA. Typically used in the footer breakout zone above the ink-colored footer proper.

### Footer

**`footer`** — Near-black (#121212) fill; surface-card (#f3f3f3) light gray text and links. Section headings in label-uppercase. The stark ink reversal at the bottom grounds the scroll and closes the parchment field; it reads as the back cover of the print object the whole page was pretending to be.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero headline drops to display-md (36px); filter pills become horizontal scroll row; size-selector tiles wrap to 2-col grid |
| Tablet | 744–1128px | 2–3 column product grid; nav may retain primary links with hamburger for secondary; hero headline at display-md or intermediate size |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with all collection links; hero at display-xl; filter pills shown as wrapping inline row |
| Wide | > 1440px | Max content width capped (~1400px) with canvas parchment gutter fill; product grid may expand to 5 columns; hero text constrained to ~50% width with image right |

### Touch Targets

- All buttons and filter pills minimum 44px touch height
- Size-selector tiles minimum 44×44px
- Nav links on mobile minimum 48px tall in collapsed menu
- Cart drawer close and quantity controls minimum 44px

### Collapsing Strategy

- Primary nav collapses to hamburger at tablet breakpoint and below; search icon always visible in collapsed state
- Filter/sort row collapses to a single "Filter" button that opens a drawer on mobile
- Hero layout shifts from 50/50 split (text + image) to stacked (image above, text below) on mobile
- Footer multi-column grid collapses to single accordion-style column on mobile
- Cart drawer becomes full-width bottom sheet on mobile rather than 420px side panel

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-active` (#2a3f96) and `primary-disabled` (#a8b9e4) are derived approximations — neither was present in the extracted color list; verify against actual hover/disabled states on site
- `body` text color (#2a2a2a) is a derived softening of extracted #121212; only pure near-black was captured, so body and ink may in practice share #121212
- No explicit hover color for sage (#596a62) secondary elements was extractable; sage hover state is unspecified
- Ratio Modern SC weight ladder is unknown beyond the inferred 400 used in display contexts; bold or medium weights may exist but were not captured
- Exact font-weight usage for ratiomodern vs ratio-modern-sc variants is unconfirmed — the two font-family strings may reference the same file or separate cuts
- Animation/transition timings (hover durations, drawer slide speed) not captured
- Mobile navigation pattern (hamburger vs. slide-over vs. bottom nav) not confirmed from extraction
- Exact product grid column counts per breakpoint not verified from live layout
- `object-fit: contain` appeared in font-family extraction — CSS parsing artifact, ignored
