---
version: alpha
name: "Mignonne Gavigan"
source_url: "https://www.mignonnegavigan.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Handwoven threads meet a palette that pulls no punches — the brand's signature marigold gold (#ffc863) shows up where other jewelry brands would settle for tasteful beige, landing as the primary CTA color, the hover glow, and the ambient warmth that ties the artisan credential to the checkout flow. The canvas oscillates between near-whites — #f1f1f1 and #f3f3f3 — surfaces that read less like background and more like the clearing a jeweler makes before laying out a collection. Against this field, #121212 grounds all typography with enough density to make serif display lines land cleanly, and a secondary jolt of electric yellow (#ffff00) fires on sale badges and flash moments, giving the two-tone energy system a vibrancy that matches the brand's handmade, maximalist product sensibility.

  Type is split across two registers that mirror the brand's own duality. Gilda Display — a serif with long calligraphic ascenders and classical engraving lineage — handles the editorial layer: hero headlines, collection titles, featured product callouts. Instrument Sans runs the functional tier: navigation, body copy, button labels, and price strings. The combination puts craft and precision in dialogue, the same conversation the physical objects have between seed bead and brass hardware.

  Corners are restrained but not sharp: primary buttons and product cards take `{rounded.sm}` to read as polished rather than severe, while filter chips and badges adopt `{rounded.full}` for the playful, accessory-adjacent energy they need to signal quickly. The `{rounded.none}` edge appears almost exclusively in full-bleed editorial photography, where zero containment lets the product breathe.

  The signature scarf necklace is the photogenic core of the entire shop, and the product card reflects that priority: a 3:4 portrait ratio, minimal UI chrome, and a hover swap to secondary imagery rather than a carousel gesture, keeping the handmade object in focus rather than the interface that frames it. Generous horizontal padding on CTAs (28px each side) gives the marigold button enough presence to function as a compositional element, not merely a conversion widget.

colors:
  primary: "#ffc863"
  primary-active: "#e6a83a"
  primary-disabled: "#ffe4a8"
  accent-flash: "#ffff00"
  ink: "#121212"
  body: "#2e2e2e"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f1f1f1"
  surface-card: "#f3f3f3"
  on-primary: "#121212"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Gilda Display', 'freight-display-pro', Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Gilda Display', 'freight-display-pro', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Gilda Display', 'freight-display-pro', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.06em
    textTransform: uppercase
  body-md:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  price:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  price-sale:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  button-md:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Instrument Sans', system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.05em
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    priceColor: "{colors.ink}"
    priceSaleColor: "{colors.primary-active}"
    imageRounded: "{rounded.xs}"
    titleTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    salePriceTypography: "{typography.price-sale}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.sm}"
    imageAspectRatio: "3/4"
    hoverBehavior: swap-to-secondary-image
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    minHeight: 580px
    layout: split-image-text
    imageRounded: "{rounded.none}"
  collection-header:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    descriptionTypography: "{typography.body-md}"
    borderBottom: "1px solid {colors.hairline}"
    paddingBottom: "{spacing.lg}"
  badge-sale:
    backgroundColor: "{colors.accent-flash}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 18px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  scarf-feature-block:
    backgroundColor: "{colors.canvas}"
    imageAspectRatio: "2/3"
    imageRounded: "{rounded.none}"
    headlineTypography: "{typography.display-sm}"
    captionTypography: "{typography.caption}"
    accentUnderlineColor: "{colors.primary}"
    layout: alternating-two-column
    columnGap: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    border: none
    padding: 10px 16px
    height: 40px
  editorial-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    height: 40px
    layout: marquee-or-centered-text
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — Marigold gold (#ffc863) on near-black text: the primary button is the single loudest element in any layout it occupies, sized at 48px tall with 28px horizontal padding so the gold bar reads as a compositional block rather than an afterthought. Active state deepens to #e6a83a; disabled washes out to #ffe4a8 with muted text. All three states share `{rounded.sm}` and the tracked uppercase `{typography.button-md}` label, keeping the button family visually coherent across states.

**`button-secondary`** — White fill with a 1px #121212 border and the same 48px height as the primary, providing a visually matched alternative for add-to-wishlist, share, or secondary collection CTAs. Hover behavior shifts the border and label to `{colors.primary}` rather than inverting fill, keeping the primary button's gold ownership intact.

**`button-ghost`** — Transparent background with an underline on the label text; used for "see all," "learn more," and editorial link-outs where a bordered or filled button would overpower the surrounding content.

### Inputs

**`text-input`** — Light canvas fill, 1px `{colors.hairline}` border that steps to `{colors.ink}` on focus; no colored focus ring, consistent with the brand's low-chromatic-interference aesthetic. At 48px tall with `{rounded.xs}` it aligns flush with button heights in side-by-side form layouts (email signup, account creation). Placeholder text renders at `{colors.muted}`.

**`search-bar`** — Floats on `{colors.surface-soft}` fill with no visible border, keeping it visually subordinate to the nav-bar. Height drops to 40px to fit within the header row without crowding category links. Focus state adds a 1px `{colors.hairline}` border rather than a bold outline to avoid disrupting the pale nav canvas.

### Navigation

**`nav-bar`** — 64px tall, white canvas, bottom-bordered with a barely-visible `{colors.hairline-soft}` rule. Navigation links use `{typography.nav-link}` — 13px, tracked uppercase Instrument Sans — giving the top level the structured feel of a boutique retailer. On desktop, a centered logo sits between left-anchored category links and right-anchored cart, search, and account icons. An editorial strip (`editorial-strip`) sits above the nav, running promotional messaging or free-shipping thresholds in tracked uppercase on the marigold `{colors.primary}` background.

### Product Card

**`product-card`** — A 3:4 portrait ratio prioritizes the drape and dimension of scarf necklaces and earring clusters over square thumbnail conventions. Background is `{colors.surface-card}` (#f3f3f3) for a soft lift off the page canvas. On hover, the card swaps to a secondary product image rather than zooming or overlaying UI — the interaction stays visual, not mechanical. Product title renders in `{typography.body-sm}` and price in `{typography.price}`; sale prices step to `{typography.price-sale}` in a darker warm tone. Badges (`badge-sale`, `badge-new`) float in the top-left corner of the image at `{rounded.full}`.

### Hero

**`hero-editorial`** — A split-image-text layout at a minimum 580px tall: full-bleed photography on one side (no rounding, bleeds to container edge) with a text panel on the other, padded generously. The headline uses `{typography.display-xl}` in Gilda Display at 56px; the subhead drops to `{typography.body-md}` in Instrument Sans. A single `button-primary` CTA anchors the bottom of the text panel. The surface-soft (#f1f1f1) background of the text panel reads as distinct from the page canvas (#ffffff) without introducing a hard color block.

### Collection & Filtering

**`collection-header`** — Collection landing pages open with a `{typography.display-md}` headline in Gilda Display (36px) above an optional description paragraph in `{typography.body-md}`. A thin `{colors.hairline}` rule separates the header from the product grid below. Filter chips (`filter-chip`) sit immediately below, horizontal-scrollable on mobile; active filters invert to `{colors.ink}` fill with white text (`filter-chip-active`).

### Signature Feature Block

**`scarf-feature-block`** — An alternating two-column module that spotlights individual hero products — particularly scarf necklaces — with a 2:3 portrait image on one side and editorial copy on the other. Columns alternate left-right across repeated instances. The headline uses `{typography.display-sm}` (24px Gilda Display); a thin marigold underline accent (`{colors.primary}`) can run beneath the product name to connect editorial and product identity. No rounded corners on images; the clean edge reinforces a gallery rather than a storefront.

### Footer

**`footer`** — Near-black (#121212) fill reverses all text and links to `{colors.on-dark}`. Column headings use `{typography.title-sm}` (13px tracked uppercase Instrument Sans); link lists use `{typography.body-sm}`. The dark footer creates a definitive visual terminus that frames the page and lets the marigold or flash-yellow accents from upper page elements read with full contrast in retrospect.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + cart; hero stacks image above text panel; filter chips scroll horizontally; scarf feature block stacks image above copy |
| Tablet | 744–1128px | Two-column product grid; nav may show abbreviated categories with a "more" overflow; hero maintains split layout at reduced image proportion; filter chips wrap |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all categories visible; hero at full 580px min-height; scarf feature block at 50/50 column split |
| Wide | > 1440px | Max-width container (~1440px) centers with canvas margins; product grid caps at four columns; editorial strip text remains centered |

### Touch Targets

- All interactive elements meet 44px minimum touch height on mobile; nav icon buttons pad to 44×44px hit area
- Filter chips pad to 40px height on mobile even if visual size is smaller
- Product card hover swap behavior becomes a tap-to-reveal secondary image on touch devices
- Cart, search, and account icons in mobile nav use 48px tap targets

### Collapsing Strategy

- Navigation: full horizontal links → hamburger drawer (links in stacked list at 18px, no uppercase tracking on mobile for legibility)
- Hero: side-by-side split → full-width image stacked above text block; headline drops from 56px to 36px (`{typography.display-md}`)
- Scarf feature block: alternating two-column → single column, image always above copy regardless of original alternation order
- Footer: multi-column grid → single stacked column with accordion toggles per section heading

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; browser chrome accent color for mobile Safari/Chrome is unconfirmed
- Only six hex values extracted — shadow tokens, overlay scrim opacity, and focus-ring colors are inferred from category conventions, not observed
- freight-display-pro appears in the font stack but its usage split with Gilda Display at specific breakpoints or component levels is unconfirmed
- Exact nav-bar height and logo dimensions were not confirmed from live extraction; 64px is an estimate consistent with Shopify brand store patterns
- Animation/transition durations (hover image swap timing, filter chip transitions) are not captured — recommend 200–250ms ease-out as a starting point
- Whether #ffff00 is a permanent sale color or a seasonal/campaign accent could not be confirmed from a single extraction snapshot
