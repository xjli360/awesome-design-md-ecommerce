---
version: alpha
name: "Milk-Barn"
source_url: "https://milkbarnkids.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Milk-Barn stakes its entire color bet on one hue: a cornflower-periwinkle (#334fb4) that reads closer to the blue in a child's first crayon set than to any corporate palette. It lands on every primary button, every navigational anchor, and every active state — a single color shouldering the expressive work that other baby brands distribute across multiple pastels. The remainder of the palette is almost entirely negative space: four near-whites (#efefef, #e0e0e0, #f6f6f6, #f7f7f7) so tonally close they read as a single luminous field rather than distinct tones, leaving product photography — printed swaddles, snap-front rompers, hand-embroidered onesies — to carry all visual weight.

  Assistant, the brand's sole typeface, is a geometric humanist sans with open apertures that make it feel readable rather than styled. At 700 weight it anchors hero text without tipping into aggression; at 400 it produces body copy that disappears into the reading experience. The constraint of one typeface alongside one accent color is a discipline that shifts the brand's personality entirely into its textile prints and illustration work, keeping UI chrome quiet. The name itself — Milk-Barn — reaches for pastoral domesticity: cream, hay, clean cotton, the sense of something made with patience in a place that does not hurry.

  Structurally the site runs on Shopify with consistent soft rounding ({rounded.md} on product cards, {rounded.full} on age chips and pill badges) that echoes Assistant's own rounded letterforms. Flat surface cards sit on {colors.surface-card} behind {colors.hairline} borders with no drop shadows, keeping hierarchy scannable for gift-buyers navigating a densely merchandised catalog. The gift-occasion taxonomy — baby shower, first birthday, new sibling — reveals that the primary buyer often shops for someone else's child, which explains why age-range chips, occasion tags, and new-arrival flags sit prominently in the hierarchy without competing with the periwinkle primary CTA. Every layout decision defers to the products.

colors:
  primary: "#334fb4"
  primary-active: "#2a3f94"
  primary-disabled: "#b3bfdf"
  ink: "#1a1a1a"
  body: "#3d3d3d"
  muted: "#767676"
  hairline: "#e0e0e0"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-card: "#f6f6f6"
  surface-muted: "#efefef"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  label:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.6px
    textTransform: uppercase
  price:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-compare:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
    textDecoration: line-through
  button-md:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  announcement:
    fontFamily: "'Assistant', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1px

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
    borderRadius: "{rounded.sm}"
    padding: "14px 28px"
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    borderRadius: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    borderRadius: "{rounded.sm}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    borderRadius: "{rounded.sm}"
    padding: "13px 27px"
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    borderRadius: "{rounded.full}"
    padding: "10px 20px"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    borderRadius: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1.5px solid {colors.primary}"
    padding: "12px {spacing.base}"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 40px
    activeColor: "{colors.primary}"
    padding: "0 {spacing.xl}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.announcement}"
    padding: "10px {spacing.base}"
    textAlign: center
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderRadius: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    imageAspectRatio: "3/4"
    imageObjectFit: cover
    padding: "{spacing.sm}"
    titleTypography: "{typography.title-md}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.ink}"
    comparePriceTypography: "{typography.price-compare}"
    comparePriceColor: "{colors.muted}"
    gap: "{spacing.xs}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    ctaComponent: button-primary
    minHeight: 520px
    padding: "{spacing.section} {spacing.xl}"
    layout: split-left
  collection-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    borderRadius: "{rounded.xs}"
    padding: "4px 8px"
    position: absolute
    placement: top-left
  age-chip:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    borderRadius: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: "6px 12px"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: none
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    borderRadius: "{rounded.sm}"
    border: "1.5px solid {colors.hairline}"
    padding: "8px 14px"
    minWidth: 48px
    selectedBackgroundColor: "{colors.primary}"
    selectedTextColor: "{colors.on-primary}"
    selectedBorder: "1.5px solid {colors.primary}"
    unavailableTextColor: "{colors.muted}"
    unavailableTextDecoration: line-through
  gift-tag:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    borderRadius: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "5px 10px"
    iconSize: 14px
  newsletter-block:
    backgroundColor: "{colors.surface-soft}"
    headlineTypography: "{typography.display-sm}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    bodyColor: "{colors.body}"
    inputComponent: text-input
    ctaComponent: button-primary
    padding: "{spacing.section} {spacing.xl}"
    borderRadius: "{rounded.none}"
    layout: inline-row
  footer:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.body}"
    linkColor: "{colors.ink}"
    linkHoverColor: "{colors.primary}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.ink}"
    borderTop: "1px solid {colors.hairline}"
    padding: "{spacing.xxl} {spacing.xl}"
    columnGap: "{spacing.xl}"
    columns: 4

## Components

### Buttons

**`button-primary`** — The main CTA button fills with the brand's sole accent (#334fb4) and white type at 48px height with {rounded.sm} corners. Hover shifts to `{colors.primary-active}` (#2a3f94); disabled state fades to `{colors.primary-disabled}` and locks the cursor. No border is used — the fill alone carries the affordance signal.

**`button-secondary`** — An outlined variant on white canvas with a 1.5px border in the primary blue and matching text color. Shares the 48px height with button-primary so the two sit flush when paired on product detail pages. Interior padding reduces by 1px on each axis to compensate for the border.

**`button-ghost`** — A text-only link-style action with underline decoration and no background. Used for dismissals, secondary nav anchors, and "View all" affordances where a visible button would crowd the layout. Ink text color keeps it subordinate without hiding it.

**`button-pill`** — A full-radius pill in the primary blue, used for filter chips, promotional callouts, and inline category selectors. Smaller 13px type at 600 weight reads clearly at pill scale without requiring the full 48px height of the primary button.

### Form Inputs

**`text-input`** — 48px-tall field with a 1px hairline border and {rounded.sm} radius. Focus upgrades to a 1.5px primary-blue border with no background change, signaling active state without disrupting the white surface. Placeholder text renders in `{colors.muted}`.

### Navigation

**`nav-bar`** — 64px sticky header on `{colors.canvas}` separated from page content by a single 1px hairline. Logo sits left at up to 40px height; primary nav links use `{typography.nav-link}` at 600 weight; the active page highlights in `{colors.primary}`. On mobile the link cluster collapses into a hamburger drawer that overlays from the left.

**`announcement-bar`** — Full-width banner above the nav in `{colors.primary}` with white centered text at 13px/500. Used for free-shipping thresholds, seasonal promotions, and new-collection alerts. Single line only; secondary messaging is hidden below 744px.

### Product Display

**`product-card`** — A 3:4 aspect-ratio product tile on `{colors.surface-card}` with {rounded.md} corners and a 1px `{colors.hairline}` border. No drop shadow — hierarchy is communicated through surface color alone. The image occupies the upper four-fifths of the card; title, price, and any compare-price stack below with {spacing.xs} gap. Collection badges float over the image's top-left corner.

**`collection-badge`** — A small rectangular flag rendered in `{typography.label}` — 11px, uppercase, 700 weight — in white on the primary blue. Positioned absolutely in the product card image corner. Can be recolored per promotional event, but the primary blue is the default and the most common variant.

**`age-chip`** — Pill-shaped filter chip for age ranges (0–3M, 3–6M, 6–12M, 1–2Y, 2–4Y). Resting state is `{colors.caption}` text on `{colors.surface-muted}` with a hairline border. Selected state fills the chip with `{colors.primary}` and white text, dropping the border entirely. Chips on mobile scroll horizontally with momentum.

**`size-selector`** — Square-ish outlined size buttons. Default: 1.5px hairline border with ink text. Selected: primary blue fill, white text, primary-colored border. Unavailable sizes keep the outline but render text in `{colors.muted}` with a strikethrough — communicating stock status without hiding the option.

**`gift-tag`** — A soft gray chip used for occasion labels such as Baby Shower, First Birthday, or New Sibling. Carries a small icon prefix at 14px. Non-interactive — decorative metadata that helps a gift-buyer scan the catalog by occasion without leaving the grid.

### Marketing Blocks

**`hero-banner`** — Full-width split-left section on `{colors.surface-soft}` with text column left and product image right. Headline uses `{typography.display-xl}` at 40px/700; supporting body at `{typography.body-md}`. The CTA is always a `button-primary`. Minimum 520px tall on desktop; below 744px the layout stacks image above text.

**`newsletter-block`** — Pre-footer section on `{colors.surface-soft}` with a headline at `{typography.display-sm}`, a short descriptor at `{typography.body-sm}`, a single `text-input` field, and a `button-primary` arranged inline on desktop. Below 744px the row stacks vertically with full-width input and button.

### Footer

**`footer`** — Sits on `{colors.surface-muted}` with a top hairline. Four-column grid on desktop: About, Shop, Help, and Social. Column headings use `{typography.title-sm}` at 600 weight; links use `{typography.body-sm}` in `{colors.ink}` with a hover color shift to `{colors.primary}`. No underline on hover — color transition alone signals interactivity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero stacks image above text; age chips scroll horizontally; announcement bar condenses to single line |
| Tablet | 744–1128px | Two-column product grid; nav shows abbreviated link set with overflow in drawer; hero switches to 50/50 split layout; filter chips wrap rather than scroll |
| Desktop | 1128–1440px | Three- or four-column product grid; full horizontal nav with all category links visible; filter rail appears as persistent left sidebar on collection pages |
| Wide | > 1440px | Grid constrained to max-width ~1400px and centered; side margins grow proportionally; hero image scales with crop adjustment to avoid excessive whitespace |

### Touch Targets

- All interactive elements maintain a minimum 44×44px touch target
- Size selector buttons expand padding on mobile to meet minimum target height even at small label sizes
- Age chips maintain at least 36px height; horizontal scroll container has `-webkit-overflow-scrolling: touch` for momentum
- Nav hamburger hit area extends to 48×48px beyond the visible icon bounds
- Product card taps register on the full card surface, not just the image or title link

### Collapsing Strategy

- Hero transitions from split-left (text left, image right) to stacked (image top, text bottom) below 744px
- Product grid steps from four columns → three → two → one as breakpoints decrease
- Filter rail converts from persistent left sidebar to a bottom-sheet modal on mobile, triggered by a "Filter" pill button fixed above the grid
- Footer collapses from four columns to a single-column accordion list on mobile, with each section heading acting as a toggle
- Announcement bar reduces font size from 13px to 12px below 375px and hides any secondary promotional line

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only five hex values were extracted; the site likely loads additional palette tokens (sale red, success state, secondary accent) via JavaScript — none were capturable
- Text colors for ink, body, and muted were not present in the extraction and have been derived from standard white-canvas conventions; verify against live site computed styles
- Primary-active (#2a3f94) and primary-disabled (#b3bfdf) are algorithmically derived by darkening and lightening the extracted primary; not confirmed from source
- No secondary or complementary accent colors identified — illustration banners and seasonal campaigns may introduce colors absent from the core CSS
- Sale and promotional overlay badge colors are unconfirmed; likely a red or coral variant but unverifiable from available extraction
- Animation and transition durations for hover states, drawer open/close, and carousel slides could not be extracted
- Icon system style (line weight, filled vs. outlined, corner style) not documented
- Exact border-radius values are unconfirmed; {rounded.md} (12px) on cards is inferred from visual category conventions, not measured
- Whether Assistant is loaded as a variable font or static weights is unconfirmed — weight range in use across the site could not be verified from extraction alone
