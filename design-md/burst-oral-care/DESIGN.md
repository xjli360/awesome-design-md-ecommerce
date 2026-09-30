---
version: alpha
name: "Burst Oral Care"
source_url: "https://www.burstoralcare.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A vibrant, confident oral-care brand that pulses with energy through a bold purple-and-yellow palette — primary purple #370078 anchors every CTA, badge, and product hero, while a sharp yellow #ffdd00 provides electric contrast on ratings, sale tags, and accent highlights. The brand reads as clinical-but-approachable: a clean white canvas (#ffffff) supports soft gray surfaces (#f4f4f6, #f7f7f8) and muted text (#676986, #9a9db1), while deep ink (#272d45) drives body copy and headings. Typography relies on a neutral sans-serif stack (inherit declarations suggest system fonts or a single weight-variable family), with button text at `{typography.button-md}` and body copy at `{typography.body-md}`. Signature moves include pill-shaped buttons (`{rounded.full}`) for primary actions, softly rounded cards (`{rounded.sm}` ~8px), and a persistent top nav with a bold purple background. The brand trusts product photography and dense informational layouts — star ratings glow yellow, subscription badges pop purple, and every interactive element feels deliberate and tactile. There is no hard edge in the UI; even input fields and search bars carry `{rounded.sm}` or `{rounded.full}` radii, reinforcing a friendly, hygienic feel. The overall mood is energetic yet trustworthy — a dental-pro-backed brand that doesn't whisper.

colors:
  primary: "#370078"
  primary-active: "#2a005e"
  primary-disabled: "#9a9db1"
  ink: "#272d45"
  body: "#676986"
  muted: "#9a9db1"
  muted-soft: "#cecece"
  hairline: "#dedede"
  hairline-soft: "#e5e5eb"
  canvas: "#ffffff"
  surface-soft: "#f4f4f6"
  surface-card: "#ffffff"
  surface-strong: "#f7f7f8"
  on-primary: "#ffffff"
  accent-yellow: "#ffdd00"
  accent-yellow-soft: "#ffee80"
  accent-blue: "#1990c6"
  accent-blue-dark: "#136f99"
  star-rating: "#ffdd00"
  badge-sale: "#ffdd00"
  badge-new: "#370078"
  legal-link: "#4285f4"
  scrim: "#121212"
  error: "#c13515"
  success: "#1990c6"

typography:
  display-xl:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.25px
  display-md:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  caption-sm:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0
  badge:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.25px
  button-sm:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.25px
  link:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "inherit, -apple-system, system-ui, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
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
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
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
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.primary}"
  button-secondary-active:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.primary-active}"
    rounded: "{rounded.full}"
    border: "2px solid {colors.primary-active}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
    padding: 0
  button-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 14px 32px
    height: 48px
  button-yellow-active:
    backgroundColor: "{colors.accent-yellow-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "1px solid {colors.error}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: 12px 24px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.accent-yellow}"
    typography: "{typography.nav-link}"
  nav-link-hover:
    backgroundColor: transparent
    textColor: "{colors.accent-yellow-soft}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 16px
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.sm}"
  product-card-title:
    typography: "{typography.title-sm}"
    textColor: "{colors.ink}"
  product-card-price:
    typography: "{typography.body-md}"
    textColor: "{colors.ink}"
  product-card-rating:
    textColor: "{colors.star-rating}"
  badge-sale:
    backgroundColor: "{colors.badge-sale}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.badge-new}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-subscription:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-banner:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.display-lg}"
    padding: "{spacing.section} {spacing.base}"
  hero-banner-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.base}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.base}"
  footer-link:
    textColor: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-link-hover:
    textColor: "{colors.on-primary}"
  section-heading:
    typography: "{typography.display-md}"
    textColor: "{colors.ink}"
    marginBottom: "{spacing.lg}"
  star-rating:
    textColor: "{colors.star-rating}"
    fontSize: 16px
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    height: 40px
    border: "1px solid {colors.hairline}"
  accordion:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.title-sm}"
    rounded: "{rounded.sm}"
    padding: "{spacing.base}"
    border: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the entire site, rendered as a pill-shaped button with a bold purple background (#370078) and white text. On hover, it deepens to `{colors.primary-active}` (#2a005e). The disabled state uses `{colors.primary-disabled}` (#9a9db1) to signal inactivity. Used for "Add to Cart", "Subscribe", and "Shop Now" actions.

**`button-secondary`** — An outlined variant with a white background, purple text, and a 2px purple border. On hover, the background shifts to `{colors.surface-soft}` (#f4f4f6) and the border deepens. Used for "Learn More" and secondary checkout actions.

**`button-yellow`** — A high-energy accent button with a yellow background (#ffdd00) and dark ink text (#272d45). On hover, it softens to `{colors.accent-yellow-soft}` (#ffee80). Used for promotional CTAs, sale banners, and limited-time offers.

**`button-tertiary-text`** — A text-only button with no background or border, using purple text. Used for "Cancel", "Skip", and inline navigation links within forms and modals.

### Cards
**`product-card`** — A white card with soft 8px rounded corners (`{rounded.sm}`) and 16px padding. Contains a product image with matching rounded corners, a title in `{typography.title-sm}`, price in `{typography.body-md}`, and a star rating in yellow (#ffdd00). On hover, a subtle box shadow elevates the card. Used across collection pages and search results.

**`hero-banner`** — A full-width section with soft gray background (`{colors.surface-soft}`) and large display typography. The primary variant uses a purple background (`{colors.primary}`) with white text for high-impact marketing banners. Padding is `{spacing.section}` (64px) on top and bottom.

### Navigation
**`nav-bar`** — A fixed or sticky top navigation bar with a bold purple background (`{colors.primary}`), white text, and 64px height. Navigation links use uppercase `{typography.nav-link}` with 0.5px letter spacing. Active and hover states shift link color to yellow (#ffdd00 or #ffee80). The nav collapses to a hamburger menu on mobile.

### Forms
**`text-input`** — A standard input field with white background, 8px rounded corners, 1px hairline border (#dedede), and 48px height. On focus, the border becomes 2px solid purple. Error state uses a red border (#c13515). Used for email, password, and text entry fields.

**`search-bar`** — A pill-shaped search input with full rounding (`{rounded.full}`), 48px height, and 24px horizontal padding. The white background and 1px hairline border keep it clean. Used in the header and on search-focused pages.

### Badges
**`badge-sale`** — A small yellow badge (#ffdd00) with dark ink text, 4px rounded corners, and uppercase 11px typography. Used to highlight discounted products.

**`badge-new`** — A purple badge (#370078) with white text, signaling newly added products.

**`badge-subscription`** — A blue badge (#1990c6) with white text, used to indicate subscription-eligible products.

### Footer
**`footer`** — A dark footer with deep ink background (`{colors.ink}` #272d45), muted text (#cecece), and generous vertical padding (48px). Links use `{typography.link}` and hover to white. Organized in columns with section headings in `{typography.title-sm}`.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Single-column layout; nav collapses to hamburger; product cards stack vertically; hero padding reduces to 32px; buttons become full-width |
| Tablet | 744–1128px | Two-column product grid; nav remains visible with condensed links; hero uses medium padding (48px); search bar shrinks to 40px height |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links; hero at full padding (64px); standard button sizes |
| Wide | > 1440px | Max-width container (1440px) centered; four-column product grid; hero may include background imagery |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility
- Nav links have 48px tap targets on mobile
- Quantity selector buttons are 40px minimum
- Search bar is 48px tall on all breakpoints

### Collapsing Strategy
- Top navigation collapses to hamburger menu below 744px
- Product grid reduces from 4 columns to 1 column on mobile
- Footer columns stack vertically on mobile
- Hero banners reduce padding and font size on mobile
- Secondary navigation (category strip) collapses to horizontal scroll on mobile

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.







- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover states for product cards (shadow depth, scale) not fully extracted — assumed 4px shadow
- Error styling for form validation (error messages, iconography) not observed
- Dark mode palette not present on live site
- Sub-brand or collection-specific color variations (e.g., whitening vs. sonicare) not captured
- Animation and transition durations (ease-in-out, 0.2s assumed) not extracted
- Modal/dialog overlay styling not observed
- Loading states (spinners, skeletons) not present in extracted data
- Specific font weights beyond 400, 500, 600, 700 not confirmed — inherit declarations suggest variable font
- Icon set and sizing conventions not documented
- Print stylesheet behavior unknown
