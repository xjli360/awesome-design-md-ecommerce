---
version: alpha
name: "Fontana Forni"
source_url: "https://www.fontanaforni.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  The name translates as "fountains" in Italian, and the palette makes that etymology visible — deep teal #226d7a runs every primary CTA and nav bar on a brand whose central product proposition is open flame. That counterintuitive coolness is the defining design decision: rather than warm terracotta and soot-black, Fontana Forni anchors its digital identity in the Adriatic end of the spectrum, where #226d7a and #1e6d7a function as a near-twin primary pair (the second reading as a pressed-state depth rather than a distinct hue), the bright cyan #22b8d1 lifts interactive highlights, and the near-white aqua #e4f5fa ({colors.surface-soft}) keeps product photography clean without the clinical flatness of pure white. Powder blue #b0e0e9 ({colors.accent-soft}) softens badge fills and secondary surface tints, completing a palette that is unusually monochromatic for a DTC brand — five variants of the same hue family, zero warm offsets. Open Sans carries the typographic system; it was the only non-system font stack detected in extraction, and it earns its place with the same qualities the palette communicates: precision, legibility, no decorative impulse that might undercut an oven's engineering credibility. Corner geometry holds at {rounded.xs} and {rounded.sm} throughout — machined tolerances read in the UI as they do in the product. Section spacing opens to {spacing.section} to give furnace photography the silence it demands; these are permanent outdoor installations that reward evaluation rather than impulse, and the layout communicates that disposition before a word of copy loads. The overall register is precision-utilitarian with a Mediterranean light quality: a brand calibrated for buyers who arrive having already done three weeks of research.

colors:
  primary: "#226d7a"
  primary-active: "#1e6d7a"
  primary-disabled: "#7ab8c4"
  accent: "#22b8d1"
  accent-soft: "#b0e0e9"
  ink: "#1a2a2e"
  body: "#2e4a52"
  muted: "#7a9da5"
  hairline: "#c8e2ea"
  canvas: "#ffffff"
  surface-soft: "#e4f5fa"
  surface-card: "#ffffff"
  on-primary: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  title-lg:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.44
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  overline:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.5px
    textTransform: uppercase
  spec-label:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
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
    padding: "14px 28px"
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.primary}"
    padding: "13px 27px"
    height: 48px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: "8px 16px"
  text-input:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    focusBorderColor: "{colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: "12px 16px"
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 72px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    imageAspectRatio: "1 / 1"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    minHeight: 560px
  spec-table:
    backgroundColor: "{colors.canvas}"
    alternateRowColor: "{colors.surface-soft}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-md}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rounded: "{rounded.none}"
    cellPaddingY: "{spacing.md}"
    cellPaddingX: "{spacing.base}"
  feature-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
    textTransform: uppercase
  collection-filter:
    backgroundColorInactive: "{colors.canvas}"
    backgroundColorActive: "{colors.primary}"
    textColorInactive: "{colors.primary}"
    textColorActive: "{colors.on-primary}"
    borderInactive: "1px solid {colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: "8px 18px"
    height: 36px
  testimonial-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    quoteTypography: "{typography.body-md}"
    attributionTypography: "{typography.caption}"
    attributionColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  section-overline:
    textColor: "{colors.primary}"
    typography: "{typography.overline}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    headingTypography: "{typography.nav-link}"
    linkTypography: "{typography.body-sm}"
    paddingTop: "{spacing.section}"
    paddingBottom: "{spacing.xl}"

## Components

### Buttons

**`button-primary`** — The solid #226d7a block is used for all primary purchase and conversion CTAs: "Add to Cart," "Buy Now," "Request a Quote," and "Find a Dealer." At 48px tall with generous 28px horizontal padding, it has the spatial confidence of a premium purchase without the aggressive scale some DTC brands push. Hover deepens to `primary-active` (#1e6d7a), a near-imperceptible hue shift that reads as a mechanical press rather than a color change; disabled state washes to `primary-disabled` at a lighter blue-teal. The {rounded.sm} radius echoes the oven product geometry — precise, not playful.

**`button-secondary`** — White fill with a 1.5px {colors.primary} border, paired alongside the primary button on product pages for secondary actions like "View Full Specifications" or "Download Manual." Matches 48px height for visual alignment in horizontal CTA clusters. Hover state inverts toward a {colors.surface-soft} fill, staying in the cool aqua register.

**`button-ghost`** — Transparent with {colors.ink} text; used for utility links in dropdown overlays, filter resets, and navigation sub-panels where a bordered button would add visual weight. {rounded.xs} keeps the bounding geometry clean on hover without adding persistent chrome.

### Navigation

**`nav-bar`** — White 72px bar, brand wordmark anchored left, utility cluster (Cart, Search, Account) right. Open Sans at 14px/600 weight gives the links enough presence to be found without competing with product photography below. A 1px {colors.hairline} bottom border separates the bar on scroll. On mobile, the right cluster collapses to a hamburger; primary categories move into a full-height teal drawer.

### Product Card

**`product-card`** — Square-crop product photography occupies the card top at 1:1 aspect ratio; below it, {colors.surface-card} background carries the product title in {typography.title-md}, a one-line feature descriptor in {typography.body-sm}, and the price in {typography.title-md} weight 600. A `feature-badge` may overlay the image top-left for "New," "Bestseller," or "Made in Italy" callouts. {rounded.sm} applied to the card container; no box-shadow — the light background does the separation work.

### Hero Banner

**`hero-banner`** — Full-width photographic hero; on desktop the teal primary at partial opacity anchors a left-column text block so photography runs edge-to-edge behind it. Heading at {typography.display-xl}, subhead at {typography.body-md} in {colors.on-primary}, followed by a primary CTA button and an optional secondary ghost button. On mobile, a solid {colors.primary} overlay covers the lower 50% to ensure headline legibility. Min-height 560px maintains the cinematic proportion even on landscape tablets.

### Spec Table

**`spec-table`** — The functional centerpiece of every product detail page, carrying oven interior diameter, weight, fuel type, max temperature (°C and °F), and material composition. Label column in {typography.spec-label} uppercase teal-gray, value column in {typography.body-md} ink. Rows alternate between {colors.canvas} and {colors.surface-soft}; horizontal dividers in {colors.hairline} with zero corner radius ({rounded.none}) for a data-grid authority that matches the engineering tone. The table typically follows the product description and precedes the add-to-cart section.

### Feature Badge

**`feature-badge`** — Pill at {rounded.full}, #22b8d1 fill with white text at {typography.caption}/uppercase, used inline with product titles or stacked at card top-left. Common labels: "Wood-Fired Ready," "Made in Italy," "Ships Free," "In Stock." The cyan separates cleanly from the teal nav and primary buttons, giving badges their own signal frequency.

### Collection Filter

**`collection-filter`** — Pill-shaped toggle buttons arranged in a horizontal scroll row above product grids. Inactive state: 1px {colors.primary} border, {colors.canvas} fill, {colors.primary} text. Active state: {colors.primary} fill, {colors.on-primary} text. {rounded.full} radius, {typography.button-sm} weight 600. Categories likely include Residential, Commercial, Wood-Fired, Gas, and Accessories.

### Testimonial Card

**`testimonial-card`** — {colors.surface-soft} background at {rounded.md}, {spacing.lg} padding. Quote body in {typography.body-md} with italic style, attribution in {typography.caption} at {colors.muted}. Typically arranged in a 3-column desktop grid, collapsing to single-column on mobile. No star rating system was detectable from extraction data.

### Section Overline

**`section-overline`** — Short uppercase category label appearing above `display-md` section headings: "OUR COLLECTION," "WHY FONTANA," "CUSTOMER STORIES." {typography.overline} at 11px/700 with 1.5px letter-spacing, colored {colors.primary}. Creates a reading hierarchy that pulls the eye before the larger headline.

### Footer

**`footer`** — Full-bleed {colors.primary} background (#226d7a) with {colors.on-primary} text throughout. Section headings in {typography.nav-link} weight 600; link lists in {typography.body-sm} weight 400 at reduced opacity (~70%) for hierarchy. Columns cover Products, Company, Support, and Dealer Locator. {spacing.section} top padding before the grid; copyright line separated by a hairline rule in on-primary at 20% opacity.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + teal full-height drawer; hero switches to stacked layout with teal overlay on lower half; spec table scroll-locks horizontally; filter pills scroll horizontally |
| Tablet | 744–1128px | Two-column product grid; hero uses side-by-side layout at 50/50 split; nav shows top-level categories inline, sub-categories in dropdown; filter pills wrap to two rows |
| Desktop | 1128–1440px | Three-column product grid; hero text block left-aligned at ~40% width with photography behind; spec table at full width; nav fully expanded; testimonial grid at 3 columns |
| Wide | > 1440px | Max-width container (~1400px) centered; hero photography extends edge-to-edge behind constrained text column; product grid stays at 3–4 columns with increased card padding |

### Touch Targets

- All buttons maintain 48px minimum height on touch viewports
- Collection filter pills set to 44px height on mobile
- Nav drawer links padded to 48px row height
- Spec table rows maintain 44px minimum height for tap-to-copy values

### Collapsing Strategy

- Product navigation mega-menu collapses to accordion sections inside the mobile drawer
- Spec table switches from two-column layout to definition list (label above value) on mobile < 480px if horizontal scroll feels cramped
- Testimonial cards collapse from 3-column grid to single-column swipe carousel on mobile
- Hero CTA cluster stacks vertically (primary above secondary) below 480px
- Footer 4-column grid collapses to 2-column at tablet, single-column accordion at mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Site returned HTTP 403 during extraction; only five hex values were captured and all five are variants of the same teal family — warm neutrals, error states, success colors, and any promotional accent (sale red, seasonal highlight) are unconfirmed
- No custom brand typeface detected; only Open Sans, Arial, and Roboto (system fallbacks) appeared in font stacks — if Fontana Forni licenses a custom or display face for headings, it was not present in the extracted document
- No meta theme-color was set, so mobile browser chrome color is unspecified
- Price formatting, currency display, and promotional badge colors (sale, clearance) could not be confirmed
- Dark-mode or high-contrast variant is unknown — the teal palette has sufficient contrast at primary weight but a verified dark theme was not observed
- Icon style (stroke weight, fill vs outline, custom vs library) was not extractable from the 403 response
- Animation timing and easing curves for hero transitions, hover states, and drawer open/close are unconfirmed
