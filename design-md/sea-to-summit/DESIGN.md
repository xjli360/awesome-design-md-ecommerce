---
version: alpha
name: "Sea to Summit"
source_url: "https://seatosummit.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep blue (#1f2a44) and a vivid cyan (#0086c9) anchor a system built for the transition from trailhead to alpine ridge — the brand’s visual language is less about gear-gloss and more about the quiet competence of well-engineered fabric. The palette draws from the extracted live site: a warm off-white canvas (#d8d4c2) that reads as sun-bleached nylon rather than sterile paper, a safety-orange accent (#cf4520) that appears in critical UI moments like cart badges and sale flags, and a secondary green (#a3cf00) that surfaces in category highlights and environmental callouts. Typography runs URW DIN and URW DIN Condensed — a condensed sans that packs information density into product cards and spec tables without sacrificing legibility at 14px body sizes. Buttons use a tight 8px radius (`{rounded.sm}`) and the primary CTA sits at 48px height with the brand’s cyan (#0086c9) on white, while secondary actions adopt the dark navy (#1f2a44) with a subtle 1px hairline (#dcdcdc). The navigation bar is a full-width navy band (#1f2a44) with white text, a rare dark-header choice in outdoor retail that signals authority and durability. Product cards float on white (`{surface-card}`) with a soft shadow and a 12px radius (`{rounded.md}`), while the search bar uses a pill shape (`{rounded.full}`) in the canvas off-white (#d8d4c2) with a cyan focus ring. The system avoids hard corners entirely below the hero level, using radii from 4px on micro-badges to 32px on promotional banners. The overall mood is expedition-ready but not aggressive — the brand trusts its photography of misty peaks and rainfly details to carry the emotional weight, letting the UI stay clean, legible, and just slightly weathered.

colors:
  primary: "#0086c9"
  primary-active: "#006fa8"
  primary-disabled: "#b3d9f0"
  ink: "#1f2a44"
  body: "#323232"
  muted: "#687782"
  muted-soft: "#768692"
  hairline: "#dcdcdc"
  hairline-soft: "#e3e3e3"
  canvas: "#d8d4c2"
  surface-soft: "#f8f8f9"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  on-dark: "#ffffff"
  accent-orange: "#cf4520"
  accent-green: "#a3cf00"
  accent-safety: "#f64221"
  badge-red: "#d34727"
  badge-gold: "#d6791b"
  star-rating: "#d6791b"
  scrim: "#000000"

typography:
  display-xl:
    fontFamily: "'URW DIN Condensed', 'DIN Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 42px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'URW DIN Condensed', 'DIN Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0
  display-sm:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-md:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-sm:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  body-md:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'URW DIN Condensed', 'DIN Condensed', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  micro-label:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.3px
  button-sm:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0.2px
  link:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.45
    letterSpacing: 0
  nav-link:
    fontFamily: "'URW DIN', 'DIN', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.2
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
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 14px 28px
    height: 48px
  button-secondary-active:
    backgroundColor: "#151e33"
    textColor: "{colors.on-dark}"
    rounded: "{rounded.sm}"
  button-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.sm}"
    padding: 13px 27px
    height: 48px
    border: "1px solid {colors.hairline}"
  button-outline-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    border: "1px solid {colors.ink}"
  button-pill-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 10px 24px
  button-pill-outline:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 9px 23px
    border: "1px solid {colors.hairline}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
    padding: 11px 15px
  text-input-error:
    border: "1px solid {colors.accent-orange}"
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.nav-link}"
    height: 72px
    padding: "0 {spacing.xl}"
  nav-link-active:
    borderBottom: "2px solid {colors.primary}"
  nav-link-hover:
    color: "{colors.primary}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.full}"
    padding: 10px 20px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.base}"
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  product-card-hover:
    boxShadow: "0 4px 16px rgba(0,0,0,0.12)"
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1/1"
  product-card-title:
    typography: "{typography.title-sm}"
    color: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.body}"
  product-card-badge:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.display-xl}"
    height: 480px
    rounded: "{rounded.none}"
  hero-banner-overlay:
    backgroundColor: "rgba(31,42,68,0.4)"
  category-tile:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.md}"
    padding: "{spacing.lg}"
    boxShadow: "0 1px 4px rgba(0,0,0,0.06)"
  category-tile-active:
    border: "2px solid {colors.primary}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-dark}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} {spacing.xl}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.primary}"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 6px"
  rating-stars:
    color: "{colors.star-rating}"
    size: 16px
  accordion-header:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.md} {spacing.base}"
  accordion-content:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action, filled with the brand cyan (#0086c9) and white text. Uses a compact 8px radius (`{rounded.sm}`) and 48px height for comfortable tap targets. On hover, shifts to `{colors.primary-active}` (#006fa8). Disabled state uses a pale cyan (#b3d9f0) with white text, signaling non-interactivity without visual noise.

**`button-secondary`** — The dark alternative, filled with the deep navy `{colors.ink}` (#1f2a44) and white text. Used for secondary actions like "View Details" or "Add to Wishlist" on light backgrounds. Hover state deepens to #151e33. Shares the same 48px height and 8px radius as primary for visual consistency.

**`button-outline`** — A transparent button with a 1px `{colors.hairline}` border and navy text. Used for tertiary actions like "Learn More" or "Compare". On hover, the border switches to `{colors.ink}` and the background fills with `{colors.surface-soft}` (#f8f8f9). Padding is adjusted by 1px to account for the border.

**`button-pill-primary`** — A fully rounded variant (`{rounded.full}`) of the primary button, used in promotional banners, hero CTAs, and sticky mobile bars. Uses `{typography.button-sm}` for a slightly tighter fit. Height is 40px for a more compact profile.

**`button-pill-outline`** — The pill-shaped outline counterpart, used for "Shop by Activity" filters and category navigation pills. Transparent with a 1px hairline border, navy text, and full rounding.

### Text Inputs
**`text-input`** — Standard form field with white background, 1px `{colors.hairline}` border, and 8px radius. Uses `{typography.body-md}` for legibility. On focus, the border thickens to 2px and switches to `{colors.primary}` (#0086c9), with padding reduced by 1px to prevent layout shift. Error state uses a 1px `{colors.accent-orange}` (#cf4520) border — no icon, just the color shift.

### Navigation
**`nav-bar`** — A full-width dark navy band (#1f2a44) at 72px height, housing the logo, category links, and utility icons (search, account, cart). Links use uppercase `{typography.nav-link}` with 0.5px letter-spacing for a technical, expedition-log feel. Active link has a 2px cyan underline (`{colors.primary}`). Hover state shifts text to cyan. The cart icon uses `{colors.accent-orange}` for the badge count.

**`search-bar`** — A pill-shaped search field (`{rounded.full}`) at 44px height, using the warm off-white canvas (#d8d4c2) background. The placeholder text is `{colors.muted}` (#687782). On focus, the border becomes 2px cyan. The search icon sits inside the pill on the left, colored `{colors.muted-soft}`.

### Product Cards
**`product-card`** — A white card with 12px radius (`{rounded.md}`), 16px padding, and a subtle drop shadow (0 2px 8px rgba(0,0,0,0.08)). On hover, the shadow deepens to 0 4px 16px rgba(0,0,0,0.12). The product image occupies the top with an 8px radius and 1:1 aspect ratio. The title uses `{typography.title-sm}` in navy, the price uses `{typography.body-md}` in dark gray. A badge overlay (sale, new, or eco) sits at the top-left corner with 4px radius.

**`product-card-badge`** — Small rectangular tags (4px radius) that overlay product images. Sale badges use `{colors.accent-orange}` (#cf4520) with white text; new badges use `{colors.accent-green}` (#a3cf00) with navy text. Uses condensed uppercase `{typography.badge}` at 11px.

### Hero
**`hero-banner`** — A full-width, full-height (480px) banner with the deep navy `{colors.ink}` background and a semi-transparent overlay (rgba(31,42,68,0.4)) for text legibility over background images. The headline uses `{typography.display-xl}` (42px condensed) in white. A pill-shaped primary CTA sits below the headline. No rounded corners — the hero bleeds edge-to-edge.

### Footer
**`footer`** — A full-width dark navy section with 64px vertical padding and 32px horizontal padding. Links use `{colors.muted-soft}` (#768692) at 14px, shifting to cyan on hover. The brand logo appears in white at the top. Newsletter signup uses the pill-shaped search bar pattern but with a white background and cyan submit button.

### Badges & Tags
**`badge-sale`** — Orange (#cf4520) rectangular tag with white condensed uppercase text. Used on product cards and collection pages to flag discounts. 4px radius, 2px vertical padding, 6px horizontal.

**`badge-new`** — Green (#a3cf00) rectangular tag with navy condensed uppercase text. Used for new arrivals and seasonal launches. Same dimensions as sale badge.

### Rating Stars
**`rating-stars`** — Gold (#d6791b) 5-star display at 16px per star. Used on product cards and review sections. Empty stars use `{colors.hairline}` (#dcdcdc). Half-star rendering supported.

### Accordion
**`accordion-header`** — Used in product specs, FAQ, and size-guide sections. Light gray background (`{colors.surface-soft}`) with navy title text and 8px radius. Padding is 12px vertical, 16px horizontal. A chevron icon rotates on open state.

**`accordion-content`** — White background with 16px padding and `{typography.body-sm}` text. No border — relies on the header's bottom edge for separation.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger menu; product cards stack single-column; hero banner height reduces to 320px; search bar moves to sticky top; button padding reduces to 12px 20px; footer links stack vertically |
| Tablet | 744–1128px | Nav bar shows condensed category labels (3-4 items); product cards display in 2-column grid; hero banner at 400px; search bar remains in nav but collapses icon-only on scroll |
| Desktop | 1128–1440px | Full nav bar with all categories; 3-column product grid; hero at 480px; search bar fully expanded with placeholder text |
| Wide | > 1440px | Max-width container at 1440px; product grid expands to 4 columns; hero banner uses full viewport width with background image scaling |

### Touch Targets
- All interactive elements (buttons, links, inputs) maintain minimum 44px height for touch accessibility
- Icon buttons (search, cart, account) use 44x44px tap targets even when the visible icon is smaller
- Product card CTAs ("Add to Cart", "Quick View") are 48px tall on mobile
- Accordion headers are 48px tall for easy finger targeting
- Category filter pills are 40px tall with 12px horizontal padding

### Collapsing Strategy
- Primary nav collapses to hamburger menu below 744px, with a slide-out drawer from the left
- Secondary nav (category strip) collapses to a horizontal scrollable row on mobile
- Product filters move from sidebar to a bottom sheet on mobile
- Footer link columns stack vertically below 744px, with accordion-style expand/collapse for each column
- Hero banner text overlay shifts from left-aligned (desktop) to center-aligned (mobile) with reduced padding
- Search bar transforms from full input (desktop) to icon-only (mobile) with a full-screen overlay on tap

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for all components are inferred from common patterns; exact transition durations and easing curves not extracted
- Error styling for forms (validation messages, error icons) not present in extracted data; `text-input-error` uses orange border as best guess
- Dark mode not implemented on the live site; no dark palette tokens available
- Sub-brand or collection-specific color variations (e.g., "Ultra-Sil" vs "Thermolite" product lines) not captured
- Typography scale beyond display-xl not extracted; condensed variants may have additional weights (300, 400) not observed
- Focus-visible ring styles (outline color, offset, width) not present in extracted CSS
- Loading states (skeleton screens, spinner colors, pulse animations) not documented
- Cart and checkout flow colors may include Shopify defaults (green "Add to Cart", blue checkout button) that are not brand-specific
- Star rating empty state color (#dcdcdc) inferred from hairline; actual empty star color may differ
- Mobile nav drawer background color and overlay scrim opacity not confirmed
- Newsletter signup success/error states not extracted
- Product card quick-add button hover state (e.g., "Add to Cart" appearing on hover) not confirmed
- Image aspect ratios for category tiles and hero banners are estimates based on common outdoor retail patterns
