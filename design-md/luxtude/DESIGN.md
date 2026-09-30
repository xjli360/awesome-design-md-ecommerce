---
version: alpha
name: "Luxtude"
source_url: "https://www.luxtude.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Every portable charger on the market is a black rectangle — Luxtude's homepage opens with one too, but shot at an angle that catches an edge gleam like a phone screen waking up, collapsing the distinction between the device being charged and the charger itself. The site runs on a Chinese website-builder platform (hkwezhan.cn) that renders all content client-side via JavaScript, so the canonical palette and font stacks cannot be extracted through static analysis. What surfaces from Amazon product photography and packaging is a brand that gravitates toward a cool teal accent — approximately #00b4c5 — set against matte black product bodies and clean white page canvases. This teal sits in the gap between consumer-electronics cyan and healthcare aqua, warm enough to feel approachable but technical enough to promise wattage. Typography appears to rely on system sans-serif stacks rather than a custom brand face; the brand invests in product photography and specification clarity over typographic personality. Button shapes lean toward soft pills ({rounded.full}) on hero CTAs and gentler radii ({rounded.sm}) on product-card actions, mirroring the rounded-rectangle silhouette of the power banks themselves. Product cards emphasize capacity (mAh), output (W), and physical dimensions in a compact spec strip below the product image — the buyer's decision is technical, not emotional. A secondary palette of status colors — battery-green for full-charge indicators, amber for compatibility warnings — maps directly to the product's LED feedback language. The dark hero sections (#111820) function like the inside of a bag where you'd reach for a charger: the product floats against negative space, lit by its own spec callouts rather than lifestyle context. Footer and support pages surface warranty claims and compatibility matrices, reflecting a brand whose post-purchase relationship is built on specs, not storytelling.

colors:
  primary: "#00b4c5"
  primary-active: "#009dac"
  primary-disabled: "#99dce3"
  ink: "#1a1a1a"
  body: "#4a4a4a"
  muted: "#8c8c8c"
  muted-soft: "#b5b5b5"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  canvas-dark: "#111820"
  surface-soft: "#f5f7f8"
  surface-card: "#ffffff"
  surface-dark: "#1c2630"
  on-primary: "#ffffff"
  on-dark: "#f2f2f2"
  battery-green: "#2ecc71"
  warning-amber: "#f5a623"
  error-red: "#e74c3c"
  star-rating: "#f5a623"
  link-blue: "#2980b9"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.12
    letterSpacing: -0.8px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  spec-value:
    fontFamily: "'SF Mono', SFMono-Regular, Consolas, 'Liberation Mono', Menlo, monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.3px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.27
    letterSpacing: 0
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.31
    letterSpacing: 0
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  mah-display:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px

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
  section: 72px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: 2px solid "{colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-dark-active:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
  button-sm:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 24px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 1px solid "{colors.error-red}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-bar-dark:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} {rounded.none} {rounded.none}"
    aspectRatio: "4 / 3"
    backgroundColor: "{colors.surface-soft}"
  product-card-body:
    padding: 16px
  spec-strip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  spec-strip-value:
    typography: "{typography.spec-value}"
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    padding: 80px 0
  hero-headline:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-dark}"
  hero-subheadline:
    typography: "{typography.body-md}"
    textColor: "{colors.muted-soft}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.full}"
    padding: 16px 40px
    height: 52px
  mah-callout:
    typography: "{typography.mah-display}"
    textColor: "{colors.primary}"
  mah-unit:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.error-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-bestseller:
    backgroundColor: "{colors.warning-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  compatibility-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: 4px 10px
  rating-stars:
    color: "{colors.star-rating}"
    size: 14px
  rating-count:
    typography: "{typography.caption-sm}"
    textColor: "{colors.muted}"
  comparison-table:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: 1px solid "{colors.hairline}"
  comparison-header:
    backgroundColor: "{colors.surface-soft}"
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    padding: 16px
  comparison-cell:
    padding: 12px 16px
    border: 1px solid "{colors.hairline-soft}"
  comparison-highlight:
    backgroundColor: "#e6f7f9"
    border: 2px solid "{colors.primary}"
  footer:
    backgroundColor: "{colors.canvas-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 48px 0
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.primary}"
  footer-heading:
    typography: "{typography.title-md}"
    textColor: "{colors.on-dark}"
  support-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px 24px
    border: 1px solid "{colors.hairline}"
  support-banner-icon:
    color: "{colors.primary}"
    size: 24px

## Components

### Buttons
**`button-primary`** — The principal CTA across the site, used for "Buy Now", "Add to Cart", and hero-section actions. Rendered as a teal (#00b4c5) pill ({rounded.full}) at 48px height with white text in {typography.button-lg}. On hover/active, the fill deepens to #009dac. Disabled state fades to a pale teal (#99dce3). The pill silhouette echoes the rounded-rectangle profile of the power banks themselves.

**`button-secondary`** — An outlined variant for secondary actions like "View Details", "Compare Models", and "Learn More". Transparent fill with a 2px teal border and teal text. On hover, fills solid teal with white text. Same 48px height and pill shape as the primary button.

**`button-dark`** — Used within the dark hero sections and promotional banners. Fills with the dark canvas color (#111820) and uses light text. On hover, lightens to the surface-dark shade. Appears alongside product-on-black photography.

**`button-sm`** — A compact 36px teal pill for inline actions within product cards and spec strips, such as "Quick View" or "Add" shorthand. Uses {typography.button-sm} for a tighter label.

**`button-ghost`** — A text-only button with no fill or border. Used for "Cancel", "Back", and tertiary navigation. On hover, may show a faint background tint.

### Cards
**`product-card`** — The primary commerce unit. A white card with {rounded.md} corners and no outer padding — the product image bleeds to the top edge with rounded top corners. The body area (16px padding) contains the product name, a spec strip showing mAh capacity, wattage, and dimensions, a star rating row, and the price. On hover, the card lifts with a subtle 4px box shadow. No border in default state; the surface-soft background of the grid provides contrast.

**`product-card-image`** — A 4:3 aspect-ratio container with a light gray (#f5f7f8) fallback background. Top corners match the card radius; bottom corners are square where the image meets the body text. Badges (NEW, SALE, BESTSELLER) overlay the top-left corner with 8px offset from both edges.

### Spec Strip
**`spec-strip`** — A compact horizontal bar inside product cards and detail pages that surfaces the three or four most critical specs (e.g., "10000mAh · 20W · 180g · USB-C"). Uses {typography.caption} in muted text on a {surface-soft} background with {rounded.sm} corners. Individual values can be highlighted in {typography.spec-value} monospace to differentiate numeric data from labels.

### mAh Callout
**`mah-callout`** — A large numeric display used in hero sections and product-detail headers to emphasize battery capacity. The number renders in {typography.mah-display} (36px/700) in the primary teal, with a smaller "mAh" unit label in {typography.caption} muted text beneath or beside it. This is the most visually distinctive text element on product pages, functioning like a price tag for capacity.

### Compatibility Tags
**`compatibility-tag`** — Small pill-shaped tags ({rounded.full}) listing device compatibility: "iPhone 15", "Galaxy S24", "iPad Air", etc. Light gray background with {body} text in {typography.caption-sm}. Arranged in a horizontal wrap row below the product description. These tags function as both information and implicit search filters.

### Navigation
**`nav-bar`** — A 60px fixed header in white (light mode) or dark canvas (dark mode, used on landing/hero pages). Contains the Luxtude logo on the left, nav links (Shop, Brand Story, Support, Posts) in the center, and search/cart icons on the right. Nav links use {typography.nav-link} and shift to teal on hover/active. The bar may include a thin 1px {hairline} bottom border on white mode.

### Comparison Table
**`comparison-table`** — A structured table used on product-detail and collection pages to compare 2–4 models side by side. White card with {rounded.md} corners and a 1px {hairline} border. Header row uses a {surface-soft} background with {typography.title-md}. Data cells are separated by {hairline-soft} borders. The "recommended" or "best value" column gets a highlighted treatment: a tinted background (#e6f7f9) and a 2px teal border.

### Badges
**`badge-new`** — Teal background with white uppercase text. Marks recently launched products. **`badge-sale`** — Red (#e74c3c) background for discounted items. **`badge-bestseller`** — Amber (#f5a623) background for top sellers. All badges use {typography.badge} at 11px uppercase with {rounded.xs} corners.

### Rating Stars
**`rating-stars`** — Amber-colored ({star-rating}) star icons at 14px, pulled from Amazon review aggregates. Accompanied by a {rating-count} label showing the review count in {typography.caption-sm} muted text. Appears in product cards and detail page headers.

### Hero Section
**`hero-section`** — A full-width dark (#111820) section with generous 80px vertical padding. Product images float against the dark field, lit to show edge details and LED indicators. The headline uses {typography.display-xl} in white, the subheadline uses {typography.body-md} in muted-soft gray, and the CTA is an oversized teal pill (52px height, 40px horizontal padding). On mobile, padding reduces and the product image stacks above the text.

### Footer
**`footer`** — A dark canvas (#111820) section with the Luxtude logo, column-grouped links (Shop, Support, About, Legal), and social media icons. Link columns use {typography.title-md} headings in white and {typography.link} body links in muted-soft gray that turn teal on hover. A bottom bar contains copyright text and payment-method icons.

### Support Banner
**`support-banner`** — A light-gray card with a teal icon (warranty shield, compatibility checkmark, or shipping truck) on the left and short copy on the right. Used in a horizontal row on product pages to communicate "2-Year Warranty", "30-Day Returns", and "Free Shipping" assurances. Uses {rounded.sm} corners and a 1px {hairline} border.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger; hero headline drops to 28px; spec strips stack vertically; comparison table becomes horizontally scrollable; mAh callout shrinks to 28px; footer columns collapse to accordion |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero headline at 32px; comparison table shows 2 models at a time with swipe; footer in two-column layout |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero headline at 40px; comparison table shows 3–4 models; support banners in horizontal row |
| Wide | > 1440px | Four-column product grid; max-width container at 1400px centered; hero section may span full viewport width with contained text block; larger product card images |

### Touch Targets
- All buttons minimum 44px height on mobile; hero CTA at 52px
- Nav hamburger menu tap area 44px × 44px
- Compatibility tags minimum 32px height with adequate horizontal padding
- Product cards: entire card is tappable, linking to product detail
- Rating stars row: tappable to jump to reviews section
- Quantity selector buttons minimum 40px × 40px

### Collapsing Strategy
- Top nav collapses to hamburger with slide-out drawer below 744px
- Product grid drops from 4 → 3 → 2 → 1 columns across breakpoints
- Hero section stacks: image on top, text below on mobile; side-by-side on desktop
- Comparison tables become horizontally scrollable cards on mobile with a sticky first column for model names
- Spec strips wrap from single-line horizontal to two-line or stacked layout on small screens
- Support banners stack vertically on mobile, horizontal row on desktop
- Footer link columns collapse to expandable accordion sections on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Zero extracted colors**: the luxtude.com site is hosted on a Chinese website-builder platform (hkwezhan.cn) that renders all content client-side via JavaScript; static extraction returned no hex values, font stacks, or CSS custom properties. All color tokens in this file are inferred from Amazon product listing photography, packaging, and general brand positioning. They should be verified against the live rendered site.
- **Zero extracted fonts**: no font-family declarations were captured. The system sans-serif stack used here is a reasonable default but may not match the actual site, which could load custom fonts via JS.
- **Primary color (#00b4c5) is a best-guess teal**: derived from the brand's Amazon presence and product packaging tone. The actual brand teal may differ by several shades. This value should be replaced once live CSS can be inspected.
- **Dark canvas (#111820) is estimated**: the dark hero/footer background color is inferred from product photography style, not measured from the live site.
- **Component dimensions (heights, padding, border-radius)** are standard e-commerce patterns, not extracted values.
- **Hover/active/disabled states** are all inferred from common interaction patterns.
- **Animation and transition timing** not specified — no data available.
- **The site may have distinct mobile vs. desktop navigation patterns** that differ from the hamburger-collapse strategy described here.
- **Product detail page layout** (image gallery, spec table, reviews section) is inferred from Amazon product page patterns and common DTC conventions.
- **Comparison table highlight color (#e6f7f9)** is a computed tint of the primary; actual implementation may differ.
- **The brand may use sub-brands or product-line-specific color systems** (e.g., different accent colors for wireless vs. wired chargers) not captured here.
- **Payment widget colors** (if any third-party checkout is used) are not included and should be excluded from brand palette.
- **Rating star data source**: the brand surfaces Amazon review counts on its own site; the visual treatment of this integration is unknown.
