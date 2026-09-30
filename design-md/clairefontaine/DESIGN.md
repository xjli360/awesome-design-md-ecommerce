---
version: alpha
name: "Clairefontaine"
source_url: "https://www.clairefontaine.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Fountain-pen ink is the calibration instrument — if it bleeds, the paper failed — and Clairefontaine's digital storefront applies that same pass/fail rigor to color: the entire UI runs on a near-white #f6f6f6 field against #232323 text, and only one deliberate chromatic injection is permitted. That accent is #24b9d7, a mid-teal cyan that functions as a single pen stroke across an otherwise monochrome layout, activating primary CTAs, navigation hover underlines, and top-strip announcements without bleeding into the merchandise field. Secondary category accents — #4cbb6c for school supplies, #ff9a52 for art materials, #ff4c4c for promotional pricing — appear at badge scale only, operating as shelf-edge markers rather than brand statements.

  Manrope carries the full typographic hierarchy, a geometric sans whose even optical spacing suits dense product naming without competing with the catalog's SKU depth. Display sizes top out near 36px at weight 700 for hero headlines; body copy runs 16px at 400 weight with a 1.6 line-height that mirrors the reading experience of the physical notebooks. Navigation is a flat 72px white bar with category links that underline in {colors.primary} on hover — no megamenu overlays, no filled dropdown backgrounds. Product cards sit on a #ffffff surface behind a 1px #eeeeee border at {rounded.sm}, presenting each item as a discrete stationery sheet rather than an elevated tile.

  The spacing rhythm is bimodal: hero and section containers breathe at 64px+ vertical padding while grid gutters compress to 16px, maximizing visible inventory density without sacrificing scan legibility — the rhythm of a well-stocked shop floor rather than a lookbook. Corner radii are deliberately restrained; promotional banners and filter chips sit at {rounded.none} or {rounded.xs} to signal precision, while only pill-shaped quantity selectors and toggle controls reach {rounded.full}. The footer reverses to #363a42 with #f6f6f6 type and cyan-tinted links, a dark coda that anchors the otherwise uniformly light layout and gives the nav tree a clear terminus.

colors:
  primary: "#24b9d7"
  primary-active: "#1d93ab"
  primary-hover: "#31b0d5"
  primary-disabled: "#a8dfe9"
  ink: "#232323"
  body: "#414141"
  muted: "#7a7a7a"
  muted-light: "#6c868e"
  hairline: "#eeeeee"
  hairline-soft: "#f5f5f5"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#ffffff"
  surface-alt: "#e5e5e5"
  on-primary: "#ffffff"
  footer-bg: "#363a42"
  accent-green: "#4cbb6c"
  accent-orange: "#ff9a52"
  accent-red: "#ff4c4c"
  alert-success-bg: "#d0e9c6"
  alert-error-bg: "#ebcccc"
  alert-success-text: "#3c763d"
  alert-error-text: "#a94442"
  alert-info-text: "#31708f"

typography:
  display-xl:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-upper:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  button-sm:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0
  badge:
    fontFamily: "'Manrope', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.3px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  md: 8px
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
    hoverBackgroundColor: "{colors.primary-hover}"
    activeBackgroundColor: "{colors.primary-active}"
    disabledBackgroundColor: "{colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
    hoverBackgroundColor: "{colors.surface-soft}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    hoverTextColor: "{colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
    hoverTextColor: "{colors.primary}"
    activeUnderlineColor: "{colors.primary}"
    activeUnderlineHeight: 2px
  product-card:
    backgroundColor: "{colors.surface-card}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "3/4"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.body-md}"
    captionTypography: "{typography.caption}"
    hoverBorderColor: "{colors.primary}"
    hoverShadow: "0 4px 12px rgba(0,0,0,0.07)"
    padding: "{spacing.base}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-xl}"
    sublineTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    paddingVertical: "{spacing.section}"
    ctaVariant: "button-primary"
    imagePosition: right
  announcement-strip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    height: 40px
    textAlign: center
  category-badge:
    rounded: "{rounded.xs}"
    typography: "{typography.badge}"
    padding: 3px 8px
    school:
      backgroundColor: "{colors.accent-green}"
      textColor: "{colors.on-primary}"
    art:
      backgroundColor: "{colors.accent-orange}"
      textColor: "{colors.on-primary}"
    promotion:
      backgroundColor: "{colors.accent-red}"
      textColor: "{colors.on-primary}"
    info:
      backgroundColor: "{colors.primary}"
      textColor: "{colors.on-primary}"
  sale-tag:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    focusBorder: "1px solid {colors.primary}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    height: 44px
    iconColor: "{colors.muted}"
    submitIconColor: "{colors.primary}"
    padding: 0 14px
  breadcrumb:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
    separatorColor: "{colors.muted-light}"
    activeTextColor: "{colors.ink}"
    hoverTextColor: "{colors.primary}"
    gap: "{spacing.xs}"
  product-filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    activeBackgroundColor: "{colors.primary}"
    activeTextColor: "{colors.on-primary}"
    activeBorder: "1px solid {colors.primary}"
  alert-banner:
    rounded: "{rounded.xs}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} {spacing.base}"
    success:
      backgroundColor: "{colors.alert-success-bg}"
      textColor: "{colors.alert-success-text}"
    error:
      backgroundColor: "{colors.alert-error-bg}"
      textColor: "{colors.alert-error-text}"
  footer:
    backgroundColor: "{colors.footer-bg}"
    textColor: "{colors.surface-soft}"
    linkColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.label-upper}"
    headingColor: "{colors.surface-soft}"
    borderTop: "none"
    paddingVertical: "{spacing.xxl}"

## Components

### Buttons

**`button-primary`** — Solid #24b9d7 fill at {rounded.xs} with white text and Manrope 600 at 15px; hover shifts to #31b0d5, active to #1d93ab, and disabled bleaches to #a8dfe9. Height locks at 44px with 12px/24px padding — compact enough for dense product pages without losing touch accessibility. Used exclusively for add-to-cart, checkout progression, and primary search submission.

**`button-secondary`** — White fill with a 1px #24b9d7 border and cyan text; matches the primary's 44px height so the two can sit side-by-side in product and comparison contexts. Hover fills to #f6f6f6 to provide visual feedback without the full primary commitment. Used for wishlist, quick-view, and secondary navigation CTAs.

**`button-ghost`** — Transparent background with #414141 text; hover shifts text to {colors.primary} with no fill change. Used for tertiary actions (clear filters, cancel, view all) where a border would add visual noise to already-dense list views.

### Navigation

**`nav-bar`** — 72px white bar with a 1px #eeeeee bottom border; category links run in Manrope 500 at 15px and underline with a 2px #24b9d7 rule on hover and active states. The logo anchors left; search, language selector, account, and cart iconography cluster right. No background color changes at hover — the underline alone carries the state signal, keeping the nav visually quiet.

### Product Card

**`product-card`** — White surface, 1px #eeeeee border, {rounded.sm} corner, 3:4 image crop for notebook/journal proportions. Title in Manrope 600 at 15px; price in body-md weight 400. On hover the border transitions to #24b9d7 and a soft `box-shadow: 0 4px 12px rgba(0,0,0,0.07)` lifts the card without animation overshoot. Category badges sit over the image top-left using the color-coded badge system. Sale tags occupy top-right in flat #ff4c4c at {rounded.none}.

### Hero Banner

**`hero-banner`** — #f6f6f6 background with text left, product image right in a 55/45 split. Headline in display-xl (36px 700), sub-headline in display-sm (20px 600), with up to two lines of body-md below. CTA maps to button-primary. Section padding is 64px vertical; no rounded corners — the full-width panel reads as a page layer rather than a card.

### Announcement Strip

**`announcement-strip`** — Full-width 40px bar in #24b9d7 with white body-sm text centered. Used for shipping thresholds, sale windows, and new-product callouts. Sits above the nav-bar and collapses to a dismissible drawer on mobile. Never carries more than one message line.

### Category Badges

**`category-badge`** — 11px Manrope 700 text at 0.3px tracking in a {rounded.xs} pill at 3px/8px padding. Four color variants mapped to content taxonomy: school (#4cbb6c), art (#ff9a52), promotion (#ff4c4c), and informational (#24b9d7). Badges appear on product cards, category landing banners, and editorial highlight strips.

### Search Bar

**`search-bar`** — Full-width 44px input at {rounded.xs} with a 1px #eeeeee border that transitions to 1px #24b9d7 on focus. Magnifier icon in #7a7a7a at left; submit arrow in #24b9d7 at right. Placeholder text in #7a7a7a Manrope 400. On desktop, search expands inline in the nav-bar slot; on mobile it opens as a full-screen overlay.

### Breadcrumb

**`breadcrumb`** — Caption-scale (12px 400) with #7a7a7a for ancestor nodes and #232323 for the current page. Separator uses a #6c868e slash or chevron glyph. Ancestor links turn #24b9d7 on hover. Appears below the nav-bar on category and PDP pages; absent on the homepage.

### Filter Chips

**`product-filter-chip`** — White background, 1px #eeeeee border, {rounded.xs}, Manrope 600 at 13px. Active state flips to #24b9d7 fill with white text and matching border — the same color logic as the primary button but at pill-label scale. Chips display horizontally in a scrollable row on mobile, wrapping grid on tablet+.

### Alert Banners

**`alert-banner`** — Form feedback and cart validation messages in a soft tinted field: success uses #d0e9c6 background with #3c763d text; error uses #ebcccc with #a94442. Body-sm Manrope 400, {rounded.xs}, 8px/16px padding. These colors match the Bootstrap alert palette present in the extracted tokens, confirming a framework-integrated alert system.

### Footer

**`footer`** — #363a42 background reversal with #f6f6f6 body text and #24b9d7 links. Column headings in label-upper (11px 700 uppercase, 0.8px tracking) in #f6f6f6. Four to five link columns cover product categories, customer service, corporate info, and social. Bottom strip carries copyright in caption scale and repeats the language/country selector from the nav. No top border — the color break is the boundary.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger drawer with full-height slide-in; search becomes full-screen overlay; product grid shifts to 2-column; hero stacks to image-above/text-below; announcement strip stays full-width but truncates to single line |
| Tablet | 744–1128px | Nav shows logo + search + icons, category links move into a secondary horizontal scroll row below; product grid is 3-column; hero maintains side-by-side split at 60/40; filter chips scroll horizontally |
| Desktop | 1128–1440px | Full 5-link nav-bar at 72px; 4-column product grid; hero at full 55/45 split with 64px section padding; footer expands to 5 columns |
| Wide | > 1440px | Max content width caps at 1440px centered; hero image scales up proportionally; product grid stays 4-column but card padding increases; footer columns gain breathing room |

### Touch Targets

- All interactive elements (buttons, nav links, filter chips, badge links) maintain a minimum 44px height or tap area
- Product card hit area covers the full card surface, not only the image or title
- Mobile drawer nav items are 48px tall rows with full-width tap zones
- Filter chip rows on mobile have 8px gap minimum between chips to prevent mis-taps

### Collapsing Strategy

- Top nav collapses at 744px; category taxonomy moves into a labeled section inside the hamburger drawer, maintaining hierarchy without a megamenu
- The announcement strip remains visible on all breakpoints but truncates to a single-line marquee if content overflows at 375px
- Breadcrumb hides on mobile to recover header vertical real estate; replaced by a single back-arrow link
- Footer column layout collapses from 5 → 2 columns at tablet, stacks to 1 column with accordions at mobile
- Hero image drops below copy on mobile; image height clamps to 280px to avoid excessive scroll commitment before the CTA

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No brand-specified typeface weight confirmed — Manrope is present in the extracted font stack but no custom variable-font axis ranges or licensed subset boundaries could be verified
- The exact primary color role of #24b9d7 vs. #5bc0de vs. #1d93ab is ambiguous from extraction alone; multiple cyan variants appear and may represent different component states or a Bootstrap info-color layer rather than distinct brand tokens
- No dark mode tokens detected; the site appears light-only but the presence of #363a42 in the extracted palette suggests a dark-footer pattern that may or may not extend to other surfaces
- Icon system could not be identified — Material Icons is present in the font stack, suggesting a Material icon library, but no icon sizing or stroke-weight spec was available
- Animation and transition timing values were not extractable; hover and active state durations are estimated at 150–200ms based on category norms
- Product image aspect ratio (used 3:4) is inferred from stationery catalog convention and not confirmed from live grid sampling
- No typography scale for non-Latin scripts confirmed; Clairefontaine distributes internationally and may use different font stacks for FR/DE/ES locales
