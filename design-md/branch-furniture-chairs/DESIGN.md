---
version: alpha
name: "Branch Furniture (Chairs)"
source_url: "https://www.branchfurniture.com/collections/office-chairs"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The browser chrome itself bleeds #314438 on mobile — Branch commits its forest-green primary so completely that it colonizes the OS status bar, not just the nav. That dark, resinous green sits against cream grounds (#faf8f4, #f3eeea) that recall natural materials rather than the sterile white of most workspace brands, and the warmth sharpens when terracotta (#da5f4d) surfaces on CTAs and promotional callouts. Sage (#9fb59e) and dusty muted sky (#8cc1d2) provide a nature-derived secondary palette that keeps the overall atmosphere closer to a well-appointed home study than to a conventional office supply catalog.

  Type leads with Frank Ruhl Libre, a serif with roots in Hebrew type design — slightly compressed, dignified, with ink traps that give it an artisanal edge at display sizes. It delivers product names and headlines with editorial gravity that no geometric sans could match for a brand selling furniture that's meant to look good in a room. Koulen, an aggressively condensed display face, handles high-contrast feature labels and promotional banners where compact verticality and uppercase geometry matter. Quicksand carries all functional UI — navigation, buttons, form fields, body copy — in a rounded, approachable weight that keeps the purchase flow light and accessible.

  Geometry is restrained throughout. Buttons use modest radii ({rounded.sm}, 8px) — not the pill-shaped softness of consumer apps, not the hard corners of enterprise procurement software. Cards read as professional but unpretentious. Product photography governs the canvas, and the palette's discipline means a single terracotta badge ({colors.accent}) reads as urgency against the forest and cream without any surrounding noise. A bright teal (#00caaa) and a pale mint ({colors.mint-pale}) appear in review widgets and trust callouts, signaling a brand layering credibility signals without overcrowding the visual field. The spacing system favors generous section breaks ({spacing.section}: 64px) and deliberate breathing room between product specifications, reinforcing an unhurried, considered purchase experience.

colors:
  primary: "#314438"
  primary-active: "#22312a"
  primary-disabled: "#9fb59e"
  accent: "#da5f4d"
  accent-hover: "#c44c3b"
  accent-light: "#f3eeea"
  sage: "#9fb59e"
  teal: "#00caaa"
  mint-pale: "#b2f9e9"
  sky-muted: "#8cc1d2"
  ink: "#212225"
  body: "#333f48"
  muted: "#6b6b6b"
  muted-soft: "#848484"
  hairline: "#d6dad7"
  hairline-soft: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f9f9f9"
  surface-warm: "#f3eeea"
  surface-card: "#faf8f4"
  on-primary: "#ffffff"
  on-accent: "#ffffff"
  slate-dark: "#272d45"
  navy: "#2c3e50"

typography:
  display-xl:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  koulen-display:
    fontFamily: "'Koulen', sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1px
    textTransform: uppercase
  koulen-label:
    fontFamily: "'Koulen', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  title-md:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Quicksand', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  price-lg:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Frank Ruhl Libre', Georgia, serif"
    fontSize: 16px
    fontWeight: 500
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-accent:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-accent-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
    borderWidth: 2px
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    borderColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    borderColor: "{colors.hairline}"
    borderColorFocus: "{colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline-soft}"
    logoColor: "{colors.primary}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  announcement-bar:
    backgroundColor: "{colors.slate-dark}"
    textColor: "{colors.canvas}"
    typography: "{typography.caption}"
    height: 36px
    linkColor: "{colors.mint-pale}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline-soft}"
    borderWidth: 1px
    rounded: "{rounded.md}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-lg}"
    captionColor: "{colors.muted}"
  product-card-hover:
    borderColor: "{colors.primary}"
    boxShadow: "0 4px 16px rgba(49,68,56,0.12)"
  product-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-sale:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-accent}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
    overlayOpacity: 0.4
  hero-warm:
    backgroundColor: "{colors.surface-warm}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xl}"
  filter-sidebar:
    backgroundColor: "{colors.canvas}"
    borderRight: "1px solid {colors.hairline}"
    labelTypography: "{typography.title-sm}"
    optionTypography: "{typography.body-sm}"
    activeColor: "{colors.primary}"
    checkboxColor: "{colors.primary}"
    width: 260px
  color-swatch:
    borderRadius: "{rounded.full}"
    size: 24px
    selectedBorder: "2px solid {colors.primary}"
    defaultBorder: "1px solid {colors.hairline}"
  breadcrumb:
    textColor: "{colors.muted}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
  price-display:
    textColor: "{colors.ink}"
    typography: "{typography.price-lg}"
    salePriceColor: "{colors.accent}"
    originalPriceColor: "{colors.muted}"
    originalPriceDecoration: line-through
  review-widget:
    backgroundColor: "{colors.surface-soft}"
    starColor: "{colors.teal}"
    textColor: "{colors.ink}"
    captionColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  feature-callout:
    backgroundColor: "{colors.surface-warm}"
    borderLeft: "4px solid {colors.primary}"
    textColor: "{colors.body}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
  comparison-table:
    headerBackgroundColor: "{colors.primary}"
    headerTextColor: "{colors.on-primary}"
    headerTypography: "{typography.koulen-label}"
    rowAlternateColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    checkColor: "{colors.teal}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.sage}"
    linkColorHover: "{colors.canvas}"
    headingTypography: "{typography.koulen-label}"
    bodyTypography: "{typography.body-sm}"

## Components

### Buttons

**`button-primary`** — The primary CTA uses Branch's forest green (#314438) fill with white Quicksand 700 text at 15px and a 0.5px letter-spacing push. Border radius is {rounded.sm} (8px) — structured enough to match the product's built-quality positioning, approachable enough to not feel institutional. Hover deepens to #22312a; disabled state fades to sage (#9fb59e) with white text.

**`button-accent`** — Terracotta (#da5f4d) buttons appear on promotional CTAs, sale events, and high-urgency add-to-cart flows where forest green is already saturating the page chrome. Same geometry as `button-primary` (48px height, {rounded.sm}), but the warm-against-cool contrast guarantees visibility without alarm. Hover steps to #c44c3b.

**`button-secondary`** — A 2px forest-green border on white fill with green Quicksand text. Used in side-by-side CTA groups alongside `button-primary` — "Add to Cart" / "Compare Models" pairings. Hover shifts fill to {colors.surface-soft} and deepens border to {colors.primary-active}.

**`button-ghost`** — Underlined green text link, no box or border. Used in footer secondary links, inline editorial callouts, and anywhere a bordered button would over-weight the visual hierarchy.

### Navigation

**`nav-bar`** — 64px white bar with a 1px soft hairline bottom border ({colors.hairline-soft}). The Branch wordmark renders in primary forest green. Nav links are Quicksand 600 at 14px with 0.2px letter spacing. Hover and active state draw a 2px forest-green underline below the link text. Sale or promotional category links use {colors.accent} terracotta text to signal without a separate badge.

**`announcement-bar`** — 36px dark slate (#272d45) strip pinned above the nav. White Quicksand caption text for the message; inline links use pale mint (#b2f9e9) — bright enough to read against the near-black strip but warm enough not to jar against the forest-green nav below.

### Product Cards

**`product-card`** — Warm cream ({colors.surface-card}, #faf8f4) background with a 1px soft hairline border and {rounded.md} (12px) corner radius. Product name uses {typography.title-sm} (Quicksand 600 at 16px); price uses {typography.price-lg} (Frank Ruhl Libre 700 at 24px) — the serif price treatment gives transaction data editorial weight and differentiates it visually from the sans-serif label above. On hover, the border steps to forest green and a soft, green-tinted shadow lifts the card. Sale price renders in terracotta ({colors.accent}); original price in {colors.muted} with line-through.

**`product-badge`** / **`product-badge-new`** / **`product-badge-sale`** — Small uppercase tags (Quicksand 700, 11px, 0.4px tracking, {rounded.xs}) sitting absolute top-left on product card images. "SALE" and urgency badges use terracotta; "NEW" and editorial tags use forest green. The badge system is intentionally minimal — one badge per card maximum to keep the product grid readable.

### Hero

**`hero`** — Full-width green (#314438) section or lifestyle photography with a 40% dark overlay. Headline is Frank Ruhl Libre 700 at 52px with -0.5px tracking — editorial, not promotional. Subhead is Quicksand body at 16px. Primary CTA uses `button-accent` (terracotta) for contrast against the dark ground; secondary CTA inverts to a white-border/white-text outline variant of `button-secondary`.

**`hero-warm`** — A warm cream ({colors.surface-warm}, #f3eeea) variant used for feature sections, mid-page product highlight banners, and "Why Branch" editorial blocks. Forest-green Frank Ruhl Libre headline, Quicksand body, `button-primary` CTA.

### Filters & Discovery

**`filter-sidebar`** — 260px left-rail column on desktop containing category tree, price range slider, color filter, and material filter. Section headers in {typography.title-sm} (Quicksand 600); filter options in {typography.body-sm}. Active checkbox and selected filter chips use forest green. On tablet and mobile, the sidebar collapses into a full-screen left-to-right drawer triggered by a sticky "Filter" button in the product grid toolbar.

**`color-swatch`** — 24px circular swatches with a 1px {colors.hairline} default ring; selected state shows a 2px forest-green border. Used on collection-page product cards to preview color variants inline, and on PDP to switch the hero image without a page reload.

### Reviews & Trust

**`review-widget`** — Off-white ({colors.surface-soft}) cards with {colors.teal} (#00caaa) five-star icons — a distinctive pairing that keeps star ratings legible against both the green nav and cream page backgrounds without competing with primary CTA color. Review body text is {typography.body-sm}; reviewer name and date in {colors.muted}.

### Comparison & Feature Content

**`comparison-table`** — Forest green header row with white Koulen uppercase column labels. Alternating data rows use {colors.surface-soft}. Checkmarks render in teal (#00caaa) — creating a three-color trust language (green = structure, teal = affirmation, terracotta = action) across the page. Used on collection pages to compare chair models across lumbar support, seat depth, weight capacity, and armrest adjustability.

**`feature-callout`** — Warm cream box ({colors.surface-warm}) with a 4px left border in forest green, {rounded.sm} corners. Used inline on PDPs to surface warranty details, free shipping thresholds, and ergonomic certifications. Heading in {typography.title-sm}, body in {typography.body-sm}.

### Pricing

**`price-display`** — Frank Ruhl Libre 700 at 24px for current price in {colors.ink}. Sale price in {colors.accent} terracotta; original price in {colors.muted} with line-through. The deliberate use of the brand's editorial serif for price — rather than the UI Quicksand — elevates price from a transactional data point to a considered element of the page composition.

### Footer

**`footer`** — Full forest-green (#314438) background provides a strong visual anchor at the bottom of the page. Column headers use Koulen uppercase at 14px/0.8px tracking — the same structural label style as comparison table headers, creating visual cohesion between informational architecture across the page. Link text is sage (#9fb59e) at rest, white on hover. No top border needed; the green fill terminates the cream-and-white page without a dividing line.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, filter sidebar becomes full-screen left drawer, hero headline scales to {typography.display-md} (28px), nav collapses to hamburger with forest-green icon, announcement bar wraps to two lines if needed, comparison table scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid, filter sidebar becomes collapsible accordion pinned above the grid, hero headline scales to {typography.display-lg} (40px), nav shows primary product categories with overflow in hamburger, comparison table scrolls horizontally |
| Desktop | 1128–1440px | Three-column product grid with persistent 260px left filter sidebar, full 64px nav bar, hero at full {typography.display-xl} (52px), comparison table fully visible |
| Wide | > 1440px | Content max-width capped at 1440px centered on canvas, product grid remains three columns with wider gutters ({spacing.xxl} between columns), filter sidebar expands to 300px, hero gains lateral padding ({spacing.section} horizontal) |

### Touch Targets

- All interactive controls (buttons, swatches, filter checkboxes, nav links) maintain a minimum 44×44px touch target
- Color swatches are 24px visual size surrounded by transparent 10px tap zones to reach 44px
- Filter option rows on mobile expand to full-width 48px tap height regardless of text length
- Drawer close controls are positioned top-right corner at a minimum 44×44px hit area
- Add-to-cart button spans full width on mobile at 52px height for thumb-friendly reach

### Collapsing Strategy

- Announcement bar: visible at all breakpoints; wraps to two lines on mobile before hiding overflow with an ellipsis
- Nav bar: primary product categories (Chairs, Desks, Accessories) promoted to visible on tablet; all remaining links in slide-out drawer; cart icon and account icon always pinned right
- Filter sidebar: persistent left column on desktop (260px); horizontal accordion above grid on tablet; full-screen left-to-right drawer on mobile triggered by sticky filter button
- Comparison table: full display on desktop; horizontal scroll container on tablet; collapses to stacked feature-card rows on mobile
- Hero copy block: overlays image with dark scrim on desktop; stacks above image on mobile with image cropped to 3:2
- Footer grid: four columns on desktop, two on tablet, single-column accordion on mobile with each section expandable via Koulen header tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact button border-radius values not confirmed from CSS extraction — {rounded.sm} (8px) inferred from visual category conventions for DTC office furniture
- Frank Ruhl Libre weight variants and precise size scale not confirmed via extraction — weights 500/600/700 attributed from visual hierarchy inference
- Koulen usage breakdown (which contexts use it vs. Quicksand) not fully resolved — attributed to structural labels, comparison headers, and footer column heads based on font character and visual weight
- Exact nav bar height (64px) not confirmed — inferred from standard Shopify DTC patterns
- Hover and focus ring styles not extracted — modeled from primary forest-green palette logic
- Animation and transition timing values not present in extraction hints
- #8cc1d2 and #8dc0d2 appear nearly identical — likely a sub-pixel rounding artifact in the extractor; consolidated to single `sky-muted` token
- #676986, #7b7e89, #9a9db1 form a purple-gray family likely sourced from review/ratings widgets (Okendo, given `oke-widget-icons` font hint) — not assigned primary component roles due to unclear first-party usage
- Mobile-specific typography scale not extracted — breakpoint downsizing inferred from responsive conventions
- Whether Quicksand or Frank Ruhl Libre is used for the logotype not confirmed — forest-green color confirmed, letterform unconfirmed
