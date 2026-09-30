---
version: alpha
name: "Grolier Poetry Book Shop"
source_url: "https://www.grolierpoetrybookshop.org"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A narrow storefront on Plympton Street in Cambridge, its digital presence carries the same quiet, ink-heavy conviction as the shelves inside. The palette is anchored on #222222 — a near-black that reads as serious, literary, and unapologetically dense — against a #fafafa canvas that never feels sterile, more like aged paper catching afternoon light. The extracted hex list is cluttered with social-platform blues (#3b5998 Facebook, #55acee Twitter, #1ab7ea Instagram) and checkout-widget greens (#7dbb00, #84bd00) that are not the brand; the true accent is #cc2127, a restrained crimson used sparingly — perhaps for a "New Arrivals" badge or a single underscored link — that carries the same weight as a red pencil mark on a manuscript. Typography runs Arial and Helvetica Neue at modest sizes, no display-weight heroics, no variable font; the site trusts the poetry itself to provide the voltage. Buttons are rectangular with {rounded.none} or at most {rounded.xs}, corners kept sharp to match the intellectual precision of the inventory. The top nav is a thin band of {colors.ink} text on {colors.canvas}, no logo fanfare, no search-bar pill — just a list of pages (Home, About, Events, Shop, Contact) that reads like a table of contents. The footer is dense with small links and social icons, each rendered in its platform's native color, which creates a strange visual noise against the otherwise monochrome restraint — a known gap the brand likely tolerates for discoverability. The overall effect is that of a hand-set typewriter page: minimal, deliberate, and entirely unconcerned with conversion optimization.

colors:
  primary: "#222222"
  primary-active: "#111111"
  primary-disabled: "#aaaaaa"
  ink: "#222222"
  body: "#272727"
  muted: "#aaaaaa"
  muted-soft: "#e1e1e1"
  hairline: "#e1e1e1"
  hairline-soft: "#eeeeee"
  canvas: "#fafafa"
  surface-soft: "#fbfbfb"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-crimson: "#cc2127"
  accent-crimson-hover: "#bd0000"
  social-facebook: "#3b5998"
  social-twitter: "#55acee"
  social-instagram: "#e4405f"
  social-youtube: "#cc2127"
  social-email: "#222222"

typography:
  display-xl:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: -0.5px
  display-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: -0.3px
  title-lg:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
    letterSpacing: 0
  body-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0
  caption:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption-sm:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0
  button-md:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "Arial, Helvetica, 'Helvetica Neue', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.3px
    textTransform: uppercase
  badge:
    fontFamily: "'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
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
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 11px 23px
    height: 44px
    border: "1px solid {colors.ink}"
  button-accent:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 12px 24px
    height: 44px
  button-accent-active:
    backgroundColor: "{colors.accent-crimson-hover}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.none}"
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "1px solid {colors.ink}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 60px
    borderBottom: "1px solid {colors.hairline-soft}"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: 16px
  product-card-image:
    rounded: "{rounded.none}"
    aspectRatio: "3/4"
  product-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.muted}"
    marginTop: "{spacing.xxs}"
  badge-new:
    backgroundColor: "{colors.accent-crimson}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "2px 8px"
  footer-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    typography: "{typography.link}"
    color: "{colors.muted-soft}"
    hoverColor: "{colors.canvas}"
  social-icon:
    height: 24px
    width: 24px
  social-icon-facebook:
    fill: "{colors.social-facebook}"
  social-icon-twitter:
    fill: "{colors.social-twitter}"
  social-icon-instagram:
    fill: "{colors.social-instagram}"
  social-icon-youtube:
    fill: "{colors.social-youtube}"
  social-icon-email:
    fill: "{colors.social-email}"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    padding: "{spacing.section} {spacing.lg}"
    maxWidth: 800px
  hero-title:
    typography: "{typography.display-xl}"
    marginBottom: "{spacing.base}"
  hero-subtitle:
    typography: "{typography.body-md}"
    color: "{colors.muted}"
  event-card:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "{spacing.base}"
    borderLeft: "3px solid {colors.accent-crimson}"
  event-card-date:
    typography: "{typography.caption-sm}"
    color: "{colors.accent-crimson}"
    fontWeight: 700
  event-card-title:
    typography: "{typography.title-md}"
    marginTop: "{spacing.xs}"
  event-card-description:
    typography: "{typography.body-sm}"
    marginTop: "{spacing.sm}"
  search-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
    width: "100%"
  search-submit:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.none}"
    padding: 10px 20px
    height: 44px

## Components

### Buttons
**`button-primary`** — A solid near-black rectangle with uppercase lettering, no rounding, used for primary actions like "Add to Cart" or "Subscribe." On hover, shifts to `{colors.primary-active}` (#111111). Disabled state uses `{colors.primary-disabled}` (#aaaaaa) with no border change. **`button-secondary`** — An outlined variant with a 1px `{colors.ink}` border on a white canvas, same uppercase `{typography.button-md}`. Active state inverts to solid `{colors.ink}` with white text. **`button-accent`** — The crimson variant (`{colors.accent-crimson}`) reserved for high-signal actions like "New Arrivals" or "Featured Poet." Hover deepens to `{colors.accent-crimson-hover}` (#bd0000). All buttons share a 44px height and 12px 24px padding.

### Navigation
**`nav-bar`** — A 60px band of `{colors.canvas}` with a soft bottom hairline (`{colors.hairline-soft}`). Navigation links use `{typography.nav-link}` (14px, 600 weight, uppercase, 0.3px letter-spacing). The active page is indicated by a 2px `{colors.ink}` underline via `nav-link-active`. Inactive links render in `{colors.muted}`. No logo or hamburger on desktop; the brand name is set in `{typography.display-md}` as a text-only wordmark at the far left.

### Cards
**`product-card`** — A simple white card with no rounding, 16px padding, containing a 3:4 aspect-ratio image, a `{typography.title-md}` title, and a `{typography.body-sm}` price in `{colors.muted}`. No shadow, no border — the card relies on the grid spacing for separation. **`event-card`** — A `{colors.surface-soft}` card with a 3px `{colors.accent-crimson}` left border, used for poetry readings and launches. The date is set in `{typography.caption-sm}` with crimson color and 700 weight; the title uses `{typography.title-md}`.

### Forms
**`text-input`** — A 44px-tall input with `{colors.canvas}` background, `{colors.ink}` text, and a 1px `{colors.hairline}` border. On focus, the border switches to `{colors.ink}`. No rounding, no placeholder styling beyond the standard browser default. **`search-bar`** — Identical to `text-input` in shape and size, paired with a `search-submit` button that uses `{typography.button-sm}` (12px uppercase) on a `{colors.primary}` background.

### Footer
**`footer-section`** — A full-width `{colors.ink}` band with `{colors.canvas}` text. Links render in `{colors.muted-soft}` (#e1e1e1) and lighten to `{colors.canvas}` on hover. Social icons are rendered at 24px square using their platform-native colors (`{colors.social-facebook}`, `{colors.social-twitter}`, `{colors.social-instagram}`, `{colors.social-youtube}`). The email icon uses `{colors.social-email}` (#222222) on a white circle background.

### Badges
**`badge-new`** — A crimson rectangle (`{colors.accent-crimson}`) with white uppercase 11px text, 2px 8px padding, no rounding. Used sparingly on product cards and event listings. **`badge-sale`** — Same shape but `{colors.ink}` background, for discounted items.

### Hero
**`hero-section`** — A centered content area on `{colors.canvas}` with a max-width of 800px, padded top and bottom at `{spacing.section}` (64px). The `hero-title` uses `{typography.display-xl}` (28px, 700 weight, -0.5px letter-spacing) and the `hero-subtitle` uses `{typography.body-md}` in `{colors.muted}`. No background image, no decorative elements — just type.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav links collapse into a hamburger menu; product cards stack single-column; hero padding reduces to 32px; footer links stack vertically; event cards lose left border and gain top border. |
| Tablet | 744–1128px | Two-column product grid; nav remains horizontal but with reduced letter-spacing; hero max-width reduces to 600px. |
| Desktop | 1128–1440px | Three-column product grid; full nav with all links visible; hero at 800px max-width. |
| Wide | > 1440px | Content max-width capped at 1440px; nav remains unchanged; product grid can expand to four columns if inventory warrants. |

### Touch Targets
- All buttons and links maintain a minimum 44px height for touch accessibility.
- Nav links on mobile have 48px tap targets.
- Social icons in footer are 24px with 44px touch padding.
- Search submit button matches input height at 44px.

### Collapsing Strategy
- Top nav collapses to a hamburger menu below 744px, with a slide-in drawer from the left.
- Product grid collapses from 3 columns → 2 columns → 1 column as viewport shrinks.
- Footer link columns collapse to a single vertical stack below 744px.
- Event cards lose the crimson left border below 744px and gain a 3px top border instead.
- Hero section reduces top/bottom padding from 64px to 32px on mobile.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for text inputs beyond the basic border color change could not be reliably extracted; placeholder styling is assumed browser-default.
- Error state styling for forms (red borders, error messages) was not visible in the extracted data.
- The exact hover state for social icons (scale, opacity, or color shift) could not be determined; the extracted hexes are the platform-native colors.
- Dark mode is not supported; the site appears to be light-mode only.
- The extracted hex list is heavily polluted with social-platform brand colors and checkout-widget greens; the true brand palette is likely much smaller (near-black, white, and a single crimson accent). The `{colors.accent-crimson}` assignment is an inference from the presence of #cc2127 and #bd0000 in the extracted list.
- No variable font or custom typeface was found; the site uses system fonts (Arial, Helvetica, Helvetica Neue). This may be intentional for performance or a known limitation of the platform.
- The exact height of the nav bar (60px) is inferred from common bookstore-site patterns; the extracted data did not include explicit nav height.
- Product card shadow or border states (if any) could not be determined; the component assumes no shadow based on the flat, minimal aesthetic.
- The hamburger menu icon style and animation were not extractable; a standard three-line icon is assumed.
- Checkout flow styling (cart, payment, confirmation) was not accessible from the extracted page data.
