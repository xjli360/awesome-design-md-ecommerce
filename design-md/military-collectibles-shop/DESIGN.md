---
version: alpha
name: "Military Collectibles Shop"
source_url: "https://militarycollectorshq.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Special Elite — a typewriter face whose ink-bleed edges evoke field-stamped orders and wartime correspondence — sets the register before a single image loads: this is a shop where provenance matters more than polish. The meta theme color #537353, an olive drab pulled straight from military field manuals and equipment stencils, functions as both primary CTA surface and navigation ground, lending the site an immediate institutional weight that a generic retail palette never could. Yeseva One provides editorial contrast in secondary display roles, its high-contrast serifs reading like a museum acquisition placard rather than a storefront sign. Open Sans carries body copy at comfortable weights, bridging the historical display atmosphere with functional legibility for catalog descriptions, condition notes, and provenance text.

  The palette is deliberately narrow: #537353 olive anchors authority, #ff0000 marks urgency on featured or sale inventory, and #ffff00 surfaces in tight accent moments — a price callout, a rare-find indicator — rather than as ambient decoration. The canvas reads as aged parchment (#f7f3e9) rather than clinical white, reinforcing the collectible context without resorting to faux-sepia filters. Cards sit on a slightly warmer surface (#faf7f0) to lift inventory cleanly from the background. Corner radii stay conservative throughout — {rounded.xs} to {rounded.sm} — because hard-edged industrial geometry suits relics and regalia better than the friendly pill shapes of a lifestyle brand. Monospace type appears in catalog-code and serial-number contexts, lending archival specificity that signals authentication consciousness to serious collectors. Social platform colors (#1877f2 Facebook, #e1306c Instagram) appear only as footer icon tints — they are not brand vocabulary. Condition grades — Good, Very Good, Excellent, Mint — surface as muted capsule badges using {colors.surface-soft}, letting the olive primary carry selective weight rather than competing with condition signals across every product card.

colors:
  primary: "#537353"
  primary-active: "#3d5a3d"
  primary-disabled: "#8da88d"
  accent-red: "#ff0000"
  accent-yellow: "#ffff00"
  social-facebook: "#1877f2"
  social-instagram: "#e1306c"
  ink: "#1c1c14"
  body: "#2e2e20"
  muted: "#5a5a48"
  hairline: "#c8c4b0"
  canvas: "#f7f3e9"
  surface-soft: "#ede9da"
  surface-card: "#faf7f0"
  on-primary: "#ffffff"
  on-dark: "#ffffff"

typography:
  display-xl:
    fontFamily: "'Special Elite', 'Courier New', monospace"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0.5px
  display-md:
    fontFamily: "'Special Elite', 'Courier New', monospace"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.3px
  display-sm:
    fontFamily: "'Yeseva One', Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Special Elite', 'Courier New', monospace"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
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
  badge:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Open Sans', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  price-display:
    fontFamily: "'Yeseva One', Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0
  mono-label:
    fontFamily: "'Courier New', Courier, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px

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
    border: none
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.xs}"
    padding: 11px 23px
    height: 44px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 10px 14px
    border: "1px solid {colors.hairline}"
    borderFocus: "1px solid {colors.primary}"
    placeholderColor: "{colors.muted}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 60px
    padding: "0 {spacing.lg}"
  nav-bar-utility:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 36px
    padding: "0 {spacing.lg}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.md}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    conditionTypography: "{typography.badge}"
    textColor: "{colors.ink}"
    mutedColor: "{colors.muted}"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaBackground: "{colors.primary}"
    ctaColor: "{colors.on-primary}"
    ctaTypography: "{typography.button-md}"
    ctaRounded: "{rounded.xs}"
    minHeight: 480px
    padding: "{spacing.section}"
    overlayOpacity: 0.55
  era-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  condition-badge:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
    border: "1px solid {colors.hairline}"
  featured-badge:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    submitBackground: "{colors.primary}"
    submitColor: "{colors.on-primary}"
    height: 44px
  category-card:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    titleTypography: "{typography.display-sm}"
    rounded: "{rounded.xs}"
    overlayGradient: "linear-gradient(to top, rgba(28,28,20,0.85) 0%, transparent 60%)"
    minHeight: 220px
  breadcrumb:
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
  catalog-code:
    typography: "{typography.mono-label}"
    textColor: "{colors.muted}"
    backgroundColor: "{colors.surface-soft}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  price-tag:
    textColor: "{colors.ink}"
    typography: "{typography.price-display}"
    saleColor: "{colors.accent-red}"
    strikethroughColor: "{colors.muted}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
    facebookIconColor: "{colors.social-facebook}"
    instagramIconColor: "{colors.social-instagram}"

## Components

### Buttons
**`button-primary`** — Olive drab #537353 fill with white uppercase Open Sans at 15px/600 weight, 4px corner radius ({rounded.xs}), 44px tall. The tight radius and uppercase letter-spacing reinforce a military-regulation formality; this is not a rounded consumer CTA. Active state deepens to #3d5a3d; disabled desaturates to the muted sage #8da88d.

**`button-secondary`** — Parchment canvas fill with olive text and a 1px olive border matching the primary's dimensions and radius. Used for secondary catalog actions — "Save to Wishlist," "Ask a Question," "View More Photos" — without competing with the primary add-to-cart CTA.

**`button-ghost`** — Transparent background with {colors.hairline} border and ink text. Applied to tertiary actions such as filter toggles, sort menus, and pagination controls. Shares uppercase button-md typography but carries the least visual weight.

### Navigation
**`nav-bar`** — Solid olive #537353 at 60px height, white uppercase Open Sans nav links. A secondary `nav-bar-utility` strip in near-black #1c1c14 sits above, hosting account links, cart icon, and shipping-notice copy at caption scale. This double-bar structure separates shop navigation from utility actions, a treatment common in specialty collectibles and coin shops that carry large SKU catalogs.

### Product Cards
**`product-card`** — Parchment surface (#faf7f0) with a 1px hairline border and 4px radius. Image region uses a 4:3 aspect ratio suited to flat-lay photography of medals, patches, and documents. Title uses Special Elite at 18px for period register; price uses Yeseva One serif at 24px. Era badges float top-left over the image; condition badges float bottom-left.

### Hero
**`hero-banner`** — Near-black base (#1c1c14) with a photographic full-bleed background at 55% overlay opacity, 40px Special Elite headline, Open Sans body copy, and a primary olive CTA. Minimum 480px height. Padding at {spacing.section} (64px) gives the panel museum-hall scale. Photography subjects are typically period military equipment, uniforms, or wartime scenes.

### Badges
**`era-badge`** — Olive fill, white uppercase 11px badge type, 4px radius. Applied to product cards to label historical era: WWII, Korean War, Civil War, Vietnam, Cold War, etc. Functions as the primary category signal on the card face.

**`condition-badge`** — Soft parchment fill ({colors.surface-soft}) with muted text and hairline border. Values run from Poor through Mint. Intentionally low-contrast so condition notation does not visually dominate the item photography.

**`featured-badge`** — Red (#ff0000) fill, white text. The one hot-voltage accent in an otherwise muted olive-and-parchment palette. Reserved strictly for "Featured" or sale callouts to preserve its attention signal.

### Search
**`search-bar`** — Parchment canvas input with hairline border and a 44px target height. Submit button carries olive fill matching the primary. Designed to appear both inline in the nav strip and as a full-width block at the top of collection and search result pages.

### Category Cards
**`category-card`** — Dark-base image cards with a bottom-to-top gradient overlay revealing Yeseva One display-sm titles at the bottom edge. A grid of 4–6 cards organizes inventory by conflict theater, branch of service, or item type. 220px minimum height keeps the label legible without cropping photography.

### Catalog Code
**`catalog-code`** — Courier New monospace at 12px on a {colors.surface-soft} pill, 2px/6px padding, 4px radius. Applied inline beside SKUs, lot numbers, and authentication identifiers. The typewriter cadence of the mono type echoes Special Elite headlines while marking the field as machine-readable data rather than editorial copy.

### Footer
**`footer`** — Near-black #1c1c14 background with white Open Sans body-sm links arranged in columns by topic: Shop, About, Policies, Contact. Facebook icon tinted #1877f2, Instagram icon tinted #e1306c — the only contexts in which those extracted colors appear. Padded at {spacing.xxl} vertically.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer over olive bar; hero shrinks to 320px minimum height; search becomes full-width bar below nav; breadcrumb truncates to first + current |
| Tablet | 744–1128px | Two-column product grid; double nav bars retained; category cards drop to 2-column grid; hero at 400px; sidebar filters become collapsible top-bar drawer |
| Desktop | 1128–1440px | Three- to four-column product grid; full horizontal nav with dropdowns; hero at 480px; sidebar filters persistent on collection pages |
| Wide | > 1440px | Max content width 1440px centered; four-column product grid; hero background extends full-bleed while content container stays constrained |

### Touch Targets
- All buttons minimum 44px tall, meeting iOS and Android tap-target guidelines
- Nav links padded to 44px hit area vertically including the nav-bar strip
- Entire product card surface is tappable on mobile, not just the title link
- Era and condition badges are display-only on mobile — filter interactions live in a dedicated filter drawer, not the badge chips

### Collapsing Strategy
- Double nav bar collapses to single olive bar on mobile; utility links move into hamburger side-drawer
- Category card grid scales 4 → 2 → 1 column as viewport narrows
- Breadcrumb hides intermediate category steps on mobile, showing only root and current page
- Catalog code renders below the item title on mobile rather than inline to prevent horizontal overflow on narrow screens
- Price and condition information stack vertically on mobile product cards; era badge and featured badge retain position over the image

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No checkout or cart page color tokens extracted; olive primary assumed for cart and checkout CTAs but a distinct accent color may exist
- Exact nav dropdown structure and mega-menu column layout not confirmed; double-bar treatment inferred from the contrast between #537353 and #1c1c14 extractions
- Hover and focus state colors not confirmed beyond primary (#537353) and active (#3d5a3d); hairline-border focus rings assumed for accessibility
- Mobile-specific font-size overrides for display-xl and display-md not confirmed; responsive scaling to ~28px and ~20px on mobile is estimated
- #ffff00 yellow appears in extraction but its exact use context (sale banner text, icon fill, highlight overlay) is unconfirmed; assigned as accent-yellow for callout use only
- Social media colors (#1877f2, #e1306c) appear to originate from embedded social icon SVGs rather than intentional design tokens; treated as icon-only tints in footer
- Yeseva One fallback rendering on Windows systems without a strong geometric serif alternative may shift display heading appearance
- No confirmed animation or transition tokens; standard 200ms ease-in-out assumed for hover and open/close states
