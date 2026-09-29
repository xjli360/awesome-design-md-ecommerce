---
version: alpha
name: "Dyson"
source_url: "https://www.dyson.com"
captured_at: "2026-09-28T04:10:58.577933+00:00"
evidence_status: "historical_unverified"
description: |-
  FoundryGridnik, the geometric industrial sans-serif that Dyson developed for use on physical product casings and in-box materials, carries precisely the same authority in the digital interface — display headings in the 40–48px range at weight 700 with near-zero letter-spacing read as specification labels rather than marketing copy. Paired with DysonFutura for body and navigation, the stack makes every product claim feel like an engineering datum: "120,000 RPM," "0.3 micron filtration," "4.2 AirWatts" inhabit the same typographic register as a tolerance spec on a technical drawing. The palette divides into two deliberate registers: a near-white day side (#fbfbfb, #f7f7f7, #f0f0f0) where products float against almost nothing on seamless light backgrounds, and a near-black night side (#1c1c1c, #2e2e2e, #212121) reserved for technology-story sections where internal cyclone renders and motor cutaways glow against darkness. Magenta (#c4398d), deepening to #ab2975 on hover and active states, is the single interactive voltage of the system — it appears on primary CTAs, sale price callouts, selected filter chips, and active navigation indicators, never as a background wash across more than a narrow badge or button face. A secondary accent palette handles product colorway and messaging: the iconic cyclone yellow (#ffff00) that Dyson established in early domestic vacuum design, sustainability-green (#79b928), and a link-blue (#006fdd) for secondary interactive elements. Form geometry across the system is nearly rectilinear — product cards and specification panels are fully square ({rounded.none}), input fields sit at {rounded.xs} (4px), primary CTAs at {rounded.sm} (8px). Only filter chips and color-swatch selectors reach {rounded.full}, marking the small set of elements where a pill shape signals selectable categorization rather than primary action. Grid discipline is tight, with {spacing.section} (64px) vertical gutters between content bands and products arranged in 3-up or 4-up formations on wide viewports.

colors:
  primary: "#c4398d"
  primary-active: "#ab2975"
  primary-disabled: "#e4a8cf"
  accent-yellow: "#ffff00"
  accent-green: "#79b928"
  accent-green-dark: "#537d1c"
  accent-blue: "#006fdd"
  accent-blue-light: "#64affd"
  error: "#da2f47"
  ink: "#1c1c1c"
  body: "#212121"
  muted: "#595959"
  muted-soft: "#919191"
  hairline: "#dcdcdc"
  hairline-soft: "#ebebeb"
  canvas: "#ffffff"
  surface-soft: "#f7f7f7"
  surface-muted: "#f0f0f0"
  surface-card: "#ffffff"
  surface-dark: "#1c1c1c"
  surface-mid-dark: "#2e2e2e"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'FoundryGridnik', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'FoundryGridnik', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'FoundryGridnik', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'FoundryGridnik', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  spec-number:
    fontFamily: "'FoundryGridnik', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1px
  spec-unit:
    fontFamily: "'FoundryGridnik', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0
  title-md:
    fontFamily: "'DysonFutura', 'FoundryGridnik', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'DysonFutura', 'FoundryGridnik', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'DysonFutura', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'DysonFutura', Arial, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'DysonFutura', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  label-sm:
    fontFamily: "'DysonFutura', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'DysonFutura', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  button-sm:
    fontFamily: "'DysonFutura', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  nav-link:
    fontFamily: "'DysonFutura', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  promo-text:
    fontFamily: "'DysonFutura', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
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
    height: 48px
    states:
      hover:
        backgroundColor: "{colors.primary-active}"
      disabled:
        backgroundColor: "{colors.primary-disabled}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 48px
    border: "1px solid {colors.ink}"
    states:
      hover:
        border: "1px solid {colors.muted}"
        textColor: "{colors.muted}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    states:
      focus:
        border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoHeight: 24px
    iconColor: "{colors.ink}"
  promo-strip:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.promo-text}"
    height: 40px
    linkColor: "{colors.accent-blue-light}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    imageBackground: "{colors.surface-soft}"
    nameTypography: "{typography.title-sm}"
    priceTypography: "{typography.title-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    imagePadding: "{spacing.xl}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    ctaMarginTop: "{spacing.lg}"
  hero-banner-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    paddingVertical: "{spacing.section}"
    ctaMarginTop: "{spacing.lg}"
  spec-callout:
    backgroundColor: "{colors.surface-soft}"
    numberColor: "{colors.ink}"
    numberTypography: "{typography.spec-number}"
    unitTypography: "{typography.spec-unit}"
    labelTypography: "{typography.caption}"
    labelColor: "{colors.muted}"
    padding: "{spacing.xl}"
    rounded: "{rounded.none}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-new:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  filter-chip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
    states:
      active:
        backgroundColor: "{colors.ink}"
        textColor: "{colors.on-dark}"
        border: "1px solid {colors.ink}"
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    selectedRing: "2px solid {colors.ink}"
    selectedRingOffset: 2px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    iconColor: "{colors.muted-soft}"
    border: "1px solid {colors.hairline-soft}"
    height: 44px
  dark-feature-section:
    backgroundColor: "{colors.surface-mid-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    accentColor: "{colors.primary}"
    paddingVertical: "{spacing.section}"
  category-card:
    backgroundColor: "{colors.surface-muted}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.title-sm}"
    rounded: "{rounded.none}"
    imageAspectRatio: "3/2"
    hoverOverlay: "rgba(0,0,0,0.08)"

## Components

### Buttons

**`button-primary`** — Solid magenta (#c4398d) at 48px height with {rounded.sm} (8px) corners, set in DysonFutura weight 600 at 16px. On hover deepens to #ab2975; disabled state shifts to muted rose (#e4a8cf). Used exclusively for primary purchase CTAs ("Add to basket", "Shop now") and modal confirmations — never as a decorative or secondary element.

**`button-secondary`** — White fill with a 1px solid ink (#1c1c1c) border at the same 48px height. Deployed in two-CTA layouts alongside a primary button where the secondary action is exploratory ("Learn more", "View all specs", "Compare"). On hover, the border and text shift to muted (#595959) to signal interactivity without competing with the primary CTA.

**`button-ghost`** — Transparent background with ink text, same type scale, no border. Appears in navigation overlay panels, product configurators, and any context requiring a third action tier without adding visual mass to an already active layout zone.

**`button-dark`** — Ink (#1c1c1c) fill with white text; used exclusively within {hero-banner-dark} and {dark-feature-section} panels where the standard magenta button would create an unwanted accent collision against a dark field.

### Navigation

**`nav-bar`** — 64px white bar with a 1px hairline (#dcdcdc) bottom border that appears on scroll. Dyson wordmark sits left-aligned at 24px height. Category links (Vacuum, Hair, Air, Fans, Lighting) run center in DysonFutura 14px weight 500; a magenta underline appears on hover. Right cluster holds search, country selector, and basket as 24px line-icon glyphs with minimum 44px tap zones each.

**`promo-strip`** — 40px announcement banner in {colors.surface-dark} pinned above the nav, carrying promotion deadlines and free-shipping thresholds. Links styled in {colors.accent-blue-light} to remain legible on dark without conflicting with the magenta primary.

### Product Card

**`product-card`** — Zero-radius rectangular card on white. The image zone sits on a {colors.surface-soft} field with {spacing.xl} padding, letting the product object float. Below the image: product family in {typography.title-sm}, model name in {typography.title-md}, then the price block where sale price is rendered in {colors.primary} magenta and full price in ink. Sale and launch badges ({product-badge}, {product-badge-new}) overlay the upper-left corner of the image zone at a fixed 4px offset.

### Hero Banners

**`hero-banner`** and **`hero-banner-dark`** — The light variant deploys {colors.surface-soft} or pure white canvas for lifestyle and product photography; the dark variant uses {colors.surface-dark} (#1c1c1c) for technology-narrative hero sections where engineering renders and material cross-sections are the visual subject. Both share {typography.display-xl} headings and {spacing.section} vertical padding. All text on dark heroes is {colors.on-dark}.

### Spec Callout

**`spec-callout`** — The most distinctively Dyson UI pattern: a panel or inline card presenting a very large numeral (56px FoundryGridnik weight 700 via {typography.spec-number}), a smaller unit label in {typography.spec-unit}, and a two-line descriptor in {typography.caption} muted gray. Examples: "120,000 / RPM / Motor speed at peak suction", "0.3 / μm / Particles captured". These panels appear in technology-story scrolls and PDP pages, always on {colors.surface-soft} with {rounded.none}.

### Badges

**`product-badge`** — Magenta rectangular badge at {rounded.xs} in {typography.label-sm} all-caps white. Used for "SALE", percentage-off, and bundle callouts overlaid on the product card image zone.

**`product-badge-new`** — Identical geometry in {colors.ink} with {colors.on-dark} text. Used only for product launch labeling; the color distinction from the sale badge is functional, not decorative.

### Filter Chips

**`filter-chip`** — Pill-shaped ({rounded.full}) toggle chips for product listing filters: category, finish color, suction tier, motor class. Resting: white fill, hairline border, ink text. Active: ink fill, white text, ink border. On mobile, chips scroll horizontally in a single row with edge fade-out gradient; on desktop they wrap in a flex row.

### Color Swatches

**`color-swatch`** — 24px circle ({rounded.full}) representing a product finish option (Nickel, Iron/Blue, Copper, Gold, Fuchsia). The selected state shows a 2px ink ring offset by 2px. Visual size is small enough that each swatch carries a 10px invisible touch padding to meet minimum 44px tap targets on mobile.

### Search

**`search-bar`** — 44px input on {colors.surface-soft} with {rounded.sm} and a hairline-soft border. Magnifier glyph in {colors.muted-soft} on the left. On mobile, activating search expands to a full-screen overlay with recent searches and category shortcuts rendered as {filter-chip} elements below the input.

### Dark Feature Section

**`dark-feature-section`** — Full-width panel in {colors.surface-mid-dark} (#2e2e2e) for technology narrative sections (patent claims, internal mechanics, material science). Heading in {typography.display-md} white, body in {typography.body-md} near-white, pull-quote statistics and highlighted claims in {colors.primary} magenta.

### Category Cards

**`category-card`** — Rectangular, zero-radius card in {colors.surface-muted} used in homepage category navigation grids. A 3:2 aspect-ratio product image fills the upper portion; the category label sits below in {typography.title-sm} ink. On hover, a 8% dark overlay applies over the image zone without adding radius or shadow.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger + logo + basket; promo-strip text marquee-scrolls; spec callouts stack vertically full-width; hero headings drop to {typography.display-md}; filter chips scroll horizontally with edge fade |
| Tablet | 744–1128px | 2-column product grid; nav shows top-level category labels with overflow "More" dropdown; hero layouts shift to 50/50 image-text split |
| Desktop | 1128–1440px | 3-column product grid; full nav with all category labels and mega-menu on hover; spec callouts appear as inline 3-up horizontal rows |
| Wide | > 1440px | 4-column product grid; max-width container (~1400px) centered with expanded margins; spec callout panel spacing widens to {spacing.xxl} between items |

### Touch Targets

- All buttons, nav links, filter chips, and icon buttons maintain minimum 44×44px touch target
- Color swatches (24px visual) are padded to 44px tap zones with invisible hit-area extension
- Promo-strip links extend tap area to the full 40px strip height
- Hamburger and basket nav icons are minimum 44px tap zones regardless of glyph size

### Collapsing Strategy

- Primary nav collapses to hamburger at < 744px; category mega-panels become full-screen left-sliding drawers
- Spec callout grid collapses 4→2→1 across Desktop→Tablet→Mobile breakpoints
- Product card grid collapses 4→3→2→1 across Wide→Desktop→Tablet→Mobile
- Two-column hero layouts (image + text) stack image-above-text at < 744px; image aspect ratio shifts from 16:9 to 4:3 for tighter mobile crops
- Footer five-column layout collapses to two columns on tablet, then to accordion panels on mobile

## Known Gaps

- **Evidence:** [SOURCE.json](./SOURCE.json) records capture time, URLs and per-token evidence status. CSS value matches do not establish semantic roles or visual fidelity; unmeasured values remain inferred or unverified.

- Exact logo clearspace rules and minimum size are not extractable from site markup
- Navigation mega-menu column count, icon dimensions, and sub-category layout inferred from brand conventions; not directly confirmed by extraction
- DysonFutura weight axis range not publicly documented; weights 400/500/600 assumed from visual rendering
- FoundryGridnik variable-font axis availability not confirmed; static weights assumed
- Easing curves and animation durations for hover transitions, product configurator interactions, and scroll-reveal effects not extractable from static analysis
- Product color-configurator (finish/accessory selector) is JS-rendered and not structurally inspectable via extraction
- Dark-mode or alternate-theme support not confirmed; site appears to be single-theme with contextual dark sections rather than a system-level dark mode
- Precise grid column count and gutter widths not confirmed; 12-column with 24px gutters assumed from visual proportion
- `primary-disabled` (#e4a8cf) is an inferred interpolation; no explicit disabled-state color appeared in extracted palette
- Exact breakpoint pixel values are approximated; Dyson may use non-standard breakpoints internally
