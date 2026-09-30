---
version: alpha
name: "Super7"
source_url: "https://super7.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Near-pitch-dark hero banners at #121212 make Super7's product photography — ReAction figures, Ultimates, SUPERSIZE vinyl — read like objects in a display case with a single overhead spotlight. The white canvas (#ffffff) that hosts the product grid exists as a deliberate relief valve: the eye cycles from dark immersion to bright showcase to dark footer, paced by a recurring orange (#fa7224) that fires at every primary CTA and price callout with the oxidized-plastic warmth of 1980s blister-pack printing. That orange is the system's only unambiguous decision — everything else is a graduated stack of near-blacks (#121212, #1a1a1a) and near-whites (#f0f0f0, #e1e3e4, #dedede), a palette that reads less like a brand guide and more like a collector's backlit display case. Sage green (#aaccaa) arrives as a soft counterpoint, surfacing in select section moments — likely a product-line differentiator or seasonal colorway — and keeping the triad from flattening into pure noir-orange. Inter runs the entire type system; Super7 substitutes weight contrast for a custom display face, running 800 at headline scale inside dark hero banners and stepping to 400 for body copy on the product grid. Buttons use `{rounded.sm}` throughout — not pill-shaped, not hard-cornered; the brand reads as collector-catalog UI rather than a consumer app. Product cards carry dense information — price, variant count, edition flags — in a tight grid that treats each figure as a showcase object rather than a commodity SKU. The hairline system uses #dedede and #e1e3e4 for light-mode dividers, while dark sections rely on the gradient between #121212 and #1a1a1a surfaces for depth rather than explicit stroke lines; the darkness itself is the container.

colors:
  primary: "#fa7224"
  primary-active: "#d95e10"
  primary-disabled: "#fcc49b"
  ink: "#121212"
  body: "#3a3a3a"
  muted: "#787878"
  hairline: "#dedede"
  hairline-soft: "#e1e3e4"
  canvas: "#ffffff"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  surface-dark: "#1a1a1a"
  near-black: "#121212"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  sage: "#aaccaa"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "Inter, sans-serif"
    fontSize: 52px
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: -1px
  display-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.25px
  title-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  price-display:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  body-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  overline:
    fontFamily: "Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.08em
    textTransform: uppercase
  badge-label:
    fontFamily: "Inter, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.06em
    textTransform: uppercase
  button-md:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.04em
    textTransform: uppercase
  button-sm:
    fontFamily: "Inter, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.04em
    textTransform: uppercase
  nav-link:
    fontFamily: "Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link-mobile:
    fontFamily: "Inter, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.25
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
    padding: 12px 24px
    height: 44px
  button-primary-hover:
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
    padding: 11px 23px
    height: 44px
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.on-dark}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "1px solid {colors.hairline}"
    height: 64px
  nav-bar-dark:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-display}"
    captionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1 / 1"
    padding: 8px
  hero-banner:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 520px
    paddingX: 48px
    paddingY: 80px
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 420px
    paddingX: 48px
    paddingY: 64px
  sale-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  edition-badge:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  sage-badge:
    backgroundColor: "{colors.sage}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 6px
  category-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.overline}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  category-tag-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.full}"
    padding: 6px 14px
  product-grid:
    columns: 4
    gap: 16px
    paddingX: 32px
  collection-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    accentColor: "{colors.primary}"
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.md}"
    padding: 48px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    paddingX: 16px
  footer:
    backgroundColor: "{colors.near-black}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.muted}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    paddingY: 48px

## Components

### Buttons
**`button-primary`** — Orange (#fa7224) fill with white uppercase Inter 700 text at 14px, 4% letter-spacing. 44px height with 8px radius; hover shifts to `{colors.primary-active}` (#d95e10) and disabled washes to `{colors.primary-disabled}`. This is the dominant CTA across add-to-cart, checkout, and newsletter signup flows.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border, matching primary dimensions exactly for inline pairing. Used for wishlist, "learn more," and non-purchase actions where the orange would oversaturate.

**`button-ghost-dark`** — Transparent fill with 1px white border and white uppercase text for placement over `{colors.near-black}` hero and collection banners. Same 44px height and `{rounded.sm}` radius as the primary/secondary pair.

### Product Card
**`product-card`** — White card with 8px radius and a square 1:1 image crop. Title renders in `{typography.title-sm}` (Inter 600 16px) and price in `{typography.price-display}` (Inter 700 18px). Edition and sale badges overlay the image corner in absolute position. Variant count appears in `{typography.caption}` below the price. Hover typically scales the image slightly; no card shadow required given white-on-white grid context.

### Hero Banner
**`hero-banner`** — Full-bleed near-black (#121212) sections with headline at `{typography.display-xl}` (Inter 800 52px) in white and subtext in `{typography.body-md}`. An orange `button-primary` sits below subtext. Minimum 520px height; content is max-width constrained and vertically centered. **`hero-banner-light`** flips to `{colors.surface-soft}` (#f0f0f0) canvas for secondary feature callouts; ink text replaces white.

### Badges
**`sale-badge`** — Compact #fa7224 label in 10px uppercase Inter 700 with 4px radius, absolute-positioned over product card image top-left. **`edition-badge`** — Near-black (#121212) variant for "Limited Edition" or "Exclusive" flags on the same image overlay layer. **`sage-badge`** — Sage green (#aaccaa) with ink text for product-line or thematic callouts where orange would conflict with the palette tone.

### Navigation
**`nav-bar`** — White background, 64px height, 1px `{colors.hairline}` bottom border. All category links at `{typography.nav-link}` (Inter 600 14px). An orange `button-primary` or cart icon anchors the right side. **`nav-bar-dark`** — Same structure but near-black (#121212) background with white links; used atop hero-banner sections or as a global dark-theme override.

### Category Tags
**`category-tag`** — Pill-shaped filter chips in `{colors.surface-soft}` with 11px uppercase overline text in `{colors.body}`. Active state flips to `{colors.primary}` fill with white text, maintaining `{rounded.full}`. Used for product line filters (ReAction, Ultimates, SUPERSIZE, Apparel).

### Collection Banner
**`collection-banner`** — Dark (#1a1a1a) inset banner with orange accent used as a decorative element or subheading tint. Headline in `{typography.display-md}` (Inter 700 36px) white, body in `{typography.body-md}`. 12px radius and 48px internal padding. Sits mid-page to introduce major product line sections.

### Search Bar
**`search-bar`** — Soft gray (#f0f0f0) rectangle at 40px height with 8px radius. Muted placeholder text; no border in default state; focus applies a 1px `{colors.ink}` outline. Expands to full width on mobile. Icon-left layout with a magnifying glass glyph in `{colors.muted}`.

### Footer
**`footer`** — Near-black (#121212) full-bleed footer. Link columns use `{typography.title-sm}` for section headings and `{typography.body-sm}` for links. Muted gray (#787878) for secondary and legal copy. Social icon row at the base; logo lockup centered or left-aligned above the link grid.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger nav with full-screen drawer in `{colors.near-black}`; hero headline downsizes from `{typography.display-xl}` to `{typography.display-sm}`; buttons expand to full-width inside card footers; category tags shift to horizontal scroll strip |
| Tablet | 744–1128px | 2-column product grid; nav collapses secondary category links into a "More" dropdown; hero minHeight reduces to 380px; collection banners stack headline and body vertically |
| Desktop | 1128–1440px | 4-column product grid; full horizontal nav with all categories visible; hero banners run edge-to-edge with constrained inner content |
| Wide | > 1440px | Content max-width 1440px centered; product grid may expand to 5 columns; hero backgrounds bleed edge-to-edge while text content stays within the max-width rail |

### Touch Targets
- All buttons minimum 44px height
- Category tag pills minimum 36px touch height on mobile
- Product card tap target covers full card surface including image
- Nav icons (cart, search, hamburger) minimum 44×44px hit area
- Badge overlays on product cards do not need separate tap targets

### Collapsing Strategy
- Primary nav collapses into hamburger at < 1024px; drawer slides from left over a `{colors.scrim}` overlay
- Category filter bar converts from inline pill row to horizontal scroll strip at mobile breakpoint; no wrapping
- Footer four-column grid collapses to two columns at tablet, single accordion-style column at mobile
- Product grid gutters reduce from 16px to 8px on mobile to maximize image display area
- Hero CTA buttons stack below headline+body block and go full-width at mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only Inter identified in the font stack; Super7 may use additional custom or licensed display faces for logo wordmark and branded section headers — not surfaced by extraction
- Sage green (#aaccaa) role is ambiguous: cannot confirm whether it is a persistent brand secondary color, a specific product-line differentiator (e.g., a particular IP collaboration), or a seasonal accent
- Primary-active (#d95e10) and primary-disabled (#fcc49b) values are interpolated from extracted #fa7224 — not directly observed via color sampling
- Muted gray (#787878) is inferred for mid-hierarchy text; no exact mid-gray was present in the extracted palette
- No motion or transition tokens captured — hover effects, add-to-cart micro-interactions, and drawer animations are likely present but not observable from static extraction
- Product card hover states (image scale ratio, shadow appearance) not directly extractable
- Icon set style and any custom illustration or character-art assets used in section decoration are not captured
- Exact nav height and any sticky/scroll-transform behavior could not be confirmed from static extraction
