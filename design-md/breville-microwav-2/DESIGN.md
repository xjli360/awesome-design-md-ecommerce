---
version: alpha
name: "Breville"
source_url: "https://www.breville.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  Brushed aluminum given a URL — that is the immediate impression of Breville's digital surface. Where most appliance brands flood their pages with lifestyle photography and pastel gradients, Breville leads with a near-monochrome charcoal palette built on #313638, the dense ink that darkens navigation bars, headline type, and product titling like the die-cast housing of a Barista Express. Warmth enters through a single burnt-orange accent (#d35b17) reserved almost exclusively for primary CTAs and promotional badges; it reads like a heating element glowing behind tempered glass — present but disciplined. Typography pairs Archer — a geometric slab-serif from Hoefler&Co in both its Screen Smart (`Archer-Ssm`) and Book weights — with a system sans-serif stack for body copy. This split gives product names and section headlines a premium-editorial tone (`{typography.display-xl}` at 600 weight, 40px) while keeping long-form descriptions crisp at `{typography.body-md}` 16px/1.6. Cards carrying $400+ countertop ovens sit on `{colors.surface-soft}` (#f5f5f5) with `{rounded.sm}` corners and a 1px `{colors.hairline}` border — no drop-shadows, no depth tricks, trusting the product photography to do the selling. A deep plum (#421540) surfaces in limited-edition or "Luxe" tier call-outs, and a teal (#046b99) marks informational links and comparison toggles. Spacing is generous: section gaps at `{spacing.section}` (64px) let each product hero breathe, while inline spec tables compress to `{spacing.sm}` row padding so dense information stays scannable. The overall system reads as an engineer's showroom — precise, restrained, and confident that the machines themselves are the spectacle.

colors:
  primary: "#d35b17"
  primary-active: "#b84d13"
  primary-disabled: "#eaad88"
  ink: "#313638"
  body: "#555555"
  muted: "#686563"
  muted-soft: "#7c7b78"
  hairline: "#e0e0e0"
  hairline-soft: "#e8e8e8"
  border-strong: "#d0d0d0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  surface-warm: "#cec1b5"
  surface-dark: "#2d2c2f"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  navy: "#13294b"
  plum: "#421540"
  teal: "#046b99"
  cyan-highlight: "#00bbff"
  success: "#007a31"
  error: "#d32f2f"
  warm-gray: "#bab9b8"
  steel: "#7c7b78"
  info-surface: "#e8f4fd"

typography:
  display-xl:
    fontFamily: "'Archer-Ssm', 'Archer-Book', Georgia, serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Archer-Ssm', 'Archer-Book', Georgia, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'Archer-Ssm', 'Archer-Book', Georgia, serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Archer-Ssm', 'Archer-Book', Georgia, serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.2px
  button-md:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.2px
  spec-label:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  spec-value:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  price-display:
    fontFamily: "'Archer-Ssm', 'Archer-Book', Georgia, serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  nav-link:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
    letterSpacing: 0
  uppercase-tag:
    fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.8px
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
    rounded: "{rounded.xs}"
    padding: 14px 28px
    height: 48px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.xs}"
    padding: 13px 27px
    height: 48px
    border: 1px solid {colors.ink}
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xs}"
    border: 1px solid {colors.ink}
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.teal}"
    typography: "{typography.button-sm}"
    padding: 8px 0
    border: none
    textDecoration: underline
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px
    height: 48px
    border: 1px solid {colors.border-strong}
    focusBorder: 1px solid {colors.ink}
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    borderBottom: 1px solid {colors.hairline}
    padding: 0 {spacing.xl}
  nav-bar-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 {spacing.xl}
  product-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    border: 1px solid {colors.hairline-soft}
    hoverBorder: 1px solid {colors.border-strong}
    imageAspectRatio: 1:1
    titleTypography: "{typography.title-md}"
    priceTypography: "{typography.price-display}"
    descriptionTypography: "{typography.body-sm}"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.xxl}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaStyle: button-primary
    minHeight: 480px
    imagePosition: right
  hero-banner-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    padding: "{spacing.section} {spacing.xxl}"
    headlineTypography: "{typography.display-xl}"
    subheadTypography: "{typography.body-md}"
    ctaStyle: button-primary
  category-tile:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "{spacing.lg}"
    titleTypography: "{typography.title-sm}"
    imageAspectRatio: 4:3
    hoverTransform: translateY(-2px)
  spec-table-row:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    padding: "{spacing.sm} 0"
    borderBottom: 1px solid {colors.hairline-soft}
    labelTypography: "{typography.spec-label}"
    valueTypography: "{typography.spec-value}"
    labelWidth: 40%
  product-badge:
    backgroundColor: "{colors.plum}"
    textColor: "{colors.on-dark}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  product-badge-sale:
    backgroundColor: "{colors.error}"
    textColor: "{colors.on-primary}"
    typography: "{typography.uppercase-tag}"
    rounded: "{rounded.xs}"
    padding: 4px 8px
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.xs}"
    padding: 12px 16px 12px 44px
    height: 48px
    border: 1px solid {colors.border-strong}
    iconColor: "{colors.muted}"
    focusBorder: 2px solid {colors.ink}
  breadcrumb:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.caption}"
    separatorColor: "{colors.muted-soft}"
    activeColor: "{colors.ink}"
    padding: "{spacing.md} 0"
  comparison-toggle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.teal}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.xs}"
    padding: 8px 16px
    border: 1px solid {colors.teal}
    activeBackgroundColor: "{colors.info-surface}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.warm-gray}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xxl}"
    headingTypography: "{typography.title-sm}"
    headingColor: "{colors.on-dark}"
    linkColor: "{colors.warm-gray}"
    linkHoverColor: "{colors.on-dark}"
    borderTop: none
  rating-stars:
    filledColor: "{colors.primary}"
    emptyColor: "{colors.hairline}"
    size: 16px
    gap: 2px
  color-swatch:
    rounded: "{rounded.full}"
    size: 32px
    border: 2px solid {colors.hairline}
    selectedBorder: 2px solid {colors.ink}
    gap: "{spacing.sm}"
  info-banner:
    backgroundColor: "{colors.info-surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base} {spacing.lg}"
    iconColor: "{colors.teal}"
    border: 1px solid {colors.teal}

---

## Components

### Buttons

**`button-primary`** — The burnt-orange (#d35b17) rectangle with tight `{rounded.xs}` corners and 600-weight sans-serif label. Hover darkens to `{colors.primary-active}`; disabled state washes to a pale apricot `{colors.primary-disabled}`. Used for "Add to Cart," "Shop Now," and primary form submissions. The compact 4px radius signals precision rather than friendliness.

**`button-secondary`** — White fill with a 1px `{colors.ink}` border and matching dark label text. On hover the fill shifts to `{colors.surface-soft}` to subtly acknowledge interaction without competing with the primary CTA. Used for "Compare," "Find a Store," and secondary navigation actions.

**`button-tertiary`** — A text-only link styled in `{colors.teal}` with underline decoration. No background, no border. Used inline within paragraphs and spec tables for "Learn more" and "View details" links.

### Navigation

**`nav-bar`** — A 64px-tall white bar with a subtle bottom hairline border. Logo sits left, category links center in `{typography.nav-link}` (14px, weight 500), utility icons (search, account, cart) right. On scroll it gains a thin box-shadow.

**`nav-bar-dark`** — Alternate dark variant (`{colors.surface-dark}`) used on product landing pages where the hero image is light. White text, no bottom border. Transitions to the light variant after scrolling past the hero.

### Product Display

**`product-card`** — A rectangular card on `{colors.surface-soft}` with `{rounded.sm}` corners and a 1:1 product image at top. Title in `{typography.title-md}` (Archer slab-serif), price in `{typography.price-display}`, and a one-line description in `{typography.body-sm}`. The border intensifies on hover from `{colors.hairline-soft}` to `{colors.border-strong}`, providing a mechanical-click feedback feel.

**`product-badge`** — Small pill in deep plum (`{colors.plum}`) with uppercase 11px white text. Used for "LUXE" or limited-edition markers. The `product-badge-new` variant uses `{colors.primary}` (orange) and `product-badge-sale` uses `{colors.error}` (red).

**`spec-table-row`** — Alternating label/value pairs separated by `{colors.hairline-soft}` lines. Labels take 40% width in `{typography.spec-label}` (500 weight), values fill remaining space in `{typography.spec-value}` (400 weight). Dense `{spacing.sm}` vertical padding keeps multi-row specs compact.

**`rating-stars`** — Five 16px stars filled in `{colors.primary}` (orange) with 2px gaps. Partial fills use a clip-path gradient. Empty stars render in `{colors.hairline}`.

### Hero & Landing

**`hero-banner`** — Full-width section with a minimum height of 480px. Headline in `{typography.display-xl}` (40px Archer, weight 600) left-aligned, product image positioned right. Background defaults to `{colors.surface-soft}` but a dark variant flips to `{colors.ink}` background with white text. CTA uses `button-primary` styling.

**`category-tile`** — A rectangular card with 4:3 product photography, `{rounded.sm}` corners, and a title in `{typography.title-sm}` below the image. On hover the card lifts 2px via translateY transform. Used in grid layouts for browsing product families.

### Search & Filtering

**`search-bar`** — A 48px input with left-aligned magnifying glass icon in `{colors.muted}`. Border is `{colors.border-strong}` at rest, thickening to 2px `{colors.ink}` on focus. Rounded at `{rounded.xs}` to match button geometry.

**`comparison-toggle`** — A small outlined button in `{colors.teal}` that activates a product comparison tray. When active, fill shifts to `{colors.info-surface}` (light blue). Used on product listing pages to select items for side-by-side spec comparison.

### Utility

**`breadcrumb`** — Horizontal chain of `{typography.caption}` links in `{colors.muted}`, separated by chevron glyphs in `{colors.muted-soft}`. The final (active) item renders in `{colors.ink}`. Sits below the nav with `{spacing.md}` vertical padding.

**`info-banner`** — A light-blue (`{colors.info-surface}`) rounded container with a teal left-border accent and a small icon. Used for shipping notices, warranty information, and promotional messages within product pages.

**`color-swatch`** — A 32px circle (`{rounded.full}`) showing a product finish option. Default border is `{colors.hairline}`; selected state switches to `{colors.ink}`. Swatches sit in a horizontal row with `{spacing.sm}` gaps.

### Footer

**`footer`** — Dark (`{colors.ink}`) full-width section with column headings in `{typography.title-sm}` rendered in white, and link lists in `{typography.body-sm}` rendered in `{colors.warm-gray}`. Links brighten to white on hover. Generous `{spacing.section}` top/bottom padding separates it from content above.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid; hero image stacks below headline; nav collapses to hamburger + search icon; spec tables go full-width; footer columns stack vertically; category tiles become horizontal scroll strip |
| Tablet | 744–1128px | Two-column product grid; hero image scales to 50% width right-aligned; nav shows top-level categories only; comparison tray fixed to bottom edge |
| Desktop | 1128–1440px | Three-column product grid; full nav with mega-menu dropdowns; hero at full 480px height; spec comparison opens as overlay modal |
| Wide | > 1440px | Content max-width caps at 1440px centered; four-column product grid on category pages; hero image bleeds to edge while text stays within max-width container |

### Touch Targets
- All interactive elements maintain a minimum 44×44px touch area on mobile
- Product cards expand tap target to full card surface including image
- Spec table rows are tappable to expand additional detail on mobile
- Color swatches increase to 40px diameter below 744px breakpoint
- Nav hamburger icon has 48×48px hit area

### Collapsing Strategy
- Mega-menu category navigation collapses to a full-screen drawer with accordion sections
- Product comparison tray transforms from side panel to bottom sheet on mobile
- Spec tables switch from side-by-side label/value to stacked layout below 480px
- Hero banner CTA becomes full-width sticky button at bottom of viewport on mobile
- Breadcrumbs truncate middle segments with "..." on mobile, showing only parent and current

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Archer-Ssm and Archer-Book are commercial typefaces from Hoefler&Co; exact weights beyond Book/Regular cannot be confirmed from extraction alone — implementation should verify available weights via font license
- No CSS custom properties or design tokens were directly extractable (site likely loads styles via bundled JS)
- Exact box-shadow values for card hover states and sticky nav not captured in color extraction
- The #421540 plum and #00bbff cyan appear in the extraction but their precise usage contexts (which pages, which states) could not be mapped without deeper interaction testing
- Animation/transition durations and easing curves not available from static extraction
- Mega-menu structure and depth could not be fully mapped from the location-chooser page that was captured
- Icon set (line weight, optical size, source library) not identified
- Exact grid gutter values between product cards were not extracted — spacing tokens are inferred from common patterns
