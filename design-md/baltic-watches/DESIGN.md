---
version: alpha
name: "Baltic Watches"
source_url: "https://baltic-watches.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Baltic builds its entire digital identity from a five-stop tonal grayscale — deep navy (#000d1e) through cool off-white (#f2f3f4) — with zero chromatic accent extracted from the live site. Where most watch brands cut in gold, red, or a brand-signature hue to signal premium positioning, Baltic withholds color entirely, letting dial photography carry all the expressive work: a sunburst blue fumé, a warm cream sub-dial, a lacquered black plate. The frame around those images is as neutral as a lightbox. Proxima Nova carries every type role without variation in family — a deliberate choice that keeps the editorial voice clipped and technical. Display headings run at weight 600–700 in tight tracking; product names such as HMS, Bicompax, Aquascaphe, and MR01 render in small-uppercase at `{typography.spec-label}` scale, echoing the engraved caseback discipline of the objects being sold. Body paragraphs stay lean at 16px/400 with 1.6 line-height — long enough to accommodate the French-language copy that appears across the bilingual storefront without crowding. The geometry is strictly orthogonal. Product cards, CTAs, and text inputs share a `{rounded.none}` envelope, and the specification table anchoring every PDP rows watch data — movement, case diameter, lug-to-lug, power reserve, water resistance — behind `{colors.hairline}` dividers at #cccfd2. The deep navy (`{colors.primary}`) doubles as hero background and mobile navigation drawer fill, creating a consistent dark-on-dark environment where `{colors.on-primary}` text reads cleanly against the near-black ground. `{colors.surface-soft}` at #f2f3f4 provides the only warmth in the palette, lifting product cards and form fields off the white canvas. Baltic's restraint is its product argument: a brand confident enough in its movements and dial craft to present them on a monochrome stage.

colors:
  primary: "#000d1e"
  primary-active: "#1a2d45"
  primary-disabled: "#6b7583"
  ink: "#000d1e"
  body: "#1c2129"
  muted: "#979798"
  hairline: "#cccfd2"
  hairline-soft: "#e5e7e8"
  canvas: "#ffffff"
  surface-soft: "#f2f3f4"
  surface-mid: "#e5e7e8"
  surface-card: "#ffffff"
  on-primary: "#f2f3f4"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 52px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.75px
  display-md:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 34px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0.5px
  body-md:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.57
    letterSpacing: 0
  caption:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  spec-label:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.45
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 2px
    textTransform: uppercase
  button-sm:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.5px
  price-display:
    fontFamily: "'proxima-nova', sans-serif"
    fontSize: 20px
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
    rounded: "{rounded.none}"
    padding: 14px 36px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 35px
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    border: none
    padding: 8px 0
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.ink}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 28px
  nav-bar-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
  mobile-menu-drawer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    linkTypography: "{typography.title-md}"
    width: 100vw
    padding: "{spacing.xl}"
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    imageAspectRatio: "1/1"
    imageBackground: "{colors.surface-soft}"
    rounded: "{rounded.none}"
    nameTypography: "{typography.spec-label}"
    priceTypography: "{typography.price-display}"
    descriptionTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    gap: "{spacing.sm}"
  hero-full:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 90vh
    headlineTypography: "{typography.display-xl}"
    subTypography: "{typography.body-md}"
    ctaVariant: button-secondary
    padding: "0 {spacing.xl}"
  hero-editorial:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 60vh
    headlineTypography: "{typography.display-md}"
    subTypography: "{typography.body-md}"
    imagePosition: right
  watch-spec-table:
    backgroundColor: "{colors.canvas}"
    borderColor: "{colors.hairline}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    labelColor: "{colors.muted}"
    valueColor: "{colors.ink}"
    rowPadding: "14px 0"
    rowBorder: "1px solid {colors.hairline-soft}"
  variant-swatch:
    size: 22px
    rounded: "{rounded.full}"
    selectedBorder: "2px solid {colors.ink}"
    selectedOffset: 2px
    unselectedBorder: "1px solid {colors.hairline}"
    gap: "{spacing.sm}"
  collection-badge:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.spec-label}"
    rounded: "{rounded.none}"
    padding: "3px 8px"
  filter-drawer:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    borderLeft: "1px solid {colors.hairline}"
    headingTypography: "{typography.spec-label}"
    optionTypography: "{typography.body-sm}"
    checkboxBorder: "1px solid {colors.hairline}"
    checkboxCheckedBg: "{colors.primary}"
    width: 300px
    padding: "{spacing.xl}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: "0 {spacing.base}"
  quantity-stepper:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.none}"
    buttonSize: 40px
    width: 120px
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.on-primary}"
    linkHoverColor: "{colors.muted}"
    headingTypography: "{typography.spec-label}"
    bodyTypography: "{typography.body-sm}"
    borderTop: none
    padding: "{spacing.xxl} 0 {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Full-width or fixed-width CTA in deep navy (#000d1e) with all-caps Proxima Nova at 2px letter-spacing. Hard corners (`{rounded.none}`) carry the instrument-catalog aesthetic throughout; there is no pill softness anywhere in the button system. Hover shifts to `{colors.primary-active}` (#1a2d45), revealing the navy character; disabled state desaturates to `{colors.primary-disabled}` at 60% opacity feel.

**`button-secondary`** — White canvas with 1px solid ink border and identical all-caps tracking. Sits alongside `button-primary` on PDPs — "Add to Wishlist" or "Find a Retailer" — occupying equal visual weight without competing for CTA hierarchy. Hover fills `{colors.surface-soft}`.

**`button-ghost`** — Borderless, transparent, used for secondary navigation affordances like "View All" in collection rows. Same uppercase tracking at `{typography.button-sm}` scale. No background change on hover; relies on underline or opacity shift.

### Text Input

**`text-input`** — Sharp-cornered field with 1px `{colors.hairline}` border at rest, upgrading to `{colors.ink}` on focus with no radius. Proxima Nova at 16px/400 matches body copy weight, keeping forms legible but visually undemanding. Used in newsletter capture, checkout, and account forms.

### Navigation

**`nav-bar`** — 64px-tall horizontal bar with bottom hairline, white canvas background, and Proxima Nova nav-link type at 13px/500. Logo anchors left; main collection links (Watches, Straps, Accessories, Journal) sit center or right depending on viewport. On scroll the bar may adopt `nav-bar-dark` (full `{colors.primary}` fill with `{colors.on-primary}` type) for hero pages with dark backgrounds. `mobile-menu-drawer` slides in full-width on a dark navy ground with enlarged link type at `{typography.title-md}`.

### Product Card

**`product-card`** — Borderless, `{colors.surface-soft}` ground, square image at 1:1 ratio with the dial photograph edge-to-edge. Product name renders at `{typography.spec-label}` — small-uppercase, tracking-wide — followed by a clean price at `{typography.price-display}` (20px/400). No hover overlay; Baltic lets the image speak without interactive chrome. Variant swatches, when present, render as 22px dial-color circles below the price.

### Hero

**`hero-full`** — Full-viewport dark module with `{colors.primary}` background, white headline at `{typography.display-xl}`, and a `button-secondary` CTA (white border on dark ground). Photography or video of watch close-ups occupies 50–60% of the frame. `hero-editorial` is a lighter variant on `{colors.surface-soft}` for collection introductions, pairing a `{typography.display-md}` headline with a right-aligned dial image.

### Watch Spec Table

**`watch-spec-table`** — The most typographically Baltic component: two-column rows with `{typography.spec-label}` uppercase labels in `{colors.muted}` on the left and `{typography.body-sm}` values in `{colors.ink}` on the right. Rows are separated by 1px `{colors.hairline-soft}` rules with 14px vertical padding. No outer border; the table floats on white canvas beneath the add-to-cart module.

### Variant Swatches

**`variant-swatch`** — 22px circles with a 2px `{colors.ink}` ring at 2px offset for the selected state, and 1px `{colors.hairline}` border for unselected. Swatches represent dial colors (not strap colors at this level), mapping to photography swaps on selection. Tight 8px gap keeps the swatch row compact under the product name.

### Badges

**`collection-badge`** — `{colors.surface-mid}` ground with `{typography.spec-label}` uppercase text; overlays the corner of collection banners to label "New Releases," "Limited Edition," or collection names. `new-badge` uses `{colors.primary}` ground with `{colors.on-primary}` type for product-card overlays.

### Filter & Search

**`filter-drawer`** — 300px panel sliding from the right on collection pages, white background with 1px left border. Section headings in `{typography.spec-label}`; checkbox options in `{typography.body-sm}`. Checked state fills the checkbox square with `{colors.primary}`. `search-bar` is a `{colors.surface-soft}` field at 44px height with no radius, used in site-wide search overlay.

### Footer

**`footer`** — Full-width `{colors.primary}` deep navy band. Column headings in `{typography.spec-label}` uppercase; links in `{typography.body-sm}` at `{colors.on-primary}`, dimming to `{colors.muted}` on hover. Newsletter input sits in a white-bordered borderless field. Social icons are white outline at 20px. The footer is the visual bookend to the hero — same dark navy, same white type, sealing the page in the brand's monochrome register.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger opening `mobile-menu-drawer`; hero headline drops to `{typography.display-md}`; spec table stacks full-width |
| Tablet | 744–1128px | Two-column product grid; nav links visible but condensed; hero transitions to split layout with 50/50 text and image |
| Desktop | 1128–1440px | Three- or four-column grid; full horizontal nav; hero-full at 90vh; spec table sits in right column of PDP two-column layout |
| Wide | > 1440px | Grid caps at 4 columns; horizontal max-width container at 1440px centers content; hero image scales to fill without stretching text region |

### Touch Targets

- All buttons minimum 48px height with adequate horizontal padding for thumb reach
- Variant swatches expand to 32px touch area via padding even though visual circle is 22px
- Nav hamburger icon minimum 44×44px tap target
- Quantity stepper buttons 40px square with clear separation to prevent mis-taps
- Filter checkboxes padded to full row height (minimum 44px) on mobile

### Collapsing Strategy

- Product grid: 4 col → 3 col (desktop) → 2 col (tablet) → 1 col (mobile)
- Hero copy: `display-xl` (52px) → `display-md` (34px) → `display-sm` (24px) at mobile
- PDP layout: two-column (image left, details right) collapses to single-column stack with image first, spec table below add-to-cart
- Footer columns: 4-col grid collapses to 2-col at tablet, single accordion-style stack at mobile
- Navigation: full horizontal links → hamburger at breakpoints below 744px; search icon always visible
- Filter panel: persistent sidebar on desktop → full-screen overlay on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No accent, highlight, or error-state color was captured — the five extracted tones are all grayscale/near-neutral; hover, error, and success states must be inferred or verified on-site
- No verified hover shade for `button-primary`; `{colors.primary-active}` (#1a2d45) is an informed estimate based on standard navy lightening
- No confirmed canvas color — site may use pure #ffffff or a very slight warm white not captured in extraction; #f2f3f4 and #ffffff are used contextually
- Font weight variants for Proxima Nova (300 light, 400, 500, 600, 700) not confirmed by extraction; weights above are typical for the brand's editorial register
- No confirmed border-radius values — all `{rounded.none}` usage is consistent with observed brand imagery but not pixel-verified
- No dark-mode palette captured; Baltic may not offer one
- Animation / transition tokens (hover easing, drawer slide duration) not available from static extraction
- Mobile-specific type scale not confirmed; responsive size drops above are estimated from common Shopify theme patterns
