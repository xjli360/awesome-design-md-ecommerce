---
version: alpha
name: "Via Vision Entertainment"
source_url: "https://viavision.com.au"
captured_at: null
evidence_status: "historical_unverified"
quality_tier: "historical_archive"
usage_scope: "inspiration_only"
layout_status: "proposed_not_measured"
recreation_verified: false
description: |-
  A deep crimson anchor at #9b0000 gives Via Vision Entertainment its theatrical gravity — this is not a playful streaming pink but a blood-drop red that recalls cinema curtains, vintage film reels, and the spine of a collector's edition Blu-ray. The brand lives in a high-contrast world of near-black ink (#121212) and warm off-white canvas (#eeecec), with a secondary dark red (#8b0000) that adds depth to hover states and active navigation. The extracted palette reveals a surprising green presence (#006400, #15975a) and a burnt orange accent (#ee9441) — likely used sparingly for genre tags, badge highlights, or limited-edition callouts — suggesting a system that can flex across horror, drama, and cult-classic categories without losing its core identity. Typography runs on Bricolage Grotesque for display moments — a geometric grotesque with subtle personality — paired with Inter for body text and Satoshi for button labels, creating a layered hierarchy where headings feel editorial and body copy stays crisp. The Shopify platform backbone means checkout flows inherit standard widget colors, but the brand's own UI is deliberately restrained: pill-shaped buttons (`{rounded.full}`) for primary actions, softly rounded cards (`{rounded.md}` ~12px) for product tiles, and generous whitespace that lets cover art do the selling. There is no gradient, no glassmorphism, no decorative illustration — just typographic weight, a single red voltage, and the photography of film stills.

colors:
  primary: "#9b0000"
  primary-active: "#8b0000"
  primary-disabled: "#dedede"
  ink: "#121212"
  body: "#444444"
  muted: "#808080"
  muted-soft: "#dedede"
  hairline: "#dedede"
  hairline-soft: "#eeecec"
  canvas: "#eeecec"
  surface-soft: "#ffffff"
  surface-card: "#ffffff"
  on-primary: "#ffffff"
  accent-green: "#15975a"
  accent-orange: "#ee9441"
  accent-dark-green: "#006400"

typography:
  display-xl:
    fontFamily: "'Bricolage Grotesque', Inter, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.5px
  display-lg:
    fontFamily: "'Bricolage Grotesque', Inter, sans-serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: -0.3px
  display-md:
    fontFamily: "'Bricolage Grotesque', Inter, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.2px
  title-lg:
    fontFamily: "'Bricolage Grotesque', Inter, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0
  title-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: 0
  title-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0
  body-md:
    fontFamily: "'Inter', sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0
  body-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0
  caption:
    fontFamily: "'Inter', sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: 0
  caption-sm:
    fontFamily: "'Inter', sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0
  badge:
    fontFamily: "'Satoshi', Inter, sans-serif"
    fontSize: 11px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.3px
    textTransform: uppercase
  button-md:
    fontFamily: "'Satoshi', Inter, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.2px
  button-sm:
    fontFamily: "'Satoshi', Inter, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.15px
  link:
    fontFamily: "'Inter', sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0
  nav-link:
    fontFamily: "'Satoshi', Inter, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.3
    letterSpacing: 0.1px

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
    padding: 12px 28px
    height: 44px
  button-primary-active:
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
    padding: 12px 28px
    height: 44px
  button-secondary-active:
    backgroundColor: "{colors.hairline-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.full}"
  button-tertiary-text:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.button-md}"
  button-tertiary-text-hover:
    backgroundColor: transparent
    textColor: "{colors.primary-active}"
    typography: "{typography.button-md}"
  text-input:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 48px
  text-input-focus:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  text-input-error:
    borderColor: "{colors.primary}"
    borderWidth: 2px
  nav-bar:
    backgroundColor: "{colors.canvas}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    height: 64px
  nav-link-active:
    color: "{colors.primary}"
    borderBottom: "2px solid {colors.primary}"
  product-card:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sm}"
    rounded: "{rounded.md}"
  product-card-hover:
    boxShadow: "0 4px 12px rgba(0,0,0,0.08)"
  product-card-image:
    rounded: "{rounded.md} {rounded.md} 0 0"
  badge-new:
    backgroundColor: "{colors.accent-green}"
    textColor: "{colors.on-primary}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-sale:
    backgroundColor: "{colors.accent-orange}"
    textColor: "{colors.ink}"
    typography: "{typography.badge}"
    rounded: "{rounded.xs}"
    padding: "2px 8px"
  badge-genre:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption-sm}"
    rounded: "{rounded.full}"
    padding: "4px 12px"
  search-bar:
    backgroundColor: "{colors.surface-card}"
    textColor: "{colors.ink}"
    typography: "{typography.body-md}"
    rounded: "{rounded.full}"
    padding: "10px 20px"
    height: 44px
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.body-sm}"
    padding: "{spacing.section} 0"
  footer-link:
    color: "{colors.muted-soft}"
    typography: "{typography.link}"
  hero-section:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.canvas}"
    typography: "{typography.display-xl}"
    padding: "{spacing.section} {spacing.lg}"
  section-header:
    typography: "{typography.display-md}"
    color: "{colors.ink}"
    padding: "{spacing.lg} 0"
  filter-chip:
    backgroundColor: "{colors.surface-soft}"
    textColor: "{colors.body}"
    typography: "{typography.caption}"
    rounded: "{rounded.full}"
    padding: "6px 16px"
    height: 32px
  filter-chip-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.full}"

## Components

### Buttons
**`button-primary`** — The primary call-to-action across the site, rendered as a full pill shape in the brand's deep crimson (#9b0000). Used for "Add to Cart", "Pre-order", and "Subscribe" actions. On hover, shifts to the darker active state (#8b0000). The disabled state drops to a light gray background (#dedede) with muted text, signaling unavailability without confusion. Text is set in Satoshi at 15px with 600 weight for a confident, slightly condensed feel.

**`button-secondary`** — An outlined or ghost-style button on the warm off-white canvas (#eeecec), using the same pill shape and typography as the primary. Hover state fills with the soft hairline color (#eeecec) for subtle feedback. Used for "Learn More", "View Details", and secondary checkout actions where the crimson primary would overwhelm.

**`button-tertiary-text`** — A text-only button with no background or border, colored in the brand's primary red. Hover shifts to the darker active red. Used for "Cancel", "Clear Filters", and inline navigation links within product cards and modals.

### Cards
**`product-card`** — The core content container for movie and TV titles, built on a white surface (#ffffff) with soft 12px rounding. The card holds a cover image (rounded at the top corners only), title, year, format badge, and price. On hover, a subtle box shadow lifts the card — no scale animation, just a depth cue. The image area is the hero; text stays minimal and left-aligned.

**`badge-new`** — A small green pill (#15975a) with white uppercase text, used to flag newly added titles. The green stands out against the crimson system without competing — it signals "fresh stock" rather than "sale." Padding is tight (2px top/bottom, 8px left/right) so it sits neatly on cover art corners.

**`badge-sale`** — An orange badge (#ee9441) for discounted titles. Uses the same uppercase Satoshi 11px treatment as the new badge but with dark text (#121212) for contrast against the bright orange. Placed in the top-right of product cards.

**`badge-genre`** — A soft, rounded pill for genre labels (e.g., "Horror", "Drama", "Cult Classic"). Uses the light surface color (#ffffff) with body-gray text (#444444) and full rounding. These sit in a horizontal strip below the hero or above product grids, allowing users to filter by category without committing to a crimson active state.

### Navigation
**`nav-bar`** — A fixed top navigation bar at 64px height on the warm off-white canvas. Logo sits left-aligned; nav links (Shop, Collections, About, Blog) are set in Satoshi 14px/600 with generous letter-spacing. The active page is underlined with a 2px crimson border. The bar stays opaque — no transparency or blur — maintaining the brand's direct, unpretentious feel.

**`nav-link-active`** — The active navigation state uses the brand's primary red for text color and a 2px solid bottom border in the same red. This creates a clear, physical indicator of the current section without relying on background fills or heavy shapes.

### Forms
**`text-input`** — Standard text input fields for search, newsletter signup, and checkout forms. White background, 48px height, 12px rounding, and 16px inner padding. On focus, the border switches to a 2px crimson stroke (#9b0000). Error states use the same crimson border with a red-tinted background — the brand doesn't introduce a separate error color, trusting the primary red to carry both positive and negative emphasis.

### Search
**`search-bar`** — A pill-shaped search input with full rounding, white background, and 44px height. Used in the nav bar and on the search results page. The placeholder text is set in Inter 16px/400. No search button — the input itself is the entry point, with a magnifying glass icon placed inside the left padding.

### Footer
**`footer`** — A dark footer section on the near-black background (#121212) with light text (#eeecec). Links are set in the muted-soft gray (#dedede) at 14px. The footer contains three columns: Customer Service, About Via Vision, and Connect. Social icons (if present) would inherit the footer's light color. Padding is generous at 64px top and bottom, giving the dark area breathing room.

## Responsive Behavior

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 744px | Nav collapses to hamburger; product cards go single-column; hero text reduces to 24px; search bar moves below nav; footer stacks vertically |
| Tablet | 744–1128px | Nav links remain visible but condensed; product cards in 2-column grid; hero maintains 28px display; search bar stays in nav |
| Desktop | 1128–1440px | Full nav with all links; product cards in 3-4 column grid; hero at 36px display; search bar in nav with expanded width |
| Wide | > 1440px | Max-width container at 1440px; product cards in 4-5 column grid; hero text at 36px with wider margins; nav remains centered |

### Touch Targets
- All buttons and interactive elements maintain minimum 44px height for touch accessibility.
- Filter chips and genre badges are at least 32px tall with 16px horizontal padding.
- Nav links have 48px touch area (padding + line-height).
- Product card images are tappable with no minimum size constraint — the card itself is the target.

### Collapsing Strategy
- On mobile, the full nav collapses into a hamburger menu with a slide-out drawer. The logo remains centered in the nav bar.
- The genre filter strip collapses from a horizontal scroll to a dropdown select on screens below 744px.
- Product grids collapse from multi-column to single-column on mobile, with full-width cards.
- The footer's three columns stack vertically on mobile, with each section separated by a hairline border.

## Known Gaps

- **Agent usage policy:** Historical tokens are unverified. Do not use them as current-site measurements or claim a faithful reconstruction.






- **Historical provenance:** The original capture time and raw evidence are unavailable. Token values have not been freshly verified; the [collection manifest](../../data/manifest.json) records this entry as historical_unverified.

- The extracted hex list includes several colors (#006400, #15975a, #ee9441) that appear to be accent or badge colors, but their exact usage context (hover states, active filters, limited-edition flags) could not be confirmed from the extraction alone. The green and orange are included as brand-specific tokens but may be used more sparingly than assumed.
- Font weights for Bricolage Grotesque, Inter, and Satoshi are inferred from common web usage — the exact weight for each text style (e.g., display-xl at 700 vs 600) is an educated guess based on the brand's editorial tone.
- Hover states for product cards (box shadow) and buttons (background color shift) are assumed from DTC e-commerce conventions — the actual animation timing, shadow depth, and color transitions were not extractable.
- Error styling for forms (border color, background tint) is inferred — the brand may use a separate error red or a different treatment entirely.
- Dark mode is not present on the live site (no `prefers-color-scheme` meta or CSS variables detected). The footer's dark background (#121212) is the only dark surface.
- The brand's Shopify checkout flow uses default widget colors (Shopify Pay green, Klarna pink, Afterpay blue) that are not part of the brand's design system and should not be replicated in brand UI.
- No animation or transition timing values were extractable — the system likely uses standard 200-300ms ease-in-out for hover and focus states, but this is unconfirmed.
- Sub-brand palettes (e.g., for genre-specific collections like "Horror" or "Cult") may exist but were not detected in the extraction.
