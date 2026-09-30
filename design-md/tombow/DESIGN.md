---
version: alpha
name: "Tombow"
source_url: "https://www.tombowusa.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  The color swatch grid — not product photography — is Tombow USA's real hero element. Fifty-six dual-brush pen shades display in their actual ink pigments: hot pink at #ea205c, warm orange at #ee9441, soft lavender at #a89cc8 — all anchored against a deep teal navigation rail at #108474 that doubles as the brand's primary surface. The UI is a deliberately neutral showcase chassis: near-white grays (#f6f6f6, #eeeeee, #dedede) absorb zero visual attention so every photon of saturated color belongs to the product itself. The teal pair (#108474, #04626c) holds all primary surfaces — navigation, CTAs, active filters — in a direct echo of the MONO graphite pencil barrel, where the same hue has lived for decades. MONO eraser yellow (#fbcd0a) operates as accent voltage: sale badges, announcement bars, and promotional CTAs carry it as a two-color shorthand that any Tombow product owner already recognizes from the pencil case in their bag. Light cyan (#c1e6e6) surfaces on hover tints and category chip backgrounds, cooling the palette without introducing a disconnected hue family.

  Type runs Nunito Sans as the functional workhorse — a rounded humanist sans whose softly terminated strokes echo the spring-loaded give of a brush pen nib. Headlines escalate into Chalet Comprime, a condensed display face that packs an entire product family name into a single typographic punch; Baskerville appears in editorial strips and campaign copy as a serif counterweight, creating a three-tier hierarchy of compressed display, rounded functional, and classical serif accent. Radius stays compressed throughout: `{rounded.xs}` on filter chips and individual color swatches, `{rounded.sm}` on buttons and product cards, `{rounded.full}` reserved only for the circular color-circle indicators themselves — a precision corner language that suits an instrument brand calibrated for consistent line quality. Spacing is generous at the macro level (`{spacing.section}`) and packed tightly at the component level, satisfying the catalog pressure of fifty-six-color product families without visual crowding.

colors:
  primary: "#108474"
  primary-active: "#04626c"
  primary-dark: "#035560"
  primary-disabled: "#c1e6e6"
  accent-yellow: "#fbcd0a"
  accent-yellow-active: "#e6b800"
  accent-pink: "#ea205c"
  accent-pink-active: "#d01d52"
  accent-orange: "#ee9441"
  accent-lavender: "#a89cc8"
  accent-cyan-light: "#c1e6e6"
  ink: "#121212"
  body: "#555555"
  muted: "#757575"
  muted-soft: "#888888"
  hairline: "#dedede"
  hairline-soft: "#e9e9e9"
  canvas: "#ffffff"
  surface-soft: "#f6f6f6"
  surface-card: "#eeeeee"
  surface-mid: "#e2e3e4"
  on-primary: "#ffffff"
  on-yellow: "#121212"

typography:
  display-xl:
    fontFamily: "'Chalet Comprime', 'Arial Narrow', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Chalet Comprime', 'Arial Narrow', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'Chalet Comprime', 'Arial Narrow', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0
  title-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  title-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0
  editorial:
    fontFamily: "Baskerville, 'Baskerville Old Face', 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0.2px
  body-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  price:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0
  product-label:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px
  color-chip-label:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  nav-link:
    fontFamily: "'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.25
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
    padding: "14px 24px"
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
    padding: "12px 22px"
    height: 48px
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
    rounded: "{rounded.sm}"
  button-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-yellow}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 24px"
    height: 48px
  button-yellow-active:
    backgroundColor: "{colors.accent-yellow-active}"
    textColor: "{colors.on-yellow}"
    rounded: "{rounded.sm}"
  button-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted-soft}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "12px 16px"
    height: 48px
  text-input-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "10px 16px 10px 44px"
    height: 44px
    iconColor: "{colors.muted}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
    rounded: "{rounded.sm}"
  announcement-bar:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-yellow}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
    logoMaxHeight: 36px
    borderBottom: none
  nav-dropdown:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    border: "1px solid {colors.hairline}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base}"
    imageBackground: "{colors.canvas}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.ink}"
  product-card-price-sale:
    typography: "{typography.price}"
    textColor: "{colors.accent-pink}"
  product-card-hover:
    border: "1px solid {colors.primary}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  color-swatch-chip:
    rounded: "{rounded.full}"
    size: 28px
    border: "2px solid transparent"
    hoverBorder: "2px solid {colors.ink}"
    selectedBorder: "3px solid {colors.primary}"
    labelTypography: "{typography.color-chip-label}"
    labelColor: "{colors.muted}"
  color-swatch-chip-lg:
    rounded: "{rounded.full}"
    size: 40px
    border: "2px solid transparent"
    selectedBorder: "3px solid {colors.primary}"
  color-palette-grid:
    gap: "{spacing.xs}"
    columns: 8
    swatchComponent: color-swatch-chip
    labelTypography: "{typography.color-chip-label}"
    labelColor: "{colors.muted}"
  category-filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.product-label}"
    rounded: "{rounded.xs}"
    padding: "6px 12px"
    border: "1px solid {colors.hairline}"
  category-filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.xs}"
    border: "1px solid {colors.primary}"
  sale-badge:
    backgroundColor: "{colors.accent-pink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  new-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  promo-badge:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.on-yellow}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "3px 8px"
  hero-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    minHeight: 480px
    headlineTypography: "{typography.display-xl}"
    bodyTypography: "{typography.body-md}"
    ctaVariant: button-yellow
  hero-banner-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    minHeight: 400px
    headlineTypography: "{typography.display-md}"
    bodyTypography: "{typography.body-md}"
    ctaVariant: button-primary
  editorial-strip:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    headlineTypography: "{typography.editorial}"
    bodyTypography: "{typography.body-md}"
    padding: "{spacing.xxl} 0"
  product-family-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.xxl} {spacing.xl}"
    accentLine: "4px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    linkColor: "{colors.hairline}"
    headingTypography: "{typography.title-sm}"
    bodyTypography: "{typography.body-sm}"
    padding: "{spacing.xxl} 0"
  footer-bottom-bar:
    backgroundColor: "{colors.primary-dark}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.caption}"
    height: 48px

## Components

### Buttons

**`button-primary`** — Deep teal (#108474) background, white text, 8px radius, 48px height. Hover deepens to `{colors.primary-active}` (#04626c); disabled state drains to the light cyan `{colors.primary-disabled}` with `{colors.muted}` text, maintaining legibility without suggesting interactivity. Used for "Add to Cart," "Shop Now," and all primary conversion actions throughout the site.

**`button-secondary`** — White canvas background with a 2px teal border and teal label text, matching primary height and radius. Hover fills with `{colors.surface-soft}` and deepens the border to `{colors.primary-active}`. Deployed alongside a primary CTA for secondary actions like "View Details" or "Compare Colors."

**`button-yellow`** — MONO eraser yellow (#fbcd0a) fill with near-black `{colors.on-yellow}` text. Reserved for promotional CTAs in hero banners and sale modules where the yellow-on-teal or yellow-on-light-surface contrast maximizes urgency signal. Active state shifts to `{colors.accent-yellow-active}`.

**`button-text`** — Transparent, teal label, no border or padding chrome. Minimal affordance for tertiary actions like "See all 56 colors" or "Read more" within content regions where a full button would be visually heavy.

### Inputs & Search

**`text-input`** — White canvas fill, 1px `{colors.hairline}` border, `{rounded.sm}`, 48px height. Focus upgrades to a 2px `{colors.primary}` border with no box-shadow — clean and precise. Placeholder renders in `{colors.muted-soft}`. Used for checkout fields, account forms, and contact inputs.

**`search-bar`** — Structurally identical to text-input but 44px tall and left-padded to 44px for a leading search icon in `{colors.muted}`. No pill shape — `{rounded.sm}` only, consistent with the brand's compressed corner language. Focus state matches text-input-focus.

### Navigation

**`nav-bar`** — Full teal (#108474) background, 64px height. Logo renders in white at left; navigation links in `{typography.nav-link}` at `{colors.on-primary}`. Dropdowns emerge on a `{colors.canvas}` white surface with `{colors.hairline}` border. The teal rail is the most persistent visual element on the page — it anchors the brand's palette relationship across every scroll depth.

**`announcement-bar`** — MONO yellow (#fbcd0a) strip above the nav, 36px tall, near-black centered text in `{typography.caption}`. Carries promotional messaging and free-shipping thresholds. The yellow-above-teal stack creates the brand's highest-density identity moment at the top of every page load.

**`nav-dropdown`** — White surface, `{rounded.sm}`, `{colors.hairline}` border, `{typography.body-sm}` links in `{colors.ink}`. Product family names may use `{typography.display-sm}` as section headers within wider mega-menu layouts.

### Product Cards

**`product-card`** — `{colors.surface-card}` (#eeeeee) fill, `{rounded.sm}`, 1px `{colors.hairline}` border. Product photography sits on a white `{colors.canvas}` inset. Title uses `{typography.title-sm}`, regular price uses `{typography.price}` in `{colors.ink}`, sale price overrides to `{colors.accent-pink}`. Hover adds a 1px `{colors.primary}` border and a soft drop shadow — the teal appears as an active selection signal before any click.

### Color Swatches

**`color-swatch-chip`** — 28px circles (`{rounded.full}`) filled in each product's actual ink color. Unselected chips carry a transparent border; hover adds a 2px `{colors.ink}` ring; selected state shows a 3px `{colors.primary}` outer ring. Labels in `{typography.color-chip-label}` sit below the chip in `{colors.muted}`. This pattern is Tombow's most distinctive UI signature — when fifty-six chips display simultaneously on a collection page, the grid IS the product catalog.

**`color-swatch-chip-lg`** — 40px variant for product detail pages and color-family landing pages, where a larger touch target and greater visual weight are appropriate. Same ring behavior at expanded scale.

**`color-palette-grid`** — 8-column grid layout of `color-swatch-chip` components, `{spacing.xs}` gap, `{typography.color-chip-label}` labels in `{colors.muted}`. The canonical layout unit for collection pages. Reduces to 4 columns on mobile.

### Filter Chips

**`category-filter-chip`** — `{colors.surface-soft}` fill, `{rounded.xs}`, `{typography.product-label}` in `{colors.body}`, 1px `{colors.hairline}` border. Active state flips to `{colors.primary}` background with `{colors.on-primary}` text and a matching border — visually identical to a small primary button. Used for product-family filters (Dual Brush Pens, MONO Drawing Pens, Adhesives), tip-type filters, and color-family filters.

### Badges

**`sale-badge`** — Hot pink (#ea205c) background, `{colors.on-primary}` text, `{typography.badge}` uppercase, `{rounded.xs}`, 3px 8px padding. **`new-badge`** — Same geometry in `{colors.primary}` teal. **`promo-badge`** — Same geometry in `{colors.accent-yellow}` with `{colors.on-yellow}` text. All three maintain identical padding and radius so they stack predictably in the product card corner without layout conflict.

### Banners & Editorial

**`hero-banner`** — Full-width teal (#108474), minimum 480px height. Headline in `{typography.display-xl}` (Chalet Comprime), body copy in `{typography.body-md}` (Nunito Sans), both in `{colors.on-primary}`. Primary CTA is always `button-yellow` — yellow on teal is the brand's peak contrast moment and its clearest promotional signal.

**`hero-banner-light`** — `{colors.surface-soft}` variant for seasonal or secondary campaign slots, with `{typography.display-md}` headline in `{colors.ink}` and a `button-primary` CTA. Lower visual energy than the teal version, appropriate for educational or artist-feature content.

**`editorial-strip`** — White canvas section, headline in `{typography.editorial}` (Baskerville, 20px), body in `{typography.body-md}` (Nunito Sans), text in `{colors.body}`. The serif register creates a deliberate pause in the otherwise Nunito-heavy page flow, surfacing in brand-storytelling sections and artist-partnership features.

**`product-family-banner`** — `{colors.surface-soft}` background with a 4px left-edge accent line in `{colors.primary}`, headline in `{typography.display-sm}` (Chalet Comprime), `{rounded.sm}` on the container. Used to introduce product families within a scrolling collection page — MONO Drawing Pens, Dual Brush Pens, ABT PRO Alcohol Markers each get their own banner with the teal accent line as the visual thread.

### Footer

**`footer`** — Near-black `{colors.ink}` (#121212) fill, column layout with `{typography.title-sm}` section headings in white and `{typography.body-sm}` links in `{colors.hairline}`. **`footer-bottom-bar`** — The darkest teal `{colors.primary-dark}` (#035560) strip beneath the main footer carries legal copy and copyright in `{typography.caption}` at `{colors.muted-soft}`. The teal reappears at the page's bottom as a bookend to the teal nav at the top.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger on teal bar; `color-palette-grid` drops to 4 columns; hero min-height reduces to 300px; announcement bar text truncates to key message only |
| Tablet | 744–1128px | Two-column product grid; nav shows primary category links inline with overflow in dropdown; `color-palette-grid` at 6 columns; hero switches to side-by-side text-and-image layout |
| Desktop | 1128–1440px | Three- to four-column product grid; full nav with mega-menu dropdowns; `color-palette-grid` at canonical 8 columns; hero at full 480px height |
| Wide | > 1440px | Content max-width capped at 1440px, centered with auto margins; hero and announcement bar backgrounds bleed full viewport width while content stays in grid |

### Touch Targets
- Color swatch chips expand to a minimum 44×44px touch target on mobile regardless of the 28px visual size — use padding or an invisible overlay
- Filter chips increase to `{spacing.sm}` vertical padding at mobile breakpoint for easier activation
- All primary buttons are already 48px height — no adjustment needed
- Nav hamburger button is 48×48px with `{rounded.sm}`
- Footer links gain 8px additional vertical padding on mobile to prevent mis-taps between dense link columns

### Collapsing Strategy
- Announcement bar persists on mobile; font reduces to 10px with message shortened to promo code or offer headline only
- `product-family-banner` left-edge accent line moves to a top-edge accent on mobile (4px top border instead of 4px left border) to maintain visual identity in a stacked layout
- Editorial strip Baskerville headline scales from 20px to 16px on mobile; line-height increases to 1.65 for legibility at smaller size
- `color-chip-label` text hidden on mobile; tooltip or bottom-sheet on long-press reveals the color name
- `nav-dropdown` mega-menu collapses to full-screen drawer on mobile with back-navigation per category level

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No meta theme-color extracted; teal #108474 assumed as the closest digital brand representative for browser chrome
- Chalet Comprime is a licensed display face with multiple regional variants (Cologne, London, Tokyo weights); exact weight variant used for display-xl and display-md headings not determinable from CSS extraction alone
- Exact computed font sizes for display headings not captured; values above are estimated from proportional relationships visible in the extracted font stack
- Button and card corner radius not explicitly confirmed in extracted CSS; `{rounded.sm}` (8px) inferred from the general compressed-radius visual language
- Exact nav height not extracted; 64px estimated from standard Shopify theme proportions
- Social share icon colors (#3b5998 Facebook, #1da1f2 Twitter, #dd4b39 Google) present in extracted palette; individual social button component layouts and sizing not captured
- Animation timings and easing curves (hover transitions, swatch ring animation) not extractable from static color/font scan
- Dark-mode or high-contrast variant not detected; assumed light-only
- Custom iconography library not identified beyond JudgeMe review star icons in the extracted font stacks
- Product color naming convention (e.g. whether #a89cc8 is "Mauve" or "Light Violet" in catalog copy) not extractable from CSS — color-chip label strings must come from product data
