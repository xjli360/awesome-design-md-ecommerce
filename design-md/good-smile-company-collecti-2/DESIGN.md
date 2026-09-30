---
version: alpha
name: "Good Smile Company"
source_url: "https://www.goodsmile.info"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A collector's portal where the brand voltage comes from a single, unmistakable orange — #ff6600, the same saturated heat that powers every primary CTA, every "Pre-Order" badge, and every price-highlight on the product grid. This is not a warm neutral or a muted coral; it is a direct, unapologetic pop against a canvas of #eeeeee and #f4f4f4, a system that trusts high-contrast accent over decorative texture. The typography stack is a pragmatic Japanese-international hybrid — Helvetica Neue and Hiragino Kaku Gothic Pro sitting side by side, Meiryo and MS PGothic for body fallback, all at modest weights that let the product photography (figures, statues, Nendoroids) carry the emotional weight. Buttons are pill-shaped (`{rounded.full}`), product cards are softly rounded (`{rounded.sm}` ~8px), and the search bar lives as a full-width field rather than an icon, signaling a catalog-first browsing logic. The secondary palette is a grab-bag of web-framework defaults — #0044cc link blue, #41d728 success green, #b94a48 error red — suggesting a site built on a shared CMS skeleton rather than a bespoke design system, but the orange (#ff6600, #ff8400 in the meta theme-color, #ff5900 on hover) is the single thread that makes it feel like a brand. The footer is dense, the nav is text-heavy, and the hero section uses large display typography over full-bleed product imagery — this is a storefront built for scrolling, not for lingering.

colors:
  primary: "#ff6600"
  primary-active: "#ff5900"
  primary-disabled: "#ffbb77"
  ink: "#222222"
  body: "#555555"
  muted: "#888888"
  muted-soft: "#aaaaaa"
  hairline: "#e6e6e6"
  hairline-soft: "#f0f0f0"
  canvas: "#ffffff"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  link: "#0044cc"
  link-visited: "#3a87ad"
  success: "#41d728"
  error: "#b94a48"
  error-soft: "#ee5f5b"
  warning: "#f89406"
  warning-soft: "#fbb450"
  info: "#0088cc"
  info-soft: "#5bc0de"
  meta-theme: "#ff8400"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, 'MS PGothic', sans-serif"
    fontSize: 32px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  title-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, 'MS PGothic', sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, 'MS PGothic', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, 'MS PGothic', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, 'MS PGothic', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  price:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, 'Hiragino Kaku Gothic Pro', Meiryo, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: 0

rounded:
  none: 0px
  xs: 4px
  sm: 8px
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
    rounded: "{rounded.full}"
    padding: 12px 28px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 11px 27px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-link:
    backgroundColor: transparent
    textColor: "{colors.link}"
    typography: "{typography.link}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 14px
    height: 44px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.error}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
  nav-link-active:
    textColor: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0px
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.price}"
    color: "{colors.primary}"
    padding: "0 {spacing.base} {spacing.sm}"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-preorder:
    backgroundColor: "{colors.warning}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-soldout:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "10px 16px"
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.canvas}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.surface-soft}"
    padding: "{spacing.section} {spacing.lg}"
  hero-title:
    typography: "{typography.display-xl}"
    color: "{colors.ink}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.body}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, rendered as a pill-shaped button in the brand's signature orange (#ff6600). Uses white text on the orange background for maximum contrast. On hover, the background shifts to `{colors.primary-active}` (#ff5900), a slightly deeper orange. The disabled state uses `{colors.primary-disabled}` (#ffbb77), a washed-out peach-orange that signals non-interactivity without introducing a gray.

**`button-secondary`** — A white pill button with dark text, used for secondary actions like "View Details" or "Cancel." The border is implicit via the white canvas background; on hover, the background shifts to `{colors.surface-soft}` (#f5f5f5) to indicate interactivity. Same height and typography as the primary button for visual consistency.

**`button-link`** — A text-only link styled as a button, using the standard link blue (#0044cc). No background, no border, no rounding. Used for "Learn More" or "See All" links within content sections.

### Cards
**`product-card`** — The core content container for the product grid. A white card with `{rounded.sm}` (8px) corners, no border, and no shadow — the card relies on the contrast between the white surface and the `{colors.surface-soft}` (#f5f5f5) background of the grid area. The product image occupies the top of the card with rounded top corners only (`{rounded.sm} {rounded.sm} 0 0`). The title uses `{typography.title-sm}` (16px, 600 weight) and the price uses `{typography.price}` (16px, 700 weight) in the brand orange.

**`badge-new`** — A small orange badge with white uppercase text, used to flag newly released products. The `{rounded.xs}` (4px) corners give it a sharp, tag-like appearance. The `badge-preorder` variant uses the warning yellow (#f89406) with dark text, and `badge-soldout` uses a muted gray (#aaaaaa) with white text.

### Navigation
**`nav-bar`** — A fixed-height (60px) white navigation bar with dark text links. The active nav link is indicated by a 2px orange bottom border and orange text color. The nav is text-heavy, with no icon-only links — consistent with a catalog-first browsing experience. The bar is full-width and sticky at the top of the viewport.

### Forms
**`text-input`** — A standard text input field with `{rounded.sm}` (8px) corners, white background, and dark text. On focus, the border switches to a 2px orange stroke. On error, the border switches to a 2px red stroke (#b94a48). The input height is 44px, matching the button height for form alignment.

### Search
**`search-bar`** — A full-width search field with a soft gray background (`{colors.surface-soft}`) and `{rounded.sm}` corners. Unlike icon-only search patterns, this is a visible text field with placeholder text, reflecting the catalog-heavy nature of the site. The field is 44px tall, matching the button and input heights.

### Footer
**`footer`** — A dark footer (`{colors.ink}` #222222) with white text. Links are white and use `{typography.link}` (14px, 400 weight). The footer padding is generous (`{spacing.xxl}` top and bottom, `{spacing.lg}` left and right), creating a visual anchor at the bottom of the page. The footer is dense with text links, organized in columns.

### Hero
**`hero-section`** — A full-width hero area with a soft gray background (`{colors.surface-soft}`) and large display typography. The title uses `{typography.display-xl}` (32px, 700 weight) and the subtitle uses `{typography.body-md}` (15px, 400 weight). The hero is designed to showcase product imagery — typically a full-bleed photo of a featured figure or statue — with the text overlaid or positioned to the side.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column product grid (1 card per row), nav collapses to hamburger menu, hero text stacks vertically, search bar moves below nav, footer links collapse into accordion |
| Tablet | 744–1128px | Two-column product grid, nav links remain visible but condensed, hero uses side-by-side layout, search bar is inline in nav |
| Desktop | 1128–1440px | Three-column product grid, full nav with all links visible, hero uses full-width layout with text overlay, search bar is prominent in nav |
| Wide | > 1440px | Four-column product grid, max-width container (1440px) centered, hero image scales up, additional whitespace around content |

### Touch Targets
- All buttons and links have a minimum touch target of 44px x 44px (meeting WCAG 2.1 guidelines).
- Product card images are tappable and link to the product detail page.
- Badges are informational only and are not tappable.
- The search bar has a minimum touch target of 44px height.

### Collapsing Strategy
- On mobile (< 744px), the top navigation collapses into a hamburger menu with a slide-out drawer.
- The product grid collapses from 4 columns (wide) to 1 column (mobile).
- The footer link columns collapse into an accordion pattern on mobile, with expandable sections.
- The hero section reduces font sizes on mobile (`{typography.display-lg}` instead of `{typography.display-xl}`) and stacks text vertically below the image.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states for secondary elements** — Hover colors for `button-secondary`, `text-input`, and `nav-link` are inferred from common web patterns, not extracted from the live site.
- **Error and validation styling** — The error state for `text-input` uses a generic red (#b94a48) from the extracted palette, but the actual error message styling (font size, color, icon) could not be determined.
- **Sub-brand or collection-specific palettes** — Good Smile Company has multiple product lines (Nendoroid, Figma, etc.) that may have their own accent colors. These were not extractable from the main site.
- **Dark mode** — No dark mode implementation was detected. All extracted colors are light-mode.
- **Animation and transition timing** — No CSS transition durations or easing functions were extracted. Default to 200ms ease-in-out for hover states.
- **Shadow and elevation** — No box-shadow values were extracted. Product cards appear to be flat (no shadow), but this could not be confirmed.
- **Font weights beyond 700** — The extracted font stack includes standard web fonts, but no variable font weights or custom font files were detected. The site may use a custom font not captured in the extraction.
- **The extracted color palette is heavily polluted with framework defaults** (Bootstrap blues, greens, reds, and grays). The true brand palette is likely much smaller — centered on #ff6600 (primary orange), #222222 (ink), #ffffff (canvas), and a few grays. The additional colors (#0044cc, #41d728, #b94a48, #f89406, #0088cc) are standard web framework colors and may not represent intentional brand choices.
