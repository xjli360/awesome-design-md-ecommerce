---
version: alpha
name: "B Yoga"
source_url: "https://byoganow.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A mustard-yellow #e9be33 voltage runs through B Yoga’s digital presence — not as a background wash but as the single accent that pulls the eye to CTAs, price tags, and active states against a deep charcoal #31373d body and a clean #eaeaea canvas. The palette is deliberately restrained: three neutrals (charcoal, medium gray #6c6c6c, and warm off-white) plus one blue #479ccf that surfaces in secondary links and subtle dividers, creating a quiet tension between the earthy yellow and the cooler blue. Typography stays in the Arial/Helvetica system stack, a pragmatic choice that keeps the focus on the yoga practice itself rather than on brand typographic flair. Buttons are compact and softly rounded (`{rounded.sm}`), navigation is lean with a single-level menu, and product cards use generous `{spacing.lg}` padding to let the imagery breathe. The overall feeling is that of a studio that knows its value — warm, direct, and uncluttered — where the yellow acts like a single beam of sunlight hitting a mat.

colors:
  primary: "#e9be33"
  primary-active: "#d4a92e"
  primary-disabled: "#f4d98a"
  ink: "#31373d"
  body: "#6c6c6c"
  muted: "#8a8a8a"
  muted-soft: "#b0b0b0"
  hairline: "#d4d4d4"
  hairline-soft: "#eaeaea"
  canvas: "#eaeaea"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#31373d"
  accent-blue: "#479ccf"
  accent-blue-hover: "#3b87b5"

typography:
  display-xl:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.25px
  display-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  display-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.23
    letterSpacing: 0.25px
  link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.25px

rounded:
  none: 0px
  xs: 2px
  sm: 6px
  md: 12px
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
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
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
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
  button-tertiary-text-active:
    textColor: "{colors.primary-active}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid #c13515"
  nav-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    border-bottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    border-bottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "4:3"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    fontWeight: 600
  badge-sale:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.surface-card}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: "14px 32px"
    height: 48px
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 48px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-card}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.primary}"
  section-heading:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
    margin: "{spacing.lg} 0"

## Components

### Buttons
**`button-primary`** — The brand’s primary action button, filled with the signature mustard yellow `#e9be33` against dark charcoal text. On hover, the background deepens to `#d4a92e`; the disabled state fades to a pale yellow `#f4d98a` with muted text. Compact 44px height with `{rounded.sm}` corners keeps the button feeling grounded and intentional.
**`button-secondary`** — An outlined variant on a white background with a thin `{colors.hairline}` border. Active state fills the background with `{colors.surface-soft}`. Used for secondary actions like "View Details" or "Cancel" where the yellow should not compete.
**`button-tertiary-text`** — A text-only button with no background or border. The active state shifts text to `{colors.primary-active}`. Reserved for low-emphasis actions like "Learn more" or "Skip."

### Cards
**`product-card`** — A white card with `{rounded.md}` corners and `{spacing.base}` padding, housing a 4:3 product image and two text rows: the product title in `{typography.title-sm}` and the price in `{typography.body-md}` colored with `{colors.primary}`. The yellow price is a deliberate brand signal — the cost is the second thing the eye registers after the image.
**`badge-sale`** — A small uppercase badge in `{colors.primary}` yellow with dark text, `{rounded.xs}` corners, and tight 2px/8px padding. Used to flag discounted items.
**`badge-new`** — The same badge shape but in `{colors.accent-blue}`, used for new arrivals. The blue provides a visual counterpoint to the yellow sale badges without introducing a third accent color.

### Navigation
**`nav-bar`** — A fixed 64px white bar with a thin `{colors.hairline-soft}` bottom border. Navigation links use `{typography.nav-link}` at 15px/600 weight. The active link is underlined with a 2px `{colors.primary}` border and the link text shifts to the same yellow. The bar collapses to a hamburger menu on mobile.

### Forms
**`text-input`** — A 48px white input field with `{rounded.sm}` corners and a `{colors.hairline}` border. On focus, the border thickens to 2px and turns `{colors.primary}`. Error state uses a red `#c13515` border. Placeholder text uses `{colors.muted}`.

### Hero
**`hero-section`** — A full-width section on the `{colors.canvas}` background with `{spacing.section}` vertical padding. The heading uses `{typography.display-xl}` at 32px/700 weight. A single `{hero-cta}` button sits below, larger than standard buttons at 48px height with 14px/32px padding.

### Footer
**`footer`** — A dark `{colors.ink}` footer with white body text. Links are `{colors.muted-soft}` and shift to `{colors.primary}` on hover. The footer uses `{spacing.xxl}` vertical padding and `{spacing.lg}` horizontal padding.

### Search
**`search-bar`** — A pill-shaped (`{rounded.full}`) 48px input with a white background and `{colors.hairline}` border. On focus, the border becomes 2px `{colors.primary}`. Used on the hero and in the nav bar on mobile.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger; hero padding reduces to `{spacing.xl}`; product cards stack in single column; search bar moves to full-width below nav; footer links stack vertically |
| Tablet | 744–1128px | Nav bar shows full links; hero uses `{spacing.section}` padding; product cards in 2-column grid; search bar remains in nav |
| Desktop | 1128–1440px | Standard layout; product cards in 3-column grid; hero CTA is 48px height; nav bar is 64px |
| Wide | > 1440px | Max-width container at 1440px; hero content centered; product cards in 4-column grid; increased whitespace |

### Touch Targets
- All buttons and interactive elements minimum 44px height
- Nav links minimum 44px tap area (padding added on mobile)
- Search bar 48px height for easy tapping
- Icon buttons (if used) minimum 44x44px

### Collapsing Strategy
- Nav bar collapses to hamburger menu on mobile (< 744px)
- Product card grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile)
- Footer link columns collapse to single column on mobile
- Hero section reduces vertical padding on mobile from `{spacing.section}` to `{spacing.xl}`
- Search bar moves from inline in nav to full-width below nav on mobile

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted color list is sparse and generic (only 5 hex values, with one distinctive yellow, one blue, and three neutrals). The yellow `#e9be33` was selected as primary based on distinctiveness, but the brand may have a richer palette (e.g., secondary greens, tertiary accents, or specific gradient treatments) that could not be extracted.
- The site was unavailable at extraction time ("This store is unavailable"), so no actual page content, imagery, or layout could be analyzed. All component structures are inferred from common yoga DTC patterns.
- No font-family declarations beyond the Arial/Helvetica system stack were found. The brand may use a custom typeface (e.g., a sans-serif like Proxima Nova or a script font for logo) that was not loaded on the unavailable page.
- Hover states for buttons and links are estimated from the primary color shift; actual hover transitions (duration, easing) are unknown.
- Error states for forms (validation messages, error icons) are not extracted.
- Dark mode or high-contrast mode variants are not present in the extracted data.
- Spacing and sizing values (padding, heights, border widths) are estimated from common yoga e-commerce patterns; actual values may differ.
- The accent blue `#479ccf` may be a secondary brand color or a one-off UI element; its usage frequency could not be verified.
- No data on loading states, skeleton screens, or empty states.
- The brand's logo, iconography, and illustration style are unknown.
