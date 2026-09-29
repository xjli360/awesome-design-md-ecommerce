---
version: alpha
name: "Pearl Octopuss.y"
source_url: "https://www.pearloctopussy.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The title card reads PEARL OCTOPUSS.Y — all caps, with a period embedded inside the name itself before the terminal character — a typographic tic that signals wit operating just below a composed surface. Warm marigold-gold (#d49a06) carries every primary CTA and decorative accent, chosen not for conventional luxury cliché but for its relationship to actual nacre: the way a quality pearl catches gold-spectrum light before it shifts toward lavender. That iridescent logic runs through the surface palette too — a pale cream-yellow (#f5f9c8) and a faint lavender mist (#f2eff7) stand in for the spectral range a pearl produces when rotated in daylight, while near-black (#121212) grounds everything without resolving to pure black's harshness. Silver-mist (#d3d3d3) punctuates links and secondary chrome, echoing the cooler overtone of a South Sea or Akoya specimen.

  Inter arrives at deliberately light weights — display text at 300, body at 400 — creating an editorial quietude that allows jewelry photography to dominate. Letter-spacing opens at `{typography.nav-link}` (0.06em uppercase) and widens further at `{typography.button-md}` (0.10em uppercase), the brand's typographic fingerprint: loose, spaced, a little archival. `{rounded.sm}` (8px) appears on buttons and text inputs; product cards take `{rounded.md}` (12px); material tags clip to `{rounded.xs}` (4px). No component reaches for hard right angles or the aggressive softness of full-pill shapes — the geometry sits between object-like and organic. The surface system layers three soft fields: #f2f2f2 for general page chrome, #f5f9c8 (cream warm enough to read as parchment) for product cards, and #f2eff7 (pearl lavender) for detail panels and feature callouts — each a different refraction of light off an organic surface. The Shopify-built storefront keeps its grid restrained: two or three columns on desktop, single column on mobile, with generous whitespace that positions each piece as an object worth pausing on rather than a unit in a catalog.

colors:
  primary: "#d49a06"
  primary-active: "#b07d04"
  primary-disabled: "#e8c96a"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#787878"
  hairline: "#dedede"
  hairline-soft: "#f2f2f2"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#f5f9c8"
  surface-pearl: "#f2eff7"
  on-primary: "#121212"
  silver-mist: "#d3d3d3"
  gold: "#d49a06"

typography:
  display-xl:
    fontFamily: "Inter, sans-serif"
    fontSize: 54px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -1.5px
  display-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 34px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0.02em
  title-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.08em
    textTransform: uppercase
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  price:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.06em
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
  button-primary-hover:
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
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoLetterSpacing: 0.12em
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    rounded: "{rounded.md}"
    imageBorderRadius: "{rounded.md}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    paddingVertical: "{spacing.section}"
    maxWidth: 640px
  material-tag:
    backgroundColor: "{colors.surface-pearl}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: "4px 10px"
  collection-label:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    paddingBottom: "{spacing.sm}"
    borderBottom: "1px solid {colors.hairline}"
  jewelry-detail-panel:
    backgroundColor: "{colors.surface-pearl}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: "{spacing.xl}"
  swatch-selector:
    borderActive: "2px solid {colors.primary}"
    borderInactive: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    size: 24px
    gap: "{spacing.xs}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    padding: "8px 16px"
    placeholderColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.silver-mist}"
    padding: "{spacing.xxl} {spacing.xl}"
    columnGap: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Gold (#d49a06) fill with near-black text on a 48px-tall block, corners at `{rounded.sm}`. Letter-spaced uppercase Inter at 12px renders less as a call-to-action and more as a composed label. Hover deepens to #b07d04; the disabled state bleaches to #e8c96a and kills pointer events.

**`button-secondary`** — White canvas fill with a 1px black border and identical typographic treatment to `button-primary`, creating a clean pairing that lets the primary gold read as the definitive action without a heavy contrast gap.

**`button-ghost`** — Transparent fill, `{colors.hairline}` border. Used for lower-hierarchy flows (filter toggles, "Learn more" links in editorial panels) where visual weight must stay minimal.

### Nav Bar

**`nav-bar`** — 64px white bar with `{colors.hairline}` bottom border. Navigation links use `{typography.nav-link}` — 12px Inter uppercase at 0.06em tracking, weight 400. The PEARL OCTOPUSS.Y wordmark likely extends the same caps-with-embedded-period treatment at a slightly wider tracking (0.12em). No background color change on scroll is expected; the border alone signals depth.

### Product Card

**`product-card`** — The parchment-cream surface (#f5f9c8) distinguishes each card from the page's #f2f2f2 chrome. `{rounded.md}` (12px) on both the card container and the image crop. Title in `{typography.title-md}` (Inter 500, 16px), price in `{typography.price}` (Inter 500, 16px). Hover state likely lifts the card via a subtle box shadow; no background color transition is extracted.

### Hero

**`hero`** — Full-width white canvas panel with `{typography.display-xl}` headline at Inter 300, 54px, −1.5px letter-spacing. Subhead drops to `{typography.body-md}` at line-height 1.65. A single `button-primary` anchors the CTA below the subhead. The light-weight display treatment trusts product imagery to carry emotional weight rather than typographic force.

### Material Tag

**`material-tag`** — Pearl-lavender (#f2eff7) pill-adjacent chip at `{rounded.xs}`. Used to label material provenance (Akoya, South Sea, Freshwater, Jade) at `{typography.caption}` (12px, 0.04em tracking). Appears on product cards and detail panels as an informational badge rather than a navigational element.

### Collection Label

**`collection-label`** — Transparent background, uppercase Inter 12px (0.08em tracking), with a `{colors.hairline}` underline rather than a background fill. Sits above grid sections to divide editorial groupings — functions as a section divider in disguise.

### Jewelry Detail Panel

**`jewelry-detail-panel`** — Pearl-lavender (#f2eff7) field at `{rounded.md}`, containing the product title in `{typography.display-sm}` (Inter 300, 24px), description in `{typography.body-md}`, and material tags in a horizontal chip row. Padding at `{spacing.xl}` (32px) creates breathing room. This panel lives below or beside the primary product image depending on viewport.

### Swatch Selector

**`swatch-selector`** — 24px circular swatches at `{rounded.full}`. Active state uses a 2px gold (#d49a06) outer ring; inactive uses `{colors.hairline}`. Used for pearl color variation (white, pink, golden, black) and jade piece selection.

### Search Bar

**`search-bar`** — 40px `{colors.surface-soft}` input field at `{rounded.sm}`, no visible border at rest. Placeholder in `{colors.muted}`. Matches the page's light gray registers without introducing a competing white box.

### Footer

**`footer`** — Near-black (#121212) fill, white body text at `{typography.body-sm}`, secondary links in silver-mist (#d3d3d3). Gold `{colors.primary}` may appear as hover color on links. Columns at 48px gap with 48px vertical padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark; hero headline drops to ~32px; jewelry-detail-panel becomes full-width stacked below image; swatch row scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level links with overflow into a "more" menu; hero gains padding increase; detail panel moves to a side column at 44% width |
| Desktop | 1128–1440px | Three-column product grid; full nav bar with all collection links visible; hero maxes at 640px text column with full-bleed image beside it |
| Wide | > 1440px | Container max-width ~1440px centered; four-column grid option for collection pages; hero text column stays at 640px, image panel fills remaining canvas |

### Touch Targets

- All buttons maintain 48px height minimum on mobile
- Swatch selectors expand touch zone to 40×40px via padding even at 24px visual size
- Nav links gain 12px vertical padding on mobile for thumb comfort
- Cart and account icons in mobile nav bar meet 44×44px minimum

### Collapsing Strategy

- Three-column desktop grid collapses to two columns at 1128px, then one column at 744px
- Jewelry detail panel: side-by-side (image left, panel right) on desktop → stacked (image top, panel bottom) on mobile
- Footer columns: four-column desktop → two-column tablet → single-column mobile with accordion-style link groups
- Collection labels remain visible at all breakpoints; no content is hidden below tablet

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only Inter is detected in font stacks; brand may use a display serif or bespoke script for logo/wordmark treatment that loads via SVG or JS — not captured in extraction
- Interactive state colors (focus rings, hover highlights beyond primary-active) are inferred, not extracted
- No shadow or elevation tokens surfaced; card lift and modal overlay values are estimated
- Animation and transition timing (ease curves, durations) not available from static extraction
- Exact nav bar height and logo dimensions not confirmed — 64px is estimated from common Shopify theme patterns
- Image aspect ratios for product cards (commonly 1:1 or 4:5 for jewelry) not extracted
- Whether gold (#d49a06) is used as a gradient or flat fill on hero or feature panels is unknown
