---
version: alpha
name: "Newel"
source_url: "https://www.newel.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Near-black at #171717 is the load-bearing surface of Newel's digital gallery — not a background but a room: dark walls, controlled light, antiques given a museum-grade stage. Type is set in ASTORIA for display headings, a condensed geometric sans whose uppercase forms echo wayfinding signage in a physical gallery, paired with EB Garamond for body copy and pricing — an Elizabethan serif that reads like catalog text from an auction house rather than an e-commerce grid. The grayscale palette runs from #fbfbfb (near-white canvas for card and search surfaces) through three grays — #e0e0e0 hairline, #757575 muted annotations, #4f4f4f body copy — down to the primary near-black ink (#262626) and the deepest field tone (#171717), an entire brand expression built without a single chromatic accent. Interactive elements hold the same dark register: a button activating reads like the same ink annotating a provenance note. Corners throughout are square or nearly so, reinforcing the gallery's institutional formality — there is no softness anywhere except the white glove. Product cards hold antiques at respectful distance: the image fills a tall 4:5 container, with item title, period, and price in compact EB Garamond beneath. The nav sits in the primary near-black with ASTORIA uppercase labels at tight tracking, echoing a gallery's room-by-room wayfinding rather than a navigation menu. Search is purposefully restrained — a clean input against the dark header, no pill, no orb, just a functional form that defers entirely to the inventory. Newel's interface is the architectural decision to let a 19th-century French commode or a 1930s Art Deco lamp speak for itself, framed by dark walls and a spare serif.

colors:
  primary: "#171717"
  primary-active: "#0a0a0a"
  primary-disabled: "#646464"
  ink: "#262626"
  body: "#4f4f4f"
  muted: "#757575"
  hairline: "#e0e0e0"
  canvas: "#fbfbfb"
  surface-soft: "#eeeeee"
  surface-card: "#ffffff"
  on-primary: "#fbfbfb"
  on-surface: "#262626"
  dark-overlay: "#1d2124"
  placeholder: "#9e9e9e"

typography:
  display-xl:
    fontFamily: "'ASTORIA', 'Astoria', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0.04em
    textTransform: uppercase
  display-md:
    fontFamily: "'ASTORIA', 'Astoria', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: 0.03em
    textTransform: uppercase
  display-sm:
    fontFamily: "'ASTORIA', 'Astoria', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.02em
    textTransform: uppercase
  title-md:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'ASTORIA', 'Astoria', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.08em
    textTransform: uppercase
  button-md:
    fontFamily: "'ASTORIA', 'Astoria', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'ASTORIA', 'Astoria', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  nav-label:
    fontFamily: "'ASTORIA', 'Astoria', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.12em
    textTransform: uppercase
  price:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  item-title:
    fontFamily: "'EB Garamond', Georgia, serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  meta-label:
    fontFamily: "'ASTORIA', 'Astoria', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1em
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
    padding: 12px 28px
    height: 44px
    border: "1px solid {colors.primary}"
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 27px
    border: "1px solid {colors.on-primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    placeholderColor: "{colors.placeholder}"
    focusBorder: "1px solid {colors.ink}"
  search-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 40px 10px 14px
    height: 44px
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-label}"
    logoTypography: "{typography.display-sm}"
    height: 64px
  nav-bar-light:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/5"
    titleTypography: "{typography.item-title}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.meta-label}"
    metaColor: "{colors.muted}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    padding: "{spacing.md}"
    gap: "{spacing.sm}"
  product-card-hover:
    outline: "1px solid {colors.hairline}"
    imageScale: 1.02
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-md}"
    subheadColor: "{colors.surface-soft}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    imageOverlay: "rgba(23,23,23,0.48)"
  category-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    padding: "{spacing.base} 0"
    gap: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  item-detail-header:
    titleTypography: "{typography.display-sm}"
    titleColor: "{colors.ink}"
    metaTypography: "{typography.meta-label}"
    metaColor: "{colors.muted}"
    priceTypography: "{typography.title-md}"
    priceColor: "{colors.ink}"
    gap: "{spacing.md}"
  inquiry-form:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.xl}"
    rounded: "{rounded.none}"
    headingTypography: "{typography.display-sm}"
    headingColor: "{colors.ink}"
    borderTop: "2px solid {colors.ink}"
  image-gallery:
    thumbnailBorder: "2px solid transparent"
    thumbnailActiveBorder: "2px solid {colors.ink}"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
  filter-panel:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    borderRight: "1px solid {colors.hairline}"
    padding: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.surface-soft}"
    headingTypography: "{typography.caption}"
    headingColor: "{colors.on-primary}"
    padding: "{spacing.section} 0"
  pagination:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    height: 36px

## Components

### Buttons
**`button-primary`** — Flat near-black fill (#171717) with all-caps ASTORIA label in `{colors.on-primary}`, zero border-radius, 1px matching border. The dark fill doubles as a visual anchor on light-canvas product pages. On hover the fill deepens to `{colors.primary-active}` (#0a0a0a) without any scale or shadow — movement is not the vocabulary here. Disabled state uses `{colors.primary-disabled}` (#646464) while holding the same dimensions.

**`button-secondary`** — Transparent fill with a 1px `{colors.primary}` border and matching dark label. Carries the same ASTORIA uppercase treatment and zero radius. Used for secondary actions such as "View More" or "Request Condition Report" placed alongside a primary inquiry button.

**`button-ghost`** — Transparent background with `{colors.on-primary}` border and text, reserved for dark hero or footer surfaces. The white-on-black inversion keeps the formal register of the primary variant without competing with the background image.

### Text Input / Search
**`text-input`** — Zero-radius input on `{colors.canvas}`, 1px `{colors.hairline}` border that sharpens to 1px `{colors.ink}` on focus. EB Garamond body text inside the field maintains the catalog register; no box-shadow or animated ring — state change is conveyed purely by border weight. Placeholder sits at `{colors.placeholder}` (#9e9e9e).

**`search-input`** — Matches `text-input` geometry but holds a right-aligned search icon in `{colors.muted}` and a fixed 44px height. Appears in the header on light surfaces; on dark nav variants the background inverts to the lightest available canvas. No pill shaping.

### Navigation
**`nav-bar`** — Deep near-black (#171717) bar at 64px height, brand wordmark in ASTORIA `{typography.display-sm}` left-anchored, navigation links in `{typography.nav-label}` (12px uppercase, 0.12em tracking) spanning the top row. Dropdowns appear as flat dark panels with no shadow or border-radius. A `nav-bar-light` variant exists for interior catalog pages where a white header better contextualizes antique photography, with a 1px `{colors.hairline}` bottom edge replacing the dark fill.

### Product Card
**`product-card`** — Square-cornered card on `{colors.surface-card}`. Image fills a 4:5 aspect-ratio container with `overflow: hidden`. Below: item title in `{typography.item-title}` (EB Garamond 15px, `{colors.ink}`), period and style in `{typography.meta-label}` (ASTORIA 10px uppercase, `{colors.muted}`), price in `{typography.price}` (EB Garamond 18px). On hover a 1px `{colors.hairline}` outline materializes and the image scales to 1.02×  — enough to signal interactivity without disturbing the measured pace of the grid.

### Hero Banner
**`hero-banner`** — Full-width near-black canvas (`{colors.primary}`) with a 48% opacity scrim over editorial photography, ensuring the headline remains legible over any image. Headline in `{typography.display-xl}` (ASTORIA 48px uppercase), subhead in `{typography.title-md}` (EB Garamond 20px) at `{colors.surface-soft}`. Minimum height 560px; `{spacing.section}` vertical padding, `{spacing.xl}` horizontal.

### Category Strip
**`category-strip`** — Horizontal scrolling list of category labels in ASTORIA `{typography.caption}` on `{colors.surface-soft}`, separated by a 1px `{colors.hairline}` bottom border. Serves as wayfinding between the main nav and the product grid, echoing the room-by-room navigation of a physical gallery.

### Item Detail
**`item-detail-header`** — Title in ASTORIA `{typography.display-sm}` (24px uppercase), period and provenance metadata in `{typography.meta-label}` (ASTORIA 10px, `{colors.muted}`), price in EB Garamond `{typography.title-md}` (20px). Fields stack vertically with `{spacing.md}` gap; no ruled dividers — white space alone separates hierarchy levels.

### Image Gallery
**`image-gallery`** — Primary image at full-column width; thumbnails in a horizontal strip below with 2px transparent border activating to 2px `{colors.ink}` on selection. Zero radius throughout, `{spacing.sm}` gap between thumbnails. Reflects the care with which provenance photography is presented in auction catalogs.

### Inquiry Form
**`inquiry-form`** — Inset block on `{colors.surface-soft}` with `{spacing.xl}` padding and a 2px `{colors.ink}` top border as the only decorative mark. Heading in ASTORIA `{typography.display-sm}`, fields using the `text-input` spec. Single `button-primary` at the bottom. Replaces add-to-cart entirely on item detail pages — purchase at Newel is a conversation, not a transaction.

### Filter Panel
**`filter-panel`** — Left-rail panel on `{colors.canvas}` with a 1px `{colors.hairline}` right border. Section labels in `{typography.caption}` (ASTORIA uppercase), filter values in `{typography.body-sm}` (EB Garamond). No pills or chips; active state is a plain checkmark with darkened label text. Keeps the filter experience as quiet as the rest of the interface.

### Footer
**`footer`** — Near-black (`{colors.primary}`) footer with `{spacing.section}` vertical padding. Column headings in ASTORIA `{typography.caption}`, links in EB Garamond `{typography.body-sm}` at `{colors.surface-soft}`. Newsletter input uses `search-input` spec with inverted fill. No ruled separator from page body — the dark band reads as a natural continuation of the gallery floor.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger revealing a full-panel dark overlay; hero height reduces to 360px; filter panel becomes a bottom-sheet drawer |
| Tablet | 744–1128px | Two-column product grid; filter panel toggles as a collapsible left rail; hero at 440px; light nav variant preferred |
| Desktop | 1128–1440px | Three- or four-column product grid; persistent left-rail filter; full nav visible with all category labels |
| Wide | > 1440px | Content max-width capped ~1400px and centered; five-column grid available for large inventory views |

### Touch Targets
- All buttons minimum 44px height across all breakpoints
- Nav links padded to minimum 44px tap area on mobile overlay
- Gallery thumbnails expanded to minimum 56×56px touch target on mobile
- Filter checkboxes expanded to a 40px tap zone on touch devices
- Pagination controls minimum 44px height

### Collapsing Strategy
- Primary nav collapses to a hamburger icon below 744px; full-panel dark overlay slides in from left, links in ASTORIA `{typography.display-sm}`
- Category strip becomes a horizontal scroll container at mobile — no wrapping, no truncation
- Filter panel converts to a "Filter" button triggering a bottom-sheet drawer on mobile and tablet
- Hero ASTORIA headline scales from 48px desktop to 28px mobile; subhead EB Garamond drops from 20px to 16px
- Item detail switches from a 60/40 image-to-info split to stacked image-first layout below 744px
- Inquiry form occupies full column width on mobile, losing the inset panel treatment

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The majority of extracted chromatic colors (#1266f1, #b23cfd, #00b74a, #39c0ed, #ffa900, #f93154, #0e52c1, #0b3d91, #6b2498, #006e2c, #22738e and their darker variants) are MDB Bootstrap framework palette defaults and have been excluded from brand tokens
- No brand accent or highlight color was identifiable in the stripped palette — Newel may be strictly monochromatic or may load an accent color via JavaScript not captured in static extraction
- ASTORIA font metrics (precise weight range, variable font status, optical sizes) not confirmed; treated as a display font at weight 600–700 uppercase
- Exact logo lockup dimensions, wordmark vs. logomark treatment, and any SVG brand mark were not captured
- Grid gutter widths, column counts, and precise nav height were not extractable from static hints alone
- Whether the site employs a dark/light nav toggle per page template or maintains a single nav treatment was not determinable
- Price display convention (published pricing vs. "inquire for price") and any condition or provenance badge system were not observed in the extraction
