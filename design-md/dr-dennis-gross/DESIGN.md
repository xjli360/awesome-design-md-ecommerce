---
version: alpha
name: "Dr. Dennis Gross"
source_url: "https://drdennisgross.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A clinical yet warm skincare authority that communicates efficacy through a restrained palette anchored on near-black `#050505` and a signature electric orange `#fe6728` that pulses across primary calls-to-action, accent badges, and ingredient-highlight moments. The brand walks a deliberate line between medical credibility and approachable luxury — the deep ink `#1b1b1b` body text sits on a clean `#fafafa` canvas, while muted grays like `#53585b`, `#868a89`, and `#9da1a0` build hierarchy in product descriptions, ingredient lists, and secondary navigation. A secondary orange `#ff651b` and a cautionary red `#cc0000` appear in promotional badges and sale indicators, while unexpected accents of cyan `#b4d5fe`, mint `#4efac0`, and electric blue `#0018ff` surface in ingredient callout cards and before/after result highlights, suggesting a brand confident enough to break its own rules. Typography leans on a mix of Avenir Next Pro for clean, legible body copy and the serif warmth of JHATimesNow for aspirational display moments — a pairing that signals both dermatological precision and editorial sophistication. Buttons use `{rounded.sm}` (8px) for a soft but not pill-like feel, while product cards and ingredient modules adopt `{rounded.md}` (12px) for a modern, approachable edge. The overall mood is confident, results-driven, and slightly warm — a clinical brand that remembers to smile.

colors:
  primary: "#fe6728"
  primary-active: "#ff651b"
  primary-disabled: "#ffd4b0"
  ink: "#050505"
  body: "#1b1b1b"
  muted: "#53585b"
  muted-soft: "#868a89"
  hairline: "#dddddd"
  hairline-soft: "#e5e5e5"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-orange: "#ff651b"
  accent-red: "#cc0000"
  accent-red-soft: "#ff5742"
  accent-cyan: "#b4d5fe"
  accent-mint: "#4efac0"
  accent-blue: "#0018ff"
  accent-green: "#00b84a"
  rating-star: "#fe6728"
  scrim: "#050505"
  badge-sale: "#cc0000"
  badge-new: "#4efac0"
  badge-limited: "#0018ff"

typography:
  display-xl:
    fontFamily: "'JHATimesNow-Light', 'Times New Roman', serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'JHATimesNow-SemiLightIT', 'Times New Roman', serif"
    fontSize: 36px
    fontWeight: 350
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  display-sm:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  title-lg:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-sm:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.15px
  badge:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.4px
    textTransform: uppercase
  link:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'AvenirNextProRegular', 'Avenir', 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0.3px
    textTransform: uppercase

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
    border: "2px solid {colors.ink}"
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    rounded: "{rounded.sm}"
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 0
  button-tertiary-hover:
    textColor: "{colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
    placeholderColor: "{colors.muted-soft}"
  text-input-focus:
    border: "1px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    boxShadow: "0 2px 8px rgba(5,5,5,0.08)"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    textColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0
    boxShadow: "0 1px 3px rgba(5,5,5,0.06)"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(5,5,5,0.1)"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-md}"
    textColor: "{colors.accent-red}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.ink}"
  hero-subheading:
    typography: "{typography.display-sm}"
    textColor: "{colors.muted}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-limited:
    backgroundColor: "{colors.badge-limited}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "4px 8px"
  badge-ingredient:
    backgroundColor: "{colors.accent-cyan}"
    textColor: "{colors.ink}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "1px solid {colors.primary}"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.muted-soft}"
  footer-link-hover:
    textColor: "{colors.primary}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    typography: "{typography.body-sm}"
    textColor: "{colors.muted}"
    padding: "0 0 {spacing.base} 0"
  ingredient-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    border: "1px solid {colors.hairline-soft}"
  ingredient-card-accent:
    borderTop: "3px solid {colors.primary}"
  rating-stars:
    color: "{colors.rating-star}"
    size: 16px
  review-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered in the signature orange `#fe6728` with white text and 8px rounded corners. On hover, the background shifts to the slightly warmer `#ff651b`. The disabled state uses a muted peach `#ffd4b0` to maintain visual hierarchy without confusing with active elements. All primary buttons use uppercase 14px/600 weight type with 0.5px letter spacing for a confident, clinical feel.

**`button-secondary`** — An outlined variant with a 2px near-black `#050505` border on a white canvas, used for secondary actions like "Add to Wishlist" or "Learn More." On hover, the button inverts to a solid near-black fill with white text, creating a satisfying tactile response. Shares the same dimensions and typography as the primary button.

**`button-tertiary`** — A text-only link styled as a button, used for less prominent actions like "View Details" or "See Ingredients." The default state is near-black with no background or border; on hover, the text shifts to the brand orange `#fe6728`, providing a subtle but clear interactive cue.

### Cards
**`product-card`** — The core product display unit, a white card with 12px rounded corners and a subtle drop shadow (`rgba(5,5,5,0.06)`). On hover, the shadow deepens to `rgba(5,5,5,0.10)` for a gentle lift effect. The card contains a product image, title in 16px/600 weight, price in 16px/400 weight, and optional sale pricing in red `#cc0000`. No padding on the card itself — internal spacing is handled by child elements.

**`ingredient-card`** — Used in ingredient spotlight sections, these white cards have a 12px rounded corner, a 1px soft hairline border, and 24px internal padding. An accent variant adds a 3px orange top border to draw attention to hero ingredients like Vitamin C or Retinol.

**`review-card`** — Customer review containers on a soft `#f5f5f5` background with 12px rounded corners and 24px padding. The muted background helps reviews sit comfortably below product imagery without competing for attention.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar at 72px height with a white background and a subtle bottom border (`1px solid #e5e5e5`). Navigation links use 13px uppercase type with 0.3px letter spacing. The active state is indicated by the brand orange text color and a 2px orange bottom border. The sticky variant adds a light box shadow for depth when scrolling.

**`nav-link`** — Individual navigation items set in 13px uppercase with medium weight. Default color is near-black `#050505`, hover and active states shift to orange `#fe6728`. The active state also includes a 2px bottom border in the same orange.

### Forms
**`text-input`** — Standard text input fields with a white background, 8px rounded corners, 48px height, and a 1px `#dddddd` border. On focus, the border switches to the brand orange for clear visual feedback. Error states use a red `#cc0000` border. Placeholder text is set in the muted gray `#868a89`.

**`select-input`** — Dropdown selectors matching the text input dimensions and styling, with a white background and 1px hairline border. The chevron icon is rendered in near-black.

### Badges
**`badge-sale`** — A small, urgent badge in red `#cc0000` with white uppercase 10px type, 4px rounded corners, and 4px/8px padding. Used to flag discounted products prominently.

**`badge-new`** — A fresh, attention-grabbing badge in mint `#4efac0` with near-black text, signaling newly launched products. Same dimensions and typography as the sale badge.

**`badge-limited`** — An exclusive badge in electric blue `#0018ff` with white text, used for limited edition or limited quantity items. Same dimensions and typography as other badges.

**`badge-ingredient`** — A pill-shaped tag in cyan `#b4d5fe` with near-black text, used to highlight key ingredients like "Vitamin C" or "Retinol" on product cards. Uses 11px type with full rounded corners for a softer, more informational appearance.

### Footer
**`footer-section`** — The site footer on a near-black `#050505` background with white text, 48px vertical padding, and 24px horizontal padding. Links are set in the muted gray `#868a89` and shift to orange on hover, maintaining the brand's signature accent color even in dark contexts.

### Accordion
**`accordion-trigger`** — Expandable section headers (used for FAQs, product details) with no background, near-black 16px/600 weight text, and a soft bottom border. The trigger area is padded at 16px top and bottom for comfortable touch targets.

**`accordion-content`** — The expandable content area below accordion triggers, set in 14px body text at the muted `#53585b` gray with 16px bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single column product grid, hamburger navigation, reduced hero font sizes, stacked ingredient cards, full-width buttons |
| Tablet | 744–1128px | Two column product grid, expanded navigation, 36px hero display type, side-by-side ingredient cards |
| Desktop | 1128–1440px | Three column product grid, full top nav with all links visible, 48px hero display type, multi-column footer |
| Wide | > 1440px | Max-width container at 1440px, centered content, four column product grid option, expanded whitespace |

### Touch Targets
- All interactive elements maintain minimum 44px height for touch accessibility
- Navigation links have minimum 44px tap area even when text is smaller
- Accordion triggers are full-width with 48px minimum touch height
- Product card CTAs are at least 48px tall
- Search bar has 44px height with adequate padding for finger taps

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces columns from 4 to 3 to 2 to 1 as viewport narrows
- Multi-column footer stacks to single column below 744px
- Ingredient cards shift from row layout to stacked below 744px
- Hero sections reduce padding and font sizes below 744px
- Side-by-side product details (image + description) stack vertically below 744px

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for secondary and tertiary buttons were inferred from common patterns rather than extracted from live CSS
- Error and success form states beyond border color changes could not be reliably extracted
- Dark mode palette is not present on the live site and would need to be designed
- Sub-brand or collection-specific color variations (e.g., holiday, professional) were not observed
- Animation durations and easing curves were not extractable from static analysis
- Focus ring styles (outline, offset) for keyboard navigation were not visible in extracted styles
- Dropdown menu and mega-menu patterns for navigation were not fully observable
- Modal and overlay component styles (backdrop, positioning) were not captured
- Tooltip and popover component specifications are absent
- Loading state and skeleton screen patterns were not extracted
- Print stylesheet specifications are not available
- The exact font weights for AvenirNextProRegular (likely 400) and AvenirNextLTPro-Regular (likely 400) are assumed based on naming conventions
