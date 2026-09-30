---
version: alpha
name: "Euclid Records"
source_url: "https://www.euclidrecords.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep, saturated #163959 — the blue of a midnight highway or a vintage sleeve — sets the foundational mood for Euclid Records, an independent store that treats the physical artifact of music with the gravity of a museum. This dark ink anchors a palette that is otherwise surprisingly bright and varied: a traffic-cone orange (#f68b1f) and a fire-engine red (#bd2426) serve as energetic accents, while a soft, almost dusty green (#bada7a) and a warm, buttery amber (#f9b169) suggest the patina of well-loved cardboard and faded liner notes. The site’s canvas is a clean, slightly warm off-white (#ebebeb), a deliberate departure from pure white that softens the reading experience. Typography defaults to system sans-serif — `-apple-system`, `Arial`, `Helvetica Neue` — a pragmatic, no-nonsense choice that lets the product photography and color do the heavy lifting. Buttons are pill-shaped (`{rounded.full}`) in the primary blue, with secondary actions rendered in the bright orange, creating a clear visual hierarchy that feels both playful and urgent. The overall impression is of a space that is deeply knowledgeable and unpretentious, where a rare pressing sits alongside a new release, and the design’s job is to get out of the way and let the music speak. The extracted palette, while wide, suggests a brand that is comfortable with a high degree of chromatic contrast, using saturated primaries as wayfinding signals against the dark, quiet backdrop.

colors:
  primary: "#163959"
  primary-active: "#0f2740"
  primary-disabled: "#8a9bb0"
  ink: "#272727"
  body: "#404040"
  muted: "#595959"
  muted-soft: "#737373"
  hairline: "#bfbfbf"
  hairline-soft: "#dedede"
  canvas: "#ebebeb"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-orange: "#f68b1f"
  accent-orange-active: "#ee730a"
  accent-red: "#bd2426"
  accent-red-active: "#de5052"
  accent-green: "#bada7a"
  accent-green-soft: "#9bca3e"
  badge-new: "#62a1d8"
  badge-sale: "#de5052"
  star-rating: "#f68b1f"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.3px
    textTransform: uppercase

rounded:
  none: 0px
  xs: 4px
  sm: 8px
  md: 12px
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
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.accent-orange-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
  button-pill-accent:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: 1px solid "{colors.hairline}"
  text-input-focus:
    border: 2px solid "{colors.primary}"
  text-input-error:
    border: 2px solid "{colors.accent-red}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    padding: 0 {spacing.lg}
  nav-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    padding: 8px 16px
    rounded: "{rounded.sm}"
  nav-link-active:
    backgroundColor: rgba(255, 255, 255, 0.15)
    textColor: "{colors.on-primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
    marginTop: "{spacing.sm}"
  product-card-artist:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
    fontWeight: 600
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: 1px solid "{colors.hairline}"
  search-bar-focus:
    border: 2px solid "{colors.primary}"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.on-primary}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: rgba(255, 255, 255, 0.8)
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: 6px 16px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered in the deep blue `{colors.primary}` with white text and a pill shape (`{rounded.full}`). On hover, it shifts to `{colors.primary-active}`. The disabled state uses `{colors.primary-disabled}`. Used for "Add to Cart," "Checkout," and primary navigation actions.

**`button-secondary`** — A high-energy alternative CTA in `{colors.accent-orange}`, used for "Shop Now," "Browse," or secondary purchase flows. Hover state darkens to `{colors.accent-orange-active}`. Same pill shape and height as the primary button to maintain rhythm.

**`button-tertiary`** — A ghost button with a transparent background and `{colors.primary}` text, used for "Learn More" or "View Details" links within cards. Has a subtle border on hover.

**`button-pill-accent`** — A smaller, compact pill in `{colors.accent-red}`, used for urgent signals like "Sale" or "Limited Edition" CTAs. Uses `{typography.button-sm}` and a reduced height of 36px.

### Navigation
**`nav-bar`** — A fixed top bar with a `{colors.primary}` background and white text. Contains the store logo, nav links, and a search icon. Height is 56px. The bar is always present on desktop and tablet.

**`nav-link`** — Uppercase, 14px, weight 600. Links are white on the dark nav background. Active or hover states get a semi-transparent white background (`rgba(255, 255, 255, 0.15)`) with `{rounded.sm}`.

### Cards
**`product-card`** — A white card (`{colors.surface-card}`) with `{rounded.md}` and 16px padding. Contains a product image (with `{rounded.sm}`), the album title in `{typography.title-md}`, the artist name in `{colors.muted}`, and the price in bold `{typography.body-md}`. Cards sit on the `{colors.canvas}` background.

**`badge-new`** and **`badge-sale`** — Small, uppercase, 11px badges that sit at the top-left of product images. "New" uses `{colors.badge-new}` (a blue), "Sale" uses `{colors.accent-red}`. Both have `{rounded.xs}` and 2px/8px padding.

### Forms & Search
**`text-input`** — A standard input field with a white background, `{colors.body}` text, and a `{colors.hairline}` border. On focus, the border thickens to 2px and turns `{colors.primary}`. Error state uses a 2px `{colors.accent-red}` border.

**`search-bar`** — A pill-shaped search field (`{rounded.full}`) with a white background and `{colors.hairline}` border. Used for searching the catalog. On focus, the border becomes 2px `{colors.primary}`.

### Footer
**`footer`** — A full-width footer in `{colors.primary}` with white text. Contains links, social icons, and store information. Links use `{typography.link}` and are white. Padding is `{spacing.xxl}` top/bottom.

### Hero & Sections
**`hero-section`** — A full-width hero banner with `{colors.primary}` background and white text. Contains a large heading (`{typography.display-xl}`) and a subheading in semi-transparent white. Used for featured releases or promotions.

**`section-heading`** — A 24px, weight 600 heading in `{colors.ink}` with `{spacing.lg}` bottom margin. Used to label product categories or content sections.

**`category-tag`** — A pill-shaped filter tag in `{colors.surface-soft}` with `{colors.body}` text. Active state flips to `{colors.primary}` background with white text. Used for genre or format filtering.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (2 columns). Nav bar collapses to hamburger menu. Hero section reduces padding to `{spacing.xl}`. Search bar moves below nav. Category tags wrap to two rows. Footer stacks links vertically. |
| Tablet | 744–1128px | Two-column product grid (3 columns). Nav links remain visible but reduced font size. Hero section uses `{spacing.xxl}` padding. Search bar is inline in nav. Category tags are a single scrollable row. |
| Desktop | 1128–1440px | Three-column product grid (4 columns). Full nav with all links. Hero section uses `{spacing.section}` padding. Search bar is prominent in nav. Category tags are a full-width row. |
| Wide | > 1440px | Four-column product grid (5 columns). Max-width container (1440px) centered. Hero section has larger typography (display-xl at 36px). Additional whitespace around cards. |

### Touch Targets
- All buttons and interactive elements are at least 44px tall (primary, secondary, search bar).
- Nav links have a minimum tap target of 44px x 44px.
- Category tags are at least 36px tall.
- Product cards have a minimum tap target of 80px x 80px for the image area.

### Collapsing Strategy
- On mobile, the top nav collapses into a hamburger menu. The menu overlay uses `{colors.primary}` background.
- The product grid collapses from 4-5 columns on wide screens to 2 columns on mobile.
- The search bar collapses from a full inline element on desktop to a toggleable icon on mobile.
- Category tags collapse from a full-width row to a horizontally scrollable strip on tablet and mobile.
- The footer collapses from a multi-column layout to a single stacked column on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted font stack is entirely system fonts (`-apple-system`, `Arial`, `Helvetica Neue`, etc.). The brand may use a custom web font (e.g., a music-industry-specific typeface) that was not detected in the extraction. If a custom font is used, the `fontFamily` values in typography should be updated.
- The extracted color palette is unusually large (22+ colors) and includes many generic web colors (multiple blues, grays, and a green). The true brand palette may be more focused. The primary (`#163959`) and accent orange (`#f68b1f`) were chosen as the most distinctive and likely brand colors, but this is an inference.
- Hover and active states for most components (except buttons and inputs) are not defined. These should be added based on interaction design patterns.
- Error styling for forms is assumed (red border) but not confirmed from the live site.
- The brand may have a specific icon set or illustration style that was not captured.
- Dark mode is not supported and was not detected.
- The `meta theme-color` was not set, so browser chrome styling is undefined.
- The brand may use a specific grid system or layout constraints (e.g., max-width, column gaps) that were not extracted.
- Loading states, skeleton screens, and animation timing are not defined.
