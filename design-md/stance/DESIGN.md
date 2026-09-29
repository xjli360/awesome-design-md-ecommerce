---
version: alpha
name: "Stance"
source_url: "https://www.stance.com"
captured_at: null
evidence_status: "historical_unverified"
description: |-
  A performance-and-culture brand where the sock becomes a canvas, Stance operates on a high-contrast palette anchored by the electric cyan of #7fddff — a color that reads as both a tech-company accent and a skate-park flash, not a team-sport primary. That cyan, alongside the deeper #1ba3d5 and the near-black #1c1c1c, creates a system that feels more like a streetwear label than a uniform supplier. The typography is the giveaway: GT Pressura Extended and GT Pressura Mono are industrial, European, and deliberately cold — a sans-serif with extended proportions that forces text to breathe, and a monospaced sibling that shows up in product specs and size charts like a factory stamp. The brand's secondary palette introduces a surprising olive (#5a6616) and lime (#b6cf2d) that appear in seasonal collections and performance graphics, while the red #c80003 is reserved for sale markers and urgency badges. Rounded corners are minimal — the product card uses `{rounded.sm}` (8px) but the hero and navigation stay at `{rounded.none}`; this is a brand that prefers straight edges and sharp transitions. The canvas is #ffffff, but the surface-soft is #dedede and the hairline is #cfcfcf, creating a slightly cooler, more industrial white environment than a warm consumer brand. Stance's design system trusts its product photography to carry the emotional weight — the UI steps back, uses thin hairlines, generous `{spacing.xl}` between sections, and lets the socks, underwear, and apparel do the talking. The "Feel good, do good" tagline is the only soft note in an otherwise rigid, engineered system.

colors:
  primary: "#7fddff"
  primary-active: "#1ba3d5"
  primary-disabled: "#cfcfcf"
  ink: "#1c1c1c"
  body: "#474747"
  muted: "#a4a4a4"
  muted-soft: "#cfcfcf"
  hairline: "#cfcfcf"
  hairline-soft: "#dedede"
  canvas: "#ffffff"
  surface-soft: "#dedede"
  surface-card: "#ffffff"
  on-primary: "#1c1c1c"
  accent-olive: "#5a6616"
  accent-lime: "#b6cf2d"
  accent-red: "#c80003"
  accent-cyan-deep: "#1f6079"
  accent-cyan-bright: "#1bc2ff"
  dark-canvas: "#232933"
  dark-surface: "#121212"
  dark-muted: "#6c717a"
  dark-hairline: "#595959"

typography:
  display-xl:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.2px
  display-sm:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0
  title-lg:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 18px
    fontWeight: 500
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  caption:
    fontFamily: "'GT Pressura Mono', 'Courier New', monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0.5px
    textTransform: uppercase
  caption-sm:
    fontFamily: "'GT Pressura Mono', 'Courier New', monospace"
    fontSize: 10px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  badge:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.5px
    textTransform: uppercase
  button-lg:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
    textTransform: uppercase
  button-md:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  button-sm:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
    textTransform: uppercase
  link:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0
  nav-link:
    fontFamily: "'GT Pressura Extended', 'Helvetica Neue', Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
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
    rounded: "{rounded.none}"
    padding: 14px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.muted}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 13px 31px
    height: 48px
    border: "2px solid {colors.ink}"
  button-secondary-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.none}"
    padding: 14px 0
  button-pill-cyan:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  button-pill-olive:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.canvas}"
    typography: "{typography.button-sm}"
    rounded: "{rounded.full}"
    padding: 8px 20px
    height: 36px
  text-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  text-input-focus:
    border: "2px solid {colors.primary}"
  text-input-error:
    border: "2px solid {colors.accent-red}"
  select-input:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: 12px 16px
    height: 48px
    border: "1px solid {colors.hairline}"
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 72px
    borderBottom: "1px solid {colors.hairline}"
  nav-bar-sticky:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 56px
    boxShadow: "0 2px 8px rgba(0,0,0,0.08)"
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    borderBottom: "2px solid {colors.ink}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.muted}"
    typography: "{typography.nav-link}"
  search-bar:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 10px 16px
    height: 44px
    border: "1px solid {colors.hairline}"
  search-bar-focus:
    border: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.sm}"
    padding: 0
  product-card-image:
    rounded: "{rounded.sm}"
    aspectRatio: "1 / 1"
  product-card-title:
    typography: "{typography.title-sm}"
    marginTop: "{spacing.sm}"
  product-card-price:
    typography: "{typography.body-sm}"
    color: "{colors.body}"
  product-card-sale-price:
    typography: "{typography.body-sm}"
    color: "{colors.accent-red}"
  badge-sale:
    backgroundColor: "{colors.accent-red}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-new:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  badge-exclusive:
    backgroundColor: "{colors.accent-olive}"
    textColor: "{colors.canvas}"
    typography: "{typography.badge}"
    rounded: "{rounded.none}"
    padding: "4px 8px"
  hero-section:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} 0"
  hero-cta:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-lg}"
    rounded: "{rounded.none}"
    padding: "16px 40px"
    height: 56px
  footer:
    backgroundColor: "{colors.dark-canvas}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.section}"
  footer-link:
    color: "{colors.muted}"
    typography: "{typography.link}"
  footer-link-hover:
    color: "{colors.canvas}"
  size-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  size-selector-active:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    border: "1px solid {colors.ink}"
  quantity-selector:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.none}"
    padding: "8px 12px"
    border: "1px solid {colors.hairline}"
  cart-item:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    padding: "{spacing.base} 0"
    borderBottom: "1px solid {colors.hairline-soft}"

## Components

### Buttons
**`button-primary`** — The brand's primary call-to-action, rendered in GT Pressura Extended uppercase at 14px/600 with zero rounding. The electric cyan `{colors.primary}` (#7fddff) background against near-black `{colors.on-primary}` (#1c1c1c) text creates a high-voltage contrast that reads as urgent and modern. On hover, the background shifts to `{colors.primary-active}` (#1ba3d5) — a deeper, more saturated cyan. The disabled state drops to `{colors.primary-disabled}` (#cfcfcf) with `{colors.muted}` (#a4a4a4) text, signaling inactivity without ambiguity.

**`button-secondary`** — An outlined variant with a 2px `{colors.ink}` (#1c1c1c) border on a white canvas. The active state inverts to a solid `{colors.ink}` background with white text. Used for "Add to Cart" secondary actions, "View Details" links, and filter resets. The hard corners (`{rounded.none}`) are consistent with the primary button — Stance does not soften its CTAs.

**`button-ghost`** — A text-only button with no background or border, used for tertiary actions like "Clear Filters" or "Cancel." The typography matches `{typography.button-md}` but with no padding beyond the text itself. Hover adds an underline or slight opacity shift.

**`button-pill-cyan`** and **`button-pill-olive`** — Pill-shaped (`{rounded.full}`) buttons reserved for promotional badges, collection tags, and filter chips. The cyan variant uses `{colors.primary}`; the olive variant uses `{colors.accent-olive}` (#5a6616) with white text. These are the only rounded buttons in the system, creating a deliberate visual distinction from the hard-cornered primary/secondary buttons.

### Navigation
**`nav-bar`** — A 72px white bar with a single `{colors.hairline}` (#cfcfcf) bottom border. Navigation links use `{typography.nav-link}` — 14px/500 in GT Pressura Extended, uppercase, with 0.5px letter-spacing. The active link is marked by a 2px `{colors.ink}` bottom border. On scroll, the bar collapses to 56px with a subtle `boxShadow` for depth. The Stance logo sits left-aligned, with the cart icon and search icon right-aligned.

**`nav-link-active`** and **`nav-link-inactive`** — Active links use `{colors.ink}` with a 2px bottom border; inactive links use `{colors.muted}` (#a4a4a4) with no border. The uppercase treatment and extended font give the navigation a technical, almost architectural feel — more like a design studio's site than a sock retailer.

### Cards
**`product-card`** — A minimal white card with `{rounded.sm}` (8px) corners, no shadow, and no border. The product image occupies a 1:1 aspect ratio with the same corner radius. Below the image, the title uses `{typography.title-sm}` (16px/500) and the price uses `{typography.body-sm}` (14px/400) in `{colors.body}` (#474747). Sale prices switch to `{colors.accent-red}` (#c80003). The card relies entirely on the product photography for visual interest — no overlays, no gradients, no decorative elements.

**`badge-sale`**, **`badge-new`**, **`badge-exclusive`** — Hard-cornered badges (`{rounded.none}`) positioned at the top-left of product images. The sale badge uses `{colors.accent-red}` (#c80003) with white text; the new badge uses `{colors.primary}` (#7fddff) with near-black text; the exclusive badge uses `{colors.accent-olive}` (#5a6616) with white text. All use `{typography.badge}` — 11px/700 uppercase with 0.5px letter-spacing.

### Forms
**`text-input`** — A 48px tall input with `{rounded.none}`, a 1px `{colors.hairline}` border, and `{typography.body-md}` (16px/400). On focus, the border thickens to 2px and switches to `{colors.primary}` (#7fddff). Error states use a 2px `{colors.accent-red}` (#c80003) border. The lack of rounding and the uppercase placeholder text (in `{colors.muted}`) maintain the industrial feel.

**`select-input`** — Matches the text-input structure but includes a custom dropdown arrow in `{colors.ink}`. Used for size selection, sorting, and filter dropdowns.

### Footer
**`footer`** — A dark section using `{colors.dark-canvas}` (#232933) as background, with white text for headings and `{colors.muted}` (#a4a4a4) for body links. Links hover to `{colors.canvas}` (#ffffff). The footer is divided into columns with `{spacing.xxl}` (48px) between them. A monospaced `{typography.caption}` (12px uppercase) is used for section headings like "Support" and "Company." The bottom bar includes legal text in `{colors.dark-muted}` (#6c717a) and social icons.

### Hero
**`hero-section`** — A full-width white section with `{spacing.section}` (64px) top and bottom padding. The headline uses `{typography.display-xl}` (48px/700) in `{colors.ink}`. The primary CTA (`{typography.button-lg}` at 16px/600 uppercase) is a 56px tall `{colors.primary}` button with `{rounded.none}`. The hero typically features a single large product image or lifestyle shot bleeding to the edge — no carousel, no overlays.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero text reduces to `{typography.display-md}` (28px); buttons become full-width; footer stacks vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; hero maintains `{typography.display-lg}` (36px); footer in 2-column layout |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3- or 4-column grid; hero at full `{typography.display-xl}` (48px); footer in 4-column layout |
| Wide | > 1440px | Content max-width at 1440px with auto margins; product cards may show 5-column; hero image scales up |

### Touch Targets
- All buttons and interactive elements maintain a minimum 44px height (48px for primary/secondary, 56px for hero CTA).
- Nav links have a minimum 44px tap area even when text is smaller.
- Size selector and quantity selector buttons are at least 40px × 40px.
- Search bar is 44px tall for easy tapping.

### Collapsing Strategy
- Primary navigation collapses to a hamburger menu below 744px, with a slide-out drawer from the left.
- Product filters collapse into a bottom sheet or modal on mobile.
- Footer columns collapse to a single column below 744px, with accordion-style expandable sections.
- Hero images may crop or stack vertically on mobile rather than maintaining a full-bleed horizontal layout.

## Known Gaps

- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- **Hover states**: Extracted only for button-primary (active color) and footer links (color change). Secondary button hover, ghost button hover, and card hover states (if any) were not reliably extracted from the live site.
- **Error styling**: Only the text-input error border color (#c80003) was inferred. Error message typography, iconography, and form-level error patterns were not observed.
- **Dark mode**: While `{colors.dark-canvas}` (#232933), `{colors.dark-surface}` (#121212), `{colors.dark-muted}` (#6c717a), and `{colors.dark-hairline}` (#595959) were extracted, the full dark-mode palette (including primary, accent, and link colors on dark backgrounds) is incomplete. The footer uses these colors, but a full dark-mode system toggle was not observed.
- **Typography scale**: Font sizes for display-xl through caption were estimated based on typical brand hierarchy and the extracted font families. Exact pixel values, line heights, and letter-spacing for every variant were not extractable from the live site's CSS. GT Pressura Mono was observed but its usage (captions, specs, size charts) is inferred.
- **Spacing scale**: The spacing tokens follow a standard 4px/8px/12px/16px/24px/32px/48px/64px scale common to Shopify-based brands. Exact section padding and component margins were not extracted.
- **Rounded corners**: The extracted palette and layout suggest minimal rounding (`{rounded.none}` for buttons, `{rounded.sm}` for cards). The pill-shaped buttons (`{rounded.full}`) are inferred from common promotional badge patterns.
- **Sub-brand palettes**: Stance may have seasonal or collaboration-specific color palettes (e.g., NBA, Marvel, or artist collections) that were not captured in the extracted hex list.
- **Animation and transitions**: No timing, easing, or motion tokens were extracted. The brand likely uses standard 200–300ms ease-in-out transitions for hover and focus states, but this is unconfirmed.
- **Checkout and cart**: The extracted colors may include Shopify Checkout widget colors (e.g., Klarna, Afterpay) that are not part of Stance's brand system. The cart-item component is inferred from common e-commerce patterns.
- **Social icon colors**: Some extracted hex values (e.g., #595959, #6c717a) may correspond to social media icon fills rather than brand UI colors. These have been assigned to `{colors.dark-hairline}` and `{colors.dark-muted}` as reasonable defaults.
