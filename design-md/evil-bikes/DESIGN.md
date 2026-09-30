---
version: alpha
name: "Evil Bikes"
source_url: "https://www.evil-bikes.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  DINWebPro-Black hammered at extreme weights against a ground of near-black (#121212, #1c1d1d) — this is the opening condition of Evil Bikes' digital identity, a Bellingham, WA mountain bike company that treats darkness and mass as primary design materials. Where most cycling brands cut toward white and clinical precision, Evil defaults to shadow: product photography floats against void, navigation sits in flat black, and the single rupture in that darkness is a charging teal (#108474) used exclusively for primary CTAs and interactive focus states. The yellow #fbcd0a arrives as emergency voltage — reserved for price badges, promotional callouts, and the occasional hover state, it reads as a warning color rather than a cheerful accent. A muted lavender (#a89cc8) surfaces in subtle UI elements, an unexpected softness inside an otherwise relentless palette that adds just enough personality to signal deliberate authorship over accidental restraint.

  Typography runs DINWebPro-Black for all display work — a grotesque industrial condensed face that compresses word-images into dense horizontal bars, making bike names feel like component specs stamped on aluminum. Barlow handles body and UI text: a geometric sans with slightly more warmth than a pure grotesque, chosen for readability in dense technical copy (geometry charts, spec tables, build kits). The two typefaces co-exist without collision because DIN occupies display-only space — never body copy — and the pairing avoids decorative serif use entirely.

  Buttons are sharp-cornered rectangles ({rounded.none} to {rounded.xs}), refusing the pill shapes and large radii common in lifestyle DTC. Product cards sit on dark surfaces ({colors.surface-card}) with tight borders rather than drop shadows. The nav collapses to a heavy hamburger on mobile with full-screen black takeover. An overline track label — uppercase Barlow, wide letter-spacing — appears above every section heading as a category signal (ENDURO, TRAIL, ALL-MOUNTAIN), functioning like a spec-sheet field label rather than editorial decoration. The overall system reads less like a store and more like a parts catalog that happens to have a checkout.

colors:
  primary: "#108474"
  primary-active: "#0c6459"
  primary-disabled: "#6db8ae"
  accent-yellow: "#fbcd0a"
  accent-lavender: "#a89cc8"
  accent-light-teal: "#c1e6e6"
  ink: "#1c1d1d"
  body: "#444444"
  muted: "#7b7b7b"
  hairline: "#dedede"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#f2f2f2"
  surface-card: "#1c1d1d"
  on-primary: "#ffffff"
  on-dark: "#eeeeee"
  on-accent: "#121212"
  dark-bg: "#121212"
  dark-mid: "#1c1d1d"
  scrim: "rgba(0,0,0,0.45)"

typography:
  display-xl:
    fontFamily: "'DINWebPro-Black W01 Regular', Arial, Helvetica, sans-serif"
    fontSize: 72px
    fontWeight: 900
    lineHeight: 1.0
    letterSpacing: -1px
    textTransform: uppercase
  display-lg:
    fontFamily: "'DINWebPro-Black W01 Regular', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 900
    lineHeight: 1.05
    letterSpacing: -0.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'DINWebPro-Black W01 Regular', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: 0
    textTransform: uppercase
  display-sm:
    fontFamily: "'DINWebPro-Black W01 Regular', Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: 0
    textTransform: uppercase
  title-md:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  overline:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 2px
    textTransform: uppercase
  body-md:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'DINWebPro-Black W01 Regular', Arial, Helvetica, sans-serif"
    fontSize: 28px
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: 0
  button-md:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Barlow', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.5px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 6px
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
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 27px
    height: 48px
  button-secondary-dark:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-accent:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.dark-mid}"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderWidth: 1px
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    typography: "{typography.body-md}"
  nav-bar:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  nav-bar-scrolled:
    backgroundColor: "{colors.dark-bg}"
    borderBottom: "1px solid #2a2a2a"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
    border: "1px solid #2a2a2a"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    padding: "{spacing.base}"
  product-card-hover:
    border: "1px solid {colors.primary}"
  hero:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    overlineTypography: "{typography.overline}"
    overlineColor: "{colors.primary}"
    minHeight: 85vh
    scrim: "{colors.scrim}"
  category-overline:
    textColor: "{colors.primary}"
    typography: "{typography.overline}"
    marginBottom: "{spacing.sm}"
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  spec-table:
    backgroundColor: "{colors.dark-mid}"
    textColor: "{colors.on-dark}"
    borderColor: "#2a2a2a"
    labelTypography: "{typography.caption}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    rowPadding: "{spacing.sm} {spacing.base}"
  size-selector:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    borderColor: "{colors.hairline}"
    selectedBg: "{colors.primary}"
    selectedText: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    height: 44px
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.primary}"
    selectedRingOffset: 2px
  search-bar:
    backgroundColor: "#2a2a2a"
    textColor: "{colors.on-dark}"
    placeholderColor: "{colors.muted}"
    rounded: "{rounded.xs}"
    height: 40px
    typography: "{typography.body-sm}"
  bike-category-tile:
    backgroundColor: "{colors.dark-mid}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-sm}"
    overlayColor: "rgba(0,0,0,0.35)"
    hoverScale: 1.03
    rounded: "{rounded.none}"
    aspectRatio: "3/2"
  footer:
    backgroundColor: "{colors.dark-bg}"
    textColor: "{colors.muted}"
    linkColor: "{colors.on-dark}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.overline}"
    borderTop: "1px solid #2a2a2a"
    padding: "{spacing.section} 0"
  section-divider:
    borderColor: "#2a2a2a"
    borderWidth: 1px
    margin: "{spacing.section} 0"

## Components

### Buttons

**`button-primary`** — A zero-radius rectangle in teal (#108474) with uppercase Barlow Bold at 1.5px letter-spacing, 48px height. The shape is deliberately anti-pill: sharp corners signal precision hardware rather than consumer softness. Active state deepens to #0c6459; disabled washes to #6db8ae at full opacity. Use on dark backgrounds exclusively — teal-on-black meets contrast requirements, but teal on white canvas reads too quiet for a brand this loud.

**`button-secondary`** — Transparent fill with a 1px `{colors.on-dark}` border and matching uppercase Barlow. Paired with `button-primary` for two-action layouts, it recedes without disappearing. Swap to `button-secondary-dark` (1px ink border) on white or light-gray canvas sections — identical geometry, inverted chrome.

**`button-accent`** — Yellow (#fbcd0a) fill with near-black (#121212) text. Reserved for promotional urgency: limited availability, sale events, configurator CTAs. The yellow reads like a warning signal inside the dark system — do not use as a default CTA; that role belongs exclusively to teal.

### Navigation Bar

**`nav-bar`** — Full-width black (#121212) at 64px height, never transparent even at page top. Nav links in uppercase Barlow 600 at 14px with 1px letter-spacing; hover shifts text to teal (#108474). The Evil Bikes wordmark sits left-flush; account and cart icons right-flush. On scroll, a 1px #2a2a2a bottom border appears via the `nav-bar-scrolled` variant. Mobile collapses to a hamburger (48×48px touch area) that opens a full-viewport black overlay with stacked items in `{typography.display-sm}` scale.

### Product Card

**`product-card`** — Dark surface (#1c1d1d) with a 1px #2a2a2a border, zero radius. On hover, the border flips to teal (#108474) via `product-card-hover` — the only interactive signal applied at the card level. Price renders in `{typography.price}` (DINWebPro-Black at 28px), making the number feel like a spec rather than a retail label. No drop shadows anywhere in the card system.

### Hero

**`hero`** — Full-bleed photography at 85vh minimum, overlaid with a 45% black scrim. Title in `{typography.display-xl}` (DINWebPro-Black uppercase, 72px, −1px tracking) stacks above a teal `{typography.overline}` category label. A single `button-primary` CTA sits directly below — no secondary actions in the hero zone. On mobile the title scales to `{typography.display-md}` (32px) and the button goes full-width.

### Category Overline

**`category-overline`** — 11px uppercase Barlow at 700 weight and 2px letter-spacing, rendered in teal (#108474). Appears above every section heading as a taxonomy signal: ENDURO, TRAIL, ALL-MOUNTAIN, COMPONENTS. Functions as a field-label typographic beat rather than a decorative accent, giving the layout a spec-sheet rhythm without resorting to ruled separators.

### Spec Table

**`spec-table`** — Two-column grid on dark-mid (#1c1d1d) with 1px dividers in near-invisible #2a2a2a. Left column uses Barlow 12px in muted (#7b7b7b); right column uses Barlow 14px in on-dark (#eeeeee). No alternating row colors — the pure darkness and minimal borders keep the table from feeling like a spreadsheet. Used for geometry charts, component specs, and build-kit breakdowns.

### Size Selector

**`size-selector`** — Flat rectangular toggles with 1px hairline borders, zero radius, and 44px height for touch adequacy. Selected state fills with teal (#108474) and swaps text to white. Typography in uppercase Barlow Bold at 12px. Out-of-stock sizes render at 40% opacity with a diagonal strikethrough line across the button face. Desktop: inline row; mobile: wraps to two columns.

### Badge System

**`badge-new`** — Yellow (#fbcd0a) fill, near-black text, no radius, 3px top/bottom × 8px left/right padding. Sits top-left of product card images without overlapping the bike silhouette. **`badge-sale`** — Identical geometry in teal (#108474) with white text. Both use `{typography.badge}` — 11px uppercase Barlow at 0.5px tracking. No rounded or circular badges exist in this system.

### Search Bar

**`search-bar`** — 40px input on a #2a2a2a dark fill with 2px radius and a magnifier icon in muted gray (#7b7b7b). On desktop, lives behind a search icon in the nav rail that expands the bar inline. On mobile, expands to full-width below the nav bar. Placeholder in muted (#7b7b7b); active text in on-dark (#eeeeee). No visible border in default state — the dark fill provides sufficient separation from the black nav.

### Bike Category Tile

**`bike-category-tile`** — 3:2 aspect-ratio image tiles with a 35% black overlay, zero radius, and a `{typography.display-sm}` DIN title in on-dark white. Hover applies 1.03 scale transform — responsive without animation-heavy. Used for the BIKES landing grid (Wreckoning, Following, Offering, Calling, Patron) as large-format navigational tiles rather than product cards.

### Footer

**`footer`** — Black ground (#121212) with a 1px top border in #2a2a2a. Column headings use `{typography.overline}` (teal on hover, muted default). Body links in Barlow 14px; hover state shifts to on-dark. A newsletter input row uses the `text-input` spec inline with a teal `button-primary` submit. Social icons sit flush at the bottom row in muted gray with on-dark hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger with full-screen black overlay; hero title scales to `display-md` (32px); hero CTA full-width; spec tables scroll horizontally; size selectors wrap to two columns |
| Tablet | 744–1128px | Two-column product grid; nav shows logo and hamburger only, no expanded link rail; hero at 70vh; bike category tiles in 2×2 grid |
| Desktop | 1128–1440px | Three-column product grid; full horizontal nav rail with all category links visible; hero at 85vh; bike category tiles in row of four |
| Wide | > 1440px | Max-width container (~1400px) centered on page; four-column product grid; nav rail gains lateral breathing room; hero photography remains full-bleed behind container bounds |

### Touch Targets

- All primary and accent buttons: 48px height minimum
- Size selector toggles: 44px height minimum
- Nav hamburger icon: 48×48px tap area including padding
- Color swatches: 28px visual diameter with 44px touch area via surrounding padding
- Product cards: full card surface is the tap target on mobile; no nested interactive elements
- Footer links: minimum 40px line-height for tappable link density

### Collapsing Strategy

- Navigation: full horizontal rail on desktop; icon-only hamburger at tablet and below; full-screen black overlay with stacked DIN links and slide-in animation at mobile
- Product filters: visible sidebar on desktop; collapsed behind a "FILTER" button on mobile/tablet opening a bottom sheet with checkbox lists and a full-width teal apply button
- Spec table: horizontal scroll container on mobile with the label column sticky at left; no content truncation
- Hero copy: display-xl title may wrap to two lines at tablet; collapses to display-md at mobile
- Bike category tile grid: 4-up row on desktop; 2-up grid on tablet; single full-width tiles stacked on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- DINWebPro-Black W01 Regular is a licensed Monotype webfont; fallback rendering on non-licensed environments and its exact weight-axis range are unconfirmed
- No explicit font-size breakpoint scale extracted — mobile type scaling is inferred from brand category conventions
- Hover and focus animation timing curves (duration, easing) not extractable from a static snapshot
- Nav height shrink behavior on scroll (possible sticky compression) not confirmed
- Product configurator and Build Kit selector internal UI structure not extracted
- Cart drawer and checkout styles not confirmed — dark-theme extension assumed but unverified
- #1c64f6 blue and social brand colors (#3b5998, #1da1f2, #dd4b39, #e60023, #0073b1) in the extracted palette are almost certainly from third-party widgets (social proof apps, login overlays), not Evil Bikes brand tokens — excluded from the design system accordingly
- #ffff00 and #fffb00 near-duplicate yellows may indicate multiple yellow variants in production; exact usage contexts unconfirmed
- Nunito Sans and Baskerville appear in the font stack extraction but no clear UI role identified — likely from review widgets (JudgemeIcons, JudgemeStar) or legacy page sections
