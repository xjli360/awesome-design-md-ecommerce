---
version: alpha
name: "Simplified"
source_url: "https://www.emilyley.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The product page carries up to six color-chooser swatches at once — sunshine yellow (#fbcd0a), dusty rose (#d16294), soft lavender (#a89cc8), warm bronze (#c18952), seafoam mint (#c1e6e6), and sage (#3ea36a) — each a distinct planner edition, and the checkout CTA stays #108474, a deep forest teal, across every colorway. That visual grammar encodes the brand's central logic: seasonal abundance held together by a single calm anchor. Sackers Gothic Std governs every eyebrow, section label, and navigation item at extended letter-spacing and font-weight 400, never loud, never bold — headers communicate by spacing rather than mass. Below it, Butler and Libre Caslon Text carry the editorial register: product descriptions, founder prose, and lifestyle headlines gain a bookish serif warmth that reinforces the ritual-of-writing-things-down positioning. Body copy and UI elements shift to Jost or Nunito Sans, geometric sans-serifs that keep checkout flows and mobile menus clean without personality bleed. The cream canvas (#faf8f5) is the true background — warmer than pure white, cooler than ivory — reading more as paper stock than digital surface. Navy (#275173) provides structural weight in feature banners and the deep footer. Gold (#c18952) operates at ornament scale: price callouts, foil-echo divider marks, and premium badge fills that recall physical foil stamping on the planner covers. Rounded corners are deliberate and restrained: `{rounded.sm}` (4px) on interactive controls, `{rounded.md}` (8px) on product cards and drawers, `{rounded.full}` exclusively on swatches and pill-style category tags. Section padding is generous at 64px; product grid gutters breathe at 24–32px; hero areas give full-bleed lifestyle photography room to expand without heavy text overlay. The grammar as a whole belongs to a premium stationery brand that has systematized its own warmth — every seasonal accent hue enumerated, every hierarchy step intentional.

colors:
  primary: "#108474"
  primary-active: "#0d6b5e"
  primary-disabled: "#a8d4cf"
  navy: "#275173"
  navy-mid: "#365072"
  gold: "#c18952"
  sunshine: "#fbcd0a"
  rose: "#d16294"
  lavender: "#a89cc8"
  mint: "#c1e6e6"
  sage: "#3ea36a"
  ink: "#141414"
  body: "#555555"
  muted: "#7b7b7b"
  hairline: "#e2e2e2"
  hairline-soft: "#eeeeee"
  canvas: "#faf8f5"
  surface-soft: "#f6f6f6"
  surface-card: "#f9fafb"
  on-primary: "#ffffff"
  on-navy: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Sackers Gothic Std', 'Butler', Georgia, serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0.15em
    textTransform: uppercase
  display-md:
    fontFamily: "'Butler', 'Libre Caslon Text', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'Sackers Gothic Std', 'Jost', sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.12em
    textTransform: uppercase
  eyebrow:
    fontFamily: "'Sackers Gothic Std', 'Jost', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.18em
    textTransform: uppercase
  title-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  editorial-body:
    fontFamily: "'Libre Caslon Text', 'Baskerville', Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: 0.01em
  caption:
    fontFamily: "'Jost', 'Nunito Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  button-md:
    fontFamily: "'Jost', 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.1em
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', 'Nunito Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.12em
    textTransform: uppercase
  nav-link:
    fontFamily: "'Jost', 'Nunito Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
  price-lg:
    fontFamily: "'Jost', 'Nunito Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0

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
  announcement-bar:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
    padding: 0 16px

  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 32px
    height: 48px

  button-primary-active:
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
    padding: 13px 31px
    height: 48px

  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 13px 31px
    height: 48px

  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px

  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"

  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px

  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    imageAspectRatio: "3/4"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-lg}"
    padding: 16px
    gap: 8px

  color-swatch:
    shape: "{rounded.full}"
    size: 24px
    border: "2px solid {colors.hairline}"
    selectedBorder: "2px solid {colors.ink}"
    gap: 6px

  seasonal-badge:
    typography: "{typography.eyebrow}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
    variants:
      new:
        backgroundColor: "{colors.gold}"
        textColor: "{colors.ink}"
      bestseller:
        backgroundColor: "{colors.navy}"
        textColor: "{colors.on-navy}"
      limited:
        backgroundColor: "{colors.rose}"
        textColor: "{colors.on-primary}"
      sale:
        backgroundColor: "{colors.primary}"
        textColor: "{colors.on-primary}"

  hero-banner:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.editorial-body}"
    ctaStyle: "button-primary"
    minHeight: 560px
    textAlign: left
    padding: "64px 24px"

  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.eyebrow}"
    rounded: "{rounded.md}"
    hoverBackgroundColor: "{colors.hairline-soft}"

  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    quoteTypography: "{typography.editorial-body}"
    attributionTypography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 32px

  planner-edition-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-sm}"
    accentColors:
      - "{colors.sunshine}"
      - "{colors.rose}"
      - "{colors.lavender}"
      - "{colors.gold}"
      - "{colors.mint}"
      - "{colors.sage}"

  footer:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.on-navy}"
    linkTypography: "{typography.body-sm}"
    headingTypography: "{typography.eyebrow}"
    padding: "48px 24px 32px"

## Components

### Buttons

**`button-primary`** — The primary CTA renders #108474 teal with an all-caps tracked Jost label at 48px height and `{rounded.sm}` (4px) corners. This button remains constant across all planner colorway pages, providing brand continuity when product imagery cycles through the seasonal accent palette. Hover darkens to `{colors.primary-active}` (#0d6b5e); disabled state drops to `{colors.primary-disabled}`, a soft teal tint that still reads as on-brand rather than neutral gray.

**`button-secondary`** — White/canvas fill with a 1px solid ink border and identical uppercase Jost label. Used for secondary actions like "Add to Wishlist" or "Learn More" when paired beside a primary CTA. The ink border ensures legibility against both the warm canvas background and lifestyle photography backdrops.

**`button-ghost`** — Transparent fill with `{colors.primary}` teal border and text. Appears in editorial feature sections and email capture modules where the primary button is already occupied by a checkout action. Maintains teal as the active-interaction color signal without adding visual weight.

### Forms & Inputs

**`text-input`** — Warm canvas fill (`{colors.canvas}`) with a `{colors.hairline}` border that upgrades to a teal `{colors.primary}` 1px ring on focus. Jost body-md at 16px keeps form fields legible and consistent with surrounding body copy. Height is 44px — slightly smaller than the 48px button to create a clear size hierarchy.

### Navigation

**`nav-bar`** — 72px tall, canvas background, with `{typography.nav-link}` (Jost 13px, weight 500, letter-spacing 0.08em) for all category links. A hairline-soft bottom border separates it from page content without visual heaviness. The announcement-bar sits above it at 36px navy with centered caption text — together they form a 108px top stack on desktop that collapses on mobile. Logo is centered or left-aligned depending on viewport.

**`search-bar`** — Surface-soft fill, 40px height, sm-rounded. Sits inside the nav on desktop; expands to full-width on mobile when a search icon is tapped. Placeholder copy in muted gray; Jost body-sm for typed input. No search button visible — submit triggers on Enter or after a short debounce.

### Product Display

**`product-card`** — Portrait 3:4 image ratio prioritizes the planner cover art. The card bottom zone shows the product name in `{typography.title-sm}` and price in `{typography.price-lg}`. Color swatches (`color-swatch`) render as a horizontal row of 24px circles beneath the name, each filled with its edition accent color and ringed with `{colors.hairline}`; the selected swatch gains a 2px `{colors.ink}` ring. `{rounded.md}` (8px) corners on the card container prevent hard geometry from clashing with the soft canvas page.

**`seasonal-badge`** — Small pill at `{rounded.xs}` (2px) with eyebrow-scale Sackers Gothic text (11px, tracked uppercase). Four fill variants keyed to context: gold fill for new arrivals (echoes foil stamping), navy for bestseller (authority), rose for limited editions, and teal primary for sale. Badges sit in the top-left corner of product card images, never stacked.

### Editorial & Marketing

**`hero-banner`** — Full-bleed lifestyle photography at minimum 560px tall with the text block left-aligned at 64px padding. The headline runs `{typography.display-xl}` — Sackers Gothic Std, 48px, tracked uppercase — over an optional light overlay or clean canvas panel set beside the image in split layouts. Subhead uses `{typography.editorial-body}` (Libre Caslon Text, 16px) to create a serif contrast against the all-caps header. The primary CTA button appears directly below at standard 48px height.

**`testimonial-card`** — Soft surface fill with 32px internal padding and md-rounded corners. Quote text runs `{typography.editorial-body}` — Libre Caslon Text at 1.7 line-height — which gives customer reviews the same bookish warmth as product descriptions. Attribution (name, planner edition year) renders in `{typography.caption}` at muted gray. Cards tile horizontally in a 3-column grid on desktop; single-column on mobile.

**`planner-edition-strip`** — A dedicated section showcasing all active colorways side by side. Each edition is represented by its accent color swatch at larger scale (40–48px circles), with the colorway name below in `{typography.eyebrow}` and a brief one-line descriptor in `{typography.body-sm}`. The strip background is surface-soft to separate it from the main canvas without a hard border. Acts as both a product navigation shortcut and a brand palette reveal.

**`category-tile`** — Square or portrait tile used in collection landing pages. Surface-soft background with an eyebrow-scale label in Sackers Gothic overlaid on or beneath a cropped product image. Hover state shifts background to `{colors.hairline-soft}`. md-rounded corners match the product card corner radius for visual consistency across grid layouts.

**`footer`** — Deep navy (#275173) background with on-navy text. Column headings use `{typography.eyebrow}` (Sackers Gothic Std, tracked uppercase) at 11px — the all-caps treatment at this size reads as organized hierarchy rather than shouting. Links render in `{typography.body-sm}` Jost at 14px. The navy footer provides the brand's strongest contrast moment and anchors the warm cream page with a grounding dark base.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger menu replaces nav links; hero stack becomes image-above, text-below; announcement bar text truncates to one line |
| Tablet | 744–1128px | 2-column product grid; nav collapses to core categories with overflow menu; hero switches to split 50/50 layout |
| Desktop | 1128–1440px | 3–4 column product grid; full horizontal nav with flyout category dropdowns; hero at full 560px min-height |
| Wide | > 1440px | Container max-width ~1440px, centered; hero photography expands further; editorial strips gain more horizontal breathing room |

### Touch Targets

- All buttons minimum 48px height; tap area extends via padding on smaller `button-sm` variants
- Color swatches expand from 24px to 36px on touch viewports
- Nav links carry a minimum 44px tap zone via vertical padding even when visually smaller
- Swatch selection adds a visible ring indicator rather than relying on hover state

### Collapsing Strategy

- Product filter sidebar collapses to a bottom-sheet drawer on mobile, triggered by a "Filter" button in a sticky toolbar
- Planner edition strip scrolls horizontally on mobile rather than wrapping to multiple rows
- Footer four-column grid stacks to two columns on tablet, single column on mobile
- Hero text overlays the image on mobile with a semi-transparent canvas panel; desktop uses side-by-side layout

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-active` (#0d6b5e) and `primary-disabled` (#a8d4cf) are computed by darkening/lightening `{colors.primary}` — not directly extracted from the live site
- Shadow depth values for product cards, drawers, and modals were not captured in extraction
- Hover/transition timing and easing curves not available
- Whether Sackers Gothic Std or Butler takes precedence for the top hero headline is ambiguous — both appear in font stacks; Sackers Gothic Std assumed primary based on brand convention
- Exact planner edition colorway names (e.g., "Sunshine", "Petal", "Lavender Mist") not confirmed — accent colors mapped by hex only
- Foil/metallic rendering treatment for gold (#c18952) badge fills is approximated — physical product uses real foil stamping which the digital UI echoes only with flat fill
- Mobile navigation structure (slide-in drawer vs. full overlay) not confirmed
- Whether `{colors.navy}` (#275173) or `{colors.navy-mid}` (#365072) is the primary structural dark — both appear in extracted colors at similar frequency; #275173 assumed primary
