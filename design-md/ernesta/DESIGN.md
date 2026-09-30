---
version: alpha
name: "Ernesta"
source_url: "https://ernesta.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every rug in the Ernesta catalog gets its own room-scene photography — a concrete commitment that drives the entire UI toward restraint. The only color confirmed by live extraction is near-black #313131, which anchors all text and primary CTAs; the brand's visual weight lives in the photography, not the chrome. No proprietary typeface was recoverable (the site served a Cloudflare bot-challenge page during extraction), so the system falls back to -apple-system / Helvetica Neue at sizes that read editorial rather than generic when letter-spacing is kept tight. Button shapes occupy a middle register — not pill-rounded, not razor-square — settling at {rounded.none} so they feel precise and grid-aligned, matching the rectilinear geometry of woven rug patterns. The layout grammar is wide-margins-first: hero modules bleed full-viewport with oversized room photography, then the catalog tightens to a two- or three-column grid where product cards surface swatch counts and material descriptors beneath each image. A persistent sticky nav carries the wordmark flush left with cart and account icons right; a search input collapses behind a magnifier icon on mobile. Filter interactions — fiber type, pile height, colorway, size — occupy a left-rail or slide-in drawer system with checkbox groups and {color-swatch-chip} rows. The footer drops into editorial mode with fiber care guides, room-sizing calculators, and lifestyle links that extend the brand voice past the transaction. Product color swatches render as tight circular chips ({rounded.full}) previewing actual rug colorways rather than categorical labels. Ernesta does not compete on brand hue; it competes on photography production value and material specificity, which is why the UI steps back entirely.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#999999"
  ink: "#313131"
  body: "#4d4d4d"
  muted: "#787878"
  hairline: "#e2e2e2"
  hairline-soft: "#efefef"
  canvas: "#ffffff"
  surface-soft: "#f8f7f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  swatch-border: "#d4d4d4"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 300
    lineHeight: 1.08
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 300
    lineHeight: 1.18
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: -0.2px
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: -0.1px
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.3px
  label-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  price-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 6px
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
    padding: 15px 32px
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
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 14px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    position: sticky
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageAspectRatio: "4/3"
    rounded: "{rounded.none}"
    titleTypography: "{typography.body-md}"
    priceTypography: "{typography.price-lg}"
    captionTypography: "{typography.caption}"
    gap: "{spacing.sm}"
  hero-module:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    imagePosition: cover
    minHeight: 580px
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaVariant: button-primary
  filter-rail:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    labelTypography: "{typography.label-sm}"
    borderRight: "1px solid {colors.hairline}"
    width: 240px
  color-swatch-chip:
    width: 24px
    height: 24px
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.swatch-border}"
    borderSelected: "2px solid {colors.ink}"
    offsetSelected: 2px
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    borderSelected: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 8px 12px
  badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.none}"
    padding: 3px 8px
  editorial-strip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    height: 40px
    textAlign: center
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-sm}"
    linkColor: "{colors.ink}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xxl}"

## Components

### Buttons
**`button-primary`** — Flat near-black (#313131) rectangle with zero border-radius and uppercase letter-spaced type at 1px tracking. The sharp corners echo the rectilinear geometry of woven flat-weaves and keep the button feeling architectural rather than consumer-generic. On hover it transitions to `{colors.primary-active}` (#1a1a1a); disabled state shifts to `{colors.primary-disabled}` (#999999) with white text preserved.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, matching the primary in height and letter-spacing. Pairs with button-primary for two-CTA rows (e.g., "Add to Cart" + "Save to Room"). On hover the border thickens to 2px or the fill transitions to `{colors.surface-soft}` to signal interactivity.

**`button-ghost`** — Transparent background, no border, underlined `{typography.button-md}` text. Reserved for low-hierarchy actions: "View all rugs," "Reset filters," "Read our size guide." Keeps the action scannable without competing visually with photography.

### Text Input & Search
**`text-input`** — Zero-radius rectangular field with a `{colors.hairline}` border that sharpens to `{colors.ink}` on focus, matching the button language precisely. Placeholder copy renders in `{colors.muted}`. The search variant uses this same field with a trailing magnifier icon; on mobile the search likely collapses to an icon in the nav that expands into a full-width overlay rather than a visible persistent input.

### Navigation
**`nav-bar`** — Sticky 64px white bar, wordmark left-aligned in `{typography.nav-link}`, top-level category links spanning the center on desktop. Cart and account sit icon-only at right, each padded to a 44px touch target. A 1px `{colors.hairline}` bottom border separates it from page content. On scroll the bar holds white — no blur, no opacity shift — so type stays legible even when the hero image begins. An `editorial-strip` (40px, ink background, promo copy) sits above the nav and is dismissible.

### Product Card
**`product-card`** — No card border, shadow, or background fill; the card is purely image + stacked metadata. The image fills a 4:3 aspect ratio with zero border-radius. Below the image: product name in `{typography.body-md}`, price in `{typography.price-lg}`, and a material/variant descriptor in `{typography.caption}` muted gray. A row of `color-swatch-chip` elements previews available colorways inline. On hover the image scales subtly to 1.02 with no other visual treatment — no overlay, no darkening.

### Hero Module
**`hero-module`** — Full-bleed room photography at minimum 580px tall on desktop. The headline in `{typography.display-xl}` (weight 300, tight letter-spacing) overlays a naturally dark image zone or a partial `{colors.ink}` scrim; body copy in `{typography.body-md}` white with a single `button-primary` CTA anchored bottom-left of the text block. On mobile, the hero crops to a portrait ratio and the text block moves below the image rather than overlaying it, preserving legibility without requiring a full scrim.

### Filter Rail
**`filter-rail`** — 240px left sidebar on desktop with section headings in `{typography.label-sm}` uppercase and filter options in `{typography.body-sm}`. Structure: checkbox groups for fiber/weave type, `color-swatch-chip` rows for colorway, and `size-selector` chips for dimensions. A `{colors.hairline}` right border separates the rail from the catalog grid. On tablet and mobile, the rail collapses to a slide-in drawer triggered by a sticky "Filter & Sort" button. An active-filter count badge appears on the button when filters are applied.

### Color Swatch Chip
**`color-swatch-chip`** — 24×24px filled circle with a 1.5px `{colors.swatch-border}` ring. Selected state gains a 2px `{colors.ink}` ring with a 2px offset gap between the ring and the chip surface — the standard selected-swatch convention used by premium textile brands. A tooltip on hover or long-press surfaces the colorway name. On mobile the chip expands to a 40px touch target with padding, keeping the visual size at 24px.

### Editorial Strip
**`editorial-strip`** — Slim 40px full-width bar above the nav, ink background, centered `{typography.body-sm}` white text. Carries shipping threshold messaging ("Free shipping on orders over $X") or limited-run callouts. Dismissible via an × icon at right; dismissed state persists in localStorage for the session.

### Footer
**`footer`** — Warm off-white `{colors.surface-soft}` background with a four-column desktop grid: Shop, Materials & Care, Sizing Tools, and About. Column headings in `{typography.label-sm}` uppercase; links in `{typography.body-sm}` `{colors.body}`. A newsletter signup row at top of the footer carries a `text-input` + `button-primary` inline pair. The bottom strip contains legal copy in `{typography.caption}` `{colors.muted}` and payment icons. On mobile, columns collapse to stacked accordions with heading as the expand toggle.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column catalog grid; hero crops to portrait with text block below image; filter-rail becomes a bottom-anchored slide-up drawer; nav collapses to hamburger + wordmark + cart; button-primary goes full-width in cart and checkout contexts |
| Tablet | 744–1128px | Two-column catalog grid; filter-rail becomes a horizontal chip strip above the grid; nav shows top-level categories only, hides secondary links behind overflow |
| Desktop | 1128–1440px | Three-column catalog grid with 240px filter-rail; full sticky nav with all category links and search visible; hero at 580px minimum height |
| Wide | > 1440px | Max-width container (~1440px) centered on canvas; hero photography extends edge-to-edge while text and CTA stay within the content column |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Color swatch chips expand from 24px visual to 40px touch target with transparent padding
- Nav icon buttons (cart, account, hamburger) padded to 44px hit areas
- Filter checkboxes and size selectors include a full-row tap target, not just the element itself
- Swatch tooltip replaced by immediate selection on mobile tap (no hover state)

### Collapsing Strategy
- Filter rail collapses to a slide-in drawer (left-anchored on tablet, bottom-sheet on mobile) triggered by a sticky "Filter & Sort" label-pill that follows the scroll
- Three-column grid reduces to two columns at 744px and one column below 744px, with card images expanding to full bleed
- Footer multi-column grid stacks into accordions on mobile, each column heading toggling content visibility
- Hero text repositions below the image on mobile rather than overlaying it, eliminating the need for a scrim at small sizes
- Editorial strip remains visible on mobile but reduces to a single line of copy with no dismiss button to preserve height

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Color palette almost entirely unextracted** — the Cloudflare bot-challenge page ("Just a moment...") returned only one hex value (#313131); all other color tokens (surface-soft, hairline, swatch-border, potential accent colors) are estimated from category conventions and are not confirmed from the live site
- **No brand typeface identified** — only system font stacks were captured; Ernesta likely loads a licensed geometric sans or editorial serif via JS or a CDN not reachable during extraction
- **No accent or secondary brand color confirmed** — premium rug brands frequently carry a warm tertiary (terracotta, sand, sage); this system omits one rather than fabricating it
- **Exact border-radius unknown** — {rounded.none} treatment is inferred from premium textile brand conventions; actual radius may be xs (4px) or sm (6px)
- **No motion or animation data** — transition durations and easing curves for hover states, filter drawer open/close, image lazy-load reveals, and swatch selection are entirely unspecified
- **Nav height and mega-menu structure unconfirmed** — 64px is estimated; whether top-level categories open a mega-menu or flat dropdown is unknown without live rendering
- **No dark mode tokens** — extraction did not reveal a dark-mode variant; assumed light-only
- **Product imagery aspect ratio unconfirmed** — 4:3 is estimated based on room-scene photography conventions; actual ratio may differ per product type or editorial module
