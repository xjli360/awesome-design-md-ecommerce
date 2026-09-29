---
version: alpha
name: "Dungeons & Dragons"
source_url: "https://dnd.wizards.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A deep, saturated #de8435 — the color of aged parchment, dragon-scale, and well-worn rulebooks — anchors the Dungeons & Dragons brand as the single accent voltage across a cool, misty canvas of #bdd6e6, a pale blue that reads like morning fog over a fantasy landscape. The site’s visual language is built on a tension between the arcane and the accessible: sharp, angular badges with {rounded.none} corners sit alongside pill-shaped CTAs at {rounded.full}, while the primary button’s {rounded.sm} offers a middle ground. The typography, set in a robust sans-serif with generous tracking on display sizes, carries the weight of epic storytelling without resorting to medieval pastiche — no faux-gothic serifs, no drop caps. Navigation is a dark, full-width band that anchors the page, with a search bar that appears only on interaction, preserving the immersive canvas. Product cards for sourcebooks and adventures use a soft {rounded.md} and a subtle shadow, letting cover art do the heavy lifting. The brand trusts its imagery — sprawling dragon art, character illustrations, and map fragments — over decorative UI chrome. The result is a portal that feels both ancient and immediate: a tavern common room rendered in CSS, where the hex codes themselves tell a story of treasure maps and twilight skies.

colors:
  primary: "#de8435"
  primary-active: "#c46f2a"
  primary-disabled: "#f0cfa0"
  ink: "#1a1a2e"
  body: "#2d2d44"
  muted: "#6b6b80"
  muted-soft: "#9a9aad"
  hairline: "#c8c8d4"
  hairline-soft: "#e0e0e8"
  canvas: "#ffffff"
  surface-soft: "#f4f4f8"
  surface-card: "#ffffff"
  surface-dark: "#1a1a2e"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-blue: "#bdd6e6"
  accent-blue-soft: "#d4e4f0"
  accent-gold: "#de8435"
  accent-gold-light: "#f5d6a8"
  badge-red: "#c0392b"
  badge-green: "#27ae60"
  link: "#de8435"
  link-hover: "#c46f2a"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Roboto Condensed', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Roboto Condensed', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Roboto Condensed', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  title-lg:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0
  badge:
    fontFamily: "'Roboto Condensed', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roboto Condensed', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Roboto Condensed', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  link:
    fontFamily: "'Roboto', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Roboto Condensed', 'Impact', 'Arial Narrow', sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0.5px
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
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 11px 27px
    height: 44px
    border: "2px solid {colors.hairline}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    border: "2px solid {colors.primary}"
  button-pill-gold:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    border: "2px solid {colors.primary}"
  icon-button-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.full}"
    height: 40px
  icon-button-light:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
  top-nav:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
  search-bar-active:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px 0px 16px 0px
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0px 0px"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: 12px 16px 4px 16px
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.primary}"
    padding: 0px 16px 12px 16px
  badge-new:
    backgroundColor: "{colors.badge-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: 2px 8px
  badge-category:
    backgroundColor: "{colors.accent-blue-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: 4px 12px
  hero-section:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    padding: 80px 24px
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.on-dark}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted-soft}"
  footer:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: 48px 24px
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
  footer-link-hover:
    color: "{colors.primary}"
  divider:
    backgroundColor: "{colors.hairline-soft}"
    height: 1px
  divider-dark:
    backgroundColor: "{colors.hairline}"
    height: 1px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Buy Now", "Pre-Order", and "Join the Adventure" flows. On hover, the gold shifts to `{colors.primary-active}` (#c46f2a) for a subtle darkening effect. Disabled state uses `{colors.primary-disabled}` (#f0cfa0) with muted text, signaling an unavailable action. The uppercase `{typography.button-md}` with 0.5px letter-spacing gives the button a heraldic weight.

**`button-secondary`** — An outlined alternative for less critical actions like "Learn More" or "View Details". The 2px `{colors.hairline}` border keeps it grounded, while the active state swaps the border to `{colors.primary}` gold. Padding is 1px less on each side than primary to account for the border.

**`button-pill-gold`** — A fully rounded variant used for promotional banners, newsletter signups, and "Get Started" CTAs in hero sections. The pill shape (`{rounded.full}`) reads as more approachable than the standard `{rounded.sm}` primary button.

**`button-pill-outline`** — The transparent counterpart to the pill gold, used for secondary actions in dark-background hero sections. The 2px gold border maintains brand consistency while the transparent background lets the hero imagery breathe.

### Cards
**`product-card`** — The primary content container for sourcebooks, adventure modules, and accessories. The card uses a white background with `{rounded.md}` corners and no border — the shadow is handled by the parent grid. The image area has its own `{rounded.md}` on top corners only, creating a seamless transition to the content below. Title and price are stacked with 12px padding on top and 16px on sides.

**`badge-new`** — A green pill badge for newly released products, using `{typography.badge}` (11px uppercase Roboto Condensed) for maximum readability at small sizes.

**`badge-sale`** — A red badge for discounted items, following the same pattern as `badge-new` but with `{colors.badge-red}`.

**`badge-category`** — A soft blue pill badge used to tag content types ("Adventure", "Sourcebook", "Accessory") in filter strips and card metadata. The `{colors.accent-blue-soft}` background ties back to the site's cool canvas.

### Navigation
**`top-nav`** — A full-width dark band (`{colors.surface-dark}`) at 64px height, housing the D&D logo on the left and navigation links on the right. Links use `{typography.nav-link}` (14px uppercase, 700 weight, 0.5px tracking) for a commanding but clean presence. Active links glow in `{colors.primary}` gold.

**`nav-link-active`** — The active navigation state, distinguished by the gold text color. No underline or background change — the color shift alone signals the current section.

**`nav-link-inactive`** — The default navigation state, using white text on the dark background. Hover state transitions to `{colors.primary}` with a 200ms ease-in-out.

### Forms
**`search-bar`** — A full-rounded input field for the site search, appearing in the top nav on desktop and as a full-width element on mobile. The `{rounded.full}` shape and generous 20px horizontal padding make it feel approachable. Active state adds a 2px gold border.

**`search-bar-active`** — The focused state, distinguished by the `{colors.primary}` border. The background remains white for contrast against the dark nav.

### Hero
**`hero-section`** — The primary brand introduction area, using the dark `{colors.surface-dark}` background to create a dramatic stage for fantasy artwork. 80px vertical padding provides generous breathing room. The `hero-title` uses `{typography.display-xl}` at 48px for maximum impact, while the `hero-subtitle` in `{typography.body-md}` provides context in a softer `{colors.muted-soft}` tone.

### Footer
**`footer`** — A dark anchor for the page, matching the top nav in background. Links use `{colors.muted-soft}` for readability without competing with primary content. Hover state shifts to `{colors.primary}` gold, creating a consistent interaction language with the rest of the site.

### Dividers
**`divider`** — A 1px hairline used to separate content sections on light backgrounds. The `{colors.hairline-soft}` value keeps it subtle.

**`divider-dark`** — A slightly stronger hairline for use on dark backgrounds, using `{colors.hairline}` for better visibility.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column grid; hero padding reduces to 48px 16px; top-nav collapses to hamburger menu; product cards stack vertically; search bar becomes full-width below nav; badges stack on mobile cards |
| Tablet | 744–1128px | Two-column product grid; top-nav remains expanded but reduces link font-size to 12px; hero uses 60px vertical padding; search bar appears as icon-only in nav |
| Desktop | 1128–1440px | Three-column product grid; full top-nav with all links visible; hero uses 80px padding; search bar expands to full input in nav |
| Wide | > 1440px | Four-column product grid; max-width container at 1440px; hero uses 100px padding; additional whitespace around content sections |

### Touch Targets
- All interactive elements (buttons, links, badges) maintain minimum 44px touch target height on mobile
- Icon buttons use 40px diameter for comfortable tapping
- Product card CTAs are at least 48px tall on touch devices
- Navigation hamburger menu toggle is 44x44px minimum

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Hero section reduces vertical padding by 40% on mobile
- Search bar collapses to icon-only in nav on tablet, expands to full-width below nav on mobile
- Footer link columns stack vertically on mobile, with 24px spacing between groups
- Badge text truncates to "NEW" or "SALE" on mobile, with full text on hover/tap

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Typography**: No font-family declarations were extracted from the live site. The typography system above uses Roboto Condensed for display/button text and Roboto for body text as a reasonable sans-serif pairing for a gaming brand, but the actual brand font (if any) is unknown. A custom fantasy typeface may be in use.
- **Color palette**: Only two hex colors were extracted (#bdd6e6, #de8435). The full palette above is constructed around these as primary and secondary accents, but the actual brand may have additional colors (e.g., a deep purple for magic, a forest green for ranger themes) that could not be captured.
- **Hover states**: Button and link hover colors are inferred from the primary-active value. Actual hover transitions, shadows, or scale effects are unknown.
- **Error states**: Form validation styling (error borders, error messages, success states) could not be extracted.
- **Dark mode**: No dark mode implementation was detected. The site appears to use a light canvas with dark navigation as its primary mode.
- **Animation**: Transition durations, easing curves, and micro-interactions (card hover lifts, button press effects) are not documented.
- **Sub-brand palettes**: Different D&D product lines (e.g., Critical Role, Magic: The Gathering crossovers, video games) may use distinct color systems not captured here.
- **Accessibility**: Contrast ratios, focus indicators, and screen reader patterns are not verified.
- **Icon system**: The site likely uses custom icons (dice, dragons, shields) that are not documented in this token system.
