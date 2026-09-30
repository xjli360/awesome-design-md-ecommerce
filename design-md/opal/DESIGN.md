---
version: alpha
name: "Opal"
source_url: "https://opalcamera.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A matte-black monolith of a webcam that signals its seriousness through a single, unapologetic accent: #ffdb01, a high-voltage marigold that appears only on the primary CTA, the badge on the product hero, and the tiny LED ring that glows when the lens is live. The rest of the system is a study in near-monochrome restraint — #171717 ink, #222222 and #1b1b1b for deep surfaces, #fafafa for the canvas, and a cascade of grays (#777777, #767676, #bbbbbb, #e7e7e7) for body copy, muted labels, and hairline borders. The brand uses Roobert, a geometric sans-serif with a slight industrial stiffness, set at modest weights (400–600) and never oversized — the hero headline sits at 28px, not 48px, because the product photography (a precision-machined aluminum cylinder on a brushed-metal stand) does the heavy lifting. Every corner is either razor-sharp ({rounded.none}) or fully pill-shaped ({rounded.full}); there is no intermediate radius. The primary button is a 48px-tall pill in #ffdb01 with #171717 text, a deliberate inversion of the typical dark-brand CTA. The nav bar is a floating translucent panel (#ffffff at 80% opacity, backdrop blur) that lets the product hero breathe behind it. The entire system feels like a Leica camera interface — minimal, dense with purpose, and unwilling to apologize for its price point.

colors:
  primary: "#ffdb01"
  primary-active: "#e6c500"
  primary-disabled: "#d9d9d9"
  ink: "#171717"
  body: "#222222"
  muted: "#777777"
  muted-soft: "#767676"
  hairline: "#e7e7e7"
  hairline-soft: "#ededed"
  canvas: "#fafafa"
  surface-soft: "#f5f5f5"
  surface-card: "#ffffff"
  on-primary: "#171717"
  on-dark: "#ffffff"
  error: "#ff3427"
  success: "#5ab864"
  badge-accent: "#ffdb01"
  badge-text: "#171717"
  scrim: "#000000"
  nav-backdrop: "rgba(255, 255, 255, 0.8)"

typography:
  display-xl:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.21
    letterSpacing: -0.56px
  display-lg:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.48px
  display-md:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 22px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: -0.44px
  title-lg:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0
  title-md:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0
  body-md:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: 0
  badge:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
    letterSpacing: 0.33px
    textTransform: uppercase
  button-md:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.23
    letterSpacing: 0.26px
  link:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
    textDecoration: underline
  nav-link:
    fontFamily: "'Roobert', 'SF Pro Display', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.29
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
    padding: 14px 32px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    rounded: "{rounded.full}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.hairline}"
  button-secondary-hover:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    border: "2px solid {colors.muted}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 8px 0
  button-tertiary-text-hover:
    textColor: "{colors.ink}"
  icon-button-circle:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
    height: 40px
    width: 40px
  nav-bar:
    backgroundColor: "{colors.nav-backdrop}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
    backdropFilter: "blur(12px)"
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    textColor: "{colors.ink}"
    borderBottom: "2px solid {colors.primary}"
  nav-link-inactive:
    textColor: "{colors.muted}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
  hero-badge:
    backgroundColor: "{colors.badge-accent}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"
  product-card-hover:
    border: "1px solid {colors.hairline}"
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.primary}"
    boxShadow: "0 0 0 3px rgba(255, 219, 1, 0.2)"
  text-input-error:
    border: "1px solid {colors.error}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: "12px 16px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-dark}"
  accordion-trigger:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.title-md}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"
  accordion-content:
    backgroundColor: transparent
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.sm} 0 {spacing.base} 0"

## Components

### Buttons
**`button-primary`** — The single most important interaction in the system: a 48px-tall pill in #ffdb01 with #171717 text, using Roobert 600 at 15px with 0.3px letter-spacing. On hover, the background shifts to #e6c500. Disabled state uses #d9d9d9 background with #777777 text — the marigold is reserved for active, intentional actions. Padding is 14px top/bottom, 32px left/right, giving the button a solid, weighted feel.

**`button-secondary`** — An outlined pill with a 2px #e7e7e7 border on a white canvas. Text is #171717. Hover thickens the border to #767676 and adds a #f5f5f5 background. Same 48px height as the primary, so they can sit side-by-side in a CTA pair without visual imbalance.

**`button-tertiary-text`** — A bare text button in #777777, 13px/500, with no padding beyond 8px vertical. Hover shifts text to #171717. Used for "Learn More" links in product cards and footer navigation.

### Navigation
**`nav-bar`** — A floating 64px bar with a white background at 80% opacity and a 12px backdrop blur. The bottom edge is a 1px #ededed hairline. Nav links are 14px/500 in #171717 (active) or #777777 (inactive). The active link gets a 2px #ffdb01 underline. The bar is fixed to the top of the viewport on desktop, collapsing to a hamburger on mobile.

**`nav-link-active` / `nav-link-inactive`** — Active links use ink (#171717) with a 2px marigold bottom border. Inactive links use muted (#777777) and no border. No background change on hover — the brand trusts the text color shift and the underline to signal state.

### Hero Section
**`hero-section`** — A full-width section with #fafafa background, 64px top padding, 24px horizontal padding. The hero contains a product image (the Opal webcam on a brushed-metal stand), a headline using `{typography.display-xl}`, and a subhead using `{typography.body-md}` in #222222. A `{components.hero-badge}` sits above the headline, reading "NEW" or "Award Winner" in uppercase 11px/600 with #171717 text on #ffdb01 background, pill-shaped with 4px/12px padding.

### Cards
**`product-card`** — A white card with 12px rounded corners, a 1px #ededed border, and 16px padding. Body text uses 14px/400 Roobert in #171717. On hover, the border shifts to #e7e7e7 and a subtle 0 4px 12px rgba(0,0,0,0.08) shadow appears. Used for product feature highlights, comparison tables, and accessory listings.

### Forms
**`text-input`** — A 48px-tall input with 8px rounded corners, 12px/16px padding, and a 1px #e7e7e7 border. Focus state swaps the border to #ffdb01 and adds a 3px rgba(255, 219, 1, 0.2) ring. Error state swaps the border to #ff3427. Typography is 16px/400 Roobert.

**`select-input`** — Same dimensions and border treatment as text-input, but with a custom dropdown arrow. Used for product configuration (e.g., "Choose your finish: Matte Black / Silver").

### Footer
**`footer`** — A full-width #171717 band with white text. Links are 14px/400 in #767676, shifting to white on hover. Padding is 48px vertical, 24px horizontal. The footer contains columns for product links, support, legal, and social icons (monochrome, white).

### Accordion
**`accordion-trigger`** — A full-width clickable row with 16px vertical padding and a 1px #ededed bottom border. Text is 16px/500 Roobert in #171717. On click, the content panel slides open with `{typography.body-sm}` text in #222222 and 8px top / 16px bottom padding.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger; hero section stacks (image above text); buttons go full-width; product cards stack in a single column; footer columns collapse to a single column; `{typography.display-xl}` drops to 24px |
| Tablet | 744–1128px | Nav bar remains expanded but link font-size drops to 13px; hero section uses a 50/50 split; product cards use a 2-column grid; footer uses 2 columns |
| Desktop | 1128–1440px | Full nav bar with all links; hero section uses a 60/40 split (image larger); product cards use a 3-column grid; footer uses 4 columns |
| Wide | > 1440px | Max-width container at 1440px, centered; hero section uses a 50/50 split with more whitespace; product cards use a 4-column grid |

### Touch Targets
- All interactive elements (buttons, links, inputs) have a minimum height of 44px on mobile.
- Icon buttons are 40px × 40px with a 44px tap area via padding.
- Nav bar hamburger icon is 44px × 44px.
- Accordion triggers are 44px minimum height.

### Collapsing Strategy
- Nav bar links collapse into a hamburger menu below 744px.
- Footer columns collapse from 4 to 2 columns at tablet, to 1 column at mobile.
- Product card grid collapses from 4 columns (wide) to 3 (desktop) to 2 (tablet) to 1 (mobile).
- Hero section switches from side-by-side to stacked at mobile.
- Accordion content is always collapsed by default on all breakpoints.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Extracted hex list is dominated by grays (#171717, #222222, #777777, #767676, #bbbbbb, #e7e7e7, #dedede, #bcbcbc, #d9d9d9, #e6e6e6, #aaaaaa, #fafafa, #dcdcdc, #ededed, #1b1b1b, #1e1e1e, #888888, #ececec, #e5e5e5, #959595, #343434, #787778, #595226, #121212, #8b790c) with one distinctive accent (#ffdb01) and a few likely checkout/social colors (#5ab864, #ff3427, #0141ff). The brand's true primary is #ffdb01 (marigold), which appears consistently across the site. The grays are the supporting palette.
- Hover states for buttons and cards are inferred from common patterns — not extracted from live CSS.
- Error styling (text-input-error border color, error message typography) is inferred from the presence of #ff3427 in the extracted list.
- Success styling (checkout confirmation, form success) uses #5ab864 but exact component styling is unknown.
- Dark mode is not present on the live site — all pages use a light canvas (#fafafa).
- Sub-brand or product-variant palettes (e.g., special edition colors) are not captured.
- The exact font stack for Roobert is inferred from the extracted font-family declarations; the brand may use a different fallback order.
- Animation durations and easing curves are not extracted.
- Focus-visible ring styles beyond the text-input are not documented.
- The nav bar's backdrop blur value (12px) is an estimate based on visual inspection.
- The product-card shadow on hover is an estimate; the actual shadow may differ.
