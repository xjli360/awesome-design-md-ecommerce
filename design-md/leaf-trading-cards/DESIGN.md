---
version: alpha
name: "Leaf Trading Cards"
source_url: "https://www.leaftradingcards.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Dharma Gothic E — the condensed-slab display face built for newspaper sports sections and stadium program covers — runs Leaf's entire headline hierarchy, from 80px hero lockups down to the 10px serial-number stamps that identify numbered parallel inserts, and this single typographic choice signals exactly who the customer is: the collector who reads card backs and knows what "1/1" means. The crimson (#c73226) has the unmistakable saturation of freshly printed sports-logo ink rather than a digital brand accent — it appears on every purchase button, presale callout, and serial badge, a concentrated signal that the system's energy is focused on availability and acquisition. Beneath it, the deep maroon (#420500) holds pressed states and hero overlays, giving interactions a felt sense of depth without introducing a third hue. Forma DJR Text handles body copy and navigation links with neutral precision that keeps the catalog scannable across Hobby, Retail, Multi-Sport, and Celebrity segments — the contrast between compressed Gothic display and upright humanist body text creates a visual hierarchy that resolves quickly at both desktop and mobile reading distances. Subway Berlin Std appears in footer headings and departmental wayfinding, lending a transit-map authority to category nomenclature. Product cards lock to a 2.5:3.5 aspect ratio that mirrors the physical trading card format; serial badges pin at {rounded.xs} to the lower-right corner in {colors.primary}, and the canvas stays white throughout — the system trusts card photography to carry visual weight and uses the two brand colors as punctuation rather than atmosphere. Category filter chips run as {rounded.full} pills below the nav bar; structural card surfaces hold at {rounded.xs} so the grid reads as organized and direct, a signal to serious buyers that the catalog is what matters.

colors:
  primary: "#c73226"
  primary-active: "#a02218"
  primary-disabled: "#e9a49f"
  deep: "#420500"
  deep-hover: "#2c0300"
  ink: "#1a1a1a"
  body: "#3c3c3c"
  muted: "#6e6e6e"
  hairline: "#e0e0e0"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-dark: "#0e0101"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'dharma-gothic-e', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 80px
    fontWeight: 800
    lineHeight: 0.9
    letterSpacing: -2px
    textTransform: uppercase
  display-lg:
    fontFamily: "'dharma-gothic-e', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 0.95
    letterSpacing: -1px
    textTransform: uppercase
  display-md:
    fontFamily: "'dharma-gothic-e', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'dharma-gothic-e', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 0
  title-md:
    fontFamily: "'forma-djr-text', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'forma-djr-text', 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'forma-djr-text', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'forma-djr-text', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'forma-djr-text', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  badge:
    fontFamily: "'dharma-gothic-e', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'dharma-gothic-e', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'dharma-gothic-e', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  nav-link:
    fontFamily: "'forma-djr-text', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  serial-label:
    fontFamily: "'dharma-gothic-e', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 10px
    fontWeight: 800
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  subway-label:
    fontFamily: "'subway-berlin-std', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 1.5px
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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 10px 26px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    logoType: "{typography.display-sm}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "2.5/3.5"
    titleType: "{typography.title-sm}"
    priceType: "{typography.title-md}"
    shadow: "0 2px 8px rgba(0,0,0,0.07)"
  hero-banner:
    backgroundColor: "{colors.deep}"
    textColor: "{colors.on-dark}"
    titleType: "{typography.display-xl}"
    subtitleType: "{typography.display-sm}"
    scrimColor: "{colors.scrim}"
    minHeight: 520px
  serial-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.serial-label}"
    rounded: "{rounded.xs}"
    padding: 2px 6px
    position: bottom-right
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-chip-inactive:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  pack-label:
    backgroundColor: "{colors.deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  presale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 42px
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.deep}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.primary-disabled}"
    headingType: "{typography.subway-label}"
    bodyType: "{typography.body-sm}"
    divider: "1px solid {colors.hairline}"
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — The primary CTA uses {colors.primary} crimson (#c73226) with {typography.button-md} dharma-gothic-e uppercase at 1.5px letter-spacing, giving purchase actions the assertive energy of sports-print headlines. Active state depresses to {colors.primary-active} (#a02218); disabled washes to {colors.primary-disabled}. {rounded.sm} keeps the corner sharp enough to read as direct without softening into a consumer-product pill shape.

**`button-secondary`** — A 2px crimson border outline on {colors.canvas} white, matching the primary's height and type scale for visual parity in side-by-side CTA contexts. Signals "available alternative" without competing with the filled crimson primary — use for wishlist, share, or secondary cart actions.

**`button-ghost`** — Transparent background with {colors.ink} text in {typography.button-sm}, no border. Used for low-priority inline actions like "View All" at the bottom of category rows. Relies on surrounding context to signal interactivity.

### Inputs

**`text-input`** — A {colors.canvas} field with a {colors.hairline} border that transitions to {colors.primary} on focus, reinforcing crimson as the system's universal interaction signal. {typography.body-md} forma-djr-text keeps form fields legible and typographically neutral against the high-energy display faces elsewhere on the page.

**`search-bar`** — A slightly recessed {colors.surface-soft} field at {rounded.sm}, carrying lower visual weight than the bordered text-input. Appropriate for inline placement in the nav area. The icon renders in {colors.muted} and transitions to {colors.ink} on activation.

### Navigation

**`nav-bar`** — A 64px {colors.canvas} bar with a {colors.hairline} bottom border, logo lockup in {typography.display-sm} dharma-gothic-e, and category links in {typography.nav-link} forma-djr-text. The contrast between the compressed Gothic logo and the lighter humanist nav links creates a clear visual anchor point. On mobile the nav collapses to a hamburger at the right edge, with the search icon persistent at all breakpoints.

### Product

**`product-card`** — Cards lock to a 2.5:3.5 aspect ratio matching the physical trading card format — the most brand-specific layout constraint in the system and the detail that immediately communicates collector intent. A {colors.hairline-soft} border on {colors.surface-card} separates tiles on white backgrounds without the overhead of a drop shadow. Set name renders in {typography.title-sm} above the price in {typography.title-md}; `serial-badge` and `pack-label` overlay the card image at fixed corner positions and are always present when applicable.

### Heroes & Banners

**`hero-banner`** — Full-width banner with a {colors.deep} maroon (#420500) base layer and an optional scrim ({colors.scrim}) over photographic backgrounds, reserving crimson exclusively for the CTA button placed within the hero frame. {typography.display-xl} dharma-gothic-e at 80px uppercase dominates; subtitle and set-release context drop to {typography.display-sm}. The 520px minimum height ensures card photography reads at full photographic scale rather than being cropped to a letterbox strip.

### Badges & Labels

**`serial-badge`** — A tight {colors.primary} crimson chip at {rounded.xs} pinned to the lower-right corner of a product card image, stamping the card's serial designation (e.g. "27/99", "1/1") in {typography.serial-label} dharma-gothic-e at 10px uppercase. This is the most collector-specific UI element in the system: print-run numbering is the primary driver of secondary-market card value and must be immediately visible at thumbnail scale.

**`category-chip-active`** / **`category-chip-inactive`** — {rounded.full} filter pills run in a horizontally scrollable rail below the nav bar on mobile and as a top-of-grid filter row on desktop. Active state fills {colors.primary} crimson with {colors.on-primary} white type; inactive rests on {colors.surface-soft} with {colors.body} text. Both use {typography.badge} dharma-gothic-e for consistent compressed-Gothic label energy throughout the filter interface.

**`pack-label`** — A small {colors.deep} maroon chip designating product format: Hobby, Retail, Collector, or Blaster. Sits at the upper-left corner of the card tile image. Uses {typography.badge} at the same typographic scale as the serial badge, keeping the two label types distinguishable by color (maroon vs. crimson) while sharing a visual language.

**`presale-badge`** — Identical geometry to `pack-label` but in {colors.primary} crimson, placed at the upper edge of a product tile to flag pre-release product. The crimson color creates an automatic visual association with the purchase CTA, signaling that action is available even before the product ships.

### Footer

**`footer`** — {colors.deep} maroon (#420500) background with {colors.on-dark} body copy and {colors.primary-disabled} washed-crimson links — muted enough to prevent the footer from competing with in-page CTAs while maintaining brand-color continuity. Column headings render in {typography.subway-label} subway-berlin-std uppercase with 1.5px letter-spacing, a nod to the transit-system categorical logic that organizes Hobby, Retail, and Celebrity product lines. Body copy uses {typography.body-sm} forma-djr-text; sections are separated by a {colors.hairline} divider at reduced opacity against the dark ground.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | 2-column product grid; hamburger nav; horizontal-scroll category chip rail below nav bar; hero text stacked over full-bleed card imagery with scrim |
| Tablet | 744–1128px | 3-column product grid; condensed nav with primary category links visible; chip rail above grid; sidebar filters collapse to a modal bottom sheet |
| Desktop | 1128–1440px | 4-column product grid; full nav bar with all category and segment links; left-sidebar filter panel on collection pages |
| Wide | > 1440px | Container max-width 1440px with wider gutters; 4-column grid maintained with proportionally larger card tile areas |

### Touch Targets
- All interactive buttons and inputs maintain a minimum 44px height
- Category chip pills minimum 36px tall with 8px vertical padding on mobile
- Serial and presale badges are display-only overlays — no tap target required
- Hamburger menu list items maintain a minimum 48px vertical hit area
- Product card tap target covers the full tile; badge overlays do not create separate targets

### Collapsing Strategy
- Desktop left-sidebar filters → horizontal scroll chip rail on tablet → full-width chip rail on mobile
- Product grid: 4-col desktop → 3-col tablet → 2-col mobile (card aspect ratio preserved at every breakpoint)
- Hero text block: right-aligned text over left-anchored image on desktop → stacked with text over scrim on mobile
- Pack-label and serial-badge remain visible at all breakpoints; type scale does not reduce below 10px
- Footer columns: 4-col desktop → 2-col tablet → 1-col stacked mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only 2 hex colors extracted (#c73226, #420500); all neutral and state-variant tokens (ink, muted, hairline, surface, canvas) are industry-standard derivations, not confirmed from the live site
- Gold, silver, or holographic foil-accent palette for parallel card grades not present in extraction — foil treatment likely handled via image assets or CSS shimmer rather than solid color tokens
- Exact border-radius values unconfirmed; {rounded.xs} for product cards is inferred from Shopify platform defaults and collector-market category conventions
- Specific nav structure, top-level category count, and dropdown behavior not confirmed from extraction
- Animation and transition values (card hover scale, badge entrance, hero carousel timing) not extracted
- Dark mode support unknown; extracted tokens contain no dark-surface variants beyond the deep maroon
- Subway Berlin Std usage scope inferred from font stack presence — exact component placements not confirmed from live site observation
