---
version: alpha
name: "Twelve South"
source_url: "https://www.twelvesouth.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Four optical widths of Freight Sans Pro on a single page — book, compressed, condensed, ultra — commit Twelve South to typographic investment that most tech accessories sites skip entirely. The ultra weight handles massive hero statements at near-zero tracking, the compressed variant drives display headlines that carry visual mass without horizontal sprawl, and the book weight settles into airy editorial body copy; the brand swings between cinematic and clinical without switching font families. The color story anchors on a deep ocean teal (#045c7d) as its primary identity token — cool and premium without defaulting to the near-neutral grays that dominate Apple-adjacent categories. Dark hero sections use a near-black (#121713) with a faint green undertone, a forest-at-midnight cast rather than pure onyx; light product sections float on a mint-tinged white (#eff5f3), giving the transition from hero to grid a sense of surfacing into daylight. The accent vocabulary runs in three frequencies: urgent red-orange (#ff4127) for sale badges and limited-availability signals, electric mint (#00caaa) for compatibility callouts and new-product indicators, and warm gold (#ffcf2a) for featured or seasonal moments. Buttons and cards sit at `{rounded.sm}` — enough curvature to read as approachable but never so soft that the premium positioning dissolves into lifestyle-brand friendliness. Product photography is the primary visual currency: every card reserves a 4:3 image slot, and hero modules alternate between lifestyle shots on dark canvas and product-isolation photography on the light mint surface. Spacing is deliberately generous — `{spacing.section}` between page chapters, `{spacing.xl}` between card rows — ensuring that nothing competes for attention in a grid that often mixes cables, stands, and charging gear from a single Apple ecosystem narrative.

colors:
  primary: "#045c7d"
  primary-active: "#034b68"
  primary-disabled: "#88afc0"
  ink: "#121713"
  body: "#404041"
  muted: "#637473"
  muted-light: "#9a9db1"
  hairline: "#e5e5e5"
  hairline-soft: "#f4f4f6"
  canvas: "#f7f7f8"
  surface-soft: "#eff5f3"
  surface-card: "#ffffff"
  surface-dark: "#121713"
  surface-dark-mid: "#1a1b18"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-orange: "#ff4127"
  accent-teal: "#00caaa"
  accent-gold: "#ffcf2a"
  accent-sky: "#86d8f7"
  accent-blue: "#08a5df"
  navy-deep: "#272d45"
  slate: "#495857"
  charcoal-mid: "#3d4246"

typography:
  ultra-hero:
    fontFamily: "'freight-sans-pro-ultra', 'freight-sans-compressed-pro', 'FreightSansProBook-Regular', Roboto, sans-serif"
    fontSize: 96px
    fontWeight: 900
    lineHeight: 0.95
    letterSpacing: -2px
  display-xl:
    fontFamily: "'freight-sans-compressed-pro', 'freight-sans-pro', 'FreightSansProBook-Regular', Roboto, sans-serif"
    fontSize: 72px
    fontWeight: 800
    lineHeight: 1.0
    letterSpacing: -1px
  display-lg:
    fontFamily: "'freight-sans-compressed-pro', 'freight-sans-pro', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'freight-sans-condensed-pro', 'freight-sans-pro', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.25px
  display-sm:
    fontFamily: "'freight-sans-condensed-pro', 'freight-sans-pro', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-md:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'FreightSansProBook-Regular', 'freight-sans-pro', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'FreightSansProBook-Regular', 'freight-sans-pro', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.5px
  button-sm:
    fontFamily: "'freight-sans-pro', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0.4px
  nav-link:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.2px
  badge-label:
    fontFamily: "'freight-sans-pro', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.8px
    textTransform: uppercase
  price-display:
    fontFamily: "'freight-sans-condensed-pro', 'freight-sans-pro', sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0
  product-name:
    fontFamily: "'freight-sans-pro', 'FreightSansProBook-Regular', sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  tag-label:
    fontFamily: "'freight-sans-pro', sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.3px

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
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.sm}"
    opacity: 0.6
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.ink}"
    padding: 13px 27px
    height: 48px
  button-ghost-light:
    backgroundColor: "transparent"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "1.5px solid {colors.on-dark}"
    padding: 13px 27px
    height: 48px
  button-accent-orange:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    padding: 12px 16px
    height: 48px
  announcement-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.caption}"
    height: 40px
    linkColor: "{colors.accent-teal}"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: "1px solid {colors.hairline}"
    logoMaxHeight: 32px
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  hero-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.display-sm}"
    minHeight: 560px
    padding: "{spacing.section} {spacing.xl}"
    ctaButton: "button-primary"
    ctaButtonSecondary: "button-ghost-light"
  hero-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    headlineTypography: "{typography.display-lg}"
    subheadTypography: "{typography.body-md}"
    minHeight: 480px
    padding: "{spacing.section} {spacing.xl}"
    ctaButton: "button-primary"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
    imageAspectRatio: "4/3"
    productNameTypography: "{typography.product-name}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.base}"
    hoverShadow: "0 4px 16px rgba(0,0,0,0.08)"
  product-card-dark:
    backgroundColor: "{colors.surface-dark-mid}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
    productNameTypography: "{typography.product-name}"
    priceTypography: "{typography.price-display}"
    padding: "{spacing.base}"
  badge-new:
    backgroundColor: "{colors.accent-teal}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  badge-bestseller:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge-label}"
    rounded: "{rounded.xs}"
    padding: 3px 8px
  compatibility-tag:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.tag-label}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 4px 12px
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    placeholderColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    borderFocus: "1.5px solid {colors.primary}"
    height: 44px
    padding: "0 {spacing.base}"
  category-filter-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 18px
  category-filter-inactive:
    backgroundColor: "transparent"
    textColor: "{colors.body}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    border: "1px solid {colors.hairline}"
    padding: 8px 18px
  color-swatch:
    size: 24px
    rounded: "{rounded.full}"
    borderSelected: "2px solid {colors.ink}"
    borderOffset: 2px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    linkColor: "{colors.muted-light}"
    linkColorHover: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    headingTypography: "{typography.title-sm}"
    padding: "{spacing.section} 0 {spacing.xl}"
  section-header:
    headlineTypography: "{typography.display-md}"
    subheadTypography: "{typography.body-md}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} 0 {spacing.lg}"

## Components

### Buttons

**`button-primary`** — Deep ocean teal (#045c7d) fill with white Freight Sans Pro text at 600 weight, `{rounded.sm}` corners, 48px height, 14px/28px padding. On hover the background deepens to `{colors.primary-active}` (#034b68); disabled state mutes to `{colors.primary-disabled}` at 60% opacity. Used exclusively for the primary purchase and "Add to Cart" actions.

**`button-secondary`** — Transparent fill with a 1.5px `{colors.ink}` border, same height and type scale as primary. Deployed alongside `button-primary` on product pages for secondary actions such as "Learn More" or "Find a Retailer." Hover inverts to ink fill with white text.

**`button-ghost-light`** — Identical structure to secondary but reversed for dark hero contexts: transparent fill, 1.5px white border, white label. Appears as the secondary CTA in `hero-dark` modules, never in light sections.

**`button-accent-orange`** — Hot red-orange (#ff4127) fill reserved for urgency moments: flash-sale countdowns, limited-stock alerts, and promotional landing-page heroes. Uses the same geometry as primary; should not appear alongside `button-primary` on the same row to avoid signal confusion.

### Text Inputs

**`text-input`** — White fill, 1px `{colors.hairline}` border at rest, 1.5px `{colors.primary}` teal border on focus; `{rounded.sm}` keeps the input consistent with the button family. Placeholder text runs in `{colors.muted}` (#637473). Applied to search overlays, email capture forms, and the checkout address flow.

### Navigation

**`announcement-bar`** — 40px full-width strip in `{colors.ink}` (#121713) with `{typography.caption}` white copy and `{colors.accent-teal}` (#00caaa) inline links for promotions. Sits above the main nav and collapses or hides at mobile breakpoints when nav real estate is tight.

**`nav-bar`** — 64px white bar with 1px bottom hairline; on scroll-into-dark-hero it transitions to `nav-bar-dark` (same height, `{colors.surface-dark}` background, white links). Logo max-height 32px preserves headroom for the category link row below it on desktop.

### Hero

**`hero-dark`** — Full-bleed dark module (`{colors.surface-dark}`) with `{typography.display-xl}` headline in white and optional subhead in `{typography.display-sm}`. Supports a left-aligned copy block with image or video filling the right 50% on desktop; collapses to stacked image-above-copy on mobile. Primary CTA is `button-primary` (teal); secondary is `button-ghost-light` (white outline).

**`hero-light`** — Uses the mint-tinted canvas (`{colors.surface-soft}`) for seasonal features and accessory launches that benefit from a lighter, editorial register. Headline drops to `{typography.display-lg}` at 48px; body copy in `{typography.body-md}`. Photography typically shows isolated product on white or soft gradient.

### Product Card

**`product-card`** — White card at `{rounded.sm}` with a 1px `{colors.hairline-soft}` border and a 4:3 image slot taking the full card width. Product name in `{typography.product-name}` (15px/500 weight), price in `{typography.price-display}` (condensed, 20px/700). Hover lifts with a subtle shadow `0 4px 16px rgba(0,0,0,0.08)`. Badges (`badge-new`, `badge-sale`, `badge-bestseller`) sit as absolute overlays at top-left of the image slot.

**`product-card-dark`** — Same structure but on `{colors.surface-dark-mid}` (#1a1b18) for use inside dark-background grid sections or "Featured Collection" panels. Text flips to white; border omitted.

### Badges

**`badge-new`** — Electric mint (#00caaa) fill, ink text, uppercase `{typography.badge-label}` at 11px, `{rounded.xs}` corners. Signals recent additions to the catalog.

**`badge-sale`** — Red-orange (#ff4127) fill, white text, same type and geometry. Reserved strictly for price-reduction events; never applied as a general promotional tag to keep urgency signal clean.

**`badge-bestseller`** — Warm gold (#ffcf2a) fill, ink text. Used on a small curated set of hero SKUs; appears in the image overlay and occasionally as an inline editorial callout in collection descriptions.

### Filtering and Compatibility

**`compatibility-tag`** — Pill-shaped (`{rounded.full}`) tag on `{colors.surface-soft}` with a 1px hairline border, `{typography.tag-label}` in `{colors.body}`. Applied to product cards and filter rows to denote device compatibility (e.g., "iPhone 16 Pro", "MacBook Air M3"). Non-interactive variants display inline in product detail copy; interactive variants behave as toggle filters with active state using `category-filter-active`.

**`category-filter-active`** — Ink-filled pill, white label, `{typography.button-sm}`. **`category-filter-inactive`** — hairline-bordered transparent pill. The two states form a horizontal scrolling filter row above collection grids on all breakpoints.

### Search

**`search-bar`** — Pill-shaped (`{rounded.full}`) input on `{colors.surface-soft}` with `{typography.body-sm}` placeholder text in `{colors.muted}`. Focus ring switches border to 1.5px `{colors.primary}`. An icon button (Font Awesome magnifier) sits at the trailing edge. Expands from a collapsed icon in the nav on mobile to a full-width overlay with recent searches displayed below.

### Color Swatches

**`color-swatch`** — 24px circle (`{rounded.full}`) showing the variant fill color. Selected state adds a 2px `{colors.ink}` ring with a 2px gap between swatch and ring, the standard Apple-ecosystem convention for avoiding color clash on the ring itself. Disabled swatches render at 40% opacity with a diagonal strikethrough line.

### Footer

**`footer`** — Full-bleed `{colors.ink}` (#121713) panel with four-column link grid on desktop. Column headings in `{typography.title-sm}` white; links in `{typography.body-sm}` at `{colors.muted-light}` (#9a9db1) with white hover. A newsletter email input and `button-primary` CTA occupy the top section. Social icons via Font Awesome 5 Brands in muted-light, teal on hover.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero collapses to image-above-copy stack; announcement-bar hides if nav overflows; category filter row becomes horizontal scroll strip; nav collapses to hamburger with full-screen drawer |
| Tablet | 744–1128px | Two-column product grid; hero switches to 60/40 split; filter pills remain visible but truncate with a "More" overflow control; footer collapses to two-column link grid |
| Desktop | 1128–1440px | Three- or four-column product grid depending on collection density; full horizontal nav with mega-dropdown for categories; hero at full 560px min-height with equal copy/image split |
| Wide | > 1440px | Grid and hero content max out at 1440px container with increased lateral padding (`{spacing.xxl}`); typography scales up one step in hero headline only; side margins fill with `{colors.canvas}` |

### Touch Targets

- All interactive elements meet 44×44px minimum; color swatches padded to 40px tap area despite 24px visual size
- Category filter pills padded to 40px height on mobile even when visual text size stays at 13px
- Cart and search nav icons use 48px tap targets via invisible padding expansion

### Collapsing Strategy

- Navigation mega-menu → hamburger drawer at < 1128px; drawer slides in from left, dark scrim covers content
- Four-column product grid → two-column at tablet, one-column at mobile
- Hero copy/image split → stacked (image first, then copy + CTA) at mobile
- Footer four-column → two-column at tablet, single-column accordion at mobile with expand/collapse per section
- Announcement bar text truncates to a single center-aligned line at mobile; secondary link hidden

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- No explicit border-radius values confirmed from CSS extraction; `{rounded.sm}` (8px) inferred from visual inspection of button and card geometry
- Hero headline size and exact weight between ultra-hero and display-xl not confirmed from CSS; both variants defined defensively
- Sale and discount badge exact hex values not isolated; `{colors.accent-orange}` (#ff4127) is extracted but its specific badge usage is inferred from common DTC patterns
- Exact nav height (64px) is estimated; no explicit CSS height rule extracted
- Footer background was not directly confirmed as `{colors.ink}` (#121713) vs. a near-identical dark shade (#101010 also extracted); the two are visually indistinguishable at screen resolution
- Product image aspect ratio (4:3) inferred from catalog layout; may vary by product category (cables vs. stands vs. cases)
- Animation/transition timing values not extracted; no easing curves confirmed
- Mobile mega-menu drawer direction (left vs. right slide) not confirmed
