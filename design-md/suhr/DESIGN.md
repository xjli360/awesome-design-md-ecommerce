---
version: alpha
name: "Suhr"
source_url: "https://www.suhr.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Guitar-builder precision announces itself in the color logic before a single product image loads: a near-monochrome scaffold running from #111111 to #444444 carries the page structure, then a high-voltage CTA blue (#2ea3f2) interrupts like the power LED on a rack unit — minimal, functional, unmissable. Suhr's Open Sans stack carries all reading text at restrained weights; no custom display face, no gestural letterforms. The typographic restraint mirrors a manufacturing floor where finish quality does the talking. Deeper-water blues (#006799, #007fd1) handle hover states and link hierarchies within the same temperature band, while an electric violet (#c600ff) appears in sparing editorial contexts — a color with enough voltage to stop a scroll without demanding permanence across the whole system. Surfaces hold to the light-gray band (#fafafa, #f4f4f4) for page fields, #eeeeee for section dividers, while the muted blue-gray #bcc8c9 surfaces in form inputs and secondary UI chrome, lending the digital shell a machined-metal quality that flat white lacks. The overall impression is a premium instrument catalog designed to let photography do the emotional work: dark-gradient hero sections behind guitar bodies, full-bleed portrait shots, color-matched finish thumbnails. Buttons and inputs sit at `{rounded.xs}` — close to square — because consumer-soft radii would undercut the precision-build story Suhr has maintained since its Santa Cruz workshop days. The site runs on a WordPress/Divi framework (ETmodules icon font in evidence), so layout follows a 12-column grid with section-padding units in the 60–80px range. Navigation is hierarchical: Guitars → Series → Model → Configuration, with tonewoods, finish, and pickup selections rendered as visual swatches in the deepest decision layer. Custom-shop pages break the catalog grid deliberately — full-width timber shots and hand-written finish names signal that these instruments exist outside normal product logic.

colors:
  primary: "#2ea3f2"
  primary-active: "#007fd1"
  primary-dark: "#006799"
  primary-disabled: "#8ed1fc"
  accent-violet: "#c600ff"
  ink: "#111111"
  body: "#222222"
  muted: "#444444"
  muted-soft: "#555555"
  dark-mid: "#3e3e3e"
  hairline: "#d9d9d9"
  hairline-soft: "#eeeeee"
  canvas: "#ffffff"
  surface-soft: "#fafafa"
  surface-card: "#f4f4f4"
  surface-mid: "#eeeeee"
  metal: "#bcc8c9"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  scrim: "#111111"

typography:
  display-xl:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-label:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 0.6px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  series-badge:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1
    letterSpacing: 1.5px
    textTransform: uppercase
  mono:
    fontFamily: "Consolas, 'Courier New', Menlo, monaco, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
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
    padding: 12px 28px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-ghost-dark:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 27px
    height: 44px
    border: "1px solid {colors.on-dark}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.primary}"
  text-input-metal:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.metal}"
    padding: 10px 14px
    height: 44px
    focusBorder: "1px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 70px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 70px
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    imageAspect: "3/4"
    padding: "{spacing.base}"
    titleTypography: "{typography.title-sm}"
    titleColor: "{colors.ink}"
    subtitleTypography: "{typography.body-sm}"
    subtitleColor: "{colors.muted}"
    ctaTypography: "{typography.button-sm}"
    ctaColor: "{colors.primary}"
  hero:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    subtitleTypography: "{typography.body-md}"
    minHeight: 600px
    paddingV: "{spacing.section}"
    paddingH: "{spacing.xl}"
    overlayColor: "{colors.scrim}"
    overlayOpacity: 0.5
  series-section:
    backgroundColor: "{colors.surface-soft}"
    titleTypography: "{typography.display-md}"
    titleColor: "{colors.ink}"
    paddingV: "{spacing.section}"
  series-badge:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.series-badge}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  accent-badge:
    backgroundColor: "{colors.accent-violet}"
    textColor: "{colors.on-primary}"
    typography: "{typography.series-badge}"
    rounded: "{rounded.none}"
    padding: "4px 10px"
  color-swatch:
    size: 28px
    rounded: "{rounded.full}"
    border: "2px solid transparent"
    selectedBorder: "2px solid {colors.primary}"
    gap: "{spacing.xs}"
    hitArea: 44px
  guitar-configurator:
    backgroundColor: "{colors.canvas}"
    sectionBorder: "1px solid {colors.hairline}"
    labelTypography: "{typography.caption-label}"
    labelColor: "{colors.muted}"
    valueTypography: "{typography.body-md}"
    valueColor: "{colors.ink}"
    padding: "{spacing.lg}"
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    activeColor: "{colors.body}"
    separator: "/"
    gap: "{spacing.sm}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "10px 14px"
    iconColor: "{colors.muted}"
    focusBorder: "1px solid {colors.primary}"
  dealer-map:
    backgroundColor: "{colors.surface-card}"
    borderColor: "{colors.hairline}"
    rounded: "{rounded.xs}"
    pinColor: "{colors.primary}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.body}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.metal}"
    linkHoverColor: "{colors.primary}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.caption-label}"
    paddingV: "{spacing.section}"
    dividerColor: "{colors.dark-mid}"

## Components

### Buttons

**`button-primary`** — #2ea3f2 fill, white text, `{typography.button-md}` (uppercase, 14px, 700, 0.6px tracking), `{rounded.xs}`, 44px tall with 12px/28px padding. The uppercase treatment and near-square corners position these closer to a spec sheet than a marketplace; hover darkens the fill to `{colors.primary-active}` (#007fd1), disabled bleaches to `{colors.primary-disabled}` (#8ed1fc) with the text remaining white. This is the standard CTA across catalog pages — add to cart, request quote, configure.

**`button-secondary`** — White fill, #111111 text, 1px `{colors.hairline}` border, same geometry and typography as primary. Used for secondary actions alongside a primary CTA: "Find a Dealer", "Compare Models", "Download Specs". The border provides definition on white page surfaces without introducing a second color.

**`button-ghost-dark`** — Transparent fill with 1px solid white border and white text; reserved for hero sections and dark marketing banners where `button-primary`'s blue would disappear against the dark overlay. Same `{typography.button-md}` and `{rounded.xs}` treatment.

### Navigation

**`nav-bar`** — 70px tall white bar with a 1px `{colors.hairline}` bottom border. Open Sans 14px/600 nav links with standard hover underline or color shift to `{colors.primary}`. Logo anchors left; primary navigation items (Guitars, Amps, Pickups, Support, Dealers) run left-justified or centered; account/cart icons sit right. On hero-led pages, `nav-bar-dark` inverts to `{colors.ink}` background with `{colors.on-dark}` text for seamless bleed into full-coverage imagery.

### Product Cards

**`product-card`** — #f4f4f4 card surface at `{rounded.xs}` with a 3:4 portrait image area (guitar-body orientation). Model name renders in `{typography.title-sm}`, category or series label in `{typography.body-sm}` at `{colors.muted}`, and a text CTA link in `{typography.button-sm}` at `{colors.primary}`. Cards organize in 4-column grids on wide desktop, 3-column on desktop, 2-column on tablet, single column on mobile. No drop shadows — the surface-card background provides enough separation on the page.

### Hero

**`hero`** — Full-bleed dark section, minimum 600px tall. A `{colors.scrim}` overlay at 50% opacity sits between the background photograph and content, keeping text legible regardless of image brightness. Title at `{typography.display-xl}` in white, supporting body copy at `{typography.body-md}` in white, CTA uses `button-ghost-dark`. Padding is `{spacing.section}` vertical and `{spacing.xl}` horizontal. Product launch heroes may run at 100vh; standard homepage heroes hold at 600–700px.

### Series Badges

**`series-badge`** — Zero-radius label (a strict rectangle at `{rounded.none}`) with `{colors.ink}` background, white text, and `{typography.series-badge}` (10px, 700, uppercase, 1.5px tracking). Sits top-left on product cards and at the opening of model detail pages to declare the product line — Standard, Pro, Classic, Custom. `accent-badge` swaps the fill to `{colors.accent-violet}` (#c600ff) for new-release, limited-run, or artist-model flagging where a visual interrupt is warranted.

### Guitar Configurator

**`guitar-configurator`** — The deepest UI layer for both standard and custom-shop models. White background with `{colors.hairline}` section dividers; specification row labels in `{typography.caption-label}` (uppercase, #444444), selected values in `{typography.body-md}` (#111111). Finish and color options render as `color-swatch` circles — 28px visual diameter, `{rounded.full}`, with a 2px `{colors.primary}` border on the active selection. Tonewood and pickup options use labeled tab groups or `text-input-metal` dropdowns. On desktop the configurator occupies a 2-column layout (image left, spec panel right); on mobile it stacks into an accordion with one section open at a time.

### Color Swatches

**`color-swatch`** — 28px circles at `{rounded.full}` with a 2px transparent border default and a 2px `{colors.primary}` border on selected state. Touch hit area expands to 44px to meet minimum targets. Swatches space at `{spacing.xs}` and wrap to a second row when the finish count exceeds the container width. Used in the configurator, product-listing filter panels, and finish gallery overlays.

### Search

**`search-bar`** — `{colors.surface-soft}` background, 1px `{colors.hairline}` border, `{rounded.xs}`, with a muted gray search icon (ETmodules glyph) left-aligned inside the field. `{typography.body-md}` for placeholder and input text. Focus replaces the border with `{colors.primary}` blue at 1px. Appears in the header utility tray on all pages and as a full-width block on the Dealer Locator and Support pages.

### Dealer Map

**`dealer-map`** — Card container at `{rounded.xs}` with `{colors.surface-card}` background and `{colors.hairline}` border wraps an embedded map (Google Maps or similar). Map pins inherit `{colors.primary}` blue. Dealer name and city labels beneath each list result render in `{typography.body-sm}` at `{colors.body}`. The locator page uses a split-panel layout: map fills the right two-thirds, scrollable dealer list fills the left third on desktop.

### Footer

**`footer`** — Full-width `{colors.ink}` (#111111) background. Column headings in `{typography.caption-label}` (uppercase, white). Body links in `{colors.metal}` (#bcc8c9) — the machined-gray tone acts as the default link state here, reserving the blue for hover. Hovering any footer link shifts to `{colors.primary}` (#2ea3f2). Social icons, warranty/legal links, newsletter sign-up form (inheriting `text-input` styling on a dark surface), and dealer program information all live in this zone.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hamburger drawer nav; hero title drops to `{typography.display-md}`; configurator panels stack into accordion; color-swatch row wraps freely |
| Tablet | 744–1128px | 2-column product grid; nav may condense to abbreviated labels or flyout; hero padding reduces to `{spacing.xl}`; series sections shift to 2-up layout |
| Desktop | 1128–1440px | 3–4-column product grids; full horizontal nav at `{typography.nav-link}`; hero at `{typography.display-xl}`; configurator in 2-column label/control layout |
| Wide | > 1440px | Content centers in ~1280px max-width container; hero imagery scales to fill viewport; section padding increases proportionally |

### Touch Targets

- All buttons and nav links: minimum 44px height
- Color swatches: 28px visual, 44×44px tap target
- Mobile nav drawer items: 48px minimum row height
- Form inputs: 44px height minimum
- Footer links: minimum 44px vertical spacing on mobile

### Collapsing Strategy

- Primary nav collapses to hamburger drawer below 744px; drawer opens left-to-right with a dark scrim overlay
- Product grids reduce from 4-col → 3-col → 2-col → 1-col across breakpoints
- Hero CTAs remain full-width on mobile; font size scales down approximately 20% from desktop
- Guitar configurator becomes a stacked accordion on mobile — Body, Neck, Electronics, Finish sections collapse independently
- Footer columns collapse to accordion pattern on mobile with `{colors.hairline}` dividers between sections
- Breadcrumb truncates to show only parent and current page on mobile with an ellipsis intermediary

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Several extracted colors (#cf2e2e, #ff6900, #fcb900, #7bdcb5, #00d084, #8ed1fc, #0693e3, #9b51e0, #f78da7) match the standard WordPress Gutenberg block-editor palette exactly and almost certainly do not represent the Suhr brand palette — excluded from the design system
- ETmodules font confirms a Divi/Elegant Themes framework; the actual icon glyph catalog and navigation icon assignments are not extractable from page metadata alone
- No custom brand display typeface was detected; Open Sans appears to be the Divi default — Suhr may use a proprietary or licensed display face in print, packaging, or headstock decals that does not load on the web
- Primary blue (#2ea3f2) may be a Divi theme default rather than a deliberate brand selection; the true brand primary should be verified against the Suhr brand guide or by inspecting site CSS variables directly
- #c600ff (electric violet) usage context could not be confirmed — it appears in extraction but its role (editorial accent, block-editor color, or promotional badge) is uncertain
- Dark-mode treatment is unknown; the extracted palette includes a full dark range but no dark-mode toggle was detected in page metadata
- Motion and animation data are not extractable; Divi section transitions, parallax intensity, and hover animation durations are unknown
- Product photography treatment (backdrop color, lighting temperature, background gradient specifics) could not be reliably inferred from metadata alone
