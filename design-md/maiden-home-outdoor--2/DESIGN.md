---
version: alpha
name: "Maiden Home"
source_url: "https://maidenhome.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Deep charcoal borders on black (#1c1c1c over #121212) wrap the Maiden Home storefront like the matte frame of an architect's portfolio — the furniture is meant to feel exhibited, not merchandised. A single cerulean accent (#334fb4) punctuates primary call-to-action buttons and hover-state underlines, its saturation calibrated just warm enough to read as confident rather than corporate against the warm off-white canvas (#f5f5f1). Headings set in ABC Whyte at generous sizes but restrained weight (500–600) let letterforms breathe; body copy drops into Maison Neue at 400 weight, a pairing that signals European type-house literacy without veering into fashion-editorial territory. Card corners land at `{rounded.sm}` — 8px, enough softness to feel approachable but far from the pill shapes of consumer marketplaces. Product photography dominates the grid with nearly zero ornamentation: no badges crowd the image, no gradient overlays dim the weave of a Sunbrella sling or the grain of teak. The spacing system is generous — `{spacing.section}` between content blocks, `{spacing.xl}` gutters in the collection grid — giving each piece room the way a showroom gives room. Navigation is minimal: a sticky top bar at 64px with uppercase category links in `{typography.nav-link}` and a dark navy hover state (#242833) that barely shifts from the ink tone, as if the interface is trying to stay out of the way of the material story. Fabric-swatch selectors, configuration drawers, and lead-time indicators are the interaction signatures — the site sells customization confidence more than impulse. Footer columns run on a #121212 ground with #dedede text, closing the page in the same near-black that opened it, a tonal bookend that makes the light canvas between feel like a window onto a sunlit courtyard.

colors:
  primary: "#334fb4"
  primary-active: "#2a4199"
  primary-disabled: "#99a8d9"
  ink: "#1c1c1c"
  ink-deep: "#121212"
  body: "#242833"
  muted: "#6b6b6b"
  muted-soft: "#9a9a9a"
  hairline: "#dedede"
  hairline-soft: "#e8e8e4"
  canvas: "#f5f5f1"
  surface-soft: "#eeeee9"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#ffffff"
  on-dark: "#dedede"
  on-dark-muted: "#9a9a9a"
  accent-hover: "#242833"
  error: "#c0392b"
  success: "#2e7d32"

typography:
  display-xl:
    fontFamily: "'ABC Whyte', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'ABC Whyte', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'ABC Whyte', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'ABC Whyte', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'ABC Whyte', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'ABC Whyte', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0.1px
  caption-sm:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'ABC Whyte', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'ABC Whyte', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'ABC Whyte', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 1.2px
    textTransform: uppercase
  link:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  label:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  price:
    fontFamily: "'ABC Whyte', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  lead-time:
    fontFamily: "'Maison Neue', 'Assistant', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
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
  section-lg: 96px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 31px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    padding: 0
    borderBottom: 1px solid {colors.ink}
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.hairline}
    borderFocus: 1px solid {colors.ink}
  text-input-error:
    border: 1px solid {colors.error}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    position: sticky
  nav-bar-link-hover:
    textColor: "{colors.accent-hover}"
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption-sm}"
    height: 36px
    padding: 0 {spacing.base}
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0
    imageAspectRatio: 4:5
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price}"
    captionTypography: "{typography.caption}"
    gap: "{spacing.sm}"
  product-card-hover:
    boxShadow: 0 2px 12px rgba(0,0,0,0.08)
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    minHeight: 85vh
    padding: "{spacing.section} {spacing.xl}"
    ctaStyle: button-primary
  hero-banner-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
  collection-grid:
    columns: 3
    gap: "{spacing.lg}"
    padding: 0 {spacing.xl}
    itemComponent: product-card
  material-swatch:
    size: 40px
    rounded: "{rounded.full}"
    border: 2px solid transparent
    borderSelected: 2px solid {colors.ink}
    outlineSelected: 2px solid {colors.canvas}
    outlineOffset: 2px
    labelTypography: "{typography.label}"
  material-swatch-lg:
    size: 64px
    rounded: "{rounded.full}"
    border: 2px solid {colors.hairline}
    borderSelected: 2px solid {colors.ink}
    labelTypography: "{typography.caption}"
  configuration-drawer:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    width: 480px
    padding: "{spacing.xl}"
    headingTypography: "{typography.display-sm}"
    bodyTypography: "{typography.body-md}"
    overlay: rgba(18,18,18,0.5)
    rounded: "{rounded.none}"
  lead-time-indicator:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.lead-time}"
    rounded: "{rounded.xs}"
    padding: "{spacing.sm} {spacing.md}"
    iconSize: 16px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separator: "/"
    activeColor: "{colors.ink}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    mutedTextColor: "{colors.on-dark-muted}"
    headingTypography: "{typography.label}"
    linkTypography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
    columnGap: "{spacing.xl}"
  footer-newsletter:
    inputBackgroundColor: transparent
    inputTextColor: "{colors.on-dark}"
    inputBorder: 1px solid {colors.on-dark-muted}
    inputRounded: "{rounded.xs}"
    buttonStyle: button-primary
  testimonial-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    quoteTypography: "{typography.body-md}"
    attributionTypography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xl}"
    border: 1px solid {colors.hairline}
  image-gallery:
    thumbnailSize: 72px
    thumbnailRounded: "{rounded.xs}"
    thumbnailBorder: 1px solid {colors.hairline}
    thumbnailBorderActive: 1px solid {colors.ink}
    mainImageRounded: "{rounded.sm}"
    gap: "{spacing.sm}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  badge-bestseller:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 10px
  search-overlay:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    inputTypography: "{typography.display-sm}"
    resultTypography: "{typography.body-md}"
    overlay: rgba(18,18,18,0.6)
    padding: "{spacing.section} {spacing.xl}"
---

## Components

### Buttons

**`button-primary`** — Solid cerulean (#334fb4) background with white uppercase text tracked at 0.5px. Corners are barely eased at `{rounded.xs}` (4px), keeping the shape architectural. On hover, the background darkens to `{colors.primary-active}` (#2a4199) with no scale or shadow animation — just a clean color shift. Disabled state desaturates to `{colors.primary-disabled}` (#99a8d9). Height is fixed at 48px with generous horizontal padding (32px each side) so the button never feels cramped beside product imagery.

**`button-secondary`** — Transparent fill with a 1px `{colors.ink}` border and uppercase dark text. On hover, the fill inverts to solid `{colors.ink}` with white text — a binary toggle rather than a gradient transition. Used for secondary actions like "View Details" and "Add to Wishlist" where the primary cerulean would compete with the main CTA.

**`button-tertiary`** — No background, no border radius, just ink-colored text with a 1px bottom underline. Used for inline actions like "Read More" or "See All Materials" where the interaction should feel like a text link rather than a button.

### Text Input

**`text-input`** — White card-surface fill with a 1px `{colors.hairline}` (#dedede) border that sharpens to `{colors.ink}` on focus. Label floats above in `{typography.label}` (uppercase, 12px, 500 weight). Error state swaps the border to `{colors.error}`. The 48px height and `{rounded.xs}` corners match button dimensions so form rows align cleanly.

### Navigation

**`nav-bar`** — Sticky 64px bar on the warm canvas (#f5f5f1) with a subtle `{colors.hairline}` bottom border. Logo sits left; category links run center in `{typography.nav-link}` — 12px uppercase with 1.2px tracking. Hover state shifts text to `{colors.accent-hover}` (#242833), a nearly imperceptible darkening that avoids visual noise. Cart icon and hamburger (mobile) sit right. The bar does not change color on scroll.

**`announcement-bar`** — Full-width strip above the nav in `{colors.ink}` (#1c1c1c) with `{colors.on-dark}` (#dedede) text. Typically a single line about lead times or free shipping thresholds. Dismissible with an × icon. Height is 36px.

### Product Card

**`product-card`** — White card on the cream canvas. Image fills the top at a 4:5 aspect ratio with no overlay or badge by default. Below the image, the product title in `{typography.title-sm}` (16px, 500 weight) is followed by the price in `{typography.price}` and a material note in `{typography.caption}`. On hover, a subtle box-shadow (0 2px 12px, 8% black) lifts the card. The `{rounded.sm}` corners keep the shape clean without looking clinical.

### Hero Banner

**`hero-banner`** — Full-bleed section with a minimum height of 85vh. The light variant uses `{colors.surface-soft}` (#eeeee9) behind a full-width lifestyle photograph with the headline in `{typography.display-xl}` (48px, 500 weight) overlaid or adjacent. The dark variant inverts to `{colors.surface-dark}` (#121212) with `{colors.on-dark}` text for seasonal campaigns. A single `button-primary` CTA sits below the headline. Text is left-aligned on desktop, stacked and centered on mobile.

### Material Swatch

**`material-swatch`** — 40px circle (`{rounded.full}`) filled with a fabric thumbnail or solid color. Unselected swatches have a transparent border; the selected swatch gains a 2px `{colors.ink}` border with a 2px white outline offset creating a ring effect. Below the row, a `{typography.label}` string names the active material. The large variant (`material-swatch-lg`) runs at 64px for the product detail page configurator.

### Configuration Drawer

**`configuration-drawer`** — A 480px slide-in panel from the right used for fabric selection, dimension options, and leg-finish choices. White background, no border radius (flush to viewport edge), with a semi-transparent overlay (rgba(18,18,18,0.5)) behind it. Section headings use `{typography.display-sm}` and option rows use `{typography.body-md}`. A sticky footer inside the drawer holds the "Add to Cart" `button-primary` so the CTA is always visible during configuration.

### Lead Time Indicator

**`lead-time-indicator`** — A compact inline element with `{colors.surface-soft}` background and `{rounded.xs}` corners. A small calendar or clock icon (16px) sits left of the estimated delivery text in `{typography.lead-time}`. Placed directly below the price on the product detail page to set delivery expectations before the customer enters configuration.

### Breadcrumb

**`breadcrumb`** — Muted-color text links in `{typography.caption}` separated by "/" characters. The last item in the chain renders in `{colors.ink}` to indicate the current page. Spacing between items is `{spacing.xs}` (4px). Positioned above the product title on detail pages.

### Footer

**`footer`** — Dark ground (#121212) that mirrors the announcement bar's tone. Column headings are uppercase `{typography.label}` in `{colors.on-dark}` (#dedede), and links use `{typography.body-sm}` in `{colors.on-dark-muted}` (#9a9a9a) that brightens to `{colors.on-dark}` on hover. A newsletter signup row uses a transparent-fill input with a muted border and a `button-primary` submit. The footer closes the page in the same darkness that opens it.

### Testimonial Card

**`testimonial-card`** — White card with a 1px `{colors.hairline}` border and `{rounded.sm}` corners. The quote in `{typography.body-md}` is followed by an attribution line in `{typography.caption}`. Padding is `{spacing.xl}` (32px). Used in a horizontal carousel on landing pages.

### Image Gallery

**`image-gallery`** — On the product detail page, a large main image with `{rounded.sm}` corners occupies the left column. Below or beside it, 72px square thumbnails with `{rounded.xs}` corners scroll horizontally. The active thumbnail has a 1px `{colors.ink}` border; inactive thumbnails use `{colors.hairline}`. Gap between thumbnails is `{spacing.sm}`.

### Badges

**`badge-new`** — Small cerulean (#334fb4) pill with white uppercase text at 11px. Positioned over the top-left corner of a product card image when applicable.

**`badge-bestseller`** — Same shape and sizing as `badge-new` but in solid `{colors.ink}` (#1c1c1c).

### Search Overlay

**`search-overlay`** — Full-screen overlay with a darkened backdrop (rgba(18,18,18,0.6)). The search input is styled as a large, borderless text field in `{typography.display-sm}` centered on a white panel. Results populate below in `{typography.body-md}` with product thumbnails. The overlay closes on Escape or clicking the backdrop.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger + logo + cart icon. Hero stacks text below image at 100vw. Collection grid drops to 1 column. Configuration drawer becomes full-screen bottom sheet. Footer columns stack vertically. `{typography.display-xl}` scales to 32px. Material swatches scroll horizontally. |
| Tablet | 744–1128px | Collection grid runs 2 columns. Nav shows top categories but secondary links move to hamburger. Hero text overlays image at reduced font size (40px). Configuration drawer remains 480px with overlay. Footer runs 2-column layout. |
| Desktop | 1128–1440px | Full 3-column collection grid. Nav displays all category links inline. Product detail runs image gallery left (60%) and configuration right (40%). Hero at full 85vh with 48px display type. |
| Wide | > 1440px | Content max-width caps at 1440px and centers. Outer margins fill with `{colors.canvas}`. Collection grid may expand to 4 columns on pages with large catalogs. Spacing scales: `{spacing.section}` increases to `{spacing.section-lg}` (96px) between major blocks. |

### Touch Targets

- All interactive elements (buttons, swatches, nav links) maintain a minimum 44×44px touch area on mobile, even when the visual element is smaller (e.g., 40px swatches gain 4px invisible padding).
- Material swatches expand to `material-swatch-lg` (64px) on touch devices for easier selection.
- The hamburger menu icon hit area is 48×48px.
- Cart and search icons in the nav maintain 48px tap targets.

### Collapsing Strategy

- Navigation categories move into a full-screen slide-out drawer on mobile, organized as a vertical list with `{typography.title-md}` sizing and `{spacing.lg}` vertical gaps.
- The product detail two-column layout (gallery + config) stacks vertically on mobile: gallery on top (full-width horizontal scroll for thumbnails), then configuration below with a sticky "Add to Cart" bar at the bottom of the viewport.
- Footer columns stack into an accordion pattern on mobile, with section headings toggling open/closed.
- Announcement bar text truncates with ellipsis on narrow viewports; a swipe or auto-rotate reveals multiple messages.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color was detected; the value used for `{colors.canvas}` (#f5f5f1) is derived from extracted background colors and may not match the brand's intended browser-chrome tint.
- The font stacks include both ABC Whyte and Maison Neue, but exact weight availability (whether the site loads 300, 400, 500, 600, or 700 cuts of each) could not be confirmed from extraction alone — the weights specified here are inferred from visual hierarchy patterns.
- The extracted palette is limited to six values; accent colors for success states, warnings, or promotional highlights (e.g., sale red) were not detected and are approximated from common conventions.
- Icon style (line weight, filled vs. outlined, custom vs. library) could not be determined from color/font extraction.
- Exact animation/transition durations and easing curves are not captured — the site likely uses subtle 200–300ms ease-out transitions on hover states and drawer open/close, but specific values would require runtime inspection.
- The `#334fb4` cerulean is identified as primary based on distinctiveness among extracted colors; if the brand uses it only as a secondary accent, the primary/secondary mapping may need inversion.
- Shopify theme template structure (sections, blocks) and Liquid-specific class naming conventions are not reflected in this design system.
