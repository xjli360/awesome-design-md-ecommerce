---
version: alpha
name: "Moments In Time"
source_url: "https://momentsintime.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Archival gravity, not storefront warmth — the dominant `#112337` navy reads like ledger ink rather than brand enthusiasm, anchoring header rails, section banners, and primary CTA buttons in a single institutional hue that signals long-term credibility over conversion pressure. The palette seldom strays from this axis: an achromatic gray ladder (`#f5f5f5` canvas, `#eeeeee` card surfaces, `#e6e6e6` inner fills, `#c4c4c4` hairlines) supports the navy without competing, creating a depth hierarchy so compressed it reads as catalogue pages rather than layered UI. The one chromatic intrusion is `#cc0000`, used narrowly on sale banners and urgency flags — functioning like a red wax seal on a certificate rather than a standard conversion nudge. No custom webfonts appear in the extracted stack; Arial and Helvetica carry everything from display headings to provenance microcopy. The flatness is appropriate: a buyer comparing a 1967 Mickey Mantle single against a 1969 Joe Namath team-signed photograph needs legible specification text, not expressive type. Product cards sit at `{rounded.xs}` — virtually sharp-cornered — which contrasts with `{rounded.full}` pill filters used for sport and era navigation, creating a two-register system: catalogue items get the hard edge, filters get the approachable pill. Authentication vocabulary drives the component set more than brand expression does. Certificate of Authenticity badges inherit the primary navy as their background, white-reversing the text in `{typography.label-upper}` uppercase tracking — functioning as institutional seals, not marketing labels. Trust copy, guarantee language, and provenance footnotes occupy persistent real estate in the footer's deep `#0a1c4c` block, which reads as the legal annex of a physical dealer catalogue brought online. The overall register is a reputable specialist dealer who considers the interface a transparent container for the objects, not a surface for brand performance.

colors:
  primary: "#112337"
  primary-active: "#0a1c4c"
  primary-disabled: "#585e6a"
  accent-red: "#cc0000"
  ink: "#313131"
  body: "#32373c"
  muted: "#686e77"
  muted-soft: "#585e6a"
  hairline: "#c4c4c4"
  hairline-soft: "#dedede"
  border-strong: "#b8b8b8"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#eeeeee"
  surface-mid: "#e6e6e6"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-bold:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.4
    letterSpacing: 0
  label-upper:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.8px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  price-lg:
    fontFamily: "Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.25px
  nav-link:
    fontFamily: "Arial, Helvetica, sans-serif"
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
    rounded: "{rounded.xs}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    opacity: 0.7
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    border: "2px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 22px
    height: 44px
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.primary}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    height: 42px
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 56px
    topBandBackgroundColor: "{colors.primary-active}"
    topBandHeight: 36px
    topBandTypography: "{typography.caption}"
  product-card:
    backgroundColor: "{colors.canvas}"
    border: "1px solid {colors.hairline}"
    hoverBorderColor: "{colors.primary}"
    rounded: "{rounded.xs}"
    imageAspectRatio: "3/4"
    padding: "{spacing.sm}"
    gap: "{spacing.sm}"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-lg}"
    captionTypography: "{typography.caption}"
    provenanceTypography: "{typography.caption}"
    provenanceColor: "{colors.muted}"
  authentication-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
    border: "1px solid {colors.primary-active}"
  sale-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-upper}"
    rounded: "{rounded.xs}"
    padding: "3px 7px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    border: "1px solid {colors.border-strong}"
    rounded: "{rounded.xs}"
    height: 44px
    padding: "0 {spacing.md}"
    buttonBackgroundColor: "{colors.primary}"
    buttonTextColor: "{colors.on-primary}"
    buttonTypography: "{typography.button-sm}"
    buttonRounded: "{rounded.xs}"
  category-pill:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  category-pill-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.primary}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} {spacing.xl}"
    minHeight: 360px
    rounded: "{rounded.none}"
    ctaBackgroundColor: "{colors.canvas}"
    ctaTextColor: "{colors.primary}"
  trust-seal:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-bold}"
    border: "1px solid {colors.hairline-soft}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
    iconColor: "{colors.primary}"
  price-display:
    textColor: "{colors.primary}"
    typography: "{typography.price-lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    separator: "/"
  section-heading-strip:
    backgroundColor: "{colors.surface-mid}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    borderLeft: "4px solid {colors.primary}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.none}"
  footer:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.hairline}"
    linkHoverColor: "{colors.canvas}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    rounded: "{rounded.none}"

## Components

### Buttons
**`button-primary`** — Solid `#112337` navy block at 44px height with sharp `{rounded.xs}` corners and bold Arial tracking. Hover deepens to `{colors.primary-active}` (`#0a1c4c`); active state identical; disabled drops to `{colors.primary-disabled}` gray-blue at reduced opacity. The flatness signals institutional action — buy, add to cart, submit — with no decorative softening.

**`button-secondary`** — White fill with a 2px `{colors.primary}` navy border. Used for secondary CTAs like "Add to Wishlist" or "View Details" alongside a primary button. Shares the same sharp `{rounded.xs}` radius, maintaining catalogue consistency.

**`button-ghost`** — Transparent background, `{colors.body}` text, used for low-priority actions such as pagination controls, filter resets, and inline text links styled as buttons. No border.

### Navigation
**`nav-bar`** — Two-band structure: a slim `{colors.primary-active}` utility bar at 36px for account links, phone numbers, and trust copy, sitting above the main 56px `{colors.primary}` nav rail with logo, primary category links, and search. Both bands use white type. No sticky behavior change; no transparent-on-scroll treatment.

### Product Cards
**`product-card`** — White canvas with a 1px `{colors.hairline}` border that steps to `{colors.primary}` on hover, the only dynamic brand-color moment on browse pages. Image occupies a 3:4 portrait ratio reflecting the vertical orientation of signed photos, jerseys, and framed pieces. Below the image: item name in `{typography.title-sm}`, provenance sub-line and condition grade in `{typography.caption}` muted, then price in `{typography.price-lg}`. Authentication Badge overlays the image corner when a COA is included.

### Authentication Badge
**`authentication-badge`** — Navy fill with white `{typography.label-upper}` uppercase text reading "COA INCLUDED" or "AUTHENTICATED." Fine `{colors.primary-active}` border at `{rounded.xs}` creates the sealed-document impression. This badge is the primary trust signal and appears on both cards and product detail headers.

### Sale Badge
**`sale-badge`** — `#cc0000` red pill at `{rounded.xs}` with white uppercase label. Used sparingly on sale items and clearance listings. Never stacked with the authentication badge on the same image corner.

### Search
**`search-bar`** — Prominent full-width or header-embedded input at 44px height with a navy submit button on the right at `{rounded.xs}`. Placeholder reads something like "Search by athlete, team, or item…" in `{colors.muted}`. Border steps from `{colors.border-strong}` at rest to `{colors.primary}` on focus.

### Category Pills
**`category-pill`** / **`category-pill-active`** — Horizontal scrolling row of `{rounded.full}` pills for sport, era, and item-type filters. Inactive state uses `{colors.surface-soft}` fill with a `{colors.hairline}` border; active flips to solid `{colors.primary}` navy with white text. The pill radius contrast against the card's `{rounded.xs}` is the interface's sharpest visual register shift.

### Hero Banner
**`hero-banner`** — Full-bleed `#112337` navy panel with white display type. Minimum 360px tall; typically features a featured athlete name in `{typography.display-xl}` with a short editorial line and a white-fill CTA button (`ctaTextColor: primary`). No image overlay or gradient — the navy is the background, keeping the focus on copy and the featured signed piece photograph floated alongside.

### Trust Seals
**`trust-seal`** — Small `{colors.surface-soft}` card with `{rounded.sm}` corners, a navy icon (money-back guarantee, authentication seal, secure checkout), and bold caption text. Arranged in a horizontal row below the add-to-cart area and repeated in the footer zone. The icon color `{colors.primary}` ties them visually to the brand rail without competing with product imagery.

### Section Heading Strip
**`section-heading-strip`** — A `{colors.surface-mid}` background band with a 4px solid `{colors.primary}` left border accent, displaying section titles in `{typography.display-sm}`. Functions as a catalogue section divider between "Featured Athletes," "New Arrivals," and category groups — the left-border treatment is the closest thing to a decorative motif in the system.

### Footer
**`footer`** — Deep `#0a1c4c` block with white body type and hairline-colored links. Contains columns for customer service, authentication guarantees, legal fine print, and social links. The deliberate deepening from `#112337` to `#0a1c4c` signals the transition from commercial space to legal/institutional space.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; category pills scroll horizontally; nav bar collapses to hamburger + logo + cart icon; hero banner min-height reduces to 240px; search bar becomes full-width below nav |
| Tablet | 744–1128px | Two-column product grid; nav shows top-level categories inline, secondary links in overflow; hero banner restores to 300px; trust seals stack in 2×2 grid |
| Desktop | 1128–1440px | Three- or four-column product grid; full two-band nav bar visible; hero banner at full 360px with side-by-side copy and product image |
| Wide | > 1440px | Max-width container (~1400px) centered; grid columns cap at four; hero text and image maintain proportional sizing within container |

### Touch Targets
- All buttons and pill filters maintain minimum 44px height on mobile
- Category pill rows use native horizontal scroll with visible overflow clipping; no custom scrollbar
- Product card tap target covers the full card face including image and text area
- Nav hamburger icon minimum 44×44px hit area

### Collapsing Strategy
- Nav mega-menu (if present) collapses to accordion inside the mobile drawer
- Two-band nav consolidates: utility top band is hidden on mobile; account/cart icons move into the main nav row
- Trust seals collapse from a 4-up horizontal row to a vertical stack on mobile
- Footer columns stack vertically at mobile; headings become accordion toggles to reduce scroll depth
- Section heading strips maintain full width at all breakpoints; left-border accent scales with padding

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No custom webfonts detected — only Arial, Helvetica, and system fallback stacks; brand may load a custom or licensed font via JS that wasn't captured
- Many vibrant hex values in the extraction (`#00d084`, `#0693e3`, `#204ce5`, `#4721fb`, `#ab1dfe`, `#34e2e4`, `#7a00df`, `#f01d4f`) are consistent with WordPress Gutenberg block editor palette defaults and are unlikely to be brand colors; excluded from the design system
- No meta theme-color tag; mobile browser chrome color unknown
- Brand may use a gold or warm amber accent for "premium" or "featured" item callouts — a common convention in authenticated memorabilia — but no such color was captured
- Exact border-radius values not confirmed from CSS inspection; `{rounded.xs}` (4px) is an inference from the institutional aesthetic
- Navigation structure (mega-menu vs. flat dropdown) not confirmed; component model above assumes flat dropdown
- COA badge exact copy, iconography, and positioning relative to product image approximated
- Dark mode or alternate theme variant not detected
- Hover / focus transition timing and easing values not extracted
