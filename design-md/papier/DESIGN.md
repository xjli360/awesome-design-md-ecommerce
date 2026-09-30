---
version: alpha
name: "Papier"
source_url: "https://www.papier.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every page in Papier's digital experience sits on the same off-white field (`#faf7f0`) declared in the site's meta theme-color — a quiet signal that the entire UI is literally color-matched to writing paper. Against this warm canvas, the single operative CTA color is a muted copper-orange (`#ffa359`): not the high-voltage red-orange of a conversion-optimized stack, but the exact tone of a Pantone swatch someone might choose for a notebook cover. Baskerville carries the editorial register — headlines sit at 40–48px in italic form, bringing the authoritative weight of a well-set printed book rather than the geometric confidence of a sans-serif challenger brand. Avenir handles the functional layer: navigation links, body copy, and labels run in clean geometric shapes at modest weights, creating a readable counterpoint without coldness. Buttons depart entirely into Avant Garde Gothic — all-caps, letter-spaced at 0.08em, and quiet in scale (12–14px) — functioning more like embossing on card stock than like clickable UI elements. The extended palette reads like a stationery color collection rotating seasonally: deep forest (`#23491b`, `#3f7427`), warm rust (`#b13f2f`), muted sage (`#66857a`), dusty mint (`#93daa3`), and amber wheat (`#e2d2ac`) appear on product tiles rather than as persistent UI chrome, so the catalog carries its own seasonal mood without repainting the global shell. Surfaces layer in degrees of warmth — `#ece1c7` for section fills, `#f4eee0` for card image wells, `#fffefa` for near-white overlays — three creams that together produce the gentle thermal gradient of paper stock under different lighting. Rounded corners stay deliberately restrained (`{rounded.xs}` to `{rounded.sm}`) because Papier's brand object has square corners. Script typefaces (Adore, Beautifully Delicious) surface only inside personalization preview panels where a customer's name renders live in ink, turning a UI widget into a product demo.

colors:
  primary: "#ffa359"
  primary-active: "#e07a3d"
  primary-disabled: "#f3d5c2"
  ink: "#1e2525"
  body: "#565c5c"
  muted: "#8e9292"
  hairline: "#c7c9c9"
  hairline-soft: "#e8e9e9"
  canvas: "#faf7f0"
  surface-soft: "#f4eee0"
  surface-card: "#fffefa"
  surface-warm: "#ece1c7"
  on-primary: "#1e2525"
  on-dark: "#faf7f0"
  forest-deep: "#23491b"
  forest: "#3f7427"
  sage: "#66857a"
  sage-light: "#91ac72"
  mint: "#93daa3"
  rust: "#b13f2f"
  amber: "#e2d2ac"
  sand: "#a99a78"
  peach: "#f3d5c2"
  sage-pale: "#dae8de"

typography:
  display-xl:
    fontFamily: "'Baskerville Italic', 'Baskerville', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    fontStyle: italic
    lineHeight: 1.13
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Baskerville', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Baskerville', Georgia, serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'Avenir', 'Avenir Bold', -apple-system, BlinkMacSystemFont, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Avenir', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'Avenir', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Avenir', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Avenir', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-caps:
    fontFamily: "'Avant Garde Gothic Bold', 'Avant Garde Gothic', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.1em
    textTransform: uppercase
  button-md:
    fontFamily: "'Avant Garde Gothic Bold', 'Avant Garde Gothic', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Avant Garde Gothic', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Avenir', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'Avenir', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  script-accent:
    fontFamily: "'Adore', 'Beautifully Delicious', cursive"
    fontSize: 32px
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    border: "1px solid {colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 0
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    border-focus: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline-soft}"
    height: 64px
    logoTypography: "{typography.display-md}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.xs}"
    padding: 10px 16px
    height: 40px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    subtitleColor: "{colors.body}"
    priceColor: "{colors.ink}"
    imageBg: "{colors.surface-soft}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.xs}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaComponent: "button-primary"
    padding: "{spacing.section} {spacing.xl}"
  category-chip:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 32px
  category-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    border: "1px solid {colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 32px
  badge-collection:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.label-caps}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  personalization-preview:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    scriptTypography: "{typography.script-accent}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  promo-banner:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
  seasonal-swatch:
    rounded: "{rounded.full}"
    size: 28px
    border: "2px solid {colors.hairline}"
    activeRing: "2px solid {colors.ink}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.label-caps}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The primary CTA runs copper-orange (`#ffa359`) with near-black ink text (`#1e2525`), in Avant Garde Gothic Bold set all-caps at 14px with 0.08em letter-spacing. Corners land at `{rounded.xs}` (4px) — deliberately square-adjacent, consistent with the brand's paper-corner vocabulary. Hover state deepens to `primary-active` (`#e07a3d`); disabled collapses to a muted peach (`#f3d5c2`) with gray text. Sits at 48px height with 28px horizontal padding to give the compact letterforms room to breathe.

**`button-secondary`** — Outlined in `{colors.ink}` with a transparent fill, matching the primary in height and Avant Garde Gothic typography. Used for secondary choices such as "Add to Wishlist" or "View Details" when a primary CTA is already present. On hover, the ink border intensifies slightly; no fill change.

**`button-ghost`** — Minimal text-only affordance in Avant Garde Gothic at 12px, all-caps. No border, no background. Used for tertiary actions like "View all" at the end of a product shelf or within inline navigation breadcrumbs.

### Text Input

**`text-input`** — Near-white fill (`#fffefa`) with a hairline border at rest (`#c7c9c9`), transitioning to a full `{colors.ink}` border on focus — a high-contrast shift that reads clearly against the warm canvas page background. Avenir body-md type, 48px height, 4px radius. Applied across search, checkout address, and personalization form fields.

### Navigation

**`nav-bar`** — A 64px bar on the warm canvas (`#faf7f0`) anchored by a barely-visible hairline-soft bottom border. The wordmark "Papier" renders in Baskerville (`{typography.display-md}`) at the left; category links — Notebooks, Diaries, Cards, Gifts — run in Avenir 14px/weight 500. Right side holds search, account, and bag icons as 44×44px tap targets. On scroll, a subtle box-shadow emerges below the bar. No filled background change on scroll; the canvas color holds throughout.

### Product Card

**`product-card`** — Near-white card (`#fffefa`) with a hairline-soft border and 4px radius. Product images sit on a warm soft cream image well (`#f4eee0`), grounding photography without clinical whiteness. Below: product title in `{typography.title-sm}` (Avenir 16px/600), optional subtitle in body muted, price in `{typography.price}`. No star ratings or reviews appear on the card face — trust is built through editorial photography rather than social proof numbers. Limited editions receive a `badge-collection` strip (warm cream, label-caps type) overlaid at the card base.

### Hero Banner

**`hero-banner`** — Full-bleed editorial panels using `{colors.surface-soft}` as default, but swap to rich seasonal palette colors (forest-deep `#23491b`, rust `#b13f2f`) for campaign moments. The headline runs in `{typography.display-xl}` — Baskerville italic at 48px, 1.13 line height — the strongest single typographic event on any Papier page. A `button-primary` CTA anchors below with section-level padding. On campaign pages a secondary `button-secondary` often accompanies it ("Shop gifts" vs. "Explore diaries").

### Category Chips

**`category-chip`** / **`category-chip-active`** — Pill-shaped filter tags (`{rounded.full}`) in Avant Garde Gothic Bold at 11px, all-caps. Inactive is outlined with `{colors.hairline}` on a transparent ground; active inverts to ink fill with on-dark text. These appear in the product listing filter strip, the personalization option selector, and the gifting guide navigator. The pill shape is the only exception to the brand's restrained corner geometry, justified because these read as tags rather than buttons.

### Personalization Preview

**`personalization-preview`** — The brand's most distinctive UI component: a framed preview panel in `{colors.surface-soft}` where the customer's name, date, or dedication renders live in `{typography.script-accent}` (Adore or Beautifully Delicious at 32px). The moment a user types, their handwriting surrogate appears on a facsimile of the product cover — turning an e-commerce input into a direct experience of the physical object. Border stays soft (`{colors.hairline-soft}`), radius at `{rounded.sm}`, padding generous at `{spacing.lg}`.

### Seasonal Swatch

**`seasonal-swatch`** — 28px circular color dot with a 2px hairline ring at rest, upgrading to a 2px ink ring on selection. Used in the product configurator to choose notebook cover colors. The swatch palette draws directly from the extended brand palette: forest, sage, rust, mint, amber, sand.

### Promo Banner

**`promo-banner`** — A slim full-width strip (`{spacing.sm}` × `{spacing.base}` padding) in `{colors.surface-warm}` above the nav, carrying short promotional copy in `{typography.body-sm}`. Dismissible on desktop via an × icon; on mobile it stacks above the hamburger bar.

### Footer

**`footer`** — A dark near-black field (`#1e2525`) spanning full width. Section headings in `{typography.label-caps}` (Avant Garde Gothic, 11px, all-caps, 0.1em spaced); body links in `{typography.body-sm}` Avenir. Four columns on desktop: Shop, Personalization, Help, About. Social icons and payment logos at the bottom in `{colors.hairline}` muted gray. The footer is the one surface where the warm-canvas metaphor is suspended — ink-black grounds the brand as a publisher, not just a stationery shop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero headline drops to `display-md` Baskerville; category chips scroll horizontally in a single row; personalization preview stacks below product image; footer sections accordion-collapse |
| Tablet | 744–1128px | Two-column product grid; nav exposes primary categories with overflow behind "More"; hero shifts to left-text / right-image split layout; search bar expands inline next to nav links |
| Desktop | 1128–1440px | Three-column product grid; full nav category row exposed; hero runs full-bleed with `display-xl` headline; personalization preview rendered inline beside product options panel |
| Wide | > 1440px | Four-column product grid; hero and editorial content max-width constrained to 1440px with auto side margins; editorial campaign sections shift to 60/40 image-text splits |

### Touch Targets
- Nav icons (search, account, bag) are minimum 44×44px on all breakpoints
- Category chips expand to 40px minimum height on mobile
- Product cards carry a full-card tap region on mobile — no isolated CTA button required
- Personalization form fields are 48px tall across all breakpoints
- Swatch dots expand to 36px on mobile for reliable color selection

### Collapsing Strategy
- Nav: full horizontal category list → primary categories + "More" dropdown → hamburger slide-in drawer
- Product grid: 4-col editorial → 3-col standard → 2-col → 1-col full-bleed cards
- Hero: editorial split-image layout → stacked image-above-text → text-only hero (image hidden) at narrowest mobile
- Personalization preview: inline beside product form → below product image → collapsed behind "Preview your personalization" toggle
- Footer: four-column grid → two-column → single accordion list per category section
- Promo banner: single-line strip → wraps to two lines → collapses to icon + tap-to-expand on narrowest breakpoints

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius not confirmed from live CSS extraction — `{rounded.xs}` (4px) inferred from visual inspection of the brand's square-corner aesthetic
- Precise Baskerville variant in use (Regular 400 vs. Bold 400-italic vs. Semibold) not determinable from font-family stack alone; weight 400 italic used as best estimate for display
- Typography pixel sizes (48px, 36px, 28px for display scale) are estimated from brand aesthetic; live stylesheet values not extracted
- Exact nav height (64px) is estimated; site may use a slightly different desktop value
- Whether `Adore` or `Beautifully Delicious` is the primary personalization script font is ambiguous — both appear in the font stack; `Adore` listed first in components as the likely default
- Letter-spacing values for Baskerville display type not captured; tracking set to slightly negative as serif display convention
- Animation easing curves and transition durations not extracted
- Mobile nav interaction pattern (slide-in drawer vs. full-screen overlay) not confirmed
- Exact hairline border-width on product cards (1px assumed) not extracted from live styles
- Dropdown behavior for "More" nav category (mega-menu vs. simple list) not confirmed
