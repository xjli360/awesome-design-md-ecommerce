---
version: alpha
name: "Otiumberg"
source_url: "https://www.otiumberg.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Two typefaces split the work cleanly: Saol Display, a high-contrast editorial serif, owns the emotive moments — hero headers, lookbook captions, category openers — while Styrene A Web, a mid-century geometric grotesque, handles every transactional surface from navigation to price display and CTAs. This pairing is the structural core of Otiumberg's visual system; neither face bleeds into the other's territory. The full extracted palette spans #121212 to #dedede without a single warm note — an achromatic sequence that functions as purposeful substrate, engineered to disappear behind photographs of yellow gold hoops and oxidized silver stacks. Primary calls-to-action render on near-black (#191919) rather than a conventional brand accent, which signals that Otiumberg treats its UI as a recessive frame rather than a graphic statement. Whitespace does heavy lifting: the {spacing.section} rhythm between blocks is generous, and product grids breathe with visible gaps. Card corners sit at {rounded.none}, reinforcing the flat-plan, editorial-magazine feel; {rounded.full} is reserved for the occasional filter chip or pill tag. Navigation is stripped to essentials — wordmark, minimal category links, bag icon — with no megamenu complexity; the brand's curated catalog makes this restraint legible rather than sparse. Typography hierarchy compresses at the label level: caption text runs at 12px to stay subordinate to product imagery, but display text can climb to 52px in Saol Display for campaign heroes, where the serif's thick-thin stroke contrast carries luxury provenance. The London positioning shows not in flourishes but in their absence — no illustrated icons, no lifestyle color-blocking, no badge clusters. Form inputs carry a hairline border in #dedede that fades near-invisible on the white canvas, keeping the checkout experience unobtrusive.

colors:
  primary: "#191919"
  primary-active: "#121212"
  primary-disabled: "#555555"
  ink: "#191919"
  body: "#393939"
  muted: "#777777"
  muted-light: "#aaaaaa"
  hairline: "#dedede"
  hairline-strong: "#404143"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  dark-field: "#121212"

typography:
  display-xl:
    fontFamily: "'Saol Display', Georgia, 'Times New Roman', serif"
    fontSize: 52px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: -0.02em
  display-md:
    fontFamily: "'Saol Display', Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: -0.01em
  display-sm:
    fontFamily: "'Saol Display', Georgia, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.22
    letterSpacing: 0
  title-md:
    fontFamily: "'Styrene A Web', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Styrene A Web', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Styrene A Web', Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0
  body-sm:
    fontFamily: "'Styrene A Web', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Styrene A Web', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.02em
  price:
    fontFamily: "'Styrene A Web', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  button-md:
    fontFamily: "'Styrene A Web', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.08em
    textTransform: uppercase
  nav-label:
    fontFamily: "'Styrene A Web', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.01em
  filter-label:
    fontFamily: "'Styrene A Web', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.04em
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
    rounded: "{rounded.none}"
    padding: 14px 24px
    height: 48px
    border: none
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
    cursor: not-allowed
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 23px
    height: 48px
    border: "1px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
    outlineOnFocus: none
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 60px
    borderBottom: "1px solid {colors.hairline}"
    layout: "wordmark-left, links-center, icons-right"
  product-card:
    backgroundColor: "{colors.canvas}"
    imageRounded: "{rounded.none}"
    rounded: "{rounded.none}"
    titleTypography: "{typography.body-sm}"
    titleColor: "{colors.ink}"
    priceTypography: "{typography.price}"
    priceColor: "{colors.body}"
    gap: "{spacing.sm}"
    hoverBehavior: "cross-fade to secondary product image"
  hero:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    paddingVertical: "{spacing.section}"
    paddingHorizontal: "{spacing.xl}"
    layout: "text-left image-right on desktop; image-above text-below on mobile"
  collection-header:
    backgroundColor: "{colors.canvas}"
    headlineTypography: "{typography.display-md}"
    textColor: "{colors.ink}"
    subheadTypography: "{typography.body-md}"
    subheadColor: "{colors.muted}"
    paddingBottom: "{spacing.xl}"
    borderBottom: "1px solid {colors.hairline}"
    alignment: left
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.filter-label}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.filter-label}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.ink}"
    padding: 6px 14px
    height: 32px
  product-detail-title:
    typography: "{typography.display-sm}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.md}"
  product-detail-price:
    typography: "{typography.title-md}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.lg}"
  category-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.none}"
    padding: 4px 10px
  editorial-callout:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.body}"
    borderLeft: "2px solid {colors.hairline-strong}"
    paddingLeft: "{spacing.lg}"
  footer:
    backgroundColor: "{colors.dark-field}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    linkTypography: "{typography.nav-label}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    borderTop: none
    layout: "multi-column desktop (newsletter + links + social); stacked accordions mobile"

---

## Components

### Buttons

**`button-primary`** — Full-width-capable dark-field CTA on near-black (#191919) with white all-caps Styrene A Web type at 13px and 0.08em tracking. `{rounded.none}` enforces the editorial-flat geometry shared across all interactive surfaces. Hover darkens imperceptibly to #121212; disabled mutes the field to #555555 and removes pointer events. On mobile, commonly stretched to full container width for bag and checkout actions.

**`button-secondary`** — White field with a 1px ink-colored stroke, matching primary in height (48px) and typography so paired CTAs ("Add to Bag" / "Save to Wishlist") read as a coherent set. Hover lifts to surface-soft (#f5f5f5). The hairline border is fine enough to read as almost typographic — a ruled line rather than a box.

### Text Input

**`text-input`** — Hairline #dedede border on white canvas with `{rounded.none}` corners. On focus the border transitions to ink (#191919) without any glow or shadow — a binary shift that signals engagement cleanly. Placeholder renders in muted (#777777). Height of 48px aligns with buttons so form rows in search, newsletter, and checkout maintain visual rhythm without explicit spacing gymnastics.

### Navigation

**`nav-bar`** — 60px bar on white canvas, hairline-separated from the page body. Wordmark sits left; category links (Rings, Earrings, Necklaces, Bracelets, New In) occupy the center in nav-label-weight Styrene A Web; bag icon with numeric count badge anchors right. No megamenu — the curated catalog makes a simple flyout or direct link sufficient. On mobile, links collapse behind a burger icon that opens a full-screen overlay with generous vertical rhythm between items.

### Product Card

**`product-card`** — Square or portrait-ratio image with `{rounded.none}` corners and no drop shadow. Title in body-sm Styrene A Web (13px/400 weight), price in the same scale. On hover, a second editorial image cross-fades in — the standard fine-jewelry DTC convention for showing a model or detail view without requiring a PDP click. No quick-add or floating CTA appears over the image; Otiumberg routes selections through the full PDP to preserve the considered purchase cadence.

### Hero

**`hero`** — Campaign hero splits text left, editorial image right on desktop at roughly a 50/50 split; stacks image-above, text-below on mobile to preserve image-first impact. Headline in Saol Display at display-xl (52px, lh 1.08); any subhead or descriptor line drops to body-md Styrene A Web in muted (#777777). Background is white canvas throughout — no color-field overlays; photography provides all chromatic energy.

### Collection Header

**`collection-header`** — Category title in Saol Display at display-md (36px), optional descriptor in body-md muted. A 1px #dedede hairline border-bottom divides the header from the product grid below. Left-aligned for shop collections; center alignment may appear on editorial or lookbook entry points.

### Filter Chips

**`filter-chip`** / **`filter-chip-active`** — Pill-shaped (`{rounded.full}`) material and metal filter tags displayed as a horizontal scroll row above the product grid. Inactive state: white fill, hairline border, body color text. Active state: inverts to near-black fill (#191919), white text. All-caps Styrene A Web at 12px with 0.04em tracking maintains the brand's editorial label register without competing with product typography.

### Editorial Callout

**`editorial-callout`** — A prose block used inside lookbook and collection editorial pages: headline in display-md Saol Display, body in body-md Styrene A Web at body color (#393939). A 2px left border in hairline-strong (#404143) provides structural accent without introducing color. Used to contextualize collections with material or origin copy.

### Category Badge

**`category-badge`** — Surface-soft (#f5f5f5) fill, muted (#777777) text, caption-scale Styrene A Web, `{rounded.none}`. Appears inline within editorial layouts to label product type (e.g., "Rings", "Limited") adjacent to imagery, subordinate to both the headline and the product image.

### Footer

**`footer`** — Near-black (#121212) field providing visual closure against the white canvas body. White nav-label links arranged in columns: Collections, About, Journal, Legal. Newsletter signup block on the left: text-input (inverted border treatment) plus button-primary. Social icon row at bottom. On mobile, link columns collapse to tap-to-expand accordions with ink-tone hairline dividers.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to wordmark + burger icon; hero stacks image-above text-below; button-primary stretches full-width; filter chips scroll horizontally in a single row |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category links, drops secondary; hero may use a 55/45 text-image split; filter chips remain inline |
| Desktop | 1128–1440px | Three-column product grid; full nav visible with all category links; hero holds 50/50 split; collection header left-aligned with full descriptor |
| Wide | > 1440px | Four-column product grid; container max-width ~1400px centered in viewport; hero image scales within its column; Saol Display display-xl size holds at 52px |

### Touch Targets

- Minimum 44×44px for all interactive controls
- Filter chips use horizontal padding to hit 44px tap height despite 32px visual height
- Mobile nav overlay items spaced at `{spacing.xxl}` (48px) vertical rhythm minimum
- Bag and search icon hit areas extended to 44×44px regardless of icon glyph size
- Accordion toggles in footer carry full-width tap target across the row

### Collapsing Strategy

- Mobile navigation: full-screen overlay with category list and close button at top-right; no partial drawer
- Filter panel: horizontal scroll row on mobile; inline above grid on tablet and desktop
- Footer link columns: collapse to accordions on mobile with hairline dividers; three-column grid on desktop
- Hero: image drops below headline text on mobile; on desktop image fills the right column
- Product grid: 1 → 2 → 3 → 4 columns across breakpoints; no masonry — strict equal-ratio grid

---

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No warm or gold accent color was extracted — Otiumberg may use a champagne, parchment, or warm cream tone for editorial hero and lookbook backgrounds that did not surface in the CSS pass
- `surface-soft` (#f5f5f5) is interpolated from the white canvas and #dedede hairline range; not directly extracted from the site
- `muted-light` (#aaaaaa) is inferred between muted (#777777) and hairline (#dedede); not confirmed in source
- `hairline-strong` (#404143) has a slight warm undertone atypical for a pure brand token — may originate from image thumbnails, SVG icons, or theme artifacts rather than deliberate palette choice
- Saol Display weight range not confirmed; 400 (regular) assumed for all editorial contexts; a lighter 300 weight may exist for large display sizes
- Styrene A Web weight range not confirmed beyond regular/medium; 500 used for buttons and titles is assumed
- Footer treatment (dark vs. light) is inferred from the monochromatic palette convention; site may use a white or light-gray footer
- Hover and transition timing values (duration, easing) are not extractable from a static CSS pass
- Product card secondary-image hover behavior is unconfirmed — site may use a lightbox, color swatch toggle, or no hover state
- Mobile navigation overlay style (slide-in vs. full-screen fade) unconfirmed
- No sale, discount, or error color extracted; red or a warm secondary tone may exist but was absent from the extraction pass
- Monospace font stack found in extraction — purpose unknown; possibly a theme artifact, product code renderer, or developer-facing element
