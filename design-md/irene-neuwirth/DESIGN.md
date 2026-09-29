---
version: alpha
name: "Irene Neuwirth"
source_url: "https://www.ireneneuwirth.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The extracted palette reads like a gem tray laid on white linen — a deep plum-mauve (#8e5c84) beside warm amber (#feaf3f), with flashes of burnt orange (#b74305), deep red (#b22c29), and ocean blue (#0073a2) that mirror the tourmalines, padparadschas, and sapphires Neuwirth hand-sets at her Los Angeles studio. Color is the central argument of the brand, not an accent to precious metal: each piece is designed around the stone, and the UI reflects that logic. Muted neutrals — a light silver-gray (#dedede) hairline, near-black (#121212) ink — function as the white-gold setting that lets gemstone hues breathe without competition. The handmade provenance is front-loaded in the page title itself ("Handmade Fine Jewelry Los Angeles"), establishing craft and geography before any product is shown. Navigation stays minimal and typographically spare — all-caps, generously tracked sans-serif at small scale — directing all visual energy toward editorial photography where organic color does the persuasion. Button shapes favor a subtly rounded edge (`{rounded.sm}`) rather than pill or sharp rectangle, landing at the deliberate middle ground between fine-jeweler's restraint and contemporary e-commerce warmth. The amber (#feaf3f) acts as the brand's equivalent of a gold bezel catch — a warm, deliberate accent deployed on featured CTAs and collection badges against the cooler neutral field. Product cards lean on large-format 4:5 imagery shot against skin or stone rather than a white float, letting the organic gemstone color key the entire visual register. Spacing is generous at the section level (`{spacing.section}`) to give each collection editorial breathing room. Display type is set in a classical serif — atelier register, zero flash — while body copy shifts to a clean sans-serif for legibility on material descriptions and care instructions. The result is a site that behaves less like a storefront and more like a gallery walk-through, where the product is always the focal point and the UI recedes to let color and craft speak.

colors:
  primary: "#8e5c84"
  primary-active: "#6e4464"
  primary-disabled: "#c9a8c5"
  accent-amber: "#feaf3f"
  accent-amber-active: "#d98e1a"
  accent-blue: "#0073a2"
  accent-red: "#b22c29"
  accent-orange: "#b74305"
  ink: "#121212"
  body: "#2e2e2e"
  muted: "#6b6b6b"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f9f7f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.02em
  display-lg:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  display-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.01em
  display-sm:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  title-md:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.54
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0.05em
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.12em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.36
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.10em
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.02em
  collection-label:
    fontFamily: "Georgia, 'Times New Roman', serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0.06em
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
    rounded: "{rounded.sm}"
    padding: 14px 32px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 44px
    border: "1px solid {colors.ink}"
  button-amber:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageAspectRatio: "4/5"
    rounded: "{rounded.none}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    textAlignment: center
    padding: "{spacing.section} {spacing.xl}"
  collection-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-md}"
    labelTypography: "{typography.collection-label}"
    textColor: "{colors.ink}"
  gem-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  stone-filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    border: "1px solid {colors.hairline}"
  stone-filter-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 16px
  product-detail-panel:
    backgroundColor: "{colors.canvas}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    priceTypography: "{typography.price}"
    textColor: "{colors.ink}"
    padding: "{spacing.xl}"
  search-drawer:
    backgroundColor: "{colors.canvas}"
    inputTypography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
  atelier-tag:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.title-sm}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The primary CTA fills with plum-mauve (#8e5c84) and white all-caps type set at 12px with 0.12em tracking — sparse enough to feel jeweler-calibrated rather than mass-market. Shape is `{rounded.sm}` (4px): not a pill, not a hard rectangle, but a subtly dressed edge. Active state deepens to #6e4464; disabled washes to #c9a8c5.

**`button-amber`** — A warm amber (#feaf3f) variant is deployed on editorial CTAs ("Shop the Collection", "Explore Stones") and promotional banner links, echoing the gold of Neuwirth's settings. Text renders in near-black (#121212) for legibility. On hover the amber deepens to #d98e1a with no shape change.

**`button-secondary`** — White fill with a 1px ink border and identical uppercase type treatment. Surfaces on PDP for secondary actions — "Inquire About This Piece", "Request Custom" — where the primary slot is held for add-to-cart. Active state inverts to ink fill and white text.

### Navigation

**`nav-bar`** — A 72px white bar with all-caps 12px nav links spaced at 0.10em. Logo centered on mobile, left-aligned on desktop. A hairline bottom border (#dedede) separates the bar from editorial content without adding visual weight. No megamenu: each collection is a direct link, keeping the navigation as minimal as the jewelry's negative space.

### Product Card

**`product-card`** — Flush-edge 4:5 ratio imagery with no card border-radius. Title renders in `{typography.title-md}` Georgian serif; price below in `{typography.price}`. The card carries zero rounding — organic jewelry photography supplies the softness. On hover, a secondary image (alternate angle or stone macro) swaps in; no UI overlay is added.

### Hero

**`hero`** — Full-width editorial frame on `{colors.surface-soft}`, headline in `{typography.display-xl}` at 42px serif, subhead in `{typography.body-md}`. Text is center-aligned with `button-amber` CTA below. On wide viewports the layout splits: type left at ~45% width, full-bleed stone or model image right — no text overlay on the image half.

### Collection Banner

**`collection-banner`** — Opens each named collection (Rainbow, Opal, Turquoise) with a small all-caps category label in `{typography.collection-label}` above a 24px serif headline. Background is `{colors.surface-soft}`, consistent with the warm off-white of studio photography. No decorative rules or ornamental dividers — the collection name alone carries the frame.

### Badges

**`gem-badge`** — Amber pill (`{rounded.full}`) for stone-type callouts ("Tourmaline", "Opal", "Sapphire") on editorial cards and product tiles. Fills with `{colors.accent-amber}`, type in `{colors.ink}`. **`new-badge`** uses `{colors.primary}` fill with white type, same pill shape, flagging new arrivals and limited editions.

### Stone Filter Pills

**`stone-filter-pill`** — On collection pages, gemstone-type and metal filters surface as horizontally scrolling pill rows. Inactive: white fill, `{colors.hairline}` border, muted body text. Active: `{colors.primary}` fill, white type. This is the primary discovery affordance on mobile, allowing rapid filtering by stone type — a pattern that directly reflects how Neuwirth's customers shop.

### Product Detail Panel

**`product-detail-panel`** — Right-hand panel on desktop, full-width stacked block on mobile. Title in `{typography.display-sm}` serif, price in `{typography.price}`, material and stone description in `{typography.body-md}`. One-of-a-kind pieces replace "Add to Cart" entirely with an "Inquire" flow — a significant UI branch that affects CTA layout and button hierarchy on a meaningful portion of the catalog.

### Search Drawer

**`search-drawer`** — Full-width overlay triggered from the nav, single centered input field with `{rounded.xs}` border at rest switching to `{colors.ink}` outline on focus. Recent searches and featured collections appear as text links below the input. Dismissed on Escape or outside-click; no animation beyond a simple fade.

### Atelier Tag

**`atelier-tag`** — A small `{colors.muted}` provenance mark reading "Handmade in Los Angeles" set in `{typography.title-sm}` all-caps. Appears on PDP below the price and on selected editorial pages. No fill, no border — purely typographic, receding enough to read as factual rather than promotional.

### Footer

**`footer`** — Near-black (#121212) background with hairline-toned link text. Four-column layout on desktop (Collections, About, Service, Subscribe); stacked single column on mobile. Email capture uses a `{colors.on-dark}` text input with a hairline underline treatment rather than a boxed field. Legal links and address in `{typography.body-sm}` at reduced opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; stone filter pills scroll horizontally; nav collapses to hamburger + centered logo; hero goes full-bleed with text stacked above image; PDP image above, detail panel below |
| Tablet | 744–1128px | Two-column product grid; nav links visible if ≤ 5 items, otherwise hamburger; hero splits 50/50 text and image |
| Desktop | 1128–1440px | Three-column product grid; full nav bar; PDP uses 60/40 image-to-panel split; collection banners use left-text, right-image side-by-side |
| Wide | > 1440px | Container max-width ~1440px centered; four-column grid on major collection pages; hero image expands without stretching type block |

### Touch Targets

- Stone filter pills minimum 44px tall via 8px vertical padding
- Nav hamburger icon minimum 44×44px hit area
- Product card tap target spans full card including image — no inset dead zone
- Primary and secondary PDP buttons full-width on mobile, minimum 44px height
- Badge pills minimum 32px tall for comfortable secondary taps

### Collapsing Strategy

- Product grid: 1 col (mobile) → 2 col (tablet) → 3 col (desktop) → 4 col (wide, major collections only)
- Stone filter row: horizontal scroll single-row on mobile, wraps to two rows on tablet, full horizontal bar on desktop
- Hero: stacked text-above / image-below on mobile, side-by-side split on tablet+
- Footer: single column on mobile, 2-col on tablet, 4-col on desktop
- Editorial side-by-side sections: image-above, text-below on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families were extracted from the live site — the brand likely loads custom typefaces via Shopify theme JS or a hosted font service. The Georgia serif / Helvetica Neue sans pairing above is inferred from fine-jewelry atelier conventions and must be verified against the live stylesheet before use.
- Meta theme-color was absent; mobile browser chrome color for iOS Safari and Android is unconfirmed.
- Exact button border-radius and padding values were not capturable; `{rounded.sm}` (4px) is an inference from the minimal aesthetic.
- The UI role of the accent colors (#0073a2 blue, #b74305 orange, #b22c29 red) is ambiguous — these may be editorial/photography colors exclusive to homepage imagery rather than active UI tokens. Confirm before applying to interactive elements.
- No hover transition durations or easing functions were captured; fine jewelry brands typically use 200–300ms ease transitions on image swaps and color state changes.
- Shopify platform confirmed but specific theme (Dawn, custom, third-party) was not identified, limiting confidence on default grid gutter widths and container breakpoint values.
- Inquire/waitlist flow for one-of-a-kind pieces — its visual treatment (modal, inline form, redirect) was not determinable from extraction.
