---
version: alpha
name: "Rise Art"
source_url: "https://www.riseart.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The artwork owns every pixel — Rise Art's gallery-white canvas recedes so completely that the only thing with visual weight is the art itself. Primary actions arrive in a concentrated red (approximately #e8262a based on observed brand materials), a deliberate interruption in an otherwise monochrome field that functions the way a gallerist's hand gesture does: decisive, never decorative. Typography falls to Arial and neutral sans-serif stacks, kept light-weight at body level so that editorial content — curator notes, artist profiles, medium descriptions — reads as curatorial voice rather than commerce noise. Cards present artwork with near-zero chrome: a thin `{rounded.xs}` corner, a hairline border in `{colors.hairline}`, artist name in `{typography.caption}` below the image, and price flush-right in `{typography.title-sm}`. The proportions are orthodox white-cube — each artwork tile gets generous breathing room through `{spacing.xxl}` gutters, and the grid collapses gracefully rather than squeezing. The nav sits in a thin horizontal band at `{colors.canvas}`, with the Rise Art logotype left-anchored and a compact suite of links — Curated Collections, Artists, Sell Art — rendered in `{typography.nav-link}` weight 500, never bold. Search is a lightweight text field, not a pill or hero bar, signaling that discovery here is browsing and editorial rather than keyword retrieval. Badges appear in two flavors: a muted `{colors.surface-soft}` chip for "Limited Edition" and a sharp `{colors.primary}` fill for "New Arrival," both in `{typography.badge}` uppercase. Footer divides into four editorial columns — About, Artists, Support, Legal — on `{colors.ink}` background with reversed `{colors.on-dark}` text, a hard tonal inversion that closes the gallery-white experience like a colophon page.

colors:
  primary: "#e8262a"
  primary-active: "#c01e22"
  primary-disabled: "#f4adaf"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  muted-soft: "#999999"
  hairline: "#e0e0e0"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  badge-limited: "#f0f0f0"
  badge-limited-text: "#333333"
  badge-new: "#e8262a"
  badge-new-text: "#ffffff"
  price-accent: "#1a1a1a"
  curator-label: "#666666"

typography:
  display-xl:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  price-display:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  artist-name:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  editorial-label:
    fontFamily: "Arial, 'Helvetica Neue', Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.2px
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
    padding: 14px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 44px
  button-text-link:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    textDecoration: underline
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    padding: "0 {spacing.xl}"
  nav-bar-logo:
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
  nav-bar-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: "10px {spacing.base}"
    height: 44px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: "10px {spacing.base}"
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline-soft}"
    imageProportion: "4/3"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
  product-card-artist:
    textColor: "{colors.muted}"
    typography: "{typography.artist-name}"
  product-card-title:
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
  product-card-price:
    textColor: "{colors.price-accent}"
    typography: "{typography.price-display}"
  product-card-badge:
    typography: "{typography.badge}"
  hero-editorial:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    subtitleColor: "{colors.muted}"
    padding: "{spacing.section} {spacing.xxl}"
    maxWidth: 720px
  hero-split:
    layout: "50/50 image left, text right"
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
  badge-limited-edition:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.badge-limited-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  badge-new-arrival:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.badge-new-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  section-label:
    textColor: "{colors.curator-label}"
    typography: "{typography.editorial-label}"
    marginBottom: "{spacing.lg}"
  curator-strip:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.muted}"
    padding: "{spacing.section} {spacing.xxl}"
  artist-card:
    backgroundColor: "{colors.canvas}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    avatarShape: "{rounded.full}"
    nameTypography: "{typography.title-sm}"
    metaTypography: "{typography.caption}"
    metaColor: "{colors.muted}"
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 14px"
  medium-nav-tab:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    activeUnderline: "2px solid {colors.primary}"
    typography: "{typography.nav-link}"
    padding: "12px {spacing.base}"
  price-range-slider:
    trackColor: "{colors.hairline}"
    fillColor: "{colors.ink}"
    thumbColor: "{colors.ink}"
    thumbSize: 16px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.on-dark}"
    mutedColor: "#999999"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.editorial-label}"
    padding: "{spacing.section} {spacing.xxl}"
    columns: 4

## Components

### Buttons
**`button-primary`** — A flat, sharp-cornered rectangle with no border radius, filled in Rise Art red (`{colors.primary}`) and set in all-caps `{typography.button-md}` with 0.5px letter-spacing. The squared geometry echoes institutional print signage rather than consumer e-commerce softness. On hover it deepens to `{colors.primary-active}`; disabled state washes to `{colors.primary-disabled}` while keeping text white. Height is fixed at 44px so paired inputs and buttons align to the same baseline.

**`button-secondary`** — Same sharp geometry and uppercase type, but canvas white with a 1px `{colors.ink}` border. Used for secondary actions on artwork pages ("Add to Wishlist", "Request More Info"). The border treatment keeps it visually present on the white gallery canvas without competing with a primary action.

**`button-text-link`** — Inline underline-only link in `{colors.primary}` at `{typography.body-sm}`. Appears inside editorial copy ("View Artist Profile") and keeps the page from accumulating button chrome in long-form content zones.

### Navigation
**`nav-bar`** — A minimal 60px horizontal band at `{colors.canvas}` with a single `{colors.hairline}` bottom border. The logotype sits left in `{typography.title-md}` weight, primary nav links are centered in `{typography.nav-link}`, and a compact "Get Art Advice" or "Start Collecting" CTA button (`{components.nav-bar-cta}`) anchors the right. The nav collapses on mobile to a hamburger that reveals a full-height drawer over `{colors.canvas}`.

### Product Card
**`product-card`** — The foundational browse unit: a 4:3 artwork image fills the top with zero padding, followed by a tight metadata block. Artist name appears first in `{typography.artist-name}` at `{colors.muted}`, then artwork title in `{typography.caption}` at `{colors.ink}`, then price in `{typography.price-display}` flush-left. Cards use a 1px `{colors.hairline-soft}` border and `{rounded.xs}` corners — enough to lift off the canvas without interrupting the gallery grid rhythm. Badges (`{components.badge-limited-edition}` or `{components.badge-new-arrival}`) overlay the image at top-left.

### Badges
**`badge-limited-edition`** — Flat chip in `{colors.badge-limited}` (light gray) with dark text, uppercase 10px lettering at 0.8px tracking. Signals scarcity without urgency — matches the curatorial register. **`badge-new-arrival`** — Same shape and type treatment but filled `{colors.primary}` red with white text: the one component where Rise Art breaks the monochrome field to signal freshness.

### Editorial Hero
**`hero-editorial`** — Full-width white section with a large, light-weight heading in `{typography.display-xl}` (fontWeight 300) sitting above a single paragraph of `{typography.body-md}` in `{colors.muted}`. Maximum content width 720px, centered. No background images, no overlaid text — the editorial voice stands alone before the artwork grid begins below it.

### Section Labels
**`section-label`** — All-caps 11px label in `{typography.editorial-label}` at `{colors.curator-label}`, 1.2px letter-spacing, used above every content section ("CURATED COLLECTIONS", "FEATURED ARTISTS", "RECENTLY ADDED"). Functions as a chapter marker in the editorial page rhythm.

### Filter System
**`filter-chip`** and **`filter-chip-active`** — Pill-shaped chips (unlike the square buttons) that live in the browse sidebar and horizontal filter bar. Inactive state: white fill with `{colors.hairline}` border. Active state: `{colors.ink}` fill with white text. The pill shape distinguishes filter affordances from action buttons, which are always squared.

**`medium-nav-tab`** — Horizontal underline-tab row for browsing by medium (Painting, Photography, Print, Sculpture). Active tab gets a 2px `{colors.primary}` underline and `{colors.ink}` text; inactive tabs sit in `{colors.muted}`. Padding is 12px vertical so the touch target meets 44px minimum with the tab bar container height.

### Curator Strip
**`curator-strip`** — Off-white (`{colors.surface-soft}`) full-width section used for "Why Rise Art" and onboarding callouts. Title in `{typography.display-sm}`, body in `{typography.body-sm}` at `{colors.muted}`, with a `{components.button-primary}` CTA centered below. Provides textural break between artwork grid sections without introducing color.

### Artist Card
**`artist-card`** — Portrait-orientation card with a circular avatar (`{rounded.full}`), artist name in `{typography.title-sm}`, and a one-line nationality/medium descriptor in `{typography.caption}` at `{colors.muted}`. Used in "Artists to Watch" carousels. The thin `{colors.hairline}` border keeps it distinct from the white background without shadow.

### Footer
**`footer`** — Four-column layout on `{colors.ink}` background with `{colors.on-dark}` text. Column headings in `{typography.editorial-label}` uppercase, links in `{typography.body-sm}`. The dark footer provides definitive page closure and ensures trust signals (payment icons, press logos) are legible on a single dark canvas rather than floating on white.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column artwork grid; nav collapses to hamburger drawer; filter chips shift to a scrollable horizontal strip above grid; hero type drops to `{typography.display-sm}`; `{spacing.base}` horizontal margins |
| Tablet | 744–1128px | Two-column artwork grid; nav shows logo + hamburger (no inline links); filter sidebar collapses into a "Filter" drawer button; hero at `{typography.display-md}` |
| Desktop | 1128–1440px | Three-column artwork grid; full nav bar with inline links and CTA; filter sidebar visible left of grid; hero at full `{typography.display-xl}` |
| Wide | > 1440px | Grid expands to four columns; content well max-width ~1280px centered; section padding grows via `{spacing.section}` multiples |

### Touch Targets
- All filter chips minimum 36px height; pill padding ensures 44px on mobile via container
- `button-primary` and `button-secondary` fixed at 44px height on all breakpoints
- `medium-nav-tab` row sits in a 48px container on mobile
- Artist card and product card tap areas cover the full card, not just title text

### Collapsing Strategy
- Filter sidebar hides at tablet and below; a sticky "Filter & Sort" bar slides in above the grid
- Nav links collapse fully at tablet; hamburger drawer uses full-height overlay at `{colors.canvas}`
- Hero editorial section stacks image and text vertically on mobile (split hero becomes stacked)
- Footer four-column grid collapses to two columns on tablet, single column on mobile
- Artwork grid never drops below one column; minimum card width ~280px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **No hex colors extracted** — the site appears to load design tokens via JavaScript or behind anti-bot protection; all colors in this file are derived from observed brand materials and general knowledge, not extraction. Treat as approximate and verify against live site before shipping.
- **Primary red value uncertain** — `#e8262a` is an approximation based on observed Rise Art brand usage; the exact value may differ (possible range #cc2027–#e8262a). Verify with eyedropper on live CTAs.
- **Font stack unconfirmed** — only `Arial` was found in extraction, almost certainly a system fallback. Rise Art likely loads a custom or licensed typeface (possibly Gill Sans, GT Walsheim, or a bespoke sans) via JS. The Arial stack here is a safe fallback only.
- **Dark mode / theming** — no evidence of dark mode tokens from extraction; none specified here.
- **Icon system** — Rise Art uses a small icon set for wishlist, zoom, share, and nav. Glyph style (outline vs. filled, stroke weight) could not be confirmed from extraction.
- **Animation and hover transitions** — card hover lift, image zoom-on-hover, and transition durations are not captured; assume 200ms ease for interactive states.
- **Exact nav height and border weight** — 60px nav height and 1px hairline are estimates based on visual inspection conventions for gallery sites; confirm against computed styles.
