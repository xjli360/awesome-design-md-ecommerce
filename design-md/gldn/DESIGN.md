---
version: alpha
name: "GLDN"
source_url: "https://www.gldn.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Four letters edit "golden" down to its skeleton, and the same compression governs the visual system — GLDN runs on a near-monochromatic foundation of near-black (#141414) through a range of warm grays to a pale surface (#f6f6f6), punctuated by a single warm amber (#ee9441) that stands in for the metal rather than illustrating it. Every primary CTA, price anchor, and personalization trigger flows through that amber; it carries exactly that one job, which is why it reads as material rather than marketing. Typography works across three registers: Spectral, a high-contrast literary serif with strong stroke contrast, handles editorial display text where slowed reading is the point; Freight Sans Compressed takes campaign headlines and category labels at tight tracking, where compressed density signals authority without loudness; Inter carries the transactional layer — field labels, cart totals, filter chips — at utilitarian precision. The phrase "Made Personal" is structural rather than tagline copy: engraving inputs, charm selectors, and metal-choice toggles occupy a persistent personalization panel sitting alongside the product image rather than collapsing into a last-step accordion. Buttons round at `{rounded.sm}` — four pixels, enough to soften without reading casual. Dark green (#006400) marks in-stock status in product tiles; a vivid pop-green (#3ed660) labels new arrivals with just enough voltage to register against the near-black canvas of promo banners. Dark red (#8b0000) handles sale ribbons and low-inventory states in a distinct temperature from the brand amber, ensuring those two signals never collide. The footer inverts to near-black (#121212), bracketing the page against the same dark register that opens the hero so the layout feels complete rather than trailing off.

colors:
  primary: "#ee9441"
  primary-active: "#d4781e"
  primary-disabled: "#f4c48b"
  ink: "#141414"
  body: "#545454"
  muted: "#808080"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#e2e2e2"
  on-primary: "#ffffff"
  near-black: "#121212"
  status-available: "#006400"
  status-new: "#3ed660"
  status-sale: "#8b0000"

typography:
  display-xl:
    fontFamily: "'Spectral', 'Spectral Fallback', Georgia, serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Spectral', 'Spectral Fallback', Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'freight-sans-compressed-pro', 'freight-sans-condensed-pro', sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: 1.5px
    textTransform: uppercase
  title-lg:
    fontFamily: "'freight-sans-pro', 'freight-sans-pro Fallback', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
  title-md:
    fontFamily: "'freight-sans-pro', 'freight-sans-pro Fallback', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  personalization-label:
    fontFamily: "'freight-sans-pro', 'freight-sans-pro Fallback', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  engraving-preview:
    fontFamily: "'Spectral', 'Spectral Fallback', Georgia, serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 3px
  price:
    fontFamily: "'freight-sans-pro', 'freight-sans-pro Fallback', sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0

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
    rounded: "{rounded.sm}"
    padding: 13px 28px
    height: 44px
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
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    padding: 12px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 60px
  product-card:
    backgroundColor: "{colors.canvas}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.xs}"
    imageRounded: "{rounded.xs}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section}"
    ctaVariant: "button-primary"
  personalization-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.personalization-label}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  engraving-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    previewTypography: "{typography.engraving-preview}"
    previewBackground: "{colors.surface-soft}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  charm-selector-item:
    backgroundColor: "{colors.surface-soft}"
    selectedBorder: "2px solid {colors.primary}"
    unselectedBorder: "1px solid {colors.hairline}"
    hoverBorder: "1px solid {colors.body}"
    rounded: "{rounded.full}"
    size: 56px
  collection-filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    activeBackground: "{colors.ink}"
    activeTextColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  badge-new:
    backgroundColor: "{colors.status-new}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-sale:
    backgroundColor: "{colors.status-sale}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  badge-available:
    backgroundColor: "{colors.status-available}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.canvas}"
    mutedTextColor: "{colors.muted}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption}"
    borderTop: "none"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Warm amber (#ee9441) fill with white Inter text in uppercase tracked at 0.8px, 44px tall, 4px radius. On hover the fill darkens to `{colors.primary-active}` (#d4781e); disabled state fades to a muted amber `{colors.primary-disabled}` at full opacity rather than reduced opacity, keeping the layout stable. This button is reserved exclusively for purchase actions (Add to Cart, Personalize Now, Checkout) — it never appears in navigation or editorial contexts.

**`button-secondary`** — White fill with a full `{colors.ink}` border and matching text, same 44px height and 4px radius as the primary. Used for secondary actions like Save to Wishlist, View Details, and filter confirmations. On hover the border thickens visually by switching to a 1.5px stroke rather than changing fill color.

**`button-ghost`** — Transparent background, ink-colored uppercase text, no border. Used for navigation-adjacent links (View All, See More) and dismissal actions in modal overlays. Padding is vertical-only so it aligns flush in text contexts.

### Text Input

**`text-input`** — White fill, 1px `{colors.hairline}` border that transitions to full `{colors.ink}` on focus; no box-shadow ring on focus (unlike most Shopify defaults), keeping the interaction minimal. Spectral is not used here — all form inputs run in Inter body-md for scan-readability. The input is 44px tall to match button height for inline pairings like email capture + subscribe.

### Nav Bar

**`nav-bar`** — White 60px bar with a 1px `{colors.hairline}` bottom border. The wordmark sits at left in Spectral at ~18px weight 300, contrasting with the Inter nav links in the center and right zones. A persistent cart-count dot appears in `{colors.primary}` amber when items exist. On scroll past 80px the nav gains a subtle shadow (0 2px 8px rgba(0,0,0,0.08)) without a background change — it was already white.

### Product Card

**`product-card`** — Off-white `{colors.surface-soft}` image well with 2px rounded corners. Title renders in `{typography.title-md}` (Freight Sans Pro, 16px, tracked), price in `{typography.price}` (Freight Sans Pro, 17px, untracked). Badge placement is top-left of the image well; only one badge renders at a time — sale takes precedence over new. On hover the product image scales to 103% with a 300ms ease transition; no card outline or shadow appears, keeping the grid clean.

### Hero

**`hero`** — Full-bleed near-black (#121212) section with white Spectral display-xl headline at weight 300. The low-contrast temperature of near-black (not pure #000) against white text keeps it warm rather than stark. A subhead in Inter body-md at reduced opacity (0.7) sits below, then the primary amber CTA. On mobile the headline drops to `{typography.display-lg}` (40px) and the section height collapses from viewport-height to auto with 48px vertical padding.

### Personalization Panel

**`personalization-panel`** — Soft gray (#f6f6f6) panel with 1px `{colors.hairline}` border and 8px radius, sitting in the right column alongside the product image on desktop. Personalization options — engraving text, charm selection, metal choice — are stacked vertically with Freight Sans Pro labels at 13px. The panel persists as the user scrolls through product images, using position: sticky.

### Engraving Input

**`engraving-input`** — White text input with live preview below: the typed characters render immediately in `{typography.engraving-preview}` (Spectral 22px weight 300, 3px letterspacing) against the soft-gray preview block, simulating how the engraving will appear on metal. Character count shows as caption-sm muted text at bottom-right. When the limit is reached the counter shifts to `{colors.status-sale}` red.

### Charm Selector

**`charm-selector-item`** — 56px circular image tiles in `{colors.surface-soft}` with a 1px hairline ring. Selected state switches to a 2px `{colors.primary}` amber ring with no fill change, so the amber bracket reads as confirmation without covering the charm image. On hover the ring steps to body gray. Items sit in a horizontal scrollable row on mobile; a 3-column grid on desktop.

### Collection Filter Chips

**`collection-filter-chip`** — Pill-shaped chips (`{rounded.full}`) with white fill and hairline border in default state. Active state inverts to full `{colors.ink}` fill with white text — no amber here, keeping amber reserved for purchase-path actions. Typography is Inter body-sm (14px) for legibility at the 32px chip height on mobile.

### Badges

**`badge-new`** — Vivid green (#3ed660) with ink text, 2px radius. Small enough (caption-scale) to sit in the product card corner without dominating. **`badge-sale`** — Dark red (#8b0000) with white text, same geometry. These two colors occupy completely different temperature zones, making the two badge types distinguishable at a glance without reading the label.

### Footer

**`footer`** — Near-black (#121212) inverted section that mirrors the hero's dark register, giving the page a closed bracket feeling. Link columns use Inter body-sm in white at 0.8 opacity; column headers use caption at full white with 0.5px letterspacing. The GLDN wordmark repeats at footer bottom in Spectral at small scale, white weight 300. No colored accents appear in the footer — the amber is reserved for above-the-fold actions.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; personalization panel drops below product images and loses sticky behavior; hero headline switches to display-lg (40px); nav collapses to hamburger + cart icon; charm selector becomes horizontal scroll row |
| Tablet | 744–1128px | Two-column product grid; personalization panel remains in right column at 40% width; hero shows truncated subhead; filter chips wrap into two rows |
| Desktop | 1128–1440px | Three-column product grid; full nav with category links visible; personalization panel sticky alongside 3-image product gallery; hero at full viewport height |
| Wide | > 1440px | Max content width 1440px with auto side margins; product grid stays at 3 columns with wider gutters; hero background extends full width but text block is capped at 700px |

### Touch Targets

- All interactive elements minimum 44×44px on mobile
- Charm selector tiles scale from 56px to 64px on mobile for easier tap precision
- Filter chips minimum 32px height with 12px horizontal padding maintaining legibility
- Nav bar hamburger zone is full left-quarter of the 60px bar height, not just the icon bounds

### Collapsing Strategy

- Personalization panel reflows below product images below 744px — sticky behavior removed to avoid fighting the mobile scroll model
- Footer link columns collapse from 4-column grid to 2-column on tablet, single accordion on mobile
- Collection filter chips collapse into a horizontal scrollable strip pinned beneath the nav on mobile rather than a sidebar
- Hero text hierarchy preserves headline + CTA on smallest breakpoint; subhead text is hidden below 480px via display:none (not opacity) to reclaim vertical space

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white (#ffffff) canvas color was not present in extraction; value is inferred from standard fine-jewelry Shopify conventions and noted as unconfirmed
- `primary-active` (#d4781e) and `primary-disabled` (#f4c48b) are derived from the extracted primary amber — not directly observed
- Exact Freight Sans Pro weight variants used per context (lights vs ultra vs standard) could not be confirmed from extraction; weights above reflect best inference from the font-stack order
- No meta theme-color was set, meaning mobile chrome bar color is system default — a missed brand touch on iOS Safari
- Hover and focus animation durations and easing curves were not extractable; 300ms ease assumed
- Whether Spectral is used at display sizes or only at editorial/editorial-adjacent scales is unconfirmed — condensed sans may dominate above-the-fold at breakpoints not observed
- Exact personalization panel layout (sticky column vs below-fold) confirmed only via product page description inference, not direct DOM inspection
