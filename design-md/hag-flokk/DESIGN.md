---
version: alpha
name: "HAG (Flokk)"
source_url: "https://www.flokk.com/en/us/hag"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Four shades of Nordic forest — running from near-black #0e352d down through #174e42 and #1f6e5e to the muted sage of #8ca6a0 — give HÅG's digital presence a chromatic depth most office-furniture brands flatten into a single brand green. The warmth comes from the canvas side: #fffbf3, a cream so gently off-white it reads almost like paper, contrasting with the forest walls without going clinical. A secondary warm strand — sand, linen, and auburn tones (#cbb6a7, #aa8e7f, #806a5f) — runs through imagery metadata and textile swatches, grounding the product in physical material rather than abstract brand color. Typography is divided between MessinaSerif and PostGrotesk, two typefaces that correspond almost architecturally to the brand's dual identity: the serif carries editorial authority in large-format display settings, while the grotesque handles precision legibility across product spec sheets, filter menus, and button labels. A proprietary FlokkIcons set locks icon weight to the house grotesque, ensuring interface glyphs never read heavier or lighter than surrounding label text. Two accent colors appear rarely but with force: #490f13, a near-black burgundy pressed almost into dried-lacquer territory, and #b84a59, a cooler rose clear enough for text usage on light surfaces; neither appears in structural navigation or primary CTA work — they surface in sale callouts, badge moments, or seasonal campaign rollouts, amplifying their signal through restraint. Geometry is deliberately understated: product cards sit at {rounded.sm}, input fields match, and primary CTAs step up modestly to {rounded.md} — no pill-shaped elements, no hard-cornered boxes, just a radius vocabulary that echoes the soft-edged profiles of the chairs themselves. Spacing is generous throughout: hero interiors breathe at {spacing.xxl} minimum and section-level vertical rhythm locks to {spacing.section}, giving product photography room to do the brand's heaviest lifting without additional graphic decoration.

colors:
  primary: "#1f6e5e"
  primary-dark: "#0e352d"
  primary-mid: "#174e42"
  primary-light: "#325850"
  primary-active: "#174e42"
  primary-disabled: "#8ca6a0"
  secondary-sage: "#8ca6a0"
  secondary-sage-light: "#d0dbd8"
  secondary-sage-softer: "#bbc8c3"
  secondary-sage-mist: "#e7edeb"
  accent-burgundy: "#490f13"
  accent-rose: "#b84a59"
  ink: "#4a4a4a"
  body: "#584641"
  muted: "#757575"
  warm-brown: "#806a5f"
  linen: "#cbb6a7"
  auburn: "#aa8e7f"
  hairline: "#e1ddda"
  hairline-soft: "#e9e9e9"
  canvas: "#fffbf3"
  surface-warm: "#f8f7f6"
  surface-soft: "#f3f3f3"
  surface-card: "#f9f9f9"
  cream-accent: "#fff5c5"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  on-canvas: "#4a4a4a"

typography:
  display-xl:
    fontFamily: "MessinaSerif, Georgia, serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-md:
    fontFamily: "MessinaSerif, Georgia, serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "MessinaSerif, Georgia, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "PostGrotesk, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "PostGrotesk, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.1px
  body-md:
    fontFamily: "PostGrotesk, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "PostGrotesk, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "PostGrotesk, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "PostGrotesk, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.8px
    textTransform: uppercase
  badge:
    fontFamily: "PostGrotesk, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.4px
    textTransform: uppercase
  button-md:
    fontFamily: "PostGrotesk, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "PostGrotesk, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "PostGrotesk, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.1px
  price-display:
    fontFamily: "MessinaSerif, Georgia, serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0

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
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 13px 27px
    height: 48px
    border: "1.5px solid {colors.primary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
  button-dark:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.md}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
    focusBorder: "1.5px solid {colors.primary}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoTextColor: "{colors.primary-dark}"
    activeItemColor: "{colors.primary}"
    activeItemIndicator: "2px underline {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    imageRatio: "4/3"
    padding: "{spacing.lg}"
    titleTypography: "{typography.display-sm}"
    priceTypography: "{typography.price-display}"
    bodyTypography: "{typography.body-sm}"
    shadow: none
    hoverShadow: "0 4px 16px rgba(14,53,45,0.10)"
    hoverBorder: "1px solid {colors.secondary-sage-light}"
  hero-banner:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.section} {spacing.xxl}"
    imageLayout: bleed-right
    overlayColor: "{colors.primary-dark}"
    overlayOpacity: 0.35
    minHeightDesktop: 520px
    minHeightMobile: 320px
  collection-grid:
    backgroundColor: "{colors.canvas}"
    columns: 3
    gap: "{spacing.lg}"
    padding: "{spacing.xl} {spacing.xxl}"
    filterBarHeight: 56px
    filterBarBackground: "{colors.surface-soft}"
    filterPillBackground: "{colors.secondary-sage-mist}"
    filterPillTextColor: "{colors.primary-dark}"
    filterPillRounded: "{rounded.full}"
  swatch-picker:
    swatchSize: 28px
    swatchGap: "{spacing.xs}"
    selectedBorder: "2px solid {colors.primary}"
    unselectedBorder: "1px solid {colors.hairline}"
    rounded: "{rounded.full}"
    labelTypography: "{typography.body-sm}"
    labelColor: "{colors.ink}"
  spec-table:
    backgroundColor: "{colors.surface-warm}"
    headerBackgroundColor: "{colors.primary-dark}"
    headerTextColor: "{colors.on-dark}"
    headerTypography: "{typography.spec-label}"
    cellTypography: "{typography.body-sm}"
    cellTextColor: "{colors.ink}"
    rowDivider: "1px solid {colors.hairline}"
    padding: "{spacing.md} {spacing.base}"
    rounded: "{rounded.sm}"
  material-badge:
    backgroundColor: "{colors.secondary-sage-mist}"
    textColor: "{colors.primary-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sale-badge:
    backgroundColor: "{colors.accent-rose}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  sustainability-badge:
    backgroundColor: "{colors.cream-accent}"
    textColor: "{colors.primary-dark}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  breadcrumb:
    textColor: "{colors.muted}"
    activeColor: "{colors.ink}"
    separatorColor: "{colors.hairline}"
    typography: "{typography.caption}"
    gap: "{spacing.xs}"
  footer:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.on-dark}"
    headingTypography: "{typography.title-sm}"
    linkTypography: "{typography.body-sm}"
    linkColor: "{colors.secondary-sage-light}"
    linkHoverColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xxl}"
    bottomBarBackgroundColor: "{colors.primary-mid}"
    bottomBarTypography: "{typography.caption}"

## Components

### Buttons

**`button-primary`** — Forest green (#1f6e5e) fill with white PostGrotesk type at 15px/500 weight, 8px radius, 48px height, and 14px/28px padding. The active state darkens to `{colors.primary-active}` (#174e42); the disabled state uses the desaturated sage `{colors.primary-disabled}` (#8ca6a0) to communicate unavailability without aggression. Use for primary purchase, configure, and request-quote actions.

**`button-secondary`** — Cream canvas background (`{colors.canvas}`) with a 1.5px forest green border and forest green type, matching the primary's geometry exactly. On hover, a light sage mist (`{colors.secondary-sage-mist}`) tints the background. Use for secondary actions like "Learn More", "Download Spec Sheet", or "Compare".

**`button-ghost`** — Transparent background with a 1px `{colors.hairline}` border and ink text at `{typography.button-sm}`, `{rounded.sm}`. Used for tertiary actions, filter chips, and pagination controls where visual weight must stay minimal.

**`button-dark`** — Deep forest (#0e352d) fill with white type. Used over light canvas sections where a strong visual anchor is needed without introducing the primary green — common in editorial landing sections and sustainability campaign pages.

### Text Input

**`text-input`** — Cream canvas background with a 1px `{colors.hairline}` border at `{rounded.sm}`, 48px height, PostGrotesk 16px body type. On focus, the border upgrades to 1.5px `{colors.primary}`. Placeholder text renders in `{colors.muted}`. Used for search bars, configurator quantity fields, and dealer-locator queries.

### Navigation

**`nav-bar`** — 64px tall, cream canvas background with a single 1px `{colors.hairline}` bottom border. The HÅG wordmark sits left in `{colors.primary-dark}`; nav links use PostGrotesk 14px/500 in `{colors.ink}`. The active link shifts to `{colors.primary}` and receives a 2px underline indicator. On scroll past the hero, the bar gains a soft box-shadow (4px blur, 10% forest alpha) to separate it from scrolled content.

### Product Card

**`product-card`** — Light `{colors.surface-card}` background at `{rounded.sm}`. The product image fills a 4:3 crop zone at the top; title renders in MessinaSerif `{typography.display-sm}`; price in MessinaSerif `{typography.price-display}` below; a one-line description excerpt in PostGrotesk `{typography.body-sm}`. No shadow at rest; hover brings a soft 16px shadow at 10% forest alpha and a `{colors.secondary-sage-light}` border outline. A row of circular swatch dots for available upholstery colorways appears beneath the excerpt.

### Hero Banner

**`hero-banner`** — Full-bleed deep forest (#0e352d) background with product photography bleeding to the right edge on desktop (bleed-right layout). Headline in MessinaSerif `{typography.display-xl}` at white; body copy in PostGrotesk `{typography.body-md}`; a `button-primary` CTA below. A 35% opacity `{colors.primary-dark}` overlay on the image zone ensures headline legibility over high-contrast photography. Minimum heights: 520px desktop, 400px tablet, 320px mobile.

### Collection Grid

**`collection-grid`** — Three-column product grid on desktop with 24px gap and cream canvas background. A 56px filter/sort bar (`{colors.surface-soft}`) anchors above the grid and sticks under the nav on scroll. It holds category filter pills (`{rounded.full}`, `{colors.secondary-sage-mist}` fill, `{colors.primary-dark}` text) and a sort dropdown. Grid collapses to 2-column at tablet, 1-column at mobile.

### Swatch Picker

**`swatch-picker`** — 28px circular swatches in a wrapping flex row with 4px gap. The selected swatch carries a 2px `{colors.primary}` border with a 2px offset ring. Unselected swatches have a 1px `{colors.hairline}` border. A `{typography.body-sm}` label beneath updates dynamically to the hovered or selected colorway name. Used in product detail pages and configurator option panels.

### Spec Table

**`spec-table`** — Two-column definition table. The header row uses a `{colors.primary-dark}` background with white `{typography.spec-label}` uppercase labels; data cells use `{colors.surface-warm}` background and `{typography.body-sm}` in `{colors.ink}`. Rows are divided by 1px `{colors.hairline}` lines. Used for dimensions, weight capacity, adjustability ranges, material certifications, and GREENGUARD/ergonomic compliance data.

### Badges

**`material-badge`** — Sage mist (#e7edeb) background with `{colors.primary-dark}` uppercase PostGrotesk 11px/600 text at `{rounded.xs}`. Used for certification labels ("Recycled Mesh", "FSC Wood", "GREENGUARD Gold"). **`sale-badge`** — Rose (#b84a59) fill with white type; appears top-left on product cards during promotions. **`sustainability-badge`** — Cream (#fff5c5) fill with dark forest text; marks products in environmental or lifecycle-conscious collections.

### Breadcrumb

**`breadcrumb`** — Inline flex row of PostGrotesk 12px links in `{colors.muted}` for ancestor pages, stepping up to `{colors.ink}` for the current page. A chevron separator renders in `{colors.hairline}` with 4px gaps. Sits 16px below the nav bar on product detail and collection pages.

### Footer

**`footer`** — Full-width deep forest (#0e352d) background. Section headings in PostGrotesk `{typography.title-sm}` white; links in PostGrotesk `{typography.body-sm}` sage-light (#d0dbd8), transitioning to full white on hover. A slightly lighter bottom bar (`{colors.primary-mid}`, #174e42) holds copyright, locale switcher, and legal links at PostGrotesk `{typography.caption}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger drawer (forest green background, white links); hero switches to vertical stack with image above text; collection grid becomes 1-column; spec table scrolls horizontally with pinned label column; swatch picker wraps to 2 rows max |
| Tablet | 744–1128px | 2-column collection grid; hero uses 50/50 split layout; nav shows primary links, overflow items collapse into a "More" dropdown; product card images switch to 1:1 crop |
| Desktop | 1128–1440px | 3-column collection grid; full nav bar with all links visible; hero uses bleed-right image layout; spec table full-width |
| Wide | > 1440px | Content max-width 1440px centered; hero image extends beyond content container to screen edges; outer horizontal padding increases to 96px |

### Touch Targets

- All buttons: minimum 48px height (enforced in button-primary, button-secondary, text-input definitions)
- Swatch pickers: 28px visual swatches expand tap zone to 40px via invisible padding
- Nav links: minimum 44px tap height on mobile via vertical padding
- Breadcrumb links: minimum 40px tap height via vertical padding on mobile
- Filter pills: minimum 40px height on mobile collection grid

### Collapsing Strategy

- Navigation: full horizontal bar collapses to hamburger drawer at < 744px; drawer slides from the left with a deep forest green background and white link text
- Filter bar: horizontal scrolling pill row on tablet; expands to a bottom-sheet modal panel on mobile
- Spec table: horizontal scroll with left column (property label) pinned on mobile
- Hero: bleed-right image layout collapses to full-width image stacked above text on mobile; headline scale drops from `display-xl` (56px) to `display-md` (36px)
- Product card grid: 3-col → 2-col at tablet → 1-col at mobile; image aspect ratio maintained throughout

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Exact border-radius values not confirmed from CSS extraction; `{rounded.md}` (8px) for CTAs is inferred from brand aesthetic and Scandinavian design norms
- No `meta theme-color` was set, so mobile browser chrome color is unspecified
- FlokkIcons glyph map, icon sizes, and stroke weights are not publicly documented; icon usage patterns inferred from site observation
- MessinaSerif licensed weight range (whether HÅG uses only Regular or also Medium/Bold) was not confirmable from extraction
- PostGrotesk weight range available in the Flokk webfont implementation (subset vs. full variable) not confirmed
- Exact nav scroll-trigger behavior (shadow onset point, transition duration) estimated
- Price display format — currency symbol position, decimal convention for EU vs. US locale split — not confirmed
- Configurator UI (custom chair builder, if present) has significant additional component complexity not captured here, likely including a step-indicator, 3D viewer embed, and multi-panel option selector
- Animation and transition timing values (hover durations, page transition style) not extractable from static hints
- Whether #490f13 (accent-burgundy) appears as a product finish/upholstery color or exclusively as a UI accent is unclear from extraction alone
