---
version: alpha
name: "Olde Good Things"
source_url: "https://ogtstore.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Salvaged architectural elements don't photograph like new inventory — a run of pressed-tin ceiling or a cast-iron newel post carries the argument once the camera is close enough. Olde Good Things builds its interface around that reality: the canvas is warm plaster white (#f3f2f1), structural type sits in charcoal mortar (#4d4749), and the single voltage color is a struck-brick rust (#904b3c) found in oxidized iron and fired clay. It lands on every call-to-action and active state with the authority of a material fact rather than a brand decision.

  Bookmania — a revival of mid-century phototypesetting aesthetics, with bracketed serifs, ink traps, and old-style figures — anchors all display headings and product titles. Bio Sans carries navigation, labels, and UI prose. The pairing reads like a specialist's trade catalogue printed on cream stock: readable, unhurried, certain of its inventory. A muted sage (#91b08e) and a deep slate (#3e5871) surface in filter tags, secondary badges, and accent flourishes — they read as verdigris and aged iron rather than injected accent colors, which fits a store whose inventory spans Victorian mantels, industrial factory windows, and Arts and Crafts hardware.

  Corner radii are minimal throughout. Product cards take `{rounded.xs}` (2px), buttons `{rounded.sm}` (4px), and modal containers `{rounded.md}` (8px) — hard geometry echoing the angular profiles of mouldings and ironwork the store sells. Nothing is pill-shaped. Spacing is generous at every level: product imagery occupies most of a card, dimension and condition metadata sits below in Bio Sans body-sm, and item numbers appear in Bookmania uppercase caption — a catalogue house convention that signals specialist knowledge. Filter navigation lives in a persistent left sidebar on desktop, collapsing to an off-canvas drawer on mobile, and allows stacking of era, material, and architectural category without a page reload. Generous vertical rhythm ({spacing.section} = 64px between content bands) and near-absence of decorative chrome preserve the archival, museum-catalogue atmosphere that justifies premium pricing on secondhand material.

colors:
  primary: "#904b3c"
  primary-active: "#7c3d2f"
  primary-disabled: "#c99890"
  ink: "#292826"
  body: "#4d4749"
  muted: "#8b8988"
  hairline: "#c7c5c4"
  canvas: "#f3f2f1"
  surface-soft: "#ebe9e8"
  surface-card: "#ffffff"
  surface-sage-tint: "#e9fad0"
  on-primary: "#f3f2f1"
  accent-sage: "#91b08e"
  accent-sage-dark: "#6e8269"
  accent-slate: "#3e5871"
  accent-slate-light: "#6289b0"
  scrim: "#292826"

typography:
  display-xl:
    fontFamily: "'Bookmania', Georgia, 'Times New Roman', serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Bookmania', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Bookmania', Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Bio Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Bio Sans', -apple-system, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Bio Sans', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Bio Sans', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Bio Sans', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.01em
  item-number:
    fontFamily: "'Bookmania', Georgia, serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.12em
    textTransform: uppercase
  category-label:
    fontFamily: "'Bio Sans', -apple-system, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  price-display:
    fontFamily: "'Bookmania', Georgia, serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-md:
    fontFamily: "'Bio Sans', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Bio Sans', -apple-system, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.06em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Bio Sans', -apple-system, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.02em

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
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
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    border: "1px solid {colors.body}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    padding: 8px 12px
    border: none
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted}"
    focusBorder: "1px solid {colors.body}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 40px 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
    iconColor: "{colors.muted}"
    iconActiveColor: "{colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoTypography: "{typography.display-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.body}"
    padding: "{spacing.sm} 0"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "4/3"
    border: "1px solid {colors.hairline}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    itemNumberTypography: "{typography.item-number}"
    itemNumberColor: "{colors.muted}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.ink}"
    metadataTypography: "{typography.caption}"
    metadataColor: "{colors.muted}"
    contentPadding: 14px 16px 16px
  product-card-hover:
    borderColor: "{colors.body}"
    imageScale: 1.02
    transition: 200ms ease
  hero-editorial:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    overlayColor: "rgba(41,40,38,0.55)"
    headingTypography: "{typography.display-xl}"
    subheadingTypography: "{typography.body-md}"
    minHeight: 560px
    contentMaxWidth: 640px
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.canvas}"
    labelTypography: "{typography.category-label}"
    rounded: "{rounded.xs}"
    aspectRatio: "3/4"
    overlayColor: "rgba(41,40,38,0.42)"
    labelPadding: 12px 16px
  condition-tag:
    typography: "{typography.category-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
    variants:
      as-found:
        backgroundColor: "{colors.surface-soft}"
        textColor: "{colors.muted}"
        border: "1px solid {colors.hairline}"
      restored:
        backgroundColor: "{colors.surface-sage-tint}"
        textColor: "{colors.accent-sage-dark}"
        border: none
      reclaimed:
        backgroundColor: "{colors.surface-soft}"
        textColor: "{colors.accent-slate}"
        border: "1px solid {colors.accent-slate-light}"
  era-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.item-number}"
    rounded: "{rounded.none}"
    padding: 4px 8px
    border: "1px solid {colors.hairline}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    width: 240px
    borderRight: "1px solid {colors.hairline}"
    sectionLabelTypography: "{typography.category-label}"
    sectionLabelColor: "{colors.ink}"
    optionTypography: "{typography.body-sm}"
    optionColor: "{colors.body}"
    activeOptionColor: "{colors.primary}"
    checkboxAccent: "{colors.primary}"
    sectionGap: "{spacing.lg}"
  item-detail-header:
    itemNumberTypography: "{typography.item-number}"
    itemNumberColor: "{colors.muted}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price-display}"
    priceColor: "{colors.primary}"
    stackGap: "{spacing.sm}"
  image-gallery:
    backgroundColor: "{colors.ink}"
    thumbnailBorder: "2px solid transparent"
    thumbnailActiveBorder: "2px solid {colors.primary}"
    thumbnailRounded: "{rounded.xs}"
    navButtonColor: "{colors.canvas}"
    navButtonBackground: "rgba(41,40,38,0.60)"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.category-label}"
    headingColor: "{colors.canvas}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.section} 0"

## Components

### Buttons
**`button-primary`** — Uppercase Bio Sans 14px/600 with 0.06em tracking, brick rust (#904b3c) fill at 44px tall, 4px corner radius, no border. Hover deepens to `{colors.primary-active}` (#7c3d2f); disabled bleaches to `{colors.primary-disabled}` (#c99890). The uppercase tracking echoes catalogue numbering and signals intentionality rather than urgency — this is not a loud CTA, it is a definitive one.

**`button-secondary`** — Identical dimensions and typography to primary, transparent fill with 1px `{colors.hairline}` border. On hover the fill shifts to `{colors.surface-soft}` and the border darkens to `{colors.body}`. Used for "Save to Wishlist," "Request More Information," and secondary confirmations — always adjacent to a primary action, never standalone.

**`button-ghost`** — No border, no fill, body-toned uppercase Bio Sans 12px/600. Used for inline controls: filter resets, breadcrumb actions, and supplementary navigation. Touch target padded to 44px minimum regardless of visual size.

### Text Input
**`text-input`** — Warm canvas fill, 1px `{colors.hairline}` border, 2px radius, 44px tall, Bio Sans 16px/400. Placeholder in `{colors.muted}`; focus promotes border to `{colors.body}` — no glow, no color injection, just weight. Pairs with a right-side magnifier icon that transitions from `{colors.muted}` to `{colors.primary}` on first keystroke.

**`search-bar`** — Same proportions as text-input but slightly recessed in `{colors.surface-soft}` to distinguish the search field from form inputs. Used in the nav bar and the category page header.

### Navigation
**`nav-bar`** — 64px tall, `{colors.canvas}` background with a 1px `{colors.hairline}` bottom rule. Logo renders in Bookmania `{typography.display-sm}` at left; category links in Bio Sans `{typography.nav-link}` span center; account, wishlist, and cart icons anchor right. Sticky on scroll with a faint box-shadow replacing the static border rule. On mobile, collapses to hamburger + wordmark + cart icon.

**`breadcrumb`** — Bio Sans 12px/400 in `{colors.muted}` with slash separators in `{colors.hairline}`. Current page node renders in `{colors.body}`, unlinked. Appears below the nav bar on all non-homepage pages. On mobile, shows only root and current node with an ellipsis for collapsed middle segments.

### Product Card
**`product-card`** — White surface card, 1px hairline border, 2px radius. Image occupies a 4:3 aspect ratio with no independent radius. Below the image: item number in `{typography.item-number}` (Bookmania, wide-tracked uppercase, muted), title in `{typography.title-sm}` (Bio Sans), inline condition and era tags, then price in `{typography.price-display}` (Bookmania 20px, ink-colored). On hover, border darkens to `{colors.body}` and image scales 1.02× over 200ms ease. No add-to-cart surface on the card — the card is a discovery surface; conversion happens on the product detail page.

### Hero
**`hero-editorial`** — Full-bleed photograph with a 42% ink scrim. Heading in `{typography.display-xl}` (Bookmania 42px) and a one-line subhead in `{typography.body-md}` both in `{colors.canvas}`. Content column caps at 640px, minimum height 560px. A single `button-primary` sits below the subhead. Used for estate-sale spotlights, seasonal features, and architectural-category campaigns ("Factory Windows: Cast Iron & Steel, 1880–1940").

### Category Tile
**`category-tile`** — 3:4 portrait tiles with a 42% ink overlay and the category label in `{typography.category-label}` (uppercase, wide-tracked) pinned to the bottom-left corner in `{colors.canvas}`. No hover animation beyond a subtle overlay darkening. Grid layout: two columns on mobile, four on desktop. Used on the homepage for Doors, Windows, Columns, Ironwork, Mantels, Plumbing Fixtures, and Tin Ceilings.

### Condition & Era Tags
**`condition-tag`** — Three variants at 2px radius, uppercase Bio Sans 11px/600. "As Found" carries hairline border on soft surface, muted text — raw, uninterpreted. "Restored" uses sage tint (#e9fad0 from `{colors.surface-sage-tint}`) with dark sage text — conservation positive. "Reclaimed" reads in `{colors.accent-slate}` with a light slate border — provenance-documented. Tags stack inline with era badges below the product title on detail pages.

**`era-badge`** — Zero-radius rectangular chip, Bookmania `{typography.item-number}` style, hairline border, `{colors.body}` text. Marks period attribution: Victorian, Edwardian, Art Deco, Industrial, Mid-Century Modern. Placed inline beside condition tags on both cards and detail pages.

### Filter Sidebar
**`filter-sidebar`** — 240px wide, canvas background, 1px hairline right border. Section headers in uppercase `{typography.category-label}` with `{spacing.lg}` vertical rhythm between groups. Checkbox accent in `{colors.primary}`; active filter values in rust. Filter dimensions: Era (Victorian, Edwardian, Art Deco, Industrial, Mid-Century), Material (Cast Iron, Marble, Hardwood, Steel, Brass, Tile), Category (Columns, Doors, Ironwork, Mantels, Windows, Plumbing), Condition (As Found, Restored, Reclaimed). On mobile and tablet, collapses to an off-canvas drawer sliding in from the left, triggered by a "Filter" ghost button.

### Item Detail Header
**`item-detail-header`** — Stacked vertically with `{spacing.sm}` between layers: item number (Bookmania uppercase caption, `{colors.muted}`), then title (Bookmania `{typography.display-md}`, `{colors.ink}`), then price (Bookmania `{typography.price-display}`, `{colors.primary}`). The item number precedes the title — a procurement catalogue convention that positions Olde Good Things as a specialist source rather than a lifestyle retailer. Material notes and dimensions follow in `{typography.body-sm}`.

### Image Gallery
**`image-gallery`** — Main image on dark `{colors.ink}` field. Thumbnail strip below; active thumbnail has a 2px rust border (`{colors.primary}`), inactive thumbnails have transparent 2px borders for consistent sizing. Navigation arrows in `{colors.canvas}` on a 60% ink scrim background. Thumbnails use `{rounded.xs}` (2px). On mobile, swipe-to-navigate replaces arrow controls; thumbnails collapse to dot indicators.

### Footer
**`footer`** — Dark ink background with a 2px rust top border serving as the structural punctuation between page content and the footer. Column headings in uppercase `{typography.category-label}` in `{colors.canvas}`; links in `{colors.hairline}`, hovering to `{colors.canvas}`. Body text in `{typography.body-sm}`, `{colors.surface-soft}`. Newsletter input is an inverted `text-input`: dark fill, canvas text, rust focus border. Padding `{spacing.section}` top and bottom.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; filter sidebar becomes off-canvas drawer; hero heading steps down to `{typography.display-md}`; nav collapses to hamburger + wordmark + cart; category tiles in 2 columns; item detail stacks gallery above metadata |
| Tablet | 744–1128px | Two-column product grid; filter sidebar inline but collapsible with a toggle; nav shows primary categories, drops secondary links; hero at display-md |
| Desktop | 1128–1440px | Three-column product grid with persistent 240px filter sidebar; full nav visible; hero at display-xl; item detail two-column layout (gallery 60%, metadata 40%) |
| Wide | > 1440px | Four-column product grid; max-width container 1440px centered; lateral whitespace preserved; hero content column 640px; catalogue-catalogue air maintained |

### Touch Targets
- All interactive elements minimum 44×44px touch area
- Filter checkboxes padded to 44px tall tap target regardless of visual glyph size
- Nav hamburger icon 44×44px
- Product card tap target spans full card surface — no isolated button required on mobile
- Gallery navigation arrows padded to 44×44px
- Condition and era tags padded to 32px minimum height on mobile

### Collapsing Strategy
- Filter sidebar moves off-canvas first, at < 1128px (tablet breakpoint)
- Nav category links collapse to hamburger at < 744px (mobile breakpoint)
- Product grid: 4 columns → 3 columns at 1128px → 2 columns at 744px → 1 column below 744px
- Hero heading: display-xl (42px) → display-md (28px) at < 744px
- Item detail two-column layout stacks at < 744px with gallery above metadata
- Breadcrumb truncates middle path segments with ellipsis at < 744px, retaining root and current node only
- Footer column grid: 4 columns → 2 columns at 744px → 1 column at < 480px

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Actual logomark treatment (wordmark vs. standalone glyph) is unconfirmed; Bookmania wordmark assumed from font stack evidence
- `surface-card` white (#ffffff) is not in the extracted palette; derived as contrast surface over the warm canvas — may be #ebe9e8 in practice
- `primary-disabled` (#c99890) is derived from `primary` (#904b3c); no extracted disabled-state color available
- The blues (#6289b0, #3e5871, #0062c0, #007cba, #007cba) may overlap with WordPress/WooCommerce admin and link defaults rather than brand accent choices; accent usage treated conservatively and limited to slate tones
- Platform confirmed as WooCommerce (not Shopify) — cart markup, pagination, and product URL structure will follow WooCommerce conventions
- Exact nav height unconfirmed; 64px is estimated from visible layout proportions
- Filter sidebar pixel width (240px) estimated; actual implementation value may differ
- No extracted shadow tokens; all box-shadow values are design inferences
- Hover and quick-view behavior on product cards unconfirmed from extraction
- Mobile navigation drawer animation direction and overlay behavior unconfirmed
