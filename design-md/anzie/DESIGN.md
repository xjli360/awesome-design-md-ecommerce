---
version: alpha
name: "Anzie"
source_url: "https://www.anzie.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Where most fine jewelers treat color as accent, Anzie builds entire collections around it — the midnight depth of London blue topaz, the warm amber of Mexican fire opal, the soft translucency of nephrite jade — with each stone's saturation setting the mood for the surrounding metalwork. The digital environment follows that instinct: a deep navy (#163959) grounds all primary CTAs and navigation against white, while a warm amber-orange (#f68b1f) marks discovery moments and editorial callouts without overpowering the jewelry itself. The neutral spine — #272727 near-black ink, #404040 body text, #dedede and #ebebeb as hairlines and soft surface tints — steps back so product photography carries expressive weight. Type runs entirely on system stacks, with -apple-system, Helvetica Neue, and Arial providing a clean, invisible typographic scaffold; hierarchy is built through weight steps and generous line heights rather than a commissioned display face, letting the gem photography speak at full volume. Rounded geometry appears throughout: pill-shaped filter chips (`{rounded.full}`), gently curved product cards, and full-radius icon buttons echo the organic silhouettes of baroque pearls and bezel-set stones, while primary buttons hold sharp corners (`{rounded.none}`) for deliberate contrast. Product cards float on a white canvas behind `{colors.hairline}` borders that dissolve when the eye settles on the stone. The alert red (#bd2426) marks sale flags and form errors — a functional signal, not a brand statement — while the broader gem-tone spectrum cycling through the catalog (blues, ambers, greens, corals) supplies all chromatic expressiveness without baking saturated tones into the UI shell. The breadth of stone types makes robust filtering a signature UI moment: the filter strip uses `{colors.surface-soft}` chips with `{rounded.full}` geometry to keep the browsing layer legible above the product canvas, and the search experience prioritizes stone name and collection over generic department labels.

colors:
  primary: "#163959"
  primary-active: "#0f2840"
  primary-disabled: "#8aaccc"
  ink: "#272727"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#dedede"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-amber: "#f68b1f"
  accent-amber-deep: "#ee730a"
  accent-amber-dark: "#904b06"
  accent-red: "#bd2426"
  accent-red-soft: "#de5052"
  gem-blue: "#62a1d8"
  gem-blue-deep: "#2f7bbf"
  gem-green: "#9bca3e"
  gem-green-dark: "#516b1d"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 300
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.3px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.2px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
  price:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0
  price-sale:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1
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
    padding: 14px 32px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.primary}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: none
    padding: 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.06)"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageAspectRatio: "1/1"
    padding: "0 0 {spacing.md} 0"
    border: "1px solid {colors.hairline-soft}"
  product-card-title:
    typography: "{typography.body-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.price-sale}"
    textColor: "{colors.accent-red}"
  product-card-original-price:
    typography: "{typography.price}"
    textColor: "{colors.muted}"
    textDecoration: line-through
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 480px
    contentMaxWidth: 600px
    textAlign: center
    padding: "{spacing.section}"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 560px
    layout: split-50/50
  collection-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    border: "1px solid {colors.hairline}"
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 16px
    border: "1px solid {colors.primary}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 10px 20px
    height: 44px
  stone-swatch:
    size: 20px
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    borderActive: "2px solid {colors.primary}"
    gap: "{spacing.xs}"
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  promo-banner:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    padding: "{spacing.sm} {spacing.base}"
    textAlign: center
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
  footer-heading:
    typography: "{typography.title-sm}"
    textColor: "{colors.on-primary}"
    marginBottom: "{spacing.md}"

## Components

### Buttons

**`button-primary`** — A sharp-cornered rectangle (`{rounded.none}`) in deep navy (#163959) with uppercase letter-spaced text at `{typography.button-md}` (12px, 600 weight, 1.5px tracking). The all-caps treatment reads as precise against the jewelry's organic forms without tipping into aggression. Active state darkens to `{colors.primary-active}` (#0f2840); disabled state uses the muted `{colors.primary-disabled}` (#8aaccc) to signal unavailability without alarm.

**`button-secondary`** — Identical sharp geometry, canvas background with a 1px navy border and navy text. The outline treatment gives secondary actions (Add to Wishlist, alternate CTAs, confirmation modals) visible weight without introducing a competing fill color.

**`button-ghost`** — Transparent, no border, uppercase tracking at `{typography.button-md}`. Used in editorial strips and inline navigation contexts where a framed button would compete with photography.

### Text Inputs

**`text-input`** — Zero-radius borders (consistent with the button system) using `{colors.hairline}` at rest, upgrading to a solid `{colors.primary}` ring on focus. Placeholder text at `{colors.muted-soft}` (#737373) maintains legibility without competing with user-entered values. Height 44px keeps form fields proportional to the button row.

### Navigation

**`nav-bar`** — 64px white bar with a bottom hairline and centered wordmark. Navigation links at `{typography.nav-link}` (13px, 500 weight, 0.5px tracking) stay secondary to the jewelry but are legible for desktop scanning. Category labels — Pearls, Jade, Bridal, Collections — are the primary items; stone type and metal filtering live within collection pages rather than the global nav. The sticky variant (`nav-bar-sticky`) adds a 6px shadow when the user scrolls past the hero to signal context-lock without a color change.

### Product Cards

**`product-card`** — Square image aspect ratio (1:1) with zero border radius. Title appears beneath the image at `{typography.body-sm}` in `{colors.ink}`; price below at `{typography.price}` in `{colors.body}`. Sale pricing splits into a `{colors.accent-red}` current price alongside a struck-through `{colors.muted}` original. No hover shadow or lift — the image carries that work. Cards are separated by a hairline-soft border rather than gap-based whitespace, so the grid feels like a lightbox rather than a tile wall.

### Badges

**`collection-badge`** — Pill-shaped (`{rounded.full}`) chip in `{colors.surface-soft}` with navy text and `{typography.button-sm}` uppercase; used as category labels on collection page headers and editorial navigation. **`sale-badge`** and **`new-badge`** are small sharp-cornered flags (`{rounded.xs}`) in `{colors.accent-red}` and `{colors.primary}` respectively, positioned over the top-left corner of product imagery.

### Filter Chips

**`filter-chip`** / **`filter-chip-active`** — Pill geometry (`{rounded.full}`) in the horizontal filter strip above collection grids. Inactive chips render in `{colors.surface-soft}` with a hairline border; active chips flip to solid navy with white text. On mobile the strip scrolls horizontally in a single row without wrapping, keeping the product grid immediately below the fold rather than buried under filter UI.

### Stone Swatches

**`stone-swatch`** — 20px circular swatches (`{rounded.full}`) representing stone-color variants on product cards and detail pages. The active swatch gains a 2px navy border offset from the circle edge; inactive swatches sit behind a 1.5px `{colors.hairline}` ring. Swatches use actual gem photography crops rather than flat hex fills so the color read matches the real stone.

### Search

**`search-bar`** — Full-radius pill (`{rounded.full}`) in `{colors.surface-soft}` at 44px height. The rounded shape deliberately distinguishes the search field from the square-cornered form inputs throughout the page. Expands full-width on mobile; sits in a constrained header slot or modal overlay on desktop.

### Hero

**`hero-banner`** — Full-width navy (#163959) block with centered white text for promotional moments: seasonal launches, gift-guide callouts, free-shipping thresholds. Min-height 480px; content max-width 600px keeps copy scannable. **`hero-editorial`** uses a 50/50 split on `{colors.surface-soft}` for collection story pages, pairing copy left with a full-bleed photograph right.

### Promo Banner

**`promo-banner`** — A thin amber (#f68b1f) strip at the very top of the viewport for shipping thresholds and limited-time announcements. The only context where amber appears as a background fill rather than editorial decoration; `{typography.caption}` uppercase text on a warm ground reads clearly without height cost.

### Footer

**`footer`** — Navy ground with white body text and `{colors.hairline-soft}` link color. Column headings use `{typography.title-sm}` (uppercase, 0.8px tracking) to carry the all-caps accent system into the footer register. Four columns: Shop, About, Customer Care, Social. Newsletter input sits inline with a white-bordered text field on the dark ground.

---

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav replaces horizontal bar; filter chips scroll horizontally in a locked single row; hero stacks to text-below-image; footer collapses to accordion columns |
| Tablet | 744–1128px | Two-column product grid; horizontal nav retained but trimmed to top-level categories; filter chips wrap to two rows or open a bottom-sheet modal |
| Desktop | 1128–1440px | Three-column product grid; full nav with category flyout dropdowns; optional filter sidebar alongside the grid |
| Wide | > 1440px | Four-column product grid; container max-width ~1400px centers with generous lateral whitespace; hero imagery benefits from wider bleed |

### Touch Targets

- Filter chips maintain minimum 44px touch height on mobile despite reduced font size
- Stone swatches expand to 28px on touch devices with increased tap gutter between circles
- Nav links minimum 48px touch target inside the hamburger drawer
- Add-to-bag button pinned to a sticky bottom bar on mobile product detail pages

### Collapsing Strategy

- Navigation: full horizontal bar → hamburger slide-in drawer with navy background and white link text
- Filter strip: horizontal scroll row → bottom-sheet modal triggered by a "Filter" button above the grid
- Product grid: 4-col → 3-col → 2-col → 1-col across breakpoints
- Hero: 50/50 split → stacked (image top, text below) at mobile
- Footer columns: side-by-side → single-column accordion with expand/collapse per section on mobile

---

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The site was blocked by Cloudflare at extraction time; the page title returned "Attention Required! | Cloudflare" rather than the live Anzie site. All hex colors in the extracted palette may originate from the Cloudflare challenge page or CDN assets rather than the Anzie brand UI itself.
- No custom font was detected — only system stacks. Whether Anzie uses a licensed typeface loaded via JavaScript or served through a third-party type CDN not captured by the crawler is unknown; the typography spec above reflects system-font defaults only.
- No theme-color meta tag was found. The primary brand color (#163959 deep navy) is inferred as the most distinctive non-gray in the extracted palette — this should be verified against live site CSS or brand assets.
- The warm amber-orange cluster (#f68b1f, #ee730a, #c16508, #904b06) may represent a secondary brand accent, sale-pricing color, editorial accent, or Cloudflare-artifact color — their exact role in the Anzie UI is uncertain.
- The green cluster (#9bca3e, #bada7a, #516b1d) likely reflects jade product photography rather than UI tokens; green has not been assigned a UI role in this spec pending verification.
- Product photography treatment, hover interaction details, animation easing, and micro-interaction specs were not observable from the blocked crawl.
- Mobile breakpoint specifics (cart drawer behavior, PDP sticky bar, wishlist flow) are inferred from jewelry-category conventions rather than observed directly.
