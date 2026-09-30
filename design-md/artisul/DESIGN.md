---
version: alpha
name: "Artisul"
source_url: "https://www.artisul.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every primary CTA fires from #108474 — an emerald-teal that sits between oxidized copper and deep sea glass, a deliberately odd color choice for a graphics tablet brand and exactly why it works: it reads as "tools for making things" rather than the neutral black-and-white minimalism that dominates peripheral hardware. Against the teal, Artisul builds an unusually wide palette — deep navy (#0e1b4d) handles dark-section weight and editorial presence; electric yellow (#f1dc0c, nearly twinned by #fbcd0a) appears as a voltage highlight on promos and call-outs; and a family of cool tints — lavender-gray (#eeeff8), soft blue (#e5e9fa), powder blue (#d0e0fa) — suggests that different product lines (pen tablets, display tablets, pen mice) carry their own ambient surface color, each echoing the physical device's colorway. A muted purple (#887fc4), a medium ink-blue (#4770db), and a peach-blush (#efbcb4) extend the vocabulary further; the result is a palette that an illustrator or colorist would feel immediately at home inside. Type pairs Bricolage Grotesque — a wide-range variable grotesque that compresses beautifully at large optical sizes — with Outfit for interface and product prose; Bricolage earns its display weight at 56–40px, with just enough stroke contrast to signal creative tool without tipping into illustration-brand territory, while Outfit runs clean at 16–14px, letting product specifications and comparison tables breathe without competing with the teal-and-yellow energy above. Cards hold at {rounded.sm} (8px) — grounded enough to avoid the plasticky feel of over-rounded consumer gadget sites — and primary buttons match that radius at 48px height; the electric yellow functions best as a surface strip or badge fill with {colors.on-accent-yellow} (#121212) text rather than as a button, since the combination skews promotional rather than functional at that scale. Section backgrounds alternate between the near-white {colors.canvas}, cool blue-gray {colors.surface-blue}, and deep {colors.accent-navy} to give the product catalog clear visual hierarchy without relying solely on whitespace.

colors:
  primary: "#108474"
  primary-active: "#0c6b5e"
  primary-disabled: "#7fc4bb"
  accent-yellow: "#f1dc0c"
  accent-golden: "#fbcd0a"
  accent-navy: "#0e1b4d"
  accent-purple: "#887fc4"
  accent-blue: "#4770db"
  accent-blue-soft: "#d0e0fa"
  accent-pink: "#efbcb4"
  accent-warm: "#f4dba5"
  ink: "#121212"
  body: "#121212"
  muted: "#7b7b7b"
  hairline: "#dedede"
  hairline-mid: "#dadada"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#f9fafb"
  surface-card: "#eff0f5"
  surface-blue: "#eeeff8"
  surface-blue-light: "#e5e9fa"
  surface-warm: "#f7e2b5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-accent-yellow: "#121212"

typography:
  display-xl:
    fontFamily: "'Bricolage Grotesque', system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 800
    lineHeight: 1.07
    letterSpacing: -1.5px
  display-lg:
    fontFamily: "'Bricolage Grotesque', system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.8px
  display-md:
    fontFamily: "'Bricolage Grotesque', system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  title-lg:
    fontFamily: "'Bricolage Grotesque', system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-md:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.1px
  spec-label:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'Bricolage Grotesque', system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.3px
  badge-label:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.4px
    textTransform: uppercase
  nav-label:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Outfit', system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.2px

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
    padding: 13px 28px
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
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 27px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.primary-active}"
    border: "1.5px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent-yellow}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 28px
    height: 48px
  button-dark:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 28px
    height: 48px
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 9px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-dark:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-label}"
    height: 64px
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.base}"
    imageAspect: "4/3"
  product-card-tinted:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    rounded: "{rounded.sm}"
    border: none
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.title-md}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    ctaGap: "{spacing.sm}"
  hero-split:
    layout: "50/50 grid — copy left, product image right"
    backgroundColor: "{colors.surface-blue}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    subheadTypography: "{typography.title-md}"
    rounded: "{rounded.none}"
  promo-strip:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent-yellow}"
    typography: "{typography.badge-label}"
    height: 40px
    padding: "0 {spacing.base}"
  product-badge:
    backgroundColor: "{colors.surface-blue-light}"
    textColor: "{colors.accent-blue}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  product-badge-sale:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-accent-yellow}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  category-chip:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  category-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 20px"
  spec-row:
    backgroundColor: "{colors.canvas}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    borderBottom: "1px solid {colors.hairline-soft}"
    padding: "{spacing.md} 0"
  spec-row-alt:
    backgroundColor: "{colors.surface-soft}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
  review-card:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    metaTypography: "{typography.caption}"
    starColor: "{colors.accent-golden}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
  footer:
    backgroundColor: "{colors.accent-navy}"
    textColor: "{colors.on-dark}"
    bodyTypography: "{typography.body-sm}"
    headingTypography: "{typography.caption}"
    linkColor: "{colors.accent-blue-soft}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — The primary action fills with {colors.primary} (#108474) teal and sets white Outfit 16px/600 type. Height is fixed at 48px with {rounded.sm} (8px) corners so it reads as purposeful rather than decorative. On hover/active the fill darkens to {colors.primary-active} (#0c6b5e); disabled state uses the lightened {colors.primary-disabled} teal. This is the only button that should appear in product-card footers and hero CTA rows.

**`button-secondary`** — Outlined variant: transparent fill, 1.5px solid {colors.primary} border, teal text. Pairs directly with `button-primary` in two-button CTA groups ("Add to Cart" + "Compare" or "Buy Now" + "Learn More"). On active state the fill moves to {colors.surface-card} (#eff0f5) for clear tactile feedback without introducing a new color.

**`button-accent-yellow`** — Uses {colors.accent-yellow} (#f1dc0c) fill with {colors.on-accent-yellow} (#121212) ink. Reserved exclusively for sale events, limited-run promos, and `promo-strip` CTAs where the yellow already dominates the surrounding context. Do not place adjacent to {colors.accent-golden} (#fbcd0a) without a clear structural separator — the near-identical hues collapse at small sizes.

**`button-dark`** — {colors.accent-navy} (#0e1b4d) fill with {colors.on-dark} white type; the fallback primary action for hero sections where a teal button would fight a teal product image. Same Outfit 16px/600 spec and {rounded.sm} radius as `button-primary` — visually consistent, contextually distinct.

**`button-sm`** — Compact 36px teal button at Outfit 14px/600 and {rounded.sm}. Used for inline add-to-cart actions within product-listing rows and for collapsed mobile CTA states where the full 48px button would overwhelm the card.

### Navigation

**`nav-bar`** — 64px fixed header on {colors.canvas} with a 1px {colors.hairline-soft} bottom rule and Outfit 15px/500 nav links in {colors.ink}. The dark variant (`nav-bar-dark`) drops to {colors.accent-navy} with {colors.on-dark} text; used when the hero section bleeds full-width to the page edge so the nav reads as part of the dark panel rather than floating above it.

### Product Cards

**`product-card`** — White cards at {rounded.sm} with a 1px {colors.hairline-soft} border. Image area holds a 4/3 aspect ratio (standard tablet device photography). Product name in `title-sm`, price in `price-display` (Bricolage Grotesque 28px/700 — the weight makes pricing feel decisive rather than incidental), category badge overlaid at top-left corner. The tinted variant (`product-card-tinted`) swaps the background to {colors.surface-card} (#eff0f5) for featured-product rails and homepage spotlights where the lavender-white gives slight depth against the page canvas.

### Hero

**`hero`** — Full-bleed {colors.accent-navy} section at 560px minimum height. Headline in `display-xl` (Bricolage Grotesque 56px/800, tight −1.5px tracking), subhead in `title-md` (Outfit 20px/600). CTA row holds `button-primary` + `button-secondary` at {spacing.sm} horizontal gap. The `hero-split` variant shifts to {colors.surface-blue} (#eeeff8) with a 50/50 grid layout — copy on the left, product image floating right — suited for mid-page line introductions and feature announcements where the navy would feel too heavy.

### Promo & Badges

**`promo-strip`** — A 40px full-width announcement bar in {colors.accent-yellow} with {colors.on-accent-yellow} text at `badge-label` uppercase. Sits above the nav at the very top of the page stack. The high-chroma yellow registers immediately even at the minimal 40px height; keep copy under 60 characters to avoid truncation on 375px viewports.

**`product-badge`** — Soft {colors.surface-blue-light} (#e5e9fa) pill at {rounded.xs} for line labels (PEN TABLET, DISPLAY TABLET, PEN MOUSE). `product-badge-new` fills with {colors.primary} teal; `product-badge-sale` fills with {colors.accent-yellow} and {colors.on-accent-yellow} ink. All three variants use `badge-label` (11px/700 uppercase, 0.4px tracking) and 3px/8px padding for compact placement over product-card images.

**`category-chip`** — Pill filter tabs ({rounded.full}) for the product catalog filter rail. Inactive state uses {colors.surface-card} background with {colors.muted} text; active state fills with {colors.primary} and flips to {colors.on-primary} white. Chips scroll horizontally on mobile, wrap in a sidebar grid on desktop. Gap between chips is {spacing.sm}.

### Specs & Reviews

**`spec-row`** — Horizontal label/value pair for product specification tables. Label in `spec-label` (Outfit 11px/600 uppercase, {colors.muted}); value in `body-sm` ({colors.ink}). Alternating rows use `spec-row-alt` with {colors.surface-soft} (#f9fafb) background for zebra contrast without a hard border. Bottom hairline uses {colors.hairline-soft}; padding is {spacing.md} top and bottom, flush to column edges.

**`review-card`** — Warm cream ({colors.surface-warm}, #f7e2b5) card at {rounded.sm} with star icons rendered in {colors.accent-golden} (#fbcd0a). Reviewer name and date in `caption` (12px/500); review body in `body-sm`. Arranged in a 2-column masonry grid on desktop product detail pages, single column on mobile. The warm cream surface distinguishes the social proof zone from the cool surface-blue spec sections above it.

### Footer

**`footer`** — Full-bleed {colors.accent-navy} (#0e1b4d) panel with Outfit `body-sm` text in {colors.on-dark}. Column headings in `caption` (12px/500, white). Links use {colors.accent-blue-soft} (#d0e0fa) — the powder blue reads legibly against the deep navy and ties back to the product-line tint vocabulary used on surface-blue sections above. No decorative top border; the color break from the content background above is sufficient.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero min-height drops to 420px; `display-xl` scales to 32px; promo-strip shows single static message; category-chips scroll horizontally; hero CTA buttons stack vertically |
| Tablet | 744–1128px | Two-column product grid; `hero-split` stacks image above copy rather than side-by-side; nav shows primary links and collapses secondary items to "More" dropdown; spec table shifts to full-width single-column |
| Desktop | 1128–1440px | Three-to-four column product grid; full nav-bar with all links visible; hero split layout at true 50/50; spec table in two-column label/value pairs; category-chip rail becomes vertical sidebar filter |
| Wide | > 1440px | Content grid caps at 1440px centered; full-bleed backgrounds (hero navy, promo-strip yellow, footer navy) extend edge-to-edge while content stays in the max-width container; product grid holds at four columns |

### Touch Targets

- All buttons minimum 48px height; `button-sm` minimum 44px on mobile via padding increase
- Category chips minimum 44px tall on mobile regardless of text size
- Nav hamburger icon tap area padded to 44×44px
- Product card entire surface is tappable (not just the title text link)
- Review star row padded to 32px height on mobile for re-rating interactions

### Collapsing Strategy

- Promo-strip: ticker/carousel disabled on mobile; single highest-priority message shown statically
- Product filter rail: horizontal scroll strip on mobile and tablet; vertical sidebar on desktop ≥ 1128px
- Hero CTA row: inline with {spacing.sm} gap on tablet+; stacked column with {spacing.sm} gap on mobile
- Nav: hamburger slide-out drawer on mobile and tablet < 1128px; full horizontal bar on desktop
- Spec table: single-column stacked (label above value, full width) on mobile; two-column grid on tablet+
- Footer column grid: single-column stack on mobile; two-column on tablet; four-column on desktop

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- `primary-active` (#0c6b5e) and `primary-disabled` (#7fc4bb) are derived by darkening and lightening the extracted primary — not captured directly from the live site
- `on-primary` (#ffffff) and `on-dark` (#ffffff) are inferred white; white does not appear in the extracted hex list and may differ slightly from the site's actual value
- Body text color between ink (#121212) and a mid-dark gray was not separable from extraction; a standard #3c3c3c or similar body shade may exist on the live site but was not captured
- The muted purple (#887fc4), ink-blue (#4770db), and peach-blush (#efbcb4) appear in the extraction but their exact component assignments (product-line color-coding vs. UI states vs. illustration assets) could not be confirmed from static extraction alone
- Animation and motion tokens (button hover transition duration, hero scroll parallax, carousel timing) are absent from static extraction
- Exact nav height, grid gutter widths, and section padding values are estimated from Shopify category conventions rather than extracted from computed styles
- JudgemeStar appears in the font-family stack as a review icon glyph font, not a text typeface — excluded from typography tokens
