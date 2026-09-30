---
version: alpha
name: "Shark"
source_url: "https://www.sharkclean.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep forest green (#33785d) and lavender (#cbc3e3) should not coexist in a vacuum brand's palette — yet together they index precisely on what SharkNinja is attempting: pulling household cleaning out of the hardware aisle and into a lifestyle register that sits somewhere between premium wellness and high-street tech. The near-white canvas (#f6f6f6) is the primary visual surface; sage (#bedccb) coats feature callout strips and bestseller badge chips; lavender (#cbc3e3) marks seasonal promotions and campaign modules; the forest green (#33785d) owns every primary action — add to cart, shop now, apply filter — creating a three-accent color grammar that doubles as implicit information architecture. No custom font stack was recoverable from the live site, pointing to a JS-loaded or self-hosted typeface; system sans-serif fills the typography tokens here until confirmed. The rounded corner register is moderate — 8px on buttons, 12px on cards, full-radius on filter and category pills — sitting between the hard utility of power-tool brands and the pillowy softness of beauty DTC. A 36px promotional strip in primary green runs above the 64px main header, keeping free-shipping thresholds and limited-time pricing permanently visible without interrupting navigation. Trust signals occupy their own between-section gray strip: "50 million sold," media endorsements, and efficiency award marks render at caption scale, readable without demanding attention. Product cards surface rating aggregates immediately and expose compare-mode via ghost buttons alongside primary CTAs — a layout suited to considered, multi-product purchases at $200–$600 appliance price points. The mega-nav organizes an unusually broad product taxonomy — vacuums, robots, hair tools, kitchen appliances, beauty devices — into product-family tabs, reflecting SharkNinja's parent-company breadth while keeping the Shark brand focused on cleaning authority.

colors:
  primary: "#33785d"
  primary-active: "#265e47"
  primary-disabled: "#8fb8a7"
  accent-lavender: "#cbc3e3"
  accent-sage: "#bedccb"
  ink: "#1a1a1a"
  body: "#333333"
  muted: "#666666"
  hairline: "#e0e0e0"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  star-fill: "#f5a623"
  badge-sale: "#e53935"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.55
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
    letterSpacing: 0
  caption-strong:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.6px
    textTransform: uppercase
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  price-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-was:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
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
    textColor: "{colors.primary}"
    border: "2px solid {colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 26px
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    border: "1px solid {colors.hairline}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 40px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "2px solid {colors.primary}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-promo-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    height: 36px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageRounded: "{rounded.md}"
    imageAspectRatio: "1 / 1"
  product-card-badge:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-card-sale-badge:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  rating-chip:
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
    starFill: "{colors.star-fill}"
    gap: "{spacing.xs}"
  price-current:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
  price-original:
    textColor: "{colors.muted}"
    typography: "{typography.price-was}"
    textDecoration: line-through
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 520px
    padding: "{spacing.xxl} {spacing.section}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    ctaRounded: "{rounded.sm}"
  hero-banner-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    minHeight: 520px
    padding: "{spacing.xxl} {spacing.section}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.body-md}"
    ctaRounded: "{rounded.sm}"
  promo-banner:
    backgroundColor: "{colors.accent-lavender}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    padding: "{spacing.lg} {spacing.section}"
    rounded: "{rounded.none}"
  feature-strip:
    backgroundColor: "{colors.accent-sage}"
    textColor: "{colors.ink}"
    padding: "{spacing.xxl} {spacing.section}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
  feature-strip-white:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.xxl} {spacing.section}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
  trust-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    padding: "{spacing.lg} {spacing.section}"
    borderTop: "1px solid {colors.hairline}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    height: 36px
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-strong}"
    rounded: "{rounded.full}"
    padding: 8px 16px
    height: 36px
  filter-pill:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 6px 14px
    height: 36px
  filter-pill-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 6px 14px
    height: 36px
  email-capture:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    inputRounded: "{rounded.sm}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonRounded: "{rounded.sm}"
    padding: "{spacing.section}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Deep forest green (#33785d) fill with white uppercase text at 0.6px tracking. Hover state deepens to #265e47; disabled washes to the muted sage #8fb8a7. The 8px radius and all-caps weight give it utilitarian authority without the softness of pill-shaped CTAs — appropriate for an appliance brand asking customers to spend $300+.

**`button-secondary`** — White fill with a 2px forest-green border and matching green text. Used for secondary purchase paths such as "Compare Models" or "Learn More" placed beside a primary add-to-cart. Identical height (48px) to primary keeps the row visually balanced.

**`button-ghost`** — Transparent fill with a hairline (#e0e0e0) border in ink text. Reserved for tertiary actions like "View All" in section footers or dismissal controls. Lowercase type is acceptable at this level when surrounding context is clear.

**`button-pill`** — Full-radius ({rounded.full}) pill at 40px height, primary green fill. Used in category filter bars and "Shop [Collection]" shortcut strips where a softer shape fits the horizontal scrolling context.

### Navigation

**`nav-bar`** — 64px white header with a bottom hairline. Logo anchors left; product-family mega-nav links in 14px/600 weight occupy the center; cart, search, and account icons sit right. A 36px `nav-bar-promo-strip` in primary green runs above the header on most sessions, surfacing free-shipping thresholds or active promotions in caption-strong white text. The promo strip is the most persistent brand-color expression on every page load.

### Product Card

**`product-card`** — White card with 12px radius and a subtle hairline border. Product image fills a 1:1 aspect-ratio area at top with matching 12px radius; below it: a badge row (sage for "Best Seller," red for "Sale"), product name in title-sm weight, a `rating-chip` with gold stars and review count, then a price row with current price in `price-display` and a struck-through original in `price-was`. A primary-green CTA button appears on hover (desktop) or is always visible (mobile). Ghost "Compare" button sits beside the CTA.

### Hero Banners

**`hero-banner`** — Full-bleed section on a soft gray (#f6f6f6) canvas, minimum 520px tall. Headlines run at 52px/700 with a 2-line maximum; subline copy at body-md below. A primary-green CTA anchors the copy block. Photography occupies the opposing half on desktop, stacking below on mobile. `hero-banner-dark` uses ink (#1a1a1a) as the background for product-launch and technology-showcase moments, providing contrast lift for white product renders.

### Promotional and Feature Strips

**`promo-banner`** — Full-width lavender (#cbc3e3) band reserved for seasonal campaigns, bundle offers, and limited-time pricing. Body-md centered text with an optional inline primary-green button. The lavender distinguishes promotional content from standard product surfaces at a glance — no other component shares this background.

**`feature-strip`** — Sage (#bedccb) background, 50/50 image and text layout, used for technology callouts (HEPA filtration, anti-tangle brush rolls, Flexology joint, DuoClean heads). `feature-strip-white` alternates on white for rhythm. Headline at display-md, body at body-md, optional green text link. Strips alternate sage and white down the page, never sage–sage.

### Trust and Ratings

**`trust-bar`** — Soft-gray (#f6f6f6) horizontal strip sitting between major content sections. Award logos, "50M+ sold" statistics, and media endorsement wordmarks render in muted gray at caption scale. No icons are colored; everything is monochrome to avoid competing with product photography above and below.

**`rating-chip`** — Gold star icons with numeric average and parenthetical review count in caption-strong weight. Appears on product cards, PDP summary rows, and comparison tables. The star-fill color (#f5a623) is the only warm-yellow element in the palette and is used exclusively for this purpose.

### Filters and Category Navigation

**`category-pill`** — Full-radius pill for top-of-collection navigation (Vacuums / Robot Vacuums / Cordless / Pet). Inactive: surface-soft background with hairline border. Active: primary green fill with white text. Scrolls horizontally on mobile in a no-wrap row.

**`filter-pill`** — Smaller full-radius pill for attribute filtering (cordless, HEPA, under $200, self-empty). Inactive: white + hairline. Active: ink fill with on-dark text — a deliberate contrast inversion that signals "currently narrowing results."

### Email Capture and Footer

**`email-capture`** — Ink-background full-width band with centered display-sm headline, body-md subline, a single email text-input, and a primary-green submit button. Appears at the base of collection and campaign pages. The dark background creates a visual chapter-break before the footer.

**`footer`** — Ink background with a 4-column link grid (Products, Support, Company, Social). Column headings in title-sm white; links in body-sm muted gray. A copyright strip below carries legal links. No top border — the ink color runs continuously from `email-capture` through footer, reading as one terminal block.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-height left-slide drawer; category pills scroll horizontally in no-wrap row; filter pills shift to bottom-sheet modal; hero height reduces to 340px with image stacked above copy; promo strip wraps to 2 lines |
| Tablet | 744–1128px | 2-column product grid; nav retains logo + icon cluster + hamburger; feature strips stack image above text block; email-capture shifts to 2-column input+button layout |
| Desktop | 1128–1440px | 3-column product grid; full mega-nav visible; persistent left-sidebar filters on collection pages; hero at 520px min-height with split layout; feature strips restore 50/50 columns |
| Wide | > 1440px | Max-width container 1440px centered with auto side margins; 4-column product grid; hero imagery scales without layout change; section padding increases to keep content from feeling sparse |

### Touch Targets
- All interactive elements minimum 44×44px on mobile
- Filter pills expand to 44px height via increased vertical padding on small screens
- Nav drawer links use 52px row height with full-width tap zone
- Rating chip and badge areas include 8px invisible padding to reach tap target minimums
- Promo strip text links expand tap area via block-level wrapping

### Collapsing Strategy
- Mega-nav collapses to hamburger at 1128px; drawer slides from left with nested accordion for product-family subcategories
- Collection sidebar filters move to a bottom-sheet toggle button below 744px; sheet displays full filter set with apply/reset controls
- Hero layout: image-right on desktop, image-above-copy on mobile (image renders first in DOM for perceived performance)
- Feature strips collapse to single column below 744px — image above, text block below
- Footer 4-column grid → 2-column at tablet → single-column accordion at mobile (headings become tap-to-expand toggles)
- Trust bar logos reflow to a 2-row centered grid at mobile widths

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No font families extracted from the live site — SharkNinja almost certainly loads a licensed or custom typeface via JavaScript; all typography tokens use system sans-serif fallbacks and must be overridden once the brand font is confirmed
- Only 4 hex values recovered; additional semantic colors (warning, error, info states; secondary surface variants; overlay tints; focus rings) are inferred from category conventions rather than extracted directly
- Meta theme-color not set — browser chrome tint behavior on mobile Safari/Chrome is unknown
- Exact button border-radius, hover transition duration, and box-shadow elevation values require JavaScript execution to observe; values here are estimated from visual inspection of comparable appliance DTC sites
- Dark-mode behavior unknown — no `prefers-color-scheme` tokens observed in extraction
- Precise rules for when lavender vs. sage surfaces are applied (promo vs. feature) are inferred from observed page structure patterns, not confirmed component documentation
- Icon glyph style (stroke weight, filled vs. outline, pixel grid size) not captured
- Animation and micro-interaction specifications (card hover lift, drawer easing, add-to-cart feedback) not extractable from static snapshot
