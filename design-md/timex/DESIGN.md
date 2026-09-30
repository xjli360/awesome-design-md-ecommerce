---
version: alpha
name: "Timex"
source_url: "https://www.timex.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Seventy years of the same red against near-black, and the formula still holds. Timex presses #bd3d44 — a brick-red that sits warmer than a stoplight and cooler than blood — into every primary CTA, sale callout, and promotional banner without apology. The near-black ink layer (#222222, bottoming at #121212) claims navigation, product names, and price display, while warm grays (#dedede, #dadada, #e4e4e4) fill hairlines and card surfaces; the page canvas settles at #f4f4f4 rather than pure white, reading like lightly aged paper without committing to nostalgia. Where the brand breaks from this two-tone spine is in product-line color coding — IRONMAN sport models arrive in school-bus yellow (#ffde17), diving-adjacent watches carry deep navy (#005385), field and military pieces get hunter green (#0b8642), and the heritage leather-strap catalog wears a warm brown (#6c4332). Badge backgrounds echo these hues in blush (#fcd6d7) and sage (#d3efcd), so categorical signals repeat at chip scale without reading as warning labels. Typography does the heaviest lifting of any design decision: Arizona, a high-contrast serif with editorial authority, handles display and hero headlines; ArizonaSans steps in for navigation and mid-hierarchy labels; Plain carries body copy and functional UI. The combination explains why a catalog of sub-$100 watches reads closer to a design magazine than a department store circular. Components carry {rounded.xs} across buttons and form inputs — near-square, no pill softness, no organic curves — and {rounded.sm} on cards. That angular discipline communicates something about the product promise: a watch that survives a construction site at $49.95 shouldn't live inside a gradient.

colors:
  primary: "#bd3d44"
  primary-active: "#c72e2f"
  primary-dark: "#d12027"
  primary-disabled: "#fcd6d7"
  yellow-sport: "#ffde17"
  navy-dive: "#005385"
  green-field: "#0b8642"
  green-vivid: "#1b9500"
  brown-heritage: "#6c4332"
  surface-pink: "#fcd6d7"
  surface-green: "#d3efcd"
  ink: "#222222"
  ink-dark: "#121212"
  body: "#1a1919"
  muted: "#717171"
  hairline: "#dedede"
  hairline-mid: "#dadada"
  hairline-soft: "#e4e4e4"
  canvas: "#ffffff"
  surface-soft: "#f4f4f4"
  surface-card: "#f1f0f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arizona, Georgia, serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arizona, Georgia, serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.3px
  display-md:
    fontFamily: "Arizona, Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "Arizona, Georgia, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.22
    letterSpacing: 0
  title-md:
    fontFamily: "ArizonaSans, arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "ArizonaSans, arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.1px
  body-md:
    fontFamily: "Plain, ArizonaSans, arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Plain, ArizonaSans, arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Plain, ArizonaSans, arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.1px
  caption-upper:
    fontFamily: "ArizonaSans, arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "ArizonaSans, arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "ArizonaSans, arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "ArizonaSans, arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "ArizonaSans, arial, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "ArizonaSans, arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  badge-label:
    fontFamily: "ArizonaSans, arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
  button-ghost-red:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  button-ghost-red-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  nav-bar-promo:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    height: 40px
    padding: "0 {spacing.base}"
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    borderTop: "2px solid {colors.primary}"
    padding: "{spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    imageBg: "{colors.surface-soft}"
    padding: "{spacing.base}"
  product-card-name:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price-display}"
    textColor: "{colors.ink}"
  product-card-sale-price:
    typography: "{typography.price-display}"
    textColor: "{colors.primary}"
  product-card-original-price:
    typography: "{typography.price-sm}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  hero-dark:
    backgroundColor: "{colors.ink-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 540px
  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  hero-red:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    minHeight: 480px
  line-badge-sport:
    backgroundColor: "{colors.yellow-sport}"
    textColor: "{colors.ink-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  line-badge-dive:
    backgroundColor: "{colors.navy-dive}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  line-badge-field:
    backgroundColor: "{colors.green-field}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  line-badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  line-badge-heritage:
    backgroundColor: "{colors.brown-heritage}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  filter-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-tab:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid transparent"
    padding: "10px 0"
  category-tab-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline-mid}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: 10px 14px
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderActive: "2px solid {colors.ink}"
    borderInactive: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.caption-upper}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"

## Components

### Buttons

**`button-primary`** — The workhorse CTA, #bd3d44 background with white text on a near-square {rounded.xs} radius. All-caps ArizonaSans at 14px/700 tracked 0.6px reads clearly at arm's length in a product grid. Hover drops to the darker #c72e2f; disabled state bleaches to the blush #fcd6d7 and dims text to muted gray, preserving the button shape and implying the action rather than removing it.

**`button-secondary`** — White background, ink text, 1px hairline border, same {rounded.xs} corners as primary. Hover shifts the background to #f4f4f4 and promotes the border to ink — a minimal state change that doesn't compete with the red CTA hierarchy. Deployed for secondary PDP actions and modal confirmations.

**`button-ghost-red`** — Transparent button, 1px #bd3d44 border, red text at rest; fills solid red on hover. Used inside dark hero banners and promotional overlays where a filled red block would disappear against a red or near-black background. The ghost-to-filled transition is the only animated brand moment on the page.

### Navigation

**`nav-bar`** — 64px canvas strip with a 1px hairline border-bottom, ArizonaSans 14px weight-500 links at ink. A `nav-bar-promo` strip sits above at 40px in #bd3d44 with uppercase caption-upper text announcing shipping thresholds or sale events. The `nav-dropdown` panel opens below the nav rail with a 2px red top accent and a white interior: category headings in caption-upper stacked above body-sm links, no internal card borders or dividers — the red top stripe does all the framing.

### Product Card

**`product-card`** — Light gray surface (#f1f0f0) with {rounded.sm} corners and {spacing.base} padding. Product image sits against a slightly lighter #f4f4f4 zone to separate it from the card shell without a visible border. Name renders in title-sm at ink weight; price in price-display at 18px/700. On sale items the current price renders in #bd3d44 and the original price appears alongside in 14px struck-through muted gray. Line badges pin to the top-left of the image area.

### Hero Banners

**`hero-dark`** — The primary campaign surface: #121212 background, white headline in Arizona 52px/700, body copy in Plain 16px, minimum 540px tall. **`hero-light`** swaps to #f4f4f4 for editorial collection pages and seasonal look-books where photography needs a neutral surround. **`hero-red`** deploys #bd3d44 as the full background — reserved for IRONMAN launch events and sitewide promotions where the primary color needs maximum surface area, with white headline and body overriding the default ink.

### Line Badges

**`line-badge-sport`** — School-bus yellow (#ffde17) with near-black ink text at badge-label scale (10px/700/uppercase/1px tracked). Carries the IRONMAN visual identity down to its smallest unit. **`line-badge-dive`** runs navy (#005385) with white text; **`line-badge-field`** runs hunter green (#0b8642) with white; **`line-badge-heritage`** wears the warm brown (#6c4332) with white. All share {rounded.xs} and identical typography — the hue alone differentiates the product family. The system works because the four hues are saturated enough to carry legibility at 10px without an added border or drop shadow.

### Filters and Tabs

**`filter-pill`** — A {rounded.full} pill on the warm-gray surface-soft with a hairline border and uppercase 12px ArizonaSans. Active state (`filter-pill-active`) fills to near-black ink with white text rather than red — a deliberate choice so multiple active filters don't produce a red cascade across the filter bar. **`category-tab`** and **`category-tab-active`** use a bottom-border underline in #bd3d44 to signal the active collection, keeping the tab row typographically stable while the red underline supplies the selection signal.

### Search

**`search-bar`** — 44px height, #f4f4f4 background, hairline-mid border, {rounded.xs} corners. Focus promotes the border to ink rather than red — a deliberate restraint that keeps search interaction neutral and reserves #bd3d44 for purchase-driving moments. The input lives in the nav on desktop and migrates into the hamburger drawer on mobile.

### Color Swatches

**`color-swatch`** — 24px circles with a 1px hairline border at rest; active swatch gains a 2px ink border that rings the chip without a gap, using a box-shadow offset to leave a thin white halo between fill and border. No red used in the swatch selection state — keeping the selection signal brand-neutral prevents conflicts when a swatch itself is red.

### Footer

**`footer`** — #121212 background, white text throughout. Column headings in caption-upper (11px/700/uppercase/1.2px tracked) stack above body-sm links at 14px. Link hover adds a white underline rather than a color change — the footer runs quiet, nothing competes with the product grid above. Social icons, legal copy, and subsidiary navigation sit in the same typographic tier.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + cart icon; promo bar persists at 40px; product grid drops to 2 columns; hero headlines scale from 52px to 28px Arizona; filter pills switch to horizontal scroll; PDP images go full-bleed edge to edge |
| Tablet | 744–1128px | 3-column product grid; nav shows top-level text links only, no dropdown panels; hero min-height 400px; filter bar wraps to two rows before switching to scroll |
| Desktop | 1128–1440px | 4-column product grid; full nav with dropdown panels on hover; hero at 540px min-height; sticky add-to-cart bar appears on PDP after scrolling past price |
| Wide | > 1440px | Content constrained to 1440px max-width with auto side margins; hero images scale to fill without stretching headline type; grid gutter increases from {spacing.base} to {spacing.lg} |

### Touch Targets

- All buttons minimum 44px height, matching WCAG 2.5.5
- Color swatches expand from 24px (desktop) to 32px (mobile) via padding compensation
- Filter pills maintain 44px tap height with vertical padding added on mobile
- Nav hamburger and cart icons: 44×44px tappable area regardless of icon render size
- Category tabs expand to 48px height on mobile via increased vertical padding

### Collapsing Strategy

- Top nav collapses at < 744px to logo + hamburger + cart; search moves into the drawer slide-in
- Footer column links accordion-collapse on mobile; headings become tap-to-expand triggers with a chevron
- Product-line filter bar switches from wrapped multi-row layout to single-row horizontal scroll at < 744px
- Hero body copy is hidden on mobile when the headline alone fills the viewport; the CTA button stays visible
- Promo bar text truncates with ellipsis at < 375px rather than wrapping to a second line
- Nav dropdown panels become full-screen drawer panels on mobile rather than hover overlays

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Muted/placeholder gray**: No mid-range neutral gray was extracted from the site; #717171 is an assumed UI gray — verify against production computed styles for `color: muted` text
- **Exact button padding and height**: Live Shopify theme may use slightly different padding than the 12px/24px values modeled here; verify with browser computed styles on the rendered CTA
- **Arizona and ArizonaSans font weights**: Specific weights loaded by the Timex license were not confirmed; available weight range (400/600/700 assumed) should be cross-checked against the actual font files
- **Plain typeface specifics**: "Plain" appears in the extracted font stack but its designer, foundry, and optical metrics were not confirmed; ArizonaSans serves as the functional fallback until Plain loads
- **Hover and focus transition timing**: No animation durations or easing curves were captured; 150ms ease-in-out assumed throughout
- **Dark mode**: No dark-mode color overrides extracted; the brand likely serves a single light theme, but this was not confirmed
- **Icon system**: No icon family name identified; Timex uses product-line icons (dive, sport, field, dress) whose source library or custom glyph set is unknown
- **Exact product-line badge placement rules**: Badge stacking order and visibility priority when multiple badges apply to one product (e.g., SALE + SPORT) was not observed in extraction
