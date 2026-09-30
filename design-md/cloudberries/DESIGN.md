---
version: alpha
name: "Cloudberries"
source_url: "https://www.cloudberries.co.uk"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fraunces carries the Cloudberries brand at every header — an optical variable serif that swells and contracts through its axis like 1890s book typography, entirely at odds with the blunt sans-serifs that dominate Shopify puzzle storefronts. Against a warm unbleached-linen canvas (#eeece7), the display characters lean into letterpress-era contrast ratios, making each collection name feel titled rather than labeled. The true brand primary is a dense forest teal (#108474) — not the chalky mint or Instagram sage saturating the leisure category, but something closer to vintage cartographer's ink or old Japanese lacquer. It reads as authoritative and slightly archival, exactly the register for a brand positioning jigsaw puzzles as slow, deliberate adult pleasure. Geometry is almost uniformly rectilinear: buttons carry `{rounded.none}`, the product grid drops sharp-cornered image tiles, and input fields forgo the softening radius standard to Shopify themes. The only intentional curves appear in piece-count and difficulty pill badges (`{rounded.full}` and `{rounded.xs}` respectively) — a studied exception that makes those pills read as labels against an otherwise flat-edged layout. Golden amber (#dfb734) appears on gift and difficulty markers, warm enough to signal premium without the preciousness of metallics. The double-font system draws a clean editorial split: Fraunces handles all emotive weight — display headlines, product names, the large piece-count selectors on the product detail page — while Futura Web manages the information layer, running navigation labels, captions, buttons, and filter tabs in tracked uppercase at small sizes, exactly as a well-designed art book separates running heads from body text. Blush surfaces (#ebdde2, #ffe5e0, #fff1e3) serve as soft tonal backdrops in featured and gifting sections, keeping the palette warm across a full scroll without competing with the teal CTAs. A near-black footer (#2a2a2a) closes the page firmly, reversing canvas text out against the dark ground.

colors:
  primary: "#108474"
  primary-active: "#0a6357"
  primary-disabled: "#8cbdb8"
  ink: "#2a2a2a"
  body: "#50463e"
  muted: "#7b7b7b"
  muted-soft: "#9e9e9e"
  hairline: "#dedede"
  hairline-soft: "#e2e2e2"
  canvas: "#eeece7"
  surface-soft: "#ebdde2"
  surface-card: "#fafafa"
  surface-blush: "#ffe5e0"
  surface-warm: "#fff1e3"
  on-primary: "#ffffff"
  accent-amber: "#dfb734"
  accent-brick: "#de3813"
  accent-sage: "#506c64"
  accent-mauve: "#584450"
  deep-amber: "#412d00"

typography:
  display-xl:
    fontFamily: "'Fraunces', 'fraunces-variable', serif"
    fontSize: 60px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Fraunces', serif"
    fontSize: 44px
    fontWeight: 300
    lineHeight: 1.12
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Fraunces', serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Fraunces', serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Futura Web', 'futura-pt', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  title-sm:
    fontFamily: "'Futura Web', 'futura-pt', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  body-md:
    fontFamily: "'Futura Web', 'futura-pt', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0.01em
  body-sm:
    fontFamily: "'Futura Web', 'futura-pt', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Futura Web', 'futura-pt', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.06em
  caption-sm:
    fontFamily: "'Futura Web', 'futura-pt', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.04em
  button-md:
    fontFamily: "'Futura Web', 'futura-pt', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.14em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Futura Web', 'futura-pt', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Futura Web', 'futura-pt', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.1em
    textTransform: uppercase
  piece-count:
    fontFamily: "'Fraunces', serif"
    fontSize: 22px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: 0
  price:
    fontFamily: "'Futura Web', 'futura-pt', sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.02em
  price-lg:
    fontFamily: "'Fraunces', serif"
    fontSize: 28px
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
    padding: "14px 32px"
    height: 48px
    hoverBackgroundColor: "{colors.primary-active}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    height: 48px
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: "13px 31px"
    height: 48px
    hoverBackgroundColor: "{colors.primary}"
    hoverTextColor: "{colors.on-primary}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    padding: "13px 31px"
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "12px 16px"
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    logoTypography: "{typography.display-sm}"
    logoColor: "{colors.body}"
  announcement-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    linkColor: "{colors.on-primary}"
    linkDecoration: underline
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    padding: "0"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.caption}"
    subtitleColor: "{colors.muted}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.body}"
    gap: "{spacing.sm}"
  hero:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-xl}"
    headlineColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.body}"
    ctaStyle: "button-primary"
    layout: "split-image-right"
    paddingVertical: "{spacing.section}"
  puzzle-size-selector:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    border: "1px solid {colors.hairline}"
    activeBorder: "1px solid {colors.primary}"
    typography: "{typography.piece-count}"
    rounded: "{rounded.none}"
    height: 52px
    minWidth: 88px
    padding: "0 {spacing.base}"
  piece-count-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  difficulty-badge:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.deep-amber}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.xs}"
    padding: "3px 10px"
  category-filter:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    activeBorderBottom: "2px solid {colors.primary}"
    inactiveBorderBottom: "2px solid transparent"
    typography: "{typography.nav-link}"
    padding: "{spacing.sm} 0"
    gap: "{spacing.xl}"
  collection-grid:
    columns: 3
    mobileColumns: 2
    tabletColumns: 2
    gap: "{spacing.lg}"
    rowGap: "{spacing.xl}"
  gift-wrap-toggle:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.accent-amber}"
    rounded: "{rounded.xs}"
    padding: "{spacing.base}"
    iconColor: "{colors.accent-amber}"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    height: 44px
    padding: "0 {spacing.base}"
    iconColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    linkColor: "{colors.canvas}"
    linkHoverColor: "{colors.primary-disabled}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.canvas}"
    padding: "{spacing.xxl} 0"
    hairlineColor: "#3a3a3a"

## Components

### Buttons

**`button-primary`** — Flat-cornered (`{rounded.none}`) teal block at 48px height, carrying the brand's forest teal (#108474) fill against white text at 13px tracked-uppercase Futura. On hover the fill deepens to #0a6357 with no transition delay, matching the brand's direct, unhurried disposition. Disabled state uses `{colors.primary-disabled}`, a washed-out teal that retains the hue family without implying interactivity.

**`button-secondary`** — Transparent fill with a 1.5px teal border and teal text; on hover inverts to full teal fill, mirroring `button-primary`. Used for secondary CTAs on collection pages and the "Add to wishlist" affordance.

**`button-ghost`** — Hairline-bordered, ink-colored; appears on filters, dismissal actions, and modal close targets. No fill change on hover — border color shifts to `{colors.ink}`.

### Nav Bar

**`nav-bar`** — 60px-tall bar in warm canvas (#eeece7) with a single 1px hairline underline. The wordmark runs in Fraunces at `{typography.display-sm}` weight 400 — not bold, trusting the serif's distinctive optical texture over weight. Navigation labels use Futura at `{typography.nav-link}`, all-caps, light-tracked, at 12px — the same size as legal fine print on a luxury product box, intentionally understated.

**`announcement-bar`** — Stacked above the nav in `{colors.primary}` teal, reversing caption-weight Futura text to white. Typically carries free-shipping thresholds or seasonal promotions; the teal strip gives the page a colored band before the cream canvas opens below.

### Product Card

**`product-card`** — Flush square image tile (1:1 aspect) with no rounding, dropping directly to a tight two-line text block: product name in `{typography.body-sm}` ink, piece count as a `{typography.caption}` muted line, then price in `{typography.price}`. The piece-count badge overlays the image corner rather than sitting in the text stack on featured cards — a pill in blush surface (#ebdde2) with `{rounded.full}`.

### Hero

**`hero`** — Split layout: editorial headline in `{typography.display-xl}` Fraunces at weight 300 occupies the left half; the puzzle artwork photograph bleeds to the right edge. Subhead runs in `{typography.body-md}` Futura at `{colors.body}` brown, creating a warm reading tone against the cream canvas. A single `button-primary` CTA anchors the bottom of the text column.

### Puzzle Size Selector

**`puzzle-size-selector`** — Horizontal button group for piece counts (e.g. 500, 1000, 1500). Each tile is flush-cornered (`{rounded.none}`), 52px tall, min-width 88px, text rendered in Fraunces at `{typography.piece-count}` weight 300. The selected count fills in `{colors.primary}` teal; unselected tiles show a hairline border only. The Fraunces numeral weight gives piece-count selection an editorial quality, treating "1000" as a named edition rather than a size option.

### Category Filter

**`category-filter`** — A horizontal row of all-caps Futura tabs (`{typography.nav-link}`) spaced at `{spacing.xl}` gaps. Active tab underlines with a 2px teal stroke; inactive tabs show a transparent underline placeholder to prevent layout shift. No pill or fill — consistent with the flat, rectilinear layout discipline.

### Difficulty & Piece Count Badges

**`difficulty-badge`** — Amber-filled (`{colors.accent-amber}`) pill with xs rounding (`{rounded.xs}`), text in deep-amber (#412d00) at `{typography.title-sm}`. Levels (e.g. "Relaxed," "Moderate," "Challenging") communicate puzzle complexity; the warm gold signals warmth and approachability even at the hard tier.

**`piece-count-badge`** — Blush-surface (`{colors.surface-soft}`) full-radius pill at `{typography.title-sm}`, body-colored text. Sits as an image overlay on featured product tiles; smaller than the difficulty badge, functioning as a catalog identifier rather than a quality signal.

### Gift Wrap Toggle

**`gift-wrap-toggle`** — A bordered selection tile in `{colors.surface-warm}` (#fff1e3) with a 1px amber border, body-weight Futura body-sm text, and an amber icon. Used on the cart/PDP as an opt-in gift service toggle. The warm honeyed surface and amber border quietly echo the gifting occasion without shouting; xs-rounded corners are the sole exception to the flat-corner system.

### Search Bar

**`search-bar`** — 44px-tall flush input in off-white surface-card (#fafafa), hairline-bordered, no rounding. A muted magnifier icon sits at the left interior edge. Placeholder text in `{colors.muted-soft}` (#9e9e9e); active focus state shifts border to `{colors.primary}`.

### Footer

**`footer`** — Near-black (#2a2a2a) ground reversing all text and links to canvas (#eeece7). Column headers in `{typography.title-sm}` Futura tracked-uppercase; link text in `{typography.body-sm}`. Internal horizontal rules use a slightly lighter #3a3a3a to separate sections without harsh contrast. The Cloudberries wordmark reappears in Fraunces at `{typography.display-md}` weight 300, anchoring the bottom of the page with the same low-key serif presence as the top nav.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Collection grid collapses to 2 columns; hero switches to stacked layout (image above text); nav becomes hamburger drawer; piece-count selector scrolls horizontally |
| Tablet | 744–1128px | 2-column collection grid; hero split layout retained but text column widens to 55%; announcement bar text truncates to single message |
| Desktop | 1128–1440px | 3-column collection grid; full nav links visible; hero split 50/50; puzzle-size-selector displayed as inline row |
| Wide | > 1440px | Max content width caps at 1440px with symmetric side gutters; hero image side scales proportionally; collection grid remains 3-column with increased card size |

### Touch Targets

- All interactive controls (buttons, size-selector tiles, filter tabs) maintain minimum 44px height on mobile
- Puzzle size-selector tiles expand to full-width on mobile, stacking vertically at 52px each
- Category filter tabs scroll horizontally behind a fade mask at narrow widths; tap target pad extends to `{spacing.lg}` above and below the label

### Collapsing Strategy

- Nav collapses to wordmark + hamburger icon at < 744px; drawer slides from right over canvas overlay
- Hero text block stacks above image at mobile breakpoint; `display-xl` font-size reduces to 38px
- Footer columns collapse from 4-column grid to 2-column at tablet, single-column at mobile
- Announcement bar maintains full teal strip at all breakpoints but truncates to the single highest-priority message on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No `meta theme-color` tag present; browser chrome color on mobile cannot be confirmed from extraction
- The hex values #5d6ac0 (slate blue) and #8e24aa (deep purple) appeared in extraction but their semantic role is unclear — possibly Shopify UI injections, review-star widgets, or dynamic badge colors rather than brand-defined tokens
- Exact Fraunces variable axis settings (optical size, weight range) used in production could not be confirmed; weight 300 ("Fraunces Light") is inferred from the `Fraunces Light` font-family string in extraction
- Hover/focus animation timing (transition duration and easing) was not extractable from static scrape
- Whether piece-count selector uses Fraunces or Futura in the live PDP is inferred from brand logic, not confirmed from DOM inspection
- Specific image hover behavior on product cards (zoom, overlay, second-image swap) could not be determined
- The `#8e24aa` purple may indicate a Judgeme or third-party review widget and is excluded from brand tokens accordingly
