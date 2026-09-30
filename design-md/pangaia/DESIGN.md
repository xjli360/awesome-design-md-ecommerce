---
version: alpha
name: "Pangaia"
source_url: "https://pangaia.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  PANGAIA foregrounds material science before aesthetics — the site's masthead reads "Materials science brand on a mission to save our environment" where a fashion company would place a campaign slogan, and the color language enforces that hierarchy. A seafoam mint (#b2f9e9) functions as the primary accent: unusual enough to feel like a laboratory indicator rather than a trend color, clinical enough to signal that the brand's sustainability claims are technical, not decorative. The primary canvas runs #f7f7f8 — a cool off-white with a faint blue undertone — against near-black (#121212) body text, producing the high-contrast readability of a research document rather than the warm ivory-and-charcoal palette most sustainable fashion prefers.

  The custom typeface named "PANGAIA" handles wordmark and logotype duties, paired with HW Cigars for editorial headlines — an unexpected companion that prevents the technical positioning from reading as sterile. Body text falls to system stacks, keeping page weight lean for a brand that measures its environmental footprint in everything. Navigation chrome and interface neutrals live in muted purple-greys (#676986, #9a9db1, #d3d4dd) — a cohesive mineral family that sits between blue and grey, giving the palette a distinctly cool quality rather than the earthy warmth expected from an eco label.

  Product presentation centers on color-story photography — PANGAIA's apparel drops are famous for sweeping saturated colorways — so the UI deliberately steps back to near-neutral containers, letting photography carry the brand-color work. Cards arrive with zero rounding ({rounded.none}), sharp enough to feel precise, not corporate-soft. Badges and material callouts use uppercase caption labels at tight letter-spacing, borrowing pharmaceutical packaging conventions to signal ingredient transparency. The teal accent (#0e7a82) serves as the active-state and link treatment, providing readable contrast against both mint and the light canvas. A medium navy (#272d45) surfaces in data-layer contexts — sustainability metrics, material breakdowns — grounding scientific claims in a palette that reads authoritative rather than promotional. Red (#ea3434) is gated strictly to error states, the only warm-spectrum color in an otherwise cool, mineral system.

colors:
  primary: "#b2f9e9"
  primary-active: "#0e7a82"
  primary-disabled: "#dbdde4"
  ink: "#121212"
  body: "#313131"
  muted: "#676986"
  muted-soft: "#9a9db1"
  hairline: "#dbdde4"
  hairline-soft: "#e5e5eb"
  canvas: "#f7f7f8"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  surface-muted: "#ebebeb"
  on-primary: "#121212"
  on-dark: "#f4f4f6"
  mineral: "#d3d4dd"
  navy: "#272d45"
  blue-data: "#32508e"
  teal-deep: "#0e7a82"
  error: "#ea3434"

typography:
  display-xl:
    fontFamily: "'PANGAIA', 'HW Cigars', Georgia, serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'HW Cigars', Georgia, serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'HW Cigars', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.02em
  body-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.03em
  caption-upper:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.10em
    textTransform: uppercase
  button-md:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.10em
    textTransform: uppercase
  nav-link:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.04em
  label-upper:
    fontFamily: "system-ui, -apple-system, 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.14em
    textTransform: uppercase
  wordmark:
    fontFamily: "'PANGAIA', Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0.08em

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
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    borderColor: "{colors.ink}"
    borderWidth: 1px
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    borderColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottomWidth: 1px
    borderBottomColor: "{colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "3/4"
    rounded: "{rounded.none}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.body-sm}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 80vh
    padding: "{spacing.section} {spacing.xl}"
  hero-dark:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 80vh
  material-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    borderWidth: 1px
    borderColor: "{colors.hairline}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  sustainability-stat:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xl}"
    rounded: "{rounded.none}"
  color-swatch:
    size: 20px
    rounded: "{rounded.full}"
    borderColorSelected: "{colors.ink}"
    borderWidthSelected: 2px
    borderColorUnselected: "{colors.hairline}"
    borderWidthUnselected: 1px
    gap: "{spacing.xs}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-upper}"
    padding: "{spacing.sm} {spacing.base}"
    height: 36px
  search-overlay:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottomWidth: 1px
    borderBottomColor: "{colors.hairline}"
    inputTypography: "{typography.title-md}"
    resultTypography: "{typography.body-sm}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    headingTypography: "{typography.caption-upper}"
    linkTypography: "{typography.body-sm}"
    borderTopWidth: 1px
    borderTopColor: "{colors.hairline}"
    padding: "{spacing.xxl} 0"
  collection-filter:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    activeAccentColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    borderBottomWidth: 1px
    borderBottomColor: "{colors.hairline}"
    rounded: "{rounded.none}"
  tag-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    borderWidth: 1px
    borderColor: "{colors.mineral}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  editorial-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    accentColor: "{colors.primary}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    maxWidth: 800px
    padding: "{spacing.section}"

## Components

### Buttons
**`button-primary`** — A sharp-cornered ({rounded.none}) mint slab (#b2f9e9) with uppercase dark ink text ({colors.on-primary}), 48px tall, tracking borrowed from pharmaceutical labeling. The zero-radius corner is deliberate: PANGAIA's UI avoids the friendliness of pill shapes in favor of a precision-instrument register. Active state steps down to teal ({colors.primary-active}) with reversed-to-light text ({colors.on-dark}); disabled washes the fill to hairline grey ({colors.primary-disabled}) with muted text ({colors.muted}).

**`button-secondary`** — Transparent fill with a 1px ink border ({colors.ink}), same uppercase button-md tracking as primary, inverts to solid ink fill on hover with on-dark text. Used for secondary CTAs on editorial sections and as "view all" actions in collection grids where mint would compete with product photography.

**`button-ghost`** — Borderless, transparent, muted-text ({colors.muted}), smaller button-sm uppercase. Appears as filter toggles, inline "show more" links, and close controls on overlays. No hover fill — underline treatment only.

### Navigation
**`nav-bar`** — 60px white bar with a 1px hairline bottom rule ({colors.hairline}). The PANGAIA wordmark (custom brand typeface at {typography.wordmark} scale) anchors left; search, account, and bag icons right-align. All category links render in {typography.nav-link} with light uppercase tracking — no decorative separator dots or hover animations beyond color shift to {colors.primary-active}. An announcement bar ({announcement-bar}) in full-ink black sits permanently above, rotating sustainability and campaign messages in caption-upper uppercase.

### Product Cards
**`product-card`** — Entirely edge-free ({rounded.none}), 3:4 portrait image fills the top — PANGAIA's photography always shows the full-length garment on a clean background to let colorways speak. Title and price sit beneath in plain {typography.body-md} and {typography.body-sm}. Color swatches ({color-swatch}) stack as 20px circles below the price row; selected swatch carries a 2px ink ring. A {product-card-badge} in mint surfaces on new-in or low-stock items in {typography.caption-upper}, always bottom-left of the image frame. No card drop shadow anywhere.

### Material Badge
**`material-badge`** — Inline label identifying fiber or process: "FLWRDWN™", "ECONYL®", "BioSoft Cotton". Uppercase {typography.caption-upper}, 1px hairline border on {colors.surface-soft} fill, no rounding. On product-detail pages these stack horizontally below the product title and above the color selector, functioning as proof-of-ingredient labels rather than decorative tags.

### Hero
**`hero`** — Full-bleed editorial panel at minimum 80vh. Title renders in {typography.display-xl} PANGAIA typeface; body copy in {typography.body-md} system stack. CTA is `button-primary` (mint, sharp-cornered). For dark-photography heroes, the `hero-dark` variant swaps canvas to {colors.navy} and text to {colors.on-dark} — no translucent scrim layer, trusting photography composition for contrast instead.

### Sustainability Stat
**`sustainability-stat`** — Navy (#272d45) tile used in "Impact" and mission sections. A large metric number renders in {typography.display-md} with the mint accent ({colors.primary}) differentiating the numeral from the explanatory label in {typography.body-sm} on-dark ({colors.on-dark}). Multiple tiles arrange as a horizontal strip on desktop, collapsing to a 2×2 grid then single column on narrower viewports.

### Color Swatch
**`color-swatch`** — 20px fully rounded circles ({rounded.full}) representing colorway options. Selected state: 2px ink ring with a 2px gap between ring and swatch circle. Unselected: 1px {colors.hairline} border. PANGAIA's colorway launches are a core brand event — swatches routinely span 10–14 options per product. Swatches are keyboard-navigable and each carries an aria-label for color name accessibility.

### Announcement Bar
**`announcement-bar`** — Full-width 36px strip in solid {colors.ink} with {colors.on-dark} text in {typography.caption-upper}. Rotates 2–3 messages on a timed carousel: sustainability certifications, free-shipping thresholds, or seasonal campaign copy. No close button — this is a permanent fixture above the nav, not a dismissible modal banner.

### Search Overlay
**`search-overlay`** — Full-width panel drops immediately below the nav bar on search activation. A large input in {typography.title-md} sits above a single 1px hairline bottom rule ({colors.hairline}) — no input border box, no background fill differentiation. Result suggestions render as plain list rows in {typography.body-sm}. No autocomplete popover bubbles; the aesthetic aligns with the clinical, research-document register of the rest of the site.

### Footer
**`footer`** — Light surface ({colors.surface-soft}) separated from content by a 1px hairline top border ({colors.hairline}). Column headings in {typography.caption-upper}; link lists in {typography.body-sm} at {colors.body}. A certification strip (B Corp mark, fiber standard logos) sits at the foot edge in muted caption scale. Newsletter input is borderless with a label-upper placeholder; submit renders as `button-primary` (mint, no border-radius).

### Collection Filter
**`collection-filter`** — A horizontally scrolling filter bar below the collection header. Each filter category renders in {typography.body-sm}; the active filter state shows a mint underline accent ({colors.primary}). All hit targets are rectangular ({rounded.none}), consistent with the brand's sharp-corner system. On mobile, the bar collapses entirely behind a single "Filter & Sort" trigger rendered as a `tag-pill` that opens a bottom sheet.

### Editorial Section
**`editorial-section`** — Centered-column long-form text block, max-width 800px. Title in {typography.display-md} (HW Cigars); body in {typography.body-md} system stack. Accent color ({colors.primary}) surfaces in section divider lines or pull-quote highlights. Used for brand-story, materials-science explainers, and sustainability reports inlined on category pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + wordmark + bag icon; hero drops to {typography.display-sm}; filter bar becomes bottom-sheet trigger pill; sustainability stat tiles stack to single column |
| Tablet | 744–1128px | 2-column product grid; nav shows wordmark + icon row, category links behind hamburger; hero shifts to split image/text layout; sustainability stats reflow to 2×2 grid |
| Desktop | 1128–1440px | 3- or 4-column product grid; full horizontal nav with category links visible; announcement bar always shown; editorial-section max-width 800px centered |
| Wide | > 1440px | Grid stays at 4 columns; content column max-width 1440px with increased side padding; hero padding scales up to preserve editorial proportion |

### Touch Targets
- All buttons minimum 48px height on mobile
- Color swatches: visual size 20px, minimum touch target 36×36px via invisible padding
- Nav icons minimum 44×44px tap area
- Filter tags and tag-pills minimum 36px height with generous horizontal padding
- Material badges are non-interactive on mobile; ensure 8px gap from adjacent tap targets

### Collapsing Strategy
- Primary navigation collapses to hamburger at < 1128px; wordmark and utility icons (search, bag) always visible
- Sustainability stat strip reflows from horizontal ribbon to 2×2 at < 744px, single column at < 420px
- Material badge rows wrap to multiple lines on PDPs at mobile widths — no horizontal scroll
- Editorial split-layout heroes (image left, text right) stack vertically — image above, text below — on mobile
- Footer 4-column grid collapses to 2 columns at tablet, single column with accordion heading toggles at mobile
- Announcement bar is always full-width and non-dismissible across all breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact weights and optical metrics for the proprietary HW Cigars and PANGAIA custom typefaces are estimated; both are closed-distribution fonts not registered in any public specimen index — validate font-size and letter-spacing values against a live browser specimen
- The mint (#b2f9e9) primary color's precise functional role — whether it fills CTAs, highlights section backgrounds, or is accent-only — could not be confirmed without a JS-rendered page capture; treat as CTA fill until validated against a live session
- No spacing or layout tokens were recoverable from computed styles; all spacing values follow an 8pt base grid assumption and should be verified against computed margin/padding in browser DevTools
- Dark-mode palette is not extractable from current extraction — PANGAIA may ship a dark theme for evening campaign pages; no confirmed dark-surface tokens
- Animation timing and easing values (hero text entrance, swatch hover, filter bar scroll) were not captured; the brand register suggests 200–300ms ease-out transitions
- The #32508e medium-blue and #2c3e50 dark blue-grey appear in the extraction but their page-level roles (data visualization, specific campaign templates, or third-party widget chrome) could not be confirmed — mapped tentatively as `blue-data` and excluded from primary component tokens
- Nav height (60px) and announcement-bar scroll behavior (sticky vs. scroll-away) are estimates requiring browser inspection to confirm
