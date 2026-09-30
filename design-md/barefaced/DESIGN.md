---
version: alpha
name: "Barefaced"
source_url: "https://www.barefaced.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  Barefaced is a skincare brand that communicates calm, clinical confidence through a restrained palette anchored on a deep forest green (`#0e3c31`) and a warm off-white canvas (`#fdf7f0`). The brand's voice is one of expert minimalism — it promises "simplified skincare" and delivers that promise through generous whitespace, soft edges (`{rounded.md}` for cards, `{rounded.sm}` for buttons), and a typographic hierarchy that pairs the clean, modern sans-serif of Inter with the editorial warmth of Newsreader. The primary green (`{colors.primary}`) appears on every CTA button and key accent, while a muted sage (`#e5edeb`) and a soft neutral (`#dedede`) provide background depth without competing for attention. A vibrant lime (`#ecfbb0`) and a coral accent (`#ef8367`) are used sparingly for badges, sale markers, and secondary highlights, injecting just enough energy to keep the palette from feeling somber. The overall mood is spa-meets-science: trustworthy, unhurried, and utterly free of the frantic, high-saturation tropes common in mass skincare. Every design decision — from the pill-shaped search bar to the generous `{spacing.section}` between product rows — reinforces the idea that skincare should be simple, effective, and beautiful.

colors:
  primary: "#0e3c31"
  primary-active: "#041e29"
  primary-disabled: "#6aa5a3"
  ink: "#041e29"
  body: "#121212"
  muted: "#6aa5a3"
  muted-soft: "#c8c8c8"
  hairline: "#dedede"
  hairline-soft: "#e5edeb"
  canvas: "#fdf7f0"
  surface-soft: "#fbf6f2"
  surface-card: "#ffffff"
  on-primary: "#fdf7f0"
  accent-lime: "#ecfbb0"
  accent-coral: "#ef8367"
  accent-gold: "#ee9441"
  badge-green: "#006400"
  badge-red: "#8b0000"
  success: "#3ed660"
  info: "#1990c6"
  info-dark: "#136f99"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Newsreader', 'Inter', 'BrandAccentFont', serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -1px
  display-lg:
    fontFamily: "'Newsreader', 'Inter', 'BrandAccentFont', serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Newsreader', 'Inter', 'BrandAccentFont', serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.3px
  link:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Inter', 'BrandBodyFont', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0.2px
  subheading:
    fontFamily: "'Newsreader', 'BrandSubheadingFont', serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
    fontStyle: italic

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
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    border: "2px solid {colors.primary-active}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 8px 16px
  button-pill:
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
    padding: 10px 24px
    border: "1.5px solid {colors.primary}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.badge-red}"
  text-input-disabled:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted-soft}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(4, 30, 41, 0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.body}"
  badge-new:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-bestseller:
    backgroundColor: "{colors.accent-gold}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.section} {spacing.lg}"
  hero-heading:
    typography: "{typography.display-xl}"
    textColor: "{colors.on-primary}"
  hero-subheading:
    typography: "{typography.subheading}"
    textColor: "{colors.on-primary}"
    opacity: 0.9
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 20px"
    height: 52px
    boxShadow: "0 2px 8px rgba(4, 30, 41, 0.06)"
  search-bar-focus:
    boxShadow: "0 2px 12px rgba(14, 60, 49, 0.15)"
  footer:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    typography: "{typography.link}"
    textColor: "{colors.on-primary}"
    opacity: 0.8
  footer-link-hover:
    opacity: 1
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.hairline-soft}"
  accordion-header:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
    padding: "{spacing.base} {spacing.lg}"
  accordion-content:
    padding: "0 {spacing.lg} {spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Add to Cart", "Shop Now", and "Subscribe". It uses the brand's deep forest green (`{colors.primary}`) background with warm off-white text (`{colors.on-primary}`) and a softly rounded 8px corner (`{rounded.sm}`). On hover/active, the background deepens to `{colors.primary-active}` (#041e29). The disabled state uses a muted sage (`{colors.primary-disabled}`) to indicate unavailability without visual noise. **`button-secondary`** — An outlined variant with a transparent background and a 2px `{colors.primary}` border, used for "Learn More" and secondary checkout actions. Active state swaps the border to `{colors.primary-active}` and adds a subtle `{colors.surface-soft}` background. **`button-ghost`** — A text-only button with no border or background, used for "Cancel" and "Back" actions; it inherits `{colors.primary}` text and respects the same typographic scale. **`button-pill`** — A fully rounded variant (`{rounded.full}`) used for promotional badges and quick-add actions on mobile; it uses the same primary color scheme but at a smaller `{typography.button-sm}` size. **`button-pill-outline`** — The outlined pill counterpart, used for filter tags and "Clear All" actions.

### Cards
**`product-card`** — The primary product display unit, a white card (`{colors.surface-card}`) with 12px rounded corners (`{rounded.md}`) and 16px internal padding. Each card contains a square product image with 8px rounded corners (`{rounded.sm}`), a title in `{typography.title-sm}`, and a price in `{typography.body-md}`. On hover, the card lifts with a subtle box-shadow (`0 4px 12px rgba(4, 30, 41, 0.08)`). Badges (New, Sale, Bestseller) are positioned at the top-left of the image area, using `{rounded.xs}` corners and uppercase `{typography.badge}` text. The card layout is responsive: single column on mobile, two columns on tablet, three or four columns on desktop.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 72px height with a white background (`{colors.canvas}`) and a thin bottom border (`{colors.hairline-soft}`). Navigation links use `{typography.nav-link}` (14px, medium weight) with `{colors.ink}` text. The active link is underlined with a 2px `{colors.primary}` border. The nav includes a centered logo (using the brand's wordmark in `{colors.primary}`), a search icon that expands into the `{search-bar}` component, a cart icon with a badge count, and a hamburger menu on mobile. On tablet and mobile, the full link set collapses into a slide-out drawer.

### Forms
**`text-input`** — Standard text input fields for email, name, and search queries. They use a white background (`{colors.canvas}`), 8px rounded corners (`{rounded.sm}`), and a 1px `{colors.hairline}` border. On focus, the border thickens to 2px and turns `{colors.primary}`. Error states use a 2px `{colors.badge-red}` border. Disabled inputs fade to `{colors.surface-soft}` background with `{colors.muted-soft}` text. The input height is 48px with 12px vertical and 16px horizontal padding.

### Footer
**`footer`** — A full-width footer with a `{colors.primary}` background and `{colors.on-primary}` text. It contains three columns: brand description and social links, quick links (About, Ingredients, Sustainability, FAQ), and a newsletter signup form. Footer links use `{typography.link}` at 80% opacity, increasing to full opacity on hover. The newsletter input is a `{text-input}` variant with a white background and a `{button-primary}` submit. The footer includes a thin top border in `{colors.primary-active}` for visual separation from the main content area.

### Hero
**`hero-section`** — The primary hero banner, typically the first thing a visitor sees. It uses a `{colors.primary}` background with `{colors.on-primary}` text. The heading uses `{typography.display-xl}` (48px Newsreader) and a subheading in `{typography.subheading}` (20px italic Newsreader) at 90% opacity. The hero includes a prominent `{button-primary}` CTA and optional background imagery (product shots or lifestyle photography) that sits behind a subtle gradient overlay. On mobile, the hero reduces to a single-column layout with the image stacking below the text.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid, hamburger nav, hero stacks vertically, search bar collapses to icon, footer stacks columns |
| Tablet | 744–1128px | Two-column product grid, full nav links visible, hero maintains side-by-side layout, search bar expands on tap |
| Desktop | 1128–1440px | Three-column product grid, full nav with search bar visible, hero full-width with large imagery, footer in three columns |
| Wide | > 1440px | Four-column product grid, max-width container at 1440px, hero may include parallax or video background |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum touch target of 44x44px.
- Icon buttons (cart, search, hamburger) are 48x48px with `{rounded.full}` corners.
- Product card tap targets extend to the full card area.
- Accordion headers are 48px tall for easy tapping.

### Collapsing Strategy
- The top navigation link set collapses into a hamburger drawer below 744px.
- The product grid collapses from 4 columns to 2 columns at tablet, then 1 column at mobile.
- The footer's three-column layout stacks vertically on mobile.
- The search bar collapses to a search icon on mobile, expanding to a full-width overlay on tap.
- The hero section's side-by-side layout collapses to a stacked layout on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be fully extracted; only primary and secondary buttons have confirmed hover/active colors.
- Error styling for forms (validation messages, error icons) is inferred from common patterns; exact error text color and iconography are not confirmed.
- Dark mode is not present on the live site; all tokens assume light mode only.
- Sub-brand or collection-specific palettes (e.g., for "Men's Routine" or "The Essentials") were not observed.
- Animation and transition timing values (ease-in-out durations, spring curves) were not extractable from static CSS.
- The exact `font-weight` values for Newsreader and Inter in display roles are estimated based on common usage; the site may use variable font weights.
- The `BrandAccentFont`, `BrandBodyFont`, and `BrandSubheadingFont` custom font-family names are placeholders; their actual font files and weights are not publicly documented.
- Modal, tooltip, and toast component designs were not observed on the live site.
- The site's Shopify platform may introduce platform-specific components (e.g., cart drawer, checkout button) that are not fully captured here.
