---
version: alpha
name: "Yamazaki Home"
source_url: "https://theyamazakihome.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The wire grid of a Yamazaki steel organizer becomes a design grammar for the whole site — thin strokes, orthogonal construction, surfaces that make no claim beyond their function. The palette runs almost entirely on a single gray axis from near-black #121212 through charcoal #4d4e55 and #75767e to soft-white #f5f5f5, with no decorative color until a single precision strike of #16c793 lands on every primary CTA, in-stock signal, and new-arrival badge. That green reads less like a brand color and more like a system status indicator — closer to a terminal confirmation than a lifestyle flourish — which suits a company that frames domestic storage as honest engineering rather than aspirational decor.

  Type makes the one editorial gesture: LibreBaskerville, a confident slab serif, governs display and editorial headings at 700 weight in deliberate contrast to Bio Sans running all UI copy, navigation, and button labels. The serif implies a domestic intelligence — the brand trusts its product logic enough to let a traditional face speak at scale without softening it. Bio Sans holds at 14–16px with weight 500–600, compact and never competing with product photography. Corners are uniformly sharp: {rounded.none} dominates buttons, inputs, and cards; {rounded.xs} appears only on status badges where the 4px radius distinguishes overlay from substrate.

  Layout is governed by wide breathing room and quiet hairline dividers at #dedede, product images settling on a #f5f5f5 groundplane. The mint-tinted well #dff3e7 pairs with #16c793 for availability and new-arrival states without raising visual temperature. #c33b31 covers error and sale-price contexts. The overall effect is a shop that organizes itself the same way its products organize a desk — every element in its lane, nothing decorative that isn't also functional.

colors:
  primary: "#16c793"
  primary-active: "#0fa878"
  primary-disabled: "#dff3e7"
  ink: "#121212"
  body: "#2b2b2b"
  muted: "#75767e"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-mid: "#e0e0e0"
  on-primary: "#ffffff"
  charcoal: "#4d4e55"
  accent-mint-bg: "#dff3e7"
  error: "#c33b31"
  footer-text: "#aaaaaa"
  scrim: "#202020"

typography:
  display-xl:
    fontFamily: "'LibreBaskerville', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'LibreBaskerville', Georgia, serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'LibreBaskerville', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Bio Sans', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Bio Sans', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Bio Sans', Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Bio Sans', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Bio Sans', Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  label-upper:
    fontFamily: "'Bio Sans', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Bio Sans', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  nav-link:
    fontFamily: "'Bio Sans', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "'Bio Sans', Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Bio Sans', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.charcoal}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
    padding: 0 32px
  nav-announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    typography: "{typography.caption}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    imageBackground: "{colors.surface-soft}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    captionTypography: "{typography.caption}"
    textColor: "{colors.ink}"
    mutedTextColor: "{colors.muted}"
    rounded: "{rounded.none}"
    imageBorderRadius: "{rounded.none}"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
    hoverShadow: "0 2px 12px rgba(0,0,0,0.08)"
  hero:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    padding: "{spacing.section} {spacing.xxl}"
    maxWidth: 1280px
    ctaStyle: button-primary
  badge-new:
    backgroundColor: "{colors.accent-mint-bg}"
    textColor: "{colors.primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  badge-in-stock:
    backgroundColor: "{colors.accent-mint-bg}"
    textColor: "{colors.primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    iconColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.charcoal}"
    rounded: "{rounded.none}"
    height: 40px
    padding: 0 12px
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    activeTextColor: "{colors.ink}"
    activeBorderColor: "{colors.charcoal}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  collection-filter-pill:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  pdp-price-block:
    priceTypography: "{typography.price-display}"
    comparePriceTypography: "{typography.price-sm}"
    priceColor: "{colors.ink}"
    comparePriceColor: "{colors.muted}"
    salePriceColor: "{colors.error}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.footer-text}"
    linkColor: "{colors.footer-text}"
    linkHoverColor: "{colors.surface-soft}"
    headingColor: "{colors.surface-soft}"
    headingTypography: "{typography.label-upper}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"

## Components

### Buttons

**`button-primary`** — A sharp-cornered 48px block in #16c793 with white Bio Sans 600 label at 14px and 0.5px letter-spacing. No border radius — the flush edge is consistent with the brand's grid-honest aesthetic. On hover, background steps to #0fa878; disabled state renders #dff3e7 fill with muted label, reusing the mint badge palette to reinforce the green's system-signal meaning. Fills available width in mobile cart and sticky add-to-cart bars; auto-width on desktop PDP.

**`button-secondary`** — Outlined 48px button with 1px #121212 border, white fill, ink label in Bio Sans 600. Used for secondary PDP actions (Add to Wishlist, Save, Share) and filter drawer confirm. No radius.

**`button-ghost`** — 1px #dedede border, transparent fill, #2b2b2b label in Bio Sans 600. Lower-hierarchy trigger for editorial modules, collection sort toggles, and inline filter controls where a full ink border would compete with surrounding content.

### Inputs

**`text-input`** — Sharp 48px input, 1px #dedede border stepping to #4d4e55 on focus with no box-shadow or glow. Placeholder at #75767e; entered text at #121212. Consistent throughout search, newsletter, and checkout fields — no variant border radius anywhere.

**`search-bar`** — Compact 40px variant with #f5f5f5 fill and a #75767e search icon. No border radius. On mobile, expands to a full-screen overlay with the input anchored at top and results scrolling beneath.

### Navigation

**`nav-bar`** — 64px white bar with a 1px #dedede underline. Bio Sans 500 nav-links at 14px, no text-transform; hover adds a thin #121212 underline. Logo left, cart/search/account icons right. Above it, `nav-announcement-bar` runs at 36px in #121212 with #f5f5f5 caption text for shipping thresholds and promotions. On mobile, collapses to hamburger + centered logo + cart icon.

### Product Cards

**`product-card`** — No border or drop-shadow at rest; the #f5f5f5 image container establishes visual containment. A 2px upward translate and 0 2px 12px rgba(0,0,0,0.08) shadow appear on hover. Title in Bio Sans 600 15px, price in Bio Sans 400 14px at #75767e (or #c33b31 for sale with compare-at strikethrough). Badge overlays (`badge-new`, `badge-sale`) pin to top-left of the image area. No border radius on card or image; image fills with object-fit: cover.

### Hero

**`hero`** — #f5f5f5 ground with headline in LibreBaskerville 700 at 48px, subhead in Bio Sans 400 16px at #75767e. `button-primary` CTA sits below with standard height and no radius. Desktop renders a two-column split — text left, product image right — at max-width 1280px. Mobile stacks text above image, preserving the CTA above the fold. 64px top and bottom padding gives the section room to breathe.

### Badges

**`badge-new`** — #dff3e7 background, #16c793 text in Bio Sans 600 11px uppercase at 1.2px letter-spacing, 4px corner radius. The mint-on-mint pairing with the primary button reinforces that green's role as the brand's only warm signal. **`badge-sale`** — #c33b31 fill, white text, same typographic treatment. **`badge-in-stock`** — #dff3e7 background, #16c793 caption-weight text, sharp corners; used inline in the PDP availability line beneath the price block.

### Collection Filters

**`collection-filter`** — Sharp-edged toggle button with 1px #dedede border. Inactive: #2b2b2b text on white; active: #121212 text with #4d4e55 border. Selected filters render as `collection-filter-pill` — a full #121212 capsule at {rounded.full} with white caption text and an inline × dismiss glyph. On mobile, filters collapse behind a sticky "Filter & Sort" bar; tapping opens a full-screen sheet.

### PDP Price Block

**`pdp-price-block`** — Sale price in #c33b31 at Bio Sans 600 18px; compare-at price in #75767e 14px with CSS `text-decoration: line-through`; regular price in #121212 at 18px 600. Stacked with 4px gap between lines. Availability badge sits immediately below the price stack.

### Footer

**`footer`** — #121212 background with a four-column link grid on desktop. Column headings in Bio Sans 600 11px uppercase at 1.2px letter-spacing, #f5f5f5; links in Bio Sans 400 14px at #aaaaaa with hover to #f5f5f5. No top border — the dark fill creates its own separation from the light storefront above. Newsletter input uses a borderless ghost field with only a white bottom rule, keeping the footer's editorial quiet.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger drawer + logo + cart icon; hero stacks text above image; product grid is 2-column; filter sidebar becomes a full-screen sheet triggered by a sticky bottom bar; footer accordion-collapses each link group; search expands to full-screen overlay |
| Tablet | 744–1128px | Product grid is 3-column; nav shows a partial link set; hero scales headline to display-md (32px); filter sidebar renders as a horizontal scrollable chip row above the grid |
| Desktop | 1128–1440px | Full 64px nav-bar; hero at 48px LibreBaskerville with side-by-side layout; product grid 4-column; filter sidebar pinned left at ~240px |
| Wide | > 1440px | Content max-width ~1280px centered; hero image allowed to extend into wider margins while text column stays constrained; grid remains 4-column with larger image aspect ratio |

### Touch Targets

- All buttons and interactive elements maintain a minimum 44×44px tap area
- Nav icons padded to 48px tap area regardless of rendered glyph size
- Collection filter chips padded to 44px minimum height on mobile
- Badge dismiss (×) icons padded to 32px tap area

### Collapsing Strategy

- Navigation: left-drawer slide with full category hierarchy and sub-menus as expandable rows
- Filters: hidden behind sticky "Filter & Sort" bottom bar; opens as full-screen bottom sheet with apply/clear controls
- Footer: each link group collapses behind a + toggle row; newsletter field remains persistently visible
- Hero: single-column stack with image below text; CTA remains above the fold at standard mobile viewport

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-active` (#0fa878) is derived by darkening the extracted #16c793 by approximately 15%; no interactive-state snapshot was available to confirm the live hover color
- "Brutal" appears in the font stack but its role is unconfirmed — it may be a display-weight variant loaded only for specific editorial modules or an unused theme remnant
- Inter / InterDisplay / InterVariable are present in the stack; their relationship to Bio Sans is not determined — likely Shopify theme fallbacks rather than brand-intentional choices
- Exact font weight availability for Bio Sans (whether 400/500/600/700 are all served) is not confirmed; design tokens assume standard weights
- Animation easing curves, transition durations, and scroll-triggered motion are not extractable from palette hints
- Icon set (category glyphs, wishlist heart, cart bag, account) not confirmed in stroke weight, size, or fill/outline style
- Checkout and cart drawer design tokens not captured — may deviate from storefront surface colors
- Grid gutter widths, column counts at edge breakpoints, and precise content max-width are inferred from Shopify conventions rather than confirmed from live layout inspection
