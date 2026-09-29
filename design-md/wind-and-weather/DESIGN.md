---
version: alpha
name: "Wind & Weather"
source_url: "https://www.windandweather.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Coral at #ff6f61 signals warmth before a word is read — Wind & Weather plants that hue on every primary CTA and promo badge against deep midnight navy (#001f39) that anchors the header bar and hero overlays. Jost, a geometric sans-serif with open circular apertures, runs the full range from 48px display headlines down to 11px uppercase badge labels without requiring a second typeface; its modest stroke contrast suits a brand that photographs kinetic objects — spinning copper weathervanes, cast-iron garden stakes, hand-painted wind spinners — and wants typography to recede gracefully. The palette splits along a warm-cool axis: navy for structural weight, coral for action and urgency, and a three-color status tier (#28bb74 green for availability, #ff9736 amber for low-stock alerts, #d74047 red for out-of-stock) that maps directly to garden-season scarcity cues without over-explaining. Cards sit on a 4/3 image ratio rather than the square default, giving wide outdoor photography room to breathe; an 8px radius softens corners without pushing toward the pill forms that lifestyle brands favor. The bleached canvas (#f5f5f5) grid background keeps product photography the primary content surface — no illustrated pattern layer, no texture overlay, just product against sky. Hairline rules at #e5e5e5 divide sections the way a horizon line divides a landscape: present, structural, never decorative. The dark register lives only in the nav and footer: midnight navy grounds both, reversing type to off-white (#f5f5f5) and surfacing coral only for hover states and CTAs, so the brand reads as an outdoor catalog by day and a coastal storefront after scroll. Spacing grows in even increments up to 64px section breaks, keeping the product grid airy on wide screens where wind spinners and wall medallions need room to register as three-dimensional objects rather than thumbnail icons.

colors:
  primary: "#ff6f61"
  primary-hover: "#e85a50"
  primary-active: "#cc594e"
  primary-disabled: "#ffa9a0"
  brand-navy: "#001f39"
  brand-navy-mid: "#1a354d"
  accent-green: "#28bb74"
  accent-amber: "#ff9736"
  alert-red: "#d74047"
  ink: "#1f1f1f"
  body: "#2b2b2b"
  muted: "#525252"
  muted-soft: "#767676"
  hairline: "#e5e5e5"
  hairline-soft: "#dcdcdc"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-warm: "#ffe2df"
  on-primary: "#ffffff"
  on-dark: "#f5f5f5"
  on-dark-muted: "#bababa"

typography:
  display-xl:
    fontFamily: "'Jost', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Jost', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Jost', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  overline:
    fontFamily: "'Jost', sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1.2px
    textTransform: uppercase
  button-md:
    fontFamily: "'Jost', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  nav-link:
    fontFamily: "'Jost', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price-lg:
    fontFamily: "'Jost', sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  price-sm:
    fontFamily: "'Jost', sans-serif"
    fontSize: 15px
    fontWeight: 500
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
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "1.5px solid {colors.ink}"
    rounded: "{rounded.sm}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    textDecoration: underline
  button-navy:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    placeholderColor: "{colors.muted-soft}"
    focusBorder: "1.5px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 60px
    topBarHeight: 40px
    topBarBackground: "{colors.brand-navy-mid}"
    activeColor: "{colors.primary}"
    iconColor: "{colors.on-dark}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "4/3"
    titleTypography: "{typography.title-sm}"
    priceTypography: "{typography.price-sm}"
    salePriceColor: "{colors.primary}"
    originalPriceColor: "{colors.muted-soft}"
    originalPriceDecoration: line-through
    badgePosition: top-left
    padding: "{spacing.sm}"
    shadow: "0 1px 4px rgba(0,31,57,0.08)"
    hoverShadow: "0 4px 16px rgba(0,31,57,0.14)"
  hero:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark}"
    overlayGradient: "linear-gradient(to right, rgba(0,31,57,0.55) 0%, rgba(0,31,57,0.2) 100%)"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 520px
    padding: "{spacing.section} {spacing.xl}"
    textAlign: left
  category-card:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark}"
    labelTypography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    imageAspectRatio: "1/1"
    overlayGradient: "linear-gradient(to top, rgba(0,31,57,0.75) 0%, transparent 60%)"
    labelPosition: bottom-left
    labelPadding: "{spacing.base}"
    hoverScale: 1.03
    transition: "transform 0.2s ease"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1.5px solid {colors.hairline}"
    padding: "10px 20px 10px 44px"
    height: 44px
    iconColor: "{colors.muted-soft}"
    focusBorder: "1.5px solid {colors.primary}"
    submitButtonBackground: "{colors.primary}"
    submitButtonColor: "{colors.on-primary}"
    submitButtonRounded: "{rounded.full}"
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-new:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-in-stock:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  badge-low-stock:
    backgroundColor: "{colors.accent-amber}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 40px
    textAlign: center
    linkDecoration: underline
  breadcrumb:
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    separatorColor: "{colors.hairline}"
    activeColor: "{colors.ink}"
    spacing: "{spacing.sm}"
  product-price-display:
    priceTypography: "{typography.price-lg}"
    priceColor: "{colors.ink}"
    salePriceColor: "{colors.primary}"
    originalPriceTypography: "{typography.price-sm}"
    originalPriceColor: "{colors.muted-soft}"
    originalPriceDecoration: line-through
  add-to-cart:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    height: 56px
    width: "100%"
    hoverBackground: "{colors.primary-hover}"
    activeBackground: "{colors.primary-active}"
  newsletter-block:
    backgroundColor: "{colors.surface-warm}"
    headlineTypography: "{typography.display-sm}"
    headlineColor: "{colors.ink}"
    bodyTypography: "{typography.body-md}"
    bodyColor: "{colors.muted}"
    rounded: "{rounded.md}"
    padding: "{spacing.xxl}"
    inputBackground: "{colors.canvas}"
    buttonBackground: "{colors.brand-navy}"
    buttonTextColor: "{colors.on-dark}"
    buttonTypography: "{typography.button-md}"
    buttonRounded: "{rounded.sm}"
  footer:
    backgroundColor: "{colors.brand-navy}"
    textColor: "{colors.on-dark-muted}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.on-dark-muted}"
    linkHoverColor: "{colors.primary}"
    dividerColor: "rgba(245,245,245,0.1)"
    padding: "{spacing.section} 0 {spacing.xl}"

## Components

### Buttons

**`button-primary`** — Coral (#ff6f61) fill on an 8px radius block, uppercase Jost at 15px/600 weight with 0.5px tracking. Hover darkens to #e85a50; active press drops to #cc594e. Disabled state uses the pastel blush #ffa9a0, keeping the coral family present while signaling unavailability. Consistent 48px height aligns with `text-input` in checkout and search form rows.

**`button-secondary`** — White fill with a 1.5px #e5e5e5 border, same 8px radius and uppercase Jost as the primary. Hover fills to #f5f5f5 and strengthens the border to #1f1f1f ink. Used for secondary CTAs like "View All" or "See Details" where coral would over-index.

**`button-ghost`** — Transparent background, coral text, underline decoration. Inline use within product descriptions, blog teaser cards, and footer utility links where a bordered block would add too much visual weight.

**`button-navy`** — Midnight navy (#001f39) fill, off-white (#f5f5f5) text, same geometry as `button-primary`. Appears on hero overlays and the newsletter block where coral would conflict with the warm blush (#ffe2df) background.

### Text Input

**`text-input`** — White ground, 1px #e5e5e5 border, 4px radius. On focus, border strengthens to 1.5px coral — the only focus ring in the system that uses primary color. Placeholder text runs at #767676 muted-soft. Height is locked at 48px to pair naturally with button rows in search and checkout.

### Navigation

**`nav-bar`** — Full-bleed midnight navy (#001f39) bar at 60px, with a 40px announcements strip above in slightly lighter #1a354d. Links run in uppercase Jost at 14px/500, tracking at 0.5px, in off-white. The active category link switches to coral (#ff6f61). Cart and account icons are off-white; cart bubble counter uses coral fill with white text. On mobile the nav collapses to a hamburger icon revealing a full-screen navy drawer with 56px-tall link rows.

### Product Card

**`product-card`** — White card, 8px radius, 4/3 image ratio suited to wide garden photography. Title in Jost 16px/600; price in 15px/500. Sale price switches to coral; original price gets line-through in #767676. Sale and "New" badges overlay the image top-left. A subtle navy-tinted shadow (0 1px 4px rgba(0,31,57,0.08)) lifts the card from the #f5f5f5 grid; hover raises to a 0 4px 16px spread, giving the card a lift-off quality appropriate for tangible garden objects.

### Hero

**`hero`** — Midnight navy base with a left-to-right gradient overlay (55% to 20% opacity) letting landscape photography read through while ensuring white headline contrast. Headlines use `display-xl` (48px/700); subheadlines use `display-sm` (24px/600). Text aligns left, primary CTA uses `button-primary`, secondary action uses `button-secondary`. Minimum 520px height; full-width bleed with 64px vertical padding on desktop.

### Category Cards

**`category-card`** — Square image tiles with a bottom-to-midpoint gradient fade (navy at 75% opacity) keeping category labels legible over any photographic background. Labels render in 16px/600 Jost white. On hover the image scales to 1.03 over 0.2s ease, giving a sense of dimensional depth suitable for a catalog of physical objects. Typical labels: Wind Spinners, Wall Art, Garden Stakes, Bird Feeders, Weather Instruments.

### Search Bar

**`search-bar`** — Pill-shaped ({rounded.full}) white field at 44px height with a loupe icon at left padding. Embedded inline in the nav-bar on desktop; expands from an icon tap on mobile. A coral ({colors.primary}) pill button at the right end submits the query. Focus border transitions to coral matching the `text-input` convention, giving the search surface a unified interaction signature.

### Badges

**`badge-sale`** — Coral fill, white uppercase Jost 11px/700, 4px radius, 3px/8px padding. Overlays the product image top-left. **`badge-new`** — Navy fill, same geometry. **`badge-in-stock`** — Green (#28bb74) fill for availability confirmation. **`badge-low-stock`** — Amber (#ff9736) for "Only N Left" signals. The four-badge vocabulary covers every product state within the three-color status tier without introducing new hues.

### Promotional Banner

**`promo-banner`** — Full-width coral strip at 40px, centered 12px/500 Jost caption in white. Used for free shipping thresholds, seasonal sale codes, and limited-time events. A single underlined white link leads to the applicable collection or terms. On mobile the strip grows to 48px to accommodate line wrapping.

### Add to Cart

**`add-to-cart`** — Full-width coral button at 56px height on the product detail page, 4px taller than the standard `button-primary` to emphasize the primary conversion action. Hover and active states mirror the primary button color sequence. Uppercase Jost 15px/600 label. Placed below the price-display block, spanning the full column width.

### Newsletter Block

**`newsletter-block`** — Warm blush ({colors.surface-warm}, #ffe2df) background at full section width, 12px radius, 48px padding. Headline at `display-sm`; body copy at `body-md` in #525252 muted. Email input is white with coral focus border; subscribe button uses navy fill (`button-navy`) rather than coral to avoid the coral-on-blush conflict. On desktop the block splits into a two-column layout: text left, input row right.

### Footer

**`footer`** — Midnight navy ground with four-column link grid. Column headers in white 16px/600 Jost; links in #bababa at body-sm, transitioning to coral (#ff6f61) on hover. A 10%-opacity white rule separates columns and the copyright row. Social icons are off-white at 24px with `{spacing.base}` spacing between them.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; hero headline drops to `display-md` (32px); hero height 360px; category grid 2-column; product grid 2-column; search expands full-width from icon tap; promo-banner grows to 48px to wrap text |
| Tablet | 744–1128px | Nav shows primary category links, hides utility items; hero 38px headline; category grid 3-column; product grid 3-column; search bar visible inline |
| Desktop | 1128–1440px | Full nav with all categories + inline search bar; hero `display-xl` 48px; category grid 4–6 column; product grid 4-column; newsletter block 2-column layout |
| Wide | > 1440px | Content capped at 1440px max-width; section paddings add 16px per side; hero min-height expands to 640px; product grid maintains 4-column but card gutters widen |

### Touch Targets

- All buttons and interactive nav links minimum 44×44px
- Nav drawer link rows use 56px height for comfortable thumb reach
- Product card entire surface is tappable (not image only)
- Badges are non-interactive; no tap-target expansion needed
- Search icon tap target is 44×44px when the input field is hidden

### Collapsing Strategy

- Nav: full links + search → primary links only → hamburger drawer (no mega-menu on mobile, stacked link list)
- Category grid: 6-up → 4-up → 3-up → 2-up
- Product grid: 4-up → 3-up → 2-up
- Hero CTA row: side-by-side → stacked (primary above secondary)
- Newsletter block: 2-column → stacked (headline + body above input row)
- Footer: 4-column → 2-column → single stacked with accordion disclosure per column

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No weight axis variants confirmed for Jost beyond the family name; weight assignments (400–700) are inferred from Jost's available variable weight range
- No meta theme-color set on the site; nav/status-bar color on mobile (#001f39) is estimated from the dominant extracted navy
- Icon library not identifiable from extraction — line vs. filled vs. custom SVG style unverified
- Exact mega-menu or fly-out structure of the nav unknown; category label copy and sub-navigation depth not extracted
- Animation and transition timing not extractable from static capture; values (0.2s ease, shadow transitions) are design-system convention defaults
- #d63384 pink and #475a96 slate blue appear in the extracted palette but no clear UI role was identified for either; omitted to avoid speculative token creation
- #3b86ff and #1199ff blues appear in palette but may be browser-default or third-party widget colors rather than brand tokens; omitted
- No design-token file (CSS custom properties or JSON) found; all tokens are reverse-engineered from computed color values
- Photography art-direction specifics (background color, prop styling, aspect ratio per subcategory) not confirmed from extraction
