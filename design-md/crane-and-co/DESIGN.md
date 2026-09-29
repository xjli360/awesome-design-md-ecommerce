---
version: alpha
name: "Crane & Co."
source_url: "https://www.crane.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Whyte-Regular at a light weight over midnight navy (#0f172b) announces a deliberate tension — a paper house with roots in the early nineteenth century choosing a contemporary grotesque as its editorial voice rather than the serifs its engraved stationery would imply. The deepest brand color is not the slate blue (#3d5789) that carries interactive links and active states, nor the warm-parchment surface (#eeedec) that quietly evokes cotton rag stock — it is the soft lavender accent (#ccb7ff) that appears in collection banners and hero washes, a chromatic move that reads as deliberate contemporary repositioning rather than heritage reverence. Roboto handles functional text at uppercase, tracked settings (500 weight, 1–1.5px letter-spacing on button and label styles), providing structural contrast that Whyte's open apertures alone do not supply. Navigation and the promotional bar ride the deep navy (#0f172b) shell, concentrating the brand's darkest statement at the very top of the page so product photography can breathe below. Product cards sit on the parchment #eeedec ground — a warm near-white that suggests laid paper without literal texture simulation. Hard corners (`{rounded.none}`) govern every interactive control: buttons, form inputs, product tiles, and content panels — square edges read as deliberate precision, the visual grammar of a clean die-cut on a high-quality envelope rather than the softened forms that consumer apps default to. Spacing scales from tight label-to-field pairs (`{spacing.sm}`) inside the monogram configurator up to full-bleed section gutters (`{spacing.section}`) on editorial collection pages. The gray midtone ramp (#1d1d1d through #8b8b8b) keeps color restrained until the lavender accent arrives at exactly the moments — hero panels, collection banners, personalization highlights — where the brand needs contemporary energy without losing the measured restraint that defines fine stationery culture.

colors:
  primary: "#3d5789"
  primary-active: "#2c4070"
  primary-disabled: "#b7b7b7"
  accent: "#ccb7ff"
  ink: "#0f172b"
  ink-warm: "#1c1917"
  body: "#1d1d1d"
  body-alt: "#404040"
  muted: "#777777"
  muted-soft: "#8b8b8b"
  hairline: "#dcdddd"
  hairline-soft: "#d8d8d8"
  hairline-light: "#eeeeee"
  canvas: "#f8f8f8"
  surface-soft: "#f5f5f5"
  surface-card: "#eeedec"
  surface-deep: "#0f172b"
  on-primary: "#ffffff"
  on-dark: "#f8f8f8"

typography:
  display-xl:
    fontFamily: "'Whyte-Regular', Roboto, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.07
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Whyte-Regular', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 300
    lineHeight: 1.17
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Whyte-Regular', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Whyte-Regular', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0
  title-md:
    fontFamily: "'Whyte-Regular', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0.3px
  caption-upper:
    fontFamily: "Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1
    letterSpacing: 0.8px
    textTransform: uppercase
  nav-link:
    fontFamily: "Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1
    letterSpacing: 0.5px
  label:
    fontFamily: "Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 1.5px
    textTransform: uppercase
  price:
    fontFamily: "'Whyte-Regular', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
    padding: 13px 31px
    height: 48px
  button-ghost:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.on-dark}"
    padding: 13px 31px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
  nav-bar:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    logoColor: "{colors.on-dark}"
    borderBottom: "none"
  nav-bar-scrolled:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    borderBottom: "1px solid {colors.hairline}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.title-md}"
    bodyTypography: "{typography.body-sm}"
    priceTypography: "{typography.price}"
    categoryTypography: "{typography.caption-upper}"
    categoryColor: "{colors.muted}"
    rounded: "{rounded.none}"
    imageAspectRatio: "4/3"
    padding: "{spacing.base}"
  hero:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 600px
    accentColor: "{colors.accent}"
    padding: "{spacing.section} {spacing.xxl}"
  hero-light:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xxl}"
  collection-banner:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    titleTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "{spacing.xxl}"
  promo-banner:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-upper}"
    height: 40px
    padding: "{spacing.sm} {spacing.base}"
  category-badge:
    backgroundColor: "transparent"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption-upper}"
    rounded: "{rounded.none}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    borderFocused: "1px solid {colors.ink}"
    iconColor: "{colors.muted}"
    height: 48px
    padding: "0 {spacing.base}"
  personalization-panel:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    bodyTypography: "{typography.body-sm}"
    labelTypography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "{spacing.lg}"
    accentColor: "{colors.accent}"
  monogram-display:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline-soft}"
    padding: "{spacing.xl}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    bodyTypography: "{typography.body-sm}"
    linkTypography: "{typography.nav-link}"
    headingTypography: "{typography.label}"
    dividerColor: "{colors.body-alt}"
    padding: "{spacing.section}"
  breadcrumb:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline-soft}"

## Components

### Buttons

**`button-primary`** — A full-width or fixed-width deep-navy block (`{colors.ink}`, #0f172b) with uppercase tracked Roboto at 500 weight and 48px height. Square corners (`{rounded.none}`) signal editorial precision — no radius softening anywhere in the control set. On hover, background shifts to the slate blue (`{colors.primary-active}`) to signal interactivity without introducing a secondary color family; disabled state uses `{colors.primary-disabled}` (#b7b7b7) with muted text on the same gray register.

**`button-secondary`** — Transparent background with a 1px `{colors.ink}` border and matching uppercase Roboto. Used in paired CTA arrangements alongside primary — "Shop All" next to "Shop Wedding" — where two actions share equal editorial weight. On dark backgrounds, `button-ghost` substitutes `{colors.on-dark}` border and text for legibility against navy or photography.

**`button-ghost`** — Transparent with `{colors.on-dark}` border and text, placed directly over dark-navy hero panels or product photography backgrounds. Maintains the same 48px height and uppercase tracking as all button variants for vertical rhythm across mixed-context pages.

### Navigation

**`nav-bar`** — A 64px deep-navy bar (`{colors.surface-deep}`) housing the Crane wordmark in `{colors.on-dark}`, with `{typography.nav-link}` (13px Roboto, 0.5px tracking) for category links spread horizontally. On scroll, the bar transitions to `nav-bar-scrolled`: a canvas background with `{colors.ink}` text and a single-pixel `{colors.hairline}` bottom border. A `promo-banner` in `{colors.accent}` lavender (#ccb7ff) sits immediately above the nav on sale and collection launch pages, making lavender the very first color the visitor reads.

### Product Card

**`product-card`** — Built on the warm parchment `{colors.surface-card}` (#eeedec), each card pairs a flush image (4:3 aspect ratio, `{rounded.none}`) with a three-row text block: category in `{typography.caption-upper}` at `{colors.muted}`, title in `{typography.title-md}`, price in `{typography.price}`. The parchment background creates warmth without any texture simulation. No drop shadows, no outer borders — cards are differentiated from the page canvas purely by background color contrast.

### Hero

**`hero`** — Full-bleed midnight-navy panels (`{colors.surface-deep}`) with `{typography.display-xl}` headlines in `{colors.on-dark}`. The lavender accent (`{colors.accent}`) may wash the lower portion of the hero as a gradient or highlight a single keyword in the headline copy. Minimum 600px height on desktop. The `hero-light` variant swaps to `{colors.surface-card}` for editorial feature pages where photography is secondary to typographic composition.

### Collection Banner

**`collection-banner`** — A full-width lavender block (`{colors.accent}`, #ccb7ff) with `{typography.display-md}` headline and generous padding (`{spacing.xxl}`). This is the primary vehicle for the brand's most distinctive color — it appears where a new collection or seasonal range demands more than a product grid, acting as an interstitial poster between browse sections. Hard edges and centered layout give it bulletin-board weight.

### Personalization Panel

**`personalization-panel`** — A soft-gray container (`{colors.surface-soft}`) housing monogram and customization options for custom stationery and business card configurators. Section headings use `{typography.label}` (uppercase, 1.5px tracked Roboto), option descriptors use `{typography.body-sm}`. The lavender accent (`{colors.accent}`) marks the selected option — either as an active-state border or a filled ink-dot indicator. This panel appears as a side rail on desktop PDP pages and collapses to a full-width accordion on mobile.

### Monogram Display

**`monogram-display`** — A canvas-background live-preview panel (`{colors.canvas}`) rendering customer initials in `{typography.display-sm}` Whyte-Regular at scale. A thin `{colors.hairline-soft}` border frames the panel; no rounding, no shadow. As the customer types in the configurator, the initials update in real time. The square frame and light typeface weight produce a facsimile of how letterpress or engraved initials appear on cotton stock.

### Search

**`search-bar`** — A 48px square-cornered input (`{rounded.none}`) on `{colors.canvas}`, with `{colors.muted}` icon and placeholder. Border steps from `{colors.hairline}` to `{colors.ink}` on focus, providing a clear active state without color-family deviation. Appears in top-nav overlay on desktop and as a full-width inline element on category browse pages at mobile.

### Footer

**`footer`** — A full-width deep-navy block (`{colors.ink}`) with three to four link columns set in `{typography.nav-link}` at `{colors.on-dark}`. Column headings use `{typography.label}` (uppercase, tracked). A `{colors.body-alt}` (#404040) hairline divides the link grid from the copyright and legal row below. Padding of `{spacing.section}` top and bottom provides room proportional to the brand's editorial page density.

### Breadcrumb

**`breadcrumb`** — A single-line path in `{typography.caption}` with inactive ancestors at `{colors.muted}` and the current page in `{colors.ink}`. Forward-slash separators render in `{colors.hairline-soft}` for minimal visual weight. Placed directly below the nav bar on collection and product detail pages.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero titles drop to display-sm (24px); nav collapses to hamburger drawer; personalization panel stacks full-width below product image as accordion; collection-banner padding reduces to spacing.lg |
| Tablet | 744–1128px | Two-column product grid; hero min-height reduces to 400px; nav shows abbreviated category labels without subcategory flyouts; promo-banner text truncates to single line |
| Desktop | 1128–1440px | Three-column product grid; full nav category row with flyout submenus; hero at full 600px min-height; personalization panel appears as fixed side rail beside product imagery |
| Wide | > 1440px | Content max-width 1440px centered with auto side margins; four-column product grid; hero display-xl at full 56px; section gaps expand proportionally |

### Touch Targets
- All buttons are 48px minimum height; icon-only controls (hamburger, search, bag icon) are 44×44px minimum tap area
- Monogram configurator letter selectors and ink-color pickers are at least 40×40px with 8px gutter
- Breadcrumb links maintain 40px tap-target height via vertical padding compensation
- Personalization accordion trigger rows are 48px tall on mobile

### Collapsing Strategy
- Primary nav collapses at 744px to a slide-in drawer revealing the full category tree with expand/collapse sub-levels
- Horizontal collection tab rows scroll natively on touch rather than wrapping to a second line
- Footer grid collapses from four columns to two at tablet, to a single stacked column at mobile with each heading acting as an expand toggle
- Hero CTAs stack vertically below 480px when two buttons appear side by side on desktop
- Promo banner condenses to a marquee ticker on screens below 480px to avoid text truncation

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Pure white (#ffffff) is absent from the extracted palette; `on-primary` is assumed as #ffffff for text-on-button contrast — verify against live CTA states
- The precise role of #ccb7ff (accent lavender) vs. #3d5789 (slate blue) in the interactive hierarchy could not be confirmed from extraction; dark navy (#0f172b) is used as primary button fill based on heritage-brand convention, but the brand may use slate blue as the default CTA
- No hover, focus-ring, or transition timing values were extractable; focus states are interpolated to `{colors.ink}` borders
- Whyte-Regular weight variants (Light 300, Book 400, Medium 500) were not distinguishable from the font-stack string alone; display weights are set at 300 by inference from the typeface's conventional usage
- Custom icon set (envelope glyphs, wax-seal motifs, monogram frame assets) is not characterized
- Exact grid gutter widths and column counts for the product listing page were not extractable
- Animation or scroll-behavior patterns (parallax on hero, fade-in on cards) could not be confirmed
- Whether the dark nav bar is always persistent or only on the homepage could not be determined from extraction alone
