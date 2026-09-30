---
version: alpha
name: "Black Crows"
source_url: "https://www.blackcrows.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Electric cyan (#00b3ff) punches through a near-black field (#121212) the way a racer's line cuts untracked slope — Black Crows concentrates its entire interactive vocabulary into that single voltage, running navigation hovers, add-to-cart events, and active filter chips all through one hue without variation. The proprietary typefaces are named with the same economy as the skis: BC-bold and BC-normal, two weights, no optical-size variants, no ornamental cuts. Both run at tight leading over wide hero headers, letting full-bleed mountain photography carry the emotional weight while type supplies precision rather than drama. The foundational palette reads as mountain shadow: deep blue-gray (#4a5764) serves as both compositional tone and secondary text color, near-black (#121212) reserved for maximum-contrast headers and body copy, and cool gray (#c1c9d1) occupying disabled states and ghost borders — one muted step between live UI and field. Surface corners are sharply angular; the brand tolerates almost nothing above {rounded.sm} on interactive elements. Product cards bleed imagery to the full frame boundary, and technical specification panels appear directly below hero photography on product pages rather than collapsed behind accordion tabs, treating engineering data as brand voice. The thin hairline (#dedede) draws every row separator, input border, and navigation edge; structural density is the design value because a buyer comparing twelve ski models across eight parameters does not want decorative breathing room between specification rows. The dark-mode footer mirrors the hero: #121212 ground, on-dark type, with cyan (#00b3ff) appearing on link hovers as the sole luminous signal in an otherwise compressed, high-contrast system.

colors:
  primary: "#00b3ff"
  primary-active: "#0099dd"
  primary-disabled: "#80d9ff"
  brand-slate: "#4a5764"
  brand-slate-active: "#3a4654"
  ink: "#121212"
  body: "#4a5764"
  muted: "#c1c9d1"
  hairline: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#f4f6f7"
  surface-card: "#ffffff"
  surface-dark: "#121212"
  on-primary: "#121212"
  on-dark: "#ffffff"
  scrim: "rgba(0,0,0,0.5)"

typography:
  display-xl:
    fontFamily: "'BC-bold', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display-md:
    fontFamily: "'BC-bold', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-sm:
    fontFamily: "'BC-bold', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: -0.25px
  title-md:
    fontFamily: "'BC-normal', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'BC-normal', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'BC-normal', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'BC-normal', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'BC-normal', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  overline:
    fontFamily: "'BC-bold', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 1.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'BC-bold', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.14
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'BC-bold', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.17
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'BC-normal', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0
  price:
    fontFamily: "'BC-bold', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  spec-label:
    fontFamily: "'BC-normal', 'Avenir Next', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 0.75px
    textTransform: uppercase

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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.ink}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 14px
    height: 44px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoColor: "{colors.ink}"
    hoverTextColor: "{colors.primary}"
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: none
    logoColor: "{colors.on-dark}"
    hoverTextColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    imageFit: cover
    imageAspect: "3/4"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price}"
    subtitleTypography: "{typography.body-sm}"
    padding: "{spacing.base}"
    border: none
    hoverShadow: "0 4px 16px rgba(0,0,0,0.12)"
  hero-banner:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 80vh
    imageFit: cover
    overlayColor: "rgba(18,18,18,0.35)"
    primaryCtaBackground: "{colors.primary}"
    primaryCtaTextColor: "{colors.on-primary}"
    ghostCtaBorder: "1px solid {colors.on-dark}"
    ghostCtaTextColor: "{colors.on-dark}"
    padding: 64px 64px
  ski-spec-badge:
    backgroundColor: "{colors.brand-slate}"
    textColor: "{colors.on-dark}"
    typography: "{typography.overline}"
    rounded: "{rounded.none}"
    padding: 4px 8px
  spec-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.body-sm}"
    borderBottom: "1px solid {colors.hairline}"
    padding: 12px 0
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    border: "1px solid {colors.hairline}"
    selectedBorder: "1px solid {colors.ink}"
    selectedBackground: "{colors.ink}"
    selectedTextColor: "{colors.on-dark}"
    height: 40px
    width: 40px
  color-swatch:
    rounded: "{rounded.full}"
    height: 20px
    width: 20px
    selectedRing: "2px solid {colors.ink}"
    selectedRingOffset: 2px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    height: 44px
    padding: 0 16px
    border: none
    iconColor: "{colors.muted}"
    activeIconColor: "{colors.primary}"
  collection-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.overline}"
    borderBottom: "1px solid {colors.hairline}"
    height: 48px
    itemPadding: 0 24px
    activeTextColor: "{colors.primary}"
    activeBorderBottom: "2px solid {colors.primary}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted}"
    activeTextColor: "{colors.ink}"
  product-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.overline}"
    rounded: "{rounded.none}"
    padding: 3px 6px
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.overline}"
    headingColor: "{colors.muted}"
    linkHoverColor: "{colors.primary}"
    borderTop: none
    padding: 48px 0

## Components

### Buttons
**`button-primary`** — Fully square-cornered ({rounded.none}), electric-cyan fill (#00b3ff) with near-black text (#121212) for maximum contrast; the uppercase BC-bold label at 14px with 0.5px letter-spacing reads as a structural directive, not decoration. On hover the fill transitions to `primary-active` (#0099dd); on disable the fill washes to pale cyan (#80d9ff) and the label shifts to muted, removing the button from the visual hierarchy without hiding it entirely.

**`button-secondary`** — White canvas fill, 1px near-black border, near-black uppercase label — the mirror negative of the primary. Used for secondary CTAs such as "view details," size-chart links, and compare actions. Hover brightens the background to `surface-soft` (#f4f6f7) while the border holds its weight.

**`button-ghost`** — Transparent fill with a 1px white border and white uppercase label, appearing exclusively over dark or photographic backgrounds: hero overlays, dark-mode drawers, full-bleed campaign panels. Never rendered on a light canvas surface.

### Navigation
**`nav-bar`** — 64px tall, white canvas background with a single hairline bottom border (#dedede). The Black Crows wordmark anchors the left; category labels (Skis, Outerwear, Equipment, Accessories) render in nav-link weight (600, 14px) and turn cyan (#00b3ff) on hover with no transition delay — the cyan appears as a pure state change, not a fade. Cart, search icon, and region selector lock to the right edge. A dark variant (`nav-bar-dark`) swaps to #121212 ground for pages where the hero image runs under the nav bar.

**`collection-strip`** — A 48px-tall horizontal sub-nav strip mounted immediately below the primary nav on category and series pages. Tab labels use overline type (BC-bold, 11px, 1.5px tracking, uppercase). The active tab gains a 2px solid cyan bottom border and its label color shifts to `primary`. This strip is the dominant navigation layer within a product family — ski series, outerwear collections — and is not present on the home page.

### Product Card
**`product-card`** — No border, no shadow at rest, square corners, full 3:4 imagery bled to the card boundary. Title in title-md (BC-normal 600, 18px); price in price scale (BC-bold 700, 20px); category or terrain tag in caption below. A 4px lift shadow (0 4px 16px rgba(0,0,0,0.12)) appears on hover. A `product-badge` can occupy the top-left corner for NEW or SALE states. Second colorway imagery may cross-fade on hover; no carousel widget appears within the card.

### Hero Banner
**`hero-banner`** — Full-bleed photographic panel at 80vh minimum height, dark scrim at 35% opacity concentrated in the lower two-thirds so the mountain horizon reads clearly. Display-xl type (BC-bold, 64px, –1px tracking) runs left-aligned in on-dark white. A cyan-fill primary CTA and a white-border ghost CTA sit side-by-side beneath the headline with {spacing.sm} gap between them. On mobile the minimum height drops to 60vh and the headline scales to display-sm (28px); CTAs stack to full-width.

### Technical Specs
**`ski-spec-badge`** — Small rectangular chip in brand-slate (#4a5764) with on-dark text in overline scale. Used to label a single engineering characteristic — ROCKER, CAMBER, EARLY RISE, ABS — at the top of a product's spec section. Square corners only; no rounded treatment at any size.

**`spec-row`** — Full-width rows with a left-column overline label in spec-label scale (11px, uppercase, 0.75px tracking, muted tone) and a right-column value in body-sm. A single hairline (#dedede) divides each row below. The complete specification table — waist width, tip width, tail width, turning radius, weight, recommended skiing level — is exposed at full height on desktop product pages without progressive disclosure.

### Size and Color Selectors
**`size-selector`** — 40×40px square tiles with hairline border at rest. Selected state: ink fill (#121212), on-dark text, ink border. Unavailable sizes display a diagonal muted strike-through and are non-interactive but remain visible. No rounded corners at any state. On mobile the tiles expand to 48px to meet touch target requirements.

**`color-swatch`** — 20px circular chips ({rounded.full}) in a horizontal row directly below the size selector. The selected chip gains a 2px ink-colored ring with a 2px transparent gap between ring and chip, creating a clear selection halo without increasing chip diameter. Unselected chips have no border.

### Search
**`search-bar`** — Borderless field on `surface-soft` (#f4f6f7) ground, square-cornered, 44px tall. A magnifier icon renders in muted gray (#c1c9d1) at rest and shifts to cyan (#00b3ff) on focus — the only animated color shift in the input system. On mobile, activating the icon expands a full-screen overlay: #121212 ground, a canvas-colored input at the top, and a recent-searches list in body-sm below.

### Footer
**`footer`** — #121212 ground with on-dark body text; no top border since the dark field contrast serves as the visual separator from the page body. Section headings in overline scale, color muted (#c1c9d1). Link hover color is cyan (#00b3ff), maintaining the hover convention established in the nav bar. The four-column desktop layout collapses to a stacked accordion on mobile, with each heading acting as the disclosure trigger.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero shrinks to 60vh, headline scales to display-sm (28px); collection-strip becomes momentum-scrollable horizontal row; footer columns collapse to disclosure accordion; CTA buttons stack full-width; size tiles expand to 48px |
| Tablet | 744–1128px | Two-column product grid; primary nav retains full labels but collection-strip collapses to horizontal scroll; hero headline at display-md (40px); spec table at full column count |
| Desktop | 1128–1440px | Three- or four-column product grid; full nav-bar with collection-strip below; hero at display-xl (64px); spec-badge row appears inline alongside hero imagery; side-by-side CTAs |
| Wide | > 1440px | Content max-width capped at 1440px, centered; side gutters fill with canvas or surface-dark depending on section background; no content reflows beyond desktop breakpoint |

### Touch Targets
- All interactive controls minimum 44×44px on mobile (buttons, size-selector tiles, nav icons padded to 44px via transparent hit-area expansion)
- Color swatches expand from 20px visual size to 44px touch target via transparent padding; visual chip size does not change
- Collection-strip tabs maintain a 48px minimum height on all viewports for reliable thumb reach
- Search icon receives a 44×44px touch region regardless of icon rendering size

### Collapsing Strategy
- **Nav bar**: Full horizontal label menu on desktop and tablet → hamburger drawer on mobile; drawer uses #121212 background with on-dark labels and cyan hover
- **Collection strip**: Horizontal scrolling tab row at all viewports; tabs never wrap to a second line — overflow scrolls with momentum
- **Product grid**: 4-col (wide) → 3-col (desktop) → 2-col (tablet) → 1-col (mobile)
- **Spec table**: Remains fully expanded at all viewports; horizontal scroll applied if a value column overflows on narrow screens
- **Footer columns**: 4-col (desktop/wide) → 2-col (tablet) → single-column accordion (mobile)
- **Hero CTAs**: Side-by-side with {spacing.sm} gap on desktop/tablet → stacked full-width with {spacing.sm} vertical gap on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; system chrome color on mobile browsers (address bar, status bar) cannot be confirmed
- `surface-soft` (#f4f6f7) is inferred rather than extracted; the site may use pure white (#ffffff) for all light surfaces
- Exact font metrics for BC-bold and BC-normal (x-height, cap-height, baseline grid unit) are unavailable without font-file inspection; line-height and letter-spacing values are approximated from visual pattern
- Precise border-radius values, if any exist on the live site, could not be confirmed; the sharp-corner assumption is inferred from brand aesthetic and sport-category norms
- Animation timing functions (hover transition duration, easing curves, page-transition choreography) not captured in extraction
- Custom icon set style (outlined vs. filled, stroke weight, pixel grid) not confirmed from extraction
- Exact grid gutter widths and column counts not extracted; values follow common Shopify theme defaults
- Whether `primary-active`, `primary-disabled`, and `brand-slate-active` match production color values; they are mathematically derived from extracted hues
- Sticky nav scroll behavior (transparent-overlay-to-solid transition) not confirmed; nav-bar-dark variant is inferred from common ski-brand convention
- Contrast ratio of #00b3ff on-primary (#121212) passes WCAG AA at ~9.6:1 but white (#ffffff) on #00b3ff would fail; implementations should use on-primary (#121212) for all cyan-background labels
