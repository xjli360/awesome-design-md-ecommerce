---
version: alpha
name: "Victus Sports"
source_url: "https://victussports.com"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A baseball bat maker that paints its identity in the black of a barrel face (#010101) and the crack-of-bat red (#db1e36) that runs through every primary action and badge. The palette is a dugout of high-contrast extremes — near-black ink (#231f20) against a warm off-white canvas (#f4f4f4), with a sky-blue accent (#80c3e4) that reads as a deliberate departure from the sport's traditional navy and gray. The brand trusts Oswald, a condensed sans-serif with a squared-off, athletic posture, for display typography — it sits at 700 weight in all-caps on hero sections, evoking jersey lettering and scoreboard LED text. Gotham serves as the supporting body face, bringing a more neutral, legible counterpoint to Oswald's intensity. The system uses tight letter-spacing on display text (1-2px), a move that compresses the type into blocks rather than letting it breathe — a visual echo of a bat's tapered handle. Buttons are pill-shaped (`{rounded.full}`) with red fills, but the brand also deploys a yellow accent (#ffb13b) for secondary calls-to-action and a deep blue (#216ba5) for trust signals like shipping guarantees. The overall mood is unapologetically masculine and competitive — the black canvas, the red voltage, the condensed type — but the sky-blue and yellow prevent it from tipping into aggression. Product cards use a clean white surface (`{rounded.md}` ~12px) with a thin hairline (#d3d3d3) that separates the photo from the description, and the footer collapses into a dense, single-column stack of links in muted gray (#aeaeae). The brand's signature move is the red-to-black gradient on hero overlays — a fade from `#db1e36` at the bottom to `#010101` at the top — that makes every product shot feel like it's emerging from a stadium tunnel.

colors:
  primary: "#db1e36"
  primary-active: "#b0182b"
  primary-disabled: "#f0a0a8"
  ink: "#010101"
  body: "#231f20"
  muted: "#888888"
  muted-soft: "#aeaeae"
  hairline: "#d3d3d3"
  hairline-soft: "#e5e5e5"
  canvas: "#f4f4f4"
  surface-soft: "#f0f0f0"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-sky: "#80c3e4"
  accent-yellow: "#ffb13b"
  accent-blue: "#216ba5"
  accent-gold: "#ffdb00"
  badge-red: "#da020f"
  badge-pink: "#c92fbe"
  star-rating: "#ffb13b"

typography:
  display-xl:
    fontFamily: "'Oswald', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: 2px
    textTransform: uppercase
  display-lg:
    fontFamily: "'Oswald', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 1.5px
    textTransform: uppercase
  display-md:
    fontFamily: "'Oswald', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 1px
    textTransform: uppercase
  title-lg:
    fontFamily: "'Oswald', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.5px
  title-md:
    fontFamily: "'Oswald', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.5px
  body-md:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0
  caption:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0.25px
  button-md:
    fontFamily: "'Oswald', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 1px
    textTransform: uppercase
  button-sm:
    fontFamily: "'Oswald', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 0.75px
    textTransform: uppercase
  link:
    fontFamily: "'Gotham', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0
  nav-link:
    fontFamily: "'Oswald', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: 1px
    textTransform: uppercase
  badge:
    fontFamily: "'Oswald', 'Helvetica Neue', Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.18
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
    padding: 12px 32px
    height: 48px
  button-primary-active:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 48px
  button-primary-disabled:
    backgroundColor: "{colors.primary-disabled}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 48px
  button-secondary:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 48px
    border: "2px solid {colors.ink}"
  button-accent-yellow:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 48px
  button-accent-blue:
    backgroundColor: "{colors.accent-blue}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-md}"
    rounded: "{rounded.full}"
    padding: 12px 32px
    height: 48px
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
  nav-bar:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.nav-link}"
  nav-link-inactive:
    backgroundColor: transparent
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-link}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
    padding: 0px
    border: "1px solid {colors.hairline}"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  product-card-title:
    typography: "{typography.title-md}"
    padding: "{spacing.base} {spacing.base} 0 {spacing.base}"
  product-card-price:
    typography: "{typography.body-md}"
    color: "{colors.primary}"
    padding: "{spacing.xs} {spacing.base} {spacing.base} {spacing.base}"
  badge:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-new:
    backgroundColor: "{colors.accent-yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.badge-red}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
    gradient: "linear-gradient(180deg, {colors.ink} 0%, {colors.primary} 100%)"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.body}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "12px 24px"
    height: 48px
    border: "1px solid {colors.hairline}"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.muted-soft}"
    typography: "{typography.body-sm}"
    padding: "{spacing.xxl} {spacing.lg}"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  footer-heading:
    color: "{colors.on-primary}"
    typography: "{typography.title-md}"
  star-rating:
    color: "{colors.star-rating}"
    size: 16px

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, used for "Shop Now", "Add to Cart", and "View Details". Rendered as a pill-shaped button with a red fill (`{colors.primary}`) and white text in Oswald uppercase. On hover, the background shifts to a darker red (`{colors.primary-active}`). The disabled state uses a lighter, desaturated red (`{colors.primary-disabled}`) to signal inactivity.

**`button-secondary`** — An outlined alternative for less prominent actions like "Learn More" or "Compare Models". Uses a transparent background with a 2px black border (`{colors.ink}`) and black text. On hover, the background fills with black and text inverts to white.

**`button-accent-yellow`** — Used for promotional or urgency-driven CTAs such as "Limited Edition" or "Free Shipping". The yellow fill (`{colors.accent-yellow}`) against black text creates a high-contrast, attention-grabbing button that stands apart from the primary red system.

**`button-accent-blue`** — Reserved for trust-signal actions like "Check Warranty" or "Register Product". The deep blue fill (`{colors.accent-blue}`) with white text provides a calm, reliable alternative to the aggressive red and yellow.

### Navigation
**`nav-bar`** — A fixed-position top bar with a black background (`{colors.ink}`) and white text in Oswald uppercase. The nav links use tight letter-spacing (1px) and sit at 14px. The active link is highlighted in red (`{colors.primary}`). The bar collapses to a hamburger menu on mobile, with the logo centered.

**`nav-link-active`** — The currently selected navigation item. Uses red text (`{colors.primary}`) on the black nav bar to indicate the user's location.

**`nav-link-inactive`** — Default navigation items. White text (`{colors.on-primary}`) on the black nav bar. On hover, the text shifts to a lighter gray to provide feedback.

### Cards
**`product-card`** — A white card with a 1px hairline border (`{colors.hairline}`) and 12px rounded corners (`{rounded.md}`). The card contains a full-width product image with rounded top corners, followed by the product title in Oswald and the price in red (`{colors.primary}`). The card elevates on hover with a subtle box-shadow.

**`product-card-image`** — The image area of the product card. Uses `{rounded.md}` on the top corners only, creating a seamless transition from the image to the text content below.

**`product-card-title`** — The product name rendered in Oswald at 18px with 0.5px letter-spacing. Sits below the image with 16px padding on the sides and top.

**`product-card-price`** — The price displayed in red (`{colors.primary}`) using Gotham body weight. Positioned below the title with 4px top padding and 16px bottom padding.

### Badges
**`badge`** — A small red (`{colors.primary}`) pill with white text used for status indicators like "Best Seller" or "Pro Series". Uses Oswald uppercase at 11px with tight padding.

**`badge-new`** — A yellow (`{colors.accent-yellow}`) badge with black text for marking new arrivals. The high-contrast yellow signals freshness and urgency.

**`badge-sale`** — A bright red (`{colors.badge-red}`) badge for sale or clearance items. Slightly more saturated than the primary red to draw immediate attention.

### Forms
**`text-input`** — A standard text input field with a white background, 1px hairline border (`{colors.hairline}`), and 8px rounded corners (`{rounded.sm}`). On focus, the border thickens to 2px and turns red (`{colors.primary}`). Used for search, newsletter signup, and contact forms.

**`text-input-focus`** — The focused state of the text input. The border changes to 2px solid red (`{colors.primary}`), providing a clear visual cue for the active field.

### Hero
**`hero-section`** — The full-width hero banner that appears on the homepage and collection pages. Uses a gradient background that fades from black (`{colors.ink}`) at the top to red (`{colors.primary}`) at the bottom, creating a dramatic tunnel-vision effect. Text is rendered in Oswald uppercase at 48px with 2px letter-spacing. The section has 64px vertical padding.

### Search
**`search-bar`** — A pill-shaped search input with a white background and 1px hairline border (`{colors.hairline}`). Used on the search results page and in the mobile nav. On focus, the border turns red (`{colors.primary}`).

### Footer
**`footer`** — A dense, black-background (`{colors.ink}`) footer with muted gray text (`{colors.muted-soft}`). Links are in Gotham at 14px, while section headings use Oswald at 18px in white. The footer stacks into a single column on mobile with 48px vertical padding between sections.

**`footer-link`** — Footer navigation links in muted gray (`{colors.muted-soft}`) with Gotham at 14px. On hover, the text brightens to white.

**`footer-heading`** — Footer section titles in Oswald at 18px with white text (`{colors.on-primary}`). Uses 0.5px letter-spacing and sits above the link list.

### Star Rating
**`star-rating`** — A 16px star icon rendered in yellow (`{colors.star-rating}`). Used on product cards and review sections. The star fill is solid for rated stars and empty for unrated.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav bar collapses to hamburger; product cards stack in single column; hero text reduces to 32px; footer stacks vertically; search bar moves to full-width below nav |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards display in 2-column grid; hero text at 40px; footer splits into 2-column layout |
| Desktop | 1128–1440px | Full nav bar with all links; product cards in 3-column grid; hero text at 48px; footer in 4-column layout |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-column grid; hero text at 56px; additional whitespace on sides |

### Touch Targets
- All buttons and links maintain a minimum 44px height for touch accessibility
- Nav bar hamburger icon is 48px x 48px
- Search bar input height is 48px
- Product card tap targets (title, price, image) are each at least 44px tall

### Collapsing Strategy
- Nav bar: links collapse into hamburger menu at < 744px; logo remains centered
- Product grid: 4-column → 3-column → 2-column → 1-column as viewport shrinks
- Footer: 4-column → 2-column → 1-column; section headings become tap-to-expand accordions on mobile
- Hero: full-width gradient remains, but text size reduces and padding compresses

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- Hover and focus states for all components could not be reliably extracted from the live site; the active states provided are best guesses based on common patterns
- Error styling for form inputs (validation errors, required field indicators) was not observed
- Dark mode is not present on the current site; no dark mode tokens are defined
- Sub-brand palettes (e.g., Victus Pro, Victus Youth) were not distinguishable from the extracted colors
- The extracted color list includes several near-duplicate grays (#f4f4f4, #f0f0f0, #f3f3f3, #f7f7f7) — the most frequent (#f4f4f4) was chosen as canvas, but the brand may use multiple surface tones
- The pink (#c92fbe) and gold (#ffdb00) in the extracted list may be social-icon colors or checkout-widget accents rather than brand colors; they are included as `badge-pink` and `accent-gold` but may not be actively used in the design system
- Font weights for Oswald and Gotham beyond 400, 500, 600, and 700 were not confirmed; the system assumes standard weight availability
- The exact gradient stops for the hero section were not extracted; the provided gradient is an approximation based on the top and bottom colors
- Animation durations and easing curves were not observed
- Spacing values for specific components (e.g., card padding, button padding) were inferred from common patterns rather than extracted from the live site
