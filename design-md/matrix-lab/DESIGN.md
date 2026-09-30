---
version: alpha
name: "Matrix Lab"
source_url: "https://matrixlab.store"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Electric violet (#7737bd) sits at an unexpected frequency for a keyboard brand — most mechanical keyboard shops default to gamer-RGB overflow or the cold-grey minimalism of audiophile hardware, but Matrix Lab plants its flag on a single saturated purple that carries every primary CTA and active state while the rest of the palette holds its breath in near-black (#121212) and bone-grey neutrals (#a0a0a0, #b9b9b9, #dedede). The result is a system with genuine tension: a precise dark ink field interrupted by purple voltage rather than the expected cool blue or hot red. An indigo accent (#4c57c7) sits a half-stop cooler on the hue wheel, deployable for secondary CTAs and hover states where the primary purple would compete with itself. Type runs entirely on the system sans-serif stack — no proprietary typeface was detected — at modest weights that prioritize legibility on dense product specification tables and keycap layout diagrams; the brand trusts hardware photography over typographic showmanship. The layout philosophy leans into Shopify conventions but with heavier visual compression on product grids: keyboards reward dense comparison over editorial whitespace, so cards carry more metadata per unit of screen real estate than a typical DTC apparel brand. Rounded corners are conservative (`{rounded.sm}` to `{rounded.md}`), keeping the mechanical hardware feeling precise rather than soft. Surface greys (#f7f7f7, #f1f1f1, #e3e3e3) build a three-stop depth stack behind the dark ink, giving product photography a clean neutral stage without bleaching the entire layout white. The multiple blues extracted from the palette (#047bd5, #3086c8, #1e90ff, #003087, #012169, #2c5cc5) are almost certainly injected by Shopify payment provider widgets (PayPal navy, generic bank-blue anchor links) rather than brand tokens — the only blue-family color worth trusting as a genuine brand signal is the indigo accent (#4c57c7), which shares enough violet DNA with the primary purple to read as intentional.

colors:
  primary: "#7737bd"
  primary-active: "#5a2595"
  primary-disabled: "#c49de0"
  accent-indigo: "#4c57c7"
  accent-indigo-active: "#3644a8"
  ink: "#121212"
  body: "#565656"
  muted: "#989898"
  muted-soft: "#b9b9b9"
  hairline: "#dedede"
  hairline-soft: "#e3e3e3"
  hairline-lighter: "#f1f1f1"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f1f1f1"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#121212"

typography:
  display-xl:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  spec-label:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
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
    padding: 12px 24px
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
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 22px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
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
  nav-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
    fontWeight: 600
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspectRatio: "4/3"
    border: "1px solid {colors.hairline}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-meta:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subhead:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 28px
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sold-out:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-in-stock:
    backgroundColor: "#1a7a3c"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  spec-table:
    backgroundColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.sm}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: "{spacing.sm} {spacing.base}"
  color-swatch:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    borderActive: "2px solid {colors.primary}"
    outlineOffset: 2px
  keycap-option:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 6px 10px
    border: "1px solid {colors.hairline}"
    borderActive: "1px solid {colors.primary}"
    textColorActive: "{colors.primary}"
  product-filter-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: "{spacing.sm} 0"
  section-header:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  cart-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    width: 400px
    padding: "{spacing.lg}"
  cart-item-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  cart-item-price:
    typography: "{typography.body-sm}"
    textColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"

---

## Components

### Buttons

**`button-primary`** — The primary action carries the full #7737bd purple on a 44px-tall pill with `{rounded.sm}` corners, keeping it mechanical-precise rather than bubbly. Hover shifts to `{colors.primary-active}` (#5a2595), a noticeably darker violet that signals depth without needing a shadow. The disabled state washes out to `{colors.primary-disabled}` (#c49de0), retaining hue identity even at low affordance. Use for Add to Cart, Buy Now, and any single dominant CTA per viewport.

**`button-secondary`** — A transparent ghost button with a 2px solid purple border and purple label text, pairing with the primary on dual-CTA rows (e.g. "Add to Cart" + "Add to Wishlist"). On hover the fill floods to full primary purple and text flips to white, matching the primary button's resting state. Height is identical at 44px so the two buttons optically align in a row.

**`button-ghost`** — Borderless, transparent, used for low-priority actions like "View More", filter toggles, and pagination links. Inherits `{typography.button-sm}` at slightly smaller weight; corners are `{rounded.xs}` for a subtle contained feel.

### Navigation

**`nav-bar`** — 60px tall, white canvas, 14px medium-weight nav links that drop a 1px `{colors.hairline}` bottom border to separate from page content. The active link gains `{colors.primary}` purple with a weight bump to 600. On mobile the nav collapses into a hamburger; the drawer inherits the white background and lists links at `{typography.title-sm}` scale for generous touch targets.

### Product Card

**`product-card`** — Sits on `{colors.surface-card}` (#f1f1f1) rather than pure white, giving the grid a subtle tonal separation from the page canvas. A 1px `{colors.hairline}` border defines card edges; `{rounded.sm}` keeps corners crisp. Images use a 4:3 aspect ratio to accommodate top-down and three-quarter keyboard shots without letterboxing. Below the image: product title in `{typography.title-sm}`, price in `{typography.price-display}`, and a muted sub-line for variant summary (switch type, layout) in `{typography.body-sm}` at `{colors.muted}`. Badges (NEW, SOLD OUT) stack top-left over the image.

### Hero

**`hero`** — Full-bleed dark section using `{colors.ink}` (#121212) as background, giving product photography maximum contrast. The headline runs `{typography.display-xl}` in white; the subhead drops to `{typography.body-md}` at `{colors.muted-soft}` to create hierarchy without a second typeface. The CTA reuses `hero-cta` — identical to `button-primary` geometry but with slightly wider padding (12px 28px) to feel proportionate at hero scale. Minimum 480px height; on wide viewports it expands with the imagery.

### Badges

**`badge-new`** — Purple fill, white text, `{rounded.xs}` corners, uppercase 11px type at 0.3px tracking. Appears top-left on product card images, overlapping the photo by ~8px for energy. **`badge-sold-out`** — Muted grey fill (`{colors.hairline-soft}`) with `{colors.body}` text; same geometry, communicates unavailability without aggression. **`badge-in-stock`** — Dark green (#1a7a3c) fill, white text; used sparingly on restocked or limited-availability items to signal urgency.

### Spec Table

**`spec-table`** — Two-column definition table on `{colors.surface-soft}` with `{rounded.sm}` container. Left column renders property names via `{typography.spec-label}` (11px, 600 weight, uppercase, 0.5px tracking) in `{colors.muted}`; right column renders values in `{typography.body-sm}` in `{colors.ink}`. Row padding is `{spacing.sm} {spacing.base}`, separated by 1px `{colors.hairline}` rules. Keyboards require many spec rows (layout, switch, PCB, plate, weight, dimensions) so the compact row height is intentional.

### Keycap / Variant Options

**`keycap-option`** — Pill-like option chip on `{colors.surface-soft}` with 1px `{colors.hairline}` border and `{typography.caption}` label. When selected, the border switches to `{colors.primary}` and the label text turns `{colors.primary}` to reinforce selection without a background fill — prevents visual noise when 10+ switch types are listed. **`color-swatch`** — 24px circle for colorway selection; a 2px `{colors.primary}` outline appears on the active swatch with 2px offset, so the swatch color remains fully visible inside the selection ring.

### Announcement Bar

**`announcement-bar`** — Full-width strip above the nav in `{colors.primary}` purple with centered white body-sm text. Carries shipping thresholds, sale codes, or launch announcements. No close button by default to preserve message visibility; can be scrolling ticker on mobile.

### Cart Drawer

**`cart-drawer`** — 400px right-side panel on a white canvas with a 1px left border in `{colors.hairline}`. Item names use `{typography.title-sm}`; prices and variant labels use `{typography.body-sm}` at `{colors.body}`. The checkout CTA at the bottom of the drawer is `button-primary` full-width. On mobile the drawer becomes a full-screen bottom sheet.

### Footer

**`footer`** — Dark `{colors.ink}` background, `{colors.muted-soft}` body text, and `{colors.hairline}` link color — links are intentionally low-contrast against the dark field, signaling utility rather than invitation. Column grid collapses to a single accordion stack on mobile. Logo sits top-left in white.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline drops to `display-md` scale; spec table scrolls horizontally; keycap options wrap freely; cart drawer becomes full-screen bottom sheet |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links, secondary links in dropdown; hero maintains two-column image+text split; filter bar collapses to a "Filters" button opening a modal tray |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with mega-dropdown for category depth; hero at full 480px min-height; spec table in fixed two-column layout beside product images |
| Wide | > 1440px | Max-width container (~1400px) centered with canvas gutters; product grid locks at four columns; hero image expands within a fixed-height viewport frame to avoid excessive crop |

### Touch Targets

- All interactive buttons, swatches, and keycap option chips target a minimum 44×44px touch area; the visual chip may be smaller with invisible padding
- Nav links in the mobile drawer use `{spacing.lg}` (24px) vertical padding per row for reliable thumb reach
- Color swatches are 24px visual diameter but wrapped in a 40px invisible touch zone
- Add-to-cart and checkout CTAs span full container width on mobile to maximize tap area

### Collapsing Strategy

- Navigation: horizontal nav → hamburger icon + full-height side drawer (left-to-right slide-in) at < 744px
- Product grid: 4-col → 3-col at 1128px → 2-col at 744px → 1-col at < 480px
- Spec table: at < 744px, spec table switches to a single-column stacked layout (label above value) rather than side-by-side to prevent horizontal scroll inside the product detail accordion
- Filter bar: at < 1128px, filters collapse into a sticky "Filter & Sort" pill button that opens a bottom modal tray; active filter count shown as a purple badge on the pill
- Hero: stacks headline above image at < 744px; image moves to top, text below with reduced padding

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom font detected — the site delivers only `sans-serif` as the font stack, meaning either a custom font loads via JS after extraction, is served as a self-hosted asset not visible in static CSS, or no custom typeface is in use. All typography tokens use the system-ui stack as a safe fallback.
- No explicit dark-mode token split was extractable; `{colors.ink}` (#121212) appears in both hero backgrounds and text contexts — a full dark/light token split would need live DOM inspection.
- The indigo accent (#4c57c7) appears in the extracted palette but its exact usage context (hover states, secondary buttons, links, or section accents) could not be confirmed from static extraction alone.
- Multiple blues (#047bd5, #3086c8, #1e90ff, #003087, #012169, #2c5cc5) are almost certainly Shopify payment provider injections (PayPal, bank links) rather than brand tokens — none have been incorporated as brand colors.
- No icon system or illustration style could be extracted; keyboard brand icon sets (switch diagrams, layout icons, PCB schematics) likely exist but are not reflected here.
- Hover/focus animation durations and easing curves could not be extracted — transition values in components are left unspecified.
- Sale price color (typically a red or orange for strikethrough pricing) was not extractable; a semantic `status-error` or `price-sale` token may be needed.
- Product photography style (studio white vs. lifestyle vs. technical detail) could not be confirmed from palette extraction alone.
