---
version: alpha
name: "Infantino"
source_url: "https://infantino.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  ArcherPro Medium — a slab serif that normally lives in magazine mastheads and editorial contexts — shows up as Infantino's foundational typeface, an unusual choice for a baby product brand and the source of its warmest quality. The site's palette hinges on a vivid red-orange (#e94125) as the single high-voltage CTA color, paired with two closely tuned teals that serve separate semantic roles: #4dacaa handles category accents, badge fills, and hover surfaces, while #00afab — perceptibly deeper — takes interactive focus states and link emphasis. A warm brown-tan (#7c6a55) functions as the tertiary: earthier than a neutral gray, it anchors lifestyle photography, secondary labels, and the occasional price-adjacent supporting text without announcing itself. Pathout Italic appears at display scale only — hero banners and seasonal campaign headers — where its looping forms supply the playful contrast that ArcherPro's upright slab character cannot.

  Rounded geometry signals the brand's approachable, child-safe posture throughout: primary CTAs run pill-shaped ({rounded.full}), product cards use {rounded.md} at their corners, and rectangular sale flags snap to {rounded.xs}. No hard 90-degree angles appear in marketing zones. The background leans toward a warm off-white — #f2f2f2 surfaces behind product grids, #e5e5e5 as hairlines — keeping photography luminous rather than clinical. At 16px with a 1.5 line-height, body text holds legibility for parents parsing ingredient lists and age-safety specs on phones during nighttime feeds; the type scale prioritizes reading conditions over aesthetic sparseness.

  On the Shopify storefront, the red-orange primary drives every add-to-cart and checkout CTA, while the teal secondary differentiates category navigation and informational callouts — effectively replacing Shopify's generic navy with a brand-owned color system. Gift-set and bundle pages draw on {colors.accent-warm} to communicate value without price-cut language, leaning into a quality-led retail register. The overall visual system reads bright but not garish: one signal color, one category color, one warmth color, held together by a slab serif that most competitors in the baby aisle would never reach for.

colors:
  primary: "#e94125"
  primary-active: "#c83018"
  primary-disabled: "#f5b3a5"
  secondary: "#4dacaa"
  secondary-active: "#00afab"
  accent-warm: "#7c6a55"
  ink: "#55565a"
  body: "#55565a"
  muted: "#7c6a55"
  hairline: "#e5e5e5"
  canvas: "#ffffff"
  surface-soft: "#f2f2f2"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-secondary: "#ffffff"

typography:
  display-hero:
    fontFamily: "'Pathout Italic', cursive"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-xl:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-sm:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  body-md:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: 0.2px
  label-uppercase:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.18
    letterSpacing: 1px
    textTransform: uppercase
  button-md:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  nav-link:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  price:
    fontFamily: "'ArcherPro Medium', Georgia, 'Times New Roman', serif"
    fontSize: 18px
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
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
    pointerEvents: none
  button-secondary:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 28px
    height: 48px
  button-secondary-active:
    backgroundColor: "{colors.secondary-active}"
    textColor: "{colors.on-secondary}"
    rounded: "{rounded.full}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary}"
    padding: 12px 26px
    height: 48px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    border: "2px solid {colors.secondary}"
    rounded: "{rounded.sm}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-link-active:
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    shadow: "0 2px 8px rgba(85,86,90,0.08)"
  product-card-title:
    typography: "{typography.title-md}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.price}"
    textColor: "{colors.primary}"
  product-card-badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    displayFont: "{typography.display-hero}"
    headingFont: "{typography.display-xl}"
    bodyFont: "{typography.body-md}"
    textColor: "{colors.ink}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
  age-badge:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.label-uppercase}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  category-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 16px
  category-chip-active:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: none
    padding: 8px 16px
  promo-banner:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption}"
    height: 36px
    textAlign: center
  safety-callout:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    border: "1px solid {colors.hairline}"
    padding: "{spacing.base} {spacing.lg}"
    iconColor: "{colors.secondary-active}"
  award-badge:
    backgroundColor: "{colors.accent-warm}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.sm}"
    padding: 6px 10px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    height: 44px
    padding: 0 {spacing.base}
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    linkColor: "{colors.secondary}"
    padding: "{spacing.xxl} {spacing.xl}"

## Components

### Buttons
**`button-primary`** — The primary CTA runs red-orange (#e94125) on a pill shape ({rounded.full}), 48px tall with 28px horizontal padding. On press, the surface deepens to {colors.primary-active} (#c83018); the disabled state fades to {colors.primary-disabled} and removes pointer events. This is the exclusive color for add-to-cart and Shopify checkout entries — nothing else on the page uses red-orange fills.

**`button-secondary`** — Teal-filled at {colors.secondary} (#4dacaa), also pill-shaped. Active state advances to {colors.secondary-active} (#00afab). Used for category navigation CTAs, gift-finder entries, and "Learn More" actions that don't trigger the purchase flow.

**`button-ghost`** — Transparent fill with a 2px red-orange border and matching label text at {typography.button-md}. Appears alongside `button-primary` in two-CTA hero layouts and gift-set pages where both options carry equal weight.

### Navigation
**`nav-bar`** — 64px tall white bar with a 1px {colors.hairline} bottom border. Type is {typography.nav-link} at 14px/500. Active category links shift to {colors.primary} text with no underline or underline animation. On mobile the bar reduces to logo-center and hamburger-right; a full-height drawer carries the category list with accordion subcategories.

### Product Cards
**`product-card`** — White ({colors.surface-card}) card with {rounded.md} corners and a soft 8px shadow at low opacity. Title in {typography.title-md}, price in {typography.price} red-orange. A `product-card-badge` at {rounded.xs} overlays the top-left corner for "New", "Sale", or "Bundle" flags in red-orange on white label text.

### Hero
**`hero-banner`** — Full-width section on {colors.surface-soft} warm-gray background, minimum 560px tall. Seasonal campaigns use {typography.display-hero} (Pathout Italic at 64px) for the main headline; evergreen product categories fall back to {typography.display-xl} (ArcherPro Medium at 48px). Body copy runs {typography.body-md}. CTA row pairs `button-primary` and `button-ghost` side by side.

### Age & Category Badges
**`age-badge`** — Teal pill ({colors.secondary}, {rounded.full}) with all-caps label tracking at 1px letter-spacing. Displays "0–3M", "6+ Months", "1 Year+" on product cards, detail pages, and filter panels to communicate developmental suitability at a glance.

**`category-chip`** — Off-white pill with {colors.hairline} border at rest; advances to a solid {colors.secondary} fill on selection with no border. Used in the horizontal filter strip above product grids. On mobile the strip is a full-bleed scrollable row with no wrapping.

### Promo Banner
**`promo-banner`** — 36px red-orange bar sitting above the nav, full viewport width. Short promotional copy in {typography.caption} white text, centered. On viewports under 375px the text truncates with a marquee scroll or collapses to an icon-only dismiss control.

### Safety Callout
**`safety-callout`** — {colors.surface-soft} box with a 1px {colors.hairline} border, {rounded.md} corners, and a {colors.secondary-active} icon on the left margin. Appears on product detail pages for age-safety disclosures, material composition, and choking-hazard warnings. Body copy in {typography.body-sm} ensures legibility at small viewport widths.

### Award Badge
**`award-badge`** — Warm brown ({colors.accent-warm}) badge with white text at {typography.badge} scale and {rounded.sm} corners. Communicates industry awards or "Bestseller" status without borrowing the red-orange primary, keeping {colors.primary} reserved exclusively for purchase actions.

### Search
**`search-bar`** — Pill-shaped ({rounded.full}) {colors.surface-soft} input with a 1px {colors.hairline} border, 44px height, and a magnifier icon in {colors.muted} on the left interior. On focus, the border advances to {colors.secondary}, mirroring the `text-input-focus` state and connecting search to the teal category system.

### Footer
**`footer`** — Charcoal ({colors.ink}) background with white body copy ({typography.body-sm}) and {colors.secondary} teal links for section headings and external destinations. Four-column grid on desktop with 48px top-and-bottom padding; collapses to accordion sections with toggle controls on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; nav collapses to hamburger drawer; hero-banner stacks text above image; promo-banner truncates or marquees; button-primary goes full-width; category-chip strip scrolls horizontally |
| Tablet | 744–1128px | Two-column product grid; nav shows primary categories with overflow in dropdown; hero-banner switches to side-by-side layout at reduced padding |
| Desktop | 1128–1440px | Three-column product grid; full five-category nav-bar; hero-banner at full 560px min-height; promo-banner displays complete message |
| Wide | > 1440px | Grid and content cap at 1440px max-width with auto lateral margins; hero-banner background color bleeds full-width while content constrains to grid |

### Touch Targets
- Minimum 44px height on all interactive elements — buttons, chips, inputs, and nav links
- Age-badge and category-chip tap areas extended with 12px vertical padding on mobile
- Hamburger nav target is 48×48px with a 12px internal icon
- Product card entire surface is tappable; not limited to the title or image alone

### Collapsing Strategy
- Nav secondary links (Gift Finder, Sale, Blog) collapse into hamburger before primary category items
- Hero dual-CTA row stacks vertically on mobile with button-primary on top
- Safety callout icon collapses on viewports under 375px; text-only version at {typography.body-sm} persists
- Footer four-column grid collapses to stacked accordion sections with plus/minus toggles
- Award badge and age-badge remain visible on product cards at all breakpoints; promo-banner is the first element hidden on print stylesheets

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Only "ArcherPro Medium" was extracted; regular-weight (400) body copy may require a separately loaded ArcherPro Regular cut not confirmed in extraction — body-md fontWeight: 400 is an inference
- Pathout Italic line-height, exact scale breakpoints, and letterspacing not extractable from live site; values estimated from visual cadence
- Exact button height and horizontal padding not confirmed via computed styles — 48px height and 28px padding derived from visual proportion against the reference format
- primary-active (#c83018) and primary-disabled (#f5b3a5) are derived tints/shades; not confirmed via source inspection
- No dark-mode token set visible in extraction — site appears light-only on the current Shopify theme build
- Shadow values for product-card not extracted; 0 2px 8px rgba approximation estimated from visual card lift
- Disabled and hover states for button-secondary and button-ghost not confirmed; only button-primary states are estimated with confidence
- Hover transition durations and easing functions not extracted; 150ms ease assumed throughout
- Meta theme-color is unset, suggesting no PWA or app-clip manifest on current build
- Semantic split between #4dacaa (category/badge) and #00afab (interactive/focus) is inferred from visual hierarchy, not confirmed via source inspection
- Exact nav-bar height not confirmed; 64px estimated from proportional inspection
