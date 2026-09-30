---
version: alpha
name: "Terror Vision"
source_url: "https://www.terror-vision.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A crimson pulse — `#cc3b3b` — drives Terror Vision’s identity, a blood-red that appears on every primary action, badge, and header accent, set against a near-black `#040404` canvas that feels like a theater after the lights go down. The brand lives in the tension between grindhouse grit and collector-grade polish: product grids float on `#fafafa` surfaces while footer bands and nav bars sink into `#272727` and `#1e1e1e`, creating a visual hierarchy that mimics the experience of browsing a video store’s horror section — bright callouts against dark shelves. Typography leans on Anton, a heavy all-caps display face that screams “VHS spine” at 48px, paired with Epilogue for body text at 14px in a restrained 400 weight, letting the reds and blacks do the shouting. Buttons use `{rounded.sm}` corners — sharp enough to feel deliberate, soft enough to not cut. The search bar is a `{rounded.full}` pill in `#111111` with `#aaaaaa` placeholder text, a quiet utility in a loud system. Badges in `#bd0000` carry limited-edition flags and “SOLD OUT” warnings, while `#e99292` appears sparingly as a hover-state blush on secondary controls. The overall mood is midnight-screening: high contrast, low tolerance for clutter, every red pixel earning its place.

colors:
  primary: "#cc3b3b"
  primary-active: "#bd0000"
  primary-disabled: "#e99292"
  ink: "#040404"
  body: "#111111"
  muted: "#aaaaaa"
  muted-soft: "#e1e1e1"
  hairline: "#272727"
  hairline-soft: "#1e1e1e"
  canvas: "#040404"
  surface-soft: "#1e1e1e"
  surface-card: "#fafafa"
  on-primary: "#fbfbfb"
  on-dark: "#fafafa"
  badge-red: "#bd0000"
  badge-blush: "#e99292"
  placeholder: "#aaaaaa"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'Anton', Arial, Helvetica, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 1px
  display-md:
    fontFamily: "'Anton', Arial, Helvetica, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.15
    letterSpacing: 0.5px
  title-md:
    fontFamily: "'Epilogue', Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'Epilogue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Epilogue', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Epilogue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Epilogue', Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "'Anton', Arial, Helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.18
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'Anton', Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Anton', Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'Epilogue', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Anton', Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
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
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.muted-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-tertiary:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  button-tertiary-active:
    backgroundColor: "{colors.badge-blush}"
    textColor: "{colors.primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    height: 36px
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    borderColor: "{colors.hairline}"
  text-input-active:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    borderColor: "{colors.primary}"
  text-input-error:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 40px
    borderColor: "{colors.primary-active}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 24px
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 64px
    padding: 0 24px
    borderBottom: "1px solid {colors.hairline}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    placeholderColor: "{colors.placeholder}"
  search-bar-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    borderColor: "{colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
    height: auto
  product-card-hover:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"
  product-card-image:
    rounded: "{rounded.sm} {rounded.sm} 0 0"
    aspectRatio: "1:1"
  product-card-title:
    typography: "{typography.title-sm}"
    padding: "{spacing.sm} {spacing.base}"
  product-card-price:
    typography: "{typography.body-sm}"
    padding: "0 {spacing.base} {spacing.sm}"
  badge:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    height: 20px
  badge-blush:
    backgroundColor: "{colors.badge-blush}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
    height: 20px
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    height: 400px
  hero-section-overlay:
    backgroundColor: "{colors.scrim}"
    opacity: 0.6
  footer:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.muted}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.link}"

## Components

### Buttons
**`button-primary`** — The brand’s primary call-to-action, rendered in `#cc3b3b` with white `#fbfbfb` text in Anton uppercase at 16px. Uses `{rounded.sm}` corners and 44px height for a compact, punchy silhouette. On hover or active, the background shifts to `#bd0000` for a deeper, more urgent red. Disabled state fades to `#e99292`, a pinkish blush that signals unavailability without breaking the red family.

**`button-secondary`** — A light variant on `#fafafa` card surfaces with `#040404` text, used for “Add to Cart” or “View Details” on product cards. Active state darkens the background to `#e1e1e1`. Shares the same 44px height and `{rounded.sm}` corners as the primary button, maintaining consistent vertical rhythm.

**`button-tertiary`** — A text-only link styled as a button, using `#cc3b3b` on a transparent background with smaller 13px Anton uppercase. Hover reveals a `#e99292` background blush. Used for “Learn More” or “Shop All” links within content sections.

### Navigation
**`nav-bar`** — A 64px fixed-height bar on `#040404` canvas, housing Anton uppercase nav links in `#fafafa`. On scroll, a `1px` `#272727` bottom border appears to separate it from content. Links use `{spacing.lg}` horizontal padding between items. Active link text shifts to `#cc3b3b`, inactive links sit at `#aaaaaa`.

**`search-bar`** — A `{rounded.full}` pill on `#1e1e1e` surface with `#aaaaaa` placeholder text in Epilogue 14px. At 44px height, it sits comfortably in the nav bar without overwhelming the header. On focus, a `#cc3b3b` border appears. The pill shape contrasts with the system’s `{rounded.sm}` buttons, giving search a distinct, friendly affordance.

### Cards
**`product-card`** — A white `#fafafa` card with `{rounded.sm}` corners, no padding on the container itself — spacing comes from inner elements. The image area uses `{rounded.sm}` top corners and a 1:1 aspect ratio. Title sits in Epilogue 16px semibold with `{spacing.sm}` top and `{spacing.base}` side padding. Price follows in Epilogue 14px regular. On hover, a subtle `0 4px 12px rgba(0,0,0,0.15)` shadow lifts the card.

**`badge`** — A compact `#bd0000` label in Anton 11px uppercase with `{rounded.xs}` corners and `2px 8px` padding. Used for “NEW”, “SOLD OUT”, or “LIMITED” flags. A blush variant uses `#e99292` background with `#040404` text for less urgent labels like “PRE-ORDER”.

### Hero
**`hero-section`** — A full-width 400px section on `#040404` canvas with Anton 48px display text in `#fafafa`. A `#000000` scrim overlay at 60% opacity sits behind text for readability when background images are present. Content is padded with `{spacing.section}` top/bottom and `{spacing.lg}` sides.

### Footer
**`footer`** — A `#1e1e1e` band with `#aaaaaa` Epilogue 14px text. Links sit at `#aaaaaa` and shift to `#cc3b3b` on hover. Padding uses `{spacing.xxl}` vertical and `{spacing.lg}` horizontal. The footer contains columns of links, a newsletter signup (using the `text-input` component), and social icons.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack single-column; hero height reduces to 280px; search bar moves below nav; footer columns stack vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; hero at 320px; search bar stays in nav |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3- or 4-column grid; hero at 400px; search bar in nav with expanded width |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero at 400px with max-width content |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have minimum 48px tap area (padding extends hit area)
- Search bar at 44px height meets touch target minimum
- Product card tap targets (title, price, button) are at least 44px apart

### Collapsing Strategy
- Nav bar collapses to hamburger menu below 744px, with a slide-in drawer from the left
- Product grid collapses from 4 columns (desktop) to 2 columns (tablet) to 1 column (mobile)
- Footer columns stack vertically below 744px, with accordion-style expandable sections
- Hero text reduces in size on mobile (display-xl scales to 32px)
- Search bar moves from inline nav position to full-width below the nav on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs and buttons are inferred from extracted colors; exact transition durations and shadow values are not available
- Error state styling for forms (red border on `text-input-error` is assumed; actual error message typography and iconography are unknown)
- Dark mode is not explicitly supported; the site’s default dark canvas may serve as a de facto dark mode, but no toggle exists
- Sub-brand or category-specific color palettes (e.g., for “Records” vs “Video”) are not distinguishable from the extracted data
- Loading states (spinners, skeleton screens) are not documented
- Modal/dialog styling (overlay opacity, close button placement, animation) is not extracted
- Dropdown menu styling for nav (if any) is not captured
- Social media icon colors and hover states are not reliably extracted
- The extracted font list includes Arial, Helvetica, and Helvetica Neue as fallbacks; the primary display font (Anton) and body font (Epilogue) are inferred from CSS declarations but may not be the complete set
- Checkout flow (if using a third-party provider) may introduce colors not reflected in the extracted palette
