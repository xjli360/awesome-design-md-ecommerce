---
version: alpha
name: "Book of the Month"
source_url: "https://www.bookofthemonth.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A subscription service built on the anticipation of a fresh hardcover arriving each month, Book of the Month uses a restrained palette anchored on a single dark ink (#313131) that does the work of both headline and body text, creating a reading-room seriousness that lets the book covers — the real product photography — supply all the color. The site trusts a clean white canvas and generous whitespace over decorative backgrounds, with soft rounded corners on selection cards ({rounded.md}) that mimic the gentle curve of a paperback spine. Navigation is minimal and utilitarian: a persistent top bar with the brand wordmark, a search field, and account links, all set in the system font stack (San Francisco, Roboto, Noto Sans) at modest weights — the brand refuses to compete with the typography of the books it sells. The primary action, whether "Add to Box" or "Subscribe Now," appears as a solid dark rectangle with white text, a deliberate visual weight that says "this is the decision." Star ratings and review counts sit in compact badges, and the monthly selection grid uses a three-column layout that feels like browsing a bookstore table. There are no hard edges on interactive elements — buttons, input fields, and cards all share a consistent 8px rounding ({rounded.sm}) that softens the otherwise stark black-and-white scheme. The overall effect is that of a well-edited shelf: the brand steps back and lets the books speak.

colors:
  primary: "#313131"
  primary-active: "#1a1a1a"
  primary-disabled: "#a0a0a0"
  ink: "#313131"
  body: "#4a4a4a"
  muted: "#757575"
  muted-soft: "#9e9e9e"
  hairline: "#e0e0e0"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  star-rating: "#313131"
  badge-new: "#313131"
  badge-sale: "#d32f2f"
  link: "#313131"
  link-hover: "#1a1a1a"

typography:
  display-xl:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0.2px
  badge:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary-active}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-sale}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
    aspectRatio: "2/3"
  product-card-info:
    padding: "{spacing.md} {spacing.base}"
  product-card-title:
    typography: "{typography.title-sm}"
    marginBottom: "{spacing.xs}"
  product-card-author:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    marginBottom: "{spacing.sm}"
  product-card-rating:
    typography: "{typography.caption}"
    textColor: "{colors.muted}"
  badge:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "8px 14px"
    height: 40px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.ink}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.base}"
  hero-subheading:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
    marginBottom: "{spacing.lg}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Box," "Subscribe Now," and checkout confirmation. A solid dark rectangle ({colors.primary}) with white text, 8px rounding ({rounded.sm}), and 44px height. On hover, the background deepens to {colors.primary-active}. The disabled state uses {colors.primary-disabled} with white text at reduced opacity.

**`button-secondary`** — An outlined alternative for secondary actions like "Learn More" or "View Details." White background with a 2px solid border in {colors.primary}, matching the primary button's typography and height. Active state shifts the border to {colors.primary-active} and adds a light fill from {colors.surface-soft}.

**`button-text`** — A text-only button for inline actions such as "Cancel" or "Skip This Month." Transparent background with {colors.primary} text, using the same button-md typography. Hover state adds a subtle underline.

### Cards
**`product-card`** — The core browsing unit for monthly selections. A white card with 12px rounding ({rounded.md}) and no padding at the card level — the image fills the top with its own 2:3 aspect ratio and rounded top corners. The info section below uses {spacing.md} horizontal padding and {spacing.base} vertical padding. The title uses {typography.title-sm} in {colors.ink}, the author line uses {typography.body-sm} in {colors.muted}, and the star rating sits as a compact caption below.

**`product-card-rating`** — A compact row of filled and unfilled star glyphs in {colors.star-rating}, followed by the average rating number and review count in {typography.caption} at {colors.muted}. The entire row sits 8px below the author line.

### Navigation
**`nav-bar`** — A persistent top bar at 64px height, white background with a 1px bottom border in {colors.hairline}. Contains the brand wordmark on the left, a search bar in the center, and account/help links on the right. Active nav links get a 2px bottom border in {colors.primary}.

**`search-bar`** — A compact search field with {colors.surface-soft} background, 8px rounding, and a 1px {colors.hairline} border. On focus, the border thickens to 2px in {colors.primary}. The placeholder text uses {colors.muted-soft}.

### Badges
**`badge`** — A small uppercase label used for "New" or "Exclusive" indicators on book selections. Dark background ({colors.badge-new}), white text, 4px rounding ({rounded.xs}), and tight 2px/8px padding. The badge-sale variant uses a red background ({colors.badge-sale}) for "Deal" or "Limited" tags.

### Forms
**`text-input`** — Standard form input for email, password, and address fields. White background, 44px height, 8px rounding, and a 1px {colors.hairline} border. On focus, the border becomes a 2px solid in {colors.primary}. Error state uses a 2px red border ({colors.badge-sale}) with an error message in {typography.caption} below.

### Footer
**`footer`** — A full-width section with {colors.surface-soft} background, containing links for Help, About, Terms, and Social. Links use {typography.link} in {colors.muted}, shifting to {colors.ink} on hover. The section has 64px vertical padding and 24px horizontal padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav bar collapses to hamburger menu; hero section reduces padding to 32px; search bar moves to a collapsible overlay |
| Tablet | 744–1128px | Two-column product grid; nav bar shows limited links with "More" dropdown; hero uses 48px padding |
| Desktop | 1128–1440px | Three-column product grid; full nav bar visible; standard spacing applied |
| Wide | > 1440px | Max-width container at 1440px; product grid can expand to four columns with larger cards |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain a minimum 44px height for touch accessibility
- Icon buttons and close targets are at least 44x44px
- Star rating stars are at least 32x32px tap targets on mobile

### Collapsing Strategy
- On mobile, the top nav collapses to a hamburger menu icon on the left and a cart icon on the right
- The search bar collapses to a magnifying glass icon that expands to a full-width overlay on tap
- The monthly selection grid collapses from three columns to one, with full-width cards
- The footer link columns stack vertically on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only one hex color (#313131) was extracted from the live site; the remaining colors in the palette (including the red badge-sale, muted grays, and surface tones) are inferred from common subscription-box patterns and may not match the exact live site values
- No font-family declarations beyond the system font stack were found; the brand may use a custom typeface (e.g., a licensed serif for headings) that was not detected
- Hover and active states for buttons, links, and inputs are estimated based on standard darkening/lightening patterns
- Error, success, and warning form states (colors, icons, messaging) are not confirmed
- The star rating component's exact glyph style (filled, half-filled, outline) and spacing are unknown
- Dark mode or high-contrast mode values are not available
- The hero section's background may include subtle patterns, gradients, or imagery that were not extracted
- Checkout flow components (payment forms, address validation, order summary) are not represented
- The monthly selection "voting" or "curation" UI (if present) is not captured
- Sub-brand or seasonal color variations (e.g., holiday themes) are not documented
