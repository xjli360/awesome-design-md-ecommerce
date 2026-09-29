---
version: alpha
name: "Sarah Flint"
source_url: "https://sarahflint.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Ivypresto Display opens every headline with high-contrast ink-trap serifs — a deliberate type choice that anchors the handcraft story before a single word is read. The palette is built around a dusty blush (#c49494) that sits between muted terracotta and pale rose, specific enough to be a brand fingerprint yet subdued enough to recede behind the photography. Every page renders on a warm off-white canvas (#f7f4f2) rather than clinical white, giving product imagery a magazine-editorial warmth that a pure white would kill. Proxima Nova handles all body copy and UI chrome — its geometric regularity creates deliberate contrast against Ivypresto's sculptural serifs, signaling that legibility and elegance operate in separate registers. An oxblood accent (#6b1c1b) surfaces in hover and urgency states, drawing from the heritage of luxury leather goods without being decorative for its own sake. Corner radii are kept at zero to softly rounded (0–8px) across the entire system — no pill shapes, no heavy curves — aligning with European luxury footwear conventions rather than DTC softness. Navigation sits transparently above hero imagery and transitions to the warm white surface on scroll, with a centered wordmark and minimal utility icons. Product cards use tall 3:4 portrait ratios that prioritize the shoe's profile over lifestyle clutter, with Ivypresto carrying the product name and Proxima Nova the price. The functional blue (#334fb4) is confined to link states and never appears in brand moments. A blush badge marks new arrivals; an ink badge marks bestsellers. The system earns its premium register through typographic authority and photographic restraint rather than ornament or logo saturation.

colors:
  primary: "#c49494"
  primary-active: "#8f6c6c"
  primary-disabled: "#e2c0c0"
  ink: "#121212"
  body: "#191919"
  muted: "#777777"
  muted-soft: "#555555"
  hairline: "#dedede"
  canvas: "#f7f4f2"
  surface-soft: "#f3f3f3"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  oxblood: "#6b1c1b"
  nav-dark: "#242833"
  link: "#334fb4"

typography:
  display-xl:
    fontFamily: "'ivypresto-display', Georgia, 'Times New Roman', serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ivypresto-display', Georgia, serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.13
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ivypresto-display', Georgia, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'ivypresto-display', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.4px
  title-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  body-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  label-caps:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  price:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-sale:
    fontFamily: "'proxima-nova', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    color: "#6b1c1b"

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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 48px
    hoverBackgroundColor: "{colors.primary}"
    transition: background-color 150ms ease
  button-primary-disabled:
    backgroundColor: "{colors.hairline}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 16px 32px
    height: 48px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 15px 31px
    height: 48px
    hoverBackgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted-soft}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderBottom: "1px solid {colors.hairline}"
    borderBottomFocus: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 0
    height: 48px
  nav-bar:
    backgroundColor: "transparent"
    backgroundColorScrolled: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottomScrolled: "1px solid {colors.hairline}"
    transition: background-color 200ms ease
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    nameTypography: "{typography.display-sm}"
    priceTypography: "{typography.price}"
    gap: "{spacing.sm}"
    hoverImageCrossfade: true
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-bestseller:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-sale:
    backgroundColor: "{colors.oxblood}"
    textColor: "{colors.canvas}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    ctaTypography: "{typography.button-md}"
    minHeight: 600px
    paddingX: "{spacing.xxl}"
    overlayOpacity: 0
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-caps}"
    height: 36px
    paddingX: "{spacing.base}"
  size-selector-tile:
    backgroundColor: "{colors.surface-card}"
    backgroundColorSelected: "{colors.ink}"
    backgroundColorDisabled: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    textColorSelected: "{colors.canvas}"
    textColorDisabled: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorSelected: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    size: 40px
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    gap: "{spacing.xs}"
  filter-chip:
    backgroundColor: "transparent"
    backgroundColorActive: "{colors.ink}"
    textColor: "{colors.ink}"
    textColorActive: "{colors.canvas}"
    borderColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: "8px 16px"
    height: 36px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-md}"
    suggestTypography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    backdropOpacity: 0.4
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    headingTypography: "{typography.label-caps}"
    headingColor: "{colors.primary}"
    linkTypography: "{typography.caption}"
    bodyTypography: "{typography.body-sm}"
    paddingY: "{spacing.section}"
  product-image-zoom:
    backgroundColor: "{colors.canvas}"
    cursorStyle: crosshair
    overlayTypography: "{typography.caption}"

## Components

### Buttons
**`button-primary`** — Ink-black fill (`{colors.ink}`) with warm-canvas text (`{colors.canvas}`), all-caps Proxima Nova at 13px / 1.5px letter-spacing, zero border radius. On hover the background transitions to dusty blush `{colors.primary}` in 150ms — an understated reveal that swaps severity for warmth without changing shape. Disabled state falls to hairline fill with muted text. This button handles "Add to Bag," "Checkout," and primary editorial CTAs.

**`button-secondary`** — Identical geometry to the primary with a 1px solid ink border and transparent fill. Paired with primary in "Add to Bag / Save to Wishlist" stacks; inner padding compensates for the border so both buttons align optically. Hover lifts to `{colors.surface-soft}`.

**`button-ghost`** — Text-only, no border, muted-soft color, smallest button type scale. Used for low-hierarchy actions: "View all," "See size guide," "Read more."

### Text Input
**`text-input`** — Renders with only a bottom hairline rule on the warm canvas surface, shifting to a full-ink bottom border on focus. Zero radius. Placeholder text in `{colors.muted}`. Used in email capture overlays, search, account login, and checkout field rows. The stripped-down styling keeps form UI from competing with product photography.

### Navigation
**`nav-bar`** — Transparent on page load, transitioning to canvas-fill with a hairline bottom border as the user scrolls past 64px. Wordmark is center-aligned; utility icons (search, account, bag with item count) cluster right; primary category links span left. Hover on any category link drops a full-width mega-menu panel containing editorial imagery and text-column navigation. On mobile the entire structure collapses into a slide-in drawer triggered by a hamburger icon.

**`announcement-bar`** — A 36px blush stripe (`{colors.primary}`) above the nav, carrying free-shipping thresholds or campaign messages in all-caps canvas text. Auto-rotates between two messages on mobile via a fade; static on desktop.

### Product Card
**`product-card`** — 3:4 portrait ratio keeps the shoe's full profile dominant. Product name uses `{typography.display-sm}` Ivypresto so listing grids carry editorial weight; price renders in Proxima Nova `{typography.price}`. Badges overlay the image at top-left: `badge-new` in dusty blush, `badge-bestseller` in ink, `badge-sale` in oxblood. On hover, a secondary product image cross-fades over the primary in ~200ms to show the shoe worn or from an alternate angle. No card shadow or border; the image bleeds to the card edge.

### Hero
**`hero`** — Full-viewport or half-viewport editorial images with text overlaid or stacked alongside. The headline uses `{typography.display-xl}` Ivypresto at 300 weight so it remains legible over photography without requiring a dark scrim — the light weight itself provides breathing room. A short subline in `{typography.body-md}` Proxima Nova and a `button-primary` CTA anchor the copy block. Campaigns may use a split-screen layout (image left, text right) at desktop widths.

### Size Selector
**`size-selector-tile`** — Square 40px tiles with hairline borders at rest; selected state inverts to ink fill with canvas text. Out-of-stock tiles render with a diagonal 1px hairline through the center and disabled color. Tiles wrap in a 5–6 column grid on desktop, 4 columns on mobile. A "Size Guide" `button-ghost` link triggers a modal with a measurement chart.

### Search Overlay
**`search-overlay`** — Full-screen takeover on the warm canvas surface with a 40% dark backdrop behind a centered panel. A single large input at `{typography.display-md}` Ivypresto dominates the upper third; suggested searches and recently viewed products appear below as Proxima Nova body rows. Pressing Escape or clicking the backdrop dismisses it.

### Filter Chip
**`filter-chip`** — Used on collection pages to filter by category, heel height, material, color, and size. Zero radius, ink border at rest; inverts to ink fill on active selection. Multiple chips may be active simultaneously; a `button-ghost` "Clear all" appears inline when any filter is active.

### Footer
**`footer`** — Ink-fill full-width section in four desktop columns: Shop, Help, About, Connect. Column headings in `{typography.label-caps}` render in dusty blush `{colors.primary}` against the ink background; link rows use `{typography.caption}` in a softened canvas tone. Newsletter input sits in the rightmost column with a `button-secondary` submit styled to invert (canvas border, canvas text) against the dark background. Social icons and legal links run along the bottom edge.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger drawer nav; hero text moves below image; size tiles compress to 4-column grid; footer collapses to accordion sections; announcement bar auto-rotates |
| Tablet | 744–1128px | Two-column product grid; top nav retains horizontal links but hides sub-labels; hero retains full-viewport image with text overlay; filter sheet opens from bottom |
| Desktop | 1128–1440px | Three- or four-column product grid; mega-menu on nav hover; hero may use editorial split layout (image + text side-by-side); size grid expands to 6 columns |
| Wide | > 1440px | Content rail max-width ~1440px; side gutters expand proportionally; hero imagery full-bleed behind contained text column |

### Touch Targets
- All interactive elements maintain minimum 44×44px touch area on mobile
- Size selector tiles expand to 48×48px tap surface on touch devices regardless of visual size
- Nav icons use 44px minimum tap zone regardless of glyph dimensions
- Announcement bar close/chevron buttons enforce 44px tap zone
- Filter chips minimum 36px height with horizontal padding ensuring 44px effective target

### Collapsing Strategy
- Footer nav collapses to tap-to-expand accordion rows on mobile; only one section open at a time
- Mega-menu converts to a full-height slide-in drawer on mobile and tablet with back-button navigation
- Product filters move from a left sidebar (desktop) to a bottom-sheet modal (mobile/tablet) with Apply/Clear controls pinned at bottom
- Hero text block stacks below image on mobile to preserve Ivypresto legibility at small viewport widths
- Product card badge moves from top-left image overlay to inline below price on very narrow widths if layout requires reflow

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact Ivypresto Display font weights per scale not confirmed from extraction — 300/400 inferred from editorial serif convention at this price tier; actual weights may differ
- No explicit border-radius values extracted; 0–8px range inferred from luxury-fashion visual convention
- Role of #242833 nav-dark is ambiguous — may be used in a dark-mode campaign module or footer variant; not assigned a primary semantic token
- Role of #334fb4 blue is unclear — may be a Shopify default link color rather than a brand intent; treated as functional link-only and excluded from brand moments
- Hover transition durations and easing curves not extractable from static analysis; 150–200ms ease inferred
- Mega-menu content structure (number of columns, presence of editorial imagery) inferred from luxury e-commerce norms, not directly observed
- Product card secondary-image hover behavior inferred; not confirmed from extraction
- Announcement bar rotation behavior on desktop (static vs. cycling) not confirmed
- Custom monospace font usage not identified — extracted stack may be a Shopify theme default for code/price formatting
